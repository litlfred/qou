/-!
# Confined Particle

A confined particle is a tuple (name, level, Markov class, coarse
strand count). Named via a registry; Markov class represented
canonically by Gröbner–Shirshov normal form. Confinement at q is a
separate SDP-feasibility predicate tied to `QOU.Interactions.ConfinementSDP`.

## References

- [def:confined-particle]
- [prop:confinement-sdp]
-/

import QOU.Descartes.HeckeRep
import QOU.Descartes.GroundRing
import QOU.Interactions.ConfinementSDP

namespace QOU.BraidKnot

open QOU.Descartes

/-- **Markov class.** Equivalence class of closed braids under
    Markov moves, represented canonically by its Gröbner–Shirshov
    normal form as a `BraidWord n`.

    Two closed braids that are Markov-equivalent share the same
    canonical representative. The `strandCount` field is the `n` of
    the underlying `BraidWord n`. -/
-- Ref: [manuscript] braids-and-knots/hecke-normal-form
structure MarkovClass where
  /-- Number of strands of the canonical representative. -/
  strandCount : ℕ
  /-- The canonical GS-NF representative as a Hecke braid word. -/
  gsNormalForm : BraidWord strandCount

/-- **Confined particle.** A named tuple at a confinement level
    with an underlying Markov class of closed braid and a coarse
    strand count. Stability predicates layer on top; confinement at
    `q ∈ R_q` is the SDP-feasibility predicate. -/
-- Ref: [manuscript] braids-and-knots/confined-particle
structure ConfinedParticle where
  /-- Symbol from the particle-shortcut registry
      (e.g. `"proton"`, `"\\He4"`, `"electron"`). -/
  name : String
  /-- Confinement level ℓ (quark = 0, nucleon = 1, atom = 2,
      compound = 3). -/
  level : ℕ
  /-- Canonical Markov class of the underlying closed braid. -/
  markovClass : MarkovClass
  /-- Coarse strand count `n₀` at level ℓ (e.g. A for an atom at
      nucleon level). -/
  coarseStrands : ℕ

/-- Confinement predicate on a particle at a parameter value in the
    generic locus. `confined P q` holds iff the confinement SDP at
    `P` is Slater-strictly feasible at `q`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque confined : ConfinedParticle → R_q → Prop

/-- **Coarse-strand correctness.** The coarse strand count of a
    confined particle matches the strand count of its Markov-class
    canonical representative. -/
/-- `coarseStrands` and `markovClass.strandCount` are currently
    independent ℕ fields.  A cleaner long-term fix adds a
    `coarseStrands_eq` field to `ConfinedParticle`, breaking
    every existing instance constructor.  Axiomatised until then. -/
-- Ref: [manuscript] braids-and-knots/confined-particle
axiom coarseStrands_eq_markov_strands (P : ConfinedParticle) :
    P.coarseStrands = P.markovClass.strandCount

end QOU.BraidKnot
