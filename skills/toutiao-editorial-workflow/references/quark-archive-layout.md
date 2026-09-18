# Quark Archive Layout

## Cloud Layout

```text
AI知识库/自媒体项目/今日头条/
  00_账号与规则/
  01_选题池/
  02_证据包/
  03_写作中/
  04_待发布/
  05_已发布/
  06_数据回读/
  07_复盘与方法库/
```

Use `YYYYMMDD_topic-id_short-title` for each article project. Store source evidence, drafts, final copy, rights notes, publish screenshots, metrics, and inventory together.

## Storage Contract

1. Keep raw exports immutable.
2. Build a SHA-256 inventory before upload.
3. Upload to an explicitly confirmed parent FID.
4. Retain returned file FIDs.
5. Read back representative text and binary files.
6. Compare readback hashes with local hashes.
7. Treat returned path strings as unverified when they conflict with expected hierarchy; verify by FID and client inspection.

The official Skill handles cloud file operations and file-level AI summary/QA. It does not currently expose the desktop player's video transcript, AI summary, or AI courseware export controls.
