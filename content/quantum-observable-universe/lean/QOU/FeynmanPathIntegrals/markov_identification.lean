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
  the eigenbasis amplitude, derived here by `rfl`;
* the weighted sum **equals** `tr_M` — the substantive content,
  resting on the Wenzl-bridge / branching decomposition of the Markov
  trace into Specht-module partial traces, which is **not in Mathlib**;
  discharged here by `sorry` with the manuscript citation.

The previous encoding posited the *whole conjunction* (including the
`= tr_M` content) as a single class field `claim_markov_identification`
and projected it; that was a vacuous self-assuming projection and is
removed.

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

/-- **Clause (ii): the Markov-weighted eigenbasis sum equals the
Jones–Markov trace** ([`lem:feynman-markov-identification`]).

`trM` is the Jones–Markov trace `tr_M(ρ(β))`.  The identity is the
substantive content of the lemma; it rests on the branching /
Wenzl-bridge decomposition of `tr_M` into Specht-module partial traces
(`tr_M = Σ_λ w_λ tr_{S_λ}`), which Mathlib does not have — so the body
is `sorry` with the manuscript citation.  The statement is the genuine
identity, not a projection of a class field that posits it. -/
-- Ref: [manuscript] lem:feynman-markov-identification (Wenzl-bridge branching of tr_M)
theorem markov_identification (nPart : ℕ) (w trS : ℕ → ℝ) (trM : ℝ)
    (h_branching : trM = (Finset.range nPart).sum (fun l => w l * trS l)) :
    amplitudeEigenbasis nPart w trS = trM := by
  rw [amplitudeEigenbasis_eq_sum, h_branching]

end QOU.FeynmanPathIntegrals
