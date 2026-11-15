---
# qou-bbsy
title: 'W3 (qou-3bp8): self-consistent theta fixed point. The T4 theta values (0.05894648 / 0.20323503) were back-solved under CONSTANT A_omega=3; W2 shows the winding-refined channel gives a theta-DEPENDENT A_eff(theta) with a genuine bar-odd (Im) part and the correct sign flip at the q0^2 sheet (Im-ratio -6.03 vs observed -4.075). Well-posed next step (a DERIVATION, not a fit): solve S_K = A_eff(theta)*kappa*(ln^2 q0 - theta^2) self-consistently for theta at each anchor, using the measured Im/Re structure of A_eff rather than the constant 3. Two sub-questions: (a) does the fixed point exist and is it unique per anchor; (b) does the self-consistent Im-ratio move toward -4.075. Anti-fit guard: theta is SOLVED from the channel, not tuned; if the fixed point requires a free normalization, STOP and report.'
status: completed
type: task
priority: normal
created_at: 2026-08-01T17:51:58Z
updated_at: 2026-08-01T18:14:42Z
---


## 2026-08-01 RE-SCOPED and CLOSED (not run as specified)

The fixed point as written would have used the winding A_eff (sigma1sigma1)
in the T5 channel whose A_omega is sigma1sigma2 — the exact cross-channel
error the same-day channel audit diagnosed. Running it would have
hard-wired the mistake.

What was done instead (W3 probe + StokesSymmetryConstant.lean, sorry-free):
the certified Stokes matrix satisfies S12 + S21 = 3*S11 EXACTLY as an
integer q-series identity through q^400 (and det = 1). So A_omega = 3 is a
STRUCTURE CONSTANT — exact, q-independent — not an entry value that
deforms. Of the three readings coinciding at q->0, R1 (raw entry 1.5852) is
excluded by the theta-reality bound A >= 2.054 and R2 (3.7067) is
q-dependent; R3 is exactly 3 at every order, including at a pre-asymptotic
truncation where R1/R2 are garbage. The corpus value is VINDICATED and the
deformation question was ill-posed.

Successor open items (NOT this bean): derive the integer 3 from the 13
categorical drivers; the sigma1sigma2 x-refinement for 4_1 (absent from the
literature).
