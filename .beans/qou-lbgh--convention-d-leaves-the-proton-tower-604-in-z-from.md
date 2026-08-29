---
# qou-lbgh
title: Convention D leaves the proton tower 6.04% in z from the Phi_q pole
status: completed
type: task
priority: normal
created_at: 2026-08-29T08:43:43Z
updated_at: 2026-08-29T10:48:58Z
---

Measured 2026-08-29, branch claude/tower-gap-lean-and-infra-2026-08-29 (PR
#5978). Probe computations/probes/tower_z_convention_pole_sensitivity_probe.py,
witness computations/tower-z-convention-pole-sensitivity.witness.json.
5 checks, all passing; mpmath 50 dps, cross-checked against the f64 producer at
1.07e-16.

CONTEXT. Companion to bean qou-zloi. There are two tower producers and they take
their Markov parameter from different places:

  mass_at_3A_proper.per_generator_V_hat_3A   Z pinned at h/2 = 0.10453 by weight
                                             symmetry; NO convention reaches it
                                             (proved: markov_param_eq_half_h)
  mass_endomorphism.additive_wedderburn_vol  reads z_mark = q^3/(q^2+1) directly
                                             -> convention D IS live here

This bean is about the second one, which is where the qou-dchz C->D question
actually applies.

FINDING 1 -- it does NOT diverge under D. Max |V_hat|/q across electron, proton
and neutron is 0.97318561755 (proton gen 0). No generator is at or past the
pole. So the +inf in qou-dchz item 1 belongs to convergence_safe_vhat_tower, a
THIRD producer, and does not generalise to this one.

FINDING 2 -- but "not divergent" is not "not close", and the headroom is small.
V_hat is affine in z (vHat_sub_vHat), so vHat_eq_iff gives the unique z landing
each generator exactly on the pole. Relative headroom z*/z_D - 1:

    electron gen 0    102.13 %
    neutron  gen 0     69.04 %
    proton   gen 0      6.04 %   <-- the tight one

So under the canonical convention the proton's gen-0 V_hat sits 6.04 % in the
Markov parameter away from a singularity. Any refinement of z of that order
tips it. (Proton/neutron gen 1 have negative dV/dz, so their pole is at negative
z and unreachable from the positive branch -- not a constraint.)

FINDING 3 -- the C->D move is NOT uniform in direction, so "D is 22.70 % larger,
therefore towers grow" is wrong as a general reading. Tower totals, D/C:

    electron   x 3.0025413626
    proton     x 14.950205664
    neutron    x 0.5982100480   <-- DOWN

The neutron falls because its dominant generator has negative slope. Any
statement about "the effect of D on the tower" has to be per-particle.

SCOPE-(a). Measures the constructions as built; says nothing about which Markov
parameter is right and excludes no ingredient. What it does say is that the
proton tower's finiteness under the canonical convention is not comfortable, and
that whoever revisits z should look at this 6 % before doing so.
