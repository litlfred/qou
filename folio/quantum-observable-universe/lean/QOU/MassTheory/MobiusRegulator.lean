import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Order.Filter.Basic
import Mathlib.Topology.Order.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.MobiusRegulator — the classical "4" is a regulator-scheme datum

Bean `qou-uh5f` (regulator-universality route; bears on its candidate route 2,
the self-energy subtraction).  Two results, both sorry-free, over `ℝ` (integrals
and `ε → 0⁺` limits are archimedean, §7c):

* **(a) The BFHW elementary integral.**  In the proof of the Möbius
  Invariance Property, Bryson–Freedman–He–Wang take `u` to be arclength on a
  closed curve of length `l` and cut off `|u − v| ≥ ε`.  The subtracted
  arc-distance term of their `E_ε(γ)` (eq. (1), the term
  `− ∬ D(γ(u),γ(v))⁻²`) is then the elementary integral of their eq. (3):
  `∫₀^l [ 2 ∫_ε^{l/2} v⁻² dv ] du`.
  **Sign, checked against the source** (`library/arxiv-math-9301212v1`,
  `sec-000`, eqs. (1) and (3)): the integral *as printed* equals
  `2l/ε − 4`; the value `4 − 2l/ε` printed after it is the **signed**
  contribution of that term to `E_ε`, i.e. with the minus sign of eq. (1)
  included.  Both are proved below (`bfhw_regularization_integral` and
  `bfhw_regularization_term`).

* **(b) Regulator universality.**  If an energy is *defined* as
  `E_R(γ) = lim_{ε→0⁺} (A_ε(γ) − R(ε, L(γ)))` for a regulator `R` that depends
  only on `(ε, length)`, and two regulators satisfy
  `R₁(ε,L) − R₂(ε,L) → c`, then `E_{R₁}(γ) − E_{R₂}(γ) = −c` for every curve
  where both limits exist — the same `−c` for every such curve.

Corollary (`bfhw_minus_minimalSubtraction`): with the BFHW regulator
`R_BFHW(ε,l) = ∫₀^l 2∫_ε^{l/2} v⁻²` and the bare pole subtraction
`R_ms(ε,l) = 2l/ε`, every curve of positive length on which both limits exist
has `E_BFHW(γ) = E_ms(γ) + 4`.  So the "4" (the round-circle value of BFHW
Theorem A) is exactly the finite part of the BFHW regulator, and
`regulator_shift` shows any other finite part is reachable by a regulator of
the same admissible shape.  This is the precise sense in which the
classical-limit constant `CategoricalMobiusEnergy.classicalLimitConst` of
`QOU.MobiusEnergy` (proved there to be unconstrained,
`classicalLimitConst_surjective`) is a **regulator-scheme datum**: fixing it is
equivalent to fixing the finite part of the regulator, not a consequence of
the energy density.  No axiom or class field is introduced here.

-- Ref: [bryson-freedman-he-wang1993]
-/

open Filter Topology intervalIntegral

namespace QOU.MobiusRegulator

/-! ## (a) The Bryson–Freedman–He–Wang elementary integral -/

/-- Inner integral: `∫_ε^{b} v⁻² dv = 1/ε − 1/b` for `0 < ε`, `0 < b`. -/
theorem integral_inv_sq_of_pos {ε b : ℝ} (hε : 0 < ε) (hb : 0 < b) :
    ∫ v in ε..b, (v ^ 2)⁻¹ = 1 / ε - 1 / b := by
  have h0 : (0 : ℝ) ∉ Set.uIcc ε b := by
    intro h
    rcases Set.mem_uIcc.mp h with h | h
    · linarith [h.1]
    · linarith [h.1]
  have hfun : (fun v : ℝ => (v ^ 2)⁻¹) = fun v : ℝ => v ^ (-2 : ℤ) := by
    funext v
    rw [zpow_neg]
    norm_cast
  rw [hfun, integral_zpow (Or.inr ⟨by norm_num, h0⟩)]
  have hε0 : ε ≠ 0 := hε.ne'
  have hb0 : b ≠ 0 := hb.ne'
  push_cast
  norm_num
  field_simp
  ring

/-- **BFHW eq. (3), the integral as printed.**  For a closed curve of
arclength `l > 0` and cutoff `ε > 0`,
`∫₀^l [2 ∫_ε^{l/2} v⁻² dv] du = 2l/ε − 4`.  (BFHW work with `ε < l/2`; the
oriented interval integral makes the identity hold for every `ε > 0`, so that
hypothesis is not needed and is not assumed.) -/
theorem bfhw_regularization_integral (l ε : ℝ) (hl : 0 < l) (hε : 0 < ε) :
    ∫ _u in (0 : ℝ)..l, 2 * ∫ v in ε..l / 2, (v ^ 2)⁻¹ = 2 * l / ε - 4 := by
  rw [integral_inv_sq_of_pos hε (by linarith), intervalIntegral.integral_const,
    smul_eq_mul]
  have hε0 : ε ≠ 0 := hε.ne'
  have hl0 : l ≠ 0 := hl.ne'
  field_simp
  ring

