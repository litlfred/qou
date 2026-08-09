---
# qou-44se
title: 'Witness provenance regressed: missing 10 -> 23 since 2026-08-01, completeness 0.9952 -> 0.9903'
status: todo
type: task
created_at: 2026-08-09T02:19:38Z
updated_at: 2026-08-09T02:19:38Z
---


Found 2026-08-09 while triaging stalled PR #4568 (bean `qou-x6as`).

#4568 refreshes the provenance-audit snapshot and claims *"missing 10 -> 9"*.
That was true on 2026-08-02. Re-running the producer
(`computations/audits/witness_provenance_audit.py`) against current main:

| snapshot | total_scanned | prov_missing | completeness_ratio |
|---|---|---|---|
| main (2026-08-01) | 2296 | 10 | 0.99521 |
| PR #4568 (2026-08-02) | 2351 | 9 | 0.99575 |
| **current main** | **2470** | **23** | **0.99028** |

**The backlog is moving the wrong way** — this is a live regression, not a
stale-snapshot artifact. 13 new witnesses landed without
`engine` / `scriptFile` / `commitSha`.

Several cluster around currently-open PRs, and are best fixed there, where
the producers are in hand:

- `whitehead-c-sigma-fig8-calib`, `whitehead-c-sigma-hiprec`,
  `whitehead-c0-mpmath`, `whitehead-volume-identification`
  -> open PRs **#4571** (c_sigma torsion) and **#4532** (VC squeeze)
- `qcollatz_cycle_census` -> open PR **#4435**
- `qbeta-5two-enhanced-dilog` -> open PR **#4588**
- `two-row-vs-higher-row-binding-split`, `qlift_kernel_candidate_crosscheck_probe`,
  `theta_jet_gb_grading_probe` -> unattributed so far

**Root-cause question worth answering before draining:** all 13 are missing
the *same three* fields, which is the signature of producers that build their
witness dict by hand instead of going through `WitnessBuilder`. If so the fix
is to route them through the builder, not to hand-patch 13 JSONs — and a
guard is wanted so the next 13 do not appear the same way.

Regenerate the number with:

```bash
python3 -u computations/audits/witness_provenance_audit.py
```

(then `git checkout --` the witness unless you intend to land the snapshot).
