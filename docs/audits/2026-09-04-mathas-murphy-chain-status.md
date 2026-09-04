# Mathas' route to the Murphy basis — the exact chain, and where the corpus stands

**Date:** 2026-09-04 · **Bean:** `qou-phir` · **Branch:** `claude/garnir-shape-construction-2026-09-04`
**Source:** [`library/hecke-alg/sections/sec-000-document.md`](../../library/hecke-alg/sections/sec-000-document.md)
(Mathas, *Hecke algebras and Schur algebras of the symmetric group*), lines 4112, 4343, 4451, 4489, 5132.

## Why this document

[`2026-08-31-murphy-basis-triangular-lever-refuted.md`](2026-08-31-murphy-basis-triangular-lever-refuted.md)
§4 established that the `Triangular` lever cannot prove the Murphy basis and that
Mathas' route is the replacement, with **spanning (Lemma 3.14)** as the single open
input. It did not decompose 3.14. This does, from the source, because the
decomposition **reorders the work**: the next lemma to prove is *not* the one that
looked next.

## The chain

Read bottom-up; each lemma's proof invokes the one above it.

| Mathas | statement (decoded from the OCR) | corpus |
|---|---|---|
| **3.9** | `μ` a **composition**, `ν` its reordering into a partition, `s,t` row-standard `μ`-tableaux ⇒ `m_{st}` is an `R`-combination of `m_{uv}` with `u,v` row-standard **`ν`**-tableaux | **open — nothing** |
| **3.12** | `g` a Garnir tableau ⇒ ∃ partition `ν >_lex λ` with `m_{t^λ g} = h + Σ_{s ∈ Std(ν), s ⊵ g} m_{t^ν s}`, `h` a combination of row-standard `ν`-terms | **shape half proved** (`GarnirShape.garnirShape_lexGt`); algebra half open, and it *calls 3.9* |
| **3.13** | `t` row-standard, not standard ⇒ ∃ Garnir `g`, `w ∈ S_n` with `t = g w` and `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)` | **length half proved** (#6444/#6527/#6557/#6598, `exists_garnir_length_additive`) |
| **3.14** | `s,t` row-standard `λ`-tableaux ⇒ `m_{st}` is a combination of `m_{uv}` with `u,v` **standard** `ν`-tableaux, where either **(i)** `ν >_lex λ`, or **(ii)** `ν = λ` and `u ⊵ s`, `v ⊵ t` | open — this is the spanning input |
| **3.20** | the Murphy basis | `murphyBasisOfSpanning`, sorry-free, spanning as an explicit hypothesis |

## Correction to the plan stated in PR #6691

That PR's body says the next step is *"the algebra half of 3.12"*. **That is out of
order.** 3.12's proof ends:

> *"In order to complete the proof we need to show that `h = Σ_v m_{vt^ν}` has the
> required form. Let `ν` be the partition obtained from `μ` by reordering its parts.
> Then `ν > μ` so the result follows from **Lemma 3.9**."*

So the algebra half of 3.12 is *an application of 3.9*, and 3.9 is not in the corpus
in any form. **3.9 is the next lemma**, and it is upstream, not downstream.

What 3.12 needs from this branch is only the *"then `ν > μ`"* step, which is now
`garnirShape_lexGt`.

## The two orders are both live, and that is not a contradiction

3.14 case **(i)** is lex on **shapes**; case **(ii)** is dominance `⊵` on **tableaux**
within a fixed shape. So the induction is a genuine double one, and the two
refutations this arc produced are consistent with it rather than with each other:

- [`2026-07-06-garnir-strict-domweight-counterexample.md`](2026-07-06-garnir-strict-domweight-counterexample.md)
  killed dominance as a **strict** tableau-level measure. Mathas uses `⊵` in case (ii)
  **non-strictly**, with lex doing the strict work in case (i). No conflict.
- PR #6653 killed dominance as the **shape** order for the Garnir step (86 failures in
  910 nodes). That is case (i), where Mathas says lex explicitly.

The practical rule: **lex across shapes, dominance within a shape.** An agent that
picks one order for both will hit one of the two counterexamples.

