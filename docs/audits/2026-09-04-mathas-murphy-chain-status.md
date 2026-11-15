# Mathas' route to the Murphy basis — the exact chain, and where the corpus stands

**Date:** 2026-09-04 · **Bean:** `qou-phir` · **Branch:** `claude/garnir-shape-construction-2026-09-04`
**Source:** [`library/hecke-alg/sections/`](../../library/hecke-alg/sections/) (one file per page since the 2026-11-15 re-ingest; the line numbers below are of the earlier single-file text)
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

### 🛑 CORRECTION (same day): the CORPUS proves exchange, so the lifting lemma is NOT blocked

The measurement above is right about **Mathlib** and the conclusion I drew from it is
wrong. `QOU.Machinery.CoxeterParabolic.rightExchange` — in
[`CoxeterReflectionCocycle.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/CoxeterReflectionCocycle.lean),
merged #4102 — **proves `RightExchangeProp cs` for every Coxeter system**, sorry-free
(`#print axioms`: `[propext, Classical.choice, Quot.sound]`, verified, as is
`strong_exchange` and `length_minRep_mul_wordProd` itself).

So `length_minRep_mul_wordProd` is **conditional only in its statement**: the
hypothesis is discharged elsewhere in this repo, and the generic Bourbaki lifting
lemma is fully available to anyone who wants it. Read the row above as "carries the
hypothesis", not "is blocked".

**How I got it wrong, and it is this document's own subject.**
`CoxeterParabolicCoset.lean`'s header calls the gap "the audited upstream gap" and
says *"nothing here proves the exchange property"* — both true **of that file** — and
I read it, measured Mathlib, and stopped. The sentence that would have redirected me
is in a *different* file. That is the same stale-pointer failure this arc opened with
(`HeckeCellular` claiming the pairing argument was open when `HeckeMurphy` had proved
it), and I walked into it while writing the document that records it.

A cross-reference has been added to `CoxeterParabolicCoset.lean` so the next reader is
not told only half of it.

### Type A does not need it either — but that is now a preference, not a necessity

The generic lifting lemma is blocked; the **type-A** length-additivity criterion is
not. `QOU.Hecke.LengthAdditive.length_mul_eq_add_iff` (#6444, merged `a2edbcffb7`,
sorry-free) gives, for `Perm (Fin (n+1))`,

    ℓ(u·v) = ℓ(u) + ℓ(v)   ↔   invSet v ⊆ invSet (u·v)

