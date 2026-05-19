/-!
# QOU.TopologicalMass.cat_transient_localises_blowup — placeholder stub

**Placeholder canonical** for content block
[`lem:topological-mass-cat-transient`](../../../quantum-observable-universe/braids-and-knots/topological-mass-cat-transient.md): *Transient terms localise to blow-up centres (categorical)*.

The full Lean statement and proof are pending; this stub exists so
the `lean.ref` URI `qou:QOU.TopologicalMass.cat_transient_localises_blowup` resolves to a real declaration in
the `qou` Lake package.  The body is `sorry` carrying the
manuscript citation per CLAUDE.md §1.
-/

namespace QOU.TopologicalMass


/-- Abstract context for the `cat_transient_localises_blowup` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class CatTransientLocalisesBlowupContext where
  /-- Fluid-dynamics velocity / vorticity field. -/
  VelocityField : Type
  /-- The `Prop`-valued claim of the lemma. -/
  claim_cat_transient_localises_blowup : Prop

/-- **Lemma statement** (from manuscript):

The transient component $\alpha - \hat{\tau}_n(\alpha) \in
\mathcal{A}_{n+1}^{\mathrm{trans}}$ has support contained in the
union of the kernels of $\mathfrak{d}_{n+1}$ at the blow-up centres
$p_1, \ldots, p_N$, and the transient trace decomposes as a sum of
disjoint local contributions:

    The Lean encoding below is a `theorem foo : True := by sorry` placeholder;
    upgrading requires choosing the appropriate Lean types and translating
    the manuscript claim above. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/topological-mass-cat-transient.ts
theorem cat_transient_localises_blowup [ctx : CatTransientLocalisesBlowupContext] : ctx.claim_cat_transient_localises_blowup := by
  -- Manuscript proof referenced above; concretisation requires
  -- type-level Lean translation of the hypotheses.
  sorry

end QOU.TopologicalMass
