import Mathlib.Data.Real.Basic

/-!
# QOU.BraidKnot.UnstableAtom.decay_channel — uniquely-determined decay channel

The violated constraint γ*(K, q) is well-defined off the boundary
variety (where two shadow prices agree).

LaTeX: `\label{prop:unstable-atom-decay-channel}`

The substantive Lean encoding (the `DecayChannelContext` class plus the
`decay_channel` conditional result) lives at the canonical library path
`QOU/BraidKnot/UnstableAtom/decay_channel.lean`
(`lean.ref = qou:QOU.BraidKnot.UnstableAtom.decay_channel`). This sibling
records the **uniqueness** sub-claim explicitly as a conditional result:
off the boundary variety the violated constraint is unique.
-/

namespace QOU.BraidKnot

universe u

/-- Abstract data carrying the decay-channel selection for an unstable
    atom at substrate parameter `q`: a partition index type, the
    selected violated constraint `lam_star`, the boundary-variety
    predicate, and — as the genuine conjectural input — the LP-duality
    fact that off the boundary variety any minimiser of the
    constraint-violation energy coincides with `lam_star`. -/
class DecayChannelSelection (R : Type u) where
  /-- Partition / Young-diagram indexing type. -/
  PartitionIdx : Type u
  /-- Substrate parameter. -/
  q : R
  /-- The selected decay-channel partition `λ*(K, q)`. -/
  lam_star : PartitionIdx
  /-- Predicate: `q` lies on the boundary variety
      `{q : ∃ λ₁ ≠ λ₂, |y_{λ₁}(q)| = |y_{λ₂}(q)|}`. -/
  on_boundary : Prop
  /-- Predicate selecting partitions that minimise the constraint-
      violation energy at `q`. -/
  IsMinimiser : PartitionIdx → Prop
  /-- LP-duality input (`prop:mass-coefficient-shadow-price`): off the
      boundary variety the violated constraint is uniquely determined,
      i.e. any partition that also minimises the constraint-violation
      energy must equal `lam_star`. This is the genuine conditional
      hypothesis; the uniqueness statement below derives from it. -/
  unique_off_boundary :
    ¬ on_boundary → ∀ lam : PartitionIdx, IsMinimiser lam → lam = lam_star

/-- **Decay channel of an unstable atom is uniquely determined.**

    Off the boundary variety
    `B := { q : ∃ λ₁ ≠ λ₂, |y_{λ₁}(q)| = |y_{λ₂}(q)| }`,
    the violated constraint `λ*` is unique: any two energy-minimising
    partitions coincide (both equal `lam_star`). Conditional on
    `[DecayChannelSelection R]` (the LP-duality selection data,
    `prop:mass-coefficient-shadow-price`). -/
-- Ref: [manuscript] braids-and-knots/local-shadow-ordering
theorem UnstableAtom.decay_channel_unique
    {R : Type u} [sel : DecayChannelSelection R]
    (h_off : ¬ sel.on_boundary)
    (lam₁ lam₂ : sel.PartitionIdx)
    (h₁ : sel.IsMinimiser lam₁) (h₂ : sel.IsMinimiser lam₂) :
    lam₁ = lam₂ :=
  (sel.unique_off_boundary h_off lam₁ h₁).trans
    (sel.unique_off_boundary h_off lam₂ h₂).symm

end QOU.BraidKnot
