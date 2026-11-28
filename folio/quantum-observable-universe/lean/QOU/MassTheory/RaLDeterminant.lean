import QOU.MassTheory.RaLSymplectic

/-!
# `|det B| = 2(a - 2)` for the `RᵃL` Neumann–Zagier matrix

`RaLSymplectic` proves that the gluing matrices `raA a`, `raB a` of the layered
triangulation of the once-punctured-torus bundle of `RᵃL` satisfy `A·Bᵀ` symmetric for
every `a ≥ 3`. This file computes the other half of the state-integral input: the
determinant of `B`.

**Theorem** (`abs_det_raB`). For every `a ≥ 3`, `|det (raB a)| = 2(a - 2)`.

Proof. Multiply by the integer matrix `V` with columns `1`, `(m)_m`, `e_a`, `e_2`, …,
`e_{a-1}`. Then `B·V` is block lower triangular: its `3 × 3` corner `corner a` has
determinant `-2(a - 2)` (`corner_det`), and the remaining block is unitriangular
(`BV_interior`). The matrix `V` is a column permutation of a lower unitriangular matrix
`V₀`, so `|det V| = 1` (`abs_det_V`).

Consequence (`raB_det_ne_zero`): `det B ≠ 0`, so with `det_smul_nzClass_mem_blochGroup`
the class `det B • Σ[z]` lies in the Bloch group, and the quadratic form `N = -B⁻¹A`
exists over `ℚ` for every word in the family. All integer arithmetic; no analytic input.
-/


namespace QOU.Archimedean.RaLDeterminant

open QOU.Archimedean.NeumannZagierBloch QOU.Archimedean.RaLSymplectic Matrix

/-- Pairing row `k` of `B` against `F`. -/
def evB (a k : ℕ) (F : ℤ → ℤ) : ℤ :=
  if k = 0 then 2 * F 0 - 2 * F (a - 1) - 2 * F a
  else if k = 1 then F 0 + F (a - 2) - 2 * F (a - 1) - 2 * F a
  else if k = 2 then -2 * F 0 + F 1 + F a
  else F (k - 3) - 2 * F (k - 2) + F (k - 1)

theorem sum_rowB_mul {a : ℕ} (h2 : 2 ≤ a) {k : ℕ} (hk : k ≤ a) (F : ℤ → ℤ) :
    ∑ j : Fin (a + 1), rowB a k (j : ℕ) * F (j : ℕ) = evB a k F := by
  unfold rowB evB
  split_ifs <;>
    simp (disch := omega) only [add_mul, sub_mul, neg_mul, mul_assoc,
      Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_neg_distrib,
      ← Finset.mul_sum, sum_iz_mul a]

/-- Column `c` of the change of basis `V = [1, (m)_m, e_a, e_2, …, e_{a−1}]`. -/
def vcol (a c : ℕ) (m : ℤ) : ℤ :=
  if c = 0 then 1 else if c = 1 then m else if c = 2 then iz (m - a) else iz (m - (c - 1))

def V (a : ℕ) : Matrix (Fin (a + 1)) (Fin (a + 1)) ℤ := of fun m c => vcol a c m

theorem BV_apply {a : ℕ} (h2 : 2 ≤ a) (i c : Fin (a + 1)) :
    (raB a * V a) i c = evB a i (vcol a c) := by
  simp only [Matrix.mul_apply, raB_apply h2, V, of_apply]
  exact sum_rowB_mul h2 (Nat.lt_succ_iff.1 i.isLt) _

/-- Interior rows vanish on the first three columns. -/
theorem BV_lower_left {a : ℕ} (h3 : 3 ≤ a) (i : Fin (a + 1)) (hi : ¬ (i : ℕ) < 3)
    (c : Fin (a + 1)) (hc : (c : ℕ) < 3) : (raB a * V a) i c = 0 := by
  rw [BV_apply (by omega)]
  have := i.isLt
  unfold evB vcol
  iz_tac

