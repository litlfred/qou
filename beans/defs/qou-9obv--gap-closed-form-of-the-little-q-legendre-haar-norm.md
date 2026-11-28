---
# qou-9obv
title: 'GAP: closed form of the little q-Legendre Haar norm on the O_q(SU(2)) Cartan block'
status: todo
type: task
created_at: 2026-11-28T01:30:18Z
updated_at: 2026-11-28T01:30:18Z
---

Related: qou-q3dc (GAP progress notes) and qou-pa7n (Part A). This bean stays open while Part A is open.

This closed form is needed to turn `coupling_raise` (QOU/FluidDynamics/q_ns_triad_raising_coupling.lean) into a decay statement for the spin-raising triad coupling.

Expected value, for monic P_n in zeta, with p = q^-2:

    h(P_n^2) = q^(-2n) p^(n^2) (p;p)_n^4 (1-p) / ((p;p)_{2n} (p;p)_{2n+1})

Source: Gasper–Rahman 2004 §7.3. After the substitution zeta = -q^-1 t, the zeta-moments are the Jackson integral on [0,1] in base p.

Evidence, not proof: the formula matches exactly in rational arithmetic for n <= 7 at q in {2, 3/2, 5/4, 7/3} (computations/qns_little_qlegendre_norm_probe.py).

If proved, the normalised raising coupling satisfies

    C(r)^2 = q^-6 p^(2r+1) ((1-p^r)/(1-p))^2 (1-p^(r+1))^4 / ((1-p^(2r+1)) (1-p^(2r+2))^2 (1-p^(2r+3)) ||beta delta||^2)

At fixed q > 1 this decays like q^(-2r). As q -> 1 it grows like r, so the decay is not uniform in q. This is scope-(a) evidence for one triad family only, not a structural exclusion.

Possible routes: a three-term recurrence or a Christoffel–Darboux identity for the jacobiPoly basis in OqSU2LittleQJacobiBasis, or a Rodrigues-type formula.
