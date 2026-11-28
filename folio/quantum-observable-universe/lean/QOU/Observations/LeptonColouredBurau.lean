import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# One `G_m` per component: the coloured Burau action on the lepton words

Thread "Derive the muon mass relation" (2026-11-28). Owner (02:14Z): "Use the (formal) group action
to see interactions between knots across components."

Each lepton closure has two components, so a torus `G_m × G_m` acts, one factor `tᵢ` per
component. Before any trace, the braid acts by the coloured (Gassner-type) Burau matrices. The
crossing `σᵢ` uses `[[1 − t, t], [1, 0]]` in slots `i, i+1`, where `t` is the colour of the strand
that crosses over. The closure invariant is the `(0,0)` minor of `I − B(β)`, which is
`(1 − t₂) · Δ_L(t₁, t₂)` up to a unit. Here `Δ_L` is the two-variable Alexander polynomial.

The colour sequences (over-strand colour per letter, read from the closure permutation) are fixed
in the definitions. Results, over any field with `t₁, t₂ ≠ 0`:
* `e_minor`: Hopf, `Δ = 1`.
* `mu_minor`: T(2,4), `Δ = 1 + t₁t₂`. It depends only on the product `t₁t₂`, so only the diagonal
  `G_m ⊂ G_m × G_m` sees the muon. Its two components are fully coupled.
* `tau_minor`: Whitehead, `Δ = (t₁ − 1)(t₂ − 1)`, a product of one factor per component. The
  components are decoupled at this level, even though the link does not split. This is the
  linking-number-zero case (Torres: `Δ(t, 1) = 0`).
* `torres`: setting `t₂ = 1` gives `Δ(t, 1) = (t^lk − 1)/(t − 1)`, with `lk = 1, 2, 0`. That is the
  `U(1) = 3·lk` of #9805, seen per component: `3, 6, 0`.
* `diag_at_minus_one`: on the diagonal `t₁ = t₂ = −1` (that is, `q = i` with `t = q²`),
  `|(t − 1)·Δ(t, t)|` gives the determinants 2, 4, 8 (`LeptonMassAtI`).

No measured value enters, and nothing here fixes a mass.
-/

namespace QOU.Observations.LeptonColouredBurau

variable {F : Type*} [Field F]

/-- `σᵢ^{±1}` in the coloured Burau action, with over-strand colour `t`. -/
def cb (i : Fin 2) (t : F) (pos : Bool) : Matrix (Fin 3) (Fin 3) F :=
  match i, pos with
  | 0, true => !![1 - t, t, 0; 1, 0, 0; 0, 0, 1]
  | 0, false => !![0, 1, 0; t⁻¹, 1 - t⁻¹, 0; 0, 0, 1]
  | 1, true => !![1, 0, 0; 0, 1 - t, t; 0, 1, 0]
  | 1, false => !![1, 0, 0; 0, 0, 1; 0, t⁻¹, 1 - t⁻¹]

theorem cb_inv (i : Fin 2) {t : F} (ht : t ≠ 0) : cb i t true * cb i t false = 1 := by
  fin_cases i <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [cb, Matrix.mul_apply, Fin.sum_univ_three, ht, mul_sub]

/-- The `(0,0)` minor of `I − M`. -/
def minor00 (M : Matrix (Fin 3) (Fin 3) F) : F :=
  (1 - M 1 1) * (1 - M 2 2) - M 1 2 * M 2 1

/-- Electron `σ₀σ₁σ₀`; colours `t₂, t₁, t₁` (later letters multiply on the left). -/
def Be (t₁ t₂ : F) := cb 0 t₁ true * cb 1 t₁ true * cb 0 t₂ true

/-- Muon `σ₀⁴σ₁⁻¹`; colours `t₂, t₁, t₂, t₁, t₂`. -/
def Bmu (t₁ t₂ : F) :=
  cb 1 t₂ false * cb 0 t₁ true * cb 0 t₂ true * cb 0 t₁ true * cb 0 t₂ true

/-- Tau `σ₀²σ₁⁻¹σ₀σ₁⁻¹`; colours `t₂, t₁, t₂, t₁, t₁`. -/
def Btau (t₁ t₂ : F) :=
  cb 1 t₁ false * cb 0 t₁ true * cb 1 t₂ false * cb 0 t₁ true * cb 0 t₂ true

theorem e_minor (t₁ t₂ : F) : minor00 (Be t₁ t₂) = 1 - t₂ := by
  simp [minor00, Be, cb, Matrix.mul_apply, Fin.sum_univ_three]

theorem mu_minor {t₁ t₂ : F} (h₂ : t₂ ≠ 0) :
    minor00 (Bmu t₁ t₂) = (1 - t₂) * (1 + t₁ * t₂) / t₂ := by
  simp [minor00, Bmu, cb, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

theorem tau_minor {t₁ t₂ : F} (h₁ : t₁ ≠ 0) (h₂ : t₂ ≠ 0) :
    minor00 (Btau t₁ t₂) = (1 - t₂) * ((t₁ - 1) * (t₂ - 1)) * (-1 / (t₁ * t₂)) := by
  simp [minor00, Btau, cb, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp
  ring

/-- The two-variable Alexander polynomials read off above. -/
def De (_ _ : F) : F := 1
def Dmu (t₁ t₂ : F) : F := 1 + t₁ * t₂
def Dtau (t₁ t₂ : F) : F := (t₁ - 1) * (t₂ - 1)

/-- **Torres, per component:** `Δ(t, 1)·(t − 1) = t^lk − 1` with `lk = 1, 2, 0`. -/
theorem torres (t : F) :
    De t 1 * (t - 1) = t ^ 1 - 1 ∧ Dmu t 1 * (t - 1) = t ^ 2 - 1 ∧
    Dtau t 1 * (t - 1) = t ^ 0 - 1 := by
  refine ⟨?_, ?_, ?_⟩ <;> (simp [De, Dmu, Dtau]; try ring)

/-- **Coupling:** the muon sees only the diagonal `t₁t₂`. The tau factorises, one factor per
component. -/
theorem mu_diagonal (t₁ t₂ s₁ s₂ : F) (h : t₁ * t₂ = s₁ * s₂) : Dmu t₁ t₂ = Dmu s₁ s₂ := by
  simp [Dmu, h]

theorem tau_split (t₁ t₂ : F) : Dtau t₁ t₂ = Dtau t₁ 0 * Dtau 0 t₂ := by
  simp [Dtau]; ring

/-- **Diagonal at `t = −1`:** `(t − 1)Δ(t, t) = −2, 4, −8`, the determinants. -/
theorem diag_at_minus_one :
    ((-1 : F) - 1) * De (-1) (-1) = -2 ∧ ((-1 : F) - 1) * Dmu (-1) (-1) = -4 ∧
    ((-1 : F) - 1) * Dtau (-1) (-1) = -8 := by
  refine ⟨?_, ?_, ?_⟩ <;> simp [De, Dmu, Dtau] <;> ring

end QOU.Observations.LeptonColouredBurau
