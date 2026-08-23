/-
  **The index across a disjoint-variable product** — the index analogue of
  `QOU/Mathlib/SeparatedHeight.lean`, and the piece Roth's induction splits on.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/RothIndex.lean` (for `index`, `idxWeight`,
  `translate`) and `QOU/Mathlib/SeparatedHeight.lean` (for `coeff_sumElim_rename_mul`).  Both
  of those are Mathlib-only, so the three lift together, but `index` is not a Mathlib notion.

  ═══ THE RESULT ═══

      index (U(x) · V(y))  =  index U  +  index V

  exactly, for disjoint variable groups, weights and base point split accordingly.

  This is what the induction on the number of variables in Roth's lemma rests on.  The
  separated Wronskian factors as `W = U(x)·V(y)` (`det_separated_wronskian` in
  `SeparatedWronskian.lean`); the induction hypothesis bounds `index U` and `index V`
  separately; and the equality is what converts those two bounds into a bound on `index W`.
  Without it the recursion has nothing to recurse on.

  ═══ ⚠ WHERE `IsDomain` DOES REAL WORK ═══

  The two directions are not equally cheap, and only one of them needs a domain.

  * **`≥`** is `RothIndex.index_mul_ge` — true over any `CommRing` — together with the
    rename-invariance lemmas below.  Nothing new.
  * **`≤`** is the new content, and it is **false in general without `IsDomain`.**  The proof
    picks multi-indices `i₀, j₀` realising each index and needs `i₀ ⊞ j₀` to actually occur in
    the product.  Its coefficient there is exactly `coeff i₀ (translate α U) · coeff j₀ (translate β V)`
    (`coeff_sumElim_rename_mul`), a product of two non-zero elements — which can only be
    concluded non-zero in a domain.  Over a ring with zero divisors that monomial can cancel,
    the realising index need not occur, and the inequality can be strict.

  So the equality is not a formality: `index_mul_ge` already gave half of it for free, and the
  half that costs something is precisely the half that constrains the coefficient ring.
-/
import QOU.Mathlib.RothIndex
import QOU.Mathlib.SeparatedHeight

namespace MvPolynomial

variable {σ τ R : Type*} [CommRing R]

/-! ### Translation commutes with the variable injections -/

/-- Translating by `Sum.elim α β` and injecting on the left is injecting and translating by
`α`: the `β` half never sees a variable of `U`. -/
theorem translate_rename_inl (α : σ → R) (β : τ → R) (U : MvPolynomial σ R) :
    translate (Sum.elim α β) (rename Sum.inl U : MvPolynomial (σ ⊕ τ) R)
      = rename Sum.inl (translate α U) := by
  induction U using MvPolynomial.induction_on with
  | C a => simp [translate]
  | add p q hp hq => rw [map_add, translate_add, translate_add, hp, hq, map_add]
  | mul_X p i hp =>
      rw [map_mul, translate_mul, translate_mul, hp, rename_X, translate_X, translate_X,
        map_mul, map_add, rename_X, rename_C]
      rfl

/-- The right-hand counterpart of `translate_rename_inl`. -/
theorem translate_rename_inr (α : σ → R) (β : τ → R) (V : MvPolynomial τ R) :
    translate (Sum.elim α β) (rename Sum.inr V : MvPolynomial (σ ⊕ τ) R)
      = rename Sum.inr (translate β V) := by
  induction V using MvPolynomial.induction_on with
  | C a => simp [translate]
  | add p q hp hq => rw [map_add, translate_add, translate_add, hp, hq, map_add]
  | mul_X p i hp =>
      rw [map_mul, translate_mul, translate_mul, hp, rename_X, translate_X, translate_X,
        map_mul, map_add, rename_X, rename_C]
      rfl

/-! ### The weight is additive across the split -/

/-- **`idxWeight` is additive on `Finsupp.sumElim`.**  The support of `sumElim i j` is the
disjoint sum of the two supports, so the defining sum splits with no overlap — this is the
combinatorial reason the index is *exactly* additive rather than merely superadditive. -/
theorem idxWeight_sumElim (d₁ : σ → ℕ) (d₂ : τ → ℕ) (i : σ →₀ ℕ) (j : τ →₀ ℕ) :
    idxWeight (Sum.elim d₁ d₂) (Finsupp.sumElim i j)
      = idxWeight d₁ i + idxWeight d₂ j := by
  classical
  unfold idxWeight
  rw [Finsupp.sumElim_support, Finset.sum_disjSum]
  rfl

/-! ### The index is invariant under the injections -/

/-- Injecting `U` into the larger variable set does not change its index.

Now a one-line specialisation of `index_rename_of_injective` in `RothIndex.lean`.  An earlier
version of this module proved it directly; deriving it instead is the check that the general
transport lemma really does subsume the injection-specific ones. -/
theorem index_rename_inl (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → R) (β : τ → R)
    (U : MvPolynomial σ R) :
    index (Sum.elim d₁ d₂) (Sum.elim α β) (rename Sum.inl U : MvPolynomial (σ ⊕ τ) R)
      = index d₁ α U := by
  classical
  exact index_rename_of_injective Sum.inl Sum.inl_injective _ _ _

/-- The right-hand counterpart of `index_rename_inl`. -/
theorem index_rename_inr (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → R) (β : τ → R)
    (V : MvPolynomial τ R) :
    index (Sum.elim d₁ d₂) (Sum.elim α β) (rename Sum.inr V : MvPolynomial (σ ⊕ τ) R)
      = index d₂ β V := by
  classical
  exact index_rename_of_injective Sum.inr Sum.inr_injective _ _ _

