# The duplicate-declaration surface is 342 groups, not 38 — and `R_q` means two rings

**Date:** 2026-08-24 · **Bean:** `qou-hjf4`
**Tool:** [`scripts/duplicate-class-declaration-census.py`](../../scripts/duplicate-class-declaration-census.py) (`--self-test`)
**Predecessor:** [`2026-08-24-faithful-instance-family.md`](2026-08-24-faithful-instance-family.md) §Finding D

---

## How this was found: a dedup that turned out to be impossible

`R5FullWitness` was the last "kind A" item — a class declared in both
`lean/QOU/BraidKnot/WitnessR5Full.lean` and the 767-line sibling
`mass-theory/conj-canonical-knot-id-sdp.lean`, apparently resolvable by having
the sibling import the library module.

**It is not resolvable that way.** The sibling declares its own
`inductive LightNucleus` (plus `LightNucleus.A`, `LightNucleus.n₀`) in
namespace `QOU.BraidKnot` — and the library's `WitnessR5Full` imports
`QOU.BraidKnot.LightNucleus`, which declares those same names in that same
namespace. The import fails with `environment already contains`. The blocker is
not `R5FullWitness` at all; it is that the sibling **forks the type the class
is indexed by**.

That `inductive` was invisible to the census, which scanned `class` and
`structure` only.

## The corrected measurement

The census now scans `class`, `structure`, `inductive`, `abbrev` and `def`.
(`theorem`/`lemma` are deliberately excluded — duplicating a proof is
redundancy, not a fork of a definition, and including them would bury the
definitional collisions this exists to surface.)

| | class/structure only | all declaration kinds |
|---|---|---|
| distinct names | 930 | **21 027** |
| declared in >1 file | 61 | **795** |
| ≥2 in the **same namespace** | 38 | **342** |
| files involved | 85 | **953** |
| library-vs-sibling pairs (§0a shape) | 27 | **257** |

Lean's environment is flat: a duplicated `def` collides on import exactly as a
duplicated `class` does. The kinds previously skipped carry **213** of the
same-namespace duplicates against `class`/`structure`'s 38.

## `R_q` denotes two different rings, and one of them crosses the §7c wall

`R_q` is declared **95 times** with **five distinct right-hand sides**:

| count | definition | library | sibling |
|---|---|---|---|
| 86 | `LaurentPolynomial ℤ` | 5 | 81 |
| **5** | **`ℝ`** | 0 | **5** |
| 2 | `RatFunc ℚ` | 1 | 1 |
| 1 | `ℤ` | 0 | 1 |
| 1 | `Archimedean.R_q` | 0 | 1 |

The five `abbrev R_q := ℝ` are the serious ones. AGENTS.md §7c makes the
substrate→archimedean wall a STRICT rule, and `ℝ` is the archimedean side
while `LaurentPolynomial ℤ` is the substrate ring. **The same symbol names
both, in the same paper.** In `QOU.Information` alone, `R_q` is `ℝ` in three
files (`phase-transition-boundary`, `quantum-ideal-gas-law`,
`quantum-pressure`) and `LaurentPolynomial ℤ` in two (`q-game-of-life`,
`quantum-entropy`).

`q_param` (71 declarations) and `q_inv_param` (68) have the same shape.

### This does *not* contradict the resolved `QOU.R_q` — it is a different population

`local/prepare-merge` records the `R_q` collision as fixed:

> The worst was `QOU.R_q` — `RatFunc ℚ` in one module and
> `LaurentPolynomial ℤ` in the other … That one is resolved:
> `QOU/GroundRingCore.lean` is the canonical minimal module, and no `R_q`,
> `q_param` or `q_inv_param` appears in the report any more.

**Verified, and it is true.** Restricted to the Lake library tree, `R_q` has
**6** declarations and **zero** same-namespace collisions; `q_param` and
`q_inv_param` likewise. `GroundRingCore.lean` did its job.

The 89 remaining `R_q` declarations are **content-block siblings**, which
`check-duplicate-decls.ts --package qou` does not scan. So the resolved library
population has an unresolved sibling population roughly **15× larger**, outside
the existing checker's scope.

**Import-hazard vs semantic hazard — they are not the same here.** Content-block
siblings are not in the Lake tree and nothing imports them, so sibling-vs-sibling
collisions are *latent*: they cannot actually fail an import today. What is not
latent is the **notation** problem. A reader, a checker, or a `lean.ref`
resolution that lands in one block sees `R_q = ℝ`; the next block over it is
`LaurentPolynomial ℤ`. That is the §7c wall and the notation-register collision
discipline, not the import graph.

## Disposition

Nothing in `content/` changed. Three items, in order of what I would do:

1. **The five `R_q := ℝ` siblings** — a §7c wall question per file: is that block
   genuinely archimedean (in which case the symbol is wrong) or substrate (in
   which case the definition is)? Authorial, but small and well-defined.
2. **`R5FullWitness` cannot be deduplicated** until `LightNucleus` is, and the
   two `LightNucleus` declarations are not identical (the sibling adds
   `numConstituents`). That is a merge of two type definitions, not a dedup.
3. **The 257 library-vs-sibling pairs** are the §0a backlog. The one resolved
   this session (`graded-trace-residue-split`) took a read of both files plus a
   check that nothing unique was lost; at that rate this is a long drain, and
   worth a decision about whether siblings should carry declarations at all.
