/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.FormalGroups.CoproductDescent
import Mathlib.RingTheory.Bialgebra.Basic

/-!
# Bialgebra structures on the splay algebra and on `U`

Thm. 3.7 of arXiv:math/0602138 (Leitner), the bialgebra half.

* `splayBialgebra`: the splay `T = ∐ᵢ Aᵢ` of bialgebras is a bialgebra, with the factorwise
  coproduct and counit.
* `quotBialgebra`: if `π` is strongly multiplicative for that coproduct (Def. 1.11) and the
  counit kills `π`, then `U = T / J` is a bialgebra, with coproduct and counit descended from
  `T` (Prop. 1.13).

The counit hypothesis `ε ∘ π = 0` is taken as stated; it is not derived here from strong
multiplicativity. The coalgebra axioms are moved along an algebra map with `q`-compatible
coproduct and counit by the `transfer_*` lemmas, applied once to each `ιᵢ : Aᵢ → T` and once
to the quotient map `T → U`.
-/

namespace QOU.FormalGroups

open TensorProduct LinearAlgebra

noncomputable section

variable {R : Type*} [CommRing R]

section Transfer

variable {B : Type*} [Ring B] [Bialgebra R B] {U : Type*} [Ring U] [Algebra R U]
  (q : B →ₐ[R] U) (Δ : U →ₐ[R] U ⊗[R] U) (ε : U →ₐ[R] R)
  (hΔ : ∀ b, Δ (q b) = Algebra.TensorProduct.map q q (Coalgebra.comul b))
  (hε : ∀ b, ε (q b) = Coalgebra.counit b)

local notation "q2" => Algebra.TensorProduct.map q q
local notation "q3" => Algebra.TensorProduct.map q (Algebra.TensorProduct.map q q)

include hΔ in
theorem transfer_assoc_aux (y : B ⊗[R] B) :
    Algebra.TensorProduct.assoc R R U U U
        (Algebra.TensorProduct.map Δ (AlgHom.id R U) (q2 y)) =
      q3 (TensorProduct.assoc R B B B (LinearMap.rTensor B Coalgebra.comul y)) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | add y z h1 h2 => simp only [map_add, h1, h2]
  | tmul a c =>
    simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply, LinearMap.rTensor_tmul, hΔ]
    induction (Coalgebra.comul a : B ⊗[R] B) using TensorProduct.induction_on with
    | zero => simp
    | add y z h1 h2 => simp only [map_add, add_tmul, h1, h2]
    | tmul a1 a2 => simp

