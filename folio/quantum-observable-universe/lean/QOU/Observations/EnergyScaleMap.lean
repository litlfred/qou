/-
# The map from categorical energy to MeV: what CAL-1/2/3 fix and what they cannot

Workstream W6 of the L2 1-ppQ plan; beans `qou-91w7` (𝔈 → MeV) and `qou-6gf9` (the muon
carrier `m_μ = m_e · Vol(4₁)/ℏ_q²`). Owner ruling 2026-11-22: *"𝔈 is categorical energy. Needs
scaling (coming from CAL123 hopefully)"*. No fourth constant, no fitting, and no measured value
appears below: every statement is about an arbitrary real datum.

## Set-up

A **chart** at the substrate point is a unit `Λ` (MeV per categorical unit) and a categorical
weight `w X` for each object `X`; its physical value is `Λ · w X`. The three calibrations, as
the model sees them, are one dimensionful number and two dimensionless ratios:

* CAL-1: the electron value `m_e`;
* CAL-2 (proxy): the ratio `m_μ/m_e`, which defines `q₀`;
* CAL-3: the ratio `m_π/m_e`, the meson-sector scale.

## What is proved

1. **Gauge freedom** (`value_rescale`, `matches_rescale`, `calibration_does_not_fix_unit`).
   `(Λ, w) ↦ (t·Λ, w/t)` leaves every physical value unchanged. So no amount of calibration data
   fixes the split between unit and weight. In particular (`energy_chart_value`) a chart whose
   weights are categorical energies `𝔈 = 𝔪 · c` and a chart whose weights are categorical masses
   `𝔪` give the same values exactly when their units differ by the factor `c`. Whether `c_q²`
   "converts mass to energy" is invisible to CAL-1/2/3.
2. **Rigidity** (`unit_eq_of_matches`, `value_eq_electron_ratio`). Once the electron's weight is
   fixed and non-zero, CAL-1 forces `Λ = m_e / w_e`, and every prediction is
   `m_e · (w X / w e)`. The unit carries no information beyond the electron's weight.
3. **The 𝔈 → MeV map** (`energy_map_eq_mass_map`). With `𝔈 = 𝔪 · c` for one common `c ≠ 0`,
   `m_e · 𝔈_X/𝔈_e = m_e · 𝔪_X/𝔪_e`: the factor `c_q²` cancels. The map is
   `Φ(𝔈) = (m_e/𝔈_e(q₀)) · 𝔈`. Mixing an energy for `X` with a mass for the electron multiplies
   the answer by `c` (`mixed_map`); that mixing is the origin of the "−99 %" reading in
   `qou-91w7`.
4. **CAL-2 and CAL-3 fix no unit** (`ratio_unit_free`). They are ratios, unchanged by any
   change of `Λ`. Their content is about weights at `q₀`: CAL-2 fixes `q₀`, CAL-3 the meson
   weight.
5. **The muon carrier is not a ratio of braid-word traces** (`muon_carrier_not_trace_ratio`).
   For any two braid words on any numbers of strands, with any framing factors continuous and
   non-zero at `q = 1`, the ratio of convention-D state-sum traces has a finite limit as
   `q → 1⁺` (`trace_ratio_tendsto`), while `Vol/ℏ_q²` does not (for `Vol ≠ 0`). The same
   argument shows that `E₀/m_e = 1/(q(q − 1))` is not a ratio of two such traces
   (`E0_not_trace_ratio`).
6. **A rational source cannot produce `Vol(4₁)`** (`const_mem_of_poly_identity`,
   `carrier_const_mem_of_rational`). If the two weights are rational functions with
   coefficients in a subfield `K ⊆ ℝ` and their ratio is `V/ℏ_q²` on `q > 1`, then `V ∈ K`.
   Applied to `K = ℚ`: a `ℚ(q)`-valued pair can carry `Vol(4₁)` only if `Vol(4₁)` is rational,
   which is not known either way. Read: `Vol(4₁)` has to enter through an analytic input
   (e.g. a volume-conjecture limit), not through a finite Hecke trace at generic `q`.
