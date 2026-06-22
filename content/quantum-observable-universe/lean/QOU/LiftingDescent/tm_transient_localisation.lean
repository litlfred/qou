import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.LiftingDescent.tm_transient_localisation

**Placeholder canonical** for content block
[`lem:topological-mass-transient-localisation`](../../../quantum-observable-universe/lifting-and-descent/topological-mass-transient-localisation.md): *Transient terms localise to exceptional divisors*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.LiftingDescent.tm_transient_localisation` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per AGENTS.md §1.
-/

namespace QOU.LiftingDescent


/-- Abstract context for the `tm_transient_localisation` claim — manuscript-themed
    typed fields below. -/
class TmTransientLocalisationContext where
  /-- Number of blow-up points `N`. -/
  N : ℕ
  /-- Norm of the multiplicative integral on disc `D_i`. -/
  MI_norm : ℕ → ℝ
  /-- Norm of the total transient multiplicative integral. -/
  MI_norm_total : ℝ
  /-- Disjoint support condition -/
  disjoint_support : Prop
  /-- Additivity over disjoint support -/
  additivity_over_disjoint : Prop
  /-- Witness for disjoint support -/
  h_disjoint_support : disjoint_support
  /-- Witness for additivity -/
  h_additivity : additivity_over_disjoint
  /-- Together, these imply the sum decomposition -/
  sum_of_disjoint : disjoint_support → additivity_over_disjoint →
    MI_norm_total = (Finset.range N).sum (fun i => MI_norm i)

/-- **Lemma statement** (from manuscript):

The transient component $\alpha - \hat{\tau}_n(\alpha)$ has support
contained in disjoint discs $D_i$ centred at the blow-up points
$p_1, \ldots, p_N$, and the norm of the multiplicative integral
decomposes as a sum over the exceptional divisors $E_i$:

    The Lean encoding below is a `theorem … : ctx.holds := by sorry` placeholder (the actual claim type sits on the context class);
    upgrading requires choosing the appropriate Lean types and translating
    the manuscript claim above. -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/topological-mass-transient-localisation.ts
theorem tm_transient_localisation [ctx : TmTransientLocalisationContext] :
    ctx.MI_norm_total = (Finset.range ctx.N).sum (fun i => ctx.MI_norm i) :=
  sorry

end QOU.LiftingDescent
