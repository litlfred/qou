---
# qou-tho9
title: 'GAP: content multiset determines the Young diagram — last step of q-deformed pairwise inequivalence'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:10:43Z
updated_at: 2026-08-21T16:20:42Z
---

## What is open

For Young diagrams `μ`, `ν`:

> if for every `d : ℤ` the number of cells of content `d` agrees
> (`(μ.cells.filter (cellContent · = d)).card = (ν.cells.filter …).card`),
> then `μ = ν`.

Classical — a partition is determined by its multiset of contents (equivalently
by its diagonal lengths). Open **in this corpus**.

## Why it matters, and exactly what it unblocks

It is the **only** step between `QOU.SchurWeyl.contentCount_eq_of_matRepEquiv`
(landed, PR #5370, sorry-free) and the unconditional

> `μ ≠ ν → ¬ MatRepEquiv (seminormalRep … μ) (seminormalRep … ν)`

i.e. the second half of SW-5 (`qou-jfr8`). Everything upstream is done: an
equivalence already forces the two shapes to agree on the number of cells of
every content. Only the identification remains.

## Corpus-grep (2026-08-21)

Name-based grep across `QOU/` for `contentMultiset` / `content_multiset` /
`contents_determine` / `eq_of_content`: **nothing**. Twenty files mention
`cellContent`; none concludes a diagram equality from a content hypothesis.

**One genuine lead, which supplies part of the statement.**
[`QOU/MathlibExt/TLContentStratification.lean`](../content/quantum-observable-universe/lean/QOU/MathlibExt/TLContentStratification.lean)
(bean `qou-lcgj`) proves, for a genuine partition:

* `hasContentCell_iff_lt_numCols` — for `N ≥ 0`, the diagram has a cell of
  content `N` iff `N < numCols`;
* `hasContentCell_iff_lt_length` — for `N < 0`, iff `-N < length`.

So the **support** of the content multiset already determines `numCols` (= `λ₁`)
and `length` (the number of rows), both sorry-free. That is the outer envelope of
the diagram, not the diagram: it says where the nonzero multiplicities live, and
says nothing about what they are. The remaining content is that the
*multiplicities* — the diagonal lengths — pin the rest.

Note the type mismatch to budget for: `TLContentStratification` works on
`Partition` (a sorted `List ℕ`) with a `HasContentCell` predicate, while
`contentCount_eq_of_matRepEquiv` works on `YoungDiagram` with `Finset.filter`
counts. A bridge is needed either way; the corpus has `YoungDiagramCellsBridges`
and `PartitionNatBridge`, unchecked for this purpose.

## Route sketch (not yet attempted)

Diagonal `d` of a Young diagram is an interval of cells, so its multiplicity is
its length. Standard argument: recover the rows greedily from the diagonal
lengths — `λ₁ = max{d : mult d > 0} + 1`, the number of rows is
`-min{d : mult d > 0} + 1`, and the interior is fixed by induction on the
diagram with its first row/column peeled. Verify against Frobenius coordinates
before committing: the Frobenius arm/leg encoding may make this a two-line
consequence rather than an induction, and the corpus may already carry Frobenius
coordinates.

## Discipline note

Do **not** close `qou-jfr8` on the strength of `contentCount_eq_of_matRepEquiv`.
That theorem is exactly what it says — equal content counts — and citing it as
pairwise inequivalence would be the "conditional-proved ≠ premise-established"
failure in its purest form.


## CLOSED 2026-08-21, same session — and my route sketch above was wrong

`youngDiagram_eq_of_contentCount_eq`, sorry-free, axiom-clean. With it,
`seminormalRep_not_matRepEquiv_of_ne` makes pairwise inequivalence
**unconditional**, closing the second half of `qou-jfr8`.

**Retracting the route sketch above.** It proposed recovering the rows greedily
from the diagonal lengths (`λ₁ = max{d : mult d > 0} + 1`, induction on the
peeled diagram) and flagged Frobenius coordinates as a possible shortcut worth
checking first. **Neither is needed, and the Frobenius detour would have been
wasted work.** The observation that collapses it:

> each **diagonal** of a Young diagram is **downward-closed**, so its *length*
> already decides membership.

With `diagIndex (i,j) = min i j` — a cell's position along its own diagonal —
`(i,j) ∈ μ` iff `diagIndex (i,j) < #{cells of content j - i}`. Diagonal lengths
*are* the content multiplicities, so equal counts give the same membership
predicate, hence the same diagram. One `ext`, no induction on the diagram.

**The `TLContentStratification` lead was also not needed** — and noting why is
worth more than the lead was. It supplies the *support* (`numCols`, `length`)
on `Partition`, which would have required the `Partition`↔`YoungDiagram` bridge
this bean warned about. The direct argument never leaves `YoungDiagram` and uses
exactly one fact about it, `up_left_mem`. I flagged the type mismatch as
something to budget for; the right response to that flag was to avoid the type,
not to bridge it.

**Sizing, for calibration.** I called this "the one I would budget for" and left
the roots argument as the cheaper half. That was backwards: the roots argument
took several iterations (`Finset.sum_boole` orientation, the `zpow_mul` tail, the
`d + n < 0` branch), and this one compiled first try in ~90 lines. The signal I
misread was "classical fact not in the corpus" — absence from the corpus says
nothing about difficulty when the object has as much structure as a Young
diagram.

Landed: `mem_iff_lt_card_of_downward`, `diagIndex`,
`cell_eq_of_content_of_diagIndex`, `diagOf`, `mem_diagOf`,
`diagIndex_image_downward`, `mem_iff_diagIndex_lt`,
`youngDiagram_eq_of_contentCount_eq`.
