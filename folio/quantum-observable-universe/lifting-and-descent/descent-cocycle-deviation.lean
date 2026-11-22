import QOU.Torsion.YekutieliTriple


/-!
# QOU.LiftingDescent.descent_cocycle_deviation

Under the central extension `𝔊_{n+1} → 𝔊ₙ` with local lift data
`a_{ij}^{(n)} ∈ 𝒪_M^×`, the cocycle deviation at level `n+1` is a
twisted Čech 2-cocycle on `M`.  The Yekutieli condition encodes this
as the `TwistedTwoCocycle` structure already declared in the Lake
tree at `QOU.Torsion.YekutieliTriple`.

This sibling extracts the cocycle-deviation statement: for any
`TwistedTwoCocycle`, the deviation is captured by the structure's
`cocycleDeviation` field, related to the coboundary via the
twisted-condition (the Peiffer-like identity that makes the
deviation a 2-cocycle when twisted by the level-`n` two-morphisms).

LaTeX label: `lem:descent-cocycle-deviation`

**Ground ring (AGENTS.md §7c).**  `TwistedTwoCocycle` is declared
under `variable (R : Type*) [GroupWithZero R]`, so its real arity is
`TwistedTwoCocycle R M` — the coefficient ring first, the base second.
This file applied it to one argument, putting `M` in `R`'s slot, and
so asked for `GroupWithZero M`:

    failed to synthesize GroupWithZero M

`GroupWithZero` is the library's deliberate minimal choice (its own
docstring says a field would over-constrain the transition groupoid),
so it is carried here rather than specialised.

## References

- [yekutieli2010] Central Extensions of Gerbes, §3 (Čech 1-cocycle
  deviation and the twisted-cocycle condition)
- [leitner2026] §3 Lifting and Descent, definition of the
  Yekutieli triple
-/

namespace QOU.LiftingDescent

open QOU.Torsion in
/-- **Cocycle deviation at level n+1 is a twisted Čech 2-cocycle.**

    For any `TwistedTwoCocycle` on `M`, the field `cocycleDeviation`
    realises the level-`n+1` deviation, satisfying the twisted
    condition

      `coboundary p = a(p) · cocycleDeviation(p) · a(p)⁻¹`

    where `a(p) = triple.twoMorphisms p`.  This is exactly the
    `twisted_condition` field of the structure. -/
-- Ref: [yekutieli2010] §3, twisted-cocycle condition
-- Ref: [leitner2026] §3 Lifting and Descent
theorem descent_cocycle_deviation
    {R : Type*} [GroupWithZero R] {M : Type*}
    (tc : QOU.Torsion.TwistedTwoCocycle R M) :
    ∀ (p : M),
      tc.coboundary p = tc.triple.twoMorphisms p *
        tc.cocycleDeviation p * (tc.triple.twoMorphisms p)⁻¹ :=
  tc.twisted_condition

/-- When the coboundary vanishes globally, the cocycle deviation
    also vanishes — the standard unobstructedness statement
    (`twisted_cocycle_unobstructed` in the Lake tree). -/
-- Ref: [yekutieli2010] §3, unobstructedness
theorem descent_cocycle_deviation_unobstructed
    {R : Type*} [GroupWithZero R] {M : Type*}
    (tc : QOU.Torsion.TwistedTwoCocycle R M)
    (h_vanish : ∀ (p : M), tc.coboundary p = 0) :
    ∀ (p : M), tc.cocycleDeviation p = 0 :=
  -- `R` is an EXPLICIT binder on the library theorem (it comes from
  -- `variable (R : Type*) [GroupWithZero R]`, not `{R}`), so it is passed.
  QOU.Torsion.twisted_cocycle_unobstructed R tc h_vanish

end QOU.LiftingDescent
