---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-020-51-proof-of-theorem-224
section_title: "Proof of Theorem 2.24"
section_number: 5.1
pages: 18-19
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
bra. Then C = Rep(A) is a fusion category. In particular, V ∗∗is isomorphic to V
for any simple object V , which means that S2 is an inner automorphism of A (this
is also proved in [BNSz, 3.22]). So let g ∈A be such that S2(x) = gxg−1 for all
x ∈A. Then g|V : V →V ∗∗: v 7→g · v is an isomorphism of representations.
The calculation of TrV (g) and TrV ((g−1)∗) yields
TrV (g)IdAt
=
Tr(S(g)1(1)|V ∗)1(2),
(24)
TrV ∗((g−1)∗)IdAt
=
Tr(g−11(1)|V )1(2).
(25)
Remark 5.1. We note an important distinction between the quantum trace in an
object V of a morphism V →V ∗∗, which is denoted by TrV , and the usual trace
of a linear operator in the vector space V , which is denoted just by Tr.
Let {qi} be primitive idempotents in Z(At) and for every i let n2
i = dimk(qiAt)
(i.e., ni is the dimension of the irreducible representation of At corresponding to
qi). Multiplying equations (24) and (25) on the right by qj and qi respectively,
ON FUSION CATEGORIES
19
applying Tr|At, and using that for a regular weak Hopf algebra Tr(z|At) = ǫ(z) for
all z ∈At [N], we get
TrV (g)n2
j = Tr(g|qjV ),
TrV ∗((g−1)∗)n2
i = Tr(g−1|S(qi)V ),
and hence,
(26)
Tr(g|qjV )Tr(g−1|S(qi)V ) = |V |2n2
i n2
j.
Taking the sum over all isomorphism classes of simple V , we obtain :
(27)
Tr(S2|qjAS(qi)) = dim(Rep(A))n2
i n2
j.
This proves the ﬁrst statement of the theorem. The second one follows from The-
orem 2.3. Theorem 2.24 is proved.
