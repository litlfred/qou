---
doc_id: arxiv-math-0203060v11
doc_title: "ON FUSION CATEGORIES"
section_id: sec-012-33-proof-of-proposition-212-and-properties-of-mo
section_title: "Proof of Proposition 2.12 and properties of modular categories"
section_number: 3.3
pages: 12-13
source_pdf: 0203060v11.pdf
source_sha256: fa7e21ceab3e9933
toc_source: outline
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in partic- ular, the theory of weak Hopf algebras), we prove a number of general results about fusion categories in"
---
well known (see [BaKi]) that the matrix T is diagonal with eigenvalues being roots
of unity. So we only need to show that the S-matrix is unitary. The entries sij of
the S-matrix are known to satisfy sij = sji, and P
j si∗jsjl = δil ([BaKi]). So it
suﬃces to show that si∗j = sij.
Recall that sj0 = ± dim(Vj)/
√
D, where D is the global dimension of the cate-
gory. So sj0 is a real number. Further, by the Verlinde formula ([BaKi, 3.1]), if vm
is the m-th column of S then
Nivm = sim
s0m
vm,
for all i. Let v∗
m denote the row vector, Hermitian adjoint to vm. Then
v∗
mNivm = sim
s0m
|vm|2.
One the other hand, since N T
i = Ni∗, and Ni is real, we have
v∗
mNivm = (N T
i vm)∗vm = (Ni∗vm)∗vm = (si∗m
s0m
vm)∗vm = si∗m
s0m
|vm|2.
Since |vm|2̸ = 0, the statement is proved.
Remark 3.2. An important property of modular categories is
Proposition 3.3. ([EG4], Lemma 1.2) The dimension of every simple object of a
modular category divides
√
D, where D is the global dimension of the category.
This implies that in a ribbon category, dimensions of objects divide the global
dimension (this is seen by taking the Drinfeld center and using Theorem 2.15 and
the well known fact that the Drinfeld center of a braided category contains the
original category). This fact is useful in classiﬁcation of modular categories (See
section 8).
In conclusion of this subsection let us give a simple application of Theorem 2.3
to modular categories.
Let c ∈C/8Z be the Virasoro central charge of a modular category C, deﬁned
by the relation (ST )3 = e2πic/8S2 (see [BaKi]), and D be the global dimension of
C. Let f : (−∞, 1] →[1, ∞) be the inverse function to the monotonely decreasing
function g(x) = (3 −x)√x/2.
ON FUSION CATEGORIES
13
Proposition 3.4. One has
Remark 3.5. The number s00 equals ±1/
Proof. We need to show that
sign(s00) cos(πc/4) ≥(3 −D)
sign(s00)eπic/4 =
where θi are the twists. This means that
sign(s00)eπic/4 −D−1/2 =
|sign(s00)eπic/4 −D−1/2|2 ≤(
√
