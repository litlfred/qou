---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-021-36-formality
section_title: "Formality"
section_number: 3.6
pages: 26-29
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
the A∞-structure on an algebra A = ⊕i,jHF(Li, Lj), where the {Li} are some ﬁnite collection
of Lagrangians distinguished by the geometry in some fashion. In general this is a rather in-
tractable problem, but in the case when A is smooth and commutative, A∞-structures up to
gauge equivalence correspond to classical Poisson structures, by Kontsevich’s formality theorem.
The particular case of this that pertains to exterior algebras was used by Seidel in computing
F(Σ2), and will play an important role later.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
27
Let A be a Z2-graded algebra. We will be interested in Z2-graded A∞-structures on A which
have trivial diﬀerential. Such a structure comprises a collection of maps
{αi : A⊗i →A}i≥2
of parity i; usually we will assume that the product agrees with the given product on A, and
consider (αi)i≥3. We introduce the mod 2 graded Hochschild cochain complex
CC•+1(A, A) =
Y
i≥2
Hom(•+i)(A⊗i, A)
where Hom(•+i) means we consider homomorphisms of parity • + i.
This carries the usual
diﬀerential dCC• and the Gerstenhaber bracket [·, ·].
Remark 3.16. The shift in grading follows the convention of [93], since we will later imitate some
arguments from that paper. The shift ﬁts with a view of A∞-structures as deﬁned by formal
super-vector ﬁelds, but disagrees with the usual conventions of the bar complex. One typically
incorporates a formal parameter q of even degree into CC•+1(A, A), which makes the resulting
Lie algebra g = CC•+1[[q]] ﬁltered pronilpotent. This is necessary to guarantee convergence
of formal gauge transformations; L∞-quasi-isomorphisms of ﬁltered pronilpotent L∞-algebras
induce bijections between equivalence classes of Maurer-Cartan elements. In the sequel, we will
encounter gauge transformations on exterior algebras Λ∗(C3) arising from formal diﬀeomorphisms
of C3 which can be seen explicitly to act on A∞-structures deﬁned over C, cf. Equation 3.13.
Geometrically, the formal parameter q can be incorporated as that of a deformation obtained by
partial compactiﬁcation, in the sense of Equation 3.9. The power of q in any given expression is
therefore determined by Lemma 3.15, and can be reconstructed from the other geometric data.
To simplify notation, we omit this parameter throughout, compare to [93, Sections 4,5].
A∞-structures (αi) on A which extend its given product correspond to elements of CC1(A, A)
satisfying the Maurer-Cartan equation
∂α + 1
2[α, α] = 0
with
α1 = α2 = 0.
(3.11)
The ﬁrst terms of the Maurer-Cartan equation give
∂α3 = 0; ∂α4 + 1
2[α3, α3] = 0; ∂α5 + [α3, α4] = 0, . . .
(3.12)
Elements (gi)i≥1 of CC0(A, A), comprising maps A⊗i →A of parity i −1, act by gauge trans-
formations on the set of Maurer-Cartan solutions (αi)i≥2, at least when suitable convergence
conditions apply. Suppose that A is ﬁnite-dimensional in each degree; let g ∈CC0(A, A) have
constant term g0 ∈A1 vanishing. Deﬁne







