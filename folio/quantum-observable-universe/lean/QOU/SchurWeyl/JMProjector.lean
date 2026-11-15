import QOU.SchurWeyl.HeckeWedderburnGeneral
import QOU.SchurWeyl.QJucysMurphyEigen
import QOU.SchurWeyl.SytContentTuple

/-!
# QOU.SchurWeyl.JMProjector — the Wedderburn matrix units as explicit polynomials in `σ`

Gap 2 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md` §5.1 (bean `qou-2vt5`):
`heckeWedderburn q : H_{n+1}(q) ≃ₐ ∏_λ M_{f^λ}` is built at each `q` by
`AlgEquiv.ofBijective`, so nothing said how its inverse depends on `q`. This file computes the
inverse on the diagonal matrix units **in closed form**:

    (heckeWedderburn q)⁻¹ (E^λ_{TT})  =  ∏_{k=0}^{n} ∏_{d ≠ c_k(T), |d| ≤ n}
                                           (Y_k − [d]_{q²}) / ([c_k(T)]_{q²} − [d]_{q²})

(`heckeWedderburn_symm_single`), where

* `Y_k = jmAddIn q σ k` is the **additive** Jucys–Murphy element, `Y_0 = 0`,
  `Y_{k+1} = σ_k Y_k σ_k + q⁻¹ σ_k`. It satisfies `(q² − 1)·Y_k = L_k − 1` against the
  multiplicative Murphy element (`sq_sub_one_smul_jmAdd`), but its recursion has no `q² − 1` in a
  denominator, so it makes sense at `q = 1` (where it is the classical `Y_k = Σ_{j<k} (j k)`);
* `[c]_{q²}` is the signed `q²`-integer (`qInt2`), `(q²−1)[c]_{q²} = q^{2c} − 1`, `[c]_1 = c`;
* `c_k(T)` is the content of the cell of `T` holding `k + 1` (`contentVec`).

The proof: the seminormal representation sends `Y_k` to `diag([c_k(S)]_{q²})`
(`seminormalRep_jmAdd`, from Ram's `L_k ↦ diag(q^{2c_k})`), so the Lagrange product is the
indicator of `S`'s content vector equal to `T`'s (`seminormalRep_jmProj`, `projVal_*`); the content
vector determines both the shape (`shape_eq_of_contentVec_eq`) and the tableau
(`eq_of_contentVec_eq`).

**Why this closes gap 2 and the algebraic half of gap 3.** The right-hand side is a fixed
non-commutative polynomial in the `σ_i` whose coefficients are rational functions of `q` with
denominators `q` and `[c]_{q²} − [d]_{q²}` (`|c|, |d| ≤ n`). Those are **nonzero at `q = 1`**
(they are `c − d`) and at every positive real `q`. So for any representation `ρ` of `H_{n+1}(q)`,
`ρ((heckeWedderburn q)⁻¹ E_{TT})` is the same polynomial in the matrices `ρ(σ_i)`
(`map_jmProjIn`), and is continuous wherever the `ρ(σ_i)` are — up to and including `q = 1`,
where `heckeWedderburn` itself is not defined. See `QOU.SchurWeyl.JMProjectorContinuity`.

Base ring (§7c): generic `[Field K]` (`[CharZero K]` where `heckeWedderburn` is used).

Refs: the JM-Lagrange form of the seminormal idempotents is classical — [murphy1981] (`q = 1`),
[ram1997] §4 (Hecke). Everything here is proved from the corpus' seminormal representation.
-/

namespace QOU.SchurWeyl

namespace JMProjector

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep Hecke

/-! ## Signed `q²`-integers -/

section QInt

variable {K : Type*} [Field K]

/-- The signed `q²`-integer `[c]_{q²}`: `1 + q² + ⋯ + q^{2(c−1)}` for `c ≥ 0`, and
`−(q^{−2} + ⋯ + q^{2c})` for `c < 0`. It is the unique Laurent polynomial with
`(q² − 1)·[c]_{q²} = q^{2c} − 1`, and `[c]_1 = c`. -/
noncomputable def qInt2 (q : K) (c : ℤ) : K :=
  if 0 ≤ c then ∑ j ∈ Finset.range c.toNat, q ^ (2 * j)
  else -∑ j ∈ Finset.range (-c).toNat, (q ^ 2)⁻¹ ^ (j + 1)

theorem sq_sub_one_mul_qInt2 (q : K) (hq0 : q ≠ 0) (c : ℤ) :
    (q ^ 2 - 1) * qInt2 q c = q ^ (2 * c) - 1 := by
  unfold qInt2
  split_ifs with hc
  · obtain ⟨m, rfl⟩ : ∃ m : ℕ, c = m := ⟨c.toNat, (Int.toNat_of_nonneg hc).symm⟩
    simp only [Int.toNat_natCast]
    have h := geom_sum_mul (q ^ 2) m
    simp only [← pow_mul] at h
    rw [mul_comm, h, show (2 : ℤ) * (m : ℤ) = ((2 * m : ℕ) : ℤ) by push_cast; ring, zpow_natCast]
  · obtain ⟨m, hm⟩ : ∃ m : ℕ, c = -(m : ℤ) := ⟨(-c).toNat, by omega⟩
    subst hm
    simp only [neg_neg, Int.toNat_natCast]
    set r : K := (q ^ 2)⁻¹ with hr
    have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq0
    have hshift : ∑ j ∈ Finset.range m, r ^ (j + 1) = r * ∑ j ∈ Finset.range m, r ^ j := by
      rw [Finset.mul_sum]; exact Finset.sum_congr rfl (fun j _ => by ring)
    have hqr : (q ^ 2 - 1) * r = 1 - r := by rw [hr]; field_simp
    have hz : q ^ (2 * -(m : ℤ)) = r ^ m := by
      rw [hr, inv_pow, ← pow_mul, show (2 : ℤ) * -(m : ℤ) = -((2 * m : ℕ) : ℤ) by push_cast; ring,
        zpow_neg, zpow_natCast]
    rw [hz, hshift, mul_neg, ← mul_assoc, hqr]
    have h := geom_sum_mul r m
    linear_combination h

@[simp] theorem qInt2_one (c : ℤ) : qInt2 (1 : K) c = c := by
  unfold qInt2
  split_ifs with hc
  · simp only [one_pow, Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
    rw [← Int.cast_natCast, Int.toNat_of_nonneg hc]
  · simp only [one_pow, inv_one, Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
    rw [← Int.cast_natCast, Int.toNat_of_nonneg (by omega), Int.cast_neg, neg_neg]

/-- At a parameter that is not a root of unity, `c ↦ [c]_{q²}` is injective. -/
theorem qInt2_injective (q : K) (hq0 : q ≠ 0) (hq : GenericParameter.NotRootOfUnity q) :
    Function.Injective (qInt2 q) := by
  intro a b hab
  have hq2 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr (GenericParameter.sq_ne_one hq)
  have h := congrArg (fun x => (q ^ 2 - 1) * x) hab
  simp only [sq_sub_one_mul_qInt2 q hq0, sub_left_inj] at h
  by_contra hne
  have hz : q ^ (2 * a - 2 * b) = 1 := by
    rw [zpow_sub₀ hq0, h, div_self (zpow_ne_zero _ hq0)]
  exact GenericParameter.zpow_ne_one hq (by omega) hz

/-- At `q = 1` the `q²`-integers are the integers, so again injective. -/
theorem qInt2_one_injective [CharZero K] : Function.Injective (qInt2 (1 : K) : ℤ → K) := by
  intro a b h
  simpa using h

end QInt

/-! ## The additive Jucys–Murphy elements, regular at `q = 1` -/

section JM

variable {K : Type*} [Field K] (q : K) {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- The **additive Jucys–Murphy elements** in any `K`-algebra `A` carrying `n` "generators" `g`:
`Y_0 = 0`, `Y_{k+1} = g_k Y_k g_k + q⁻¹ g_k`. With `g = σ` in `H_{n+1}(q)` this is
`(L_k − 1)/(q² − 1)` (`sq_sub_one_smul_jmAdd`), but the recursion itself has no denominator
`q² − 1`, so it is defined — and polynomial in the `g_i` with coefficients in `ℤ[q⁻¹]` — at every
`q ≠ 0`, including `q = 1`, where it is the classical `Y_{k+1} = s_k Y_k s_k + s_k`. -/
noncomputable def jmAddIn (g : Fin n → A) : ℕ → A
  | 0 => 0
  | k + 1 => if h : k < n then g ⟨k, h⟩ * jmAddIn g k * g ⟨k, h⟩ + q⁻¹ • g ⟨k, h⟩
      else jmAddIn g k

theorem jmAddIn_succ (g : Fin n → A) {k : ℕ} (hk : k < n) :
    jmAddIn q g (k + 1) = g ⟨k, hk⟩ * jmAddIn q g k * g ⟨k, hk⟩ + q⁻¹ • g ⟨k, hk⟩ := by
  rw [jmAddIn, dif_pos hk]

theorem jmAddIn_succ_of_le (g : Fin n → A) {k : ℕ} (hk : n ≤ k) :
    jmAddIn q g (k + 1) = jmAddIn q g k := by
  rw [jmAddIn, dif_neg (by omega)]

/-- Algebra maps commute with the recursion. -/
theorem map_jmAddIn {B : Type*} [Ring B] [Algebra K B] (φ : A →ₐ[K] B) (g : Fin n → A) :
    ∀ k, φ (jmAddIn q g k) = jmAddIn q (fun i => φ (g i)) k
  | 0 => by simp [jmAddIn]
  | k + 1 => by
      by_cases hk : k < n
      · rw [jmAddIn_succ q g hk, jmAddIn_succ q _ hk, map_add, map_mul, map_mul, map_smul,
          map_jmAddIn φ g k]
      · rw [jmAddIn_succ_of_le q g (by omega), jmAddIn_succ_of_le q _ (by omega),
          map_jmAddIn φ g k]

/-- The additive JM elements of the Hecke algebra itself. -/
noncomputable abbrev jmAdd (n : ℕ) (k : ℕ) : Hecke K q q⁻¹ n :=
  jmAddIn q (σ K q q⁻¹ n) k

/-- **`(q² − 1)·Y_k = L_k − 1`** in `H_{n+1}(q)`, for every `q ≠ 0`. -/
theorem sq_sub_one_smul_jmAdd (hq0 : q ≠ 0) (n : ℕ) :
    ∀ k, (q ^ 2 - 1) • jmAdd q n k = qJM K q q⁻¹ n k - 1
  | 0 => by simp [jmAdd, jmAddIn, qJM_zero]
  | k + 1 => by
      by_cases hk : k < n
      · have ih := sq_sub_one_smul_jmAdd hq0 n k
        have hquad := σ_quadratic_qou K q q⁻¹ n (mul_inv_cancel₀ hq0) ⟨k, hk⟩
        set s := σ K q q⁻¹ n ⟨k, hk⟩
        rw [jmAdd, jmAddIn_succ q _ hk, qJM_succ K q q⁻¹ n hk, smul_add, smul_smul]
        rw [show (q ^ 2 - 1) • (s * jmAddIn q (σ K q q⁻¹ n) k * s)
            = s * ((q ^ 2 - 1) • jmAdd q n k) * s by
          rw [mul_smul_comm, smul_mul_assoc]]
        rw [ih]
        have hc : (q ^ 2 - 1) * q⁻¹ = q - q⁻¹ := by field_simp
        rw [hc, mul_sub, sub_mul, mul_one, hquad]
        abel
      · have ih := sq_sub_one_smul_jmAdd hq0 n k
        rw [jmAdd, jmAddIn_succ_of_le q _ (by omega), ← jmAdd, ih]
        simp only [qJM, dif_neg hk]

end JM

/-! ## The JM projector -/

section Proj

variable {K : Type*} [Field K] (q : K) {A : Type*} [Ring A] [Algebra K A] {n : ℕ}

/-- The integers `−n, …, n`, as a list. -/
def contentRange (n : ℕ) : List ℤ := (List.range (2 * n + 1)).map (fun j : ℕ => (j : ℤ) - n)

theorem mem_contentRange {n : ℕ} {d : ℤ} : d ∈ contentRange n ↔ -(n : ℤ) ≤ d ∧ d ≤ n := by
  simp only [contentRange, List.mem_map, List.mem_range]
  constructor
  · rintro ⟨j, hj, rfl⟩; omega
  · intro h; exact ⟨(d + n).toNat, by omega, by omega⟩

/-- The `k`-th Lagrange factor `∏_{d ≠ c, |d| ≤ n} (Y_k − [d])/([c] − [d])`. -/
noncomputable def jmFactorIn (g : Fin n → A) (k : ℕ) (c : ℤ) : A :=
  (((contentRange n).filter (fun d => d ≠ c)).map
    (fun d => (qInt2 q c - qInt2 q d)⁻¹ • (jmAddIn q g k - algebraMap K A (qInt2 q d)))).prod

/-- The **JM projector** attached to a content vector `c`: `∏_{k ≤ n} jmFactorIn k (c k)`. -/
noncomputable def jmProjIn (g : Fin n → A) (c : ℕ → ℤ) : A :=
  ((List.range (n + 1)).map (fun k => jmFactorIn q g k (c k))).prod

theorem map_jmProjIn {B : Type*} [Ring B] [Algebra K B] (φ : A →ₐ[K] B) (g : Fin n → A)
    (c : ℕ → ℤ) : φ (jmProjIn q g c) = jmProjIn q (fun i => φ (g i)) c := by
  simp only [jmProjIn, jmFactorIn, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun k _ => ?_)
  simp only [Function.comp_apply, map_list_prod, List.map_map]
  congr 1
  refine List.map_congr_left (fun d _ => ?_)
  simp only [Function.comp_apply, map_smul, map_sub, AlgHom.commutes, map_jmAddIn]

end Proj

/-! ## Diagonal evaluation -/

section Diag

variable {K : Type*} [Field K] {m : Type*} [Fintype m] [DecidableEq m]

theorem list_prod_diagonal {α : Type*} (l : List α) (F : α → m → K) :
    (l.map fun x => Matrix.diagonal (F x)).prod
      = Matrix.diagonal (fun T => (l.map fun x => F x T).prod) := by
  induction l with
  | nil => simp [Matrix.diagonal_one]
  | cons a l ih =>
      rw [List.map_cons, List.prod_cons, ih, Matrix.diagonal_mul_diagonal]
      simp

end Diag

/-! ## Contents of a diagram with `n + 1` cells lie in `[−n, n]` -/

theorem cellContent_bound {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    {c : ℕ × ℕ} (hc : c ∈ μ.cells) : -(n : ℤ) ≤ cellContent c ∧ cellContent c ≤ n := by
  classical
  obtain ⟨i, j⟩ := c
  have hmem : (i, j) ∈ μ := by simpa using hc
  have hj : j + 1 ≤ n + 1 := by
    rw [← hN]
    have hsub : (Finset.range (j + 1)).image (fun t => (0, t)) ⊆ μ.cells := by
      intro x hx
      obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hx
      have := μ.up_left_mem (Nat.zero_le i) (Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)) hmem
      simpa using this
    have := Finset.card_le_card hsub
    rwa [Finset.card_image_of_injective _ (fun a b h => by simpa using h),
      Finset.card_range] at this
  have hi : i + 1 ≤ n + 1 := by
    rw [← hN]
    have hsub : (Finset.range (i + 1)).image (fun t => (t, 0)) ⊆ μ.cells := by
      intro x hx
      obtain ⟨t, ht, rfl⟩ := Finset.mem_image.mp hx
      have := μ.up_left_mem (Nat.lt_succ_iff.mp (Finset.mem_range.mp ht)) (Nat.zero_le j) hmem
      simpa using this
    have := Finset.card_le_card hsub
    rwa [Finset.card_image_of_injective _ (fun a b h => by simpa using h),
      Finset.card_range] at this
  simp only [cellContent]
  omega

/-- The content vector `k ↦ c(T(k+1))` of a standard tableau. -/
noncomputable def contentVec {μ : YoungDiagram} (T : StandardYoungTableau μ) (k : ℕ) : ℤ :=
  cellContent (cellOf T (k + 1))

theorem contentVec_mem {μ : YoungDiagram} {n : ℕ} (hN : μ.cells.card = n + 1)
    (T : StandardYoungTableau μ) {k : ℕ} (hk : k ∈ Finset.range (n + 1)) :
    contentVec T k ∈ contentRange n := by
  rw [Finset.mem_range] at hk
  rw [mem_contentRange]
  exact cellContent_bound hN (cellOf_mem T (Set.mem_Icc.mpr ⟨by omega, by omega⟩))

/-! ## The seminormal representation sends `Y_k` and the projector to diagonal matrices -/

section Seminormal

variable {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q)

theorem seminormalRep_jmAdd {μ : YoungDiagram} (n : ℕ) (hN : μ.cells.card = n + 1) (k : ℕ)
    (hk : k ≤ n) :
    seminormalRep q hq0 hq2 n hN (jmAdd q n k)
      = Matrix.diagonal (fun T => qInt2 q (contentVec T k)) := by
  have hsq : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr (GenericParameter.sq_ne_one hq2)
  apply smul_right_injective _ hsq
  simp only
  rw [← map_smul, sq_sub_one_smul_jmAdd q hq0 n k, map_sub, map_one,
    seminormalRep_qJM q hq0 hq2 n hN k hk]
  ext T U
  by_cases h : T = U
  · subst h
    simp [jmDiagVal, contentVec, sq_sub_one_mul_qInt2 q hq0]
  · simp [jmDiagVal, Matrix.diagonal_apply_ne _ h, Matrix.one_apply_ne h]

/-- The scalar the projector takes on the seminormal vector `S`. -/
noncomputable def projVal (n : ℕ) (c e : ℕ → ℤ) : K :=
  ((List.range (n + 1)).map (fun k =>
    (((contentRange n).filter (fun d => d ≠ c k)).map
      (fun d => (qInt2 q (c k) - qInt2 q d)⁻¹ * (qInt2 q (e k) - qInt2 q d))).prod)).prod

theorem seminormalRep_jmProj {μ : YoungDiagram} (n : ℕ) (hN : μ.cells.card = n + 1)
    (c : ℕ → ℤ) :
    seminormalRep q hq0 hq2 n hN (jmProjIn q (σ K q q⁻¹ n) c)
      = Matrix.diagonal (fun S => projVal q n c (contentVec S)) := by
  rw [map_jmProjIn]
  simp only [jmProjIn, jmFactorIn]
  have hY : ∀ k ∈ List.range (n + 1), ∀ d : ℤ,
      (qInt2 q (c k) - qInt2 q d)⁻¹ •
        (jmAddIn q (fun i => seminormalRep q hq0 hq2 n hN (σ K q q⁻¹ n i)) k
          - algebraMap K _ (qInt2 q d))
      = Matrix.diagonal (fun S => (qInt2 q (c k) - qInt2 q d)⁻¹ *
          (qInt2 q (contentVec S k) - qInt2 q d)) := by
    intro k hk d
    rw [List.mem_range] at hk
    rw [← map_jmAddIn, ← jmAdd, seminormalRep_jmAdd q hq0 hq2 n hN k (by omega)]
    ext S U
    by_cases h : S = U
    · subst h; simp [Matrix.algebraMap_eq_diagonal]
    · simp [Matrix.algebraMap_eq_diagonal, Matrix.diagonal_apply_ne _ h]
  rw [List.map_congr_left (fun k hk => by
    rw [List.map_congr_left (fun d _ => hY k hk d), list_prod_diagonal])]
  rw [list_prod_diagonal]
  rfl

omit hq0 hq2 in
theorem projVal_self (n : ℕ) (hinj : Set.InjOn (qInt2 q) {d | d ∈ contentRange n})
    (c : ℕ → ℤ) (hc : ∀ k ∈ Finset.range (n + 1), c k ∈ contentRange n) :
    projVal q n c c = 1 := by
  unfold projVal
  refine List.prod_eq_one (fun x hx => ?_)
  obtain ⟨k, hk, rfl⟩ := List.mem_map.mp hx
  refine List.prod_eq_one (fun y hy => ?_)
  obtain ⟨d, hd, rfl⟩ := List.mem_map.mp hy
  rw [List.mem_filter] at hd
  have hdc : d ≠ c k := by simpa using hd.2
  have hne : qInt2 q (c k) - qInt2 q d ≠ 0 := by
    refine sub_ne_zero.mpr (fun h => hdc (hinj ?_ hd.1 h).symm)
    exact hc k (by simpa [Finset.mem_range, List.mem_range] using hk)
  exact inv_mul_cancel₀ hne

omit hq0 hq2 in
theorem projVal_eq_zero (n : ℕ) (c e : ℕ → ℤ)
    (he : ∀ k ∈ Finset.range (n + 1), e k ∈ contentRange n)
    {k : ℕ} (hk : k ∈ Finset.range (n + 1)) (hne : e k ≠ c k) :
    projVal q n c e = 0 := by
  unfold projVal
  refine List.prod_eq_zero (List.mem_map.mpr ⟨k, by simpa using hk, ?_⟩)
  refine List.prod_eq_zero (List.mem_map.mpr ⟨e k, ?_, by simp⟩)
  rw [List.mem_filter]
  exact ⟨he k hk, by simpa using hne⟩

end Seminormal

/-! ## The content vector determines the shape and the tableau -/

theorem shape_eq_of_contentVec_eq {μ ν : YoungDiagram} {n : ℕ} (hμ : μ.cells.card = n + 1)
    (hν : ν.cells.card = n + 1) (S : StandardYoungTableau μ) (T : StandardYoungTableau ν)
    (h : ∀ k ∈ Finset.range (n + 1), contentVec S k = contentVec T k) : μ = ν := by
  classical
  refine youngDiagram_eq_of_contentCount_eq (fun d => ?_)
  have hS := sum_cellOf_range S hμ (fun c => if cellContent c = d then (1 : ℕ) else 0)
  have hT := sum_cellOf_range T hν (fun c => if cellContent c = d then (1 : ℕ) else 0)
  have hST : ∑ k ∈ Finset.range (n + 1), (if cellContent (cellOf S (k + 1)) = d then 1 else 0)
      = ∑ k ∈ Finset.range (n + 1), (if cellContent (cellOf T (k + 1)) = d then 1 else 0) :=
    Finset.sum_congr rfl (fun k hk => by
      have := h k hk
      simp only [contentVec] at this
      rw [this])
  have e1 : (diagOf μ d).card = ∑ c ∈ μ.cells, (if cellContent c = d then (1 : ℕ) else 0) := by
    simp only [diagOf, Finset.card_filter]
  have e2 : (diagOf ν d).card = ∑ c ∈ ν.cells, (if cellContent c = d then (1 : ℕ) else 0) := by
    simp only [diagOf, Finset.card_filter]
  rw [e1, e2, ← hS, ← hT, hST]

theorem eq_of_contentVec_eq {μ : YoungDiagram} {n : ℕ} (hμ : μ.cells.card = n + 1)
    (S T : StandardYoungTableau μ)
    (h : ∀ k ∈ Finset.range (n + 1), contentVec S k = contentVec T k) : S = T := by
  refine syt_eq_of_cellContent_eq S T (fun k hk1 hkn => ?_)
  obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
  exact h j (Finset.mem_range.mpr (by omega))

/-! ## The projector is the Wedderburn matrix unit -/

section Wedderburn

variable {K : Type*} [Field K] [CharZero K] (q : K) (hq0 : q ≠ 0)
  (hq2 : GenericParameter.NotRootOfUnity q)

/-- **The seminormal product sends the JM projector of `T` to the matrix unit `E^λ_{TT}`.** -/
theorem heckeProduct_jmProj (n : ℕ) (lam : Nat.Partition (n + 1))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    heckeProduct q hq0 hq2 n (jmProjIn q (σ K q q⁻¹ n) (contentVec T))
      = Pi.single lam (Matrix.single T T 1) := by
  classical
  have hinj : Set.InjOn (qInt2 q) {d | d ∈ contentRange n} :=
    (qInt2_injective q hq0 hq2).injOn
  funext mu
  rw [heckeProduct_apply, seminormalRep_jmProj]
  ext S U
  by_cases hmu : mu = lam
  · subst hmu
    rw [Pi.single_eq_same]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      by_cases hST : S = T
      · subst hST
        rw [projVal_self q n hinj _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)]
        exact (Matrix.single_apply_same _ _ _).symm
      · have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
          by_contra hcon
          push_neg at hcon
          exact hST (eq_of_contentVec_eq (partitionShape_card_succ mu) S T hcon)
        obtain ⟨k, hk, hne⟩ := this
        rw [projVal_eq_zero q n _ _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)
          hk hne]
        exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hST h.1.symm)).symm
    · rw [Matrix.diagonal_apply_ne _ hSU]
      exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hSU (h.1.symm.trans h.2))).symm
  · rw [Pi.single_eq_of_ne hmu]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
        by_contra hcon
        push_neg at hcon
        exact hmu (QOU.Mathlib.partitionShape_injective
          (shape_eq_of_contentVec_eq (partitionShape_card_succ mu) (partitionShape_card_succ lam)
            S T hcon))
      obtain ⟨k, hk, hne⟩ := this
      rw [projVal_eq_zero q n _ _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)
        hk hne]
      rfl
    · rw [Matrix.diagonal_apply_ne _ hSU]
      rfl

/-- **The inverse Wedderburn map on a matrix unit is an explicit polynomial in the `σ_i`.**
`(heckeWedderburn q)⁻¹ (E^λ_{TT}) = jmProjIn q σ (contentVec T)`, whose coefficients are rational
functions of `q` with denominators the differences `[c]_{q²} − [d]_{q²}`, `|c|, |d| ≤ n`. -/
theorem heckeWedderburn_symm_single (n : ℕ) (lam : Nat.Partition (n + 1))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    (heckeWedderburn q hq0 hq2 n).symm (Pi.single lam (Matrix.single T T 1))
      = jmProjIn q (σ K q q⁻¹ n) (contentVec T) := by
  rw [AlgEquiv.symm_apply_eq]
  exact (heckeProduct_jmProj q hq0 hq2 n lam T).symm

end Wedderburn

end JMProjector

end QOU.SchurWeyl
