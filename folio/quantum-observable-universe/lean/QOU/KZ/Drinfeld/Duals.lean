import QOU.KZ.Drinfeld.Monoidal
import QOU.KZ.ZigZag
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import QOU.MathlibExt.RigidTensorDual

/-!
# Duals in `D_ℏ`: the exact pairing `(V, V)` for small transcendental `ℏ`

Stage S4 of bean `qou-zoyv`. The associator of `D_ℏ` on `(V ⊗ V) ⊗ V` is, after relabelling the
three legs as `Fin 3`, the matrix `ZigZag.assoc = Φ_KZ(ℏ P₁₂, ℏ P₂₃)`. Through that relabelling the
zigzag composites of `(η, ν⁻¹ ε)` become `ZigZag.zigzag_identities`, so for
`ℏ` transcendental with `‖ℏ‖ ≤ 1/12` the object `V` is self-dual in `D_ℏ`. Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S4)
-/

noncomputable section

namespace QOU.KZ.Drinfeld

open QOU.KZ.DrinfeldAssociator CategoryTheory MonoidalCategory Finset QOU.KZ.FuchsianFormal QOU.KZ.BlockResidues
  QOU.KZ.KZPentagon QOU.KZ.GLnKZ QOU.KZ.ZigZag Obj

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

/-! ### Relabelling the legs of `(V ⊗ V) ⊗ V` -/

/-- The legs of `(V ⊗ V) ⊗ V` are `0, 1, 2`. -/
def e3L : Leaves (tensor (tensor V V) V) ≃ Fin 3 where
  toFun
    | Sum.inl (Sum.inl _) => 0
    | Sum.inl (Sum.inr _) => 1
    | Sum.inr _ => 2
  invFun i := if i = 0 then Sum.inl (Sum.inl ()) else if i = 1 then Sum.inl (Sum.inr ())
    else Sum.inr ()
  left_inv k := by rcases k with (k | k) | k <;> rfl
  right_inv i := by fin_cases i <;> rfl

theorem tB_single (i j : Fin 3) : tB ℂ 2 {i} {j} = P 2 i j := by
  simp [tB]; rfl

theorem e3_blkX : (blkX V V V).map e3L.toEmbedding = {0} := by
  ext i; fin_cases i <;> simp [blkX, e3L]
theorem e3_blkY : (blkY V V V).map e3L.toEmbedding = {1} := by
  ext i; fin_cases i <;> simp [blkY, e3L]
theorem e3_blkZ : (blkZ V V V).map e3L.toEmbedding = {2} := by
  ext i; fin_cases i <;> simp [blkZ, e3L]

variable {c : ℂ}

theorem ΦB_fin3 (hc : Transcendental ℚ c) (hs : ‖c‖ < 1 / 2) :
    ΦB kz hc ({0} : Finset (Fin 3)) {1} {2} = assoc hs :=
  KZShiftPhi.Φ_congr (by rw [tB_single]) (by rw [tB_single]) _ _ _ _

/-- The associator on `(V ⊗ V) ⊗ V` is `ZigZag.assoc`, relabelled. -/
theorem αmat_VVV (hc : Transcendental ℚ c) (hs : ‖c‖ < 1 / 2) :
    αmat kz hc V V V = reidx (assocLegs V V V) * (reidx e3L.symm * assoc hs * reidx e3L) := by
  have h := reidx_ΦB kz hc e3L (blkX V V V) (blkY V V V) (blkZ V V V)
  rw [e3_blkX, e3_blkY, e3_blkZ, ΦB_fin3 hc hs] at h
  have hΦ : ΦB kz hc (blkX V V V) (blkY V V V) (blkZ V V V) =
      reidx e3L.symm * (assoc hs * reidx e3L) := by
    rw [← h, ← Matrix.mul_assoc, reidx_mul, Equiv.self_trans_symm, reidx_refl, Matrix.one_mul]
  rw [αmat, hΦ, Matrix.mul_assoc (reidx e3L.symm)]

