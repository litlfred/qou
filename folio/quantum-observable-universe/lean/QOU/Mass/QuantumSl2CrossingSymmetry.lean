import QOU.Mass.QuantumSl2ClaspDeltaF

/-!
# Crossing symmetry: the rotated crossing is the inverse crossing

Let `V = V_{m+1}` with the cup and cap of `QuantumSl2CupCap` (Kauffman normalisation: they
carry the sign `(−1)^m`). For an operator `Z` on `V ⊗ V`, its **rotation**

    rot Z = (cap ⊗ 1 ⊗ 1) (1 ⊗ Z ⊗ 1) (1 ⊗ 1 ⊗ cup)

is `Z` turned by a quarter turn. The clasp of van der Veen's Lemma 1 is `rot M`, with `M = Ř²`
the monodromy (`clasp_eq_rotOp`). This file proves

    rot Ř · Ř = 1                                          (`rotOp_rCheck_mul_rCheck`),

that is, `rot Ř = Ř⁻¹`. This is the crossing symmetry of the `U_q(sl₂)` R-matrix in the
unoriented form that the Kauffman normalisation of the cup and cap allows: a positive crossing
turned by a quarter turn is a negative crossing. With it, the cup/cap closure of a diagram
can be moved by planar isotopy past crossings, which is what relates the tangle formula of
van der Veen to the braid-closure quantum trace.

**Method.** Both sides commute with `Δ(F)`. An operator on `V ⊗ V` that commutes with `Δ(F)` is
determined by its columns at `v_0 ⊗ v_k` (`eq_zero_of_deltaF_comm`), because `Δ(F)` reaches
every `v_i ⊗ v_k` from those (the coefficient `[i+1]` of `F v_i` is nonzero). On `v_0 ⊗ v_k`
the R-matrix has a single term, `Ř (v_0 ⊗ v_k) = s^{wt 0 · wt k} v_k ⊗ v_0`, and the rotated
crossing undoes it by the snake identity. No q-series identity is needed.

The identity `rot Ř = Ř⁻¹` was first checked exactly in sympy at `N = 2, 3`, together with the
full Whitehead identity it serves (session scratch; see issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV (duality and the R-matrix)
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Operators commuting with `Δ(F)` are fixed by their columns at `v_0 ⊗ v_k` -/

section Generation

variable (q : 𝕜) (m : ℕ)

/-- **A `Δ(F)`-module map on `V ⊗ V` that kills every `v_0 ⊗ v_k` is zero.** -/
theorem eq_zero_of_deltaF_comm (hF : ∀ i < m, qint q (i + 1) ≠ 0)
    (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hZ : Z * deltaF q m m = deltaF q m m * Z)
    (h0 : ∀ y (k : Fin (m + 1)), Z y (⟨0, by omega⟩, k) = 0) : Z = 0 := by
  have key : ∀ i : ℕ, ∀ hi : i ≤ m, ∀ y (k : Fin (m + 1)), Z y (⟨i, by omega⟩, k) = 0 := by
    intro i
    induction i with
    | zero => intro _ y k; exact h0 y k
    | succ i ih =>
      intro hi y k
      have IH := ih (by omega)
      have h := congrFun (congrFun hZ y) (⟨i, by omega⟩, k)
      -- right side vanishes: the column `(i, k)` of `Z` is zero
      have hR : (deltaF q m m * Z) y (⟨i, by omega⟩, k) = 0 := by
        rw [mul_apply]
        exact Finset.sum_eq_zero fun x _ => by rw [IH x k, mul_zero]
      rw [hR, mul_apply, deltaF] at h
      simp only [add_apply, kroneckerMap_apply, mul_add, Finset.sum_add_distrib,
        Fintype.sum_prod_type] at h
      have h1 : ∑ a : Fin (m + 1), ∑ b : Fin (m + 1),
          Z y (a, b) * (irrepKm q m a ⟨i, by omega⟩ * irrepF q m b k) = 0 := by
        refine Finset.sum_eq_zero fun a _ => Finset.sum_eq_zero fun b _ => ?_
        by_cases ha : a = ⟨i, by omega⟩
        · subst ha; rw [IH y b, zero_mul]
        · rw [irrepKm, diagonal_apply_ne _ ha, zero_mul, mul_zero]
      have h2 : ∑ a : Fin (m + 1), ∑ b : Fin (m + 1),
          Z y (a, b) * (irrepF q m a ⟨i, by omega⟩ * (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) b k)
          = Z y (⟨i + 1, by omega⟩, k) * qint q (i + 1) := by
        rw [Finset.sum_eq_single (⟨i + 1, by omega⟩ : Fin (m + 1))]
        · rw [Finset.sum_eq_single k]
          · simp [irrepF]
          · intro b _ hb; rw [one_apply_ne hb, mul_zero, mul_zero]
          · simp
        · intro a _ ha
          refine Finset.sum_eq_zero fun b _ => ?_
          have : ¬ ((a : ℕ) = i + 1) := fun h => ha (Fin.ext h)
          simp [irrepF, this]
        · simp
      rw [h1, h2, zero_add] at h
      exact (mul_eq_zero.mp h).resolve_right (hF i (by omega))
  ext y x
  exact key x.1 (by omega) y x.2

end Generation

/-! ### The rotation of an operator on `V ⊗ V` -/

section Rotation

variable (q : 𝕜) (m : ℕ)

/-- `1 ⊗ Z ⊗ 1` on the four-fold tensor, for `Z` on `V ⊗ V`. -/
def mid4Op (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    Matrix ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1)))
      ((Fin (m + 1) × Fin (m + 1)) × (Fin (m + 1) × Fin (m + 1))) 𝕜 :=
  ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
    (Z ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))).submatrix (regroup m) (regroup m)