7. **The corpus chart is the trivial instance** (`massFormula_carrier`, `massFormula_unit`).
   The mass formula `m(K) = m_e · Vol(K)·ρ(K)/ℏ_q²` is the chart with unit `m_e/ℏ_q²`,
   electron weight `ℏ_q²` and muon weight `Vol(4₁)`. Its carrier holds by definition, and at
   the CAL-2 point its unit equals `m_μ/Vol(4₁)`. So `cal2_identity_pinned` is a restatement of
   the definition of `q₀`, not a derivation, and nothing here makes it one.

## What stays open

* The electron's categorical weight in each pipeline (trace pipeline: the convention-D trace of
  `σ₀σ₁σ₀` with Hopf closure, finite and non-zero at `q = 1`; mass-formula pipeline: `ℏ_q²`,
  order 2 at `q = 1`). They are different functions, so the two pipelines use different units.
  Which is canonical is the open derivation; the calibrations cannot decide it (item 1).
* For the muon carrier: an electron-side object whose weight vanishes to order exactly 2 more
  than the muon-side object at `q = 1` (item 5), and an analytic source of `Vol(4₁)` (item 6).

**Ground ring**: `ℝ`, because the obstructions use limits at `q = 1` and a real-valued `Vol`.
Items 1–4 and 7 are field identities and would hold over any field.

Ref: [leitner2026] observations/three-calibration-discipline; bean qou-91w7; bean qou-6gf9.
-/
import QOU.QBeta.E0WeightAllWords
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

namespace QOU.Observations.EnergyScale

open Filter Topology Polynomial

/-! ## 1. Charts and gauge freedom -/

/-- A scale chart at the substrate point: a unit `Λ` and a categorical weight per object. -/
structure Chart (ι : Type*) where
  /-- MeV per categorical unit. -/
  unit : ℝ
  /-- Categorical weight of each object, evaluated at the substrate point. -/
  weight : ι → ℝ

/-- The three calibration data: the electron value (CAL-1) and the two ratios
    `m_μ/m_e` (CAL-2 proxy) and `m_π/m_e` (CAL-3). -/
structure CalData where
  me : ℝ
  muOverE : ℝ
  piOverE : ℝ

namespace Chart

variable {ι : Type*}

/-- Physical value of an object in a chart. -/
def value (c : Chart ι) (X : ι) : ℝ := c.unit * c.weight X

/-- The rescaled chart `(t·Λ, w/t)`. -/
noncomputable def rescale (c : Chart ι) (t : ℝ) : Chart ι :=
  ⟨t * c.unit, fun X => c.weight X / t⟩

/-- A chart reproduces the calibration data on the electron, the muon and the pion. -/
def Matches (c : Chart ι) (e mu pi : ι) (d : CalData) : Prop :=
  c.value e = d.me ∧ c.value mu = d.muOverE * d.me ∧ c.value pi = d.piOverE * d.me

theorem value_rescale (c : Chart ι) {t : ℝ} (ht : t ≠ 0) (X : ι) :
    (c.rescale t).value X = c.value X := by
  unfold value rescale
  field_simp

/-- **Gauge freedom.** Rescaling preserves agreement with the calibration data. -/
theorem matches_rescale (c : Chart ι) {e mu pi : ι} {d : CalData} {t : ℝ} (ht : t ≠ 0)
    (h : c.Matches e mu pi d) : (c.rescale t).Matches e mu pi d := by
  unfold Matches at *
  simp only [value_rescale c ht]
  exact h

/-- **The calibrations do not fix the unit.** Any chart with a non-zero unit that matches the
    data has a second matching chart with a different unit and the same value on every object. -/
theorem calibration_does_not_fix_unit (c : Chart ι) {e mu pi : ι} {d : CalData}
    (h : c.Matches e mu pi d) (hu : c.unit ≠ 0) :
    ∃ c' : Chart ι, c'.Matches e mu pi d ∧ c'.unit ≠ c.unit ∧ ∀ X, c'.value X = c.value X := by
  refine ⟨c.rescale 2, matches_rescale c two_ne_zero h, ?_, value_rescale c two_ne_zero⟩
  unfold rescale
  intro h2
  apply hu
  linarith

/-- **Energy chart versus mass chart.** Weights `𝔪 X · κ` with unit `Λ` give the same values as
    weights `𝔪 X` with unit `Λ · κ`. So whether the weights are categorical energies
    (`κ = c_q²`) or categorical masses is absorbed in the unit. -/