theorem αinv_VVV (hc : Transcendental ℚ c) (hs : ‖c‖ < 1 / 2) :
    αinv kz hc V V V = reidx e3L.symm * assocInv hs * reidx e3L * reidx (assocLegs V V V).symm := by
  set R := reidx e3L.symm * assocInv hs * reidx e3L * reidx (assocLegs V V V).symm
  have hR : αmat kz hc V V V * R = 1 := by
    rw [αmat_VVV hc hs]
    simp only [R, Matrix.mul_assoc]
    rw [← Matrix.mul_assoc (reidx e3L) (reidx e3L.symm), reidx_mul, Equiv.symm_trans_self,
      reidx_refl, Matrix.one_mul, ← Matrix.mul_assoc (assoc hs), (assoc_mul_assocInv hs).1,
      Matrix.one_mul, ← Matrix.mul_assoc (reidx e3L.symm) (reidx e3L), reidx_mul, Equiv.self_trans_symm,
      reidx_refl, Matrix.one_mul, reidx_mul, Equiv.symm_trans_self, reidx_refl]
  calc αinv kz hc V V V = αinv kz hc V V V * (αmat kz hc V V V * R) := by rw [hR, Matrix.mul_one]
    _ = R := by rw [← Matrix.mul_assoc, αinv_mul_αmat, Matrix.one_mul]

/-! ### The pairing matrices -/

/-- `r · ε : V ⊗ V → 𝟙`. -/
def epsL (r : ℂ) : Matrix (Idx unit) (Idx (tensor V V)) ℂ :=
  Matrix.of fun _ x => r * eps (x (Sum.inl ())) (x (Sum.inr ()))

/-- `η : 𝟙 → V ⊗ V`. -/
def etaL : Matrix (Idx (tensor V V)) (Idx unit) ℂ :=
  Matrix.of fun y _ => eps (y (Sum.inl ())) (y (Sum.inr ()))

/-- `V ⊗ 𝟙 ≅ ℂ²`. -/
def Uout : Matrix (Idx (tensor V unit)) (Fin 2) ℂ :=
  Matrix.of fun y a => if y (Sum.inl ()) = a then 1 else 0

/-- `ℂ² ≅ 𝟙 ⊗ V`. -/
def Uin : Matrix (Fin 2) (Idx (tensor unit V)) ℂ :=
  Matrix.of fun b x => if x (Sum.inr ()) = b then 1 else 0

theorem zig_left (r : ℂ) :
    kron (1 : EndL (Leaves V)) (epsL r) * reidx (assocLegs V V V) * reidx e3L.symm =
      r • (Uout * E1) := by
  rw [Matrix.mul_assoc, reidx_mul]
  ext y x
  rw [mul_reidx_apply, kron_apply]
  simp [Matrix.mul_apply, Uout, E1, epsL, Matrix.one_apply, e3L, assocLegs, funext_iff,
    Unique.forall_iff]

theorem zig_right :
    reidx e3L * kron etaL (1 : EndL (Leaves V)) = E2 * Uin := by
  ext x w
  rw [reidx_mul_apply, kron_apply]
  simp [Matrix.mul_apply, Uin, E2, etaL, Matrix.one_apply, e3L, funext_iff, Unique.forall_iff]

theorem Uout_mul_Uin :
    Uout * Uin = reidx (rightLegs V).symm * reidx (leftLegs V) := by
  rw [reidx_mul]
  ext y x
  simp [Matrix.mul_apply, Uout, Uin, reidx, funext_iff, Unique.forall_iff, leftLegs, rightLegs]
  exact if_congr eq_comm rfl rfl

/-- `ℂ² ≅ 𝟙 ⊗ V` read on the right. -/
def Uin' : Matrix (Idx (tensor unit V)) (Fin 2) ℂ :=
  Matrix.of fun y a => if y (Sum.inr ()) = a then 1 else 0

/-- `V ⊗ 𝟙 ≅ ℂ²` read on the left. -/
def Uout' : Matrix (Fin 2) (Idx (tensor V unit)) ℂ :=
  Matrix.of fun b x => if x (Sum.inl ()) = b then 1 else 0

theorem zag_left (r : ℂ) :
    kron (epsL r) (1 : EndL (Leaves V)) * reidx e3L.symm = r • (Uin' * E1') := by
  ext y x
  rw [mul_reidx_apply, kron_apply]
  simp [Matrix.mul_apply, Uin', E1', epsL, Matrix.one_apply, e3L, funext_iff, Unique.forall_iff]

theorem zag_right :
    reidx e3L * reidx (assocLegs V V V).symm * kron (1 : EndL (Leaves V)) etaL = E2' * Uout' := by
  rw [reidx_mul]
  ext x w
  rw [reidx_mul_apply, kron_apply]
  simp [Matrix.mul_apply, Uout', E2', etaL, Matrix.one_apply, e3L, assocLegs, funext_iff,
    Unique.forall_iff]

