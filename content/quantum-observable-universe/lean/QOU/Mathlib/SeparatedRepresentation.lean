/-
  **Separated representations** — every polynomial in two variable groups is a finite sum
  `∑ₖ φₖ(x)·ψₖ(y)`.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/SeparatedHeight.lean` for
  `sumElim_eq_mapDomain_add` and `eq_sumElim`.

  ═══ THE AUDIT FOUND THIS MISSING ═══

  Now that Roth's lemma has a statement (`QOU/Mathlib/RothLemmaStatement.lean`), its
  hypotheses can be matched against named theorems.  Doing that for the induction step: the
  separated machinery — `RothInductionStep`, `SeparatedIndex`, `SeparatedHeight`,
  `det_separated_wronskian` — all *takes* a separated representation
  `∑ₖ rename inl (φ k) * rename inr (ψ k)` as given, and **nothing in the corpus produced
  one.**  Checked by grep before writing: no `exists_separated…` of any kind.

  ═══ ⚠ WHAT THIS GIVES, AND WHAT IT DOES NOT ═══

  `exists_separated_representation_monomial` gives a representation whose `φ` are **distinct
  monomials**, hence linearly independent (`linearIndependent_monomial`).  That is the half
  the bounded-order Wronskian criterion needs on the `x` side.

  ⚠ It does **not** give independent `ψ`.  Roth's lemma's induction wants a *minimal-length*
  representation, in which **both** families are independent; extracting one is a rank
  argument and is **not here**.

  ⚠ It is also indexed by a `Finset (σ →₀ ℕ)`, while `det_separated_wronskian` wants
  `Fin r → _`.  Bridging is `Finset.equivFin`, and is likewise not written.

  Both gaps are small and mechanical next to the recursion itself, but they are gaps: this
  module is **not** a drop-in for the induction step.
-/
import QOU.Mathlib.SeparatedHeight
import Mathlib.RingTheory.MvPolynomial.Basic

namespace MvPolynomial

variable {σ τ R : Type*} [CommRing R]

/-- A monomial on `σ ⊕ τ` splits as a product, with the coefficient on the left factor. -/
theorem monomial_sumElim_eq (i : σ →₀ ℕ) (j : τ →₀ ℕ) (c : R) :
    monomial (Finsupp.sumElim i j) c
      = (rename Sum.inl (monomial i c) : MvPolynomial (σ ⊕ τ) R)
        * rename Sum.inr (monomial j (1 : R)) := by
  rw [rename_monomial, rename_monomial, monomial_mul, mul_one, sumElim_eq_mapDomain_add]

/-- The same split with the coefficient on the *right* factor — the orientation the grouped
representation below needs, since there the left factors are bare monomials. -/
theorem monomial_sumElim_eq' (i : σ →₀ ℕ) (j : τ →₀ ℕ) (c : R) :
    monomial (Finsupp.sumElim i j) c
      = (rename Sum.inl (monomial i (1 : R)) : MvPolynomial (σ ⊕ τ) R)
        * rename Sum.inr (monomial j c) := by
  rw [rename_monomial, rename_monomial, monomial_mul, one_mul, sumElim_eq_mapDomain_add]

/-- **Every polynomial has a separated representation**, indexed by its own support.

The crude version: one term per monomial of `P`.  ⚠ Its `φ` are *not* independent — distinct
monomials of `P` can share an `x`-part.  Use the grouped version below when independence
matters. -/
theorem exists_separated_representation (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (s : Finset ((σ ⊕ τ) →₀ ℕ)) (φ : ((σ ⊕ τ) →₀ ℕ) → MvPolynomial σ R)
      (ψ : ((σ ⊕ τ) →₀ ℕ) → MvPolynomial τ R),
      P = ∑ n ∈ s, (rename Sum.inl (φ n) : MvPolynomial (σ ⊕ τ) R) * rename Sum.inr (ψ n) := by
  classical
  refine ⟨P.support,
    fun n => monomial (Finsupp.sumFinsuppEquivProdFinsupp n).1 (coeff n P),
    fun n => monomial (Finsupp.sumFinsuppEquivProdFinsupp n).2 (1 : R), ?_⟩
  conv_lhs => rw [as_sum P]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [← monomial_sumElim_eq, ← eq_sumElim]

/-- **A separated representation with linearly independent `φ`.**

Grouping the monomials of `P` by their `x`-part makes the left factors *distinct* monomials,
which `linearIndependent_monomial` shows are independent.  The `ψ` collect the corresponding
`y`-parts.

⚠ The `ψ` need not be independent, and Roth's lemma wants a representation where both families
are — see the module header. -/
theorem exists_separated_representation_monomial (P : MvPolynomial (σ ⊕ τ) R) :
    ∃ (t : Finset (σ →₀ ℕ)) (ψ : (σ →₀ ℕ) → MvPolynomial τ R),
      P = ∑ i ∈ t, (rename Sum.inl (monomial i (1 : R)) : MvPolynomial (σ ⊕ τ) R)
            * rename Sum.inr (ψ i) := by
  classical
  refine ⟨P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1),
    fun i => ∑ n ∈ P.support.filter (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1 = i),
      monomial (Finsupp.sumFinsuppEquivProdFinsupp n).2 (coeff n P), ?_⟩
  conv_lhs => rw [as_sum P]
  rw [← Finset.sum_fiberwise_of_maps_to
    (g := fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1)
    (t := P.support.image (fun n => (Finsupp.sumFinsuppEquivProdFinsupp n).1))
    (fun n hn => Finset.mem_image_of_mem _ hn)
    (fun n => monomial n (coeff n P))]
  refine Finset.sum_congr rfl fun i _ => ?_
  dsimp only
  rw [map_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun n hn => ?_
  obtain ⟨-, hni⟩ := Finset.mem_filter.mp hn
  rw [← monomial_sumElim_eq', ← hni, ← eq_sumElim]

/-- Distinct monomials are linearly independent: they are part of `basisMonomials`. -/
theorem linearIndependent_monomial (t : Set (σ →₀ ℕ)) :
    LinearIndependent R (fun i : t => (monomial (i : σ →₀ ℕ) (1 : R) : MvPolynomial σ R)) := by
  have h := (basisMonomials σ R).linearIndependent
  rw [coe_basisMonomials] at h
  exact h.comp _ Subtype.val_injective

/-! ### Next

Two mechanical gaps before this feeds the induction step: extract a **minimal** representation
(so both families are independent) and reindex from `Finset (σ →₀ ℕ)` to `Fin r`.

⚠ The other entry the audit came back empty on is **`ω(m, ε)`** — the growth constant in
`RothGrowth`.  Nothing supplies or constrains it, and nothing can until the recursion is
written, because `ω` is whatever the recursion's error terms force it to be.  That is the one
open item that is genuinely mathematical rather than mechanical. -/

end MvPolynomial
