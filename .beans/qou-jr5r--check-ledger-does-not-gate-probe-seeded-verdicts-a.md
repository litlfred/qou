---
# qou-jr5r
title: 'check-ledger does not gate probe-seeded verdicts: a stale genuine verdict passes'
status: scrapped
type: task
priority: high
created_at: 2026-08-30T09:53:46Z
updated_at: 2026-08-30T10:03:27Z
---

## The gap

`proof-carrier-inhabited-by-probe` is the category I added in `qou-rq9n` for
carriers a source-reading scanner cannot decide, adjudicated only via the
vacuity review ledger. **Its candidates never reach `--check-ledger`'s check
path**, so an adjudicated verdict in that category can go stale and the gate
still exits 0. That is the one guarantee the ledger exists to provide:
"a verdict goes stale the moment the file changes -- the machine can flag, only
an agent can clear."

## Measured on `origin/main` and on a branch, 2026-08-30

Worked case, `QOU.AlgebraicSubstrate.BlowupYekutieli`:

| fact | value |
|---|---|
| in `docs/audits/vacuous-prop-carrier-baseline.json` | yes, `proved-vacuous` |
| its file exists, decl present | yes / yes (regex-verified) |
| ledger verdict | `genuine`, `file_sha: 3f4362244eaf` |
| live `sha256(file)[:12]` (= `hashFile`, line 2402) | `4d855ce423f8` |
| verdict fresh? | **NO** |
| `--check-ledger` exit | **0** |

And the carrier really is still vacuous -- `∃ r, 0 ≤ r ∧ r ≤ 1 + T`, satisfied
by `r = 0`. It is the exact case the category was created for.

Two independent confirmations that this is not branch-local:

- `proof-carrier-inhabited-by-probe` appears **0 times** in the audit's own
  output JSON, both freshly regenerated and as committed on `origin/main`,
  while the ledger carries **5** adjudicated entries in that category.
- The console summary's per-category breakdown (112 + 1 + 2 + 6 + 3 + 12 = 136)
  accounts for every reported defect and contains no row for it.

## Where it goes wrong (read, not yet fixed)

`content/pipeline/lean-vacuity-axiom-audit.ts:2985`

    candidates.push(...seedProbeInhabitedCandidates(shaCache));

feeds the ledger-seeding path -- which is why the 5 ledger entries exist at all
-- but those candidates do not appear in the reporting/checking path. So
`--review-ledger` can CREATE a verdict in this category and `--check-ledger`
will never ASK for it again.

## Caveat on my own measurement

I first asserted the staleness from a hash computed with an assumed algorithm.
That was not evidence. `hashFile` at line 2402 is
`createHash("sha256").update(readFileSync(p)).digest("hex").slice(0, 12)` --
the same function -- so the comparison above is now like-for-like and the
mismatch holds. Recorded because the first version of this finding was one
guessed hash away from being wrong.

## Relation to the sibling guard

NOT the same hazard as `qou-rep6` / PR #6162 (a rebase resolution deleting
adjudicated verdicts wholesale), and not the same as the `--review-ledger`
delete loop guarded by `lean-vacuity-ledger-foreign-entries.test.ts`. Those two
are about verdicts being DESTROYED. This is about a surviving verdict never
being RE-CHECKED. Three mechanisms, one ledger.

## Proposed fix, not attempted here

Route the probe-seeded candidates into the same freshness check as the scanner
candidates, then re-run `--check-ledger` and expect it to exit 1 on the current
tree with `BlowupYekutieli` named. A regression test should pin exactly that:
edit a file carrying a probe-seeded `genuine` verdict, assert the gate fails.
Deliberately not done on `claude/critical-exponent-deboxing-2026-08-30`, which
is a Lean content change and should stay reviewable on its own.

## 🛑 RETRACTED — the finding is FALSE. The gate works; I never ran it.

`--check-ledger` takes a **required path argument** (`--check-ledger F`,
line 2741: `else if (a === "--check-ledger") checkLedger = argv[++i];`). I ran
it bare. `checkLedger` was therefore `undefined`, the enclosing
`if (reviewLedger || checkLedger)` at line 2943 was false, the whole block was
skipped, and the process exited 0 having **never run the gate at all**.

Run correctly:

    bun run content/pipeline/lean-vacuity-axiom-audit.ts \
      --check-ledger docs/audits/lean-vacuity-review-ledger.json
    -> EXIT 1

    ✗ agent-inspection gate: 4 candidate(s) lack a fresh agent verdict:
      ...ConditionalClasses.lean:244 [proof-carrier-inhabited-by-probe/
         lean-inhabited-no-hypotheses] QOU.AlgebraicSubstrate.BlowupYekutieli

It names the exact declaration, in the exact category, on the exact staleness
I claimed it could not see. The gate does compare `e.file_sha !== c.file_sha`
(line 3097) and probe-seeded candidates DO reach it — they are pushed at 2985,
inside the block that runs for `--check-ledger` as well as `--review-ledger`.

**Both legs of the finding collapse to the same cause.** The
"`carrier-inhabited-by-probe` appears 0 times in the audit JSON, on my branch
and on origin/main" observation is not evidence of a blind detector: without
the flag the probe candidates are never seeded, so of course the category is
absent. The committed artifact was generated the same way.

## What this actually was

**I mistook "the gate did not run" for "the gate passed"** — the precise
failure mode the sibling documented as their E2BIG TRAP on PR #6162
(*"a guard that reports OK when it did not run is worse than no guard"*),
which I had quoted approvingly to them in the same comment where I reported
this non-existent gap. An empty result read as a clean one. The tool was
honest; it printed no gate line at all, and I did not notice the absence.

The one methodological point that survives: **check for the affirmative
signal, not the absence of a negative one.** A passing run prints
`✓ agent-inspection gate: all N candidate(s) carry a fresh agent verdict`.
I never saw that line and should have asked why.

## What IS true, and is not mine

Run correctly, the gate is **red on `main`** with 4 candidates:

- `ConditionalClasses.lean:244` `BlowupYekutieli` — **mine**, staled by the
  #6161 edit; needs re-adjudication, and its existing `agent_note` also
  repeats the "conjecture block does not exist" claim corrected in `qou-88nf`.
- `root-of-unity-truncation.lean:31` `RootOfUnityTruncationContext`
- `magic-A-binding-formula.lean:107` `MagicABindingFormula`
- `phi-q-aj-machinery-identification.lean:167` `QuantumAPolynomial`

The last three are `proof-dependent-conjecture-not-conditional`, in files I
have never touched, and are seeded as `needs-agent` by a fresh
`--review-ledger` — i.e. they are new candidates from someone else's change,
not from mine. Tracked separately as `qou-s3zd`; not adjudicated here, since
clearing them requires reading three unfamiliar blocks.

Also observed while measuring, minor: a `--review-ledger` run on the current
tree takes the ledger 385 -> 383. All 5 deletions are legitimate
("declaration is genuinely gone"): three are the `QAubinLions` /
`NSCounterexample` / `RegularityBreakdown` carriers I re-encoded, which are no
longer vacuous and so no longer candidates; two are declarations siblings have
since fixed. Verified by diffing the entry sets, not by the count. The reseed
was reverted rather than committed, because landing a partial adjudication
would be worse than the current red.
