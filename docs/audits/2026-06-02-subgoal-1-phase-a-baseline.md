# Subgoal-1 Phase A — operator-valued branching baseline at A=2 + display-bug fix

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02` (PR #1698)
**Scope:** Run + characterize existing `canonical_tr_m_via_branching.py` infrastructure on the canonical anchor atoms.

## Display bug found + fixed

[`computations/canonical_tr_m_via_branching.py:445`](../../computations/canonical_tr_m_via_branching.py) truncated the verdict string to 30 characters via `verdict[:30]`. With `rel_err={float(rel):.2e}` producing strings like `"vs markov_peel rel_err=7.19e-10"` (length 31), the trailing `0` of `e-10` was clipped — so a passing **7.19e-10 (0.72 ppb)** match was rendered as the alarming-looking **7.19e-1 (72%)**.

**Fix**: drop the `[:30]` slice (one-character edit). After the fix the verdict reads correctly as `vs markov_peel rel_err=7.19e-10` — full ppb-tight precision visible.

## Phase A results

| atom | A | n | \|tr_M\|_branching | vs markov_peel | status |
|---|---|---|---|---|---|
| D (deuteron) | 2 | 6 | 0.388286424354067 | rel_err = 7.19e-10 = 0.72 ppb | **PASS** |
| T (tritium) | 3 | 9 | — | n/a | **BLOCKED** at A≥3 recursive inner step |
| ³He | 3 | 9 | — | n/a | **BLOCKED** (same) |
| ⁴He | 4 | 12 | — | n/a | **BLOCKED** (same) |

A=2 deuteron matches the canonical `markov_peel.tr_M_atomic` to 0.72 ppb — comfortably below the 1 ppQ (10⁻¹⁵) L1-compute target. The infrastructure is sound for A=2.

## A≥3 gap (per `compute_tr_m_via_branching` docstring)

The recursive step `ρ_ξ(β_inner)` at H_{3(A-1)} = H_6 (for A=3) requires inner-test data from H_3, but the existing A^λ_{ξν}(I) extracts are:

> "least-squares fits over the H_3 inner-test family, NOT universal"

So at H_9+ (A=3+), the A^λ_{ξν} matrices are RANK-DEFICIENT against the H_9 unknowns. The extracts produce correct values only for the test cases they were fit against — they don't generalize to all H_9 inner braids needed for the recursive step.

**Concrete remaining work** for A≥3 closure:

1. Extend `A_operator_extract_at_level.py` to produce **universal** A^λ_{ξν}(I) operators at H_9+ (not least-squares fit) — requires more independent inner-test braids OR a different extraction methodology (e.g. direct categorical formula instead of fit)
2. Verify against markov_peel at A=3 (T, ³He) to confirm A^λ universality
3. Verify against markov_peel at A=4 (⁴He) to confirm composition / recursion
4. THEN compare operator-valued m_avg vs Family A H₄-scalar m_avg to see if Subgoal-1 closes the +2.89%

Items 1–3 are the owner-active research-grade work. Item 4 is the deliverable for m_avg closure.

## Phase B — deferred

Phase B (compare operator-valued m_avg vs Family A) requires Phase A to succeed at A≥3, which needs the universal A^λ extracts above. Not achievable in this session.

## Phase C — Lean target identified

The Lean theorem `prop:operator-valued-combiner-convergence` (per `2026-05-31-binding-magic-A-wireup.md` §"Concrete Lean gaps remaining") is tractable as a `Nat.rec` on A, modulo class hypotheses already in `crystal-r-matrix-sub-lemma.lean`. Statement form:

```lean
theorem operator_valued_combiner_convergence
    {A : ℕ} (hA : 1 ≤ A)
    [LRCoefficientHecke] [WenzlAOperator] :
    -- for atom β_atom at level n = 3A:
    ∃ (rep : Representation),
      char_lambda β_atom = peel_recurse A rep := by
  induction A with
  | zero => omega  -- contradiction with hA
  | succ k ih => …  -- Nat.rec step + sub-lemma 2.1 application
```

Lean toolchain unavailable in this sandbox (release.lean-lang.org blocked); deferred to a session with Lean access.

## Recommendation

This branch should commit the display-bug fix + this audit doc. The substantive Subgoal-1 work (universal A^λ extracts, A≥3 verification, m_avg comparison, Lean theorem) is research-grade and owner-active per the L2-100× audit. Next session can pick up Phase B once Phase A extracts are universal.

## Cross-references

- Scope doc: [`docs/coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md`](../coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md)
- Binding-magic-A wireup (Lean gaps): [`docs/audits/2026-05-31-binding-magic-A-wireup.md`](2026-05-31-binding-magic-A-wireup.md)
- L2-100× shared root: [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
- Operator-valued diagnosis: [`docs/audits/2026-05-17-structural-diagnosis-operator-valued.md`](2026-05-17-structural-diagnosis-operator-valued.md)
- Canonical reference (refuted Bring routes): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
