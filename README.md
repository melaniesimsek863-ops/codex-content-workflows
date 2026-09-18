# Codex Content Workflows

Three locally customized workflow skills for story development and evidence-led
editorial work, prepared for an initial public release. They are instructions,
templates and small Python utilities, not autonomous content businesses.

| Skill | Purpose | External requirements |
| --- | --- | --- |
| `ai-comic-drama-writer` | Story structure, continuity, scripts and storyboard templates | An AI assistant; optional Cangjie library |
| `toutiao-editorial-workflow` | Evidence packs, publication gates and export validation | Python for utilities; optional Quark integration |
| `cangjie-book-skills` | Locate methods in a separately supplied local library | A lawfully obtained Cangjie library configured by its owner |

## Use

Inspect the selected skill's `SKILL.md`, then install that skill directory into
your assistant's configured skills location. Keep references, scripts, assets
and agents together. Set optional library locations to your own paths. The
Cangjie library, books, courses, personal articles and cloud credentials are
not included.

Example requests: develop a story bible from an original premise; validate an
article's evidence pack; check a publication package for missing human review.
Publishing requires a human decision. Recheck platform policies against current
official sources before publishing.

## Utilities

```text
python skills/ai-comic-drama-writer/scripts/scaffold_project.py --help
python skills/toutiao-editorial-workflow/scripts/validate_project.py --help
python skills/toutiao-editorial-workflow/scripts/build_inventory.py --help
python skills/toutiao-editorial-workflow/scripts/ingest_quark_exports.py --help
```

See [VALIDATION.md](VALIDATION.md) for verification and limitations. Model output
quality, rights and factual accuracy need human review. No traffic, revenue or
originality certification is promised.

## Attribution

The human-voice reference acknowledges Humanizer-zh by op7418 / 歸藏. Its MIT
notice is retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
The Cangjie router refers to a separate book-derived library; this repository
does not claim authorship of that library or redistribute its contents.
Quark Drive, Nuwa and Shuorenhua are optional third-party skills, not included
here and not claimed as this maintainer's original work.
