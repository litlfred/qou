/-
  **The bounded-order generalized Wronskian criterion** — the form Roth's lemma actually
  consumes — proved here at `m = 2`.

  Bean `qou-sq3h`.  ⚠ Staged for Mathlib; depends only on other staged files, never on QOU
  content.

  ═══ WHY BOUNDED ORDER ═══

  `QOU.Mathlib.MvGenWronskian` proves that an independent family has *some* non-zero
  generalized Wronskian, with no bound on the order of the operators, and the witnesses
  there (`mvGenWronskian_pow_five_six`) show that proof cannot be sharpened.  Roth's lemma
  needs `ord (Δᵢ) ≤ i`: the order bound is what ties the Wronskian's degree to the degrees of
  the auxiliary polynomial, and without it the index estimate has nothing to bound.

  At `m = 2` the bound is `(0, 1)`, so the family is `(id, ∂ₖ)` and the criterion reads

      f, g independent over K  ⟹  ∃ k,  f ∂ₖg − g ∂ₖf ≠ 0

  which is `exists_bounded_order_mvGenWronskian_two` below, stated in the committed
  `mvGenWronskian` shape.

  ═══ THE PROOF, AND WHY IT MIRRORS THE UNIVARIATE ONE ═══

  Divide out the gcd (`MvPolynomial σ K` is a UFD for **any** `σ`); coprimality turns the
  identity `p ∂ₖq = q ∂ₖp` into `p ∣ ∂ₖp`; the total degree forbids that unless `∂ₖp = 0`;
  and a polynomial killed by every partial is constant in characteristic zero.

  This is the same shape as `Polynomial.exists_dependence_of_wronskian_eq_zero` in
  `QOU.Mathlib.GenWronskian` — the univariate `m = 2` converse — with `degreeOf`/`natDegree`
  replaced by `totalDegree` and Bézout coprimality replaced by `IsRelPrime`.

  ⚠ `IsCoprime` is the wrong notion here.  It is Bézout-flavoured and is **false** for `x, y`
  in `MvPolynomial` even though they share no non-unit factor, so the argument must go
  through `UniqueFactorizationMonoid` / `IsRelPrime`.
-/
import QOU.Mathlib.MvGenWronskian
import Mathlib.RingTheory.MvPolynomial.MonomialOrder.DegLex
import Mathlib.RingTheory.Polynomial.UniqueFactorization

namespace MvPolynomial

variable {σ R : Type*} [CommRing R]

