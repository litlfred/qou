---
# qou-htk4
title: 'GAP: lepton generation mass dependence via the T(2,n)-4_1 coupling. The multiplicative net(T(2,n)) bridge is EXCLUDED (docs/audits/2026-08-07-lepton-net-to-mass-bridge-exclusion.md, Lean morganVoyceBK_binet + mass_ratio_rigidity): net is log-linear in the winding, the observed tower is log-concave. Torus knots have Vol=0, and the corpus muon mass already comes from Vol(4_1) (the hyperbolic Higgs knot), so generation dependence should be sought in a linking/satellite quantity coupling T(2,n) to 4_1 -- something NOT multiplicative in a normal-form amplitude. Successor to qou-lsp9.'
status: todo
type: task
created_at: 2026-08-07T17:40:00Z
updated_at: 2026-08-07T23:30:00Z
---

## Scope sharpened, 2026-08-07 (second pass on qou-lsp9)

Do NOT retry the Markov trace. The exclusion is no longer "the net does
not work" -- it now covers EVERY positive H_2(q)-linear readout, the
canonical tr_M included, on a proved invariant (positivity of the
Morgan-Voyce continuant for q > 1 leaves no node for a ratio to blow up
at). See `docs/audits/2026-08-07-lepton-linear-readout-rigidity.md`.

The consequence for this bean is a sharper target: a working bridge must
be NON-LINEAR in H_2(q), or must read from outside H_2(q) altogether.
Reading any single number off the lepton's own 2-dimensional braid
algebra is now closed. The linking/satellite coupling to 4_1 qualifies on
the second count (4_1 is not in H_2); an additive interface term
qualifies on the first.

## Screening tool landed, 2026-08-07 — test candidates BEFORE building them

`docs/audits/2026-08-07-lepton-tower-bend-screening.md`;
Lean `lepton_tower_bend_invariant.lean`;
probe `computations/lepton_tower_bend_screening.py`.

Use the BEND before doing anything else on this bean:

    bend(x, w) = x(w+2)^2 / ( x(w) x(w+4) )

For m_w = C g^w f(w)^p, bend(m) = bend(f)^p -- C and g cancel EXACTLY, so
a candidate is screened by one number against one free exponent instead of
three free parameters. Target: bend(m) = m_mu^2/(m_e m_tau) = 12.295.
A viable parameter-free bridge needs bend 12.295 at p=1, 3.51 at p=2,
2.31 at p=3.

HARD-EXCLUDED (scope-(b), every C/g/p at once): any readout exactly
geometric in the winding, since bend = 1 there. That is one step, no
fine-tuning argument.

SCREENED OUT as implausible (a judgement, not a proof): every standard
parameter-free invariant of T(2,n). Best is genus / |signature| at
bend = 4/3, needing p = 8.72. net 667, tr_M 64.9, determinant and
crossing number 14.4, Alexander negative-and-large.

Also settled: the bend is BLIND to the Jones writhe prefactor (drift
1.8e-71), so no row of that table can be argued away by choosing a
different Jones normalisation.

NOT screened by this tool: an additive interface term is outside the class
m = C g^w f^p entirely. Still open, still worth attacking.

Reading: nothing on the lepton's OWN knot supplies the bend, which is
independent support for the linking/satellite route to 4_1 -- the mass
enters through a coupling to an object outside T(2,n).