theorem Uin'_mul_Uout' :
    Uin' * Uout' = reidx (leftLegs V).symm * reidx (rightLegs V) := by
  rw [reidx_mul]
  ext y x
  simp [Matrix.mul_apply, Uout', Uin', reidx, funext_iff, Unique.forall_iff, leftLegs, rightLegs]
  exact if_congr eq_comm rfl rfl

theorem sum_idxV {M : Type*} [AddCommMonoid M] (F : (Unit → Fin 2) → M) :
    ∑ u, F u = F (fun _ => 0) + F (fun _ => 1) := by
  rw [← (Equiv.funUnique Unit (Fin 2)).symm.sum_comp, Fin.sum_univ_two]
  rfl

theorem equivariant_etaL : Equivariant (X := unit) (Y := tensor V V) etaL := by
  intro a ha
  rw [Matrix.trace_fin_two] at ha
  ext y w
  simp [Matrix.mul_apply, kron_apply, ρ, etaL, sum_sumArrow, sum_idxV, Matrix.one_apply,
    funext_iff, Unique.forall_iff]
  generalize y (Sum.inl ()) = i
  generalize y (Sum.inr ()) = j
  fin_cases i <;> fin_cases j <;> simp [eps]
  all_goals first | exact ha | (rw [← neg_add, ha, neg_zero])

theorem equivariant_epsL (r : ℂ) : Equivariant (X := tensor V V) (Y := unit) (epsL r) := by
  intro a ha
  rw [Matrix.trace_fin_two] at ha
  ext w x
  simp [Matrix.mul_apply, kron_apply, ρ, epsL, sum_sumArrow, sum_idxV, Matrix.one_apply,
    funext_iff, Unique.forall_iff]
  generalize x (Sum.inl ()) = i
  generalize x (Sum.inr ()) = j
  fin_cases i <;> fin_cases j <;> simp [eps]
  all_goals first | exact Or.inr ha | exact Or.inr (by rw [add_comm]; exact ha)

/-! ### The zigzag identities in matrix form -/

/-- The zigzag scalar `ν = zig(Φ)₀₀`. -/
def νV (hs : ‖c‖ < 1 / 2) : ℂ := zig (assoc hs) 0 0

theorem zig_mat (hc : Transcendental ℚ c) (hs : ‖c‖ < 1 / 2) (hν : νV hs ≠ 0) :
    kron (1 : EndL (Leaves V)) (epsL (νV hs)⁻¹) * αmat kz hc V V V *
        kron etaL (1 : EndL (Leaves V)) =
      reidx (rightLegs V).symm * reidx (leftLegs V) := by
  rw [αmat_VVV hc hs, ← Uout_mul_Uin]
  calc kron (1 : EndL (Leaves V)) (epsL (νV hs)⁻¹) *
        (reidx (assocLegs V V V) * (reidx e3L.symm * assoc hs * reidx e3L)) *
          kron etaL (1 : EndL (Leaves V))
      = (kron (1 : EndL (Leaves V)) (epsL (νV hs)⁻¹) * reidx (assocLegs V V V) *
          reidx e3L.symm) * assoc hs * (reidx e3L * kron etaL (1 : EndL (Leaves V))) := by
        simp only [Matrix.mul_assoc]
    _ = ((νV hs)⁻¹ • (Uout * E1)) * assoc hs * (E2 * Uin) := by rw [zig_left, zig_right]
    _ = (νV hs)⁻¹ • (Uout * zig (assoc hs) * Uin) := by
        simp only [zig, Matrix.smul_mul, Matrix.mul_assoc]
    _ = Uout * Uin := by
        rw [zig_scalar hs, show zig (assoc hs) 0 0 = νV hs from rfl, Matrix.mul_smul,
          Matrix.smul_mul, smul_smul, inv_mul_cancel₀ hν, one_smul, Matrix.mul_one]

