---
# qou-7y3g
title: 'NOT-LEAN-PROVED (Mathlib gap): Vol(4_1)=2xV_tet, Vol(B_3)=2xV_oct are numerical only'
status: todo
type: task
priority: low
created_at: 2026-08-07T17:10:12Z
updated_at: 2026-08-07T17:10:12Z
---

NOT LEAN-PROVED, and NOT REALISTICALLY CLOSABLE SOON — a large Mathlib gap.
Recorded so the numerical status is not mistaken for a proof.

CLAIM (PR #4513, qbeta_sdp_angle_offset_theta_probe.py, R1 section):
  Vol(4_1)  = 2 x volume of the regular ideal TETRAHEDRON
  Vol(B_3)  = 2 x volume of the regular ideal OCTAHEDRON
verified numerically to 9.5e-12 and 3.1e-13 relative (SnapPy vs closed forms
Im Li_2(e^{i*pi/3}) and 4*Catalan).

CONSEQUENCE BEING CLAIMED ON THIS BASIS: neither volume is a measured input —
both are FORCED by the cell decomposition. That reclassifies them from
untraceable literals to `structural` for the no-free-parameter certificate
(bean qou-skum). That reclassification currently rests on NUMERICS.

WHY IT IS HARD: Mathlib has no hyperbolic-volume theory for ideal tetrahedra —
no Lobachevsky function, no ideal-simplex volume, no Mostow rigidity. Proving
this in Lean means building that infrastructure first. This is infra-scale, not
a session-scale task.

HONEST DISPOSITION: leave numerical, labelled numerical. Do NOT axiomatise the
volume identity as a Lean `class` and consume it downstream — that would be
exactly the laundering AGENTS.md forbids ("Axiomatization is NOT a Proof"). If
qou-skum wants `structural` classification, the justification is the cited
literature fact plus this numeric check, stated as such.
