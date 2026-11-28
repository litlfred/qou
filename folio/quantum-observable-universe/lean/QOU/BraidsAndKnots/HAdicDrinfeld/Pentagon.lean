import QOU.BraidsAndKnots.HAdicDrinfeld.Hexagon

/-!
# The pentagon for a rational associator on four strands

Epic `qou-dk7p`, step B of `docs/audits/2026-11-27-kz-trio-strangler-plan.md`.

A rational associator `Φ` satisfies the pentagon in the universal truncated algebra `U4 N`
(`RationalAssociator.Pentagon` at the family `t₁₂, t₁₃, t₂₃, t₂₄, t₃₄`). This file carries it to
`A^{⊗4}` through a `CasimirData`, in the quasi-Hopf form

  `(id ⊗ id ⊗ Δ)(Φ) · (Δ ⊗ id ⊗ id)(Φ) = (1 ⊗ Φ) · (id ⊗ Δ ⊗ id)(Φ) · (Φ ⊗ 1)`,

where `Φ = assoc3 ∈ A^{⊗3}` is the `realize3`-image of `φ(t₁₂, t₂₃)`, i.e. `φ(c t₁₂, c t₂₃)`.

* `face0 … face4`: the five coface algebra maps `A^{⊗3} → A^{⊗4}`;
* `face*_leg12`, `face*_leg23`: their values on the two leg copies, by tensor induction;
* `face*_t`: with the splitting identities of `CasimirData`, the images of `t₁₂, t₂₃` are the
  sums of four-strand legs that the pentagon needs;
* `pentagon`: the displayed identity, from the pentagon in `U4 N` mapped by `CasimirData.evalU4`.

The hypothesis is the pentagon alone (not `AssocU4`), so it does not depend on the choice of the
exponential `E`. No analysis and no numerical value is used.
-/

namespace QOU.BraidsAndKnots.HAdicDrinfeld

open scoped TensorProduct
open QOU.HeckeTemperleyLieb.QuasiYangBaxterFromHexagon
open QOU.BraidsAndKnots.RationalAssociator
open Algebra.TensorProduct

set_option linter.unusedSectionVars false

variable {k A : Type*} [CommRing k] [Algebra ℚ k] [Ring A] [Algebra k A] [Algebra ℚ A]
  [IsScalarTower ℚ k A]

namespace CasimirData

variable (D : CasimirData k A)

/-- `1 ⊗ x`. -/
noncomputable def face0 (_D : CasimirData k A) : T3 k A →ₐ[k] T4 k A := omit1

/-- `(Δ ⊗ id ⊗ id)`. -/
noncomputable def face1 : T3 k A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.map (Algebra.TensorProduct.map D.Δ (AlgHom.id k A)) (AlgHom.id k A)

/-- `(id ⊗ Δ ⊗ id)`. -/
noncomputable def face2 : T3 k A →ₐ[k] T4 k A :=
  Algebra.TensorProduct.map
    ((Algebra.TensorProduct.assoc k k A A A).symm.toAlgHom.comp
      (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ)) (AlgHom.id k A)

/-- `(id ⊗ id ⊗ Δ)`. -/
noncomputable def face3 : T3 k A →ₐ[k] T4 k A :=
  (Algebra.TensorProduct.assoc k k (A ⊗[k] A) A A).symm.toAlgHom.comp
    (Algebra.TensorProduct.map (AlgHom.id k (A ⊗[k] A)) D.Δ)

/-- `x ⊗ 1`. -/
noncomputable def face4 (_D : CasimirData k A) : T3 k A →ₐ[k] T4 k A := omit4

section Legs

theorem face1_leg12 (x : A ⊗[k] A) :
    D.face1 (leg12 x) = omit4 (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) x) := by
  simp [face1, omit4, leg12, map_tmul, includeLeft_apply]

theorem face2_leg12 (x : A ⊗[k] A) :
    D.face2 (leg12 x) = omit4 ((Algebra.TensorProduct.assoc k k A A A).symm
      (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ x)) := by
  simp [face2, omit4, leg12, map_tmul, includeLeft_apply]

