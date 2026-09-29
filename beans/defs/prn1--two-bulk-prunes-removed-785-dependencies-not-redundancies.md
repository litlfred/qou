---
# prn1
title: 'two bulk prunes removed 785 dependencies, not redundancies'
status: in-progress
type: bug
priority: high
created_at: 2026-08-10T04:30:00Z
updated_at: 2026-08-10T04:30:00Z
---
Audit: `docs/audits/2026-08-10-transitive-prune-overreach.md`.

Two commits pruned `uses[]` edges in bulk on the rule *if A→B and B→C, drop
A→C*. That is a valid transitive reduction **only when B→C survives the same
pass**. Where both were dropped together, the dependency was removed rather
than deduplicated, and the reader loses the path entirely.

| commit | edges dropped | genuine reduction | reachability destroyed |
|---|---|---|---|
| `aa07f51383` "transitive-prune (1797 edges)" | 1796 | 1259 | **537** |
| `d2dcd93ebf` "prune 764 transitive deps" | 764 | 445 | **319** |

On `main` today: of those 856, 25 source blocks no longer exist and 46 became
reachable again by later edits. **785 remain unreachable, across 335 blocks, 80
of which declare nothing at all.**

Method: rebuild the `uses[]` graph in worktrees at each commit and its parent;
for every edge present before and absent after, ask whether the target is still
reachable from the source through the post-commit graph. Repeated against
current `main`.

## Why this matters beyond the count

**It explains the empty-`uses[]` population.** `fwr10` treated ~510 blocks
declaring no prerequisites as an editorial question. A large part of it is
prune damage.

**It invalidates sibling parity as evidence, and that is the methodological
finding.** Two independent readers in `fwr10` judged the five-member
surreal-bound family "deliberately empty" because *all* of them declare
nothing — a well-reasoned inference from uniformity. Every member lost 8-10
edges to the same commit:

| block | edges lost | still empty |
|---|---|---|
| `rem:bsd-surreal-bound` | 10 | yes |
| `rem:rh-surreal-bound` | 9 | yes |
| `rem:ns-surreal-bound` | 9 | yes |
| `conj:p-vs-np-qou` | 9 | yes |
| `rem:yang-mills-surreal-bound` | 8 | yes |
| `rem:p-vs-np-surreal-bound` | 8 | yes |

A bulk operation damages siblings **uniformly by construction**, so parity
cannot distinguish a shared convention from shared damage. Any reasoning of the
form "the whole family does this, so it is deliberate" is unsafe wherever a bulk
edit has touched the family. Check the history of the *family*, not just the
block.

## What this is not

**Not a licence to restore 785 edges in bulk.** That would repeat the original
error in the opposite direction — a mechanical rule applied across a corpus
without reading. Some of these edges may be genuinely unwanted for reasons the
prune never considered, and at least one deliberate removal is already known
(`def:adelic-substrate` lost `def:classical-limit-functor` by owner decision in
`78a570365d`, to break a mutual pair; restoring it re-opens a cycle).

The audit document lists every block and edge so restoration can be reviewed in
tranches, under the two-reader standard the `uses-editorial-review` skill now
carries.


## 2026-08-15 — re-driven against today's corpus: 785 → 692, and the parity family split

Audit: `docs/audits/2026-08-15-prune-damage-redrive.md`. Script:
`scripts/prune-damage-redrive.ts` (editorial edges only — the graph accessors
default to the union, which would count Lean paths no reader can follow).

The 2026-08-10 figures were the state of a corpus five days gone, and tranches
were going to be reviewed against them. Re-read now:

| | 2026-08-10 | today |
|---|---|---|
| still lost | 785 | **692** |
| across blocks | 335 | **320** |
| declaring nothing | 80 | **78** |

93 repaired: 39 edges re-declared, 27 reachable again by a new path, 27 targets
deleted. Nothing restored by this pass.

### It shrinks `fwr10` rather than confirming it

21 of those 39 re-declarations landed on the surreal-bound family — every one an
edge the prune removed. Three of `fwr10`'s four parity-compromised blocks have
since been re-populated (`yang-mills` 6, `rh` 4, `bsd` 3), so their
`correctly-empty` verdicts are moot rather than pending.

