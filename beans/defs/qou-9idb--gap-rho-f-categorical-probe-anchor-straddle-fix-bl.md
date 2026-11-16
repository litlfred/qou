---
# qou-9idb
title: 'GAP: rho_f_categorical_probe -- anchor straddle fix BLOCKED behind a float64 drain (17 -> 44 raw floats on any re-run)'
status: in-progress
pr: 8184
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T00:39:16Z
updated_at: 2026-11-16T20:16:00Z
parent: qou-2002
---

## The straddle (real, and the fix is one line)

`computations/probes/rho_f_categorical_probe.py` is manifest-declared
**`ideal_muon`** -- a POSITIVE declaration, not a runtime default -- and reads
`markov-peel-atomic-tr-m.witness.json`, which is **proton**. The anchor-matched
twin `markov-peel-atomic-tr-m-muon.witness.json` exists, carries the same six
atoms, and is not read. This is the MIRROR of the tr_m_q_hecke defect
(PR #5723): muon consumer, proton reference, rather than the other way round.

One-line fix, verified to work: line 75, point `_peel` at the `-muon` twin.
Measured effect on the values: ~7.9e-8, e.g. `tr_M_proton`
1.06530614425 -> 1.06530622861. Exactly the mu-p gap, as expected.

## Why it cannot land yet

Re-running the producer -- with OR WITHOUT the anchor fix -- takes its witness
from **17 raw float64 fields to 44**, which trips the raw-float64 ratchet as a
REGRESSION. Measured both ways to be sure the anchor change was not the cause:

    baseline (committed)        17
    re-run, reference UNCHANGED 44     <-- pre-existing staleness
    re-run, anchor-FIXED        44     <-- identical; not my edit

The committed witness is simply old: the current producer emits `true_rho`,
`delta` and `err_pct` fields that the committed one does not contain at all.

So the anchor fix is correct and cannot be committed, because committing the
regenerated witness needs the ratchet green and the ratchet's own rule is "Fix AT
THE PRODUCER. Do not add a file to a baseline, do not --rebaseline, and do not
hand-edit a number, to make this green."

## What the drain actually requires

Not a serialization tidy -- the probe computes in `float` end to end:

    L95   _peel_data[(int(z), int(n))] = float(trm)
    L134  return float(n)
    L180  def score(rho_pred: float, true_rho: float | None) -> dict
    L183  delta = rho_pred - true_rho
    L184  err_pct = delta / true_rho * 100.0

Per AGENTS.md, "PROBES ARE NOT EXEMPT" and a float64 input poisons the result.
The fix is to carry `mpmath.mpf` from `float(trm)` onward and serialize via
`_precision.fmt` -- the same rewrite applied to `rho_k_h3a_gg_trajectory`,
`native_5_strand_baryon` and `tr_m_q_hecke_seminormal` in PR #5723. Small, but it
changes what the probe publishes and deserves its own diff.

## Do BOTH in one change

Draining without the anchor fix leaves the straddle; fixing the anchor without
the drain cannot pass the gate. They land together or not at all.

## Progress Update (2026-11-16, PR #8184)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/AnchorManifestTriageAndAmeFloatDrain.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/anchor_manifest_triage_and_ame_float_drain_probe.py` and stamped witness `computations/probes/anchor-manifest-triage-and-ame-float-drain.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 100f1be37af2187c6d27ac18b72a859b25538c6c`).
- [ ] Awaiting merge of PR [`litlfred/qou#8184`](https://github.com/litlfred/qou/pull/8184) (`0a6bb0fe54cf925fb3bdc7285374e8ee0913d6dd`).

