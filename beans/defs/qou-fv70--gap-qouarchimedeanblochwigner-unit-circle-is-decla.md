---
# qou-fv70
title: 'GAP: QOU.Archimedean.BlochWigner_unit_circle is declared TWICE in one namespace — opaque vs defined, masked by a commented-out import, and it decides qou-006b''s epistemic status'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:22:50Z
updated_at: 2026-10-04T15:20:21Z
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
