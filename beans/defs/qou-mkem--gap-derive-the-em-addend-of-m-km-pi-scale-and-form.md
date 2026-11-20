---
# qou-mkem
title: 'GAP: derive the m_K/m_pi EM addend (alpha/pi)*m_pi^2*(1+log(1+hbar_q)) -- scale and form are chosen, not derived'
status: todo
type: task
priority: normal
created_at: 2026-11-20T08:13:33Z
updated_at: 2026-11-20T08:13:33Z
parent: qou-3l2l
---

**Open, by six-path corpus-grep 2026-11-20** (audit docs/audits/2026-11-20-mk-mpi-derivation-status.md §5, PR #8529).

No content block or Lean declaration derives the scale (alpha/pi)*m_pi^2 (picked from four
candidates by closeness to the residual, 2026-05-28 audit) or the factor 1+log(1+hbar_q) ((1+hbar)
closed to 0.46 %, -hbar^2/2 closed further, then the log was named as a series with that jet).
qou-v6oz removed the truncation knob; it did not derive the form. meson_EM_closed_form proves only
the truncation's rational rewrite.

Proved 2026-11-20 (QOU.BraidKnot.MesonFusionIndexSelection): sqrt_jet_agrees_to_order_two,
pade_jet_agrees_to_order_two -- the matched order-2 jet is shared by sqrt(1+2h) and the [1/1] Pade.
Measured: err 51.48 (log) / 63.68 (sqrt) / 44.96 (Pade) / -8718.6 ppb (factor 1); all
order-2-jet forms inside 263.6 ppb, so the FORM choice does not move the verdict, the SCALE does.

Assessment (not a corpus claim): the addend is ~4 % of the measured pi+- EM splitting
(49.5 vs 1261 MeV^2) and does not have Dashen-LO structure; a derivation must say which object it is.
