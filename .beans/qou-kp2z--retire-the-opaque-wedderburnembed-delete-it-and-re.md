---
# qou-kp2z
title: 'Retire the opaque wedderburnEmbed: delete it, and repoint every surface that called it opaque'
status: completed
type: task
priority: normal
created_at: 2026-09-05T17:12:41Z
updated_at: 2026-09-26T11:03:21Z
---


Follow-up to `qou-usol`, which built `wedderburnEmbedOf` but left the `opaque`
it replaced standing. `opaque` is not free notation: it is irreducible *and* it
reports in `#print axioms`, so the declaration stood as a fourth standing axiom
in the Hecke layer for as long as it existed.

## What was measured before touching anything

On merged `main` at `7e75622`, comment-stripped scan of every non-`.lake` Lean
source: **zero** term-level uses of `wedderburnEmbed`. The sole occurrence was
the declaration itself. `scripts/lean-axiom-guard.py` never names it, so there
was no allow-list entry to retire. The axiom was being paid for by nobody —
the cheapest case to remove, and the easiest to leave standing forever.

A second thing fell out of that scan. `MarkovTrace.lean`'s module doc
advertised `wenzlBridge` as
`markovTrace n (wedderburnEmbed x) = Σ_λ y_λ(q_0) · trace (x λ)`. The theorem
is `markovTraceOnWedderburn x = Σ_λ y_λ(q_0) · trace (x λ) := rfl` — an
unfolding lemma whose left-hand side *is* that sum by definition. The doc
described a materially stronger statement (relating `markovTrace` on the global
matrix algebra to the block sum) that is proved nowhere. Corrected in place.

## What this changed, and what it did not

Deleted the `opaque` and repointed seven surfaces: the two Lean prose sites in
`MarkovTrace.lean`, the module doc and open-port note in `Wedderburn.lean`, the
intro and docstring in `WedderburnConstruction.lean`, the `QOU.lean`
registration comment, `docs/audits/2026-08-21-wedderburn-instance-artin-scoping.md`,
and the reader-facing block `unified-iterative-correction-proof.md`.

The block is the one that mattered. `qou-qb7p` gave **three** reasons the
`(2,1)` clause could not be discharged; two are now retired (opaque,
fourth-axiom) and **one is untouched**: the constructed map has the same type
`⊕_λ M_{f^λ} → M_{n!}`, assembling blocks into one matrix rather than splitting
one block's scalar `C_{(2,1)}` into three coefficients. Building the map
changed its *status*, not its *direction* or *arity*. The clause therefore
remains an open obligation, and the block now says which reason survived —
a reader must not read "the embedding was built" as "the clause was
discharged".

`qbeta_wedderburn_bridge_probe.py` asserted the opaque *exists*
(`src.count("opaque wedderburnEmbed") == 1`), so deleting it would have taken
that gate red. Inverted rather than deleted: it now measures the new state,
retains the two retired facts as dated history, and keeps the shape objection
as the fact carrying the conclusion. Its scan was also hardened — the old
backtick filter counted every doc mention as a use, including the retirement
note itself; it now strips Lean comments properly, which is the only version
that would actually catch a real use.

## Gates

- `lean`-direct exit 0 on `Wedderburn.lean` and `WedderburnConstruction.lean`.
- `lean-direct-cone.sh QOU.HeckeAlgebra.Wedderburn` — 7 modules, 0 errors.
- Axiom footprints of `wenzlBridge`, `markovTraceOnWedderburn` and
  `markovTrace_zero` **identical** to the pre-deletion baseline. That was the
  named falsifier: had any footprint or elaboration moved, something did consume
  the opaque and the change would have had to be a migration. It did not fire.
- `qbeta_wedderburn_bridge_probe.py` 9/9; `probe-float64-guard.py --diff` clean
  (1 of 8 changed files in scope); `lean-orphan-audit.ts --diff` clean.

## Not verified, and why

`MarkovTrace.lean` cannot be recompiled by `lean`-direct against the restored
olean snapshot: 21 errors, all "already been declared". The cause is snapshot
staleness, not a source defect — `JonesMarkovWenzl.olean` is dated 2026-07-02
and was built when that module still imported `MarkovTrace`; the source (last
changed 2026-08-26, `22013eb256`) no longer does, and a BFS over source imports
finds no cycle. My edits there are comment-only and provably inert: the
line/column-normalised error set is byte-identical, 21 messages before and
after. Same class as the `seminormalDim_pos'` staleness hit during `qou-usol`.

## Correction to PR #6848

That PR's body said "Two doc-comment references remain (both in
`MarkovTrace.lean`)". Wrong — stated from memory rather than from a grep.
There were seven non-bean surfaces, one of which was a live gate. An agent
trusting that sentence would have shipped a red probe.
