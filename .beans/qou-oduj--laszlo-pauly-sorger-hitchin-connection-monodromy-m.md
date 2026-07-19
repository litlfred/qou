---
# qou-oduj
title: 'Laszlo-Pauly-Sorger Hitchin connection monodromy (MonodromyHitchinY): WZW/Stokes monodromy — hbar<->2pi i/N wall + s5-so3 keystone'
status: todo
type: task
created_at: 2026-07-18T22:17:25Z
updated_at: 2026-07-18T22:17:25Z
---


## Fresh-look gap-feed (2026-07-19, see qou-do3a)
Hitchin connection monodromy = CS/WZW mapping-class-group rep = the framework's Hecke braiding; relates flat sections across Stokes sectors. Speculative for mass/binding; candidate handle on the ħ↔2πi/N resummation wall (Q_β two-faces).

## RE-POINT (2026-07-19) — Hitchin monodromy ↔ τ = tr B frontier (NOT just Q_β)

Sharper than the original "speculative for mass/binding": the binding kernel
R(q,x)=x²−τx+1 (GAP-3, derived) has its ONE open number τ = tr B — a **fibre
monodromy trace**. Laszlo–Pauly–Sorger compute exactly such monodromy traces of the
Hitchin connection (= CS/WZW mapping-class-group rep = the framework's Hecke
braiding). So this paper is a candidate handle on the τ = tr B geometric derivation
(the s5-so3 keystone / Beasley–Witten route, #2524/#2503), the actual mass/binding
frontier — not merely the Q_β two-faces resummation. Coordinate with z2bn/lever1-trB.

## ATTACK 2 RESULT (2026-07-19) — classification (ii): right object type + A₅=level-8, but unitarity wall
Probe tau_binding_hitchin_wzw_wall_probe.py (3/3). LPS Prop 5.1 gives the SL₂ det-1 bar-even WZW/Hecke
monodromy trace [2]²−[2] (=τ_torus 2.033 at q0, ≠ τ_binding 2.6424); Prop 5.3 gives l=8→A₅ = the keystone
icosahedral symmetry (genuine confirmation). BUT root-of-unity WZW monodromy is unitary → elliptic
|tr|≤2 at every level incl. l=8 (tr=1.0); cannot reach hyperbolic τ>2 (scope-b, WRT unitarity). So the
Hitchin route re-lands on the owner-gated keystone archimedean-continuation wall — structural analogy,
NOT a derivation. Do not pass off as closure.
