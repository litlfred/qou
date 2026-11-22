---
# qou-abzr
title: 'GAP: no scale variable for a running coupling'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T16:16:13Z
updated_at: 2026-11-22T16:34:57Z
parent: qou-8lxd
blocking:
    - qou-5iaz
---

qou has no object a coupling can run along. q0 is a boundary value only (q0 derivation forever-gated). Candidates: Hecke tower index n, q-heat-kernel time t, KZ coupling kappa ~ log q. Curvature-rank depth k excluded (qou-hnri, 2026-09-04-depth-one-is-empty). Not established that any candidate IS a renormalisation scale. Source: computations/probes/mn_own_identity/GAP-STUDY-qcd-scales.md §6 (main, merged via PR #8804); CORPUS-GREP-gluon-dynamics.md. Owner chose 'Both' 2026-11-22 (create beans + start heat-kernel route). Anti-fit: CAL-1/2/3 only; no selection against PDG/lattice values.

2026-11-22 (n/kappa arms, PR #9059, commits 40489bd8bd5 prereg / 2f12731a1ff probe 89/89 / aefbbf3242c RESULT, computations/probes/qcd_scale_candidates/): MISS scope (a) for tower index n and KZ kappa as scale. N1 Ocneanu isotypic weight: g2 = W_8/W_1 = 8k/(k+3)*[2]_q[4]_q (SU(N): (N^2-1)k/(k+N)*dim_q adj), b = dlog g2/dlog n = N/(k+N) > 0, q-free — definite antiscreening-direction sign with coefficient C_A (N in baryon count k, N^2 in strand count n), but 1/g2 ~ 1+N/k: power law, no log, no n_f. N2 last-strand JM branching: sign bar-odd (b<0 at q0, >0 at 1/q0). KZ K1: omega_8-omega_1 = C_A/2 for any external pair, b = Re(kappa)*C_A, quark and gluon pairs identical; Drinfeld-Kohno q=e^{i pi kappa} at real q0 gives b=0 exactly; resonance logs only at |q|=1. No candidate (t, n, kappa) gives log running with a C_A vs T_F n_f split. Stays open.
