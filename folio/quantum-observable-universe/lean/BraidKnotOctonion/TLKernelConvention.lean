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

**The corrected inclusion (twisted form).**

* `theta` — the algebra involution `σ_i ↦ (q - q⁻¹) - σ_i = -σ_i⁻¹` (`theta_theta`), which
  exchanges the eigenvalues `q` and `-q⁻¹`, i.e. rows and columns.  It sends the pulled-back
  `U_i` to `q • E_i` with `E_i = q - σ_i` (`seminormalRep_theta_U`).
* `eq_zero_of_twoRow` — **the combinatorial core**: on a shape with at most two rows, a
  matrix `Y` with `Y (ρ(σ_k) + q⁻¹) = 0` and `Y (ρ(σ_{k+1}) + q⁻¹) = 0` is zero.  The three
  cells holding `k, k+1, k+2` occupy at most two rows, so two of them share a row; a shared
  row of consecutive entries forces the column to vanish directly, and the remaining case
  (`k` and `k+2` in one row, `k+1` in the other) reduces to it through one admissible swap.
* `E_adj_twoRow` — hence `E_i E_j E_i = E_i` for adjacent `i, j` on every such shape: the
  element `E_i E_j E_i - E_i` equals `E_j E_i E_j - E_j` (braid and quadratic relations
  only, `E_triple_symm`), so it is annihilated on the right by both `σ_i + q⁻¹` and
  `σ_j + q⁻¹` (`E_mul_eq_zero`).
* `seminormalRep_theta_eq_zero` — every at-most-two-row block kills `θ(tlKernelPulled)`,
  through the presentation `heckeTLEquiv` (`TL ≅ H / ⟨relators⟩`): the composite
  `ρ ∘ θ ∘ skeinCoxeterEquiv⁻¹` respects `TLRel`, so it factors through `HeckeTL`.
* `theta_mem_rad` — **`θ(tlKernelPulled) ⊆ rad(wtrace)` over `ℝ`**, by
  `mem_rad_iff_twoRow_blocks_vanish`.

The reverse inclusion `rad(wtrace) ⊆ θ(tlKernelPulled)` is not addressed here.

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

