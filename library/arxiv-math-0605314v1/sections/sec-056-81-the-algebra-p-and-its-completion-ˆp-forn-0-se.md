---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-056-81-the-algebra-p-and-its-completion-ˆp-forn-0-se
section_title: "The algebra P and its completion ˆP. Forn≥ 0, set"
section_number: 8.1
pages: 28-29
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
P ′
n = Pn
{n}!∈R Q(v),
˜P ′
n =v− 1
2 n(n−1)P ′
n∈R Q(v).
We haveP ′
0 = 1. Deﬁne a Z[q,q −1]-submoduleP ofRQ(v) by
P = Span Z[q,q−1]{ ˜P ′
n| n≥ 0}.
Lemma 8.1. P is a Z[q,q −1]-subalgebra ofRQ(v).
Proof. By induction, we obtain
PmPn =
min(m,n)∑
i=0
{m}i{n}i{m +n}i
{i}! Pm+n−i.
Hence,
P ′
mP ′
n =
min(m,n)∑
i=0
{m +n}!
{i}!{m−i}!{n−i}!P ′
m+n−i.(8.1)
The coeﬃcient in the right-hand side is contained in vdZ[q,q −1], whered≡
(m+n+1
2
)
−(i+1
2
)
−
(m−i+1
2
)
−
(n−i+1
2
)
≡
(i+1
2
)
(mod 2). Since
(m
2
)
+
(n
2
)
−
(m+n−i
2
)
≡
(i+1
2
)
(mod 2), we have v(
m
2 )P ′
mv(
n
2)P ′
n∈P . Therefore, we have PP⊂P . Since we have
1 = P ′
0∈P , we have the assertion.
Fork≥ 0, set
Pk = Span Z[q,q−1]{ ˜P ′
n| n≥k}⊂P .
We have
P =P0⊃P 1⊃P 2⊃··· .
It follows from (8.1) that each Pk is an ideal in P. Set
ˆP = lim←−k≥0P/Pk,
which inherits a Z[q,q −1]-algebra structure from P. Each element x∈ ˆP can be
uniquely expressed as an inﬁnite sum x = ∑ ∞
k=0xk ˜P ′
k, where xk ∈ Z[q,q −1] for
k≥ 0. Since ⋂
k≥0Pk ={0}, we may regard P as a subalgebra of ˆP.
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 29
