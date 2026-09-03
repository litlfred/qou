---
# qou-c35w
title: 'Wire canonicalInstance to the Markov-derived n=3 weights + credit-sweep: 3y was prior art'
status: completed
type: task
priority: normal
created_at: 2026-09-03T09:09:28Z
updated_at: 2026-09-03T12:47:22Z
parent: qou-59vq
---

## Corpus-grep verdict for 3y ("push the sl2 family into the mass channel")
CLOSED BY PRIOR ART, all sorry-free, all general n, all in Lean since 2026-08-16..24:
- QOU/MassTheory/TwoRowCapDerived.lean (#5242): traceSum_eq_twoRow_of_wenzl, twoRow_share_eq_one_of_wenzl (chi free — so "does chi_lambda cooperate" is moot; the drop is in the weight).
- QOU/QBeta/WenzlWeightVanishing.lean: wenzlLevel_conventionD, level_eq_two_of_conventionD (D = Wenzl level r=2).
- QOU/SchurWeyl/OcneanuWeight.lean (#5575): general-n Ocneanu cell product, z_D row cap, "z_D is the k=2 member of z = q^{2k+1}/(1+...+q^{2k}); C in no member".
- QOU/SchurWeyl/OcneanuWeightWenzl.lean: ocneanuWeight q z_D mu = schurPrincipal 2 (q^2) mu / (q^2+1)^{|mu|} — THE bridge I was about to write.
- QOU/SchurWeyl/WenzlWeightLevelR.lean: wenzlWeight r Q, wenzlMarkovParam (= my z_N family in Hecke normalisation).
- QOU/SchurWeyl/MarkovTraceInstance.lean: ocneanuWeight at D IS the Markov trace.

## Self-correction owed (mine)
#6370 ("D is the sl_2 point of the Ocneanu family z_N = q^N/[N]_q; C off the family") and #6440 ("canonical inhabitant derived from the Ocneanu product") re-derived the above and credited none of it. Sweep: markov-z-reconciliation.md (lines ~96-102), ocneanu_weights_are_sl_n_quantum_dimensions.py docstring, toffoli-lp-stability.lean markovZAt/ocneanu_numerator_collapse docstrings, explicit-instance-proof.md canonical section, comments on #6370/#6440, qou-dwf4.

## The one non-duplicative deliverable
Wire today's CanonicalMarkovWeightsH3.canonicalInstance (canonical_y3/y21/0) to the corpus's Markov-DERIVED n=3 weights (HeckeMarkov3.markovWeight0/1/2 at z_D, equivalently ocneanuWeight q z_D on the three partitions of 3), so the class inhabitant is proved equal to the derived object rather than checked against a probe.



PR #6494 (draft) on claude/ocneanu-schur-bridge-2026-09-03: f06c00e315 (Lean wiring), 59cdc3060f (credit sweep), 621a3c2437 (chore). Comments posted on #6370 / #6440.



LANDED on main via REST landing PR #6506 (rebase-merge, tip ff9d0e85d0); #6494 superseded.
