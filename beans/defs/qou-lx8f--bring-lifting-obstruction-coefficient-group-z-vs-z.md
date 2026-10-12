---
# qou-lx8f
title: 'Bring lifting obstruction: coefficient group (Z vs Z/2 vs O^x) and the Bring-specific vanishing claim'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:14:41Z
updated_at: 2026-10-12T19:14:41Z
parent: qou-vo9t
---

## Question
The brane-tower lifting obstruction kappa_n on Bring's surface Sigma_4 is written with three different coefficient groups in the corpus:
- **Z**: the Euler class e(xi) = -6 in H^2(Sigma_4, Z) (fluid-dynamics/ns-obstruction-*.md). Also the `persistence` field and `perpetual_obstruction` in lifting-and-descent/yekutieli-lifting.lean.
- **Z/2 = centre(SU_q(2))**: QOU/BringsSurface.lean `yekutieli_lifting`. Its docstring falsely said H^2(Sigma_4, Z/2) = 0; corrected in PR #7747.
- **O_M^x**: yekutieli-lifting.md and the archimedean band.

## The tension
-6 is nonzero in H^2(Sigma_4, Z) = Z, but -6 = 0 mod 2. So "the obstruction persists" (Z) and "the obstruction vanishes" (Z/2) can both be true of the same Euler class under different coefficient groups. The two readings imply opposite answers to "does the tower lift on Bring?".

## Facts already true
- H^2(Sigma_g, Z/2) = Z/2 and H^2(Sigma_g, Z) = Z for a closed orientable surface.
- w_2(T Sigma_g) = chi mod 2 = 0, so every closed orientable surface is spin; for Bring, chi = -6.

## To do
1. Identify which bundle or gerbe the tower lifts, and its band (corpus-grep is running).
2. Formalize (sorry-free) the reduction-mod-2 statement: the mod-2 image of an even Euler class vanishes.
3. Report which reading the corpus actually supports; do not choose one by fit.
