/-
  The **index of a multivariate polynomial at a point**, the first missing prerequisite
  for Thue–Siegel–Roth.

  Bean `qou-br3w`.  ⚠ **Staged here, destined for Mathlib.**  This is written in Mathlib
  style and depends on nothing from QOU, so it can be lifted out verbatim.  It lives in
  this repo only because this session cannot open a pull request against
  `leanprover-community/mathlib4` — GitHub access is scoped to `litlfred/qou`.

  ═══ WHERE THIS SITS IN ROTH'S PROOF ═══

  Roth's theorem is proved by contradiction: from too-good rational approximations one
  builds an auxiliary polynomial in `m` variables vanishing to high order at the
  approximants, then shows via **Roth's lemma** that it cannot vanish that hard.  "Vanishing
  to high order", made precise and weighted by the degrees, is the **index**.

  An inventory of Mathlib as of this writing (measured, not assumed):

  | prerequisite | status |
  |---|---|
  | Siegel's lemma | **present** — `exists_ne_zero_int_vec_norm_le` |
  | house of an algebraic number | **present** — `NumberField.house` |
  | Mahler measure | **present** |
  | Hasse derivative, `MvPolynomial.pderiv` | **present** |
  | Wronskian | present, but **two polynomials only** |
  | **index at a point** | **absent — this file** |
  | generalized Wronskians | absent in Mathlib — supplied in `QOU.Mathlib.GenWronskian`
    (univariate) and `QOU.Mathlib.MvGenWronskian` (several variables), each with the
    dependence criterion proved in **both** directions |
  | Roth's lemma, Roth's theorem | absent |

  ═══ THE DEFINITION, AND WHY IT AVOIDS DERIVATIVES ═══

  The textbook index is a minimum over multi-indices `i` with `∂ⁱP(α) ≠ 0` of `∑ᵢ iⱼ/dⱼ`.
  Formalised that way it drags in iterated partial derivatives and — outside characteristic
  zero — the factorials that make `∂ⁱ` the wrong object (one wants Hasse derivatives).

  Translating instead, `P(x + α)`, the same data is the **support** of the translated
  polynomial: the coefficient of `xⁱ` in `P(x + α)` is nonzero exactly when the `i`-th Hasse
  derivative of `P` at `α` is.  So the index is a minimum over a `Finset`, with no
  derivative and no characteristic hypothesis.

  ═══ WHY `WithTop ℚ` ═══

  The index of `0` is genuinely `⊤` — the zero polynomial vanishes to infinite order — and
  `Finset.inf` over the empty support returns `⊤` on its own.  So the total function is the
  honest one, and no `P ≠ 0` hypothesis has to be threaded through every lemma.  The
  alternative (a junk value of `0` at `P = 0`) would make `index_mul_ge` below false.
-/
import Mathlib.Algebra.MvPolynomial.Equiv
import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Algebra.Order.Ring.Rat
import Mathlib.Algebra.MvPolynomial.Division
import Mathlib.Algebra.MvPolynomial.CommRing
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.Ring.Int.Units

namespace MvPolynomial

variable {σ : Type*} {R : Type*} [CommRing R]

/-- Translate a polynomial by a point: `translate α P` is `P(x + α)`. -/
noncomputable def translate (α : σ → R) (P : MvPolynomial σ R) : MvPolynomial σ R :=
  aeval (fun j => X j + C (α j)) P

@[simp]
theorem translate_zero (α : σ → R) : translate α (0 : MvPolynomial σ R) = 0 := by
  simp [translate]

@[simp]
theorem translate_add (α : σ → R) (P Q : MvPolynomial σ R) :
    translate α (P + Q) = translate α P + translate α Q := by
  simp [translate]

@[simp]
theorem translate_mul (α : σ → R) (P Q : MvPolynomial σ R) :
    translate α (P * Q) = translate α P * translate α Q := by
  simp [translate]

/-- The **weight** of a multi-index against the degree vector `d`: `∑ⱼ iⱼ / dⱼ`. -/
noncomputable def idxWeight (d : σ → ℕ) (i : σ →₀ ℕ) : ℚ :=
  ∑ j ∈ i.support, (i j : ℚ) / (d j : ℚ)

theorem idxWeight_nonneg (d : σ → ℕ) (i : σ →₀ ℕ) : 0 ≤ idxWeight d i := by
  unfold idxWeight
  -- `positivity` does not close this: it wants `d j ≠ 0`, which is not assumed.  The
  -- statement is true regardless — `x / 0 = 0` in `ℚ` — so `div_nonneg` is the right tool.
  exact Finset.sum_nonneg fun j _ => div_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _)

@[simp]
theorem idxWeight_zero (d : σ → ℕ) : idxWeight d 0 = 0 := by simp [idxWeight]

