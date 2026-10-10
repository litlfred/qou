---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-030-452-deformation-functors-at-ﬁxed-points-of-q
section_title: "Deformation functors at ﬁxed points of Q"
section_number: 4.5.2
pages: 14-15
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
The deformation functor can be deﬁned in terms of a formal gra ded Q-manifold M with base point
(denoted by 0). The set of solutions of the Maurer-Cartan equ ation with coeﬃcients in a ﬁnite-dimensional
nilpotent non-unital algebra m is deﬁned as the set of m-points of the formal scheme of zeroes of Q:
Maps
((
Spec(m⊕ k· 1), base point
)
,
(
Zeroes(Q), 0
))
⊂Maps
((
Spec(m⊕ k· 1), base point
)
,
(
M, 0
))
.
In terms of the coalgebra C corresponding to M this set is equal to the set of homomorphisms of
coalgebras m∗−→C with the image annihilated by Q. Another way to say is to introduce a global (i.e. not
formal) pointed Q-manifold of maps from
(
Spec(m⊕ k· 1), base point
)
to (M, 0) and consider zeroes of the
global vector ﬁeld Q on it.
Two solutions p0 and p1 of the Maurer-Cartan equation are called gauge equivalent i ﬀ there exists
(parametrized by Spec(m⊕ k· 1)) polynomial family of odd vector ﬁelds ξ(t) on M (of degree −1 with
respect to Z-grading) and a polynomial solution of the equation
dp(t)
dt = [Q,ξ (t)]|p(t), p(0) = p0, p(1) = p1,
where p(t) is a polynomial family of m-points of formal graded manifold M with base point.
In terms of L∞-algebras, the set of polynomial paths {p(t)} is naturally identiﬁed with g1⊗ m⊗ k[t].
Vector ﬁelds ξ(t) depending polynomially on t are not necessarily vanishing at the base point 0. The set of
these vector ﬁelds is
Hom Gradedk (C(g[1])⊕ (k· 1)∗, g)⊗ (m⊕ k· 1) .
One can check that the gauge equivalence deﬁned above is an eq uivalence relation. Alternatively, one
can deﬁne the equivalence relation as the transitive closur e of the relation from above. For formal graded
pointed manifold M we deﬁne set DefM (m) as the set of gauge equivalence classes of solutions of the
14
Maurer-Cartan equation. The correspondence m↦→DefM (m) extends naturally to a functor denoted also
byDefM . Analogously, for L∞-algebra g we denote by Defg the corresponding deformation functor.
One can easily prove the following properties:
1) for a diﬀerential graded Lie algebra g the deformation functor deﬁned as above for ( g[1]f ormal, 0), is
naturally equivalent to the deformation functor deﬁned in 3 .2,
2) any L∞-morphism gives a natural transformation of functors,
3) the functor Defg1⊕g2 corresponding to the direct sum of two L∞-algebras, is naturally equivalent to
the product of functors Defg1×Defg2,
4) the deformation functor for a linear contractible L∞-algebra g is trivial, Defg(m) is a one-element
set for every m.
Properties 2)-4) are just trivial, and 1) is easy. It follows from properties 1)-4) that if an L∞-morphism
of diﬀerential graded Lie algebras is a quasi-isomorphism, then it induces an isomorphism of deformation
functors. The theorem is proven. Q.E.D.
We would like to notice here that in the deﬁnition of the defor mation functor one can consider just
a formal pointed super Q-manifold (M, 0) (i.e. not a graded one), and m could be a ﬁnite-dimensional
nilpotent diﬀerential super commutative associative non- unital algebra.
