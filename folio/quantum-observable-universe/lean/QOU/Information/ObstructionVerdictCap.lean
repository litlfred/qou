import Mathlib.Logic.Basic

/-!
# QOU.Information.ObstructionVerdictCap — the single-verdict reading, and its counter-model

**Companion to** [`ObstructionGenericity`](ObstructionGenericity.lean) and content
block [`thm:qou-obstruction-reduction`](../../../quantum-observable-universe/stochastic-mechanics/qou-obstruction-reduction.md).

## The question this answers

`thm:qou-obstruction-reduction` computes the classical-limit obstruction space as
**one**-dimensional, `HH²(𝒰_q, Ad) ≅ k`, with class `χ(A) = -6 ≠ 0`; and the
corpus attaches several Millennium reformulations to *restrictions* of that one
class. It is tempting to read this as: one scalar, therefore one verdict,
therefore the legs stand or fall together. Call that the **single-verdict
reading**.

This file makes the reading precise, shows what it would cost, and then exhibits
the corpus's own **counter-model** to it. The conclusion is the opposite of the
tempting one: the restrictions are *independent*, the unification is weaker than
it reads, and no leg constrains another through the shared class alone.

## Why the reading is not the corpus's

Three facts, each checkable in the corpus, defeat any attempt to model "the
obstruction vanishes" as a single `Prop`:

1. **Vanishing is level-indexed, not a proposition.**
   `qou-obstruction-reduction.md` part (c) reads *"the obstruction vanishes at
   Kummer level `n` iff `n ∣ χ(A)`"*, carried in Lean as
   `kappa_vanishes : ℕ → Prop` with `kappa_vanishes_iff_chi` a **family** over
   `n` (`QOU.AlgebraicSubstrate.qou_obstruction_reduction`). There is no single
   Prop to be faithful to.

2. **The evaluation maps are explicitly different.** `conj:qou-p-neq-np` states
   the shared-class corollary as *"their evaluation maps **differing** but the
   underlying class remaining identical"*, and scopes proportionality to
   *"RH, NS, and BSD"* plus P-vs-NP — **q-Collatz is not among them.**

3. **The restrictions land in three different groups**: `χ(A) ∈ HH²(𝒰_q, Ad)`,
   `κ_C ∈ H²(𝒮_{C_q}, 𝔾_m)`, `NS(A) ∈ H³_loc(A, Θ)`. Classes in different
   groups may vanish independently by construction.

## The counter-model (the punchline)

The corpus proves **both** of the following at `χ(A) = -6`, with no
inconsistency:

* `kappa_vanishes 2` is **true** — since `2 ∣ -6`, the q-Collatz even-branch
  `[2]_q` Kummer divisor is removable
  (`QOU.AlgebraicSubstrate.qcollatz_kummer_removable_of_chi_neg_six`, proved);
* `res_ℛ(χ(A)) ≠ 0` — because `q₀` is strictly non-torsion, **no** finite Kummer
  level applies (`QouPNeqNp.chiResidual_ne_zero`).

A vanishing verdict on one leg and a non-vanishing verdict on another, from the
same class, simultaneously. That pair **is** a counter-model to the
single-verdict hypothesis: `single_verdict_refuted_by_counter_model` below turns
it into a refutation. So the collision results in this file are conditional on a
hypothesis the corpus itself falsifies — which is exactly why the "one scalar,
three problems" intuition must not be used to transfer results between legs.

## Correction record (2026-08-15)

An earlier revision of this file asserted the opposite: that the three
faithfulness claims plus proportionality were "not jointly tenable" and that the
package "predicts q-Collatz is false, contradicting `conj:q-collatz`". **That was
wrong**, for the three reasons above — it collapsed a level-indexed family to one
`Prop`, and applied a proportionality claim to a leg that claim excludes. The
error was caught by adversarial review before merge. The present file keeps the
formal skeleton (which was sound) and replaces the interpretation with the
counter-model. Recorded per AGENTS.md §"Report honest negatives".

## Scope

Every hypothesis is a named argument — no `axiom`, no `instance`, nothing
instantiated. `Collatz`, `NSRegular`, `PNeqNP` are opaque `Prop`s throughout,
exactly as in `QouPNeqNp`. Nothing here proves or refutes any conjecture; the
only thing refuted is the single-verdict *reading*, and it is refuted by corpus
facts supplied as explicit hypotheses.
-/

namespace QOU.Information

/-! ### What one verdict would buy -/

