/-!
# QOU.LiftingDescent.tm_transient_localisation — placeholder stub

**Placeholder canonical** for content block
[`lem:topological-mass-transient-localisation`](../../../quantum-observable-universe/lifting-and-descent/topological-mass-transient-localisation.md): *Transient terms localise to exceptional divisors*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.LiftingDescent.tm_transient_localisation` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per CLAUDE.md §1.
-/

namespace QOU.LiftingDescent


/-- Abstract context for the `tm_transient_localisation` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class TmTransientLocalisationContext where
  /-- Fluid-dynamics velocity / vorticity field. -/
  VelocityField : Type
  /-- The `Prop`-valued claim of the lemma. -/
  holds : Prop

/-- **Lemma statement** (from manuscript):

The transient component $\alpha - \hat{\tau}_n(\alpha)$ has support
contained in disjoint discs $D_i$ centred at the blow-up points
$p_1, \ldots, p_N$, and the norm of the multiplicative integral
decomposes as a sum over the exceptional divisors $E_i$:

    The Lean encoding below is a `theorem foo : True := by sorry` placeholder;
    upgrading requires choosing the appropriate Lean types and translating
    the manuscript claim above. -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/topological-mass-transient-localisation.ts
theorem tm_transient_localisation [ctx : TmTransientLocalisationContext] : ctx.holds := by
  -- Manuscript proof referenced above; concretisation requires
  -- type-level Lean translation of the hypotheses.
  sorry

end QOU.LiftingDescent
