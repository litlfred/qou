---
# qou-16yn
title: 'MAIN IS BROKEN: 70ae502091 gutted the deuteron chi witness 2h ago -- consumer crashes, values match nothing'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T20:28:09Z
updated_at: 2026-10-04T15:21:23Z
parent: qou-5vkl
---


Found 2026-09-05 ~20:30 by rebasing `qou-49vn`'s work onto current `main` and
re-running its probe, which had passed 11/11 an hour earlier and now dies at
`KeyError: 'tr_M_at_q0'`.

## The breakage

`70ae502091` (2026-09-05 **18:09**, *"drain(qou-psjm): route 372 AME/CODATA
literals to the registry across 178 files"*, 290 files, 7537 deletions) replaced
`computations/chi-deuteron-h6-at-q0-50dps.witness.json` with a much thinner
object.

**Top-level keys lost (8):** `tr_M_at_q0`, `Z`, `N`, `convention`, `producer`,
`description`, `engineVersion`, `q_0_50dps`. Added: `_provenance`, `kind`,
`q_str`, `scriptFile`.

**Per-partition keys lost (4 of 6):** `dim`, `y_lambda`, `contribution`,
`compute_time_sec`. Each entry is now just `{partition, chi_lambda}`.

**The real consumer crashes on `main`:**

    $ python3 computations/option_e_multi_isotope_delta_lambda_probe_v3.py
    File ".../option_e_multi_isotope_delta_lambda_probe_v3.py", line 65, in parse_rows
        "dim": int(entry["dim"])
    KeyError: 'dim'

It would also have failed at line 129, `mpf(tr_M_data["tr_M_at_q0"])`.

**Its two siblings are intact.** `chi-tritium-h9-at-q0-50dps` and
`chi-helium-3-h9-at-q0-50dps` still carry `tr_M_at_q0`, `dim`, `y_lambda` and
`chi_lambda`. Only the deuteron was replaced — so this is not a deliberate
schema migration; it is one file.

## First in that file's history

Measured along HEAD's own ancestry, not a single-parent diff (`main` carries a
merge, and the naive `70ae502091^` diff disagrees with HEAD for the siblings):

| commit | date | `tr_M_at_q0` |
|---|---|---|
| `70ae502091` | 09-05 18:09 | **LOST** |
| `7e4d1aa6d0` | 08-10 18:22 | `0.5751722439177718708265…` |
| `98f4ea6595` | 08-10 15:36 | `0.3883571411977909894164…` |
| `efcaf79ed2` | 08-08 19:29 | `0.3883571411977909894164…` |
| `362beea471` | 08-08 14:59 | `0.3883571225623528401603…` |
| `4ba18f437c` | 08-08 14:04 | `0.3883571225623528401603…` |

The field had been present continuously since at least 2026-08-08.

## 🛑 The replacement values match NOTHING we can name

The new `chi_lambda` are **not** the previous committed values and **not** the
Rust kernel's. Measured across all 11 partitions:

    matches the Rust kernel               2 / 11
    matches the previous committed values 0 / 11

**I nearly reported this as "the commit swapped in the Rust values"**, on the
strength of λ=(6,) alone matching Rust to 29 digits. Checking all eleven refuted
it. A single-value match is not an identification — that is the fourth time in
this session the same shortcut nearly became a claim.

So the provenance of the numbers now on `main` for the deuteron χ is
**unestablished**, which is worse than either candidate.

## Two smaller casualties in the same commit

`deltalambda/s5so3-geometric-wlambda-a4-helium.witness.json` lost `q0Value`;
`probes/qbeta-sdeformed-leading-bound.witness.json` lost `q0AnchorReason`.

## What I did NOT do

**Nothing.** No revert, no regeneration, no witness restored. The deuteron χ is
the exact quantity `qou-49vn` is adjudicating (colour-weighted `0.1519683392…`
vs colour-blind `0.1519468395…` vs the superseded cache `0.5751722439…`), and
restoring any version of it picks a side in an open question. This bean reports;
it does not fix.

## Suggested handling

1. **Ask `qou-psjm`'s author what wrote that file.** The commit's subject is
   about routing AME/CODATA *literals* to a registry; gutting one χ witness's
   schema is not obviously in scope, so this looks like collateral rather than
   intent.
2. **Restore from `7e4d1aa6d0`** as the minimal un-break if the answer is
   "collateral" — it puts the consumer back on the value `main` carried for
   three weeks, and leaves `qou-49vn`'s question exactly as open as it was.
3. Do **not** regenerate it from a producer until `qou-49vn` settles which
   kernel is canonical.

- **Round 91 (`https://github.com/litlfred/qou/pull/8413`, head `1d95d75db1b41a96e3b4987d5771f9fd945187c9`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
