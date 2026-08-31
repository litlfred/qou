---
doc_id: arxiv-2007.13108v1
doc_title: "Log concavity and concentration of Lipschitz functions on the Boolean hypercube"
section_id: sec-001-11-a-lower-bound-on-the-entropy
section_title: "A lower bound on the entropy"
section_number: 1.1
pages: 3-3
source_pdf: 2007.13108v1.pdf
source_sha256: b298478f5f5b948d
---
Our second result addresses the question of ﬁnding conditio ns under which the entropy of the
measure ν is close to that of the corresponding product measure, havin g the same marginals as
ν. This result is inspired by a corresponding bound due to Anar i, Oveis-Gharan and Vinzant [3,
Theorem 5.2], see the discussion below.
Given a measure ν on Cn, we deﬁne,
H(ν) :=
∫
Cn
log 1
ν({y})dν(y),
the entropy of ν. Moreover, for all i let πi(ν) be the marginal of ν onto the i-th coordinate, and
deﬁne
˜H(ν) :=
∑
i∈[n]
H(πi(ν)).
A well-known fact is that H(ν) ≤ ˜H(ν). We show that under a log-concavity-type condition,
this inequality can be reversed.
Theorem 5. Let ν be a probability measure on Cn. Suppose that, for some β ≥ 1, ν satisﬁes
the condition
∇2L[ν](x) ≼ β diag
(
∇2L[ν](x)
)
, ∀x ∈ Rn. (5)
Then one has
˜H(ν) ≤ β H(ν).
Remark 6. Condition (5) is stronger than condition (2). Indeed, it is n ot hard to check that
diag (∇2L[ν](x)) ≼ In (see formula (8) below).
