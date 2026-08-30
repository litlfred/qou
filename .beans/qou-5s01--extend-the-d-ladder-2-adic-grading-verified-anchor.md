---
# qou-5s01
title: Extend the D-ladder 2-adic grading verified anchor from K=5 to K=21 (data already committed)
status: todo
type: task
created_at: 2026-08-19T17:21:15Z
updated_at: 2026-08-19T17:21:15Z
---


## Done — anchor extended K=5 -> K=21, lean-direct exit 0

The Lean's own docstring already said "compute extends this to k=21" while the
FORMALIZED window stopped at 5. The data was committed; the formalization had
not caught up. Nothing new was computed.

**Verified first, then formalized.** Recomputed den(b_k) from the exact
`b_k_sqrt3_coeff` fractions in
`qbeta-dladder-generating-function-structure.witness.json` (21 orders, ORD 43)
rather than reading the witness's own `v2_den_b` field -- so the two are an
independent cross-check. They agree at every order, and the grading holds 21/21:
den(b_k) odd <=> k odd.

**Lean.** `bDen` extended to all 21 committed orders;
`bDen_two_adic_graded : TwoAdicParityGraded bDen 21`, `interval_cases <;> decide`.
Kept `bDen_two_adic_graded_five` as a corollary because the audit and surrounding
prose cite the five-term result by name.

    lean-direct exit 0, 2m29s (decide handles the 58-digit numerals)
    #print axioms -> [propext, Classical.choice, Quot.sound]  (no sorryAx)
    three_not_parity_graded -> [propext]

**What this is NOT.** Evidence, not proof. 21 orders of `decide` do not
establish a law for all k, and `DLadderGradingConjecture` remains the open
target -- it still needs the ser_sqrt/ser_div construction in Lean. Said in the
theorem docstring so the strengthened anchor cannot be mistaken for a closure.

## Env note for the next agent (cost me two failed runs)

lean-direct LEAN_PATH must point at `.../\.lake/**/build/lib/lean`, NOT
`.../build/lib` -- there is an extra `lean/` level. Also: the ROOT
`.lake/packages/mathlib` has 6990 oleans but the QOU-local
`content/quantum-observable-universe/lean/.lake/packages/mathlib` (3319) is the
one carrying `Mathlib/Tactic.olean`. Use the QOU-local tree:

    R=content/quantum-observable-universe/lean
    export LEAN_PATH=$(find "$R/.lake" -type d -name lean -path "*build/lib*" | tr '\n' ':')
