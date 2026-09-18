# Local Cangjie Catalog

Root path: the user's configured `<CANGJIE_LIBRARY>` directory. This catalog
describes a separately obtained library; it does not redistribute that library.

## Categories

- `00_元技能蒸馏引擎(meta-skill)` - book2skill / RIA-TV++ production workflow
- `01_哲学思维类(philosophy)` - 周易, 毛泽东选集, 穷查理宝典, 第一性原理, 黄帝内经
- `02_商业投资类(business-investment)` - 不拘一格_网飞, 巴菲特致股东信, 段永平投资问答录, 认知红利
- `03_文案营销类(copywriting-marketing)` - 1000个铁粉, 影响力, 文案创作完全手册, 爆款文案, 疯传
- `04_战略兵法类(strategy)` - 孙子兵法
- `05_技术工具类(tech-tools)` - 165个系统提示词, 高等数学上册第一章
- `06_文学历史类(literature-history)` - 我与地坛, 明朝那些事儿

## Standard Book Pack Shape

Most book packs contain:

- `README（说明）.md` - user-facing overview
- `INDEX（技能地图）.md` or `INDEX.md` - skill map and recommended order
- `BOOK_OVERVIEW（全书概览）.md` or `BOOK_OVERVIEW.md` - Adler-style book overview
- `candidates（待选候选）/` - extracted candidates
- `verified（验证记录）.md` - triple-verification record
- `rejected（淘汰项）/` - rejected candidates and reasons
- one folder per skill, usually with `SKILL.md` and `test-prompts.json`

## Known Structure Difference

`03_文案营销类(copywriting-marketing)\1000个铁粉(1000-true-fans-skill)` stores skill modules under `skills(技能列表)\v*.md` and tests as `test-prompts-v*.json`, rather than one folder per skill.

## Search Hints

- Use `rg --files` to find candidate paths.
- Search Chinese and English terms. Many folders include both, such as `injection-defense(注入防御)`.
- For trigger selection, prioritize fields/sections named `description`, `A2`, `触发场景`, `语言信号`, `边界`, and `不要在以下情况使用`.
- For source audit, read `verified（验证记录）.md`, `BOOK_OVERVIEW`, and the selected skill's `R` section.

## High-Value Entry Points

- Book distillation workflow: `00_元技能蒸馏引擎(meta-skill)\00_元技能_仓颉蒸馏规范(cangjie-skill)\SKILL.md`
- Prompt engineering/security: `05_技术工具类(tech-tools)\165个系统提示词(system-prompt-skills)\INDEX（技能地图）.md`
- Math learning: `05_技术工具类(tech-tools)\高等数学上册第一章(high-math-vol1-ch1-skill)\INDEX（技能地图）.md`
- Decision making: `01_哲学思维类(philosophy)\穷查理宝典(poor-charlies-almanack-skill)\INDEX（技能地图）.md`
- Strategy: `04_战略兵法类(strategy)\孙子兵法(sunzi-bingfa-skill)\INDEX（技能地图）.md`
- Organization/complex problems: `01_哲学思维类(philosophy)\毛泽东选集(mao-selected-works-skill)\INDEX（技能地图）.md`
- Personal brand/copywriting: `03_文案营销类(copywriting-marketing)`
