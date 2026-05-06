/-
  Electroweak interface knot Δ_I — categorical analog of the
  inter-nucleon coupling I from the W-3 deuteron derivation.

  Companion: ew-interface-knot.md
  Path: content/quantum-observable-universe/braids-and-knots/

  Definition is structural — a non-empty word in the adjacent-
  pair generators σ_2, σ_4 of H_6(q). The specific choice that
  realises the Higgs vacuum-expectation-value is open per
  conj:categorical-higgs-mechanism Step C.

  Refs:
    [hoefsmit1974] Hoefsmit thesis, 1974.
    [kassel1995quantum] Kassel, "Quantum Groups," Springer 1995.
    docs/audits/2026-05-06-refocused-1ppb-workplan-v2.md
-/

import Mathlib.Algebra.Algebra.Basic

namespace QOU.BraidsAndKnots

/--
  An `EWInterfaceKnot R q` instance carries the abstract
  structural data for the electroweak interface knot Δ_I.

  Δ_I is an element of H_6(q) realised as a non-empty word in
  the adjacent-pair generators σ_2, σ_4.  Its three sub-
  interfaces Δ_I^{W→Z}, Δ_I^{Z→H}, Δ_I^{H→W} bridge the disjoint
  strand-pairs on which the EW carriers W, Z, H act.

  The trivial Δ_I = 1 case corresponds to the disjoint-product
  pre-EWSB free-boson sector; non-trivial Δ_I encodes the
  Higgs-vev induced coupling.
-/
class EWInterfaceKnot
    (R : Type*) [CommRing R] (q : R)
    where
  /-- Generic-q hypothesis (q not a root of unity). -/
  q_generic : True
  /-- The interface is non-empty (Δ_I ≠ 1) iff the EW symmetry
      is broken (post-EWSB).  Open per conj:categorical-higgs-
      mechanism. -/
  ewsbCoupling : True
  /-- Each sub-interface uses generators from a specific
      adjacent-pair set (σ_2 for W↔Z, σ_4 for Z↔H, both for
      W↔H). -/
  subinterfacesAdjacent : True

/--
  The minimal non-trivial choice Δ_I^minimal := σ_2 · σ_4 · σ_2 —
  a T_{2,3}-shaped interface (single trefoil-like inter-pair
  coupling).

  Whether this realises the physical Higgs-vev is open per
  `conj:categorical-higgs-mechanism` Step C.
-/
class EWInterfaceKnotMinimal
    (R : Type*) [CommRing R] (q : R)
    extends EWInterfaceKnot R q where
  /-- Minimal-choice marker: the interface is σ_2 σ_4 σ_2. -/
  minimal : True

end QOU.BraidsAndKnots
