---
# qou-64jx
title: 'GAP: identify the 3.7e-4 branch splitting in the C1 q-Borel singularity'
status: todo
type: task
priority: high
created_at: 2026-08-07T08:45:08Z
updated_at: 2026-08-07T08:45:08Z
---

MEASUREMENT (no label attached — deliberately):
The level-1/2 q-Borel transform of the C1 solutions has finite radius
~ q^8.2526. Ratio-test limits converge to 10 digits WITHIN a branch but
differ BETWEEN branches by 3.7e-4.

The same 3.7e-4 scale has now shown up in three independent estimators:
  1. the step-2 ratio test
  2. the step-3 Prony blend
  3. step-4's C

Three independent estimators agreeing on a scale makes it a real feature,
not numerical noise. WHAT IT IS HAS NOT BEEN ESTABLISHED. Candidate
readings (none tested): the separation of the two q-Borel singularities;
a relative offset between the two sectors indexed by B_1,2 = ±sqrt(q-1)/q;
an artefact of the level-1/2 normalisation. Do NOT write any of these into
a witness description before measuring it.

PROCESS NOTE inherited from agent 4656, and the reason this bean is
phrased as a measurement: three times across steps 2-4 that agent wrote
the interpretation into the probe output BEFORE seeing the numbers, and
the data contradicted it each time ('ratios are NOT settling' -> they
settled to 10 digits; 'same singularity => module invariant' -> branches
disagreed; same again for C). Each was caught only because the number
happened to print next to the claim. Rule going forward: print the
measurement, derive the label afterwards.

Witness: computations/qbeta/c3-w2-c1-qborel-singularity.witness.json
