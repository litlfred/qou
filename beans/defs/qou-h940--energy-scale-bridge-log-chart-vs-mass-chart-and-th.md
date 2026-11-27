---
# qou-h940
title: 'Energy-scale bridge: log chart vs mass chart, and the sign conflict'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T22:03:24Z
updated_at: 2026-11-27T22:18:18Z
parent: qou-myts
---

Thread 'Unify the log and mass-formula energy scales', branch claude/energy-scale-bridge-2026-11-27.
Proved (Lean, sorry-free): the mass chart (w = q d/dq log tau, #9733) is the Euler derivative of the log chart (L = log tau, #9718); E1 - E0 = m_e (L_e/w_e) delta(L_X/L_e). With L_e < 0 < w_e the charts agree in sign on X iff L_X w_X < 0 (sign_agree_iff).
Consequences at q0 (probe scale_bridge_probe.py): n-p +0.289 MeV (log) vs -0.319 MeV (mass); Delta-N -0.989 vs +0.066; ruled bond letters give B < 0 in both charts under the CAL-1 orientation; production binding is positive only because the ruled law uses T = |c| (ruled_law_opposite).
Open: the orientation (which convention carries the sign). Nothing wired. Related: qou-91w7, qou-mbfv.

2026-11-27 22:07Z: isospin thread reports kappa on the log chart = 2 ln q m_e/(-ln tau_e) = 0.2887 MeV per T(T+1), with larger T binding more there: the same chart split, opposite to the ruled antitone law. Their kappa waits on this bean's orientation decision.

2026-11-27 framing-corrected check (y3=(q^4+1)/(q^2+1)^2 in place of tau_e): L_e=-0.68240, w=q d_q log y3=0.20348, L*w=-0.1389<0, so the sign split SURVIVES framing correction. n-p cell: mass chart -2/w=-9.83 m_e vs log chart +0.306 m_e. w(1)=0, so the mass-chart unit diverges at q=1. Only the k=1 (q d_q) chart is ring-valued; log is not in Q(q). Sign theorem is algebraic, so it holds in the ring-valued setting too.
