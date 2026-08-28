---
# qou-stlw
title: 'Two audit witnesses on main under-report their own live counts (stale-low ratchets)'
status: todo
type: bug
priority: normal
created_at: 2026-08-28T00:00:00Z
updated_at: 2026-08-28T00:00:00Z
---

Surfaced 2026-08-28 by `scripts/precision-gates.sh --changed`, which re-runs
producers to check drift and then reverts anything drift-only. The run was
killed by a 2-minute cap before the revert step, which is how two substantive
regenerations became visible instead of being tidied away.

## Measured

Both are **substantive**, not ephemeral — no `computedAt`/`environment` masking
explains them:

| witness | field | committed | live |
|---|---|---|---|
| `mpf-import-time-dps-audit` | `files_with_findings` | 11 | **12** |
| | `literal_findings` | 0 | **1** |
| `q0-value-drift-audit` | `proton-pin` | 1745 | **1749** |
| | a recorded `value` | 50 digits | **68 digits** |

Both move in the direction that matters: the committed artifact reports **fewer**
findings than the corpus currently has. A ratchet whose recorded count is
stale-low is slack the gate will not notice being taken up.

## Not caused by the branch that found it

Checked rather than assumed: stashed the only `computations/` edit in flight
(`binding_hbarq_rung_forward_test.py`), restored the witness, re-ran the
producer — the diff reproduces identically (3 insertions / 3 deletions). So this
is pre-existing on `main`.

The two stray regenerations were reverted rather than committed; they are not
this branch's to land.

## What is NOT established

- **Which** file is newly flagged. The witness records counts, not a path list
  under any `file`/`path` key the diff exposes, so the new `literal_findings: 1`
  is not identified here. Whoever picks this up should re-run the producer and
  read its stdout, which does name sites.
- Whether the `q0-value-drift` move (1745 → 1749, and a value string widening
  from 50 to 68 digits) is a real drift or a producer-precision change. The
  digit widening looks like the latter, which would make the count change a
  side effect rather than four new drifting sites. Do not quote "4 new sites"
  without checking that.

## Why it is worth a bean rather than an inline fix

Refreshing either witness is a one-command re-run, but committing a ratchet
artifact whose *cause* is unidentified is how a stale-low baseline gets blessed.
Identify the newly-flagged site first, then refresh — in that order.
