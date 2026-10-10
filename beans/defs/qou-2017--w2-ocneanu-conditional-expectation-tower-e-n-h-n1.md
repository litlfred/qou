---
# qou-2017
title: 'W2: Ocneanu conditional-expectation tower E_n : H_{n+1} -> H_n in Lean — build on the cyclicity bricks (#4126/#4110)'
status: completed
type: task
priority: normal
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-08-26T13:52:07Z
parent: qou-utb3
---


## W1 re-scope note (2026-07-25, qou-xik5 audit)

Wenzl positivity is SURPLUS to the `MarkovTrace` fields
(`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`). Trim W2's
deliverable: build `E_n` + the basic-construction absorption + the spanning
decomposition `H_{n+1} = H_n + H_n σ_n H_n` (what Ocneanu cyclicity induction
actually needs). Thread `HeckeConditionalExpectation` / `JonesBasicConstruction`
(HeckeTowerBasicConstruction.lean:169/:187, both positivity-free) as §3b-cond
hypotheses if needed; do NOT thread `WenzlTowerStep` (:209 — the
nondegeneracy/semisimplicity ascent is a different deliverable, not needed for
the three class fields).


## FINDING 2026-08-26 (from W3, PR #5827) — one of W2's three deliverables is missing

This bean is marked **completed**. Its own re-scope note names THREE deliverables:

  1. `E_n` (the conditional expectation)          — DELIVERED (`HeckeConditionalExpectation`, :169)
  2. basic-construction absorption                — DELIVERED (`JonesBasicConstruction`, :187)
  3. the spanning decomposition H_{n+1} = H_n + H_n σ_n H_n — **NOT DELIVERED**

`HeckeTowerBasicConstruction.lean` contains exactly three classes: the two above
plus `WenzlTowerStep` (:209, explicitly out of scope per this note). Corpus-grepped
the whole `QOU/` tree for a spanning/coset decomposition of H_{n+1} over H_n — the
only hits are `MarkovInductiveCyclicity.lean:116` (a docstring describing the shape
it ASSUMES) and `CoxeterParabolicInclusion.lean` (parabolic coset decomposition, a
different object). No class, no theorem.

**Why it matters:** the note itself calls it "what Ocneanu cyclicity induction
actually needs", and that is exactly right — it is what blocks W3's second half.

Not reopening (status changes are the author's call); flagging so the next agent
does not read `completed` as "the tower is fully interfaced".
