/-
  **Heights of products and determinants of multivariate polynomials over `ℤ`.**

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  "Height" here is the sup-norm on coefficients, `H(f) = maxₙ |coeff n f|`, kept implicit:
  every statement takes a bound `B` with `∀ n, |coeff n f| ≤ B` rather than committing to a
  definition of `H`.  That keeps the results usable without a `Finset.sup'` and a non-emptiness
  side condition at every call site.

  ═══ THE SHAPE OF THE BOUNDS ═══

  A product costs a factor of the **support size**, not just the heights:

      H(f · g)         ≤ #supp(f) · H(f) · H(g)
      H(∏_{i<k} fᵢ)    ≤ (S · B)^k          for  #supp(fᵢ) ≤ S,  H(fᵢ) ≤ B,  1 ≤ S
      H(det M)         ≤ m! · (S · B)^m      for an  m × m  matrix

  The support factor is real: `coeff n (f·g)` is a *sum* over the antidiagonal of `n`, and a
  summand survives whenever `a ∈ supp f` — at most `#supp f` of them, since `b = n − a` is
  then determined.  Disjoint variables collapse that sum to a single term, which is why
  `MvPolynomial.abs_coeff_mul_separated_le` in `QOU/Mathlib/SeparatedHeight.lean` has no such
  factor.

  ⚠ **Everything here is the EASY direction** — up, from factors to the product.  Gelfond's
  inequality is the direction that comes *down*, from a product's height to its factors', and
  it is the one that needs the Mahler measure (`QOU/Mathlib/MahlerJensen.lean`).  Nothing in
  this module supplies it, and no bound here should be cited as though it did.

  ═══ WHY THE DETERMINANT ═══

  A generalized Wronskian `mvGenWronskian D f` is a determinant whose entries are iterated
  `pderiv`s of the auxiliary polynomial, so `abs_coeff_det_le` is what turns a height bound on
  that polynomial into one on its Wronskian.  The per-entry inputs it needs — a height bound
  and a support-size bound for `pderiv` — are in `QOU/Mathlib/MvGenWronskian.lean`, next to
  `coeff_pderiv`, which they depend on.
-/
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Algebra.Ring.Int.Units
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.Ring

namespace MvPolynomial

variable {σ : Type*}

/-- `H(1) ≤ 1`: the base case of the product induction. -/
theorem abs_coeff_one_le (n : σ →₀ ℕ) : |coeff n (1 : MvPolynomial σ ℤ)| ≤ 1 := by
  classical
  rw [coeff_one]
  split_ifs <;> simp

/-- **`H(f·g) ≤ #supp(f) · H(f) · H(g)`.**

In `coeff n (f·g) = ∑ coeff a f · coeff b g` over the antidiagonal of `n`, a summand survives
only when `a ∈ supp f`, and `b = n − a` is then determined — so at most `#supp f` terms
survive, each bounded by `H(f)·H(g)`.

