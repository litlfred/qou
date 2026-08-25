---
# qou-43co
title: 'DEFECT: def:hecke-normal-form asserts confluence that QOU''s own Lean refutes at n=4'
status: todo
type: bug
priority: high
created_at: 2026-08-09T18:27:58Z
updated_at: 2026-08-09T18:27:58Z
---

`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md` says of
the three-rule system (Hecke relation, far commutativity, Yang-Baxter in the
shortlex-decreasing direction):

> This reduction is confluent, making the normal form independent of rule order.

That is exactly the system `heckeRewritingSystem` in
`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean`, and
`NotAGSBasis.hecke_not_gs_basis_four` in that file is a machine-checked
REFUTATION at n = 4: the overlap of the Yang-Baxter rule for (sigma_2, sigma_3)
(lm = s3 s2 s3) with the far-commutation rule for (sigma_3, sigma_1)
(lm = s3 s1) over the word s3 s2 s3 s1 has S-polynomial

    s2 s3 s2 s1 - s3 s2 s1 s3

and both words are irreducible for the system, so the S-polynomial is a nonzero
normal form and the system is not confluent. The Lean module header states this
outright and records that the axiom `hecke_is_gs_basis` was deleted for being
false, not merely unproved.

So the manuscript block asserts, uncited, precisely what the folio's own
sorry-free Lean disproves. Fix the block, do not just add a citation.

WHAT THE REPAIR NEEDS (all three sources agree on the shape):
- HeckeGS.lean:461 names the missing family itself:
  sigma_i sigma_{i-1} ... sigma_j sigma_i -> sigma_{i-1} sigma_i sigma_{i-1} ... sigma_j,
  of which s3 s2 s1 s3 -> s2 s3 s2 s1 is the first instance. That is the
  Bokut-Shiao completion, now citable as [bokut2001].
- [kimlee2018] Prop. 3.1 shows the same shape on the Temperley-Lieb quotient:
  the GS basis needs the two extra families E_{i,j}E_i - E_{i-2,j}E_i (i > j)
  and E_j E_{i,j} - E_j E_{i,j+2} (i > j) beyond the defining relations.
- The q-deformed type-A statement itself is Kang-Lee-Lee-Oh 2002 (see the
  sibling bean); [bokut2001] is a Coxeter-GROUP theorem and does not by itself
  license the H_n(q) claim.

Two acceptable outcomes: (a) restate the block over the COMPLETED rewriting
system and cite the completion; or (b) drop the confluence sentence and say the
normal form is defined by a fixed rule order, with a pointer to
`NotAGSBasis.hecke_not_gs_basis_four` for why order-independence fails. Either
way `def:hecke-normal-form` currently has no `cites` field at all and carries
the `groebner-shirshov` tag.

Surfaced by relevance triage of the nine-PDF batch (library/fd58d8e1...pdf and
library/arxiv-1808.05026v1/1808.05026v1.pdf); ledger rows carry the join.
