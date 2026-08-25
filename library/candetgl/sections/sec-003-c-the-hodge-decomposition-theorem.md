---
doc_id: candetgl
doc_title: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics"
section_id: sec-003-c-the-hodge-decomposition-theorem
section_title: "The Hodge decomposition theorem"
section_number: C
pages: 5-7
source_pdf: candetgl.pdf
source_sha256: d788af715428b8b2
doc_brief: "The Biot–Savart operator for application to knot theory, fluid dynamics, and plasma physics — 18 sections: INTRODUCTION; PRELIMINARIES; Fuller,9 Bauer, Crick, and"
---
In this section we present the Hodge Decomposition Theorem for vector ﬁelds on bounded
domains in R3, which we will use throughout the paper. Although we state it below for the space
VF~V! of smooth vector ﬁelds on V with the usual L2 inner product, it holds just as well for the
L2 completions of VF ~V! and of the various subspaces described below.
The papers of Weyl 41 and Friedrichs, 42 the notes of Blank, Friedrichs, and Grad, 43 and the
book of Schwarz44 are all good references; an exposition of this theorem in the form given below
appears in Ref. 45.
Hodge Decomposition Theorem: We have a direct sum decomposition of VF (V) into ﬁve
mutually orthogonal subspaces ,
VF~V!5FK % HK % CG % HG % GG,
with
ker curl 5 HK % CG % HG % GG,
image grad 5 CG % HG % GG,
image curl 5FK % HK % CG,
ker div 5FK % HK % CG % HG,
where
FK5Fluxless Knots 5$„"V50, V"n50, all interior ﬂuxes 50%,
HK5Harmonic Knots 5$„"V50, „ 3V50, V"n50%,
CG5Curly Gradients 5$V5„ w, „"V50, all boundary ﬂuxes 50%,
HG5Harmonic Gradients 5$V5„ w, „"V50, w locally constant on ]V%,
GG5Grounded Gradients 5$V5„ w, wu]V50%,
and furthermore,
HK>H1~V;R!>H2~V,]V;R!>Rgenus of ]V,
HG>H2~V;R!>H1~V,]V;R!>R~# components of ]V!2~# components of V!.
We need to explain the meanings of the conditions which appear in the statement of this
theorem.
The outward pointing unit vector ﬁeld orthogonal to ]V is denoted by n, so the condition
V"n50 indicates that the vector ﬁeld V is tangent to the boundary of V.
879J. Math. Phys., Vol. 42, No. 2, February 2001 The Biot –Savart operator
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
Let S stand generically for any smooth surface in V with ]S,]V. Earlier, when commenting
on the statement of Theorem C, we indicated this by writing ( S,]S),(V,]V). Now, orient S by
picking one of its two unit normal vector ﬁelds n. Then, for any vector ﬁeld V on V, we can deﬁne
the ﬂux of V through S to be the value of the integral F5*SV"n d(area).
Assume that V is divergence-free and tangent to ]V. Then the value of this ﬂux depends only
on the homology class of S in the relative homology group H2(V,]V;Z). For example, if V is an
n-holed solid torus, then there are disjoint oriented cross-sectional disks S1 ,..., Sn , positioned so
that cutting V along these disks will produce a simply-connected region. The ﬂuxes F1 ,..., Fn of
V through these disks determine the ﬂux of V through any other cross-sectional surface.
If the ﬂux of V through every smooth surface S in V with ]S,]V vanishes, we say ‘‘all
interior ﬂuxes50.’’ Then,
FK5$Ve VF~V!:„"V50, V"n50, all interior ﬂuxes 50% ~2.5!
will be the subspace of ﬂuxless knots, already mentioned when explaining the statement of Theo-
rem C.
The subspace,
HK5$Ve VF~V!:„"V50, „ 3V50, V"n50% ~2.6!
of harmonic knots is isomorphic to the absolute homology group H1(V;R) and also, via Poincare´
duality, to the relative homology group H2(V,]V;R), and is thus a ﬁnite-dimensional vector
space, with dimension equal to the genus of ]V.
The orthogonal direct sum of these two subspaces,
K~V!5FK% HK ~2.7!
is the subspace of VF ~V! consisting of all divergence-free vector ﬁelds deﬁned on V and tangent
to its boundary. These are the vector ﬁelds that represent current ﬂows in the standard versions of
the laws of Magnetostatics.
We called these vector ﬁelds ﬂuid knots in the Introduction, and pause to explain this termi-
nology. Given a knot in 3-space, we can choose a thin tubular neighborhood of the knot to be our
domain V, and then choose a divergence-free vector ﬁeld V in V, for example orthogonal to the
cross-sectional disks and hence tangent to the boundary. In this way, questions about the geometry
of the knot can sometimes proﬁtably be reformulated as questions about the vector ﬁeld V, our
‘‘ﬂuid knot.’’ We did exactly this in our paper
28 when deriving an upper bound for the writhing
number of a knot of given length and thickness.
If V is a vector ﬁeld deﬁned on V, we will say that all boundary ﬂuxes of V are zero if the ﬂux
of V through each component of ]V is zero. Then,
CG5$Ve VF~V!:V5„ w, „V50, all boundary ﬂuxes 50% ~2.8!
will be called the subspace of curly gradients because these are the only gradients which lie in the
image of curl.
Next we deﬁne the subspace of harmonic gradients,
HG5$Ve VF~V!:V5„ w, „V50, w locally constant on ]V%, ~2.9!
meaning that w is constant on each component of ]V. This subspace is isomorphic to the absolute
homology group H2(V;R) and also, via Poincare ´ duality, to the relative homology group
H1(V,]V;R), and is hence a ﬁnite-dimensional vector space, with dimension equal to the number
of components of ]V minus the number of components of V.
The deﬁnition of the subspace of grounded gradients,
GG5$Ve VF~V!:V5„ w, wu]V50%, ~2.10!
is self-explanatory.
880 J. Math. Phys., Vol. 42, No. 2, February 2001 Cantarella, DeTurck, and Gluck
 This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to  IP:
129.215.149.98 On: Sat, 10 May 2014 06:24:42
A vector ﬁeld V belongs to the subspace HG % GG of VF~V! if and only if it is the gradient
of a smooth function w on V which is constant on each component of ]V, or equivalently, is a
gradient vector ﬁeld which is orthogonal to ]V. Theorem B asserts that these vector ﬁelds form the
kernel of the Biot–Savart operator.
The ﬁve orthogonal direct summands of VF ~V! can be characterized as follows:
FK5~ker curl !’ ,
HK5~ker curl ! ø~image grad !’ ,
CG5~image grad! ø~image curl !,
HG5~ker div ! ø~image curl !’ ,
GG5~ker div !’ .
These characterizations bear witness to the geometric and analytic signiﬁcance of the summands.
We end this section with examples of vector ﬁelds from each of the ﬁve summands.
