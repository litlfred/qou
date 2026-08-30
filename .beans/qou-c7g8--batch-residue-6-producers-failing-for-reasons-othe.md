---
# qou-c7g8
title: 'Batch residue: 6 producers failing for reasons other than the qou_substrate stamp import'
status: in-progress
type: bug
priority: normal
created_at: 2026-08-30T15:52:44Z
updated_at: 2026-08-30T18:35:00Z
---

Recorded so they are not lost. Measured in the `qou-j0nv` regeneration batch
(43 producers, serial, 600s cap). The 16 `qou_substrate` failures are
`qou-ya1e`; these are the rest, and they are **six distinct defects**, not one.

## The six

| producer | rc | time | symptom |
|---|---|---|---|
| `deltalambda/he4_binding_k_averaged_interface_probe.py` | 1 | 31s | non-zero exit, **no error text captured** by the batch's regex |
| `deltalambda/he4_binding_k_fingerprint_stage1_probe.py` | 124 | 600s | hit the cap — unknown whether slow or hung |
| `q0_migration_decompose.py` | 124 | 600s | hit the cap — same question |
| `probes/baldfn_theta_limit_probe.py` | 1 | 42s | `AssertionError: ('qt=2', 'reliable window too short', 0)` — a genuine assertion, not an environment fault |
| `qbeta/qbeta_counit_trace_transport_overshoot_probe.py` | 1 | 0s | `ModuleNotFoundError: codata_constants` — same SHAPE as qou-ya1e (missing path bridge) but a different module |
| `three_quark_borromean_lp_sweep.py` | 1 | 0s | `ModuleNotFoundError: matplotlib` — a genuinely absent third-party dependency, unrelated to the bridge |

## Notes

- The first one is a gap in my instrumentation, not necessarily in the producer:
  the batch captured `^[A-Za-z.]*(Error|Exception)` and this failure printed
  something that pattern missed. Re-run it alone and read the output.
- The two timeouts are NOT known to be hangs. `q0_migration_decompose` is a
  corpus-wide scan and may simply need more than 600s.
- `matplotlib` is a real dependency question: either install it, or the producer
  should degrade without plotting rather than fail to write its witness.

## Todo

- [ ] Re-run `he4_binding_k_averaged_interface_probe` alone and capture the real error.
- [ ] Time the two cap-hitters without a cap to separate "slow" from "hung".
- [ ] `baldfn_theta_limit_probe`: decide whether the assertion is a real
      regression or a threshold that no longer suits the data.
- [ ] `qbeta_counit_trace_transport_overshoot_probe`: fold into qou-ya1e's fix if
      that fix is "ensure the bridge is imported", since the cause is the same.
- [ ] `three_quark_borromean_lp_sweep`: install matplotlib or make it optional.

## 2026-08-30 — 2 of 6 closed, and neither was the defect it looked like

### 1. `he4_binding_k_averaged_interface_probe.py` — NOT A DEFECT

Ran it alone as the note suggested. It completes, writes its witness, and exits
**1** — because `allPassed: false`, not because anything threw. There was no
error text for the batch's `^[A-Za-z.]*(Error|Exception)` regex to capture
because there was never an exception. The failing assertion is honest science:

    label   "averaged interface improves on plain best (3.8% < 14.7%)"
    passed  false        rel Δ = 0.227913  vs plain best 0.147

**The instrumentation gap is real though**: a batch that classifies producers by
regex over stderr cannot distinguish "crashed" from "ran and reported a red
assertion". Those need different responses. Classify on exit code + presence of
a witness, not on stderr shape.

Re-running it was a strict gain: the committed witness (2026-08-23) carried NO
provenance at all, and the run added `scriptFile`, `scriptHash`,
`scriptCommitSha`, `commitSha`, `durationMs`, `q0Anchor: proton` and `q0Value`.
No science value moved (verified field-by-field).

Two loose ends, NOT fixed here (they are science/schema, not batch defects):
- the assertion uses `label`, with no `computed`/`expected` — a schema deviation
  from every other witness's `name`/`computed`/`expected`/`passed`;
- the verdict prose says "3.8%" and "96.2% captured" while the computed rel Δ is
  22.79% and the assertion compares 0.2279 against 0.147. Those disagree.

### 2. `qbeta_counit_trace_transport_overshoot_probe.py` — FIXED, exit 0

Not the same shape as qou-ya1e. The real cause was two lines hardcoding an
absolute path into a **different machine's checkout**:

    sys.path.insert(0, "/home/user/qou/computations")
    sys.path.insert(0, "/home/user/qou/computations/substrate")

This repo is at `/workspace/qou`, so both inserts resolved to nothing. Replaced
with `__file__`-relative paths. Now exits 0; witness diff is ephemeral only.

### The class behind it — 27 hardcoded `/home/user/qou` paths

Fixed 7 in 4 files (6 `sys.path.insert` + 1 Lean output path in
`gen_l6a4_angle_structure_lean.py`, which was writing to an unreachable
directory and dying with FileNotFoundError before emitting its file).

⚠️ My first count of "6 live" was WRONG — it filtered on `sys.path.insert`
alone and missed `sys.path[:0] = [...]`, `for _p in ("...",)` loops, and
`Path("/home/user/qou")` roots. **20 live occurrences across 12 files remain**,
beaned separately as a portability defect rather than refactored mid-bean.

### Still open here

- `he4_binding_k_fingerprint_stage1_probe.py` — 600s cap, slow-vs-hung unknown
- `q0_migration_decompose.py` — 600s cap, same question
- `baldfn_theta_limit_probe.py` — AssertionError ('qt=2', 'reliable window too
  short', 0), a genuine assertion
- `three_quark_borromean_lp_sweep.py` — matplotlib absent
