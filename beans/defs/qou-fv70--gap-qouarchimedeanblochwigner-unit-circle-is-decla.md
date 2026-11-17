---
# qou-fv70
title: 'GAP: QOU.Archimedean.BlochWigner_unit_circle is declared TWICE in one namespace — opaque vs defined, masked by a commented-out import, and it decides qou-006b''s epistemic status'
status: in-progress
pr: 8240
updated_at: 2026-11-17T07:03:07Z
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:22:50Z
updated_at: 2026-11-15T18:12:08Z
parent: qou-r9ih
---

MEASURED 2026-09-04 during the qou-08zf Lean gap assessment. Verified
independently before filing.

Two declarations, one fully-qualified name, both under `namespace
QOU.Archimedean` (line 53 of each file):

  lean/QOU/Archimedean/BlochWignerUnitCircle.lean
    noncomputable opaque BlochWigner_unit_circle (_theta : R) : R    -- SEALED
  lean/QOU/Archimedean/BlochWignerMathlibFiller.lean
    noncomputable def    BlochWigner_unit_circle (theta : R) : R := Cl_2 theta

Importing both fails:

  error: import QOU.Archimedean.BlochWignerMathlibFiller failed, environment
  already contains 'QOU.Archimedean.BlochWigner_unit_circle' from
  QOU.Archimedean.BlochWignerUnitCircle

WHY NOBODY HAS HIT IT: `QOU/Archimedean.lean:36` has the filler import
COMMENTED OUT, inside a block labelled "COMPILE-PENDING -- these files have
never been in the build". So nothing that builds the library root can see the
collision, and it will surface the moment anyone uncomments that line.

## Why this is not just hygiene: it DECIDES qou-006b

`qou-006b` says `BringZeroModeBlochClass` quantifies over an "opaque"
`BlochWigner_unit_circle` and calls its field unfalsifiable. The accurate word
is UNDECIDABLE, and the reason is this collision rather than a weak field:

  under the OPAQUE import  -- the field cannot be discharged; `<<0, rfl>>` fails
  under the FILLER import  -- the field is PROVABLE BY IVT (Cl_2 is a real
                              function with the needed continuity)

Same syntax, opposite epistemic status, selected by which file is imported. A
conjecture whose openness is an import choice is not an open conjecture; it is
an unresolved editorial decision wearing one.

## The decision this needs (owner-level, not agent-level)

Which is the intended object? Sealing it (opaque) keeps the Bloch class genuinely
open and is the current de-facto state. Defining it as `Cl_2` makes qou-006b
closeable by IVT but commits the framework to that identification, which is the
substantive claim. Deleting the loser is then mechanical.

## Also found, same files

FOUR docstrings across those two files cite
`predicted-spectra/bloch-wigner-mathlib-filler.lean`, which DOES NOT EXIST --
that block has `.md` and `.ts` siblings and no `.lean`. Dead citations, same
class as the `substrate-anchor-alternatives.md` pointer AGENTS.md records.



## 2026-11-15, PR #7946

`BlochWignerUnitCircle.lean` now defines `BlochWigner_unit_circle := Cl_2` (was `opaque`), so qou-006b's field is decidable and true by IVT. **The duplicate name is NOT fixed**: `BlochWignerMathlibFiller.lean` still defines the same constant, and importing both still collides. Both bodies are now `Cl_2`, so the fix is to delete one; left for a separate change.

## Progress Update (PR #8240)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8240` at `cb076a625e5995208490115a8926f02d958314a7`).
- **Lean Formalization**: `QOU.QBeta.AnglePolytopeFeasibilityAndClausenUnitCircleBrick.bloch_wigner_unit_circle_clausen_odd_reflection_and_triplication` (Unit-circle Clausen / Bloch-Wigner oddness at 0 and pi plus Kubert duplication at pi/3 locking D(2*pi/3) = (2/3)*D(pi/3) and D(pi/3) + D(2*pi/3) = (5/3)*D(pi/3).)
- **80-dps Witness**: `computations/probes/angle-polytope-feasibility-and-clausen-unit-circle-brick.witness.json` (`scriptHash: 2cbc25827af3`, `scriptCommitSha: ec2c1b177f9eff729f315a26ddbb5ea7edbf540d`).
