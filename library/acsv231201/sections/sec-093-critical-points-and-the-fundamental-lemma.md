---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-093-critical-points-and-the-fundamental-lemma
section_title: "Critical points and the fundamental lemma"
section_number: null
pages: 536-541
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We now extend the geometric concepts discussed in previous appendices to
stratiﬁed spaces.
Critical points for stratiﬁed spaces
Fix a Whitney stratiﬁcation {S α : α ∈I} of a closed subset X of a smooth
manifold M ⊆Rn and let f = h|X be the restriction to X of a smooth function
h : M →R.
Deﬁnition D.12 (stratiﬁed critical points and Morse functions). Any point p ∈
X is contained in a unique stratum S = S (p), and we say that p is a critical
point of the height function h on the stratiﬁed space X if p is a critical point
of h|S (p) (in other words, if the restriction of the diﬀerential of h to the tangent
space TpS (p) is zero). We call h a Morse function if
(1) the restriction h|S α is a Morse function for each α ∈I, meaning that its
critical points are nondegenerate (i.e., its Hessian is nonsingular at each
critical point), and
(2) whenever p ∈S α is a critical point of h|S α and T is a limit of tangent planes
Tpi(S β) as pi →p in a stratum S β with β > α, then either T = Tp(S α) or
T contains a tangent vector on which dh(p) does not vanish.
This generalization of Morse functions to stratiﬁed spaces appears in [Pig79,
Section 3]; see also [Laz73]. In many contexts it is assumed that Morse func-
tions have distinct critical values – in which case we say we have a Morse
function with distinct critical values – or are proper – in which case we say
we have a proper Morse function. Figure D.3 shows two height functions, one
failing condition (2) in Deﬁnition D.12 and one satisfying it: on the left, the
limit of tangent lines at the cusp is horizontal, and is therefore annihilated by
D.2 Critical points and the fundamental lemma
519
h
h
Figure D.3 A non-Morse function (left) and a Morse function (right).
dh. A standard perturbation argument shows that coinciding critical values do
not aﬀect topology.
The stratiﬁed version of the Fundamental Morse Lemma (Lemma C.27) is
the following.
Theorem D.13 (Stratiﬁed Morse Lemma [GM88, Theorem SMT part A]). Let
X ⊆Cd
∗be a stratiﬁed space with proper Morse function h and let a < b be
real numbers such that the interval [a, b] contains no critical values of h. If
h−1([a, b]) is compact, then the inclusion X≤a ,→X≤b is a homotopy equiva-
lence.
□
Tangent vector ﬁelds
The argument behind Theorem D.13 is worth understanding for readers who
have made it this far into the appendices. Both Theorem D.13 and Theorem D.9
will be derived from Thom’s Isotopy Lemma, stated as Lemma D.16 below.
For non-experts, the geometric intuition behind Theorem D.13 is not apparent,
and it can be instructive to pursue a line of reasoning that sometimes fails but
more closely parallels classical Morse theory.
Proposition D.14. In the following cases, the local product structure in Theo-
rem D.9 is induced by a diﬀeomorphism.
1. When Z is a smooth algebraic hypersurface.
2. When Z is the simplex or the complexiﬁcation of a simplex.
3. When Z is a hyperplane arrangement.
4. When Z is the product of two spaces on which the local product is induced
by a diﬀeomorphism.
Proof
In Cases 2 and 3, diﬀeomorphisms can be explicit constructed. Case 1
follows from the smooth implicit function theorem, while Case 4 follows from
taking a product diﬀeomorphism.
□
520
Stratiﬁcation and stratiﬁed Morse theory
Proof sketch of Theorem D.13 (assuming diﬀeomorphic product structure)
Step 1: Each stratum S is a smooth manifold. The nonvanishing of the gradient
of h|S implies the existence of a nonvanishing downward gradient vector ﬁeld
vS parallel to S. More speciﬁcally, there is a smooth nonvanishing section of
the tangent bundle (i.e., a map vS : S →TS) such that dh(vS) < 0.
Step 2: By assumption of diﬀeomorphic local product structure, for each
point p in each k-dimensional stratum S of X there is a Cd-neighborhood N
of p and a smooth change of coordinates in N under which S ∩N = {z ∈
N : z j = 0 for j > k} and X ∩N = {z ∈N : (zj+1, . . . , zd) ∈N′}, where
N′ is the normal slice consisting of all (d −j)-tuples (z j+1, . . . , zd) such that
(0, . . . , 0, z j+1, . . . , zd) ∈X. Strata in this neighborhood are the products of
strata of N′ in the ﬁrst k coordinates with Rd−k. Vectors v tangent to S in
this neighborhood have v j = 0 for j > k and are therefore tangent to all strata
in the neighborhood.
The within-stratum downward gradient ﬂows vS can be stitched together
via a partition of unity to form a single gradient-like ﬂow v with Lipschitz
constant 1. More speciﬁcally, each point p in a stratum has a neighborhood
Up in Cd that intersects only strata whose closure contains S(p), the stratum
containing p, and on which dh(vS(p)) < 0. If {ψUp : p ∈E} is a partition of
unity subordinate to a ﬁnite subcover of h−1[a, b] by these neighborhoods, then
v =
X
p∈E
ψUpvS(p)
(D.2.1)
deﬁnes the required ﬂow. It is gradient-like because dh(v) is a convex combi-
nation of values dh(vS(p)), which are all negative. It is tangent to each stratum
because v(p′) is a convex combination of vectors v(S(p)) tangent to strata
S(p) whose tangent spaces are contained in the tangent space to p′. Choosing
Up small enough that some constant multiple of each vS(p) can be chosen to
have Lipschitz constant 1 on Up, convexity implies that v globally has Lips-
chitz constant 1.
Figure D.4 shows a picture of this. The left-hand picture shows that the
vector ﬁeld w(p) = vS(p)(p) is gradient-like but not continuous. It changes
direction sharply when approaching a substratum, because S(p) changes dis-
continuously from one stratum to a substratum. The right-hand picture shows
these blended by a partition of unity, so as to become smooth while remaining
gradient-like.
Step 3: Let c > 0 be the inﬁmum value of |dh(v)| on X, and let Ψ :
X × [0, ∞] →X be the ﬂow deﬁned by (d/dt)Ψ(x, t) = v(Ψ(x, t)), stopped
when it hits h−1(c). Such a ﬂow exists and is unique because v is Lipschitz,
being a convex combination of locally constant vector ﬁelds (in the natural
D.2 Critical points and the fundamental lemma
521
Figure D.4 Left: A ﬂow in a 2D stratum that turns sharply when reaching a bound-
ary. Right: A partition of unity blends the ﬂow smoothly between strata (note that
the ﬂow smoothly becomes zero in a neighborhood of the zero-dimensional stra-
tum).
identiﬁcation of tangent spaces with subspaces of the tangent space to the am-
bient space Rd). Fixing any T ≥(b−a)/c the time T map deﬁnes a deformation
retract of X≤b onto X≤a, proving homotopy equivalence.
□
The problem with this sketched proof is that, in general, the local product
structure is not witnessed by a diﬀeomorphism. This is shown by Whitney’s
counterexample [Whi65a], reproduced in Goresky’s introduction [Gor12] to
Mather’s cleaned up notes [Mat12] as motivation for the work that follows.
Figure D.5 shows three planes and a ruled surface in R3, whose common inter-
section is the x-axis. Intersecting with a plane parallel to the yz-plane moving
down the x-axis results in a conﬁguration of four lines, the ﬁrst three constant
and the fourth becoming more sloped. Any coordinate system in which the ﬁrst
three lines remain ﬁxed as the slice moves down the x-axis also ﬁxes the slope
at the origin of the fourth line, and therefore cannot represent the ﬁgure as a
product of the x-axis with a four-line conﬁguration.
Figure D.5 Whitney’s counterexample to smooth isotopy.
The trouble is that the category in which one most naturally deals with
stratiﬁed spaces is smooth within strata and continuous across strata. Whit-
522
Stratiﬁcation and stratiﬁed Morse theory
ney’s conditions do not guarantee the existence of a diﬀerential structure that
is smooth across strata, even for algebraic hypersurfaces in Euclidean space.
Nevertheless, it is true that there is a continuous isotopy moving the yz-plane to
the right while continuously deforming a sector so that the line of intersection
with the ruled surface in each slice remains identiﬁed. Working in the smooth
within strata continuous across strata category, one can obtain a vector ﬁeld
but it will generally not be Lipschitz. The ﬂow in Step 3 will not necessarily
exist, and the argument falls apart.
Remark D.15. In the neighborhood of a hyperbolic point of a complex alge-
braic hypersurface, a Lipschitz vector ﬁeld can be constructed explicitly from a
lower-semicontinuously varying family of cones. This is carried out in [BP11]
(see Lemma 5.1 there) and is based on the lengthier development in [ABG70];
the construction is summarized in Section 11.2 of this book. Thus, the three
steps above prove Theorem D.13 when X is a complex algebraic hypersur-
face with all critical points hyperbolic, even though Proposition D.14 will not
necessarily hold.
Isotopy
To repair the stratiﬁed gradient ﬂow argument, one needs a statement of Thom’s
Isotopy Lemma strong enough to imply the deformation retract in Step 3 di-
rectly, as well as implying Theorem D.9. This lemma is proved by giving up
on the idea that the desired vector ﬁeld can be continuous, providing instead a
controlled vector ﬁeld satisfying a set of axioms allowing one to infer that the
vector ﬁeld deﬁnes a continuous ﬂow with the desired properties. We will not
go into the theory of controlled vector ﬁelds, being content to quote where they
are used and referring the reader to [Mat12, Proposition 11.1] for the proof of
the following results and full details of controlled vector ﬁelds for stratiﬁed
spaces.
Lemma D.16 (Thom’s Isotopy Lemma). Let Z be a Whitney stratiﬁed space
Z that is a closed subset of some smooth manifold M, and suppose that π :
M →P is a smooth proper mapping to a connected manifold P such that
the restriction π|S of π to each stratum S of Z is a submersion (surjective
on tangent spaces). Then any smooth vector ﬁeld V on P has a lift ˜V to a
controlled vector ﬁeld on Z. By a lift, we mean that V is a (not necessarily
continuous) section of the tangent bundle of each stratum of Z such that π∗◦˜V =
V ◦π. Although ˜V is not necessarily continuous, it has a continuous ﬂow ˜Ψ
that projects under π to the ﬂow Ψ deﬁned by V on P. The fact that there is a
continuous ﬂow lifting the ﬂow of V implies that π|Z : Z →P is a locally trivial
ﬁber bundle.
□
