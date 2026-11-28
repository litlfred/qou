import QOU.MassTheory.NeumannZagierBloch

/-!
# The symplectic property of the `RᵃL` gluing rows, for every `a`

`NeumannZagierBloch` gives the closed-form gluing rows `raA a`, `raB a` of the
Floyd–Hatcher layering of the once-punctured-torus bundle `RᵃL`, and proves
`A·Bᵀ` symmetric for `3 ≤ a ≤ 8` by computation. This file proves it for **every**
`a ≥ 3` (`ra_isSymm_all`). So every solution of the `RᵃL` rows gives a Bloch class up
to `det B` (`raClass_mem_blochGroup_all`). This covers the lepton words `τ = σ₀⁴σ₁⁻¹`
(`a = 4`) and every longer `σ₀ᵃσ₁⁻¹`.

**Proof.** Over `ℤ` each row is a combination of unit vectors `e_p` at positions
`p ∈ {0, 1, a − 2, a − 1, a, k − 3, k − 2, k − 1}`, all in `[0, a]`. So the entry
`(A Bᵀ)_kl = ∑_j A_kj B_lj` is row `k` of `A` evaluated on row `l` of `B`
(`sum_rowA_mul`). That is a finite sum of `[p = q]` terms in `a, k, l`, and
`evA_rowB_symm` decides the symmetry by splitting one equality at a time (`iz_tac`).
There is no `ℝ` and no limit.

`|det B| = 2(a − 2)` is checked by the probe for `3 ≤ a ≤ 12`. It is not proved here,
and nothing above needs it.
-/

namespace QOU.Archimedean.RaLSymplectic

open QOU.Archimedean.NeumannZagierBloch Matrix

/-- `1` at `0`, else `0`. -/
def iz (x : ℤ) : ℤ := if x = 0 then 1 else 0

theorem sum_iz_mul (a : ℕ) (p : ℤ) (h0 : 0 ≤ p) (h1 : p ≤ a) (f : ℤ → ℤ) :
    ∑ j : Fin (a + 1), iz ((j : ℕ) - p) * f (j : ℕ) = f p := by
  rw [Finset.sum_eq_single ⟨p.toNat, by omega⟩]
  · simp [iz, Int.toNat_of_nonneg h0]
  · intro j _ hj
    have : ((j : ℕ) : ℤ) - p ≠ 0 := by
      intro h; apply hj; ext; simp; omega
    simp [iz, this]
  · simp

/-- Decide a goal built from `if x = 0` by splitting one condition at a time and
pruning every condition that the hypotheses already decide. -/
macro "iz_tac" : tactic =>
  `(tactic| (simp only [iz]; repeat' (first | omega | (simp (disch := omega) only [if_pos, if_neg]) | split)))

/-! ## The rows over `ℤ` -/

/-- Row `k` of `A` (exponents of `z`), as a function of the tetrahedron index `j`. -/
def rowA (a k : ℕ) (j : ℤ) : ℤ :=
  if k = 0 then -2 * iz (j - 0) + 2 * iz (j - (a - 1)) - 2 * iz (j - a)
  else if k = 1 then -iz (j - 0) - iz (j - (a - 2))
  else if k = 2 then -iz (j - 1) - iz (j - a)
  else -iz (j - (k - 3)) - iz (j - (k - 1))

/-- Row `k` of `B` (exponents of `1 − z`). -/
def rowB (a k : ℕ) (j : ℤ) : ℤ :=
  if k = 0 then 2 * iz (j - 0) - 2 * iz (j - (a - 1)) - 2 * iz (j - a)
  else if k = 1 then iz (j - 0) + iz (j - (a - 2)) - 2 * iz (j - (a - 1)) - 2 * iz (j - a)
  else if k = 2 then -2 * iz (j - 0) + iz (j - 1) + iz (j - a)
  else iz (j - (k - 3)) - 2 * iz (j - (k - 2)) + iz (j - (k - 1))

/-- Pairing row `k` of `A` against `F`. -/
def evA (a k : ℕ) (F : ℤ → ℤ) : ℤ :=
  if k = 0 then -2 * F 0 + 2 * F (a - 1) - 2 * F a
  else if k = 1 then -F 0 - F (a - 2)
  else if k = 2 then -F 1 - F a
  else -F (k - 3) - F (k - 1)

theorem raA_apply {a : ℕ} (h2 : 2 ≤ a) (k j : Fin (a + 1)) :
    raA a k j = rowA a k (j : ℕ) := by
  have := k.isLt; have := j.isLt
  simp only [raA, rowA, Matrix.of_apply, ind]
  iz_tac

theorem raB_apply {a : ℕ} (h2 : 2 ≤ a) (k j : Fin (a + 1)) :
    raB a k j = rowB a k (j : ℕ) := by
  have := k.isLt; have := j.isLt
  simp only [raB, rowB, Matrix.of_apply, ind]
  iz_tac

theorem sum_rowA_mul {a : ℕ} (h2 : 2 ≤ a) {k : ℕ} (hk : k ≤ a) (F : ℤ → ℤ) :
    ∑ j : Fin (a + 1), rowA a k (j : ℕ) * F (j : ℕ) = evA a k F := by
  unfold rowA evA
  split_ifs <;>
    simp (disch := omega) only [add_mul, sub_mul, neg_mul, mul_assoc,
      Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_neg_distrib,
      ← Finset.mul_sum, sum_iz_mul a]

set_option maxHeartbeats 4000000 in
theorem evA_rowB_symm {a : ℕ} (h3 : 3 ≤ a) {k l : ℕ} (hk : k ≤ a) (hl : l ≤ a) :
    evA a k (rowB a l) = evA a l (rowB a k) := by
  unfold evA rowB
  split_ifs <;> iz_tac

/-- **The symplectic property of the `RᵃL` rows, for every `a ≥ 3`.** -/
theorem ra_isSymm_all {a : ℕ} (h3 : 3 ≤ a) : (raA a * (raB a)ᵀ).IsSymm := by
  have h2 : 2 ≤ a := by omega
  refine Matrix.IsSymm.ext fun k l => ?_
  simp only [Matrix.mul_apply, Matrix.transpose_apply, raA_apply h2, raB_apply h2]
  rw [sum_rowA_mul h2 (Nat.lt_succ_iff.1 l.isLt) (rowB a k),
    sum_rowA_mul h2 (Nat.lt_succ_iff.1 k.isLt) (rowB a l)]
  exact evA_rowB_symm h3 (Nat.lt_succ_iff.1 l.isLt) (Nat.lt_succ_iff.1 k.isLt)

variable {F : Type*} [Field F] [DecidableEq F]

/-- **Every solution of the `RᵃL` gluing rows gives a Bloch class up to `det B`, for every
`a ≥ 3`.** -/
theorem raClass_mem_blochGroup_all {a : ℕ} (h3 : 3 ≤ a)
    (s : NZSolution F (Fin (a + 1)) (raA a) (raB a)) :
    (raB a).det • nzClass s ∈ PreArchimedeanBloch.BlochGroup F :=
  det_smul_nzClass_mem_blochGroup (ra_isSymm_all h3) s

end QOU.Archimedean.RaLSymplectic
