---
# qou-g7nn
title: Repoint 4 lean refs with an obvious successor; count structure fields in the ref audit
status: completed
type: task
priority: high
tags:
    - lean
created_at: 2026-11-22T09:20:30Z
updated_at: 2026-11-22T09:29:46Z
parent: qou-uwyf
---

Refs: QOU.Observations.centered_hecke_variance_positive -> centeredVariance_pos (also in qou-5d0x); QOU.BraidKnot.confined_knot_binding -> confined_knot_extremal_cancellation or confined_knot_weighted_cancellation (pick from the block statement; also in qou-2u26); QOU.QBeta.FiveTwoDTSpectrumSplit (module name) -> dt_spectrum_two_element; GBResidueSpectralSum.spectral_decomposition is a structure field, so teach computations/audits/lean_ref_resolution_audit.py to count structure/class fields. Re-run the audit and commit the witness.

Record: docs/audits/2026-11-22-lean-audit-snapshot-gaps.md (§3). Epic qou-uwyf.

Done 2026-11-22 in PR #8977 (commit 642d84bd06c). 1321 of 1328 refs resolve.
