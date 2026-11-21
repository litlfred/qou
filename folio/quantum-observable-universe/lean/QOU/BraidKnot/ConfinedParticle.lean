import QOU.Archimedean.HeckeRep
import QOU.Archimedean.GroundRing
import QOU.Interactions.ConfinementSDP

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

namespace QOU.BraidKnot

open QOU.Archimedean

/-- **Markov class.** Equivalence class of closed braids under
    Markov moves, represented canonically by its Gröbner–Shirshov
    normal form as a `BraidWord n`.

    Two closed braids that are Markov-equivalent share the same
    canonical representative. The `strandCount` field is the `n` of
    the underlying `BraidWord n`. -/
-- Ref: [leitner2026] braids-and-knots/hecke-normal-form
structure MarkovClass where
  /-- Number of strands of the canonical representative. -/
  strandCount : ℕ
  /-- The canonical GS-NF representative as a Hecke braid word. -/
  gsNormalForm : BraidWord strandCount

/-- **Confined particle.** A named tuple at a confinement level
    with an underlying Markov class of closed braid. Stability
    predicates layer on top; confinement at `q ∈ R_q` is the
    SDP-feasibility predicate.

    Note: the coarse strand count is derived from the Markov class
    rather than stored separately, so well-formedness
    (`coarseStrands = markovClass.strandCount`) holds by definition. -/
-- Ref: [leitner2026] braids-and-knots/confined-particle
structure ConfinedParticle where
  /-- Symbol from the particle-shortcut registry
      (e.g. `"proton"`, `"\\He4"`, `"electron"`). -/
  name : String
  /-- Confinement level ℓ (quark = 0, nucleon = 1, atom = 2,
      compound = 3). -/
  level : ℕ
  /-- Canonical Markov class of the underlying closed braid. -/
  markovClass : MarkovClass

namespace ConfinedParticle

/-- Coarse strand count `n₀` at level ℓ — derived from the Markov
    class so well-formedness holds definitionally. -/
def coarseStrands (P : ConfinedParticle) : ℕ :=
  P.markovClass.strandCount

end ConfinedParticle

/-- Confinement predicate on a particle at a parameter value. The
    semantic content (`confined P q ↔ Slater-strict SDP feasibility
    at (P, q)`) is supplied per-instance via `HasConfinementWitness`
    below; the ambient predicate is just a typeclass accessor. -/
-- Ref: [leitner2026] particle-interactions/confinement-sdp
class HasConfinementWitness (P : ConfinedParticle) where
  /-- The confinement predicate at parameter `q`. -/
  confined : R_q → Prop

/-- Confinement predicate accessor. -/
def confined (P : ConfinedParticle) [h : HasConfinementWitness P] (q : R_q) :
    Prop :=
  h.confined q

/-- **Coarse-strand correctness** — proved by definition.
    The earlier `WellFormedConfinedParticle` typeclass is no longer
    needed: `coarseStrands` is now a derived projection through the
    Markov class, so the equality holds by `rfl`. -/
-- Ref: [leitner2026] braids-and-knots/confined-particle
theorem coarseStrands_eq_markov_strands (P : ConfinedParticle) :
    P.coarseStrands = P.markovClass.strandCount := rfl

end QOU.BraidKnot
