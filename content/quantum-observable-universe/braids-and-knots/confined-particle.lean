/-!
# QOU.BraidKnot.ConfinedParticle

A confined particle is a tuple (name, level, Markov-class of closed
braid, coarse strand count). Named via a registry
(particle-shortcut); Markov class represented canonically by
Gröbner–Shirshov normal form. Confinement at q is a separate
SDP-feasibility predicate.

LaTeX: `\label{def:confined-particle}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- A Markov-equivalence class of closed braids in `H_n(q)`,
    represented canonically by its Gröbner-Shirshov normal form. -/
-- Ref: [manuscript] braids-and-knots/hecke-normal-form
structure MarkovClass where
  /-- Canonical GS-NF representative as a formal word. -/
  gsNormalForm : String
  /-- Strand count `n` of the closed braid. -/
  strandCount : ℕ

/-- **Confined particle.** A named tuple at a confinement level
    with an underlying Markov-class of closed braid and coarse
    strand count. Stability predicates layer on top. -/
-- Ref: [manuscript] braids-and-knots/confined-particle
structure ConfinedParticle where
  /-- Symbol from the particle-shortcut registry (e.g. `proton`, `\He4`). -/
  name : String
  /-- Confinement level ℓ (quark = 0, nucleon = 1, atom = 2, molecule = 3). -/
  level : ℕ
  /-- Canonical Markov class of the closed braid. -/
  markovClass : MarkovClass
  /-- Coarse strand count `n₀` at level `ℓ`. -/
  coarseStrands : ℕ

/-- Confinement predicate: `confined P q` holds iff the
    [confinement SDP](#prop:confinement-sdp) at `P` is
    Slater-strictly feasible at the substrate parameter `q`. -/
-- Ref: [manuscript] particle-interactions/confinement-sdp
opaque confined : ConfinedParticle → ℝ → Prop

end QOU.BraidKnot
