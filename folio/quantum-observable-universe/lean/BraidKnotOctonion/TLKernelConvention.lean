import BraidKnotOctonion.TLCarrierBridge
import BraidKnotOctonion.WtraceRadicalTwoRowSubset

/-!
# The TL kernel and `rad(wtrace)` sit on opposite sides of the transpose

`TLCarrierBridge.tlKernelPulled` is the kernel of the Temperley–Lieb quotient read on the
skein carrier, and `WtraceRadicalTwoRow.mem_rad_iff_twoRow_blocks_vanish` characterises
`rad(wtrace)` as the elements killed by every seminormal block of a shape with at most two
**rows**.  The open remark `rem:hecke-radical-is-temperley-lieb` asks whether the two ideals
agree.  In the present normalisations they do not, and the reason is one sign convention.

## The mechanism

`skeinCoxeterEquiv` sends `σ_i ↦ q⁻¹ • T_i`, so the TL generator `U_i = T_i + 1` pulls back to
`q σ_i + 1`.  The skein generator satisfies `(σ - q)(σ + q⁻¹) = 0`, so `U_i` vanishes on the
`-q⁻¹`-eigenspace of `σ_i` and is `q² + 1` on the `q`-eigenspace.  In the seminormal form the
eigenvalue `q` is axial distance `+1` (`seminormalParam_one`), i.e. `i` and `i+1` in the
**same row**.  So the TL relator `U_i U_j U_i - q² U_i` is the *symmetriser* side of the
local `H₃`, and it survives on the one-row shape, which has at most two rows.

## What is proved

**The counterexample (untwisted form).**

* `genMat_eq_smul_one_of_oneRow` — on a one-row shape every generator matrix is `q • 1`.
* `seminormalRep_skeinRelator_oneRow` — there the pulled-back relator acts as the scalar
  `(q² + 1)((q² + 1)² - q²)`.
* `tlKernelPulled_not_le_rad` — for every real `q ≠ 0` that is not a root of unity, the
  pulled-back relator at `n = 2` lies in `tlKernelPulled` and not in `rad(wtrace)`.  So the
  inclusion `tlKernelPulled ≤ rad(wtrace)` fails as stated, already on `H₃`.

**The involution.**

* `theta` — the algebra involution `σ_i ↦ (q - q⁻¹) - σ_i = -σ_i⁻¹` (`theta_theta`), which
  exchanges the eigenvalues `q` and `-q⁻¹`, i.e. rows and columns.

The corrected statement, `tlKernelPulled = θ(rad(wtrace))`, is
`TLKernelEquality.mem_tlKernelPulled_iff`; the twisted inclusion `theta_mem_rad` is a
corollary there.  (An earlier version of this file proved that inclusion directly, by a
pigeonhole argument on seminormal matrices; it was removed once the equality made it
redundant.)

Purely algebraic: no numerical evaluation enters any proof.
-/

namespace QOU.IwahoriHecke.TLKernelConvention

open QOU.Mathlib (StandardYoungTableau)
open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep QOU.SchurWeyl.TableauCells
open QOU.SchurWeyl.Seminormal
open QOU.MathlibExt.HeckeToTemperleyLieb QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.CoxeterCarrier
open QOU.IwahoriHecke.TLCarrierBridge

section OneRow

variable {μ : YoungDiagram} {K : Type*} [Field K] (q : K)

/-- On a shape with no second row, every cell lies in row `0`. -/
theorem row_eq_zero_of_rowLen_one_eq_zero (h : μ.rowLen 1 = 0) {c : ℕ × ℕ}
    (hc : c ∈ μ.cells) : c.1 = 0 := by
  by_contra hne
  have h1 : (1, c.2) ∈ μ := μ.up_left_mem (by omega) le_rfl hc
  rw [YoungDiagram.mem_iff_lt_rowLen, h] at h1
  omega

/-- On a one-row shape the cells holding `k` and `k + 1` share row `0`, so the axial
distance is `+1`. -/
theorem axialDist_eq_one_of_oneRow (h : μ.rowLen 1 = 0) (T : StandardYoungTableau μ)
    {k : ℕ} (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) : axialDist T k = 1 := by
  have hk1 : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hk2 : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  obtain ⟨m1, e1⟩ := cellOf_spec T hk1
  obtain ⟨m2, e2⟩ := cellOf_spec T hk2
  have r1 := row_eq_zero_of_rowLen_one_eq_zero h m1
  have r2 := row_eq_zero_of_rowLen_one_eq_zero h m2
  have m1' : (0, (cellOf T k).2) ∈ μ := by
    rw [← r1]; simpa using m1
  have m2' : (0, (cellOf T (k + 1)).2) ∈ μ := by
    rw [← r2]; simpa using m2
  rw [r1] at e1
  rw [r2] at e2
  exact axialDist_of_sameRow T m1' m2' e1 e2

