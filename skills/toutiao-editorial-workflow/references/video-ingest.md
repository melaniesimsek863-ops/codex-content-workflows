# Quark Video Lesson Ingest

## Source Priority

1. Transcript: primary fact base and fullest course content.
2. AI summary: navigation and topic hierarchy.
3. AI courseware: visual evidence and page-level orientation.

## Procedure

1. Export the three assets from the Quark desktop player into one immutable raw folder.
2. Inventory file name, format, size, modified time, and SHA-256.
3. Confirm that the transcript is readable and note whether it has timestamps.
4. Extract the AI summary structure without replacing the transcript.
5. Convert legacy PPT to PPTX/PDF when necessary; inspect every rendered page.
6. Separate course claims, agent analysis, current platform facts, and implementation recommendations.
7. Upload the raw and processed folders, retain FIDs, and perform hash readback.

Do not claim to have learned a video merely because the Skill summarized its folder. Require the exported transcript or another complete, readable content source.

## Batch Intake

Put all lesson exports into one inbox without renaming them. File names must start with the lesson number and contain exactly one recognizable type marker: `AI总结`, `文稿`, or `课件`.

Run:

```text
python scripts/ingest_quark_exports.py <inbox> --output-root <course-root> --lessons 2-10
```

The script copies source files, never moves them. It creates four directories per lesson, writes per-lesson `intake-status.json`, and writes a batch-level `batch-status.json`. A complete lesson has exactly one or more recognized files for all three required types and no duplicate type requiring review.

Interpret status as follows:

- `complete`: all three output types are present.
- `incomplete`: one or more required types are missing.
- `needs_review`: more than one source matched the same type; inspect before processing.

Do not start content analysis for an incomplete or review-required lesson.
