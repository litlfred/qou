---
# qou-r3sw
title: GUT SU(5) is near-absent from content/ — decide whether to author it from baez-huerta2010
status: completed
type: task
priority: normal
created_at: 2026-08-25T18:48:29Z
updated_at: 2026-08-25T19:15:48Z
parent: qou-8lxd
---

Owner flagged 2026-08-25: 'we are maybe missing SU(5) in qou'. Measured: grand-unification SU(5) has ~3 hits in content/, all bibliographic (references.ts, bib-qa-verifications.json). The instinct is correct.

DO NOT use arxiv-1205.4617v1 for this. Triaged 2026-08-25 (docs/audits/2026-08-25-octonion-division-algebra-upload-triage.md): it is a relabelling of textbook Georgi-Glashow, physics.gen-ph, whose own culminating gauge field contains no octonions, and whose central map sends 8 su(3) generators onto 7 octonion imaginaries by reusing e_3.

USE baez-huerta2010 (arXiv:0904.1556), which is ALREADY ingested at library/arxiv-0904.1556v2/, registered in references.ts, claim-verified in the source ledger, analysed in docs/audits/2026-07-31-sm-lit-analysis-bean-workplan.md §3, and cited by 3 content blocks. It does SU(5) in Lambda C^5 with hypercharge from the grading.

WHY THIS MIGHT MATTER BEYOND COMPLETENESS: the eightfold chapter's §8 item 2 (hypercharge Y) is OPEN -- the writhe map is falsified since p and n share Y=+1 with different writhes, and the chapter needs a second crossing invariant. SU(5)'s Lambda C^5 grading is exactly a source of Y. Whether QOU can reach that grading is the open question; noting the adjacency, NOT claiming it works.

HAZARD: docs/audits/2026-08-16-su-r-level-tower-gap-map.md:46 has an SU(5) row that is the WENZL LEVEL r=5 (z_5 = q^5/[5]_q), unrelated to grand unification. Same glyph, different object.

## DONE 2026-08-25 (PR #5764) — and the first answer was WRONG

Owner asked the sharper question mid-session: 'where does SU(5) come from
categorically?' My first draft answered by importing Lambda C^5 from
Georgi-Glashow. That is not a categorical answer, it is a citation, and it is
the move the framework should not make.

THE ACTUAL ANSWER: SU(5) is already in the corpus, as level r=5 of the Wenzl
tower z_r = q^r/[r]_q. Its r=2 member IS the framework's canonical trace
parameter (z_D = q^3/(q^2+1)); its r=5 member is z_5 ~ 0.32275 at the anchor.
Row cap at level r is l(lambda) <= r, so the tower is a ladder: framework on
rung 2, flavour fundamental on rung 3, SU(5) on rung 5.

The rung fixes the parameter with NO FIT -- ocneanu_param_eq_of_fibre_qdim is
proved general in N: dim_q V = [N]_q forces z[N]_q = q^N. So a level-5 fibre
would carry z_5 as a consequence.

CONSEQUENCE: what is missing is not the object but a mechanism to CLIMB, which
is the flavour gap one rung further. Climbing cannot happen inside the fibre
(Sym2GateMultiplicity: any single-fibre object passing the gate has even
dimension). SU(5) is strictly DOWNSTREAM of an open gate and is no route around
it.

Authored rem:su5-hypercharge-n3-gate in the SM appendix. Kept the Lambda C^5
material as a secondary section for one surviving observation: hypercharge there
is FORCED (alpha^2 beta^3 = 1 cuts U(1)xU(1) to one U(1); the grading fixes every
Y), so the corpus's 'missing hypercharge' and 'missing 3-dim fundamental' are ONE
gap rather than two.

CAVEAT CARRIED IN THE BLOCK: the two fives are not known to be the same five.
The tower fixes a row cap and a trace parameter, NOT a flavour-colour
decomposition. 'Both are 5' is flagged as the open question, not asserted.

NOT DONE, deliberately: no SU(5) derivation, because the framework cannot reach
it. arxiv-1205.4617v1 stays triaged not-relevant.
