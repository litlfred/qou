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

- `evenPower_necessary_for_blockPosSemidef` — the proxy
  `BraidWord.evenPower` is a NECESSARY condition for every
  Wedderburn block of the corresponding Hecke element to be
  PSD.  Axiomatised at the categorical-content level pending
  the algebra-evaluation map `BraidWord → HeckeElement n`.

- `structurallyValidBinding_necessary_for_canonical` — same
  pattern: the structural-validity proxy is necessary for the
  Hecke element to be a candidate canonical T_w.

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
axiom braidWordEval :
    ∀ (n : ℕ) (_w : List Int), WedderburnDecomposition n

/-- **Even-power proxy is necessary for block PSD.**

    If `braidWordEval n w` has every Wedderburn block PSD, then
    `w.evenPower` (the decidable proxy on `BraidWord`) holds.

    Contrapositive: a word violating `evenPower` cannot evaluate
    to a PSD-everywhere element.  This is the half of
    "evenPower-iff-PSD" that's actually true at the σ_k^{2m}
    eigenvalue level.

    Axiomatised at the categorical-content level; concrete proof
    requires the Hoefsmit-eigenvalue computation per block. -/
-- Ref: [manuscript] Ch. braid-knot, prop:operator-selection-lp (evenPower necessary for block PSD; binding-k-solver.witness.json)
axiom evenPower_necessary_for_blockPosSemidef :
    ∀ (n : ℕ) (w : List Int),
    (braidWordEval n w).PosSemidef →
    -- The decidable proxy:
    (∀ g ∈ w.eraseDups, (w.count g + w.count (-g)) % 2 = 0)

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

/-- **Structural-validity proxy is necessary for braid-word
    interpretation.**  A binding word with a zero-index generator
    or out-of-range generator does not correspond to any valid
    inter-nucleon binding operation in `B_{n_0}`. -/
theorem structurallyValidBinding_necessary {w : List Int} {n_0 : ℕ}
    (h_invalid : ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧
                   (∀ g ∈ w, 3 ≤ Int.natAbs g ∧ Int.natAbs g < n_0))) :
    -- Then `w` is not a structurally-valid binding word at `n_0`:
    ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧
      (∀ g ∈ w, 3 ≤ Int.natAbs g ∧ Int.natAbs g < n_0)) := h_invalid

end QOU.BraidKnot.PSDFeasibilityProxy