theorem face3_leg12 (x : A ⊗[k] A) : D.face3 (leg12 x) = omit4 (leg12 x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp [leg12]
  | tmul a b =>
    simp [face3, omit4, leg12, map_tmul, includeLeft_apply, Algebra.TensorProduct.one_def,
      assoc_symm_tmul]
  | add x y hx hy => simp only [CasimirData.leg12_add, map_add, hx, hy]

theorem face1_leg23 (x : A ⊗[k] A) : D.face1 (leg23 x) = omit2 (leg23 x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b => simp [face1, omit2, leg13, leg23, map_tmul, includeLeft_apply, includeRight_apply,
      Algebra.TensorProduct.one_def]
  | add x y hx hy => simp only [map_add, hx, hy]

theorem face2_leg23 (x : A ⊗[k] A) :
    D.face2 (leg23 x) = omit1 (Algebra.TensorProduct.map D.Δ (AlgHom.id k A) x) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [face2, omit1, leg23, map_tmul, includeRight_apply, AlgHom.id_apply,
      AlgHom.coe_comp, Function.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe]
    induction D.Δ a using TensorProduct.induction_on with
    | zero => simp
    | tmul u v => simp [map_tmul, includeRight_apply, assoc_symm_tmul]
    | add u v hu hv => simp only [TensorProduct.tmul_add, TensorProduct.add_tmul, map_add, hu, hv]
  | add x y hx hy => simp only [map_add, hx, hy]

theorem face3_leg23 (x : A ⊗[k] A) :
    D.face3 (leg23 x) = omit1 ((Algebra.TensorProduct.assoc k k A A A).symm
      (Algebra.TensorProduct.map (AlgHom.id k A) D.Δ x)) := by
  induction x using TensorProduct.induction_on with
  | zero => simp
  | tmul a b =>
    simp only [face3, omit1, leg23, map_tmul, includeRight_apply, AlgHom.id_apply,
      AlgHom.coe_comp, Function.comp_apply, AlgEquiv.toAlgHom_eq_coe, AlgHom.coe_coe]
    induction D.Δ b using TensorProduct.induction_on with
    | zero => simp
    | tmul u v => simp [map_tmul, includeRight_apply, assoc_symm_tmul]
    | add u v hu hv => simp only [TensorProduct.tmul_add, map_add, hu, hv]
  | add x y hx hy => simp only [map_add, hx, hy]

end Legs

/-! ### The images of `t₁₂` and `t₂₃` -/

theorem face0_t12 : D.face0 (leg12 D.t) = D.t4 3 := omit1_leg12 _
theorem face0_t23 : D.face0 (leg23 D.t) = D.t4 5 := omit1_leg23 _
theorem face4_t12 : D.face4 (leg12 D.t) = D.t4 0 := rfl
theorem face4_t23 : D.face4 (leg23 D.t) = D.t4 3 := rfl
theorem face1_t12 : D.face1 (leg12 D.t) = D.t4 1 + D.t4 3 := by
  rw [face1_leg12, D.split_left, map_add]; rfl
theorem face1_t23 : D.face1 (leg23 D.t) = D.t4 5 := D.face1_leg23 _
theorem face2_t12 : D.face2 (leg12 D.t) = D.t4 0 + D.t4 1 := by
  rw [face2_leg12, D.split_right, map_add]; rfl
theorem face2_t23 : D.face2 (leg23 D.t) = D.t4 4 + D.t4 5 := by
  rw [face2_leg23, D.split_left, map_add, omit1_leg13, omit1_leg23]; rfl
theorem face3_t12 : D.face3 (leg12 D.t) = D.t4 0 := D.face3_leg12 _
theorem face3_t23 : D.face3 (leg23 D.t) = D.t4 3 + D.t4 4 := by
  rw [face3_leg23, D.split_right, map_add, omit1_leg12, omit1_leg13]; rfl

/-! ### The pentagon -/

variable {N : ℕ} (c : k) (hc : c ^ N = 0)

/-- The associator on three strands, `φ(c t₁₂, c t₂₃)`. -/
noncomputable def assoc3 (Φ : FreeAlgebra ℚ (Fin 2)) : T3 k A :=
  D.realize3 N c hc (eval (RationalAssociator.t N 0) (RationalAssociator.t N 3) Φ)

theorem assoc3_eq (Φ : FreeAlgebra ℚ (Fin 2)) :
    D.assoc3 c hc Φ = eval (c • leg12 D.t) (c • leg23 D.t) Φ := by
  rw [assoc3, map_eval, realize3_t, realize3_t]; rfl

theorem face_assoc3 (f : T3 k A →ₐ[k] T4 k A) (Φ : FreeAlgebra ℚ (Fin 2)) :
    f (D.assoc3 c hc Φ) = eval (c • f (leg12 D.t)) (c • f (leg23 D.t)) Φ := by
  rw [assoc3_eq]
  refine (map_eval (A := T3 k A) (B := T4 k A) (f.restrictScalars ℚ) _ _ Φ).trans ?_
  rw [AlgHom.restrictScalars_apply, AlgHom.restrictScalars_apply, map_smul, map_smul]

/-- **The pentagon on four strands.** If `Φ` satisfies the pentagon in `U4 N`, then
`Φ = assoc3` satisfies

  `(id ⊗ id ⊗ Δ)(Φ) · (Δ ⊗ id ⊗ id)(Φ) = (1 ⊗ Φ) · (id ⊗ Δ ⊗ id)(Φ) · (Φ ⊗ 1)`

in `A^{⊗4}`. -/
theorem pentagon {Φ : FreeAlgebra ℚ (Fin 2)}
    (hp : Pentagon Φ (RationalAssociator.t N 0) (RationalAssociator.t N 1)
      (RationalAssociator.t N 3) (RationalAssociator.t N 4) (RationalAssociator.t N 5)) :
    D.face3 (D.assoc3 c hc Φ) * D.face1 (D.assoc3 c hc Φ) =
      D.face0 (D.assoc3 c hc Φ) * D.face2 (D.assoc3 c hc Φ) * D.face4 (D.assoc3 c hc Φ) := by
  have key := congrArg (D.evalU4 N c hc) hp
  simp only [map_mul] at key
  have hm : ∀ a b, D.evalU4 N c hc (eval a b Φ) =
      eval (D.evalU4 N c hc a) (D.evalU4 N c hc b) Φ := fun a b =>
    map_eval (A := U4 N) (B := T4 k A) (D.evalU4 N c hc) a b Φ
  rw [hm, hm, hm, hm, hm] at key
  simp only [map_add, evalU4_t] at key
  simp only [face_assoc3, face0_t12, face0_t23, face1_t12, face1_t23, face2_t12, face2_t23,
    face3_t12, face3_t23, face4_t12, face4_t23, smul_add]
  exact key

end CasimirData

end QOU.BraidsAndKnots.HAdicDrinfeld
