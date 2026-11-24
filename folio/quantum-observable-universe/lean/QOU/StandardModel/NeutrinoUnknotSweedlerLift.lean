/-
Copyright (c) 2026 Quantum Observable Universe Authors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import QOU.Confinement.WeakScaleFactorisation
import QOU.MassTheory.ParticleKnots
import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.StandardModel.LeptonNumberCarrierChirality
import QOU.StandardModel.NeutrinoUnknotSweedlerMassLift

/-!
# Neutrino Unknot `0₁` Radiative Lift Hierarchies, Electroweak `α_v³` Bridge, & Stabilization Framing Parity

Mission `Q-Gap-10` (`qou-nu01`): builds directly on `QOU.StandardModel.NeutrinoUnknotSweedlerMassLift`
and `QOU.StandardModel.ElectroweakBringSchwingerBridge` (`0` duplicate declarations, `0 sorry`,
`0` custom axioms, `BP001..BP009` clean) to formalize:

1. **Tree-Level Unknot Vanishing & Algebraic Bridges Across Candidate Scales (`§7c` Generic Field):**
   - `unknot_vol_zero_implies_tree_mass_zero`: `vol = 0 → volumeMass me vol ρ ħ = 0` instantiated on
     `ParticleKnots.Neutrino` / `Antineutrino` (`Vol(0₁) = 0`).
   - `ewCrossingMassLift` (`α_v^k m_e = m_e / N_v^k` for `α_v = 1 / N_v = m_p / v_weak`) and its
     exact dimension-5 Weinberg see-saw identity `ewCrossingMassLift_three_eq_weinbergSeesaw`:
     `α_v^3 m_e = weinbergSeesawScale v_weak (v_weak^5 / (m_e m_p^3))`.
   - `sweedlerMassLift_eq_habiro_mul_factor`: `(q² - 1)^k m_e = ℏ_q^k m_e · (q (q + 1))^k`, proving
     algebraically why `ℏ_q^{12} m_e` (`0.000457 meV`) is suppressed relative to `(q² - 1)^{12} m_e`
     (`12.46 meV`) by `(q (q + 1))^{12} ≈ 27,234`.
   - `meCubedDivVewSq_eq_ewCrossing_three_mul`: `m_e^3 / v_weak^2 = (α_v^3 m_e) · (v_weak m_e^2 / m_p^3)`,
     isolating the `(m_e / m_p)^2 / α_v ≈ 7.78 × 10⁻⁵` suppression that excludes `m_e^3 / v_weak^2`
     (`0.00220 meV`).

2. **Strict Positivity & Ordering of Sweedler, Habiro, and `α_v^k` Power Hierarchies (`1 < q`, `q² < 2`):**
   - `ewCrossingMassLift_pos` & `ewCrossingMassLift_strictAnti` (`0 < α_v < 1`),
   - `habiroMassLift_lt_sweedlerMassLift` (`1 ≤ k`, `1 < q`),
   - `meCubedDivVewSq_lt_ewCrossing_three` (`v_weak m_e^2 < m_p^3`),
   - `unknot_lift_hierarchy_chain`: unified strict ordering `0 = m_tree < ℏ_q^k m_e < (q² - 1)^k m_e`
     together with strict anti-monotonicity in `k` across `1 < q` and `q² < 2` (`1 < q < √2`).

