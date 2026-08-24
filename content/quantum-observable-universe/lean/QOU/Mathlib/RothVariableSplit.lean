/-
  **The variable split** — `σ ≃ Fin n ⊕ Unit` from an ordering `σ ≃ Fin (n+1)`, and the
  transport of `index`, `RothGrowth` and `degreeOf` across it.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/RothOperatorFamily.lean` and through it the rest
  of the arc.

  ═══ WHY THIS EXISTS ═══

  Roth's lemma's statement (`RothLemmaUniform`) carries an ordering `o : σ ≃ Fin m` and one
  degree vector `d : σ → ℕ`.  Its induction step splits off the *last* variable in that
  ordering, and every theorem in `RothOperatorFamily` is written for the split form
  `σ' ⊕ Unit`.  Nothing connected the two.

  ⚠ This is the second time the indexing choice has cost real work, and it is worth setting
  against **correction 7**, which called `Fin m` transport "pure overhead" on the strength of
  `index_rename_equiv` being three lines.  That lemma *is* three lines; what it does not do is
  produce the split, transport the growth condition, or line up `degreeOf`.  The correction was
  right that transport is not deep and wrong that it is free.

  ═══ WHAT IS HERE, AND WHAT IS NOT ═══

  Here: the equivalence, its computation rules, and the transport of the three things the step
  needs.  `index_le_of_rothGrowth_split` applies §13's conclusion to a polynomial presented in
  `o : σ ≃ Fin (n+1)` form.

  ⚠ **Not** here: the integrality step.  The induction hypothesis is about polynomials with
  *integer* coefficients, and the Wronskians it is applied to are rational combinations —
  Gauss's lemma (§6, `RothHeightBound`) is what fixes that, and it is not wired in.  So
  `hres` below remains a hypothesis and this module does not discharge it.
-/
import QOU.Mathlib.RothOperatorFamily

namespace MvPolynomial

variable {σ : Type*} {R : Type*} [CommRing R]

/-! ### The equivalence -/

/-- `Fin (n+1) ≃ Fin n ⊕ Unit`, sending `Fin.last` to the `Unit` component. -/
def splitLast (n : ℕ) : Fin (n + 1) ≃ Fin n ⊕ Unit :=
  finSuccEquivLast.trans (Equiv.optionEquivSumPUnit.{0} (Fin n))

@[simp] theorem splitLast_castSucc {n : ℕ} (i : Fin n) :
    splitLast n i.castSucc = Sum.inl i := by
  simp [splitLast]

@[simp] theorem splitLast_last (n : ℕ) : splitLast n (Fin.last n) = Sum.inr () := by
  simp [splitLast]

@[simp] theorem splitLast_symm_inl {n : ℕ} (i : Fin n) :
    (splitLast n).symm (Sum.inl i) = i.castSucc := by
  simp [splitLast]

@[simp] theorem splitLast_symm_inr (n : ℕ) :
    (splitLast n).symm (Sum.inr ()) = Fin.last n := by
  simp [splitLast]

/-- The variable equivalence an ordering induces: the last variable becomes the `Unit`
component, and every other variable keeps its position. -/
def splitOrder {n : ℕ} (o : σ ≃ Fin (n + 1)) : σ ≃ Fin n ⊕ Unit :=
  o.trans (splitLast n)

theorem splitOrder_symm_apply {n : ℕ} (o : σ ≃ Fin (n + 1)) (x : Fin (n + 1)) :
    (splitOrder o).symm (splitLast n x) = o.symm x := by
  have h : splitLast n x = splitOrder o (o.symm x) := by
    rw [splitOrder, Equiv.trans_apply, Equiv.apply_symm_apply]
  rw [h, Equiv.symm_apply_apply]

/-- The split-off variable: the last one in the ordering. -/
theorem splitOrder_symm_inr {n : ℕ} (o : σ ≃ Fin (n + 1)) :
    (splitOrder o).symm (Sum.inr ()) = o.symm (Fin.last n) := by
  rw [← splitLast_last n, splitOrder_symm_apply]

/-! ### Transport

