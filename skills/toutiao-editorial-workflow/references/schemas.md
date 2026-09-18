# Project Schemas

## Required Files By Stage

```text
project/
  account_profile.json
  topic-card.json
  evidence-pack.json
  style-profile.json          # when style research is used
  article-brief.md
  opening-options.md
  reader-review.md
  fact-check-report.json
  publish-checklist.json
  metrics-snapshot.csv
```

## account_profile.json

Required fields: `account_name`, `positioning`, `audience`, `content_pillars`, `boundaries`.

## topic-card.json

Required fields: `topic_id`, `reader_problem`, `angle`, `status`. Recommended: `timeliness`, `risk`, `content_pillar`, `owner`.

## evidence-pack.json

Use `sources` as an array. Each source requires `claim`, `url`, `publisher`, `published_at`, and boolean `verified`. Add `accessed_at`, `source_type`, `quote_limit`, and `notes` when relevant.

## article-brief.md

Require `# Article Brief`, `## Thesis`, and `## Outline`. Add reader benefit, exclusions, evidence map, and desired action when useful.

## style-profile.json

Recommended fields: `profile_name`, `account_voice`, `source_samples`, `transferable_mechanisms`, `source_specific_elements_to_avoid`, `fusion_rules`, `similarity_review`, and `updated_at`. Each `source_samples` item should record author or account, work title or URL, observed performance evidence, and whether each conclusion is observed or inferred.

## opening-options.md And reader-review.md

Keep three materially different opening candidates, the selection reason, and rejected risks. Reader review records the target reader, likely stop points, trust breaks, missing context, objections, and the resulting revisions. Do not fabricate reader quotations or claim that a simulated review is real user research.

## fact-check-report.json

Recommended fields: `status`, `body_file`, `body_sha256`, `checked_at`, `claims`, and `unresolved`. `status` may be `passed`, `blocked`, or `needs_review`; only `passed` with a matching current file hash may advance to publication.

## publish-checklist.json

All required booleans must be true: `facts_verified`, `title_compliant`, `rights_checked`, `ai_label_reviewed`, `originality_reviewed`, `human_approved`.

## metrics-snapshot.csv

Recommended columns: `captured_at`, `hours_since_publish`, `impressions`, `reads`, `completion_rate`, `comments`, `likes`, `shares`, `follows`, `negative_feedback`, `review_status`, `experiment_variable`.
