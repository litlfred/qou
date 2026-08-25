---
# qou-nc5h
title: 'qbeta_ohtsuki_sixone_kappa_series.py: LOSSY module-const VOL_6_1 reds two precision gates on main'
status: todo
type: task
priority: normal
created_at: 2026-08-22T09:43:54Z
updated_at: 2026-08-22T09:44:20Z
---

## What

`computations/qbeta/qbeta_ohtsuki_sixone_kappa_series.py:166` builds

    VOL_6_1 = mpf('3.163963228883143983991757529167384812325703962')

at module scope with **`set_compute_dps()` never called at module scope**.
The 45-digit string is truncated to float64 at construction, so the
constant is already wrong when built — the audit classes it `LOSSY`, its
most severe class, and it is the only LOSSY finding in the corpus.

## Impact — two gates, red on main

Reds `scripts/precision-gates.sh` on two independent rows:

- `module-const precision` (`module_const_precision_audit.py --strict`) —
  LOSSY 1, across 5 files (11 further PADDING_RISK).
- `import-time dps ratchet` (`mpf_import_time_dps_audit.py --strict`) —
  this file is the single `new_not_baselined` entry:
  `files_with_findings 14 -> 15`, `literal_findings 0 -> 1`.

Because it is un-baselined and new, it fails the ratchet for **every**
branch that touches a `computations/` script, not just qbeta work.

## Not mine — red-on-arrival

Surfaced on `claude/a-operator-interface-convention-2026-08-21`
(PR #5427, bean `qou-zck8`), which touches only
`sublemma_2_1_A_operator_extract.py`. Skipped per the ratchet discipline
(a gate red on arrival is not the touching branch's to clear), and
different domain (qbeta vs A-operator), so not absorbed.

Two consequences of leaving it:

1. `computations/mpf-import-time-dps-audit.witness.json` is **stale on
   main** — its committed counts predate this file. I regenerated it,
   confirmed the delta was entirely this file, and reverted rather than
   commit a sibling's regression into an A-operator PR.
2. Same for `q0-value-drift-audit.witness.json`, whose committed counts
   also no longer match the tree (`STALE 310 -> 306`,
   `proton-pin 897 -> 1224`, `canonical 534 -> 213` — 327 witnesses moved
   category). That shift is unrelated to this bean and is worth its own
   look; noting it here only because the same regen surfaced it.

## Fix

Per the audit's own instruction: call the idempotent `set_compute_dps()`
at module scope, above the constant. Safe alongside the existing call in
`main()`. Then regenerate both audit witnesses and commit them with the
count change named. Do NOT baseline the file.
