/-
# QOU.QBeta.BirkhoffBarOddPythagorasBridge — the bar-odd unit-modulus carrier is a √−1, and the A=3 lift's modulus is a Pythagorean quadrature

The A=3 Δ_λ magnitude program (`A3AntiSelfAdjointLift`, merged #4611) reduced the lift
`r* = μ₃/c₃ ≈ 1.585` to **one** free anti-self-adjoint amplitude `E`, with the even-face
factor **affine** in `E`:

  `factor = factor_sa − (B·D⁻¹/A)·E = factor_sa − s·E`,   `factor_sa ≤ 1`,  slope `s := B·D⁻¹/A`.

Two later results pinned `E` to the frame-free Birkhoff connection cross-ratio
`E = χ(P)` (`BirkhoffAmplitudeE`, `BirkhoffAmplitudeWellPosed`), and the numeric evaluation
found `χ(P)|q₀` is a **pure unit-modulus phase**, `|χ| = 1` exactly (dev < 1e-30,
`computations/qbeta/c1-chi-magnitude-vs-r-star.witness.json`). That produced a "genuine type
tension" flagged in `BirkhoffAmplitudeE`'s docstring, left OPEN with no instance: how does a
carrier that is a **unit phase** supply the **real** magnitude `r* > 1` the lift needs — a
`real E` vs a `complex phase`?

This file resolves the *type tension* structurally (it does **not** compute `χ(P)`'s value —
that is beans `qou-wgnx`/`qou-vkg5`). Two corpus facts about the carrier `E = χ(P)`:

* **bar-odd** — `σ E = −E` (anti-self-adjoint; `DTIndexAmplitudeE.amplitude_barOdd`);
* **unit-modulus** — `E · σ E = 1` (the `|χ| = 1` numeric, w.r.t. the bar involution `σ`).

together force **`E² = −1`** (`E·(−E) = 1 ⇒ E² = −1`): the bar-odd unit-modulus carrier is a
**square root of −1**, not a real number (`sq_ne_neg_one_of_ordered`: no ordered field hosts
it — the exact statement of the "type tension"). Consequently, reading the physical lift as
the **modulus** of the complex affine carrier `factor_ℂ = factor_sa − s·E` gives a
**Pythagorean quadrature**

  `|factor_ℂ|² = factor_ℂ · σ(factor_ℂ) = factor_sa² + s²`

(the `E² = −1` cross-term `−s²E² = +s²` adds *in quadrature*, since `factor_sa`, `s` are
bar-even). This is the elliptic (unit-circle) counterpart of the **hyperbolic**
bar-even/bar-odd identity `P_m² − Q_m² = (2 cosh η)⁻²`
(`BarSymmetricBarAntiSymmetricIdentities`): there the bar-odd part enters with a `−` (cosh/sinh,
difference of squares); here the unit-modulus carrier enters with a `+` (E² = −1, sum of
squares).

**Reframing (scope-(a), the genuine value — recorded in the audit/witness, not wired).** The
magnitude question turns from "why is the longitudinal even-face correction
`ρ = 1 − factor ≈ −0.585` a negative `O(1)`" (all real readings `ρ ∈ {±h, ±ℏ_q} ≈ ±0.1`
**miss**, `a3_magnitude_berezinian_crossterm_probe.py`) into "why is the **transverse** slope
`s = √(r*² − factor_sa²)` an `O(1)` off-block amplitude". The datum is relocated to the
**transverse** (imaginary-`q`) direction — the same object as bean `qou-prjo` (transverse
NA-Stokes surface-curvature) — which is precisely why every *longitudinal* / real-reading /
`O(h)` probe failed.

**Honesty (STRICT — AGENTS.md §Axiomatization-is-NOT-a-Proof / §3b / §Strict Lean Discipline).**
This does **NOT** derive `1.585`: `factor_sa` and `s` are not independently pinned here (the
demonstration model `A=C=D=1` gives `√(1²+1²)=√2 ≠ 1.585`; the real values need the branching
compute, bean `qou-jqof`). Every theorem is generic algebra (a two-line `E²=−1`, a
ring-hom quadrature identity, an ordered-field impossibility), sorry-free, no `native_decide`,
no trivial-true, no axiom beyond the ambient. The physical *modulus reading* is a
`structure`-carried hypothesis with **NO instance** (`ModulusReadingHypothesis`); the
Pythagorean consequence is derived *conditionally* on it. `r*`/`μ₃`/`c₃` are never inverted;
nothing is wired.

## References

- [leitner2026] `QOU.QBeta.A3AntiSelfAdjointLift` (`factor_affine_in_amplitude`,
  `amplitude_surjective`/`_injective`, `evenFaceCorrection`, `crossTerm`);
  `QOU.QBeta.BirkhoffAmplitudeE` (`E = χ(P)`, the unit-modulus type tension);
  `QOU.QBeta.DTIndexAmplitudeE` (`amplitude_barOdd`, `σ E = −E`);
  `QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities` (the hyperbolic `P²−Q²` counterpart);
  beans `qou-wiub`, `qou-wgnx`, `qou-vkg5`, `qou-prjo`, `qou-jqof`.