/-- **BFHW eq. (3), the signed term.**  The arc-distance term enters
`E_ε(γ)` (eq. (1)) with a minus sign; its contribution is `4 − 2l/ε`. -/
theorem bfhw_regularization_term (l ε : ℝ) (hl : 0 < l) (hε : 0 < ε) :
    -(∫ _u in (0 : ℝ)..l, 2 * ∫ v in ε..l / 2, (v ^ 2)⁻¹) = 4 - 2 * l / ε := by
  rw [bfhw_regularization_integral l ε hl hε]
  ring

/-! ## (b) Regulator universality -/

variable {Γ : Type*}

/-- The regularized energy of a curve `γ` for regulator `R : ε → length → ℝ`:
`lim_{ε→0⁺} (A ε − R ε L)`, as a `limUnder` (meaningful when the limit exists). -/
noncomputable def regEnergy (A : Γ → ℝ → ℝ) (L : Γ → ℝ) (R : ℝ → ℝ → ℝ)
    (γ : Γ) : ℝ :=
  limUnder (𝓝[>] (0 : ℝ)) fun ε => A γ ε - R ε (L γ)

/-- **Regulator universality, limit form.**  If `A_ε(γ) − R₁(ε,L) → E₁`,
`A_ε(γ) − R₂(ε,L) → E₂`, and `R₁(ε,L) − R₂(ε,L) → c` as `ε → 0⁺`, then
`E₁ − E₂ = −c`. -/
theorem regulator_difference (A : ℝ → ℝ) (ℓ : ℝ) (R₁ R₂ : ℝ → ℝ → ℝ)
    (c E₁ E₂ : ℝ)
    (hR : Tendsto (fun ε => R₁ ε ℓ - R₂ ε ℓ) (𝓝[>] 0) (𝓝 c))
    (h₁ : Tendsto (fun ε => A ε - R₁ ε ℓ) (𝓝[>] 0) (𝓝 E₁))
    (h₂ : Tendsto (fun ε => A ε - R₂ ε ℓ) (𝓝[>] 0) (𝓝 E₂)) :
    E₁ - E₂ = -c := by
  have hdiff : Tendsto (fun ε => (A ε - R₁ ε ℓ) - (A ε - R₂ ε ℓ)) (𝓝[>] 0)
      (𝓝 (E₁ - E₂)) := h₁.sub h₂
  have hneg : Tendsto (fun ε => (A ε - R₁ ε ℓ) - (A ε - R₂ ε ℓ)) (𝓝[>] 0)
      (𝓝 (-c)) := by
    have := hR.neg
    refine this.congr ?_
    intro ε
    ring
  exact tendsto_nhds_unique hdiff hneg

/-- **Regulator universality for `regEnergy`.**  For a curve `γ` on which both
regularized limits exist, `E_{R₁}(γ) − E_{R₂}(γ) = −c` where
`c = lim (R₁ − R₂)(ε, L(γ))`. -/
theorem regEnergy_sub (A : Γ → ℝ → ℝ) (L : Γ → ℝ) (R₁ R₂ : ℝ → ℝ → ℝ) (c : ℝ)
    (γ : Γ)
    (hR : Tendsto (fun ε => R₁ ε (L γ) - R₂ ε (L γ)) (𝓝[>] 0) (𝓝 c))
    (h₁ : ∃ E, Tendsto (fun ε => A γ ε - R₁ ε (L γ)) (𝓝[>] 0) (𝓝 E))
    (h₂ : ∃ E, Tendsto (fun ε => A γ ε - R₂ ε (L γ)) (𝓝[>] 0) (𝓝 E)) :
    regEnergy A L R₁ γ - regEnergy A L R₂ γ = -c := by
  obtain ⟨E₁, hE₁⟩ := h₁
  obtain ⟨E₂, hE₂⟩ := h₂
  unfold regEnergy
  rw [hE₁.limUnder_eq, hE₂.limUnder_eq]
  exact regulator_difference (A γ) (L γ) R₁ R₂ c E₁ E₂ hR hE₁ hE₂