theorem energy_chart_value (Λ κ : ℝ) (m : ι → ℝ) (X : ι) :
    (⟨Λ, fun Y => m Y * κ⟩ : Chart ι).value X = (⟨Λ * κ, m⟩ : Chart ι).value X := by
  unfold value
  ring

/-! ## 2. Rigidity: the electron's weight fixes everything -/

/-- **CAL-1 fixes the unit once the electron's weight is fixed.** -/
theorem unit_eq_of_matches (c : Chart ι) {e mu pi : ι} {d : CalData}
    (h : c.Matches e mu pi d) (hw : c.weight e ≠ 0) : c.unit = d.me / c.weight e := by
  rw [← h.1]
  unfold value
  field_simp

/-- **Every prediction is `m_e` times a categorical ratio to the electron.** -/
theorem value_eq_electron_ratio (c : Chart ι) {e mu pi : ι} {d : CalData}
    (h : c.Matches e mu pi d) (hw : c.weight e ≠ 0) (X : ι) :
    c.value X = d.me * (c.weight X / c.weight e) := by
  rw [← h.1]
  unfold value
  field_simp

/-- **CAL-2 and CAL-3 fix no unit.** A ratio of two values does not depend on the unit. -/
theorem ratio_unit_free (w : ι → ℝ) {Λ Λ' : ℝ} (hΛ : Λ ≠ 0) (hΛ' : Λ' ≠ 0) (X Y : ι) :
    (⟨Λ, w⟩ : Chart ι).value X / (⟨Λ, w⟩ : Chart ι).value Y
      = (⟨Λ', w⟩ : Chart ι).value X / (⟨Λ', w⟩ : Chart ι).value Y := by
  unfold value
  by_cases hY : w Y = 0
  · simp [hY]
  · field_simp

end Chart

/-! ## 3. The 𝔈 → MeV map -/

/-- The CAL-1 map: a categorical value `x`, normalised by the electron's categorical value
    `x_e` in the same pipeline, sent to MeV. -/
noncomputable def calMap (me xe x : ℝ) : ℝ := me * (x / xe)

/-- The map sends the electron to `m_e`. -/
theorem calMap_electron (me xe : ℝ) (hxe : xe ≠ 0) : calMap me xe xe = me := by
  unfold calMap
  field_simp

/-- **`c_q²` cancels.** With `𝔈 = 𝔪 · κ` for a common `κ ≠ 0`, the energy map and the mass map
    agree: `m_e · 𝔈_X/𝔈_e = m_e · 𝔪_X/𝔪_e`. -/
theorem energy_map_eq_mass_map (me me_cat mX κ : ℝ) (hκ : κ ≠ 0) :
    calMap me (me_cat * κ) (mX * κ) = calMap me me_cat mX := by
  unfold calMap
  by_cases h : me_cat = 0
  · simp [h]
  · field_simp

/-- **Mixing multiplies by `κ`.** Sending an energy `𝔪_X · κ` through a map normalised by the
    electron's mass `𝔪_e` gives `κ` times the consistent answer. With `κ = c_q²(q₀) ≈ 82.7` read
    the other way round, this is the "−99 %" reading of bean `qou-91w7`. -/
theorem mixed_map (me me_cat mX κ : ℝ) :
    calMap me me_cat (mX * κ) = κ * calMap me me_cat mX := by
  unfold calMap
  ring

/-! ## 4. The muon carrier is not a ratio of braid-word traces -/

/-- `ℏ_q = 1 − q⁻¹` (the same definition as `QOU.QBeta.E0WeightAllWords.hbar`). -/
noncomputable abbrev hbar (q : ℝ) : ℝ := QOU.QBeta.E0WeightAllWords.hbar q

theorem hbar_ne_zero {q : ℝ} (hq : 1 < q) : hbar q ≠ 0 := by
  unfold hbar QOU.QBeta.E0WeightAllWords.hbar
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  intro h
  linarith

/-- **A ratio of two functions continuous at `1`, the denominator non-zero there, has a finite
    limit at `1⁺`.** -/
theorem ratio_tendsto (f g R : ℝ → ℝ) (hf : ContinuousAt f 1) (hg : ContinuousAt g 1)
    (hg1 : g 1 ≠ 0) (h : ∀ q : ℝ, 1 < q → f q = R q * g q) :
    Tendsto R (𝓝[>] 1) (𝓝 (f 1 / g 1)) := by
  have hfg : Tendsto (fun q => f q / g q) (𝓝[>] 1) (𝓝 (f 1 / g 1)) :=
    ((hf.div hg hg1).tendsto).mono_left nhdsWithin_le_nhds
  have hne : ∀ᶠ q in 𝓝[>] (1 : ℝ), g q ≠ 0 :=
    (hg.eventually_ne hg1).filter_mono nhdsWithin_le_nhds
  refine hfg.congr' ?_
  filter_upwards [hne, self_mem_nhdsWithin] with q hq hq1
  rw [h q hq1]
  field_simp

/-- **No function with a finite limit at `1⁺` is `(q − 1)^{-k} · u(q)` with `u → c ≠ 0`.** -/
theorem not_tendsto_of_pole (R u : ℝ → ℝ) (k : ℕ) (hk : 1 ≤ k) (c L : ℝ) (hc : c ≠ 0)
    (hu : Tendsto u (𝓝[>] 1) (𝓝 c))
    (h : ∀ q : ℝ, 1 < q → R q * (q - 1) ^ k = u q) :
    ¬ Tendsto R (𝓝[>] 1) (𝓝 L) := by
  intro hR
  have hp : Tendsto (fun q : ℝ => (q - 1) ^ k) (𝓝[>] 1) (𝓝 0) := by
    have : ContinuousAt (fun q : ℝ => (q - 1) ^ k) 1 :=
      (continuousAt_id.sub continuousAt_const).pow k
    have h0 := this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
    simpa [zero_pow (by omega : k ≠ 0)] using h0
  have hprod : Tendsto (fun q => R q * (q - 1) ^ k) (𝓝[>] 1) (𝓝 (L * 0)) := hR.mul hp
  have heq : (fun q => R q * (q - 1) ^ k) =ᶠ[𝓝[>] 1] u :=
    eventually_nhdsWithin_of_forall fun q hq => h q hq
  have := tendsto_nhds_unique (hprod.congr' heq) hu
  exact hc (by simpa using this.symm)

/-- `(V/ℏ_q²) · (q − 1)² = V q²`. -/
theorem carrier_mul_sq (V q : ℝ) (hq : 1 < q) :
    V / hbar q ^ 2 * (q - 1) ^ 2 = V * q ^ 2 := by
  have hq0 : q ≠ 0 := by positivity
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.2 (ne_of_gt hq)
  unfold hbar QOU.QBeta.E0WeightAllWords.hbar
  have : (1 : ℝ) - q⁻¹ = (q - 1) / q := by field_simp
  rw [this]
  field_simp

/-- **`Vol/ℏ_q²` has no finite limit at `1⁺`** (for `Vol ≠ 0`). -/
theorem carrier_not_tendsto (V L : ℝ) (hV : V ≠ 0) :
    ¬ Tendsto (fun q => V / hbar q ^ 2) (𝓝[>] 1) (𝓝 L) := by
  refine not_tendsto_of_pole _ (fun q => V * q ^ 2) 2 (by norm_num) V L hV ?_
    (fun q hq => carrier_mul_sq V q hq)
  have : ContinuousAt (fun q : ℝ => V * q ^ 2) 1 := continuousAt_const.mul (continuousAt_id.pow 2)
  simpa using this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))

