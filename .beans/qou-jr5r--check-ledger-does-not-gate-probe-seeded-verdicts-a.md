---
# qou-jr5r
title: 'check-ledger does not gate probe-seeded verdicts: a stale genuine verdict passes'
status: todo
type: task
priority: high
created_at: 2026-08-30T09:53:46Z
updated_at: 2026-08-30T09:54:26Z
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