**And the asymmetry reversed.** `rem:ns-surreal-bound` declares nothing while
five siblings now declare 2–6 each. When the family was uniformly empty,
"deliberately empty" was a fair reading; with five restored and one at zero the
same argument now says the opposite. It is the strongest candidate in the file.
`rem:archimedean-stpart-strategy` — `fwr10`'s remaining fourth block, still
zero, 7 lost — is second.

### Tranche by TARGET, not by source

The audit lists damage per source, i.e. 320 questions. By target it collapses:
`thm:jones-markov-trace` lost by 21 sources, `def:hecke-normal-form` by 20,
`def:borromean-baryon` by 16, `def:crossing-energy` by 12. Foundational
definitions, which is exactly what a transitive prune eats — they sit at the
bottom of long chains, so every `A → B → foundational` triangle offered them up
and the pass dropped `B → foundational` in the same sweep.

Restoring one of those is **one** editorial question asked once and applied 21
times, not 21 judgements. That is the tranche structure this bean asked for, and
it is the recommended order.

`def:q-from-epsilon` is the sharp small case: lost by 10 sources including
**all seven** family members, and the five that were otherwise fully restored
did not get it back. One question, seven applications.

Still not a licence to restore in bulk, and the two-reader standard still
governs what is applied.


## 2026-08-15 — tranche 1 evidence assembled (not applied)

`docs/audits/2026-08-15-tranche-1-jones-markov-trace.md`, from
`scripts/prune-tranche-sheet.ts <target>`. Nothing restored.

`thm:jones-markov-trace` was stripped from 21 blocks in one pass, so this is one
editorial question with 21 applications. The sheet gives a reader, per source:
an explicit prose link to the target, a concept mention without a link, whether
the block's `.lean` touches the decl, and what the block declares today.

- **2 are near-certain restores on a structural ground rather than taste** —
  `def:three-calibration-discipline` and `prf:atom-knot-mass-derivation` link
  to the target from their prose while omitting it from `uses[]`. One block's
  two halves contradicting each other.
- **4 more mention the Markov trace without linking**; that is where judgement
  is actually needed.
- **16 of 21 declare at most one prerequisite** (6 declare nothing, 10 declare
  one). The prune's fingerprint, not a convention.
- **No formal corroboration exists.** Of the 18 with a `.lean`, none references
  `QOU.Braiding.JonesMarkovTrace`. Not an argument either way — the relations
  diverge legitimately and `uses[]` is never populated from Lean — but the case
  rests entirely on editorial reading, and nobody should read the formal graph
  as support.

The sheet had to be fixed before it was worth anything: a missing `.md` first
rendered as `—` in the same column as "searched, found nothing". That is the
absent-baseline-reads-as-agreement defect this whole arc is about, and I had
written it into the tool meant to detect it. It now reports `n/a` distinctly.
All 21 do have narratives, so the numbers were right; the sheet just could not
say so.

Two counts in the first draft of the write-up were wrong (nine/six for what is
six/ten). Corrected against the table before commit.


## 2026-08-15 — tranches 2-4 assembled, and the caveat that gates all of them

Index: `docs/audits/2026-08-15-tranche-index.md`. Sheets for
`def:hecke-normal-form` (20), `def:borromean-baryon` (16),
`def:crossing-energy` (12). Nothing applied.

Across the first four tranches: **69 sources, 6 with a prose link to the target
they omit from `uses[]`** — a block's two halves contradicting each other — and
about 22 more mentioning the concept without linking, which is where judgement
decides.

Not all tranches are equal, and size is the wrong order:

- `def:crossing-energy` is the **strongest** (3 of 12 link, 6 mention, and
  `rem:commutative-crossing-energy` links in prose *and* references the decl in
  Lean) despite being the smallest.
- `def:borromean-baryon` is the **weakest** — zero prose links, 10 of 16 with no
  `.lean`, a narrative cluster of remarks and an example. Almost no mechanical
  signal, so it should not be done early merely for being large.
- `def:hecke-normal-form`'s mention column needs care: bare "normal form" is
  generic and appears for unrelated reasons. Only the three exact
  "hecke normal form" matches are strong.

### Restoring an edge can CREATE a forward reference — this gates application

