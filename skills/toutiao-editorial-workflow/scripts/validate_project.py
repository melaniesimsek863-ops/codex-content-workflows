#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path


REQUIRED_BY_STAGE = {
    "position": ["account_profile.json"],
    "topic": ["account_profile.json", "topic-card.json"],
    "draft": ["account_profile.json", "topic-card.json", "evidence-pack.json", "article-brief.md"],
    "publish": ["account_profile.json", "topic-card.json", "evidence-pack.json", "article-brief.md", "publish-checklist.json"],
    "review": ["account_profile.json", "topic-card.json", "evidence-pack.json", "article-brief.md", "publish-checklist.json", "metrics-snapshot.csv"],
}

JSON_FIELDS = {
    "account_profile.json": ["account_name", "positioning", "audience", "content_pillars", "boundaries"],
    "topic-card.json": ["topic_id", "reader_problem", "angle", "status"],
}

PUBLISH_GATES = [
    "facts_verified",
    "title_compliant",
    "rights_checked",
    "ai_label_reviewed",
    "originality_reviewed",
    "human_approved",
]


def load_json(path, errors):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.name}: invalid JSON: {exc}")
        return None


def require_fields(name, data, fields, errors):
    if not isinstance(data, dict):
        errors.append(f"{name}: root must be an object")
        return
    for field in fields:
        value = data.get(field)
        if value is None or value == "" or value == []:
            errors.append(f"{name}: missing or empty field '{field}'")


def validate(project, stage):
    errors = []
    required = REQUIRED_BY_STAGE[stage]
    for name in required:
        if not (project / name).is_file():
            errors.append(f"missing file: {name}")

    for name, fields in JSON_FIELDS.items():
        path = project / name
        if path.is_file():
            data = load_json(path, errors)
            if data is not None:
                require_fields(name, data, fields, errors)

    evidence_path = project / "evidence-pack.json"
    if evidence_path.is_file():
        evidence = load_json(evidence_path, errors)
        if isinstance(evidence, dict):
            sources = evidence.get("sources")
            if not isinstance(sources, list) or not sources:
                errors.append("evidence-pack.json: sources must be a non-empty array")
            else:
                for index, source in enumerate(sources):
                    if not isinstance(source, dict):
                        errors.append(f"evidence-pack.json: source {index} must be an object")
                        continue
                    require_fields(
                        f"evidence-pack.json source {index}",
                        source,
                        ["claim", "url", "publisher", "published_at", "verified"],
                        errors,
                    )
                    if not str(source.get("url", "")).startswith(("http://", "https://")):
                        errors.append(f"evidence-pack.json: source {index} URL must be HTTP(S)")
                    if source.get("verified") is not True:
                        errors.append(f"evidence-pack.json: source {index} is not verified")

    brief_path = project / "article-brief.md"
    if brief_path.is_file():
        brief = brief_path.read_text(encoding="utf-8-sig")
        for heading in ("# Article Brief", "## Thesis", "## Outline"):
            if heading not in brief:
                errors.append(f"article-brief.md: missing heading '{heading}'")

    checklist_path = project / "publish-checklist.json"
    if checklist_path.is_file():
        checklist = load_json(checklist_path, errors)
        if checklist is not None:
            require_fields("publish-checklist.json", checklist, PUBLISH_GATES, errors)
            for gate in PUBLISH_GATES:
                if checklist.get(gate) is not True:
                    errors.append(f"publish-checklist.json: gate '{gate}' must be true")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate a Toutiao editorial project stage.")
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--stage", choices=REQUIRED_BY_STAGE, default="draft")
    args = parser.parse_args()

    project = args.project_dir.resolve()
    if not project.is_dir():
        print(json.dumps({"ok": False, "errors": ["project directory not found"]}, ensure_ascii=False))
        return 1

    errors = validate(project, args.stage)
    print(json.dumps({"ok": not errors, "stage": args.stage, "project": str(project), "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
