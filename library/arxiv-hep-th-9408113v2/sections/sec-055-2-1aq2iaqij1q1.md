---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-055-2-1aq2iaqij1q1
section_title: "(1−aq2i)(aq)i+j−1(q)−1"
section_number: 2
pages: 51-52
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
i−j. (12b)
Prove that M and M ∗ are inverse, inﬁnite, lower-triangle matrices. That is
∑
j≤k≤i
MikM ∗
kj =δij.
Hint: use the terminating very well-poised 4ϕ3 summation theorem (see e.g. [GR]).
2) Let α ={αn} and β ={βn}, n≥ 0 be sequences of functions in q. Let M and M ∗ be
as in (12). We say (cf. [An3]) that α and β form a Bailey pair relative to a if
βn =
n∑
k=0
Mnkαk, for all n≥ 0.
52 Anatol N. Kirillov
It is clear that (Bailey’s pair inversion rule)
αn =
n∑
k=0
M ∗
nkβk.
Theorem (G. Andrews [An2]) (Bailey’s lemma). Let the sequences α ={αn} and
β ={βn} form a Bailey pair. If α′ ={α′
n} and β′ ={β′
n} are deﬁned by
α′
n := (ρ1)n(ρ2)n
(aq/ρ1)n(aq/ρ2)n
(aq/ρ1ρ2)nαn,
β′
n :=
n∑
k=0
(ρ1)k(ρ2)k(aq/ρ1ρ2)n−k
(q)n−k(aq/ρ1)k(aq/ρ2)k
(aq/ρ1ρ2)kβk,
then α′ and β′ also form a Bailey pair.
A proof can be found in [An3].
• Prove the following corollary of Bailey’s lemma:
∑
k≥0
akqk2
βk = 1
(aq)∞
∞∑
k=0
akqk2
αk, (13)
for any Bailey pair α ={αn} and β ={βn}.
Hint: take the limit n,ρ 1,ρ 2→∞ in the Bailey pair deﬁning relation
β′
n =
n∑
k=0
α′
k
(q)n−k(aq)n+k
.
More generally, prove that if α ={αn} and β ={βn} is a Bailey pair, then
∑
m1,...,mk
aN1+···+NkqN 2
1 +···+N 2
k
(q)m1··· (q)mk
βmk = 1
(aq)∞
∑
n≥0
qkn2
aknαn.
(G. Andrews, 1984)
Hint: use the k-fold iteration of Bailey’s lemma.
3) Prove that the following sequences form the Bailey pair
i) βn =
{ 1, n = 0,
0, n> 0, (15)
αn = (−1)nq
n(n−1)
