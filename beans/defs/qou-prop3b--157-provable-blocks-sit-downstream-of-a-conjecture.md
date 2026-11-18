---
# qou-prop3b
title: 'CORRECTED: 34 propagation violators, not ~150 — my screen inverted the answer; 9 platform scripts unrunnable'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T19:05:00Z
updated_at: 2026-10-04T15:10:52Z
parent: qou-5vkl
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


--------

## 2026-09-02 — re-measured. The count is right; the ARC is 4 conjectures, not 34 blocks.

### The headline holds

Re-ran `conjectural-propagation-audit.ts` on current `main`: **34 violators**,
164 provable blocks touching a conjecture, 130 correctly `conditional_on_class`.
This bean's count is accurate and current.

**Its worked example is done, though.** `prop:crystal-basis-resolves-mass-tower-
open-problems` was repaired on 2026-08-31 (bean `qou-z9ws`) — the
`reduction_holds : Prop` + `reduction_holds_proof` shape became a parameterised
`ReducesTo` encoding. Verified: it is **absent** from the violator list, so that
fix cleared both the vacuity and propagation axes.

### 5 of the 34 are DETECTOR FALSE POSITIVES — a namespace is not a directory

A violator is *"a block whose cone touches a **non-class-axiomatised**
conjecture"* (audit line 205). `isClassAxiomatised` resolves a conjecture's
`lean.ref` by mapping the **declaration path to a file path** —
`QOU.A.B.C` → `lean/QOU/A/B/C.lean`.

That assumption is false in this corpus, because a Lean **namespace** need not
mirror a directory. Three conjectures have a class that genuinely exists at a
non-derived path:

| conjecture | `lean.ref` decl | class actually in |
|---|---|---|
| `conj:tower-geometric-lower-bound` | `QOU.Mass.LevelSelection.TowerGeometricLowerBound` | `QOU/Mass/**LevelSelectionLogarithmic**.lean:48` |
| `conj:gs-graded-markov-trace-existence` | `QOU.IwahoriHecke.MarkovTrace.GradedMarkovTraceExistence` | `QOU/IwahoriHecke/**MarkovTrace**.lean` |
| `conj:kashaev-surreal` | `QOU.AppendixSurreals.KashaevSurreal` | `QOU/AppendixSurreals/**Conjectures**.lean` |

Worked case: `prop:level-selection-not-linear` satisfies **all five** §3b-cond
conditions — class-axiomatised conjecture, `[TowerGeometricLowerBound w r c]` as
an explicit Lean hypothesis, the conditional banner literally opening its `.md`,
`uses[]` naming the conjecture, and a genuine derivation via Mathlib's
`isLittleO_coe_const_pow_of_one_lt` rather than a projection. It is not a
violator; the detector cannot see its class.

**Corrected: 34 reported → 29 true.**

**Fix location** (folio-assistant, not qou):
`content/pipeline/conjectural-propagation-audit.ts::isClassAxiomatised` —
fall back to a tree-wide `class <Decl>` search when the derived path is absent.

### The 29 trace to FOUR conjectures

| conjecture | violating blocks |
|---|---|
| `conj:magic-numbers-from-q` | **17** |
| `conj:b1-hyperbolic-rows-theorem` | 6 |
| `conj:shell-transition-knot` | 4 |
| `conj:im-q-physical-role` | 1 |

So this is **not 34 per-block judgements**. Class-axiomatise four conjectures
and the whole arc closes; do the first and 17 of 29 go.

### Why the 17 exist, and why they are NOT a cheap fix

