/-
Copyright (c) 2026 litlfred. All rights reserved.

# What "Brunnian" means in this corpus — four tiers, and they are NOT equivalent

The word `Brunnian` names **four different properties** across `QOU/`, and on
2026-09-07 that cost a wrong reading of the three-body binding channel: a theorem
whose hypothesis is tier 4 was applied to a carrier that satisfies only tier 2,
on the strength of the shared name.  This file is the single place that states the
hierarchy and proves the parts of it that are provable.

    T1  TRUE BRUNNIAN          every proper sub-link is the UNLINK
                               `QOU.KnotTheory.Brunnian` (`borromean_brunnian`)
    T2  LINKING VANISHES       every pairwise Gauss linking number is 0
                               `MilnorIndeterminacyGate.ClusterTriple.Brunnian`
    T3  LINKING VANISHES AT k  the same, localised at one component
                               `FreedmanHeGenusHandleNeedsVanishingLinking.BrunnianAt`
    T4  NO ISOLATED PAIR ENERGY   a pair carries no mutual ENERGY in isolation
                               `CrossingModelPairLocality.NoIsolatedPairEnergy`
                               (renamed 2026-09-07; it was called `Brunnian`)

**T1 ⟹ T2, and the converse is FALSE.**  A sub-link that is an unlink has
vanishing linking number, so T1 implies T2.  The converse fails: the **Whitehead
link** has linking number `0` and is not the unlink.  That non-implication is a
statement about links, not about arithmetic, so it is *cited and not proved here*
— manufacturing a Lean "theorem" for it would be exactly the laundering
AGENTS.md forbids.  What matters for readers is the direction of the arrow:
**calling T2 "Brunnian" is an over-claim** unless the carrier is independently
known to be T1.  `L6a4` (the Borromean rings) happens to be both, which is why
the over-claim survived.

**T2 ⟺ T3 pointwise**, and that IS proved here (`linkingVanishes_iff_forall_at`):
all three pairwise linkings vanish exactly when every component is unlinked from
the others.  This is the bridge the two files never had.

**T4 IS NOT IMPLIED BY ANY OF T1–T3 — it is CONTRADICTED for any crossing pair.**
This is the one that bit.  `BrunnianBindingChannel.brunnian_binding_survives`
proves `0 < countChannel m m q` for `0 < m`, `1 < q`: a pair with `n₊ = n₋ = m`
has linking number zero (T2/T3 hold) and **strictly positive** mutual energy
(T4 fails).  `noIsolatedPairEnergy_fails_for_crossing_pair` below records that as
a standalone statement so it cannot be walked past again.  The full refutation for
the actual carrier, from both the structure side and the AME data side, is
`QOU.Mass.BrunnianHypothesisNotSatisfied`.

## The rule for authors

Use `Brunnian` **only** for T1.  For T2/T3 say *"vanishing pairwise linking"*.
For T4 say `NoIsolatedPairEnergy`, and expect it to be **false** on any carrier
with crossings — it is a hypothesis, not a property this framework's carriers have.

§7c: `linkingVanishes_iff_forall_at` is pure `ℤ` arithmetic over an abstract
linking matrix; only the energy statement touches `ℝ`, because `countChannel` and
`1 < q` are archimedean.  Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md
-/
import QOU.Mass.FreedmanHeGenusHandleNeedsVanishingLinking
import QOU.Mass.BrunnianBindingChannel
import QOU.Mass.MilnorIndeterminacyGate

namespace QOU.Mass.BrunnianTierDisambiguation

open QOU.Mass.FreedmanHeGenusHandleNeedsVanishingLinking
open QOU.Mass.BrunnianBindingChannel

/-- **T2 ⟺ T3, on a three-component cluster.**

All three pairwise linking numbers vanish exactly when every component is
unlinked from the other two.  Symmetry of the linking matrix is a hypothesis
because `BrunnianAt` reads the matrix in one direction only; the Gauss linking
number is symmetric, so this is not a restriction in practice.

This is the bridge `MilnorIndeterminacyGate` and
`FreedmanHeGenusHandleNeedsVanishingLinking` never had between them — they state
the same condition, one globally and one pointwise, and nothing related them. -/
theorem linkingVanishes_iff_forall_at (lk : Fin 3 → Fin 3 → ℤ)
    (hsymm : ∀ i j, lk i j = lk j i) :
    (lk 0 1 = 0 ∧ lk 0 2 = 0 ∧ lk 1 2 = 0) ↔ ∀ k, BrunnianAt lk k := by
  constructor
  · rintro ⟨h01, h02, h12⟩ k j hjk
    fin_cases k <;> fin_cases j <;> simp_all [hsymm 1 0, hsymm 2 0, hsymm 2 1]
  · intro h
    exact ⟨h 0 1 (by decide), h 0 2 (by decide), h 1 2 (by decide)⟩

/-- **T4 fails for every crossing pair — the statement that was walked past.**

A pair with `n₊ = n₋ = m` and `0 < m` has vanishing linking number (so T2 and T3
hold of it) and **strictly positive** mutual energy, so `NoIsolatedPairEnergy`
(`w₂ = 0`) is false of it.  Vanishing linking does not empty the energy; it
empties only the *signed* channel, and the unsigned count channel survives.

Restated from `brunnian_binding_survives` under the name of the property it
refutes, because the failure mode this file exists to prevent was reading a
theorem about linking as a theorem about energy. -/
theorem noIsolatedPairEnergy_fails_for_crossing_pair
    (m : ℕ) (hm : 0 < m) (q : ℝ) (hq : 1 < q) :
    pairEnergy m m q ≠ 0 := by
  rw [brunnian_energy_is_count_channel]
  exact ne_of_gt (brunnian_binding_survives m hm q hq)

/-- **And the two channels genuinely disagree on such a pair**: the signed
channel is zero while the total is not.  So "the linking number vanishes" and
"the mutual energy vanishes" are not two readings of one fact — they differ on
exactly the configurations this framework's carriers are made of. -/
theorem signed_zero_but_energy_nonzero
    (m : ℕ) (hm : 0 < m) (q : ℝ) (hq : 1 < q) :
    signedChannel m m q = 0 ∧ pairEnergy m m q ≠ 0 :=
  ⟨brunnian_signedChannel_zero m q,
   noIsolatedPairEnergy_fails_for_crossing_pair m hm q hq⟩

/-- **T2 in its concrete `ClusterTriple` form is the same condition.**  Recorded
so a reader holding a `ClusterTriple` can reach the pointwise form without
re-deriving the translation. -/
theorem clusterTriple_brunnian_iff (t : MilnorIndeterminacyGate.ClusterTriple) :
    t.Brunnian ↔ (t.l12 = 0 ∧ t.l13 = 0 ∧ t.l23 = 0) := Iff.rfl

end QOU.Mass.BrunnianTierDisambiguation
