---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-018-36-formality
section_title: "Formality"
section_number: 3.6
pages: 26-30
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
The particular case of this that pertains to exterior algebras was u sed by Seidel in computing
F(Σ 2), and will play an important role later.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 27
Let A be a Z2-graded algebra. We will be interested in Z2-graded A∞-structures on A which
have trivial diﬀerential. Such a structure comprises a collection of m aps
{αi :A⊗i→A}i≥2
of parity i; usually we will assume that the product agrees with the given produ ct on A, and
consider (αi)i≥3. We introduce the mod 2 graded Hochschild cochain complex
CC •+1(A,A ) =
∏
i≥2
Hom (•+i)(A⊗i,A )
where Hom (•+i) means we consider homomorphisms of parity • +i. This carries the usual
diﬀerential dCC • and the Gerstenhaber bracket [ ·,·].
Remark 3.16. The shift in grading follows the convention of [93], since we will later imita te some
arguments from that paper. The shift ﬁts with a view of A∞-structures as deﬁned by formal
super-vector ﬁelds, but disagrees with the usual conventions of the bar complex. One typically
incorporates a formal parameter q of even degree into CC •+1(A,A ), which makes the resulting
Lie algebra g = CC •+1[[q]] ﬁltered pronilpotent. This is necessary to guarantee convergen ce
of formal gauge transformations; L∞-quasi-isomorphisms of ﬁltered pronilpotent L∞-algebras
induce bijections between equivalence classes of Maurer-Cartan e lements. In the sequel, we will
encounter gauge transformations on exterior algebras Λ ∗(C3) arising from formal diﬀeomorphisms
of C3 which can be seen explicitly to act on A∞-structures deﬁned over C, cf. Equation 3.13.
Geometrically, the formal parameter q can be incorporated as that of a deformation obtained by
partial compactiﬁcation, in the sense of Equation 3.9. The power of q in any given expression is
therefore determined by Lemma 3.15, and can be reconstructed f rom the other geometric data.
To simplify notation, we omit this parameter throughout, compare t o [93, Sections 4,5].
A∞-structures (αi) on A which extend its given product correspond to elements of CC 1(A,A )
satisfying the Maurer-Cartan equation
∂α + 1
2 [α,α ] = 0 with α1 =α2 = 0. (3.11)
The ﬁrst terms of the Maurer-Cartan equation give
∂α3 = 0; ∂α4 + 1
2 [α3,α 3] = 0; ∂α5 + [α3,α 4] = 0,... (3.12)
Elements (gi)i≥1 of CC 0(A,A ), comprising maps A⊗i→ A of parity i− 1, act by gauge trans-
formations on the set of Maurer-Cartan solutions ( αi)i≥2, at least when suitable convergence
conditions apply. Suppose that A is ﬁnite-dimensional in each degree; let g∈ CC 0(A,A ) have
constant term g0∈A1 vanishing. Deﬁne



