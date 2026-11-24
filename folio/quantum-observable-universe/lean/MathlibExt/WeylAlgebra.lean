import Mathlib.Algebra.RingQuot
import Mathlib.Algebra.FreeAlgebra

universe u
variable (K : Type u) [CommRing K]

inductive WeylGen
| X
| D

def weylRel : FreeAlgebra K WeylGen → FreeAlgebra K WeylGen → Prop
| a, b => a = FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1 ∧ b = 0

def WeylAlgebra := RingQuot (weylRel K)

instance : Ring (WeylAlgebra K) := RingQuot.instRing (weylRel K)
instance : Algebra K (WeylAlgebra K) := RingQuot.instAlgebra (weylRel K)

namespace WeylAlgebra

/-- The position generator `x`, defined via `mkAlgHom` so `liftAlgHom_mkAlgHom_apply` fires. -/
def X : WeylAlgebra K := (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.X)
/-- The momentum generator `∂`, defined via `mkAlgHom` so `liftAlgHom_mkAlgHom_apply` fires. -/
def D : WeylAlgebra K := (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D)

/-- The commutation relation `[∂, x] = 1`. -/
lemma D_X_sub_X_D : D K * X K - X K * D K = 1 := by
  have H : (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) =
           (RingQuot.mkAlgHom K (weylRel K)) 0 :=
    RingQuot.mkAlgHom_rel K ⟨rfl, rfl⟩
  rw [map_zero] at H
  have H1 : (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 = 0 := by
    calc (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1
      _ = (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - (RingQuot.mkAlgHom K (weylRel K)) 1 := by rw [map_one]
      _ = (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) := by rw [← map_sub]
      _ = 0 := H
  have H2 : D K * X K - X K * D K - 1 = 0 := by
    unfold D X
    calc (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D) * (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.X) - (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.X) * (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D) - 1
      _ = (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X) - (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 := by rw [map_mul, map_mul]
      _ = (RingQuot.mkAlgHom K (weylRel K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 := by rw [← map_sub]
      _ = 0 := H1
  exact sub_eq_zero.mp H2

def FourierLaplaceFreeGen : WeylGen → FreeAlgebra K WeylGen
| WeylGen.X => -(FreeAlgebra.ι K WeylGen.D)
| WeylGen.D => FreeAlgebra.ι K WeylGen.X

def FourierLaplaceFree : FreeAlgebra K WeylGen →ₐ[K] FreeAlgebra K WeylGen :=
  FreeAlgebra.lift K (FourierLaplaceFreeGen K)

lemma FourierLaplaceFree_D_X_sub_X_D :
  FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1)
  = FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1 := by
  have H1 : FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) =
    FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D) * FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.X) -
    FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.X) * FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D) - FourierLaplaceFree K 1 := by
    simp
  rw [H1]
  have hd : FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D) = FreeAlgebra.ι K WeylGen.X := by
    change FreeAlgebra.lift K (FourierLaplaceFreeGen K) (FreeAlgebra.ι K WeylGen.D) = _
    simp [FourierLaplaceFreeGen]
  have hx : FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.X) = -FreeAlgebra.ι K WeylGen.D := by
    change FreeAlgebra.lift K (FourierLaplaceFreeGen K) (FreeAlgebra.ι K WeylGen.X) = _
    simp [FourierLaplaceFreeGen]
  rw [hd, hx, map_one]
  have eq : FreeAlgebra.ι K WeylGen.X * -FreeAlgebra.ι K WeylGen.D - -FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X = FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D := by
    calc FreeAlgebra.ι K WeylGen.X * -FreeAlgebra.ι K WeylGen.D - -FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X
      _ = - (FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - (- (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X)) := by
        rw [mul_neg, neg_mul]
      _ = - (FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) + FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X := by rw [sub_neg_eq_add]
      _ = FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D := by rw [add_comm, sub_eq_add_neg]
  rw [eq]

def FourierLaplace : WeylAlgebra K →ₐ[K] WeylAlgebra K :=
  RingQuot.liftAlgHom K 
    ⟨(RingQuot.mkAlgHom K (weylRel K)).comp (FourierLaplaceFree K), by
      intro a b h
      rcases h with ⟨rfl, rfl⟩
      show ((RingQuot.mkAlgHom K (weylRel K)).comp (FourierLaplaceFree K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) = ((RingQuot.mkAlgHom K (weylRel K)).comp (FourierLaplaceFree K)) 0
      have h2 : FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) =
               FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1 := FourierLaplaceFree_D_X_sub_X_D K
      have h3 : ((RingQuot.mkAlgHom K (weylRel K)).comp (FourierLaplaceFree K)) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) =
               RingQuot.mkAlgHom K (weylRel K) (FourierLaplaceFree K (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1)) := rfl
      rw [h3, h2]
      have H'' : RingQuot.mkAlgHom K (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) =
                 RingQuot.mkAlgHom K (weylRel K) 0 :=
        RingQuot.mkAlgHom_rel K ⟨rfl, rfl⟩
      rw [map_zero] at H''
      rw [H'']
      have h4 : ((RingQuot.mkAlgHom K (weylRel K)).comp (FourierLaplaceFree K)) 0 = 0 := map_zero _
      rw [h4]
    ⟩

