---
# qou-prop3b
title: 'CORRECTED: 34 propagation violators, not ~150 — my screen inverted the answer; 9 platform scripts unrunnable'
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

---

## 🛑 CORRECTION 2026-08-29 — I ran the real audit, and it INVERTS this bean

I fixed `requirePaper()` locally and ran
`conjectural-propagation-audit.ts quantum-observable-universe`. The authoritative
result:

```
Class-axiomatised conjectures (§3b-cond eligible)          : 145
Violators (cone touches a NON-class-axiomatised conjecture):  34
Conditional-on-class (cone fully class-axiomatised)        : 121
```

**121 of 155 are FINE.** "Conditional-on-class" is a *recognised, non-violating*
status — AGENTS.md §3b-cond says the audit "reports such blocks separately as
conditional-on-class rather than as violations." The actionable population is
**34**, not ~150.

My screen said the opposite: 1 compliant in a sample of 15. **It was measuring
the wrong thing.** §3b-cond eligibility turns on whether the *upstream
conjectures in the cone are class-axiomatised* — an upstream property. I tested
two downstream markers (an instance binder in the block's own `.lean`, a banner
in its own `.md`) and read their absence as non-compliance. Those are
requirements 2 and 3 of five; the audit's classification is the cone condition.
Different question, inverted answer.

Two specific retractions:

- **"All five in the KL cone fail the screen" is wrong.**
  `prop:bloch-group-quotient-construction` is in the conditional-on-class list.
- **`prop:crystal-basis-resolves-mass-tower-open-problems` is NOT a propagation
  violator.** It does not appear among the 34; its cone conjecture
  `conj:kazhdan-lusztig-classical-limit` is class-axiomatised.

**What survives, and it is the part that matters for that block.** The
self-assuming projection is a defect *independent* of propagation:

```lean
class CrystalBasisCorrespondence where
  reduction_holds : Prop
  reduction_holds_proof : reduction_holds
theorem crystal_basis_reduction [ctx] : ctx.reduction_holds := ctx.reduction_holds_proof
```

That is §3b-cond **item 5** (non-degeneracy) and `proof-statement-integrity` —
the class carries the conclusion plus its proof and the theorem projects it;
`⟨True, trivial⟩` inhabits it. The propagation audit does not check item 5, so
being classified conditional-on-class does not clear it. Fix that block on its
own merits, not as part of a tranche.

**And the policy question I raised is smaller than I said.** 34 blocks, listed by
the audit with the offending conjecture named for each, is a reviewable tranche —
not a decision about a fifth of the paper.

## The platform defect is 9 scripts, not 2

Also undercounted. Bare `requirePaper()` — unrunnable wherever a folio holds more
than one paper:

```
audit-wiring.ts                     prune-transitive-deps.ts
conditional-class-banner-audit.ts   qa-agent-drain-queue.ts
conjectural-propagation-audit.ts    validate-references.ts
conjectural-propagation-sweep.ts    wall-violations-sweep.ts
generate-index.ts
```

Nine, and they include **both** §3b-cond enforcers (propagation *and* the
conditional-class banner audit), the bibliography cross-check, and the §7c wall
sweep. The idiom to fix them already exists in the same directory —
`find-dangling-remarks.ts` calls `requirePaper(process.argv[2])`.

Patched six locally to prove it; the propagation audit then ran and produced the
numbers above. Not pushed — a second repository, awaiting the owner.

**Do NOT fix these with `requirePaper(process.argv[2])`, even though that is the
idiom `find-dangling-remarks.ts` uses.** I did, and it broke two of them: in
`conjectural-propagation-audit.ts` and `conjectural-propagation-sweep.ts`,
`argv[2]` is *already* the output path —

```ts
const WITNESS_OUT = process.argv[2] ?? join(REPO_ROOT, "docs/audits/…witness.json");
```

— so naming the paper positionally also redirects the witness, and the audit
wrote a 70 KB JSON to a file called `quantum-observable-universe` at the repo
root. Caught by the stop hook, not by me. Five of the six collide: the other
three take `--strict` or slice positionals; only `generate-index.ts` is safe.

The working shape is **both** of:

1. `--paper <name>` as a **flag**, matching `extract-status-sections.ts`
   (`requirePaper(get("--paper"))`), never a positional.
2. In the two scripts that take an output path, read the **first non-flag**
   argument rather than `argv[2]` — with `--paper` alone, the witness lands in a
   file literally named `--paper`. The flag is necessary and not sufficient.

Verified end to end after both: `Witness:
docs/audits/2026-05-01-p3-1-conjectural-propagation.witness.json`, no stray
files, numbers stable.

**The regenerated witness was reverted, deliberately.** The run refreshed the
committed artifact by 814 insertions / 915 deletions — genuinely fresher than
the stale committed copy — but it was produced by a locally patched producer
that exists in no branch. Committing it would place a number in the corpus that
nobody could reproduce. Regenerate it *after* the platform fix lands, with the
landed version.

## Lesson, recorded because it is the fifth time this session

I substituted a hand-rolled proxy for an authoritative tool that was one
one-line fix away, and quoted the proxy. I had already written "sample before
quoting" into a detector docstring earlier in the same session. The rule needed
here is stronger: **when a corpus tool exists for the question, fix the tool
rather than approximate it** — the approximation was not merely imprecise, it
pointed the opposite way.