/-- **The rotation** `rot Z = (cap ⊗ 1 ⊗ 1)(1 ⊗ Z ⊗ 1)(1 ⊗ 1 ⊗ cup)` of an operator on `V ⊗ V`. -/
def rotOp (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  (cap4 q m * mid4Op m Z * cup4 q m).submatrix (Equiv.punitProd _).symm (Equiv.prodPUnit _).symm

/-- **Entries of the rotation:** `(rot Z)_{(y₁,y₂),(x₁,x₂)} = Σ_{β,γ} cap(x₁,β) Z_{(β,y₁),(x₂,γ)} cup(γ,y₂)`. -/
theorem rotOp_apply (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (y x : Fin (m + 1) × Fin (m + 1)) :
    rotOp q m Z y x = ∑ β : Fin (m + 1), ∑ γ : Fin (m + 1),
      capVec q m (x.1, β) * Z (β, y.1) (x.2, γ) * cupVec q m (γ, y.2) := by
  obtain ⟨y1, y2⟩ := y
  obtain ⟨x1, x2⟩ := x
  simp only [rotOp, submatrix_apply, mul_apply, cap4, cup4, mid4Op,
    kroneckerMap_apply, capRow, cupCol, of_apply, regroup, Equiv.coe_fn_mk,
    Equiv.punitProd_symm_apply, Equiv.prodPUnit_symm_apply, Fintype.sum_prod_type,
    one_apply, Finset.sum_mul]
  simp only [mul_ite, ite_mul, mul_one, one_mul, mul_zero, zero_mul, Prod.mk.injEq]
  simp [Finset.sum_ite_eq, Finset.sum_ite_eq', ite_and, mul_comm, mul_assoc]
  exact Finset.sum_comm

variable (hq : q ≠ 0)

include hq in
/-- **The rotation of a `Δ(F)`-module map commutes with `Δ(F)`.** -/
theorem rotOp_deltaF (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hZF : Z * deltaF q m m = deltaF q m m * Z)
    (hZK : Z * deltaKm q m m = deltaKm q m m * Z) :
    rotOp q m Z * deltaF q m m = deltaF q m m * rotOp q m Z := by
  have hc : ∀ p < m, qint q (m - p) ≠ 0 := fun p hp => hint (m - p) (by omega) (by omega)
  have hmid : mid4Op m Z * delta4F q m = delta4F q m * mid4Op m Z := by
    have h' : ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Z ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) * delta4F' q m
        = delta4F' q m * ((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ
          (Z ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜))) := by
      unfold delta4F'
      simp only [mul_add, add_mul, ← mul_kronecker_mul, one_mul, mul_one, one_kronecker_one,
        hZK, hZF]
    unfold mid4Op
    rw [delta4F_regroup, ← submatrix_mul _ _ _ _ _ (regroup m).bijective,
      ← submatrix_mul _ _ _ _ _ (regroup m).bijective, h']
  have hbig : cap4 q m * mid4Op m Z * cup4 q m * (deltaF q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜))
      = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaF q m m) * (cap4 q m * mid4Op m Z * cup4 q m) := by
    simp only [Matrix.mul_assoc]
    rw [← delta4F_cup4 q hq m hc, ← Matrix.mul_assoc (mid4Op m Z), hmid, Matrix.mul_assoc,
      ← Matrix.mul_assoc (cap4 q m), cap4_delta4F q hq m hint, Matrix.mul_assoc]
  have h1 : deltaF q m m = (deltaF q m m ⊗ₖ (1 : Matrix Unit Unit 𝕜)).submatrix
      (Equiv.prodPUnit _).symm (Equiv.prodPUnit _).symm := by
    ext a b; simp
  have h2 : deltaF q m m = ((1 : Matrix Unit Unit 𝕜) ⊗ₖ deltaF q m m).submatrix
      (Equiv.punitProd _).symm (Equiv.punitProd _).symm := by
    ext a b; simp
  unfold rotOp
  conv_lhs => rw [h1]
  conv_rhs => rw [h2]
  rw [← submatrix_mul _ _ _ _ _ (Equiv.prodPUnit _).symm.bijective,
    ← submatrix_mul _ _ _ _ _ (Equiv.punitProd _).symm.bijective, hbig]