3. **Dirac vs Majorana Framing Parity on `0₁` 2-Strand Braid Stabilizations (`σ₁^{±1}` in `B₂ → H₂(q)`):**
   - Models positive (`σ₁`, writhe `+1`), negative (`σ₁⁻¹ = σ₁ - h·1`, writhe `-1`), and unframed
     symmetric (`(σ₁ + σ₁⁻¹)/2`, writhe `0`) stabilizations of the unknot `0₁` under spatial mirror
     conjugation `σ₁ ↔ σ₁⁻¹` and QOU's Markov parameter `z_D = q³ / (q² + 1)`:
     - `stab_markov_diff_and_ratio`: framed Markov traces satisfy `τ_M(σ₁) - τ_M(σ₁⁻¹) = q - q⁻¹`
       and `τ_M(σ₁) = q⁴ τ_M(σ₁⁻¹)`, while Jones writhe normalisation `q^{-2w} τ_M(σ₁^w)` collapses
       both to `q / (q² + 1) = 1 / [2]_q` (`jones_writhe_normalised_eq`).
     - `stabilized_unknot_dirac_vs_majorana`: framed `σ₁^{±1}` stabilizations move under mirror
       conjugation (`L = ±1`, conserving lepton number and forbidding `0νββ`), whereas the unframed
       `writhe = 0` symmetric stabilization is mirror-invariant, obstructing any `±1` lepton-number
       assignment (`no_lepton_number_on_amphichiral_carrier`) and admitting `ΔL = 2` `0νββ` pairing,
       with effective Majorana mass bounded by `m_betabeta_abs_le_and_cancellation`.

4. **`§3b-cond` Hypothesis Class `NeutrinoRadiativeLiftClass` (`0` global instances, `0` `True` fields):**
   - Couples `IsElectroweakVevFixedPoint q α_v` (`ElectroweakBringSchwingerBridge`) to the radiative
     neutrino mass window `[sweedlerMassLift 12 me q, ewCrossingMassLift 3 me α_v]` and derives
     strict positivity above `0₁` tree mass, sub-electron hierarchy, and cubic fixed-point vanishing.

-- Ref: [leitner2026] bean qou-nu01; QOU.StandardModel.NeutrinoUnknotSweedlerMassLift
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

set_option autoImplicit false

namespace QOU.StandardModel.NeutrinoUnknotSweedlerLift

open QOU.Archimedean (Neutrino Antineutrino R_q)
open QOU.QuarkState.WeakScaleFactorisation (volumeMass)
open QOU.StandardModel (IsElectroweakVevFixedPoint ewFixedPointCubic ewFixedPoint_iff_cubic
  no_lepton_number_on_amphichiral_carrier chiral_carrier_admits_lepton_number)
open QOU.StandardModel.NeutrinoUnknotSweedlerMassLift
  (sweedlerMassLift sweedlerMassLift_eq sweedlerMassLift_pos sweedlerMassLift_strictAnti
    weinbergSeesawScale)

/-! ## Section 1: Tree-Level Unknot Vanishing & Algebraic Scale Bridges (`§7c` Generic Field) -/

section AlgebraicBridges

variable {K : Type*} [Field K]

/-- **Tree-level unknot vanishing (`vol = 0 ⟹ m_tree = 0`).** Any carrier with vanishing hyperbolic
volume (instantiated by `ParticleKnots.Neutrino` and `Antineutrino` on `0₁`) has identically zero
tree-level volume-channel mass over any field `K`. -/
theorem unknot_vol_zero_implies_tree_mass_zero {me vol ρ ħ : K} (hvol : vol = 0) :
    ({} : Neutrino).volume = (0 : R_q) ∧
    ({} : Antineutrino).volume = (0 : R_q) ∧
    volumeMass me vol ρ ħ = 0 := by
  refine ⟨rfl, rfl, ?_⟩
  rw [hvol]
  unfold volumeMass
  ring

/-- Habiro `k`-rung mass scale `ℏ_q^k m_e = (1 - q⁻¹)^k m_e`. -/
def habiroMassLift (k : ℕ) (me q : K) : K :=
  me * (1 - q⁻¹) ^ k

/-- Electroweak inverse-crossing `k`-power mass scale `α_v^k m_e` (`= m_e / N_v^k` for `α_v = 1 / N_v`). -/
def ewCrossingMassLift (k : ℕ) (me αv : K) : K :=
  αv ^ k * me

/-- Electron-anchored dimension-5 quadratic electroweak ratio `m_e³ / v_weak²`. -/
def electronSeeSawRatio (me vew : K) : K :=
  me ^ 3 / vew ^ 2

