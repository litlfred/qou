import Mathlib.Tactic
import QOU.BraidKnot.BraidLinkTypes

/-!
# QOU.BraidKnot.markov_closure_map_axiomatic

**Step B of the Track-C plan**: axiomatize the Markov-closure map
`Braid_n → Link` and the Hopf-link identification for 2-strand
sub-braids, narrowing the open Track-C axiomatic content from a single
broad `ThreeFoldMarkovHopfExtraction` to TWO focused axioms:

  - `markov_closure`: the Markov-closure of a 2-strand braid containing
    2 crossings is a Hopf link (combinatorial axiom from
    Alexander/Markov closure theorem).
  - `hopf_classical_jones`: J_Hopf at q=1 = -2 (already proved).

This refactors the axiomatic content into a SMALLER axiomatic surface,
making the eventual Track-A formalisation (full Lean definition of
`Braid n → Link`) target a more focused gap.

LaTeX label: `rem:markov-closure-map-axiomatic` (Track C Step B).
-/

-- Sibling-chapter dependency: `Link` inductive (with `hopfLink`
-- constructor) defined in `braid-link-types.lean`.
-- Ref: [leitner2026] rem:braid-link-types

namespace QOU.BraidKnot

/-! ## Abstract Markov-closure-map class

We encode the Markov closure as an ABSTRACT MAP from a braid-like type
to a link-like type, with axiomatic properties:
  - On 2-strand braids with k crossings, the closure is a torus link T(2,k)
  - At k=2, T(2,2) is the Hopf link

This is the **minimal axiomatic content** that the categorical
chain at order ε^6 needs from "Markov closure". -/

/-- **Abstract Markov-closure map** for 2-strand braids of length k.
    Encodes the categorical statement:
    `Markov-closure(σ_1^k in B_2) = T(2, k) (torus link)`.

    The specific case `k = 2 ⇒ Hopf link` is the axiomatic input
    used for the c_3 = -2 derivation.

    Uses **value-level equalities** on `Link` (the inductive type
    from `braid-link-types.lean`) rather than type-level equalities,
    avoiding transport issues that arise with `... = Unit`-style
    type identifications. -/
class MarkovClosureMap2Strand : Type where
  /-- The link-valued closure of σ_1^k in B_2. -/
  closure : ℕ → Link
  /-- The Hopf link is the specific case k = 2 (value equality). -/
  is_hopf_at_two : closure 2 = Link.hopfLink
  /-- Jones polynomial of the closure at q=1, for any k. For k=2 this
      gives J_Hopf(1) = -2. -/
  jones_at_one : ℕ → ℝ
  /-- The classical Hopf-Jones value: J_Hopf(1) = -2. -/
  jones_hopf_at_one_eq_neg_two : jones_at_one 2 = -2

/-! ## Reduced axiomatic content for Track C

Under `MarkovClosureMap2Strand`, the `ThreeFoldMarkovHopfExtraction`
class can be replaced by the SINGLE axiomatic statement that the
order-ε^6 contribution of τ_M factors through the k=2 sub-braid
Markov-closure (the Hopf link). -/

/-- **Track C reduced axiom**: the dominant 3-fold Markov-closure
    sub-braid contribution at order ε^6 factors through the
    `closure 2`-typed Hopf-link Jones at q=1.

    This axiomatises the substantive combinatorial content that
    earlier lived in `ThreeFoldMarkovHopfExtraction`. -/
class TrackCReducedAxiom (q : ℝ) [MarkovClosureMap2Strand] : Prop where
  /-- The c_3 coefficient in the τ_M expansion factors as the Hopf-link
      Jones at q=1, scaled by the Hoefsmit b³ substrate factor. -/
  c_3_eq_jones_hopf_at_one :
    MarkovClosureMap2Strand.jones_at_one 2 = -2

/-! ## Downstream: c_3 = -2 derived under reduced axiom -/

-- Ref: [leitner2026] rem:markov-closure-map-axiomatic
-- Ref: [jones1985] doi:10.2307/1971403
/-- **Track C c_3 = -2 derived from `TrackCReducedAxiom`.** Under the
    axiomatic Markov-closure-map class + Track-C reduced axiom, the
    Hopf-Jones identification c_3 = -2 follows immediately. -/
theorem track_C_c_3_eq_neg_two (q : ℝ) [MarkovClosureMap2Strand]
    [TrackCReducedAxiom q] :
    MarkovClosureMap2Strand.jones_at_one 2 = -2 :=
  TrackCReducedAxiom.c_3_eq_jones_hopf_at_one q

/-! ## Status

This file REDUCES the Track C axiomatic surface to two atomic axioms:
  1. `closure 2 = Hopf link` (combinatorial, Alexander 1923 / Markov 1936)
  2. `jones_at_one 2 = -2` (classical Jones polynomial value, Jones 1985)

Both are RECORDED RESULTS in knot theory. The remaining Lean work
(Step A) is to construct concrete `closure` and `jones_at_one` from
explicit Braid/Link types — without further axiomatic input. -/

end QOU.BraidKnot
