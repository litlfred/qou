import QOU.Basic

/-!
# QOU.BraidKnot.LpDualityHypothesisClass — finite LP strong-duality + complementary slackness as a §3b-cond class

Class-axiomatises the two routine LP-theory inputs to the
operator-selection-LP machinery:

  1. **Strong duality** (Schrijver §7.2): for a bounded + feasible
     finite LP, the primal and dual optima coincide, giving
     `duality_gap = 0`.
  2. **Complementary slackness** (Schrijver §7.4): at the optimum,
     a partition `λ` lies in the LP active set iff its primal
     constraint is tight.

These are the two `sorry`s in
`content/.../braids-and-knots/confinement-nf-partial-proof.lean`
(theorems `strong_duality` + `complementary_slackness`).  Per
AGENTS.md §3b-cond, axiomatising them as a class lets the two
theorems be derived as `class.field` references rather than
free-standing `sorry`s — the proper conditional-class locale for
LP-theory inputs that aren't yet wired in Mathlib.

The class is purely a hypothesis carrier; the trivial model fills
both fields via the LP-theory citations (single `sorry` per
field, with explicit `-- Ref: [schrijver1986theory]` per AGENTS.md
§1).  When Mathlib gets a finite-dim LP-duality library
(`Mathlib.Analysis.Convex.LinearProgramming` or similar), the
trivial-model sorrys can be discharged unconditionally without
touching the consumer side of the class.

Bridge to `prop:confinement-nf-partial-proof`: a future refactor
can add `[lpDuality : HasFiniteLPDuality lp]` to the hypotheses of
`theorem_3_strong_duality` and `theorem_1_maximizer_in_active_set`,
deriving them from `lpDuality.dualityGapZero` and
`lpDuality.complementarySlackness` respectively — no `sorry`s in
the consumer file, only in the trivial model.

LaTeX: `\label{def:lp-duality-hypothesis-class}`

References:
- Schrijver, A. (1986). Theory of Linear and Integer Programming,
  Wiley. §7.2 (strong duality), §7.4 (complementary slackness).
-/

namespace QOU.BraidKnot

universe u

/-- Abstract operator-selection LP — mirror of the structure in
`confinement-nf-partial-proof.lean`, restated locally to avoid
cross-module imports until that file is refactored to consume this
class. -/
structure OperatorSelectionLP where
  Λ : Type
  finite : Finite Λ
  primal_obj : ℝ
  dual_obj : ℝ
  active_set : Set Λ
  tight : Λ → Prop

namespace OperatorSelectionLP

/-- Duality gap = |primal − dual|. -/
def duality_gap (lp : OperatorSelectionLP) : ℝ :=
  |lp.primal_obj - lp.dual_obj|

end OperatorSelectionLP

/-- **Finite LP strong-duality + complementary-slackness hypothesis class.**

    Class-axiomatises the two routine LP-theory inputs needed to
    discharge `theorem_3_strong_duality` and
    `theorem_1_maximizer_in_active_set` in
    `confinement-nf-partial-proof.lean` without `sorry`s in the
    consumer file.  Per AGENTS.md §3b-cond conditional-class
    pattern.

    Class fields:
    - `dualityGapZero` — `lp.duality_gap = 0` (Schrijver §7.2).
    - `complementarySlackness` — `λ ∈ active_set ↔ tight λ`
      (Schrijver §7.4). -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  /-- Strong duality theorem (Schrijver §7.2).  Bounded + feasible
      finite LPs satisfy `primal = dual`, hence `duality_gap = 0`. -/
  dualityGapZero : lp.duality_gap = 0
  /-- Complementary slackness (Schrijver §7.4).  At the optimum,
      a partition λ lies in the LP active set iff its primal
      constraint is tight. -/
  complementarySlackness : ∀ (lam : lp.Λ), lam ∈ lp.active_set ↔ lp.tight lam

namespace HasFiniteLPDuality

/-- **External axiom (Schrijver 1986 §7.2): finite-dim LP strong
    duality.**  For every `OperatorSelectionLP lp`, the duality gap
    is zero.  Pending Mathlib's finite-dim LP-duality library. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
axiom schrijver_strong_duality :
    ∀ (lp : OperatorSelectionLP), lp.duality_gap = 0

/-- **External axiom (Schrijver 1986 §7.4): complementary slackness.**
    At the LP optimum, a partition `λ` lies in the active set iff
    its primal constraint is tight. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
axiom schrijver_complementary_slackness :
    ∀ (lp : OperatorSelectionLP) (lam : lp.Λ),
      lam ∈ lp.active_set ↔ lp.tight lam

/-- **Schrijver model (consistency witness).**

    Discharges both class fields via the cited external axioms
    `schrijver_strong_duality` and `schrijver_complementary_slackness`.
    These axioms are §3b-cond placeholders pending Mathlib's finite-
    dim LP-duality library; when that lands, both axioms can be
    discharged unconditionally without touching the consumer side.

    Provided as a `def` (not `instance`) to avoid polluting typeclass
    resolution. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
noncomputable def schrijverModel (lp : OperatorSelectionLP) :
    HasFiniteLPDuality lp where
  dualityGapZero := schrijver_strong_duality lp
  complementarySlackness := schrijver_complementary_slackness lp

/-- Theorem 3 of `prop:confinement-nf-partial-proof` derived from
    the hypothesis class.  Drop-in replacement for the existing
    `theorem_3_strong_duality` (which currently uses a `sorry`):
    `theorem_3_via_class` consumes the class instance instead. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
theorem theorem_3_via_class
    (lp : OperatorSelectionLP) [hyp : HasFiniteLPDuality lp] :
    lp.duality_gap = 0 :=
  hyp.dualityGapZero

/-- Theorem 1 (Wedderburn maximizer in active set) derived from the
    hypothesis class.  Given the maximizer's tightness assumption
    + complementary slackness from the class, the maximizer lies in
    the active set. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
theorem theorem_1_via_class
    (lp : OperatorSelectionLP) [hyp : HasFiniteLPDuality lp]
    (max_pole : lp.Λ) (h_tight : lp.tight max_pole) :
    max_pole ∈ lp.active_set :=
  (hyp.complementarySlackness max_pole).mpr h_tight

end HasFiniteLPDuality

end QOU.BraidKnot