/-- FL on the X generator: `FL(x) = −∂`. -/
lemma FourierLaplace_X : FourierLaplace K (X K) = -(D K) := by
  unfold X D FourierLaplace FourierLaplaceFree
  erw [RingQuot.liftAlgHom_mkAlgHom_apply]
  change (RingQuot.mkAlgHom K (weylRel K)) ((FreeAlgebra.lift K (FourierLaplaceFreeGen K)) (FreeAlgebra.ι K WeylGen.X)) = _
  rw [FreeAlgebra.lift_ι_apply]
  change (RingQuot.mkAlgHom K (weylRel K)) (FourierLaplaceFreeGen K WeylGen.X) = _
  simp [FourierLaplaceFreeGen, map_neg]

/-- FL on the D generator: `FL(∂) = x`. -/
lemma FourierLaplace_D : FourierLaplace K (D K) = X K := by
  unfold X D FourierLaplace FourierLaplaceFree
  erw [RingQuot.liftAlgHom_mkAlgHom_apply]
  change (RingQuot.mkAlgHom K (weylRel K)) ((FreeAlgebra.lift K (FourierLaplaceFreeGen K)) (FreeAlgebra.ι K WeylGen.D)) = _
  rw [FreeAlgebra.lift_ι_apply]
  simp [FourierLaplaceFreeGen]

/-- FL² on X: `FL(FL(x)) = FL(−∂) = −FL(∂) = −x`. FL is order 4, NOT 2! -/
lemma FourierLaplace_sq_X : FourierLaplace K (FourierLaplace K (X K)) = -(X K) := by
  rw [FourierLaplace_X, map_neg, FourierLaplace_D]

/-- FL² on D: `FL(FL(∂)) = FL(x) = −∂`. -/
lemma FourierLaplace_sq_D : FourierLaplace K (FourierLaplace K (D K)) = -(D K) := by
  rw [FourierLaplace_D, FourierLaplace_X]

/-- FL⁴ on X = X. Chain: FL(X)=−D, FL(−D)=−X, FL(−X)=D, FL(D)=X. -/
lemma FourierLaplace_four_X :
    FourierLaplace K (FourierLaplace K (FourierLaplace K (FourierLaplace K (X K)))) = X K := by
  rw [FourierLaplace_X, map_neg, FourierLaplace_D]
  -- now: FL(FL(−(X K))) = X K
  rw [map_neg, FourierLaplace_X]
  -- now: FL(−(−(D K))) = X K
  simp [FourierLaplace_D]

/-- FL⁴ on D = D. Chain: FL(D)=X, FL(X)=−D, FL(−D)=−X, FL(−X)=D. -/
lemma FourierLaplace_four_D :
    FourierLaplace K (FourierLaplace K (FourierLaplace K (FourierLaplace K (D K)))) = D K := by
  rw [FourierLaplace_D, FourierLaplace_X, map_neg, FourierLaplace_D]
  -- now: FL(−(X K)) = D K
  rw [map_neg, FourierLaplace_X]
  simp

end WeylAlgebra
