---
# qou-xjh4
title: 'GAP: q-Beta eigenphase alpha has no branch-3 derivation (KZ/Kohno-Drinfeld holonomy)'
status: scrapped
type: task
priority: normal
created_at: 2026-09-03T15:12:34Z
updated_at: 2026-09-04T02:34:19Z
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

🛑 SCRAPPED 2026-09-04, the same day I opened it. THIS BEAN IS WRONG, and the
error is mine.

WHAT IT CLAIMED: that branch 3 (KZ / Kohno-Drinfeld holonomy) is "the only
remaining option" for deriving alpha, and "NOT attempted, by anyone".

WHAT IS TRUE: the Kohno-Drinfeld form is EXCLUDED, and was already excluded four
days before I wrote this. QOU/QBeta/HolonomySpectrumSignObstruction.lean landed
2026-08-31 (4471ee72ce, 6 theorems, sorry-free), with a 6/6 probe and the audit
docs/audits/2026-08-31-qbeta-holonomy-spectrum-sign-obstruction.md. It excludes
EVERY holonomy whose generator has real spectrum:

  - residue-independent step: a real generator eigenvalue a gives character
    (e^a + e^-a)/2 = cosh a >= 1 for EVERY real a, so a q-dependent residue only
    changes which a occurs.
  - the required correction factor is 0.998399, BELOW 1 -- wrong side, not merely
    off.
  - at the KD value itself, matching P exp(h t/2) to the Hecke eigenvalues
    {q, -q^-1} forces hbar = 2 ln q; q0 > 1 is real, so the generator is
    HYPERBOLIC (det A = -(ln q0)^2 < 0) and gives 1.005448.
  - the whole obstruction is (x-1)^2 >= 0. No analysis, no transcendence.

WHAT ACTUALLY SURVIVES, and it is owned elsewhere: not "find a connection" but
"find one whose generator is ELLIPTIC at real q" -- det A > 0, spectrum +-i*theta,
theta = 0.0565947 -- so the imaginarity is the thing that has to be sourced, and
the corpus names conj:im-q-physical-role as the candidate. Recorded as tier-0
condition D0 on the D1-D6 acceptance test. LIVE TRACKERS: qou-pdix and qou-cds1.
Do not re-open this bean; work those.

SCOPE, as the audit states it: it does NOT show no connection exists, does NOT
derive alpha, and adjudicates no convention.

HOW I GOT IT WRONG -- the mechanism, which is the reusable part. I read
EigenphaseCarrierVacuity.lean's §3 trichotomy, which says branch 3 is "the only
one that could be contentful", and treated it as authoritative. That file was
written BEFORE the obstruction landed and was never updated. I then propagated
"branch 3 is where a derivation must live" into THREE further places in PR #6507
(the content block's Lean docstring, its .ts authorNote, and the vacuity review
ledger) before opening this bean as a fourth.

I did not run the corpus-grep checklist. Paths 1-4 find the obstruction
IMMEDIATELY -- docs/audits/, content/ (the .lean itself), computations/ (probe +
witness) and docs/coordination/ all hit on "kohno|knizhnik|zamolodchikov". The
checklist exists for exactly this and I skipped it because a sibling file sounded
definitive.

AGENTS.md already records the general form of this ("a sibling's bean is not a
primary source"); this is the same trap one file over -- a sibling's LEAN FILE is
not a primary source either. All four propagated sites are corrected in the
follow-up branch.
