---
# qou-tho9
title: 'GAP: content multiset determines the Young diagram — last step of q-deformed pairwise inequivalence'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:10:43Z
updated_at: 2026-08-21T16:11:26Z
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
