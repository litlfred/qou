---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-057-cone-point-asymptotics
section_title: "Cone point asymptotics"
section_number: null
pages: 357-359
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Cone point asymptotics
Once again, let F(z) = P(z)/Q(z) = P
r arzr be a convergent Laurent ex-
pansion with domain of convergence D = Relog−1(B) for a component B of
amoeba(Q)c. In Chapter 6 we deﬁned the logarithmic growth rate
β( ˆr) = lim sup
s→∞
s/|s|= ˆr
1
|s| log |as|,
the neighborhood growth rate
β( ˆr) = lim sup
s→∞
s/|s|→ˆr
1
|s| log |as|,
and the dual rate
β∗( ˆr) = inf
x∈B −ˆr · x ,
and showed that
β( ˆr) ≤β( ˆr) ≤β∗( ˆr)
for every direction ˆr. In this chapter we study conditions under which the
equality β( ˆr) = β*( ˆr) holds – a useful criterion because β* is much easier to
compute than β or β (which usually require determining dominant asymptotic
behavior). Our framework also allows us to give asymptotics in the presence
of cone points, going beyond the smooth and multiple point cases of the last
two chapters.
Deformations and vector ﬁelds: a third approach
Deformation of cycles underlies every result in ACSV. The surgery method,
sketched in Chapter 9 for smooth points and Chapter 10 for multiple points,
is very explicit but applies only to minimal points. In contrast, the power-
ful Morse-theoretic decompositions in Chapter 7 use Thom’s Isotopy Lemma
339
340
Cone point asymptotics
(Lemma D.16), which requires the advanced apparatus of controlled vector
ﬁelds. In this chapter we chart a course between these extremes, using the the-
ory of hyperbolic polynomials to build a smooth vector ﬁeld to deform a torus
of integration below a given height except at minimal critical points. This is
reasonably general, deforming any torus deﬁned by an element of B up to and
just beyond the amoeba boundary except arbitrarily close to critical points.
Proving all necessary results from scratch would necessitate adding (at least)
another appendix to this book, so this chapter is not entirely self-contained. In-
stead, some of the technical background is cited from [BP11], which itself
condenses a fair amount of background from [ABG70]. We give a complete,
albeit telegraphic, rendition of the geometric results, extending the foundation
built in Chapter 6 to the context of hyperbolic polynomials, but largely quote
without proof the generalized function theory from [BP11, Section 6] neces-
sary for rigorous justiﬁcation of certain Fourier transforms.
Organization of the chapter
The remainder of this chapter proceeds as follows. First, we state Theorem 11.1,
which asserts the existence of certain semi-continuously varying cones. In this
context, a function from points x ∈Cd to open cones K(x) ⊆Rd is lower
semi-continuous if for all sequences xn →x we have K(x) ⊆lim inf K(xn),
where the limit inferior of a sequence (S n) of sets contains the point y if and
only if y is in all but ﬁnitely many of the sets S n.
Exercise 11.1. Let Hn be the open halfspace {(x, y) ∈R2 : x + ny > 0}. What
is lim inf Hn?
Several deformation results are derived from Theorem 11.1. In order to il-
lustrate the concepts involved, a proof of Theorem 11.1 is ﬁrst provided in
the simplest case when the intersection of the minimal torus and the variety
consists entirely of smooth points. The second section of this chapter con-
tains a full proof of Theorem 11.1, divided into a number of subsections: using
cones to construct deformations, cones of hyperbolicity in the homogeneous
case, cones of hyperbolicity in the general case, strong and weak hyperbolic-
ity, semi-continuity of cones, the ﬁnal steps of the proof, and a coda in which
a projective (log-linear) version of the deformation is constructed.
Having localized all integrals using these deformations, in the third sec-
tion we compute asymptotics for the local integrals using results from [BP11]
and [ABG70]. These computations are simpliﬁed using log-linear deforma-
tions. The ﬁnal section of the chapter applies this computational apparatus to a
number of examples including cube groves, Szeg˝o functions, Aztec diamonds,
