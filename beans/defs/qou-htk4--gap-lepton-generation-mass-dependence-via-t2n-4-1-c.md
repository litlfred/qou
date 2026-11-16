---
# qou-htk4
title: 'GAP: lepton generation mass dependence via the T(2,n)-4_1 coupling. The multiplicative net(T(2,n)) bridge is EXCLUDED (docs/audits/2026-08-07-lepton-net-to-mass-bridge-exclusion.md, Lean morganVoyceBK_binet + mass_ratio_rigidity): net is log-linear in the winding, the observed tower is log-concave. Torus knots have Vol=0, and the corpus muon mass already comes from Vol(4_1) (the hyperbolic Higgs knot), so generation dependence should be sought in a linking/satellite quantity coupling T(2,n) to 4_1 -- something NOT multiplicative in a normal-form amplitude. Successor to qou-lsp9.'
status: in-progress
pr: 8185
type: task
priority: normal
tags:
    - 8f-mass
    - reorg-2026-10-04
created_at: 2026-08-07T17:40:00Z
updated_at: 2026-10-10T07:15:55Z
parent: qou-8lxd
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

## Additive direction CLOSED, 2026-08-08 — one shape left

`docs/audits/2026-08-08-lepton-additive-class-log-convexity.md`;
Lean `lepton_tower_log_convexity.lean`;
probe `computations/lepton_tower_additive_screening.py`.

The additive interface term -- the shape the bend screen explicitly could
NOT touch -- is now closed for POSITIVE modes, and by a sharper argument
than the multiplicative screen:

    x(w) = c g^w + d h^w,  c,d >= 0, g,h > 0
    x(w)x(w+4) - x(w+2)^2 = c d g^w h^w (g^2-h^2)^2 >= 0   =>  bend <= 1

Observed lepton bend is 12.295 (log-CONCAVE). A positive sum of geometric
modes is log-CONVEX. Strict inequality, no free parameter left -- unlike
the multiplicative screen, which ruled things out by how large an exponent
they needed.

Equality only in the degenerate single-mode limits (g = h, or a vanishing
coefficient). NOT monotone in the second coefficient: the bend dips to an
interior minimum (~0.967) and returns to 1 as d -> infinity. An earlier
draft claimed monotone worsening; that was wrong and is corrected.

NOT CLOSED, deliberately: (i) more than two modes -- the same Lagrange
identity symmetrises over pairs, not formalised; (ii) sign-indefinite
combinations.

## THE ONE SHAPE LEFT STANDING -- check this first on any new candidate

Sign-indefiniteness escapes ALL THREE exclusions, always via a NODE:

  * linear readouts of H_2(q): alpha, beta of opposite sign
  * multiplicative C g^w f^p: a readout with a zero has unbounded ratios
  * additive c g^w + d h^w: d < 0 breaks Cauchy-Schwarz; node at d = -q^(2w)

Everything closed so far was closed by POSITIVITY. Everything that survives
does so by having a zero in or near the generation window. So: before
building any new candidate bridge, check whether it has a node. That is the
only place the freedom to bend the tower has ever been found.

Open question this line has NOT touched: whether a node is physically
available -- i.e. whether the electron can sit near a genuine zero of the
underlying quantity. That is a strong, testable structural claim, not a
fitting knob, and it is the natural next target.

## Progress Update (Round 55 — PR #8185)
- [x] Formalized non-vacuous Lean 4 theorems (`0` `sorry`, `0` vacuity advisories across all 6 static audits) in `folio/quantum-observable-universe/lean/QOU/Eightfold/ColourConjugationGMODeviationAndAsymmetry.lean` and wired into `QOU.lean`.
- [x] Added 50-dps `mpmath` probe `computations/probes/colour_conjugation_gmo_deviation_and_asymmetry_probe.py` and 2-commit stamped witness `computations/probes/colour-conjugation-gmo-deviation-and-asymmetry.witness.json` (`scriptCommitSha: dc490df3193b70802e4608a98cc9402380f4dbcd`, `HEAD: ea791bb906663eb37105b3486abd6e07818699ed`).
- [x] Opened `litlfred/qou#8185` (status kept at `in-progress` per no-unilateral-closure policy).
