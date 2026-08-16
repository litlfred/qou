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
  | generalized Wronskians | absent |
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
import Mathlib.Algebra.Order.Ring.Rat

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

/-! ### ⚠ The definition computes the right number

`index_nonneg` and `index_add_ge` would both hold of a definition that returned `0`
everywhere, and `index_eq_top_iff` of one that returned `⊤` off the zero polynomial. None
of the lemmas above pins the *value*, so a wrong definition would satisfy all of them.

This does pin it: `X²` vanishes to order two at the origin, and the index says `2`. -/

/-- **Validation.**  At the origin with unit weights, `X²` has index exactly `2` — the
order of vanishing, as it should be. -/
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

/-! ### Next, in order

1. `index_mul_ge : index d α P + index d α Q ≤ index d α (P * Q)` — needs the support of a
   product and a minimal-multi-index argument. The one genuinely load-bearing algebraic
   property, and the reason `index` must return `⊤` at `0` rather than a junk `0`.
2. **Generalized Wronskians** — `m × m` determinants of differential operators applied to
   `m` polynomials. Mathlib's `wronskian` is the two-polynomial case only.
3. **Roth's lemma** — the induction on the number of variables. The hard core.
4. **Roth's theorem** itself, by the auxiliary-polynomial contradiction, using Mathlib's
   existing `exists_ne_zero_int_vec_norm_le` (Siegel's lemma) for the construction. -/

end MvPolynomial
