---
# qou-eea0
title: 'CAMPAIGN: regenerate all 84 convention-C witnesses under D and report total impact'
status: in-progress
type: task
created_at: 2026-08-10T01:15:27Z
updated_at: 2026-08-10T01:15:27Z
---


## Why this exists

The producer layer is fully convention D (`qou-9xla`, 178 actionable → 0), but
their committed outputs are not: **84 witness JSONs still carry convention-C
fingerprints**. Code and data disagree. Until this closes, the repo is in a state
where a reader cannot tell whether a given number is production or history.

Owner directive 2026-08-10: *"just do them all… I want to see total impact not
partial results"*, and *"work slowly diligently"*.

## Hard constraints

- **NEVER two producers concurrently in one checkout** (standing owner directive).
  The harness is strictly serial.
- **NEVER hand-edit a witness number.** Every value here comes from a producer run.
- The container is ephemeral and has already died mid-task twice in this arc, at
  ~1h each. The harness therefore writes **JSONL incrementally after every
  producer** and resumes by skipping what is already recorded. Losing an hour of
  runs to a restart is not acceptable when the fix is one append per producer.

## Method

For each producer, in order:

1. snapshot the witness (sha256 + extracted numeric fields)
2. run the producer with a per-producer timeout, capturing stdout/stderr
3. snapshot again
4. record: status, wall time, whether the C fingerprint cleared, per-field deltas
5. append one JSONL line — *then* move on

No commit until every producer has been attempted, so the impact is reported
whole rather than in fragments.

## What "total impact" means here

Not "84 files changed". The number that matters is how far each *physical*
quantity moves. The registry already records the expected order for migrated
channels — **195.8 ppm on β_Bor, −197 ppm on m_p** — so the report must give,
per witness, the largest relative change and what quantity it belongs to, and
must separate:

- **structural zeros** — `y_λ = 0` for `ℓ(λ) ≥ 3`. Not a "change", a collapse,
  and the thing convention D is *for*.
- **genuine shifts** — everything else, in ppm.
- **noise** — q₀-refresh at digit ~9 and timestamp churn, which must NOT be
  reported as convention impact. This bit me once already: a witness regenerated
  before its producer was migrated moved only at digit 9 and looked like a real
  result.

## Checklist

- [ ] harness written, resumable, serial
- [ ] dry-run on a known producer to confirm before/after capture works
- [ ] full run over all resolvable producers
- [ ] failures triaged: pre-existing breakage vs. breakage this migration caused
- [ ] 14 witnesses with no recorded `scriptFile` — find their producers or record why not
- [ ] impact report: per-quantity ppm, structural zeros separated from shifts
- [ ] commit witnesses + report together
