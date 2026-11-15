---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-032-52-looking-through-a-magnifying-glass
section_title: "Looking through a magnifying glass"
section_number: 5.2
pages: 19-22
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
The deﬁnition of the compactiﬁcation given in the previous subsection is not descriptive. We are going
to explain an intuitive idea underlying a direct construction of the compactiﬁcation Cn,m as a manifold with
corners. For more formal treatment of compactiﬁcations of conﬁguration spaces we refer the reader to [FM]
(for the case of smooth algebraic varieties).
Let us try to look through a magnifying glass, or better through a microscope with arbitrary magniﬁ-
cation, on diﬀerent parts of the picture formed by points on H ∪R ⊂C, and by the line R ⊂C. Here we
use Euclidean geometry on C ≃R2 instead of Lobachevsky geometry.
Before doing this let us ﬁrst consider the case of a conﬁguration on R2 ≃C, i.e. without the horizontal
line R ⊂C. We say that the conﬁguration (p1, . . . , pn) is in standard position iﬀ
1) the diameter of the set {p1, . . . , pn} is equal to 1, and,
2) the center of the minimal circle containing {p1, . . . , pn} is 0 ∈C.
It is clear that any conﬁguration of n pairwise distinct points in the case n ≥2 can be uniquely put
to standard position by an element of group G(2). The set of conﬁgurations in standard position gives a
continuous section scont of the natural projection map Confn−→Cn.
For a conﬁguration in standard position there could be several domains where we will need magniﬁcation
in order to see details. These domains are those where at least two points of the conﬁguration come too
close to each other.
After an appropriate magniﬁcation of any such domain we again get a stable conﬁguration (i.e.the
number of points there is at least 2).
Then we can put it again in standard position and repeat the
procedure.
In such a way we get an oriented tree T with one root, and leaves numbered from 1 to n. For example,
the conﬁguration on the next ﬁgure
19
. ..
..
.
2
1
3
4
5
6
gives the tree
.
.
.
.
.
.
1
root
2
.
3
4
5
6
.
.
.
For every vertex of tree T except leaves, we denote by Star(v) the set of edges starting at v.
For
example, in the ﬁgure from above the set Star(root) has three elements, and sets Star(v) for other three
vertices all have two elements.
Points in Cn close to one which we consider, can be parametrized by the following data:
a) for each vertex v of T except leaves, a stable conﬁguration cv in standard position of points labeled
by the set Star(v),
b) for each vertex v except leaves and the root of the tree, the scale sv > 0 with which we should put a
copy of cv instead of the corresponding point pv ∈C on stable conﬁguration cu where u ∈VT is such that
(u, v) ∈ET .
More precisely, we act on the conﬁguration cv by the element (z 7→svz + pv) of G(2).
Numbers sv are small but positive. The compactiﬁcation Cn is achieved by formally permitting some
of scales sv to be equal to 0.
In this way we get a compact topological manifold with corners, with strata CT labeled by trees T (with
leaves numbered from 1 to n). Each stratum CT is canonically isomorphic to the product Q
v CStar(v) over all
vertices v except leaves. In the description as above points of CT correspond to collections of conﬁgurations
with all scales sv equal to zero. Let us repeat: as a set Cn coincides with
G
trees T
Y
v∈VT \{leaves}
CStar(v) .
In order to introduce a smooth structure on Cn, we should choose a Σn-equivariant smooth section
ssmooth of the projection map Confn−→Cn instead of the section scont given by conﬁgurations in standard
position. Local coordinates on Cn near a given point lying in stratum CT are scales sv ∈R≥0 close to zero
and local coordinates in manifolds CStar(v) for all v ∈VT \ {leaves}. The resulting structure of a smooth
manifold with corners does not depend on the choice of section ssmooth.
The case of conﬁgurations of points on H ∪R is not much harder. First of all, we say that a ﬁnite
non-empty set S of points on H ∪R is in standard position iﬀ
20
1) the projection of the convex hull of S to the horizontal line R ⊂C ≃R2 is either the one-point set
{0}, or it is an interval with the center at 0,
2) the maximum of the diameter of S and of the distance from S to R is equal to 1.
It is easy to see that for 2n + m ≥2 (the stable case) any conﬁguration of n points on H and m points
on R can be put uniquely in standard position by an element of G(1). In order to get a smooth structure,
we repeat the same arguments as for the case of manifolds Cn.
Domains where we will need magniﬁcation in order to see details, are now of two types. The ﬁrst case is
when at least two points of the conﬁguration come too close to each other. We want to know whether what
we see is a single point or a collection of several points. The second possibility is when a point on H comes
too close to R. Here we want also to decide whether what we see is a point (or points) on H or on R.
If the domain which we want to magnify is close to R, then after magniﬁcation we get again a stable
conﬁguration which we can put into the standard position. If the domain is inside H, then after magniﬁcation
we get a picture without the horizontal line in it, and we are back in the situation concerning Cn′ for n′ ≤n.
It is instructional to draw low-dimensional spaces Cn,m. The simplest one, C1,0 = C1,0 is just a point.
The space C0,2 = C0,2 is a two-element set. The space C1,1 is an open interval, and its closure C1,1 is a
closed interval (the real line R ⊂C is dashed on the picture):
.
.
0 = q1
~~
.
.
.
The space C2,0 is diﬀeomorphic to H \ {0 + 1 · i}. The reason is that by action of G(1) we can put point
p1 to the position i = √−1 ∈H. The closure C2,0 can be drawn like this:
.
p 1
=
i
.
.
or like this:
The Eye
.
.
Forgetting maps (see the end of 5.1) extend naturally to smooth maps of compactiﬁed spaces.
21
