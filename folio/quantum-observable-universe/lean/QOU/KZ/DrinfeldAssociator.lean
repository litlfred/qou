import QOU.KZ.KZShiftPhi
import QOU.KZ.KZFunctorial
import QOU.KZ.KZHexagonCentral

/-!
# Drinfeld associators as an algebraic class

An **evaluated Drinfeld associator** is a rule `Φ` that assigns to two admissible elements
`A, B` of any complete normed `ℂ`-algebra an element `Φ(A, B)`, subject to purely algebraic
laws:

* **inversion** `Φ(B, A) Φ(A, B) = 1 = Φ(A, B) Φ(B, A)` (group-likeness in evaluated form);
* **unit** `Φ(0, B) = 1`;
* **central shift** `Φ(A, B + z) = Φ(A, B)` for `z` commuting with `A` and `B`;
* **commutant** `c` commuting with `A, B` commutes with `Φ(A, B)`;
* **naturality** along continuous `ℂ`-algebra homomorphisms;
* the **pentagon** on four-point residues satisfying the infinitesimal braid relations;
* the **hexagon** in the central form `e^{−iπA} Φ(C', A) e^{−iπC'} Φ(B, C') e^{−iπB} Φ(A, B)
  = e^{−iπ(A+B+C')}`.

These are exactly the laws the braided category `D_ℏ` (`QOU/KZ/Drinfeld/*`) uses about `Φ_KZ`.
The structure isolates them, so the braided structure is a consequence of the axioms and not of
the analysis that produced one particular `Φ`. The analysis enters only in the instance
`Associator.kz`, built from the Knizhnik–Zamolodchikov connection: every field there is an
existing theorem of `QOU/KZ`.

This file is the class and the KZ instance. Rebuilding `D_ℏ` over a general associator is a
separate step and is not done here.
-/

universe u

namespace QOU.KZ.DrinfeldAssociator

open QOU.KZ.FuchsianFormal QOU.KZ.KZ4 QOU.KZ.KZHexagon

/-- The normalised half-twist `e^{−iπX}` used in the hexagon (the KZ normalisation). -/
noncomputable abbrev ePi {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] (X : R) : R := eπ X

