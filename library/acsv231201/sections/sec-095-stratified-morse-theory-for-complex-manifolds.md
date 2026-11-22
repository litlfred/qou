---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-095-stratified-morse-theory-for-complex-manifolds
section_title: "Stratified Morse theory for complex manifolds"
section_number: null
pages: 545-551
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
527
D.4 Stratiﬁed Morse theory for complex manifolds
If X is a complex variety then the Morse data has an alternate description obey-
ing the complex structure of X. Let S be a stratum containing a critical point p,
let N(p) be a small ball in the normal space to S at p, and deﬁne the complex
link L(S ) to be the intersection of X with a generic hyperplane A ⊆N(p) that
comes suﬃciently close to p but does not contain it. It is shown in [GM88,
page 16] that the normal Morse data at p ∈X is given in terms of L(S ) by the
pair
(Cone R(L(S )), L(S )) ,
(D.4.1)
where Cone R(L(S )) denotes the real cone over L(S ). In other words, the nor-
mal link has the homotopy type of the pair (L(S )×[0, 1] / L(S )×{1} , L(S )×
{0}), where the real cone (the ﬁrst space of this pair) is deﬁned as a quotient.
Suppose that X has dimension d, the stratum S has dimension k, and the
ambient space has dimension n (all dimensions are complex). Then N(p) is a
complex space of dimension n −k, its intersection with a generic hyperplane
has dimension n −k −1, and thus
dimC L(S ) = d −k −1 .
In fact the homeomorphism type of the complex link depends on X and S but
not on the individual choice of p ∈S , nor the ambient space, nor the choice of
proper Morse function h on the stratiﬁed space X (see [GM88, Section II:2.3]).
Suppose next that X is the complement of a d-dimensional variety in Cd+1.
A formula for the Morse data at a point p < X in a stratum S is given [GM88,
page 18] by
(L(S ), ∂L(S )) × (B1, ∂B1) ,
(D.4.2)
where B1 is a real interval (which can be interpreted as a 1-ball).
Theorem D.23. (i) If X is a complex analytic variety of dimension d then X
has the homotopy type of a cell complex of dimension at most d. (ii) If X is the
complement in a domain of Cn of a complex variety of dimension d then X has
the homotopy type of a cell complex of dimension at most 2n −d −1.
Remark. The proof of this result in [GM88] is somewhat diﬃcult, mostly
due to the necessity of establishing the invariance properties of the complex
link. The result, however, is very useful. For example, suppose that X is the
complement of the zero set of a polynomial in n variables. Then d = n −1
and the homotopy dimension of X is at most n. Note that X may have strata
of any complex dimension j ≤d, and that the complement of a j-dimensional
complex space in Cn has homotopy dimension 2n −2 j. The theorem asserts
528
Stratiﬁcation and stratiﬁed Morse theory
that the complex structure prevents the dimensions of contributions at strata
of dimensions j < d from exceeding the dimension of the contributions from
d-dimensional strata.
Proof sketch
(i) Assume that the variety is embedded in Cn and that the height
function h has been chosen to be the square of the distance from a generic
point. We examine the homotopy type of the attachment at a point p in a stra-
tum of dimension k. It suﬃces, as in the proof of Theorem C.39, to show that
each attachment has the homotopy type of a cell complex of dimension at most
d.
First, if k = d (p is a smooth point) then, as was observed prior to stating
Theorem C.39, the Morse index of h is at most d. The attachment is (Bi, ∂Bi)
where i is the Morse index of h, so in this case the homotopy type of the
attachment is at most d.
When k < d, we proceed by induction on d. The tangential Morse data has
the homotopy type of a cell complex of dimension at most k. The space L(S ) is
a complex analytic space, with complex dimension one less than the dimension
of the normal slice, meaning it has dimension d−k−1. The induction hypothesis
shows that the homotopy dimension of L(S ) is at most d −k −1. Taking the
cone brings the dimension to at most d −k and adding the dimension of the
tangential data brings this up to at most d, completing the induction.
(ii) When X is the complement of a variety V, still assuming h to be the
square of the distance to a generic point, all critical points with respect to
the pair (X, V) are contained in V, not in X. Again it suﬃces to show that
the attachments all have homotopy dimension at most 2n −d −1, and again
we start with the case k = d. Here p is a smooth point of V, so the normal
data is the same as for the complement of a point in Cn−d, which is S 2(n−d)−1.
The tangential data has homotopy dimension at most d, so the attachment has
dimension at most 2n −d −1.
When k < d, we again proceed by induction on d. The link L(S ) is the
complement of V∩A in a generic hyperplane A. We have directly dimC N(p) =
n −k and dimC(A) = n −k −1, and dimC(V ∩A) = d −k −1 because V has
codimension n −d, intersects A generically, and k ≤d −1. The induction
hypothesis applied to the complement of V ∩A in A shows that L(S ) has the
homotopy type of a cell complex of dimension at most 2(n −k −1) −(d −k −
1) −1 = 2n −d −k −2. The normal Morse data is the product of this with a
1-complex, hence it has homotopy dimension at most 2n−d −k−1, and taking
the product with the tangential Morse data brings the dimension up to at most
2n −d −1, completing the induction.
□
It is useful for the main part of this book to summarize the results from this
D.4 Stratiﬁed Morse theory for complex manifolds
529
section for complements of manifolds, applying the K¨unneth formula to obtain
a description of the attachments in terms of speciﬁc relative cycles.
Deﬁnition D.24 (quasi-local cycles). A (relative or absolute) local cycle at a
point p is a cycle which may be deformed so as to be in an arbitrarily small
neighborhood of p. Given a stratiﬁed space with Morse function h, a quasi-
local cycle at a critical point p of the stratiﬁcation is a cycle C⊥× C∥, where
C∥is a disk in S on which h is strictly maximized at p, Bp is a small ball
around p in the normal slice, C⊥is a local cycle in (Bp \ Y, (Bp \ Y)≤h(p)−ε),
and the product is taken in any local coordinatization of a neighborhood of p
by Bp × S .
Theorem D.25. Let X be the complement of a complex variety of dimension d
in Cd+1. Then X may be built by attaching spaces that are homotopy equivalent
to cell complexes of dimension at most d + 1. Consequently, Hd(X) has a basis
of quasi-local cycles which may be described as B = {σp,i}p,i, where p ranges
over critical points in diﬀerent strata, and each σp,i ∈Xc,p. For each ﬁxed p,
the projection π∗: Xc,p →(Xc,p, X≤c−ε) = Xp,loc maps the set {σp,i} to a basis
for the relative homology group Hd(Xp,loc).
□
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
ested in the space X = Vc which is not closed. Dealing with nonproper height
functions requires two extra developmental steps. The ﬁrst is to develop a sys-
tem for keeping track of the change in topology of the complement of a closed
space up to a varying height cutoﬀ. This computation is similar to the one for
the space itself. Goresky and MacPherson state the two results together in a
530
Stratiﬁcation and stratiﬁed Morse theory
later version of the “Main Theorem” of [GM88], and we have followed their
example, stating the results together in Theorem D.21. The second way h can
fail to be proper occurs at inﬁnity. The results of [GM88] across the height
interval [a, b] can be extended to unbounded spaces when there are no critical
points at inﬁnity with heights in [a, b]. This was the motivation for the results
on CPAI derived in [BMP22], which we use in Chapter 7.
Additional exercises
Exercise D.4 (Whitney umbrella). Let f(x, y, z) = x2 + y2z be the polynomial
whose real variety V f forms the Whitney umbrella. Decompose Vf into the
union of smooth sets by computing algebraic equations for its singularities, the
singularities of its singularities, and so on until no singularities remain. Either
prove that this decomposition is a Whitney stratiﬁcation of V f , or prove that it
is not and ﬁnd a reﬁnement that is.
Exercise D.5. Let X be the complement in C2 of the smooth curve x2 +y2 = 1.
Deﬁne a Morse function and use it to compute the homology of X.
Figure D.7 The real variety in Exercise D.6.
Exercise D.6. Let Q = x2 −y3 −z2y2 and let VQ denote the corresponding
D.4 Stratiﬁed Morse theory for complex manifolds
531
real aﬃne variety shown in Figure D.7. Compute the set S of singularities of
VQ, and then determine whether {VQ \S, S } is a Whitney stratiﬁcation of VQ.
Hint: Consider points xn = (0, −t2, t) ∈VQ \ S and yn = (0, t, 0) ∈S .
