---
# qou-c7g8
title: 'Batch residue: 6 producers failing for reasons other than the qou_substrate stamp import'
status: todo
type: bug
priority: normal
created_at: 2026-08-30T15:52:44Z
updated_at: 2026-08-30T15:52:44Z
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
