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

/-- Frobenius separation on the horizon graded module: the pairing
    between trapped interior degree-0 data and exterior graded probes
    (jet-bundle degree ≥ 1 / positive Gröbner–Shirshov filtration
    degree) separates interior states.

    This is the conjectural *input* isolated by the filtration-level
    reframing (owner, 2026-07-03): the evolution on the full
    jet/GS-filtered algebra is already unitary (P1a); the only open
    content of exterior unitarity is that the Frobenius-type pairing
    against the accumulated graded tower distinguishes interior states.
    Away from the horizon this non-degeneracy is definitional for
    membership in the observable subcategory; the class asserts its
    persistence on the horizon graded module.  Generic base types per
    §7c: separation needs no archimedean structure. -/
class FrobeniusSeparation (Interior Probe R : Type*) where
  /-- The Frobenius-type pairing of an interior state against an
      exterior graded probe. -/
  pair : Interior → Probe → R
  /-- **Conjecture (open):** the pairing separates interior states. -/
  separating : ∀ x y : Interior, (∀ p, pair x p = pair y p) → x = y

-- No instance: the separation on the *horizon* graded module is the
-- open conjectural input (away from the horizon it is definitional).
-- Ref: [susskind1993] https://doi.org/10.1103/PhysRevD.48.3743

/-- **Witness completeness from Frobenius separation** (sorry-free
    reduction).  If the lifetime-total witness stream of an interior
    state is its family of Frobenius pairings against exterior graded
    probes, then separation of the pairing *derives* injectivity of
    the witness stream — i.e. `conj:witness-completeness` reduces to
    `FrobeniusSeparation` on the horizon graded module.  The
    conjectural content is thereby isolated in the single named
    hypothesis class, per §3b-cond (the class carries the hypothesis,
    the theorem derives the conclusion). -/
theorem witnessComplete_of_frobeniusSeparation
    {Interior Probe R : Type*} [FrobeniusSeparation Interior Probe R] :
    Function.Injective
      (fun x : Interior => (FrobeniusSeparation.pair x : Probe → R)) := by
  intro x y h
  exact FrobeniusSeparation.separating x y (fun p => congrFun h p)

end QOU.Information