⚠ The easy direction.  See the module header. -/
theorem abs_coeff_mul_le {f g : MvPolynomial σ ℤ} {Bf Bg : ℤ}
    (hf : ∀ a, |coeff a f| ≤ Bf) (hg : ∀ b, |coeff b g| ≤ Bg) (n : σ →₀ ℕ) :
    |coeff n (f * g)| ≤ (f.support.card : ℤ) * (Bf * Bg) := by
  classical
  have hBf : (0 : ℤ) ≤ Bf := le_trans (abs_nonneg _) (hf 0)
  have hBg : (0 : ℤ) ≤ Bg := le_trans (abs_nonneg _) (hg 0)
  set S := (Finset.antidiagonal n).filter (fun p => p.1 ∈ f.support) with hS
  rw [coeff_mul]
  refine le_trans (Finset.abs_sum_le_sum_abs _ _) ?_
  have hfilter : ∑ p ∈ Finset.antidiagonal n, |coeff p.1 f * coeff p.2 g|
      = ∑ p ∈ S, |coeff p.1 f * coeff p.2 g| := by
    refine (Finset.sum_filter_of_ne ?_).symm
    intro p _ hne
    rw [mem_support_iff]
    intro h0
    exact hne (by rw [h0, zero_mul, abs_zero])
  rw [hfilter]
  have hbound : ∀ p ∈ S, |coeff p.1 f * coeff p.2 g| ≤ Bf * Bg := by
    intro p _
    rw [abs_mul]
    exact mul_le_mul (hf _) (hg _) (abs_nonneg _) hBf
  refine le_trans (Finset.sum_le_card_nsmul S _ (Bf * Bg) hbound) ?_
  rw [nsmul_eq_mul]
  refine mul_le_mul_of_nonneg_right ?_ (mul_nonneg hBf hBg)
  have hcard : S.card ≤ f.support.card := by
    refine Finset.card_le_card_of_injOn (fun p => p.1) ?_ ?_
    · intro p hp
      exact (Finset.mem_filter.mp hp).2
    · -- `b = n − a` is determined by `a` on the antidiagonal, so `p ↦ p.1` is injective.
      intro p hp q hq hpq
      have hpq' : p.1 = q.1 := hpq
      have hp' := Finset.mem_antidiagonal.mp (Finset.mem_filter.mp hp).1
      have hq' := Finset.mem_antidiagonal.mp (Finset.mem_filter.mp hq).1
      have h2 : p.2 = q.2 := by
        have hh := hp'.trans hq'.symm
        rw [hpq'] at hh
        exact add_left_cancel hh
      exact Prod.ext hpq' h2
  exact_mod_cast hcard

/-- **`H(∏ t) ≤ (S·B)^{card t}`** for a multiset of factors, each of support size at most `S`
and height at most `B`.

`1 ≤ S` is what lets the bound be stated as a clean `k`-th power.  The sharp form shaves one
`S` — the recursion only ever applies `abs_coeff_mul_le` with an *original* factor in the
first slot, never a partial product, so the last factor contributes no support cost — but
carrying `S^{k-1}` through the induction costs more than it buys. -/
theorem abs_coeff_multiset_prod_le {S B : ℤ} (hS1 : 1 ≤ S) (hB0 : 0 ≤ B)
    (t : Multiset (MvPolynomial σ ℤ))
    (hS : ∀ f ∈ t, (f.support.card : ℤ) ≤ S) (hB : ∀ f ∈ t, ∀ n, |coeff n f| ≤ B)
    (n : σ →₀ ℕ) :
    |coeff n t.prod| ≤ (S * B) ^ Multiset.card t := by
  classical
  have hSB0 : (0 : ℤ) ≤ S * B := mul_nonneg (le_trans zero_le_one hS1) hB0
  revert hS hB n
  induction t using Multiset.induction_on with
  | empty =>
      intro _ _ n
      simpa using abs_coeff_one_le n
  | cons f t ih =>
      intro hS hB n
      have hSf : (f.support.card : ℤ) ≤ S := hS f (Multiset.mem_cons_self f t)
      have hBf : ∀ m, |coeff m f| ≤ B := hB f (Multiset.mem_cons_self f t)
      have hSt : ∀ g ∈ t, (g.support.card : ℤ) ≤ S :=
        fun g hg => hS g (Multiset.mem_cons_of_mem hg)
      have hBt : ∀ g ∈ t, ∀ m, |coeff m g| ≤ B :=
        fun g hg => hB g (Multiset.mem_cons_of_mem hg)
      rw [Multiset.prod_cons, Multiset.card_cons]
      have hstep := abs_coeff_mul_le (f := f) (g := t.prod) (Bf := B)
        (Bg := (S * B) ^ Multiset.card t) hBf (fun m => ih hSt hBt m) n
      refine le_trans hstep ?_
      have h1 : (0 : ℤ) ≤ B * (S * B) ^ Multiset.card t :=
        mul_nonneg hB0 (pow_nonneg hSB0 _)
      calc (f.support.card : ℤ) * (B * (S * B) ^ Multiset.card t)
          ≤ S * (B * (S * B) ^ Multiset.card t) := mul_le_mul_of_nonneg_right hSf h1
        _ = (S * B) ^ (Multiset.card t + 1) := by rw [pow_succ]; ring

/-- **`H(∏_{i ∈ s} Fᵢ) ≤ (S·B)^{#s}`** — the `Finset` form of the previous theorem. -/
theorem abs_coeff_prod_le {ι : Type*} {S B : ℤ} (hS1 : 1 ≤ S) (hB0 : 0 ≤ B)
    (s : Finset ι) (F : ι → MvPolynomial σ ℤ)
    (hS : ∀ i ∈ s, ((F i).support.card : ℤ) ≤ S) (hB : ∀ i ∈ s, ∀ n, |coeff n (F i)| ≤ B)
    (n : σ →₀ ℕ) :
    |coeff n (∏ i ∈ s, F i)| ≤ (S * B) ^ s.card := by
  classical
  rw [Finset.prod_eq_multiset_prod]
  have hcard : Multiset.card (s.val.map F) = s.card := by
    rw [Multiset.card_map]; rfl
  rw [← hcard]
  refine abs_coeff_multiset_prod_le hS1 hB0 _ ?_ ?_ n
  · intro g hg
    obtain ⟨i, hi, rfl⟩ := Multiset.mem_map.mp hg
    exact hS i hi
  · intro g hg
    obtain ⟨i, hi, rfl⟩ := Multiset.mem_map.mp hg
    exact hB i hi

/-- **`H(det M) ≤ m! · (S·B)^m`** for an `m × m` matrix of integer multivariate polynomials
with entries of support size at most `S` and height at most `B`.

Leibniz expands the determinant into `m!` signed products of `m` entries.  The sign is a unit
of `ℤ`, so it does not move the absolute value at all; each product is bounded by
`abs_coeff_prod_le`; and the `m!` is just the number of permutations.

This is what turns a height bound on an auxiliary polynomial into one on a generalized
Wronskian.  ⚠ It needs `S` — a *support-size* bound on the entries — not only a height bound;
supplying that for iterated `pderiv`s is `card_support_pderiv_le` in
`QOU/Mathlib/MvGenWronskian.lean`. -/
theorem abs_coeff_det_le {ι : Type*} [Fintype ι] [DecidableEq ι] {S B : ℤ}
    (hS1 : 1 ≤ S) (hB0 : 0 ≤ B) (M : Matrix ι ι (MvPolynomial σ ℤ))
    (hS : ∀ i j, ((M i j).support.card : ℤ) ≤ S)
    (hB : ∀ i j, ∀ n, |coeff n (M i j)| ≤ B)
    (n : σ →₀ ℕ) :
    |coeff n M.det| ≤ ((Fintype.card ι).factorial : ℤ) * (S * B) ^ (Fintype.card ι) := by
  classical
  have hsm : ∀ (p : Equiv.Perm ι) (q : MvPolynomial σ ℤ),
      |coeff n (Equiv.Perm.sign p • q)| = |coeff n q| := by
    intro p q
    rw [Units.smul_def, coeff_smul, smul_eq_mul, abs_mul]
    rcases Int.units_eq_one_or (Equiv.Perm.sign p) with h | h <;> rw [h] <;> simp
  have hterm : ∀ p : Equiv.Perm ι,
      |coeff n (Equiv.Perm.sign p • ∏ i, M (p i) i)| ≤ (S * B) ^ (Fintype.card ι) := by
    intro p
    rw [hsm]
    have h := abs_coeff_prod_le (σ := σ) hS1 hB0 Finset.univ (fun i => M (p i) i)
      (fun i _ => hS (p i) i) (fun i _ => hB (p i) i) n
    rwa [Finset.card_univ] at h
  rw [Matrix.det_apply, coeff_sum]
  refine le_trans (Finset.abs_sum_le_sum_abs _ _) ?_
  refine le_trans (Finset.sum_le_card_nsmul _ _ _ (fun p _ => hterm p)) ?_
  rw [Finset.card_univ, Fintype.card_perm, nsmul_eq_mul]

end MvPolynomial
