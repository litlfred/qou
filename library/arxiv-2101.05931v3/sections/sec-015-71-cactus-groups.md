---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-015-71-cactus-groups
section_title: "Cactus groups"
section_number: 7.1
pages: 17-17
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
---
17
6.2. Θw0 on general categorical representations. In this section we prove that Θw0 is a per-
verse equivalence on an arbitrary categorical representation. Fix µ ∈X such that Cµ is nonzero.
For ease of notation, set A = Cµ and A′ = Cw0(µ).
Consider a ﬁltration by Serre subcategories
0 = C0 ⊂C1 ⊂· · · ⊂Cr = C,
which can be either the Jordan-H¨older ﬁltration (Theorem 3.6) or the isotypic ﬁltration (Remark
3.9). So for every i, Ci is a subrepresentation of C, and Ci/Ci−1 is either a simple categoriﬁcation
or an isotypic one. Deﬁne λi ∈X+ by requiring that [Ci/Ci−1]C(q) is a representation of type λi.
Construct ﬁltrations of A and A′ by Ai = Ci ∩A, A′
i = Ci ∩A′. These are Serre subcategories of
A and A′ respectively. Let p : {0, ..., r} →Z be given by p(i) = ht(µ −w0(λi)).
Theorem 6.8. Θw0
1µ : Db(A) →Db(A′) is a perverse equivalence with respect to (A•, A′
•, p) for
either the Jordan-H¨older or the isotypic ﬁltration.
Proof. Since Ci ⊂C is a categorical subrepresentation, the terms of the functor Θw0
1µ leave Ci invari-
ant, and in particular take objects in Ai to A′
i. By Lemma 4.8 this implies that Θw0
1µ(Db
Ai(A)) ⊆
Db
A′
i(A′).
Now, Ci/Ci−1 is a simple or isotypic categoriﬁcation (of type λi). By Corollary 6.7, Θw0
1µ[−p(i)]
restricts to an abelian equivalence Ai/Ai−1 →A′
i/A′
i−1, i.e. the functor
Θw0
1µ[−p(i)] : Db
Ai(A)/Db
Ai−1(A) →Db
A′
i(A′)/Db
A′
i−1(A′)
is a t-exact equivalence. This shows that Θw0
1µ is a perverse equivalence with respect to (A•, A′
•, p).
□
Remark 6.9. The sl2 case of Theorem 6.8 appears as [15, Proposition 8.4], by a diﬀerent argument
relying on a technical lemma [15, Lemma 4.12].
