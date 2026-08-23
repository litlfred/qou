---
# qou-9e7p
title: '§7c checker: an inherited archimedean construct reads as gratuitous R'
status: todo
type: task
priority: normal
created_at: 2026-08-23T16:45:03Z
updated_at: 2026-08-23T16:45:53Z
---

## The false positive

`scripts/check-sidecars.sh` classifies a standalone library Lean file by looking
for archimedean constructs **in that file**. A file whose `R` is forced by an
IMPORTED archimedean construction therefore reads as
*'R in type but NO archimedean construct -> likely gratuitous'*.

Worked case (2026-08-23, PR #5558):
`QOU/SchurWeyl/HeckeProductSurjective.lean`. Every R in it comes from
`seminormalRep`, which is R-only because `OffDiagNonvanishing.sq_geom_lt` is an
inequality in an ORDERED field (`0 < y`, `nlinarith`). Nothing built on
`seminormalRep` can be generalised to a bare `[Field R]`, so the flag is
un-actionable as stated — the suggested fix (`generalize to {R}/[Field R]`) is
impossible.

## Why this matters rather than being cosmetic

The gate's instruction is 'act on the warning lines before commit'. A warning
that cannot be acted on trains agents to wave the gate through, which is exactly
how a REAL gratuitous-R would get past it. The 7c rule earned its place after a
gratuitous `(q : R)` landed on an algebraic tau-kernel lemma; the checker's value
depends on its warnings being actionable.

## Options, not a prescription

1. Follow the import graph one hop and treat an archimedean construct in a
   directly-imported QOU module as justifying the importer's R. Cheap, and
   catches this class; may over-forgive a file that imports something
   archimedean but does not depend on it.
2. Recognise an explicit in-file justification marker, so a file can say 'the R
   is inherited from X' and be classified accordingly. Auditable, but only as
   honest as the marker.
3. Leave it and accept the class as known noise — in which case say so in the
   skill doc, so agents know which warnings are expected to be un-actionable.

I did not implement any of these: this is the qou-0h5k session and the checker
is not its scope. The file carries a header paragraph explaining the
justification instead; see PR #5558.
