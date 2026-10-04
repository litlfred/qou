---
# qou-dw20
title: 'qou-t2sc saddle-value: prove (2π/N)log S_{n*,k*} → 4G (van der Veen Clausen/Lobachevsky max-value; the single open hsaddle input of whitehead_vc_of_saddle_value)'
status: todo
type: task
priority: normal
tags:
    - close-candidate
    - reorg-2026-10-04
created_at: 2026-08-01T23:54:37Z
updated_at: 2026-10-04T15:13:40Z
parent: qou-n4nr
---


## Validated (2026-08-01) — hsaddle is TRUE; saddle pinned
- Saddle location (t*,x*)=(1/2,1/4) (discrete argmax of log S_{n,k}).
- Continuum saddle value = 4G EXACTLY (40 dps): 2π∫_0^{1/2}[log2+2log
  sin(π(u+1/4))−log sin(π u)]du = 8Λ(π/4). See computations/whitehead_saddle.py.
- Lean discharge = Riemann-sum→integral convergence at nseq→N/2, kseq→N/4,
  value 4G, via QOU.Knot.Clausen (FigureEightVolumeSaddle analogue). Needs the
  QOU-library build to verify (no longer Mathlib-only).

## Lean discharge UNBLOCKED + started (2026-08-01)
QOU/Knot/WhiteheadSaddleClausen.lean (imports QOU.Knot.Clausen; verified via
lean-direct against built QOU oleans):
- integral_log_two_sin_pi(b): ∫_0^b log(2 sin(π u))du = -clausen(2πb)/(2π) — SORRY-FREE.
- Full value-identity + convergence roadmap documented in-file (all Clausen
  ingredients confirmed present).
Remaining (tractable, next focused pass): (A) prove V=4·clausen(π/2) [log2
cancels → integral_log_two_sin_pi at 1/2,1/4,3/4 + clausen(π)=0 +
clausen(3π/2)=−clausen(π/2)]; (B) Riemann-sum convergence [integral_le_sum_log_sin
/_falling, FigureEightVolumeSaddle E5c pattern]. (A)+(B) ⇒ hsaddle ⇒ unconditional VC.

## VALUE half DONE sorry-free (2026-08-01)
saddle_integral (WhiteheadSaddleClausen.lean): ∫_0^{1/2}(2 log(2sin(π(u+1/4)))
− log(2sin(πu))) = 2·clausen(π/2)/π ⇒ continuum saddle value 2π·∫ = 4·clausen(π/2)
= 4G. Sorry-free (lean-direct). Ingredients all sorry-free: integral_log_two_sin_pi,
intervalIntegrable_log_two_sin_pi, clausen_three_pi_div_two, integral_A, integral_B_zero.
REMAINING = the CONVERGENCE half only (new child bean) — the big Riemann-sum campaign.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