/-- The weight is a `Finsupp.sum`, which is what makes it additive. -/
theorem idxWeight_eq_sum (d : σ → ℕ) (i : σ →₀ ℕ) :
    idxWeight d i = i.sum fun j n => (n : ℚ) / (d j : ℚ) := rfl

/-- **The weight is additive on multi-indices.**

This is the whole reason the index behaves like an order of vanishing: `∑ⱼ iⱼ/dⱼ` is linear
in `i`, so a monomial split across a product splits its weight too. -/
theorem idxWeight_add (d : σ → ℕ) (i k : σ →₀ ℕ) :
    idxWeight d (i + k) = idxWeight d i + idxWeight d k := by
  simp only [idxWeight_eq_sum]
  refine Finsupp.sum_add_index' (fun a => by simp) (fun a b₁ b₂ => ?_)
  push_cast
  rw [add_div]

/-- **The index of `P` at `α`, weighted by `d`.**

The least weight of a multi-index occurring in `P(x + α)`; `⊤` when `P = 0`, which is the
correct value rather than a convention — the zero polynomial vanishes to infinite order,
and `Finset.inf` over the empty support delivers it without a side condition. -/
noncomputable def index (d : σ → ℕ) (α : σ → R) (P : MvPolynomial σ R) : WithTop ℚ :=
  (translate α P).support.inf fun i => (idxWeight d i : WithTop ℚ)

@[simp]
theorem index_zero (d : σ → ℕ) (α : σ → R) : index d α (0 : MvPolynomial σ R) = ⊤ := by
  simp [index]

/-- The index is never negative — every multi-index has nonnegative weight. -/
theorem index_nonneg (d : σ → ℕ) (α : σ → R) (P : MvPolynomial σ R) :
    (0 : WithTop ℚ) ≤ index d α P := by
  unfold index
  refine Finset.le_inf fun i _ => ?_
  exact_mod_cast idxWeight_nonneg d i

/-- `index = ⊤` exactly for the zero polynomial: an infinite order of vanishing is not
attainable otherwise. -/
theorem index_eq_top_iff (d : σ → ℕ) (α : σ → R) {P : MvPolynomial σ R} :
    index d α P = ⊤ ↔ translate α P = 0 := by
  unfold index
  rw [Finset.inf_eq_top_iff]
  constructor
  · intro h
    by_contra hne
    obtain ⟨i, hi⟩ := support_nonempty.mpr hne
    exact (WithTop.coe_ne_top) (h i hi)
  · intro h i hi
    rw [h] at hi
    simp at hi

/-- **A lower bound is checked on the support.**  The workhorse for the estimates in Roth's
lemma: to show the index is at least `c`, show every occurring multi-index has weight at
least `c`. -/
theorem le_index_iff (d : σ → ℕ) (α : σ → R) (P : MvPolynomial σ R) (c : WithTop ℚ) :
    c ≤ index d α P ↔ ∀ i ∈ (translate α P).support, c ≤ (idxWeight d i : WithTop ℚ) := by
  unfold index
  exact ⟨fun h i hi => le_trans h (Finset.inf_le hi), fun h => Finset.le_inf h⟩

/-- **The index of a sum is at least the smaller of the two.**

Vanishing to order `a` and to order `b` gives vanishing to order `min a b`; cancellation can
only *raise* the index, never lower it, which is why this is an inequality. -/
theorem index_add_ge (d : σ → ℕ) (α : σ → R) (P Q : MvPolynomial σ R) :
    min (index d α P) (index d α Q) ≤ index d α (P + Q) := by
  classical
  rw [le_index_iff]
  intro i hi
  rw [translate_add] at hi
  -- a multi-index of the sum occurs in one of the summands
  rcases Finset.mem_union.mp (support_add hi) with h | h
  · exact le_trans (min_le_left _ _) (Finset.inf_le h)
  · exact le_trans (min_le_right _ _) (Finset.inf_le h)

/-- **The index of a product is at least the sum of the indices.**

The load-bearing algebraic property, and the reason `index` must return `⊤` at `0` rather
than a junk `0`: with a junk value this is *false*, since `index 0 + index Q = index Q`
would have to bound `index 0 = 0`.

Every monomial of `P·Q` is a sum of one from `P` and one from `Q`, and the weight is
additive — so the weight of any monomial of the product is a sum of two weights, each
bounded below by its factor's index. -/
theorem index_mul_ge (d : σ → ℕ) (α : σ → R) (P Q : MvPolynomial σ R) :
    index d α P + index d α Q ≤ index d α (P * Q) := by
  classical
  rw [le_index_iff]
  intro m hm
  rw [translate_mul] at hm
  -- `m` splits as `i + k` with `i` from `P`'s support and `k` from `Q`'s
  obtain ⟨i, hi, k, hk, rfl⟩ := Finset.mem_add.mp (support_mul _ _ hm)
  rw [idxWeight_add]
  push_cast
  exact add_le_add (Finset.inf_le hi) (Finset.inf_le hk)