theorem E_mul_eq_zero {q : K} (hq : q ≠ 0) {a : A} (ha : a * a = (q - q⁻¹) • a + 1) :
    (q • 1 - a) * (a + q⁻¹ • 1) = 0 := by
  have h : (q • (1:A) - a) * (a + q⁻¹ • 1) = q • a + (q * q⁻¹) • (1:A) - a * a - q⁻¹ • a := by
    simp only [sub_mul, mul_add, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    module
  rw [h, ha, mul_inv_cancel₀ hq]; module

theorem E_triple_symm {q : K} (hq : q ≠ 0) {a b : A} (ha : a * a = (q - q⁻¹) • a + 1)
    (hb : b * b = (q - q⁻¹) • b + 1) (hab : a * b * a = b * a * b) :
    (q • 1 - a) * (q • 1 - b) * (q • 1 - a) - (q • 1 - a)
      = (q • 1 - b) * (q • 1 - a) * (q • 1 - b) - (q • 1 - b) := by
  have key : ((q • (1:A) - a) * (q • 1 - b) * (q • 1 - a) - (q • 1 - a))
      - ((q • 1 - b) * (q • 1 - a) * (q • 1 - b) - (q • 1 - b))
      = q • (a * a) - q • (b * b) - (q * q) • a + (q * q) • b + a - b
        - (a * b * a - b * a * b) := by
    simp only [sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
      mul_assoc]
    module
  rw [ha, hb, hab] at key
  rw [← sub_eq_zero, key]
  have : q * (q - q⁻¹) = q * q - 1 := by field_simp
  simp only [smul_add, smul_smul, this, sub_self]
  module
end Alg

open QOU.Mathlib (StandardYoungTableau)
open QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep QOU.SchurWeyl.TableauCells
open QOU.SchurWeyl.Seminormal

section Core
variable {μ : YoungDiagram} {K : Type*} [Field K] (q : K)

theorem seminormalParam_eq_neg_inv (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {d : ℤ} (h : seminormalParam q d = -q⁻¹) : d = -1 := by
  by_contra hd
  unfold seminormalParam at h
  by_cases hden : (1 : K) - q ^ (-2 * d) = 0
  · rw [hden, div_zero] at h
    exact inv_ne_zero hq0 (neg_eq_zero.mp h.symm)
  · rw [div_eq_iff hden] at h
    have hz : q ^ (2 * d + 2) = 1 := by
      have e1 : q ^ (2 * d + 2) = q ^ (2 : ℤ) * (q ^ (-2 * d))⁻¹ := by
        rw [← zpow_neg, ← zpow_add₀ hq0]; ring_nf
      rw [e1]
      have hpow : q ^ (-2 * d) ≠ 0 := zpow_ne_zero _ hq0
      field_simp
      have h' : q * (q - q⁻¹) = q * (-q⁻¹ * (1 - q ^ (-2 * d))) := by rw [h]
      field_simp at h'
      linear_combination h'
    exact zpow_ne_one hq2 (m := 2 * d + 2) (by omega) hz

theorem add_inv_ne_zero (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) :
    q + q⁻¹ ≠ 0 := by
  intro h
  have h4 : q ^ 4 = 1 := by
    have : q ^ 2 = -1 := by
      have := congrArg (· * q) h
      simp only [add_mul, inv_mul_cancel₀ hq0, zero_mul] at this
      linear_combination this
    calc q ^ 4 = (q ^ 2) ^ 2 := by ring
      _ = 1 := by rw [this]; ring
  exact hq2 4 (by norm_num) h4

variable {q}

theorem genMat_congr {k k' : ℕ} (h : k = k') {hk : 1 ≤ k} {hkn : k + 1 ≤ μ.cells.card}
    {hk' : 1 ≤ k'} {hkn' : k' + 1 ≤ μ.cells.card} :
    genMat q k hk hkn = genMat q k' hk' hkn' := by
  subst h; rfl

/-- Entry form of `Y * (genMat + q⁻¹ • 1)`. -/
theorem mul_genMat_add_apply (m : ℕ) (hm : 1 ≤ m) (hmn : m + 1 ≤ μ.cells.card)
    (Y : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K) (T' T) :
    (Y * (genMat q m hm hmn + q⁻¹ • 1)) T' T = (Y * genMat q m hm hmn) T' T + q⁻¹ * Y T' T := by
  rw [Matrix.mul_add, Matrix.add_apply, Matrix.mul_smul, Matrix.mul_one, Matrix.smul_apply,
    smul_eq_mul]

/-- (E1) Same row at `m` kills the column. -/
theorem entry_zero_of_sameRow (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (hm : 1 ≤ m) (hmn : m + 1 ≤ μ.cells.card)
    (Y : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K)
    (hY : Y * (genMat q m hm hmn + q⁻¹ • 1) = 0) (T' T : StandardYoungTableau μ)
    (hrow : (cellOf T m).1 = (cellOf T (m + 1)).1) : Y T' T = 0 := by
  have hm1 : m ∈ Set.Icc 1 μ.cells.card := ⟨hm, by omega⟩
  have hm2 : m + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hmn⟩
  have hna : ¬ SwapAdmissible T m := fun ha => ha.1 hrow
  have hd : axialDist T m = 1 := by
    have m1 : ((cellOf T m).1, (cellOf T m).2) ∈ μ := by simpa using cellOf_mem T hm1
    have m2 : ((cellOf T m).1, (cellOf T (m + 1)).2) ∈ μ := by
      rw [hrow]; simpa using cellOf_mem T hm2
    have e2 : T.entry (cellOf T m).1 (cellOf T (m + 1)).2 = m + 1 := by
      rw [hrow]; exact entry_cellOf T hm2
    exact axialDist_of_sameRow T m1 m2 (entry_cellOf T hm1) e2
  have h := congrFun (congrFun hY T') T
  rw [mul_genMat_add_apply, genMat_mul_apply_of_not_admissible q m hm hmn Y hna, hd,
    seminormalParam_one q hq0 (GenericParameter.sq_ne_one hq2), Matrix.zero_apply] at h
  have h' : Y T' T * (q + q⁻¹) = 0 := by linear_combination h
  exact (mul_eq_zero.mp h').resolve_right (add_inv_ne_zero q hq0 hq2)

/-- (E2) An admissible column whose partner vanishes vanishes. -/
theorem entry_zero_of_partner (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (m : ℕ) (hm : 1 ≤ m) (hmn : m + 1 ≤ μ.cells.card)
    (Y : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K)
    (hY : Y * (genMat q m hm hmn + q⁻¹ • 1) = 0) (T' T : StandardYoungTableau μ)
    (hadm : SwapAdmissible T m) (hS : Y T' (swapTableau T m hm hmn hadm) = 0) :
    Y T' T = 0 := by
  have h := congrFun (congrFun hY T') T
  rw [mul_genMat_add_apply, genMat_mul_apply q m hm hmn Y hadm, hS, Matrix.zero_apply] at h
  have h' : Y T' T * (seminormalParam q (axialDist T m) + q⁻¹) = 0 := by
    linear_combination h
  rcases mul_eq_zero.mp h' with h0 | hpar
  · exact h0
  · have hd : axialDist T m = -1 :=
      seminormalParam_eq_neg_inv q hq0 hq2 (eq_neg_of_add_eq_zero_left hpar)
    have hadm' : SwapAdmissible (swapTableau T m hm hmn hadm) m :=
      swapAdmissible_swapTableau T hm hmn hadm
    have hback : swapTableau (swapTableau T m hm hmn hadm) m hm hmn hadm' = T :=
      swapTableau_involutive T hm hmn hadm
    have hdS : axialDist (swapTableau T m hm hmn hadm) m = 1 := by
      rw [axialDist_swapTableau T hm hmn hadm, hd]; rfl
    have h2 := congrFun (congrFun hY T') (swapTableau T m hm hmn hadm)
    rw [mul_genMat_add_apply, genMat_mul_apply q m hm hmn Y hadm', hback, hdS, hS,
      offDiag_of_not_neg q (by omega), Matrix.zero_apply] at h2
    linear_combination h2

/-- **The joint `-q⁻¹`-eigenspace of two adjacent generators is zero on a shape with at
most two rows** (right-multiplication form). -/
theorem eq_zero_of_twoRow (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    (h2 : μ.rowLen 2 = 0) (k : ℕ) (hk : 1 ≤ k) (hkn : k + 2 ≤ μ.cells.card)
    (Y : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K)
    (hYk : Y * (genMat q k hk (by omega) + q⁻¹ • 1) = 0)
    (hYl : Y * (genMat q (k + 1) (by omega) hkn + q⁻¹ • 1) = 0) : Y = 0 := by
  ext T' T
  rw [Matrix.zero_apply]
  have r0 := row_le_one_of_rowLen_two_eq_zero h2 (cellOf_mem T (k := k) ⟨hk, by omega⟩)
  have r1 := row_le_one_of_rowLen_two_eq_zero h2 (cellOf_mem T (k := k + 1) ⟨by omega, by omega⟩)
  have r2 := row_le_one_of_rowLen_two_eq_zero h2 (cellOf_mem T (k := k + 2) ⟨by omega, hkn⟩)
  by_cases h01 : (cellOf T k).1 = (cellOf T (k + 1)).1
  · exact entry_zero_of_sameRow hq0 hq2 k hk (by omega) Y hYk T' T h01
  by_cases h12 : (cellOf T (k + 1)).1 = (cellOf T (k + 2)).1
  · exact entry_zero_of_sameRow hq0 hq2 (k + 1) (by omega) hkn Y hYl T' T h12
  have h02 : (cellOf T k).1 = (cellOf T (k + 2)).1 := by omega
  by_cases ha : SwapAdmissible T k
  · refine entry_zero_of_partner hq0 hq2 k hk (by omega) Y hYk T' T ha ?_
    apply entry_zero_of_sameRow hq0 hq2 (k + 1) (by omega) hkn Y hYl
    rw [cellOf_swapTableau_succ T hk (by omega) ha,
      cellOf_swapTableau_of_ne T hk (by omega) ha ⟨by omega, hkn⟩ (by omega) (by omega)]
    exact h02
  · have hc01 : (cellOf T k).2 = (cellOf T (k + 1)).2 := by
      by_contra hc
      exact ha ⟨h01, hc⟩
    have ha' : SwapAdmissible T (k + 1) := by
      refine ⟨h12, fun hc => ?_⟩
      have hcell : cellOf T k = cellOf T (k + 2) := Prod.ext h02 (hc01.trans hc)
      have e1 := entry_cellOf T (k := k) ⟨hk, by omega⟩
      have e2 := entry_cellOf T (k := k + 2) ⟨by omega, hkn⟩
      rw [hcell] at e1
      omega
    refine entry_zero_of_partner hq0 hq2 (k + 1) (by omega) hkn Y hYl T' T ha' ?_
    apply entry_zero_of_sameRow hq0 hq2 k hk (by omega) Y hYk
    rw [cellOf_swapTableau_self T (by omega) hkn ha',
      cellOf_swapTableau_of_ne T (by omega) hkn ha' ⟨hk, by omega⟩ (by omega) (by omega)]
    exact h02

end Core

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

/-- On the seminormal side, `θ` sends the pulled-back TL generator `U_i` to `q • E_i` with
`E_i = q - ρ(σ_i)`, which vanishes on the `q`-eigenspace. -/
theorem seminormalRep_theta_U (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {μ : YoungDiagram} (n : ℕ) (hN : μ.cells.card = n + 1) (i : Fin n) :
    seminormalRep q hq0 hq2 n hN
        (theta q hq0 n ((skeinCoxeterEquiv q hq0 n).symm (U K q (AMat n) i)))
      = q • (q • 1 - seminormalGen q n hN i) := by
  rw [U, map_add, map_one, skeinCoxeterEquiv_symm_T, map_add, map_one, map_smul, theta_σ,
    map_add, map_one, map_smul, map_sub, map_smul, map_one, seminormalRep_σ]
  have e : q * (q - q⁻¹) = q * q - 1 := by field_simp
  rw [smul_sub, smul_sub, smul_smul, smul_smul, e, sub_smul, one_smul]
  abel

/-- **`E_i E_j E_i = E_i` on every shape with at most two rows**, for adjacent `i, j`. -/
theorem E_adj_twoRow (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {μ : YoungDiagram} (n : ℕ) (hN : μ.cells.card = n + 1) (h2 : μ.rowLen 2 = 0)
    {i j : Fin n} (hij : adjFin i j) :
    (q • 1 - seminormalGen q n hN i) * (q • 1 - seminormalGen q n hN j)
        * (q • 1 - seminormalGen q n hN i) = q • 1 - seminormalGen q n hN i := by
  set ρ := seminormalRep q hq0 hq2 n hN
  have hquad : ∀ l : Fin n, seminormalGen q n hN l * seminormalGen q n hN l
      = (q - q⁻¹) • seminormalGen q n hN l + 1 := fun l => by
    have := congrArg ρ (σ_sq' q hq0 n l)
    simpa only [ρ, map_mul, map_add, map_smul, map_one, seminormalRep_σ] using this
  have hbraid : seminormalGen q n hN i * seminormalGen q n hN j * seminormalGen q n hN i
      = seminormalGen q n hN j * seminormalGen q n hN i * seminormalGen q n hN j := by
    rcases hij with h | h
    · have hi : (i : ℕ) + 1 < n := h ▸ j.isLt
      have hj : j = ⟨(i : ℕ) + 1, hi⟩ := Fin.ext h.symm
      subst hj
      have := congrArg ρ (Hecke.σ_braid K q q⁻¹ n i hi)
      simpa only [ρ, map_mul, seminormalRep_σ] using this
    · have hj : (j : ℕ) + 1 < n := h ▸ i.isLt
      have hi : i = ⟨(j : ℕ) + 1, hj⟩ := Fin.ext h.symm
      subst hi
      have := congrArg ρ (Hecke.σ_braid K q q⁻¹ n j hj)
      simpa only [ρ, map_mul, seminormalRep_σ] using this.symm
  set Y := (q • 1 - seminormalGen q n hN i) * (q • 1 - seminormalGen q n hN j)
        * (q • 1 - seminormalGen q n hN i) - (q • 1 - seminormalGen q n hN i) with hYdef
  have hYi : Y * (seminormalGen q n hN i + q⁻¹ • 1) = 0 := by
    have : Y = ((q • 1 - seminormalGen q n hN i) * (q • 1 - seminormalGen q n hN j) - 1)
        * (q • 1 - seminormalGen q n hN i) := by rw [hYdef, sub_mul _ (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K), one_mul]
    rw [this, mul_assoc, E_mul_eq_zero hq0 (hquad i), mul_zero]
  have hYj : Y * (seminormalGen q n hN j + q⁻¹ • 1) = 0 := by
    have : Y = ((q • 1 - seminormalGen q n hN j) * (q • 1 - seminormalGen q n hN i) - 1)
        * (q • 1 - seminormalGen q n hN j) := by
      rw [hYdef, E_triple_symm hq0 (hquad i) (hquad j) hbraid,
        sub_mul _ (1 : Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K), one_mul]
    rw [this, mul_assoc, E_mul_eq_zero hq0 (hquad j), mul_zero]
  have hY0 : Y = 0 := by
    rcases hij with h | h
    · exact eq_zero_of_twoRow hq0 hq2 h2 ((i : ℕ) + 1) (by omega)
        (by have := j.isLt; omega) Y hYi (by convert hYj using 3; exact genMat_congr (by omega))
    · exact eq_zero_of_twoRow hq0 hq2 h2 ((j : ℕ) + 1) (by omega)
        (by have := i.isLt; omega) Y hYj (by convert hYi using 3; exact genMat_congr (by omega))
  exact sub_eq_zero.mp hY0

/-- **Every ≤2-row seminormal block kills `θ(tlKernelPulled)`.** -/
theorem seminormalRep_theta_eq_zero (q : K) (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) {δ : K} (hδ : q * δ = q ^ 2 + 1) (n : ℕ)
    {μ : YoungDiagram} (hN : μ.cells.card = n + 1) (h2 : μ.rowLen 2 = 0)
    (x : Hecke K q q⁻¹ n) (hx : x ∈ tlKernelPulled hq0 n hδ) :
    seminormalRep q hq0 hq2 n hN (theta q hq0 n x) = 0 := by
  let φ : HeckeAlgebra K (q ^ 2) (AMat n) →ₐ[K]
      Matrix (StandardYoungTableau μ) (StandardYoungTableau μ) K :=
    ((seminormalRep q hq0 hq2 n hN).comp (theta q hq0 n)).comp
      (skeinCoxeterEquiv q hq0 n).symm.toAlgHom
  have hU : ∀ l : Fin n, φ (U K q (AMat n) l) = q • (q • 1 - seminormalGen q n hN l) :=
    fun l => seminormalRep_theta_U q hq0 hq2 n hN l
  have hφ : ∀ ⦃a b⦄, TLRel K q (AMat n) adjFin a b → φ a = φ b := by
    intro a b hab
    cases hab with
    | adj i j hij =>
      rw [map_mul, map_mul, map_mul, AlgHom.commutes, hU, hU,
        smul_mul_smul_comm, smul_mul_smul_comm, E_adj_twoRow q hq0 hq2 n hN h2 hij,
        Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul, smul_smul]
      congr 1
      ring
  let ψ := RingQuot.liftAlgHom K ⟨φ, hφ⟩
  have hψ : ∀ y, ψ (mkTL K q (AMat n) adjFin y) = φ y := fun y =>
    RingQuot.liftAlgHom_mkAlgHom_apply K φ hφ y
  have hker : heckeToTL hδ (isTypeADiagram_AMat n) (skeinCoxeterEquiv q hq0 n x) = 0 := by
    rw [tlKernelPulled, TwoSidedIdeal.mem_ker] at hx
    exact hx
  have hmk : mkTL K q (AMat n) adjFin (skeinCoxeterEquiv q hq0 n x) = 0 := by
    apply (heckeTLEquiv hδ (isTypeADiagram_AMat n) (w := q⁻¹) (mul_inv_cancel₀ hq0)).injective
    rw [map_zero]
    show quotToTL hδ (isTypeADiagram_AMat n) _ = 0
    rw [quotToTL_mkTL, hker]
  have : φ (skeinCoxeterEquiv q hq0 n x) = 0 := by rw [← hψ, hmk, map_zero]
  simpa [φ] using this

/-- **`θ(tlKernelPulled) ⊆ rad(wtrace)`, over `ℝ`.**  For every real `q ≠ 0` that is not a
root of unity: if `x` lies in the pulled-back Temperley–Lieb kernel, then `θ x` lies in the
trace radical of `wtrace`. -/
theorem theta_mem_rad {q : ℝ} (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
    {δ : ℝ} (hδ : q * δ = q ^ 2 + 1) (n : ℕ) (x : Hecke ℝ q q⁻¹ n)
    (hx : x ∈ tlKernelPulled hq0 n hδ) (b : Hecke ℝ q q⁻¹ n) :
    wtrace q hq0 hq2 n (theta q hq0 n x * b) = 0 := by
  have hq21 : q ^ 2 + 1 ≠ 0 := by positivity
  have hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1 := fun k hk => by
    rw [← pow_mul]; exact hq2 _ (by omega)
  exact (QOU.SchurWeyl.WtraceRadicalTwoRow.mem_rad_iff_twoRow_blocks_vanish hq0 hq2 hq21 hgen n
    (theta q hq0 n x)).mpr
    (fun d hd hrow => seminormalRep_theta_eq_zero q hq0 hq2 hδ n hd hrow x hx) b

end Twisted
end QOU.IwahoriHecke.TLKernelConvention