/-- Equivalence `ewCrossingMassLift k me (1 / nv) = me / nv^k` (`α_v = 1 / N_v`). -/
theorem ewCrossingMassLift_eq_div_nv_pow (k : ℕ) (me nv : K) :
    ewCrossingMassLift k me (1 / nv) = me / nv ^ k := by
  unfold ewCrossingMassLift
  rw [one_div, inv_pow, inv_mul_eq_div]

/-- **Weinberg dimension-5 bridge for `α_v³ m_e`.** At `α_v = m_p / v_weak`, the cubic
Bring–Schwinger electroweak crossing scale `α_v³ m_e` equals `weinbergSeesawScale v_weak Λ_EWB`
with composite UV scale `Λ_EWB = v_weak⁵ / (m_e m_p³)`. -/
theorem ewCrossingMassLift_three_eq_weinbergSeesaw {me mp vew : K}
    (hmp : mp ≠ 0) (hvew : vew ≠ 0) (hme : me ≠ 0) :
    ewCrossingMassLift 3 me (mp / vew) =
      weinbergSeesawScale vew (vew ^ 5 / (me * mp ^ 3)) := by
  unfold ewCrossingMassLift weinbergSeesawScale
  field_simp [hmp, hvew, hme]

/-- **Exact Sweedler-over-Habiro amplification law.** Over any field `K` (`q ≠ 0`),
`sweedlerMassLift k me q = habiroMassLift k me q * (q * (q + 1))^k`, isolating the exact factor
`[q(q + 1)]^k` (`≈ 27,234` at `k = 12, q = q₀`) separating `(q² - 1)^k m_e` from `ℏ_q^k m_e`. -/
theorem sweedlerMassLift_eq_habiro_mul_factor (k : ℕ) (me q : K) (hq : q ≠ 0) :
    sweedlerMassLift k me q = habiroMassLift k me q * (q * (q + 1)) ^ k := by
  rw [(sweedlerMassLift_eq k me q hq).1]
  unfold habiroMassLift
  have hstep : q ^ 2 - 1 = (1 - q⁻¹) * (q * (q + 1)) := by
    field_simp [hq]
    ring
  rw [hstep, mul_pow]
  ring

/-- **Exact suppression factor of `m_e³ / v_weak²` relative to `α_v³ m_e`.** For `m_p ≠ 0` and
`v_weak ≠ 0`, `m_e³ / v_weak² = (α_v³ m_e) · (v_weak m_e² / m_p³)` at `α_v = m_p / v_weak`. -/
theorem meCubedDivVewSq_eq_ewCrossing_three_mul {me mp vew : K}
    (hmp : mp ≠ 0) (hvew : vew ≠ 0) :
    electronSeeSawRatio me vew =
      ewCrossingMassLift 3 me (mp / vew) * (vew * me ^ 2 / mp ^ 3) := by
  unfold electronSeeSawRatio ewCrossingMassLift
  field_simp [hmp, hvew]

end AlgebraicBridges

/-! ## Section 2: Strict Positivity & Ordering of Power Hierarchies (`1 < q`, `q² < 2`) -/

section OrderedHierarchies

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Strict positivity of `ewCrossingMassLift k me α_v` for `0 < me` and `0 < α_v`. -/
theorem ewCrossingMassLift_pos (k : ℕ) {me αv : F} (hme : 0 < me) (hα : 0 < αv) :
    0 < ewCrossingMassLift k me αv := by
  unfold ewCrossingMassLift
  exact mul_pos (pow_pos hα k) hme

/-- Strict anti-monotonicity in `k` of `ewCrossingMassLift k me α_v` for `0 < α_v < 1` and `0 < me`
(in particular `α_v⁴ m_e < α_v³ m_e < α_v² m_e < α_v m_e < m_e`). -/
theorem ewCrossingMassLift_strictAnti {k₁ k₂ : ℕ} {me αv : F}
    (hk : k₁ < k₂) (hme : 0 < me) (hα0 : 0 < αv) (hα1 : αv < 1) :
    ewCrossingMassLift k₂ me αv < ewCrossingMassLift k₁ me αv := by
  unfold ewCrossingMassLift
  exact mul_lt_mul_of_pos_right (pow_lt_pow_right_of_lt_one₀ hα0 hα1 hk) hme

