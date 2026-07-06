# Gram matrix H_3 determinant — second root correctness finding

**Date:** 2026-05-25
**Branch:** `claude/three-tracks-1ppb-2026-05-25`
**Track:** A (Δ_λ closure / Option E Phase 1b-2)
**Severity:** correctness — theorem statement incorrect as written

## Finding

The Lean theorem `gramMatrix_det_ne_zero` in
[`content/quantum-observable-universe/particle-interactions/gram-matrix-h3-symbolic.lean`](../../content/quantum-observable-universe/particle-interactions/gram-matrix-h3-symbolic.lean)
was stated as:

```lean
theorem gramMatrix_det_ne_zero (u : ℝ) (hu_pos : 0 < u) (hu_ne_one : u ≠ 1) :
    (gramMatrix u).det ≠ 0
```

This statement is **false**. The H_3(q) Hoefsmit-seminormal Gram matrix
determinant has a **second positive real root** at
`u ≈ 0.6823278038...` — the unique positive real root of
`u³ + u − 1 = 0`, equivalently `q ≈ 0.4655712319...`
(real root of `q³ + 2q² + q − 1 = 0`).

## Evidence

Symbolic factorization (sympy, 6×6 Berkowitz det + sp.factor):

```
det(gramMatrix u)  =

       (u-1)(u+1)(u³+u-1)⁵(u³+u²+1)⁵ · p(u) · r(u)
   −  ──────────────────────────────────────────────
                  u¹⁰ · (u²+1)¹²

where
  p(u) = u⁶ − u⁵ + u⁴ − u³ + 2u² − u + 1   (no real roots)
  r(u) = u⁶ + u⁵ + 2u⁴ + u³ + u² + u + 1   (no positive real roots)
```

Numerical sign table:

| `u` | `det(G(u))` |
|---:|---:|
| 0.5 | −3.629729 |
| 0.6 | −0.013910 |
| 0.68232780 | 0 (root of u³+u−1) |
| 0.7 | +1.7e-6 |
| 0.8 | +0.006915 |
| 0.9 | +0.042706 |
| 1.0 | 0 (root of u−1) |
| 1.054 | −0.191698 |
| 1.110 | −0.691741 |
| 2.0 | −1768.253 |

Two sign changes ⇒ two positive real roots: `u ≈ 0.6823` and `u = 1`.

## Impact

The substrate value used by the QOU framework is `q_0 ≈ 1.110`, so
`u_0 = √q_0 ≈ 1.0535 > 1`. The framework's actual evaluation point
sits on the `u > 1` side of both roots, so this finding does not
invalidate the empirical numerical witnesses (`det(G(q_0)) ≈ −0.189`
remains true). The bug is **only in the theorem statement**: the
hypothesis `0 < u ∧ u ≠ 1` was too weak to derive
`det(gramMatrix u) ≠ 0`.

The downstream `gramInstanceAtPositiveQ` instance sketch in the
file's docstring (lines 181–189) was correspondingly under-conditioned;
no production code consumes it yet (the instance is in a docstring
comment, not active Lean), so there is no downstream breakage.

## Fix

Strengthen the hypothesis from `u ≠ 1` to `u > 1`. This:

1. Covers the framework's substrate (`q_0 > 1`).
2. Discards both roots (`u = 1` and `u ≈ 0.6823`) cleanly.
3. Makes the factorization-positivity argument tractable in Lean:
   for `u > 1`, every irreducible factor is provably positive
   (each `u^k`, `u² + 1`, `u + 1`, `u³ + u² + 1` is `> 0` for
   `u > 0`; `u − 1` and `u³ + u − 1` are both `> 0` for `u > 1`;
   `p(u)`, `r(u)` are unconditionally positive on ℝ).

Alternative weaker hypothesis: keep `0 < u, u ≠ 1` and add
`u³ + u − 1 ≠ 0`. Less clean; less aligned with the framework's
actual substrate constraint. Not preferred.

## Cross-check

Sympy regression script emits the full factorization as a witness:
[`computations/gram_h3_det_factorization.py`](../../computations/gram_h3_det_factorization.py).
The witness asserts:

- `det(G(q_0)) ≈ −0.189` (matches existing regression)
- numerator polynomial degree = 44 in `u` (after rational-cancellation
  against the denominator `u^10·(u²+1)^12`)
- factor list matches above
- positive-real root set = `{1, root(u³+u−1)}`

## Provenance

Discovered while attempting to discharge `gramMatrix_det_ne_zero`
sorry on branch `claude/three-tracks-1ppb-2026-05-25` (Track A of
the 1-ppb push, 2026-05-25). The proof strategy in the
file's docstring (lines 150–157) anticipated only the `(u−1)` factor;
the `(u³+u−1)⁵` factor was missed.
