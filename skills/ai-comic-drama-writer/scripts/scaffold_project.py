#!/usr/bin/env python3
"""Scaffold an AI comic drama project folder from bundled templates."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

TEMPLATES = {
    "project-bible.md": "project-bible.md",
    "character-card.md": "characters/character-card.md",
    "season-outline.md": "season-outline.md",
    "episode-script.md": "episodes/episode-001.md",
    "storyboard-table.md": "storyboards/episode-001-storyboard.md",
    "visual-prompt-sheet.md": "visual-prompts/episode-001-prompts.md",
    "short-video-script.md": "short-videos/short-video-001.md",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "ai-comic-drama-project"


def scaffold(title: str, output_dir: Path, force: bool = False) -> Path:
    skill_root = Path(__file__).resolve().parents[1]
    template_dir = skill_root / "assets" / "templates"
    project_dir = output_dir / slugify(title)

    if project_dir.exists() and any(project_dir.iterdir()) and not force:
        raise SystemExit(f"Project folder already exists and is not empty: {project_dir}")

    project_dir.mkdir(parents=True, exist_ok=True)
    for src_name, dest_name in TEMPLATES.items():
        src = template_dir / src_name
        dest = project_dir / dest_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)

    index = project_dir / "README.md"
    index.write_text(
        f"# {title}\n\n"
        "## Files\n\n"
        "- `project-bible.md` - core positioning, story engine, world rules, ledgers\n"
        "- `characters/` - character cards\n"
        "- `season-outline.md` - season and episode plan\n"
        "- `episodes/` - episode scripts\n"
        "- `storyboards/` - AI comic storyboard tables\n"
        "- `visual-prompts/` - image/video prompt sheets\n"
        "- `short-videos/` - vertical short-video scripts\n",
        encoding="utf-8",
    )
    return project_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an AI comic drama project folder.")
    parser.add_argument("title", help="Project title")
    parser.add_argument("--output", default=".", help="Parent output directory")
    parser.add_argument("--force", action="store_true", help="Allow writing into an existing folder")
    args = parser.parse_args()

    project_dir = scaffold(args.title, Path(args.output).resolve(), args.force)
    print(project_dir)


if __name__ == "__main__":
    main()