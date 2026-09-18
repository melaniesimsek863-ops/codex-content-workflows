# Article Quality Pass

## Order Of Operations

Run these steps after the evidence pack and outline exist:

1. Generate three `开头候选`.
2. Select against the reader problem and evidence, not intensity alone.
3. Complete the article and run `读者评审`.
4. Revise argument and missing context.
5. Mark `受保护文本` and apply `shuorenhua` for final language polish.
6. Run the originality and similarity review.
7. Run `事实复核` on the exact final body and bind the result to its `SHA-256`.

## Opening Candidates

The three candidates must use different mechanisms:

- **Concrete fact or scene**: begin with a verified detail that creates a question.
- **Reader cost or benefit**: name a specific problem without exaggerated stakes.
- **Tension or counterintuitive finding**: state a defensible contrast the article will resolve.

Do not create three cosmetic rewrites of the same sentence. Score each candidate for accuracy, relevance, curiosity, trust, and fit with the account voice. Keep the selected opening and the reason for rejecting the others.

## Reader Review

Simulate at least three useful reading positions: the intended reader, a skeptical reader, and a reader with limited background. Record likely stop points, unclear terms, trust breaks, unanswered questions, excessive repetition, and unsupported leaps.

Reader simulation is editorial analysis, not real user research. Never fabricate reader quotations, demographic data, or testing results. Resolve substantive objections before polishing sentences.

## Language Controls

Use `shuorenhua` to improve clarity, specificity, rhythm, and natural Chinese. Keep edits reversible and compare before and after.

Prefer direct entry, concrete nouns and verbs, varied but readable sentence length, explicit logical relations, and conclusions earned by the preceding evidence. Remove throat-clearing, forced binary contrasts, repetitive slogan triples, dramatic fragments without content, fake punchlines, false agency, and generic wrap-ups.

Do not flatten deliberate voice, domain terminology, necessary repetition, or emotional force that is supported by the material. Natural writing is the goal; detector evasion is not.

## Protected Spans

Before language polishing, mark these as `受保护文本`:

- names, dates, figures, quotations, URLs, citations, and evidence identifiers;
- legal, medical, financial, policy, and safety wording whose precision matters;
- user-approved titles, disclaimers, and deliberate wording;
- any passage whose modification requires renewed source verification.

The polishing pass may adjust surrounding prose but may not alter protected meaning. Any necessary protected-span change returns to the evidence stage.

## Final Fact And Hash Gate

Run `事实复核` after all substantive edits. Record the exact body file, status, timestamp, unresolved claims, and lowercase hexadecimal `SHA-256`. Recompute the hash immediately before packaging or publishing.

If the current hash differs from the checked hash, the prior result is stale. Block publication, review the diff, and rerun the affected checks.
