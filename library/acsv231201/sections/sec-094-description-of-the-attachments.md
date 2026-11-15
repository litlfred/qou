---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-094-description-of-the-attachments
section_title: "Description of the attachments"
section_number: null
pages: 541-545
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
523
Proof of Theorem D.13
Apply Thom’s Isotopy Lemma with manifolds P =
R and M = C∗
d, stratiﬁed space Z = X ∩h−1(a −ε, b + ε), and mapping
π = h. If h : X →R has no critical values in [a, b] then it has no critical
values in [a −ε, b + ε], hence h is a submersion on each stratum of X. The
conclusion of the lemma is that the level surfaces of h are ﬁbers of a local
product bundle, hence the ﬂow ˜V witnesses a strong deformation retraction of
X≤b onto X≤a.
□
To conclude this section, we show how Thom’s Isotopy Lemma can be used
to derive the local product topological structure of stratiﬁed spaces.
Proof of Theorem D.9
Let Z be a stratiﬁed space in Rd and let S be a stratum
of dimension k, with •S denoting a closed tubular neighborhood of S in Rd and
π : •S →S denoting the projection map. Then •S is a manifold with boundary
oS and an interior which we denote (•S)◦. If the tubular neighborhood was
chosen suﬃciently small, then X = Z ∩•S is naturally stratiﬁed with strata
of the form W ∩(•S)◦and W ∩oS, where W runs over strata whose closure
contains S.
The mapping π on X satisﬁes the conditions of Thom’s isotopy lemma. Con-
sequently, its normal slice N = π−1(p) ∩Z is stratiﬁed by its intersection with
the strata of X. Taking Up to be a small ball around p in the stratum S that con-
tains p, there is a stratum-preserving homeomorphism, smooth in each stratum,
given by π−1(Up)∩Z  Up×N. Since π−1(Up) is a neighborhood of p in Z, we
have shown that each stratum has a neighborhood that is locally a topological
product of a k-ball Up with the normal slice.
□
D.3 Description of the attachments
Let V∗denote the intersection V ∩Cd
∗of an aﬃne algebraic hypersurface V
with Cd
∗, and let M = Cd
∗\ V. We return to our plan to use Morse theory
to ﬁnd generators for Hd(M). Because we may want to describe either M or
V∗, depending on the situation, results in the literature are often stated in two
parts, so as to cover both cases, and we continue to adhere to this. For what
follows we ﬁx a Whitney stratiﬁcation {Sα : α ∈I} of the pair (Cd
∗, V∗) as
in Proposition D.11, so that M will be the unique stratum of dimension 2d.
The function h = h ˆr is assumed to be a Morse function and the space X may
denote either V∗or M. The point p denotes a stratiﬁed critical point for h in
the stratum S, and we let N = Np(V) denote the complex normal space to V∗
at p.
524 Stratification and stratified Morse theory

The tangential Morse data is defined in terms of p and S, regardless of
whether X = V, or X = M.

Definition D.17 (tangential Morse data). The tangential Morse data at p is
the homotopy type of the pair (B*, 0B“), where J is the Morse index of hls at
p and B* denotes the ball of dimension 2. By Theorem C.28, this is the Morse
data at p for the height function hls on the smooth manifold S.

The normal Morse data is defined in terms of the intersection of X with a
slice normal to the stratum S, localized to the point p. If D is an arbitrarily
small disk in N,(V) centered at p then the normal slice at p is N(X) := XO D.
To visualize this, it sometimes helps to picture the normal link L£(X) at p, de-
fined by L£(X) := XM 6D. When X = ‘V,, the normal slice N(X) is homeomor-
phic to a cone over £(X) from the point p. In particular, N(X) is contractible.
When X = M the point p is absent from the normal slice, which then retracts
onto £(X), hence N(X) ~ L£(X).

Example D.18. Let V be the union of two complex planes in complex 3-space
meeting at the line S and let p be a point on S. This line is the stratum con-
taining p, and the tangent space at p or any other point on S is the translation
of S to the origin. The normal space N,(‘V) at p (or any other point on S) is
the complex two-space orthogonal to S.

First consider the case X = ‘V,. The intersection of X with a normal plane
to S at p is two complex lines meeting at p. The normal slice N(X) is the inter-
section of this with a ball around p, and thus is two disks joined by identifying
their centers. The link £(X) = XN dD is the union of two disjoint circles, each
on one of the complex lines, and the normal slice N(X) is the cone over these
circles.

