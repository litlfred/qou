---
# qou-1kq0
title: 'path_b probe reports nonzero binding for a FREE nucleon: B_AME(p) = 1.27e-06 MeV'
status: in-progress
pr: 8215
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T03:08:49Z
updated_at: 2026-10-04T15:25:59Z
parent: qou-v2om
---


Found 2026-08-31 while draining convention-C residues from
`computations/probes/path_b_defect_binding_probe.py` (PR #6330). **Pre-existing
on `main` — not introduced by that PR**, which was verified explicitly (see
"How I nearly mis-attributed it" below).

## The defect

A free proton has zero binding energy by definition. The probe reports

    rows[0] (atom "p")  B_AME_MeV = 1.2706900633929763e-06

because the two sides of `B_AME = constituent_sum − M_AME` are computed at
different precisions:

- `constituent_sum(1, 0) = M_P_MEV + M_E_MEV`, now full-precision `mpf`
  (`qou_substrate` CODATA constants);
- `M_AME["p"] = 938.78308711`, a **hardcoded 11-digit literal** in the probe.

Under the old all-float64 arithmetic the two happened to cancel to `0.0`. They
no longer do, and the residue is exactly the truncation of that literal.

## Why this is a real defect and not a rounding curiosity

It is a **precision straddle inside one computed quantity** — the class
AGENTS.md forbids outright: *"Never straddle the two layers inside one
quantity. Mixing ... in a single computed number is a defect regardless of its
size."* Here it is not two anchor layers but two precisions, and the effect is
the same: a quantity that is zero by definition acquires a nonzero value from
its own bookkeeping.

Downstream it also produces `B_err_pct = -100.0` for the proton row, which is
noise in the probe's own error statistics.

## What is NOT established

**What the fix should be.** There are at least two readings and they are not
equivalent:

1. `M_AME["p"]` is meant to be the AME table value, in which case the probe
   should carry it at full table precision and `B_AME(p)` is legitimately a
   small nonzero residual measuring table-vs-CODATA disagreement.
2. `M_AME["p"]` is meant to be *definitionally* the free-proton constituent
   sum, in which case it should be derived from the same constants and
   `B_AME(p)` is identically zero.

Reading 1 makes the number meaningful; reading 2 makes it a bug. **Choosing
between them is a decision about what the probe measures, not a repair**, so it
was deliberately not made in passing during a convention-residue drain.

## Priority: low, and here is why

`path_b_defect_binding_probe` is already a **scope-(a) negative** — the
defect-binding model misses AME by a mean 65.4 % on `A >= 2` under convention D
(70.6 % under C). A 1.27e-06 MeV artifact on the p row does not change that
verdict in any direction. Fix it when the probe is next revisited for its own
sake.

## How I nearly mis-attributed it

The first witness diff showed this field as `0 -> 1.27e-06`, which reads as
"the change I just made broke the physics". It did not. I had diffed against
the **committed** witness, which is stale, rather than against a fresh run of
the unmodified code — the contaminated-baseline trap the corpus already
documents in the witness-staleness triage. Re-baselined from a fresh unmodified
run, the field is `1.2706900633929763e-06` **on both sides**, and the number of
moved fields drops 53 -> 42.

**Baseline from a fresh run of the unmodified code, never from the committed
artifact.** The committed artifact carries every drift since it was last
regenerated, and attributes all of it to whatever you changed last.


## Progress Update (PR #8215)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`FreeNucleonPrecisionStraddleDefect.lean`, `TowerPartitionGrowthAndWeightSubstitution.lean`, `InterfaceScaleFloorAndBandDisjointness.lean`, `SWaveAntisymmetryIsospinGrading.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact integer-partition DP probe (`computations/probes/free_nucleon_straddle_h3a_band_isospin_probe.py`) and stamped witness (`computations/probes/free-nucleon-straddle-h3a-band-isospin-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8215 (`ready: 5d009c2bc892c5362b5b72a46c0f7f2e162d8d40`)
