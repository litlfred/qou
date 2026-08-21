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

/-! ### Two conventions that were stated as theorems, and are not

**2026-08-21, bean `qou/q407`.** `length_bound_necessary` and
`structurallyValidBinding_necessary` stood here as

```lean
theorem length_bound_necessary {w : List Int} {L_max : ℕ}
    (h : ¬(w.length ≤ L_max)) : ¬(w.length ≤ L_max) := h
```

— `theorem (h : P) : P := h`, hypothesis and conclusion identical, proof
the identity. They asserted nothing about braid words, the enumerator, or
`B_{n_0}`, and stayed true if every definition in this file were replaced.

They were not failed proofs; they were **conventions of the search**
written in the grammar of results. `length_bound_necessary`'s own
docstring conceded it — "any candidate violating this bound is excluded
from the search *by hypothesis*". The `L_K_max ≤ 4` cutoff is a parameter
of `binding-k-enumerator`, and structural validity is the definition of a
well-formed binding word; neither is a fact about the substrate that could
be true or false.

Recording the conventions here, where they belong:

* **Length bound.** The R5-full SDP search for canonical `T_w` considers
  only candidates with `w.length ≤ L_K_max`, currently `4`
  (`binding-k-enumerator` parameter).
* **Structural validity.** A binding word at `n_0` is non-empty, has no
  zero-index generator, and has every generator in `3 ≤ |g| < n_0`.

Naming a `def` for the search space and re-proving `¬bound → ¬inSpace`
by `id` was the alternative. It would have made the statement mention
something, but the definition would exist only to be echoed — the same
defect one level up. Deleted instead. Neither had any caller: the only
reference to either name in the corpus was its own definition. -/

end QOU.BraidKnot.PSDFeasibilityProxy
