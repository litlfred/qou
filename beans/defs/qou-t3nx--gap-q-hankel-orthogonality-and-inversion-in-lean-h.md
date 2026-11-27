---
# qou-t3nx
title: 'GAP: q-Hankel orthogonality and inversion in Lean (Hahn-Exton, base p^2, p = 1/q0)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T21:59:36Z
updated_at: 2026-11-27T22:30:56Z
---

Thread 'Audit the q-Bessel special-function dictionary' 2026-11-27. The Coulomb shape factor f = 0.520011 (PR #9665) rests on q-Hankel orthogonality on p^Z checked numerically only. State the base p^2 explicitly against the sphere side's q^2 Haar convention.



2026-11-27: Algebraic half proved, sorry-free, in PR #9796 (QOU/Nuclear/QHankelGreenIdentity.lean). The Hahn-Exton formal q-difference equation, its symmetric lattice form t(F_{k+1}+F_{k-1})-(1+t^2)F_k = -Q^k F_k with weight Q^k = p^{2k}, the discrete Green identity, and (Q^n - Q^m)*window sum = boundary Casoratians. Base: Q = p^2 = q0^-2, the inverse of the sphere side's q^2. Still OPEN, so the bean stays open: the boundary Casoratians tend to 0 at +-infinity (orthogonality), the normalisation, and inversion. All three are analytic and go in QOU/Transcendental/.
