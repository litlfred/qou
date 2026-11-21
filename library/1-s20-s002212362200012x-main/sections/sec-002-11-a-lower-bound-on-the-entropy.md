---
doc_id: 1-s20-s002212362200012x-main
doc_title: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-002-11-a-lower-bound-on-the-entropy
section_title: "A lower bound on the entropy"
section_number: 1.1
pages: 4-4
source_pdf: 1-s2.0-S002212362200012X-main.pdf
source_sha256: 6fc7d28c8d40bf42
toc_source: outline
doc_brief: "Journal of Functional Analysis Log concavity and concentration of Lipschitz functions on the Boolean hypercube — V Article history: Received 17 December 2020 Accepted 13 January 2022 Available online"
---
Our second result addresses the question of ﬁnding conditions under which the entropy 
of the measure ν is close to that of the corresponding product measure, having the same 
marginals as ν. This result is inspired by a corresponding bound due to Anari, Oveis-
Gharan and Vinzant [3, Theorem 5.2], see the discussion below.
Given a measure ν on Cn, we deﬁne the entropy of ν by
H(ν) :=

Cn
log
1
ν({y})dν(y),
the entropy of ν. Moreover, for all i let πi(ν) be the marginal of ν onto the i-th coordinate, 
and deﬁne
˜H(ν) :=

i∈[n]
H(πi(ν)).
A well-known fact is that H(ν) ≤˜H(ν). We show that under a log-concavity-type con-
dition, this inequality can be reversed. For a square matrix A, deﬁne diag(A) to be the 
diagonal matrix whose diagonal entries coincide with those of A.
Theorem 6. Let ν be a probability measure on Cn. Suppose that, for some β ≥1, ν
satisﬁes the condition
∇2L[ν](x) ⪯βdiag

∇2L[ν](x)

,
∀x ∈Rn.
(5)
Then one has
˜H(ν) ≤βH(ν).
Remark 7. Condition (5) is stronger than condition (2). Indeed, it is not hard to check 
that diag

∇2L[ν](x)

⪯In (see formula (8) below).
