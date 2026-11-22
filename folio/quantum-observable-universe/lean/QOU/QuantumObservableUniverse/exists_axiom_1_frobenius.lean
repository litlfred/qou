import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverse.exists_axiom_1_frobenius

**Placeholder canonical** for content block
[`lem:qou-exists-axiom-1`](../../../quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-1.md): *Axiom 1 — Haar state gives a non-degenerate Frobenius pairing*.

The lemma is *named* as a `Prop` over a primitive-data carrier
(pattern C of the vacuity-fix playbook) rather than asserted via a
self-assuming projection; the `lean.ref` URI
`qou:QOU.QuantumObservableUniverse.exists_axiom_1_frobenius`
resolves to it.  An instance of the proposition is the open
faithfulness claim. -/

namespace QOU.QuantumObservableUniverse


/-- Carrier for the `exists_axiom_1_frobenius` data — only the
    primitive, non-conclusory fields (pattern C): the Hopf algebra,
    its dual, the Haar state, and the induced Frobenius pairing map.
    The conclusion (non-degeneracy / bijectivity of the pairing) is
    **not** a field here — it is the named proposition
    `exists_axiom_1_frobenius` below, so the claim is stated, not
    self-assumed. -/
class ExistsAxiom1FrobeniusContext where
  /-- Hopf algebra carrier `A`. -/
  A : Type
  /-- Dual object `A^∨`. -/
  A_dual : Type
  /-- Haar state `h : A → ℝ`. -/
  h : A → ℝ
  /-- Frobenius pairing `(a, b) ↦ h(a · b)` induced map `A → A^∨`. -/
  pairing_map : A → A_dual

/-- **Axiom 1 — Haar-state Frobenius pairing** (pattern C — named,
not asserted).

**Lemma statement** (from manuscript): the Haar state
$h = \int_{A}$ on $A = \mathcal{O}_{q}(G)$ is faithful; equivalently,
the pairing $(a, b) \mapsto h(ab)$ is non-degenerate and induces an
isomorphism $A \xrightarrow{\sim} A^{\vee}$, verifying axiom~(1) of
[quantum observable universe](#def:quantum-observable-universe).

We **name** non-degeneracy as the bijectivity of the induced pairing
map — a `Prop` over the context's primitive data — rather than
projecting it from self-assuming `pairing_inj`/`pairing_surj` fields.
An instance of this proposition is the open faithfulness claim. -/
-- Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/qou-exists-axiom-1.ts
def exists_axiom_1_frobenius [ctx : ExistsAxiom1FrobeniusContext] : Prop :=
    Function.Bijective ctx.pairing_map

end QOU.QuantumObservableUniverse
