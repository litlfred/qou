# The fluid-dynamics reorder is not mechanical — a correction

Generated 2026-08-10. Bean: `cnd4`. Follows
[`blocked-edges-three-problems.md`](2026-08-10-blocked-edges-three-problems.md),
which this audit corrects.

## What the previous audit claimed

Group 2 was described as **22 edges fixed by 11 block moves**, and recommended
as *"mechanical to compute, but it changes reading order, so it is proposed
and not applied"* — the implication being that the only thing standing between
the corpus and those 22 edges was a reviewer glancing at a diff.

For `fluid-dynamics`, the largest single piece (12 of the 22), that was wrong.
Attempting the move surfaced three facts the graph-level analysis had not.

## 1. The chapter already carries 12 intra-chapter forward edges

Before adding anything, `uses[]` in `fluid-dynamics` already declares twelve
same-chapter forward references:

| from | to |
|---|---|
| 5 `rem:hamilton-jacobi-phase` | 10 `rem:geodesic-vortices` |
| 8 `rem:q-ns-properties` | 36 `thm:q-ns-wellposedness` |
| 9 `rem:q-metric-contact-deformation` | 96 `rem:q-ns-research-programme` |
| 37 `rem:q-ns-proof-strategy` | 43 `prop:q-ns-nonlinear-uniqueness` |
| 37 `rem:q-ns-proof-strategy` | 40 `thm:quantum-peter-weyl` |
| 47 `rem:observability-fluid-context` | 55 `prop:core-levi-form` |
| 48 `rem:observability-independent-motivation` | 69 `thm:ns-singularity-descartes` |
| 52 `rem:substrate-gm-torsion` | 62 `prop:ns-obstruction-tower` |
| **55 `prop:core-levi-form`** | **91 `prop:vorticity-lower-bound`** |
| 56 `rem:core-levi-interpretation` | 74 `prop:root-of-unity-truncation` |
| 63 `rem:ns-obstruction-tower-summary` | 92 `conj:levi-degeneracy` |
| 74 `prop:root-of-unity-truncation` | 91 `prop:vorticity-lower-bound` |

The proposed move targets the §4–§6 region. That region is **already knotted**:
`prop:core-levi-form` (§4, pos 55) is the block whose conditional banner forces
the whole move, and it *already* reaches forward to pos 91 — which in turn
depends on `conj:q-aubin-lions` at pos 88, one of the blocks being moved.

A five-block move inside that knot is not a reorder; it is a partial
restructuring whose effect on the other twelve edges is unmodelled.

## 2. The move set is a closure, and it crosses a section boundary

The four conjectures cannot move alone. `conj:ns-counterexample` depends on
`prop:universality` (pos 85), so the closure is five:

| pos | § | block |
|---|---|---|
| 81 | 6 | `conj:regularity-breakdown` |
| 83 | 6 | `conj:critical-exponent` |
| 85 | 6 | `prop:universality` |
| 87 | 6 | `conj:ns-counterexample` |
| 88 | 6 | `conj:q-aubin-lions` |

All five sit in **§6 "NS obstruction tower, specialisations, and observable
MTC"** and would land in **§4 "Global regularity for `q > 1`"**. That is not a
reordering within a section — it changes which section five blocks belong to,
and it hollows out §6.

It also strands companions. `tbl:regularity-breakdown-table-data` (82) tabulates
`conj:regularity-breakdown` (81); `rem:p4-universality-interpretation` (86)
interprets `prop:universality` (85). Moving the parents without the companions
separates a table from what it tabulates. Including them makes the move seven
blocks and takes most of §6 with it — at which point the honest description is
"merge §6 into §4", which is an editorial proposal about the chapter's
argument, not a bookkeeping fix.

## 3. The banner names five, and one is not a conjecture

`core-levi-form.md` opens:

> **Proposition (conditional on [`conj:q-aubin-lions`],
> [`conj:ns-counterexample`], [`conj:critical-exponent`],
> [`prop:blowup-yekutieli`], and [`conj:regularity-breakdown`];
> "Core Levi form").**

Its `uses[]` declares neither — only `prop:vorticity-lower-bound` and
`rem:c-substrate-via-levi`. So §3b-cond rule 4 is genuinely violated, and by
**five** antecedents rather than four: `prop:blowup-yekutieli` never entered
the rule-4 scan because that scan keys on the `conj:` prefix.

Both `prop:blowup-yekutieli` and `rem:c-substrate-via-levi` are absent from the
chapter manifest entirely, so the block's declared and undeclared dependencies
already reach outside the chapter.

## Correction to the recommendation

Group 2 should not be described as needing only a reviewer. Split it:

- **`appendix-surreals` (1 edge) and `predicted-spectra` (1 edge)** — genuinely
  local, single-position moves within one section. Still mechanical.
- **`mass-theory` (8 edges, 5 moves)** — spans §20–§46 with jumps of 200+
  positions. Not re-verified here; assume it has the same character as
  `fluid-dynamics` until someone checks, and note that one of its movers,
  `prop:curvature-rank-gb-stratification`, is already filed under `msc1` for a
  phantom hook-length attribution. Moving a block whose *content* is in
  question is premature.
- **`fluid-dynamics` (12 edges)** — an editorial question about the chapter,
  not a diff to approve. The question is whether §6's conjectural inputs
  belong ahead of §4–§5's conditional results, which is the same question as
  whether §6 and §4 should be one section.

## What is safe to do now

Nothing in `fluid-dynamics` without the author. The 12 edges stay held, and
the reason is now stronger than "it points forward": **the ordering fix is a
chapter restructuring with 12 pre-existing forward edges underneath it.**

The generalisable lesson matches the `§0`-overview finding in the companion
audit. Both times the graph-level view proposed a move that reading the actual
blocks showed to be wrong — first a definition relocated ahead of its own
introduction, now a five-block section transplant. **A position metric can
tell you an ordering is inconsistent; it cannot tell you which end to move,
and it does not know what a section means.**