`uses[]` pointing at a later block in the same chapter is exactly what
`detangler-no-forward-ref` counts, and what the `fwr` arc spent five PRs cutting
from 274 to 194. Restoration adds `uses[]` entries, so some restorations push it
back up.

Concretely: `def:crossing-energy` was relocated into knots-particles-confinement
**§8** on 2026-08-09 *so that* the electroweak results would stop
forward-referencing their own definitions. `prop:hadron-exists`, one of the
blocks that lost the edge, sits in **§3** of that same chapter. Restoring it
would recreate precisely the forward reference that relocation removed.

So every tranche needs a third, mechanical question after the two editorial
ones: does restoring this point forward, and if so is that acceptable, does the
block need `foreshadows[]`, or does something need to move?

**It is not automated, and until it is, no tranche should be applied in bulk.**
Not because the editorial reading is unsound, but because a correct restoration
can silently undo a different piece of correct work.

The obstacle is small and belongs on the platform: the position map lives in
`loadChapterGraph`, private to `qa-checkers-extended.ts`, so a consumer asking
"where is this block?" has no accessor and would have to hand-roll a second
manifest parser — the exact duplication `fsl7` exists to prevent and
folio-assistant #116 just finished undoing. The fix is an exported accessor,
not a second parser here.


## 2026-08-15 — the forward-reference check is automated, and it reorders the queue

`pointsForward` is now exported from `qa-checkers-extended.ts`
(folio-assistant, alongside `blockPlacement`) and every tranche sheet costs each
proposed edge with it. Measured rather than assumed:

| tranche | sources | would point FORWARD |
|---|---|---|
| `thm:jones-markov-trace` | 21 | **0** |
| `def:hecke-normal-form` | 20 | **0** |
| `def:borromean-baryon` | 16 | **4** |
| `def:crossing-energy` | 12 | **1** |

**Tranches 1 and 2 are ordering-safe wholesale** — all 41 sources point
backward, so restoring any or all of them cannot regress the detangler metric.
They are also the two largest. The only question left for them is the editorial
one, which is the state a tranche is meant to reach.

Five blocks across tranches 3 and 4 need individual handling:
`rem:down-quark-properties`, `rem:up-quark-properties`,
`rem:binding-knots-visual-inventory`, `rem:knot-particle-dictionary`, and
`prop:hadron-exists`. Each needs `foreshadows[]`, a relocation, or a deliberate
decision to accept the forward edge. The other 23 sources in those tranches are
unaffected.

Recommended order is now **1, 2, 4, 3** rather than by size. Tranche 4 has the
strongest evidence despite being smallest; tranche 3 is the weakest (no prose
links at all, 10 of 16 without a `.lean`) and carries 4 of the 5 forward blocks,
so it should not be done early merely for being large.

The accessor was the right shape rather than a convenience: it returns
`undefined` when it cannot place a block, never `false`, so "I could not check"
cannot be read as "it is fine". That is the same lesson as `9giz` and `mcp1`,
applied before it could bite here.


## 2026-08-15 — twelve tranches, and the earlier restoration pass has a systematic gap

`docs/audits/2026-08-15-tranche-index.md` now covers the twelve largest targets:
**153 of the 692 still-lost edges, 22 with a prose link to the target the block
omits, 10 that would point forward if restored.** Totals re-derived from the
sheets rather than carried forward by hand. Nothing applied.

### Tranche 9 (`def:q-from-epsilon`) goes first, and it indicts the restoration

Highest prose-link rate of any tranche by a wide margin — **5 of 10**, against a
next-best of 3 of 12 — and **zero forward edges**, so it is ordering-safe
wholesale.

What makes it more than a good candidate is *which* five. Six blocks had edges
re-declared since the prune: yang-mills-surreal-bound (6),
p-vs-np-surreal-bound (6), rh-surreal-bound (4), millennium-unification (3),
bsd-surreal-bound (3), p-vs-np-qou (2).

**Five of those six are exactly the five whose prose links to
`def:q-from-epsilon`.** Someone worked through these blocks, restored 3-6
dependencies to each, and omitted in every case the one their own narrative
sends the reader to. That is not five independent judgements — it is one
systematic gap in the restoration pass, visible five times. The blocks that do
not link are precisely the ones that pass never reached.

### Nine of twelve tranches are ordering-safe wholesale

