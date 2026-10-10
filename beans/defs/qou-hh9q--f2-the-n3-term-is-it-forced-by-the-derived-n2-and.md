---
# qou-hh9q
title: 'F2 the n=3 term: is it FORCED by the derived n=2 and n=4 anchors?'
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:37:40Z
updated_at: 2026-08-26T04:00:28Z
---

## Result 2026-08-26 — NOT FORCED, exactly one free parameter

Probe: computations/binding_n3_forcing_probe.py
Audit: docs/audits/2026-08-26-n3-body-order-forcing.md
Commits: ff57b4f843 (probe+audit), 675d86d95c (conjecture .md correction)

VERDICT: the n=3 body-order term is NOT forced by the two stated anchors.
Three unknowns (w_2,w_3,w_4) against two anchor equations = ONE free
parameter, and w_3 is a coordinate on it. Both anchors hold identically
along a one-parameter family whose A=3 prediction is unbounded, so A=3
cannot test the n=3 term -- it defines it. Count invariant under whether
the n=4 anchor is read as the 4He total or the n=4 term alone.

Positivity + monotone growth w_2<=w_3<=w_4 narrows the induced B(3H) to a
window 66-78% of the observable's magnitude. Data lands inside -- the one
non-circular check the anchors support, worth ~1 bit.

Anchor integrity (all three weaker than the conjecture stated):
 - rho_F=2 consumed as an input hypothesis (its own context block says so)
 - B_sym DERIVED* KVC-CONDITIONAL (Volume Conjecture)
 - corpus w_2=4.353 is B_AME(2H) inverted; derived bond gives 5.544 (+27.3%)

Third reading closed: displayed a_D^(n)(K) is K-dependent and WOULD force
n=3, but all ten a_D definitions in computations/ are a_D(n) returning
S(n)/n. No per-knot n=3 residue sum exists. "Forced but uncomputed" is not live.

multi-link emit is NOT the n=3 term: parameter-free and nearly closes A=3
(1.38/1.44 -> 1.06/1.07), but E_multilink(2H)=1.1678 MeV != 0 and a
body-order n=3 term is identically zero on a two-body system.

Coulomb computed not inherited: E_C(3He)=0.847422 MeV at the canonical
derived r0=hbar c/m_pi. At that geometry the correction OVERSHOOTS -- residual
CSB ~-1% with 3He more bound, not the +2.73% the 2026-07-11 audits quote.
Three-geometry spread 0.159 MeV, two orders below the w_3 window.

FOLLOW-UPS (not done here): (1) build a per-knot a_D^(n)(K) -- the honest
route to making n=3 a prediction; (2) mass_binding_dashboard.py:610-614
casts traces to float64 before a near-cancelling subtraction; (3) trace
multi-link emit's provenance against the B_vol deprecation precedent.
