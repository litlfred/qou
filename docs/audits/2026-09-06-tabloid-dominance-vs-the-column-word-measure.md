# 3.14's inner induction axis is a tabloid-level measure — and the corpus already has a counterexample to one

**Date:** 2026-09-06 · **Bean:** `qou-phir` · **Branch:** `claude/mathas-314-descent-2026-09-06`

## The finding

`MurphyInductionMeasure.murphyLex` (merged, #6899) is a lexicographic product:

* **outer** — `PartitionLexWellFounded.lexGtOn`, lex across shapes of fixed size;
* **inner** — `DominanceWellFounded.domGtOn`, **strict dominance on `Specht.Tabloid μ`**.

Opening the next step — 3.14's descent — with the corpus-grep the arc's discipline requires
turned up a directly relevant result that **neither of those two files cites**, and that a
topic-grep for "3.14" or "Murphy" does not reach because it lives in the `q = 1` Specht
tree under the word *straightening*.

[`SpechtStandardBasisCore.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/SpechtStandardBasisCore.lean),
§"Measure correction (2026-07-07)", lines 81–90 and 821–836:

> An earlier version used `domWeight` (a linear extension of *tabloid dominance*). That
> measure is **wrong** for straightening: `straightening_step_colMax` stated over it is
> FALSE (exact-arithmetic disproof, μ=(3,2), t=[[1,2,3],[5,4]]; audit §3.5), because Garnir
> produces terms whose tabloids are dominance-*incomparable* to `{t}`.
>
> […] **so no tabloid-level measure orders them.**

The replacement is the classical **column-reading word** `colWordNum` (James Thm 8.4, Sagan
§2.6), *"validated exhaustively to (3,3,2)/(4,3,1)"*, on which the whole `q = 1` spanning
argument then goes through **sorry-free**: `straightening_step`,
`straightening_step_colMax`, `standardPolytabloid_straightening`. `domWeight`/`domBound`
survive as *"orphaned […] no longer on the spanning path"*.

Counterexample audit:
[`2026-07-06-garnir-strict-domweight-counterexample.md`](2026-07-06-garnir-strict-domweight-counterexample.md).

## What this does and does not establish about `murphyLex`

**Stated carefully, because the two claims are different and only one is measured.**

What is measured: a **Garnir step in the `q = 1` polytabloid straightening** produces terms
whose tabloids are dominance-incomparable to the source's, at an explicit shape and tableau.

What is **not** measured, and must not be inferred from it: that Mathas 3.14's case (ii)
has the same defect. Three reasons to keep them apart:

1. **Different step.** Sagan §2.6 straightens a *polytabloid* `e_t` in the Specht module.
   Mathas 3.14 rewrites a *Murphy element* `m_{st}` in `H_n(q)`. That they share the name
   "Garnir" is not an argument.
2. **Different strictness.** Mathas' case (ii) states `u ⊵ s`, `v ⊵ t` — **non-strictly** —
   with case (i)'s lex drop doing the strict work. `domGtOn` is the *strict* part. The
   chain-status audit already records this reconciliation
   ([`2026-09-04`](2026-09-04-mathas-murphy-chain-status.md), §"The two orders are both
   live"), and it is why the 2026-07-06 counterexample was not treated as fatal then.
3. **The outer axis may carry every Garnir step anyway.** `GarnirShapeCard.lexGtOn_garnirPartOf`
   (merged) shows the Garnir step drops the **shape**, so on that step `murphyLex` descends
   on the outer axis and never consults dominance. If case (ii) is reached only by steps
   that do *not* change the shape, the counterexample's population and case (ii)'s may be
   disjoint.

So the honest status is: **`murphyLex` is not refuted, and it is not validated either.**
What is new is that the corpus holds a measured reason to doubt the inner axis and a
*validated alternative* for the same job, and the merged files pointed at neither.

## Why this is worth recording rather than just fixing

`murphyLex_wellFounded` proves the measure **terminates**. It says nothing about whether the
terms 3.14 produces actually **descend** in it — the scope note in
`MurphyInductionMeasure.lean` says exactly that. So the risk is not an unsound proof; it is
a measure that terminates and that the descent step cannot be proved against, discovered
after an induction has been written on it. That is what happened at `q = 1` in July, and it
cost a measure plus everything stated over it.

## The measurement that would settle it

A probe, in the arc's established style — exact arithmetic, self-checked, refuting-or-not
before any Lean:

> For every shape `μ ⊢ n` (n ≤ 6) and every row-standard non-standard `t`, take the Garnir
> tableau `g` and the `w` of 3.13 (already built,
> `DescentNodeExists.exists_garnir_length_additive`), expand `m^row_{s t} = m^row_{s g}·T_w`
> in the Murphy family, and ask of each surviving term `m_{uv}`: is its shape lex-greater
> than `μ`, or — when equal — is `u` dominance-comparable to `s`?

Three outcomes, all useful:

* every same-shape term is dominance-**comparable** and descends ⇒ `murphyLex`'s inner axis
  is right and case (ii) differs from the `q = 1` step;
* some same-shape term is **incomparable** ⇒ the `q = 1` counterexample's conclusion carries,
  and the inner axis should be `colWordNum` (which is already built, sorry-free, and has
  `colWordNum_lt_of_first_diff`, `colWordNum_swap_lt`, `fibre_colWordNum_decrease`);
* **no same-shape terms arise at all** ⇒ 3.14's case (ii) is vacuous on this route and the
  induction is single-axis, which would simplify it considerably.

The third is worth naming because it is cheap to test and would make the inner axis moot.

## Two things the corpus turned out to already have

Both were found by this grep and neither was known to the merged work:

1. **A complete, sorry-free straightening theorem at `q = 1`** —
   `standardPolytabloid_straightening`, by well-founded induction on `colWordNum`
   descending. The chain-status audit records that 3.13's *length* half has "NO `q = 1`
   antecedent in the corpus: Sagan's Garnir straightening never tracks Coxeter lengths".
   True of the length half. **It is not true of the spanning half**, which is what 3.14 is,
   and that antecedent is proved.
2. **A validated well-founded measure for exactly this kind of descent**, with its
   monotonicity lemmas already in place.

Neither closes 3.14 — `q`-deformation is the whole difficulty — but the next tranche should
open by asking what the `q = 1` argument gives and what the deformation costs, rather than
deriving from scratch.

## Action taken here

Cross-references added to `MurphyInductionMeasure.lean` and `DominanceWellFounded.lean` so a
reader of either meets this before writing an induction on it. No measure changed, no proof
touched, nothing retracted — the merged results stand exactly as stated.
