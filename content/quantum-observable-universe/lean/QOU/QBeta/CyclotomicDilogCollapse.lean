/-
# Cyclotomic collapse of the q-Pochhammer denominator (Φ_b workplan result L1)

This file proves the *finite root-of-unity reduction* of the q-Pochhammer
symbol `(x; q)_N` evaluated at a primitive `N`-th root of unity `q = ζ_N`.

At a primitive `N`-th root of unity the infinite/contour q-Pochhammer product
collapses to a finite one, and that finite product telescopes against the
cyclotomic factorisation `Y^N - 1 = ∏_{k<N}(Y - ζ^k)`:

    ∏_{k=0}^{N-1} (1 - x·ζ^k) = 1 - x^N .

This is the `contour → finite-algebra` step of the Φ_b construction
(PR #3768, bean qou-b8iu): it turns the analytic q-Pochhammer denominator
into a polynomial in `x` whose only zeros are the `N`-th roots of `1`.

The result is stated over a generic field `K` (never specialised to `ℂ`),
per the §7c base-ring convention — a field is a `CommRing` + `IsDomain`,
which is all the cyclotomic factorisation `Polynomial.X_pow_sub_one_eq_prod`
requires.
-/
import Mathlib.RingTheory.RootsOfUnity.Basic
import Mathlib.RingTheory.Polynomial.Cyclotomic.Basic
import Mathlib.Tactic

namespace QOU.QBeta.CyclotomicDilogCollapse

open Polynomial Finset

/-- **Cyclotomic collapse.** Over a field `K`, if `ζ` is a primitive `N`-th
root of unity (`N > 0`), then for every `x : K`,
`∏_{k=0}^{N-1} (1 - x·ζ^k) = 1 - x^N`.

This is the finite root-of-unity reduction of the q-Pochhammer denominator
`(x; q)_N` at `q = ζ_N`. -/
theorem cyclotomic_collapse
    {K : Type*} [Field K] {ζ : K} {N : ℕ} (hN : 0 < N)
    (hζ : IsPrimitiveRoot ζ N) (x : K) :
    ∏ k ∈ Finset.range N, (1 - x * ζ ^ k) = 1 - x ^ N := by
  classical
  -- The map `k ↦ ζ^k` sends `range N` bijectively onto the N-th roots of unity.
  have hInjOn : Set.InjOn (fun i => ζ ^ i) (Finset.range N : Finset ℕ) := by
    intro i hi j hj h
    exact hζ.pow_inj (by simpa using hi) (by simpa using hj) h
  have himg : (Finset.range N).image (fun i => ζ ^ i) = nthRootsFinset N (1 : K) := by
    apply Finset.eq_of_subset_of_card_le
    · intro y hy
      simp only [Finset.mem_image, Finset.mem_range] at hy
      obtain ⟨i, _, rfl⟩ := hy
      rw [mem_nthRootsFinset hN]
      rw [← pow_mul, mul_comm, pow_mul, hζ.pow_eq_one, one_pow]
    · rw [hζ.card_nthRootsFinset, Finset.card_image_of_injOn hInjOn, Finset.card_range]
  -- Cyclotomic factorisation, evaluated at `x⁻¹`.
  have hpoly := X_pow_sub_one_eq_prod hN hζ
  have heval := congrArg (Polynomial.eval x⁻¹) hpoly
  simp only [eval_sub, eval_pow, eval_X, eval_one, eval_prod, eval_C] at heval
  -- Reindex the root product `∏ ω` as `∏ k∈range N` via the bijection.
  rw [← himg, Finset.prod_image hInjOn] at heval
  -- Now `heval : x⁻¹ ^ N - 1 = ∏ k ∈ range N, (x⁻¹ - ζ ^ k)`.
  by_cases hx : x = 0
  · subst hx
    simp [zero_pow hN.ne']
  · calc ∏ k ∈ Finset.range N, (1 - x * ζ ^ k)
        = ∏ k ∈ Finset.range N, (x * (x⁻¹ - ζ ^ k)) := by
          apply Finset.prod_congr rfl
          intro k _
          rw [mul_sub, mul_inv_cancel₀ hx]
      _ = (∏ _k ∈ Finset.range N, x) * ∏ k ∈ Finset.range N, (x⁻¹ - ζ ^ k) := by
          rw [Finset.prod_mul_distrib]
      _ = x ^ N * ∏ k ∈ Finset.range N, (x⁻¹ - ζ ^ k) := by
          rw [Finset.prod_const, Finset.card_range]
      _ = x ^ N * (x⁻¹ ^ N - 1) := by rw [← heval]
      _ = 1 - x ^ N := by
          rw [mul_sub, ← mul_pow, mul_inv_cancel₀ hx, one_pow, mul_one]

end QOU.QBeta.CyclotomicDilogCollapse
