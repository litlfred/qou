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

## Second half: ALSO not this branch's — main regenerates them on its own cadence

The sibling entry above is the record for the **ratchet** half; nothing below
re-credits it.

I picked this up intending to drain the **witness** half, did so, and then
**dropped it** — a sibling had already established the better convention, in
`ae0ef5dc1a` *("chore(diff hygiene): drop three audit witnesses this branch
never meant to touch")*:

> All three are self-describing audit outputs that measure the whole tree, so
> what they carried here were measurements taken mid-rebase against a tree in
> flux — **asserting them would have made this PR claim corpus counts it never
> verified.** … Reset to main's versions, which main regenerates on its own
> cadence.

That applies verbatim to what I had done. My drained copies asserted
`Q0_OK 1017→1027`, `total_scanned 2840→2842` and so on, measured against a base
that moved 23 commits before the branch was ready — and the commit **conflicted
on its first rebase for exactly that reason**, which is the symptom the sibling
names. `main` does refresh them itself (`115e860ea3`, *"chore(audits): refresh
three stale audit …"*).

So **both halves of this bean were resolved elsewhere**, and the correct action
for a feature branch is to touch neither. Closing it as such.

Re-measured on the way through, agreeing with the sibling's reading, and
recorded because the numbers are the evidence the ratchet really is drained:

| | filed | now |
|---|---:|---:|
| proven lossy (literal arg) | 1 | **0** |
| files affected | 12 | **11** |
| NEW files (not baselined) | 1 | **0** |

`scripts/precision-gates.sh` reports **"All blocking precision gates green"** —
so the *second* RED this bean named (audits-tree raw-float64) has cleared too,
which the sibling entry does not cover.

**Lesson worth keeping.** This bean was three hours old and *both* its findings
were obsolete: the ratchet fixed by one sibling, the witness question settled
by another's convention. Two agents also independently wrote the same ratchet
fix, one dropping theirs on discovering the other. Re-measuring — and reading
what siblings had already landed — is what kept this from being recorded as
three separate fixes and one unnecessary diff.
