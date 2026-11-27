---
# qou-mkem
title: 'GAP: derive the m_K/m_pi EM addend (alpha/pi)*m_pi^2*(1+log(1+hbar_q)) -- scale and form are chosen, not derived'
status: todo
type: task
priority: normal
created_at: 2026-11-20T08:13:33Z
updated_at: 2026-11-27T15:10:00Z
tags:
    - compute-accuracy
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

**2026-11-27 (compute-accuracy C5, PR #9449).** Still open; label **Selected**. Since 2026-11-24 the factor is a
proper-time integral over [e^-1,1] U [1,1+hbar_q] (`meson_em_schwinger_proper_time_decomp`), but the UV endpoint
1+hbar_q vs q is not fixed by any corpus object (gap -log(1-hbar_q^2) > 0, +51 vs +967 ppb), and the Dashen sign
identity shows the term is not the leading EM shift. Scale (alpha/pi)*m_pi^2 still chosen. α_em is not the blocker
(Lipschitz bound, <= 0.048 ppb across sorry-free arms). Audit docs/audits/2026-11-27-mk-mpi-selection-status.md.