/-- **Verdict cap.** If one verdict `v` is faithful to two predicates, those
    predicates are equivalent. This is the whole content of "one scalar cannot
    answer two questions differently" — and it is `Iff` algebra, which is the
    point: the mathematics is trivial, so all the weight sits on whether the
    hypotheses hold. Per the counter-model below, they do not. -/
theorem verdict_cap {v A B : Prop} (hA : v ↔ A) (hB : v ↔ B) : A ↔ B :=
  hA.symm.trans hB

/-- **Opposite polarity.** A predicate faithful to a verdict and a predicate
    faithful to its negation are negations of one another. -/
theorem opposite_polarity {z A B : Prop} (hA : z ↔ A) (hB : ¬ z ↔ B) : A ↔ ¬ B := by
  constructor
  · intro ha hb; exact (hB.mpr hb) (hA.mpr ha)
  · intro hnb; exact hA.mp (Classical.byContradiction fun hz => hnb (hB.mp hz))

/-! ### The single-verdict hypothesis, named rather than assumed

The three restrictions get **three distinct** propositions, as the corpus has
them. `SingleVerdict` is the extra assumption that collapses them — stated
explicitly so it can be pointed at, and, below, falsified. -/

variable {VanC VanNS VanR Collatz NSRegular PNeqNP : Prop}

/-- **The single-verdict hypothesis.** The Collatz, Navier–Stokes and
    resolution-tree restrictions of `κ₀` agree: the first two vanish together,
    and the third's vanishing is the same event. This is what "one class, one
    verdict" would require. It is **not** a corpus claim. -/
def SingleVerdict (VanC VanNS VanR : Prop) : Prop :=
  (VanC ↔ VanNS) ∧ (VanC ↔ VanR)

/-- **Under the single-verdict hypothesis, q-Collatz and q-NS regularity
    collide.** Both legs sit on the vanishing side, so one verdict identifies
    them: two problems the corpus treats as independent would become one. -/
theorem collatz_iff_nsRegular_of_single
    (hsv : SingleVerdict VanC VanNS VanR)
    (hColl : VanC ↔ Collatz) (hNS : VanNS ↔ NSRegular) :
    Collatz ↔ NSRegular :=
  verdict_cap hColl (hsv.1.trans hNS)

/-- **Under the single-verdict hypothesis, q-Collatz and `P ≠ NP` become
    negations.** The Collatz leg is faithful to *vanishing*, the P-vs-NP leg to
    *non-vanishing*; one verdict makes the two conjectures incompatible. That
    this conclusion is absurd is a mark against the hypothesis, not against
    either conjecture. -/
theorem collatz_iff_not_pnp_of_single
    (hsv : SingleVerdict VanC VanNS VanR)
    (hColl : VanC ↔ Collatz) (hPNP : ¬ VanR ↔ PNeqNP) :
    Collatz ↔ ¬ PNeqNP :=
  opposite_polarity (hsv.2.symm.trans hColl) hPNP

/-! ### The counter-model: the corpus falsifies the hypothesis -/

/-- **The single-verdict hypothesis is refuted by the corpus's own arithmetic.**
    Feed it the two facts the corpus proves at `χ(A) = -6` — the Collatz-side
    level-2 restriction **vanishes** (`2 ∣ -6`, so the `[2]_q` divisor is
    removable), while the resolution-tree restriction does **not** (`q₀` strictly
    non-torsion, so no finite Kummer level applies) — and it is inconsistent.

    Hence no collision result above applies to the corpus, and the shared class
    transfers nothing between legs. -/
theorem single_verdict_refuted_by_counter_model
    (hCvanishes : VanC) (hRnonzero : ¬ VanR) :
    ¬ SingleVerdict VanC VanNS VanR :=
  fun hsv => hRnonzero (hsv.2.mp hCvanishes)

/-- **Restated as the corpus's disposition.** Given the same two facts, the legs
    are *not* forced together: the collision hypothesis fails, so `Collatz` and
    `PNeqNP` may both hold. This is the honest reading of "one class, several
    restrictions" — the class is shared, the verdicts are not. -/
theorem legs_independent_of_counter_model
    (hCvanishes : VanC) (hRnonzero : ¬ VanR) :
    ¬ SingleVerdict VanC VanNS VanR ∧ (VanC ∧ ¬ VanR) :=
  ⟨single_verdict_refuted_by_counter_model hCvanishes hRnonzero, hCvanishes, hRnonzero⟩

end QOU.Information
