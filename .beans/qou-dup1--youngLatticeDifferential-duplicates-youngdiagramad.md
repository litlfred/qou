---
# qou-dup1
title: 'YoungLatticeDifferential DUPLICATES YoungDiagramAddable (my error, root cause: head -20 on a corpus-grep) + a pre-existing IsAddableCell collision on main'
status: completed
type: task
priority: high
created_at: 2026-08-30T04:57:36Z
updated_at: 2026-08-30T09:03:02Z
---

## What happened

On 2026-08-29 I built QOU/Mathlib/YoungLatticeDifferential.lean (PR #6052, commit
33ec18ec, 19:04 UTC) as "the missing Mathlib infra" for the Young-lattice differential
property. It was not missing. QOU/Mathlib/YoungDiagramAddable.lean landed on main at
07:47 UTC the SAME DAY (commit 2fb2194f), eleven hours earlier, and was present in my
working tree when I ran the corpus-grep.

## Root cause, measured

The grep I ran was scoped correctly and DID match the file. I piped it through
`head -20`. The first YoungDiagramAddable hit is at position **36** of the result list.
The truncation hid it, and I concluded "no addable/corner machinery exists" from a
truncated view.

  LESSON: never `head` a corpus-grep whose purpose is to establish ABSENCE. Truncation
  turns "I did not see it" into "it is not there", which is exactly the false negative
  the checklist exists to prevent. Count first (`| wc -l`), then page.

## The duplication, itemised

YoungDiagramAddable (main) already had, sorry-free:

  rowLen_pos_iff, cornerRows, addableRows, addableRows_eq, card_addableRows,
  cornerCells, addableCells, mem_cornerCells, mem_addableCells (both @[simp], both
  directions), card_cornerCells, card_addableCells,
  card_addableCells_eq_card_cornerCells_succ

Every one of those is duplicated in my YoungLatticeDifferential under a near-identical
name (e.g. my card_addableCells_eq_card_cornerCells_add_one vs their
..._succ; my addableRows_eq_insert_image vs their addableRows_eq). Their docstring
even uses the same hook-(2,1) worked example I reached for.

GENUINELY NOT DUPLICATED, and worth keeping:
  - card_cornerCells_eq_card_subtype / card_subtype_corners_add_one
    (bridge to numStandardYoungTableaux_branching's index SUBTYPE)
  - addableRows/Cells_nonempty, cornerRows/Cells_nonempty (structural non-vacuity)
  - ALL of YoungLatticeCornerCount: rankExchange, sum_cornerCells_succ*,
    sum_numSYT_succ*, sum_numSYT_mul_corners_of_upOperator, sum_numSYT_recurrence,
    UpOperatorIdentity. Grepped: nothing else in the corpus proves these.

## A SEPARATE, PRE-EXISTING DEFECT ON MAIN (not mine)

QOU.Mathlib.IsAddableCell and QOU.Mathlib.addCell are each defined TWICE in the SAME
namespace:
  QOU/Mathlib/YoungDiagramAddCell.lean:41,45
  QOU/Mathlib/YoungDiagramAddable.lean:108,116
The two IsAddableCell bodies are character-identical apart from the binder name
(s vs c), so this is duplication rather than a semantic hazard -- but importing both
makes the bare name ambiguous. QOU.lean currently imports only YoungDiagramAddable
(line 1028); YoungDiagramAddCell reaches the cone transitively through my module.

## Disposition -- NEEDS A DECISION, do not act blind

The consolidation is architectural, not mechanical, because the two colliding modules
are BOTH load-bearing and my new work straddles them:
  - YoungLatticeCornerCount depends on cornerAddEquiv, which lives in
    YoungDiagramAddCell (the module QOU.lean does NOT import directly);
  - docs/audits/2026-08-30-pieri-corner-identity-and-the-substrate-question.md
    designates the YoungDiagram substrate (option B) as "the answer for the partition
    layer" and cites YoungDiagramAddable by name.

RECOMMENDED (my judgement): retarget YoungLatticeCornerCount onto YoungDiagramAddable's
API, delete YoungLatticeDifferential except the bridge + non-vacuity lemmas (move those
into the CornerCount module), and open a separate item for the AddCell/Addable
namespace collision -- that one is main's, predates this branch, and should not be
folded into a PR about the SW period.

DEFAULT IF NOTHING HAPPENS: PR #6052 carries a ~310-line duplicate module. It is
correct and sorry-free, so nothing breaks, but it is dead weight and a second copy of
a definition the corpus already standardises elsewhere.


## RESOLVED 2026-08-30 — consolidated onto YoungDiagramAddable

YoungLatticeDifferential.lean is DELETED. Replacement:
QOU/Mathlib/YoungLatticeExchange.lean, built on YoungDiagramAddable, carrying only what
Addable does NOT already have:

  isCornerCell_addCell' / eraseCorner_addCell' /
  isAddableCell_eraseCorner' / addCell_eraseCorner'   the four round-trips
  SizedCornerPair / SizedAddPair / sizedCornerAddEquiv the exchange
  card_cornerCells_eq_card_subtype                    bridge to branching's index type
  card_subtype_corners_add_one
  addableCells_nonempty / cornerCells_nonempty        structural non-vacuity

Everything Addable already proved (cornerRows, addableRows, cornerCells, addableCells,
mem_*, card_*, card_addableCells_eq_card_cornerCells_succ) is now CONSUMED, not
re-proved. YoungLatticeCornerCount retargeted onto the new module.

Names deliberately differ from YoungDiagramAddCell's (SizedCornerPair vs CornerPair) so
this module does not re-create the collision it works around.

Verified: all three modules lean-direct exit 0; QOU.lean's two imports restored and the
four-way co-import (Exchange + CornerCount + Addable + SWPeriodSuperExponential) checks
clean; #print axioms clean on every capstone.

STILL OPEN, and NOT this branch's to fix: YoungDiagramAddCell and YoungDiagramAddable
remain mutually exclusive on main (both declare QOU.Mathlib.IsAddableCell / addCell).
Main is unaffected today because QOU.lean's cone contains only Addable -- verified: none
of the AddCell consumers (YoungDiagramCornerReindex, HookLengthAddCell, and their
importers) is in that cone. It is a latent trap for the next module that needs both.
