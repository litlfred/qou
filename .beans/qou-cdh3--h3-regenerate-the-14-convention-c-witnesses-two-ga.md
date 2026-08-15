---
# qou-cdh3
title: 'H3 (hygiene): regenerate the 14 convention-C witnesses — two hard gates first'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-15T00:00:00Z
---

Parent: `qou-cdx1`. Successor to the `qou-eea0` cascade, which drained the bulk.

## Measured (`scripts/convention-c-witness-audit.py`, structural test, 2026-08-15)

**13 structural (825 dead-block entries) + 1 symbolic (14 expressions) = 14.**

```
computations/alpha/alpha-k-jones-markov-h12.witness.json              (70)
computations/chi-deuteron-h6-at-q0-50dps-matrix-m.witness.json         (7)  *rust
computations/chi-helium-3-h9-at-q0-50dps-matrix-m.witness.json        (25)  *rust
computations/chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json       (70)  *rust
computations/chi-helium-4-h12-numeric.witness.json                    (70)
computations/chi-lithium-5-h15-at-q0-50dps-matrix-m.witness.json     (168)  *rust
computations/chi-lithium-6-h18-at-q0-50dps-matrix-m.witness.json     (375)  *rust
computations/chi-neutron-h3-at-q0-50dps-matrix-m.witness.json          (1)  *rust
computations/chi-proton-h3-at-q0-50dps-matrix-m.witness.json           (1)  *rust
computations/chi-tritium-h9-at-q0-50dps-matrix-m.witness.json         (25)  *rust
computations/derived-chi-catalogue.witness.json                        (2)
computations/probe-1b-li6-orthogonality.witness.json                   (9)
computations/tr-m-q-hecke-seminormal.witness.json                      (2)
computations/y-lambda-macdonald-telescope.witness.json         (symbolic, 14)
```

## The two gates — do not start a cascade without clearing these

1. **The `chi-*-matrix-m` family has no Python producer.** `qou-eea0` resolved
   them to `producer: "rust-chi-q-via-gp-lossless"` — a `hecke-engine` binary.
   That is exactly the layer where `qou-j6il` found a binary **silently
   returning convention C while its source read D**. Apply the convention gate
   to the binary *before* regenerating, or the regeneration launders C.
2. **`delta_lambda_2row_stratum_analysis.py` has never completed.** It consumed
   the full 2400 s timeout on every attempt and is first in topo order, so every
   cascade restart pays 40 minutes before producer 2. Diagnose or re-order.

## Standing constraints (from `qou-eea0`, all learned the hard way)

- **Never two producers concurrently in one checkout.** The harness has a
  `SerialLock` (`O_EXCL` + liveness) and process-group cleanup because killing a
  harness once left its producer child running, reparented to init, and a
  second harness started the same script — three concurrent writers on one
  witness.
- **Never hand-edit a witness number.** Every value comes from a producer run.
- **JSONL incrementally after every producer.** The container has died mid-task
  at ~1h more than once.
- **"C fingerprint cleared" is the wrong headline metric.** A witness can be
  fully migrated and still legitimately contain the string — an audit *of* C, a
  stored non-recomputed value, a preserved historical field. Count deltas by
  kind; treat surviving fingerprints as a triage queue.
- **Separate structural zeros from genuine shifts from q₀-refresh noise.**
