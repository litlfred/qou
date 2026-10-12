import QOU.KZ.KZShiftPhi
import QOU.KZ.KZHexagon

/-!
# The hexagon with a central total residue

Stage S3 prerequisite of bean `qou-zoyv`. `KZHexagon.hexagon` is stated with the residue at
infinity `C = −A − B`. In the Drinfeld category the three residues are `t₁₂, t₁₃, t₂₃` and
`T = t₁₂ + t₁₃ + t₂₃` commutes with each of them. Then `C = t₁₃ − T`, and shift invariance
(`KZShiftPhi`) removes `T` from the associators. What remains is

  `e^{−iπA} Φ(C', A) e^{−iπC'} Φ(B, C') e^{−iπB} Φ(A, B) = e^{−iπT}`,   `T = A + B + C'`

(`hexagon_central`), whenever `T` commutes with `A, B, C'`. Sorry-free.

-- Ref: [manuscript] beans/defs/qou-zoyv (stage S3)
-/

namespace QOU.KZ.KZHexagonCentral

open QOU.KZ.FuchsianFormal QOU.KZ.FuchsianParam QOU.KZ.AssociatorKZ QOU.KZ.KZPentagon
  QOU.KZ.KZHexagon QOU.KZ.KZShiftPhi

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-- `Φ(A, B)` commutes with anything commuting with `A` and `B`. -/
theorem commute_Φ {c A B : R} (hA : NonResonant A) (hB : NonResonant B) (hcA : Commute c A)
    (hcB : Commute c B) : Commute c (Φ A B hA hB) :=
  KZShift.commute_phiKZ A B c _ _ _ _ _ _ hcA hcB (commute_H0 hA hcA hcB) (commute_H0 hB hcB hcA)

omit [CompleteSpace R] in
theorem commute_eπ {c X : R} (h : Commute c X) : Commute c (eπ X) :=
  Commute.exp_right ℂ (h.smul_right _)

theorem eπ_add {X Y : R} (h : Commute X Y) : eπ (X + Y) = eπ X * eπ Y := by
  unfold eπ
  rw [smul_add]
  exact NormedSpace.exp_add_of_commute ((h.smul_left _).smul_right _)

/-- The hexagon with the residue at infinity written through the three-point residues. -/
theorem hexagon_Φ (A B : R) (hA : NonResonant A) (hB : NonResonant B)
    (hC : NonResonant (-A - B)) :
    eπ A * Φ (-A - B) A hC hA * eπ (-A - B) * Φ B (-A - B) hB hC * eπ B * Φ A B hA hB = 1 :=
  hexagon _ _ (fun k hk => (hA k hk).1) (fun k hk => (hB k hk).1) (fun k hk => (hC k hk).1)
    _ _ _ _ _ _
    (H0_zero _ _ hA) (H0_gauge _ _ hA) (H0_zero _ _ hB) (H0_gauge _ _ hB)
    (H0_zero _ _ hB) (H0_gauge _ _ hB) (H0_zero _ _ hC) (H0_gauge _ _ hC)
    (H0_zero _ _ hC) (H0_gauge _ _ hC) (H0_zero _ _ hA) (H0_gauge _ _ hA)

/-- **The central hexagon.** If `T = A + B + C'` commutes with `A`, `B`, `C'`, then
`e^{−iπA} Φ(C', A) e^{−iπC'} Φ(B, C') e^{−iπB} Φ(A, B) = e^{−iπT}`. -/
theorem hexagon_central (A B C' : R) (hA : NonResonant A) (hB : NonResonant B)
    (hC' : NonResonant C') (hC : NonResonant (-A - B))
    (hTA : Commute (A + B + C') A) (hTB : Commute (A + B + C') B)
    (hTC : Commute (A + B + C') C') :
    eπ A * Φ C' A hC' hA * eπ C' * Φ B C' hB hC' * eπ B * Φ A B hA hB = eπ (A + B + C') := by
  set T := A + B + C' with hTdef
  have eC : -A - B = C' + -T := by rw [hTdef]; abel
  have hC'' : NonResonant (C' + -T) := eC ▸ hC
  have zA : Commute (-T) A := hTA.neg_left
  have zB : Commute (-T) B := hTB.neg_left
  have zC : Commute (-T) C' := hTC.neg_left
  have s1 : Φ (-A - B) A hC hA = Φ C' A hC' hA :=
    (Φ_congr eC rfl hC hA hC'' hA).trans (Φ_shift_left C' A (-T) hC' hA hC'' zC zA)
  have s2 : Φ B (-A - B) hB hC = Φ B C' hB hC' :=
    (Φ_congr rfl eC hB hC hB hC'').trans (Φ_shift_right B C' (-T) hB hC' hC'' zB zC)
  have s3 : eπ (-A - B) = eπ C' * eπ (-T) := by rw [eC, eπ_add zC.symm]
  have H := hexagon_Φ A B hA hB hC
  rw [s1, s2, s3] at H
  -- move the central factor `e^{iπT}` to the right
  have cT1 : Commute (eπ (-T)) (Φ B C' hB hC') :=
    (commute_eπ (commute_Φ hB hC' zB zC).symm).symm
  have cT2 : Commute (eπ (-T)) (eπ B) := (commute_eπ (commute_eπ zB).symm).symm
  have cT3 : Commute (eπ (-T)) (Φ A B hA hB) := (commute_eπ (commute_Φ hA hB zA zB).symm).symm
  set X := eπ A * Φ C' A hC' hA * eπ C' * Φ B C' hB hC' * eπ B * Φ A B hA hB
  have hX : X * eπ (-T) = 1 := by
    rw [← H]
    simp only [X, mul_assoc, cT3.eq, cT2.eq, cT1.eq]
  have hinv : eπ (-T) * eπ T = 1 := by
    rw [← eπ_add (Commute.neg_left (Commute.refl T)), neg_add_cancel]
    simp [eπ]
  calc X = X * (eπ (-T) * eπ T) := by rw [hinv, mul_one]
    _ = eπ T := by rw [← mul_assoc, hX, one_mul]

end QOU.KZ.KZHexagonCentral