/-- Interior rows are lower unitriangular. -/
theorem BV_interior {a : ℕ} (h3 : 3 ≤ a) (i c : Fin (a + 1)) (hi : 3 ≤ (i : ℕ))
    (hc : 3 ≤ (c : ℕ)) :
    (raB a * V a) i c = if (i : ℕ) < c then 0 else if (i : ℕ) = c then 1 else
      (raB a * V a) i c := by
  have := i.isLt; have := c.isLt
  split_ifs with h1 h2
  · rw [BV_apply (by omega)]; unfold evB vcol; iz_tac
  · rw [BV_apply (by omega)]; unfold evB vcol; iz_tac
  · rfl

/-- The entries of the `3 × 3` corner of `raB a * V a`. -/
def cornerFn (a r c : ℕ) : ℤ :=
  if r = 2 then (if c = 0 then 0 else if c = 1 then (a : ℤ) + 1 else 1)
  else if r = 1 then (if c = 1 then -3 * (a : ℤ) else -2)
  else (if c = 1 then -(4 * (a : ℤ) - 2) else -2)

/-- The `3 × 3` corner of `raB a * V a`. -/
def corner (a : ℕ) : Matrix (Fin 3) (Fin 3) ℤ := of fun r c => cornerFn a r c

/-- The corner entries as a function of naturals. -/
theorem evB_corner {a : ℕ} (h3 : 3 ≤ a) (r c : ℕ) (hr : r < 3) (hc : c < 3) :
    evB a r (vcol a c) = cornerFn a r c := by
  interval_cases r <;> interval_cases c <;>
    simp only [evB, vcol, cornerFn, iz, reduceIte, Nat.reduceEqDiff, OfNat.ofNat_ne_zero,
      one_ne_zero, OfNat.zero_ne_ofNat, zero_ne_one] <;>
    (try split_ifs) <;> omega

theorem BV_corner {a : ℕ} (h3 : 3 ≤ a) (r c : Fin 3) :
    (raB a * V a) ⟨r, by have := r.isLt; omega⟩ ⟨c, by have := c.isLt; omega⟩ = corner a r c := by
  rw [BV_apply (by omega)]
  exact evB_corner h3 r c r.isLt c.isLt

theorem corner_det (a : ℕ) : (corner a).det = -2 * ((a : ℤ) - 2) := by
  simp [corner, cornerFn, Matrix.det_fin_three]
  ring

