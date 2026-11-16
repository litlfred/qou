---
# qou-q0dr
title: 'DRAIN: 329 stale q_0 anchors across witnesses (ratchet baselined)'
status: in-progress
pr: 8188
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T23:23:43Z
updated_at: 2026-11-16T20:23:00Z
parent: qou-2002
---

q0_value_drift_audit.py classifies 1617 q0-bearing witness fields: 699 canonical (CAL-2 muon), 564 proton-pin (DOCUMENTED, legitimate -- do not touch), 329 STALE at -0.00284 ppb (2840 ppQ, ~2840x the L1 <=1 ppQ goal), 25 unknown. The stale value 1.10997859555418057528159407960950937799328227995870 matches no documented pin; it agrees with canonical only to 12 digits, i.e. an older or looser solve. ~229 of the 329 are in computations/_deprecated. DRAIN BY RE-RUNNING PRODUCERS, never hand-edit; then --rebaseline (count must go DOWN). Also: 3 witnesses carry 1.1097090248999998962631252652499824762344360351563, a float64 value serialized to 50 dps (option-e-canonical-reeb-v5, option-e-v6-combined-canonical) -- separate float64-padding defect. Found via qou-ny4j follow-up.

---

**ID CHANGED 2026-08-30: `qou-rrgk` -> `qou-q0dr`.** This bean and
`qou-rrgk--germ-viability-probe-...` both carried the ID `qou-rrgk`, and
`beans show qou-rrgk` resolved silently to *this* one -- so the germ bean was
unreachable by its own ID, and a commit message citing `qou-rrgk` read as
closing a q0-drain task it never touched.

This bean was chosen as the rename target because its ID was cited **nowhere**
outside `.beans/`, while the germ bean's is cited in four tracked files
(`computations/alpha_em_germ_viability_probe.py`,
`computations/alpha-em-germ-viability.witness.json`,
`docs/audits/2026-08-29-alpha-em-germ-viability-live.md`, and a landed commit
message). Verified with `git grep` at rename time; no intra-`.beans/`
references and no parent/child links existed either.

Report and guard: bean `qou-ut5r`.

## Progress Update (2026-11-16, PR #8188)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/CodataTruncationAndQ0AnchorRecentering.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/codata_truncation_and_q0_anchor_recentering_probe.py` and stamped witness `computations/probes/codata-truncation-and-q0-anchor-recentering.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 4f0055fd85b9bb82232f9b87ef757139e895bd6d`).
- [ ] Awaiting merge of PR [`litlfred/qou#8188`](https://github.com/litlfred/qou/pull/8188) (`548ed6acbe88e5772065a0fdb4d623f3472d3430`).

