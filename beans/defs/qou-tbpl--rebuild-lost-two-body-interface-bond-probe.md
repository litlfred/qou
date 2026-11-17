---
# qou-tbpl
title: Rebuild the lost two_body_interface_bond_probe (committed 0-byte in 079fd5e51b)
status: in-progress
type: task
priority: normal
tags:
    - compute
    - provenance
parent: qou-ales
created_at: 2026-10-13T14:10:00Z
updated_at: 2026-10-13T16:00:00Z
---

Owner ruling 2026-10-13 (option 1, "delete + bean"): the producer
`computations/probes/two_body_interface_bond_probe.py` was committed as a **0-byte file**
in `079fd5e51b` (session `session_01SVz9wTyu9X4uLbfvEKADVH`). That is the only commit that
ever touched it and its witness was never on `main`, so there is nothing to restore. The empty
file is deleted; the Lean companion `QOU/Mass/TwoBodyInterfaceBond.lean` (sorry-free, 9 decls)
is intact and does not depend on it.

**UNVERIFIED — not citable until reproduced.** The only record of the probe's numbers is the
commit message of `079fd5e51b`:

- candidate set: γγ words over the two straddling vertices v1 = σ₁σ₂⁻¹, v2 = σ₂σ₃⁻¹, all 126
  words up to 6 vertices, convention D, H_6, proton pin, E_0^full, 60 dps;
- 83/126 genuinely two-body; 34 pass bond-alone reading 3;
- S1 (bond-alone reading 3, cost-minimal): forced tie at 4 crossings {v12, v21};
  v21 two-body with B_pp 4.318023, B_nn 4.271811, B_pn 4.561864, B_np 3.986218 MeV;
- S2 (whole-element, live (B) scope): no two-body word selected.

**Task.** Re-derive the probe from that specification (mpmath end to end, witness with
provenance, `scripts/precision-gates.sh --changed` clean). Anti-fit: the rebuilt numbers stand
on their own — do **not** tune anything to reproduce the figures above; a disagreement is a
finding to report, not a bug to fit away.

2026-10-13 follow-up: the 0-byte witness `computations/probes/two-body-interface-bond-probe.witness.json` (hyphenated name, missed by the first underscore grep) is also deleted under the same ruling; the q0 audit had been reporting it as `Q0_PARSE_ERROR`.

## Round 68 Formalization Progress (PR #8285)
- Formalized `QOU.Mass.TwoBodyInterfaceBond.cross_difference_eq_zero` (sorry-free, 0 advisories across all 6 static vacuity audits).
- Verified at 80-dps `mpmath` (`computations/probes/twobody_deficit_regulator_sdp_milnor_probe.py`, `scriptHash: 39a564805d3e`, Commit 1 `70bec575bb493c7f91cf1b39cb54e58ef8343777`, Commit 2 / Witness `250465c60a6cea44d9f569e88cc79ee2c8d8051b`, PR `litlfred/qou#8285`).