/-! ### ⚠ The definition computes the right number

`index_nonneg` and `index_add_ge` would both hold of a definition that returned `0`
everywhere, and `index_eq_top_iff` of one that returned `⊤` off the zero polynomial. None
of the lemmas above pins the *value*, so a wrong definition would satisfy all of them.

This does pin it: `X²` vanishes to order two at the origin, and the index says `2`. -/

/-- **Validation.**  At the origin with unit weights, `X` has index exactly `1`. -/
theorem index_X :
    index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ)) (X 0) = (1 : ℚ) := by
  have ht : translate (fun _ : Fin 1 => (0 : ℚ)) (X 0) = (X 0 : MvPolynomial (Fin 1) ℚ) := by
    simp [translate]
  rw [index, ht, X, support_monomial]
  simp [idxWeight, Finsupp.single_apply]

/-- **Validation.**  At the origin with unit weights, `X²` has index exactly `2` — the
order of vanishing, as it should be.

Together with `index_X` this shows `index_mul_ge` is **tight** at `X · X`: the bound reads
`1 + 1 ≤ 2` and both sides are computed, not estimated. A product law that merely held
loosely would be much weaker evidence that the definition is the intended one. -/
theorem index_X_sq :
    index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ)) (X 0 ^ 2) = (2 : ℚ) := by
  have ht : translate (fun _ : Fin 1 => (0 : ℚ)) (X 0 ^ 2)
      = (X 0 ^ 2 : MvPolynomial (Fin 1) ℚ) := by
    simp [translate]
  rw [index, ht]
  rw [show ((X 0 : MvPolynomial (Fin 1) ℚ) ^ 2) = monomial (Finsupp.single 0 2) 1 by
        simp [X_pow_eq_monomial]]
  rw [support_monomial]
  simp [idxWeight, Finsupp.single_apply]

/-! ### Differentiation

Roth's lemma estimates the index of *derivatives* of the auxiliary polynomial, so the index
has to interact with `pderiv`. Because `index` is defined through the support of the
**translate**, everything of that kind rests on the commutation below. -/

/-- Translation is an algebra map, so it fixes constants. -/
@[simp]
theorem translate_C (α : σ → R) (a : R) : translate α (C a) = C a := by
  simp [translate]

/-- Translation sends `xⱼ` to `xⱼ + αⱼ` — the defining property, worth a simp lemma so the
proofs below never unfold `translate`. -/
@[simp]
theorem translate_X (α : σ → R) (j : σ) : translate α (X j) = X j + C (α j) := by
  simp [translate]

/-- **Translation commutes with partial differentiation:** `(∂ⱼP)(x + α) = ∂ⱼ(P(x + α))`.

This is the chain rule for a translation, whose Jacobian is the identity. Mathlib has no
chain rule for `aeval`, so it goes by induction on `P`; the multiplicative step is the only
one with content, and it splits on whether the differentiated variable is the multiplied
one.

⚠ **Why this is the gateway lemma.** `index` is a minimum over the support of the
*translate*, so any statement about the index of a derivative has to move `pderiv` across
`translate` before the support is visible at all. Without this, no
index-under-differentiation estimate can even be stated in terms of the definition used
here. -/
theorem translate_pderiv [DecidableEq σ] (α : σ → R) (i : σ) (P : MvPolynomial σ R) :
    translate α (pderiv i P) = pderiv i (translate α P) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq]
  | mul_X p j hp =>
    by_cases h : i = j
    · subst h
      simp only [Derivation.leibniz, smul_eq_mul, pderiv_X_self, mul_one, translate_add,
        translate_mul, translate_X, map_add, pderiv_C, add_zero, hp]
    · simp only [Derivation.leibniz, smul_eq_mul, pderiv_X_of_ne (Ne.symm h), mul_zero,
        zero_add, translate_mul, translate_X, map_add, pderiv_C, add_zero, hp]

/-! ### The index under differentiation

The estimate Roth's lemma runs on: differentiating once costs at most `1/dⱼ` of index. -/

/-- The support of a derivative sits inside the shift of the support by `-eⱼ`. -/
theorem support_pderiv_subset [DecidableEq σ] (i : σ) (P : MvPolynomial σ R) :
    (pderiv i P).support ⊆ P.support.image (fun s => s - Finsupp.single i 1) := by
  classical
  have hP : P = ∑ v ∈ P.support, monomial v (coeff v P) :=
    (support_sum_monomial_coeff P).symm
  intro t ht
  rw [hP, map_sum] at ht
  have hb := support_sum ht
  simp only [Finset.mem_biUnion] at hb
  obtain ⟨v, hv, htv⟩ := hb
  rw [pderiv_monomial] at htv
  have h1 : t = v - Finsupp.single i 1 := by
    have := support_monomial_subset htv
    simpa using this
  exact Finset.mem_image.mpr ⟨v, hv, h1.symm⟩

