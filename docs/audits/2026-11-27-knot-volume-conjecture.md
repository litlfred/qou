# Knot volume conjecture: what the corpus already proves, where V0^m stops being easy, and what the external discussion gets right

**Date:** 2026-11-27 · **Thread:** "Formalize knot volume conjecture" (QOU project, research front 1 of the 2026-11-27 swarm) · **PR:** #9456
**Inputs:** the owner's external AI discussion, 2026-11-25 to 2026-11-27 (unverified text, read critically here); brief `qou-swarm-2026-11-27/briefs/1-knot-volume.md`.
**Probe:** `computations/probes/weaving_kashaev_root_of_unity/` (pre-registered; `PREREGISTRATION.md` and Addendum 1 were written before the code they describe ran).
**Lean:** `QOU/Transcendental/SqueezeModulus.lean` (sorry-free).

Notation: V0 = σ₀σ₁⁻¹ ∈ B₃, the photon's chiral vertex. W(3,m) = closure of V0^m (the weaving, or Turk's-head, knots and links). ⟨K⟩_N = J_N(K; e^{2πi/N}) is the Kashaev invariant, normalised so that the unknot gives 1.

## 1. Summary

1. **The brief's first theorem target was already done.** The Kashaev–Murakami–Murakami volume conjecture for 4_1 = W(3,2) is machine-proved in the repository, sorry-free, by exactly the positive-sum squeeze the discussion proposes (`kashaev_saddle_volume`, `BraidKnotOctonion/FigureEightVolumeLiterature.lean`, July 2026). The Borromean rings W(3,3) are also proved (`BorromeanVolume.lean`, target 8·Cl₂(π/2)). Re-checked today: both compile, and `#print axioms` lists only `propext`, `Classical.choice`, `Quot.sound`.
2. **The family's next member, 8_18 = W(3,4), does not admit the same proof.** Its Habiro cyclotomic coefficients are computed here exactly. The first one is c₁(8_18) = q² − 3q + 3 − 3q⁻¹ + q⁻², which is negative at q = e^{2πi/N} for every N ≥ 5. So the Habiro sum of 8_18 is **not** term-wise positive at the Kashaev point. The 4_1 and Borromean proofs rely on that positivity, so their route does not extend to 8_18 as it stands.
3. **Amphichirality does not cause positivity.** The discussion credits the positivity of the 4_1 terms to amphichirality. 8_18 and 10_123 are amphichiral and their Habiro sums have negative terms, so that explanation is refuted by counterexample.
4. **Two volumes in the discussion are wrong.** Vol(8_18) = 12.3509 (the discussion says 5.3335) and Vol(10_123) = 17.0857 (it says 6.927).
5. **The owner's squeeze question has a sharp answer, now in Lean.** As an error estimate, the squeeze holds in every ordered group. Turning "error at most 1/(n+1) for every n" into "equal" holds **exactly when** the field is Archimedean (`archimedean_iff_modulus_limit_unique`). In a field with infinitesimals the same estimate is met by a whole halo of points.

## 2. What the corpus already had (not duplicated)

| object | where | status |
|---|---|---|
| VC for 4_1 | `BraidKnotOctonion/FigureEightVolumeSqueeze.lean`, `FigureEightVolumeLiterature.lean` | proved, sorry-free (beans qou-f248, qou-cpfn) |
| VC for Borromean rings | `BraidKnotOctonion/BorromeanVolume.lean` | proved, sorry-free (bean qou-z1wh and successors) |
| Borromean positive-sum feasibility | `computations/borromean_kashaev_positive_sum_probe.py` | the Habiro terms for W(3,3) are positive |
| Weaving-link R-matrix state model | `computations/probes/weaving_link_rmatrix_state_sum_vs_borromean_tower_probe.py` (bean qou-spds) | pins the convention of [arxiv-2209.06973v1] §5 and checks it against the 4_1 Habiro tower; re-run today, ALL PASS |
| Kashaev invariant as a typeclass | `QOU/Kashaev.lean`, block `conj:kashaev-volume-conjecture` | the 4_1 and Borromean instances are discharged |
| Surreal reading of the limit | `appendix-surreals/kashaev-surreal.md`, `conj:surreal-limit-transfer`, `hyperreal-limit-transfer` | a limit becomes an equality up to an infinitesimal, then the standard part |
| Vol(8_18) | `computations/substrate/knot_volumes.py` | 12.350906209158200174736304438426152014199256704120 |

## 3. Braid words and volumes

Checked with SnapPy, `snappy.Link(braid_closure=[1,-2]*m).exterior().high_precision()`. These values are numerical, not certified, and are used only as comparison targets.

