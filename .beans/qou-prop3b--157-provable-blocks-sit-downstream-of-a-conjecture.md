---
# qou-prop3b
title: '157 provable blocks sit downstream of a conjecture, and the audit that checks this cannot run here'
status: todo
type: task
priority: high
created_at: 2026-08-29T19:05:00Z
updated_at: 2026-08-29T19:05:00Z
---

Reached from `qou-hprp`'s revised order, which put
`prop:crystal-basis-resolves-mass-tower-open-problems` first because its *kind*
over-claims. Fixing that one block turned out to be the wrong unit of work.

## The one block, first — it is a textbook §3b-cond item-5 defect

```lean
class CrystalBasisCorrespondence where
  reduction_holds : Prop
  reduction_holds_proof : reduction_holds

theorem crystal_basis_reduction [ctx : CrystalBasisCorrespondence] :
    ctx.reduction_holds := by
  exact ctx.reduction_holds_proof
```

The class carries the block's **own conclusion** as a field *plus a proof of it*,
and the "theorem" projects that proof. `⟨True, trivial⟩` inhabits it. AGENTS.md
§3b-cond item 5 names this exactly: *"A class that carries the block's own
conclusion as a field, with a 'theorem' that merely projects it, is a vacuous
self-assuming projection."*

The block is a **`proposition`** whose `uses[]` contains
`conj:kazhdan-lusztig-classical-limit`, with no conditional banner in the `.md`
and no instance hypothesis in the Lean — so it fails §3b-cond on requirements 1,
2, 3 and 5, and under §3b propagation a provable kind is not permitted there.

Its claim is not established either: the context remark describes the three
reductions in prose, and the third *"reduces to the Kazhdan-Lusztig
classical-limit functor"* — i.e. routes through the conjecture itself.

## Why I did not just demote it

Demoting cascades. `prop:type-b-folded-crystal-combinatorics` uses it, so it
would inherit the conjectural cone. Measuring that cone:

```
blocks transitively downstream of conj:kazhdan-lusztig-classical-limit : 20
  of which provable-kind                                               :  5
```

All five fail the §3b-cond screen (zero instance binders, zero banners; one has
no `.lean` sibling at all). But five is not the population:

```
CORPUS-WIDE provable blocks downstream of some conjecture : 157
  out of provable blocks total                            : 744   (21 %)
```

Demoting one block is an arbitrary dent in a population of 157, and it would
cascade into four siblings that are in exactly the same state. **This is a
tranche and a policy question, not a repair.**

## How many of the 157 are genuine violations — SCREENED, not adjudicated

Random sample of 15 (seed 3), checking the two *visible* §3b-cond markers: an
instance binder in the `.lean`, and conditional wording in the `.md`.

```
  3b-cond compliant   1/15     (prop:feynman-classical-limit)
  fails one or both  10/15
  no .lean sibling    4/15     (cannot satisfy requirement 2 at all)
```

**Read this as a screen, not a verdict.** The instance-binder test is deliberately
generous — any `[Capital…]` counts, including ordinary `[CommRing R]` — so most
of the ten fail on the **missing banner**, requirement 3, rather than on the Lean
structure. A careful adjudication could move blocks in either direction. What the
screen supports is that compliance is the exception; it does not support a
precise violation count, and no one should quote "147".

## The likely reason this accumulated

`folio-assistant/content/pipeline/conjectural-propagation-audit.ts` — the audit
that enforces exactly this rule — **cannot run in this folio.** It calls
`requirePaper()` with no argument, and with five papers present that throws:

```
error: 5 papers found (bach2013-double-slit, fred2005-formal-groups,
quantum-observable-universe, unital-groebner-bases, visualizer) — name one explicitly.
```

The same one-line defect as `qou-idxg`, in a second script. So **two** platform
audits are unrunnable here, and one of them is the propagation gate. That is the
cheapest thing on this bean by a wide margin: fix `requirePaper(Bun.argv[2])`
upstream and the authoritative list replaces my screen.

## Suggested order

1. **Fix the two platform scripts** (`qou-idxg` covers the index one). One line
   each, and it converts this bean from an estimate into a report.
2. **Decide the policy** on the 157: demote-to-conjecture, retrofit §3b-cond
   banners + binders, or accept a documented exception class. This is an owner
   call — it touches a fifth of the paper's provable blocks.
3. **Then** fix `crystal-basis-resolves-mass-tower-open-problems`, whose Lean is
   a self-assuming projection regardless of which policy wins — that part is a
   defect under any reading.
