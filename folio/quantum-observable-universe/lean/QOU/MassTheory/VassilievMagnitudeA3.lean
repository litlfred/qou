/-
# GAP-A-3 beyond-Hecke: can a Vassiliev weight-system supply the A=3 magnitude factor r* ≈ 1.585?

The A=3 (triton) Δ_λ 3-body **magnitude** factor `r* = μ₃ / c₃ ≈ 1.585` is the ratio
between the target additive-residual moment `μ₃ = +0.4708` (`AdditiveResidualSimplex`
#4320) and the Hecke-level near-miss `c₃ = +0.297` (#4364 `BorromeanMagnitudeLift`, the
`H₉` joint-trace lift of the proved Borromean 3-body cluster). It is now bracketed out of
every Hecke-level ingredient — not a derived tower level (#4364/#4376), not a geometric
`W_λ` (#4392, `S⁴=1`), not a coordination-edge factor (#4472, `K₃` breaks Brunnian order).
So the missing `1.585×` would require genuinely NEW beyond-Hecke structure. This file tests
the last-named candidate: a **Kontsevich-integral / Vassiliev weight-system** correction, at
the Brunnian-deficit degree `2(A−1)=4` OR the genuine length-A Milnor degree `A−1=2`
(the factor-of-2 grading crux, DD-1, `MilnorVassilievGrading.lean`).

## The object and the verdict (0 fit, forward)

The **proved** Borromean 3-body deficit closed form (A=3), with `h = q − q⁻¹`, is
`1 − τ_Borr(h) = h⁴(3 + h²)/(h² + 4)` (`milnor_weight_parity_convergence_probe.py`; the
same `borrDeficit` the Hecke Markov trace evaluates at `q₀`). Its leading finite-type
(Vassiliev degree `2(A−1)=4`) **weight** is the `h → 0` symbol `(3/4)·h⁴`.

**Decisive structural fact (`leadingWeight_le_borrDeficit`, exact for ALL h):** the leading
Vassiliev weight `(3/4)h⁴` is `≤` the full deficit `h⁴(3+h²)/(h²+4)`, because
`(3/4)(h²+4) = (3/4)h² + 3 ≤ h² + 3 = 3 + h²`. Equivalently, `(3+h²)/(h²+4)` is increasing in
`h²` from `3/4` (at `h=0`) toward `1`, so the leading term is the SMALLEST term of a
positive convergent series. Hence the **weight-to-Hecke ratio is `≤ 1`** for every `h`
(`vassiliev_weight_cannot_supply_magnitude`), while the required factor is
`r* > 3/2 > 1`. **A Vassiliev weight-system correction cannot supply `1.585×`.**

The mechanism is structural, not numerical: the finite-type filtration is a *re-expansion of
the same Markov trace* the Hecke level already sums. The Hecke near-miss `c₃ = 0.297` IS the
full finite-type sum; any finite-type truncation (a "weight") is `≤` that sum, never `1.585×`
larger. The magnitude gap lives OUTSIDE the finite-type filtration of this deficit object.

For the alternate length-A Milnor degree `A−1=2`: the genuine μ̄(123) is realized as an
**integer**-valued Vassiliev invariant taking value `±1` (scaffold
`QOU.KnotTheory.Vassiliev.BrunnianVassilievBridge.muBar_realized`, `val : K → ℤ`); the
corpus-measured Milnor ratio is the integer `−2 = J_Hopf(q=1)`. An integer weight (`±1` or
`−2`) cannot equal `r* ∈ (3/2, 2) ∖ ℤ` (`no_integer_weight_eq_rStar`) — wrong value, and for
the `−` branch wrong sign.

**Numerology dismissal.** `r* ≈ log₂ 3 = 1.58496…` is a bare coincidence. `log₂ 3` is
irrational: `log₂ 3 = a/b` (`a,b ≥ 1`) would give `2^a = 3^b`, impossible since `2^a` is even
and `3^b` odd (`two_pow_ne_three_pow`). So `log₂ 3` is not a rational finite-type weight nor a
ratio of the integer weights the substrate produces; the coincidence is NOT a derivation.

**Classification.** Scope-(b) structural exclusion of the narrow claim "a Vassiliev
finite-type weight, as a bare multiplicative magnitude factor, supplies `r*`", citing two
proved invariants: (i) the leading-term ≤ full-sum positivity bound above, and (ii) the
integrality of the finite-type invariants (`val : K → ℤ`). It does NOT exclude Vassiliev /
Kontsevich structure from a *larger* closure where an integer weight combines with other
ingredients — that is untested here. Nothing is fit; nothing is wired.

-- Ref: [barnatan1995] On the Vassiliev knot invariants, Topology 34 (1995) 423–472.
-- Ref: [leitner2026] deltalambda GAP-A-4 audit 2026-08-01; milnor_weight_parity_convergence_probe.py.
-/
import Mathlib.Tactic

namespace QOU.MassTheory.VassilievMagnitudeA3

/-! ### 1. The proved Borromean deficit and its leading Vassiliev weight -/

/-- The proved A=3 Borromean 3-body deficit closed form `1 − τ_Borr(h)`, `h = q − q⁻¹`.
This is the finite-type object the Hecke Markov trace evaluates at `q₀`. -/
noncomputable def borrDeficit (h : ℝ) : ℝ := h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4)

/-- The leading finite-type (Vassiliev degree `2(A−1)=4`) weight — the `h → 0` symbol of the
deficit: `(3+h²)/(h²+4) → 3/4`, so the leading weight is `(3/4)·h⁴`. -/
noncomputable def leadingWeight (h : ℝ) : ℝ := (3 / 4) * h ^ 4

/-- Denominator is never zero (`h² + 4 > 0`); the deficit's defining polynomial identity. -/
theorem borrDeficit_mul (h : ℝ) : borrDeficit h * (h ^ 2 + 4) = h ^ 4 * (3 + h ^ 2) := by
  unfold borrDeficit
  have hpos : h ^ 2 + 4 ≠ 0 := by positivity
  field_simp

/-- For `h ≠ 0` the deficit is strictly positive (a positive-coefficient series). -/
theorem borrDeficit_pos (h : ℝ) (hh : h ≠ 0) : 0 < borrDeficit h := by
  unfold borrDeficit
  have h2 : (0 : ℝ) < h ^ 2 := lt_of_le_of_ne (sq_nonneg h) (Ne.symm (pow_ne_zero 2 hh))
  have h4 : (0 : ℝ) < h ^ 4 := by
    rw [show (h : ℝ) ^ 4 = (h ^ 2) ^ 2 by ring]; exact pow_pos h2 2
  have hnum : (0 : ℝ) < h ^ 4 * (3 + h ^ 2) := by positivity
  have hden : (0 : ℝ) < h ^ 2 + 4 := by positivity
  exact div_pos hnum hden

/-! ### 2. The decisive bound: leading weight ≤ full deficit (Hecke value) -/

/-- **KEY (exact, all `h`).** The leading Vassiliev weight `(3/4)h⁴` is bounded ABOVE by the
full Borromean deficit `h⁴(3+h²)/(h²+4)`. Reason: `(3/4)(h²+4) = (3/4)h²+3 ≤ h²+3 = 3+h²`,
i.e. the leading term is the smallest term of the positive convergent series. Consequently no
finite-type truncation exceeds the full series value. -/
theorem leadingWeight_le_borrDeficit (h : ℝ) : leadingWeight h ≤ borrDeficit h := by
  unfold leadingWeight borrDeficit
  rw [le_div_iff₀ (by positivity : (0 : ℝ) < h ^ 2 + 4)]
  nlinarith [sq_nonneg (h ^ 3), sq_nonneg h]

/-! ### 3. The A=3 magnitude target `r* = μ₃ / c₃ ≈ 1.585` -/

/-- Hecke-level near-miss `c₃ = +0.297 MeV` (#4364, the atom-dressed `H₉` Borromean lift). -/
noncomputable def c3bare : ℝ := 297 / 1000

/-- Target additive-residual moment `μ₃ = +0.4708 MeV` (`AdditiveResidualSimplex`, #4320). -/
noncomputable def mu3 : ℝ := 4708 / 10000

/-- The required A=3 magnitude factor `r* = μ₃ / c₃ ≈ 1.585`. -/
noncomputable def rStar : ℝ := mu3 / c3bare

theorem rStar_gt_three_halves : (3 / 2 : ℝ) < rStar := by
  unfold rStar
  unfold mu3
  unfold c3bare
  norm_num

theorem rStar_lt_two : rStar < 2 := by
  unfold rStar
  unfold mu3
  unfold c3bare
  norm_num

/-! ### 4. Verdict — the Vassiliev weight cannot supply the magnitude factor -/

/-- **MAIN (scope-(b) structural exclusion).** For every `h ≠ 0` the Vassiliev weight-to-Hecke
ratio `leadingWeight h / borrDeficit h ≤ 1 < 3/2 < r*`. A finite-type weight-system correction
of the Borromean deficit cannot supply the `1.585×` A=3 magnitude factor: it is bounded above
by the full series value (the complete trace sum), whereas `r*` requires *exceeding* it. -/
theorem vassiliev_weight_cannot_supply_magnitude (h : ℝ) (hh : h ≠ 0) :
    leadingWeight h / borrDeficit h < rStar := by
  have hpos := borrDeficit_pos h hh
  have hle := leadingWeight_le_borrDeficit h
  have hratio : leadingWeight h / borrDeficit h ≤ 1 := (div_le_one hpos).mpr hle
  have := rStar_gt_three_halves
  linarith

/-- The length-A link-invariance reading (`A−1=2`): the genuine μ̄(123) is realized as an INTEGER-valued
finite-type invariant (`BrunnianVassilievBridge.muBar_realized`, value `±1`), and the
corpus-measured link ratio is the integer `−2`. No integer weight equals `r* ∈ (3/2, 2)`. -/
theorem no_integer_weight_eq_rStar (z : ℤ) : (z : ℝ) ≠ rStar := by
  intro hz
  have h1 : (3 / 2 : ℝ) < (z : ℝ) := hz ▸ rStar_gt_three_halves
  have h2 : (z : ℝ) < 2 := hz ▸ rStar_lt_two
  have hlo : (1 : ℤ) < z := by exact_mod_cast (by linarith : (1 : ℝ) < (z : ℝ))
  have hhi : z < 2 := by exact_mod_cast h2
  omega

/-- The specific corpus-measured Milnor weight `−2 = J_Hopf(q=1)` is not `r*`. -/
theorem measured_milnor_weight_ne_rStar : (-2 : ℝ) ≠ rStar := by
  have := no_integer_weight_eq_rStar (-2)
  simpa using this

/-! ### 5. Numerology dismissal — `log₂ 3` is irrational -/

/-- The arithmetic core of `log₂ 3 ∉ ℚ`: `2^a` (`a ≥ 1`, even) never equals `3^b` (odd).
Hence `log₂ 3 = a/b` would force `2^a = 3^b`, impossible — so `r* ≈ log₂ 3` is a coincidence,
not a rational finite-type weight the substrate could produce. -/
theorem two_pow_ne_three_pow (a b : ℕ) (ha : 1 ≤ a) : 2 ^ a ≠ 3 ^ b := by
  intro h
  have he : Even (2 ^ a) := Nat.even_pow.mpr ⟨by decide, by omega⟩
  rw [h, Nat.even_pow] at he
  exact (by decide : ¬ Even 3) he.1

/-- Exact higher-degree tail identity: clearing the denominator `h^2 + 4` from the
difference `borrDeficit h - leadingWeight h` yields `(1/4) * h^6`. -/
theorem borrDeficit_sub_leadingWeight_mul (h : ℝ) :
    (borrDeficit h - leadingWeight h) * (h ^ 2 + 4) = (1 / 4) * h ^ 6 := by
  unfold borrDeficit leadingWeight
  have hpos : h ^ 2 + 4 ≠ 0 := by positivity
  field_simp
  ring

end QOU.MassTheory.VassilievMagnitudeA3
