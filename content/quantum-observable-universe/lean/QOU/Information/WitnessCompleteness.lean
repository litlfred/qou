import Mathlib.Tactic

/-!
# QOU.Information.WitnessCompleteness — conjectural class

**§3b class axiomatisation** for content block
[`conj:witness-completeness`](../../../quantum-observable-universe/information-theory/witness-completeness.md):
*the exterior degree-≥1 record determines the trapped degree-0 data*.

This is a **conjecture** (primary): the class carries the content of the
claim as Prop fields; the `noncomputable instance` is the conjectural
witness whose `sorry` represents the open conjecture itself (per
AGENTS.md §3b), NOT a missing proof.  Downstream theorems may take
`[WitnessCompleteness Interior Witness]` as an explicit hypothesis to
derive conditional results (§3b-cond).

Intended interpretation: `Interior` is the trapped degree-0 section data
of a finite-lifetime jet horizon (elements of `Γ(𝓗, A₀)`-type interior
states); `Witness` is the space of lifetime-total accumulated exterior
degree-≥1 witness streams (`Γ(𝓗ₜ, A_k/A₀)`, `k ≥ 1`, integrated over the
evaporation); `perSlice` is the fixed-time degree-0 restriction and
`witnessStream` the lifetime-total record.  Generic base types per
AGENTS.md §7c: nothing archimedean is needed to state injectivity.
-/

namespace QOU.Information

/-- Witness completeness (exterior unitarity), the QOU form of the first
    postulate of black hole complementarity.

    Conjectural class — see
    [`conj:witness-completeness`](../../../quantum-observable-universe/information-theory/witness-completeness.md).

    The two fields carry the two halves of the physical content:
    `hidden` is the (established) jet-horizon fact that no fixed-time
    degree-0 restriction survives the horizon ideal; `complete` is the
    open claim that the lifetime-total degree-≥1 record nevertheless
    separates interior states. -/
class WitnessCompleteness (Interior Witness : Type*) [Zero Witness] where
  /-- The fixed-time degree-0 restriction across the horizon. -/
  perSlice : Interior → Witness
  /-- Degree-0 data is blocked at every fixed time: the horizon ideal
      kills each per-slice restriction (the jet-horizon mechanism). -/
  hidden : ∀ x : Interior, perSlice x = 0
  /-- The lifetime-total accumulated degree-≥1 witness stream. -/
  witnessStream : Interior → Witness
  /-- **Conjecture (open):** the total record is injective — no two
      distinct trapped interior states produce the same lifetime-total
      exterior leakage.  Equivalently the exterior-restricted evolution
      is unitary: information sits in the Hawking-type record and only
      *decoding* is obstructed. -/
  complete : Function.Injective witnessStream

-- No instance is declared: the conjecture is open, and it is a claim
-- about the *intended* interpretation (jet-horizon interior states and
-- lifetime-total witness streams), not about arbitrary type pairs — a
-- universal instance would assert a generically false proposition.
-- Downstream conditional results take `[WitnessCompleteness I W]` as an
-- explicit hypothesis (§3b-cond).
-- Ref: [susskind1993] https://doi.org/10.1103/PhysRevD.48.3743

end QOU.Information
