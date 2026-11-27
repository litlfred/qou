# Covariance kernel (`qou-x631`): the depth-2 tail ν_{n−2}(n) in closed form, sign onset n₂ = 10

**Date:** 2026-11-27 · **Branch:** `claude/kernel-three-routes-2026-11-27` · **Epic:** `qou-x631`
· **Tier:** closed form derived by hand and checked exactly for n = 4…26; the sign analysis of the
closed form is proved in Lean (sorry-free); the identity "ν = closed form" is **not** formalized.

## Statement

`ν_v(n) = Cov_Planch(N_v, ω₃)`, with `N_v` the number of cells of hook length `v` and
`ω₃ = Σ_□ c² − C(n,2)` (`YoungDiagramKernelPincer.nuV`). Depth 1 (`v = n−1`) is proved in
`YoungDiagramTailSecondInstance`, with sign onset `n₁ = 8`. For depth 2, and every `n ≥ 4`:

```
ν_{n−2}(n) = (n−2)(n−5)·Q(n)·C(2n−8, n−4) / (6(n−3)·n!)
Q(n)       = n⁶ − 25n⁵ + 235n⁴ − 1067n³ + 2528n² − 3112n + 1680
```

Values n = 4…9: `−2/3, 0, 2/3, −5/6, −139/60, −343/270`. Sign pattern from n = 4: `−, 0, +, −, −, −`,
then `+` for every `n ≥ 10`.

## Derivation

1. **Carriers.** A cell of hook `n−2` sits at `(1,1)`, `(1,2)`, `(2,1)`, `(1,3)` or `(3,1)`.
   - At `(1,1)` the shape minus its first hook has two cells, so it is `(a, 3, 1^b)` or its conjugate
     `(a, 2, 2, 1^b)`.
   - At `(1,2)`: `(n−1,1)` or `(n−2,2)`. At `(1,3)`: `(n)`. Conjugates give the column cases.
   - `ω₃` is conjugation-invariant, so ν is twice the row-side sum.
2. **One family.** Put `k = b+3`, so the shape is `(n−k, 3, 1^{k−3})`. The hook-length formula plus
   `C(m,b)/(b+3) = (b+1)(b+2)C(m+3,b+3)/((m+1)(m+2)(m+3))` give
   `f_k = (n−k−2)(k−1)(k−2)·C(n,k)/(2(n−2))`.
   Extending k to `0…n`, the terms `k = 1, 2, n−2` vanish. The terms `k = 0, n, n−1` reproduce
   `f` and `ω₃` of the boundary shapes `(n)`, `(n−1,1)` and `(n−2,2)` exactly. So
   `ν_{n−2}(n) = (2/n!)·Σ_{k=0}^{n} f_k² ω₃(k)`, with `ω₃(k)` a cubic in k.
3. **Collapse.** Write `f_k² ω₃(k)/C(n,k)²` in the falling-factorial basis `(k)_j`, then use
   Vandermonde: `Σ_k C(n,k)² (k)_j = (n)_j C(2n−j, n−j)`. Every term is a rational multiple of
   `C(2n−8, n−4)`. This is the same architecture as depth 1.
4. **Sign.** `Q(m+10) = m⁶ + 35m⁵ + 485m⁴ + 3333m³ + 11518m² + 17348m + 6360`, so `Q > 0` for
   `n ≥ 10`. The real roots of Q are ≈ 2.62, 3.70, 6.58, 9.48.

## Verification

- [`wlambda_covariance_depth_two_tail.py`](../../computations/deltalambda/wlambda_covariance_depth_two_tail.py)
  evaluates ν three independent ways: brute force over all partitions, the one-family k-sum, and
  the closed form. All three agree exactly (`Fraction`) for n = 4…26. Witness:
  `wlambda-covariance-depth-two-tail.witness.json`.
- `BraidKnotOctonion/YoungDiagramTailThirdInstance.lean` (sorry-free; axioms `propext,
  Classical.choice, Quot.sound`; `lean -DautoImplicit=false -s 65536` exit 0):
  - `nuDepthTwo_pos_of_ge_ten`
  - `nuDepthTwo_small_values`
  - `nuDepthTwo_pos_iff`: for n ≥ 4, positive iff n = 6 or n ≥ 10
  - `nuDepthTwo_eq_zero_iff`: for n ≥ 4, zero iff n = 5
  These are statements **about the closed form**, over a generic ordered field.

## What it is not

- **Not formalized:** steps 1–3, i.e. `nuV (n−2) n = nuDepthTwoClosedForm n`. The depth-1 file did this
  with a carrier classification (`DepthOneHookClassification`) plus a binomial collapse. Depth 2 has
  more carrier families (five cell positions, four boundary shapes) but the same method. Tracked as a
  bean `qou-swk4`.
- **Not a bound on M₁.** The tails are the top of the hook spectrum. The onsets so far are
  `n₁ = 8, n₂ = 10`. Whether the depth-d onset grows like `n_d ≈ 2d + 6` is an observation from two points,
  not a claim.
