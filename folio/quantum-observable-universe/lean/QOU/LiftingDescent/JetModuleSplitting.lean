/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.RingTheory.Kaehler.Basic

/-!
# The base object is a direct summand of the jet module (`lem:descent`, Step 1)

Step 1 of the proof of `lem:descent` needs `A` to be a direct summand of `J¹(A)`,
with section `ℓ` (ascent) and retraction `r` (descent), `r ∘ ℓ = id`.

1. **With the corpus's `J¹(A) := A ⊗ Ω¹(A)` this fails.** For `A = R`,
   `Ω¹(R) = ker (m : R ⊗ R → R) = 0`, so `J¹(R) = 0` and no injective linear map
   `R → J¹(R)` exists when `R` is nontrivial (`not_injective_into_naiveJet_self`).
2. **With the standard first jet module `J¹(S) := (S ⊗ S) ⧸ I²`**, `I = ker m`, it
   holds for every commutative `R`-algebra `S`: `ℓ(a) = [a ⊗ 1]` and `r` induced by
   `m` satisfy `r ∘ ℓ = id` (`jetRetract_comp_jetSection`), and the complement
   `ker r` is the image of `I`, i.e. `I/I² = Ω[S⁄R]`.

No `sorry`, no axiom beyond Lean's three.

## References
- [leitner2026] §3 Lifting and Descent
- Grothendieck, EGA IV 16.7 (first-order jets as `(S ⊗ S)/I²`)
-/

namespace QOU.LiftingDescent

open TensorProduct

section Naive

variable (R : Type*) [CommRing R]

/-- `Ω¹(R) = 0`: multiplication `R ⊗ R → R` is injective. -/
theorem kerMul_self_eq_bot : LinearMap.ker (LinearMap.mul' R R) = ⊥ := by
  have : LinearMap.mul' R R = (TensorProduct.lid R R).toLinearMap := by
    ext; simp
  rw [this, LinearEquiv.ker]

/-- **Step 1 fails for `J¹(A) := A ⊗ Ω¹(A)`**: at `A = R` (nontrivial), no linear map
`R → R ⊗ Ω¹(R)` is injective, because `Ω¹(R) = 0`. -/
theorem not_injective_into_naiveJet_self [Nontrivial R]
    (f : R →ₗ[R] R ⊗[R] LinearMap.ker (LinearMap.mul' R R)) : ¬ Function.Injective f := by
  intro hf
  have hsub : Subsingleton (LinearMap.ker (LinearMap.mul' R R)) := by
    rw [kerMul_self_eq_bot]; infer_instance
  have : Subsingleton (R ⊗[R] LinearMap.ker (LinearMap.mul' R R)) := inferInstance
  exact zero_ne_one (hf (Subsingleton.elim (f 0) (f 1)))

end Naive

section Standard

variable (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]

/-- The standard first jet module `J¹(S) = (S ⊗ S) ⧸ I²`, `I = ker m`. -/
abbrev jetModule : Type _ := (S ⊗[R] S) ⧸ (KaehlerDifferential.ideal R S ^ 2)

/-- Retraction `r : J¹(S) → S`, induced by multiplication (it kills `I² ⊆ I`). -/
noncomputable def jetRetract : jetModule R S →ₐ[R] S :=
  Ideal.Quotient.liftₐ _ (Algebra.TensorProduct.lmul' R) fun x hx => by
    have : x ∈ KaehlerDifferential.ideal R S := Ideal.pow_le_self two_ne_zero hx
    exact (RingHom.mem_ker).mp this

/-- Section `ℓ : S → J¹(S)`, `a ↦ [a ⊗ 1]`. -/
noncomputable def jetSection : S →ₐ[R] jetModule R S :=
  (Ideal.Quotient.mkₐ R _).comp Algebra.TensorProduct.includeLeft

/-- **`S` is a direct summand of `J¹(S)`**: `r ∘ ℓ = id`. -/
theorem jetRetract_comp_jetSection :
    (jetRetract R S).comp (jetSection R S) = AlgHom.id R S := by
  ext a
  simp [jetRetract, jetSection]

/-- The complement `ker r` contains the image of `I = ker m`, whose quotient by `I²`
is `Ω[S⁄R]`; every jet splits as `ℓ(r j) + (j − ℓ(r j))` with the second term in
`ker r`. -/
theorem jet_split (j : jetModule R S) :
    jetRetract R S (j - jetSection R S (jetRetract R S j)) = 0 := by
  have := congrArg (fun f : S →ₐ[R] S => f (jetRetract R S j)) (jetRetract_comp_jetSection R S)
  simp only [AlgHom.comp_apply, AlgHom.id_apply] at this
  rw [map_sub, this, sub_self]

/-- **The complement is `I/I²`**: `ker r` is the image of `I = ker m` in `J¹(S)`. -/
theorem ker_jetRetract :
    RingHom.ker (jetRetract R S) =
      (KaehlerDifferential.ideal R S).map
        (Ideal.Quotient.mk (KaehlerDifferential.ideal R S ^ 2)) := by
  ext x
  obtain ⟨y, rfl⟩ := Ideal.Quotient.mk_surjective x
  rw [RingHom.mem_ker]
  constructor
  · intro h
    exact Ideal.mem_map_of_mem _ ((RingHom.mem_ker).mpr (by simpa [jetRetract] using h))
  · intro h
    rw [Ideal.mem_map_iff_of_surjective _ Ideal.Quotient.mk_surjective] at h
    obtain ⟨z, hz, hzy⟩ := h
    rw [Ideal.Quotient.eq] at hzy
    have hd : z - y ∈ KaehlerDifferential.ideal R S := Ideal.pow_le_self two_ne_zero hzy
    have hz' : z ∈ KaehlerDifferential.ideal R S := hz
    have hy : y ∈ KaehlerDifferential.ideal R S := by
      have := Ideal.sub_mem _ hz' hd
      simpa using this
    simpa [jetRetract] using (RingHom.mem_ker).mp hy

end Standard

end QOU.LiftingDescent
