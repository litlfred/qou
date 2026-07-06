import Mathlib.Data.Real.Basic

/-!
# `conj:cpt-d6-d7-d8-closure` — CPT closure compound conjecture

Parent conjecture for the discrete-symmetry trio (D6 + D7 + D8).
Each component (`conj:c-from-color-flavor-swap`,
`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`) names
a QOU-canonical realisation of one symmetry; the **joint**
statement is that they compose to give CPT preservation of the
Markov trace.

Axiomatised as a Lean class per AGENTS.md §3b-cond.  Downstream
blocks that need CPT-closure as a hypothesis take this class as
`[CPTD6D7D8Closure]`.
-/

namespace QOU.ParticleInteractions.CPTD6D7D8Closure

/-- The CPT-closure compound conjecture, as a class.

    Existence of `C`, `P`, `T` actions on closed-braid
    representatives such that `C · P · T` preserves the Markov
    trace.  The three components (D6 / D7 / D8) live in their
    respective component files; here we just record the
    composite. -/
class CPTD6D7D8Closure where
  /-- The closed-braid representative space (carrier of the Markov
      trace), abstracted to a generic type to avoid committing to a
      specific braid encoding here. -/
  ClosedBraid : Type
  /-- The Markov trace `tr_M : ClosedBraid → ℝ` (the Jones invariant). -/
  markovTrace : ClosedBraid → ℝ
  /-- The joint CPT composite `C · P · T` acting on closed-braid
      representatives (D6 charge-conjugation ∘ D7 parity ∘ D8 time
      reversal). -/
  cptComposite : ClosedBraid → ClosedBraid
  /-- **The conjecture itself** (D6 + D7 + D8 joint closure): the CPT
      composite preserves the Markov trace on every closed braid.
      `sorry` in any concrete instance is understood as conjecture
      per AGENTS.md §3b. -/
  cpt_trace_preserved : ∀ b : ClosedBraid, markovTrace (cptComposite b) = markovTrace b

/-- Restatement marker: `cpt_closure` names the proposition
    `conj:cpt-d6-d7-d8-closure` from the .ts manifest — the joint
    CPT-invariance of the Markov trace, derived directly from the
    class field. -/
def cpt_closure [inst : CPTD6D7D8Closure] :
    ∀ b : inst.ClosedBraid, inst.markovTrace (inst.cptComposite b) = inst.markovTrace b :=
  -- Ref: [manuscript] prop:cpt-orbit-closure-density (substrate-side density)
  -- Ref: [manuscript] def:bar-involution (categorical CPT building block)
  -- Ref: [wigner1937], [jones1987], [kassel1995]
  inst.cpt_trace_preserved

end QOU.ParticleInteractions.CPTD6D7D8Closure
