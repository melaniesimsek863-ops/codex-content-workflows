# Quality Gates

## Fact Gate

- Every material claim maps to the evidence pack.
- Names, dates, numbers, quotations, and causal claims are checked.
- Inference is labeled as inference.

## Originality Gate

- The article contains the author's own material, analysis, experience, or synthesis.
- It is not a synonym rewrite, reordered copy, stitched compilation, or lightly modified repost.
- Reused public information does not dominate the work.
- Style research uses `多源融合` when practical and records which mechanisms were transferred.
- No distinctive phrase, signature metaphor, unique story, or identifying argument chain is concentrated from one source.
- A `相似性检查` reviews unusually long matching phrases and source-order reproduction; common terms and unavoidable factual overlap are not counted as copying by themselves.

## Title Gate

- The title accurately reflects the article and identifies the subject.
- It avoids unsupported scope, certainty, urgency, emotion, and outcome claims.
- It avoids click coercion and confusing fiction, games, or drama with real news.

## Rights And Privacy Gate

- Text, images, video, screenshots, logos, and quotations have a documented basis for use.
- Personal data, private identities, reputational allegations, and sensitive details receive explicit review.

## AI And Platform Gate

- Current official AI labeling requirements are reviewed.
- Originality declaration eligibility is reviewed separately from authorship quality.
- Repeated or near-duplicate publication across formats or accounts is checked.

## Human Voice Gate

Remove generic assistant framing, empty transitions, fabricated emotion, over-clean symmetry, and unsupported confidence. Preserve facts and make the author's concrete judgment visible.

- Reject throat-clearing, forced binary contrasts, repeated slogan-like triples, fake punchlines, and generic conclusions when they add no reader value.
- Treat facts, quotations, names, numbers, links, legal wording, and user-specified wording as `受保护文本` during language polishing.
- Final polish may improve rhythm and clarity but must not create experience, emotion, testimony, or certainty the author did not provide.

## Final Body Integrity Gate

- Run the final fact check after every substantive rewrite, including a human-voice pass.
- Record the final body path, fact-check status, and its `SHA-256` together.
- If the file changes after fact checking, the previous pass is stale and publishing is blocked until the check is repeated.

## Publish Gate

Publishing is blocked unless every `publish-checklist.json` field is true and the human author has explicitly approved the final title, body, media, labels, and settings.
