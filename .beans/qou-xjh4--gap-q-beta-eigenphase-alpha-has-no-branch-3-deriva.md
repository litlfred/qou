---
# qou-xjh4
title: 'GAP: q-Beta eigenphase alpha has no branch-3 derivation (KZ/Kohno-Drinfeld holonomy)'
status: todo
type: task
priority: normal
created_at: 2026-09-03T15:12:34Z
updated_at: 2026-09-03T15:13:08Z
---

THE GAP. The eigenphase `alpha = (z-1)h/2` on V_(2,1) of H_3(q) is asserted
nowhere and derived nowhere. `prop:q-beta-cos-resummation` now carries it as a
content-bearing class hypothesis (PR #6507) rather than the vacuous carrier it
had, but that is branch 2 of the trichotomy below and buys no evidence about
the substrate.

THE TRICHOTOMY, established in
content/quantum-observable-universe/lean/QOU/QBeta/EigenphaseCarrierVacuity.lean
(bean qou-cds1), not by me. Only one branch can be contentful:

  1. M in the braid image -- EXCLUDED. Every character lies in Z[q,q^-1] and
     2cos((z-1)h/2) is transcendental over Q(q,z), so no such M exists as a
     functional identity. Route-3 exclusion corroborated by QOU.QBeta.Seminormal
     and qbeta_eigenphase_seminormal_exclusion_probe.py.
  2. M arbitrary -- CIRCULAR. `circularWitness` in that file: the rotation
     exp(alpha*J) has trace 2cos(alpha) and det 1 for EVERY alpha, built from
     alpha itself. This is where the current encoding sits.
  3. M the holonomy of an independently-defined connection whose monodromy
     reproduces the Hecke braiding -- the only remaining option. Escapes (1)
     because a holonomy is transcendental, and (2) because the connection is
     defined without reference to alpha, which is then DERIVED as its holonomy
     angle rather than assumed.

WHAT BRANCH 3 IS. Kohno-Drinfeld / KZ. The corpus's canonical derivation chain
already invokes exactly this shape at the "Yekutieli non-abelian Stokes" step,
so the construction is not foreign to the framework -- it is a step the chain
names and this leg does not use.

NOT ATTEMPTED, by anyone. Neither EigenphaseCarrierVacuity nor #6507 carries it
out; both only establish that it is the only place a derivation can live.

CONVENTION SCOPE. This whole leg is convention-C-frame. `markovZC` in the
content block is z_C = sqrt(q)/(q+1), and the file's docstring records that it
CANNOT be migrated to D by swapping the body: the file's bar-antisymmetry
result needs z bar-even, z_C(1/q) = z_C(q) identically while z_D is neither
bar-even nor bar-odd. So a D-frame derivation is a re-derivation, not a
substitution. See also qou-cds1 (the c_k ladder is C-frame and unre-derived).

WHY IT MATTERS. This is the leg the Q_beta cos-resummation's empirical claim
rests on -- the 5.49x CODATA tightening (1677.5 -> 305.7 ppm) recorded in
q-beta-tightening-landscape.witness.json is evidence FOR the identification,
not a consequence of it. Without branch 3 the tightening is an unexplained
numerical fit.

FIRST HONEST STEP. Not a probe. Formalize-first: state what connection would
have to exist, and what its holonomy angle would have to be, before searching
for one. Per qbeta_ladder_required_phase_probe.py the required phase is pinned
to a window of half-width ~1.1e-5 rad and z_D sits ~1.19e-2 rad away, so under
D the FUNCTIONAL FORM has to change -- that is a constraint on branch 3, not
just on the value.