| m | closure of V0^m | components | Vol | identified as |
|---|---|---|---|---|
| 2 | 4_1 | 1 | 2.029883212819307250… | 4_1, m004 |
| 3 | Borromean rings | 3 | 7.327724753417752120… | 6³₂ |
| 4 | **8_18** | 1 | **12.350906209158200174…** | 8_18 = K8a12 |
| 5 | **10_123** | 1 | **17.085709482982861276…** | 10_123 = K10a121 |

The discussion's values 5.3335 for 8_18 and 6.9274 for 10_123 are wrong. They match no standard invariant of these knots. A related claim also fails: the discussion says the complement of 8_18 is a 4-fold cover of the figure-eight complement. Hyperbolic volume multiplies by the degree under finite covers, and 12.3509 ≠ 4 × 2.0299 = 8.1195, so this is refuted (scope (b); the invariant is multiplicativity of volume under finite covers).

## 4. Probe results

### Q0, calibration (passed)

The state model evaluated at the root of unity reproduces the corpus 4_1 Habiro sum Σ_{m<N} Π_{j≤m} 4 sin²(πj/N) for every N = 2..24 at `mp.dps = 60`. The relative difference is below 10⁻⁵⁰ for N ≤ 22. At N = 23 and 24 it is 3·10⁻⁵⁰ and 8·10⁻⁵⁰, so the pre-registered 10⁻⁵⁰ threshold prints FAIL in `run-N15-24.log`. That is digit loss from the state sum's internal cancellation (Q3: the cancellation ratio grows like e^{1.2N}), not a disagreement. Above N ≈ 30 the run would need a higher `dps`. This is high-precision agreement, not exact arithmetic.

### Q1, values (diagnostic)

⟨8_18⟩_N and ⟨10_123⟩_N are real for every N tested (|Im| / |value| < 10⁻⁵⁰) and positive. At small N they are integers: ⟨8_18⟩ = 45, 493, 3987 at N = 2, 3, 4.

| N | (2π/N)·log⟨4_1⟩ − Vol | (2π/N)·log⟨8_18⟩ − Vol | (2π/N)·log⟨10_123⟩ − Vol |
|---|---|---|---|
| 16 | +1.541 | +0.686 | +0.261 |
| 24 | +1.183 | +0.601 | +0.313 |

All three sit above the volume and drift slowly, as an O(log N / N) correction would. The 10_123 offset is still rising at N = 24, so it has not reached its approach-from-above regime. **No limit is claimed from this table.** For 4_1, where the limit is proved, the offset at N = 24 is still +1.18. The table only shows that the numbers are consistent with the conjecture and that N ≤ 24 is far too small to read a limit off.

### Q3, state-model positivity (uninformative; recorded as such)

Write ⟨V0^{2k}⟩ = Σ_{a,b} clos(a)·P[a,b]·P[b,a], where P is the state-model transfer matrix of V0^k. This tests the discussion's "J_N(8_18) = Tr(M²) with M Hermitian". The products P[a,b]P[b,a] do not change under any diagonal change of state basis. Result: about half of the terms are negative **for 4_1 as well as for 8_18**. The cancellation ratio Σ|T| / |ΣT| grows like e^{≈1.24N} for 4_1 and e^{≈1.46N} for 8_18 (at N = 15). Since 4_1 has a positive Habiro sum, this test cannot detect positivity: the R-matrix state model is the wrong object. That is why Addendum 1 moved to the Habiro coefficients, which are canonical.

### Q4, Habiro coefficients (the result)

Habiro's cyclotomic expansion J_N(K;q) = Σ_{k<N} c_k(K;q) · Π_{j=1}^{k} {N+j}{N−j} is unique, with c_k ∈ ℤ[q^{±1}] independent of N. At q = e^{2πi/N} the product equals Π 4 sin²(πj/N) ≥ 0. So ⟨K⟩_N is a term-wise non-negative sum **iff** c_k(K; e^{2πi/N}) ≥ 0 for every k < N.

The c_k are computed exactly, as integer Laurent polynomials, by triangular solve from J_1, …, J_{K+1}. The divisions are exact integer long divisions and would raise on any remainder, so integrality, which Habiro's theorem predicts, is checked at every step. The 4_1 calibration gives c_k = 1 for every k, as it should.

| knot | c₁(q) | c₁ at q = e^{iθ}, x = 2cos θ | sign at the Kashaev point |
|---|---|---|---|
| 4_1 | 1 | 1 | > 0 |
| **8_18** | q² − 3q + 3 − 3q⁻¹ + q⁻² | **x² − 3x + 1** (roots φ⁻², φ²) | **< 0 for every N ≥ 5**; c₁(1) = −1 |
| 10_123 | −q³ + 4q² − 6q + 8 − 6q⁻¹ + 4q⁻² − q⁻³ | — | < 0 only at N = 5 among N ≤ 60; c₁(1) = 2 |

