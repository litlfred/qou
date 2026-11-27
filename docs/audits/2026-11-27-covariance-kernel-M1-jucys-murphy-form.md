# Covariance kernel (`qou-x631`): M₁ and its Fulman split as Jucys–Murphy 3-cycle coefficients

**Date:** 2026-11-27 · **Branch:** `claude/m1-jucys-murphy-form-2026-11-27` · **Beans:** `qou-h315`
(M₁ machinery), `qou-k5r5` (M₁ > 0 gap), epic `qou-x631` · **Tier:** exact reformulation,
computer-verified n = 3…7. It is not a bound and does not prove M₁ > 0.

## Statement

The objects:
- `M₁(n) = Cov_Planch(Σ_□ h, ω₃)`, where `ω₃ = Σ_□ c² − C(n,2)` and `c` is the cell content.
- The Fulman split `Σ_□ h = A + D`, where `A = Σ_□ |c|` and `D = Σ_u d_u²`.
- `P = Cov(A, ω₃)` and `N = −Cov(D, ω₃)`, so that `M₁ = P − N`.

These are the inputs of `YoungDiagramKernelCSMargin.m1_pos_all_of_cs_inputs`.

The tools: `J_k = Σ_{i<k} (i k)` is the k-th Jucys–Murphy element. The elements `J_k` commute, and on
the Young vector `v_T` the element `J_k` acts by the content of box `k` of `T`. So `Σ_k φ(J_k)` and
`Σ_{k≠l} ψ(J_k − J_l)` are symmetric functions of the `J`'s. That makes them central [Jucys 1974;
Okounkov–Vershik 1996], acting on `V^λ` by `Σ_□ φ(c)` and `Σ_{□≠□'} ψ(c − c')` respectively.

For a central `Z` with eigenvalue `F(λ)`, `[σ]Z = Σ_λ F(λ) f^λ χ^λ(σ)/n!`. Combined with
`ω₃ = n(n−1)(n−2)χ^λ(3-cycle)/(3f^λ)` this gives `Cov_Planch(F, ω₃) = (n(n−1)(n−2)/3)·[σ]Z_F`.
Since `E ω₃ = 0`, the covariance needs no centring. Hence:

```
P(n)   = (n(n−1)(n−2)/3) · [(1 2 n)] |J_n|
−N(n)  = (n(n−1)(n−2)/3) · [(1 2 3)] Σ_{k≠l} δ(J_k = J_l)
M₁(n)  = (n(n−1)(n−2)/3) · [(1 2 3)] ( Σ_k |J_k| + Σ_{k≠l} δ(J_k = J_l) )
```

The first line uses a **single** element `|J_n|`. Because `Σ_k |J_k|` is central, its coefficient on
`(1 2 n)` equals its coefficient on `(1 2 3)`. Every `|J_k|` with `k < n` lies in `C[S_k]`, so on
`(1 2 n)` only `|J_n|` contributes.

Corollaries, all exact:
1. **`P(n) > 0` if and only if `[(1 2 n)] |J_n| > 0`.** That is a sign condition on one
   Jucys–Murphy element.
2. Centrality also gives the telescoping form `[(1 2 n)]|J_n| = 1/3 + Σ_{k=4}^{n} [(1 2 3)]|J_k|`.
   The measured increments `[(1 2 3)]|J_k|` are `0, −1/30, −7/180, −1/30, −1/40` for `k = 4…8`. All
   are negative, and `[(1 2 n)]|J_n|` decreases: `1/3, 1/3, 3/10, 47/180, 41/180, 73/360` for
   `n = 3…8`. Since `P ~ ρ_P σ_A σ_W ~ n^{5/2}`, the coefficient decays like `n^{−1/2}`, and
   the sum of the increments converges to `−1/3`. So `P > 0` says the partial sums never reach
   their limit from above. This is an observation, not a proof.

## Verification

[`wlambda_covariance_M1_jucys_murphy_form.py`](../../computations/deltalambda/wlambda_covariance_M1_jucys_murphy_form.py)
computes each side independently, with no shared code:
- **Group-algebra side.** It multiplies by transpositions only. `|J_k|` and `δ(J_k − J_l)` are built
  as Lagrange polynomials through the possible integer eigenvalues. No characters, no partitions.
- **Partition side.** Hook-length formula plus contents. This side also asserts `Σh = A + D` on every
  partition.

The two sides agree exactly for `n = 3…7`: `P = 2/3, 8/3, 6, 94/9, 287/18` and
`M₁ = 2/3, 4/3, 8/3, 14/3, 7`. Arithmetic is exact `Fraction` throughout, with no float64.
Witness: `wlambda-covariance-M1-jucys-murphy-form.witness.json`.

## What it is, and what it is not

- **Is:** an exact translation of the CS-margin inputs `P` and `N` into the Jucys–Murphy algebra. In
  particular `P` becomes the spectral data of the one operator `J_n` against the 3-cycle `(1 2 n)`.
  This puts `P` within reach of the literature on JM-element moments and star factorizations
  (Lassalle; Goulden–Jackson; Irving–Rattan), which was not visible from the partition sums. A
  corpus grep for "Jucys" in the covariance-kernel audits found no prior statement of it (2026-11-27).
- **Is not:** a bound. The open input of `qou-k5r5` is unchanged: a rigorous finite-n bound on
  `δ_A = V_A/(n² v_A) − 1` (and on `ρ_P`) for `n ≥ 79`. `V_A = [e](Z_A²) − ([e]Z_A)²` is also a JM
  coefficient, but so far that is notation, not a bound.
- **Not checked:** whether the moments `[(1 2 n)] J_n^m` have a closed form strong enough to give an
  explicit finite-n bound on `[(1 2 n)]|J_n|`. That is the next question on this route.

## Cross-references

- CS-margin reduction: `YoungDiagramKernelCSMargin.lean`, [`2026-08-28-…-cauchy-schwarz-margin-reduction.md`](2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md)
- Current target: [`2026-09-04-…-ratio-route-is-the-target.md`](2026-09-04-covariance-kernel-M1-k5r5-ratio-route-is-the-target.md)
- Same day, the kernel side: [`2026-11-27-covariance-kernel-square-law-inverse.md`](2026-11-27-covariance-kernel-square-law-inverse.md)
