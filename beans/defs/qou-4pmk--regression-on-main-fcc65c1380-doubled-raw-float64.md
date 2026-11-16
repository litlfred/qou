---
# qou-4pmk
title: 'REGRESSION on main: fcc65c1380 doubled raw float64 in he-nu-sdp-saturation-obstruction (5->11) and the ratchet cannot see it'
status: in-progress
pr: 8186
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T13:08:55Z
updated_at: 2026-10-04T15:15:50Z
parent: qou-9nnz
---

Found while auditing my OWN probe against the raw-float64 ratchet (bean
qou-cds1 / PR #6211). Not mine, and not this PR's to fix — filed so the
qou-tekx arc can drain it at the producer.

## The trace, exact

    ref                raw float64 fields in
                       computations/he-nu-sdp-saturation-obstruction.witness.json
    fcc65c1380^         5
    fcc65c1380         11      <- doubled here
    origin/main        11

`fcc65c1380` is "fix(qou-tekx): three probes computed at the retired muon pin
while stamping proton", 2026-08-30 11:43:36Z. The pin fix was right; it
regenerated this witness and the regenerated form carries 6 MORE raw float64
fields than the one it replaced.

## Why nothing caught it — the part that matters

main's COMMITTED `computations/witness-raw-float64-audit.witness.json` reads

    regressed = 0     total_fields = 34565

A fresh run on a clean checkout of main reads

    regressed = 1     total_fields = 34571

So the audit witness was not regenerated alongside the change, and **the
ratchet reads GREEN on main while the tree is RED**. This is the exact class
AGENTS.md already warns about ("main is currently carrying a STALE
witness-raw-float64-audit.witness.json") — here is a fresh instance with a
named cause and a 90-minute-old commit, rather than an aged one.

Note the same run also reports 157 files DRAINED (e.g.
chi-lambda-he4-full-partition-table 194 -> 1), so the stale committed audit is
hiding real progress as well as this regression. Regenerating it is not
cosmetic in either direction.

## What must NOT happen

Do NOT add the file to `raw-float64-baseline.json`, do NOT `--rebaseline`, and
do NOT hand-edit the count. AGENTS.md: baselines drain, never grow. The fix is
at the producer — carry the value as `mpmath.mpf` from source and serialize
with `_precision.fmt`.

## Why I did not fix it here

PR #6211 is a Lean file, a sympy probe and a bean; it touches nothing in this
witness's cone. Committing the regenerated audit witness there would bank
another arc's regression under my change and misattribute it. I discarded the
local regeneration rather than commit it.

## Next step for whoever takes it

1. Diff `fcc65c1380^..fcc65c1380` on the producer behind
   he-nu-sdp-saturation-obstruction and find which 6 values became bare floats.
2. Fix at the producer (mpf end to end, `_precision.fmt` on serialize).
3. Re-run the producer AND regenerate witness-raw-float64-audit.witness.json in
   the same commit, naming the count that moved — both the regression closing
   and the 157 drained files.


## Round 51 Progress
- [x] PR https://github.com/litlfred/qou/pull/8186 (`fb4f6926d3f96fd99209ef3cb58128ff0ce2701b`): serialized `q0` via `Q_50_DIGIT_STR` and LP support weights as strings in `computations/probes/he_nu_sdp_saturation_obstruction.py`, wrapped witness emission via `WitnessBuilder.wrap_legacy` with checkable assertions, and regenerated `he-nu-sdp-saturation-obstruction.witness.json` (0 raw float64).
