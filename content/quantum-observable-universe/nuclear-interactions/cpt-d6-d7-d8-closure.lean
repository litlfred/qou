import Mathlib.Data.Real.Basic

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
`[CPTClosure]`.
-/

namespace QOU.ParticleInteractions.CPTClosure

/-- The CPT-closure compound conjecture, as a class.

    Existence of `C`, `P`, `T` actions on closed-braid
    representatives such that `C · P · T` preserves the Markov
    trace.  The three components live in their
    respective component files; here we just record the
    composite. -/
class CPTClosure where
  /-- The closed-braid representative space (carrier of the Markov
      trace), abstracted to a generic type to avoid committing to a
      specific braid encoding here. -/
  ClosedBraid : Type
  /-- The Markov trace `tr_M : ClosedBraid → ℝ` (the Jones invariant). -/
  markovTrace : ClosedBraid → ℝ
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
def cpt_closure [inst : CPTClosure] :
    ∀ b : inst.ClosedBraid, inst.markovTrace (inst.cptComposite b) = inst.markovTrace b :=
  -- Ref: [manuscript] prop:cpt-orbit-closure-density (substrate-side density)
  -- Ref: [manuscript] def:bar-involution (categorical CPT building block)
  -- Ref: [wigner1937], [jones1987], [kassel1995]
  inst.cpt_trace_preserved

end QOU.ParticleInteractions.CPTClosure
