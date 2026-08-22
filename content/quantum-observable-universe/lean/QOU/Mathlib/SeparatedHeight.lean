/-
  **Heights of a disjoint-variable product** — and a third correction to where the
  difficulty of Roth's lemma sits.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ THE FINDING ═══

  For polynomials in **disjoint** groups of variables the height is *exactly* multiplicative:

      H(U(x) · V(y)) = H(U) · H(V)

  and the reason is not an estimate at all.  The monomials `x^i y^j` are pairwise distinct, so
  the coefficient of `x^i y^j` in the product **is** `uᵢ · vⱼ` — one term, no cancellation, no
  sum over an antidiagonal that survives.  That identity is `coeff_sumElim_rename_mul`; the
  two height statements below are its two directions in the form a caller wants.

  ═══ ⚠ WHY THIS MATTERS, AND EXACTLY HOW FAR IT GOES ═══

  Bean `qou-4lbh` has predicted three times where the remaining cost of Roth's lemma sits, and
  been wrong twice.  Its current prediction is that the induction step needs **Gelfond's
  inequality** to bound the heights of the factors.

  For the step this repo has actually formalised — the separated-Wronskian factorization
  `W = U(x) · V(y)` of `QOU/Mathlib/SeparatedWronskian.lean`, `det_separated_wronskian` — that
  prediction is **wrong, and this module is the witness.**  `abs_coeff_le_of_mul_separated`
  gives `H(U) ≤ H(W)` from nothing but the identity above and the fact that a non-zero integer
  has absolute value at least one.  Gelfond is an inequality about factors of a product in
  *shared* variables, where coefficients genuinely mix; here they do not mix at all.

  ⚠ **This does not say Gelfond is unnecessary for Roth's lemma.**  It says it is unnecessary
  *for this step*.  Whether some other step needs it is a question this module has **not**
  measured, and — given the record above — should be measured rather than asserted.  The
  Mahler machinery in `QOU/Mathlib/MahlerJensen.lean` is proved and costs nothing to keep;
  what should not be kept is the claim that this particular step is blocked on it.

  ═══ THE SHARED-VARIABLE CONTRAST ═══

  `MvPolynomial.abs_coeff_mul_le` in `QOU/Mathlib/MvPolynomialHeight.lean` is the same bound
  without disjointness: `H(f·g) ≤ #supp(f)·H(f)·H(g)`.  The `#supp f` is exactly what
  disjointness removes — there the antidiagonal sum collapses to one term regardless of how
  large the supports are.

  Note which direction is easy.  Going *up*, from the factors' heights to the product's, is
  elementary in either case.  Gelfond is the direction that comes *down*, from a product's
  height to its factors', and only in shared variables; that is the one that needs the Mahler
  measure, and nothing in either module supplies it.
-/
import Mathlib.Algebra.MvPolynomial.Rename
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Algebra.Order.Ring.Int

open Finsupp

namespace MvPolynomial

variable {σ τ R : Type*} [CommRing R]

/-- The exponent vector `Finsupp.sumElim i j` on `σ ⊕ τ` is the sum of the two pushed-forward
vectors — the bookkeeping that lets `coeff_mul`'s antidiagonal be evaluated. -/
theorem sumElim_eq_mapDomain_add (i : σ →₀ ℕ) (j : τ →₀ ℕ) :
    Finsupp.sumElim i j
      = Finsupp.mapDomain Sum.inl i + Finsupp.mapDomain Sum.inr j := by
  classical
  ext x
  cases x with
  | inl a =>
    rw [Finsupp.add_apply, Finsupp.mapDomain_apply Sum.inl_injective,
      Finsupp.mapDomain_notin_range (f := Sum.inr) j (Sum.inl a) (by simp),
      Finsupp.sumElim_inl, add_zero]
  | inr b =>
    rw [Finsupp.add_apply, Finsupp.mapDomain_apply Sum.inr_injective,
      Finsupp.mapDomain_notin_range (f := Sum.inl) i (Sum.inr b) (by simp),
      Finsupp.sumElim_inr, zero_add]

/-- Every exponent vector on `σ ⊕ τ` splits, so the identity below covers *all* coefficients
of the product, not just those of a special shape. -/
theorem eq_sumElim (n : (σ ⊕ τ) →₀ ℕ) :
    n = Finsupp.sumElim (Finsupp.sumFinsuppEquivProdFinsupp n).1
      (Finsupp.sumFinsuppEquivProdFinsupp n).2 := by
  ext x
  cases x with
  | inl a => rfl
  | inr b => rfl

