---
# qou-6r6d
title: 'A=3 magnitude ROUTE 2: super-Berezinian even/odd cross-sector mixing'
status: in-progress
type: task
priority: normal
tags:
    - a3-cross-channel
    - reorg-2026-10-04
created_at: 2026-08-01T23:36:58Z
updated_at: 2026-11-17T07:28:00Z
parent: qou-v2om
---

ROUTE 2 result (scope-(a), 2026-08-01): the super-Berezinian even/odd cross-term t=B·D⁻¹·C does NOT derive the A=3 magnitude r*=μ3/c3≈1.585 — it supplies it only as a FIT.

Lean QOU/QBeta/SuperBerezinianA3Magnitude.lean (sorry-free, exit 0, generic [Field R]):
- crossTerm_magnitude_surjective: even-face correction (A−t)/A is surjective in the off-block B ⇒ r* is one real constraint on an unconstrained B = a fit; magnitude is a hidden DOF (Rule 14).
- evenFaceCorrection_no_mixing: t=0 → correction ≡1 (why single-trace ingredients are all bracketed at 0.63×).
- A3CrossTermMagnitudeClosed: §3b-tax dependent conjecture, NO instance (the DM-cubic-derived off-block closure = qou-jqof, open).

Distinct from the on-main PARITY bricks (OddDecayWeightParity, BerezinianSelfAdjointCrossTerm): those settle the SIGN (bar-odd, needs non-self-adjoint independent off-blocks); this is the MAGNITUDE angle.

Probe a3_magnitude_berezinian_crossterm_probe.py (0 fit): 0/13 natural substrate readings land r*; r*≈log2 3 (flagged coincidence).

NET: cross-term is the FIRST A=3-magnitude route not EXCLUDED (can reach O(1)), but not a closure — it relocates the wall to deriving B,C from the DM q-cubic (qou-jqof). Nothing wired; free_parameters=0. STOP: qou-jqof stays open.

## Round 62 Update (PR #8255)
- Formalized in PR https://github.com/litlfred/qou/pull/8255 (head `b4ec4b15ca43f486c66d8f53b0eeb216293fc6aa`, Commit 1 `c715790dad2efe16f1713c8a17825e912524e641`, `scriptHash: e2eb499467fc`).