**unconditionally**, by inversion sets rather than by exchange. Given the correction
above there is no gap to route around; what remains true is that the type-A route is
**lighter** — it needs no reflection-cocycle machinery and no `IsReduced` residue — and
it is what this arc's results are actually built on
(`CompositionMinimal.length_mul_eq_add_of_isDistinguished`,
`exists_garnir_length_additive` #6598). That is a design choice, not a necessity.

## 🛑 Lemma 3.9's conjugation step is FREE — do not build it

3.9's proof opens by choosing `d` with `S_ν = d S_μ d⁻¹`, and the obvious plan is to
build a block-stabiliser API and prove that conjugacy. **Do not.** Two facts meet:

1. The corpus's Young subgroup is *already* a `MulAction.stabilizer` —
   `Specht.rowStab t = MulAction.stabilizer (Perm (Fin (nOf μ))) (rowPattern t)`,
   where `rowPattern t : Fin (nOf μ) → ℕ` sends a label to its row.
2. Mathlib has the conjugacy in exactly that generality:

       MulAction.stabilizer_smul_eq_stabilizer_map_conj (g : G) (a : α) :
         stabilizer G (g • a) = Subgroup.map (MulAut.conj g) (stabilizer G a)

They compose with **no glue at all** — verified, `lean`-direct **exit 0**:

```lean
example {μ : YoungDiagram} (t : Tableau μ) (d : Perm (Fin (nOf μ))) :
    MulAction.stabilizer (Perm (Fin (nOf μ))) (d • rowPattern t)
      = (rowStab t).map (MulAut.conj d).toMonoidHom :=
  MulAction.stabilizer_smul_eq_stabilizer_map_conj d (rowPattern t)
```

**One catch, and it is why the first attempt reported "unknown constant".**
`QOU.BraidKnot.Specht`'s import cone does **not** reach
`Mathlib.GroupTheory.GroupAction.Basic`, so the lemma is invisible from a file that
imports only the corpus. Add that import; the lemma is there. A missing import
reads exactly like a missing lemma, and this arc has already spent two tranches on
that confusion in the other direction.

### So what is 3.9 actually made of

Not the conjugacy. What remains is:

1. **Composition-shaped tableaux.** `Specht.Tableau` is indexed by a `YoungDiagram`;
   3.9 is stated for a *composition*, whose blocks are not weakly decreasing. Nothing
   in the corpus has this. **This is the real cost of 3.9.**
2. **That the row-sorting `d` carries `μ`'s block pattern to `ν`'s** — i.e. supplying
   the specific `d`, which the Mathlib lemma takes as given.
3. **The Hecke step**: `m_{st}` expands over `m_{uv}`.

## Status of the pieces this branch added

All sorry-free, `#print axioms` clean:

- `PartitionLex` (#6653, merged `c20a10e766`) — the lex order, `lexGt_of_partitionDom_of_ne`
  (dominance ⇒ lex, Mathas' own note), `dom_fails_lex_holds` (the converse fails),
  and `lexGt_of_colLen` (a lex step from two column-length facts).
- `PartitionOfComposition` (#6691) — `colLen_ofComposition`: a composition's column
  lengths are its part counts, so no sorted-list reasoning is needed downstream.
- `GarnirShape` (#6691) — `garnirShape_lexGt`.

## Update 2026-09-05 — 3.9's two named inputs are now both in the corpus, sorry-free

The section above ends by saying `D_μ` exists generically (`IsMinRep` /
`exists_minRep` in `CoxeterParabolicCoset`) but that the **composition-indexed** form
Mathas' 3.9 actually uses had not been checked. It is now built, concretely for
`S_n` and `Composition (n+1)`, on branch `claude/mathas-coset-completeness-2026-09-05`:

| Mathas | statement | declaration | status |
|---|---|---|---|
| **3.3** | `D_μ` meets each right coset of `S_μ` in exactly one element, and `ℓ(v·d) = ℓ(v) + ℓ(d)` there | `CompositionCosetExists.existsUnique_isDistinguished_mem_coset`, `CompositionMinimal.length_mul_eq_add_of_isDistinguished` | **proved, sorry-free** |
| **3.4** | `M^μ = x_μ H` is free on `{x_μ T_d : d ∈ D_μ}` | `CompositionCosetSum.repr_xComp_mul_Tw`, `.linearIndependent_xComp_mul_Tw` | **proved, sorry-free** |

`repr_xComp_mul_Tw` is the concrete form worth quoting: **in the `T_w` basis the
coordinates of `x_μ T_e` are the indicator function of the coset `e·S_μ`** — every
coordinate `0` or `1`, and `q` does not appear. Freeness is then disjointness of
cosets plus `TwBasis.basisTwOfField`.

### Two orientation traps, both measured rather than guessed

1. **`sortPerm`** (the conjugating `d` of 3.9) is length-additive on one side only.
   Measured exhaustively: the orientation now in `CompositionYoung` is additive
   1955/1955; its inverse fails 522/1955
   ([`sortperm_length_additive_probe.py`](../../computations/hecke/sortperm_length_additive_probe.py)).
2. **`Tw_mul_Tw` is flipped** (`T_v · T_w = T_{w·v}`), so `x_μ · T_e` lands on a
   **left** coset while `IsDistinguished` is the **right**-coset notion. The two meet
   through `ℓ(x) = ℓ(x⁻¹)`, so the correct hypothesis is `IsDistinguishedL c e :=
   IsDistinguished c e⁻¹`, and Prop 3.3 transports with no second argument
   (`existsUnique_isDistinguishedL`). An agent that skips this gets a length
   hypothesis that is simply false.

### What is still open on the chain

Unchanged, and now sharper: **Lemma 3.9 itself**. Its algebraic engine is
`CompositionIntertwine.Tw_sortPerm_mul_xComp` (`T_d · x_μ = x_ν · T_d`, sorry-free) and
its two structural inputs are the table above. What is *not* in the corpus is the
bridge from **row-standard `μ`-tableaux to coset representatives** — Mathas' `d(t)` for
a *composition*-shaped tableau — without which "`m_{st}` is an `R`-combination of
`m_{uv}`" cannot even be stated. That is the next thing to build, and it is combinatorial
rather than algebraic.

### 🛑 CORRECTION (2026-09-05, same day, minutes later): `d(t)` IS in the corpus

The section immediately above ends: *"the bridge from **row-standard `μ`-tableaux to
coset representatives** — Mathas' `d(t)` … — is absent"*. **That is false**, and I wrote
it without running the corpus-grep checklist on that specific claim — the same failure
this document already records once, three sections up.

[`QOU/BraidKnot/TableauPerm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/TableauPerm.lean)
supplies exactly it, and its own docstring opens *"`d(t)`: the permutation carrying the
reference tableau to `t`"*:

| declaration | content |
|---|---|
| `refTab μ` | the row-superstandard reference `t^μ` |
| `dOf t` | **`d(t)`** |
| `dOf_unique`, `dOf_smul` | characterisation, and `t = w • g ⇒ d(t) = w · d(g)` |
| `dOf_injective` / `_surjective` / `equivPerm` | tableaux `≃` permutations |
| `length_dOf_smul_eq_add_iff` | Mathas' length condition, reduced to an inversion claim |

`RowStandardTableau.lean` likewise has `IsRowStandard`, `IsColStandard`, `IsStandard`,
all decidable, with `RowStandardTab μ` a `Fintype`.

**What is genuinely missing is narrower, and the correction shrinks it twice over.**
`Specht.Tableau μ` is indexed by a `YoungDiagram`, i.e. a **partition** shape; Mathas 3.9
is about a **composition** `μ`, whose rows need not decrease, so `dOf` does not apply to
it as stated. The remaining gap is therefore *composition-shaped* tableaux only.

**And that gap is smaller than it looks, because `IsDistinguished` already IS row
standardness.** Read `d : Fin n → Fin n` as *entry ↦ cell* — which is how `dOf` is
oriented. The cells of row `i` of a composition are the consecutive positions
`sizeUpTo i .. sizeUpTo i + blocksFun i − 1`, so `c.index` is exactly "which row is this
cell in", and

    IsDistinguished c d  ≡  ∀ a b, c.index (d a) = c.index (d b) → a < b → d a < d b

says precisely *entries increase left-to-right along every row* — row standardness,
verbatim. So Prop 3.3, proved today, already reads: **every right coset of `S_μ`
contains exactly one row-standard composition tableau.** What is left is the tableau
*vocabulary* wrapping a fact that is proved, not a new proof.

**So "the next node is combinatorial rather than algebraic" overstates it too.** Both
halves of that sentence were written from an absence I had not measured.

## Where 3.9 actually stops, and why — the `T_d⁻¹` obstruction

`CompositionIdeal.exists_xComp_swap` proves `a · x_μ · b = (a T_d⁻¹) · x_ν · (T_d b)`, and
its commit called that **sharper** than Mathas' *`R`-combination*. That is true in one
direction and **false in the other**, and the difference is the whole remaining problem:

- **Stronger as a statement about ideals.** `T_d` is a unit, so `H x_μ H = H x_ν H`
  — equality, not containment, and one term rather than a combination.
- **Weaker as a statement about the Murphy basis.** Nothing there says `a T_d⁻¹` and
  `T_d b` are again of Murphy form `T*_{d(u)}`, `T_{d(v)}`.

They generally are not, for an exact reason rather than a suspicion: **`T_w⁻¹ ≠ T_{w⁻¹}`.**
At a simple reflection `s` is an involution, so `T_{s⁻¹} = T_s` — while the quadratic
relation forces the *algebra* inverse over two basis elements,

    σ⁻¹ = q⁻¹·T_s − q⁻¹(q−1)·T_1      (`CompositionIdeal.inv_Tw_sw_expansion`, proved)

Iterated along a reduced word for `d`, `T_d⁻¹` generically meets up to `2^ℓ(d)` basis
elements. **That spread is Mathas' `R`-combination.** So the two statements never
conflicted: his combination lives at the *basis* level and collapses to a single term
exactly when one stops requiring the coefficients to be Murphy-shaped.

**So the remaining step is not vocabulary.** Reaching 3.9 as stated means expanding
`T_d⁻¹` in the `T`-basis and showing the surviving terms are indexed by row-standard
`ν`-tableaux — a triangularity argument, and genuinely the next piece of mathematics on
this chain. The estimate in the update above (*"vocabulary over a proved fact"*) applies
to Prop 3.3's tableau restatement, which is done (`existsUnique_rowStandard`), and **not**
to this.

### The support of `T_d⁻¹`, measured — and the handedness trap for the third time

The section above says the remaining step is a triangularity argument over the `T_d⁻¹`
expansion. Before building any of it,
[`tw_inverse_support_probe.py`](../../computations/hecke/tw_inverse_support_probe.py)
measures that support exactly (sympy over `ℚ(q)`, no float), over all of `S_2`, `S_3`,
`S_4`:

| | |
|---|---|
| (A) support has length `≤ ℓ(w)` | **32 / 32** |
| (B) support inside Bruhat `[e, w]` | 16 / 32 |
| (C) leading coefficient at `w` is `q^{−ℓ(w)}` | 16 / 32 |
| **(B′) support inside Bruhat `[e, w⁻¹]`** | **32 / 32** |
| **(C′) leading coefficient at `w⁻¹` is `q^{−ℓ(w)}`** | **32 / 32** |
| involutions (`w = w⁻¹`) in range | 16 / 32 |

**The naive statements hold on exactly the involutions, and nowhere else.** In this
corpus's convention `T_w⁻¹` is triangular with respect to **`w⁻¹`**, not `w` — because
`Tw_mul_Tw` is flipped. That is the same trap as `sortPerm`'s orientation and as
`IsDistinguishedL`, now for the third time on this arc, and it is exactly the kind of
thing that would have made a triangularity formalisation fail after it was written.

**A slack bound to stop quoting.** `2^ℓ(w)` is attained only for `ℓ ≤ 3`; the longest
element of `S_4` (`ℓ = 6`) spreads over **24** terms, not 64. The real bound is the size
of the interval `[e, w⁻¹]`.

**The probe checks itself before printing a verdict**, and that is not decoration: its
first version reported "(B) fails for half of `S_4`" from a Bruhat test with an unverified
reduced-word orientation and a subword enumeration that built the wrong set. It now
asserts that every reduced word multiplies back to its permutation with the right length,
and that `T_w · T_w⁻¹ = T_w⁻¹ · T_w = T_1` symbolically, before any support claim is
printed. The 16/32 above survived that fix; the earlier run's *different* 32/32 on (C) did
not.

**Consequence for the next agent.** State triangularity against `w⁻¹`. The subword order
has to be built before 3.9 can be stated at basis level: Mathlib has no Bruhat order, and
the corpus's `QOU/Mathlib/KazhdanLusztigBasis.lean` is an abstract `BarInvolution`/`KLBasis`
axiomatisation with no concrete construction.

> **🛑 CORRECTION (same day) — the CONCLUSION above is right and the EVIDENCE I first gave
> for it was worthless.** This paragraph read *"Mathlib has no Bruhat order (`grep Bruhat`
> over `Mathlib/GroupTheory/Coxeter/` returns nothing)"*. That grep cannot return anything:
> in this sandbox `.lake/packages/mathlib` holds **6990 oleans and zero `.lean` files**, so
> every Mathlib source grep is silent whatever the truth is — and `ls` on a Mathlib source
> path prints nothing rather than erroring, which is how it passed unnoticed.
>
> Re-measured by the method that works against an olean-only tree — **enumerating
> `env.constants`** after importing `Coxeter.Length` and `Coxeter.Inversion`
> ([`scripts/lean-probes/`](../../scripts/lean-probes/)):
>
>     Coxeter constants reachable: 439
>       containing 'ruhat' : 0
>       containing 'ubword': 0
>
> Corroborated by a **filename** check, valid because the olean tree is real:
> `find … -iname '*bruhat*'` returns nothing, and the only Coxeter oleans are `Matrix`,
> `Inversion`, `Basic`, `Length`.
>
> **The lesson is the method, not the answer.** *"My grep found nothing"* and *"it is not
> there"* are different claims, and against a source-less checkout only the first is ever
> measured. The same trap does **not** apply to this arc's earlier exchange-property
> finding, which used environment enumeration from the start — and that is exactly why
> that one held up.

## 3.9 is proved in span form — and the follow-up I proposed is FALSE

**Proved and merged** (#6871, `5869585579`), all sorry-free:

| | declaration |
|---|---|
| `x_μ · T_v = q^{ℓ(v)} · x_μ` for all `v ∈ S_μ` | `CompositionEigenPower.xComp_mul_Tw_of_mem` |
| the mirror, `T_v · x_μ` | `CompositionCosetReduceMirror.Tw_mul_xComp_of_mem` |
| `x_μ · T_a` reduces onto `D_μ` | `CompositionCosetReduce.xComp_mul_Tw_reduce` |
| `T_a · x_μ` reduces onto `D_μ` | `CompositionCosetReduceMirror.Tw_mul_xComp_reduce` |
| **3.9, span form** | `CompositionDoubleCoset.mul_xComp_mul_mem` |

The eigenvector power is the one worth reading: the obvious proof needs the parabolic
fact (a parabolic subgroup is Coxeter on the simple reflections it contains), which the
corpus does **not** have. It is avoidable because a Young-subgroup element can only
descend *within* a block, so every descent is automatically at a generator of `S_μ`.

### 🛑 The follow-up I named as "next" does not hold

I proposed proving the double-coset terms **linearly independent**, which with the span
statement would give a basis of `H x_μ H`. **That is false**, and the counting settles it
before any Lean is attempted. At `μ = (1,…,1)`:

* `S_μ` is trivial, so `x_μ = 1`;
* every `d` is distinguished (the condition quantifies over pairs sharing a block, and no
  two positions do), so `D_μ = S_n`;
* the family is `{T_d · T_e}` — **`(n!)²` members in an `n!`-dimensional space.**

Measured exactly over `ℚ(q)` in
[`double_coset_independence_probe.py`](../../computations/hecke/double_coset_independence_probe.py):

| n | μ | pairs | rank | dim H |
|---|---|---|---|---|
| 2 | (2) | 1 | 1 | 2 |
| 2 | (1,1) | 4 | **2** | 2 |
| 3 | (2,1) | 9 | **5** | 6 |
| 3 | (1,1,1) | 36 | **6** | 6 |
| 4 | (2,2) | 36 | **14** | 24 |
| 4 | (1,1,1,1) | 576 | **24** | 24 |

Independent only in the degenerate `μ = (n)` rows, where there is one pair.

**The correct route to a basis is different.** Murphy's basis is indexed by pairs of
**standard** tableaux of a **common shape**, summed over shapes — not by pairs drawn from
one `D_μ`. The corpus already carries the matching count:
`HeckeMurphyYoung.murphyIndex_card_eq_finrank` shows that index set has exactly
`dim H_n(q)` elements, by RSK/Burnside. So **spanning + that cardinality** is the route,
which is precisely why **3.14 is the arc's real open node** and always was.

## Update 2026-09-06 — 3.13 is lifted to the `T`-basis, and a reference-tableau gap surfaces

The section above lands on 3.14 as the real open node. Its two induction axes now have a
well-founded measure (`MurphyInductionMeasure.murphyLex_wellFounded`), the `T_d⁻¹`
triangularity that 3.9 at basis level needs is proved against `w⁻¹`
(`TwInverseBruhat.TwInv_mem_spanBruhatLe`, the orientation the probe demanded), and the
Garnir step is known to drop the shape in the order the outer axis runs on
(`GarnirShapeCard.lexGtOn_garnirPartOf`). What was left was the **step** 3.14's induction
rewrites with, and that is now proved.

[`QOU/BraidKnot/MurphyGarnirFactor.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MurphyGarnirFactor.lean),
eight declarations, all sorry-free (`#print axioms`: `[propext, Classical.choice,
Quot.sound]`), `lean`-direct exit 0:

| declaration | content |
|---|---|
| `HeckeMurphyYoung_dOf_smul`, `dAt_smul` | `d(w·g) = w·d(g)` for the **column**-superstandard reference — the companion of `TableauPerm.dOf_smul`, which was missing |
| `invSet_toFinSucc_mono` | inversion containment survives the re-indexing `Fin (nOf μ) ≃ Fin (n+1)` |
| `Tw_dOf_smul`, `Tw_dAt_smul` | **the lift**: a length-additive tableau factorisation becomes `T_{d(w·g)} = T_{d(g)} · T_w` |
| `smul_eq_of_dOf` | recovers the `w` from `d` being a bijection |
| `exists_garnir_Tw_factor` | **Mathas 3.13 in the `T`-basis** — a row-standard non-standard `t` has `T_{d(t)} = T_{d(g)} · T_w` through a Garnir `g` |
| `murphyM_smul` | `m_{s, w·g} = m_{s, g} · T_w` |

The whole content is that `T` **is** a homomorphism on a length-additive factorisation
(`TwBasis.Tw_mul_Tw`) though not on `S_n`; everything else is routing the hypothesis.

### The flipped handedness pays off, for once

`Tw_mul_Tw` reads `T_v · T_w = T_{w·v}`. So the permutation factorisation `d(t) = w · d(g)`
lifts with `T_w` on the **right** — which is the side Mathas needs, because
`m_{st} = T*_{d(s)} · x_λ · T_{d(t)}` has `T_{d(t)}` rightmost, so the Garnir factor lands
adjacent to `x_λ` and the residual is peeled off outside. The unflipped convention would
have produced `T_w · T_{d(g)}` and stranded `T_w` in the middle. This is the **fourth**
instance of the handedness trap on this arc (after `sortPerm`'s orientation,
`IsDistinguishedL`, and `T_w⁻¹`'s triangularity against `w⁻¹`) and the first where it helps
rather than costs.

### 🛑 The gap this exposed: **two reference tableaux, both called `dOf`**

`d(t)` is *"the permutation carrying the reference tableau to `t`"*, and this corpus has two
references, in two files, under one name:

| | reference | file |
|---|---|---|
| `TableauPerm.dOf` | **row**-superstandard `t^λ` — Mathas' | `QOU/BraidKnot/TableauPerm.lean` |
| `HeckeMurphyYoung.dOf` | **column**-superstandard | `QOU/BraidKnot/HeckeMurphyYoung.lean` |

The entire Garnir chain (`GarnirTableau`, `GarnirDescentAdditive`, `DescentNodeExists`,
`length_dOf_smul_eq_add_iff`) is built on the row one; `murphyM` is built on the column one.
They differ by a fixed permutation on the right — with `c := colSuperstandard ≫ (t^λ)⁻¹`,

    HeckeMurphyYoung.dOf t = TableauPerm.dOf t * c

so the **factorisation** transfers (it is reference-insensitive — that is why both
`dOf_smul`s have the same one-line proof), while **length additivity does not**: `ℓ(x)` and
`ℓ(x·c)` are unrelated, and `length_mul_eq_add_iff` reduces the hypothesis to an
inversion-set containment that right multiplication does not preserve.

**So `exists_garnir_Tw_factor` and `murphyM_smul` are deliberately NOT composed.** The first
is proved for the row reference, the second for the column one, and each is exactly as
strong as its own hypothesis. Chaining them would be **false as an inference** even though
both halves are true — the same arity/scope conflation
[`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md)
records as `da-arity-conflation`. Closing it needs one of:

1. restate `murphyM` over `refTab` (a definitional change to merged code — `murphyM`'s own
   docstring already says the reference is *"a red herring: `colSuperstandard` is as good as
   Murphy's row-superstandard `t^λ` — both are full rank"*, but that was a **rank**
   measurement, and rank is not what is at stake here); or
2. re-prove the Garnir length additivity against the column reference.

Neither is done. Tracked on `qou-phir`.

### A method note: the olean was stale and the signature had moved

`HeckeMurphyYoung.olean` in the restored cache was built 2026-08-31T02:52Z against a source
last committed 05:26Z the same day, and the two disagreed **in the statement**: the cached
`murphyM` carried `[DecidablePred (· ∈ youngSubgroup n h t)]` — the per-`t` row stabiliser
that the file's own docstring records as the rank-deficient version that was **replaced** —
against the live `colSuperstandard μ`. A `#check` against the cache therefore described a
`murphyM` that no longer exists, and any lemma written to that signature would have been
about the wrong object while compiling cleanly.

Rebuilding just that module from source took **5 s** and its dependency cone needed nothing,
so the fix is cheap once noticed. Noticing is the problem: nothing in the toolchain says the
olean is behind, and the signature difference is one instance argument. Compare the
committed source's `git log` timestamp against the olean's mtime before trusting a `#check`.

### 🛑 The cheap way out of that gap is REFUTED (2026-09-06, same day)

The gap above admitted two closures: **(1)** restate `murphyM` over `refTab` — a definitional
change to merged code, touching every consumer; **(2)** re-prove the Garnir length additivity
against the column reference — cheap *if true*. Whether (2) is true is a factual question
about small symmetric groups, so it was measured before either was attempted.

[`computations/hecke/murphy_reference_tableau_additivity_probe.py`](../../computations/hecke/murphy_reference_tableau_additivity_probe.py)
— exact integer arithmetic, no float anywhere, four self-checks that must pass before any
verdict prints (Garnir construction vs Mathas' three worked `λ = (3,3)` examples; the
column-superstandard filling is a bijection and column-increasing; `d(t) = w·d(g)` holds for
**both** references over 886 instances, i.e. the factorisation really is
reference-insensitive; and the ROW column reproduces the sibling probe):

| `n` | row-standard non-standard `t` | **row** reference (Mathas') | **column** reference (`murphyM`) |
|---|---|---|---|
| 3 | 6 | 6/6 | 6/6 |
| 4 | 37 | 37/37 | **30/37** |
| 5 | 220 | 220/220 | **138/220** |
| 6 | 1526 | 1526/1526 | **797/1526** |

Counting a `t` as a success when **some** descent node gives length additivity, which is what
3.13 asserts. Smallest counterexample: `λ = (2,1,1)`, `t = ((1,3),(4),(2))`, whose single
descent node gives `ℓ(d_col(t)) = 2` against `ℓ(d_col(g)) + ℓ(w) = 3 + 1`.

**The failure rate grows with `n`** — 0 %, 19 %, 37 %, 48 % — so this is not a small-`n`
artifact that a larger range would wash out. **Option (2) is false; option (1) is forced.**

Scope, stated per the refutation discipline: this is a **refutation of a specific universally
quantified statement**, with an explicit witness — not a scope-(b) exclusion of an
*ingredient*. Nothing here says the column-superstandard reference is bad for anything else;
it says Garnir length additivity is a property **of the row-superstandard reference**, not a
fact about Garnir tableaux that happens to be recorded relative to one.

**It also corrects a claim already in the corpus.** `murphyM`'s docstring calls the reference
*"a red herring: `colSuperstandard` is as good as Murphy's row-superstandard `t^λ` — both are
full rank"*. That was a **rank** measurement and is still true as one. It does not generalise,
and this is a property where the reference is decisive. The generalisation was never measured;
it was inferred from the rank result, which is the same shape of error as the two absence
claims this document already records.

### The gap is CLOSED — the reference tableau is now a parameter (2026-09-06, same day)

The refutation above forces option (1): the Murphy element must be stated over `t^λ`. That
is done, and **not** by editing `HeckeMurphyYoung` — the reference is made an **explicit
parameter**, since its absence is exactly what let two objects share the name `dOf`.
[`QOU/BraidKnot/MurphyRefTab.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MurphyRefTab.lean),
ten declarations, all sorry-free:

| declaration | content |
|---|---|
| `dOfRef r t`, `dAtRef n h r t` | `d(t)` relative to an arbitrary reference `r` |
| `dOfRef_colSuperstandard`, `dOfRef_refTab` | the corpus's two `dOf`s are the two instances — both `rfl` |
| `dOfRef_smul`, `dAtRef_smul` | `d_r(w·g) = w·d_r(g)` for **every** reference, in one lemma |
| `murphyMRef r s t` | `T*_{d_r(s)} · x_r · T_{d_r(t)}` |
| `murphyMRef_colSuperstandard` | **`murphyM` is one instance, definitionally** |
| `murphyMRow` | `murphyMRef (refTab μ)` — Mathas' element |
| `Tw_dAtRef_smul`, `murphyMRef_smul` | the lift, for every reference at once |
| **`exists_garnir_murphyMRow_factor`** | **3.13 on Mathas' Murphy element: `m^row_{s t} = m^row_{s g} · T_w`** |

Because `murphyM` is *definitionally* `murphyMRef (colSuperstandard μ)`, `murphyFamily`,
`basisOfSpanning` and `murphyBasisOfSpanning` are untouched and keep proving exactly what
they proved. No merged file changed.

**What the parameterisation buys beyond the composition.** `dOfRef_smul` proves
`d_r(w·g) = w·d_r(g)` once, for every reference. The corpus previously had that fact twice —
`TableauPerm.dOf_smul` and `MurphyGarnirFactor.HeckeMurphyYoung_dOf_smul` — with the same
one-line proof and nothing connecting them, which is what made it easy to believe the
reference never mattered. Separating the half that transfers (the factorisation) from the
half that does not (length additivity) is the file's point.

**Rank axis: checked, and narrowly.** The row instance is full rank at `n = 3,4,5`
(`6/6`, `24/24`, `120/120`), the same as the column one. That licenses exactly one thing —
the reference does not change the **rank**. It does change 3.13's length additivity, so the
"red herring" reading stays refuted.

### 🛑 The rank guard that established that had never run

`murphy_supp_rsk_probe.py`'s `run_rank_guard` is defined **below** its file's `if __name__`
block, so it was never called — the *"standing guard rather than a one-off check"* its own
docstring describes had not run in `main` since it was written. It is wired in now (0.02 s /
0.09 s / 16 s at `n = 3/4/5`) and reproduces the figures above. **A guard nobody invokes is
documentation**, which is the same finding this corpus already recorded for
`precision-gates.sh`.

Two labels in it were also wrong in a way that made its output assert something false:

1. The deficient row was tagged *"as the corpus's `murphyM` does"*. That describes the
   **superseded** `murphyM`; the live one sums over the fixed
   `youngSubgroup n h (colSuperstandard μ)`, which is the **full-rank** row. The output was
   accusing current code of a defect it no longer has.
2. *"the reference does not matter"* is scoped to **rank**, and was quoted in `murphyM`'s
   docstring as the reference being *"a red herring"* without qualification. The docstring
   now says which axis it measured.

### What is still open

3.14. The rewriting step is proved on the right object; the induction is not run. What
remains is that the terms it produces **descend** in `MurphyInductionMeasure.murphyLex` —
which needs 3.12's algebra half, and hence 3.9 at basis level. `murphyLex_wellFounded` says
such an induction terminates; it does not say the terms descend.

### A measurement of the Lean sweep gate, taken in passing (2026-09-06)

`prepare-merge-auto` now mandates `scripts/lean-library-sweep.py` for any branch touching
`.lean`, over bare `lean`-direct, because the latter verifies against a **snapshot** of the
olean cache. Running it on this branch produced two figures worth recording, both well
outside what the docs lead an agent to expect:

- **The dirty closure was 1288 modules**, against the **145** #6827 measured and the **74**
  `AGENTS.md` records. It is not drift in the scripts — it is `main`'s Lean churn: the
  closure is computed against *this container's* olean tree, and `main` had moved 26 commits
  since the branch last rebased. **Budget by the closure, not by the documented time.**
- At **45 minutes** it had reached **761 of 1288, every one `ok`, zero RED** — and had not
  yet reached `QOU/BraidKnot/*`, which is alphabetically after `QOU/Archimedean/*`, so it
  said nothing about this branch's own files. Throughput fell from ~64 modules/min to ~5 in
  the `QOU/Archimedean/PauliWitness/*` block.

Two operational notes for the next agent:

1. **The gate as `main` carries it cannot run on a quota-constrained container.** It does a
   2.3 GB `shutil.copytree` of the olean tree; on this container that hit `ENOSPC` and took
   the whole session to **0 MB free**, at which point every command fails — including the
   `rm` that would fix it. The fix (hardlink instead of copy: `du` reads 2.3 GB while `df`
   does not move) is on **#6827**, unmerged. This run used that PR's script from `/tmp`,
   uncommitted, rather than porting it and widening someone else's active scope.
2. **Freeing space:** `content/quantum-observable-universe/lean/.lake/build/ir` is ~1.1 GB of
   C intermediates from Lean's backend. `lean`-direct verification never reads them, and this
   corpus never runs `lake` against a restored cache. Deleting it is the cheapest reclaim.

Neither figure is a defect in the sweep — it did exactly what it claims, and 761/761 green is
a real result about `main`. The point is that its *cost* is a function of how far the branch
has fallen behind, and that is not what the recorded timings suggest.
