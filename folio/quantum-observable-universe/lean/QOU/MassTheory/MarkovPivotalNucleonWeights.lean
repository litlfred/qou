import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# The Markov condition at `z_D` forces the nucleon weight ratio `q²`

Take Jimbo's `Ř` on `V ⊗ V` (basis `uu, ud, du, dd`) and a diagonal pivotal weight
`K = diag(a, b)` on the closed strand. The Markov condition asks that the weighted partial
trace of `Ř` over the second strand be a scalar `μ` times the identity, and then
`z = μ / (a + b)`.

* `markov_forces_ratio`: the condition holds iff `b = a q⁻²`. So the `u : d` weight ratio is
  `q² : 1`, whatever the overall scale `a`.
* `markov_z_eq_zD`: the resulting Markov parameter is `z_D = q³/(q² + 1)`, for every scale.
* `nucleon_weight_ratio`: on three strands the proton sector (`uud`) carries `a²b` and the
  neutron sector (`udd`) carries `ab²`, so neutron = `q⁻²` × proton, for every scale.
* `framed_unit_scale`: with the trace normalised (`a + b = 1`) and the framing factor
  `(1 + q²)³ q⁻³` of `def:mass-identity`, the weights are exactly `q` and `q⁻¹`.

So the `q⁻²` ratio follows from convention D's Markov condition, with no symmetric `K` assumed.
The overall scale does not: the framed, normalised trace gives `q` and `q⁻¹` (the K2 reading,
which the proton test falsified), and the proton-normalised K1 needs a further `q⁻¹` that this
file does not produce. No measured value enters.
-/

namespace QOU.MassTheory.MarkovPivotalNucleonWeights

variable {R : Type*} [Field R]

/-- Jimbo's `Ř` on `V ⊗ V`, basis `uu, ud, du, dd`. -/
def Rcheck (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- Weighted partial trace over the second strand, diagonal `u` entry. -/
def ptrU (q a b : R) : R := a * Rcheck q 0 0 + b * Rcheck q 1 1
/-- Diagonal `d` entry. -/
def ptrD (q a b : R) : R := a * Rcheck q 2 2 + b * Rcheck q 3 3
/-- Off-diagonal entries. -/
def ptrUD (q a b : R) : R := a * Rcheck q 0 2 + b * Rcheck q 1 3
def ptrDU (q a b : R) : R := a * Rcheck q 2 0 + b * Rcheck q 3 1

theorem ptr_offdiag (q a b : R) : ptrUD q a b = 0 ∧ ptrDU q a b = 0 := by
  simp [ptrUD, ptrDU, Rcheck]

/-- **The Markov condition fixes the ratio.** The partial trace is scalar iff `b = a q⁻²`. -/
theorem markov_forces_ratio (q a b : R) (hq : q ≠ 0) :
    ptrU q a b = ptrD q a b ↔ b = a * q⁻¹ ^ 2 := by
  simp only [ptrU, ptrD, Rcheck]
  simp
  constructor
  · intro h
    have : b * q = a * q⁻¹ := by linear_combination -h
    field_simp at this ⊢
    linear_combination this
  · intro h
    subst h
    field_simp
    ring

/-- **The Markov parameter is `z_D`, for every scale `a`.** -/
theorem markov_z_eq_zD (q a : R) (hq : q ≠ 0) (ha : a ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    ptrU q a (a * q⁻¹ ^ 2) / (a + a * q⁻¹ ^ 2) = q ^ 3 / (q ^ 2 + 1) := by
  simp [ptrU, Rcheck]
  have h1 : a + a * (q ^ 2)⁻¹ ≠ 0 := by
    rw [show a + a * (q ^ 2)⁻¹ = a * (q ^ 2 + 1) / q ^ 2 by field_simp]
    exact div_ne_zero (mul_ne_zero ha hq2) (pow_ne_zero 2 hq)
  field_simp

/-- **Neutron = `q⁻²` × proton, for every scale.** Proton sector weight `a²b`, neutron `ab²`. -/
theorem nucleon_weight_ratio (q a : R) :
    a * (a * q⁻¹ ^ 2) ^ 2 = q⁻¹ ^ 2 * (a ^ 2 * (a * q⁻¹ ^ 2)) := by
  ring

/-- With `a + b = 1` and the framing factor `(1 + q²)³ q⁻³` of `def:mass-identity`, the proton
and neutron weights are `q` and `q⁻¹`. -/
theorem framed_unit_scale (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    let a := q ^ 2 / (q ^ 2 + 1)
    let b := 1 / (q ^ 2 + 1)
    a + b = 1 ∧ b = a * q⁻¹ ^ 2 ∧
      (1 + q ^ 2) ^ 3 * q⁻¹ ^ 3 * (a ^ 2 * b) = q ∧
      (1 + q ^ 2) ^ 3 * q⁻¹ ^ 3 * (a * b ^ 2) = q⁻¹ := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> field_simp <;> ring

end QOU.MassTheory.MarkovPivotalNucleonWeights
