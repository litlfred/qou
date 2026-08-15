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
  `prop:three-calibration-discipline` and `prf:atom-knot-mass-derivation` link
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
