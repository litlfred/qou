import BraidKnotOctonion.MarkovTraceInstance
import HeckeTemperleyLieb.AxialDistanceBound
import HeckeTemperleyLieb.OcneanuWeightTwoRowPositive

/-!
# QOU.SchurWeyl.WtraceTwistedPositivity — the Markov trace at `z_D` is positive on `X·X†`

`wtrace` (`MarkovTraceInstance`) is the Markov trace on `H_{n+1}(q)` at convention D,
`z_D = q³/(q²+1)`. The untwisted form `wtrace(X·X)` is **not** positive for `n + 1 ≥ 3`
(`t-beta-markov-frobenius-collapse-general.lean`, bean `qou-baov`). This file proves that the twisted
form is:

  `0 ≤ wtrace(X · X†)`   for every `X`, whenever `1 < q`,

where `†` is the anti-involution of `H_{n+1}(q)` fixing every generator `σᵢ`. It also proves
`wtrace(X†) = wtrace(X)`.

## The argument

* **`†` exists** (`Hecke.dag`): the relations are palindromic (quadratic, braid) or symmetric
  (far commutation), so `σᵢ ↦ op σᵢ` lifts to an algebra map into the opposite algebra.
* **Each seminormal block is self-adjoint for a positive diagonal form.** Young's seminormal
  matrices are not symmetric: the two off-diagonal entries of a size-2 orbit are `1` and
  `1 + a(d)a(-d)`. Put `D_T = ∏_{a<b} g(c_T(b) − c_T(a))` over pairs of entries of `T`, with
  `g(d) = 1 + a(d)a(−d)` for `d ≤ −2` and `g(d) = 1` otherwise (`pairW`). The swap `s_k`
  permutes the pairs and reverses only `(k, k+1)`, which gives
  `D_{s_k T}·ρ(σ_k)_{s_k T, T} = ρ(σ_k)_{T, s_k T}·D_T` (`pairW_mul_genMat`), i.e.
  `D·ρ(σ_k) = ρ(σ_k)ᵀ·D`. Multiplicativity then gives `D·ρ(X†) = ρ(X)ᵀ·D` for all `X`
  (`diag_mul_rep_dag`).
* **Positivity of `D`** for `q > 1`: `1 + a(d)a(−d) > 0` when `|d| ≥ 2` (`offDiag_pos`).
* **Positivity of the trace.** `tr(ρ(X)ρ(X†)) = Σ_{T,T'} ρ(X)_{T T'}² · D_T / D_{T'} ≥ 0`, and every
  weight at `z_D` is `≥ 0`: positive on shapes with at most two rows
  (`ocneanuWeight_conventionD_pos_of_two_rows`), zero on the rest
  (`ocneanuWeight_conventionD_eq_zero_of_three_rows`).

## What is not claimed

**Non-degeneracy fails.** The weights vanish on every shape with three rows, so for `n + 1 ≥ 3`
the form `wtrace(X·X†)` has a nonzero radical (`OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal`
at `n + 1 = 3`). The equality half of the T_β collapse (`TwistedNonDegTrace`) therefore does not
apply to `wtrace` at `z_D`; only the inequality half does.

## Base ring (§7c)

`[Field K] [LinearOrder K] [IsStrictOrderedRing K]` with `1 < q`. The order is used for the
positivity of `D` and of the weights. No `ℝ`.
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells Seminormal

/-! ## 1. The anti-involution `†` fixing each generator -/

namespace Hecke

variable (K : Type*) [CommRing K] (q qi : K) (n : ℕ)

/-- `σᵢ ↦ op σᵢ`, an algebra map into the opposite algebra. -/
noncomputable def dagOp : Hecke K q qi n →ₐ[K] (Hecke K q qi n)ᵐᵒᵖ :=
  lift K q qi n (fun i => MulOpposite.op (σ K q qi n i))
    (fun i => by
      apply MulOpposite.unop_injective
      simp only [MulOpposite.unop_mul, MulOpposite.unop_op, MulOpposite.unop_add,
        MulOpposite.unop_smul, MulOpposite.unop_one]
      exact σ_quadratic K q qi n i)
    (fun i hi => by
      apply MulOpposite.unop_injective
      simp only [MulOpposite.unop_mul, MulOpposite.unop_op]
      have h := σ_braid K q qi n i hi
      simpa only [mul_assoc] using h)
    (fun i j hij => by
      apply MulOpposite.unop_injective
      simp only [MulOpposite.unop_mul, MulOpposite.unop_op]
      exact (σ_commute K q qi n i j hij).symm)

