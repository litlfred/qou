---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-010-33-proof-of-proposition-212-and-properties-of-mo
section_title: "Proof of Proposition 2.12 and properties of modular categories"
section_number: 3.3
pages: 12-13
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
---
well known (see [BaKi]) that the matrix T is diagonal with eigenvalues being roots
of unity. So we only need to show that the S-matrix is unitary. The en tries sij of
the S-matrix are known to satisfy sij = sji, and ∑
jsi∗jsjl = δil ([BaKi]). So it
suﬃces to show that si∗j =sij.
Recall that sj0 = ± dim(Vj )/
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
One the other hand, since NT
i =Ni∗ , and Ni is real, we have
v∗
mNivm = (NT
i vm)∗vm = (Ni∗ vm)∗vm = (si∗m
s0m
vm)∗vm = si∗m
s0m
|vm|2.
Since |vm|2 ⁄= 0, the statement is proved.
Remark 3.2. An important property of modular categories is
Proposition 3.3. ([EG4], Lemma 1.2) The dimension of every simple object of a
modular category divides
√
D, where D is the global dimension of the category.
This implies that in a ribbon category, dimensions of objects divide the global
dimension (this is seen by taking the Drinfeld center and using Theore m 2.15 and
the well known fact that the Drinfeld center of a braided category contains the
original category). This fact is useful in classiﬁcation of modular ca tegories (See
section 8).
In conclusion of this subsection let us give a simple application of Theor em 2.3
to modular categories.
Let c ∈ C/8Z be the Virasoro central charge of a modular category C, deﬁned
by the relation ( ST )3 = e2πic/8S2 (see [BaKi]), and D be the global dimension of
C. Let f : ( −∞, 1] → [1, ∞) be the inverse function to the monotonely decreasing
function g(x) = (3 −x)√x/2.
ON FUSION CATEGORIES 13
Proposition 3.4. One has
D ≥f (sign(s00) cos(πc/4))
Remark 3.5. The number s00 equals ±1/
√
D.
Proof. We need to show that
sign(s00) cos(πc/4) ≥ (3 −D)
√
D/2
To prove this, recall [BaKi] that the number eπic/4 can be expressed via a Gaussian
sum:
sign(s00)eπic/4 =
∑
|Xi|2θi/
√
D,
where θi are the twists. This means that
sign(s00)eπic/4 −D−1/2 =
∑
i⁄=0
|Xi|2θi/
√
D.
Taking squared absolute values of both sides, and using that |θi| = 1, and |Xi|2> 0
(by Theorem 2.3), we get
|sign(s00)eπic/4 −D−1/2|2 ≤ (
∑
i⁄=0
|Xi|2)2/D = (D − 1)2
D .
After simpliﬁcations, this yields the desired inequality. □
Remark 3.6. Sometimes this inequality sharp. For example, for c = ±2/5, ±22/5,
it yields an estimate D ≥ (5−
√
5)/2, which becomes an equality for the well known
Yang-Lee category (c = −22/5, see [DMS]) and three its Galois images. The same
is true for c = ±14/5, ±34/5, in which case the estimate is D ≥ (5 +
√
5)/2 (it is
attained at four Galois images of the Yang-Lee category). Also, it g oes without
saying that the inequality is sharp for c = 0, where it becomes an equality for the
trivial category.
These considerations inspire the following questions.
Questions. Does there exist a sequence of nontrivial fusion categories over C
for which the global dimensions tend to 1? Does there exist such a se quence with
a bounded number of simple objects? Is the set of global dimensions of fusion
categories over C a discrete subset of R?
We expect that the answer to the ﬁrst question is “no”, i.e. the poin t 1 of the
set of possible dimensions of fusion categories is an isolated point (“c ategorical
property T”).
