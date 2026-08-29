---
# qou-x4zl
title: 'GAP(3quc): prove normalizedSum n q = 1 (fake-degree/[n]_q! identity) general n'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T07:27:01Z
updated_at: 2026-08-29T08:23:42Z
---

PROGRESS 2026-08-29: found a THIRD route to normalizedSum n q = 1, more elementary than the two named (coinvariant-algebra Poincare / maj-q-RSK). INDUCTION on n reduces the whole forall-n gap to a SINGLE one-step recursion normalizedSum(n+1)=normalizedSum(n) (R). Lean: QOU.MathlibExt.MolienFakeDegreeInduction (normalizedSum_eq_one_of_recursion + molienSum_eq_qFactorial_of_recursion), sorry-free, lean-direct EXIT 0 -- the induction skeleton + conditional main theorem. (R) follows from (A) SYT branching f^lam=Sum_{mu-corner} f^mu [corpus infra: SYTBranchingBijection, YoungDiagramAddCell.cornerAddEquiv, SYTBranching2Row.dimHLF_branching_pair] + (B) the ADDABLE-BOX HOOK IDENTITY Sum_{b addable to mu} q^-c(b) qDim(mu+b)/qDim(mu) = [|mu|+1]_q. (B) verified EXACT for all mu |mu|<=6 (fake_degree_addable_box_recursion_probe.py, 3/3). (B) needs NO coinvariant algebra, no maj, no q-RSK -- c(b) is a q-Jucys-Murphy content (QJucysMurphyEigen the natural tool). RESIDUAL: prove (B) in Lean + wire (A) into the reindexing over Nat.Partition (addable/removable box correspondence via cornerAddEquiv). Sharpened from multi-week-opaque to one bounded verified q-hook lemma.

2026-08-29: the (B)/induction route is now an INDEPENDENT SECOND PROOF, not the path -- normalizedSum=1 closes via the corpus general-X telescope at X=0 (qou-3quc note, fake_degree_via_telescope_probe.py). (B) no longer needs to be driven to close the gap.