theorem zag_mat (hc : Transcendental ℚ c) (hs : ‖c‖ < 1 / 2) (hν : νV hs ≠ 0) :
    kron (epsL (νV hs)⁻¹) (1 : EndL (Leaves V)) * αinv kz hc V V V *
        kron (1 : EndL (Leaves V)) etaL =
      reidx (leftLegs V).symm * reidx (rightLegs V) := by
  rw [αinv_VVV hc hs, ← Uin'_mul_Uout']
  calc kron (epsL (νV hs)⁻¹) (1 : EndL (Leaves V)) *
        (reidx e3L.symm * assocInv hs * reidx e3L * reidx (assocLegs V V V).symm) *
          kron (1 : EndL (Leaves V)) etaL
      = (kron (epsL (νV hs)⁻¹) (1 : EndL (Leaves V)) * reidx e3L.symm) * assocInv hs *
          (reidx e3L * reidx (assocLegs V V V).symm * kron (1 : EndL (Leaves V)) etaL) := by
        simp only [Matrix.mul_assoc]
    _ = ((νV hs)⁻¹ • (Uin' * E1')) * assocInv hs * (E2' * Uout') := by rw [zag_left, zag_right]
    _ = (νV hs)⁻¹ • (Uin' * zag (assocInv hs) * Uout') := by
        simp only [zag, Matrix.smul_mul, Matrix.mul_assoc]
    _ = Uin' * Uout' := by
        rw [zag_eq_zig hs, zig_scalar hs, show zig (assoc hs) 0 0 = νV hs from rfl,
          Matrix.mul_smul, Matrix.smul_mul, smul_smul, inv_mul_cancel₀ hν, one_smul,
          Matrix.mul_one]

theorem νV_ne_zero (hsm : ‖c‖ ≤ 1 / 12) : νV (c := c) (by linarith) ≠ 0 := zig_ne_zero hsm

/-! ### `V` is self-dual in `D_ℏ` -/

section Pairing

variable (c) [hc : Fact (Transcendental ℚ c)] [hsm : Fact (‖c‖ ≤ 1 / 12)]

/-- **`V` is self-dual in `D_ℏ`** for `ℏ` transcendental with `‖ℏ‖ ≤ 1/12`:
`η = e₀ ⊗ e₁ − e₁ ⊗ e₀`, `ε' = ν⁻¹ ε`, `ν = zig(Φ)₀₀ ≠ 0`. -/
instance exactPairingV : ExactPairing (C := DH kz c) Obj.V Obj.V where
  coevaluation' := ⟨etaL, equivariant_etaL⟩
  evaluation' := ⟨epsL (νV (c := c) (by linarith [hsm.out]))⁻¹, equivariant_epsL _⟩
  coevaluation_evaluation' := hom_ext (by
    show kron (epsL (νV (c := c) (by linarith [hsm.out]))⁻¹) (1 : EndL (Leaves V)) *
        αinv kz hc.out V V V * kron (1 : EndL (Leaves V)) etaL =
      reidx (leftLegs V).symm * reidx (rightLegs V)
    exact zag_mat hc.out _ (νV_ne_zero hsm.out))
  evaluation_coevaluation' := hom_ext (by
    show kron (1 : EndL (Leaves V)) (epsL (νV (c := c) (by linarith [hsm.out]))⁻¹) *
        αmat kz hc.out V V V * kron etaL (1 : EndL (Leaves V)) =
      reidx (rightLegs V).symm * reidx (leftLegs V)
    exact zig_mat hc.out _ (νV_ne_zero hsm.out))

/-- The dual word: `𝟙ᘁ = 𝟙`, `Vᘁ = V`, `(X ⊗ Y)ᘁ = Yᘁ ⊗ Xᘁ`. -/
def dualObj : Obj → Obj
  | .unit => .unit
  | .V => .V
  | .tensor X Y => .tensor (dualObj Y) (dualObj X)

/-- The exact pairing `(X, Xᘁ)`, built from `(V, V)` by `tensorExactPairing`. -/
def pairing : (X : Obj) → ExactPairing (C := DH kz c) X (dualObj X)
  | .unit => (exactPairingUnit : ExactPairing (C := DH kz c) (𝟙_ (DH kz c)) (𝟙_ (DH kz c)))
  | .V => exactPairingV c
  | .tensor X Y =>
      @QOU.MathlibExt.tensorExactPairing (DH kz c) _ _ X (dualObj X) Y (dualObj Y)
        (pairing X) (pairing Y)

/-- **`D_ℏ` is right rigid** for `ℏ` transcendental with `‖ℏ‖ ≤ 1/12`. -/
instance rightRigid : RightRigidCategory (DH kz c) where
  rightDual X := ({ rightDual := (dualObj X : DH kz c), exact := pairing c X } : HasRightDual (C := DH kz c) X)

end Pairing

end QOU.KZ.Drinfeld
