---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-022-37-the-fukaya-category-of-a-curve
section_title: "The Fukaya category of a curve"
section_number: 3.7
pages: 29-30
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
p→P1 to be the unique curve branched
over the points {0, ξj, 1 ≤j ≤2g + 1}, where ξ is a primitive (2g + 1)-st root of unity. We
can exhibit embedded circles in C via matching arcs amongst these points, i.e. the projections
of Z2-invariant curves to P1. For instance, when g = 2, 5 Lagrangian submanifolds {Lj} of C
are determined by the arcs of the pentagram on the left of Figure 1 (the vertices are the 5th
roots of unity); more generally there is a spikier (2g + 1)-gram deﬁning 2g + 1 associated spheres
permuted by the obvious cyclic symmetry. In an act of shameless innumeracy, we will refer to all
these ﬁgures as pentagrams. If we divide C by the lift of this cyclic group action from P1 to C,
all the circles {Lj} are identiﬁed with a single immersed circle ¯L ⊂S2
orb in an orbifold S2 with
3 orbifold points each of order 2g + 1 (these come from the unique preimage of 0 ∈P1 in C and
the two preimages of ∞∈P1). This immersed curve actually bounds no teardrops, hence Floer
theory can be deﬁned unproblematically for it, or one can work equivariantly upstairs.
Figure 1. Lagrangian spheres from the g = 2 pentagram and its g = 3 cousin;
on the left one radial path and one basic path are also dotted.
For any symplectic surface Σg, ωΣ of genus g ≥2, let σ : ST Σ →Σ be the projection from
the unit tangent bundle. Seidel deﬁnes the balanced Fukaya category, an A∞-category linear
over C, with respect to an auxiliary choice of one-form θ ∈Ω1(ST Σ) which is a primitive for the
pullback of the symplectic form, dθ = σ∗ωΣ. (Such forms exist since, by the Gysin sequence,
H2(ST Σ, R) = 0 for g(Σ) ≥2.) Objects of the balanced Fukaya category are simple closed
curves L ⊂Σ for which R
L ι∗
Lθ = 0, where ιL : L →ST Σ is the tangent lift of L֒ →Σ (these
curves should be equipped with orientations and Spin structures as usual). Homotopically trivial
2Classically, HH∗would be 2-periodic and we’re just taking HH0 and HH1.
30
IVAN SMITH
curves are never balanced; there is a unique balanced representative up to Hamiltonian isotopy
in every other homotopy class of embedded curve.
The balancing condition is an analogue
of monotonicity; it implies that energy and index are correlated for holomorphic curves with
balanced boundary conditions, which in turn means that the balanced category F(Σ) is deﬁned
over C. Diﬀerent choices of θ yield quasi-isomorphic categories, and the mapping class group Γg
acts by autoequivalences of DπF(Σg), cf. [93].
Remark 3.22. An isotopy class of essential simple closed curve γ ⊂Σ deﬁnes two objects in F(Σ)
modulo shifts, namely the balanced representative of γ equipped with either Spin structure.
Label these γ and ¯γ for the non-trivial respectively trivial Spin-structure. Then
HF(γ, γ) ∼= C ∼= HF(¯γ, ¯γ);
HF(γ, ¯γ) = 0.
(3.16)
One can equivalently regard ¯γ as the pair (γ, ξ) where ξ →γ is the non-trivial line bundle with
holonomy in Z2, from which point of view one sees that the group H1(Σ; Z2) acts on F(Σ),
tensoring by ﬂat line bundles.
Remark 3.23. One can combine the actions of diﬀeomorphisms and tensoring by ﬂat line bundles
into an action of the canonical split extension bΓsplit(Σg) of Γg by H1(Σ; Z2). Strictly, this is only a
weak action, meaning that the functors Ggi associated to group elements gi satisfy Gg1Gg2 ∼= Gg1g2
(but we do not keep track of coherence amongst these isomorphisms). We will suppress this point
in the sequel, but it would probably enter in reconciling the appearance of bΓsplit with Remark
2.1; compare to [92, Remark 10.4].
We collect a number of other facts from the work of Seidel [93] and Eﬁmov [29]: let V be a
3-dimensional vector space over K = C.
(1) The pentagram circles {L1, . . . , L2g+1}, each equipped with the non-trivial Spin struc-
ture, split-generate F(Σg) (this is an application of Proposition 3.8);
(2) The Floer cohomology algebra A = L2g+1
i,j=1 HF(Li, Lj) ∼= Λ∗(V ) ⋊Z/(2g + 1), where V
is graded in degree 1 and the exterior algebra inherits the obvious Z/2-grading;
(3) The A∞-structure A on A = H(A) is characterised up to A∞-equivalence as follows: the
operation µd = µd
0+µd
1+. . . decomposes as a sum of pieces µd
i of degrees 6−3d+(4g−4)i;
and there is a basis {x1, x2, x3} for V such that, if e generates Λ0(V ), then
µ3
0(x1, x2, x3) = −e;
µ2g+1
1
(xi, . . . , xi) = e for i ∈{1, 2, 3}
(3.17)
(4) Concretely, the operation µd
i counts holomorphic polygons u which, projected to P1, have
i = multu(∞) + (1/2)multu(0).
The critical statement (3) is a “ﬁnite determinacy” theorem, and at heart is an application
of Theorem 3.18. Unfortunately, we will not be able to use the result in quite this form: even
working over C∗⊂P1, the Fukaya category of the relative quadric Z̸=0,∞which appears later
is not Z-graded. However, Seidel and Eﬁmov deduce this ﬁnite determinacy statement from
the result in singularity theory that a power series with an isolated singularity at the origin is
determined up to formal change of variables by a ﬁnite part of its Taylor series. This result does
not rely on gradings, so we will reduce ourselves to applying that directly.
