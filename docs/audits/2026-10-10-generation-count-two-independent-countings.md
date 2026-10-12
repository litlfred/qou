# The generation count: two independent countings, and they disagree

**Date:** 2026-10-10
**Beans:** `qou-xtcl` (the keystone), `qou-x4qm` (the parent gap), `qou-a5os` (completed, the mislabel finding)
**Status:** OPEN. This document records a measurement and states the open
problem. **It adopts no criterion** — doing so is an owner decision and is
deliberately not taken here.

## The decision this records, and why it is not taken here

The framework asserts **three** fermion generations. Measured on `main`
2026-10-10, the corpus contains **four** candidate bases for that number, and
they do not agree. Two of them are not even counting the same object. Adopting
one changes what the paper claims — in one case it retracts a headline claim —
so this document states the disagreement and stops.

## The four candidates

| # | criterion | what it counts | count |
|---|---|---|---:|
| 1 | Seifert genus `g(T_{m,n}) = (m−1)(n−1)/2 ≤ 4` | admissible `T(2,n)` indices | **4** — `{3,5,7,9}` |
| 2 | continuant divisibility `b_a ∣ b_n ⟺ a ∣ n`, singling out `9 = 3·3` | candidate 1, minus 9 | **3** — `{3,5,7}` |
| 3 | `S₅`-equivariant embedding | `T(2,n)` whose cyclic symmetry injects into `Aut(Σ₄)` | **2** — `{3,5}` |
| 4 | pairs of branch points of the Bring fibration | complex-conjugate pairs of the six branch points | **3** |

### The split that matters: these are two different questions

Candidates 1, 2 and 3 answer *"which torus knots are admissible?"*.
Candidate 4 answers *"how many orbits does the ambient geometry have?"*.
They are not competing readings of one criterion — they are **two independent
countings of the same physical quantity**, and the knot-index counting returns
**4 or 2** while the branch-point counting returns **3**.

That reframes `qou-x4qm`'s roast item (iv), which calls the defect *"two
filters, two counts"*. The sharper statement is: **the framework has a
geometric reason for three and an admissibility criterion that gives
something else.**

## Candidate 1 — the genus bound

`brings-surface/torus-embeddable-complete.md` states the generator set as an
*iff*: `T_{m,n}` with `gcd(m,n) = 1`, `1 < m < n` embeds in `Σ₄` exactly for
`{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)}` — six knots, plus the unknot, so
`|𝒢| = 7`. Its `-proof.md` enumerates: `m = 2 ⇒ n ≤ 9`, odd coprime
`n ∈ {3,5,7,9}`; `m = 3 ⇒ n ∈ {4,5}`; `m ≥ 4` empty.

**This is the derived one.** `QOU.Archimedean.torus_knot_genus_four_unique`
(`TorusKnotGenusFourUnique.lean`) is a real theorem — `interval_cases` over a
genuine finite split, using the structure's own `coprime`, `m_ge_two` and
`m_le_n` fields, sorry-free — and it establishes that the genus-4 pair is
exactly `{T(2,9), T(3,5)}`, with `genus_four_crossing_numbers` giving their
crossing numbers 9 and 10.

**`g = 4` is forced, not chosen.** `brings-surface-def.md`: `Σ₄` *"is a smooth
projective curve of genus 4. Its automorphism group is `Aut(Σ₄) ≅ S₅`. It has
order 120, the maximum possible for genus 4."* So the bound comes from the
ambient surface.

🛑 **But `torus-embeddable-completeness-remark.md` states it backwards:** *"The
Descartes value `g = 4` is the smallest genus accommodating all three lepton
generations plus the required `m = 3` generators for the quark sector."* That
sentence describes a derived value as though it had been selected to fit the
generation count. The underlying fact is fine; **the register is not**, and
under §NO FITTING it reads as selection against the target. Worth fixing on its
own account, independently of which candidate wins.

## Candidate 3 — and its exclusion is stronger than the corpus's own argument

`observations/s5-equivariant-torus-knots.md` states `s ∈ {3,5}`, and its
`-proof.md` argues: an equivariant embedding needs `ℤ_s ↪ Aut(Σ) = S₅`, hence
an element of order `s`; the element orders of `S₅` are `{1,2,3,4,5,6}`; odd
`s ≥ 3` leaves `{3,5}`. It states the comparison itself — *"Pure topological
(Seifert-genus) embedding into `Σ₄` admits four knots … The stronger
equivariant criterion retains only `T_{2,3}` and `T_{2,5}`."*

**Lagrange gives it in one line and is robust.** `|S₅| = 120 = 2³·3·5`, so

- `7 ∤ 120` — **no group of order 120** has an element of order 7;
- `9 ∤ 120` (120 carries only `3¹`) — likewise none of order 9.

So the exclusion of `T(2,7)` and `T(2,9)` does not depend on inspecting an
order table, and it is not an artifact of the cycle-type enumeration. Prefer
this argument; it cannot go stale.