A function on `σ` becomes a `Sum.elim` on the split, and everything else follows from that
one rewriting. -/

/-- The left half of a `σ`-indexed function, read through the split. -/
def splitLeft {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) : Fin n → β :=
  fun j => f ((splitOrder o).symm (Sum.inl j))

/-- The right half — a one-element family, the split-off variable. -/
def splitRight {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) : Unit → β :=
  fun u => f ((splitOrder o).symm (Sum.inr u))

theorem split_eq {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) :
    f ∘ (splitOrder o).symm = Sum.elim (splitLeft o f) (splitRight o f) := by
  funext x
  cases x <;> rfl

@[simp] theorem splitRight_unit {β : Type*} {n : ℕ} (o : σ ≃ Fin (n + 1)) (f : σ → β) :
    splitRight o f () = f (o.symm (Fin.last n)) := by
  rw [splitRight, splitOrder_symm_inr]

/-- **The index, transported.**  One rewriting of `index_rename_equiv`. -/
theorem index_splitOrder [DecidableEq σ] {n : ℕ} (o : σ ≃ Fin (n + 1)) (d : σ → ℕ)
    (α : σ → R) (P : MvPolynomial σ R) :
    index d α P
      = index (Sum.elim (splitLeft o d) (splitRight o d))
          (Sum.elim (splitLeft o α) (splitRight o α)) (rename (splitOrder o) P) := by
  rw [index_rename_equiv (splitOrder o).symm d α P, Equiv.symm_symm, split_eq, split_eq]

