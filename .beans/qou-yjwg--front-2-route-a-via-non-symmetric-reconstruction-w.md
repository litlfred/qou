---
# qou-yjwg
title: 'Front 2: Route A via non-symmetric reconstruction — what is the Lentner-Mombelli Hopf algebra of a QOU'
status: todo
type: task
created_at: 2026-09-03T04:37:53Z
updated_at: 2026-09-03T04:37:53Z
parent: qou-icj2
---


## RESULT 2026-09-03 (PR #6458) — the T3g question is answered YES, and it is the wrong question

Audit: docs/audits/2026-09-03-fibre-functors-do-not-change-the-category.md
Lean:  QOU/Eightfold/FibreFunctorDimensionNotCategorical.lean (12 decls, sorry-free)
Probe: computations/probes/fibre_functor_dimension_not_categorical_probe.py (exact)

- The 2026-08-25 re-posing ("what is the Lentner-Mombelli Hopf algebra in C?")
  applied the reconstruction for a braided TARGET. QOU's tau lands in R-Mod
  (symmetric), so the classical braided-SOURCE reconstruction applies, and the
  corpus already ran it: ex:tannaka-krein-su2 gives H = O_q(SU(2)).
- Fibre functors on Rep(SL_q(2)) are CLASSIFIED (Bichon 2003, B(E) for
  tr(E^-1 E^t) = -q - 1/q; Etingof-Ostrik 2004). They exist at every n >= 2 and
  are real at q0 (n = 3: b = -2.6308 or -0.3801, exact roots in the probe).
- They change dim tau'(V) and NOTHING else: V^{x3} = 21 + 3 + 3 at n = 3, never
  10 + 8 + 8 + 1. The singlet is absent from V^{x3} by Clebsch-Gordan parity
  (Lean: zero_not_mem_cgSpins_three, no_one_dimensional_summand_of_cube).
- Scope-(b) exclusion of the fibre-functor route; invariant = CG parity. NOT an
  exclusion of the eightfold way: the missing object is in the CATEGORY
  (Lambda^3 W != 0), which axiom 5 forbids for the fundamental.
- Bib: bichon2003, etingof-ostrik2004 added UNVERIFIED (egress blocked).
Status: this bean's question is closed; the honest successor is an owner-level
question about axiom 5 / a second fundamental, not a fibre-functor search.