/-- An **evaluated Drinfeld associator**: a rule `Φ(A, B)` on admissible pairs, in every complete
normed `ℂ`-algebra of universe `u`, satisfying the algebraic associator laws. -/
structure Associator where
  /-- Admissibility of an argument. -/
  Adm : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R], R → Prop
  /-- Every non-resonant element is admissible. -/
  adm_of_nonResonant : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    {A : R}, NonResonant A → Adm A
  /-- The associator. -/
  Φ : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (A B : R), Adm A → Adm B → R
  /-- Inversion: `Φ(B, A) Φ(A, B) = 1 = Φ(A, B) Φ(B, A)`. -/
  swap_mul : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (A B : R) (hA : Adm A) (hB : Adm B), Φ B A hB hA * Φ A B hA hB = 1 ∧
      Φ A B hA hB * Φ B A hB hA = 1
  /-- Unit: `Φ(0, B) = 1`. -/
  zero_left : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (B : R) (h0 : Adm (0 : R)) (hB : Adm B), Φ 0 B h0 hB = 1
  /-- Central shift on the right argument. -/
  shift_right : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (A B z : R) (hA : Adm A) (hB : Adm B) (hBz : Adm (B + z)), Commute z A → Commute z B →
      Φ A (B + z) hA hBz = Φ A B hA hB
  /-- Anything commuting with both arguments commutes with the associator. -/
  commute : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    {c A B : R} (hA : Adm A) (hB : Adm B), Commute c A → Commute c B → Commute c (Φ A B hA hB)
  /-- Naturality along continuous `ℂ`-algebra homomorphisms. -/
  map : ∀ {R S : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    [NormedRing S] [NormedAlgebra ℂ S] [CompleteSpace S] (f : R →ₐ[ℂ] S), Continuous f →
    ∀ (A B : R) (hA : Adm A) (hB : Adm B) (hfA : Adm (f A)) (hfB : Adm (f B)),
      f (Φ A B hA hB) = Φ (f A) (f B) hfA hfB
  /-- The pentagon, in Drinfeld's coproduct form, on residues with the infinitesimal braid
  relations. -/
  pentagon : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (t : Res R), t.Rel → ∀ (h12 : Adm t.t12) (h23 : Adm t.t23) (h34 : Adm t.t34)
    (_h123 : Adm t.T123) (_h234 : Adm t.T234) (h1213 : Adm (t.t12 + t.t13))
    (h2434 : Adm (t.t24 + t.t34)) (h2324 : Adm (t.t23 + t.t24)) (h1323 : Adm (t.t13 + t.t23)),
    Φ t.t23 t.t34 h23 h34 * Φ (t.t12 + t.t13) (t.t24 + t.t34) h1213 h2434 *
        Φ t.t12 t.t23 h12 h23 =
      Φ t.t12 (t.t23 + t.t24) h12 h2324 * Φ (t.t13 + t.t23) t.t34 h1323 h34
  /-- The hexagon in central form. -/
  hexagon : ∀ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]
    (A B C' : R) (hA : Adm A) (hB : Adm B) (hC' : Adm C'), Adm (-A - B) →
    Commute (A + B + C') A → Commute (A + B + C') B → Commute (A + B + C') C' →
    ePi A * Φ C' A hC' hA * ePi C' * Φ B C' hB hC' * ePi B * Φ A B hA hB = ePi (A + B + C')

namespace Associator

variable (Ψ : Associator.{u}) {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-- `Φ` depends only on its arguments, not on the admissibility proofs. -/
theorem Φ_congr {A A' B B' : R} (eA : A = A') (eB : B = B') (hA : Ψ.Adm A) (hB : Ψ.Adm B)
    (hA' : Ψ.Adm A') (hB' : Ψ.Adm B') : Ψ.Φ A B hA hB = Ψ.Φ A' B' hA' hB' := by
  subst eA eB; rfl

/-- Central shift on the left argument, derived from `shift_right` and `swap_mul`. -/
theorem shift_left (A B z : R) (hA : Ψ.Adm A) (hB : Ψ.Adm B) (hAz : Ψ.Adm (A + z))
    (hzA : Commute z A) (hzB : Commute z B) : Ψ.Φ (A + z) B hAz hB = Ψ.Φ A B hA hB := by
  have h := Ψ.shift_right B A z hB hA hAz hzB hzA
  have i1 := (Ψ.swap_mul (A + z) B hAz hB).2
  have i2 := (Ψ.swap_mul A B hA hB).1
  rw [h] at i1
  calc _ = Ψ.Φ (A + z) B hAz hB * (Ψ.Φ B A hB hA * Ψ.Φ A B hA hB) := by rw [i2, mul_one]
    _ = _ := by rw [← mul_assoc, i1, one_mul]

/-- `Φ(A, 0) = 1`, derived from `zero_left` and `swap_mul`. -/
theorem zero_right (A : R) (hA : Ψ.Adm A) (h0 : Ψ.Adm (0 : R)) : Ψ.Φ A 0 hA h0 = 1 := by
  have i := (Ψ.swap_mul A 0 hA h0).1
  rw [Ψ.zero_left] at i
  simpa using i

/-- `Φ(A, B)` is a unit. -/
theorem isUnit (A B : R) (hA : Ψ.Adm A) (hB : Ψ.Adm B) : IsUnit (Ψ.Φ A B hA hB) :=
  ⟨⟨_, _, (Ψ.swap_mul A B hA hB).2, (Ψ.swap_mul A B hA hB).1⟩, rfl⟩

/-- If `A` and `B` commute, `Φ(A, B) = 1`: shift `B` away to `0` (with `z = −B`), then use
the unit law. -/
theorem eq_one_of_commute (A B : R) (hA : Ψ.Adm A) (hB : Ψ.Adm B) (h0 : Ψ.Adm (0 : R))
    (hAB : Commute A B) : Ψ.Φ A B hA hB = 1 := by
  have hB0 : Ψ.Adm (B + -B) := by simpa using h0
  have := Ψ.shift_right A B (-B) hA hB hB0 hAB.symm.neg_left (Commute.refl B).neg_left
  rw [← this, Ψ.Φ_congr rfl (add_neg_cancel B) hA hB0 hA h0]
  exact Ψ.zero_right A hA h0

end Associator

section KZ

open QOU.KZ.KZPentagon

/-- **The Knizhnik–Zamolodchikov associator** as an instance of the class. Admissibility is
non-resonance; every law is an existing theorem about `Φ_KZ`. -/
noncomputable def kz : Associator.{u} where
  Adm := fun A => NonResonant A
  adm_of_nonResonant := fun h => h
  Φ := fun A B hA hB => KZPentagon.Φ A B hA hB
  swap_mul := fun A B hA hB => KZShiftPhi.Φ_swap_mul A B hA hB
  zero_left := fun B h0 hB => KZShiftPhi.Φ_zero_left B h0 hB
  shift_right := fun A B z hA hB hBz hzA hzB => KZShiftPhi.Φ_shift_right A B z hA hB hBz hzA hzB
  commute := fun hA hB hcA hcB => KZHexagonCentral.commute_Φ hA hB hcA hcB
  map := fun f hf A B hA hB hfA hfB => KZFunctorial.map_Φ f hf A B hA hB hfA hfB
  pentagon := fun t h h12 h23 h34 h123 h234 h1213 h2434 h2324 h1323 =>
    KZShiftPhi.pentagon_drinfeld t h h12 h23 h34 h123 h234 h1213 h2434 h2324 h1323
  hexagon := fun A B C' hA hB hC' hC hTA hTB hTC =>
    KZHexagonCentral.hexagon_central A B C' hA hB hC' hC hTA hTB hTC

/-- The KZ instance evaluates to `Φ_KZ`. -/
theorem kz_Φ {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R] (A B : R)
    (hA : NonResonant A) (hB : NonResonant B) : kz.Φ A B hA hB = KZPentagon.Φ A B hA hB := rfl

end KZ

end QOU.KZ.DrinfeldAssociator