φ1 = id + g1 + 1
2g1g1 + · · · = exp(g1),
φ2 = g2 + 1
2g1g2 + 1
2g2(g1 ⊗id) + 1
2g2(id ⊗g1) + 1
3g2(g1 ⊗g1) + · · · ,
...
(3.13)
The term φj is the sum of all possible concatenations of components of g to yield a j-linear map.
For a term involving r components, which may be ordered in s diﬀerent ways compatibly with
their appearance in the concatenation, the constant in front of the associated term is s(r!)−1,
which ensures convergence of φj. If α and ˜α are Maurer-Cartan elements which are related by (gi),
the associated A∞-structures are related by φ, which is an A∞-isomorphism. There are obvious
simpliﬁcations to the formulae when g1 = 0, which will be the case for gauge transformations
acting trivially on cohomology relating solutions with α2 = 0.
28
IVAN SMITH
Lemma 3.17. Let A denote the A∞-algebra deﬁned by the Maurer-Cartan element α ∈CC1(A, A),
with H(A) = A.
The Hochschild cohomology HH∗(A, A) is the cohomology of the complex
CC•(A, A) with respect to the twisted diﬀerential dCC• + [·, α].
Proof. The Maurer-Cartan equation for α implies that the twisted diﬀerential does square to
zero. The Lemma follows on comparing the resulting complex with the bar complex deﬁning
Hochschild cohomology of an A∞-algebra given in Equation 3.5.
□
Kontsevich’s remarkable result [53], specialised to the case of relevance in the sequel, is then:
Theorem 3.18 (Formality Theorem, Kontsevich). When A = Λ(V ) is an exterior algebra, with
its natural Z2-grading placing V in degree 1, there is an L∞-quasi-isomorphism
Φ : CC•(A, A) −→Sym•(V ∨) ⊗Λ(V )
between the Hochschild complex and its cohomology, the Lie algebra of polyvector ﬁelds.
Remark 3.19. In fact, this Φ is strictly left-inverse to an explicit quasi-isomorphism
Ψ : Sym•(V ∨) ⊗Λ(V ) →CC•(Λ(V ), Λ(V ))
deﬁned by Kontsevich. The components of Ψ are linear combinations Ψi = P λi ⊗UΓi, where
UΓi is a multilinear operation indexed by a certain class of graphs {Γi}, and the coeﬃcients λi
are explicit integrals over conﬁguration spaces of points in the upper half-plane.
The Lie algebra of polyvector ﬁelds on a ﬁnite-dimensional vector space V is the algebra
Sym•(V ∨) ⊗Λ(V ) = C[[V ]] ⊗Λ(V ).
The Lie algebra structure comes from the Schouten bracket
[f ξi1 ∧· · · ∧ξik, g ξj1 ∧· · · ξjl] =
P
q(−1)k−q−1f (∂iqg) ξi1 ∧· · · ∧c
ξiq ∧· · · ∧ξik ∧ξj1 ∧· · · ∧ξjl+
P
q(−1)l−q+(k−1)(l−1)g (∂jqf) ξj1 ∧· · · ∧c
ξjq ∧· · · ∧ξjl ∧ξi1 ∧· · · ∧ξik.
(3.14)
The quasi-isomorphism Φ identiﬁes gauge equivalence classes of Maurer-Cartan solutions. In
particular, since the Schouten bracket vanishes on functions, any formal function W ∈C[[V ]]
deﬁnes a solution of Maurer-Cartan, hence an A∞-structure on Λ(V ).
Lemma 3.17 and the
Formality Theorem 3.18 imply that the Hochschild cohomology of a Z2-graded A∞-structure on
Λ(V ) deﬁned by an element α ∈HH1 is given by the cohomology of the Z2-graded complex
(C[[V ]] ⊗Λev(V ))
[·,α]
−−−−⇀
↽−−−−
[·,α]
(C[[V ]] ⊗Λodd(V )).
(3.15)
The following Example will recur in the discussion of Fukaya categories of quadric hypersur-
faces in Section 4.1.
Example 3.20. Let V have dimension 1 and A = Λ(V ), with basis 1, x say. Any formal function
W ∈C[[x]] of degree ≥2 deﬁnes an A∞-structure on A, which induces the given product if and
only if the degree 2 component vanishes. Up to formal change of variables (gauge transformation),
any
W(x) = xk + O(xk+1) ≃yk
via y = x(1 + α1x + α2x2 + · · · )
is equivalent to a monomial, hence the resulting A∞-structures are equivalent to those deﬁned
by monomial functions. Equation 5.11 simpliﬁes to the complex
0 −→C[[x]] ⊗⟨dx⟩
ιdW
−−−−→C[[x]] −→0
with cohomology C[[x]]/⟨W ′(x)⟩given by the Jacobian ring, so the Hochschild cohomology of
Ak = (A, W = xk) has rank k −1.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
29
Remark 3.21. For the ring R = C[x]/⟨x2 −1⟩, the Hochschild cohomology2 group of the category
of Z2-graded modules has rank 2 if deg(x) is even and rank 1 if deg(x) is odd (the latter fact is
the computation of Example 3.20 in the special case k = 1, where the underlying product on A
is itself deformed). This comes down to the fact that the group
HomR⊗R(R ⊗R, R)
of bimodule homomorphisms has rank 2 in the ﬁrst case, comprising the elements 1⊗1 7→α1+βx,
but only rank 1 in the second, since for a Z2-graded map one must have 1 ⊗1 7→α1. From
another viewpoint, when deg(x) is even, R is semisimple, splitting into two orthogonal idempotent
summands, but when deg(x) is odd the idempotents are not of pure degree and there is no such
splitting.
