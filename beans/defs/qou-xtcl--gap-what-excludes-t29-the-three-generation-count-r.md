---
# qou-xtcl
title: 'GAP: what excludes T(2,9)? The three-generation count reduces to this ONE lemma. Genus bound (PROVED) admits n in {3,5,7,9}; corpus assigns generations to {3,5,7}. The ''odd primes'' condition that would close it occurs ONCE in the corpus, asserted not derived. Candidate: for odd n>=3, n factors into smaller odd windings iff composite, so sigma^9=(sigma^3)^3 is a harmonic of gen 1 -- prove or refute that a composite odd winding cannot carry a generation.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-gen
    - 8f-open
created_at: 2026-08-01T22:05:54Z
updated_at: 2026-10-10T12:22:45Z
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