φ1 = id + g1 + 1
2g1g1 +··· = exp(g1),
φ2 =g2 + 1
2g1g2 + 1
2g2(g1⊗ id) + 1
2g2(id⊗g1) + 1
3g2(g1⊗g1) +··· ,
...
(3.13)
The term φj is the sum of all possible concatenations of components of g to yield a j-linear map.
For a term involving r components, which may be ordered in s diﬀerent ways compatibly with
their appearance in the concatenation, the constant in front of t he associated term is s(r!)−1,
which ensures convergence ofφj . If α and ˜α are Maurer-Cartan elements which are related by (gi),
the associated A∞-structures are related by φ, which is an A∞-isomorphism. There are obvious
simpliﬁcations to the formulae when g1 = 0, which will be the case for gauge transformations
acting trivially on cohomology relating solutions with α2 = 0.
28 IV AN SMITH
Lemma 3.17. Let A denote theA∞-algebra deﬁned by the Maurer-Cartan element α∈CC 1(A,A ),
with H(A) = A. The Hochschild cohomology HH ∗(A, A) is the cohomology of the complex
CC •(A,A ) with respect to the twisted diﬀerential dCC • + [·,α ].
Proof. The Maurer-Cartan equation for α implies that the twisted diﬀerential does square to
zero. The Lemma follows on comparing the resulting complex with the b ar complex deﬁning
Hochschild cohomology of an A∞-algebra given in Equation 3.5. □
Kontsevich’s remarkable result [53], specialised to the case of releva nce in the sequel, is then:
Theorem 3.18 (Formality Theorem, Kontsevich). When A = Λ(V ) is an exterior algebra, with
its natural Z2-grading placing V in degree 1, there is an L∞-quasi-isomorphism
Φ : CC •(A,A )−→Sym •(V ∨)⊗ Λ(V )
between the Hochschild complex and its cohomology, the Lie a lgebra of polyvector ﬁelds.
Remark 3.19. In fact, this Φ is strictly left-inverse to an explicit quasi-isomorphism
Ψ : Sym •(V ∨)⊗ Λ(V )→CC •(Λ(V ), Λ(V ))
deﬁned by Kontsevich. The components of Ψ are linear combinations Ψ i = ∑ λi⊗U Γ i , where
UΓ i is a multilinear operation indexed by a certain class of graphs {Γ i}, and the coeﬃcients λi
are explicit integrals over conﬁguration spaces of points in the uppe r half-plane.
The Lie algebra of polyvector ﬁelds on a ﬁnite-dimensional vector sp ace V is the algebra
Sym •(V ∨)⊗ Λ(V ) = C[[V ]]⊗ Λ(V ).
The Lie algebra structure comes from the Schouten bracket
[fξ i1∧···∧ ξik,gξ j1∧··· ξjl ] =
∑
q(−1)k−q−1f (∂iqg)ξi1∧···∧ ˆξiq∧···∧ ξik∧ξj1∧···∧ ξjl +
∑
q(−1)l−q+(k−1)(l−1)g (∂jqf )ξj1∧···∧ ˆξjq∧···∧ ξjl∧ξi1∧···∧ ξik.
(3.14)
The quasi-isomorphism Φ identiﬁes gauge equivalence classes of Maur er-Cartan solutions. In
particular, since the Schouten bracket vanishes on functions, an y formal function W ∈ C[[V ]]
deﬁnes a solution of Maurer-Cartan, hence an A∞-structure on Λ( V ). Lemma 3.17 and the
Formality Theorem 3.18 imply that the Hochschild cohomology of a Z2-gradedA∞-structure on
Λ(V ) deﬁned by an element α∈HH 1 is given by the cohomology of the Z2-graded complex
(C[[V ]]⊗ Λ ev(V ))
[·,α]
−−−−⇀↽−−−−
[·,α]
(C[[V ]]⊗ Λ odd(V )). (3.15)
The following Example will recur in the discussion of Fukaya categories of quadric hypersur-
faces in Section 4.1.
Example 3.20. Let V have dimension 1 and A = Λ(V ), with basis 1 ,x say. Any formal function
W∈ C[[x]] of degree ≥ 2 deﬁnes an A∞-structure on A, which induces the given product if and
only if the degree 2 component vanishes. Up to formal change of va riables (gauge transformation),
any
W (x) = xk +O(xk+1) ≃ yk via y =x(1 +α1x +α2x2 +··· )
is equivalent to a monomial, hence the resulting A∞-structures are equivalent to those deﬁned
by monomial functions. Equation 5.11 simpliﬁes to the complex
0−→ C[[x]]⊗⟨dx⟩
ιdW
−−−−→C[[x]]−→ 0
with cohomology C[[x]]/⟨W ′(x)⟩ given by the Jacobian ring, so the Hochschild cohomology of
Ak = (A,W =xk) has rank k− 1.
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 29
Remark 3.21. For the ring R = C[x]/⟨x2− 1⟩, the Hochschild cohomology 2 group of the category
of Z2-graded modules has rank 2 if deg(x) is even and rank 1 if deg(x) is odd (the latter fact is
the computation of Example 3.20 in the special case k = 1, where the underlying product on A
is itself deformed). This comes down to the fact that the group
Hom R⊗R(R⊗R,R )
of bimodule homomorphisms has rank 2 in the ﬁrst case, comprising th e elements 1⊗1↦→α1+βx,
but only rank 1 in the second, since for a Z2-graded map one must have 1 ⊗ 1↦→α1. From
another viewpoint, when deg(x) is even,R is semisimple, splitting into two orthogonal idempotent
summands, but when deg(x) is odd the idempotents are not of pure degree and there is no such
splitting.
3.7. The F ukaya category of a curve. Take Σ g∼=C
p
→ P1 to be the unique curve branched
over the points {0,ξ j, 1≤ j≤ 2g + 1}, where ξ is a primitive (2 g + 1)-st root of unity. We
can exhibit embedded circles in C via matching arcs amongst these points, i.e. the projections
of Z2-invariant curves to P1. For instance, when g = 2, 5 Lagrangian submanifolds {Lj} of C
are determined by the arcs of the pentagram on the left of Figure 1 (the vertices are the 5th
roots of unity); more generally there is a spikier (2 g + 1)-gram deﬁning 2g + 1 associated spheres
permuted by the obvious cyclic symmetry. In an act of shameless inn umeracy, we will refer to all
these ﬁgures as pentagrams. If we divide C by the lift of this cyclic group action from P1 to C,
all the circles {Lj} are identiﬁed with a single immersed circle ¯L⊂S2
orb in an orbifold S2 with
3 orbifold points each of order 2 g + 1 (these come from the unique preimage of 0 ∈ P1 in C and
the two preimages of ∞∈ P1). This immersed curve actually bounds no teardrops, hence Floer
theory can be deﬁned unproblematically for it, or one can work equiv ariantly upstairs.
Figure 1. Lagrangian spheres from the g = 2 pentagram and its g = 3 cousin;
on the left one radial path and one basic path are also dotted.
For any symplectic surface Σ g,ω Σ of genus g≥ 2, let σ : ST Σ → Σ be the projection from
the unit tangent bundle. Seidel deﬁnes the balanced Fukaya category, an A∞-category linear
over C, with respect to an auxiliary choice of one-form θ∈ Ω 1(ST Σ) which is a primitive for the
pullback of the symplectic form, dθ = σ∗ωΣ . (Such forms exist since, by the Gysin sequence,
H 2(ST Σ, R) = 0 for g(Σ) ≥ 2.) Objects of the balanced Fukaya category are simple closed
curves L⊂ Σ for which ∫
Lι∗
Lθ = 0, where ιL : L→ ST Σ is the tangent lift of֒→Σ (these
curves should be equipped with orientations and Spin structures as usual). Homotopically trivial
2Classically, HH ∗ would be 2-periodic and we’re just taking HH 0 and HH 1.
30 IV AN SMITH
curves are never balanced; there is a unique balanced representa tive up to Hamiltonian isotopy
in every other homotopy class of embedded curve. The balancing co ndition is an analogue
of monotonicity; it implies that energy and index are correlated for h olomorphic curves with
balanced boundary conditions, which in turn means that the balance d category F(Σ) is deﬁned
over C. Diﬀerent choices of θ yield quasi-isomorphic categories, and the mapping class group Γ g
acts by autoequivalences of DπF(Σ g), cf. [93].
Remark 3.22. An isotopy class of essential simple closed curve γ⊂ Σ deﬁnes two objects in F(Σ)
modulo shifts, namely the balanced representative of γ equipped with either Spin structure.
Label these γ and ¯γ for the non-trivial respectively trivial Spin-structure. Then
HF (γ,γ )∼= C∼=HF (¯γ, ¯γ); HF (γ, ¯γ) = 0. (3.16)
One can equivalently regard ¯γ as the pair ( γ,ξ ) where ξ→γ is the non-trivial line bundle with
holonomy in Z2, from which point of view one sees that the group H 1(Σ; Z2) acts on F(Σ),
tensoring by ﬂat line bundles.
Remark 3.23. One can combine the actions of diﬀeomorphisms and tensoring by ﬂat line bundles
into an action of the canonical split extension ˆΓ split(Σ g) of Γ g byH 1(Σ; Z2). Strictly, this is only a
weak action, meaning that the functors Ggi associated to group elements gi satisfy Gg1 Gg2
∼= Gg1g2
(but we do not keep track of coherence amongst these isomorphis ms). We will suppress this point
in the sequel, but it would probably enter in reconciling the appearanc e of ˆΓ split with Remark
2.1; compare to [92, Remark 10.4].
We collect a number of other facts from the work of Seidel [93] and Eﬁmov [29]: let V be a
3-dimensional vector space over K = C.
(1) The pentagram circles {L1,...,L 2g+1}, each equipped with the non-trivial Spin struc-
ture, split-generate F(Σ g) (this is an application of Proposition 3.8);
(2) The Floer cohomology algebra A = ⨁ 2g+1
i,j=1HF (Li,L j)∼= Λ ∗(V ) ⋊ Z/(2g + 1), where V
is graded in degree 1 and the exterior algebra inherits the obvious Z/2-grading;
(3) The A∞-structure A onA =H(A) is characterised up to A∞-equivalence as follows: the
operationµd =µd
0 +µd
1 +... decomposes as a sum of pieces µd
i of degrees 6−3d+(4g−4)i;
and there is a basis {x1,x 2,x 3} for V such that, if e generates Λ 0(V ), then
µ3
0(x1,x 2,x 3) =−e; µ2g+1
1 (xi,...,x i) = e for i∈{ 1, 2, 3} (3.17)
(4) Concretely, the operation µd
i counts holomorphic polygons u which, projected to P1, have
i =multu(∞) + (1/2)multu(0).
The critical statement (3) is a “ﬁnite determinacy” theorem, and a t heart is an application
of Theorem 3.18. Unfortunately, we will not be able to use the result in quite this form: even
working over C∗⊂ P1, the Fukaya category of the relative quadric Z⁄=0,∞ which appears later
is not Z-graded. However, Seidel and Eﬁmov deduce this ﬁnite determinac y statement from
the result in singularity theory that a power series with an isolated sin gularity at the origin is
determined up to formal change of variables by a ﬁnite part of its Ta ylor series. This result does
not rely on gradings, so we will reduce ourselves to applying that dire ctly.
