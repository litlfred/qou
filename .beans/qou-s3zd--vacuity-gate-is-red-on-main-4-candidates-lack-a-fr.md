---
# qou-s3zd
title: 'Vacuity gate is RED on main: 4 candidates lack a fresh agent verdict'
status: completed
type: task
priority: high
created_at: 2026-08-30T10:04:11Z
updated_at: 2026-08-30T10:41:12Z
---

## Measured on main, 2026-08-30

    bun run content/pipeline/lean-vacuity-axiom-audit.ts \
      --check-ledger docs/audits/lean-vacuity-review-ledger.json
    -> EXIT 1

    ✗ agent-inspection gate: 4 candidate(s) lack a fresh agent verdict

| candidate | category | whose |
|---|---|---|
| `ConditionalClasses.lean:244` `QOU.AlgebraicSubstrate.BlowupYekutieli` | `proof-carrier-inhabited-by-probe` | **mine** (#6161 staled it) |
| `root-of-unity-truncation.lean:31` `RootOfUnityTruncationContext` | `proof-dependent-conjecture-not-conditional` | not mine |
| `magic-A-binding-formula.lean:107` `MagicABindingFormula` | same | not mine |
| `phi-q-aj-machinery-identification.lean:167` `QuantumAPolynomial` | same | not mine |

The last three are seeded `needs-agent` by a fresh `--review-ledger` — new
candidates from someone else's change, in files this session never touched.

## NOTE THE FLAG TAKES A PATH

`--check-ledger` requires its argument. Run bare, `checkLedger` is `undefined`,
the `if (reviewLedger || checkLedger)` block at line 2943 is skipped entirely,
and the process **exits 0 having never run the gate** — with no gate line in
the output at all. That is how `qou-jr5r` (scrapped) came to report a
non-existent detector gap. A passing run prints
`✓ agent-inspection gate: all N candidate(s) carry a fresh agent verdict`;
if that line is absent, the gate did not run.

## What each needs

- **BlowupYekutieli** — re-adjudication by me. The carrier is unchanged and
  still vacuous (`∃ r, 0 ≤ r ∧ r ≤ 1 + T`); only the file sha moved, via the
  `CriticalExponent` de-boxing in #6161. Its stored `agent_note` additionally
  repeats the *"its conjecture block does not exist"* claim that `qou-88nf`
  corrects — the block is live at `lifting-and-descent/`, labelled `prop:`
  rather than `conj:` — so the note needs rewriting, not just the sha.
- **The other three** — an agent has to read each declaration and its `.md` to
  decide whether the prose really claims a conditionality the signature does
  not carry. Not doable as a side effect of an unrelated branch.

## Ledger-shrink note for whoever does this

A `--review-ledger` run on the current tree takes the ledger 385 -> 383.
All 5 deletions are the legitimate "declaration is genuinely gone" case:
`QAubinLions`, `NSCounterexample` and `RegularityBreakdown` in
`ConditionalClasses.lean` are no longer vacuous after the `qou-rq9n`
re-encodings and so are no longer candidates, and two more
(`q_ns_wellposedness`, `traceInner_nonneg_of_posSemidef`) were fixed by
siblings. Verified by diffing the entry SETS, not by the count — per
`qou-rep6` / PR #6162, say so in the commit message when landing it.

## RESOLVED — all 4 adjudicated, gate green (PR #6177, merged)

    ✓ agent-inspection gate: all 174 candidate(s) carry a fresh agent verdict.
    EXIT 0

Verified on `main` itself after the merge, not only on the branch.

All three `proof-dependent-conjecture-not-conditional` hits share one shape —
the `.md` banner names an upstream `conj:` and the Lean binds a local context
class instead — so the shape separates nothing. What separates them is whether
the dependency is auditable ANYWHERE, measured by BFS over every `uses[]` edge
in `content/`:

| candidate | path to the named `conj:` | verdict |
|---|---|---|
| `phi-q-aj` `QuantumAPolynomial` | **direct `uses[]` edge** | legit |
| `root-of-unity-truncation` `RootOfUnityTruncationContext` | 2 hops via `prop:vorticity-lower-bound` | legit |
| `magic-A-binding-formula` `MagicABindingFormula` | **unreachable within 4 hops** | **genuine** |
| `ConditionalClasses` `BlowupYekutieli` | n/a — still vacuous | **genuine** |

**The acquittal worth recording.** `root-of-unity-truncation` may NOT list the
conjecture directly: `uses[]` carries immediate neighbours only and
`prune-transitive-deps.ts` enforces it, so adding `conj:q-aubin-lions` beside
`prop:vorticity-lower-bound` is exactly the transitive redundancy that tool
strips. §3b-cond item 4 and the immediate-neighbours rule genuinely conflict
there and the graph convention wins. Its Lean is honestly conditional in
substance too: the context class is content-bearing, has no instance, and the
result derives the conjunction rather than projecting its own conclusion.

**The true positive.** `magic-A-binding-formula`'s banner claims conditionality
on `conj:magic-numbers-bring`, and the claim exists in one prose sentence and
nowhere else — the Lean never mentions `MagicNumbersBring` (zero occurrences),
`uses[]` does not carry it, no path reaches it. Left `genuine` rather than
fixed: adding the edge or correcting the banner is a content decision, not gate
maintenance.

**`BlowupYekutieli`** re-adjudicated `genuine`, note corrected in place. The
carrier is unchanged and still vacuous; only the sha moved, via the
`CriticalExponent` de-boxing in #6161. Its previous note's *"its conjecture
block does not exist"* is retracted — true of the label, false of the corpus
(`qou-88nf`).

## Ledger accounting

385 -> 383. All 5 deletions are the sanctioned "declaration is genuinely gone"
case, verified by diffing entry SETS rather than counts: three are carriers
re-encoded under `qou-rq9n` (no longer vacuous, so no longer candidates), two
were fixed by siblings. `scripts/precommit-ledger-shrink-warn.sh --check` exits
1 on it as designed; stated in the merge commit per its instruction.

## Follow-ups left open

1. `magic-A-binding-formula` — add the `uses[]` edge or correct the banner.
   Needs an author's call on which is true.
2. Teach the criterion to check `uses[]` reachability before flagging a
   block-level prose claim. On this sweep that turns 3 hits into 1, and the 1
   is the true positive.