end Rotation

/-- **The clasp is the rotated monodromy.** -/
theorem clasp_eq_rotOp (s : 𝕜) (hs : s ≠ 0) (m : ℕ) :
    clasp s hs m = rotOp (s ^ 2) m (mono s hs m m) := rfl

/-! ### Crossing symmetry -/

section Crossing

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ)

/-- **The column of `Ř` at `v_0 ⊗ v_k`:** `Ř (v_0 ⊗ v_k) = s^{wt 0 · wt k} v_k ⊗ v_0`. -/
theorem rCheckMat_apply_col0 (k : Fin (m + 1)) (y : Fin (m + 1) × Fin (m + 1)) :
    rCheckMat s hs m m y (⟨0, by omega⟩, k)
      = if y = (k, ⟨0, by omega⟩) then s ^ (wt m 0 * wt m k) else 0 := by
  unfold rCheckMat rMat cartanTheta
  rw [submatrix_apply, id, diagonal_mul, rSum_apply_col0 s hs m m]
  obtain ⟨y1, y2⟩ := y
  by_cases h : (y1, y2) = (k, (⟨0, by omega⟩ : Fin (m + 1)))
  · obtain ⟨rfl, rfl⟩ := Prod.mk.injEq _ _ _ _ ▸ h
    simp
  · rw [if_neg h, if_neg (by simpa [Prod.swap, and_comm] using h), mul_zero]

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **Crossing symmetry: `rot Ř · Ř = 1`**, i.e. the quarter-turned crossing is `Ř⁻¹`. -/
theorem rotOp_rCheck_mul_rCheck (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0) :
    rotOp (s ^ 2) m (rCheckMat s hs m m) * rCheckMat s hs m m = 1 := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hr : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0 := fun k hk =>
    hint (k + 1) (by omega) (by unfold rOrder at hk; omega)
  have hRF := rCheckMat_deltaF s hs hq2 m m hr
  have hRK := rCheckMat_deltaKm s hs m m
  have hrot := rotOp_deltaF (s ^ 2) m hq hint (rCheckMat s hs m m) hRF hRK
  rw [← sub_eq_zero]
  refine eq_zero_of_deltaF_comm (s ^ 2) m (fun i hi => hint (i + 1) (by omega) (by omega)) _ ?_ ?_
  · rw [sub_mul, mul_sub, Matrix.one_mul, Matrix.mul_one, Matrix.mul_assoc, hRF,
      ← Matrix.mul_assoc, hrot, Matrix.mul_assoc]
  · intro y k
    rw [sub_apply, mul_apply, Finset.sum_eq_single (k, (⟨0, by omega⟩ : Fin (m + 1)))]
    · rw [rCheckMat_apply_col0, if_pos rfl, rotOp_apply]
      simp only
      -- only `β = γ = m − k` and `y = (0, k)` survive
      rw [Finset.sum_eq_single (⟨m - k, by omega⟩ : Fin (m + 1))]
      · rw [Finset.sum_eq_single (⟨m - k, by omega⟩ : Fin (m + 1))]
        · rw [rCheckMat_apply_col0]
          by_cases hy : y = (⟨0, by omega⟩, k)
          · subst hy
            simp only [capVec, cupVec, hwVec, if_true, one_apply_eq]
            have hk := k.isLt
            rw [if_pos (by omega), if_pos (by omega)]
            have hsn := snake_coef (s ^ 2) hq m hint k (by omega)
            have hexp : s ^ (wt m 0 * wt m ((⟨m - k, by omega⟩ : Fin (m + 1)) : ℕ))
                * s ^ (wt m 0 * wt m k) = 1 := by
              rw [← zpow_add₀ hs]
              unfold wt
              rw [show ((m : ℤ) - 2 * ((0 : ℕ) : ℤ)) * ((m : ℤ) - 2 * (((m - k : ℕ)) : ℤ))
                  + ((m : ℤ) - 2 * ((0 : ℕ) : ℤ)) * ((m : ℤ) - 2 * ((k : ℕ) : ℤ)) = 0 by
                  push_cast [Nat.cast_sub (show (k : ℕ) ≤ m by omega)]; ring, zpow_zero]
            simp only at hexp
            rw [sub_eq_zero]
            calc capCoefQ (s ^ 2) m k * s ^ (wt m 0 * wt m (m - k)) * hwCoef (s ^ 2) m m m (m - k)
                  * s ^ (wt m 0 * wt m k)
                = (capCoefQ (s ^ 2) m k * hwCoef (s ^ 2) m m m (m - k))
                  * (s ^ (wt m 0 * wt m (m - k)) * s ^ (wt m 0 * wt m k)) := by ring
              _ = 1 := by rw [hsn, hexp, one_mul]
          · rw [one_apply_ne hy, sub_zero]
            obtain ⟨y1, y2⟩ := y
            by_cases h1 : y1 = (⟨0, by omega⟩ : Fin (m + 1))
            · subst h1
              have h2 : y2 ≠ k := fun h => hy (by rw [h])
              have hc : cupVec (s ^ 2) m ((⟨m - k, by omega⟩ : Fin (m + 1)), y2) = 0 := by
                unfold cupVec hwVec
                rw [if_neg]
                intro h; apply h2; ext; simp only at h; omega
              simp only [hc, mul_zero, zero_mul]
            · have hne : ¬ (((⟨m - k, by omega⟩ : Fin (m + 1)), y1) =
                  ((⟨m - k, by omega⟩ : Fin (m + 1)), (⟨0, by omega⟩ : Fin (m + 1)))) :=
                fun h => h1 ((Prod.mk.injEq _ _ _ _).mp h).2
              simp only [if_neg hne, mul_zero, zero_mul]
        · intro γ _ hγ
          rw [rCheckMat_apply_col0]
          by_cases hg : ((⟨m - k, by omega⟩ : Fin (m + 1)), y.1) = (γ, (⟨0, by omega⟩ : Fin (m + 1)))
          · exfalso; apply hγ; exact ((Prod.mk.injEq _ _ _ _).mp hg).1.symm
          · rw [if_neg hg]; simp
        · simp
      · intro β _ hβ
        refine Finset.sum_eq_zero fun γ _ => ?_
        have : ¬ ((k : ℕ) + (β : ℕ) = m) := fun h => hβ (Fin.ext (by simp; omega))
        simp [capVec, this]
      · simp
    · intro x _ hx
      rw [rCheckMat_apply_col0, if_neg hx, mul_zero]
    · simp

end Crossing

end QOU.Mass.QuantumSl2