/-! ### The index is exactly additive across a disjoint-variable product -/

/-- **`index (U(x)·V(y)) = index U + index V`** for disjoint variable groups, over a domain.

The `≥` half is `index_mul_ge` plus the rename-invariance above, and holds over any
`CommRing`.  The `≤` half is the new content and is where `IsDomain` is used: it picks
multi-indices realising each index and needs their combination to occur in the product, whose
coefficient there is a product of two non-zero elements.  See the module header — over a ring
with zero divisors that monomial can cancel and the inequality can be strict.

`⊤` is handled by the same argument rather than by a special case: if `translate α U = 0` then
the left side is `⊤` and so is the right, since `⊤ + x = ⊤`. -/
theorem index_separated [IsDomain R] (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → R) (β : τ → R)
    (U : MvPolynomial σ R) (V : MvPolynomial τ R) :
    index (Sum.elim d₁ d₂) (Sum.elim α β)
        ((rename Sum.inl U : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr V)
      = index d₁ α U + index d₂ β V := by
  classical
  refine le_antisymm ?_ ?_
  · rcases eq_or_ne (translate α U) 0 with hU0 | hU
    · rw [(index_eq_top_iff d₁ α).mpr hU0, top_add]
      exact le_top
    rcases eq_or_ne (translate β V) 0 with hV0 | hV
    · rw [(index_eq_top_iff d₂ β).mpr hV0, add_top]
      exact le_top
    have hUs : (translate α U).support.Nonempty := support_nonempty.mpr hU
    have hVs : (translate β V).support.Nonempty := support_nonempty.mpr hV
    obtain ⟨i₀, hi₀, hieq⟩ := Finset.exists_mem_eq_inf _ hUs
      (fun i => (idxWeight d₁ i : WithTop ℚ))
    obtain ⟨j₀, hj₀, hjeq⟩ := Finset.exists_mem_eq_inf _ hVs
      (fun j => (idxWeight d₂ j : WithTop ℚ))
    have hmem : Finsupp.sumElim i₀ j₀ ∈
        (translate (Sum.elim α β)
          ((rename Sum.inl U : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr V)).support := by
      rw [translate_mul, translate_rename_inl, translate_rename_inr, mem_support_iff,
        coeff_sumElim_rename_mul]
      -- ⚠ the only use of `IsDomain`: a product of two non-zero coefficients is non-zero.
      exact mul_ne_zero (mem_support_iff.mp hi₀) (mem_support_iff.mp hj₀)
    refine le_trans (Finset.inf_le hmem) ?_
    rw [idxWeight_sumElim, WithTop.coe_add]
    unfold index
    rw [hieq, hjeq]
  · rw [← index_rename_inl d₁ d₂ α β U, ← index_rename_inr d₁ d₂ α β V]
    exact index_mul_ge _ _ _ _

/-! ### Validation

`RothIndex.lean` pins the *value* of `index` on `X` and `X²` rather than trusting its
properties, on the grounds that a wrong definition would satisfy all the structural lemmas.
The same applies here: `index_separated` is symmetric-looking, and with `σ = τ` a version that
attached `d₁` to the wrong factor would still typecheck.

The example below distinguishes them.  It uses **different weights on the two sides** — `1` on
the left, `2` on the right — with `X` on the left and `X²` on the right, giving `1 + 1 = 2`.
Had the weights been attached to the wrong factors the value would be `1/2 + 2 = 5/2`. -/

theorem index_X_sq_weight_two :
    index (fun _ : Fin 1 => 2) (fun _ : Fin 1 => (0 : ℚ)) (X 0 ^ 2) = (1 : ℚ) := by
  have ht : translate (fun _ : Fin 1 => (0 : ℚ)) (X 0 ^ 2)
      = (X 0 ^ 2 : MvPolynomial (Fin 1) ℚ) := by
    simp [translate]
  rw [index, ht]
  rw [show ((X 0 : MvPolynomial (Fin 1) ℚ) ^ 2) = monomial (Finsupp.single 0 2) 1 by
        simp [X_pow_eq_monomial]]
  rw [support_monomial]
  norm_num [idxWeight, Finsupp.support_single_ne_zero, Finsupp.single_apply]

example :
    index (Sum.elim (fun _ : Fin 1 => 1) (fun _ : Fin 1 => 2))
        (Sum.elim (fun _ : Fin 1 => (0 : ℚ)) (fun _ : Fin 1 => (0 : ℚ)))
        ((rename Sum.inl (X 0) : MvPolynomial (Fin 1 ⊕ Fin 1) ℚ)
          * rename Sum.inr (X 0 ^ 2))
      = (2 : ℚ) := by
  rw [index_separated, index_X, index_X_sq_weight_two, ← WithTop.coe_add]
  norm_num

/-! ### Next

With this and `QOU/Mathlib/WronskianHeight.lean`, both halves the induction splits on — index
and height — are exactly additive/controlled across the separated factorization.

⚠ What remains is the **statement of Roth's lemma itself** and the recursion: the parameter
bookkeeping (`dⱼ/dⱼ₊₁` growth, `ε`, the `qⱼ` conditions) and the argument that feeds the `m = 1`
case (`RothHeightBound.lean`) and the `m−1` case back into the `m` case.  That is where the
remaining work is, and none of it is index or height machinery. -/

end MvPolynomial