/-- **The identity this module rests on.**  For disjoint variable groups the coefficients of a
product are *exactly* the products of the coefficients:

    coeff (i ⊞ j) (U · V) = coeff i U * coeff j V

`coeff_mul` sums over the antidiagonal of `i ⊞ j`, but a summand can be non-zero only if its
first component is supported on `σ` and its second on `τ` — and there is exactly one such
splitting.  Every other term dies, so no estimate is involved and the result is an equality.

Stated over any `CommRing`; no domain hypothesis, because the vanishing of the other terms is
established factor-by-factor rather than through `mul_ne_zero_iff`. -/
theorem coeff_sumElim_rename_mul (u : MvPolynomial σ R) (v : MvPolynomial τ R)
    (i : σ →₀ ℕ) (j : τ →₀ ℕ) :
    coeff (Finsupp.sumElim i j)
        ((rename Sum.inl u : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr v)
      = coeff i u * coeff j v := by
  classical
  rw [coeff_mul, Finset.sum_eq_single
    (Finsupp.mapDomain Sum.inl i, Finsupp.mapDomain Sum.inr j)]
  · rw [coeff_rename_mapDomain _ Sum.inl_injective, coeff_rename_mapDomain _ Sum.inr_injective]
  · rintro ⟨a, b⟩ hab hne
    dsimp only
    rcases eq_or_ne (coeff a (rename Sum.inl u : MvPolynomial (σ ⊕ τ) R)) 0 with h0 | hna
    · rw [h0, zero_mul]
    rcases eq_or_ne (coeff b (rename Sum.inr v : MvPolynomial (σ ⊕ τ) R)) 0 with h0 | hnb
    · rw [h0, mul_zero]
    exfalso
    obtain ⟨d, hd, -⟩ := coeff_rename_ne_zero _ _ _ hna
    obtain ⟨e, he, -⟩ := coeff_rename_ne_zero _ _ _ hnb
    subst hd
    subst he
    rw [Finset.mem_antidiagonal] at hab
    apply hne
    have hdi : d = i := by
      ext x
      have hx := congrArg (fun f => f (Sum.inl x)) hab
      simpa [Finsupp.mapDomain_apply Sum.inl_injective,
        Finsupp.mapDomain_notin_range (f := Sum.inr) e (Sum.inl x) (by simp),
        Finsupp.sumElim_inl] using hx
    have hej : e = j := by
      ext y
      have hy := congrArg (fun f => f (Sum.inr y)) hab
      simpa [Finsupp.mapDomain_apply Sum.inr_injective,
        Finsupp.mapDomain_notin_range (f := Sum.inl) d (Sum.inr y) (by simp),
        Finsupp.sumElim_inr] using hy
    rw [hdi, hej]
  · intro h
    exact absurd (Finset.mem_antidiagonal.mpr (sumElim_eq_mapDomain_add i j).symm) h

/-- **`H(U · V) ≤ H(U) · H(V)`**, one coefficient at a time.

Immediate from the identity: every coefficient of the product is a single product `uᵢvⱼ`. -/
theorem abs_coeff_mul_separated_le {u : MvPolynomial σ ℤ} {v : MvPolynomial τ ℤ} {Bu Bv : ℤ}
    (hu : ∀ i, |coeff i u| ≤ Bu) (hv : ∀ j, |coeff j v| ≤ Bv) (n : (σ ⊕ τ) →₀ ℕ) :
    |coeff n ((rename Sum.inl u : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr v)| ≤ Bu * Bv := by
  have hBu : (0 : ℤ) ≤ Bu := le_trans (abs_nonneg _) (hu 0)
  rw [eq_sumElim n, coeff_sumElim_rename_mul, abs_mul]
  exact mul_le_mul (hu _) (hv _) (abs_nonneg _) hBu

/-- **`H(U) ≤ H(U · V)`** for a non-zero integer `V` in disjoint variables — the direction the
induction step of Roth's lemma needs, and the one bean `qou-4lbh` predicted would require
Gelfond's inequality.

It requires nothing of the kind.  Choose any `j` in the support of `V`; then `coeff j V` is a
non-zero integer, so `1 ≤ |coeff j V|`, and

    |coeff i U|  ≤  |coeff i U| · |coeff j V|  =  |coeff (i ⊞ j) (U · V)|  ≤  B.

The middle step is the identity, not an estimate.  Gelfond bounds the heights of factors of a
product in *shared* variables, where the coefficients genuinely mix; in disjoint variables
they do not mix, and the bound is free. -/
theorem abs_coeff_le_of_mul_separated {u : MvPolynomial σ ℤ} {v : MvPolynomial τ ℤ}
    (hv : v ≠ 0) {B : ℤ}
    (hB : ∀ n, |coeff n ((rename Sum.inl u : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr v)| ≤ B)
    (i : σ →₀ ℕ) : |coeff i u| ≤ B := by
  classical
  obtain ⟨j, hj⟩ : v.support.Nonempty :=
    Finset.nonempty_iff_ne_empty.mpr (fun h => hv (support_eq_empty.mp h))
  have hvj : coeff j v ≠ 0 := mem_support_iff.mp hj
  have h1 : (1 : ℤ) ≤ |coeff j v| := Int.one_le_abs (by omega)
  calc |coeff i u| ≤ |coeff i u| * |coeff j v| :=
        le_mul_of_one_le_right (abs_nonneg _) h1
    _ = |coeff i u * coeff j v| := (abs_mul _ _).symm
    _ = |coeff (Finsupp.sumElim i j)
          ((rename Sum.inl u : MvPolynomial (σ ⊕ τ) ℤ) * rename Sum.inr v)| := by
        rw [coeff_sumElim_rename_mul]
    _ ≤ B := hB _

/-! ### Non-vacuity guards

The identity above would still typecheck with a wrong index convention — it would simply be a
true statement about a different coefficient.  These two examples pin it down against a case
computed by hand: `(3x²)·(5y)` has coefficient `15` at `x²y` and `0` at `x¹y`. -/

example :
    coeff (Finsupp.sumElim (Finsupp.single () 2) (Finsupp.single () 1))
      ((rename Sum.inl (C 3 * X () ^ 2 : MvPolynomial Unit ℤ) : MvPolynomial (Unit ⊕ Unit) ℤ)
        * rename Sum.inr (C 5 * X () : MvPolynomial Unit ℤ)) = 15 := by
  rw [coeff_sumElim_rename_mul, coeff_C_mul, coeff_X_pow, if_pos rfl, mul_one,
    coeff_C_mul, coeff_X', if_pos rfl, mul_one]
  norm_num

example :
    coeff (Finsupp.sumElim (Finsupp.single () 1) (Finsupp.single () 1))
      ((rename Sum.inl (C 3 * X () ^ 2 : MvPolynomial Unit ℤ) : MvPolynomial (Unit ⊕ Unit) ℤ)
        * rename Sum.inr (C 5 * X () : MvPolynomial Unit ℤ)) = 0 := by
  rw [coeff_sumElim_rename_mul, coeff_C_mul, coeff_X_pow, if_neg (by simp), mul_zero, zero_mul]

/-! ### Next

The symmetric statement `H(V) ≤ H(U · V)` for non-zero `U` is the same proof with the roles
exchanged; it is not written here because nothing yet calls for it.  Add it when something
does, rather than on speculation.

The next real step is the **height of a generalized Wronskian**, and it is now assembled
rather than open.  `mvGenWronskian D f` is a determinant whose entries are iterated `pderiv`s
of `P`, and the three pieces line up:

* `MvPolynomial.abs_coeff_pderiv_le` and `card_support_pderiv_le`
  (`QOU/Mathlib/MvGenWronskian.lean`) bound an entry's height and support size;
* `MvPolynomial.abs_coeff_det_le` (`QOU/Mathlib/MvPolynomialHeight.lean`) turns per-entry
  bounds into `m!·(S·B)^m` for the determinant;
* `abs_coeff_le_of_mul_separated` above then carries that down to each separated factor.

The composite is now written too — `abs_coeff_mvGenWronskian_le` in
`QOU/Mathlib/WronskianHeight.lean` gives `H(mvGenWronskian D f) ≤ m!·(S·(d^L·B))^m`, with the
`pderivList` iteration actually performed.  An earlier version of this note said the chain had
not been walked; it has.

⚠ What remains is **structural**: assembling the induction on the number of variables. No
further height machinery is known to be needed, but that is a prediction, not a measurement —
see bean `qou-4lbh` for why predictions from this arc deserve suspicion. -/

end MvPolynomial
