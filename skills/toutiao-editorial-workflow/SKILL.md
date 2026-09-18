---
name: toutiao-editorial-workflow
description: Use when planning, researching, drafting, reviewing, publishing, archiving, or analyzing 今日头条 or 头条号 articles, including 选题, 证据包, 标题, 原创, AI标识, 数据复盘, 夸克网盘课程资料, and self-media workflow requests.
---

# Toutiao Editorial Workflow

## Core Principle

Build evidence before prose. Let AI prepare options, but keep factual judgment, originality, rights, final voice, and publishing responsibility with the human author.

## Route The Task

1. For lesson ingestion or batch Quark exports, read `references/video-ingest.md`.
2. For a new article, read `references/workflow.md` and `references/schemas.md`.
3. For author, competitor, or successful-account style research, read `references/style-modeling.md`; use `huashu-nuwa` for deep extraction only after enough representative material is available.
4. For openings, reader review, final language polish, and final-body integrity, read `references/article-quality-pass.md`; use `shuorenhua` only after facts and protected spans are marked.
5. Before publishing, read `references/quality-gates.md` and refresh `references/toutiao-policy-baseline.md` against current official rules.
6. For Cangjie methods, read `references/cangjie-routing-map.md` and load only the selected source skill.
7. For cloud storage, read `references/quark-archive-layout.md` and use `quarkclouddrive`.

## Stage Contract

| Stage | Required output | Stop condition |
|---|---|---|
| Position | `account_profile.json` | Audience or boundary is unclear |
| Topic | `topic-card.json` | No distinct angle or reader problem |
| Evidence | `evidence-pack.json` | Material claims lack reliable sources |
| Style | `style-profile.json` when style research is used | Single-source imitation or unclear transfer boundary |
| Draft | `article-brief.md` plus draft | Claims exceed the evidence pack |
| Publish | `publish-checklist.json` | Any gate is false or human approval is absent |
| Review | `metrics-snapshot.csv` | Observation window is incomplete |

Run `scripts/validate_project.py <project-dir> --stage <stage>` before advancing. Use `scripts/build_inventory.py` before cloud upload and after readback.

For multiple Quark lessons, place all exports in one inbox and run `scripts/ingest_quark_exports.py <inbox> --output-root <course-root> --lessons 2-10`. Exit code `2` means missing, ambiguous, or duplicate exports require attention; it is not a completed batch.

## Non-Negotiable Boundaries

- Do not invent facts, quotations, experience, sources, data, or authority.
- Do not turn competitor research into copying, low-effort rewriting, or stitched summaries.
- Do not claim platform originality eligibility from writing quality alone.
- Do not automatically publish. Prepare the final package and require explicit human approval.
- Do not treat a successful upload as verified storage; read back representative files and compare SHA-256.
- Treat current platform rules as time-sensitive and verify official sources before a real release.

## Output Order

Return the decision or status first, then the evidence, gaps, next action, and file locations. Keep source-derived facts, course claims, and engineering recommendations visibly separate.
