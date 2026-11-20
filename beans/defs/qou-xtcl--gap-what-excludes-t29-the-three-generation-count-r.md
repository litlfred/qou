---
# qou-xtcl
title: 'GAP: what excludes T(2,9)? The three-generation count reduces to this ONE lemma. Genus bound (PROVED) admits n in {3,5,7,9}; corpus assigns generations to {3,5,7}. The ''odd primes'' condition that would close it occurs ONCE in the corpus, asserted not derived. Candidate: for odd n>=3, n factors into smaller odd windings iff composite, so sigma^9=(sigma^3)^3 is a harmonic of gen 1 -- prove or refute that a composite odd winding cannot carry a generation.'
status: todo
pr: 8183
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-08-01T22:05:54Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

**Title-only until 2026-10-10 (654 chars, body entirely empty), and it is the
keystone of the `8f-gen` front** — `qou-x4qm` names it as the front's one lemma
and is `blocked-by` it. Body written during the front triage.

## The question, restated so it can be answered

The genus bound admits four odd windings in the `T(2,·)` family. Three
generations requires excluding exactly one. **Which one, and on what grounds?**

## 🛑 There are THREE filters in the corpus, and they give THREE different counts

`qou-x4qm`'s roast says *"two filters, two counts, is the live defect."*
Measured 2026-10-10, it is **three**:

| # | filter | admits | count | status |
|---|---|---|---:|---|
| 1 | Seifert genus `g(T_{m,n}) = (m−1)(n−1)/2 ≤ 4` | `{3, 5, 7, 9}` | **4** | derived; `torus_knot_genus_four_unique` is a real theorem (`interval_cases` + coprimality, sorry-free) |
| 2 | continuant divisibility `b_a ∣ b_n ⟺ a ∣ n`, singling out `9 = 3·3` | `{3, 5, 7}` | **3** | Lean sorry-free, but **the criterion is unrelated to generation counting** (`qou-a5os`, completed) |
| 3 | `S₅`-equivariant embedding into Bring's surface | `{3, 5}` | **2** | narrative argument sound; **its Lean is `trivial`** — see below |

Sources: `brings-surface/torus-embeddable-complete-proof.md` (the enumeration:
`m = 2 ⇒ n ≤ 9`, odd coprime `n ∈ {3,5,7,9}`);
`observations/s5-equivariant-torus-knots.md` (the `{3,5}` statement) and its
`-proof.md`, which states the comparison itself — *"Pure topological
(Seifert-genus) embedding into `Σ₄` admits four knots … The stronger
equivariant criterion retains only `T_{2,3}` and `T_{2,5}`."*

### Why that is worse than "two filters disagree"

**Filters 1 and 3 are two properties of the SAME object.**
`brings-surface-def.md` gives both in one sentence: `Σ₄` *"is a smooth
projective curve of genus 4. Its automorphism group is `Aut(Σ₄) ≅ S₅`."* So
they are not competing criteria to choose between — they are two constraints
imposed by one surface, and they return **four** and **two**. **Three is
produced by neither.** Only filter 2 returns three, and `qou-a5os` already
records why that is not evidence: *"Any criterion eliminating exactly one of
four would have produced three."*

### And the corpus had a SECOND such criterion, also aimed at 9

`prop:lepton-meson-torus-knot-dictionary` read `for n = 3, 5, 7, … (odd
primes)` until 2026-10-10. `9 = 3²` is the only non-prime in `{3,5,7,9}`, so
**primality was doing exactly filter 2's work in a parenthesis** — a second
criterion, unrelated to the first and equally unrelated to generation counting,
excluding the same single element. It was removed on owner instruction (Q1-D,
this PR), so the four-element set is now visible rather than silently trimmed.
That removal does not change any filter's count; it changes what a reader sees.

## What this bean needs

Not "exclude 9". The live defect is upstream of that: **reconcile the filters,
or establish which one is the physical criterion.** Three dispositions, none
enacted here:

- **(a) Filter 3 is the criterion** — then the framework predicts **two**
  generations and the three-generation claim is refuted by its own geometry.
  This is the possibility the roast forecasts as likeliest (*"a proof that the
  filters disagree is likelier than a derivation of three"*) and it is the one
  nobody has written down.
- **(b) Filter 1 is the criterion** — then there are **four**, and a fourth
  generation is a prediction, not a defect to remove.
- **(c) A derivation of three exists that is not any of these** — then it needs
  the physical bridge `qou-x4qm` (i) names: *"normal-form-independent winding ⇒
  generation"*. Nothing in the corpus supplies it.

## Scope note on filter 3, because it is load-bearing for (a)

The `{3,5}` **narrative** argument is sound and complete: an equivariant
embedding needs `ℤ_s ↪ Aut(Σ) = S₅`, which needs an element of order `s`; the
element orders of `S₅` are `{1,2,3,4,5,6}`; odd `s ≥ 3` leaves `{3,5}`.

**Its Lean proves none of that.** `s5-equivariant-torus-knots.lean` declares
`s5OddOrdersGe3 : Set ℕ := {3, 5}` and then states
`(s ∈ s5OddOrdersGe3) ↔ (s = 3 ∨ s = 5)` — set-membership unfolding, `rfl` on
both branches, with **both hypotheses (`3 ≤ s`, `Odd s`) unused** and
`s5ElementOrders` defined and never referenced. The actual content (the orders
of `S₅`) sits in a **docstring**. `Mathlib.GroupTheory.Perm.Cycle.Type` is
imported and unused.

**This is not a new finding — the corpus already measured it.**
`docs/audits/lean-triviality.json` (oracle
`lean-tactic-ladder(trivial|rfl|simp|decide|omega|aesop)`, 802 declarations)
records this one as `{"closed": true, "steps": 1, "tactic": "trivial"}`,
checked 2026-08-07. The block is nonetheless still a `proposition`, with
`validation: "not_checked"`. Disposition across those 802 is another arc's.

**Two incidental defects in the same file**, recorded because the second is a
named pattern:

1. `uses: ["def:brings-surface"]` only — the block's `-proof.md` leans on the
   `S₅` element-order table and on the genus comparison, neither declared.
2. **The manifest's `lean.ref` is `qou:QOU.TorusKnot.s5_equivariant_classification`
   and the file's docstring header says the same, but the declaration is
   `QOU.s5_equivariant_classification`** — the file has `namespace QOU` and no
   `TorusKnot`. The library's only `TorusKnot` namespace is
   `QOU.Archimedean.TorusKnot` (`TorusKnotGenusFourUnique.lean`) and has no such
   declaration. So **two labels agree with each other and both are wrong; only
   the body is right** — the `markovZc` pattern AGENTS.md records verbatim:
   *"Agreement between two labels is not evidence about the third thing."* It
   resolves anyway, because §0a candidate 1 matches on **filename**, so the
   declaration path in a `lean.ref` is never checked.

Tagged `8f-open`: this is open research — three dispositions, one of which
refutes a headline claim — not the one-lemma repair the title implies.


## 🛑 CORRECTION of my own append above (same day) — there are FOUR candidates, not three, and the fourth reframes the problem

The table above says "three filters, three counts". **Measured further the same
day: there is a fourth, and it is the one that makes the problem statable.**

| # | criterion | what it counts | count |
|---|---|---|---:|
| 1 | Seifert genus `≤ 4` | admissible `T(2,n)` indices | **4** |
| 2 | continuant divisibility | candidate 1 minus 9 | 3 |
| 3 | `S₅`-equivariance | `T(2,n)` with `ℤ_n ↪ S₅` | **2** |
| 4 | **branch-point pairs** | complex-conjugate pairs of the Bring fibration's six branch points | **3** |

**Candidate 4 is `ex:archimedean-yekutieli`:** *"These correspond to the three
pairs of branch points under `S₃ ⊂ S₅`. … The three lepton generations then
correspond to the orbits of the cyclotomic Galois group on the six branch
points. The fact that there are exactly three generations is a
Galois-theoretic statement, not an analytic count."* The six points are
independently recorded and numeric — `bring-fibre-qhalf-figure.md` lists them
as `z ≈ (0.119, ±1.054)`, `(0.106, ±0.937)`, `(−0.975, ±0.223)`.

### Why this is not a fourth column in the same table

Candidates 1–3 answer *"which torus knots are admissible?"*. Candidate 4
answers *"how many orbits does the ambient geometry have?"*. So they are **two
independent countings of one physical quantity**, and the knot-index counting
gives 4 or 2 while the branch-point counting gives 3.

**That makes the open problem nameable, which "three filters disagree" did
not:**

> Construct the bijection between the branch-point pairs and the admissible
> `T(2,n)`, or prove it cannot exist.

Under candidate 1 it cannot (`4 ≠ 3`); under candidate 3 it cannot (`2 ≠ 3`).
So at least one of the two identifications is wrong, and establishing which is
the content. This is `qou-x4qm` item (i) — *"a physical bridge
'normal-form-independent winding ⇒ generation'"* — with both sides now
measured.

### Three further things the first append got wrong or missed

1. **Candidate 3's exclusion is by LAGRANGE, and is stronger than the corpus's
   own argument.** `|S₅| = 120 = 2³·3·5`, so `7 ∤ 120` and `9 ∤ 120` (only
   `3¹`): **no group of order 120** has an element of order 7 or 9. The
   `-proof.md` argues by inspecting the cycle-type order table `{1,2,3,4,5,6}`;
   Lagrange gives it in one line and cannot go stale. Prefer it.
2. **The physical consequence, which I did not state: candidate 3 excludes the
   TAU.** `prop:lepton-meson-torus-knot-dictionary` assigns `τ = T(2,7)` (with
   `𝔱`, `𝔟`). So reading candidate 3 as the criterion predicts **two**
   generations and drops the tau, the top and the bottom — a refutation of a
   headline claim, not a tidy-up.
3. **`torus-embeddable-completeness-remark.md` states the genus bound
   backwards:** *"The Descartes value `g = 4` is the smallest genus
   accommodating all three lepton generations…"* — a derived value (`Σ₄` IS
   genus 4, maximal `|Aut| = 120`) described as selected to fit the generation
   count. The fact is fine; the register reads as selection against the target
   under §NO FITTING. Recorded, not fixed.