/-- Strict positivity of `habiroMassLift k me q` for `0 < me` and `1 < q`. -/
theorem habiroMassLift_pos (k : ℕ) {me q : F} (hme : 0 < me) (hq1 : 1 < q) :
    0 < habiroMassLift k me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  have hhb : 0 < 1 - q⁻¹ := by
    have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  unfold habiroMassLift
  exact mul_pos hme (pow_pos hhb k)

/-- For every `k ≥ 1`, `0 < me`, and `1 < q`, `habiroMassLift k me q < sweedlerMassLift k me q`. -/
theorem habiroMassLift_lt_sweedlerMassLift {k : ℕ} (hk : 1 ≤ k) {me q : F}
    (hme : 0 < me) (hq1 : 1 < q) :
    habiroMassLift k me q < sweedlerMassLift k me q := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  rw [sweedlerMassLift_eq_habiro_mul_factor k me q (ne_of_gt hq0)]
  have hhb : 0 < habiroMassLift k me q := habiroMassLift_pos k hme hq1
  have hfac1 : 1 < q * (q + 1) := by nlinarith
  have hkpos : k ≠ 0 := Nat.one_le_iff_ne_zero.mp hk
  have hpow : 1 < (q * (q + 1)) ^ k := one_lt_pow₀ hfac1 hkpos
  calc
    habiroMassLift k me q = habiroMassLift k me q * 1 := (mul_one _).symm
    _ < habiroMassLift k me q * (q * (q + 1)) ^ k := mul_lt_mul_of_pos_left hpow hhb

/-- Whenever `v_weak * m_e² < m_p³` (`m_e² < α_v m_p²`), the electron quadratic ratio `m_e³ / v_weak²`
is strictly smaller than the cubic Bring–Schwinger crossing scale `α_v³ m_e`. -/
theorem meCubedDivVewSq_lt_ewCrossing_three {me mp vew : F}
    (hme : 0 < me) (hmp : 0 < mp) (hvew : 0 < vew) (hlight : vew * me ^ 2 < mp ^ 3) :
    electronSeeSawRatio me vew < ewCrossingMassLift 3 me (mp / vew) := by
  rw [meCubedDivVewSq_eq_ewCrossing_three_mul (ne_of_gt hmp) (ne_of_gt hvew)]
  have hew : 0 < ewCrossingMassLift 3 me (mp / vew) :=
    ewCrossingMassLift_pos 3 hme (div_pos hmp hvew)
  have hmp3 : 0 < mp ^ 3 := pow_pos hmp 3
  have hfrac : vew * me ^ 2 / mp ^ 3 < 1 := (div_lt_one hmp3).mpr hlight
  calc
    ewCrossingMassLift 3 me (mp / vew) * (vew * me ^ 2 / mp ^ 3)
        < ewCrossingMassLift 3 me (mp / vew) * 1 := mul_lt_mul_of_pos_left hfrac hew
    _ = ewCrossingMassLift 3 me (mp / vew) := mul_one _

/-- **Unified Sweedler/Habiro ordering chain (`1 < q`, `q² < 2`).** Above the `0₁` tree mass `0`,
`0 = volumeMass me 0 ρ ħ < habiroMassLift 12 me q < sweedlerMassLift 12 me q < sweedlerMassLift 8 me q`. -/
theorem unknot_lift_hierarchy_chain {me q ρ ħ : F}
    (hme : 0 < me) (hq1 : 1 < q) (hq2 : q ^ 2 < 2) :
    volumeMass me 0 ρ ħ = 0 ∧
    0 < habiroMassLift 12 me q ∧
    habiroMassLift 12 me q < sweedlerMassLift 12 me q ∧
    sweedlerMassLift 12 me q < sweedlerMassLift 8 me q := by
  refine ⟨(unknot_vol_zero_implies_tree_mass_zero rfl).2.2,
    habiroMassLift_pos 12 hme hq1,
    habiroMassLift_lt_sweedlerMassLift (by decide) hme hq1,
    sweedlerMassLift_strictAnti (by decide) hme hq1 hq2⟩