/-- On a one-row shape no swap is admissible: the two cells share row `0`. -/
theorem not_swapAdmissible_of_oneRow (h : μ.rowLen 1 = 0) (T : StandardYoungTableau μ)
    {k : ℕ} (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) : ¬ SwapAdmissible T k := by
  intro ha
  apply ha.1
  rw [row_eq_zero_of_rowLen_one_eq_zero h (cellOf_mem T ⟨hk, by omega⟩),
    row_eq_zero_of_rowLen_one_eq_zero h (cellOf_mem T ⟨by omega, hkn⟩)]

/-- **On a one-row shape every generator matrix is the scalar `q`.** -/
theorem genMat_eq_smul_one_of_oneRow (hq0 : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (h : μ.rowLen 1 = 0) (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    genMat q k hk hkn = q • (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K) := by
  ext T' T
  by_cases hTT : T' = T
  · subst hTT
    rw [genMat_diag, axialDist_eq_one_of_oneRow h T' hk hkn, seminormalParam_one q hq0 hq2]
    simp
  · rw [genMat_of_not_admissible q k hk hkn hTT (not_swapAdmissible_of_oneRow h T hk hkn)]
    simp [hTT]

end OneRow

section Relator

variable {K : Type*} [Field K]

/-- The Temperley–Lieb relator `U₀ U₁ U₀ - q² U₀` in the Coxeter presentation at rank `2`,
`U_i = T_i + 1`.  `tlRelator_mem_ker` places it in `tlKernel`. -/
noncomputable def coxRelator (q : K) : HeckeAlgebra K (q ^ 2) (AMat 2) :=
  (T K (q ^ 2) (AMat 2) 0 + 1) * (T K (q ^ 2) (AMat 2) 1 + 1) * (T K (q ^ 2) (AMat 2) 0 + 1)
    - algebraMap K (HeckeAlgebra K (q ^ 2) (AMat 2)) (q ^ 2) * (T K (q ^ 2) (AMat 2) 0 + 1)

/-- The relator pulled back to the skein carrier. -/
noncomputable def skeinRelator (q : K) (hq : q ≠ 0) : QOU.SchurWeyl.Hecke K q q⁻¹ 2 :=
  (skeinCoxeterEquiv q hq 2).symm (coxRelator q)

/-- The inverse of `skeinCoxeterEquiv` sends `T_i` to `q • σ_i`. -/
theorem skeinCoxeterEquiv_symm_T (q : K) (hq : q ≠ 0) (n : ℕ) (i : Fin n) :
    (skeinCoxeterEquiv q hq n).symm (T K (q ^ 2) (AMat n) i)
      = q • QOU.SchurWeyl.Hecke.σ K q q⁻¹ n i := by
  rw [AlgEquiv.symm_apply_eq, map_smul, skeinCoxeterEquiv_σ, smul_smul,
    mul_inv_cancel₀ hq, one_smul]

/-- **The pulled-back relator lies in `tlKernelPulled`.** -/
theorem skeinRelator_mem (q δ : K) (hq : q ≠ 0) (hδ : q * δ = q ^ 2 + 1) :
    skeinRelator q hq ∈ tlKernelPulled hq 2 hδ := by
  rw [tlKernelPulled, TwoSidedIdeal.mem_ker]
  show heckeToTL hδ (isTypeADiagram_AMat 2)
      (skeinCoxeterEquiv q hq 2 ((skeinCoxeterEquiv q hq 2).symm (coxRelator q))) = 0
  rw [AlgEquiv.apply_symm_apply]
  exact tlRelator_mem_ker hδ (isTypeADiagram_AMat 2) (i := 0) (j := 1) (Or.inl rfl)

/-- **On a one-row shape the pulled-back relator is the nonzero scalar
`(q² + 1)((q² + 1)² - q²)`.** -/
theorem seminormalRep_skeinRelator_oneRow (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {μ : YoungDiagram} (hN : μ.cells.card = 2 + 1)
    (h : μ.rowLen 1 = 0) :
    seminormalRep q hq0 hq2 2 hN (skeinRelator q hq0)
      = algebraMap K (Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K)
          ((q ^ 2 + 1) * ((q ^ 2 + 1) ^ 2 - q ^ 2)) := by
  have hT : ∀ i : Fin 2, seminormalRep q hq0 hq2 2 hN
      ((skeinCoxeterEquiv q hq0 2).symm (T K (q ^ 2) (AMat 2) i))
        = algebraMap K _ (q ^ 2) := by
    intro i
    rw [skeinCoxeterEquiv_symm_T, map_smul, seminormalRep_σ]
    show q • genMat q ((i : ℕ) + 1) _ _ = _
    rw [genMat_eq_smul_one_of_oneRow q hq0 (GenericParameter.sq_ne_one hq2) h, smul_smul,
      Algebra.algebraMap_eq_smul_one, sq]
  simp only [skeinRelator, coxRelator, map_sub, map_mul, map_add, map_one,
    AlgEquiv.commutes, AlgHom.commutes, hT]
  simp only [← map_one (algebraMap K (Matrix (StandardYoungTableau μ)
    (StandardYoungTableau μ) K)), ← map_add, ← map_mul, ← map_sub]
  congr 1
  ring

end Relator

section Counterexample

open QOU.SchurWeyl.WtraceRadicalTwoRow

/-- The one-row shape with three cells. -/
def threeRow : YoungDiagram := YoungDiagram.ofRowLens [3] (by simp)

theorem mem_threeRow_iff (c : ℕ × ℕ) : c ∈ threeRow ↔ c.1 = 0 ∧ c.2 < 3 := by
  rcases c with ⟨i, j⟩
  simp only [threeRow, YoungDiagram.mem_ofRowLens]
  constructor
  · rintro ⟨hi, hj⟩
    simp at hi
    subst hi
    simpa using hj
  · rintro ⟨hi, hj⟩
    subst hi
    exact ⟨by simp, by simpa using hj⟩

theorem threeRow_cells : threeRow.cells = {(0, 0), (0, 1), (0, 2)} := by
  ext ⟨i, j⟩
  rw [YoungDiagram.mem_cells, mem_threeRow_iff]
  simp only [Finset.mem_insert, Finset.mem_singleton, Prod.mk.injEq]
  omega

theorem threeRow_card : threeRow.cells.card = 2 + 1 := by
  rw [threeRow_cells]; rfl

theorem threeRow_rowLen_one : threeRow.rowLen 1 = 0 := by
  by_contra hne
  have : (1, 0) ∈ threeRow := by
    rw [YoungDiagram.mem_iff_lt_rowLen]; omega
  rw [mem_threeRow_iff] at this
  omega

theorem threeRow_rowLen_two : threeRow.rowLen 2 = 0 := by
  by_contra hne
  have : (2, 0) ∈ threeRow := by
    rw [YoungDiagram.mem_iff_lt_rowLen]; omega
  rw [mem_threeRow_iff] at this
  omega

/-- **The inclusion `tlKernelPulled ≤ rad(wtrace)` fails at `n = 2`.**  For every real
`q ≠ 0` that is not a root of unity, the pulled-back TL relator lies in `tlKernelPulled` but
some `b` has `wtrace (x * b) ≠ 0`.  The witness block is the one-row shape `(3)`. -/
theorem tlKernelPulled_not_le_rad {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {δ : ℝ} (hδ : q * δ = q ^ 2 + 1) :
    ∃ x ∈ tlKernelPulled hq0 2 hδ, ∃ b : QOU.SchurWeyl.Hecke ℝ q q⁻¹ 2,
      wtrace q hq0 hq2 2 (x * b) ≠ 0 := by
  refine ⟨skeinRelator q hq0, skeinRelator_mem q δ hq0 hδ, ?_⟩
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  have hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1 := fun k hk => by
    rw [← pow_mul]; exact hq2 _ (by omega)
  by_contra hall
  push_neg at hall
  have hvan := (mem_rad_iff_twoRow_blocks_vanish hq0 hq2 hq21 hgen 2
    (skeinRelator q hq0)).mp hall threeRow threeRow_card threeRow_rowLen_two
  rw [seminormalRep_skeinRelator_oneRow q hq0 hq2 threeRow_card threeRow_rowLen_one] at hvan
  obtain ⟨T⟩ : Nonempty (StandardYoungTableau threeRow) := inferInstance
  have h0 := congrFun (congrFun hvan T) T
  rw [Algebra.algebraMap_eq_smul_one, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul,
    mul_one, Matrix.zero_apply] at h0
  have hpos : 0 < (q ^ 2 + 1) * ((q ^ 2 + 1) ^ 2 - q ^ 2) := by
    have : 0 < (q ^ 2 + 1) ^ 2 - q ^ 2 := by nlinarith [sq_nonneg q, sq_nonneg (q ^ 2)]
    positivity
  exact hpos.ne' h0

end Counterexample

section Alg
variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A]

theorem twist_quad (c : K) {a : A} (ha : a * a = c • a + 1) :
    (c • 1 - a) * (c • 1 - a) = c • (c • 1 - a) + 1 := by
  have h : (c • (1:A) - a) * (c • 1 - a) = (c * c) • (1:A) - (2 * c) • a + a * a := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  rw [h, ha]; module

theorem twist_braid (c : K) {a b : A} (ha : a * a = c • a + 1) (hb : b * b = c • b + 1)
    (hab : a * b * a = b * a * b) :
    (c • 1 - a) * (c • 1 - b) * (c • 1 - a) = (c • 1 - b) * (c • 1 - a) * (c • 1 - b) := by
  have key : (c • (1:A) - a) * (c • 1 - b) * (c • 1 - a) - (c • 1 - b) * (c • 1 - a) * (c • 1 - b)
      = c • (a * a - c • a - 1) - c • (b * b - c • b - 1) - (a * b * a - b * a * b) := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
      mul_assoc]
    module
  rw [ha, hb, hab] at key
  simpa [sub_eq_zero] using key

theorem twist_comm (c : K) {a b : A} (hab : a * b = b * a) :
    (c • 1 - a) * (c • 1 - b) = (c • 1 - b) * (c • 1 - a) := by
  have key : (c • (1:A) - a) * (c • 1 - b) - (c • 1 - b) * (c • 1 - a) = a * b - b * a := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  rw [hab, sub_self, sub_eq_zero] at key
  exact key

end Alg


section Twisted

open QOU.MathlibExt.HeckeToTemperleyLieb QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.IwahoriHecke QOU.IwahoriHecke.CoxeterCarrier
open QOU.IwahoriHecke.TLCarrierBridge

variable {K : Type*} [Field K]

theorem σ_sq' (q : K) (hq0 : q ≠ 0) (n : ℕ) (i : Fin n) :
    Hecke.σ K q q⁻¹ n i * Hecke.σ K q q⁻¹ n i = (q - q⁻¹) • Hecke.σ K q q⁻¹ n i + 1 := by
  rw [Hecke.σ_quadratic, mul_inv_cancel₀ hq0, one_smul]

/-- **The involution `θ : σ_i ↦ (q - q⁻¹) - σ_i = -σ_i⁻¹`.**  It exchanges the two
eigenvalues `q` and `-q⁻¹` of every generator. -/
noncomputable def theta (q : K) (hq0 : q ≠ 0) (n : ℕ) :
    Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n :=
  Hecke.lift K q q⁻¹ n (fun i => (q - q⁻¹) • 1 - Hecke.σ K q q⁻¹ n i)
    (fun i => by rw [mul_inv_cancel₀ hq0, one_smul]; exact twist_quad _ (σ_sq' q hq0 n i))
    (fun i hi => twist_braid _ (σ_sq' q hq0 n _) (σ_sq' q hq0 n _)
      (Hecke.σ_braid K q q⁻¹ n i hi))
    (fun i j h => twist_comm _ (Hecke.σ_commute K q q⁻¹ n i j h))

@[simp] theorem theta_σ (q : K) (hq0 : q ≠ 0) (n : ℕ) (i : Fin n) :
    theta q hq0 n (Hecke.σ K q q⁻¹ n i) = (q - q⁻¹) • 1 - Hecke.σ K q q⁻¹ n i :=
  Hecke.lift_σ K q q⁻¹ n _ _ _ _ i

/-- `θ` is an involution. -/
theorem theta_theta (q : K) (hq0 : q ≠ 0) (n : ℕ) (x : Hecke K q q⁻¹ n) :
    theta q hq0 n (theta q hq0 n x) = x := by
  have h : (theta q hq0 n).comp (theta q hq0 n) = AlgHom.id K _ := by
    apply Hecke.hom_ext
    intro i
    simp only [AlgHom.comp_apply, theta_σ, map_sub, map_smul, map_one, AlgHom.id_apply]
    abel
  exact congrArg (fun φ : Hecke K q q⁻¹ n →ₐ[K] Hecke K q q⁻¹ n => φ x) h

end Twisted
end QOU.IwahoriHecke.TLKernelConvention
