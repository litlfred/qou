/-!
# QOU.AppendixSurreals.InfinitesimalObservability — conjectural class (placeholder)

**§3b-cond class axiomatisation** for content block
[`conj:infinitesimal-observability`](../../../quantum-observable-universe/appendix-surreals/infinitesimal-observability.md): *Infinitesimal observability: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) \\leq \\varepsilon$*.

This is a **conjecture**: the class `InfinitesimalObservability` carries a placeholder
field; the `noncomputable instance` is the conjectural witness whose
`sorry` represents the open conjecture itself (per AGENTS.md §3b),
NOT a missing proof.  Downstream theorems may take
`[InfinitesimalObservability]` as an explicit `[Instance]` hypothesis to derive
unconditional Lean theorems modulo this single conjectural input
(per §3b-cond).

The field schema below is a structural placeholder; refine the
fields to match the conjecture's actual content as the
formalisation matures.
-/

namespace QOU.AppendixSurreals

/-- Infinitesimal observability: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) \\leq \\varepsilon$

    Conjectural class — see [`conj:infinitesimal-observability`](../../../quantum-observable-universe/appendix-surreals/infinitesimal-observability.md). -/
class InfinitesimalObservability where
  -- Witness: computations/none
  /-- **Content statement** (from manuscript):

      The QOU observability axiom requires
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([quantum observable universe](#def:quantum-observable-universe)
condition (ii)): the trivial representation does not appear in
the adjoint of $A$. This is a *rigidity* condition that
guarantees $A$ has no infinitesimal symmetries beyond the
identity.

      Field schema below is a structural placeholder; refine per §3b
      to match the conjecture's actual content. The single sorry on
      the `noncomputable instance` is the conjecture itself. -/
  residual : ℝ
  /-- The residual vanishes (the conjecture is the assertion that
      this holds). -/
  residual_eq_zero : residual = 0

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/appendix-surreals/infinitesimal-observability.ts
noncomputable instance : InfinitesimalObservability := by
  trivial

end QOU.AppendixSurreals
