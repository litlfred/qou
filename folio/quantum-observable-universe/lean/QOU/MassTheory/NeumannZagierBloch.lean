import QOU.MassTheory.NahmBlochBridge

/-!
# Neumann–Zagier rows define Bloch classes, in every polarization

`NahmBlochBridge` needs an integer symmetric Nahm datum `N`. For the layered
triangulations of the bundles `RᵃL`, `N = −B⁻¹A` is integral for `a ≤ 4` in one
polarization, but fractional for `a ≥ 5`, and the polarization that makes it integral
changes with `a` (`computations/probes/lepton_bundle_nahm_probe.py`). Choosing a
polarization per word to make `N` integral would be a selection. This file removes
the need for it.

**Theorem** (`det_smul_nzClass_mem_blochGroup`). Let `A, B` be square integer matrices
whose rows are gluing equations `∏_j z_j ^ A_kj (1 − z_j) ^ B_kj = 1` with every
`z_j` and `1 − z_j` a unit. If `A Bᵀ` is symmetric (the Neumann–Zagier symplectic
property), then `det B · ∑_i [z_i] ∈ B(F)`.

No integrality of `B⁻¹A`, no invertibility of `B` and no choice of polarization is
assumed (if `det B = 0` the statement is empty). The proof: with `C = adj B`,
combining the rows with `C` gives `det B · (1 − z_i) = −∑_j (CA)_ij · z_i` additively,
and `CA` is symmetric because `det B · CA = C (A Bᵀ) Cᵀ`. So
`det B · δ ∑ [z_i] = −∑_{i,j} (CA)_ij z_i ∧ z_j = 0`.

Pre-Archimedean only: no `ℝ`, `ℂ`, limit or regulator.

-- Ref: [neumann-zagier1985] Neumann, Zagier, Volumes of hyperbolic three-manifolds, Topology 24 (1985) 307-332.
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group, Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-/

namespace QOU.Archimedean.NeumannZagierBloch

open QOU.Archimedean.PreArchimedeanBloch QOU.Archimedean.NahmBlochBridge
  QOU.Archimedean.SubstantiveFillers Matrix

set_option linter.unusedSectionVars false

noncomputable section