/-- `raB a * V a` has determinant `-2(a - 2)`. -/
theorem det_BV {a : ℕ} (h3 : 3 ≤ a) : (raB a * V a).det = -2 * ((a : ℤ) - 2) := by
  rw [twoBlockTriangular_det _ (fun i : Fin (a + 1) => (i : ℕ) < 3)
    (fun i hi j hj => BV_lower_left h3 i hi j hj)]
  have hlow : (toSquareBlockProp (raB a * V a) fun i : Fin (a + 1) => ¬ (i : ℕ) < 3).det = 1 := by
    rw [det_of_lowerTriangular]
    · refine Finset.prod_eq_one fun i _ => ?_
      have h := BV_interior h3 i.1 i.1 (by have := i.2; omega) (by have := i.2; omega)
      simp only [lt_irrefl, if_false, if_true] at h
      simpa [toSquareBlockProp, toBlock_apply] using h
    · intro i j hij
      have hij' : (i.1 : ℕ) < j.1 := hij
      have h := BV_interior h3 i.1 j.1 (by have := i.2; omega) (by have := j.2; omega)
      simp only [hij', if_true] at h
      simpa [toSquareBlockProp, toBlock_apply] using h
  let e : Fin 3 ≃ {i : Fin (a + 1) // (i : ℕ) < 3} :=
    { toFun := fun r => ⟨⟨r, by have := r.isLt; omega⟩, r.isLt⟩
      invFun := fun i => ⟨i.1, i.2⟩
      left_inv := fun r => rfl
      right_inv := fun i => rfl }
  have hcorner : (toSquareBlockProp (raB a * V a) fun i : Fin (a + 1) => (i : ℕ) < 3).det =
      -2 * ((a : ℤ) - 2) := by
    rw [← det_submatrix_equiv_self e, ← corner_det a]
    congr 1
    ext r c
    simpa [toSquareBlockProp, toBlock_apply, e] using BV_corner h3 r c
  rw [hlow, hcorner, mul_one]

/-- The column-reordered matrix: `V₀ m c = 1, m, [m = c]` for `c = 0, 1, ≥ 2`. -/
def V₀ (a : ℕ) : Matrix (Fin (a + 1)) (Fin (a + 1)) ℤ :=
  of fun m c => if (c : ℕ) = 0 then 1 else if (c : ℕ) = 1 then (m : ℤ) else iz ((m : ℤ) - c)

theorem det_V₀ (a : ℕ) : (V₀ a).det = 1 := by
  rw [det_of_lowerTriangular]
  · refine Finset.prod_eq_one fun i _ => ?_
    simp only [V₀, of_apply, sub_self, iz, if_true]
    split_ifs <;> omega
  · intro i j hij
    have hij' : (i : ℕ) < j := hij
    simp only [V₀, of_apply, iz]
    split_ifs <;> omega

/-- The column map `0 ↦ 0`, `1 ↦ 1`, `2 ↦ a`, `c ↦ c - 1` for `c ≥ 3`. -/
def colMap (a : ℕ) (c : Fin (a + 1)) : Fin (a + 1) :=
  ⟨if (c : ℕ) < 2 then c else if (c : ℕ) = 2 then a else c - 1, by
    have := c.isLt; split_ifs <;> omega⟩

theorem colMap_injective {a : ℕ} (h3 : 3 ≤ a) : Function.Injective (colMap a) := by
  intro c d h
  have h' := congrArg Fin.val h
  simp only [colMap] at h'
  have := c.isLt; have := d.isLt
  ext; split_ifs at h' <;> omega

theorem V_eq_submatrix {a : ℕ} (h3 : 3 ≤ a) : V a = (V₀ a).submatrix id (colMap a) := by
  ext m c
  have := c.isLt
  simp only [V, V₀, vcol, colMap, submatrix_apply, id, of_apply]
  split_ifs <;> first | rfl | omega | (congr 1; omega)

theorem abs_det_V {a : ℕ} (h3 : 3 ≤ a) : |(V a).det| = 1 := by
  let σ : Equiv.Perm (Fin (a + 1)) :=
    Equiv.ofBijective (colMap a) (Finite.injective_iff_bijective.mp (colMap_injective h3))
  have : V a = (V₀ a).submatrix id σ := V_eq_submatrix h3
  rw [this, det_permute', det_V₀, mul_one]
  rcases Int.units_eq_one_or (Equiv.Perm.sign σ) with h | h <;> simp [h]

/-- **`|det B| = 2(a - 2)`** for the `RᵃL` Neumann–Zagier matrix, for every `a ≥ 3`. -/
theorem abs_det_raB {a : ℕ} (h3 : 3 ≤ a) : |(raB a).det| = 2 * ((a : ℤ) - 2) := by
  have h := congrArg abs (det_BV h3)
  rw [det_mul, abs_mul, abs_det_V h3, mul_one] at h
  rw [h, abs_mul, abs_of_nonneg (by omega : (0 : ℤ) ≤ (a : ℤ) - 2)]
  norm_num

theorem raB_det_ne_zero {a : ℕ} (h3 : 3 ≤ a) : (raB a).det ≠ 0 := by
  intro h; have := abs_det_raB h3; rw [h, abs_zero] at this; omega

end QOU.Archimedean.RaLDeterminant