/-- **The growth condition, transported.** -/
theorem rothGrowth_splitOrder {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (d : σ → ℕ)
    (hg : RothGrowth o ω d) :
    RothGrowth (splitLast n).symm ω (Sum.elim (splitLeft o d) (splitRight o d)) := by
  have hD : ∀ x : Fin (n + 1),
      Sum.elim (splitLeft o d) (splitRight o d) (splitLast n x) = d (o.symm x) := by
    intro x
    rw [← split_eq]
    exact congrArg d (splitOrder_symm_apply o x)
  intro j k hjk
  rw [Equiv.symm_symm, hD, hD]
  exact hg j k hjk

/-- **The split-off variable comes last** — the hypothesis `index_le_of_rothGrowth_*` needs. -/
theorem splitLast_hlast (n : ℕ) (k : Fin n) :
    (((splitLast n).symm (Sum.inl k) : Fin (n + 1)) : ℕ) + 1
      ≤ (((splitLast n).symm (Sum.inr ()) : Fin (n + 1)) : ℕ) := by
  rw [splitLast_symm_inl, splitLast_symm_inr, Fin.coe_castSucc, Fin.val_last]
  exact k.isLt

/-- **`degreeOf`, transported.** -/
theorem degreeOf_splitOrder [DecidableEq σ] {n : ℕ}
    (o : σ ≃ Fin (n + 1)) (P : MvPolynomial σ R) (x : σ) :
    degreeOf (splitOrder o x) (rename (splitOrder o) P) = degreeOf x P :=
  degreeOf_rename_of_injective (splitOrder o).injective x

/-! ### §13 for a polynomial presented with an ordering -/

/-- **§13's conclusion, for a polynomial given as `o : σ ≃ Fin (n+1)` plus one degree vector.**

This is the shape `RothLemmaUniform` uses.  Everything about the `σ' ⊕ Unit` split is handled
internally; the caller states degrees, growth and the index bound entirely in terms of `σ`.

⚠ `hres` is still phrased on the **renamed** polynomial, and deliberately: that is what the
induction actually produces, since the sub-problems live on the split.  Hiding the rename here
would only move the transport into the caller.

⚠ It also carries the two non-vanishing hypotheses — see the tenth correction in
`QOU/Mathlib/RothOperatorFamily.lean`.  Without them the hypothesis is unsatisfiable, because
the all-empty operator family is bounded-order, realises the same representation, and has a
vanishing Wronskian for `r ≥ 2`. -/
theorem index_le_of_rothGrowth_split {K : Type*} [Field K] [CharZero K] [DecidableEq σ]
    {n : ℕ} (o : σ ≃ Fin (n + 1)) (ω : ℚ) (hω : 1 ≤ ω) (d : σ → ℕ)
    (hg : RothGrowth o ω d) (hd0 : d (o.symm (Fin.last n)) ≠ 0)
    {D₂ : ℕ} (hD₂ : D₂ ≠ 0) (hd₂ : D₂ ≤ d (o.symm (Fin.last n)))
    (α : σ → K) (P : MvPolynomial σ K) (hP : P ≠ 0)
    (hdeg : degreeOf (o.symm (Fin.last n)) P ≤ d (o.symm (Fin.last n)))
    (εU εV : ℚ) (hε : 0 ≤ εU + εV)
    (hres : ∀ (r : ℕ) (φ : Fin r → MvPolynomial (Fin n) K) (ψ : Fin r → MvPolynomial Unit K)
        (Dx : Fin r → List (Fin n)) (Dy : Fin r → List Unit),
      0 < r → (∀ i, (Dx i).length ≤ (i : ℕ)) → (∀ j, (Dy j).length ≤ (j : ℕ)) →
      rename (splitOrder o) P
          = ∑ k, (rename Sum.inl (φ k) : MvPolynomial (Fin n ⊕ Unit) K)
              * rename Sum.inr (ψ k) →
      mvGenWronskian Dx φ ≠ 0 → mvGenWronskian Dy ψ ≠ 0 →
      index (fun j => r * splitLeft o d j) (splitLeft o α) (mvGenWronskian Dx φ)
          ≤ ((εU : ℚ) : WithTop ℚ) ∧
        index (fun j => r * splitRight o d j) (splitRight o α) (mvGenWronskian Dy ψ)
          ≤ ((εV : ℚ) : WithTop ℚ))
    (θ q : ℚ) (hθt : 2 / ω ≤ θ) (hq0 : 0 ≤ q)
    (hq : ((d (o.symm (Fin.last n)) : ℚ) + 1) * (εU + εV) ≤ q ^ 2 * (D₂ : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P) :
    θ ≤ 2 / ω + 2 * max (εU + εV) q := by
  classical
  have hPne : rename (splitOrder o) P ≠ 0 := fun h =>
    hP (rename_injective _ (splitOrder o).injective (by rw [h, map_zero]))
  refine index_le_of_rothGrowth_of_rescaled_bounds (splitLast n).symm ω hω
    (splitLeft o d) (splitRight o d) (rothGrowth_splitOrder o ω d hg)
    (splitLast_hlast n) ?_ hD₂ ?_ (splitLeft o α) (splitRight o α)
    (rename (splitOrder o) P) hPne ?_ εU εV hε hres θ q hθt hq0 ?_ ?_
  · rwa [splitRight_unit]
  · intro u
    cases u
    rwa [splitRight_unit]
  · rw [splitRight_unit]
    have : degreeOf (splitOrder o (o.symm (Fin.last n))) (rename (splitOrder o) P)
        = degreeOf (o.symm (Fin.last n)) P :=
      degreeOf_rename_of_injective (splitOrder o).injective _
    rw [show (Sum.inr () : Fin n ⊕ Unit) = splitOrder o (o.symm (Fin.last n)) by
      rw [splitOrder, Equiv.trans_apply, Equiv.apply_symm_apply, splitLast_last], this]
    exact hdeg
  · rwa [splitRight_unit]
  · rwa [← index_splitOrder]

/-! ### Next

The transport is done; `index_le_of_rothGrowth_split` states §13's conclusion entirely in
terms of `σ`, `o` and `d`.

⚠ What still stands between this and the recursion is **integrality**, not indexing.  The
induction hypothesis (`RothLemmaUniform`) is about polynomials with *integer* coefficients;
the Wronskians `hres` speaks of are rational combinations of the representation's factors.
Gauss's lemma is what reconciles them — §6 of the source does exactly this, and
`RothHeightBound` has the Gauss step — but it is **not wired in**, so `hres` remains a
hypothesis.

That is the next piece, and it is the last one before the induction can be written. -/

end MvPolynomial