theorem idxWeight_single (d : σ → ℕ) (i : σ) (n : ℕ) :
    idxWeight d (Finsupp.single i n) = (n : ℚ) / (d i : ℚ) := by
  rw [idxWeight_eq_sum]
  exact Finsupp.sum_single_index (by simp)

/-- When the variable does not occur, truncated subtraction is the identity. -/
theorem sub_single_of_eq_zero [DecidableEq σ] {s : σ →₀ ℕ} {i : σ} (h : s i = 0) :
    s - Finsupp.single i 1 = s := by
  ext j
  by_cases hj : j = i
  · subst hj; simp [h]
  · simp [Ne.symm hj]

/-- **The weight drops by at most `1/dᵢ` under one differentiation.**

⚠ **This must be an inequality, and that is what makes it easy.** The `ℕ`-subtraction on
`σ →₀ ℕ` is truncated, so `s - eᵢ = s` exactly when `sᵢ = 0`, and there the *equality*
`idxWeight (s - eᵢ) = idxWeight s - 1/dᵢ` is plainly false. Stated as `≤` the degenerate
case costs nothing, because `1/dᵢ ≥ 0` makes the bound slack rather than tight. -/
theorem idxWeight_le_sub_single_add [DecidableEq σ] (d : σ → ℕ) (s : σ →₀ ℕ) (i : σ) :
    idxWeight d s ≤ idxWeight d (s - Finsupp.single i 1) + 1 / (d i : ℚ) := by
  by_cases h : Finsupp.single i 1 ≤ s
  · refine le_of_eq ?_
    have hcancel : s - Finsupp.single i 1 + Finsupp.single i 1 = s := tsub_add_cancel_of_le h
    calc idxWeight d s
        = idxWeight d (s - Finsupp.single i 1 + Finsupp.single i 1) := by rw [hcancel]
      _ = idxWeight d (s - Finsupp.single i 1) + idxWeight d (Finsupp.single i 1) :=
          idxWeight_add _ _ _
      _ = idxWeight d (s - Finsupp.single i 1) + 1 / (d i : ℚ) := by
          rw [idxWeight_single]; norm_num
  · have hzero : s i = 0 := by
      rw [Finsupp.single_le_iff] at h
      omega
    rw [sub_single_of_eq_zero hzero]
    exact le_add_of_nonneg_right (div_nonneg zero_le_one (Nat.cast_nonneg _))

/-- **The index drops by at most `1/dⱼ` under one differentiation.**

The `⊤` case is not a technicality to be routed around: when `∂ⱼP = 0` the right-hand side
is `⊤` and the bound is free, which is exactly the behaviour the `WithTop` return type was
chosen for at the top of this file. -/
theorem index_le_index_pderiv_add [DecidableEq σ] (d : σ → ℕ) (α : σ → R) (j : σ)
    (P : MvPolynomial σ R) :
    index d α P ≤ index d α (pderiv j P) + ((1 / (d j : ℚ) : ℚ) : WithTop ℚ) := by
  classical
  have htr : translate α (pderiv j P) = pderiv j (translate α P) := translate_pderiv α j P
  by_cases hemp : (pderiv j (translate α P)).support = ∅
  · have htop : index d α (pderiv j P) = ⊤ := by
      rw [index, htr, hemp, Finset.inf_empty]
    rw [htop, top_add]
    exact le_top
  · have hne : (pderiv j (translate α P)).support.Nonempty :=
      Finset.nonempty_of_ne_empty hemp
    obtain ⟨t, ht, hinf⟩ :=
      Finset.exists_mem_eq_inf _ hne (fun m => ((idxWeight d m : ℚ) : WithTop ℚ))
    have hidx : index d α (pderiv j P) = ((idxWeight d t : ℚ) : WithTop ℚ) := by
      rw [index, htr]; exact hinf
    obtain ⟨s, hs, hst⟩ :=
      Finset.mem_image.mp (support_pderiv_subset j (translate α P) ht)
    have hweight : idxWeight d s ≤ idxWeight d t + 1 / (d j : ℚ) := by
      rw [← hst]; exact idxWeight_le_sub_single_add d s j
    calc index d α P ≤ ((idxWeight d s : ℚ) : WithTop ℚ) := by
          rw [index]; exact Finset.inf_le hs
      _ ≤ ((idxWeight d t + 1 / (d j : ℚ) : ℚ) : WithTop ℚ) := by exact_mod_cast hweight
      _ = ((idxWeight d t : ℚ) : WithTop ℚ) + ((1 / (d j : ℚ) : ℚ) : WithTop ℚ) := by
          rw [WithTop.coe_add]
      _ = index d α (pderiv j P) + ((1 / (d j : ℚ) : ℚ) : WithTop ℚ) := by rw [hidx]