/-- **The anti-involution `†`** of `H_n(q)` with `σᵢ† = σᵢ`, as a `K`-linear map. -/
noncomputable def dag : Hecke K q qi n →ₗ[K] Hecke K q qi n :=
  (MulOpposite.opLinearEquiv K).symm.toLinearMap ∘ₗ (dagOp K q qi n).toLinearMap

theorem dag_apply (x : Hecke K q qi n) : dag K q qi n x = MulOpposite.unop (dagOp K q qi n x) :=
  rfl

@[simp] theorem dag_one : dag K q qi n 1 = 1 := by
  simp [dag_apply]

theorem dag_mul (x y : Hecke K q qi n) : dag K q qi n (x * y) = dag K q qi n y * dag K q qi n x := by
  simp [dag_apply]

@[simp] theorem dag_σ (i : Fin n) : dag K q qi n (σ K q qi n i) = σ K q qi n i := by
  simp [dag_apply, dagOp]

@[simp] theorem dag_algebraMap (r : K) :
    dag K q qi n (algebraMap K (Hecke K q qi n) r) = algebraMap K (Hecke K q qi n) r := by
  simp [dag_apply]

end Hecke

namespace SeminormalRep

variable {K : Type*} [Field K]

/-! ## 2. The diagonal form `D` -/

section Form

variable (q : K) {μ : YoungDiagram}

/-- The content of the cell holding entry `m`. -/
noncomputable def cnt (T : StandardYoungTableau μ) (m : ℕ) : ℤ :=
  QOU.SchurWeyl.cellContent (cellOf T m)

/-- The pair factor: `1 + a(d)a(-d)` for `d ≤ −2`, and `1` otherwise. -/
noncomputable def gfac (d : ℤ) : K := if d ≤ -2 then offDiag q d else 1

/-- The factor of the pair `p = (a, b)` of entries. -/
noncomputable def pairFac (T : StandardYoungTableau μ) (p : ℕ × ℕ) : K :=
  if p.1 < p.2 then gfac q (cnt T p.2 - cnt T p.1) else 1

/-- **The diagonal weight `D_T`**: the product of the pair factors over all pairs of entries. -/
noncomputable def pairW (T : StandardYoungTableau μ) : K :=
  ∏ p ∈ Finset.Icc 1 μ.cells.card ×ˢ Finset.Icc 1 μ.cells.card, pairFac q T p

theorem axialDist_eq_cnt (T : StandardYoungTableau μ) (k : ℕ) :
    axialDist T k = cnt T (k + 1) - cnt T k := rfl

/-- The swap moves the cell of `m` to the cell of `swapVal k m`. -/
theorem cellOf_swapTableau (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) {m : ℕ}
    (hm : m ∈ Set.Icc 1 μ.cells.card) :
    cellOf (swapTableau T k hk hkn hadm) m = cellOf T (swapVal k m) := by
  by_cases h0 : m = k
  · subst h0
    rw [cellOf_swapTableau_self]
    simp [swapVal]
  · by_cases h1 : m = k + 1
    · subst h1
      rw [cellOf_swapTableau_succ]
      simp [swapVal]
    · rw [cellOf_swapTableau_of_ne T hk hkn hadm hm h0 h1, swapVal_of_ne k m h0 h1]

