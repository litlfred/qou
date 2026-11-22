/-
# The α_EM B2 wall needs only reality + symmetry — not the Gram/PSD structure

`QOU.Archimedean.HodgeGramLift` tightened the per-loop B2 lift
(`TauRhoHodgeLift`) to the single open identification

    `LoopWeightIsHodgeGram W  :=  ∃ B : Matrix (Fin g) (Fin g) ℝ, W = complexify (Bᵀ * B)`

— "the categorical α_EM loop weight `W` on `H^{1,0}(Bring)` is a complexified real
**Hodge Gram** `Bᵀ·B`." A Gram matrix is real symmetric **and** positive-
semidefinite. This file observes — and proves sorry-free — that the positivity is
**not needed** for the B2 lift: the class fields (`hermitian`, `conjugated`) are
discharged by `HodgeGramLift.hodgeSymmLift` from **any real symmetric** matrix, so
the genuinely-required premise is strictly weaker:

    `LoopWeightIsRealSymm W  :=  ∃ M : Matrix (Fin g) (Fin g) ℝ, M.IsSymm ∧ W = complexify M`

and `LoopWeightIsHodgeGram W → LoopWeightIsRealSymm W → TauRhoHodgeLift`.

**Why this advances the wall (honestly).** The open categorical input shrinks from
"the loop weight is a real symmetric *positive-semidefinite* Gram" to just "the loop
weight is **real and symmetric**." Both are the *derivable* Hecke-side properties —
reality from the seminormal / Young-orthogonal representations at the real substrate
`q₀`, symmetry from the Markov-trace bilinear form — and the harder **positivity**
(Wenzl's positive Markov trace, the compact real form) is a *bonus*, not a
requirement. So a future discharge of the wall need only exhibit the loop weight as
`complexify` of a real symmetric matrix; it need not also prove positive-
semidefiniteness.

STRICT (§"Axiomatization is NOT a Proof"): no `TauRhoHodgeLift` instance is
registered for the *actual* α_EM loop weight. The τ-identification `W = complexify
(real symmetric Markov weight)` is still the open categorical input — here only
weakened in form, never fabricated. `1/(8π)` stays a phase-4 identification; nothing
is wired.

-- Ref: [leitner2026] prop:em-coupling-bring-zero-mode
-- Ref: [voisin2002] https://doi.org/10.1017/CBO9780511615344
-/
import QOU.Archimedean.HodgeGramLift

namespace QOU.Archimedean.LoopWeightRealSymmReduction

open Matrix
open QOU.Archimedean.HodgeGramLift
open QOU.Archimedean.TauRhoHodgeLiftInterface

variable {g : ℕ}

/-- **The minimal B2 premise: the loop weight is real and symmetric.** Strictly
weaker than `LoopWeightIsHodgeGram` (no positive-semidefiniteness). -/
def LoopWeightIsRealSymm (W : Matrix (Fin g) (Fin g) ℂ) : Prop :=
  ∃ M : Matrix (Fin g) (Fin g) ℝ, M.IsSymm ∧ W = complexify M

/-- **Wall-weakening (sorry-free).** Real + symmetric already instantiates the B2
lift — positivity is not used. If the loop weight is the complexification of a real
symmetric matrix, then `TauRhoHodgeLift` holds for it (with `Wbar = W`). -/
theorem tauRhoHodgeLift_of_realSymm {W : Matrix (Fin g) (Fin g) ℂ}
    (h : LoopWeightIsRealSymm W) : Nonempty (TauRhoHodgeLift g W W) := by
  obtain ⟨M, hSymm, hW⟩ := h
  subst hW
  exact ⟨hodgeSymmLift hSymm⟩

/-- **The Gram premise is strictly stronger.** `LoopWeightIsHodgeGram` (a Hodge Gram
`Bᵀ·B`) implies `LoopWeightIsRealSymm` (real symmetric), since `Bᵀ·B` is symmetric
(`gram_isSymm`). So the positivity carried by the Gram framing is surplus to the B2
lift's requirement. -/
theorem loopWeightIsHodgeGram_imp_realSymm {W : Matrix (Fin g) (Fin g) ℂ}
    (h : LoopWeightIsHodgeGram W) : LoopWeightIsRealSymm W := by
  obtain ⟨B, hW⟩ := h
  exact ⟨Bᵀ * B, gram_isSymm B, hW⟩

/-- **Consistency:** the weakened route reproduces the Gram route's conclusion.
Chaining the implication with `tauRhoHodgeLift_of_realSymm` gives the same B2 lift
that `HodgeGramLift.tauRhoHodgeLift_of_loopWeightIsHodgeGram` produces — via the
strictly weaker hypothesis. -/
theorem tauRhoHodgeLift_of_loopWeightIsHodgeGram' {W : Matrix (Fin g) (Fin g) ℂ}
    (h : LoopWeightIsHodgeGram W) : Nonempty (TauRhoHodgeLift g W W) :=
  tauRhoHodgeLift_of_realSymm (loopWeightIsHodgeGram_imp_realSymm h)

end QOU.Archimedean.LoopWeightRealSymmReduction
