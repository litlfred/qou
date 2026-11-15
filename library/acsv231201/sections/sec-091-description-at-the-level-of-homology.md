---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-091-description-at-the-level-of-homology
section_title: "Description at the level of homology"
section_number: null
pages: 523-531
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
505
values is then removed by homotopically perturbing h so as to satisfy the con-
ditions, and a limiting argument removes the assumption of a ﬁnite number of
critical points.
□
Example C.33. The 2-sphere from Example C.29 is a cell complex with one
2-cell and one 0-cell; as noted above, up to homotopy equivalence, there is
only one choice for the attachment map. The 2-torus from Example C.30 is
a cell complex with one 0-cell, two 1-cells, and one 2-cell. Up to homotopy
equivalence, the one skeleton must be the wedge of two circles. There are a
number of ways to attach a 2-cell to a wedge of two circles, and the right
attaching map can be worked out by knowing what the boundary (i.e., the level
set ε below the maximum height) looks like.
◁
Remark C.34. Let X be a complex d-manifold in Cn and, for p ∈Cn, let
hp denote the function mapping z ∈Cn to the complex distance ||z −p|| =
(Pn
j=1 |zj −p j|2)1/2. Andreotti and Frankel’s original proof of Proposition B.20
from Appendix B proved that p can be chosen to make hp a Morse function by
establishing that the set of p for which it is not a Morse function has positive
codimension, then showing that the Morse index of any critical point on X for
hp is at most d.
C.4 Description at the level of homology
For our purposes it is useful to consider the successive attachments from the
last section on the level of homology. Suppose that c is a critical value and
(B, A) is any pair with the same homotopy type of the attachment (X≤c+ε, X≤c−ε).
The long exact sequence has a portion
Hn+1(B, A)
∂n+1
−−−→Hn(A)
ι∗−→Hn(B)
π∗
−→Hn(B, A)
∂n
−→Hn−1(A),
which implies
Hn(A)
Image(∂n+1) = Hn(A)
ker(ι∗)  Image(ι∗) = ker(π∗).
In particular, there is a short exact sequence
0 →
Hn(A)
Image(∂n+1) →Hn(B) →ker(∂n) →0
and, by Remark B.7, Hn(B) decomposes as a direct sum of the kernel of ∂n and
the cokernel of ∂n+1.
This decomposition allows us to construct a basis for the homology groups
506
Residue forms and classical Morse theory
Hn(B) from knowledge of the homology of A and the boundary map ∂∗: starting
with a basis for Hn(A) we identify basis elements diﬀering by elements in the
image of ∂n+1 and then add new basis elements indexed by a basis for the kernel
of ∂n. These new basis elements have an explicit geometric description. The
group Hn(B, A) consists of equivalence classes of chains in B whose boundaries
lie in A. If C is a chain in the kernel of ∂n then the image ∂∗([C]) is the class
of ∂C ∈Hn−1(A), which bounds some n-chain D in A. The inverse image of
the class [C] by π∗is the class of the chain C −D, which is a cycle because
∂C = ∂D. Heuristically, we write
π−1
∗([C]) = C −∂−1
A (∂C)
(C.4.1)
and view π−1
∗([C]) as the relative cycle C in Zn(B, A), completed to an actual
cycle in a way that stays within A.
Remark C.35. The choice of D in this construction is not natural (see Re-
mark B.7). A particular composition of a space B as a subspace A attached to
C = B \ A comes with an explicit inclusion map from ∂C to A, and this induces
the ∂∗operator. There may, however, be more than one way to reassemble A,C,
and ∂∗into B, giving homotopy equivalent spaces with diﬀerent homology
bases.
One further remark on notation: when attaching a space Y along Y0, the pair
(Y, Y0) is commonly referred to as the attachment data or, in the case of Morse
theory, the Morse data for the attachment. This data should really include the
homotopy type of the attachment map, or else the homotopy type of X and
the attachment data do not determine the homotopy type of the new space. On
the level of homology what we need to know is the relative homology of the
pair (Y, Y0), which is the homology of the new space relative to the old space,
together with the ∂∗map.
Filtered spaces
A ﬁltered space Xn is the end of a nested sequence X0 ⊆X1 ⊆· · · ⊆Xn of
topological spaces. We use the terminology of ﬁltered spaces to describe how
homology changes among sublevel sets Xj = X≤a j, and our ﬁrst result concerns
the homology of a chain that is successively pushed toward lower heights.
Lemma C.36 (Pushing Down Lemma). Let X0 ⊆· · · ⊆Xn be a ﬁltered space
and let C be a non-zero homology class in Hk(Xn, X0) for some k. Then there is
a unique positive j ≤n such that for some C∗∈Hk(X j, Xj−1),
ι(C∗) = π(C) , 0 in Hk(Xn, Xj−1),
(C.4.2)
C.4 Description at the level of homology
507
where ι is the map induced by the inclusion of pairs (Xj, Xj−1) →(Xn, Xj−1)
and π is the map induced by the projection of pairs (Xn, X0) →(Xn, Xj−1). If ι
is an injection then C∗is unique.
Proof
To prove uniqueness of j, suppose that (C.4.2) is satisﬁed for some
minimal j with a chain C∗, and let j < r ≤n. The composition of the two maps
(Xj, Xj−1) →(Xn, Xj−1) →(Xn, Xr−1)
induces the zero mapping on homology because any class in the image of
the ﬁrst map has a cycle representative in Xj. Letting π′ denote projection of
(Xn, X0) to (Xn, Xr−1), we have π′(C) = π′(π(C)) = π′(ι(C∗)) = 0 and there-
fore (C.4.2) cannot hold for r > j.
For existence we argue by induction on n. The case n = 1 is trivial because
then j = 1 and C∗= C. Assume the result for n−1 and let C be a non-zero class
in Hk(Xn, X0). If the image of C under the projection of (Xn, X0) to (Xn, Xn−1) is
non-zero then we may take C∗to be this image and j to be n. Assume therefore
that C projects to zero. The short exact sequence of chain complexes for the
pairs
0 →(Xn−1, X0) →(Xn, X0) →(Xn, Xn−1) →0
induces the exact sequence
Hk(Xn−1, X0) →Hk(Xn, X0) →Hk(Xn, Xn−1) .
By assumption C is in the kernel of the second map, hence is the image under
the ﬁrst map of some non-zero class C′. Applying the inductive hypothesis to
C′ yields some j ≤n −1 and a cycle C∗∈Hk(Xj, X j−1) satisfying (C.4.2) with
C′ in place of C. The commuting diagram
C∗∈(Xj, X j−1)
-
ι1
(Xn−1, Xj−1)
-
ι2
(Xn, Xj−1)
C′ ∈(Xn−1, X0)
-
ι3
?
π1
C ∈(Xn, X0)
?
π
allows us to conclude π(C) = π(ι3(C′)) = ι2(π1(C′)) = ι2(ι1(C∗)) = ι(C∗),
verifying (C.4.2).
□
508
Residue forms and classical Morse theory
Building up by successive attachments
If we understand the topology of each pair (Xk+1, Xk) of consecutive elements
in a ﬁltration X0 ⊆· · · ⊆Xn and we understand the homology groups of X0
then, using the argument above and induction, we understand the homology
groups of all Xk. Furthermore, if X is a smooth manifold with a proper height
function h then the Morse Lemma implies that the topology of the continuum
of spaces {X≤t} is captured by a ﬁltration of sets described by the critical values
c0 < c1 < · · · < cn−1 of h. The Morse ﬁltration of X with respect to h is the
ﬁltration deﬁned by Xj = X≤c j−ε for 0 ≤j ≤n −1 and Xn = X≤cn−1+ε, where ε
is any suﬃciently small positive number.
When h has distinct critical values the pairs (Xi+1, Xi) are homotopy equiv-
alent to Xpi,loc, where pi are the critical points listed in order of increasing
height. In general, the successive pairs are homotopy equivalent to ]
M
h(p)=c j
Xp,loc
as c j increases through all critical values. We could describe how to keep track
of generators and relations for the homologies of Xj inductively on j in the gen-
eral case, however what we will need is both more specialized (our spaces are
complex algebraic or analytic varieties) and more general (our spaces may not
be manifolds). Accordingly, we restrict the discussion here to one illustration,
continuing our example of the torus to show what can happen.
Example C.37. In Example C.30 we examined a height function on the torus
X with four critical points: one of Morse index 0, two of Morse index 1, and one
of Morse index 2. All ∂∗maps vanish so the homology groups H0(X), H1(X),
and H2(X) are cyclic groups of rank 1, 2, and 1, respectively. The ﬁltration con-
sists of X0 = ∅, X1 which is contractible to a point, X2 which is homeomorphic
to a cylinder, X3 which is homeomorphic to a punctured torus, and X4 which is
the whole torus.
As an illustration of the non-naturality of the homology basis in (C.4.1),
consider the second 1-cell to be added. Let α be the homology class in H1(X2)
of the ﬁrst 1-cell. Then the second 1-cell, which is a well-deﬁned relative ho-
mology class β in H1(X3, X2), may be completed to an absolute class in H1(X3)
in many diﬀerent ways, resulting in cycles diﬀering by multiples of α. Geomet-
rically, one may for example complete β to the circle deﬁned by x2 + z2 = 1,
or instead wrap around the torus any integer number of times.
◁
Exercise C.5. Let γ be the cycle pictured in Figure C.7, going around the torus
between the critical points p4 and p3. Applying the Pushing Down Lemma with
respect to the Morse ﬁltration for the pictured height function, what is j and
what cycle represents ι(C∗) = π(C)?
C.4 Description at the level of homology
509
c
p
p
c
2
2
3
4
p1
4
3
p
1
c
c
Figure C.7 A cycle on a torus.
Assume now that X ⊆Cd
∗is a smooth algebraic hypersurface (a real mani-
fold of dimension 2d −2) and that the speciﬁc height function h(z) = hr(z) =
−r1 log |z1| −· · · −rd log |zd| is a proper Morse function on X. The purpose
of introducing critical points at inﬁnity in Chapter 7 is to remove the strong
assumption that h is proper, however, to see how everything works, we now
derive the results of Chapter 7 in this setting. The height function h is the real
part of (a branch of) a holomorphic function −r · log z, and is thus harmonic,
so all critical points for h on X have middle Morse index d −1. Let p(j) for
1 ≤j ≤m enumerate the critical points, ordered so that the critical values
c j = h(pj) are nondecreasing.
By the Morse Lemma, any cycle supported on X<c1 can be deformed via
gradient ﬂow to a cycle in X≤t for t arbitrarily small, therefore integrals of
z−rF(z)dz over such cycles decay faster than any exponential. For this reason,
it suﬃces to describe the homology of (X, −∞), where −∞stands for X≤t for
any t < c1. The ﬁnal set of results in this appendix describes this homology.
Theorem C.38. Suppose h = hr is a proper Morse function on a smooth
algebraic hypersurface X in Cd
∗. Then Hk(X, −∞) vanishes in dimensions k ,
510
Residue forms and classical Morse theory
d −1. The (d −1)-homology is given by Hd−1(X, −∞)  Cm, where m is the
number of critical points. A basis {γp} may be chosen, indexed by the critical
points p of h on X, with the property that h is maximized on γp at p. By the
isomorphism of smooth homology and singular homology, each γp may be
chosen to be smooth.
Proof
First assume distinct critical values c1 < · · · < cm with corresponding
critical points p(1), . . . , p(m), and let Xj denote the space X≤c j+ε. Inducting on j,
we show that the conclusion of the theorem holds for X j in place of X. First,
we note that each pair (Xj, X j−1) is homotopy equivalent to a (d −1)-ball Bd−1
modulo its boundary, whose homology has rank 1 in dimension d −1 and zero
in every other dimension. For the base step j = 1, where we take X0 = X≤t for
any t < c1, the conclusion is immediate.
Now assume the conclusion holds with X = Xj for some j < m, and consider
the short exact sequence of chain complexes of pairs
0 →C∗(X j, −∞) →C∗(Xj+1, −∞) →C∗(Xj+1, Xj) →0 .
None of these pairs has any homology in dimensions higher than d −1, there-
fore the long exact sequence is as follows, with an arrow from the rightmost
element of each row other than the bottom row to the leftmost element of the
next row down.
0
→
Hd−1(Xj, −∞)
→
Hd−1(X j+1, −∞)
→
Hd−1(X j+1, Xj)
Hd−2(Xj, −∞)
→
Hd−2(X j+1, −∞)
→
Hd−2(X j+1, Xj)
Hd−3(Xj, −∞)
→
Hd−3(X j+1, −∞)
→
Hd−3(X j+1, Xj)
...
...
...
H0(X j, −∞)
→
H0(Xj+1, −∞)
→
H0(Xj+1, Xj) →0.
Identifying each Hk(Xj+1, Xj) as C if k = d −1 and 0 otherwise, and using the
induction hypothesis, ﬁlls in most of this sequence:
0
→
Cj
→
Hd−1(Xj+1, −∞)
→
C
0
→
Hd−2(Xj+1, −∞)
→
0
0
→
Hd−3(Xj+1, −∞)
→
0
...
...
...
0
→
H0(X j+1, −∞)
→
0 ,
from which we deduce that Hk(Xj+1, −∞) has rank one more than that of
Hk(Xj, −∞) when k = d −1 and rank zero otherwise. The extra generator
comes from the attachment of Bd−1 modulo its boundary, for which the gen-
erator γ j+1 may be chosen to maximize h at p(j) (see Exercise C.10), thereby
C.4 Description at the level of homology
511
completing the induction. Finally, the assumption of distinct critical values
may be removed via (C.3.1).
□
Exercise C.6. Let X be a smooth complex algebraic variety of complex di-
mension d in Cm
∗for m > d and let h be a Morse function on X which is the
real part of a complex analytic function. Suppose X has ﬁve critical points.
Can you determine the homotopy type of the pair (X≤b, X≤a) when a →−∞
and b →+∞?
We now have the tools to state a result analogous to what Theorem C.38 tells
us about X for M = Cd
∗\ X. Recall the tube operator o : Hd−1(V∗) →Hd(M)
from Theorem C.2 – this is not only an injection, but (as we will see in the
next appendix) is an isomorphism on (X j+1, Xj). An induction then gives the
following result.
Theorem C.39. Suppose the height function hr is a proper Morse function on
a smooth complex algebraic hypersurface X in Cd
∗and let M = Cd
∗\ X. Then
there is a basis for Hd(M, −∞) consisting of a single generator γp for each
critical point p of hr, which is tube around a cycle reaching maximum height
at p and is homotopy equivalent to S 1 × (Bd−1, ∂Bd−1).
□
We cover Theorem C.39, and generalizations, in Appendix D.
Notes
Detailed treatments of multivariate residues are given in [Pha11; AY83], while
the classic text on Morse theory, which we have based our presentation around,
is [Mil63].
Additional exercises
Exercise C.7 (univariate residues via Stokes’s Theorem). Let f be a meromor-
phic function inside and on a closed contour γ such that f has no singularities
on γ. The familiar residue theorem in one variable states that
1
2πi
Z
γ
f =
X
a
Res( f; a),
where the sum is over the poles a of f inside γ. Derive this from Theorem C.9.
What are α, β, ω, V, and INT[α, β; V]?
512
Residue forms and classical Morse theory
Exercise C.8. Let P be a polynomial in two complex variables such that P(0, y)
has only simple, non-zero roots. Let α be a small torus of polyradius (ε, ε) and
let β be a torus of polyradius (ε, M), where M is much larger than any root
of P(0, y). Compute the intersection class INT[α, β; V]. Hint: Use the obvious
homotopy and parametrize V∗as y = f j(x) near each root yj of P(0, y).
Exercise C.9 (lumpy sphere). Let X be a sphere with a lump, that is, a patch
on the northern hemisphere where the surface is raised to produce a local,
but not global, maximum of the height function. List the critical points of the
lumpy sphere and determine the homotopy types of the attachments. This gives
a description of the lumpy sphere as a cell complex diﬀerent from the complex
with just two cells. Use this to compute the homology and verify it is the same
as for the non-lumpy sphere.
Exercise C.10. Let M be a manifold with Morse function h having distinct
critical values and let x be a critical point of Morse index k. Let P be any sub-
manifold of M diﬀeomorphic to an open k-ball about x such that h is strictly
maximized on P at x. Prove that P is a homology generator for the local ho-
mology group Hk(Mh(x)+ε, Mh(x)−ε). Hint: This is true of any embedded k-disk
through x in Mh(x) that intersects the ascending (n −k)-disk transversely.
Exercise C.11. Let ιd : CPd−1 ,→CPd denote the embedding ιd(z0 : · · · : zd) =
(z0 : · · · : zd : 0).
(i) Show that CPd \ Image(ι) is homeomorphic to a (2d)-ball.
(ii) Describe CPd as CPd−1 with a (2d)-cell attached. What is the attachment
map on homology?
(iii) Use induction on d to compute the homology of CPd.
Appendix D
Stratiﬁcation and stratiﬁed Morse theory
In this ﬁnal appendix we extend the Morse-theoretic decompositions of Ap-
pendix C to handle general algebraic varieties and their complements. More
speciﬁcally, we cover results from stratiﬁed Morse theory [GM88] that char-
acterize the topology of a stratiﬁed space X through changes in topology in
the sublevel sets X≤c as c passes through critical values (in a stratiﬁed sense)
of a height function. We develop from scratch the notion of a Whitney strat-
iﬁed space, Morse functions, and stratiﬁed critical points. We discuss non-
proper extensions of this material and then summarize a number of basic re-
sults of [GM88], including speciﬁc properties enjoyed by complex algebraic
varieties.