/-- Away from the pair `{k, k+1}`, `swapVal k` preserves the order. -/
theorem swapVal_lt_iff {k a b : ℕ} (h : ¬(a = k ∧ b = k + 1)) (h' : ¬(a = k + 1 ∧ b = k)) :
    swapVal k a < swapVal k b ↔ a < b := by
  unfold swapVal
  split_ifs <;> omega

/-- **The swap changes `D` only through the pair `(k, k+1)`.** -/
theorem pairW_swapTableau (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    pairW q (swapTableau T k hk hkn hadm) * gfac q (axialDist T k)
      = pairW q T * gfac q (-axialDist T k) := by
  classical
  set S := Finset.Icc 1 μ.cells.card ×ˢ Finset.Icc 1 μ.cells.card with hS
  set T' := swapTableau T k hk hkn hadm
  set sw : ℕ × ℕ → ℕ × ℕ := fun p => (swapVal k p.1, swapVal k p.2) with hsw
  have hIcc : ∀ m, m ∈ Finset.Icc 1 μ.cells.card → swapVal k m ∈ Finset.Icc 1 μ.cells.card := by
    intro m hm
    simp only [Finset.mem_Icc] at hm ⊢
    unfold swapVal
    split_ifs <;> omega
  have hswS : ∀ p ∈ S, sw p ∈ S := by
    intro p hp
    rw [hS, Finset.mem_product] at hp ⊢
    exact ⟨hIcc _ hp.1, hIcc _ hp.2⟩
  -- reindex the product for `T'` by `sw`
  have hre : pairW q T' = ∏ p ∈ S, pairFac q T' (sw p) := by
    unfold pairW
    refine (Finset.prod_nbij' sw sw hswS hswS (fun p _ => ?_) (fun p _ => ?_) (fun p _ => rfl)).symm
    · simp [hsw, swapVal_involutive]
    · simp [hsw, swapVal_involutive]
  -- `pairFac T' (sw p)` in terms of `T`
  have hcnt : ∀ m ∈ Finset.Icc 1 μ.cells.card, cnt T' (swapVal k m) = cnt T m := by
    intro m hm
    have hm' : swapVal k m ∈ Set.Icc 1 μ.cells.card := by
      have := hIcc m hm
      simpa [Finset.mem_Icc, Set.mem_Icc] using this
    unfold cnt
    rw [cellOf_swapTableau T hk hkn hadm hm', swapVal_involutive]
  set d := axialDist T k with hd
  have hk0 : k ∈ Finset.Icc 1 μ.cells.card := by simp [Finset.mem_Icc]; omega
  have hk1 : k + 1 ∈ Finset.Icc 1 μ.cells.card := by simp [Finset.mem_Icc]; omega
  have hkS : (k, k + 1) ∈ S := by rw [hS, Finset.mem_product]; exact ⟨hk0, hk1⟩
  have hkS' : (k + 1, k) ∈ S := by rw [hS, Finset.mem_product]; exact ⟨hk1, hk0⟩
  have hpt : ∀ p ∈ S,
      pairFac q T' (sw p) * (if p = (k, k + 1) then gfac q d else 1)
        = pairFac q T p * (if p = (k + 1, k) then gfac q (-d) else 1) := by
    intro p hp
    rw [hS, Finset.mem_product] at hp
    obtain ⟨a, b⟩ := p
    simp only at hp
    unfold pairFac
    simp only [hsw, hcnt a hp.1, hcnt b hp.2]
    have e1 : swapVal k k = k + 1 := by simp [swapVal]
    have e2 : swapVal k (k + 1) = k := by simp [swapVal]
    by_cases h1 : a = k ∧ b = k + 1
    · obtain ⟨ha, hb⟩ := h1
      rw [ha, hb, e1, e2, if_neg (by omega), if_pos rfl, if_pos (by omega),
        if_neg (by simp), hd, axialDist_eq_cnt]
      ring
    · by_cases h2 : a = k + 1 ∧ b = k
      · obtain ⟨ha, hb⟩ := h2
        rw [ha, hb, e1, e2, if_pos (by omega : k < k + 1), if_neg (by simp), if_neg (by omega),
          if_pos rfl, hd, axialDist_eq_cnt, neg_sub]
        ring
      · have hne1 : (a, b) ≠ (k, k + 1) := fun h => h1 (by simpa using h)
        have hne2 : (a, b) ≠ (k + 1, k) := fun h => h2 (by simpa using h)
        rw [if_neg hne1, if_neg hne2]
        have hlt := swapVal_lt_iff (k := k) (a := a) (b := b) h1 h2
        simp only [hlt]
  have hprod := Finset.prod_congr rfl hpt
  rw [Finset.prod_mul_distrib, Finset.prod_mul_distrib, Finset.prod_ite_eq' S (k, k + 1),
    Finset.prod_ite_eq' S (k + 1, k), if_pos hkS, if_pos hkS'] at hprod
  rw [hre]
  unfold pairW
  exact hprod

/-- The swapped tableau has the opposite axial distance. -/
theorem axialDist_swapTableau (T : StandardYoungTableau μ) {k : ℕ} (hk : 1 ≤ k)
    (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k) :
    axialDist (swapTableau T k hk hkn hadm) k = -axialDist T k := by
  unfold axialDist
  rw [cellOf_swapTableau_self, cellOf_swapTableau_succ]
  simp only [QOU.SchurWeyl.axialDistance]
  ring

/-- **`D` is self-adjoint for each generator**, entrywise:
`D_{T'}·ρ(σ_k)_{T' T} = ρ(σ_k)_{T T'}·D_T`. -/
theorem pairW_mul_genMat (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card)
    (T' T : StandardYoungTableau μ) :
    pairW q T' * genMat q k hk hkn T' T = genMat q k hk hkn T T' * pairW q T := by
  classical
  have hkI : k ∈ Set.Icc 1 μ.cells.card := ⟨hk, by omega⟩
  have hk1I : k + 1 ∈ Set.Icc 1 μ.cells.card := ⟨by omega, hkn⟩
  by_cases heq : T' = T
  · subst heq; ring
  by_cases hadm : SwapAdmissible T k
  · by_cases hT' : T' = swapTableau T k hk hkn hadm
    · -- the orbit pair
      have hadm' : SwapAdmissible T' k := hT' ▸ swapAdmissible_swapTableau T hk hkn hadm
      have hTT : T = swapTableau T' k hk hkn hadm' := by
        subst hT'; exact (swapTableau_involutive T hk hkn hadm).symm
      have hne' : swapTableau T' k hk hkn hadm' ≠ T' := by rw [← hTT]; exact Ne.symm heq
      have e1 : genMat q k hk hkn T' T = offDiag q (axialDist T k) := by
        rw [hT']; exact genMat_swap q k hk hkn hadm (by rw [← hT']; exact heq)
      have e2 : genMat q k hk hkn T T' = offDiag q (-axialDist T k) := by
        conv_lhs => rw [hTT]
        rw [genMat_swap q k hk hkn hadm' hne', hT', axialDist_swapTableau]
      rw [e1, e2]
      have key := pairW_swapTableau q T hk hkn hadm
      rw [← hT'] at key
      have hbd := two_le_natAbs_axialDist T hkI hk1I hadm
      rcases le_or_gt (axialDist T k) (-2) with hneg | hpos
      · have g1 : gfac q (axialDist T k) = offDiag q (axialDist T k) := if_pos hneg
        have g2 : gfac q (-axialDist T k) = 1 := if_neg (by omega)
        have o2 : offDiag q (-axialDist T k) = 1 := offDiag_of_not_neg q (by omega)
        rw [g1, g2, mul_one] at key
        rw [o2, key, one_mul]
      · have hpos' : 2 ≤ axialDist T k := by omega
        have g1 : gfac q (axialDist T k) = 1 := if_neg (by omega)
        have g2 : gfac q (-axialDist T k) = offDiag q (-axialDist T k) := if_pos (by omega)
        have o1 : offDiag q (axialDist T k) = 1 := offDiag_of_not_neg q (by omega)
        rw [g1, g2, mul_one] at key
        rw [o1, mul_one, key, mul_comm]
    · -- not the partner: both entries vanish
      have e1 : genMat q k hk hkn T' T = 0 := genMat_apply_of_ne q k hk hkn heq hadm hT'
      have e2 : genMat q k hk hkn T T' = 0 := by
        by_cases hadm' : SwapAdmissible T' k
        · refine genMat_apply_of_ne q k hk hkn (Ne.symm heq) hadm' ?_
          intro hTT
          apply hT'
          have := swapTableau_involutive T' hk hkn hadm'
          rw [← this]
          congr 1
          exact hTT.symm
        · exact genMat_of_not_admissible q k hk hkn (Ne.symm heq) hadm'
      rw [e1, e2]; ring
  · have e1 : genMat q k hk hkn T' T = 0 := genMat_of_not_admissible q k hk hkn heq hadm
    have e2 : genMat q k hk hkn T T' = 0 := by
      by_cases hadm' : SwapAdmissible T' k
      · refine genMat_apply_of_ne q k hk hkn (Ne.symm heq) hadm' ?_
        intro hTT
        exact hadm (hTT ▸ swapAdmissible_swapTableau T' hk hkn hadm')
      · exact genMat_of_not_admissible q k hk hkn (Ne.symm heq) hadm'
    rw [e1, e2]; ring

end Form

/-! ## 3. Positivity of `D` for `q > 1` -/

section Order

variable [LinearOrder K] [IsStrictOrderedRing K] (q : K) {μ : YoungDiagram}

/-- `1 + a(d)·a(−d) > 0` for `d ≤ −2` and `q > 1`. -/
theorem offDiag_pos (hq : 1 < q) {d : ℤ} (hd : d ≤ -2) : 0 < offDiag q d := by
  have hq0 : (0 : K) < q := by linarith
  obtain ⟨e, rfl⟩ : ∃ e : ℕ, d = -(e : ℤ) := ⟨(-d).toNat, by omega⟩
  have he : 2 ≤ e := by omega
  rw [offDiag, if_pos (by omega)]
  set x : K := q ^ e with hx
  have hx1 : q ^ 2 ≤ x := pow_le_pow_right₀ hq.le he
  have hq2 : q < q ^ 2 := by nlinarith
  have hxq : q < x := lt_of_lt_of_le hq2 hx1
  have hx0 : 0 < x := by positivity
  have hp1 : q ^ (-2 * -(e : ℤ)) = x ^ 2 := by
    rw [show (-2 : ℤ) * -(e : ℤ) = ((2 * e : ℕ) : ℤ) by push_cast; ring, zpow_natCast, hx,
      ← pow_mul, mul_comm]
  have hp2 : q ^ (-2 * -(-(e : ℤ))) = (x ^ 2)⁻¹ := by
    rw [show (-2 : ℤ) * -(-(e : ℤ)) = -((2 * e : ℕ) : ℤ) by push_cast; ring, zpow_neg,
      zpow_natCast, hx, ← pow_mul, mul_comm]
  rw [seminormalParam, seminormalParam, hp1, hp2]
  have hx21 : 1 < x ^ 2 := by nlinarith
  have hA : x ^ 2 - 1 > 0 := by linarith
  have hqi : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have hqi0 : 0 < q⁻¹ := inv_pos.mpr hq0
  have hxi : x⁻¹ < q⁻¹ := (inv_lt_inv₀ hx0 hq0).mpr hxq
  -- key: x - x⁻¹ > q - q⁻¹
  have hkey : x ^ 2 - 1 - (q - q⁻¹) * x > 0 := by
    have : x - x⁻¹ > q - q⁻¹ := by linarith
    have hxx : x * x⁻¹ = 1 := mul_inv_cancel₀ hx0.ne'
    nlinarith
  have hden1 : (1 : K) - x ^ 2 ≠ 0 := by linarith
  have hden2 : (1 : K) - (x ^ 2)⁻¹ ≠ 0 := by
    have : (x ^ 2)⁻¹ < 1 := inv_lt_one_of_one_lt₀ hx21
    linarith
  have hx2ne : x ^ 2 ≠ 0 := by positivity
  have hform : 1 + (q - q⁻¹) / (1 - x ^ 2) * ((q - q⁻¹) / (1 - (x ^ 2)⁻¹))
      = ((x ^ 2 - 1) ^ 2 - (q - q⁻¹) ^ 2 * x ^ 2) / (x ^ 2 - 1) ^ 2 := by
    field_simp
    ring
  rw [hform]
  apply div_pos _ (by positivity)
  have hpos2 : x ^ 2 - 1 + (q - q⁻¹) * x > 0 := by
    have : q - q⁻¹ > 0 := by linarith
    positivity
  nlinarith

theorem gfac_pos (hq : 1 < q) (d : ℤ) : 0 < gfac q d := by
  unfold gfac
  split_ifs with h
  · exact offDiag_pos q hq h
  · exact one_pos

theorem pairW_pos (hq : 1 < q) (T : StandardYoungTableau μ) : 0 < pairW q T := by
  unfold pairW
  refine Finset.prod_pos fun p _ => ?_
  unfold pairFac
  split_ifs
  · exact gfac_pos q hq _
  · exact one_pos

/-- Every Ocneanu weight at `z_D` is `≥ 0` for `q > 1`: positive with at most two rows, zero
otherwise. -/
theorem ocneanuWeight_conventionD_nonneg (hq : 1 < q) (ν : YoungDiagram) :
    0 ≤ ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) ν := by
  rcases Nat.eq_zero_or_pos (ν.rowLen 2) with h | h
  · exact (ocneanuWeight_conventionD_pos_of_two_rows q (by linarith) (ne_of_gt hq) ν h).le
  · rw [ocneanuWeight_conventionD_eq_zero_of_three_rows q (by positivity) ν h]

/-- `q > 1` is not a root of unity. -/
theorem notRootOfUnity_of_one_lt (hq : 1 < q) : GenericParameter.NotRootOfUnity q :=
  fun _m hm => (one_lt_pow₀ hq hm.ne').ne'

end Order

/-! ## 4. The intertwining `D·ρ(X†) = ρ(X)ᵀ·D` and the positivity of `wtrace(X·X†)` -/

section Rep

variable [LinearOrder K] [IsStrictOrderedRing K] (q : K) {μ : YoungDiagram}

open Matrix

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem diag_mul_genMat (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) :
    diagonal (pairW q) * genMat q k hk hkn = (genMat q k hk hkn)ᵀ * diagonal (pairW q) := by
  ext T' T
  rw [diagonal_mul, mul_diagonal, transpose_apply]
  exact pairW_mul_genMat q k hk hkn T' T

variable (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
  (hN : μ.cells.card = n + 1)

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **`D·ρ(X†) = ρ(X)ᵀ·D`** for every `X ∈ H_{n+1}(q)`. -/
theorem diag_mul_rep_dag (x : Hecke K q q⁻¹ n) :
    diagonal (pairW q) * seminormalRep q hq0 hq2 n hN (Hecke.dag K q q⁻¹ n x)
      = (seminormalRep q hq0 hq2 n hN x)ᵀ * diagonal (pairW (μ := μ) q) := by
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective K (HeckeRel K q q⁻¹ n) x
  induction y using FreeAlgebra.induction with
  | grade0 r =>
      have h : RingQuot.mkAlgHom K (HeckeRel K q q⁻¹ n) (algebraMap K _ r)
          = algebraMap K (Hecke K q q⁻¹ n) r := AlgHom.commutes _ r
      rw [h, Hecke.dag_algebraMap, AlgHom.commutes, Algebra.algebraMap_eq_smul_one,
        Matrix.mul_smul, Matrix.mul_one, transpose_smul, transpose_one, Matrix.smul_mul,
        Matrix.one_mul]
  | grade1 i =>
      have h : RingQuot.mkAlgHom K (HeckeRel K q q⁻¹ n) (FreeAlgebra.ι K i)
          = Hecke.σ K q q⁻¹ n i := rfl
      rw [h, Hecke.dag_σ, seminormalRep_σ]
      exact diag_mul_genMat q _ _ _
  | mul a b ha hb =>
      rw [map_mul, Hecke.dag_mul, map_mul, ← Matrix.mul_assoc, hb, Matrix.mul_assoc, ha,
        ← Matrix.mul_assoc, ← transpose_mul, ← map_mul, ← map_mul,
        map_mul (RingQuot.mkAlgHom K (HeckeRel K q q⁻¹ n))]
  | add a b ha hb =>
      rw [map_add, map_add, map_add, Matrix.mul_add, ha, hb, map_add, transpose_add,
        Matrix.add_mul]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- Entrywise form: `D_{T'}·ρ(X†)_{T' T} = ρ(X)_{T T'}·D_T`. -/
theorem pairW_mul_rep_dag_apply (x : Hecke K q q⁻¹ n) (T' T : StandardYoungTableau μ) :
    pairW q T' * seminormalRep q hq0 hq2 n hN (Hecke.dag K q q⁻¹ n x) T' T
      = seminormalRep q hq0 hq2 n hN x T T' * pairW q T := by
  have h := congrFun (congrFun (diag_mul_rep_dag q hq0 hq2 n hN x) T') T
  rwa [diagonal_mul, mul_diagonal, transpose_apply] at h

/-- `tr ρ(X†) = tr ρ(X)`. -/
theorem trace_rep_dag (hq : 1 < q) (x : Hecke K q q⁻¹ n) :
    (seminormalRep q hq0 hq2 n hN (Hecke.dag K q q⁻¹ n x)).trace
      = (seminormalRep q hq0 hq2 n hN x).trace := by
  unfold Matrix.trace
  refine Finset.sum_congr rfl fun T _ => ?_
  have h := pairW_mul_rep_dag_apply q hq0 hq2 n hN x T T
  have hp := (pairW_pos q hq T).ne'
  simp only [Matrix.diag_apply]
  rw [mul_comm (seminormalRep q hq0 hq2 n hN x T T)] at h
  exact mul_left_cancel₀ hp h

/-- `0 ≤ tr(ρ(X)·ρ(X†))`. -/
theorem trace_rep_mul_dag_nonneg (hq : 1 < q) (x : Hecke K q q⁻¹ n) :
    0 ≤ (seminormalRep q hq0 hq2 n hN x
      * seminormalRep q hq0 hq2 n hN (Hecke.dag K q q⁻¹ n x)).trace := by
  unfold Matrix.trace
  refine Finset.sum_nonneg fun T _ => ?_
  simp only [Matrix.diag_apply, Matrix.mul_apply]
  refine Finset.sum_nonneg fun T' _ => ?_
  have h := pairW_mul_rep_dag_apply q hq0 hq2 n hN x T' T
  have hp' := pairW_pos q hq T'
  have hp := pairW_pos q hq T
  set A := seminormalRep q hq0 hq2 n hN x T T'
  set B := seminormalRep q hq0 hq2 n hN (Hecke.dag K q q⁻¹ n x) T' T
  have : 0 ≤ A * B * pairW q T' := by
    rw [mul_assoc, mul_comm B, h, ← mul_assoc]
    exact mul_nonneg (mul_self_nonneg A) hp.le
  exact (mul_nonneg_iff_of_pos_right hp').mp this

end Rep

/-! ## 5. The Markov trace at `z_D` -/

section Wtrace

variable [LinearOrder K] [IsStrictOrderedRing K] (q : K)

/-- **`wtrace(X†) = wtrace(X)`.** -/
theorem wtrace_dag (hq : 1 < q) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke K q q⁻¹ n) :
    wtrace q hq0 hq2 n (Hecke.dag K q q⁻¹ n x) = wtrace q hq0 hq2 n x := by
  rw [wtrace_apply, wtrace_apply]
  refine Finset.sum_congr rfl fun ν _ => ?_
  rw [trace_rep_dag q hq0 hq2 n ν.2 hq]

/-- **Positivity of the twisted form at `z_D`: `0 ≤ wtrace(X · X†)` for `q > 1`.** -/
theorem wtrace_mul_dag_nonneg (hq : 1 < q) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)
    (x : Hecke K q q⁻¹ n) :
    0 ≤ wtrace q hq0 hq2 n (x * Hecke.dag K q q⁻¹ n x) := by
  rw [wtrace_apply]
  refine Finset.sum_nonneg fun ν _ => ?_
  rw [map_mul]
  exact mul_nonneg (ocneanuWeight_conventionD_nonneg q hq ν.1)
    (trace_rep_mul_dag_nonneg q hq0 hq2 n ν.2 hq x)

end Wtrace

end SeminormalRep

end QOU.SchurWeyl
