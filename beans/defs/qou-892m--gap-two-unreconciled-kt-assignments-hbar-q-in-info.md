---
# qou-892m
title: 'GAP: two unreconciled kT assignments -- hbar_q in information-theory vs E_0 in the binding law'
status: in-progress
pr: 8219
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T17:31:15Z
updated_at: 2026-10-10T07:01:41Z
parent: qou-v2om
---

Found doing the literature check on the S-vs-H question (qou-y0mc, already closed).

Two blocks assign kT differently and nothing reconciles them:

  information-theory/boltzmann-constant.md
      k_B * T_phys = hbar_q = (q-1)/q   ~ 0.09908171604   (dimensionless)

  mass-endomorphism/markov-trace-gibbs-free-energy.md
      Delta F = kT ln(Z1/Z2)  with  kT = E_0 = 4.185981363 MeV

NOT a unit conversion. Measured: E_0/m_e = 8.191761172 against 1/hbar_q =
10.09267946; m_e*hbar_q = 0.0506 MeV; m_e/hbar_q^2 = 52.05 MeV. No simple
relation lands on E_0.

Grepped: the information-theory chapter is 177 blocks and NEVER mentions E_0.
So the two thermodynamic frames do not refer to each other anywhere.

This is orthogonal to which entropy functional is right (that is settled -- S,
by extensivity). It asks whether the framework has ONE temperature or two
unrelated ones wearing the same name.


## 2026-10-10 — pointer

Tracked under related carrier M13 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.


## Progress Update (PR #8219)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`ThermodynamicTemperatureAndRepinBound.lean`, `SiteVsBondVolumeFactorTwo.lean`, `TwoDimensionalInterfaceCollapseAndOrdering.lean`, `WritheSignOppositionEndpointSplit.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` probe (`computations/probes/kt_repin_octahedron_interface_writhe_probe.py`) and stamped witness (`computations/probes/kt-repin-octahedron-interface-writhe-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8219 (`ready: 0004396c02a14ba756cc43c66855073b0a08f82d`)
