import QOU.IwahoriHecke.JimboClassicalLimit
import Mathlib.Algebra.Lie.Matrix

/-!
# QOU.StandardModel.ColourBridge — the strengthened colour-action conjecture (option A)

Bean `qou-cb3r` (option A, owner-approved 2026-11-15). Audit:
`docs/audits/2026-11-15-colour-stabilizer-bridge.md`, §1 and §5.

`ColourStabilizerAction g V` (`QOU.StandardModel.ColourStabilizerAction`) asks only for an
injective linear map `g → End V`, and is equivalent to `finrank g ≤ (finrank V)²`
(`ColourBridgeObstructions.colourStabilizerAction_of_finrank_le`). An instance of it is therefore
no evidence of a bridge. This file states the strengthening the audit proposes:

* **Lie hom.** `Φ : g →ₗ⁅K⁆ gl₃(K)` respects brackets, not only linear structure.
* **Complex structure.** The base field `K` is a parameter. The intended `K` is `ℚ(i)`, with `i`
  acting on the octonion colour triplet as `+L_e` or `−L_e`. Asking `Φ` to be `K`-linear is asking
  it to intertwine that complex structure. The choice `±L_e` is the one 3 vs 3̄ bit (audit §0, item 2);
  the class does not fix it.
* **Crossing compatibility.** For every `x`, the primitive coproduct `x ⊗ 1 + 1 ⊗ x` of `Φ x`
  commutes with Jimbo's crossing `Ř(q, q⁻¹)` on `K³ ⊗ K³`, the tower's level-3 colour channel.

The intended instance is `g = su3 e ⊗ ℚ(i)`, `K = ℚ(i)`. It is **not provided**: providing it is
the open derivation (`conj:sm-colour-stabilizer-action`). Complexification of `su3 e` is not yet
formalised in the corpus, so the class is stated over an abstract `g`.

Proved here:
* `ColourBridge.q_eq_one_of_e01_mem` — if the image of `Φ` contains the root vector `E₀₁`, the
  crossing field forces `q = 1`. This is `JimboClassicalLimit.primitive_commute_rCheckN_iff`
  read through the class. By the audit (§0, §8, §8.1) the class is a `q = 1` statement.
* `colourBridge_gl3_one` — calibration: at `q = 1` the class is satisfiable, by `gl₃(K)` itself
  with `Φ = id`. So the class is not vacuous at the classical point.
-/

namespace QOU.StandardModel

open QOU.IwahoriHecke.TensorEmbedGL QOU.IwahoriHecke.JimboClassicalLimit Matrix

/-- **Conjecture (colour bridge, strengthened).** Over a field `K` (intended: `ℚ(i)`, carrying the
octonion complex structure `±L_e`), the colour Lie algebra `g` (intended: `su3 e ⊗ ℚ(i)`) maps
injectively and bracket-preservingly into `gl₃(K)`, and every image matrix, acting by the primitive
coproduct, commutes with Jimbo's crossing `Ř(q, q⁻¹)` on `K³ ⊗ K³`. -/
class ColourBridge (K : Type*) [Field K] (g : Type*) [LieRing g] [LieAlgebra K g] (q : K) :
    Prop where
  /-- A faithful Lie action on the tower triplet, compatible with the tower crossing at `q`. -/
  bridge : ∃ Φ : g →ₗ⁅K⁆ Matrix (Fin 3) (Fin 3) K, Function.Injective Φ ∧
    ∀ x, rCheckN q q⁻¹ * primDelta (Φ x) = primDelta (Φ x) * rCheckN q q⁻¹

/-- **The crossing field forces `q = 1` once `E₀₁` is in the image.** -/
theorem ColourBridge.q_eq_one_of_e01_mem {K : Type*} [Field K] {g : Type*} [LieRing g]
    [LieAlgebra K g] {q : K} (Φ : g →ₗ⁅K⁆ Matrix (Fin 3) (Fin 3) K)
    (hΦ : ∀ x, rCheckN q q⁻¹ * primDelta (Φ x) = primDelta (Φ x) * rCheckN q q⁻¹)
    (x : g) (hx : Φ x = e01) : q = 1 :=
  ((primitive_commute_rCheckN_iff q q⁻¹).mp (hx ▸ hΦ x)).1

/-- At `q = 1` Jimbo's crossing is the flip. -/
private theorem rCheckN_one_inv_one {K : Type*} [Field K] :
    rCheckN (d := 3) (1 : K) (1 : K)⁻¹ = Matrix.of fun a b => if a = b.swap then 1 else 0 := by
  ext a b
  rcases a with ⟨a1, a2⟩
  rcases b with ⟨b1, b2⟩
  simp only [rCheckN_apply, inv_one, sub_self, Matrix.of_apply, Prod.swap_prod_mk, Prod.ext_iff]
  by_cases h1 : a1 = b1 <;> by_cases h2 : a2 = b2 <;> by_cases h3 : b1 = b2 <;>
    by_cases h4 : b1 < b2 <;> simp_all

/-- **Calibration: the class is satisfiable at `q = 1`**, by `gl₃(K)` with `Φ = id`. -/
theorem colourBridge_gl3_one (K : Type*) [Field K] :
    ColourBridge K (Matrix (Fin 3) (Fin 3) K) 1 := by
  refine ⟨⟨LieHom.id, Function.injective_id, fun x => ?_⟩⟩
  rw [rCheckN_one_inv_one]
  ext ⟨a1, a2⟩ ⟨b1, b2⟩
  simp only [Matrix.mul_apply, Matrix.of_apply, Fintype.sum_prod_type, primDelta,
    Prod.swap_prod_mk, Prod.ext_iff, LieHom.coe_id, id_eq]
  simp [ite_and, Finset.sum_ite_eq, eq_comm]
  ring

end QOU.StandardModel
