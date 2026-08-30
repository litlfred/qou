---
# qou-qf8t
title: 'TOOL: does the projected class field''s TYPE equal the theorem''s conclusion (the computable half of the 3b-cond reading)'
status: completed
type: task
priority: normal
created_at: 2026-08-30T11:12:58Z
updated_at: 2026-08-30T11:24:45Z
---

## Candidate 2 measured and REFUTED — and it explains candidate 1

Hypothesis: AGENTS.md §3b-cond rule 5 states both forms — degenerate is *"the
class carries the block's own conclusion as a field"* (read out ONE field);
sanctioned is *"carry the two directions of an iff as hypotheses, derive it by
`Iff.intro`"* (compose TWO OR MORE). So the count of distinct local field
projections should discriminate.

Measured, same 297 theorems / 18 modules / 29 ledger verdicts as `qou-eqt3`:

    legit   (false alarm)  n=11   1 projection × 11   — ALL of them
    genuine (real defect)  n=18   1 ×15,  2 ×1,  5 ×2

**Every single `legit` reads exactly one field, and so do 15 of 18 `genuine`.**
The premise is false: composition does not occur in the `legit` population at
all. Best threshold 62 % = the always-flag baseline.

## The pair is the result

Two independent structural proxies, both landing at exactly baseline, and the
reason is now MEASURED rather than inferred: on every structural axis tried the
two populations are IDENTICAL — one local field projection, few external
constants — and differ only in what that one field MEANS (a hypothesis of the
claim, or the claim itself).

That upgrades `valueOnlyProjects`'s own docstring from caveat to finding:
*"what separates the two is whether the class carries the conclusion or its
inputs, and that is a reading, not a computation."* Two attempts to make it a
computation have failed for the same measured reason.

## The remaining candidate, stated precisely so it is not mis-built

Ask the semantic question directly: is the projected field's instantiated type
the conclusion? **It is NOT `isDefEq fieldType conclusion`** — `q_hecke_eigenvalue`
projects `∀ a b, a.sp = b.sp → … → a = b` and applies it, so the types differ
while the declaration is still degenerate. The shape to test is closer to
"the projection is applied only to bound variables and their projections", i.e.
the proof introduces no term of its own. Not attempted here; NOT known to work.

Both counters kept and emitted (`substantive_external`, `local_proj_count`) with
their refutations in the docstrings, marked DO NOT THRESHOLD, so neither is
rebuilt by an agent who reads a bean and not the code.
