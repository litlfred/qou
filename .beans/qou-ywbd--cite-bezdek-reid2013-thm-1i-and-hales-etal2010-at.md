---
# qou-ywbd
title: Cite [bezdek-reid2013] Thm 1(i) and [hales-etal2010] at rem:bk-coordination-multiplicity / prop:coordination-saturation — the close-packing coordination bound is unsourced
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T13:41:14Z
updated_at: 2026-09-07T06:41:23Z
parent: qou-2akx
---

Source: triage of the 2026-09-06 uploads (docs/audits/2026-09-06-uploads-triage-eight-documents.md; ledger rows library/arxiv-1210.5756v1 and library/arxiv-0902.0350v1).

WHAT. rem:bk-coordination-multiplicity (content/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md, lines 83-86: 'the coordination number saturates to a geometric close-packing count') and the Lean prop:coordination-saturation (QOU/Mass/CoordinationSaturation.lean: bounded degree k, 'the close-packing / fcc picture') appeal to Euclidean sphere-packing geometry with NO held source — docs/audits/2026-09-05-max-contact-sub-affine-negative.md §5 recorded 'references.ts has no packing entry' and deliberately did not cite the sharp forms. Both sources are now held and registered in references.ts:
- [bezdek-reid2013] Theorem 1(i) (p. 2, proof §2): touching pairs in any packing of n unit balls in E^3 < 6n − 0.926 n^{2/3}; (ii) lattice < 6n − 3.665 n^{2/3}; fcc lower bound > 6n − 7.862 n^{2/3} (n = (2k^3+k)/3). Theorem 2: triplets ≤ 25n/3, quadruples ≤ 11n/4. This is the affine (12·n/2) + sub-affine (n^{2/3} surface) shape the saturation lemma and 2026-09-05-coordination-surface-deficit.md assume.
- [hales-etal2010] Introduction p. 2: the Kepler theorem statement (fcc density maximal); the paper itself proves no contact bound.

DO. Add both keys to cites[] of bk-coordination-multiplicity.ts and cite them in the .md sentence quoted above (one clause: 'the close-packing count is bounded by the kissing number 12 with an n^{2/3} surface deficit [bezdek-reid2013, Thm 1]'); add a '-- Ref: [bezdek-reid2013] Thm 1(i)' line to the CoordinationSaturation.lean module docstring where it names the fcc picture. Render-QA the .md (math-bearing) and refresh the sidecar.

DO NOT. Do not read this as resolving the four recorded objections to the geometric import (2026-09-05-max-contact-sub-affine-negative.md §5: qou-rav3 demands an internal derivation; ambient geometry is hyperbolic, costing 2.64x; three-dimensionality is derived nowhere; the exponent is imported). A citation makes the import citable, not derived. qou-brng is unchanged. Optional follow-up worth a separate bean if wanted: a compute-check comparing the surface-deficit coefficient the corpus computes for fcc facets against the Bezdek–Reid bracket [0.926, 7.862] on the n^{2/3} coefficient.



Claimed 2026-09-07 (session cite-wiring, branch claude/cite-wiring-6962-ids-2026-09-07) after #6962 (the ids) and #6964 (candidates + locators) merged. Scope extended per #6964's follow-up list: also [martelli2016] Thm 13.1.3 at the Λ-form Vol(4_1) site in alg:mba-step09a-mass-identity, and [bezdek-reid2013] at the kissing-number-12 mentions in MaxContactSimplex.lean / MaxContactHasBulk.lean.



PR #6999 (draft) carries the wiring: rem:bk-coordination-multiplicity + alg:mass-identity cites[] and .md clauses, -- Ref: lines in CoordinationSaturation / MaxContactSimplex / MaxContactHasBulk. Both sidecars refreshed; two Mathlib-only Lean files lean-direct exit 0; MaxContactHasBulk awaiting the QOU library sweep (its dependency olean is absent from the restored cache).
