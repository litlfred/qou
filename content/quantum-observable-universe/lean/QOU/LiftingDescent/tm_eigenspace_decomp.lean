import Mathlib.Tactic

/-!
# QOU.LiftingDescent.tm_eigenspace_decomp

**Canonical declaration** for content block
[`lem:topological-mass-eigenspace-decomp`](../../../quantum-observable-universe/lifting-and-descent/topological-mass-eigenspace-decomp.md): *Eigenspace decomposition of the mass integrand (descent involution)*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.LiftingDescent


/-- Abstract context for the `tm_eigenspace_decomp` claim — manuscript-named
    typed fields below. -/
class TmEigenspaceDecompContext where
  /-- Multiplicative-integral norm `‖MI(α)‖`. -/
  MI_alpha : ℝ
  /-- Descended-component norm `‖MI(α_desc)‖`. -/
  MI_desc : ℝ
  /-- Transient-component norm `‖MI(α_trans)‖`. -/
  MI_trans : ℝ
  /-- Killing-form orthogonality -/
  killing_orthogonal : Prop
  /-- Multiplicative-integral additivity -/
  mi_additive : Prop
  /-- Witness for Killing-form orthogonality -/
  h_killing_orthogonal : killing_orthogonal
  /-- Witness for Multiplicative-integral additivity -/
  h_mi_additive : mi_additive
  /-- These two properties imply the norm additivity -/
  additivity_of_orthogonal : killing_orthogonal → mi_additive → MI_alpha = MI_desc + MI_trans

/-- **Lemma statement** (from manuscript):

Let $\alpha = (\nabla_A q, L \wedge F^+)$ be the integrand of the
mass identity for a vortex $\varrho$, and let $\hat{\tau}_n$ be the
descent involution.  The Killing-form orthogonality of
$\mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
together with multiplicative-integral additivity over orthogonal
direct sums gives

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/topological-mass-eigenspace-decomp.ts
theorem tm_eigenspace_decomp [ctx : TmEigenspaceDecompContext] :
    ctx.MI_alpha = ctx.MI_desc + ctx.MI_trans :=
  ctx.additivity_of_orthogonal ctx.h_killing_orthogonal ctx.h_mi_additive

end QOU.LiftingDescent