Tranches 1, 2, 5, 8, 9, 10 have zero forward edges; 4, 6, 7, 11 have one each.
**Only 10 blocks out of 153** need individual handling.

Recommended order is by evidence, not size: `q-from-epsilon`, `crossing-energy`,
`categorical-neutron`, `jones-markov-trace`, then 5/7/8/12/2. **Last:**
`borromean-baryon`, `habiro-ring`, `hadron` — no prose links at all between the
three of them, and `borromean-baryon` carries 4 of the 10 forward edges. Being
large is the worst reason to do one of those first.

## 2026-08-15 — tranche 9 APPLIED (the structural half): 5 edges restored

First edges restored under this bean. `rem:millennium-unification`,
`rem:bsd-surreal-bound`, `rem:rh-surreal-bound`, `rem:yang-mills-surreal-bound`
and `rem:p-vs-np-surreal-bound` now declare `def:q-from-epsilon`.

**Applied on a structural ground, not a reading.** Each of the five contains the
same sentence introducing two definitions together — `def:reeb-epsilon`, then
`$q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon))` — and
four of the five already declared the first while none declared the second. Same
sentence, same role, one dependency carried and the other not. That is a block's
two halves contradicting each other; nothing is being judged, so two readers are
not what was missing.

Verified before applying rather than after:

- `def:q-from-epsilon` uses only `def:reeb-epsilon` and cannot reach any of the
  five, so no cycle is created. Editorial graph still **acyclic corpus-wide**,
  preserving what #4881 established.
- **None of the five points forward** — the restored edges cannot regress
  `detangler-no-forward-ref`.
- `run-validate` ✓ Valid, **42 issues, unchanged**.

`rem:millennium-unification` declared *neither* definition while linking both.
Only `def:q-from-epsilon` was added; `def:reeb-epsilon` is a different tranche's
question and folding it in silently would be the bulk-edit error again. Recorded
here instead.

**What remains, and why it stops here.** The tranche went 10 → 5, and the
remaining five carry **no prose link at all**. The self-contradicting subset is
fully drained, so the residue is exactly where a reader's judgement decides
something — and there the two-reader standard has not been met and I cannot meet
it alone.

## 2026-08-15 — 13 more structural restorations, and the audit's own graph was blind

Applied 13 edges across tranches 1, 2, 4, 5, 7, 8, 11, 12 — every block whose
prose links a target its `uses[]` omitted, each cleared of forward-reference and
cycle refusals, each linking sentence read and confirmed a prerequisite use.
18 restored under this bean now. `run-validate` ✓ Valid, 42 issues, unchanged;
editorial graph still acyclic.

`scripts/prune-structural-candidates.ts` is committed: it finds these
corpus-wide, refuses the forward and cycle cases mechanically, and prints the
linking sentence so the one judgement left is made on one sentence.

### Three candidates withdrawn: the dependency was declared via `interprets`

`rem:commutative-crossing-energy`, `rem:body-asymptotics-catalog` and
`rem:archimedean-image-table` declare their target with `interprets:`, not
`uses[]`. `buildContentGraph` builds editorial edges from `uses[]` alone, so the
audit counted these as destroyed when they are stated.

**37 of the still-lost edges are in this position.** The damage figure answers
"unreachable through `uses[]`" — correct for the ordering metrics, which run on
that graph — but it is not "the author never declared this". Worth a platform
decision: the detangler already treats `interprets` as an ordering constraint
("no block may precede one it interprets"), so the graph and the checker
disagree about whether it is an editorial edge.

### A fourth candidate withdrawn, and it exposed a parser bug

`prop:strangelet-crossing-energy` carries an explicit author comment: the edge
to `def:crossing-energy` "is NOT listed: it is reached through
def:coulomb-charge". My candidate list contradicted that, which should not have
been possible — and the author was right.

