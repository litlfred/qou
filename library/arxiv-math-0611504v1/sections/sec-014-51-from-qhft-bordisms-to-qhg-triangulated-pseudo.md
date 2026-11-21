---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-014-51-from-qhft-bordisms-to-qhg-triangulated-pseudo
section_title: "From QHFT bordisms to QHG-triangulated pseudomanifolds"
section_number: 5.1
pages: 22-24
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
a pseudomanifold Z(B). Fill each tunnel boundary component of ˜Y with a solid tube, thus recovering
a copy of the manifold Y . The cores of the solid tubes make a parallel unframed copy λ′′ of L. We
deﬁne Z(B) as the result of collapsing to one point each component of λ′′. In other words, we glue
to each tunnel component of ˜Y the oriented topological cusp ˆC = B × [0, +∞]/(B × {∞}) with base
equal to either B = S1 × [−1, 1] or B = S1 × S1.
Next we describe a procedure to convert Z(B) to a distinguished QHG-triangulated pseudomanifold.
We refer to the notions introduced in Subsection 2.4.
We say that a branched triangulation (T, b) of B as above is admissible if B ∩∂± ˜Y and the tangles
λ, λ′ are covered by the 1-skeleton. We denote ( ˆT,ˆb) the branched triangulation of ˆC, where ˆT is
QUANTUM HYPERBOLIC GEOMETRY
23
the cone over T from the non manifold point, say ∞, and ˆb extends b so that ∞is a pit for every
branched tetrahedron of ˆT. Assume we are given an idealizable PB+(2, C)-valued cocycle z on an
admissible triangulation of B. The idealization of z determines for each 2-simplex of B a face of
an ideal hyperbolic tetrahedron with further vertex at ∞(see Figure 12, where opposite vertical
triangles are identiﬁed). Since the fundamental group of B is Abelian, the resulting family of oriented
ideal hyperbolic tetrahedra actually makes an I-triangulation ( ˆT ,ˆb, w), which we call an I-cusp. By
conjugating if necessary, we see that I-cusps make sense also when z takes values more generally in
PSL(2, C). We get ﬂattenings similarly as in Lemma 2.9: at a corner of a 2-simplex formed by edges
el and er we put the diﬀerence of the logarithms of the vectors in C associated by the idealization to
el and er, respectively.
Figure 11.
An I-cusp.
Deﬁnition 5.1. A D-triangulation of B = ( ˜Y , ˜LF, ρ, α±) consists of a 4-uple K = (K, ¯H, b, z) where:
(a) (K, b) is a branched triangulation of ˜Y extending that on ∂± ˜Y , and inducing an admissible cusp
base triangulation at each tunnel component of ˜LF.
(b) The 1-dimensional subcomplex ¯H = H ∪H′ of K is ambiently isotopic to the tangle ¯λ = λ ∪λ′,
and ¯H contains all the vertices of K.
(c) z is an idealizable PSL(2, C)-valued 1-cocycle on (K, b) such that:
(i) the conjugacy class of PSL(2, C)-representations of π1( ˜Y ) associated to z coincides with ρ;
(ii) the (+)-exponential I-parameters given by the restriction of z to ∂± ˜Y coincide with that of the
objects α−∪α+ (see Deﬁnition 4.1).
(d) the restriction of z to each vertical tunnel component of ˜LF takes values in the Borel subgroup
PB+(2, C) of PSL(2, C).
For any D-triangulation K = (K, ¯H, b, z) of B we get a distinguished I-triangulation KI = (K, ¯H, b, w)
of (Z(B), ¯λ) by gluing the idealization of K with the I-cusp given by the cocycle at each tunnel
component. Note that ¯H contains all the vertices of KI that are manifold points.
Deﬁnition 5.2. We say that T (B) = (KI, f, c) = (K, ¯H, b, w, f, c) is a distinguished ﬂat/charged
I-triangulation of (Z(B), ¯λ) if it satisﬁes Deﬁnition 2.10, and at every boundary edge of Z(B) the
total (classical or quantum) log-branch of (KI, f, c) of (7) coincides with the (classical or quantum)
Log-I-parameter of the boundary object α−∪α+.
Recall the cohomological weights from section 2.4. These notions still make sense for distinguished
ﬂat/charged I-triangulations, where the homology of ∂T0 is replaced with that of the tunnel compo-
nents ˜LF. Since we have weights (hf, kf) for log-branches and (hc, kc) for charges at the same time,
we will denote them (h, k) = ((hf, hc), (kf, kc)). We can also deﬁne, in the very same way, boundary
weights kf ∈H1(∂˜Y ; C), but these are completely encoded by α±. We have:
Theorem 5.3. For every bordism B = ( ˜Y , ˜LF, ρ, α±) and every (h, k) ∈H1( ˜Y ; Z/2Z) × H1(˜LF; C)
satisfying the properties (14), there are distinguished ﬂat/charged I-triangulations T (B) of Z(B) with
weight (h, k), and any two are QHG-isomorphic.
24
ST´EPHANE BASEILHAC1 AND RICCARDO BENEDETTI2
Proof. The existence of distinguished I-triangulations KI of Z(B) follows from a tedious but straight-
forward generalization of Theorem 4.13 in [4]. Global ﬂattenings and integral charges with arbitrary
weight exist on the double DKI of KI by the results recalled with Theorem 2.12.
Consider the (+)-Log-I-parameters {W ±(z)(e)}e at α±. They are in one-one correspondence with the
interior edges of the corresponding e-triangulations, which is less than the cardinality of the families
m and n used to deﬁned ﬂattenings and charges in Deﬁnition 4.1. Hence any family of determinations
of the logarithms of the W ±(z)(e) is a system of (+)-Log-I-parameters. Also, Lemma 2.9 implies that
any system of (+)-Log-I-parameters at α± extends to a distinguished ﬂat/charge I-triangulation of
the pseudo manifold obtained from the trivial cylinders over ∂± ˜Y by collapsing to a point each annulus
of ∂(∂± ˜Y ) × [−1, 1].
This means that any QHFT surface bounds a QHFT bordism, and that for the bordism B there are
ﬂat/charges on DKI whose restriction to KI induce the Log-I-parameters of α±. Hence we get global
ﬂat/charges as in Deﬁnition 5.2. In fact the aﬃne spaces of ﬂat/charges on DKI project onto that
on KI compatible with α± (see the end of section 2). Then, the Mayer-Vietoris exact sequence in
cohomology for the triad (DKI, KI, −KI) shows that (h, k) is induced by some weight on DKI. As
we can choose the latter arbitrarily, this concludes the proof of the ﬁrst claim.
The second is harder, but follows strictly from the arguments in the proof of Theorem 6.8 (2) in [5].
The only new ingredient is the presence of I-cusps, which mimic the ends of cusped manifolds treated
in that paper.
✷
An alternative characterization of classical/quantum log-branches of distinguished ﬂat/charged I-
triangulations T (B) follows from Remark 2.11.
