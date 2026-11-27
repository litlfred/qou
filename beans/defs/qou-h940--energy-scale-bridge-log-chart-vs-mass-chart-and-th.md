---
# qou-h940
title: 'Energy-scale bridge: log chart vs mass chart, and the sign conflict'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T22:03:24Z
updated_at: 2026-11-27T22:25:42Z
parent: qou-myts
---

Thread 'Unify the log and mass-formula energy scales', branch claude/energy-scale-bridge-2026-11-27.
Proved (Lean, sorry-free): the mass chart (w = q d/dq log tau, #9733) is the Euler derivative of the log chart (L = log tau, #9718); E1 - E0 = m_e (L_e/w_e) delta(L_X/L_e). With L_e < 0 < w_e the charts agree in sign on X iff L_X w_X < 0 (sign_agree_iff).
Consequences at q0 (probe scale_bridge_probe.py): n-p +0.289 MeV (log) vs -0.319 MeV (mass); Delta-N -0.989 vs +0.066; ruled bond letters give B < 0 in both charts under the CAL-1 orientation; production binding is positive only because the ruled law uses T = |c| (ruled_law_opposite).
Open: the orientation (which convention carries the sign). Nothing wired. Related: qou-91w7, qou-mbfv.

2026-11-27 22:07Z: isospin thread reports kappa on the log chart = 2 ln q m_e/(-ln tau_e) = 0.2887 MeV per T(T+1), with larger T binding more there: the same chart split, opposite to the ruled antitone law. Their kappa waits on this bean's orientation decision.

2026-11-27 framing-corrected check (y3=(q^4+1)/(q^2+1)^2 in place of tau_e): L_e=-0.68240, w=q d_q log y3=0.20348, L*w=-0.1389<0, so the sign split SURVIVES framing correction. n-p cell: mass chart -2/w=-9.83 m_e vs log chart +0.306 m_e. w(1)=0, so the mass-chart unit diverges at q=1. Only the k=1 (q d_q) chart is ring-valued; log is not in Q(q). Sign theorem is algebraic, so it holds in the ring-valued setting too.

2026-11-27 orientation (Carl chose A): tau_e = q^3*y3, y3 bar-invariant, omega bar-odd (EnergyScaleOrientation.lean, sorry-free; orientation_probe 19/19). Log-chart unit sign comes from the framing-free part l_e=-0.682; the mass-chart unit sign comes from the writhe 3. The split already holds at q=1 (l=-ln2, omega=0). The log unit flips only at tau_e=1, q*=1.2414. The n-p q^-2 is not framing (nucleon writhe 0 under the ruled word). Open fork: does the energy sign come from the framing or from the framing-free part?

2026-11-27 relay from isospin thread (#9747 335b6c7e2): the C(3A,n_d) weight count read through B += alpha*ln(count) gives (N-Z)^2/A with coefficient alpha/6, which is 0.62 MeV at alpha=8G m_e, about 37x below the classical 23 MeV. It is a test term for any derived log-count scale. With the CAL-1 log-chart unit |m_e/L_e| = 2.707 m_e = 1.383 MeV/nat, alpha/6 = 0.23 MeV, which is about 100x below. Noted, not wired.

2026-11-27 no-go (Lean log_chart_np_delta_opposite / mass_chart_np_delta_opposite): in either chart, for ANY electron unit, n-p (pure power) and Delta-N (bar-even) get opposite signs. The #9789 reading [4]/q^3 turns n-p positive (+0.805 m_e mass chart) but Delta-N negative (-0.166). Getting both right needs pure powers and bar-even cells read with different sign, which is a second structural input.
