---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
toc_source: undetermined
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of symmet- ric groups."
---
2
PHILIPPE BIANE
in the theory of free probability, where it appears under the name of “free Poisson
distribution”. We shall also consider more general measures on Young diagrams
coming from tensor states on B(H)⊗q. By tuning the state with q we will get limit
diagrams which are related to freely inﬁnitely divisible measures.
This paper is organized as follows. In Section 1 we settle notations, recall results
from [B], and state the main result of the paper. In Section 2 we prove the result,
and in Section 3 we discuss the decomposition of the tensor representation.
1. Notations and statement of the main result
We recall notations from [B], to which we refer for more details.
1.1 Symmetric groups and Young diagrams. We denote by Sq the symmet-
ric group on {1, . . . , q}, by (ij) the transposition exchanging i and j, and more
generally by (i1i2 . . . in) cyclic permutations of order n. For σ ∈Sq, let c(σ) be
its number of cycles, and s(σ) be the number of elements not ﬁxed by σ. Then
|σ| := q −c(σ) is the smallest number n such that σ can be written as a product
of n transpositions. We denote by Yq the set of Young diagrams with q boxes,
and Y = ∪∞
q=1Yq. If λ ∈Yq let [λ] be the associated irreducible representation
of Sq, and χλ be its normalized character, i.e. χλ(e) = 1. Recall from [B], [K]
that a Young diagram can be identiﬁed with a piecewise linear function with slopes
±1, and local minima and maxima occuring at two interlacing sequences of integer
points
x1 < y1 < x2 < . . . < yn−1 < xn
as in the following example
x1
y1
x2
y2
x3
y3
x4
and that we can embed the set of Young diagrams in the space CY of continuous
Young diagrams, i.e. functions ω : R →R satisfying
(1) |ω(u1) −ω(u2)| ≤|u1 −u2|
for all
u1, u2 ∈R
(2) ω(u) = |u| for suﬃciently large |u|.
To each continuous diagram ω ∈CY one can associate a probability measure mω
with compact support on R, determined by the equation
(1.1)
1
z exp
Z
R
1
x −z σ′(x) dx =
Z
R
1
z −xmω(dx)
z ∈C \ R
where σ(u) = (ω(u) −|u|)/2; u ∈R. This measure is called the transition mea-
sure of the diagram and its moments are called the moments of the corresponding
