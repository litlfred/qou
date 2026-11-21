import QOU.KZ.KZShiftPhi
import QOU.KZ.KZFunctorial
import QOU.KZ.KZHexagonCentral
import QOU.KZ.KZIntertwine
import QOU.KZ.BlockResidues

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

The second half of the file restates the `Φ` toolkit that `D_ℏ` uses (`ΦN`, the associator
with non-resonant arguments) for an arbitrary associator, with the same signatures as the KZ
lemmas, so that `QOU/KZ/Drinfeld/*` is built over any `Ψ : Associator`.
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

/-! ### The toolkit for an arbitrary associator, on non-resonant arguments -/

namespace Associator

variable (Ψ : Associator.{u}) {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-- `Φ(A, B)` for non-resonant `A, B`. -/
def ΦN (A B : R) (hA : NonResonant A) (hB : NonResonant B) : R :=
  Ψ.Φ A B (Ψ.adm_of_nonResonant hA) (Ψ.adm_of_nonResonant hB)

theorem ΦN_congr {A A' B B' : R} (eA : A = A') (eB : B = B') (hA : NonResonant A)
    (hB : NonResonant B) (hA' : NonResonant A') (hB' : NonResonant B') :
    Ψ.ΦN A B hA hB = Ψ.ΦN A' B' hA' hB' := by
  subst eA eB; rfl

theorem ΦN_swap_mul (A B : R) (hA : NonResonant A) (hB : NonResonant B) :
    Ψ.ΦN B A hB hA * Ψ.ΦN A B hA hB = 1 ∧ Ψ.ΦN A B hA hB * Ψ.ΦN B A hB hA = 1 :=
  Ψ.swap_mul A B _ _

theorem ΦN_zero_left (B : R) (h0 : NonResonant (0 : R)) (hB : NonResonant B) :
    Ψ.ΦN 0 B h0 hB = 1 :=
  Ψ.zero_left B _ _

theorem ΦN_shift_right (A B z : R) (hA : NonResonant A) (hB : NonResonant B)
    (hBz : NonResonant (B + z)) (hzA : Commute z A) (hzB : Commute z B) :
    Ψ.ΦN A (B + z) hA hBz = Ψ.ΦN A B hA hB :=
  Ψ.shift_right A B z _ _ _ hzA hzB

theorem ΦN_shift_left (A B z : R) (hA : NonResonant A) (hB : NonResonant B)
    (hAz : NonResonant (A + z)) (hzA : Commute z A) (hzB : Commute z B) :
    Ψ.ΦN (A + z) B hAz hB = Ψ.ΦN A B hA hB :=
  Ψ.shift_left A B z _ _ _ hzA hzB

theorem commute_ΦN {c A B : R} (hA : NonResonant A) (hB : NonResonant B) (hcA : Commute c A)
    (hcB : Commute c B) : Commute c (Ψ.ΦN A B hA hB) :=
  Ψ.commute _ _ hcA hcB

theorem map_ΦN {S : Type u} [NormedRing S] [NormedAlgebra ℂ S] [CompleteSpace S]
    (f : R →ₐ[ℂ] S) (hf : Continuous f) (A B : R) (hA : NonResonant A) (hB : NonResonant B)
    (hfA : NonResonant (f A)) (hfB : NonResonant (f B)) :
    f (Ψ.ΦN A B hA hB) = Ψ.ΦN (f A) (f B) hfA hfB :=
  Ψ.map f hf A B _ _ _ _

theorem pentagon_drinfeldN (t : Res R) (h : t.Rel) (h12 : NonResonant t.t12)
    (h23 : NonResonant t.t23) (h34 : NonResonant t.t34) (h123 : NonResonant t.T123)
    (h234 : NonResonant t.T234) (h1213 : NonResonant (t.t12 + t.t13))
    (h2434 : NonResonant (t.t24 + t.t34)) (h2324 : NonResonant (t.t23 + t.t24))
    (h1323 : NonResonant (t.t13 + t.t23)) :
    Ψ.ΦN t.t23 t.t34 h23 h34 * Ψ.ΦN (t.t12 + t.t13) (t.t24 + t.t34) h1213 h2434 *
        Ψ.ΦN t.t12 t.t23 h12 h23 =
      Ψ.ΦN t.t12 (t.t23 + t.t24) h12 h2324 * Ψ.ΦN (t.t13 + t.t23) t.t34 h1323 h34 :=
  Ψ.pentagon t h _ _ _ (Ψ.adm_of_nonResonant h123) (Ψ.adm_of_nonResonant h234) _ _ _ _

theorem hexagon_centralN (A B C' : R) (hA : NonResonant A) (hB : NonResonant B)
    (hC' : NonResonant C') (hC : NonResonant (-A - B))
    (hTA : Commute (A + B + C') A) (hTB : Commute (A + B + C') B)
    (hTC : Commute (A + B + C') C') :
    eπ A * Ψ.ΦN C' A hC' hA * eπ C' * Ψ.ΦN B C' hB hC' * eπ B * Ψ.ΦN A B hA hB =
      eπ (A + B + C') :=
  Ψ.hexagon A B C' _ _ _ (Ψ.adm_of_nonResonant hC) hTA hTB hTC

open QOU.KZ.KZHexagonCentral in
/-- The hexagon rearranged, for any associator (as `KZHexagonCentral.hexagon_rearranged`). -/
theorem hexagon_rearrangedN (A B C : R) (hA : NonResonant A) (hB : NonResonant B)
    (hC : NonResonant C) (hTA : Commute (A + B + C) A) (hTB : Commute (A + B + C) B)
    (hTC : Commute (A + B + C) C)
    (H : eπ A * Ψ.ΦN C A hC hA * eπ C * Ψ.ΦN B C hB hC * eπ B * Ψ.ΦN A B hA hB =
      eπ (A + B + C)) :
    Ψ.ΦN B C hB hC * eπ (-(A + C)) * Ψ.ΦN A B hA hB =
      eπ (-C) * Ψ.ΦN A C hA hC * eπ (-A) := by
  set T := A + B + C with hT
  have hBAC : Commute B (A + C) := by
    have : A + C = T - B := by rw [hT]; abel
    rw [this]; exact (hTB.symm).sub_right (Commute.refl B)
  have heB : eπ B = eπ T * eπ (-(A + C)) := by
    have : T = B + (A + C) := by rw [hT]; abel
    rw [this, eπ_add hBAC, mul_assoc, eπ_mul_eπ_neg, mul_one]
  have hinv := (Ψ.ΦN_swap_mul A C hA hC).2
  have H2 : Ψ.ΦN B C hB hC * eπ B * Ψ.ΦN A B hA hB =
      eπ (-C) * Ψ.ΦN A C hA hC * eπ (-A) * eπ T := by
    rw [← H]
    simp only [mul_assoc]
    rw [← mul_assoc (eπ (-A)) (eπ A), eπ_neg_mul_eπ, one_mul, ← mul_assoc (Ψ.ΦN A C hA hC),
      hinv, one_mul, ← mul_assoc (eπ (-C)) (eπ C), eπ_neg_mul_eπ, one_mul]
  have cT : ∀ {X : R}, Commute T X → Commute (eπ T) X := fun h => (commute_eπ h.symm).symm
  have c1 : Commute (eπ T) (Ψ.ΦN B C hB hC) := cT (Ψ.commute_ΦN hB hC hTB hTC)
  have c2 : Commute (eπ T) (eπ (-C)) := cT (commute_eπ hTC.neg_right)
  have c3 : Commute (eπ T) (Ψ.ΦN A C hA hC) := cT (Ψ.commute_ΦN hA hC hTA hTC)
  have c4 : Commute (eπ T) (eπ (-A)) := cT (commute_eπ hTA.neg_right)
  rw [heB] at H2
  have H3 : eπ T * (Ψ.ΦN B C hB hC * eπ (-(A + C)) * Ψ.ΦN A B hA hB) =
      eπ T * (eπ (-C) * Ψ.ΦN A C hA hC * eπ (-A)) := by
    calc eπ T * (Ψ.ΦN B C hB hC * eπ (-(A + C)) * Ψ.ΦN A B hA hB)
        = Ψ.ΦN B C hB hC * (eπ T * eπ (-(A + C))) * Ψ.ΦN A B hA hB := by
          rw [← mul_assoc, ← mul_assoc, c1.eq, mul_assoc (Ψ.ΦN B C hB hC)]
      _ = eπ (-C) * Ψ.ΦN A C hA hC * eπ (-A) * eπ T := by rw [← H2]
      _ = _ := by
          rw [mul_assoc (eπ (-C) * Ψ.ΦN A C hA hC), ← c4.eq, ← mul_assoc,
            mul_assoc (eπ (-C)), ← c3.eq, ← mul_assoc, ← c2.eq]; simp only [mul_assoc]
  have hu : eπ (-T) * eπ T = 1 := eπ_neg_mul_eπ T
  calc _ = eπ (-T) * (eπ T * (Ψ.ΦN B C hB hC * eπ (-(A + C)) * Ψ.ΦN A B hA hB)) := by
        rw [← mul_assoc, hu, one_mul]
    _ = _ := by rw [H3, ← mul_assoc, hu, one_mul]

section Product

variable {R' : Type u} [NormedRing R'] [NormedAlgebra ℂ R'] [CompleteSpace R']

open QOU.KZ.KZIntertwine in
theorem ΦN_prod (A B : R) (A' B' : R') (hA : NonResonant A) (hB : NonResonant B)
    (hA' : NonResonant A') (hB' : NonResonant B') :
    Ψ.ΦN ((A, A') : R × R') (B, B') (nonResonant_prod hA hA') (nonResonant_prod hB hB') =
      (Ψ.ΦN A B hA hB, Ψ.ΦN A' B' hA' hB') := by
  ext
  · exact Ψ.map_ΦN (AlgHom.fst ℂ R R') continuous_fst ((A, A') : R × R') (B, B')
      (nonResonant_prod hA hA') (nonResonant_prod hB hB') hA hB
  · exact Ψ.map_ΦN (AlgHom.snd ℂ R R') continuous_snd ((A, A') : R × R') (B, B')
      (nonResonant_prod hA hA') (nonResonant_prod hB hB') hA' hB'

end Product

section Blocks

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {ι ι' : Type u} [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι']

open QOU.KZ.KZIntertwine in
/-- **The associator intertwines** (as `KZIntertwine.Φ_intertwine`). -/
theorem ΦN_intertwine (A B : Matrix ι ι ℂ) (A' B' : Matrix ι' ι' ℂ) (T : Matrix ι' ι ℂ)
    (hTA : T * A = A' * T) (hTB : T * B = B' * T)
    (hA : NonResonant A) (hB : NonResonant B) (hA' : NonResonant A') (hB' : NonResonant B')
    (hDA : NonResonant (Matrix.fromBlocks A 0 0 A'))
    (hDB : NonResonant (Matrix.fromBlocks B 0 0 B')) :
    T * Ψ.ΦN A B hA hB = Ψ.ΦN A' B' hA' hB' * T := by
  have hDA' : NonResonant (blockDiag ((A, A') : PR ι ι')) := by
    rw [blockDiag_apply]; exact hDA
  have hDB' : NonResonant (blockDiag ((B, B') : PR ι ι')) := by
    rw [blockDiag_apply]; exact hDB
  have hmap := Ψ.map_ΦN blockDiag
    (LinearMap.continuous_of_finiteDimensional blockDiag.toLinearMap) ((A, A') : PR ι ι') (B, B')
    (nonResonant_prod hA hA') (nonResonant_prod hB hB') hDA' hDB'
  rw [Ψ.ΦN_prod A B A' B' hA hB hA' hB', blockDiag_apply,
    Ψ.ΦN_congr (blockDiag_apply _) (blockDiag_apply _) hDA' hDB' hDA hDB] at hmap
  set Toff : Matrix (ι ⊕ ι') (ι ⊕ ι') ℂ := Matrix.fromBlocks 0 0 T 0
  have cA : Commute Toff (Matrix.fromBlocks A 0 0 A') := by
    show Toff * _ = _ * Toff
    simp [Toff, Matrix.fromBlocks_multiply, hTA]
  have cB : Commute Toff (Matrix.fromBlocks B 0 0 B') := by
    show Toff * _ = _ * Toff
    simp [Toff, Matrix.fromBlocks_multiply, hTB]
  have hc := (Ψ.commute_ΦN hDA hDB cA cB).eq
  have e : Ψ.ΦN (Matrix.fromBlocks A 0 0 A') (Matrix.fromBlocks B 0 0 B') hDA hDB =
      Matrix.fromBlocks (Ψ.ΦN A B hA hB) 0 0 (Ψ.ΦN A' B' hA' hB') := hmap.symm
  rw [e] at hc
  simp only [Toff, Matrix.fromBlocks_multiply, Matrix.zero_mul, Matrix.mul_zero, add_zero,
    zero_add] at hc
  exact (Matrix.fromBlocks_inj.1 hc).2.2.1

end Blocks

section BlockResidues

open QOU.KZ.BlockResidues

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {n : ℕ} {L : Type u} [Fintype L] [DecidableEq L] {c : ℂ}

/-- The pentagon for four leg blocks (as `BlockResidues.pentagon_blocks`). -/
theorem pentagon_blocksN (hc : Transcendental ℚ c) (B : Blocks L) :
    Ψ.ΦN (blockRes n c B).t23 (blockRes n c B).t34 (nr23 hc B) (nr34 hc B) *
      Ψ.ΦN ((blockRes n c B).t12 + (blockRes n c B).t13)
        ((blockRes n c B).t24 + (blockRes n c B).t34) (nr1213 hc B) (nr2434 hc B) *
      Ψ.ΦN (blockRes n c B).t12 (blockRes n c B).t23 (nr12 hc B) (nr23 hc B) =
    Ψ.ΦN (blockRes n c B).t12 ((blockRes n c B).t23 + (blockRes n c B).t24)
        (nr12 hc B) (nr2324 hc B) *
      Ψ.ΦN ((blockRes n c B).t13 + (blockRes n c B).t23) (blockRes n c B).t34
        (nr1323 hc B) (nr34 hc B) :=
  Ψ.pentagon_drinfeldN _ (blockRes_rel n c B) _ _ _ (nr123 hc B) (nr234 hc B) _ _ _ _

/-- The central hexagon for three disjoint leg blocks (as `BlockResidues.hexagon_blocks`). -/
theorem hexagon_blocksN (hc : Transcendental ℚ c) {X1 X2 X3 : Finset L}
    (d12 : Disjoint X1 X2) (d13 : Disjoint X1 X3) (d23 : Disjoint X2 X3) :
    eπ (c • tB ℂ n X1 X2) *
      Ψ.ΦN (c • tB ℂ n X1 X3) (c • tB ℂ n X1 X2)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) *
      eπ (c • tB ℂ n X1 X3) *
      Ψ.ΦN (c • tB ℂ n X2 X3) (c • tB ℂ n X1 X3)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) *
      eπ (c • tB ℂ n X2 X3) *
      Ψ.ΦN (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3)
        (by rw [tB_intCast]; exact nonResonant_cast hc _)
        (by rw [tB_intCast]; exact nonResonant_cast hc _) =
    eπ (c • tB ℂ n X1 X2 + c • tB ℂ n X2 X3 + c • tB ℂ n X1 X3) := by
  have nm := @not_mem_of_disjoint L
  have smc : ∀ {x y : Matrix (L → Fin n) (L → Fin n) ℂ}, Commute x y →
      Commute (c • x) (c • y) := fun h => (h.smul_left c).smul_right c
  have cA : Commute (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3 + c • tB ℂ n X1 X3) := by
    rw [← smul_add, add_comm, ← tB_union_left d12]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [ha, hb])
      (fun a ha b hb => by simp [nm d13 ha, nm d23 hb]))
  have cB : Commute (c • tB ℂ n X2 X3) (c • tB ℂ n X1 X2 + c • tB ℂ n X1 X3) := by
    rw [← smul_add, ← tB_union_right d23]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12.symm ha, nm d13.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  have cC : Commute (c • tB ℂ n X1 X3) (c • tB ℂ n X1 X2 + c • tB ℂ n X2 X3) := by
    rw [← smul_add, tB_comm X1 X2, ← tB_union_right d13]
    exact smc (commute_tB_tB (fun a ha b hb => by simp [nm d12 ha, nm d23.symm hb])
      (fun a ha b hb => by simp [ha, hb]))
  exact Ψ.hexagon_centralN (c • tB ℂ n X1 X2) (c • tB ℂ n X2 X3)
    (c • tB ℂ n X1 X3) (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by rw [tB_intCast]; exact nonResonant_cast hc _)
    (by
      have e : -(c • tB ℂ n X1 X2) - c • tB ℂ n X2 X3 =
          c • (Int.castRingHom ℂ).mapMatrix (-(tBZ n X1 X2 + tBZ n X2 X3)) := by
        rw [tB_intCast, tB_intCast, map_neg, map_add, smul_neg, smul_add]; abel
      rw [e]; exact nonResonant_cast hc _)
    (by rw [add_assoc]; exact ((Commute.refl _).add_right cA).symm)
    (by rw [add_comm (c • tB ℂ n X1 X2), add_assoc]; exact ((Commute.refl _).add_right cB).symm)
    (by rw [add_comm _ (c • tB ℂ n X1 X3)]; exact ((Commute.refl _).add_right cC).symm)

end BlockResidues

end Associator

/-- For the KZ associator, `ΦN` is `Φ_KZ`. -/
theorem kz_ΦN {R : Type u} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R] (A B : R)
    (hA : NonResonant A) (hB : NonResonant B) : kz.ΦN A B hA hB = KZPentagon.Φ A B hA hB := rfl

end QOU.KZ.DrinfeldAssociator
