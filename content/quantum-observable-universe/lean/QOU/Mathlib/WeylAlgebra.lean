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

def X : WeylAlgebra K := RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X)
def D : WeylAlgebra K := RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D)

lemma D_X_sub_X_D : D K * X K - X K * D K = 1 := by
  have H : RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) = RingQuot.mkRingHom (weylRel K) 0 := by
    apply RingQuot.mkRingHom_rel
    exact ⟨rfl, rfl⟩
  rw [map_zero] at H
  have H1 : RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 = 0 := by
    calc RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1
      _ = RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - RingQuot.mkRingHom (weylRel K) 1 := by rw [map_one]
      _ = RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D - 1) := by rw [← map_sub]
      _ = 0 := H
  have H2 : RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D) * RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X) - RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X) * RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D) - 1 = 0 := by
    calc RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D) * RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X) - RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X) * RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D) - 1
      _ = RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X) - RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 := by rw [map_mul, map_mul]
      _ = RingQuot.mkRingHom (weylRel K) (FreeAlgebra.ι K WeylGen.D * FreeAlgebra.ι K WeylGen.X - FreeAlgebra.ι K WeylGen.X * FreeAlgebra.ι K WeylGen.D) - 1 := by rw [← map_sub]
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

lemma FourierLaplace_involutive (a : WeylAlgebra K) : FourierLaplace K (FourierLaplace K a) = a := by
  sorry

end WeylAlgebra
