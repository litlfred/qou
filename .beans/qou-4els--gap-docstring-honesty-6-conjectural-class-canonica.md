---
# qou-4els
title: 'GAP: docstring-honesty — 6 conjectural-class canonical instances discharged by degenerate data'
status: completed
type: task
priority: normal
created_at: 2026-08-24T19:14:06Z
updated_at: 2026-08-24T19:14:39Z
---

Queue from the new `lean-docstring-honesty` criterion in
`content/pipeline/qa-checkers-vacuity.ts` (folio-assistant). Same defect class as
`dsm1` and `qou-fngs`: a docstring claims a `sorry`/axiomatisation the body does
not carry, so the *only* record of the incompleteness is false prose that
`#print axioms` cannot contradict.

Worked on `claude/mt7r-archimedean-eval-2026-08-24`, 10 reported hits.

## Category 1 — false docstring, vacuous by construction (6, all fixed)

All six carried the identical archetype string *"**Faithful instance.** Carries
the explicit research-grade conjecture as a sorry."* and contained no `sorry`.
Each is now a `def` with a docstring saying what actually discharges the field
and what is still open, matching `ConfinementGradingCorrespondence.canonical`
(fixed under `qou-fngs`).

| decl | what discharged the conjecture |
|---|---|
| `CrystalGraphRealization.canonical` | `CrystalNode := PUnit`, `raising _ _ := none` → `crystal_realises` is `none = none` |
| `KazhdanLusztigClassicalLimit.canonical` | `statSign _ := 1` → `kl_compatible_with_tau` is `Or.inl rfl` |
| `SymmetricCrystalPairProduction.canonical` | `barInvolution := id` → `bar_invariant` is `T = T` |
| `RootOfUnityMTCTruncation.canonical` | `columnCount _ := 0`, `inTruncation _ := (0 < 2)` (ignores its argument) |
| `CemeteryGroupEmergence.canonical` | `tauImage _ := 0` → monotonicity is `0 = 0`, `inCemetery` unused |
| `GSOrderMatch.canonical` | `NormalForm := PUnit`, both degrees `0` → (★) is `0 = 0` |

`CrystalGraphRealization.canonical` was the root: the other five classes take
`[CrystalGraphRealization R q]` upstream, so resolution supplied the one-point
crystal everywhere.

No consumers broken. Only `CrystalRMatrixSubLemma.canonical` references the
demoted term, and it already names it explicitly
(`let C := CrystalGraphRealization.canonical R q`). Nothing in the corpus applies
any of these classes' theorems at a concrete `R`, `q`.

## Not-a-sorry-but-not-proved-either (2 fixed, + 3 consistency edits)

`YoungTableauStandard.branching_two_one` and `.sum_dimSYT_eq_involution` said
"is left as a sorry". They are §3b-conditional on `RSKIdentitiesContext` and
their bodies are the matching class fields — no `sorry`, no axiom. **No instance
of `RSKIdentitiesContext` exists anywhere in the corpus**, so nothing is silently
discharged and neither identity can be applied at a concrete `k`. Docstrings now
say that. Also corrected in the same file for consistency: the module header
("the two remaining cited `sorry`s"), the section header ("the fill is `sorry`
with a `-- Ref:` to Sagan"), and `c8_superexp` ("unconditional modulo the two
remaining RSK `sorry`s above").

## Category 4 — false positives (2, files untouched)

- `qou_obstruction_reduction.lean:123` `kappa_vanishes_iff_chi` — docstring says
  "Both are sorry-free … carry the domain gap as explicit *hypotheses* rather
  than as a `sorry`". Already correct; `dsm1` fixed this one on 2026-08-09.
- `QJucysMurphy.lean:1082` `barSymJMSum_central` — says "sorry-free" twice and
  describes a *past* `sorry` deleted under `qou-gjg6`: "A hypothesis-free version
  of this statement was carried here as a `sorry` until 2026-08-17".

Both trip `HONESTY_CLAIM` on the substring "as a `sorry`" and are not rescued by
`NEGATED_HONESTY_CLAIM`. Two cheap tunings, for the checker author:
1. add `sorry-free` (and `not by a \`sorry\``, `rather than as a \`sorry\``) to
   `NEGATED_HONESTY_CLAIM`;
2. do not fire on past-tense mentions — `was carried … as a sorry`,
   `until <date>`.

## Verification

- `scripts/lean-direct-cone.sh QOU.BraidKnot` — 246 modules, ok=246 err=0.
- `#print axioms` on all six demoted defs, the ten theorems they used to make
  unconditional, `CrystalRMatrixSubLemma.canonical`, and the three RSK
  declarations: **no `sorryAx` anywhere**. Only `propext` / `Quot.sound` /
  `Classical.choice`. The demotions are docstring+keyword only; the axiom profile
  is unchanged.

## Left open, deliberately

`KazhdanLusztigClassicalLimit.kl_compatible_with_tau` is
`∀ T, statSign (klMap T) = 1 ∨ statSign (klMap T) = -1`, which is
`statSign_pm_one (klMap T)` in **any** instance — the "conjecture" field is
derivable from its sibling, so the class states no conjectural content even with
real data, and the manuscript claims (KLR canonical basis → KL basis at `q → 1`,
monoidality, `τ`-compatibility) appear in no field. Recorded in the decl
docstring; restating the class is a separate change.