/-- **The iterated bound:** `k` differentiations in one variable cost at most `k/dⱼ`. -/
theorem index_le_index_iterate_pderiv_add [DecidableEq σ] (d : σ → ℕ) (α : σ → R) (j : σ)
    (k : ℕ) (P : MvPolynomial σ R) :
    index d α P ≤ index d α ((pderiv j)^[k] P) + (((k : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ) := by
  induction k generalizing P with
  | zero => simp
  | succ n ih =>
    have hstep := index_le_index_pderiv_add d α j P
    have hih := ih (pderiv j P)
    have hsplit : (((n : ℚ) + 1) / (d j : ℚ) : ℚ) = (n : ℚ) / (d j : ℚ) + 1 / (d j : ℚ) := by
      rw [add_div]
    calc index d α P
        ≤ index d α (pderiv j P) + ((1 / (d j : ℚ) : ℚ) : WithTop ℚ) := hstep
      _ ≤ (index d α ((pderiv j)^[n] (pderiv j P))
            + (((n : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ))
            + ((1 / (d j : ℚ) : ℚ) : WithTop ℚ) := by gcongr
      _ = index d α ((pderiv j)^[n + 1] P)
            + ((((n : ℚ) + 1) / (d j : ℚ) : ℚ) : WithTop ℚ) := by
          rw [← Function.iterate_succ_apply, hsplit, WithTop.coe_add, add_assoc]
      _ = index d α ((pderiv j)^[n + 1] P)
            + ((((n + 1 : ℕ) : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ) := by push_cast; ring_nf

/-! ### Bounding the index from BELOW

Every result above bounds the index from above.  Roth's lemma also needs the other
direction: its auxiliary polynomial is *constructed* to vanish to high order, and the index
is what that construction buys. -/

/-- A single term is at most the whole weight, since every term is non-negative. -/
theorem le_idxWeight (d : σ → ℕ) (i : σ →₀ ℕ) (j : σ) :
    (i j : ℚ) / (d j : ℚ) ≤ idxWeight d i := by
  classical
  by_cases hj : i j = 0
  · rw [hj]
    simpa using idxWeight_nonneg d i
  · exact Finset.single_le_sum (f := fun j' => (i j' : ℚ) / (d j' : ℚ))
      (fun j' _ => div_nonneg (Nat.cast_nonneg _) (Nat.cast_nonneg _))
      (Finsupp.mem_support_iff.mpr hj)

/-- **High-order vanishing in one variable forces a lower bound on the index.** -/
theorem le_index_of_forall_le_support (d : σ → ℕ) (α : σ → R) (P : MvPolynomial σ R)
    (j : σ) (k : ℕ) (h : ∀ i ∈ (translate α P).support, k ≤ i j) :
    (((k : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ) ≤ index d α P := by
  rw [le_index_iff]
  intro i hi
  -- ⚠ `gcongr` leaves this side goal because `h i hi` is not a local hypothesis; in
  -- `le_index_of_X_pow_dvd_translate` below the analogous fact *is* in context and `gcongr`
  -- discharges it itself, so the follow-up must be omitted there.  Both spellings are
  -- correct in their own context and copying either into the other fails.
  have hstep : (k : ℚ) / (d j : ℚ) ≤ (i j : ℚ) / (d j : ℚ) := by
    gcongr
    exact_mod_cast h i hi
  exact_mod_cast le_trans hstep (le_idxWeight d i j)

/-! ### Divisibility, support, and the index -/

/-- Divisibility by a monomial is a condition on the support. -/
theorem monomial_one_dvd_iff_support {s : σ →₀ ℕ} {x : MvPolynomial σ R} :
    monomial s (1 : R) ∣ x ↔ ∀ i ∈ x.support, s ≤ i := by
  rw [monomial_one_dvd_iff_modMonomial_eq_zero]
  constructor
  · intro h i hi
    by_contra hle
    rw [mem_support_iff] at hi
    exact hi (by rw [← coeff_modMonomial_of_not_le x hle, h, coeff_zero])
  · intro h
    ext i
    by_cases hle : s ≤ i
    · rw [coeff_modMonomial_of_le x hle, coeff_zero]
    · rw [coeff_modMonomial_of_not_le x hle, coeff_zero]
      by_contra hne
      exact hle (h i (mem_support_iff.mpr hne))

/-- **Divisibility by a power of a variable, as a support condition.**

Mathlib has the univariate `Polynomial.X_pow_dvd_iff`; multivariately it has only
`X_dvd_iff_modMonomial_eq_zero`, the first-power case. -/
theorem X_pow_dvd_iff_support {j : σ} {k : ℕ} {x : MvPolynomial σ R} :
    (X j : MvPolynomial σ R) ^ k ∣ x ↔ ∀ i ∈ x.support, k ≤ i j := by
  rw [X_pow_eq_monomial, monomial_one_dvd_iff_support]
  exact forall_congr' fun i => forall_congr' fun _ => Finsupp.single_le_iff

/-- The index lower bound, phrased as divisibility of the translate. -/
theorem le_index_of_X_pow_dvd_translate (d : σ → ℕ) (α : σ → R) (P : MvPolynomial σ R)
    (j : σ) (k : ℕ) (h : (X j : MvPolynomial σ R) ^ k ∣ translate α P) :
    (((k : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ) ≤ index d α P := by
  rw [X_pow_dvd_iff_support] at h
  exact le_index_of_forall_le_support d α P j k h

/-! ### Transport along a renaming

Reindexing the variables does not change the index, provided the weights and the base point
are transported with them.  This is what lets a result proved for one variable type be used
at another — and it subsumes the two injection-specific lemmas in
`QOU/Mathlib/SeparatedIndex.lean`, which are now derived from it. -/

/-- Translating after an injective renaming is renaming after translating by the pulled-back
point.  The variables outside the image never see `α`. -/
theorem translate_rename_of_injective {τ : Type*} (f : σ → τ) (α : τ → R)
    (P : MvPolynomial σ R) :
    translate α (rename f P) = rename f (translate (α ∘ f) P) := by
  induction P using MvPolynomial.induction_on with
  | C a => simp [translate]
  | add p q hp hq => simp only [map_add, translate_add, hp, hq]
  | mul_X p i hp =>
      rw [map_mul, rename_X, translate_mul, translate_mul, translate_X, translate_X, hp,
        map_mul, map_add, rename_X, rename_C]
      rfl

/-- Pushing a multi-index forward along an injection and weighting by `d` is weighting by
`d ∘ f`: injectivity is what keeps the support sum term-for-term. -/
theorem idxWeight_mapDomain_of_injective {τ : Type*} [DecidableEq τ] (f : σ → τ)
    (hf : Function.Injective f) (d : τ → ℕ) (i : σ →₀ ℕ) :
    idxWeight d (Finsupp.mapDomain f i) = idxWeight (d ∘ f) i := by
  classical
  unfold idxWeight
  rw [Finsupp.mapDomain_support_of_injective hf, Finset.sum_image (fun a _ b _ h => hf h)]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Finsupp.mapDomain_apply hf]
  rfl

/-- **The index is invariant under an injective renaming**, with the weights and base point
transported. -/
theorem index_rename_of_injective {τ : Type*} [DecidableEq τ] (f : σ → τ)
    (hf : Function.Injective f) (d : τ → ℕ) (α : τ → R) (P : MvPolynomial σ R) :
    index d α (rename f P) = index (d ∘ f) (α ∘ f) P := by
  classical
  unfold index
  rw [translate_rename_of_injective, support_rename_of_injective hf, Finset.inf_image]
  refine congrArg (Finset.inf (translate (α ∘ f) P).support) ?_
  refine _root_.funext fun i => ?_
  simp only [Function.comp_apply, idxWeight_mapDomain_of_injective f hf d i]

/-- **Transport along an equivalence.**  A corollary of `index_rename_of_injective`, and the
lemma that makes reindexing the variable *type* cheap.

Three lines.  That matters for a design decision: an `m`-indexed formulation of Roth's lemma
needs `Fin (m+1) ≃ Unit ⊕ Fin m` transport to meet the `σ ⊕ τ` machinery, and this is that
transport for the index side.  The height side is free — Mathlib's `coeff_rename_mapDomain`
already matches coefficients across a renaming. -/
theorem index_rename_equiv {τ : Type*} [DecidableEq τ] (e : σ ≃ τ) (d : τ → ℕ) (α : τ → R)
    (P : MvPolynomial τ R) :
    index d α P = index (d ∘ e) (α ∘ e) (rename e.symm P) := by
  classical
  have h := index_rename_of_injective (e : σ → τ) e.injective d α (rename e.symm P)
  rwa [rename_rename, Equiv.self_comp_symm, rename_id_apply] at h

/-! ### Rescaling the degree vector

⚠ These exist because of a gap identified in `QOU/Mathlib/RothInductionStep.lean`: the
classical proof of Roth's lemma measures a *Wronskian's* index against the **Wronskian's own**
degree vector, while every other statement in this arc uses one degree vector throughout.

`degreeOf_mvGenWronskian_le` says a generalized Wronskian of `r` functions of degree `≤ d`
has degree `≤ r · d`, so the scale factor is exactly `r`.  These three lemmas are what let
that rescaling be expressed and moved across.

⚠ They make the rescaling **expressible**.  They do **not** by themselves establish that the
error term in the induction step becomes small — that is the recursion's arithmetic, and it is
not done. -/

/-- **Scaling the degree vector scales the weight inversely.**

No hypothesis on `c`: at `c = 0` both sides are `0`, since `x / 0 = 0` in `ℚ`. -/
theorem idxWeight_scale_degree (c : ℕ) (d : σ → ℕ) (i : σ →₀ ℕ) :
    idxWeight (fun j => c * d j) i = idxWeight d i / (c : ℚ) := by
  unfold idxWeight
  rw [div_eq_mul_inv, Finset.sum_mul]
  refine Finset.sum_congr rfl fun j _ => ?_
  push_cast
  rw [mul_comm (c : ℚ) (d j : ℚ), ← div_div, div_eq_mul_inv]

/-- **Lower bounds transport across a rescaling:** `θ ≤ index_{c·d} P ↔ c·θ ≤ index_d P`.

Stated as an iff on bounds rather than as `index_{c·d} = index_d / c`, because `WithTop ℚ` has
no usable division and `⊤` must be handled. -/
theorem le_index_scale_degree_iff {c : ℕ} (hc : c ≠ 0) (d : σ → ℕ) (α : σ → R)
    (P : MvPolynomial σ R) (θ : ℚ) :
    ((θ : ℚ) : WithTop ℚ) ≤ index (fun j => c * d j) α P
      ↔ (((c : ℚ) * θ : ℚ) : WithTop ℚ) ≤ index d α P := by
  have hcQ : (0 : ℚ) < (c : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hc
  rw [le_index_iff, le_index_iff]
  refine forall_congr' fun i => forall_congr' fun _ => ?_
  rw [idxWeight_scale_degree, WithTop.coe_le_coe, WithTop.coe_le_coe, le_div_iff₀ hcQ,
    mul_comm θ (c : ℚ)]

/-- **Upper bounds transport across a rescaling:** `index_{c·d} P ≤ θ ↔ index_d P ≤ c·θ`.

This is the direction the induction *hypothesis* is used in — it supplies upper bounds on the
factors' indices, which have to be converted out of the rescaled weights.

The proof goes through `Finset.inf_le_iff`, which needs the bound to be below `⊤`; a coerced
rational always is. -/
theorem index_scale_degree_le_iff {c : ℕ} (hc : c ≠ 0) (d : σ → ℕ) (α : σ → R)
    (P : MvPolynomial σ R) (θ : ℚ) :
    index (fun j => c * d j) α P ≤ ((θ : ℚ) : WithTop ℚ)
      ↔ index d α P ≤ (((c : ℚ) * θ : ℚ) : WithTop ℚ) := by
  have hcQ : (0 : ℚ) < (c : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hc
  unfold index
  rw [Finset.inf_le_iff (WithTop.coe_lt_top _), Finset.inf_le_iff (WithTop.coe_lt_top _)]
  refine exists_congr fun i => and_congr_right fun _ => ?_
  rw [idxWeight_scale_degree, WithTop.coe_le_coe, WithTop.coe_le_coe, div_le_iff₀ hcQ,
    mul_comm (c : ℚ) θ]

/-! ### Sums, products and determinants

The index counterparts of the height bounds in `QOU/Mathlib/MvPolynomialHeight.lean`, and
what the generalized-Wronskian estimate needs.  Note the direction: heights are bounded from
**above** by their parts, indices from **below** — vanishing to high order is preserved by
sums and *added* by products, so every statement here is a lower bound. -/

/-- **The index of a finite sum is at least the least index of a summand.**  The `Finset`
form of `index_add_ge`; the empty sum is `0`, whose index is `⊤`, matching `Finset.inf_empty`
with no side condition. -/
theorem index_sum_ge {ι : Type*} (d : σ → ℕ) (α : σ → R) (s : Finset ι)
    (F : ι → MvPolynomial σ R) :
    s.inf (fun i => index d α (F i)) ≤ index d α (∑ i ∈ s, F i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.inf_insert]
      exact le_trans (min_le_min le_rfl ih) (index_add_ge d α _ _)

/-- **The index of a finite product is at least the sum of the indices.**  The `Finset` form
of `index_mul_ge`; the empty product is `1`, and `0 ≤ index d α 1` is `index_nonneg`. -/
theorem index_prod_ge {ι : Type*} (d : σ → ℕ) (α : σ → R) (s : Finset ι)
    (F : ι → MvPolynomial σ R) :
    ∑ i ∈ s, index d α (F i) ≤ index d α (∏ i ∈ s, F i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using index_nonneg d α (1 : MvPolynomial σ R)
  | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.prod_insert ha]
      exact le_trans (add_le_add le_rfl ih) (index_mul_ge d α _ _)

/-- Scaling by a unit of `ℤ` — the only scalars the Leibniz expansion produces — leaves the
index alone. -/
theorem index_smul_units (d : σ → ℕ) (α : σ → R) (u : ℤˣ) (P : MvPolynomial σ R) :
    index d α (u • P) = index d α P := by
  rcases Int.units_eq_one_or u with h | h
  · rw [h, one_smul]
  · -- ⚠ `simp [index, translate]` closes this only with a wider import closure than this
    -- file has; spelled out so it does not depend on what happens to be imported.
    rw [h, Units.smul_def, Units.val_neg, Units.val_one, neg_smul, one_smul]
    unfold index translate
    rw [map_neg, support_neg]

/-- Multiplying by a non-zero constant does not change the support. -/
theorem support_C_mul [NoZeroDivisors R] {c : R} (hc : c ≠ 0) (P : MvPolynomial σ R) :
    (C c * P).support = P.support := by
  ext i
  simp [mem_support_iff, coeff_C_mul, hc]

/-- **Rescaling the polynomial does not move its index.**

`index_smul_units` says this for `ℤˣ`; this says it for any non-zero constant over a domain,
which is what a determinant of derivatives needs — a generalized Wronskian of powers is
always a *scalar multiple* of a monomial, and the scalar is an accident of the differentiation
rather than part of the vanishing behaviour. -/
theorem index_C_mul [NoZeroDivisors R] (d : σ → ℕ) (α : σ → R) {c : R} (hc : c ≠ 0)
    (P : MvPolynomial σ R) : index d α (C c * P) = index d α P := by
  rw [index, index, translate_mul, translate_C, support_C_mul hc]

/-- **The index of a determinant is at least the least permutation-sum of entry indices.**

Leibniz plus the two lemmas above: the determinant is a sum over permutations, so
`index_sum_ge` takes the least term; each term is a unit times a product, so `index_smul_units`
discards the sign and `index_prod_ge` adds the entries' indices.

This is what bounds the index of a generalized Wronskian from below in terms of the indices
of the differentiated entries — the estimate Roth's lemma runs on.  ⚠ It says nothing about
the *entries* themselves; relating `index (pderivList D (f j))` back to `index (f j)` is
`index_le_index_iterate_pderiv_add` above, and that is where the differentiation cost enters. -/
theorem index_det_ge {ι : Type*} [Fintype ι] [DecidableEq ι] (d : σ → ℕ) (α : σ → R)
    (M : Matrix ι ι (MvPolynomial σ R)) :
    (Finset.univ : Finset (Equiv.Perm ι)).inf
        (fun p => ∑ i : ι, index d α (M (p i) i))
      ≤ index d α M.det := by
  classical
  rw [Matrix.det_apply]
  refine le_trans ?_ (index_sum_ge d α Finset.univ _)
  refine Finset.le_inf ?_
  intro p _
  refine le_trans (Finset.inf_le (Finset.mem_univ p)) ?_
  rw [index_smul_units]
  exact index_prod_ge d α Finset.univ _

/-! ### Next, in order

1. ~~`index_mul_ge`~~ — **done**, above.
2. ~~**Generalized Wronskians**~~ — **done, both directions**.  Univariate:
   `genWronskian_eq_zero_iff` in `QOU.Mathlib.GenWronskian`.  Several variables:
   `linearIndependent_iff_exists_mvGenWronskian_ne_zero` in `QOU.Mathlib.MvGenWronskian`.
3. ~~**The index under differentiation**~~ — **done**, `index_le_index_pderiv_add` and its
   iterate above.

   ⚠ **The earlier note here predicted the wrong difficulty.** It said the statement "is
   rescued only because `pderiv_monomial` carries a factor `sᵢ` that kills exactly those
   monomials" with `sᵢ = 0`. No such rescue was needed: `support_pderiv_subset` filters
   nothing, and the degenerate case is free because the statement is an *inequality* —
   when `sᵢ = 0` truncated subtraction gives `s - eᵢ = s` and the `+1/dᵢ` is simply slack.
   Reaching for the sharper equality is what would have forced the filter.
4. **Roth's lemma** — the induction on the number of variables. The hard core, and the one
   step where no part of it is bookkeeping.

   What is now in place for it: the index and its product law, both generalized-Wronskian
   criteria in full, and the differentiation estimate above.

   ⚠ What is *not*, and is easy to overlook: Roth's lemma needs the operator family to have
   **bounded order**, and `exists_mvGenWronskian_ne_zero` produces one from arbitrary
   multi-indices with no such bound.  Supplying the bound is where the degree hypotheses on
   the auxiliary polynomial enter — a real step, not bookkeeping.  Then the induction
   itself.
5. **Roth's theorem** itself, by the auxiliary-polynomial contradiction, using Mathlib's
   existing `exists_ne_zero_int_vec_norm_le` (Siegel's lemma) for the construction. -/

end MvPolynomial
