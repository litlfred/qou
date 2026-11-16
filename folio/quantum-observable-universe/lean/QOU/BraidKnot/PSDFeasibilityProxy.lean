import Mathlib.Data.Int.Basic
import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.Wedderburn

/-!
# QOU.BraidKnot.PSDFeasibilityProxy

Bridge between the decidable structural proxies on `BraidWord`
(`structurallyValidBinding`, `evenPower`, `length ≤ 4`) used in
the `CanonicalKnotIdSDP` placeholder instances, and the
categorical PSD-feasibility statement on the abstract Hecke-
algebra Wedderburn decomposition.

## What this module provides

- A note recording that the former axiom
  `evenPower_necessary_for_blockPosSemidef` was false (the full
  twist in `H_3` is block-PSD with odd generator counts) and was
  removed 2026-11-15; the even-power test is right only for
  single-generator words.

- `withinLengthBound` — the enumerator's search-space bound as a
  named decidable predicate.

**Not provided, despite an earlier version of this list saying so:**
a `structurallyValidBinding_necessary_for_canonical` — "the
structural-validity proxy is necessary for the Hecke element to be
a candidate canonical T_w". No such declaration exists or has ever
existed in this file. What stood in its place was a tautology under
the similar name `structurallyValidBinding_necessary`, removed on
2026-08-30 (see the note at the foot of this file). The predicate
itself is `BraidWord.structurallyValidBinding` in
`mass-theory/conj-canonical-knot-id-sdp.lean`; the necessity claim
awaits the same algebra-evaluation map as its `evenPower` sibling.

## Mathematical content

The decidable Lean predicates `evenPower`, `structurallyValidBinding`,
and `length ≤ L_K_max` are NECESSARY but NOT SUFFICIENT
conditions for the categorical PSD-feasibility / minimal-length
/ canonical-Markov-trace claims.  This module captures the
arrow `decidable proxy → categorical claim` direction (the only
direction that's relevant for falsification: violating the
proxy disqualifies the candidate categorically).

The reverse direction (sufficiency) requires the full SDP
machinery: PSD eigenvalue check per Wedderburn block via
`QOU.HeckeAlgebra.Hoefsmit`, Markov-trace evaluation via
`QOU.HeckeAlgebra.MarkovTrace`.  These are the open Lean ports.

## References

- `binding-k-enumerator.witness.json` — empirical justification
  that the placeholder bindingKWord [3, 3] satisfies the
  decidable predicates.
- `binding-k-solver.witness.json` — empirical PSD-feasibility
  verification per Wedderburn block.
-/

namespace QOU.BraidKnot.PSDFeasibilityProxy

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Wedderburn

/-- **Abstract braid-word evaluation map** from a list of integer
    generator indices to a `WedderburnDecomposition n`.  Axiomatised
    pending the Hoefsmit-based concrete construction.

    The signature: takes a word `w : List Int` and a strand count
    `n`, returns the Wedderburn decomposition of the corresponding
    Hecke-algebra element.  The map respects the Hecke and braid
    relations (a downstream `axiom`). -/
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9 §13.6 (braid-word → Hecke element evaluation)
opaque braidWordEval :
    ∀ (n : ℕ) (_w : List Int), WedderburnDecomposition n

/-! **The former axiom `evenPower_necessary_for_blockPosSemidef` was false
    under its intended reading** (removed 2026-11-15). It claimed that a word
    whose Hecke evaluation is PSD on every Wedderburn block uses each
    generator an even number of times (counting inverses). The full twist
    `Δ² = (σ₁σ₂)³` in `H_3(q)`, `q > 0`, refutes it: `Δ²` is central and acts
    by `q⁶` on `(3)`, `q⁻⁶` on `(1³)` and `1` on `(2,1)`, so it is PSD on every
    block, yet `σ₁` and `σ₂` each occur three times. (The `(2,1)` value was
    checked on the seminormal 2×2 representation.) Lean cannot see the
    counterexample because `braidWordEval` is `opaque`, so this is a
    removal of a wrong claim, not a kernel refutation. Nothing in Lean used
    the axiom; `HopfBindingK` only cited it in prose.

    What is true is narrower: for a word in a single generator `σ_g`
    (with `g` a valid index), the element is `σ_g^k`, whose eigenvalues are
    `q^k` and `(−q⁻¹)^k`, so it is block-PSD iff `k` is even. A repaired
    statement needs a concrete `braidWordEval`; recorded in bean `qou-n2un`. -/

/-- The **length-bound proxy** for the canonical-T_w search: a candidate
    word is within the enumerator's search space only if `w.length ≤ L_max`
    (the R5-full SDP search bounds candidate length to `L_K_max ≤ 4`, per
    `binding-k-enumerator`'s parameter).

    Named as a decidable predicate (§3b: naming, not asserting). The
    necessity is the enumerator's search-space restriction — a definitional
    bound, not a derived theorem. The previous `(h : ¬P) : ¬P := h` was a
    self-assuming tautology that asserted nothing about braid words. -/
def withinLengthBound (w : List Int) (L_max : ℕ) : Prop :=
  w.length ≤ L_max

/-! ### `structurallyValidBinding_necessary` — REMOVED 2026-08-30

It read, in full:

    theorem structurallyValidBinding_necessary {w : List Int} {n_0 : ℕ}
        (h_invalid : ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧
                       (∀ g ∈ w, 3 ≤ Int.natAbs g ∧ Int.natAbs g < n_0))) :
        ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧
          (∀ g ∈ w, 3 ≤ Int.natAbs g ∧ Int.natAbs g < n_0)) := h_invalid

Hypothesis and conclusion are the same proposition and the proof is the
hypothesis: `(h : ¬P) : ¬P := h`, which is `id` under a name that promises a
necessity result. It asserted nothing about braid words, PSD blocks, or
`n_0`.

**The fix is this file's own precedent, applied one declaration later than it
should have been.** `withinLengthBound` above records that *"the previous
`(h : ¬P) : ¬P := h` was a self-assuming tautology"* and replaces it with a
named decidable predicate — naming, not asserting (§3b). The same move was
available here and was not made.

It is a removal rather than a renaming because the predicate **already has a
canonical name elsewhere**: `BraidWord.structurallyValidBinding` in
[`mass-theory/conj-canonical-knot-id-sdp.lean:156`], a `@[reducible] def`
with roughly twenty use sites, whose body unfolds to exactly the proposition
restated above. Defining a second copy here would have been the worse fix.

Nothing consumed this declaration — the only other mention in the corpus was
the module header's entry for a *differently named* theorem that does not
exist, corrected above.

The necessity direction this file's header describes — structural validity
being necessary for the Hecke element to be a candidate canonical `T_w` — is
**not stated anywhere**, and writing it is authorial: it needs the
algebra-evaluation map the header lists as an open Lean port. Its sibling
`evenPower_necessary_for_blockPosSemidef` was an `axiom` for that reason,
and turned out false (see above). Bean `qou-z9ws`.
-/

end QOU.BraidKnot.PSDFeasibilityProxy
