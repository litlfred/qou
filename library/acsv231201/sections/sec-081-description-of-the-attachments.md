---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-081-description-of-the-attachments
section_title: "Description of the attachments"
section_number: null
pages: 541-551
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
Proof of Theorem D.13 Apply Thom’s Isotopy Lemma with manifolds P =
R andM = C∗
d, stratiﬁed space Z = X∩ h−1(a− ε, b + ε), and mapping
π = h. If h : X → R has no critical values in [ a, b] then it has no critical
values in [ a−ε, b +ε], hence h is a submersion on each stratum of X. The
conclusion of the lemma is that the level surfaces of h are ﬁbers of a local
product bundle, hence the ﬂow ˜V witnesses a strong deformation retraction of
X≤b onto X≤a. □
To conclude this section, we show how Thom’s Isotopy Lemma can be used
to derive the local product topological structure of stratiﬁed spaces.
Proof of Theorem D.9 Let Z be a stratiﬁed space inRd and letS be a stratum
of dimension k, with•S denoting a closed tubular neighborhood ofS inRd and
π :•S→S denoting the projection map. Then•S is a manifold with boundary
oS and an interior which we denote ( •S)◦. If the tubular neighborhood was
chosen suﬃciently small, then X = Z∩•S is naturally stratiﬁed with strata
of the form W∩ (•S)◦ and W∩ oS, where W runs over strata whose closure
containsS.
The mappingπ on X satisﬁes the conditions of Thom’s isotopy lemma. Con-
sequently, its normal slice N = π−1(p)∩ Z is stratiﬁed by its intersection with
the strata of X. TakingUp to be a small ball aroundp in the stratumS that con-
tainsp, there is a stratum-preserving homeomorphism, smooth in each stratum,
given byπ−1(Up)∩Z  Up×N. Sinceπ−1(Up) is a neighborhood ofp in Z, we
have shown that each stratum has a neighborhood that is locally a topological
product of a k-ball Up with the normal slice. □
D.3 Description of the attachments
LetV∗ denote the intersectionV∩ Cd
∗ of an aﬃne algebraic hypersurfaceV
with Cd
∗, and let M = Cd
∗\V . We return to our plan to use Morse theory
to ﬁnd generators for Hd(M). Because we may want to describe either M or
V∗, depending on the situation, results in the literature are often stated in two
parts, so as to cover both cases, and we continue to adhere to this. For what
follows we ﬁx a Whitney stratiﬁcation {Sα : α∈ I} of the pair (Cd
∗,V∗) as
in Proposition D.11, so that M will be the unique stratum of dimension 2 d.
The function h = h ˆr is assumed to be a Morse function and the space X may
denote eitherV∗ orM. The pointp denotes a stratiﬁed critical point for h in
the stratumS, and we let N = Np(V) denote the complex normal space toV∗
atp.
524 Stratiﬁcation and stratiﬁed Morse theory
The tangential Morse data is deﬁned in terms of p andS, regardless of
whether X =V∗ or X =M.
Deﬁnition D.17 (tangential Morse data) . The tangential Morse data atp is
the homotopy type of the pair ( Bλ,∂ Bλ), whereλ is the Morse index of h|S at
p and Bλ denotes the ball of dimensionλ. By Theorem C.28, this is the Morse
data atp for the height function h|S on the smooth manifold S .
The normal Morse data is deﬁned in terms of the intersection of X with a
slice normal to the stratum S, localized to the point p. If D is an arbitrarily
small disk in Np(V) centered atp then the normal slice atp is N(X) := X∩ D.
To visualize this, it sometimes helps to picture the normal linkL(X) atp, de-
ﬁned byL(X) := X∩∂D. When X =V∗ the normal slice N(X) is homeomor-
phic to a cone overL(X) from the point p. In particular, N(X) is contractible.
When X =M the pointp is absent from the normal slice, which then retracts
ontoL(X), hence N(X)≃L (X).
Example D.18. LetV be the union of two complex planes in complex 3-space
meeting at the lineS and letp be a point onS. This line is the stratum con-
tainingp, and the tangent space atp or any other point onS is the translation
ofS to the origin. The normal space Np(V) atp (or any other point onS) is
the complex two-space orthogonal toS.
First consider the case X =V∗. The intersection of X with a normal plane
toS atp is two complex lines meeting atp. The normal slice N(X) is the inter-
section of this with a ball aroundp, and thus is two disks joined by identifying
their centers. The linkL(X) = X∩∂D is the union of two disjoint circles, each
on one of the complex lines, and the normal slice N(X) is the cone over these
circles.
Alternatively, if X =M thenL(X) = X∩∂D is the complement of two
intersecting lines in a small bi-disk, which is the product of two punctured
disks. Each punctured disk retracts to its boundary, so the four-dimensional
space N(X) retracts to the three-dimensional space L(X), which retracts to a
two-dimensional torus S 1× S 1. ◁
Deﬁnition D.19 (normal Morse data). Let X beV∗ orM. The normal Morse
data for X atp is deﬁned to be the homotopy type of the pair
(
N(X)∩ h−1([c−ε, c +ε]), N(X)∩ h−1(c +ε)
)
, (D.3.1)
where the disk D in the deﬁnition of N(X) is suﬃciently small, and ε is a suf-
ﬁciently smaller positive number. It is proved in [GM88] that these homotopy
types are the same for all D andε suﬃciently small.
D.3 Description of the attachments 525
Example D.20. Suppose thatV∗ is a smooth algebraic hypersurface near one
of its pointsp.
(1) If X =V then N(X) is the single point p. Formally, the homotopy type is
that of ({p},∅).
(2) If X =M then N(X) has the homotopy type of (D\0,q), where D is a small
disk andq is a point on the boundary of D. This is the reduced homotopy
type of a circle, cyclic in dimension 1 and null in every other dimension.◁
The following theorem is stated for the case X = V∗ in [GM88, Theo-
rem SMT B on page 8] and for the case X =M in [GM88, unnamed theorem
on page 12]; the equivalent characterizations of the homotopy type are stated
in [GM88, pages 7, 66–67, 120–122].
Theorem D.21 (attachments are determined by Morse data) . Let X be either
V∗ orM with a Whitney stratiﬁcation as above, and let p be a critical point
for h in a stratumS with critical value c = h(p).
1. The homotopy type of the attachment at p is the product, in the category of
pairs, of the normal and tangential Morse data as given in Deﬁnitions D.19
and D.17.
2. The tangential data for a stratum of codimension k is always the reduced
homology of a (d− k)-sphere: rank 1 in dimension (d− k) and vanishing
otherwise.
3. The normal data has the following characterizations.
(i) When X =V∗, the normal data is homotopy equivalent to the pair
(Cone(𝓁−),𝓁−), where Cone(Y) is the topological quotient Y×[0, 1]/ Y×
{1} and𝓁− is the lower halﬂink deﬁned as the level set ofN(X) at height
c−ε for suﬃciently smallε> 0.
(ii) When X =M, the normal data is homotopy equivalent to the pair
(L+(X),∂L+(X)), whereL+(X) is the part ofL(X) at height at least c.
(iii) When X =M, the normal data is also homotopy equivalent to the
pair (L+(X),L0(X)), whereL0(X) is the intersection ofL(X) with the
level set{z∈ X : h(z) = c}.
□
Remark. Goresky and MacPherson have this to say [GM88, page 9]: “Theo-
rem SMT Part B, although very natural and geometrically evident in examples,
takes 100 pages to prove rigorously in this book.”
Example D.22 (complement of S 2 inR3). Let X be the complement of the unit
526 Stratiﬁcation and stratiﬁed Morse theory
Figure D.6 The complement of the unit sphere up to height +1/2.
sphere S⊆ R3. The function h(x, y, z) = z extends to a proper height function
onR3, which is Morse with respect to the stratiﬁcation{S, X}.
There are no critical points in X but there are two in S : the South pole and
the North pole. In each case the normal slice is an interval minus a point, so the
normal data is homotopy equivalent to ( S 0, S 0
−), where S 0 is two points, one
higher than the other, andS 0
− is the lower of the two points. For the South pole,
which has Morse index 0, the tangential data is a point, so the attachment is
(S 0, S 0
−), which is the addition of a disconnected point. Figure D.6 illustrates
that for−1 < a < 1, the space X≤a is in fact the union of two contractible
components. The North pole has Morse index 2, so the tangential data at the
North pole is ( D2,∂ D2), a polar cap modulo its boundary. Taking the product
with the normal data gives two polar caps modulo all of the lower one and
the boundary of the upper one. This is the upper polar cap sewn down along
its boundary, the boundary being a point in one of the components. Thus, one
component becomes a sphere and the other remains contractible. ◁
Suppose we have a closed space Y⊂ Rd whose complement X we view as
a stratiﬁed space with Morse function h. Ifp is a critical point for h in some
stratum S then there is a local coordinatization of Y as S× Bp, where Bp is a
small ball of dimension d− k and k is the dimension of S . The set Bp\ Y is
this ball minus the origin, so it is a cone over L(p) with vertexp. Any chain in
Bp\ Y may be brought arbitrarily close top.
D.4 Stratiﬁed Morse theory for complex manifolds 527
D.4 Stratiﬁed Morse theory for complex manifolds
If X is a complex variety then the Morse data has an alternate description obey-
ing the complex structure ofX. Let S be a stratum containing a critical pointp,
let N(p) be a small ball in the normal space to S atp, and deﬁne the complex
linkL(S ) to be the intersection of X with a generic hyperplane A⊆ N(p) that
comes suﬃciently close to p but does not contain it. It is shown in [GM88,
page 16] that the normal Morse data atp∈ X is given in terms ofL(S ) by the
pair
(ConeR(L(S )),L(S )), (D.4.1)
where ConeR(L(S )) denotes the real cone overL(S ). In other words, the nor-
mal link has the homotopy type of the pair (L(S )×[0, 1]/L(S )×{1},L(S )×
{0}), where the real cone (the ﬁrst space of this pair) is deﬁned as a quotient.
Suppose that X has dimension d, the stratum S has dimension k, and the
ambient space has dimension n (all dimensions are complex). Then N(p) is a
complex space of dimension n− k, its intersection with a generic hyperplane
has dimension n− k− 1, and thus
dimCL(S ) = d− k− 1.
In fact the homeomorphism type of the complex link depends on X and S but
not on the individual choice of p∈ S , nor the ambient space, nor the choice of
proper Morse function h on the stratiﬁed space X (see [GM88, Section II:2.3]).
Suppose next that X is the complement of a d-dimensional variety in Cd+1.
A formula for the Morse data at a point p< X in a stratum S is given [GM88,
page 18] by
(L(S ),∂L(S ))× (B1,∂ B1), (D.4.2)
where B1 is a real interval (which can be interpreted as a 1-ball).
Theorem D.23. (i) If X is a complex analytic variety of dimension d then X
has the homotopy type of a cell complex of dimension at most d. (ii) If X is the
complement in a domain ofCn of a complex variety of dimension d then X has
the homotopy type of a cell complex of dimension at most 2n− d− 1.
Remark. The proof of this result in [GM88] is somewhat di ﬃcult, mostly
due to the necessity of establishing the invariance properties of the complex
link. The result, however, is very useful. For example, suppose that X is the
complement of the zero set of a polynomial in n variables. Then d = n− 1
and the homotopy dimension of X is at most n. Note that X may have strata
of any complex dimension j≤ d, and that the complement of a j-dimensional
complex space in Cn has homotopy dimension 2 n− 2 j. The theorem asserts
528 Stratiﬁcation and stratiﬁed Morse theory
that the complex structure prevents the dimensions of contributions at strata
of dimensions j < d from exceeding the dimension of the contributions from
d-dimensional strata.
Proof sketch (i) Assume that the variety is embedded inCn and that the height
function h has been chosen to be the square of the distance from a generic
point. We examine the homotopy type of the attachment at a pointp in a stra-
tum of dimension k. It suﬃces, as in the proof of Theorem C.39, to show that
each attachment has the homotopy type of a cell complex of dimension at most
d.
First, if k = d (p is a smooth point) then, as was observed prior to stating
Theorem C.39, the Morse index of h is at most d. The attachment is ( Bi,∂ Bi)
where i is the Morse index of h, so in this case the homotopy type of the
attachment is at most d.
When k < d, we proceed by induction on d. The tangential Morse data has
the homotopy type of a cell complex of dimension at mostk. The spaceL(S ) is
a complex analytic space, with complex dimension one less than the dimension
of the normal slice, meaning it has dimensiond−k−1. The induction hypothesis
shows that the homotopy dimension of L(S ) is at most d− k− 1. Taking the
cone brings the dimension to at most d− k and adding the dimension of the
tangential data brings this up to at most d, completing the induction.
(ii) When X is the complement of a variety V, still assuming h to be the
square of the distance to a generic point, all critical points with respect to
the pair ( X,V) are contained in V, not in X. Again it su ﬃces to show that
the attachments all have homotopy dimension at most 2 n− d− 1, and again
we start with the case k = d. Here p is a smooth point of V, so the normal
data is the same as for the complement of a point in Cn−d, which is S 2(n−d)−1.
The tangential data has homotopy dimension at most d, so the attachment has
dimension at most 2n− d− 1.
When k < d, we again proceed by induction on d. The link L(S ) is the
complement ofV∩ A in a generic hyperplaneA. We have directly dimC N(p) =
n− k and dimC(A) = n− k− 1, and dimC(V∩ A) = d− k− 1 becauseV has
codimension n− d, intersects A generically, and k ≤ d− 1. The induction
hypothesis applied to the complement ofV∩ A in A shows thatL(S ) has the
homotopy type of a cell complex of dimension at most 2(n− k− 1)− (d− k−
1)− 1 = 2n− d− k− 2. The normal Morse data is the product of this with a
1-complex, hence it has homotopy dimension at most 2n− d− k− 1, and taking
the product with the tangential Morse data brings the dimension up to at most
2n− d− 1, completing the induction. □
It is useful for the main part of this book to summarize the results from this
D.4 Stratiﬁed Morse theory for complex manifolds 529
section for complements of manifolds, applying the K¨unneth formula to obtain
a description of the attachments in terms of speciﬁc relative cycles.
Deﬁnition D.24 (quasi-local cycles). A (relative or absolute) local cycle at a
pointp is a cycle which may be deformed so as to be in an arbitrarily small
neighborhood of p. Given a stratiﬁed space with Morse function h, a quasi-
local cycle at a critical point p of the stratiﬁcation is a cycle C⊥×C‖, where
C‖ is a disk in S on which h is strictly maximized at p, Bp is a small ball
aroundp in the normal slice, C⊥ is a local cycle in ( Bp\ Y, (Bp\ Y)≤h(p)−ε),
and the product is taken in any local coordinatization of a neighborhood of p
by Bp× S .
Theorem D.25. Let X be the complement of a complex variety of dimension d
inCd+1. Then X may be built by attaching spaces that are homotopy equivalent
to cell complexes of dimension at most d+ 1. Consequently, Hd(X) has a basis
of quasi-local cycles which may be described asB ={σp,i}p,i, wherep ranges
over critical points in diﬀerent strata, and eachσp,i∈ Xc,p. For each ﬁxedp,
the projectionπ∗ : Xc,p→ (Xc,p, X≤c−ε) = Xp,loc maps the set{σp,i} to a basis
for the relative homology group Hd(Xp,loc). □
Notes
The idea to use Morse theory to evaluate integrals was not one of the original
purposes of Morse theory. Nevertheless, the utility of Morse theory for this
purpose has been known for over 50 years. Much of the history appears diﬃcult
to trace: the present authors learned it from Yuliy Baryshnikov, who related it
as mathematical folklore from Arnold’s seminar. The smooth Morse theory
in this chapter (and some of the pictures) is borrowed from Milnor’s classic
text [Mil63]. Stratiﬁed Morse theory is a relatively new ﬁeld, in which the
seminal text is [GM88]; most of our understanding came from this text.
The result usually quoted as the description of the attachment in the strati-
ﬁed case (a stratiﬁed version of Theorem C.28) is an unnumbered result named
“Theorem” in [GM88, Section 3.12]. This computes the change in topology of
a stratiﬁed space X on which the function h is proper. When h is a continuous
function on Cd
∗, this requires the subset X to be closed. We are chieﬂy inter-
ested in the space X =Vc which is not closed. Dealing with nonproper height
functions requires two extra developmental steps. The ﬁrst is to develop a sys-
tem for keeping track of the change in topology of the complement of a closed
space up to a varying height cutoﬀ. This computation is similar to the one for
the space itself. Goresky and MacPherson state the two results together in a
530 Stratiﬁcation and stratiﬁed Morse theory
later version of the “Main Theorem” of [GM88], and we have followed their
example, stating the results together in Theorem D.21. The second way h can
fail to be proper occurs at inﬁnity. The results of [GM88] across the height
interval [a, b] can be extended to unbounded spaces when there are no critical
points at inﬁnity with heights in [ a, b]. This was the motivation for the results
on CPAI derived in [BMP22], which we use in Chapter 7.
Additional exercises
Exercise D.4 (Whitney umbrella). Let f (x, y, z) = x2 + y2z be the polynomial
whose real varietyV f forms the Whitney umbrella. DecomposeV f into the
union of smooth sets by computing algebraic equations for its singularities, the
singularities of its singularities, and so on until no singularities remain. Either
prove that this decomposition is a Whitney stratiﬁcation ofV f , or prove that it
is not and ﬁnd a reﬁnement that is.
Exercise D.5. Let X be the complement inC2 of the smooth curve x2 + y2 = 1.
Deﬁne a Morse function and use it to compute the homology of X.
Figure D.7 The real variety in Exercise D.6.
Exercise D.6. Let Q = x2− y3− z2y2 and letVQ denote the corresponding
D.4 Stratiﬁed Morse theory for complex manifolds 531
real aﬃne variety shown in Figure D.7. Compute the set S of singularities of
VQ, and then determine whether{VQ\ S, S} is a Whitney stratiﬁcation ofVQ.
Hint: Consider points xn = (0,−t2, t)∈V Q\ S and yn = (0, t, 0)∈ S .
