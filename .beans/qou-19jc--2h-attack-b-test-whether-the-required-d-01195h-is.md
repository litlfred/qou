---
# qou-19jc
title: '2H ATTACK B: test whether the required d = -0.1195h is the sigma^2 stacked crossing or another Hecke-admissible element, NOT a free parameter'
status: todo
type: task
priority: normal
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-08-25T18:39:30Z
parent: qou-9ot5
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
