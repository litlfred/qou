# Covariance kernel: the Q⁻¹ series coefficients a_m, quantified

**Date:** 2026-11-27 · **Branch:** `claude/kernel-three-routes-2026-11-27` · **Epic:** `qou-x631`
· **Tier:** one classical identity (exact check) plus a high-precision measurement for n = 3…26.
It proves nothing about the kernel for other n, and it is not a bound.

Setting and notation:
[`2026-11-27-covariance-kernel-square-law-inverse.md`](2026-11-27-covariance-kernel-square-law-inverse.md).

## Objects

`Q = (1/n!) Σ_x x²` acts on `V^λ` by `1/f^λ`. The kernel is equivalent to `[σ]Q⁻¹ ≤ 0`, and
`Q⁻¹ = Σ_{m≥0} (e − Q)^m`. Up to one positive constant:

- `a_m = (1/n!) Σ_λ (f^λ)² ω₃(λ) (1 − 1/f^λ)^m`, with `a_0 = 0`.
- The tail has a closed form: `Σ_{m≥M} a_m = R(M) = (1/n!) Σ_λ (f^λ)³ ω₃(λ)(1 − 1/f^λ)^M`.
- `[σ]Q⁻¹ = R(1)`.

The square-law audit showed that the sign condition "(AM): every a_m ≤ 0" is false at n = 18. This
note measures how much that failure costs.

## 1. The first term is a count

`a_m = Σ_j C(m,j)(−1)^j p_j`, where `p_j = [σ]Q^j = P(X₁²⋯X_j² = σ)` for iid uniform `X_i`, so every
`p_j ≥ 0`. For `j = 1` the count is explicit.

- If `x² = (1 2 3)`, then x restricted to the other n−3 points is an involution, and on {1,2,3} it is
  `(1 3 2)`. So `#{x : x² = σ} = I(n−3)`, the number of involutions of n−3 points.
- Hence `a_1 = −p_1 = −I(n−3)/n! < 0` for every `n ≥ 3`.
- In the spectral normalisation this is `Σ_λ f^λ ω₃(λ) = (n(n−1)(n−2)/3)·I(n−3)` (Frobenius–Schur,
  `ν(λ) = 1`). The probe checks this exactly for n = 3…26 (check A).

More generally, Frobenius' formula for products of squares gives
`p_j = (1/n!) Σ_λ χ^λ(σ)·(f^λ)^{1−j}`: this counts maps from a non-orientable surface with j crosscaps
and one boundary labelled σ. The kernel `[σ]Q⁻¹ = (1/n!) Σ_λ χ^λ(σ)(f^λ)²` is the same exponential sum
at `j = −1`, while `j = 0` gives `0`. This is a reformulation, not a proof route.

## 2. Measurement of the sign pattern and the cancellation

`wlambda_covariance_qinv_series_coefficients.py` uses mpmath at 50 digits, with no float.
- It scans `t ↦ a(t)` on a log grid over `[1, 10⁷·f_max]` and refines each sign change by root finding.
- It then splits `R(1)` into the positive mass `P₊ = Σ_{a_m>0} a_m` and the negative mass
  `N₋ = −Σ_{a_m<0} a_m`, using R at the integer cuts.

| n | sign changes of a(t), t ≥ 1 | zero / f_max | P₊ / N₋ |
|---|---|---|---|
| 3…17, 19…25 | 0 (a_m < 0 for every m ≥ 1) | — | 0 |
| 18 | 1, at m ≈ 5.92·10⁹ | ≈ 362 | ≈ 2.6·10⁻¹⁶¹ |
| 26 | 1, at m ≈ 3.53·10¹⁴ | ≈ 143 | ≈ 1.9·10⁻⁶⁶ |

- **Where the sign flips.** The crossing sits at `m ≈ s*·f_max`, where `s*` is the large-tilt crossing
  of `Cov(ω₃, f^s)` (362.94 at n = 18, 144.13 at n = 26). Near the top shapes,
  `(1 − 1/f)^m ≈ e^{−m/f}` varies in f like `f^{m/f_max}`.
- **The cancellation is not close.** Where (AM) fails, the positive tail is smaller than the negative
  bulk by 66 to 161 orders of magnitude. `[σ]Q⁻¹ = P₊ − N₋` holds to 40 digits in every row.
- **What this says about a proof.** The sufficient condition (AM) is false, but only through a tail
  that the first term alone outweighs. A weakened condition of the form "a_m ≤ 0 for m ≤ C·f_max,
  plus a tail bound R(C·f_max) ≤ |a_1|" holds in every measured row. Proving it for all n needs two
  things: control of `Σ_{f ≥ f_max/C} f³|ω₃|` against `I(n−3)`, and the sign of a_m up to C·f_max.
  **Neither is proved.** Recorded as an option on bean `qou-x631`.

## Provenance

- Probe and witness: `computations/deltalambda/wlambda_covariance_qinv_series_coefficients.py`,
  `wlambda-covariance-qinv-series-coefficients.witness.json`.
- Measured, not proved: "no sign change for n ≤ 26 except 18, 26" is a grid scan up to `10⁷·f_max`.
  Beyond that the sign is the sign of `ω₃` summed over the max-dimension shapes, which the
  square-law audit tabulates exactly.
