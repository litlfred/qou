---
# qou-ukqh
title: 'GAP: categorical Higgs mechanism — Goldstone-eating linking, post-breaking Markov traces and the E_x·mu_0 scale are not derived (CategoricalHiggsMechanism has no instance)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - lean
    - gap
    - 8f-ew
created_at: 2026-09-03T09:08:31Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
---

Class B gap (SM-surface Lean sweep, bean qou-08zf, 2026-09-03). mass-theory/categorical-higgs-mechanism.lean now carries a content-bearing DEPENDENT conjecture class (instance binder [WeinbergAngleCategorical …] is the §3b-tax dependency edge): q_generic, MassEigenstateCountThree lk (exactly three bosons with lk = 1, photon lk = 0, over an explicit EWBoson type), CategoricalMassFormula trM e β scale m (m_X = scale · tr_M(e_X β_X e_X)), photon_massless. The consequences linked_iff_ne_photon_of_higgs and photon_projected_trace_eq_zero are derived. The old mkSkeleton (an inhabitant built from trivial and global instances) is removed.

OPEN (Steps A–D of the .md): construct the post-breaking 2-component links from the pre-breaking 1-component knots plus the Higgs doublet, compute their linking numbers and Hoefsmit-projected Markov traces, and derive the scale E_× · μ₀. Tower status ORDER-ZERO-ONLY (one Hoefsmit projection per boson at fixed n).

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.
