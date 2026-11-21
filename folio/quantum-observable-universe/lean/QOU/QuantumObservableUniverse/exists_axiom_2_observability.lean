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

/-- **Lemma statement** (from manuscript):

For $\mathbf{C} = \mathbf{Rep}(U_{q}(\mathfrak{g}))$ at generic $q$
and $A = \mathcal{O}_{q}(G)$,
$\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
modulo the unit, verifying axiom~(2) of
[quantum observable universe](#def:quantum-observable-universe).

    Stated, not proved. Until 2026-11-21 the class also carried
    `total_hom_dim_eq : total_hom_dim = 1`, which is the conclusion, and the
    proof only subtracted (round-trip audit pass 2, C06). That field is
    deleted. Note the claim needs a reading: for the adjoint coaction of
    `𝒪_q(G)` on itself the invariants are the class functions, one per
    dominant weight by Peter–Weyl, so `total_hom_dim` is infinite in that
    reading. The claim holds for the Lie-algebra adjoint of semisimple `𝔤`.

    **Not closable as stated (QA on #8888, 2026-11-21).** `total_hom_dim`
    is a free natural number, so `hom_dim = total_hom_dim - 1 = 0` is false
    for a generic instance (take `total_hom_dim = 5`). Closing it needs the
    class to carry the representation itself, e.g. the adjoint module of
    `sl₂` with `total_hom_dim` defined as the dimension of its invariants
    plus the unit summand; Schur's lemma then gives the value. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-2.ts
theorem exists_axiom_2_observability [ctx : ExistsAxiom2ObservabilityContext] :
    ctx.hom_dim = 0 := by
  -- Ref: [kassel1995] Quantum Groups, Ch. VII (Peter–Weyl for 𝒪_q(G))
  sorry

end QOU.QuantumObservableUniverse
