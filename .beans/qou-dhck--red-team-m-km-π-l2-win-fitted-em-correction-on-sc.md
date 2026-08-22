---
# qou-dhck
title: 'RED-TEAM m_K/m_π L2 win: fitted EM correction on scan-selected term, NOT parameter-free'
status: todo
type: task
created_at: 2026-08-22T15:35:55Z
updated_at: 2026-08-22T15:35:55Z
---

Verdict: the single claimed L2 accuracy success (m_K/m_π, 23.45 ppb, 'beats 100x') is NOT a genuine parameter-free prediction.

Formula: m_K^2/m_pi^2 = [3]_q[4]_q + (alpha_em/pi)(3q^2-1)/(2q^2).

Ablation (mpmath 70dps, reproduces witness):
- strong-only sqrt([3]_q[4]_q): 101.6 ppm -> MISSES 100x target (264 ppb) by 385x.
- full: 23.45 ppb -> beats. Entire win is the EM correction.
- (3q^2-1)/(2q^2) is a 3-term truncation of 1+log(1+hbar_q); the truncation (23.4 ppb) BEATS the untruncated series (51.5 ppb) => stopping point chosen against data (ladder-fit signature).
- alpha_em value barely matters (CODATA vs derived: 23.40 vs 23.45 ppb); the truncation is the lever.

DOF: scan-selected pair (3,4) [audit: 'found by scanning q-integer products', 'spin assignment post-hoc'] + alpha_em (4th input, conditional on open Witten-kappa Lean sorry, own selected crossings 9,10) + data-selected truncation order. >=3 discrete knobs + conditional input.

'Only observable that beats 100x' partly because kaon target (264 ppb) is ~85000x looser than m_p target (0.003 ppb) - kaon measured to only 26 ppm.

Lean 'both pieces proved': meson_qCG_3x4 = q-CG fusion decomposition (real algebra, says nothing about kaon); meson_EM_closed_form = rational-function rewrite (X=X tautology class). sorry-free != derived.

Honest count of UNCONDITIONAL parameter-free sub-100x predictions: 0/5, not 1/5.

Doc: docs/audits/2026-08-22-mK-mpi-l2-red-team.md. Read-only audit; recommends footnoting the dashboard/AGENTS.md row as conditional+truncation-selected and marking stale meson-kaon-pion-derivation.witness.json (retracted (9/5)^2 power-scan fit).
