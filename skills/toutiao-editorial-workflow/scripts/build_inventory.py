#!/usr/bin/env python3
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main():
    parser = argparse.ArgumentParser(description="Build a deterministic SHA-256 project inventory.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project = args.project_dir.resolve()
    output = (args.output or (project / "inventory.json")).resolve()
    files = []
    for path in sorted(project.rglob("*")):
        if not path.is_file() or path == output or ".git" in path.parts:
            continue
        stat = path.stat()
        files.append({
            "path": path.relative_to(project).as_posix(),
            "size": stat.st_size,
            "modified_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "sha256": sha256(path),
        })

    payload = {
        "schema_version": 1,
        "project": str(project),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "file_count": len(files),
        "total_bytes": sum(item["size"] for item in files),
        "files": files,
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "output": str(output), "file_count": len(files), "total_bytes": payload["total_bytes"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
