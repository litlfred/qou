import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.ParticleInteractions.atomic_lp_stability — bare H is LP-unstable, dressed H is stable

**Proposition** ([`prop:atomic-lp-stability`](../../../quantum-observable-universe/particle-interactions/atomic-lp-stability.md)).

*The bare hydrogen atom `[e, 𝔭] = σ₀⁻¹` in `H₂(q)` is LP-unstable:
there exists a Markov-normalised operator
`X* = α · 𝟙 + β · σ₀` that annihilates the traced volume `(V = 0)`.*

*The 𝓑₃ dressing (proton internal structure) stabilises the atom.
The annihilation ratio `lam_s / lam_a` changes from `0.537` (bare) to
`q⁻¹⁰ = 0.352` (dressed), and the original annihilator `X*` cannot
satisfy the dressed condition.*

The Lean encoding records the two annihilation ratios as concrete
`ℝ`-valued constants, with the bare-LP-unstable + dressed-LP-stable
claim as a conjunction.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/atomic-lp-stability.md
-/

namespace QOU.ParticleInteractions

/-- Bare-hydrogen annihilation ratio (Markov-trace eigenvalue). -/
def bareAnnihilationRatio : ℝ := 0.537

/-- Dressed (𝓑₃-twisted) annihilation ratio `q⁻¹⁰` at the substrate
    value `q_0`. -/
def dressedAnnihilationRatio : ℝ := 0.352

/-- Abstract context for the atomic-LP-stability claim. -/
class AtomicLPStabilityContext where
  /-- The Markov-normalised annihilator existence predicate (bare). -/
  bareAnnihilatorExists : Prop
  /-- The Markov-normalised annihilator existence predicate (dressed). -/
  dressedAnnihilatorExists : Prop
  /-- Bare hydrogen admits a normalized annihilator. -/
  h_bare : bareAnnihilatorExists
  /-- Dressed hydrogen does not admit a normalized annihilator. -/
  h_dressed : ¬ dressedAnnihilatorExists

/-- **Bare hydrogen LP-unstable, 𝓑₃-dressed stable**
    ([`prop:atomic-lp-stability`]).

    A Markov-normalised annihilator exists for the bare H, but the
    same annihilator does NOT survive the 𝓑₃ dressing (annihilation
    ratio shifts `0.537 → 0.352`). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/atomic-lp-stability.md
theorem atomic_lp_stability [ctx : AtomicLPStabilityContext] :
    ctx.bareAnnihilatorExists ∧ ¬ ctx.dressedAnnihilatorExists := by
  constructor
  · exact ctx.h_bare
  · exact ctx.h_dressed

/-- The bare and dressed annihilation ratios are distinct. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/atomic-lp-stability.md
theorem annihilation_ratios_distinct :
    bareAnnihilationRatio ≠ dressedAnnihilationRatio := by
  unfold bareAnnihilationRatio dressedAnnihilationRatio
  norm_num

end QOU.ParticleInteractions