### 🛑 Do NOT conflate the three "three"s

Three distinct triples appear and **I did not establish they are the same
triple**:

1. three complex-conjugate pairs of **branch points** (`bring-fibre-qhalf-figure`);
2. three generations ↔ branch-point pairs (`ex:archimedean-yekutieli`);
3. three copies of `S₃ ⊂ S₅` as *"the stabilisers of the three pairs of **color
   coordinates**"* (`descartes-braid-structure-proof.md:20`).

(3) is a different object, and that line does not say which three of the ten
2-subsets of five coordinates it means. Whether (1) and (3) index the same
triple is **unsettled by anything measured here.**

### Epistemic status of candidate 4

`ex:archimedean-yekutieli` is an `example` block (`interprets:
"thm:qu-to-qou"`), has **no Lean sibling**, and its `uses[]` are three
`remark`s — so under §3a it makes no logical claim. It is an **asserted
correspondence**, not a derivation. What makes it worth more than candidate 2
is that its mechanism is about the geometry generations are supposed to come
from, rather than about an unrelated divisibility property.

## Owner decision taken 2026-10-10: option 1, record as an open problem

The owner selected *"record the disagreement as an open problem; adopt no
filter"*. Enacted as
[`docs/audits/2026-10-10-generation-count-two-independent-countings.md`](../../docs/audits/2026-10-10-generation-count-two-independent-countings.md),
which carries all four candidates, the Lagrange sharpening, the tau
consequence, the register defect, the three-"three"s caution, and the bijection
statement. **No criterion is adopted, no block is edited, no number moves.**
The two remaining dispositions (candidate 3 ⇒ two generations; candidate 1 ⇒
four) stay open and are still the owner's.

## 2026-10-10 — owner decision

Owner decision 2a (ofri, 2026-10-10): adopt none of the four generation-count rules; the count stays an open problem, as already recorded in `docs/audits/2026-10-10-generation-count-two-independent-countings.md`. The task this bean names is still open: build a bijection between the branch-point pairs and the allowed $T(2,n)$, or prove there is none. Rule 13a: not closed.

## Progress Update (Round 54 — PR #8183)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity candidates across all 4 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/CoCasimirFigureEightAndGenerationCompleteness.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/co_casimir_figure_eight_and_generation_completeness_probe.py` and 2-commit stamped witness `computations/probes/co-casimir-figure-eight-and-generation-completeness.witness.json` (`scriptCommitSha: 0a9a3d4c2110ac1fe5749fd28e2cb610a48c9e50`, `HEAD: 531c8d4812e2909b18a4bc18eeba6be23a873d7f`).
- [x] Opened `litlfred/qou#8183` (status kept at `in-progress` per no-unilateral-closure policy).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8183, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
