# Staircase EW-residual k=4 pairwise reading — 2026-05-17

## Question

Companion to `2026-05-17-staircase-ew-k3-mpfr-spectral.md` (PR #680):
does the k=4 case of the staircase EW-residual conjecture exhibit the
same pattern as k=3 (= literal conjecture falsified, leading-order
approximation only)?

The existing `staircase_ew_residual_conjecture.py` (on `main`) reports
a `0.14 %` pairwise match for k=4, cited as evidence that the
literal conjecture holds at k=4 with `q^(1/7)` as the exact pairwise
ratio. **Is the 0.14 % match structural, or a random coincidence in
the dim-768 spectrum?**

## Probe

[`probe_staircase_ew_k4_pairwise_readings.py`](../../computations/probe_staircase_ew_k4_pairwise_readings.py)
runs the literal-conjecture reading + a coincidence-by-chance test:

1. Build 768×768 Hoefsmit `V_(4,3,2,1)` matrices at float64 via
   the existing `build_seminormal_matrices` fast path.
2. Compute the canonical β_EW word image
   `M = σ_1⁴ · Δ_I · σ_3⁶ · Δ_I · σ_5⁸ · Δ_I · σ_7⁶ · Δ_I · σ_9⁴ · Δ_I`
   (43 generators from
   [`staircase_ew_predictions.beta_ew_word(10)`](../../computations/staircase_ew_predictions.py)).
3. Full float64 eigendecomposition of `M` (`np.linalg.eigvals`).
4. **Literal-conjecture pairwise search**: scan all
   `(i, j)` pairs of positive-real eigenvalues for the best
   ratio match to `q^(1/7)`.
5. **Coincidence test**: compute `expected |Δ_rel| if random ≈
   max_eig / (N_pos × (N_pos − 1))`. The number of ordered pairs
   determines the floor of "best match by chance".
6. **Bar-pair structure check**: count `e_+ · e_- ≈ ±1` pairings.

## Results (float64 at q_0)

| Quantity | Value |
| --- | --- |
| dim V_(4,3,2,1) | 768 |
| positive-real eigenvalues | 384 |
| ordered pairs searched | 147072 |
| max eigenvalue magnitude | 56.005 |
| target `q_0^(1/7)` | 1.015017 |
| best pair indices | `(236, 188)` |
| best pair eigenvalues | `(3.067296, 3.026218)` |
| best pair ratio | 1.013574 |
| **|Δ_rel| (literal conjecture)** | **1.42 × 10⁻³** (0.14 %) |
| **expected |Δ_rel| if random** | **3.81 × 10⁻⁴** |
| **coincidence factor (actual/random)** | **3.73 ×** |
| bar-pair structure | 384 (−1) + 0 (+1) + 0 unpaired |

## Conclusions

### 1. The 0.14 % match is NOT structural — it is comparable to (or worse than) random coincidence

With ~147k ordered pairs in the spectrum and eigenvalues spanning
[0.018, 56], pure random pairwise search has an *expected* best match
of `3.8 × 10⁻⁴`. The actual best match of `1.4 × 10⁻³` is **3.73 ×
worse than this random-coincidence floor.** If the conjecture were
structural, we would expect the actual match to be many orders of
magnitude *tighter* than the random floor; instead it is 3.7 × *looser*.

**The 0.14 % match cited in `staircase_ew_residual_conjecture.py` for
k=4 is essentially noise** — not evidence of a structural `q^(1/7)`
identity in the V_(4,3,2,1) spectrum.

### 2. Consistent with the k=3 falsification

[`probe_staircase_ew_k3_categorical.py`](../../computations/probe_staircase_ew_k3_categorical.py)
(PR #680) showed at 50 dps that the literal conjecture for k=3 is
falsified (best pairwise off by 6.95 %). The k=4 finding here
strengthens that conclusion: **the literal conjecture fails at every
testable k — k=2 (untestable), k=3 (falsified at 50 dps), k=4
(random-coincidence at float64).**

The empirical `0.13 %` (k=3) and `0.14 %` (k=4) figures previously
cited as evidence for the conjecture come from **different readings**
of the spectrum — `0.13 %` (k=3) was the CODATA-residual reading
(`cot θ_W / bare top/2nd ≈ q^(1/5)`, a leading-order approximation),
while `0.14 %` (k=4) was the literal pairwise search that this probe
now shows to be a random match.

### 3. Bar-pair structure is exact at float64

All 384 positive eigenvalues pair perfectly with their 384 negative
counterparts to form 384 `e_+ · e_- = −1` bar-pairs — exactly as
predicted by the conjugate-pairing analysis (`prop:beta-ew-bar-pair-
recursion`). This structural prediction is independent of `q^(1/7)`
and stands.

## Precision-upgrade caveat

Direct 50-dps verification of the dim-768 case (matching the k=3 probe's
mpmath approach) is infeasible in a single session:

* mpmath 768×768 multiplication at 50 dps ≈ 768³ × 50² ≈ 1.1 × 10¹³
  byte-ops per generator product.
* β_EW word has 43 generators → ~5 × 10¹⁴ byte-ops at ~10⁷ ops/sec
  ≈ **14 hours just for the matrix product**, plus ~30–50 hours for
  the 50-dps QR-based eigendecomposition.

Natural follow-up infrastructure (deferred):

1. **Sparse-aware mpmath multiplication** — exploit Hoefsmit's ≤ 2
   nonzeros per row in the first few generator products.
2. **Schur-Weyl block-decomposition** — decompose V_(4,3,2,1) into
   smaller H_n irreps via the `H_10 → H_n` chain, reducing the
   eigendecomposition to a sequence of smaller subproblems.
3. **Targeted inverse-iteration** — refine only the candidate
   eigenvalue pair via mpmath inverse iteration, starting from
   float64 eigenvectors.

Until that infrastructure is built, the float64 result here is the
authoritative status. The coincidence-by-chance analysis gives strong
evidence the conjecture is falsified at k=4 without needing 50 dps —
the random-coincidence floor at this dimension is **already comparable
to the empirical match**, so higher precision cannot rescue the
literal conjecture.

## Recommendation

* **Update `staircase_ew_residual_conjecture.py`** to report the
  coincidence factor alongside the `0.14 %` match — the bare residual
  alone is misleading in the dim-768 search regime.
* **Refine `conj:staircase-ew-residual`** per
  `2026-05-17-staircase-ew-k3-mpfr-spectral.md` — downgrade from
  "exact identity" to "leading-order approximation"; the k=3 Reading-A
  (CODATA-residual at 0.15 %) is the surviving content; the literal
  pairwise reading is falsified at both k=3 (6.95 %) and k=4
  (random coincidence).
* **Lean status** (`StaircaseCornerHook.lean` on #664):
  `StaircaseEWResidual` class instance's `sorry` should encode the
  approximate match, not an exact identity.

## Provenance

* Probe: `computations/probe_staircase_ew_k4_pairwise_readings.py`
* Witness: `computations/staircase-ew-k4-pairwise-readings.witness.json`
* Float64 baseline (existing): `computations/staircase_ew_residual_conjecture.py`
* k=3 50-dps companion: `docs/audits/2026-05-17-staircase-ew-k3-mpfr-spectral.md`
