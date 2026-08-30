# 41% of the "duplicate declaration" backlog is the schema working as designed

**Date:** 2026-08-24 · **Bean:** `qou-hjf4`
**Corrects:** [`2026-08-24-duplicate-declarations-beyond-classes.md`](2026-08-24-duplicate-declarations-beyond-classes.md) §Disposition item 2

---

## The correction

That audit called the 257 library-vs-sibling duplicate pairs "the §0a backlog"
and said the drain was *"worth a decision about whether siblings should carry
declarations at all before it starts."*

**That decision is already made, by the schema, and it is not free to reverse.**
AGENTS.md's Type system table:

| Block kind | Lean required? |
|---|---|
| `definition` | **Yes** (enforced at type level) |

and §0a, listing when a sibling is legitimate:

> A sibling `.lean` is legitimate ONLY when it carries the **real**
> formalisation (not `: True`), **for a `definition` block (sibling
> required)**, or as a genuine placeholder …

So for a `definition` block whose declaration *also* lives in the library tree,
the duplication is **mandated**. Deleting the sibling would fail validation.

## Measured

Classifying the sibling side of every library-vs-sibling collision group by its
block kind (259 groups, 437 sibling-side files — a group can have more than one
sibling):

| block kind of the sibling | count | sibling required? |
|---|---|---|
| `definition` | **181** | **yes — schema-enforced** |
| `proposition` | 119 | no (expected, warns if missing) |
| `conjecture` | 55 | no |
| `example` | 33 | no |
| `proof` | 18 | no |
| `theorem` | 17 | no |
| *no `.ts` sibling at all* | 8 | n/a |
| `remark` | 5 | no |
| `corollary` | 1 | no |

**181 of 437 — 41% — cannot be drained without a schema change.**

## What this does and does not change

**Does not change:** the census measurement (795 names in >1 file, 342
same-namespace groups). Those counts are of *names declared more than once*,
which is a fact about the tree regardless of whether any given instance is
intended.

**Does not change:** the `LightNucleus` blocker. `R5FullWitness` is still
unresolvable, and now for a second reason — the sibling holding the forked
`LightNucleus` is `conj-canonical-knot-id-sdp`, a `conjecture` block, so its
sibling is *not* schema-mandated; but the library file it would need to import
is reachable only if the fork is merged first.

**Does change:** the framing of the remaining backlog. It is not one population
of 257 candidate defects. It is at least two:

1. **~181 schema-mandated `definition` siblings.** Any change here is a change
   to the content-object architecture — whether a `definition` block's Lean
   should be allowed to *reference* a library declaration rather than restate
   it. That is a design question about the pipeline, not a cleanup, and the
   `Place` / `MotivicSubstrate` pair is the clean worked example: **19 code
   lines, zero differing**, the sibling carrying only more prose.

2. **~256 where the sibling is optional**, and each still needs both
   declarations read before anything is deleted — the discipline the `R_q`
   retraction and the six-inductives read both establish.

## Method note

Block kind is read from the `.ts` sibling's builder import
(`import { definition } from "…/builders"`), which is how the schema itself
determines it. Eight collision groups have a `.lean` sibling with **no `.ts`
sibling at all** — those are neither content blocks nor library modules, and
are worth a look on their own.

> **🛑 The "eight" is 4, corrected 2026-08-29** —
> [`2026-08-29-the-four-orphan-lean-siblings.md`](2026-08-29-the-four-orphan-lean-siblings.md).
> This bucket did not separate library modules from content siblings.
> Re-measured by testing `.ts` existence on every file in every
> same-namespace collision group: **134** such files, of which **130** are
> library modules under `/lean/QOU/` (where no `.ts` is expected) and **4**
> are content-tree orphans. The four are read in that audit; two are stale
> copies left behind by a block move and a block demotion.
