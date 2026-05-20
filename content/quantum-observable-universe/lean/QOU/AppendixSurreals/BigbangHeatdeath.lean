/-!
# QOU.AppendixSurreals.BigbangHeatdeath — conjectural class (placeholder)

**§3b-cond class axiomatisation** for content block
[`conj:bigbang-heatdeath`](../../../quantum-observable-universe/appendix-surreals/bigbang-heatdeath.md): *Big Bang and heat-death functors as evaluations at named surreal endpoints*.

This is a **conjecture**: the class `BigbangHeatdeath` carries a placeholder
field; the `noncomputable instance` is the conjectural witness whose
`sorry` represents the open conjecture itself (per CLAUDE.md §3b),
NOT a missing proof.  Downstream theorems may take
`[BigbangHeatdeath]` as an explicit `[Instance]` hypothesis to derive
unconditional Lean theorems modulo this single conjectural input
(per §3b-cond).

The field schema below is a structural placeholder; refine the
fields to match the conjecture's actual content as the
formalisation matures.
-/

namespace QOU.AppendixSurreals

/-- Big Bang and heat-death functors as evaluations at named surreal endpoints

    Conjectural class — see [`conj:bigbang-heatdeath`](../../../quantum-observable-universe/appendix-surreals/bigbang-heatdeath.md). -/
class BigbangHeatdeath where
  /-- **Content statement** (from manuscript):

      **Caveat: this conjecture is more speculative than the others.**
It sketches a use of surreals as endpoints of cosmological time
that the rest of the paper does not depend on.

      Field schema below is a structural placeholder; refine per §3b
      to match the conjecture's actual content. The single sorry on
      the `noncomputable instance` is the conjecture itself. -/
  residual : ℝ
  /-- The residual vanishes (the conjecture is the assertion that
      this holds). -/
  residual_eq_zero : residual = 0

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/bigbang-heatdeath.ts
noncomputable instance : BigbangHeatdeath := by
  sorry

end QOU.AppendixSurreals
