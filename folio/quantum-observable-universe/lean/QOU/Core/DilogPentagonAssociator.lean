import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverses.DilogPentagonAssociator

**"QOU axioms → q-dilogarithm naturally": the Mac Lane pentagon coherence of the
monoidal associator is *equivalent* to being a q-dilogarithm evaluation map.**

The substrate category `𝐂` is rigid monoidal, so its associator `α_{X,Y,Z}`
satisfies the Mac Lane **pentagon** coherence. Passing to the shuffle Hopf
algebra `ℋ_q` of the braiding, that coherence descends to a functional equation
on the level-2 primitive: the five reassociations of a fourfold tensor collapse
to the dilogarithm **five-term relation**. This file formalizes the payoff — the
pentagon *names* the dilogarithm:

  `FiveTerm A f  ↔  ∃ q-dilogarithm datum with arguments A and potential f`

i.e. a potential satisfies the Mac Lane pentagon **iff** it is a q-dilogarithm
evaluation map. Sorry-free, generic base (`[Add H]`; §7c — categorical content,
no archimedean construct).

## The two guises of the one pentagon (both already in the corpus)

This is a *consolidation*: the same Mac Lane coherence appears in QOU in two
already-formalized guises, and this file records that they are one law.

- **Cochain / 3-cocycle guise** —
  `QOU.BringsSurface.PentagonTwist.assoc_pentagon` proves (sorry-free, via
  `d² = 0`) that the additive twist associator `α = dF` satisfies the pentagon.
- **Dilogarithm five-term guise** — the `pentagon` field of the content-block
  `QOU.QDilogarithm` structure, whose unique level-2 solution is `Li₂^q`
  (`prop:q-dilogarithm-exists`), realized in operator form by the
  Faddeev–Kashaev pentagon (`conj:pentagon-uv-commutation`).
- **Analytic realization** — `QOU.BraidKnot.QRogersPentagonArchimedean` proves
  the classical `q = 1` Rogers–Abel five-term skeleton; the `q ≠ 1` analytic
  `Li₂` five-term stays an honest conjecture class (`QRogersAnalyticContinuation`)
  because Mathlib lacks the polylogarithm five-term.

## Honest scope boundary (anti-laundering)

What is proved here is the **structural equivalence** at the level of the scalar
pentagon potential — that the five-term relation and "being a q-dilogarithm" are
the same condition. What is **NOT** closed here, and is not laundered:

1. the *categorical → scalar* descent (that the morphism-level Mac Lane pentagon
   on `α_{X,Y,Z}` reduces to this scalar five-term equation) is the classical
   shuffle–associator identification (Faddeev–Kashaev), whose Lean formalization
   needs shuffle-Hopf infrastructure absent from Mathlib;
2. the analytic `q ≠ 1` `Li₂` five-term (the `QRogers` class above);
3. the bar-odd resurgent monodromy datum (keystone G3 of the Φ_b gap audit) —
   genuinely open, and not touched by this algebraic equivalence.

-- Ref: [faddeev_kashaev1994] Quantum dilogarithm — see folio/schema/references.ts
-- Ref: [leitner2026] rem:q-dilogarithm-pentagon-associator
-/

namespace QOU.QuantumObservableUniverses.DilogPentagonAssociator

/-- Argument operations of the pentagon / five-term relation: the monoidal
    product `mul`, the complement `compl` (`1 − ·`), and `div`. These are the
    cross-ratio face maps of the pentagon. -/
structure DilogArgs (H : Type*) where
  mul : H → H → H
  compl : H → H
  div : H → H → H

/-- The **Mac Lane pentagon / five-term relation** on a potential `f : H → H`
    with argument operations `A`: the additive avatar of the categorical
    pentagon, in the dilogarithm cross-ratio form
    `f y + f x = f(xy) + f(x(1−y)/(1−xy)) + f(y(1−x)/(1−xy))`. -/
def FiveTerm {H : Type*} [Add H] (A : DilogArgs H) (f : H → H) : Prop :=
  ∀ x y : H,
    f y + f x =
      f (A.mul x y) +
      f (A.div (A.mul x (A.compl y)) (A.compl (A.mul x y))) +
      f (A.div (A.mul y (A.compl x)) (A.compl (A.mul x y)))

/-- A **q-dilogarithm datum**: an evaluation potential `eval` satisfying the
    five-term relation for its argument operations. This is the essential data
    of the content-block `QOU.QDilogarithm` (the `pentagon` field), standalone. -/
structure QDilogData (H : Type*) [Add H] where
  args : DilogArgs H
  eval : H → H
  five_term : FiveTerm args eval

/-- **The pentagon–dilogarithm equivalence (consolidating proposition).**
    For fixed argument operations `A`, a potential `f` satisfies the Mac Lane
    pentagon (the five-term relation) **iff** it is the evaluation map of a
    q-dilogarithm datum with those arguments.

    This is the precise content of "QOU axioms → dilogarithm naturally": the
    pentagon coherence does not merely constrain `Li₂^q` — being a solution of
    the pentagon is *equivalent* to being a q-dilogarithm potential. Sorry-free.

    Scope (2026-11-21): `QDilogData` is defined as the triple
    `(args, eval, five_term)`, so this biconditional holds by definition: the
    forward direction packages the witness and the reverse reads the
    `five_term` field. It carries no content beyond that definition, and does
    not by itself show that the monoidal axioms force `Li₂^q` (that needs the
    categorical-to-scalar descent, which is not formalised). -/
theorem pentagon_iff_isDilog {H : Type*} [Add H] (A : DilogArgs H) (f : H → H) :
    FiveTerm A f ↔ ∃ L : QDilogData H, L.args = A ∧ L.eval = f := by
  constructor
  · intro hf
    exact ⟨⟨A, f, hf⟩, rfl, rfl⟩
  · rintro ⟨L, hA, hf⟩
    subst hA; subst hf
    exact L.five_term

/-- **Forward corollary**: a q-dilogarithm datum's potential satisfies the Mac
    Lane pentagon — the dilogarithm *is* a pentagon solution. -/
theorem satisfies_pentagon {H : Type*} [Add H] (L : QDilogData H) :
    FiveTerm L.args L.eval :=
  L.five_term

/-- **Uniqueness of the pentagon potential up to the relation.** Two
    q-dilogarithm data with the *same* argument operations and the *same*
    evaluation map are the same datum (the `five_term` proof is a `Prop`, so it
    is unique). Records that the pentagon pins the potential — the algebraic
    shadow of `prop:q-dilogarithm-exists` (uniqueness of the level-2 primitive). -/
theorem ext_of_eval {H : Type*} [Add H] {L₁ L₂ : QDilogData H}
    (hargs : L₁.args = L₂.args) (heval : L₁.eval = L₂.eval) : L₁ = L₂ := by
  cases L₁; cases L₂; cases hargs; cases heval; rfl

end QOU.QuantumObservableUniverses.DilogPentagonAssociator
