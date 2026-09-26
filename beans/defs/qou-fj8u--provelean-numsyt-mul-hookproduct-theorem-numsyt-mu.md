---
# qou-fj8u
title: 'PROVE(lean): numSYT_mul_hookProduct — theorem numSYT_mul_hookProduct (μ : YoungDiagram) : numSYT μ * hookProduct μ = (μ.card).fa [cited sagan2001]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-sagan2001
created_at: 2026-08-01T23:31:03Z
updated_at: 2026-08-31T02:53:38Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/StandardYoungTableau.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/StandardYoungTableau.lean

### `numSYT_mul_hookProduct`  —  line 113  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem numSYT_mul_hookProduct (μ : YoungDiagram) : numSYT μ * hookProduct μ = (μ.card).factorial `
- **Cited:** `[sagan2001]`
  - [sagan2001] Sagan (2001), *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* — (no DOI/URL)
- **Tractability:** Hook-length formula numSYT·hookProduct = n!; Mathlib has no hook-length formula.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.


## RE-TRIAGED 2026-08-31 — MATHLIB LACKS IT (true) BUT IT IS BUILDABLE IN-REPO — do not track upstream

The `Next step` line above ("Infra-blocked: needs Mathlib theory that does not exist. Track
upstream") is one verdict that was stamped on fourteen beans in six seconds, and is wrong here.
Full audit: `docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md`.

The absence claim is correct: Mathlib has no hook-length formula. The INFERENCE is what is
wrong. The corpus already carries `YoungDiagram`, `StandardYoungTableau`, the branching rule
(`numStandardYoungTableaux_branching`) and, since #6164, `upSum_eq`. `numSYT_bot` in the same
file is already proved properly.

"Track upstream" tells the next agent to wait for something nobody is building. This is
in-repo work -- substantial, but in-repo.

The original text is kept above, not deleted: the Tractability line is per-item and is accurate;
only the Next-step verdict is being corrected.
