import Mathlib.Algebra.Ring.Defs

/-!
# `conj:cpt-d6-d7-d8-closure` — CPT closure compound conjecture

Parent conjecture for the discrete-symmetry trio: charge
conjugation, parity, and time reversal.
Each component (`conj:c-from-color-flavor-swap`,
`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`) names
a QOU-canonical realisation of one symmetry; the **joint**
statement is that they compose to give CPT preservation of the
Markov trace.

Axiomatised as a Lean class with no instance.  Downstream
blocks that need CPT-closure as a hypothesis take this class as
`[CPTClosure R]`.

**Base ring (AGENTS.md §7c).** The Markov trace is the Jones invariant,
whose home is the Laurent ring $\mathbb{Z}[q, q^{-1}]$ — not the
archimedean completion.  The trace codomain is therefore a generic
`(R : Type*) [CommRing R]`, and the file never mentions `ℝ`.  An
archimedean evaluation of the invariant at the substrate $q_0$ is the
instantiation `R := ℝ`, which belongs on the observation side of the
substrate→archimedean wall.

`CommRing` is documentation of the invariant's actual home rather than
a proof obligation: the closure statement below is an equation between
two trace *values*, so it would type-check over a bare `Type`.  The
component conjectures (`conj:c-from-color-flavor-swap`,
`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`) do use the
ring structure — the bar involution $q \mapsto q^{-1}$ and the skein
relation — so weakening past `CommRing` would misname the object.
-/

namespace QOU.ParticleInteractions

/-- The CPT-closure compound conjecture, as a class.

    Existence of `C`, `P`, `T` actions on closed-braid
    representatives such that `C · P · T` preserves the Markov
    trace.  The three components live in their
    respective component files; here we just record the
    composite. -/
class CPTClosure (R : Type*) [CommRing R] where
  /-- The closed-braid representative space (carrier of the Markov
      trace), abstracted to a generic type to avoid committing to a
      specific braid encoding here. -/
  ClosedBraid : Type
  /-- The Markov trace `tr_M : ClosedBraid → R` (the Jones invariant),
      valued in the generic coefficient ring `R` — canonically
      $\mathbb{Z}[q, q^{-1}]$, never `ℝ`. -/
  markovTrace : ClosedBraid → R
  /-- The joint CPT composite `C · P · T` acting on closed-braid
      representatives (charge conjugation ∘ parity ∘ time
      reversal). -/
  cptComposite : ClosedBraid → ClosedBraid
  /-- **The conjecture itself** (joint closure of the three symmetries):
      the CPT composite preserves the Markov trace on every closed
      braid.  No instance is supplied; the class is the conjecture. -/
  cpt_trace_preserved : ∀ b : ClosedBraid, markovTrace (cptComposite b) = markovTrace b

/-- Restatement marker: `cpt_closure` names the proposition
    `conj:cpt-d6-d7-d8-closure` from the .ts manifest — the joint
    CPT-invariance of the Markov trace, derived directly from the
    class field. -/
def cpt_closure {R : Type*} [CommRing R] [inst : CPTClosure R] :
    ∀ b : inst.ClosedBraid, inst.markovTrace (inst.cptComposite b) = inst.markovTrace b :=
  -- Ref: [manuscript] prop:cpt-orbit-closure-density (substrate-side density)
  -- Ref: [manuscript] def:bar-involution (categorical CPT building block)
  -- Ref: [wigner1937], [jones1987], [kassel1995]
  inst.cpt_trace_preserved

end QOU.ParticleInteractions
