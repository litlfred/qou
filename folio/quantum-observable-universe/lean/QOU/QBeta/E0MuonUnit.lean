/-
# E₀ in the units of the model mass formula

The corpus mass formula is `m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`, and the muon pin is its
`K = 4₁` case, `m_μ = m_e · Vol(4₁) / ℏ_q²`, with `ℏ_q = 1 - q⁻¹` and `c_q = 1/(q - 1)`.
This file shows, over a generic field, that the decay energy `E₀ = m_e / (q (q - 1))`
carries the same `c_q²` as every model mass:

* `one_div_hbar_sq` : `1/ℏ_q² = q² · c_q²`, so every model mass is a multiple of
  `m_e · c_q²`;
* `E0_eq_me_cq_sq_hbar` : `E₀ = m_e · c_q² · ℏ_q`;
* `E0_eq_muon_fraction` : under the muon pin, `E₀ = m_μ · ℏ_q / (q² · Vol)`;
* `E0_eq_model_mass` : `E₀ = m_e · (ℏ_q / q²) / ℏ_q²`, i.e. `E₀` is the model mass of
  categorical weight `ℏ_q / q²`.

These are identities. They do not derive the weight `ℏ_q / q²` from Hecke structure,
and the `1/ℏ_q²` is the CAL-2 pin itself.
-/
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.E0MuonUnit

variable {R : Type*} [Field R]

/-- `ℏ_q = 1 - q⁻¹`. -/
def hbar (q : R) : R := 1 - q⁻¹

/-- `c_q = 1/(q - 1)`. -/
def cq (q : R) : R := 1 / (q - 1)

/-- `E₀ = m_e / (q (q - 1))`. -/
def E0 (me q : R) : R := me / (q * (q - 1))

theorem hbar_ne_zero {q : R} (_hq : q ≠ 0) (h1 : q ≠ 1) : hbar q ≠ 0 := by
  unfold hbar
  intro h
  apply h1
  have : q⁻¹ = 1 := by linear_combination -h
  have := congrArg Inv.inv this
  simpa using this

theorem one_div_hbar_sq {q : R} (hq : q ≠ 0) (h1 : q ≠ 1) :
    1 / hbar q ^ 2 = q ^ 2 * cq q ^ 2 := by
  have h1' : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  unfold hbar cq
  field_simp

theorem E0_eq_me_cq_sq_hbar (me : R) {q : R} (hq : q ≠ 0) (h1 : q ≠ 1) :
    E0 me q = me * cq q ^ 2 * hbar q := by
  have h1' : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  unfold E0 hbar cq
  field_simp

theorem E0_eq_muon_fraction (me mmu V : R) {q : R} (hq : q ≠ 0) (h1 : q ≠ 1)
    (hV : V ≠ 0) (hpin : mmu = me * V / hbar q ^ 2) :
    E0 me q = mmu * hbar q / (q ^ 2 * V) := by
  have hh := hbar_ne_zero hq h1
  have h1' : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  subst hpin
  unfold E0
  unfold hbar at hh ⊢
  field_simp

theorem E0_eq_model_mass (me : R) {q : R} (hq : q ≠ 0) (h1 : q ≠ 1) :
    E0 me q = me * (hbar q / q ^ 2) / hbar q ^ 2 := by
  have hh := hbar_ne_zero hq h1
  have h1' : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  unfold E0
  unfold hbar at hh ⊢
  field_simp

end QOU.QBeta.E0MuonUnit
