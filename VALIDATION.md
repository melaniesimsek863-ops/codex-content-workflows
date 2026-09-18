# Validation

Checked on 2026-09-18:

- All three SKILL.md files pass the local skill-creator metadata validator.
- All four Python utilities respond successfully to `--help`.
- The story scaffold creates the expected eight Markdown files.
- All bundled JSON templates parse successfully.

The validator is run in UTF-8 mode on Windows. This checks packaging and basic
utility behavior, not writing quality, end-to-end editorial stage validation,
cloud uploads or publishing. No external account operation is exercised.
