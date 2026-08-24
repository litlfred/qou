---
# qou-hjf4
title: Triage the 11 unread trivially-inhabiting-instance candidates
status: todo
type: task
priority: normal
created_at: 2026-08-24T14:36:01Z
updated_at: 2026-08-24T14:36:55Z
---

From `scripts/trivially-inhabiting-instance-census.py` (PR #5621, audit
`docs/audits/2026-08-24-vacuity-detector-gap-five-files.md`).

The shape: an **unguarded** global `instance` filling a **data** field with
constant content, where the class it inhabits is consumed as a `[C …]`
hypothesis somewhere. That combination silently satisfies every such binder —
the `triv_hecke` / `triv_wedderburn` shape demoted in PR #5581.

`3112 .lean → 37 constant data field → 23 unguarded → 14 actionable.`

**Three hand-read, three confirmed harmful:**

- `mass-theory/phi-q-tower-jsj-bridge.lean:114` `TowerSummandRealization` —
  **FIXED** in `4204be07ed2` (demoted to `def`; the file also had never
  compiled, 6 errors → 0).
- `lean/QOU/MassEndomorphism/MassEndomorphismTrivial.lean:28` `MassEndomorphism`
  — global zero instance over an **arbitrary** `β`. Its docstring claims it
  "shows the conditional theorems are discharged non-vacuously", which is true
  of the *inhabitation* but not of the *global instance*: as an instance it also
  preempts resolution everywhere. Same disposition as `triv_hecke` — `def`.
- `lean/QOU/Interactions/QIntegerMassFormula.lean:185` `QIntegerMassFormula` —
  `f_magic := fun _ => 0` discharging the `[QIntegerMassFormula]` of
  `fits_AME_conditional`, making a §3b-cond conditional theorem unconditional at
  a degenerate magic-number correction.

**The 11 unread — candidates, NOT findings.** Each needs the same hand-read the
three above got; do not bulk-demote.

    he4-channel-active-set.lean:129            HasHe4ChannelActiveSet     c=12
    BraidKnot/Helium3Witness.lean:100          R5FullWitness              c=10
    Interactions/WedderburnMassFormula.lean:125 HasHoefsmitData           c=10
    Encounter/MostowRigidity.lean:200          MostowRigidity             c=4
    mass-endomorphism/topological-mass-conjecture.lean:180
                                               TopologicalDecompositionMass c=4
    AppendixSurreals/ClassicalLimitStpart.lean:75  ClassicalLimitStpart    c=2
    Molecular/ShellClosureNfTermCount.lean:399 ShellClosureNFTermCount    c=2
    mass-theory/jet-tower-uniform-delta-max.lean:82  JetTowerUniformDeltaMax c=2
    molecular-construction/shell-closure-nf-term-count.lean:381
                                               ShellClosureNFTermCount    c=2
    Infra/Polylogarithm.lean:107               TheoremA                   c=1
    mass-theory/lifted-crossing-locality.lean:67  LiftedCrossingLocality  c=1

**Read the instance body before deciding.** The discriminator recorded on
`qou-lo1t`: `he4_strong_duality_value` has exactly this shape yet is `legit`,
because its field reads `strong_duality := by norm_num` over concrete rationals
— a checked certificate, not a constant. Inhabitation alone never decides it.
Note `he4-channel-active-set` is in the list above and may be the same story.

Two of the eleven are the **same class in two files**
(`ShellClosureNFTermCount`), so a single verdict likely covers both.
