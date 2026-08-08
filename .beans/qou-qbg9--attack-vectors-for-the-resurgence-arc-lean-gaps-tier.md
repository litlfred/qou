---
# qou-qbg9
title: 'Attack vectors for the resurgence-arc Lean gaps, TIERED by kind (not by file)'
status: todo
type: task
priority: high
created_at: 2026-08-08T12:05:00Z
updated_at: 2026-08-08T12:05:00Z
---

Survey 2026-08-08 of real `sorry`s in the resurgence arc (grep corrected to
exclude the phrase "sorry-free", which inflates naive counts):

    Mathlib/ArgumentPrinciple.lean          2
    Mathlib/BorelResummation.lean           4
    Mathlib/EllipticDivisorDegree.lean      2
    Mathlib/HadamardFactorization.lean      4
    Mathlib/IdentityIHLFBridge.lean         1
    Mathlib/QGevreyOrder.lean               4
    Mathlib/RSKBridge.lean                  1
    Mathlib/SYTBranchingRecursion.lean      3
    Mathlib/SYTHookGNW.lean                 3
    Resurgence/StokesMatrixDescent.lean     1

**These are not one kind of gap and must not be attacked as one.** Tiering:

## TIER 1 — hard Mathlib gaps. NOT session-closeable. Do not start casually.

`ArgumentPrinciple`, `EllipticDivisorDegree`, `HadamardFactorization`,
`BorelResummation`.

`EllipticDivisorDegree`'s cited sorry says it outright: *"needs the argument
principle (Σ ord = (1/2πi)∮ f'/f) from complex analysis"*, absent from Mathlib
v4.24.0. Hadamard factorization and Borel resummation are the same shape: real
analytic theorems missing upstream. These belong to the existing epic `qou-08a2`
(keystone de-abstraction, hard Mathlib-gap infra), not to an afternoon.

**Honest note against my own session's work.** The `det A` argument in
`qou-qbe9x` -- that C1's third singular site is non-removable because
`deg div(det A)|_{C*} = -1` is gauge-invariant -- leans on exactly the
sum-of-orders fact that `EllipticDivisorDegree` cannot yet formalise. The
argument is correct mathematics and standard, but it is **not** Lean-backed, and
this bean records that so nobody cites it as if it were.

## TIER 2 — algebraic, plausibly closeable. START HERE.

`Resurgence/StokesMatrixDescent.lean` (1 sorry): block-diagonalisation (A.i) of
an `S_n`/Wedderburn-equivariant Stokes matrix. The neighbouring lemma is already
a clean `calc` over orthogonal idempotents (`e i * S * e j = 0` from
`hf.ortho`), so the missing step looks like idempotent bookkeeping rather than
analysis. **Assess first; if it is genuinely algebraic, close it.**

`Mathlib/IdentityIHLFBridge.lean` (1), `Mathlib/RSKBridge.lean` (1): single
sorries in bridge files -- cheap to at least CLASSIFY (algebraic vs analytic)
even if not to close.

## TIER 3 — combinatorial, off the resurgence critical path.

`SYTBranchingRecursion` (3), `SYTHookGNW` (3). Standard-Young-tableaux
combinatorics. Likely tractable with effort, but they do not gate the alien-
calculus work; do not let them absorb the arc's budget.

## TIER 4 — the analytic residual of q-Gevrey order.

`Mathlib/QGevreyOrder.lean` (4). Read the file's own header before touching it:
the **algebraic heart is already proved sorry-free** -- product adds order, bar
involution negates it, geometric sequences have order 0, and the dominant-balance
inequality `s k² + t j² <= E(s,t)(k+j)²` (a completing-the-square argument per
regime). What remains is the **Cauchy-convolution order law** (MI-2): the ε-δ
assembly into the order LIMIT, plus a lower bound needing a non-cancellation
hypothesis on leading coefficients.

That residual is real analysis, not bookkeeping -- but it is the most *on-arc* of
the analytic gaps, since q-Gevrey order is exactly the growth class the new
`QGevreyTaming.lean` works in. If any Tier-1-flavoured gap is worth the
investment, it is this one.

## Method

1. Classify before attacking. A "sorry" in an analytic file and a "sorry" in an
   algebraic one are different tasks; the counts above deliberately do not rank
   files by sorry-count, which would put `BorelResummation` (4, hard) above
   `StokesMatrixDescent` (1, plausibly easy).
2. Tier 2 first, then re-assess. Closing one algebraic sorry is worth more than
   half-finishing an analytic one.
3. Anything Tier 1 that is attempted must go through `qou-08a2`, and must record
   which Mathlib theorem is missing rather than working around it with an axiom
   (§"Axiomatization is NOT a Proof").