section Traces

open QOU.QBeta.E0WeightAllWords

variable {α β : Type*} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β]

/-- **A framed trace ratio has a finite limit at `1⁺`.** For braid words `wX` (on `α`-strands)
    and `we` (on `β`-strands) and framing factors `fX`, `fe` continuous at `1` with
    `fe 1 ≠ 0`: if `fX · T_{wX} = R · fe · T_{we}` on `q > 1`, then `R` has a finite limit. -/
theorem trace_ratio_tendsto (wX : List (Letter α)) (we : List (Letter β)) (fX fe R : ℝ → ℝ)
    (hfX : ContinuousAt fX 1) (hfe : ContinuousAt fe 1) (hfe1 : fe 1 ≠ 0)
    (h : ∀ q : ℝ, 1 < q → fX q * traceD q wX = R q * (fe q * traceD q we)) :
    ∃ L, Tendsto R (𝓝[>] 1) (𝓝 L) := by
  have hT1 : traceD 1 we ≠ 0 := by
    rw [traceD_one]
    exact_mod_cast (trClassical_pos (wordPerm we)).ne'
  exact ⟨_, ratio_tendsto (fun q => fX q * traceD q wX) (fun q => fe q * traceD q we) R
    (hfX.mul (traceD_continuousAt_one wX)) (hfe.mul (traceD_continuousAt_one we))
    (mul_ne_zero hfe1 hT1) h⟩

