---
# qou-m3ad
title: 'M3 reframed: the target is the INDEX SET (not a CoHA); H_Ad = adjoint-weight core, with the 5_2 remainder Lean-forced to 1'
status: in-progress
type: task
priority: high
tags:
    - g3-aomega
    - route-c
created_at: 2026-08-18T21:00:00Z
updated_at: 2026-08-18T21:00:00Z
parent: qou-rtec
---

## The reframing (the main contribution)

M2 showed the closed-sector BPS spectrum would be ABELIAN — every Borel ray distinct,
trivial Davison-Meinhardt plethystic log, dim BPS_d = |Omega_d|, all multiplicities 1.
CONSEQUENCE: a direct sum of 1-dimensional spaces carries no information beyond WHICH
RAYS EXIST. So M3's real target is NOT "build a cohomological Hall algebra" (the
original Route C framing) but **derive the index set Omega**. That is a materially
sharper and more tractable goal, and it is what qou-rtec's M3 rung should now read.

## H_Ad — the hypothesis (NOT a derivation; do not upgrade without a proof)

The knot-INDEPENDENT core of the index set is the weight set of the ADJOINT rep of
sl_2: for meridian eigenvalues (m,1/m) and x=m^2, Ad has eigenvalues (x,1,1/x), so
chi_Ad(x) = x + 1 + 1/x = s(x) exactly and chi_Ad(1) = 3 = dim sl_2.

MECHANISM (why not numerology): in complex Chern-Simons the Borel singularities are
differences of complex volumes of flat connections, and the deformation theory of a
flat connection is governed by H^1(M, Ad rho) — the adjoint local system is the
CANONICAL coefficient object, not a chosen one. In QOU terms Ad = Sym^2 V = the
partition-(2) Wedderburn block of H_2(q), so it is expressible in Hecke language.

## What was tested (probe: computations/probes/aomega_m3_adjoint_index_set.py, 4/4)

 T1 chi_Ad reproduces M2's s(x) exactly — exponents AND multiplicities, no free parameter.
 T2 H_Ad PREDICTS knot-independence; observed (same s(x) governs 5_2, GGM 239/277/307).
    This is the fact that defeated every knot-specific reading (Driver14's eight + R1).
 T3 ADVERSARIAL: H_Ad FAILS as a scalar — knot-independent gives (3,3) vs certified
    (3,4), exactly like blockCountH3. So its content is the GRADING, not the count.
    Recorded so H_Ad cannot be mis-sold as a counting answer.
 T4 ADVERSARIAL: the 3-element palindromic SHAPE is generic ({a,0,-a} for any a), so
    the shape proves nothing; H_Ad rests entirely on its mechanism + the a=1
    normalization forced by x=m^2.

## Lean (QOU/QBeta/AdjointIndexSetM3.lean, core Int, lean-direct exit 0, sorry-free)

 adjoint_multiplicity_free / adjoint_dim_three / adjoint_palindromic / s_at_one_eq_three
 knot_independent_core_forces_unit_remainder  <- THE LOAD-BEARING ONE: any
     knot-independent core forces a knot-DEPENDENT remainder differing by exactly 1.
 adjoint_core_pins_remainder  -> under H_Ad the remainder is pinned to (0, 1).
 no_purely_knot_independent_count -> H_Ad alone is PROVABLY incomplete (derived, not
     conceded).

This converts the otherwise-unfalsifiable move "add one more state for 5_2" into a
structural requirement with a definite value.

## NEXT STEP (the open piece)

Derive the single extra 5_2 ray independently. Candidate (NOT verified): 5_2 has 4
boundary-parabolic flat connections vs 4_1's 3, so the extra ray would be the
additional geometric connection. If that lands, H_Ad + that = the full index set, and
M3 becomes a derivation rather than a hypothesis. Until then: HYPOTHESIS ONLY, and no
derivation of the DT spectrum from Hecke data is claimed.