`conj:magic-numbers-from-q` became a conjecture in `dfb14e3efe` (*"demote
magic-numbers-from-q to conjecture: the signal is a parity test at K=10"*). That
demotion was correct, and **its propagation was never followed up** — 17
downstream provable blocks have violated §3b ever since.

But class-axiomatising it is **not mechanical**, and this is the part that needs
the author. Its Lean (`QOU/AtomicMass/MagicNumbersFromQ.lean`, 301 lines) is a
**fully proved, sorry-free theorem**:

    theorem magic_numbers_from_q :
        ∀ Z, Z ∈ [8, 20, 28] → delta2_Phi 10 Z q_zero > 0

proved by `norm_num` from a tabulation, with `magic_numbers_from_q_holds_at_
every_q` besides. **The arithmetic is not open.** What is conjectural is the
*physical* reading — that this `K = 10` second-difference signal identifies
nuclear magic numbers rather than being a truncation artifact.

So a class carrier has to encode **that** claim, and writing it means deciding
what the conjecture asserts beyond the proved arithmetic. That is a physics
judgement, not a refactor, and I am not inventing it.

**Recommendation, marked as judgement:** fix the detector first (cheap, clears 5
and prevents the next agent re-deriving this), then take
`conj:magic-numbers-from-q` — with the author naming what the open content is —
since it alone is 17 of the remaining 29.


---

## 2026-09-03 — measured, fixed the detector, and stopped short of the laundering

**Detector fix landed (folio-assistant#162).** `isClassAxiomatised` resolved a
conjecture's Lean as `<lakeRoot>/<Decl/Path>.lean`, appending the *declaration
name* as a path segment. A `lean.ref` is a namespace-plus-declaration path, not
a file path, so that only resolves when the file is named after its
declaration. Route (2) resolved to a **non-existent file for all seven**
blocking conjectures, and three already carried the exact `class` the audit
said was missing:

| conjecture | class actually at |
|---|---|
| `gs-graded-markov-trace-existence` | `QOU/IwahoriHecke/MarkovTrace.lean:93` |
| `kashaev-surreal` | `QOU/AppendixSurreals/Conjectures.lean:463` |
| `tower-geometric-lower-bound` | `QOU/Mass/LevelSelectionLogarithmic.lean:48` |

Added route (c), the grep fallback of AGENTS.md §0a's resolution order.
Violators **34 → 29**; class-axiomatised conjectures **147 → 165**.

**Correcting my own earlier entry here.** I wrote "34 → 29, five detector false
positives" and gave the mechanism as *"a Lean namespace is not a directory"*.
The count was right, the mechanism was not sharp enough, and it applies to
**all seven** blockers rather than five. The five is the number of *blocks*
that clear — much smaller than the 22 conjecture-instances involved, because
most affected blocks are independently blocked by a genuinely un-axiomatised
conjecture in the same cone. **A second self-correction:** a hand-rolled regex
graph I built mid-investigation reported `NO PATH` from all 17 blocks to the
conjecture. That was the parser, not the graph — under the audit's own
`loadBlocksUnder` every path resolves. Second false negative from a hand-rolled
parser this session.

**The remaining 29, by blocker:** `magic-numbers-from-q` 17,
`b1-hyperbolic-rows-theorem` 7, `shell-transition-knot` 4,
`im-q-physical-role` 1.

**All 17 funnel through ONE edge.** `conj:diagrammatic-double-magic-lr-fusion`
is the only block in the corpus listing `conj:magic-numbers-from-q` in
`uses[]`. Every one of the 17 paths ends
`… → conj:diagrammatic-double-magic-lr-fusion → conj:magic-numbers-from-q`.

**Why I did NOT write the class carrier.** `conj:magic-numbers-from-q`'s title
asserted what its own scope refutes — the sign of δ²Φ is a parity test
satisfied by every even Z; the local maxima over even Z at K=10 are {4,12,16},
none magic, with Z=8 sixth of fourteen; and Z=20 is a local maximum at no q in
(1, φ). The block's own conclusion is *"what survives is the construction and
its q-dependence, not the identification"*. A class carrier would have to
encode the identification the block measured and refuted, and would then
discharge 17 provable blocks against it — 29 → 12 while the corpus got less
honest. Note the audit checks only **half** of §3b-cond (the class, not the
downstream `[Instance]` hypothesis), so satisfying the visible half is exactly
audit-dodging.

**Done instead:** retitled to the block's own opening sentence, with an
`authorNotes` caveat recording the determination.

**Two dispositions would genuinely clear the 17, both content decisions:**
(a) state the surviving conjecture precisely enough to axiomatise — the block
says *"whether some other functional of the same Hoefsmit data carries shell
structure is open"*, and an existential over unspecified functionals is not a
class field; (b) retarget the choke-point edge — the LR-fusion conjecture is
stated for Z, N ∈ 𝔐, the *empirical* magic set, and gets its single-self-
conjugate-partition support from `prop:categorical-neutrality-saturated-shells`,
so it may not need the q-derivation of 𝔐 at all. If it does not, all 17 clear
at once.

Audit doc: `docs/audits/2026-09-03-propagation-audit-detector-blindness-and-the-magic-number-chokepoint.md`


### 2026-09-03 (cont.) — 29 → 25, by fixing a `lean.ref` that named a namespace which does not exist

`conj:shell-transition-knot` declared `lean.ref = "qou:QOU.Braiding.stability_pairs_correct"`.
**There is no `QOU.Braiding` namespace anywhere in its sibling** — the file declares
no `namespace` at all, so `stability_pairs_correct` and fifteen companions sit in
the **root** namespace. Meanwhile the real axiomatisation was already in the
library: `class BorromeanQuark` and `class ShellTransitionKnot [BorromeanQuark]`
in `lean/QOU/Conjectures/ShellTransitionKnot.lean`, dependency threaded through
the type, **no instance**.

Repointed. Violators **29 → 25**, conditional-on-class 135 → 138. The four that
clear are `prop:hook-weight-derivation`, `prop:mass-formula-regime-switching`,
`thm:frobenius-codim-universal`, `thm:knot-mass-formula-unified` — and they clear
*honestly*: the class exists, its fields carry content, no instance is supplied,
so the conjecture stays open and the four are correctly conditional.

**Accounting, since the axiomatised count did not move (165 → 165).** In the same
window a sibling agent promoted `conj:tower-geometric-lower-bound` to a
**proposition** (`53945eef2c`), removing it from the conjecture population and
taking its one violator with it. So this repoint accounts for **4** of the
29 → 25; do not read the whole delta as mine.

**Remaining blockers: `conj:magic-numbers-from-q` 17, `conj:b1-hyperbolic-rows-theorem` 7,
`conj:im-q-physical-role` 1.** `shell-transition-knot` is off the list.

**Found on the way, NOT fixed — the sibling is the anti-pattern its own library
file forbids.** The library file's closing comment refuses to supply a mock
instance because *"a `mockCorrectedClosure` that hardcodes
`{2,8,20,28,50,82,126}` and discharges `closures_match` by `decide` is FITTING the
answer into a lookup table"*. The sibling does exactly that:

```lean
def stabilityPair : ℕ → ℕ
  | 0 => 2 | 1 => 8 | 2 => 20 | 3 => 28 | 4 => 50 | 5 => 82 | 6 => 126 | _ => 0
theorem stability_pairs_correct : [stabilityPair 0, …, 6] = [2,8,20,28,50,82,126] := by decide
```

`rfl` in disguise. Only the first four values link to anything; **50, 82 and 126 —
the three that would actually test the mechanism — connect to nothing.** And the
file does not establish its own headline: its header asserts *"the 3 crossings of
B_3 set the threshold at N ≥ 3"*, while its only theorem on the criterion,
`so_exceeds_spacing`, gives **N ≥ 1** and its docstring concedes *"(but empirical
threshold is N ≥ 3 due to gap structure)"* — formalised nowhere. The `3` is a
`def`, not a derivation.

Disposition left to the owner: AGENTS.md §0a "no shadowing stubs" indicates
preserving the genuinely-new parts (`ho_spacing`, `so_exceeds_spacing`,
`shellTransition_threshold`) into the library file and deleting the sibling, as
`qou-scrx` did for `scratch_skein.lean`. Not taken unilaterally — it removes a
`theorem` a reader may be citing and changes what the block renders from. The ref
repoint stands independently of it.

Audit: `docs/audits/2026-09-03-shell-transition-knot-ref-repoint-and-the-sibling-lookup-table.md`


### 2026-09-03 — 🛑 the 2026-08-08 inconsistency repair fixed the LIBRARY copy and left the sibling

`lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean` carries a history
section recording that until 2026-08-08 its statement was

```lean
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : Nat) (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified
```

— every binder universally quantified, **the count included**, so it asserts
`3 ≤ n` for *every* `n` given *any* two `Prop`s, and instantiating at `n = 0`
with both `True` proves `False`. Bean `qou-t7zg` repaired it.

**The sibling `appendix-surreals/b1-hyperbolic-rows-theorem.lean` still had it,
verbatim, as of today.** Reproduced rather than inferred:

```
theorem sibling_axiom_is_inconsistent : False := by
  have h : (3 : Nat) ≤ 0 := b1_hyperbolic_rows 0 True True trivial trivial
  omega

lean exit 0
'sibling_axiom_is_inconsistent' depends on axioms:
  [propext, Quot.sound, QOU.AppendixSurreals.B1HyperbolicRowsTheorem.b1_hyperbolic_rows]
```

Its own header said *"This file is documentation only"* — an `axiom` in a
`.lean` file is not documentation, whatever the header says. And this sibling is
what the block's `lean.ref` resolves to **first** (§0a candidate 1), so a reader
following the reference reached the unsound copy, not the repaired one.

**Fixed:** the sibling now declares nothing, so route (1) finds nothing and the
reference falls through to the repaired library version. `lean` exit 0 on the
emptied file. **The propagation audit is unchanged at 25 with the same three
blockers — this is a soundness fix, not a violator fix**, and I checked rather
than claiming otherwise.

**Generalisation worth a sweep:** a repair applied to one of a library/sibling
pair leaves the other live, and the sibling is the one `lean.ref` reaches first.
Nothing in the corpus checks that the two agree.

### And why `conj:b1-hyperbolic-rows-theorem`'s 7 violators should NOT be cleared yet

The obvious move is converting the library's `axiom b1_holds_at_row` into a
`class`, which is what §3b prescribes for a conjecture and is strictly weaker
than a global axiom (a class with no instance forces every consumer to carry the
binder; an axiom is usable silently). That would clear all 7.

**Do not do it alone.** The propagation audit checks only the *class* half of
§3b-cond, not the downstream `[Instance]` binder. Converting the axiom while the
7 downstream blocks still lack their binders would clear 7 violators in the
audit while nothing downstream actually became conditional — the same
satisfying-the-visible-half move this bean refused for `conj:magic-numbers-from-q`.
The conversion is right **only** as a package with the 7 downstream signatures,
which is real work across 7 blocks and should be claimed as such.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-03 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
