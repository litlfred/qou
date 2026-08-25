---
# qou-ap47
title: 'V7: are states GS normal forms or Markov classes? -- decides every state function'
status: completed
type: task
priority: normal
created_at: 2026-08-10T18:57:48Z
updated_at: 2026-08-15T22:31:26Z
---

THE PIVOTAL QUESTION, surfaced by refuting L = sign(writhe).
Markov II sends beta -> beta*sigma_n with the SAME link closure and raises the
writhe by 1. So ANY state function built from the writhe is ill-defined on
Markov classes. Proved: leptonNumber_not_markov_invariant (baryon L: 0 -> 1).
But lepton-number-categorical-properties.md conservation clause 3 asserts
Delta L = 0 under Markov moves.
Meanwhile mba-step02-gs-reduction.md says 'the reducer is the SINGLE SOURCE of
Hecke normal forms; every downstream algorithm consumes NF(w), not the raw
braid. Treating the normal form as the canonical object.'
So the corpus appears to use GS normal forms as states -- in which case Markov
moves do NOT act within the state space, writhe IS well-defined, and clause 3 is
about a different object. RESOLVE THIS: it decides whether ANY writhe-derived
quantity (L, I_3 = w/2, Q = w/2!) is a state function. Note Q and I_3 are
ALREADY wired to production and have the same exposure.


RESOLVED 2026-08-11 via PR #4961 (merged, rebase). Owner ruled reading 1: GS
normal forms ARE the states, and the observable is the trace on the LOWEST part
of the substrate tower -- a canonical SECTION of the vertical move, not a
quotient. Lean landed sorry-free in WritheMarkovInvariance.lean (writhe_conj,
writhe_stabilize, writhe_stabilize_neg, coulombCharge_not_stabilization_invariant).
Bean was left at 'todo' after the merge; closed here on the reorientation pass.
