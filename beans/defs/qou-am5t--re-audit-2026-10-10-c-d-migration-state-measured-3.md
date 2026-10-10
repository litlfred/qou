---
# qou-am5t
title: 'RE-AUDIT 2026-10-10: C->D migration state measured — 3 of 4 channels DONE, one science blocker, 57 todo beans against 6 live sites'
status: in-progress
type: epic
priority: normal
created_at: 2026-10-10T07:15:58Z
updated_at: 2026-10-10T07:28:16Z
---

## Measurement record — 2026-10-10, `main` 77695711d

Full write-up with the command behind every number:
[`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md).
This bean is the audit trail; that file is what readers should be sent to.

### Channels (registry `trace-convention-registry.json`)

| channel | def | prod | status |
|---|---|---|---|
| `mass` | D | D | agreed |
| `binding` | D | D | agreed |
| `borromean-binding-single-pipeline` | D | D | agreed |
| `qbeta-decay` | D | **C** | agreed-migration-pending (`qou-cds1`) |

### Code

| surface | measured | note |
|---|---|---|
| Python by VALUE, `computations` | 143 C, **143 adjudicated, BLOCKING 0**, 576 D | was BLOCKING 6; six adjudicated in `e6a5d23e9` |
| Python by VALUE, `tools` / `folio` / `scripts` | 0 C | these roots had never been scanned |
| Python by VALUE, `qou-mass` | 1 | generated mirror of an adjudicated `_HISTORICAL` fn |
| Python by SHAPE | 13 actionable | 12 probes + **1 producer** |
| Rust / `tools` | 0 live | only `archive/v2.rs`; **no audit scans `.rs`** |
| Lean | 23 C defs -> **0 actionable**, 23 deliberate; 57 D | quote `defs`, not the 243 sites |
| witnesses | 0 structural, 1 symbolic | `qou-eea0` says 84 |
| paper | 159 mentions / 89 files; 136 scoped, 23 residual | scoped, not corrected — correct disposition |

**The one site that matters:** `computations/qbeta/qbeta_ck_cache.py:140` — the
canonical `c_k` producer, the only non-probe production file on C, and the
`qbeta-decay` channel. Not drainable by `z`-substitution
(`decayLadder_zC_threeRow_ne_zero`, sorry-free), and **not** blocked on the
phase `α`: `cos <= 1` caps the N=2 factor at `1 - u^2 = 0.99992745` while the
ruled `z_D` base needs `F_required = 1.759`.

### Tracker — the actual mess

| | count |
|---|---:|
| beans naming a convention | 487 |
| of those open | 269 |
| `qou-cdx1` children, all `todo` | 57 |
| of those naming a still-actionable file | **1** (`qou-pmkh`) |
| naming no path (claim-level) | 15 |
| all named files clean (**reading queue, not a close list**) | 41 |
| lines in `qou-cds1` | 8593 |
| `convention-c-*` scripts | 16 |
| beans whose `updated_at` is the reorg date 2026-10-04 | **2592 of 5513 (47 %)** |

### Two corrections of my own, recorded because the wrong version is cheap to repeat

1. **The paper classifier reported 66 unscoped and was wrong about nearly all of
   them.** The flagged sites say *was* / *now* / *gives* / *withdrawn* /
   *retracted* inside two-column C-vs-D tables — correctly scoped, in vocabulary
   my regex lacked. Broadening it from what those sites actually say took
   **66 -> 23**. The 66 would have read as a large live defect.
2. **I called `qou-m7py` "measurably satisfied" off one grepped line and
   retracted it within the hour.** `gram.rs:138` says the `z^3` bug was fixed
   2026-08-15 — true, and one day after that bean's last update — but the bean
   exists to say *do not just fix the Rust bug*, and its Remaining items 3-4
   (rebuild `pyhecke_native`; regenerate 53 certificates, `[OWNER]`) are
   unverified. Evidence on `qou-m7py`; retraction on `qou-cdx1`.

### What I did NOT do, and why

- **Did not close any of the 41.** Most are about published figures, witnesses,
  detector blind spots, q-integer naming or laundering — all of which survive a
  clean code surface. Closing them because no `z_C` binding remains in the files
  they cite is *"shrinking the number without changing the corpus"*, which the
  registry's `blocked_on_rederivation_note` names as the thing it exists to
  prevent.
- **Did not retitle or restatus `qou-wgta`** (stale by ~30x) — retitling an
  append-only campaign ledger rewrites the record of what the campaign believed.
  Flagged on the bean; owner's call.
- **Did not refresh the registry's `updated: 2026-09-05`.** Its content is
  correct and only its date is behind; the status doc carries its own date in
  every table instead.