/-- **Independence of the curve.**  If `R₁ − R₂ → c` at every length, the
energy difference is the same number for any two curves on which all four
limits exist. -/
theorem regEnergy_sub_indep (A : Γ → ℝ → ℝ) (L : Γ → ℝ) (R₁ R₂ : ℝ → ℝ → ℝ)
    (c : ℝ) (hR : ∀ ℓ, Tendsto (fun ε => R₁ ε ℓ - R₂ ε ℓ) (𝓝[>] 0) (𝓝 c))
    (γ γ' : Γ)
    (h₁ : ∃ E, Tendsto (fun ε => A γ ε - R₁ ε (L γ)) (𝓝[>] 0) (𝓝 E))
    (h₂ : ∃ E, Tendsto (fun ε => A γ ε - R₂ ε (L γ)) (𝓝[>] 0) (𝓝 E))
    (h₁' : ∃ E, Tendsto (fun ε => A γ' ε - R₁ ε (L γ')) (𝓝[>] 0) (𝓝 E))
    (h₂' : ∃ E, Tendsto (fun ε => A γ' ε - R₂ ε (L γ')) (𝓝[>] 0) (𝓝 E)) :
    regEnergy A L R₁ γ - regEnergy A L R₂ γ
      = regEnergy A L R₁ γ' - regEnergy A L R₂ γ' := by
  rw [regEnergy_sub A L R₁ R₂ c γ (hR _) h₁ h₂,
    regEnergy_sub A L R₁ R₂ c γ' (hR _) h₁' h₂']

/-! ## Corollaries: the BFHW "4" and the freedom to move it -/

/-- The BFHW regulator: the arc-distance integral of eq. (3). -/
noncomputable def bfhwRegulator (ε l : ℝ) : ℝ :=
  ∫ _u in (0 : ℝ)..l, 2 * ∫ v in ε..l / 2, (v ^ 2)⁻¹

/-- The bare pole subtraction ("minimal subtraction"): `2l/ε`. -/
noncomputable def msRegulator (ε l : ℝ) : ℝ := 2 * l / ε

/-- For `l > 0`, `R_BFHW(ε,l) − R_ms(ε,l) → −4` as `ε → 0⁺` (it equals `−4`
for every `ε > 0`, by (a)). -/
theorem bfhw_sub_ms_tendsto (l : ℝ) (hl : 0 < l) :
    Tendsto (fun ε => bfhwRegulator ε l - msRegulator ε l) (𝓝[>] 0) (𝓝 (-4)) := by
  refine tendsto_const_nhds.congr' ?_
  filter_upwards [self_mem_nhdsWithin] with ε (hε : 0 < ε)
  unfold bfhwRegulator msRegulator
  rw [bfhw_regularization_integral l ε hl hε]
  ring

/-- **The classical "4" is the finite part of the BFHW regulator.**  For every
curve of positive length on which both regularized limits exist,
`E_BFHW(γ) = E_ms(γ) + 4`. -/
theorem bfhw_minus_minimalSubtraction (A : Γ → ℝ → ℝ) (L : Γ → ℝ) (γ : Γ)
    (hL : 0 < L γ)
    (h₁ : ∃ E, Tendsto (fun ε => A γ ε - bfhwRegulator ε (L γ)) (𝓝[>] 0) (𝓝 E))
    (h₂ : ∃ E, Tendsto (fun ε => A γ ε - msRegulator ε (L γ)) (𝓝[>] 0) (𝓝 E)) :
    regEnergy A L bfhwRegulator γ = regEnergy A L msRegulator γ + 4 := by
  have := regEnergy_sub A L bfhwRegulator msRegulator (-4) γ
    (bfhw_sub_ms_tendsto (L γ) hL) h₁ h₂
  linarith

/-- **The finite part is free.**  Given any regulator `R` of the admissible
shape (a function of `(ε, length)` only) and any target shift `k`, the
regulator `R' = R − k` has the same shape, differs from `R` by a constant (so
has the same divergent part), and moves the energy of *every* curve on which
the `R`-limit exists by exactly `k`.  Hence no value of an additive
classical-limit constant follows from the energy density `A` alone: it is
fixed only by choosing the regulator's finite part. -/
theorem regulator_shift (A : Γ → ℝ → ℝ) (L : Γ → ℝ) (R : ℝ → ℝ → ℝ) (k : ℝ) :
    (∀ ℓ, Tendsto (fun ε => R ε ℓ - (R ε ℓ - k)) (𝓝[>] 0) (𝓝 k)) ∧
    ∀ γ : Γ, (∃ E, Tendsto (fun ε => A γ ε - R ε (L γ)) (𝓝[>] 0) (𝓝 E)) →
      regEnergy A L (fun ε ℓ => R ε ℓ - k) γ = regEnergy A L R γ + k := by
  refine ⟨fun ℓ => ?_, fun γ ⟨E, hE⟩ => ?_⟩
  · refine tendsto_const_nhds.congr ?_
    intro ε
    ring
  · have hE' : Tendsto (fun ε => A γ ε - (fun ε ℓ => R ε ℓ - k) ε (L γ)) (𝓝[>] 0)
        (𝓝 (E + k)) := by
      refine (hE.add_const k).congr ?_
      intro ε
      simp only
      ring
    unfold regEnergy
    rw [hE.limUnder_eq, hE'.limUnder_eq]

/-- **Pointwise BFHW-minus-MS regulator identity at every positive cutoff (`qou-uh5f`).**
For any curve length `l > 0` and cutoff `ε > 0`, `bfhwRegulator ε l - msRegulator ε l = -4`
identically before taking `ε → 0⁺`. -/
theorem bfhwRegulator_sub_msRegulator_eq_neg_four (l ε : ℝ) (hl : 0 < l) (hε : 0 < ε) :
    bfhwRegulator ε l - msRegulator ε l = -4 := by
  unfold bfhwRegulator msRegulator
  rw [bfhw_regularization_integral l ε hl hε]
  ring

end QOU.MobiusRegulator
