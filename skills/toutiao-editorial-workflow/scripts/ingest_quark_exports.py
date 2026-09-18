#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


TYPE_MARKERS = {
    "ai_summary": ("ai总结", "AI总结", "总结"),
    "transcript": ("文稿", "完整文稿", "字幕"),
    "courseware": ("课件", "ai课件", "AI课件"),
}
REQUIRED_TYPES = tuple(TYPE_MARKERS)
LESSON_PATTERN = re.compile(r"^\s*(\d{1,2})(?!\d)")


def parse_lessons(value):
    selected = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = (int(item) for item in part.split("-", 1))
            if start > end:
                raise argparse.ArgumentTypeError("lesson range start must not exceed end")
            selected.update(range(start, end + 1))
        else:
            selected.add(int(part))
    if not selected or any(item < 1 or item > 99 for item in selected):
        raise argparse.ArgumentTypeError("lessons must be between 1 and 99")
    return sorted(selected)


def classify(name):
    lowered = name.lower()
    matches = []
    for kind, markers in TYPE_MARKERS.items():
        if any(marker.lower() in lowered for marker in markers):
            matches.append(kind)
    return matches[0] if len(matches) == 1 else None


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def unique_destination(directory, source):
    candidate = directory / source.name
    if not candidate.exists():
        return candidate
    if candidate.stat().st_size == source.stat().st_size and sha256(candidate) == sha256(source):
        return candidate
    suffix = sha256(source)[:8]
    return directory / f"{source.stem}_{suffix}{source.suffix}"


def create_lesson_tree(output_root, lesson):
    root = output_root / f"{lesson:02d}_课程"
    paths = {
        "root": root,
        "raw": root / "01_原始导出",
        "processed": root / "02_加工成果",
        "publish": root / "03_发布资产",
        "records": root / "04_校验记录",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def main():
    parser = argparse.ArgumentParser(description="Copy and validate Quark video AI exports by lesson number.")
    parser.add_argument("inbox", type=Path)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--lessons", type=parse_lessons, default=parse_lessons("2-10"))
    args = parser.parse_args()

    inbox = args.inbox.resolve()
    output_root = args.output_root.resolve()
    if not inbox.is_dir():
        print(json.dumps({"ok": False, "error": "inbox not found", "inbox": str(inbox)}, ensure_ascii=False))
        return 1

    selected = set(args.lessons)
    candidates = {lesson: {kind: [] for kind in REQUIRED_TYPES} for lesson in selected}
    ignored = []
    ambiguous = []

    for source in sorted(inbox.iterdir()):
        if not source.is_file():
            continue
        match = LESSON_PATTERN.match(source.name)
        if not match or int(match.group(1)) not in selected:
            ignored.append(source.name)
            continue
        lesson = int(match.group(1))
        kind = classify(source.name)
        if kind is None:
            ambiguous.append(source.name)
            continue
        candidates[lesson][kind].append(source)

    lesson_results = []
    for lesson in sorted(selected):
        paths = create_lesson_tree(output_root, lesson)
        copied = []
        duplicates = []
        missing = []
        for kind in REQUIRED_TYPES:
            sources = candidates[lesson][kind]
            if not sources:
                missing.append(kind)
                continue
            if len(sources) > 1:
                duplicates.append({"type": kind, "files": [item.name for item in sources]})
            for source in sources:
                destination = unique_destination(paths["raw"], source)
                if not destination.exists():
                    shutil.copy2(source, destination)
                copied.append({
                    "type": kind,
                    "source": source.name,
                    "destination": destination.name,
                    "size": destination.stat().st_size,
                    "sha256": sha256(destination),
                })

        status = "complete"
        if duplicates:
            status = "needs_review"
        elif missing:
            status = "incomplete"
        lesson_result = {
            "lesson": f"{lesson:02d}",
            "status": status,
            "missing": missing,
            "duplicates": duplicates,
            "files": copied,
            "root": str(paths["root"]),
        }
        (paths["records"] / "intake-status.json").write_text(
            json.dumps(lesson_result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        lesson_results.append(lesson_result)

    payload = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "inbox": str(inbox),
        "output_root": str(output_root),
        "lessons": lesson_results,
        "ignored": ignored,
        "ambiguous": ambiguous,
    }
    output_root.mkdir(parents=True, exist_ok=True)
    status_path = output_root / "batch-status.json"
    status_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    complete = sum(item["status"] == "complete" for item in lesson_results)
    print(json.dumps({
        "ok": complete == len(lesson_results) and not ambiguous,
        "complete": complete,
        "total": len(lesson_results),
        "ambiguous": ambiguous,
        "status_file": str(status_path),
    }, ensure_ascii=False))
    return 0 if complete == len(lesson_results) and not ambiguous else 2


if __name__ == "__main__":
    sys.exit(main())
