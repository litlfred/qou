---
# qou-19jc
title: '2H ATTACK B: test whether the required d = -0.1195h is the sigma^2 stacked crossing or another Hecke-admissible element, NOT a free parameter'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-10-04T15:16:02Z
parent: qou-10v9
---

## MEASURED 2026-08-25 (PR #5765) — NEGATIVE, and it redirects the attack

Tested the required deuteron interface offset against a **pre-specified** list of
Hecke-admissible elements `a·σ + b·I` (μ = a·z + b under Markov). Pre-specified, so
this is a test and not a search. Convention D, proton pin, 50 dps.

    REQUIRED mu = 0.58771506411074    (d/h = -0.11945345)

    element                          mu             d/h        vs required
    sigma                            0.6126880371    0.0          4.249%
    sigma^-1 = sigma - h             0.4036277384   -1.0         31.323%
    sigma^2 = h.sigma + 1            1.128088744     2.465321    91.945%
    sigma^-2                         0.9156174644    1.449005    55.793%
    I                                1.0             1.852633    70.150%
    P+ = (sigma+1/q)/(q+1/q)         0.7527021133    0.6697306   28.073%
    P- = (q-sigma)/(q+1/q)           0.2472978867   -1.747774    57.922%
    (sigma+sigma^-1)/2  [= derived]  0.5081578877   -0.5         13.537%
    q*P+ - (1/q)*P-                  0.6126880371    0.0          4.249%

**No pre-specified element lands on it.** Closest is bare `σ` at 4.25 %, which is the
`d = 0` endpoint, not a candidate for a p-n bond.

### Why this is the useful result rather than a dead end

The framework's **derived** choice IS a principled element — `(σ + σ⁻¹)/2`, the uniform
bar-invariant projection, `d/h = -0.5`. It is 13.5 % wrong in μ (27 % in B). The
**required** value `d/h = -0.11945` corresponds to **nothing** on the list and sits
between two elements.

So the situation is not "the right element has not been found yet". It is:

- a principled element gives the wrong number, and
- the right number is not a principled element.

Tuning `d` to reach it is therefore **pure fitting** with no candidate to point at — and
`content_keyed_interface_refuted` independently says no content-keyed assignment can
work, because the two `pn` channels (3S1 bound, 1S0 virtual) share nucleon content.

**This redirects to ATTACK C (`qou-d5e8`): the defect is more likely in the FUNCTIONAL
FORM than in the element.** `qou-kj4v` already argues this from the other side — the
exact flavour-only degeneracy `mu(3S1) = mu(1S0) = 0.18614164195799085217` means no
flavour-only μ can split the channels whatever the functional, so `B = -α·ln(μ)` over a
single interface scalar is the thing under suspicion, not the choice of scalar.

### Scope
Scope **(a)**: a negative over a finite pre-specified list at this q₀ under convention D.
It does **not** exclude every Hecke-admissible element — the list is 10 entries, not the
algebra — and a genuinely-derived element from a space-indexed construction
(`qou-vbyi`) would be a new candidate, not one of these. Do not cite this as a
structural exclusion.


## 2026-08-31 (PR #6320) — colour weighting priced (0.097% of the gap), and the once-only condition PROVED

**ATTACK B's table predates R3.** Its "derived" row `(sigma+sigma^-1)/2`, d/h = -0.5,
is the COLOUR-BLIND interface. Owner ruling R3 (2026-08-15) makes
`bring_color_weighted` canonical, and that arm had never been evaluated here.
Now measured (proton pin, 50 dps, B = -alpha ln mu, alpha = 4.185981 MeV):

    interface                        mu                    B / MeV    err
    colour-BLIND    d = -h/2         0.50815788774864559   2.8337548  +27.385%
    colour-WEIGHTED d = -h(1/2-d/4)  0.50822978937673896   2.8331626  +27.358%
    required (inverted from AME)     0.58776247263801610   2.224566    0

    shortfall 0.6091888 MeV; weighting moves B by -0.0005923 MeV
    => it closes 0.0972% of the gap.

So "is the missing 27% the colour weighting?" is answered NO, by three orders of
magnitude. That question is now closed rather than open.

**Bookkeeping note:** this bean's quoted `REQUIRED mu = 0.58771506411074` differs
from a self-consistent inversion of B = 2.224566 by 4.741e-5 (absolute, in mu).
The colour-weighting shift is 7.190e-5 — the SAME ORDER, 1.52x larger. Neither
affects the 13.5% conclusion; recorded so nobody reads more precision into the
quoted value than it carries.

## The identity behind the table is ALREADY PROVED — and now so is its side condition

`QOU.QBeta.InterfaceScalar.interface_scalar` proves
`tr(W(a.sigma + b.1)) = (a z + b) tr W`, which generates this bean's whole table
(all 5 rows reproduced from `mu = a*z_D + b`). Its premise — Markov stabilisation
— is carried there as a HYPOTHESIS standing in for Jones (1987).

PR #6320 proves when that premise may be invoked (all sorry-free, lean-direct
exit 0, no sorryAx):

  markov_repeat_forces_quadratic        z^2 = h z + 1 if stabilisation is
                                        assumed at W = sigma.  AXIOM-FREE.
  conventionD_markov_defect             z^2 - h z - 1
                                          = -(q^2-q+1)(q^2+q+1)/(q^2+1)^2
  conventionD_markov_defect_neg         < 0 for EVERY q > 0
  markov_stabilisation_fails_on_repeat  so the premise fails on a repeated
                                        interface generator

Scope-(b), invariant cited (both factors are (q +- 1/2)^2 + 3/4). The interface
scalar is available exactly when the interface generator occurs ONCE — true of
every canonical light nucleus (D/T at gen 2, 3He/4He at gen 5).

Wired: paper `prop:markov-stabilisation-needs-a-fresh-generator`
(nuclear-interactions, validate exit 0); compute
`markov_repeat_defect_lean_guard_probe.py` (4/4, symbolic difference exactly 0).

**This bean's redirect to ATTACK C stands.** Nothing here rescues the element
search; it prices one candidate out and pins the side condition of the collapse.

## Round 69 Update (PR #8249)
- Formalized in `ToffoliDimensionMismatchHeckeOffsetHypernuclearRatioNielsenThurstonAndNolenSchiffer.lean` and verified via 80-dps `mpmath` witness in PR #8249.
