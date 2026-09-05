---
# qou-psjm
title: 'Session: precision-truncation audit — AME + witness-copy classes, HARD GATE wiring, drain queue'
status: in-progress
type: milestone
priority: normal
created_at: 2026-09-05T12:02:04Z
updated_at: 2026-09-05T12:28:22Z
---

## 2026-09-05 — detector extended, wired, calibrated (branch claude/precision-truncation-audit-sidecar-r5vjkx)

`codata_truncation_audit.py` already existed (#4960, qou-46ke) and was in NO
array — nothing had run it for three weeks. Now a blocking entry in
`scripts/precision-gates.sh`, verified running in the harness.

Four defects fixed, three of them the gate's own defect class:

1. **The canonical was itself truncated.** `str(Q_MP)` renders at ambient
   `mp.dps` = mpmath default **15** at import, so canonical q0 was 15 of its
   50 digits. `classify()` asks `canon.startswith(lit)`, so every q0 literal
   LONGER than 15 digits was reported CLEAN — and long literals are exactly
   the hand-copied ones.
2. **Prefix-only cannot see a WRONG value.** Added `DIVERGENT`, decided on
   the VALUE not the string SHAPE.
3. **No AME coverage.** Added the 7 AME2020 binding energies. 492 of the
   findings are AME.
4. **Two false-positive classes**, caught by re-measuring before shipping:
   `ROUNDED` (correct round-to-nearest, ~20x over-flag) and the MUON pin
   (11.6 ppb from proton, inside tolerance — 195 correct literals scored
   wrong until the muon anchor got its own CANON row).

Measured: **970 blocking in ~500 files** (450 TRUNCATED / 498 DIVERGENT /
22 ROUNDED), 305 exact duplicates not blocking. Baselined; NEW arrivals block.

### CONFIRMED: scripts copy a deprecated witness rather than load it
`8.481798`, `7.718043`, `28.295673` are all present in
`qou-mass/src/qou_mass/data/_deprecated/ame-2020-binding-energies.witness.json`
— the hand-maintained file `codata_constants.py` says "had drifted on
5Li/7Li/9Be" and which was eliminated as a source of truth. ~190 live script
literals are copies of that stale witness. This is the user's own hypothesis,
verified.

### OPEN
- The 970-item drain (value-changing; overlaps qou-46ke / me3r / ce18).
- A general witness-copy detector (class C) — phenomenon confirmed, detector
  not built.
- Scope: `scan()` walks `computations/` only — not `tools/`, not `qou-mass/`.
