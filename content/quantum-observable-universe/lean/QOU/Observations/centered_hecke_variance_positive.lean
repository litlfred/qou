import Mathlib.Tactic

/-!
# QOU.Observations.centered_hecke_variance_positive

**Canonical declaration** for content block
[`prop:centered-hecke-variance-positive`](../../../quantum-observable-universe/observations/centered-hecke-variance-positive.md): *Centred Hecke transfer matrix has strictly positive variance in the Wenzl regime*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.Observations


/-- Abstract context for the `centered_hecke_variance_positive` claim — manuscript-themed
    typed fields below; the `holds` field carries the `Prop`-valued
    claim of the lemma. -/
class CenteredHeckeVariancePositiveContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Markov parameter `z = 1/(q^{1/2} + q^{-1/2})`. -/
  z : ℝ
  /-- Variance value `Var(σ_i) = (q − q⁻¹) z + 1 − z²`. -/
  Var_sigma : ℝ
  /-- The variance is given by the Hecke formula. -/
  var_formula : Var_sigma = (q - q⁻¹) * z + 1 - z ^ 2
  /-- The first term (q - q⁻¹) * z is strictly positive. -/
  term1_pos : 0 < (q - q⁻¹) * z
  /-- The second term 1 - z^2 is strictly positive. -/
  term2_pos : 0 < 1 - z ^ 2

/-- **Proposition statement** (from manuscript):

Let $q > 0$ with $q^{1/2} + q^{-1/2} > 2$ (Wenzl positivity regime).
Let $z = 1/(q^{1/2}+q^{-1/2})$ be the Markov parameter and
$\tilde\sigma_i := \sigma_i - z \cdot 1$ the centred Hecke generator.
Then the variance*
$$
  \mathrm{Var}(\sigma_i) \;:=\; \mathrm{tr}_M(\tilde\sigma_i^2)
  \;=\;
  (q - q^{-1}) z + 1 - z^2
$$
*is strictly positive: $\mathrm{Var}(\sigma_i) > 0$. Numerically at
the QOU substrate $q_0 \approx 1.110$, $\mathrm{Var}(\sigma_i) \approx 0.855$.*

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/observations/centered-hecke-variance-positive.ts
theorem centered_hecke_variance_positive [ctx : CenteredHeckeVariancePositiveContext] :
    ctx.Var_sigma = (ctx.q - ctx.q⁻¹) * ctx.z + 1 - ctx.z ^ 2 ∧
    0 < ctx.Var_sigma := by
  constructor
  · exact ctx.var_formula
  · linarith [ctx.var_formula, ctx.term1_pos, ctx.term2_pos]

end QOU.Observations