variable {F : Type*} [Field F] [DecidableEq F]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- A solution of the gluing rows `(A | B)`: shapes `z_j` and `1 − z_j`, all units, with
`∏_j z_j ^ A_kj (1 − z_j) ^ B_kj = 1` for every row `k`. -/
structure NZSolution (F : Type*) [Field F] (ι : Type*) [Fintype ι]
    (A B : Matrix ι ι ℤ) where
  /-- The shapes. -/
  w : ι → Fˣ
  /-- The complementary shapes `1 − z`. -/
  w' : ι → Fˣ
  hw' : ∀ i, (w' i : F) = 1 - w i
  rows : ∀ k, ∏ j, (w j ^ A k j * w' j ^ B k j) = 1

variable {A B : Matrix ι ι ℤ}

/-- The class `∑_i [z_i]` on the free group. -/
def nzSum (s : NZSolution F ι A B) : PreBlochGroup F := ∑ i, gen (s.w i : F)

/-- The class `∑_i [z_i] ∈ P(F)`. -/
def nzClass (s : NZSolution F ι A B) : PreBloch F := QuotientAddGroup.mk (nzSum s)

/-- `ℤ`-scalar helpers on an additive group, stated with `zsmul` so that they match
`Additive Fˣ` syntactically. -/
theorem zsmul_sum' {G : Type*} [AddCommGroup G] (r : ℤ) (f : ι → G) :
    r • ∑ j, f j = ∑ j, r • f j :=
  map_sum (zsmulAddGroupHom r) f _

theorem sum_zsmul' {G : Type*} [AddCommGroup G] (g : ι → ℤ) (x : G) :
    (∑ j, g j) • x = ∑ j, g j • x :=
  map_sum (zmultiplesHom G x) g _

theorem zsmul_zsmul' {G : Type*} [AddCommGroup G] (a b : ℤ) (x : G) :
    a • b • x = (a * b) • x :=
  (mul_zsmul x a b).symm

/-- The rows, written additively. -/
theorem rows_additive (s : NZSolution F ι A B) (k : ι) :
    ∑ j, (A k j • Additive.ofMul (s.w j) + B k j • Additive.ofMul (s.w' j)) = 0 := by
  have h := congrArg Additive.ofMul (s.rows k)
  simpa [ofMul_prod, ofMul_mul, ofMul_zpow] using h

/-- Combining the rows with `adj B`: `∑_j (adj B · A)_ij z_j + det B · (1 − z_i) = 0`. -/
theorem adjugate_combination (s : NZSolution F ι A B) (i : ι) :
    ∑ j, (B.adjugate * A) i j • Additive.ofMul (s.w j) + B.det • Additive.ofMul (s.w' i) = 0 := by
  have h : ∑ k, B.adjugate i k •
      ∑ j, (A k j • Additive.ofMul (s.w j) + B k j • Additive.ofMul (s.w' j)) = 0 := by
    simp [rows_additive s]
  have hCB : ∀ j, (B.adjugate * B) i j = if i = j then B.det else 0 := by
    intro j
    rw [adjugate_mul, Matrix.smul_apply, Matrix.one_apply]
    split_ifs <;> simp
  have expand : ∑ k, B.adjugate i k •
      ∑ j, (A k j • Additive.ofMul (s.w j) + B k j • Additive.ofMul (s.w' j)) =
      ∑ j, (B.adjugate * A) i j • Additive.ofMul (s.w j) +
        ∑ j, (B.adjugate * B) i j • Additive.ofMul (s.w' j) := by
    simp only [Matrix.mul_apply, zsmul_sum', zsmul_add, Finset.sum_add_distrib, sum_zsmul',
      zsmul_zsmul']
    congr 1 <;> exact Finset.sum_comm
  rw [expand] at h
  simpa [hCB] using h

/-- `adj B · A` is symmetric when `A Bᵀ` is and `det B ≠ 0`. -/
theorem adjugate_mul_isSymm (hS : (A * Bᵀ).IsSymm) (hd : B.det ≠ 0) :
    (B.adjugate * A).IsSymm := by
  have key : B.adjugate * (A * Bᵀ) * (B.adjugate)ᵀ = B.det • (B.adjugate * A) := by
    have : Bᵀ * (B.adjugate)ᵀ = B.det • (1 : Matrix ι ι ℤ) := by
      rw [← transpose_mul, adjugate_mul, transpose_smul, transpose_one]
    calc B.adjugate * (A * Bᵀ) * (B.adjugate)ᵀ
        = B.adjugate * (A * (Bᵀ * (B.adjugate)ᵀ)) := by simp only [Matrix.mul_assoc]
      _ = B.det • (B.adjugate * A) := by
        rw [this, Matrix.mul_smul, Matrix.mul_one, Matrix.mul_smul]
  have hsym : (B.adjugate * (A * Bᵀ) * (B.adjugate)ᵀ).IsSymm := by
    unfold Matrix.IsSymm at hS ⊢
    rw [transpose_mul, transpose_mul, transpose_transpose, hS]
    simp only [Matrix.mul_assoc]
  rw [key] at hsym
  unfold Matrix.IsSymm at hsym ⊢
  rw [transpose_smul] at hsym
  exact smul_right_injective _ hd hsym

/-- **Neumann–Zagier rows give a Bloch class, up to `det B`.** -/
theorem det_smul_nzClass_mem_blochGroup (hS : (A * Bᵀ).IsSymm) (s : NZSolution F ι A B) :
    B.det • nzClass s ∈ BlochGroup F := by
  by_cases hd : B.det = 0
  · simp [hd]
  have hM := adjugate_mul_isSymm hS hd
  set M := B.adjugate * A
  have hne : ∀ i, (s.w i : F) ≠ 1 := fun i h => by
    have := s.hw' i
    rw [h, sub_self] at this
    exact (Units.ne_zero _) this
  have hgen : ∀ i, delta (wedge F) (gen (s.w i : F)) =
      wedge F (Additive.ofMul (s.w i)) (Additive.ofMul (s.w' i)) := fun i => by
    rw [delta_gen _ (s.w i).ne_zero (hne i), ← s.hw' i, u_units, u_units]
  simp only [BlochGroup, AddMonoidHom.mem_ker, nzClass, ← QuotientAddGroup.mk_zsmul,
    deltaP_mk, map_zsmul, nzSum, map_sum, hgen, Finset.smul_sum]
  have step : ∀ i, B.det • wedge F (Additive.ofMul (s.w i)) (Additive.ofMul (s.w' i)) =
      - ∑ j, M i j • wedge F (Additive.ofMul (s.w i)) (Additive.ofMul (s.w j)) := fun i => by
    rw [← map_zsmul, eq_neg_of_add_eq_zero_right (adjugate_combination s i), map_neg,
      map_sum]
    simp [map_zsmul, M]
  simp only [step, Finset.sum_neg_distrib, neg_eq_zero]
  refine sum_sum_eq_zero_of_antisymm _ (fun i j => ?_) (fun i => ?_)
  · rw [wedge_antisymm, smul_neg, show M j i = M i j from hM.apply i j]
  · rw [wedge_self, smul_zero]

/-! ## The gluing rows of the bundles `RᵃL`, `a ≥ 2`

The formulas hold for `a ≥ 2`; the Bloch statement below needs `a ≥ 3`.

Tetrahedra `0, …, a` (one per letter). Row `0` is the cusp row; rows `1, …, a` are the
edge rows other than the first (which is dependent). The formulas are read off the
Floyd–Hatcher layering in `nz_gluing_from_braid_monodromy_probe.py`; the probe
`lepton_bundle_nahm_probe.py` checks they equal the layering's rows, and that `A Bᵀ` is symmetric, for
`2 ≤ a ≤ 12`. A proof of the symmetry for every `a` is not given here. -/

/-- `1` if `j = p`, else `0`. -/
def ind (p j : ℕ) : ℤ := if j = p then 1 else 0

/-- Exponents of `z` in the rows of `RᵃL`. -/
def raA (a : ℕ) : Matrix (Fin (a + 1)) (Fin (a + 1)) ℤ := Matrix.of fun k j =>
  if k.val = 0 then -2 * ind 0 j + 2 * ind (a - 1) j - 2 * ind a j
  else if k.val = 1 then -ind 0 j - ind (a - 2) j
  else if k.val = 2 then -ind 1 j - ind a j
  else -ind (k.val - 3) j - ind (k.val - 1) j

/-- Exponents of `1 − z` in the rows of `RᵃL`. -/
def raB (a : ℕ) : Matrix (Fin (a + 1)) (Fin (a + 1)) ℤ := Matrix.of fun k j =>
  if k.val = 0 then 2 * ind 0 j - 2 * ind (a - 1) j - 2 * ind a j
  else if k.val = 1 then ind 0 j + ind (a - 2) j - 2 * ind (a - 1) j - 2 * ind a j
  else if k.val = 2 then -2 * ind 0 j + ind 1 j + ind a j
  else ind (k.val - 3) j - 2 * ind (k.val - 2) j + ind (k.val - 1) j

/-- **The symplectic property for `a = 3, …, 8`**, by computation. -/
theorem ra_isSymm_3 : (raA 3 * (raB 3)ᵀ).IsSymm := by decide
theorem ra_isSymm_4 : (raA 4 * (raB 4)ᵀ).IsSymm := by decide
theorem ra_isSymm_5 : (raA 5 * (raB 5)ᵀ).IsSymm := by decide
theorem ra_isSymm_6 : (raA 6 * (raB 6)ᵀ).IsSymm := by decide
theorem ra_isSymm_7 : (raA 7 * (raB 7)ᵀ).IsSymm := by decide
theorem ra_isSymm_8 : (raA 8 * (raB 8)ᵀ).IsSymm := by decide

theorem ra_isSymm {a : ℕ} (h3 : 3 ≤ a) (h8 : a ≤ 8) : (raA a * (raB a)ᵀ).IsSymm := by
  interval_cases a
  exacts [ra_isSymm_3, ra_isSymm_4, ra_isSymm_5, ra_isSymm_6, ra_isSymm_7,
    ra_isSymm_8]

/-- **Every solution of the `RᵃL` gluing rows gives a Bloch class up to `det B`**, for
`3 ≤ a ≤ 8`. This covers `τ` (`a = 4`) without choosing a polarization; `det B` is
`±2(a − 2) ≠ 0` there (probe). For `a = 2` (`μ`) this cusp row has the same `B`-part as
edge row `1`, so `det B = 0` and the statement is empty; `μ` is covered by the integral
datum in `LeptonBundleNahm`. -/
theorem raClass_mem_blochGroup {a : ℕ} (h3 : 3 ≤ a) (h8 : a ≤ 8)
    (s : NZSolution F (Fin (a + 1)) (raA a) (raB a)) :
    (raB a).det • nzClass s ∈ BlochGroup F :=
  det_smul_nzClass_mem_blochGroup (ra_isSymm h3 h8) s

end

end QOU.Archimedean.NeumannZagierBloch