c₂(8_18) = q⁶ − 3q⁵ + 9q³ − 8q² − 6q + 16 − 6q⁻¹ − 8q⁻² + 9q⁻³ − 3q⁻⁵ + q⁻⁶.

The roots of c₁(8_18) in x are the squares of the golden ratio and of its inverse, (3 ± √5)/2. That is an observation, not a claim of meaning.

Through k = 7, c_k(8_18)(e^{2πi/M}) is negative on long runs of M for every k ≥ 1 (see `habiro-K7.log`). The 10_123 coefficients are positive at almost every tested M, with isolated negatives (k = 1 at M = 5, k = 6 at M = 14). Full per-term tables: `weaving-habiro.result.json`, key `kashaev_terms`.

### 4b. The Kashaev-point Habiro terms, N ≤ 14 (run with K = 13, `habiro-K13.log`)

For N ≤ 14 every coefficient needed is known, so each ⟨K⟩_N splits exactly into its N Habiro terms t_k(N) = c_k(e^{2πi/N})·Π_{j≤k} 4 sin²(πj/N).

**Cross-check.** The sums Σ_k t_k(N) agree with the Q1 values to every printed digit. For example, ⟨8_18⟩_11 = 8744099146.7265990122 by both routes, and ⟨10_123⟩_12 = 203293768051548.60238 by both. The two routes are independent: Q1 evaluates the state model at the root of unity in mpmath, while Q4 solves for the exact polynomials and then evaluates them. So evaluating at the root of unity commutes with the state sum, as it should.

| N | negative Habiro terms of 8_18 (k) | negative Habiro terms of 10_123 (k) |
|---|---|---|
| 2–4 | none | none |
| 5 | 1 | 1 |
| 6–9 | 1, 2 | none |
| 10–12 | 1 | none |
| 13 | 1, 5 | none |
| 14 | 1, 4, 5, 6 | 6 |

Through k = 13, each c_k(8_18) is negative on long runs of roots of unity. The 10_123 coefficients are positive at every tested M (k + 1 ≤ M ≤ 60) for k = 2..12; the only exceptions are k = 1 at M = 5, k = 6 at M = 14 and k = 13 at M = 28. So **⟨10_123⟩_N is a term-wise positive Habiro sum for every N = 6..13**, and fails only at N = 5 and N = 14 in the range computed. Whether the negatives stay sparse and small as N grows is the question behind bean `qou-8xyf`.

