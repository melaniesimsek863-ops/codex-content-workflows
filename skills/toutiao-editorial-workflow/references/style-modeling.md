# Style Modeling

## Purpose

Use successful authors, accounts, and high-performing works as research evidence without turning the final article into a disguised copy. The output is an account-owned editorial model, not a substitute identity.

## Inputs

- Prefer 5-10 relevant authors or accounts and 3-8 representative works from each when enough material exists.
- Include recent high-performing work, ordinary work, and at least one weak or atypical sample where possible.
- Record public performance evidence, source dates, account size, topic, and format. Mark causal explanations as inference unless verified.
- A smaller sample may support an exploratory profile, but label its confidence as low and do not treat it as a stable house style.

## Extraction Dimensions

Analyze reader promise, opening speed, sentence and paragraph rhythm, evidence/story/analysis ratio, explanation patterns, emotional intensity, transitions, conclusion type, and comment prompt. Separate topic effects from expression effects.

Use `huashu-nuwa` when deep extraction is justified. Its output is research material that must pass the boundaries below before entering the editorial workflow.

## Three-Layer Model

1. **Transferable mechanisms**: genre conventions, common terminology, opening logic, pacing, evidence placement, explanation methods, and reader interaction patterns.
2. **Account voice**: our stable reader relationship, judgment style, vocabulary range, emotional ceiling, evidence standard, and recurring content promise.
3. **Source-specific elements to avoid**: distinctive phrases, signature metaphors, unique stories, personal identity claims, and identifying argument chains.

## Multi-Source Fusion

`多源融合` does not mean mechanically averaging writers. Choose complementary mechanisms for a stated reader problem, explain why each is useful, and resolve conflicts in favor of the account voice and evidence standard.

A production profile must record:

- which mechanisms came from which samples;
- which parts are common genre practice;
- which conclusions are observations versus inference;
- how the mechanisms were changed for this account;
- what source-specific material is excluded.

## Named-Author Boundary

`具名作者` research is allowed because concrete examples make style analysis testable. However, `禁止直接模仿` a single living or identifiable author in the final deliverable. Do not promise indistinguishability, impersonate the source, or preserve signature wording.

When the user names one author, use that author as one benchmark and add other relevant sources or the account's established voice before drafting. If only one source is available, output an exploratory analysis first and ask for approval before using it in production.

## Account Adaptation

`账号化改造` must specify the target reader, expected value, evidence level, vocabulary, sentence rhythm, emotional range, and disallowed tactics. The article's thesis, source combination, reasoning, examples, and final wording remain newly constructed.

## Similarity Review

Run a `相似性检查` against all supplied source texts before publication:

- flag unusually long matching phrases and sequences of distinctive short phrases;
- flag copied story order, example order, or argument order from one source;
- ignore unavoidable names, facts, common terms, and standard genre phrases unless their arrangement is distinctive;
- rewrite or attribute flagged material, then recheck.

This review reduces accidental copying. It is not an AI-detector or platform-evasion test.

## Validation

Test the profile on a withheld source and an unrelated topic. A useful profile should explain recurring choices without reproducing source sentences, and should still sound like the account when the topic changes.
