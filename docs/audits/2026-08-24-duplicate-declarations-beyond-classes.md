# The duplicate-declaration surface is 342 groups, not 38

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

## RETRACTED — `R_q` is not a defect

**This section originally claimed that `R_q` "denotes two different rings" and
that five `abbrev R_q := ℝ` siblings "cross the §7c wall". Both claims are
wrong. I flagged them from a count without reading the declarations.**

`R_q` is declared 95 times with five distinct right-hand sides:

| count | definition |
|---|---|
| 86 | `LaurentPolynomial ℤ` |
| 5 | `ℝ` |
| 2 | `RatFunc ℚ` |
| 1 | `ℤ` |
| 1 | `Archimedean.R_q` |

**All nine non-Laurent declarations are deliberate, and every one states its
reason at the declaration site.** The five `ℝ` ones read:

> *"Ground ring: **archimedean specialisation** `R_q := ℝ` (**AGENTS.md §7c**).
> The numerical substrate value `q₀ ≈ 1.1097` lives in `ℝ`."*

Three cite §7c **by name**, and their files use `Real.*` constructs heavily
(5–19 occurrences each). §7c requires exactly this: a file using `Real.sqrt`,
ordering, or `linarith` *must* declare its types as `ℝ`, with the archimedean
specialisation living in its own file. These are the wall being **observed**,
not crossed. The remaining four are annotated likewise — `RatFunc ℚ` as
*"Ground ring `R_q = ℚ(q)`"*, `ℤ` as *"an abstract carrier type … the axioms
below only require a target type, not the Laurent-polynomial structure"*, and
`Archimedean.R_q` as an alias.

So the corpus uses `R_q` for *"the ground ring at this file's layer"* and
annotates which layer each file is on. That is a convention, documented at each
site — not a fork.

**What the retraction does not touch.** The census measurement above stands: it
counts *names declared in more than one file*, which `R_q` is, and that count
was never a claim about correctness. The error was mine in reading a
name-collision count as a semantic defect without opening the files. The
`prepare-merge` skill's own note about the resolved `QOU.R_q` — `RatFunc ℚ`
against `LaurentPolynomial ℤ` — describes a genuine past collision *within the
library*, which is a different thing from a per-layer convention across
siblings.

## Disposition

Nothing in `content/` changed, and after the retraction above there is **no
confirmed defect here** — only a measurement and one blocked item.

1. **`R5FullWitness` cannot be deduplicated** until `LightNucleus` is, and the
   two `LightNucleus` declarations are not identical (the sibling adds
   `numConstituents`). That is a merge of two type definitions, not a dedup.
2. **The 257 library-vs-sibling pairs** are a *candidate* population, not a
   defect list — and the `R_q` retraction is the reason to say so explicitly.
   A name declared in two files may be a fork, or it may be a deliberate
   per-layer convention annotated at each site. **Deciding which requires
   reading both declarations**, exactly as the one resolved in
   [#5686](https://github.com/litlfred/qou/pull/5686) did. At that rate this is
   a long drain, and worth a decision about whether siblings should carry
   declarations at all before it starts.
3. **The 6 duplicated `inductive`s** are the sharpest sub-population, because a
   forked *type* blocks imports that a forked abbreviation does not —
   `LightNucleus` is the worked case.

### The six, read

Each is exactly **one library-vs-sibling pair in the same namespace** — the §0a
shape, uniformly. Comparing constructor lists splits them four ways, and only
one is a genuine fork:

| type | namespace | verdict |
|---|---|---|
| `Flavor` | `QOU.FlavorDressing` | **identical** — both the 6-flavor list |
| `LightNucleus` | `QOU.BraidKnot` | **identical** — `deuterium \| tritium \| helium3` |
| `Place` | `QOU.AlgebraicSubstrate` | **identical** — `infty \| finite : Nat.Primes → Place` |
| `NucleonType` | `QOU.Archimedean` | **cosmetic** — same constructors; the library adds `Inhabited` to its `deriving` |
| `CrossingType` | `QOU.BraidKnot` | **rename** — `sigma \| sigma_inv \| averaged` against `Plus \| Minus \| Averaged`; the same three-way crossing notion under different constructor names |
| `ConfMorphism` | `QOU.BraidKnot` | **genuine fork** — `unfold \| fold` against `nil \| cons`; two different category constructions, not two spellings of one |

So **four of six carry no semantic question** and one is a naming choice. That
is a better answer than "six pairs, all authorial", which is what this said
before the declarations were read — the same error the `R_q` retraction above
records, caught earlier this time.

**Identical constructors do not make the merge free.** `LightNucleus` is the
caution: the inductive matches exactly, and the *surrounding API* does not — the
sibling defines `LightNucleus.numConstituents`, which the library does not. The
pair still cannot be merged by deleting one side.

**`CrossingType` is declared five times in total**, of which only this pair
collides; the other three sit in different namespaces with three further
constructor lists (`sameUp \| sameDown \| mixed`, `pp \| nn \| mixed`,
`pp \| nn \| pn \| pe \| ne`). Those are not import hazards, but five notions of
"crossing type" under one name is worth an author's eye.