theorem sum_add_single_one (t : σ →₀ ℕ) (k : σ) :
    (t + Finsupp.single k 1).sum (fun _ e => e) = t.sum (fun _ e => e) + 1 := by
  rw [Finsupp.sum_add_index' (fun _ => rfl) (fun _ _ _ => rfl)]
  congr 1
  exact Finsupp.sum_single_index rfl

/-- **Differentiating strictly drops the total degree.**

Mathlib has the univariate `Polynomial.natDegree_derivative_lt`; this is the multivariate
statement.  Companion to `degreeOf_pderiv_lt` in `QOU.Mathlib.MvGenWronskian`; the total
degree is the one that pairs with `totalDegree_mul_of_isDomain`, which is why both exist. -/
theorem totalDegree_pderiv_lt [DecidableEq σ] {k : σ} {p : MvPolynomial σ R}
    (hp : pderiv k p ≠ 0) : totalDegree (pderiv k p) < totalDegree p := by
  have hstep : ∀ t ∈ (pderiv k p).support, (t.sum fun _ e => e) + 1 ≤ totalDegree p := by
    intro t ht
    rw [mem_support_iff, coeff_pderiv] at ht
    have hne : coeff (t + Finsupp.single k 1) p ≠ 0 := fun h => ht (by rw [h, mul_zero])
    have hle := le_totalDegree (mem_support_iff.mpr hne)
    rwa [sum_add_single_one] at hle
  obtain ⟨t, ht⟩ := support_nonempty.mpr hp
  have hpos : 0 < totalDegree p := lt_of_lt_of_le (Nat.succ_pos _) (hstep t ht)
  rw [totalDegree, Finset.sup_lt_iff hpos]
  intro b hb
  exact Nat.lt_of_succ_le (hstep b hb)

open UniqueFactorizationMonoid in
/-- **If every first-order directional Wronskian vanishes, the pair is proportional over the
constants.** -/
theorem exists_const_dependence_of_forall_wronskian_eq_zero
    {K : Type*} [Field K] [CharZero K] [DecidableEq σ] {f g : MvPolynomial σ K}
    (h : ∀ k : σ, f * pderiv k g - g * pderiv k f = 0) :
    ∃ lam mu : K, (lam ≠ 0 ∨ mu ≠ 0) ∧ C lam * f + C mu * g = 0 := by
  classical
  by_cases hf : f = 0
  · exact ⟨1, 0, Or.inl one_ne_zero, by simp [hf]⟩
  by_cases hg : g = 0
  · exact ⟨0, 1, Or.inr one_ne_zero, by simp [hg]⟩
  obtain ⟨p, q, d, hrel, hdp, hdq⟩ := exists_reduced_factors f hf g
  have hd : d ≠ 0 := by rintro rfl; rw [zero_mul] at hdp; exact hf hdp.symm
  have hp : p ≠ 0 := by rintro rfl; rw [mul_zero] at hdp; exact hf hdp.symm
  have hq : q ≠ 0 := by rintro rfl; rw [mul_zero] at hdq; exact hg hdq.symm
  -- the common factor cancels as `d²`, leaving the reduced pair
  have hpq : ∀ k : σ, p * pderiv k q = q * pderiv k p := by
    intro k
    have hk := h k
    rw [← hdp, ← hdq] at hk
    simp only [Derivation.leibniz, smul_eq_mul] at hk
    have hd2 : d ^ 2 ≠ 0 := pow_ne_zero 2 hd
    have hzero : d ^ 2 * (p * pderiv k q - q * pderiv k p) = 0 := by linear_combination hk
    exact sub_eq_zero.mp ((mul_eq_zero.mp hzero).resolve_left hd2)
  -- coprimality turns the identity into a self-divisibility, which the degree forbids
  have hkill : ∀ (u v : MvPolynomial σ K), u ≠ 0 → IsRelPrime u v →
      (∀ k : σ, u * pderiv k v = v * pderiv k u) → ∀ k : σ, pderiv k u = 0 := by
    intro u v hu hrel' huv k
    by_contra hne
    obtain ⟨s, hs⟩ := hrel'.dvd_of_dvd_mul_left ⟨pderiv k v, (huv k).symm⟩
    have hsne : s ≠ 0 := by rintro rfl; rw [mul_zero] at hs; exact hne hs
    have hdeg : totalDegree (pderiv k u) = totalDegree u + totalDegree s := by
      rw [hs]; exact totalDegree_mul_of_isDomain hu hsne
    have hlt := totalDegree_pderiv_lt hne
    omega
  obtain ⟨a0, hpc⟩ : ∃ a0 : K, p = C a0 :=
    ⟨coeff 0 p, eq_C_of_pderiv_eq_zero (hkill p q hp hrel hpq)⟩
  obtain ⟨b0, hqc⟩ : ∃ b0 : K, q = C b0 :=
    ⟨coeff 0 q, eq_C_of_pderiv_eq_zero (hkill q p hq hrel.symm (fun k => (hpq k).symm))⟩
  refine ⟨b0, -a0, Or.inl ?_, ?_⟩
  · intro h0
    rw [h0, map_zero] at hqc
    exact hq hqc
  · rw [← hdp, ← hdq, hpc, hqc, map_neg]
    ring

/-- **The `m = 2` bounded-order criterion, in the committed shape.**

The family `(id, ∂ₖ)` has orders `0` and `1`, which is exactly `ord (Δᵢ) ≤ i`. So for two
polynomials the bounded-order generalized Wronskian criterion holds outright. -/
theorem exists_bounded_order_mvGenWronskian_two {K : Type*} [Field K] [CharZero K]
    [DecidableEq σ] {f g : MvPolynomial σ K} (h : LinearIndependent K ![f, g]) :
    ∃ k : σ, mvGenWronskian ![[], [k]] ![f, g] ≠ 0 := by
  classical
  by_contra hcon
  push_neg at hcon
  have hw : ∀ k : σ, f * pderiv k g - g * pderiv k f = 0 := by
    intro k
    have hk := hcon k
    simpa [mvGenWronskian, mvWronskianMatrix, Matrix.det_fin_two] using hk
  obtain ⟨lam, mu, hne, hsum⟩ := exists_const_dependence_of_forall_wronskian_eq_zero hw
  have hzero : ∑ j, ![lam, mu] j • (![f, g] : Fin 2 → MvPolynomial σ K) j = 0 := by
    rw [Fin.sum_univ_two]
    simpa [smul_eq_C_mul] using hsum
  have hall := Fintype.linearIndependent_iff.mp h ![lam, mu] hzero
  rcases hne with hl | hm
  · exact hl (by simpa using hall 0)
  · exact hm (by simpa using hall 1)

/-! ### General `m`: the criterion Roth's lemma consumes

The `m = 2` case above is exactly the base case that the *univariate* general-`m` converse
in `QOU.Mathlib.GenWronskian` is built on, and the rest of that proof transposes: kernel
vector, derivative descent, Wronskian combination, the `m = 2` case, substitution.

⚠ **The earlier note here recorded this as a plan and warned the analogy might fail where
the univariate proof uses the canonical operator `dⁱ/dxⁱ` while the multivariate family is
chosen.  It does not fail, and the reason is worth stating:** the hypothesis is that *every*
bounded-order Wronskian vanishes, so the cofactor expansion is available for an **arbitrary**
last operator `Δ` with `ord Δ ≤ m−1`.  Being able to vary that operator freely is exactly
what replaces canonicity.  Descent then goes through because `ord (∂ₖ ∘ Δ_l) = |l| + 1 ≤ m−1`
whenever `|l| ≤ m−2`.

**No genericity is used anywhere** — no generic direction, no generic point, no
infinite-field argument.  The generic-direction machinery in
`QOU.Mathlib.DirectionalWronskian` is therefore not needed for this result; it remains as an
independently meaningful reduction. -/

section GeneralM

variable {K : Type*} [Field K] [CharZero K] [DecidableEq σ]

/-- Restatement of the `m = 2` case in the shape the induction consumes: with `f ≠ 0`, the
coefficient of `g` can be taken non-zero, so `g` is a constant multiple of `f`.

Mirrors `Polynomial.exists_dependence_of_wronskian_eq_zero`. -/
theorem exists_dependence_of_forall_wronskian_eq_zero {f g : MvPolynomial σ K} (hf : f ≠ 0)
    (h : ∀ k : σ, f * pderiv k g - g * pderiv k f = 0) :
    ∃ lam mu : K, lam ≠ 0 ∧ C lam * g + C mu * f = 0 := by
  classical
  by_cases hg : g = 0
  · exact ⟨1, 0, one_ne_zero, by simp [hg]⟩
  obtain ⟨lam, mu, hne, hsum⟩ := exists_const_dependence_of_forall_wronskian_eq_zero h
  -- `C lam * f + C mu * g = 0`; with both non-zero, BOTH coefficients are non-zero
  have hmu : mu ≠ 0 := by
    rintro rfl
    rw [map_zero, zero_mul, add_zero] at hsum
    rcases mul_eq_zero.mp hsum with h1 | h1
    · exact (hne.resolve_right (fun h => h rfl)) (by simpa using h1)
    · exact hf h1
  exact ⟨mu, lam, hmu, by rw [← hsum]; ring⟩

omit [CharZero K] [DecidableEq σ] in
/-- **Derivative descent for bounded-order operators.**

If `c` annihilates every operator of order `≤ n`, then `∂ₖc` annihilates every operator of
order `< n`.  Mirrors `Polynomial.sum_derivative_of_forall_sum_eq_zero`; the reason it works
is that `∂ₖ ∘ Δ_l = Δ_{k::l}` has order `|l| + 1 ≤ n`, so the cross term is already zero. -/
theorem sum_pderiv_descent {m : ℕ} (f c : Fin m → MvPolynomial σ K) (n : ℕ)
    (h : ∀ l : List σ, l.length ≤ n → ∑ j, c j * pderivList l (f j) = 0) :
    ∀ (k : σ) (l : List σ), l.length < n →
      ∑ j, pderiv k (c j) * pderivList l (f j) = 0 := by
  intro k l hl
  have hbase := h l (le_of_lt hl)
  have hnext := h (k :: l) (by simpa using hl)
  have hd : pderiv k (∑ j, c j * pderivList l (f j)) = 0 := by rw [hbase, map_zero]
  rw [map_sum] at hd
  have hexp : ∀ j : Fin m, pderiv k (c j * pderivList l (f j))
      = pderiv k (c j) * pderivList l (f j) + c j * pderivList (k :: l) (f j) := by
    intro j
    have hcons : pderivList (k :: l) (f j) = pderiv k (pderivList l (f j)) := rfl
    rw [Derivation.leibniz, hcons]
    simp only [smul_eq_mul]
    ring
  simp only [hexp, Finset.sum_add_distrib] at hd
  rw [hnext, add_zero] at hd
  exact hd

omit [CharZero K] [DecidableEq σ] in
/-- **The Wronskian combination, bounded-order version.**

`∑ⱼ (c_l ∂ₖc_j − c_j ∂ₖc_l) Δ_l fⱼ = 0`, and its `l`-th entry vanishes identically.  Mirrors
`Polynomial.sum_wronskian_combo_eq_zero`: multiplying by `c_l` where the classical proof
divides is what keeps everything inside the polynomial ring. -/
theorem sum_wronskian_combo_bounded {m : ℕ} (f c : Fin m → MvPolynomial σ K) (n : ℕ)
    (jl : Fin m) (h : ∀ l : List σ, l.length ≤ n → ∑ j, c j * pderivList l (f j) = 0) :
    ∀ (k : σ) (l : List σ), l.length < n →
      ∑ j, (c jl * pderiv k (c j) - c j * pderiv k (c jl)) * pderivList l (f j) = 0 := by
  intro k l hl
  have hdesc := sum_pderiv_descent f c n h k l hl
  have hbase := h l (le_of_lt hl)
  have hexp : ∑ j, (c jl * pderiv k (c j) - c j * pderiv k (c jl)) * pderivList l (f j)
      = c jl * (∑ j, pderiv k (c j) * pderivList l (f j))
        - pderiv k (c jl) * (∑ j, c j * pderivList l (f j)) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl fun j _ => by ring
  rw [hexp, hdesc, hbase, mul_zero, mul_zero, sub_zero]

/-- **Collapse to constants.**  Once every Wronskian `c_l ∂ₖc_j − c_j ∂ₖc_l` vanishes and
`c_l ≠ 0`, the polynomial coefficient vector is a constant multiple of `c_l`, and the
constant vector is non-zero because its `l`-th entry is `1`.

Mirrors `Polynomial.exists_constant_dependence_of_wronskians_vanish`. -/
theorem exists_constant_dependence_of_bounded_wronskians_vanish {m : ℕ}
    (f c : Fin m → MvPolynomial σ K) (jl : Fin m) (hl : c jl ≠ 0)
    (hw : ∀ (j : Fin m) (k : σ), c jl * pderiv k (c j) - c j * pderiv k (c jl) = 0)
    (h0 : ∑ j, c j * f j = 0) :
    ∃ lam : Fin m → K, lam ≠ 0 ∧ ∑ j, C (lam j) * f j = 0 := by
  classical
  have key : ∀ j, ∃ t : K, c j = C t * c jl := by
    intro j
    obtain ⟨lam, mu, hlam, hsum⟩ := exists_dependence_of_forall_wronskian_eq_zero hl (hw j)
    refine ⟨-mu / lam, ?_⟩
    have hlam0 : (C lam : MvPolynomial σ K) ≠ 0 := by simpa using hlam
    apply mul_left_cancel₀ hlam0
    have hcollect : C lam * (C (-mu / lam) * c jl) = C (lam * (-mu / lam)) * c jl := by
      rw [map_mul]; ring
    have hval : lam * (-mu / lam) = -mu := by field_simp
    rw [hcollect, hval, map_neg]
    linear_combination hsum
  choose t ht using key
  have htl : t jl = 1 := by
    have hj := ht jl
    nth_rewrite 1 [show c jl = C 1 * c jl by simp] at hj
    exact ((C_inj K _ _).mp (mul_right_cancel₀ hl hj)).symm
  refine ⟨t, fun hzero => ?_, ?_⟩
  · rw [hzero] at htl; simp at htl
  · have hfac : c jl * ∑ j, C (t j) * f j = 0 := by
      rw [Finset.mul_sum, ← h0]
      exact Finset.sum_congr rfl fun j _ => by rw [ht j]; ring
    exact (mul_eq_zero.mp hfac).resolve_left hl

open Matrix in
/-- **Route B: the bounded-order criterion for general `m`.** -/
theorem exists_dependence_of_forall_bounded_mvGenWronskian_eq_zero :
    ∀ {m : ℕ}, 0 < m → ∀ f : Fin m → MvPolynomial σ K,
      (∀ D : Fin m → List σ, (∀ i, (D i).length ≤ (i : ℕ)) → mvGenWronskian D f = 0) →
      ∃ lam : Fin m → K, lam ≠ 0 ∧ ∑ j, C (lam j) * f j = 0 := by
  classical
  intro m
  induction m with
  | zero => intro h; exact absurd h (lt_irrefl 0)
  | succ n ih =>
    intro _ f hall
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · refine ⟨fun _ => 1, ?_, ?_⟩
      · intro h; have := congrFun h 0; simp at this
      · have h1 : mvGenWronskian (fun _ => ([] : List σ)) f = f 0 := by
          simp [mvGenWronskian, mvWronskianMatrix]
        have h2 := hall (fun _ => []) (by intro i; simp)
        rw [h1] at h2
        simp [h2]
    · by_cases hminor : ∀ D' : Fin n → List σ, (∀ i, (D' i).length ≤ (i : ℕ)) →
          mvGenWronskian D' (Fin.init f) = 0
      · obtain ⟨lam', hne, hsum⟩ := ih hn (Fin.init f) hminor
        refine ⟨Fin.snoc lam' 0, ?_, ?_⟩
        · intro h
          refine hne (_root_.funext fun j => ?_)
          have := congrFun h j.castSucc
          simpa [Fin.snoc_castSucc] using this
        · rw [Fin.sum_univ_castSucc]
          simp only [Fin.snoc_castSucc, Fin.snoc_last, map_zero, zero_mul, add_zero]
          exact hsum
      · push_neg at hminor
        obtain ⟨D', hD'bd, hD'ne⟩ := hminor
        have hbd : ∀ (l : List σ), l.length ≤ n →
            ∀ i : Fin (n+1), ((Fin.snoc D' l : Fin (n+1) → List σ) i).length ≤ (i : ℕ) := by
          intro l hl i
          induction i using Fin.lastCases with
          | last => simpa using hl
          | cast i' => simpa [Fin.snoc_castSucc] using hD'bd i'
        obtain ⟨c, hclast, hexp⟩ : ∃ c : Fin (n+1) → MvPolynomial σ K,
            c (Fin.last n) = mvGenWronskian D' (Fin.init f) ∧
            ∀ l : List σ, l.length ≤ n → ∑ j, c j * pderivList l (f j) = 0 := by
          refine ⟨fun j => (-1) ^ ((Fin.last n : ℕ) + (j : ℕ)) *
            ((mvWronskianMatrix (Fin.snoc D' ([] : List σ)) f).submatrix
              (Fin.last n).succAbove j.succAbove).det, ?_, ?_⟩
          · dsimp only
            have hsign : (-1 : MvPolynomial σ K) ^ ((Fin.last n : ℕ) + (Fin.last n : ℕ)) = 1 := by
              rw [← two_mul, pow_mul]; norm_num
            have hmin : (mvWronskianMatrix (Fin.snoc D' ([] : List σ)) f).submatrix
                (Fin.last n).succAbove (Fin.last n).succAbove
                = mvWronskianMatrix D' (Fin.init f) := by
              refine Matrix.ext fun i k => ?_
              simp [mvWronskianMatrix, Fin.succAbove_last, Fin.snoc_castSucc, Fin.init]
            rw [hsign, hmin, one_mul, mvGenWronskian]
          · intro l hl
            dsimp only
            have hsub : ∀ j : Fin (n+1), (mvWronskianMatrix (Fin.snoc D' l) f).submatrix
                (Fin.last n).succAbove j.succAbove
                = (mvWronskianMatrix (Fin.snoc D' ([] : List σ)) f).submatrix
                    (Fin.last n).succAbove j.succAbove := by
              intro j
              refine Matrix.ext fun i k => ?_
              simp [mvWronskianMatrix, Fin.succAbove_last, Fin.snoc_castSucc]
            have hkey : ∑ j : Fin (n+1), ((-1 : MvPolynomial σ K) ^ ((Fin.last n : ℕ) + (j : ℕ)) *
                ((mvWronskianMatrix (Fin.snoc D' ([] : List σ)) f).submatrix
                  (Fin.last n).succAbove j.succAbove).det) * pderivList l (f j)
                = (mvWronskianMatrix (Fin.snoc D' l) f).det := by
              rw [Matrix.det_succ_row _ (Fin.last n)]
              refine Finset.sum_congr rfl fun j _ => ?_
              have hentry : mvWronskianMatrix (Fin.snoc D' l) f (Fin.last n) j
                  = pderivList l (f j) := by simp [mvWronskianMatrix, Fin.snoc_last]
              rw [hentry, ← hsub j]
              ring
            rw [hkey]
            exact hall (Fin.snoc D' l) (hbd l hl)
        have hclne : c (Fin.last n) ≠ 0 := by rw [hclast]; exact hD'ne
        -- the Wronskian combination is a kernel vector of the non-degenerate minor
        have hw : ∀ (j : Fin (n+1)) (k : σ),
            c (Fin.last n) * pderiv k (c j) - c j * pderiv k (c (Fin.last n)) = 0 := by
          intro j k
          have hcombo := sum_wronskian_combo_bounded f c n (Fin.last n) hexp k
          have hker : mvWronskianMatrix D' (Fin.init f) *ᵥ (Fin.init (fun j' =>
              c (Fin.last n) * pderiv k (c j') - c j' * pderiv k (c (Fin.last n)))) = 0 := by
            refine _root_.funext fun i => ?_
            have hi := hcombo (D' i) (lt_of_le_of_lt (hD'bd i) i.isLt)
            rw [Fin.sum_univ_castSucc] at hi
            simp only [sub_self, zero_mul, add_zero] at hi
            simp only [Matrix.mulVec, dotProduct, mvWronskianMatrix, Matrix.of_apply,
              Pi.zero_apply, Fin.init]
            rw [← hi]
            exact Finset.sum_congr rfl fun k' _ => mul_comm _ _
          have hinit : Fin.init (fun j' =>
              c (Fin.last n) * pderiv k (c j') - c j' * pderiv k (c (Fin.last n))) = 0 :=
            Matrix.eq_zero_of_mulVec_eq_zero (by rw [← mvGenWronskian]; exact hD'ne) hker
          induction j using Fin.lastCases with
          | last => ring
          | cast j' => simpa [Fin.init] using congrFun hinit j'
        have h0 : ∑ j, c j * f j = 0 := by simpa using hexp [] (by simp)
        exact exists_constant_dependence_of_bounded_wronskians_vanish f c (Fin.last n)
          hclne hw h0

/-- **An independent family has a non-zero generalized Wronskian of BOUNDED ORDER.**

`ord (Δᵢ) ≤ i` — the form Roth's lemma consumes. -/
theorem exists_bounded_order_mvGenWronskian_ne_zero {m : ℕ} (hm : 0 < m)
    (f : Fin m → MvPolynomial σ K) (hf : LinearIndependent K f) :
    ∃ D : Fin m → List σ, (∀ i, (D i).length ≤ (i : ℕ)) ∧ mvGenWronskian D f ≠ 0 := by
  classical
  by_contra hcon
  push_neg at hcon
  obtain ⟨lam, hlam, hsum⟩ :=
    exists_dependence_of_forall_bounded_mvGenWronskian_eq_zero hm f hcon
  refine hlam (_root_.funext fun j => ?_)
  refine Fintype.linearIndependent_iff.mp hf lam ?_ j
  rw [← hsum]
  exact Finset.sum_congr rfl fun j _ => smul_eq_C_mul _ _

/-- **Independence is exactly a non-vanishing bounded-order generalized Wronskian.** -/
theorem linearIndependent_iff_exists_bounded_order_mvGenWronskian_ne_zero {m : ℕ} (hm : 0 < m)
    (f : Fin m → MvPolynomial σ K) :
    LinearIndependent K f
      ↔ ∃ D : Fin m → List σ, (∀ i, (D i).length ≤ (i : ℕ)) ∧ mvGenWronskian D f ≠ 0 := by
  classical
  refine ⟨exists_bounded_order_mvGenWronskian_ne_zero hm f, ?_⟩
  rintro ⟨D, _, hDne⟩
  rw [Fintype.linearIndependent_iff]
  by_contra hcon
  push_neg at hcon
  obtain ⟨lam, hsum, i, hi⟩ := hcon
  refine hDne (mvGenWronskian_eq_zero_of_dependent D f lam ?_ ?_)
  · intro h0
    rw [h0] at hi
    exact hi rfl
  · rw [← hsum]
    exact Finset.sum_congr rfl fun j _ => (smul_eq_C_mul _ _).symm

end GeneralM

end MvPolynomial
