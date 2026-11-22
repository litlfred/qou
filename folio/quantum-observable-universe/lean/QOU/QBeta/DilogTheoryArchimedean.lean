import QOU.QBeta.DilogTheory
import QOU.QBeta.FiveTwoAbelFiveTerm
import QOU.Archimedean.BlochRigidity.Reflection

/-!
# The Rogers instance of `RogersDilogTheory` (archimedean half of `DilogTheory`, split per §7c)

The analysis is exactly Euler reflection (`rogersL_reflection`) and Abel's relation
(`rogersL_fiveTerm`). Everything downstream is `RogersDilogTheory.numerators`.

Part B: the Bloch–Wigner function `blochD` of PR #7946 is a `SuslinDilogTheory ℂ ℝ`, and by
#7946's rigidity theorem every continuous, conjugation-odd instance over `ℂ` is a real multiple
of it. So the class has a one-dimensional space of "archimedean" instances.
-/

namespace QOU.QBeta.DilogTheory

open FiveTwoRogersReflection FiveTwoAbelFiveTerm in
/-- **The real instance.** Rogers' `L` on `(0,1)`. The analysis is exactly
`rogersL_reflection` (Euler reflection) and `rogersL_fiveTerm` (Abel). -/
noncomputable def rogers : RogersDilogTheory ℝ where
  L := rogersL
  L1 := Real.pi ^ 2 / 6
  reflection _ h0 h1 := rogersL_reflection h0 h1
  abel _ _ hx0 hx1 hy0 hy1 := rogersL_fiveTerm hx0 hx1 hy0 hy1

/-- `FiveTwoAbelFiveTerm.numerators_of_root` is the `rogers` instance of
`RogersDilogTheory.numerators`. -/
example {x : ℝ} (hx : x ^ 3 - 2 * x ^ 2 - x + 1 = 0) (hlo : 1 / 2 < x) (hhi : x < 1) :=
  rogers.numerators hx hlo hhi

open QOU.Archimedean in
/-- **The Bloch–Wigner instance.** The analysis is `blochD_inv` and the five-term relation
`blochWignerFiveTerm_blochD` (PR #7946). -/
noncomputable def blochWigner : SuslinDilogTheory ℂ ℝ where
  D := FiveTermProof.blochD
  inv_odd z _ := by rw [one_div]; exact FiveTermProof.blochD_inv
  five := blochWignerFiveTerm_blochD.five_term

open QOU.Archimedean in
/-- **Rigidity of the archimedean instances.** A `SuslinDilogTheory ℂ ℝ` that is continuous
off `{0,1}` and odd under conjugation is a real multiple of Bloch–Wigner. This is PR #7946's
`BlochSuslinRigidity` instance, read as a statement about the class. -/
theorem SuslinDilogTheory.eq_mul_blochWigner (T : SuslinDilogTheory ℂ ℝ)
    (hc : ContinuousOn T.D {0, 1}ᶜ) (hconj : ∀ z, T.D ((starRingEnd ℂ) z) = -T.D z) :
    ∃ c : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 → T.D z = c * FiveTermProof.blochD z :=
  BlochSuslinRigidity.uniqueness (D := FiveTermProof.blochD) T.D hc
    ⟨fun z h0 _ => by rw [← one_div]; exact T.inv_odd z h0, hconj⟩ T.five

open QOU.Archimedean in
/-- **The anharmonic orbit of Bloch–Wigner, unconditionally.** Reflection oddness is
`FiveTermProof.blochD_one_sub`; the rest is the algebra of `SuslinDilogTheory.anharmonic`. -/
theorem blochWigner_anharmonic {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    blochWigner.D (1 / (1 - z)) = blochWigner.D z ∧
      blochWigner.D ((z - 1) / z) = blochWigner.D z ∧
      blochWigner.D (z / (z - 1)) = -blochWigner.D z :=
  blochWigner.anharmonic (fun w => FiveTermProof.blochD_one_sub w) hz0 hz1

open QOU.Archimedean in
/-- **Reflection for every continuous archimedean instance.** Off `{0,1}` it follows from
rigidity: such an instance is `c · D`, and `D` is reflection-odd. -/
theorem SuslinDilogTheory.reflection_of_continuous (T : SuslinDilogTheory ℂ ℝ)
    (hc : ContinuousOn T.D {0, 1}ᶜ) (hconj : ∀ z, T.D ((starRingEnd ℂ) z) = -T.D z)
    {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) : T.D (1 - z) = -T.D z := by
  obtain ⟨c, hcD⟩ := T.eq_mul_blochWigner hc hconj
  have h0 : (1 : ℂ) - z ≠ 0 := sub_ne_zero.2 (Ne.symm hz1)
  have h1 : (1 : ℂ) - z ≠ 1 := fun h => hz0 (by linear_combination -h)
  rw [hcD _ h0 h1, hcD _ hz0 hz1, FiveTermProof.blochD_one_sub]
  ring

end QOU.QBeta.DilogTheory
