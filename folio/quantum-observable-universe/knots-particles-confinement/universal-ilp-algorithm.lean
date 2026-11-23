/-
  Universal ILP algorithm for operator selection.

  The same LP selects operators at every level of the QOU construction:
  confinement, gluon, electron attachment, and molecular bonding.

  Ref: [leitner2026] Ch 11 §8, def:universal-ilp-algorithm
-/

import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic

namespace QOU.Interactions

/-- A knot operator in H₃(q) represented by its NF coefficients.

    `IsSingleComponent` is **caller-supplied**: the predicate that decides
    whether a coefficient vector with a given crossing number closes to a
    single-component braid.  It is a parameter rather than a field because a
    field typed with the *universe* `Prop` holds a proposition as data — the
    constructor then chooses it, `True` is a legal choice, and the `is_knot`
    conjunct in `universal_ilp` below was satisfied for free.

    Parameterising makes the structure **refutable**: see
    `knotOperator_isEmpty_of_never_single_component`. -/
structure KnotOperator (q : ℝ)
    (IsSingleComponent : (Fin 6 → ℝ) → ℕ → Prop) where
  coeffs : Fin 6 → ℝ
  crossing_number : ℕ
  /-- The closure is a single component — a **proof**, discharged by the
      caller against their own `IsSingleComponent`, not a proposition the
      constructor picks. -/
  is_knot : IsSingleComponent coeffs crossing_number
  is_nontrivial : crossing_number > 0

/-- The structure is refutable: no knot operator exists over a predicate
    that holds of nothing.  The previous `is_knot : Prop` admitted
    `is_knot := True` and so could not be empty for any `q`. -/
-- Ref: [leitner2026] Ch 11 §8, def:universal-ilp-algorithm
theorem knotOperator_isEmpty_of_never_single_component (q : ℝ) :
    IsEmpty (KnotOperator q (fun _ _ => False)) :=
  ⟨fun K => K.is_knot⟩

/-- The Frobenius Gram matrix G of H₃(q) — **a zero placeholder**, and the
    LP built on it therefore constrains nothing
    (`universal_ilp_holds_of_zero_gram` below proves this, rather than
    leaving it as a docstring claim).

    **Docstring corrected 2026-09-14.** This said the intended `G(q)`
    (Halverson–Ram seminormal Gram on the 6-dimensional `H₃(q)`) "is
    sharper".  Under the canonical convention D (`z = q³/(q²+1)`, owner
    ruling 2026-08-15) that understates it: the real Gram is **singular**.
    `mass-theory/frobenius-gram-matrix` records that `y_(1³) = 0`
    symbolically, so the `(1³)` Wedderburn block *is* the radical of the
    form, `det G = 0` **exactly** (not numerically — at rational `q` the
    whole Gram is rational under D), and `G⁻¹` does not exist; `pyhecke`
    exports `G_PINV` on the quotient `H₃(q)/rad` instead, with `RADICAL`
    the q-antisymmetriser `Σ_w (−1/q)^ℓ(w) T_w`.

    So wiring the real Gram is not a drop-in: `frobenius_positive` over a
    rank-5 form is a different condition, and picking how the radical
    direction is treated is a modelling choice, not a transcription.  Left
    to the author; NOT changed here. -/
-- Ref: [leitner2026] Ch 11, prop:frobenius-gram-matrix
noncomputable def gram_matrix (_q : ℝ) : Matrix (Fin 6) (Fin 6) ℝ :=
  0

/-- Frobenius positivity: G · x ≥ 0 componentwise. -/
def frobenius_positive (q : ℝ) (x : Fin 6 → ℝ) : Prop :=
  ∀ i : Fin 6, (gram_matrix q).mulVec x i ≥ 0

/-- The universal ILP: min cr(K) s.t. K ∈ knots \ {1}, G · NF(x · K) ≥ 0.

    Two conjuncts were dropped as redundant, not as a weakening:
    `K.is_knot` and `K.crossing_number > 0` are now **guaranteed by the
    structure** (`is_knot`, `is_nontrivial`), so restating them here added
    nothing.  Before this change the first was worse than redundant — it
    was the free universe-`Prop` field, satisfiable by `True`. -/
-- Ref: [leitner2026] Ch 11 §8
def universal_ilp (q : ℝ) (state : Fin 6 → ℝ)
    {IsSingleComponent : (Fin 6 → ℝ) → ℕ → Prop} :
    KnotOperator q IsSingleComponent → Prop :=
  fun K => frobenius_positive q (fun i => state i + K.coeffs i)

/-- **The LP currently constrains nothing, and this proves it.**  With the
    zero placeholder for `gram_matrix`, `universal_ilp` holds of *every*
    knot operator, at every `q` and every `state`.

    Reported rather than hidden (AGENTS.md "report honest negatives"): the
    vacuity was already stated in `gram_matrix`'s docstring, where nothing
    checked it.  A machine-checked statement goes stale the moment a real
    Gram lands — this theorem will simply stop compiling. -/
-- Ref: [leitner2026] Ch 11 §8
theorem universal_ilp_holds_of_zero_gram
    (q : ℝ) (state : Fin 6 → ℝ)
    {IsSingleComponent : (Fin 6 → ℝ) → ℕ → Prop}
    (K : KnotOperator q IsSingleComponent) :
    universal_ilp q state K := by
  intro i
  simp [gram_matrix]

/-- **The LP selects the minimum-crossing feasible knot operator**, as a
    predicate: `K` is feasible (`universal_ilp q state K`) and no feasible
    operator has strictly fewer crossings. This names the LP's optimality
    condition (§3b). The previous
    `(hmin : K.cr ≤ K'.cr) : K.cr ≤ K'.cr := hmin` self-assumingly
    re-projected the given comparison and asserted nothing about the LP. -/
-- Ref: [leitner2026] Ch 11 §8
def universal_ilp_selects_minimum (q : ℝ) (state : Fin 6 → ℝ)
    {IsSingleComponent : (Fin 6 → ℝ) → ℕ → Prop}
    (K : KnotOperator q IsSingleComponent) : Prop :=
  universal_ilp q state K ∧
    ∀ K' : KnotOperator q IsSingleComponent, universal_ilp q state K' →
      K.crossing_number ≤ K'.crossing_number

end QOU.Interactions