## Lemma 3.9's shape, for whoever takes it

The proof is a conjugation argument, not a counting one:

> *"Choose an element `d ∈ S_n` such that `S_ν = d S_μ d⁻¹` and such that `t^μ d` and
> `t^ν d⁻¹` are both row standard (`d` and `d⁻¹` permute the rows of `t^μ` and `t^ν`
> respectively). Then `S_ν d = d S_μ`, `d ∈ D_μ` …"*

So it needs: Young subgroups of a **composition** (not just a partition), the
conjugating `d` that sorts the rows, and `D_μ` the distinguished coset
representatives. The corpus has `youngSubgroup` for a *tableau's* row stabiliser
(`HeckeMurphyYoung`); whether it has composition-indexed Young subgroups or `D_μ` at
all has **not** been checked here and should be corpus-grepped before any of it is
written.

## Lemma 3.9's inputs — the corpus-grep, run

Flagged above as "not checked". Now checked, and the first vocabulary tried was the
wrong one: `D_mu`, "distinguished coset representative" and `cosetRep` return
nothing. The infrastructure is there under **"minimal-length coset representative"**,
in [`QOU/Machinery/CoxeterParabolicCoset.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/CoxeterParabolicCoset.lean),
**sorry-free** (0 code sorries, comments stripped):

| declaration | content | conditional? |
|---|---|---|
| `parabolic cs J` | the parabolic subgroup `W_J` | no |
| `SameCosetJ` + refl/symm/trans | the coset relation | no |
| `IsMinRep` | minimal-length coset representative — **this is `D_μ`** | no |
| `exists_minRep` | every coset has one | **no — unconditional** |
| `minRep_not_isRightDescent` | a minimal rep has no `J`-descent | no |
| `length_minRep_mul_wordProd` | the lifting lemma `ℓ(u · π p) = ℓ(u) + |p|` | **yes — on `RightExchangeProp`** |

That file states the exchange property (Bjorner–Brenti Thm 1.4.3) as an explicit
hypothesis rather than an axiom or a `sorry`, on the ground that Mathlib lacks it.

### That "upstream Mathlib gap" is REAL, re-checked today

Given how much of this arc turned out to rest on stale notes, it was worth
re-measuring rather than trusting. Enumerating the Lean environment directly (the
`lean-lsp` MCP server is `CONNECT_TIMEOUT`, and the restored olean cache carries no
Coxeter `.ilean`, so neither `leansearch` nor an index grep can answer it):

    import Mathlib.GroupTheory.Coxeter.Inversion + .Length
    run_cmd  -- every constant whose name contains "Coxeter" and exch/delet/isreduced

returns **`IsReduced` machinery only — zero hits on "exch" and zero on "delet"**. So
the gap is current, not stale, and `length_minRep_mul_wordProd` is rightly
conditional. **Do not go looking for `CoxeterSystem.exchange`; it is not there.**

### But type A does not need it

The generic lifting lemma is blocked; the **type-A** length-additivity criterion is
not. `QOU.Hecke.LengthAdditive.length_mul_eq_add_iff` (#6444, merged `a2edbcffb7`,
sorry-free) gives, for `Perm (Fin (n+1))`,

    ℓ(u·v) = ℓ(u) + ℓ(v)   ↔   invSet v ⊆ invSet (u·v)

**unconditionally**, by inversion sets rather than by exchange. The Murphy basis is a
type-A statement, so the exchange gap is not on its critical path — a route around it
already exists inside this same arc, and `exists_garnir_length_additive` (#6598) is
built on it.

## Status of the pieces this branch added

All sorry-free, `#print axioms` clean:

- `PartitionLex` (#6653, merged `c20a10e766`) — the lex order, `lexGt_of_partitionDom_of_ne`
  (dominance ⇒ lex, Mathas' own note), `dom_fails_lex_holds` (the converse fails),
  and `lexGt_of_colLen` (a lex step from two column-length facts).
- `PartitionOfComposition` (#6691) — `colLen_ofComposition`: a composition's column
  lengths are its part counts, so no sorted-list reasoning is needed downstream.
- `GarnirShape` (#6691) — `garnirShape_lexGt`.