/-- **The muon carrier is not a ratio of framed braid-word traces.** For any words `wμ`, `we`,
    any framing factors continuous at `1` (the electron's non-zero there) and any `V ≠ 0`,
    `fμ · T_{wμ} = (V/ℏ_q²) · fe · T_{we}` fails somewhere on `q > 1`. -/
theorem muon_carrier_not_trace_ratio (wmu : List (Letter α)) (we : List (Letter β))
    (fmu fe : ℝ → ℝ) (hfmu : ContinuousAt fmu 1) (hfe : ContinuousAt fe 1) (hfe1 : fe 1 ≠ 0)
    (V : ℝ) (hV : V ≠ 0) :
    ¬ ∀ q : ℝ, 1 < q → fmu q * traceD q wmu = V / hbar q ^ 2 * (fe q * traceD q we) := by
  intro h
  obtain ⟨L, hL⟩ := trace_ratio_tendsto wmu we fmu fe (fun q => V / hbar q ^ 2) hfmu hfe hfe1 h
  exact carrier_not_tendsto V L hV hL

/-- **`E₀/m_e = 1/(q(q − 1))` is not a ratio of framed braid-word traces.** -/
theorem E0_not_trace_ratio (wX : List (Letter α)) (we : List (Letter β))
    (fX fe : ℝ → ℝ) (hfX : ContinuousAt fX 1) (hfe : ContinuousAt fe 1) (hfe1 : fe 1 ≠ 0) :
    ¬ ∀ q : ℝ, 1 < q → fX q * traceD q wX = 1 / (q * (q - 1)) * (fe q * traceD q we) := by
  intro h
  obtain ⟨L, hL⟩ := trace_ratio_tendsto wX we fX fe (fun q => 1 / (q * (q - 1))) hfX hfe hfe1 h
  refine not_tendsto_of_pole (fun q => 1 / (q * (q - 1))) (fun q => 1 / q) 1 le_rfl 1 L
    one_ne_zero ?_ (fun q hq => ?_) hL
  · have : ContinuousAt (fun q : ℝ => 1 / q) 1 := continuousAt_const.div continuousAt_id one_ne_zero
    simpa using this.tendsto.mono_left (nhdsWithin_le_nhds (s := Set.Ioi (1 : ℝ)))
  · have hq0 : q ≠ 0 := by positivity
    have hq1 : q - 1 ≠ 0 := sub_ne_zero.2 (ne_of_gt hq)
    field_simp

end Traces

/-- **Order of vanishing.** If the carrier holds between two weights continuous at `1`, the
    electron-side weight vanishes at `1`. -/
theorem electron_weight_vanishes (wmu we : ℝ → ℝ) (hmu : ContinuousAt wmu 1)
    (he : ContinuousAt we 1) (V : ℝ) (hV : V ≠ 0)
    (h : ∀ q : ℝ, 1 < q → wmu q = V / hbar q ^ 2 * we q) : we 1 = 0 := by
  by_contra hne
  obtain ⟨L, hL⟩ : ∃ L, Tendsto (fun q => V / hbar q ^ 2) (𝓝[>] 1) (𝓝 L) :=
    ⟨_, ratio_tendsto wmu we _ hmu he hne h⟩
  exact carrier_not_tendsto V L hV hL

/-! ## 5. A rational source cannot produce `Vol(4₁)` -/

/-- **Coefficient field.** If `p(q) = V · r(q)` for every `q > 1`, with `p, r` polynomials over a
    subfield `K ⊆ ℝ` and `r ≠ 0`, then `V ∈ K`. -/
theorem const_mem_of_poly_identity (K : Subfield ℝ) (p r : K[X]) (hr : r ≠ 0) (V : ℝ)
    (h : ∀ q : ℝ, 1 < q → (p.map K.subtype).eval q = V * (r.map K.subtype).eval q) :
    V ∈ K := by
  set P : ℝ[X] := p.map K.subtype - C V * r.map K.subtype with hP
  have hP0 : P = 0 := by
    apply Polynomial.eq_zero_of_infinite_isRoot
    apply Set.Infinite.mono (s := Set.Ioi (1 : ℝ))
    · intro q hq
      simp only [Set.mem_setOf_eq, IsRoot, hP, eval_sub, eval_mul, eval_C]
      rw [h q hq]
      ring
    · exact Set.Ioi_infinite 1
  obtain ⟨n, hn⟩ : ∃ n, r.coeff n ≠ 0 := by
    by_contra hall
    push_neg at hall
    exact hr (Polynomial.ext fun n => by simpa using hall n)
  have hc := congrArg (fun Q : ℝ[X] => Q.coeff n) hP0
  simp only [hP, coeff_sub, coeff_C_mul, coeff_map, coeff_zero] at hc
  have hrn : (K.subtype (r.coeff n)) ≠ 0 := by
    simpa using hn
  have hV : V = K.subtype (p.coeff n / r.coeff n) := by
    rw [map_div₀]
    field_simp
    linarith
  rw [hV]
  exact (p.coeff n / r.coeff n).2

/-- **The carrier from rational weights forces `V ∈ K`.** If the muon weight is `a/b` and the
    electron weight is `c/d`, with `a, b, c, d` polynomials over `K`, `b` and `d` non-vanishing on
    `q > 1`, `c ≠ 0`, and `a/b = (V/ℏ_q²) · c/d` on `q > 1`, then `V ∈ K`. -/
theorem carrier_const_mem_of_rational (K : Subfield ℝ) (a b c d : K[X]) (hc : c ≠ 0)
    (hb : ∀ q : ℝ, 1 < q → (b.map K.subtype).eval q ≠ 0)
    (hd : ∀ q : ℝ, 1 < q → (d.map K.subtype).eval q ≠ 0) (V : ℝ)
    (h : ∀ q : ℝ, 1 < q → (a.map K.subtype).eval q / (b.map K.subtype).eval q
        = V / hbar q ^ 2 * ((c.map K.subtype).eval q / (d.map K.subtype).eval q)) :
    V ∈ K := by
  have hb0 : b ≠ 0 := by
    rintro rfl
    exact hb 2 (by norm_num) (by simp)
  refine const_mem_of_poly_identity K (a * d * (X - 1) ^ 2) (X ^ 2 * c * b) ?_ V ?_
  · exact mul_ne_zero (mul_ne_zero (pow_ne_zero 2 X_ne_zero) hc) hb0
  · intro q hq
    have e := h q hq
    have hbq := hb q hq
    have hdq := hd q hq
    have hq0 : q ≠ 0 := by positivity
    have hq1 : q - 1 ≠ 0 := sub_ne_zero.2 (ne_of_gt hq)
    simp only [Polynomial.map_mul, Polynomial.map_pow, Polynomial.map_sub, Polynomial.map_X,
      Polynomial.map_one, eval_mul, eval_pow, eval_sub, eval_X, eval_one]
    unfold hbar QOU.QBeta.E0WeightAllWords.hbar at e
    have : (1 : ℝ) - q⁻¹ = (q - 1) / q := by field_simp
    rw [this] at e
    field_simp at e
    linear_combination e

/-! ## 6. The corpus chart is the trivial instance -/

/-- The mass-formula weights `m(K)/unit`: electron `ℏ_q²`, muon `Vol`. -/
noncomputable def massFormulaElectron (q : ℝ) : ℝ := hbar q ^ 2

/-- **The carrier holds in the mass-formula chart by definition.** -/
theorem massFormula_carrier (V q : ℝ) (hq : 1 < q) :
    V = V / hbar q ^ 2 * massFormulaElectron q := by
  have hh : hbar q ≠ 0 := hbar_ne_zero hq
  unfold massFormulaElectron
  field_simp

/-- **At the CAL-2 point the mass-formula unit `m_e/ℏ_q²` is `m_μ/Vol`.** -/
theorem massFormula_unit (me mmu V q : ℝ) (hV : V ≠ 0)
    (hpin : mmu / me = V / hbar q ^ 2) (hme : me ≠ 0) :
    me / hbar q ^ 2 = mmu / V := by
  have hmmu : mmu = me * (V / hbar q ^ 2) := by
    field_simp at hpin ⊢
    linear_combination hpin
  rw [hmmu]
  field_simp

end QOU.Observations.EnergyScale
