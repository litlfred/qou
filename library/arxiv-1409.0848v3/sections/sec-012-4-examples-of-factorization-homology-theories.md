---
doc_id: arxiv-1409.0848v3
doc_title: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES"
section_id: sec-012-4-examples-of-factorization-homology-theories
section_title: "Examples of factorization homology theories"
section_number: 4
pages: 42-43
source_pdf: 1409.0848v3.pdf
source_sha256: 5af73ef812ccee40
doc_brief: "FACTORIZATION HOMOLOGY OF STRATIFIED SPACES — This work forms a foundational study of factorization homol ogy, or topological chiral homology, at the generality of stratiﬁed spaces with tangen tial"
---
In this section we give examples of factorization homology over stra tiﬁed spaces. To illustrate
the relevance to low-dimensional topology, we show that the free Diskfr
3,1-algebra can distinguish the
homotopy type of link complements, and in particular deﬁnes a non-t rivial link invariant.
4.1. F actorization homology of stratiﬁed 1-manifolds
When the target symmetric monoidal ∞-category V is Mod⊗
k , the category of k-modules for some
commutative algebra k, then factorization homology of closed 1-manifolds gives variants o f Hochschild
homology.
The simplest and most fundamental example is factorization homolog y for framed 1-manifolds,
Mﬂdfr
1 . In this case, there is an equivalence between framed 1-disk algebr as and associative algebras
in V, AlgDiskfr
1
(V) ≃ Alg(V), and we have the following immediate consequence of the excision
property of factorization homology (Theorem 2.40).
Proposition 4.1. For an associative algebra A in Modd, there is an equivalence∫
S1
A≃ HC∗(A)
between the factorization homology of the circle with coeﬃc ients in A and the Hochschild homology
of A relative k.
Proof. We have the equivalences∫
S1
A≃
∫
R1
A ⊗∫
S0×R1
A
∫
R1
A≃A ⊗
A⊗Aop
A≃ HC∗(A)
using excision and a decomposition of the circle by two slightly overlapp ing hemispheres. □
Remark 4.2. Lurie in§5.5.3 of [Lu2] shows further that the obvious circle action by rotatio ns on∫
S1A agrees with the usual simplicial circle action on the cyclic bar constru ction.
42
It is interesting to probe this example slightly further and see the alg ebraic structure that results
when one introduces marked points and singularities into the 1-manif olds. Recall the ∞-category
Mﬂdfr
1,0 of framed 1-manifolds with marked points, and the ∞-subcategory Dfr
1,0 of framed 1-disks
with at most one marked point – its set of objects is the two-element set{U 1
∅−1,U 1
S0} whose elements
we justiﬁably denote as R1 :=U 1
∅−1 and ( R1,{0}) := U 1
S0. So AlgDiskfr
1,0
(V) is equivalent to the ∞-
category whose objects are pairs ( A1,A b) consisting of an algebra A1 and a unital A1-bimodule Ab,
i.e., a bimodule with an invariant map from the unit. Speciﬁcally, A1≃A(R1) andAb≃A(R1,{0}).
The proof of the Proposition 4.1 extends mutatis mutandis to the fo llowing.
Proposition 4.3. There is an equivalence∫
(S1,∗)
A≃ HC∗(A1,A b)
between the factorization homology of the pointed circle (S1,∗) with coeﬃcients in A = (A1,A b) and
the Hochschild homology of A1 with coeﬃcients in the bimodule Ab.
Finally, we mention the example of factorization homology for Snglrfr
1 , the category of 1-dimensional,
framed, stratiﬁed spaces. In this case, the ∞-category of basic opens Bscfr
1 has as its set of objects
{R} ∐{(C(J),σ )} where the latter set is indexed by ﬁnite sets J together with an orientation σ of
the ordinary 1-manifold ⨆
J R>0 = C(J) /integerdivide∗.
An object A in AlgDisk(Bscfr
1)(V) is then equivalent, by evaluating on directed graphs with a single
vertex, to the data of an associative algebra A(R) in V and for each pair i,j≥ 0 an object A(i,j )∈ V
equipped with i intercommuting leftA(R)-module structures and j intercommuting right compatible
A(R)-module structures. One can see, for instance, that the facto rization homology of a wedge of
two circles with a marked point on each circle, ( S1∪{0}S1,{1,−1}), can be calculated as
∫
(S1∪{0}S1,{1,−1})
A≃A(1, 1) ⊗
A1⊗Aop
1
A(2, 2) ⊗
A1⊗Aop
1
A(1, 1) .