`content-graph.extractUses` anchored on `/(?:^|[{,])\s*uses\s*:\s*\[/`, and
`\s*` does not span comments. That block has three comment lines between the
previous field's comma and its `uses:` key, so **its whole array was invisible**
and it appeared to declare nothing. Corpus-wide: **27 blocks, 53 declared edges**
that no ordering, cone or reachability metric could see. Fixed in
folio-assistant (#117); still-lost drops **679 → 666**.

**A correction to my own reporting.** I called `rem:archimedean-stpart-strategy`
the second-strongest candidate on the grounds that it declares nothing. It
declares `conj:classical-limit-stpart`; the graph could not see it. Any
"declares nothing" figure in the tranche sheets predating the fix is suspect and
the sheets need regenerating.

## 2026-08-15 — sheets regenerated on the fixed graph; the structural pass is finished

All twelve sheets and the index regenerated after folio-assistant #117. Earlier
revisions were wrong in the `declares now` column for any block with a comment
before its `uses:` key, and the index now says so at the top rather than quietly
superseding them.

Current state: **18 edges restored**, twelve tranches down to **131 remaining
sources**, **3 prose-linked** (all withheld — the `interprets` cases) and **10**
that would point forward.

Still-lost, measured now: **658** unreachable through `uses[]`, of which **37**
are declared via `interprets:`, so **621** are undeclared anywhere. The figure
falls faster than edges are applied, because one restoration can make several
pairs reachable transitively — the same effect the original prune tried to
exploit and got wrong by dropping both legs of the triangle.

**The structural pass is finished.** Every block whose prose linked a target its
`uses[]` omitted is resolved: 18 restored, 4 withdrawn on evidence. What remains
carries no textual signal at all. "The prune removed it" is a reason to ask
whether an edge belongs, not an answer — so the rest needs readers, and that is
a budget decision rather than a technical one.

## 2026-08-15 — regenerated on the union graph; the structural pass is CLOSED

All twelve sheets and the index rebuilt after `i8ad` made `interprets` an
editorial edge. That plus the `extractUses` fix (#117) shrinks the queue again,
both times by revealing declared dependencies the graph could not see:

| | at audit | after #117 | after `i8ad` |
|---|---|---|---|
| still lost | 785 | 658 | **581** |
| tranche sources | 153 | 131 | **107** |
| prose-linked left | 22 | 3 | **0** |

**`prune-structural-candidates.ts` now reports 0 candidates corpus-wide.** That
is the terminal state for everything decidable without reading.

The four withdrawals both vindicated themselves. Three declared their target via
`interprets`, and `i8ad` has made that visible — they resolve as declared rather
than lost, exactly as withholding them anticipated. The fourth,
`prop:strangelet-crossing-energy`, had an author comment saying the edge was
deliberately absent because it is reached through `def:coulomb-charge`; the
comment was right and my candidate was an artifact of the parser bug.

**Two lessons this bean should carry forward**, both instances of the same
thing: *before concluding a dependency is missing, make sure the tool can see
the ones that are there.* The audit's 785 was measured on a graph blind to 53
edges from a parser defect and 342 from a relation it did not model. A quarter
of the reported damage was never damage.

What remains — 107 sources — carries no textual signal, so it needs readers
under the two-reader standard. Ten of the 107 would point forward; four of those
are in `def:borromean-baryon`, which also has the least evidence, so it is the
worst place to start despite being the largest.

## 2026-08-15 — prepare-merge: figures re-verified on the merged corpus

`origin/main` merged in (3792 files moved since this branch's base), so every
number in these docs was re-measured rather than assumed. They hold:

- still lost **581**, across 279 blocks, 44 declaring nothing
- structural candidates **0**
- `content_validate` ✓ Valid, 42 issues, exit 0

**One figure did move, and it is not this branch's doing.** The editorial graph
now has **4 cycles**, not the 1 recorded when `i8ad` landed:

```
rem:frobenius-packing-density -> conj:mass-volume-factorization -> …
thm:ns-singularity-descartes  -> prop:ns-kummer-specialisation  -> …
rem:skein-filtration-trichotomy -> conj:q-collatz -> …
prop:ns-kummer-specialisation -> rem:skein-filtration-trichotomy -> conj:q-collatz -> …
```

None of the six blocks involved is touched by this branch. All four are
pre-existing content cycles that counting `interprets` makes visible; three
arrived with content merged from `main` after `i8ad` was measured. The
forward-reference gate reads **196**, up one from 195, from the same merged
content and likewise not from these edits.

Both are author questions, recorded here so the next reader does not have to
rediscover that "1 cycle" was a snapshot rather than a property.
