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

/-! ### ⚠ This changes the outlook for general `m`

`QOU.Mathlib.DirectionalWronskian` records a route to the general bounded-order criterion
via a **generic direction**, and flags the direction-existence step as genuinely open — a
genericity statement over a vector space that the naive argument cannot close.

The theorem just proved suggests a **second route that avoids genericity entirely**, because
it is precisely the base case the univariate proof already in this repo is built on.
`Polynomial.exists_dependence_of_genWronskian_eq_zero` (in `QOU.Mathlib.GenWronskian`)
proves the general-`m` univariate converse from:

1. a kernel vector from the vanishing determinant,
2. **derivative descent** — `sum_derivative_of_forall_sum_eq_zero`,
3. the **Wronskian combination** `c_l ∂c_j − c_j ∂c_l`, which kills one entry without
   dividing,
4. the `m = 2` converse, consumed at step 3's output,
5. substitution.

Each step has a bounded-order multivariate analogue, and the reason is that the contradiction
hypothesis is *"every* bounded-order Wronskian vanishes", which is exactly what makes the
cofactor expansion valid for an **arbitrary** last operator `Δ` with `ord Δ ≤ m−1`. Descent
then works because `ord (∂ₖ ∘ Δ) ≤ m−1` whenever `ord Δ ≤ m−2`.

⚠ **Recorded as a plan, not a theorem.** Nothing above is proved for general `m`, and the
analogy could fail at the point where the univariate argument uses the canonical operator
`dⁱ/dxⁱ` while the multivariate family is chosen. It is written down because the base case
landing here makes it the cheaper of the two routes to try first. -/

end MvPolynomial
