import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Data.Fintype.Fin
import Mathlib.Data.Real.Basic

/-!
# QOU.BraidKnot.SixTermPerDerivationWeights.binding_assembly

**Canonical declaration** for content block
[`prop:six-term-per-derivation-weights`](../../../quantum-observable-universe/braids-and-knots/six-term-per-derivation-weights.md): *Per-derivation weights for the six-term mass formula*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.BraidKnot.SixTermPerDerivationWeights


/-- Abstract context for the `binding_assembly` claim — manuscript-named
    typed fields below; the atomic mass recovery formula from the six-
    term decomposition is captured as `claim_six_term_recovery`. -/
class BindingAssemblyContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- The atomic mass `𝓜(Z, N)`. -/
  atomic_mass : ℝ
  /-- The six per-derivation weighted contributions (one per spectral-
      sequence term). -/
  term_weights : Fin 6 → ℝ
  /-- Manuscript claim — atomic-mass recovery: the atomic mass is the
      sum of the six per-derivation weighted contributions. -/
  claim_six_term_recovery :
    atomic_mass = (Finset.univ.sum (fun i : Fin 6 => term_weights i))

/-- **Proposition statement** (from manuscript):

The atomic mass $\mathcal{M}(Z, N)$ is recovered from the
[unified six-term decomposition](#thm:six-term-mass-formula-complete)
by

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/six-term-per-derivation-weights.ts
def binding_assembly [ctx : BindingAssemblyContext] :
    ctx.atomic_mass = (Finset.univ.sum (fun i : Fin 6 => ctx.term_weights i)) :=
  ctx.claim_six_term_recovery

end QOU.BraidKnot.SixTermPerDerivationWeights
