---
# qou-bwwr
title: 'Research: heat-kernel time as RG time — sign of the colour one-loop coefficient'
status: in-progress
type: task
priority: normal
created_at: 2026-11-22T16:16:14Z
updated_at: 2026-11-22T16:26:11Z
parent: qou-8lxd
---

Route R-alpha3 / R-beta3 of the gap study: treat q-heat-kernel time t as RG time and compute the SIGN of the colour one-loop coefficient (antiscreening vs screening) from the braid/Hecke heat kernel. Pre-register the sign prediction and decision rule before computing; no fitting. Coordinate with the alpha_EM per-loop arc (shared a0). Related: qou-bcig (canonical Reeb time s*=hbar_q). Started 2026-11-22 (thread 'Derive m_n', owner card 'Both'). Source: computations/probes/mn_own_identity/GAP-STUDY-qcd-scales.md §6 (main, merged via PR #8804); CORPUS-GREP-gluon-dynamics.md. Owner chose 'Both' 2026-11-22 (create beans + start heat-kernel route). Anti-fit: CAL-1/2/3 only; no selection against PDG/lattice values.



2026-11-22 (branch claude/qcd-heat-kernel-beta0-sign-2026-11-22, draft PR #9059, issue #9058). Prereg 58c6511cf52, probe e553a9052d1 (43/43 exact), RESULT ab5399cf6a6 in computations/probes/qcd_heat_kernel/. MISS on all three pre-registered constructions, scope (a). C1 (corpus Delta_xi, adjoint/singlet heat-weight ratio in (C^3)^{x3k}): b = d log g^2/dt = -[3]_q[2k-2]_q; exactly 0 at k=1 (V x Vbar = 1+8, by the c -> -1-c symmetry of [c][c+1]); screening for k>=2 (-6.12, -12.51, -19.44 at q0); k-dependence shows Delta_xi sees the gl3 U(1) part, so it is not a colour Casimir. C2 (ribbon Casimir): -C_A = -3, screening, trivial. Side check: F-projection of e^{-t Delta_xi} is 0. C3 (1/2 Tr_R H^2): gluon 36 / quark 8/3 (Casimir), 4(q^2+1)^2/q^2 / 0 (Delta_xi), same sign; opposite only via inserted (-1)^F. n_f enters only as an input count. Structural reason (not a proof): a positive colour heat kernel suppresses higher-Casimir channels toward IR; QCD antiscreening is the vector-gluon spin/background-curvature term, which qou has no object for (qou-ni4b). Remains open: background-field/spin reading; whether t is an RG scale (qou-abzr). Kept in-progress.