include hΔ in
theorem transfer_lassoc_aux (y : B ⊗[R] B) :
    Algebra.TensorProduct.map (AlgHom.id R U) Δ (q2 y) =
      q3 (LinearMap.lTensor B Coalgebra.comul y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | add y z h1 h2 => simp only [map_add, h1, h2]
  | tmul a c =>
    simp only [Algebra.TensorProduct.map_tmul, AlgHom.id_apply, LinearMap.lTensor_tmul, hΔ]

include hΔ in
theorem transfer_coassoc (b : B) :
    Algebra.TensorProduct.assoc R R U U U
        (Algebra.TensorProduct.map Δ (AlgHom.id R U) (Δ (q b))) =
      Algebra.TensorProduct.map (AlgHom.id R U) Δ (Δ (q b)) := by
  rw [hΔ, transfer_assoc_aux q Δ hΔ, transfer_lassoc_aux q Δ hΔ, Coalgebra.coassoc_apply]

include hε in
theorem transfer_rTensor_aux (y : B ⊗[R] B) :
    Algebra.TensorProduct.map ε (AlgHom.id R U) (q2 y) =
      Algebra.TensorProduct.map (AlgHom.id R R) q (LinearMap.rTensor B Coalgebra.counit y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | add y z h1 h2 => simp only [map_add, h1, h2]
  | tmul a c => simp [hε]

include hε in
theorem transfer_lTensor_aux (y : B ⊗[R] B) :
    Algebra.TensorProduct.map (AlgHom.id R U) ε (q2 y) =
      Algebra.TensorProduct.map q (AlgHom.id R R) (LinearMap.lTensor B Coalgebra.counit y) := by
  induction y using TensorProduct.induction_on with
  | zero => simp
  | add y z h1 h2 => simp only [map_add, h1, h2]
  | tmul a c => simp [hε]

include hΔ hε in
theorem transfer_rTensor (b : B) :
    Algebra.TensorProduct.map ε (AlgHom.id R U) (Δ (q b)) = 1 ⊗ₜ q b := by
  rw [hΔ, transfer_rTensor_aux q ε hε, Coalgebra.rTensor_counit_comul]
  simp

include hΔ hε in
theorem transfer_lTensor (b : B) :
    Algebra.TensorProduct.map (AlgHom.id R U) ε (Δ (q b)) = q b ⊗ₜ 1 := by
  rw [hΔ, transfer_lTensor_aux q ε hε, Coalgebra.lTensor_counit_comul]
  simp

end Transfer

section Splay

variable (R) {I : Type*} [DecidableEq I] (A : I → Type*) [∀ i, CommRing (A i)]
  [∀ i, Bialgebra R (A i)]

/-- The coproduct of the splay algebra `T = ∐ᵢ Aᵢ`: the unique algebra map that is the
coproduct of `Aᵢ` (composed with `ιᵢ ⊗ ιᵢ`) on each factor. -/
noncomputable def splayComul : SplayAlgebra R A →ₐ[R] SplayAlgebra R A ⊗[R] SplayAlgebra R A :=
  FreeProduct.lift R A fun {i} =>
    (Algebra.TensorProduct.map (FreeProduct.ι R A i) (FreeProduct.ι R A i)).comp
      (Bialgebra.comulAlgHom R (A i))

/-- The counit of the splay algebra: the counit of `Aᵢ` on each factor. -/
noncomputable def splayCounit : SplayAlgebra R A →ₐ[R] R :=
  FreeProduct.lift R A fun {i} => Bialgebra.counitAlgHom R (A i)

theorem splayComul_ι (i : I) (a : A i) :
    splayComul R A (FreeProduct.ι R A i a) =
      Algebra.TensorProduct.map (FreeProduct.ι R A i) (FreeProduct.ι R A i)
        (Coalgebra.comul a) := by
  rw [splayComul, ← AlgHom.comp_apply, FreeProduct.lift_comp_ι]; rfl

theorem splayCounit_ι (i : I) (a : A i) :
    splayCounit R A (FreeProduct.ι R A i a) = Coalgebra.counit a := by
  rw [splayCounit, ← AlgHom.comp_apply, FreeProduct.lift_comp_ι]; rfl

/-- Two algebra maps out of the splay algebra agree when they agree on every factor. -/
theorem splay_algHom_ext {B : Type*} [Semiring B] [Algebra R B]
    {f g : SplayAlgebra R A →ₐ[R] B}
    (h : ∀ i (a : A i), f (FreeProduct.ι R A i a) = g (FreeProduct.ι R A i a)) : f = g := by
  have hf := FreeProduct.lift_unique (R := R) (A := A)
    (maps := fun {i} => f.comp (FreeProduct.ι R A i)) f (fun _ => rfl)
  have hg := FreeProduct.lift_unique (R := R) (A := A)
    (maps := fun {i} => f.comp (FreeProduct.ι R A i)) g
    (fun i => AlgHom.ext fun a => (h i a).symm)
  rw [hf, hg]

theorem splay_coassoc :
    (Algebra.TensorProduct.assoc R R _ _ _).toAlgHom.comp
        ((Algebra.TensorProduct.map (splayComul R A) (.id R _)).comp (splayComul R A)) =
      (Algebra.TensorProduct.map (.id R _) (splayComul R A)).comp (splayComul R A) := by
  refine splay_algHom_ext R A fun i a => ?_
  exact transfer_coassoc (FreeProduct.ι R A i) (splayComul R A) (splayComul_ι R A i) a

theorem splay_rTensor :
    (Algebra.TensorProduct.map (splayCounit R A) (.id R _)).comp (splayComul R A) =
      (Algebra.TensorProduct.lid R (SplayAlgebra R A)).symm := by
  refine splay_algHom_ext R A fun i a => ?_
  exact transfer_rTensor (FreeProduct.ι R A i) (splayComul R A) (splayCounit R A)
    (splayComul_ι R A i) (splayCounit_ι R A i) a

theorem splay_lTensor :
    (Algebra.TensorProduct.map (.id R _) (splayCounit R A)).comp (splayComul R A) =
      (Algebra.TensorProduct.rid R R (SplayAlgebra R A)).symm := by
  refine splay_algHom_ext R A fun i a => ?_
  exact transfer_lTensor (FreeProduct.ι R A i) (splayComul R A) (splayCounit R A)
    (splayComul_ι R A i) (splayCounit_ι R A i) a

/-- **The splay of bialgebras is a bialgebra** (§1 of arXiv:math/0602138): the coproduct
and counit are the factorwise ones. -/
noncomputable abbrev splayBialgebra : Bialgebra R (SplayAlgebra R A) :=
  Bialgebra.ofAlgHom (splayComul R A) (splayCounit R A) (splay_coassoc R A)
    (splay_rTensor R A) (splay_lTensor R A)

end Splay

section Quotient

variable {I : Type*} [DecidableEq I] {A : I → Type*} [∀ i, CommRing (A i)]
  [∀ i, Bialgebra R (A i)] (π : PoissonStructure R (SplayAlgebra R A))
  (hΔ : IsStronglyMultiplicative (opMul R _) (splayComul R A).toLinearMap π.bracket)
  (hε : ∀ f g, splayCounit R A (π.bracket f g) = 0)

/-- The coproduct of `U = T / J`, descended from the splay coproduct (Prop. 1.13). -/
noncomputable def quotComul :
    IntegrationQuotient π →ₐ[R] IntegrationQuotient π ⊗[R] IntegrationQuotient π :=
  descendedComul π (opMul R _) (opMul_integrationMk π) (splayComul R A) hΔ

/-- The counit of `U = T / J`, descended from the splay counit. -/
noncomputable def quotCounit : IntegrationQuotient π →ₐ[R] R :=
  counitDescends π (splayCounit R A) hε

theorem quotComul_mk (f : SplayAlgebra R A) :
    quotComul π hΔ (integrationMk π f) =
      Algebra.TensorProduct.map (integrationMk π) (integrationMk π)
        (@Coalgebra.comul R _ _ _ _ (splayBialgebra R A).toCoalgebra.toCoalgebraStruct f) :=
  descendedComul_mk π (opMul R _) (opMul_integrationMk π) (splayComul R A) hΔ f

theorem quotCounit_mk (f : SplayAlgebra R A) :
    quotCounit π hε (integrationMk π f) =
      @Coalgebra.counit R _ _ _ _ (splayBialgebra R A).toCoalgebra.toCoalgebraStruct f := by
  simp [quotCounit, counitDescends, integrationMk]; rfl

theorem quot_algHom_ext {B : Type*} [Semiring B] [Algebra R B]
    {f g : IntegrationQuotient π →ₐ[R] B}
    (h : ∀ x, f (integrationMk π x) = g (integrationMk π x)) : f = g :=
  RingQuot.ringQuot_ext' (S := R) f g (AlgHom.ext h)

/-- **Thm. 3.7 of arXiv:math/0602138, the bialgebra half.** If `π` is strongly
multiplicative for the splay coproduct and the splay counit kills `π`, then
`U = T / J` is a bialgebra, with coproduct and counit descended from the splay. -/
noncomputable abbrev quotBialgebra : Bialgebra R (IntegrationQuotient π) :=
  letI := splayBialgebra R A
  Bialgebra.ofAlgHom (quotComul π hΔ) (quotCounit π hε)
    (quot_algHom_ext π fun x =>
      transfer_coassoc (integrationMk π) (quotComul π hΔ) (quotComul_mk π hΔ) x)
    (quot_algHom_ext π fun x =>
      transfer_rTensor (integrationMk π) (quotComul π hΔ) (quotCounit π hε)
        (quotComul_mk π hΔ) (quotCounit_mk π hε) x)
    (quot_algHom_ext π fun x =>
      transfer_lTensor (integrationMk π) (quotComul π hΔ) (quotCounit π hε)
        (quotComul_mk π hΔ) (quotCounit_mk π hε) x)

end Quotient


end

end QOU.FormalGroups