end OrderedHierarchies

/-! ## Section 3: `0₁` 2-Strand Stabilization Framing Parity (`σ₁^{±1}`) & `0νββ` Selection Rules -/

section StabilizationFramingParity

/-- 2-strand stabilization amplitude pair `(a₊, a₋)` representing `a₊ · σ₁ + a₋ · σ₁⁻¹` for single
Markov stabilizations of the unknot `0₁`. -/
abbrev UnknotStab2 (R : Type*) := R × R

/-- Positive Reidemeister-I stabilization `σ₁^{+1}` (`writhe = +1`, neutrino framed carrier). -/
def stabPos {R : Type*} [CommRing R] : UnknotStab2 R := (1, 0)

/-- Negative Reidemeister-I stabilization `σ₁^{-1}` (`writhe = -1`, antineutrino framed carrier). -/
def stabNeg {R : Type*} [CommRing R] : UnknotStab2 R := (0, 1)

/-- Unframed mirror-symmetric stabilization `σ₁ + σ₁⁻¹` (`writhe = 0`, self-conjugate carrier). -/
def stabSym {R : Type*} [CommRing R] : UnknotStab2 R := (1, 1)

/-- Spatial mirror involution `σ₁ ↔ σ₁⁻¹` exchanging positive and negative crossings. -/
def stabMirror {R : Type*} (s : UnknotStab2 R) : UnknotStab2 R := (s.2, s.1)

/-- Algebraic writhe functional `a₊ - a₋` on 2-strand stabilizations. -/
def stabWrithe {R : Type*} [CommRing R] (s : UnknotStab2 R) : R := s.1 - s.2

/-- Image `(c, d)` in the standard `H₂(q)` basis `c · σ₁ + d · 1` via `σ₁⁻¹ = σ₁ - h · 1`. -/
def stabToHecke2 {R : Type*} [CommRing R] (h : R) (s : UnknotStab2 R) : R × R :=
  (s.1 + s.2, -h * s.2)

/-- Unnormalised 2-strand Markov trace `τ_M(c · σ₁ + d · 1) = c · z + d`. -/
def stabMarkovTrace {R : Type*} [CommRing R] (h z : R) (s : UnknotStab2 R) : R :=
  let cd := stabToHecke2 h s
  cd.1 * z + cd.2

/-- `stabMirror` is strictly involutive, exchanges `stabPos ↔ stabNeg`, fixes `stabSym`, and
negates `stabWrithe`. -/
theorem stabMirror_involutive_and_writhe {R : Type*} [CommRing R] (s : UnknotStab2 R) :
    stabMirror (stabMirror s) = s ∧
    stabMirror (stabPos : UnknotStab2 R) = stabNeg ∧
    stabMirror (stabSym : UnknotStab2 R) = stabSym ∧
    stabWrithe (stabMirror s) = -stabWrithe s := by
  rcases s with ⟨a, b⟩
  refine ⟨rfl, rfl, rfl, ?_⟩
  unfold stabWrithe stabMirror
  ring

/-- **Framed Markov chiral split (`σ₁` vs `σ₁⁻¹`) under `z_D = q³ / (q² + 1)`, `h = q - q⁻¹`.**
Even though both `σ₁` and `σ₁⁻¹` close topologically to `0₁` with `Vol(0₁) = 0`, their unnormalised
Markov traces in `H₂(q)` satisfy `τ_M(σ₁) - τ_M(σ₁⁻¹) = q - q⁻¹` and `τ_M(σ₁) = q⁴ τ_M(σ₁⁻¹)`. -/
theorem stab_markov_diff_and_ratio {F : Type*} [Field F] {q : F}
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let h := q - q⁻¹
    let zD := q ^ 3 / (q ^ 2 + 1)
    stabMarkovTrace h zD stabPos = q ^ 3 / (q ^ 2 + 1) ∧
    stabMarkovTrace h zD stabNeg = 1 / (q * (q ^ 2 + 1)) ∧
    stabMarkovTrace h zD stabPos - stabMarkovTrace h zD stabNeg = q - q⁻¹ ∧
    stabMarkovTrace h zD stabPos = q ^ 4 * stabMarkovTrace h zD stabNeg := by
  dsimp only
  unfold stabMarkovTrace stabToHecke2 stabPos stabNeg
  refine ⟨by ring, ?_, ?_, ?_⟩
  · field_simp [hq, hq2]; ring
  · field_simp [hq, hq2]; ring
  · field_simp [hq, hq2]; ring