- [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (the Birkhoff connection matrix `P`
  whose cross-ratio `χ(P)` is the carrier `E`).
-/
import Mathlib.Tactic

namespace QOU.QBeta.BirkhoffBarOddPythagorasBridge

/-! ### Part 1 — the bar-odd unit-modulus carrier squares to `−1`. -/

/-- **Bar-odd + unit-modulus ⇒ `E² = −1` (sorry-free).** For a carrier `E` in any commutative
ring with a bar involution `σ`, if `E` is bar-odd (`σ E = −E`, anti-self-adjoint) and has unit
modulus (`E · σ E = 1`, the `|χ| = 1` datum), then `E` is a square root of `−1`. This is the
algebraic core of the "real amplitude vs unit phase" type tension: the carrier is genuinely
`√−1`, never a real scalar. -/
theorem barOdd_unitModulus_sq_eq_neg_one {K : Type*} [CommRing K]
    {σ : K → K} {E : K} (hbar : σ E = -E) (hnorm : E * σ E = 1) :
    E ^ 2 = -1 := by
  rw [hbar, mul_neg, neg_eq_iff_eq_neg] at hnorm
  rw [pow_two]; exact hnorm

/-! ### Part 2 — the affine lift's modulus is a Pythagorean quadrature. -/

/-- **Quadrature identity (sorry-free).** For a ring-hom bar involution `σ : K →+* K`, a
bar-even self-adjoint reduction `fs` (`σ fs = fs`), a bar-even slope `s` (`σ s = s`), and a
bar-odd carrier `E` (`σ E = −E`) with `E² = −1`, the "modulus" `factor_ℂ · σ(factor_ℂ)` of the
affine lift `factor_ℂ = fs − s·E` is the **sum of squares** `fs² + s²` — the `−s²E²` cross-term
becomes `+s²`. -/
theorem affine_modulus_quadrature {K : Type*} [CommRing K] (σ : K →+* K)
    {fs s E : K} (hfs : σ fs = fs) (hs : σ s = s) (hbar : σ E = -E)
    (hE2 : E ^ 2 = -1) :
    (fs - s * E) * σ (fs - s * E) = fs ^ 2 + s ^ 2 := by
  rw [map_sub, map_mul, hfs, hs, hbar]
  linear_combination (-s ^ 2) * hE2

/-- **The bridge (sorry-free).** Bar-even background `(fs, s)`, bar-odd (`σ E = −E`)
unit-modulus (`E · σ E = 1`) carrier `E` ⇒ the affine lift's modulus is `fs² + s²`. Combines
Parts 1–2: the unit-modulus phase supplies a **real** magnitude to the lift via quadrature. -/
theorem barOdd_carrier_quadrature {K : Type*} [CommRing K] (σ : K →+* K)
    {fs s E : K} (hfs : σ fs = fs) (hs : σ s = s)
    (hbar : σ E = -E) (hnorm : E * σ E = 1) :
    (fs - s * E) * σ (fs - s * E) = fs ^ 2 + s ^ 2 :=
  affine_modulus_quadrature σ hfs hs hbar
    (barOdd_unitModulus_sq_eq_neg_one hbar hnorm)

/-! ### Part 3 — the type tension: no ordered (real) field hosts the carrier. -/

/-- **The carrier is not real (sorry-free).** In any ordered field, `E² = −1` is impossible
(`E² ≥ 0 > −1`). With Part 1 this is the exact statement of the "real `E` vs complex phase"
type tension: the bar-odd unit-modulus carrier `E = χ(P)` **cannot** live in the real ordered
lift field of `A3AntiSelfAdjointLift` — it is genuinely transverse (imaginary-`q`). -/
theorem sq_ne_neg_one_of_ordered {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (E : K) : E ^ 2 ≠ -1 := by
  intro h
  have h0 : (0 : K) ≤ E ^ 2 := sq_nonneg E
  rw [h] at h0
  have h1 : (0 : K) < 1 := zero_lt_one
  linarith

/-! ### Part 4 — the physical modulus reading as a §3b hypothesis (NO instance). -/

/-- **The modulus-reading hypothesis (content-bearing; NO instance is constructed).** Bundles
the derived inputs — a bar-involution `σ`, the bar-even self-adjoint reduction `fs`, the
bar-even transverse slope `s`, the bar-odd unit-modulus carrier `E`, and the target `rStar` —
together with the *physical modulus reading* `rStar² = factor_ℂ · σ(factor_ℂ)` (that the
physical A=3 lift is the modulus of the complex affine carrier). This is the OPEN premise
(§3b): it is **not** inhabited here — an inhabitant needs a ring hosting `√−1` with a genuine
involution *and* the branching-derived `fs, s` making the reading hold; constructing one to
hit `rStar = 1.585` would be the forbidden fit. -/
structure ModulusReadingHypothesis (K : Type*) [CommRing K] where
  σ : K →+* K
  fs : K
  s : K
  E : K
  rStar : K
  bar_even_fs : σ fs = fs
  bar_even_s : σ s = s
  carrier_barOdd : σ E = -E
  carrier_unitModulus : E * σ E = 1
  physical_modulus : rStar ^ 2 = (fs - s * E) * σ (fs - s * E)

/-- **Conditional derivation (sorry-free).** *Given* the modulus-reading hypothesis, the A=3
magnitude is the Pythagorean quadrature of the (derived, bar-even) self-adjoint reduction and
the transverse slope: `r*² = fs² + s²`. No instance of the hypothesis is constructed — the
modulus reading and the `|χ| = 1` input are the open premises (beans `qou-wiub`/`qou-wgnx`),
so this is a genuine *conditional* result, never a closure. -/
theorem modulusReading_gives_pythagorean {K : Type*} [CommRing K]
    (H : ModulusReadingHypothesis K) : H.rStar ^ 2 = H.fs ^ 2 + H.s ^ 2 := by
  rw [H.physical_modulus]
  exact barOdd_carrier_quadrature H.σ H.bar_even_fs H.bar_even_s
    H.carrier_barOdd H.carrier_unitModulus

end QOU.QBeta.BirkhoffBarOddPythagorasBridge
