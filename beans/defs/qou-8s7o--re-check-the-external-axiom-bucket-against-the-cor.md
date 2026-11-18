---
# qou-8s7o
title: Re-check the External axiom bucket against the corpus, not against docstrings (57 entries)
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T01:10:32Z
updated_at: 2026-11-18T11:34:19Z
parent: qou-6qbv
---

Generalization of qou-mame (PR #5807).

docs/audits/2026-06-03-lean-axiom-tractability-triage.md sorts 58 axioms into an 'External / cited / deep' bucket described as 'not a feasible session-scale goal'. That bucket was populated by READING EACH AXIOM'S OWN DOCSTRING.

One entry has now been checked against the corpus instead: lobachevsky_pi_div_four_eq_half_catalan, an 'External transcendental identity', proved sorry-free in ~20 lines using QOU.Knot.clausen_eq_series which was already in the tree. Its docstring's claim ('needs Mathlib's full polylogarithm machinery ... none of which is currently upstream') was false in both halves and had survived at least two revisits.

Sample of 1, so the base rate is unknown -- but the SELECTION was not adversarial (it was picked because a user directive pointed at it), which is weak evidence the bucket is not uniformly correct.

Method that worked, for whoever takes this:
1. For each axiom, extract the mathematical ingredients its docstring names as missing.
2. grep the corpus for each: content/**/*.lean (QOU/MathlibExt/ is a 54-file Mathlib-gap staging area), then the .lake mathlib OLEANS by symbol name (strings -n 6 on the .olean; the SOURCE tree is not present in a restored container, only oleans).
3. Never conclude 'absent' from one import cone. That is the error this bean exists to catch.

AUDIT DONE 2026-08-26. Deliverable: docs/audits/2026-08-26-live-axiom-surface-recheck.md, PR #5811.

Findings:
1. Bucket stale: triage doc says 77 axioms / 58 External; live tree has 23 TOTAL. The '57 remaining' figure in this bean's original body was wrong and is corrected in the doc + triage headline.
2. Corpus-grep of all 23: only 2 same-stem hits, both in the SDP ladder, both downstream of the axiom they shadow (import cycle blocks in-place replacement). Measured by proof term, swapping trades 1 axiom for 2 -- SDPRankEquality's 'replaces the dependency' is a DECOMPOSITION, not a reduction. Nothing imports SDPRankEquality.
3. Reclassification: 11/23 co-located with 'opaque'. MarkovTrace_cyclic / markovTrace_linear assert properties of an OPAQUE symbol -> unprovable by construction, not a Mathlib gap. Corpus has TWO markovTrace's (opaque IwahoriHecke/MarkovTrace.lean:77, concrete def MathlibExt/MarkovTrace.lean:117) with nothing bridging them -- same hazard shape as catalan_G vs Cl_2. That bridge is the real open question behind the Hecke cluster.
4. THE INSTRUMENT WAS UNSOUND. #print axioms reads oleans, which are mixed-vintage (2026-06-09..08-26). Both SDP cones reported entry_sq_le_diag_mul_axiom, which does not exist in source (PosSemidefDiagZero proves it as a theorem; its olean is from Jun 9). Rebuilding that module removed the phantom. Fix: scripts/lean-rebuild-cone.py --from-guard (15 roots -> 199 modules, lean-direct not lake build).
5. Three measurement artifacts recorded: shallow-clone boundary (all 2207 files 'new'), rebase-merge flattening defeating --no-merges, clone-time mtime (845/1046 'stale' = exactly the restored set).

NOT done: full Mathlib-side symbol search for each of the 23 (only spot-checked). Left open.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 84 (`lane-e667`): Formalized `qou-2u26`, `qou-42ls`, `qou-5po6`, `qou-8s7o`, `qou-aqyf` in `QOU.Foundations.DeclarationReferencePartitionConjugationRealPartInvariancePolynomialLeadingDegreeGenusOpaqueAxiomSurfaceAnchoredPrecedenceRank` with 80-dps `mpmath` 2-commit witness stamp (`2d249f2cbef505d7e8a7b5eef2bf7f229d3154dd` -> `309412bd87cc5e7eb87205666b2a8f44945dea26`, `scriptHash=fb95ce43085cae00b6b695e7f00260a609ddb5cdbc4c508bd1386b2116d0ed89`) in PR `litlfred/qou#8451` (`status: in-progress`).
