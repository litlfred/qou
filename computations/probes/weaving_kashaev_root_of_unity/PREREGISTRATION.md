# Pre-registration: is the Kashaev invariant of the weaving knots V0^m a positive sum?

Written 2026-11-27, **before any code in this directory was run.** Thread
"Formalize knot volume conjecture" (QOU project). Brief:
`qou-swarm-2026-11-27/briefs/1-knot-volume.md`, item 2.

## Objects

* V0 = σ₀σ₁⁻¹ ∈ B₃ (the photon's chiral vertex). W(3,m) = closure of V0^m.
  Identified with SnapPy 3.x (high-precision numerical volumes, not
  certified): W(3,2) = 4_1 (Vol 2.02988), W(3,3) = Borromean rings (7.32772),
  W(3,4) = 8_18 (12.35091), W(3,5) = 10_123 (17.08571). All amphichiral.
  The external discussion's values Vol(8_18) ≈ 5.3335 and Vol(10_123) ≈ 6.927
  are wrong.
* The coloured Jones state model of [arxiv-2209.06973v1] §5 in the convention
  pinned by `computations/probes/weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py`
  (convention `(True, True, False, 1, 1, 1)`; reproduces the corpus Habiro tower
  for 4_1 at n = 1, 2, 3 exactly). Long-knot normalisation J'_n(unknot) = 1.
* Kashaev point: colour n = N − 1, q = t = v² = e^{2πi/N}, w = v^{1/2} = e^{2πi/(4N)}.
  ⟨K⟩_N := J'_{N−1}(K; q = e^{2πi/N}).

## Arithmetic

mpmath complex at `mp.dps = 60`. No float. The quantum binomials are evaluated
by the q-Pascal recursion (no division, so no 0/0 at the root of unity).
This is high-precision evaluation, **not exact arithmetic**: sign and
positivity verdicts are reported with the size of the imaginary part and the
margin, and agreement is never called "exact".

## Questions and predictions (stated before running)

**Q0 (calibration).** ⟨4_1⟩_N from the state model equals the Habiro sum
Σ_{m<N} Π_{j≤m} 4 sin²(πj/N) (the corpus `kashaev N`) for N = 2..10.
Prediction: agree to ≥ 50 digits. A disagreement invalidates every row below.

**Q1 (values).** ⟨V0^m⟩_N for m = 4, 5 and N = 2..12 (as far as runtime allows).
Prediction: real (amphichirality), and (2π/N)·log|⟨K⟩_N| approaches Vol from
above with an O(log N / N) correction, as for 4_1. No claim is made from the
approach rate; it is a diagnostic.

**Q2 (sign of the invariant).** Is ⟨8_18⟩_N > 0 for every N tested? No
prediction; the discussion asserts it.

**Q3 (term-wise positivity, the discussion's "Tr(M²), M Hermitian" claim).**
For even m = 2k let P = (transfer matrix of V0)^k on the colour-state space and
write ⟨V0^{2k}⟩ = Σ_{a,b} T(a,b), T(a,b) = clos(a)·P[a,b]·P[b,a], a ranging
over long-strand states (first colour 0). The product P[a,b]P[b,a] is invariant
under every diagonal change of state basis, so the test does not depend on
that gauge. Measure: the number of terms with Re T < 0 or |Im T| > 10⁻⁴⁰|T|,
and the cancellation ratio ρ_N = Σ|T| / |Σ T|.

* Calibration m = 2 (4_1): a positive formula is known (Habiro), so if this
  test reports negative terms for 4_1 then failure of the test for 8_18 is
  **not** evidence against a positive formula for 8_18; it only says this
  state model is not one. That is the expected reading: verdicts are scope (a).
* Prediction: negative terms occur for m = 4; whether (1/N)·log ρ_N tends to a
  positive constant (exponential cancellation) is the measured quantity.

## What would change the plan

* Q0 fails: stop; the convention or the root-of-unity evaluation is wrong.
* Q3 shows no negative terms and ρ_N = 1 for m = 4: then a positive state sum
  exists in this model and the 4_1/Borromean squeeze architecture is worth
  attempting for 8_18. Otherwise record the obstruction as scope (a): this
  model, alone, is not a positive sum.

## Addendum 1 (2026-11-27, after the first run of Q0–Q3, before any Habiro code ran)

Result that prompted it: Q3 reports exponential cancellation for **4_1 as well
as 8_18** (ρ_N grows like e^{≈1.2N} for 4_1, e^{≈1.45N} for 8_18). Since 4_1 has a
positive Habiro sum, Q3 cannot decide whether 8_18 has one: the state model is
the wrong object. The right object is canonical.

**Q4 (Habiro positivity).** Habiro's cyclotomic expansion is unique:
J_N(K; q) = Σ_{k<N} c_k(K; q) · Π_{j=1}^{k} {N+j}{N−j}, with c_k(K) ∈ ℤ[q^{±1}]
independent of N. At q = ζ_N the product is Π_{j≤k} 4 sin²(πj/N) ≥ 0, so
⟨K⟩_N is a term-wise non-negative sum **iff** c_k(K; ζ_N) is real and ≥ 0 for
every k < N. Compute c_0, …, c_K exactly (integer Laurent polynomials in
w = q^{1/4}; no float) for 8_18 and 10_123 by triangular solve from
J_1..J_{K+1}, calibrate on 4_1 (prediction: c_k = 1), and evaluate c_k(ζ_M)
with mpmath for M = k+1..60.

* If some c_k(ζ_M) < 0 with M > k: the Habiro sum of that knot is **not**
  term-wise positive at the Kashaev point. That is a statement about a
  canonical invariant (scope (b) for "the Habiro route", since the expansion is
  unique), but it says nothing about other positive decompositions (scope (a)
  for "no positive formula").
* If all tested c_k(ζ_M) ≥ 0: report as evidence only (finitely many k, M).
