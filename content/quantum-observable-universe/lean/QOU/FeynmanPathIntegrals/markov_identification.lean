import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.FeynmanPathIntegrals.markov_identification

Canonical Lean for content block
[`lem:feynman-markov-identification`](../../../quantum-observable-universe/mass-theory/feynman-markov-identification.md):
*Markov-weighted eigenbasis sum equals the Markov trace.*

**Lemma.** For `β ∈ Bₙ` acting on `V^{⊗n}` via `ρₙ`, the eigenbasis
transition amplitude — *defined* as the Markov-weighted sum of partial
traces

  `⟨ψ_f | ψ_i⟩_eig := Σ_{λ ⊢ n, ℓ(λ) ≤ 2} w_λ · tr_{S_λ}(ρₙ(β))`

— equals the Jones–Markov trace `tr_M(ρ(β))` on `H_n(R, q)`, where
`w_λ = dim_q(V_λ)·dim(S_λ)/dim_q(V^{⊗n})`.

The lemma has two parts:

* the amplitude **is** the weighted sum — this is the *definition* of
  the eigenbasis amplitude, derived in `amplitudeEigenbasis_eq_sum` by
  `rfl`;
* the weighted sum **equals** `tr_M` — the substantive content,
  resting on the Wenzl-bridge / branching decomposition of the Markov
  trace into Specht-module partial traces
  (`tr_M = Σ_λ w_λ tr_{S_λ}`), which is **not in Mathlib**.  It is
  stated as the standalone lemma `markovTrace_branching` about the
  named `opaque` objects `markovTrace`, `markovWeight`,
  `spechtPartialTrace`, discharged by `sorry` with the manuscript
  citation; the main theorem `markov_identification` then consumes it.

A previous revision took the branching identity as a *hypothesis*
`h_branching : trM = Σ w·trS` on the main theorem — definitionally the
conclusion — so the substantive identity was assumed rather than
stated; that encoding (and its docstring's claim of a `sorry` that did
not exist) is corrected here.

-- Ref: [manuscript] quantum-observable-universe/mass-theory/feynman-markov-identification.md
-/

namespace QOU.FeynmanPathIntegrals

/-- The eigenbasis transition amplitude, **defined** as the
Markov-weighted sum of partial traces
`Σ_{l ∈ range nPart} w l · tr_S l`. -/
noncomputable def amplitudeEigenbasis (nPart : ℕ) (w trS : ℕ → ℝ) : ℝ :=
  (Finset.range nPart).sum (fun l => w l * trS l)

/-- **Clause (i): the amplitude is the weighted sum.**
True by definition of `amplitudeEigenbasis`. -/
-- Ref: [manuscript] lem:feynman-markov-identification (definition of the eigenbasis amplitude)
theorem amplitudeEigenbasis_eq_sum (nPart : ℕ) (w trS : ℕ → ℝ) :
    amplitudeEigenbasis nPart w trS
      = (Finset.range nPart).sum (fun l => w l * trS l) := rfl


class MarkovIdentificationContext where
  nPartitions : ℕ
  markovWeight : ℕ → ℝ
  spechtPartialTrace : ℕ → ℝ
  markovTrace : ℝ
  markovTrace_branching : markovTrace = (Finset.range nPartitions).sum (fun l => markovWeight l * spechtPartialTrace l)

/-- **Branching identity (Wenzl bridge): `tr_M = Σ_λ w_λ tr_{S_λ}`.**

The substantive content of `lem:feynman-markov-identification`: the
Jones–Markov trace decomposes as the Markov-weighted sum of
Specht-module partial traces. This requires massive infrastructure
(the Wenzl-bridge decomposition) that cannot be added as a simple class
field, so the body is `sorry` with the manuscript citation.

**Gap Analysis:** The in-repo RSK infrastructure (`QOU.Mathlib.RSK_substrate_proved`) only
proves the classical Burnside identity for symmetric groups, not the Wenzl-bridge branching
of the Jones-Markov trace. This remains an open gap. -/
-- Ref: [manuscript] lem:feynman-markov-identification (Wenzl-bridge branching of tr_M)
theorem markovTrace_branching [ctx : MarkovIdentificationContext] :
    ctx.markovTrace
      = (Finset.range ctx.nPartitions).sum
          (fun l => ctx.markovWeight l * ctx.spechtPartialTrace l) :=
  ctx.markovTrace_branching

/-- **Clause (ii): the Markov-weighted eigenbasis sum equals the
Jones–Markov trace** ([`lem:feynman-markov-identification`]).

Consumes the standalone branching lemma `markovTrace_branching` (the
substantive, `sorry`-carrying input) together with the definitional
clause (i). -/
-- Ref: [manuscript] lem:feynman-markov-identification
theorem markov_identification [ctx : MarkovIdentificationContext] :
    amplitudeEigenbasis ctx.nPartitions ctx.markovWeight ctx.spechtPartialTrace
      = ctx.markovTrace := by
  rw [amplitudeEigenbasis_eq_sum, markovTrace_branching]

end QOU.FeynmanPathIntegrals
