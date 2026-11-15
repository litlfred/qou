---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-007-5-relation-to-operator-space-entanglement-entrop
section_title: "Relation to operator space entanglement entropy"
section_number: 5
pages: 9-9
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
ment entropy
Next, we discuss the connection between the rα-
negativity and the operator space entanglement
entropy (OSEE) [86]. For a mixed state ρ, the
operator Schmidt decomposition with respect to
the bipartition A and B is given by [120]
ρ
q
tr(ρ2
A)
=
X
i
q
λO
i OA,i ⊗OB,i ,
(44)
where λO
i
are the operator Schmidt coefficients
and {OA,i} and {OB,i} are a set of orthonormal
operators in the subsystem A and B, respectively.
The operator Schmidt decomposition can be ob-
tained by vectorizing the (normalized) operator
|ρ⟩=
ρ
√
tr(ρ2
A) and performing the Schmidt de-
composition for pure states on |ρ⟩. The R´enyi
OSEE is given by [86]
SO
α (ρ) =
1
1 −α ln
 X
i
(λO
i )α
!
.
(45)
A state ρ has zero OSEE iff it can be written
as a product state in the form of ρ = ρA ⊗ρB.
The OSEE quantifies the representability of the
state |ρ⟩as a matrix product state, since it plays
a similar role as the entanglement R´enyi entropy
for pure states [95].
Therefore, while OSEE is
not a good measure of mixed-state entanglement
(since separable mixed states can have non-zero
OSEE), it has a direct relevance to the simula-
bility of a mixed state using the well-established
tools of matrix product states [29], originally de-
veloped for simulation of pure states.
Furthermore, the OSEE can be directly related
to the CCNR negativity [88]. Indeed, one can see
that the operator Schmidt coefficients λi are sim-
ply the (rescaled) singular values of the realign-
ment matrix Rρ. Therefore, the R´enyi OSEE are
related to the realignment moments by
SO
α (ρ) =
1
1 −α ln(r2α) +
α
1 −αS2(ρ).
(46)