**Verdict.**
* "The Habiro sum of 8_18 is term-wise non-negative at the Kashaev point": **false**. This is scope (b) for the Habiro route, because the expansion is unique and c₁(8_18)(e^{2πi/N}) < 0 is exact algebra (x² − 3x + 1 < 0 on 2cos(2π/N) ∈ (φ⁻², φ²)). It is scope (a) for the wider claim "8_18 has no positive formula": other decompositions are not excluded.
* "Amphichiral ⇒ term-wise positive" (the discussion's explanation for 4_1): **false**, with 8_18 as the counterexample.

## 5. Verdicts on the discussion's other claims

| # | claim | verdict | basis |
|---|---|---|---|
| 1 | S₄ (the Amitsur–Levitzki standard polynomial) vanishes on H₃(q) | **true** | H₃ ⊗ ℚ(q) ≅ ℚ(q) ⊕ ℚ(q) ⊕ M₂(ℚ(q)) is split semisimple. S₄ vanishes on M₂ (Amitsur–Levitzki) and on commutative factors, and H₃ over ℤ[q^{±1}] is free, so it embeds. **Proved in Lean, sorry-free** (`QOU/StandardModel/HeckeH3StandardPolynomial.lean`, `S4_elem_eq_zero`; axioms `propext`, `Classical.choice`, `Quot.sound`). Stronger than the semisimple argument: it holds over every commutative ring and for every `h`, with no invertibility of `[2]_q[3]_q`. Method: `S₄` as an alternating map reduces to the 15 sorted basis quadruples; the ten containing `T_e = 1` vanish since `S₄(1,·,·,·) = 0`; the other five are checked on the single vector `T_e`, which suffices because the model's elements commute with right multiplication by `σ₀`, `σ₁`. |
| 1′ | "tr_D(S₄²) < 0 while tr_D(S₄*S₄) > 0" on H₃ | **inconsistent with 1** | If S₄ ≡ 0 on H₃, every trace of S₄² and of S₄*S₄ is 0. The sign claims can only refer to n ≥ 4 (TL₄ has an M₃ block, where S₄ ≠ 0). As written, the discussion applies them to 3-braids. |
| 2 | Chen–Yang: TV = \|RT\|² | **true for closed manifolds; different for link complements** | For a complement, Detcherry–Kalfagianni–Yang (arXiv:1701.07818, Thm 1.1) write TV_r as a sum over colourings of \|J_{L,c}\|², not as one \|RT\|². Not in `library/`, so a candidate for intake. |
| 3 | Murakami arXiv:2501.00225 proves the VC for hyperbolic double-twist knots | **the paper exists; the content is unverified** | Title: "Complexified tetrahedrons, fundamental groups, and volume conjecture for double twist knots". Not in `library/`. The discussion's "4 of 20 eight-crossing knots proved" table is unverified. Its "8_4 ≅ J(4,−3)" looks doubtful: 8_4 has continued fraction [3,1,4], of length 3. |
| 4 | "All 12 hyperbolic knots with ≤ 7 crossings are proved" | **contested in the corpus** | 5₂ and the 6-crossing knots are proved (audit 2026-08-30, Ohtsuki; Ohtsuki–Yokota). Bean qou-b5h9 records Ohtsuki–Yokota stating that their homotopy step fails at 7₂. The 7-crossing claim needs a pinpoint citation before the corpus repeats it. |
| 5 | Turaev genus of the (−2,3,7) pretzel is 1 | **plausible, unverified** | (−2,3,7) is non-alternating, so g_T ≥ 1. g_T ≤ 1 would follow if it is almost alternating (Armond–Lowrance). No held source checked. |
| 6 | "Lifting to Bring's thickened surface makes S₄ positive / switches S₄ on" | **not assessable** | No algebra, trace or lift is specified, so it is not yet a mathematical statement and cannot be formalised until it is defined. |
| 7 | Borromean VC proved by a positive-sum squeeze | **true, in-corpus** | `BorromeanVolume.lean`. |
| 8 | 8_18 is the closure of V0⁴; 10_123 of V0⁵ | **true** | SnapPy identification, §3. |
| 9 | J_N(8_18) = Tr(M²) with M real symmetric, hence positive | **false via Habiro (§4, Q4); untested otherwise** | The canonical expansion has negative terms. The state-model trace form cancels exponentially, but so does 4_1's (Q3). |

## 6. The owner's question: is the squeeze just an error estimate, and what happens with infinitesimals?

**Yes, and Lean now says exactly where the Archimedean property enters.** `QOU/Transcendental/SqueezeModulus.lean`:

* `abs_sub_le_of_squeeze`: if a ≤ x ≤ b and both a and b are within e of L, then so is x. This holds in any linearly ordered additive group, with no Archimedean property, topology or completeness. `abs_sub_le_of_squeeze_relaxed` adds a target known only to within η (the error becomes e + η). This covers the "interval domain" idea: a constant known to finite precision widens the bound and costs nothing more.
* `abs_log_sub_log_le_log_of_le_mul` and `abs_scaled_log_sub_le`: if 0 < T ≤ S ≤ N·T, then |(c/N)·log S − (c/N)·log T| ≤ c·log N / N. This is the max-term step of the 4_1 and Borromean proofs, isolated.
* `archimedean_iff_modulus_limit_unique`: a linearly ordered field is Archimedean **iff** every sequence has at most one limit with modulus 1/(n+1). The non-Archimedean direction (`exists_halo_of_not_archimedean`) produces a nonzero infinitesimal L with |L| ≤ 1/(n+1) for every n. So in the hyperreals or the surreals the squeeze pins down a halo, not a point.

How this fits the corpus: `conj:surreal-limit-transfer` and `hyperreal-limit-transfer` already say that a limit statement becomes an equality up to an infinitesimal, recovered exactly by the standard part. The halo theorem is the converse half: without Archimedes the standard-part step cannot be skipped, because the estimate alone leaves the infinitesimal undetermined. By Hölder's theorem every Archimedean ordered field embeds in ℝ, so "any Archimedean ordered field" means "any subfield of ℝ".

**The Lawvere / ev–coev view, judged on cost and benefit.** In Lawvere's picture a Dedekind real is a pair of adjoint bimodules over the quantale [0, ∞], and the "squeeze" condition inf(U − L) = 0 is the unit (coev) of that adjunction, i.e. the locatedness of the cut. That reformulates what the two Lean statements above already capture: the error estimate, plus locatedness / uniqueness. It produces no new estimate for any knot, and building enriched-category reals in Lean would cost far more than it returns here. **My judgement: do not formalise it on this front.** At most it merits a one-paragraph remark beside `conj:surreal-limit-transfer` (proposed, not applied). Evaluating transseries at ω while keeping the (log N)/N one-loop term is the same story: the Q1 table shows that this term dominates the finite-N offsets, but naming it at ω derives nothing.

## 7. What this changes, and options

**For the paper.** Nothing published moves. The 4_1 and Borromean instances stand. The external discussion should not be imported as written: the volumes for 8_18 and 10_123 are wrong, the amphichirality explanation is refuted, and the S₄ sign claims contradict the S₄ ≡ 0 statement made in the same text.

**For the V0^m programme.** W(3,2) and W(3,3) are proved because their Habiro terms are positive. W(3,4) = 8_18 breaks that pattern at the very first coefficient. W(3,5) = 10_123 is unexpectedly close to positive (isolated negatives at small M only), so it is the better next candidate for a squeeze-type argument. Its sum is not term-wise positive either, so a proof would need to control the few negative terms rather than rely on positivity.

Options (each states what it costs and what it gives):

1. **Stop here and land the PR** (audit, probe, Lean lemmas). Costs nothing more. Records the 8_18 negative and the squeeze answer.
2. **Formalise the c₁(8_18) negativity in Lean**: the trigonometric inequality, sorry-free, with the identification of c₁ as computed data cited from the probe. About an hour. It gives a durable, checkable form of the scope-(b) statement.
3. **Probe 10_123's near-positivity**: compute c_k for k up to about 20 and locate every negative Kashaev-point term, then test whether a max-term squeeze survives with an explicit negative-mass bound. A few hours of compute and analysis. It might open a third proved member of the family, or might not.
4. ~~Prove S₄ ≡ 0 on the concrete H₃ model.~~ **Done** (owner card choice 2026-11-27): `HeckeH3StandardPolynomial.lean`, over any commutative ring and any `h`. Claim 1 is settled formally; the n = 3 versus n ≥ 4 line stands.

**My recommendation (judgement, not a finding):** 1 + 2 now, then 3. If nothing is chosen, the PR lands options 1 and 2 only.

## 8. Reproduce

```bash
python3 -u computations/probes/weaving_kashaev_root_of_unity/weaving_kashaev_probe.py 16          # Q0–Q3, N = 2..16
python3 -u computations/probes/weaving_kashaev_root_of_unity/weaving_kashaev_probe.py 24 15 0 -N15-24   # Q1 only, N = 15..24
python3 -u computations/probes/weaving_kashaev_root_of_unity/weaving_habiro_coefficients.py 13     # Q4, exact c_k for k ≤ 13
```

## 9. Addendum (stage 3 of qou-pc7n): total positivity at every Galois conjugate

A per-N Hermitian-square certificate (a sum of norms from Q(ζ_N) down to Q(ζ_N)⁺, as proved for 4₁ in `QOU/Core/KashaevHermitianCertificate.lean` and `KashaevReflection.lean`) forces ⟨K⟩_N > 0 at **every** primitive N-th root, not only at e^{2πi/N}. Measured with `galois_total_positivity_probe.py` (mpmath, 60 digits, from the exact Habiro c_k of §5, so N ≤ 14):

| knot | N range | conjugates negative | smallest value | max imaginary residue |
|---|---|---|---|---|
| 4₁ (control) | 2–14 | none | 5 | 0 |
| 8₁₈ | 2–14 | **none** | 45 | 4e-48 |
| 10₁₂₃ | 2–14 | **none** | 121 | 9e-44 |

The 4₁ control matches the Lean bounds: at N = 5 the conjugate a = 2 gives 41.53, against the proved N² + (N−1)² = 41.

**Consequence.** For 8₁₈ and 10₁₂₃ the obstruction found in §5 (negative Habiro terms) is **not** an embedding obstruction: their Kashaev values are totally positive for every N ≤ 14. By Siegel's theorem, a totally positive element of the totally real field Q(ζ_N)⁺ is a sum of squares there, hence a sum of norms from Q(ζ_N). So per-N Hermitian-square certificates **exist** for these N; what is missing is a **uniform-in-N** certificate like the Pochhammer one for 4₁.

**This corrects my thread remark** that the embedding caveat "will bite for 8₁₈". The negative c₁ rules out the term-wise Habiro certificate only. Total positivity beyond N = 14 is not measured; that needs c_k for k > 13.

```bash
python3 -u computations/probes/weaving_kashaev_root_of_unity/galois_total_positivity_probe.py
```
