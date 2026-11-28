/-
# Which reading is the mass? What `def:mass-identity` forces for the least-trace ladder

Thread "Derive the electron's categorical weight" (2026-11-28). Owner ruling "Derive the reading
first" (PR #9853), then the recommended card "Derive the reading from the axioms".
Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §18.

`def:mass-identity` (mass-endomorphism/mass-identity.md) already fixes the three choices left
open in §16–§17:

1. **Colour.** The Hecke/Temperley–Lieb model acts on `V^{⊗n}` with `V = R²` (Jimbo's R-matrix),
   so the colour is `N = 2`. No other colour appears in the definition.
2. **Reading.** The mass is a ring element `∫_A ρ(β) ∈ ℚ(q)`, framing-corrected to
   `[2]ⁿ q^{−2w} ∫_A ρ(β)`. A comparison applies one ring homomorphism `φ` and then `|·|`. The
   growth `(2π/N) log|c_N|` along the family `N → ∞` at `ζ_N` is not `|φ(m)|` for any single
   ring element `m`, so it is not the mass under the current definition.
3. **Cycle.** The mass is read on braid classes (conjugation and both stabilisations). The axis
   is not part of the class of `β`: `closure(β) ∪ A` is the class of the 4-braid
   `β σ₃σ₂σ₁σ₁σ₂σ₃`, which is a different cycle.

This file computes the forced reading in the convention-D Hecke model, over any field:
* `massWord_e`, `massWord_mu`: `m(σ₁σ₂σ₁) = m(σ₁²σ₂⁻¹) = (q² + 1)(q⁴ + 1)/q⁶ = [4]/q³`.
  Both braids close to the Hopf link, so the definition gives **equal masses** (`mass_mu_eq_e`).
* `massWord_tau`: `m(σ₁⁴σ₂⁻¹) = (q² + 1)(q⁸ + q⁴ − q² + 1)/q¹²`, the class of `σ₁⁴` (the
  `(2,4)` torus link).
So under the definition as it stands, the least-trace ladder cannot give `e` and `μ` different
masses. Separating them needs either other words (other braid classes) or a change of the
definition (axis in the cycle, or the `ζ_N` growth as the reading), and that change needs the
owner's own tap. No measured value enters.
-/
import QOU.Nuclear.WeightSpaceMarkov
import Mathlib.Tactic

namespace QOU.Observations.MassReadingForced

open QOU.QBeta.WeightSpaceMarkov

variable {R : Type*} [Field R]

/-- `σ₂⁻¹` on the 2-dimensional block: `ρ(σ₂)⁻¹ = ρ(σ₂) − (q − q⁻¹)`. -/
def r21bInv (q : R) : Matrix (Fin 2) (Fin 2) R := r21b q - (q - q⁻¹) • 1

theorem r21bInv_eq (q : R) : r21bInv q = !![-q, 0; 1, q⁻¹] := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [r21b, r21bInv]; ring

theorem r21bInv_mul (q : R) (hq : q ≠ 0) : r21b q * r21bInv q = 1 := by
  rw [r21bInv_eq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [r21b] <;> field_simp

/-- Convention-D Ocneanu weights on the blocks `(3)` and `(2,1)`. -/
def y3 (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2
def y21 (q : R) : R := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- Framing-corrected 3-strand mass (`def:mass-identity`): `[2]³ q^{−2w} (y₃ q^w + y₂₁ tr M)`,
with `w` the writhe and `M` the image of the braid on the `(2,1)` block. -/
def massWord (q : R) (w : ℕ) (M : Matrix (Fin 2) (Fin 2) R) : R :=
  (q + q⁻¹) ^ 3 * (q ^ (2 * w))⁻¹ * (y3 q * q ^ w + y21 q * M.trace)

/-- `e = σ₁σ₂σ₁`. -/
theorem massWord_e (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 3 (r21a q * r21b q * r21a q) = (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 6 := by
  simp [massWord, y3, y21, r21a, r21b, Matrix.trace_fin_two]
  field_simp
  ring

/-- `μ = σ₁²σ₂⁻¹`. -/
theorem massWord_mu (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 1 (r21a q * r21a q * r21bInv q) = (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 6 := by
  simp [massWord, y3, y21, r21a, r21bInv_eq, Matrix.trace_fin_two]
  field_simp
  ring

/-- **The forced reading cannot separate `e` and `μ`**: equal braid-class masses. -/
theorem mass_mu_eq_e (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 1 (r21a q * r21a q * r21bInv q) = massWord q 3 (r21a q * r21b q * r21a q) := by
  rw [massWord_e q hq h2, massWord_mu q hq h2]

/-- `τ = σ₁⁴σ₂⁻¹`, the class of the `(2,4)` torus link. -/
theorem massWord_tau (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 3 (r21a q * r21a q * r21a q * r21a q * r21bInv q) =
      (q ^ 2 + 1) * (q ^ 8 + q ^ 4 - q ^ 2 + 1) / q ^ 12 := by
  simp [massWord, y3, y21, r21a, r21bInv_eq, Matrix.trace_fin_two]
  field_simp
  ring

end QOU.Observations.MassReadingForced
