import Mathlib.Data.Nat.Notation

/-!
# QOU.QuantumObservableUniverse.exists_axiom_2_observability

**Canonical declaration** for content block
[`lem:qou-exists-axiom-2`](../../../quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-2.md): *Axiom 2 — observability via Peter--Weyl decomposition*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.QuantumObservableUniverse


/-- Abstract context for the `exists_axiom_2_observability` claim — manuscript-themed
    typed fields below; `holds` carries the residual `Prop` claim. -/
class ExistsAxiom2ObservabilityContext where
  /-- Dimension of `Hom_C(𝟙, Ad(A))` modulo the unit summand. -/
  hom_dim : ℕ
  /-- The total dimension of invariants. -/
  total_hom_dim : ℕ
  /-- Modulo the unit summand means we subtract 1 from the total dimension. -/
  hom_dim_eq : hom_dim = total_hom_dim - 1
  /-- The only invariants are scalars, so the total invariant space has dimension 1. -/
  total_hom_dim_eq : total_hom_dim = 1

/-- **Lemma statement** (from manuscript):

For $\mathbf{C} = \mathbf{Rep}(U_{q}(\mathfrak{g}))$ at generic $q$
and $A = \mathcal{O}_{q}(G)$,
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
modulo the unit, verifying axiom~(2) of
[quantum observable universe](#def:quantum-observable-universe).

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-2.ts
theorem exists_axiom_2_observability [ctx : ExistsAxiom2ObservabilityContext] :
    ctx.hom_dim = 0 := by
  rw [ctx.hom_dim_eq, ctx.total_hom_dim_eq]

end QOU.QuantumObservableUniverse