🛑 **Its Lean proves none of this.** `s5-equivariant-torus-knots.lean` declares
`s5OddOrdersGe3 : Set ℕ := {3, 5}` and states
`(s ∈ s5OddOrdersGe3) ↔ (s = 3 ∨ s = 5)` — set-membership unfolding, `rfl` on
both branches, with **both hypotheses (`3 ≤ s`, `Odd s`) unused** and
`s5ElementOrders` defined and never referenced; the `S₅` order content sits in
a docstring, and `Mathlib.GroupTheory.Perm.Cycle.Type` is imported unused. Not
a new finding — `docs/audits/lean-triviality.json` records it as
`{"closed": true, "steps": 1, "tactic": "trivial"}`, checked 2026-08-07. **The
narrative proof is sound and complete; only the Lean is vacuous.** The block is
still a `proposition`, with `validation: "not_checked"`.

Incidentally, its manifest `lean.ref` and the file's own docstring header both
say `QOU.TorusKnot.s5_equivariant_classification` while the declaration is
`QOU.s5_equivariant_classification` — the file has `namespace QOU` and no
`TorusKnot`, and the library's only `TorusKnot` namespace is
`QOU.Archimedean.TorusKnot`, which has no such declaration. It resolves anyway
because §0a candidate 1 matches on **filename**, so a ref's declaration path is
never checked.

### The physical consequence, stated plainly

`prop:lepton-meson-torus-knot-dictionary` assigns `τ = T(2,7)` (3rd
generation, with the top and bottom quarks). So **candidate 3 excludes the tau
lepton**, and with it `𝔱` and `𝔟`. If `S₅`-equivariance is the criterion, the
framework predicts **two** generations and the three-generation claim is
refuted by its own geometry. That is the possibility `qou-x4qm`'s roast
forecasts as likeliest — *"a proof that the filters disagree is likelier than a
derivation of three"* — and nobody has written it down.

## Candidate 2 — and why its three is not evidence

`qou-a5os` (completed) already settled this: three is obtained by **removing
one element from a four-element set**, on a criterion (harmonicity via
continuant divisibility) *unrelated to generation counting*, so **any**
criterion eliminating exactly one of four would have produced three. Its
suggested retier — `open, with an adjacent proved divisibility lemma` rather
than `partially derived` — stands.

**The corpus had a second criterion doing the same job.**
`prop:lepton-meson-torus-knot-dictionary` read `for n = 3, 5, 7, … (odd
primes)` until 2026-10-10 (removed on owner instruction, Q1-D, PR #7553).
`9 = 3²` is the only non-prime in `{3,5,7,9}`, so **primality was excluding
exactly 9, in a parenthesis** — a second criterion, unrelated to the
divisibility one and equally unrelated to generation counting, trimming the
same single element. Two independent such criteria is the pattern `qou-a5os`
describes, not two independent confirmations.

## Candidate 4 — the one that counts something else

`ex:archimedean-yekutieli`: *"These correspond to the three pairs of branch
points under `S₃ ⊂ S₅`. … The three lepton generations then correspond to the
orbits of the cyclotomic Galois group on the six branch points. The fact that
there are exactly three generations is a Galois-theoretic statement, not an
analytic count."*

The six branch points are **concrete and independently recorded**:
`bring-fibre-qhalf-figure.md` lists them as three complex-conjugate pairs,
`z ≈ (0.119, ±1.054)`, `(0.106, ±0.937)`, `(−0.975, ±0.223)`.

**Epistemic status.** `ex:archimedean-yekutieli` is an `example` block
(`interprets: "thm:qu-to-qou"`), has **no Lean sibling**, and its `uses[]` are
three `remark`s. Under §3a an `example` makes no logical claim, so this is an
**asserted correspondence**, not a derivation. What makes it worth more than
candidate 2 is that its mechanism is *about* the geometry generations are
supposed to come from, rather than about an unrelated divisibility property.

🛑 **Do not conflate the three "three"s.** Three distinct triples appear and I
did not establish that they are the same triple:

1. three complex-conjugate pairs of branch points (`bring-fibre-qhalf-figure`);
2. three generations ↔ branch-point pairs (`ex:archimedean-yekutieli`);
3. three copies of `S₃ ⊂ S₅` as *"the stabilisers of the three pairs of **color
   coordinates**"* (`descartes-braid-structure-proof.md:20`) — **colour
   coordinates, not branch points**.

(3) is a different object from (1), and the line does not say which three of
the ten 2-subsets of five coordinates it means. Whether (1) and (3) index the
same triple is **not settled by anything read here.**

## The open problem, stated so it can be worked

Generations are identified **twice**: as admissible torus-knot indices, and as
branch-point pairs. The counts are `4` (or `2`) and `3`.

> **Construct the bijection between the branch-point pairs and the admissible
> `T(2,n)`, or prove it cannot exist.**

Under candidate 1 it cannot (`4 ≠ 3`); under candidate 3 it cannot (`2 ≠ 3`).
So at least one of the two identifications is wrong, and establishing *which*
is the content. This is `qou-x4qm` item (i) — *"a physical bridge
'normal-form-independent winding ⇒ generation'"* — restated with both sides
measured.

## What this document does not do

- It **adopts no criterion.** The three dispositions (candidate 3 ⇒ two
  generations and a retracted claim; candidate 1 ⇒ four and a fourth-generation
  prediction; or the bridge above) are on `qou-xtcl` and are an owner decision.
- It **changes no number and no block.** The register defect in
  `torus-embeddable-completeness-remark.md` and the vacuous Lean in
  `s5-equivariant-torus-knots.lean` are recorded, not fixed — both change what
  a block claims or how strongly.
- It **closes no bean.** `qou-xtcl` and `qou-x4qm` track open conjectures and
  stay open per AGENTS.md rule 13a.