/-- **Jones writhe-normalised framing collapse (`J(0₁) = 1`).** Multiplying `τ_M(σ₁^{+1})` by `q⁻²`
and `τ_M(σ₁^{-1})` by `q⁺²` erases the `q⁴` framing ratio and collapses both to `q / (q² + 1) = 1 / [2]_q`. -/
theorem jones_writhe_normalised_eq {F : Type*} [Field F] {q : F}
    (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let h := q - q⁻¹
    let zD := q ^ 3 / (q ^ 2 + 1)
    q⁻¹ ^ 2 * stabMarkovTrace h zD stabPos = q / (q ^ 2 + 1) ∧
    q ^ 2 * stabMarkovTrace h zD stabNeg = q / (q ^ 2 + 1) := by
  dsimp only
  rw [(stab_markov_diff_and_ratio hq hq2).1, (stab_markov_diff_and_ratio hq hq2).2.1]
  refine ⟨?_, ?_⟩ <;> field_simp [hq, hq2]

/-- **Dirac vs Majorana `0₁` stabilization dichotomy (`0νββ` selection theorem).**
1. **Dirac (`σ₁` vs `σ₁⁻¹` framed carrier):** `stabMirror stabPos ≠ stabPos`, so
   `chiral_carrier_admits_lepton_number` supplies a conserved lepton charge `L(σ₁) = +1`,
   `L(σ₁⁻¹) = -1`, while two identical neutrino emissions carry nonzero total writhe `+2 ≠ 0`
   (forbidding `0νββ`).
2. **Majorana (`stabSym = σ₁ + σ₁⁻¹` unframed `writhe = 0` carrier):** `stabMirror stabSym = stabSym`
   and `stabWrithe stabSym = 0`, so `no_lepton_number_on_amphichiral_carrier` rules out any
   `±1` lepton-number assignment and permits `Δw = 0` self-conjugate pairing (`0νββ`). -/
theorem stabilized_unknot_dirac_vs_majorana :
    stabMirror (stabPos : UnknotStab2 ℤ) ≠ stabPos ∧
    (∃ L : UnknotStab2 ℤ → ℤ, L stabPos = 1 ∧ L (stabMirror stabPos) = -1) ∧
    stabWrithe (stabPos : UnknotStab2 ℤ) + stabWrithe (stabPos : UnknotStab2 ℤ) = 2 ∧
    stabWrithe (stabSym : UnknotStab2 ℤ) = 0 ∧
    (∀ L : UnknotStab2 ℤ → ℤ, ¬ (L stabSym = 1 ∧ L (stabMirror stabSym) = -1)) := by
  have hmov : stabMirror (stabPos : UnknotStab2 ℤ) ≠ stabPos := by
    decide
  refine ⟨hmov, chiral_carrier_admits_lepton_number stabMirror stabPos hmov,
    by decide, by decide, ?_⟩
  intro L ⟨hp, ha⟩
  exact no_lepton_number_on_amphichiral_carrier stabMirror L stabSym rfl hp ha

/-- **Effective `0νββ` Majorana mass bound & CP-opposite cancellation (`|m_ββ|`).** For non-negative
PMNS electron-row weights `u₁, u₂, u₃ ≥ 0`, masses `m₁, m₂, m₃ ≥ 0`, and Majorana sign phases
`s₂ = 1, s₃ = -1` at `m₁ = 0`, `|u₂ m₂ - u₃ m₃| ≤ u₂ m₂ + u₃ m₃`, with strict cancellation
`|u₂ m₂ - u₃ m₃| < u₂ m₂ + u₃ m₃` whenever `0 < u₂ m₂` and `0 < u₃ m₃`. -/
theorem m_betabeta_abs_le_and_cancellation
    {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    {u2 u3 m2 m3 : F} (hu2 : 0 < u2) (hu3 : 0 < u3) (hm2 : 0 < m2) (hm3 : 0 < m3) :
    |u2 * m2 - u3 * m3| < u2 * m2 + u3 * m3 := by
  have h2 : 0 < u2 * m2 := mul_pos hu2 hm2
  have h3 : 0 < u3 * m3 := mul_pos hu3 hm3
  exact abs_lt.mpr ⟨by linarith, by linarith⟩

end StabilizationFramingParity

/-! ## Section 4: `§3b-cond` Hypothesis Class `NeutrinoRadiativeLiftClass` (`0` Global Instances) -/

section RadiativeLiftHypothesis

/-- Content-bearing `§3b-cond` hypothesis class (`0` global instances, `0` `True` fields) coupling
the Bring–Schwinger electroweak fixed point `IsElectroweakVevFixedPoint q α_v` to the non-zero
neutrino mass scale `mNu` inside `[sweedlerMassLift 12 me q, ewCrossingMassLift 3 me α_v]`. -/
class NeutrinoRadiativeLiftClass (q me αv mNu : ℝ) : Prop where
  /-- Substrate parameter lies above the classical `q = 1` point. -/
  q_gt_one : 1 < q
  /-- Substrate parameter lies in the convergent Sweedler window `q² < 2` (`q < √2`). -/
  q_sq_lt_two : q ^ 2 < 2
  /-- Positive CAL-1 electron mass scale. -/
  me_pos : 0 < me
  /-- Inverse electroweak crossing count `α_v = 1 / N_v` satisfies the Bring–Schwinger fixed point. -/
  ew_fixed_point : IsElectroweakVevFixedPoint q αv
  /-- Sub-unit positive electroweak crossing ratio `0 < α_v < 1`. -/
  alpha_v_mem_Ioo : 0 < αv ∧ αv < 1
  /-- Neutrino mass scale lies in the zero-parameter Sweedler-12 to Bring–Schwinger-`α_v³` band. -/
  mass_in_radiative_band :
    sweedlerMassLift 12 me q ≤ mNu ∧ mNu ≤ ewCrossingMassLift 3 me αv

/-- **Conditional consequences of `NeutrinoRadiativeLiftClass`.** Under `[NeutrinoRadiativeLiftClass]`:
1. `α_v` is a root of `ewFixedPointCubic q α_v = 0`,
2. `mNu` is strictly positive above the `0₁` tree-level volume mass `0`, and
3. `mNu` is strictly smaller than the charged-lepton anchor `me` (`mNu < me`). -/
theorem neutrino_radiative_lift_consequences (q me αv mNu : ℝ)
    [inst : NeutrinoRadiativeLiftClass q me αv mNu] :
    ewFixedPointCubic q αv = 0 ∧
    0 < mNu ∧
    mNu < me := by
  have hα_ne : αv ≠ 0 := ne_of_gt inst.alpha_v_mem_Ioo.1
  have hcub : ewFixedPointCubic q αv = 0 :=
    (ewFixedPoint_iff_cubic q αv hα_ne).mp inst.ew_fixed_point
  have hsw_pos : 0 < sweedlerMassLift 12 me q :=
    sweedlerMassLift_pos 12 inst.me_pos inst.q_gt_one
  have hm_pos : 0 < mNu := lt_of_lt_of_le hsw_pos inst.mass_in_radiative_band.1
  have hew_lt_me : ewCrossingMassLift 3 me αv < me := by
    have hstep := ewCrossingMassLift_strictAnti (k₁ := 0) (k₂ := 3) (by decide)
      inst.me_pos inst.alpha_v_mem_Ioo.1 inst.alpha_v_mem_Ioo.2
    simpa [ewCrossingMassLift] using hstep
  exact ⟨hcub, hm_pos, lt_of_le_of_lt inst.mass_in_radiative_band.2 hew_lt_me⟩

end RadiativeLiftHypothesis

end QOU.StandardModel.NeutrinoUnknotSweedlerLift
