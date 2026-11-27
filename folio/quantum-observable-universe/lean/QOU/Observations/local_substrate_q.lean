import Mathlib.Data.Real.Basic

/-!
# QOU.Experimental.local_substrate_q

Canonical Lean declaration for content block referenced by
`qou:QOU.Experimental.local_substrate_q`.

The manuscript claim — that in a sufficiently small neighbourhood the
substrate parameter `q` agrees with its measured value within the
uncertainty `Δq` — is an *empirical consistency* statement about an
opaque substrate parameter.  No faithful Mathlib structure reduces it,
so this is pattern C of the vacuity-fix playbook: the context class is
the carrier of the substrate data, and `LocalSubstrateQ` **names** the
conditional conjecture as a `Prop` (it is honestly *not asserted* — no
`theorem … := ⟨ctx.claim_*⟩` self-assuming projection; an instance
discharging it is the open conditional claim).
-/

namespace QOU.Experimental

/-- Substrate data for the `local_substrate_q` claim: the substrate
parameter `q`, its locally measured value `q_measured`, and the
measurement uncertainty `Δq > 0`. -/
class LocalSubstrateQContext where
  /-- The substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Measured value of `q` at the local observable universe. -/
  q_measured : ℝ
  /-- Measurement uncertainty `Δq`. -/
  Δq : ℝ
  /-- The uncertainty is strictly positive. -/
  Δq_pos : 0 < Δq

/-- **Content statement** (from manuscript), named as a `Prop`:

In any sufficiently small neighbourhood `U ⊂ M` of the observable
universe, the substrate parameter `q`
([substrate parameter](#def:substrate-parameter)) agrees with its
locally measured value within the measurement uncertainty:

  `|q − q_measured| ≤ Δq`.

This is the §3b "name the conditional conjecture" disposition (pattern
C): `LocalSubstrateQ ctx` is the proposition the manuscript conjectures
for the substrate data `ctx`; the open state is honestly represented by
the absence of an instance.  It is *not* a self-assuming projection. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/local-substrate-q.ts
def LocalSubstrateQ (ctx : LocalSubstrateQContext) : Prop :=
    |ctx.q - ctx.q_measured| ≤ ctx.Δq

end QOU.Experimental
