---
# qou-ylcp
title: 'y_lambda_two_row_cap_gate.py trips the import-time-dps ratchet on main (new_not_baselined 0 -> 1)'
status: completed
type: task
priority: medium
created_at: 2026-08-28T16:32:49Z
updated_at: 2026-08-28T00:00:00Z
---

`scripts/precision-gates.sh` is RED on `main` (measured 2026-08-28, not
introduced by any branch of mine -- confirmed by `git diff --name-only`).

```
computations/audits/y_lambda_two_row_cap_gate.py
  L47: CAP_RATIO_MAX = mp.mpf("1e-30")     <- module scope
  L134: mp.mp.dps = 60                     <- precision raised only later
```

Default mpmath dps is 15, so the threshold constant is built at 15 digits and
then compared against 60-dps quantities. Counted as
`literal_findings 0 -> 1` and `new_not_baselined 0 -> 1` by
`mpf_import_time_dps_audit`; `files_with_findings` 11 -> 12.

Landed 2026-08-27 in `25e8f8c1d9` ("gate(y_lambda): assert the convention-D
two-row cap at the TABLE, not per consumer").

**Fix** is the one the audit itself prescribes: an idempotent
`set_compute_dps()` at module scope ABOVE the constant. Do NOT baseline it --
`AGENTS.md` is explicit that baselines drain, never grow.

Not fixed here: different domain from the branch that found it
(`claude/lean-orphan-sibling-drain-2026-08-28`, Lean siblings).

## Also stale, same run

Four committed audit witnesses under-report because new files landed that they
had not scanned. Fresh values, so the next agent need not spend the 3-minute
gate run to learn them:

| witness | committed | fresh |
|---|---|---|
| `witness-provenance-audit` | scanned 2838 / ok 2401 | 2840 / 2403 |
| `mpf-import-time-dps-audit` | findings 11, literal 0 | 12, literal 1 |
| `q0-value-drift-audit` | proton-pin 1745 | 1749 |
| `witness-raw-float64--docs-audits-audit` | dirty 32 / fields 1178 | 33 / 1180 |

Regenerating them is clean and mechanical; it was deliberately not carried on
the Lean branch.

---

## FIXED on main 2026-08-28 — `ad65db8d49`, by a sibling

`fix(y_lambda gate): raise dps before the module-scope mpf, draining the
ratchet` (PR #5898) puts `set_compute_dps()` at module scope above
`CAP_RATIO_MAX`, using the file's existing `_precision` import.

Verified on main just now: `mpf_import_time_dps_audit` reports
`literal 0 / expr 20`, **NEW files (not baselined) 0**, **REGRESSED 0** — the
`new_not_baselined 0 -> 1` this bean names is back to 0. The gate itself still
PASSes on all four rows.

I independently wrote the same fix against `qou-stlw` and **dropped it during a
rebase** in favour of this one, which is cleaner (it reuses the existing import
rather than adding a second path to `qou_substrate`). Recorded so the two beans
are not read as two separate fixes: there is one, and it is `ad65db8d49`.
