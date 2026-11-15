import QOU.Basic


/-!
# QOU.BraidKnot.ConfinedParticle

A confined particle is a tuple (name, level, Markov-class of closed
braid, coarse strand count). Named via a registry
(particle-shortcut); Markov class represented canonically by
Gröbner–Shirshov normal form. Confinement at q is a separate
SDP-feasibility predicate.

LaTeX: `\label{def:confined-particle}`
-/

namespace QOU.BraidKnot

universe u

/-- A Markov-equivalence class of closed braids in `H_n(q)`,
    represented canonically by its Gröbner-Shirshov normal form. -/
-- Ref: [leitner2026] braids-and-knots/hecke-normal-form
structure MarkovClass where
  /-- Canonical GS-NF representative as a formal word. -/
  gsNormalForm : String
  /-- Strand count `n` of the closed braid. -/
  strandCount : ℕ

/-- **Confined particle.** A named tuple at a confinement level
    with an underlying Markov-class of closed braid and coarse
    strand count. Stability predicates layer on top. -/
-- Ref: [leitner2026] braids-and-knots/confined-particle
structure ConfinedParticle where
  /-- Symbol from the particle-shortcut registry (e.g. `proton`, `\He4`). -/
  name : String
  /-- Confinement level ℓ (quark = 0, nucleon = 1, atom = 2, molecule = 3). -/
  level : ℕ
  /-- Canonical Markov class of the closed braid. -/
  markovClass : MarkovClass
  /-- Coarse strand count `n₀` at level `ℓ`. -/
  coarseStrands : ℕ

/-! ### The `confined` predicate was removed 2026-09-02

This file used to close with

    /-- ... **Concrete model**: every particle is confined at every `q`.
        The genuine SDP-feasibility predicate lives in
        `particle-interactions/confinement-sdp`; this stub provides a
        Lean-verifiable surrogate so downstream theorems can close. -/
    def confined : ConfinedParticle → ℝ → Prop := fun _ _ => True

The docstring is candid about the value — *"every particle is confined at
every `q`"* — but its stated **purpose** was false: nothing downstream used
it. Measured 2026-09-02 across every `.lean` in `content/`, the sole
application of a `confined P q` is
[`confinement-phase-stratification.lean`](confinement-phase-stratification.lean),
which declares its **own** `opaque confined : ConfinedParticleTy → ℝ → Prop`
— a different declaration on a different type — and content-block siblings do
not import one another, so it never reached this one.

So this was a `Prop`-valued definition equal to `True`, justified by a
downstream that did not exist. It is deleted rather than kept as a surrogate.

**The block is unaffected.** `def:confined-particle`'s `lean.ref` is
`qou:QOU.BraidKnot.ConfinedParticle` — the **structure** above, which is real
data and is untouched.

**And `opaque` is the right shape for the other one.** An `opaque` predicate
asserts nothing and *cannot* be unfolded to `True`, so a theorem quantified
over it stays falsifiable. That is the honest form of "the genuine predicate
lives elsewhere"; `:= fun _ _ => True` is not.

Bean `qou-z9ws`. -/

end QOU.BraidKnot
