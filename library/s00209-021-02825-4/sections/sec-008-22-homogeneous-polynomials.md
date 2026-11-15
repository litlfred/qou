---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-008-22-homogeneous-polynomials
section_title: "Homogeneous polynomials"
section_number: 2.2
pages: 7-8
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
The usual degree-n homogenization of a polynomial f ∈Cn[x] is deﬁned on monomials as
follows and is extended linearly.
Hmgn : Cn[x] →V (n)
xk →xk yn−k
More generally, for λ ∈Nm
0 the degree-λ homogenization is deﬁned on monomials as follows
and is extended linearly.
Hmgλ : Cλ[x1, . . . , xm] →V (λ)
xμ →xμyλ−μ
Cn[x] and V (n) are isomorphic as vector spaces via Hmgn, and we will mainly utilize
bivariate homogeneous polynomials in V (n) over the usual univariate polynomials in Cn[x].
What homogeneity gets us is a simpliﬁcation of a number of issues related to the fact that
polynomials in Cn[x] have at most n zeros. Speciﬁcally, it is more natural to think of the
missing zeros (when the number of zeros is less than n) as being “at inﬁnity”. Certain
results require premises restricting to convex regions or to polynomials of degree exactly
n (e.g., the classical Grace–Walsh–Szeg˝o coincidence theorem), and such details vanish
when considering homogeneous polynomials with possible roots at inﬁnity. Another way
to say this is that we consider polynomials in V (n) to have exactly n roots in CP1, which
can also be thought of as the Riemann sphere. We also consider polynomials p(x, y) =
p(x1, y1, . . . , xm, ym) ∈V (λ) to have zeros in (CP1)m, where each pair (xk, yk) corresponds
to a single factor of CP1 in (CP1)m.
We use the notation (a : b) ∈CP1, which is meant to give off the connotation of a ratio;
that is, (a : b) should feel like a/b. We also use the notation (a : b) =

(a1 : b1), . . . , (am :
bm)
	
∈(CP1)m. Note that this connotation aligns with the idea of considering the zeros of
1366
J. Leake
polynomials to be in (CP1)m. given the following equality. Deﬁning p := Hmgλ( f ) for a
given polynomial f ∈Cλ[x1, . . . , xm], we have:
p(x, y) = p(x1, y1, . . . , xm, ym) =

k
yλk
k · f (x1/y1, . . . , xm/ym) = yλ · f (x/y)
Finally, we give an important deﬁnition which will essentially replace the notion of a monic
polynomial for homogeneous polynomials.
Deﬁnition 2.1 Given p ∈V (λ), we say that p is top-degree monic if the coefﬁcient of xλ in
p equals 1. In particular, if p ∈V (n) is top-degree monic, then p has no roots at inﬁnity.
