---
# qou-xi16
title: 'GAP: KS primitive wall-crossing <-> quantum pentagon link is unformalized (WallCrossing placeholder axiom)'
status: in-progress
pr: 8201
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T21:02:22Z
updated_at: 2026-10-04T15:20:08Z
parent: qou-frzo
---

Found draining the small-category vacuity tranche (qou-h3ly), PR #5408.

**Two linked placeholders in QOU/Mathlib/WallCrossing.lean:**

1. `KontsevichSoibelman.primitive_wall_crossing` — the KS axiom field is
   `∀ (_W : Wall L) (_Zp _Zm : CentralCharge L), True`, with the real
   content ('multiplicities differ by ±⟨γ₁,γ₂⟩·Ω(γ₁)·Ω(γ₂)') living only in
   a comment. So the class does not constrain any instance.
2. `primitive_KS_is_pentagon : True := trivial` — REMOVED in #5408. It
   claimed to link the rank-2 KS formula to the quantum pentagon identity
   `E(e₁)E(e₂) = E(e₂)E(e₁+e₂)E(e₁)`, said to be the content of
   `QOU.BraidKnot.QRogersPentagonArchimedean`. WallCrossing.lean does not
   import that module and nothing consumed the declaration.

**Why it could not be restated in place:** the pentagon identity needs the
quantum torus algebra and the `E(·)` dilogarithm operator (absent here);
the obligation on the other side of the link is itself a placeholder; and
the file is `sorry`-free, so the state-and-queue route would have added
the first `sorry` to a clean file (Strict Lean Discipline §2).

**Real work required:** give `primitive_wall_crossing` a genuine Prop field
(the multiplicity-jump formula over a quantum torus), then either import
`QRogersPentagonArchimedean` and derive the rank-2 reduction, or state it
as a §3b conditional. Do not restore a `True`-valued link.

## Progress Note (2026-11-16, PR #8201)
- Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/C1ConnectionThetaAndKSWallCrossing.lean` (wired into `QOU.lean`, `0` `sorry`, `0` `axiom`, `0 CRITICAL / 0 advisory` across all 7 Lean static vacuity/borrowed-name audits).
- Verified by 80-dps `mpmath` / exact rational probe `computations/probes/c1_connection_theta_and_ks_wall_crossing_probe.py` and witness `computations/probes/c1-connection-theta-and-ks-wall-crossing.witness.json` (`scriptCommitSha: 6a7d9973a198adec786d4227a4bfc12f4785934e`, `scriptHash: c4713523ced0`, `allPassed: true`, `0` raw `float64` fields).
- PR: https://github.com/litlfred/qou/pull/8201 (`671820c7c233d2a9562f6f72f68cfb5b01b9b764`).