Alternatively, if X¥ = M then £(X) = XM OD is the complement of two
intersecting lines in a small bi-disk, which is the product of two punctured
disks. Each punctured disk retracts to its boundary, so the four-dimensional
space N(X) retracts to the three-dimensional space £(X), which retracts to a
two-dimensional torus $! x S!. 4

Definition D.19 (normal Morse data). Let X be V, or M. The normal Morse
data for X at p is defined to be the homotopy type of the pair

(NOX) NAc e,¢+ ED), NX)NN (+8), (D.3.1)

where the disk D in the definition of N(X) is sufficiently small, and ¢ is a suf-
ficiently smaller positive number. It is proved in [GM88] that these homotopy
types are the same for all D and « sufficiently small.
D.3 Description of the attachments
525
Example D.20. Suppose that V∗is a smooth algebraic hypersurface near one
of its points p.
(1) If X = V then N(X) is the single point p. Formally, the homotopy type is
that of ({p}, ∅).
(2) If X = M then N(X) has the homotopy type of (D\0, q), where D is a small
disk and q is a point on the boundary of D. This is the reduced homotopy
type of a circle, cyclic in dimension 1 and null in every other dimension.◁
The following theorem is stated for the case X = V∗in [GM88, Theo-
rem SMT B on page 8] and for the case X = M in [GM88, unnamed theorem
on page 12]; the equivalent characterizations of the homotopy type are stated
in [GM88, pages 7, 66–67, 120–122].
Theorem D.21 (attachments are determined by Morse data). Let X be either
V∗or M with a Whitney stratiﬁcation as above, and let p be a critical point
for h in a stratum S with critical value c = h(p).
1. The homotopy type of the attachment at p is the product, in the category of
pairs, of the normal and tangential Morse data as given in Deﬁnitions D.19
and D.17.
2. The tangential data for a stratum of codimension k is always the reduced
homology of a (d −k)-sphere: rank 1 in dimension (d −k) and vanishing
otherwise.
3. The normal data has the following characterizations.
(i) When X = V∗, the normal data is homotopy equivalent to the pair
(Cone(ℓ−), ℓ−), where Cone(Y) is the topological quotient Y×[0, 1] / Y×
{1} and ℓ−is the lower halﬂink deﬁned as the level set of N(X) at height
c −ε for suﬃciently small ε > 0.
(ii) When X = M, the normal data is homotopy equivalent to the pair
(L+(X), ∂L+(X)), where L+(X) is the part of L(X) at height at least c.
(iii) When X = M, the normal data is also homotopy equivalent to the
pair (L+(X), L0(X)), where L0(X) is the intersection of L(X) with the
level set {z ∈X : h(z) = c}.
□
Remark. Goresky and MacPherson have this to say [GM88, page 9]: “Theo-
rem SMT Part B, although very natural and geometrically evident in examples,
takes 100 pages to prove rigorously in this book.”
Example D.22 (complement of S 2 in R3). Let X be the complement of the unit
526
Stratiﬁcation and stratiﬁed Morse theory
Figure D.6 The complement of the unit sphere up to height +1/2.
sphere S ⊆R3. The function h(x, y, z) = z extends to a proper height function
on R3, which is Morse with respect to the stratiﬁcation {S, X}.
There are no critical points in X but there are two in S : the South pole and
the North pole. In each case the normal slice is an interval minus a point, so the
normal data is homotopy equivalent to (S 0, S 0
−), where S 0 is two points, one
higher than the other, and S 0
−is the lower of the two points. For the South pole,
which has Morse index 0, the tangential data is a point, so the attachment is
(S 0, S 0
−), which is the addition of a disconnected point. Figure D.6 illustrates
that for −1 < a < 1, the space X≤a is in fact the union of two contractible
components. The North pole has Morse index 2, so the tangential data at the
North pole is (D2, ∂D2), a polar cap modulo its boundary. Taking the product
with the normal data gives two polar caps modulo all of the lower one and
the boundary of the upper one. This is the upper polar cap sewn down along
its boundary, the boundary being a point in one of the components. Thus, one
component becomes a sphere and the other remains contractible.
◁
Suppose we have a closed space Y ⊂Rd whose complement X we view as
a stratiﬁed space with Morse function h. If p is a critical point for h in some
stratum S then there is a local coordinatization of Y as S × Bp, where Bp is a
small ball of dimension d −k and k is the dimension of S . The set Bp \ Y is
this ball minus the origin, so it is a cone over L(p) with vertex p. Any chain in
Bp \ Y may be brought arbitrarily close to p.
