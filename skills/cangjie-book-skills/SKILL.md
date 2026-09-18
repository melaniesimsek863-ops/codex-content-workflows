---
name: cangjie-book-skills
description: Use the local Cangjie book-derived skill pack when the user asks to apply, inspect, install, compare, or create book/prompt-derived Agent skills; when they mention Cangjie/仓颉 skill, book2skill, RIA-TV++, 拆书, 蒸馏一本书, or any included book such as 穷查理宝典, 毛泽东选集, 孙子兵法, 巴菲特致股东信, 影响力, 爆款文案, 高等数学第一章, 我与地坛, 明朝那些事儿, 165个系统提示词. Also use when choosing a relevant book methodology for a real decision, writing, strategy, business, marketing, math-learning, or prompt-engineering problem.
---

# Cangjie Book Skills

## Purpose

Use the user's separately obtained local Cangjie skill pack as a searchable library of book-derived Agent skills. Ask for its directory when it has not been configured; below, `<CANGJIE_LIBRARY>` means that directory. The library is not included. Do not load the whole pack. Locate the relevant book or module, read only the needed `INDEX`, `README`, `BOOK_OVERVIEW`, `SKILL.md`, or `test-prompts*.json`, then apply that module's execution steps.

## Quick Routing

1. If the user names a book, author, category, or skill slug, go directly to that book directory and read its `INDEX` first.
2. If the user describes a real-world problem without naming a book, search the pack for trigger language and candidate skill names:
   - `rg -n --glob "SKILL.md" --glob "*.md" "<keywords>" "<CANGJIE_LIBRARY>"`
   - Prefer hits in `description`, `A2`, `语言信号`, `E`, and `B`.
3. If multiple skills match, read each candidate's `description`, `A2`, and `B`; choose the narrowest skill whose trigger and boundary fit.
4. Before applying a module, read its full skill file. Follow its `E` execution steps and respect its `B` boundaries.
5. When explaining the result to the user, name the Cangjie source skill and book, and distinguish source-derived guidance from your own inference.

## Library Map

Read `references/catalog.md` for the local category/book map and known structure differences.

## Applying a Cangjie Skill

When a skill is selected:

1. State the selected skill briefly if it helps the user understand the method.
2. Translate the user's problem into the skill's trigger frame.
3. Execute the skill's steps, not just summarize the book idea.
4. Use adjacent skills only when the selected skill's `related_skills`, `INDEX`, or the user's problem clearly calls for a combination.
5. Avoid political, medical, investment, legal, or safety overreach. Treat source books as thinking frameworks, not authority for current facts or regulated advice.

## Installing Or Adapting

For Codex installation tasks, prefer a router skill over bulk-copying every Cangjie `SKILL.md`. Bulk installation can flood Codex with hundreds of trigger descriptions and some packs use nonstandard file names. If the user explicitly wants direct installation of selected modules, normalize each selected module into a proper Codex skill folder:

- folder name: lowercase letters, digits, and hyphens only
- required file: `SKILL.md`
- frontmatter: only `name` and `description`
- optional UI metadata: `agents/openai.yaml`
- keep original source files as references when needed

Validate any created skill with:

`python <your-skill-creator-directory>/scripts/quick_validate.py <skill-folder>`
