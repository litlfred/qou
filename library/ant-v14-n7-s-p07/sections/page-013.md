---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-013
section_title: "Page 13"
section_number: null
pages: 13-13
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1907
1-cycle. In either case, when 4∤deg f we can apply Theorem 1.5 to conclude that ZC f does not vanish at
1
2 and so behaves L(s, χ f ).
For any X = q2g+2, the set of irreducible polynomials of odd degree at most 2g + 1 gives quadratic
characters with bounded conductor whose L-function does not vanish at the central point s = 1
2. By the
prime number theorem for function ﬁelds, the number of irreducible polynomials in Fq[x] of degree at
most n is ≫qn/n. This gives the lower bound in statement.
□
The proof of Theorem 1.7 is very similar to that of Theorem 1.5, but we treat it separately in order to
make the hyperelliptic case above more readable.
Proof of Theorem 1.7. Let x1, . . . , xm be the ramiﬁcation points of the (Z/ℓZ)-cover of P1 in S, where
m = k1 + · · · + kr. The Jacobian J(C) of C carries an action of Z[(Z/ℓZ)]; write λ ∈Z[(Z/ℓZ)] for
ζℓ−1, where ζℓis a generator of (Z/ℓZ). A Riemann–Hurwitz computation shows that the genus of C is
(m −2)(ℓ−1)/2, so the Tate module TℓJ(C) is a free Zℓ[ζℓ]-module of rank m −2, and J(C)[λ] has
dimension m −2.
The λ-torsion subgroup of J(C) is spanned by the degree-0 λ-torsion divisors xi −x j. That is, the
group of divisors of the form P aixi with P ai = 0 surjects onto J(C)[λ]. This surjection is not an
isomorphism; there is a 1-dimensional kernel, which we can describe as follows. Over Fq, the curve C
has an afﬁne model of the form yℓ= f (x) with f a rational function with no zeroes or poles at ∞. Then
the principal divisor associated to y is P aixi where ai = ordxi f . We have now expressed J(C)[λ] as
an explicit subquotient of Fm
ℓ.
This identiﬁcation is equivariant for the Frobenius action on both sides, so it allows us to describe the
mod ℓGalois representation afforded by J(C) in terms of the permutation π which Frobenius induces on
x1, . . . , xm.
The action of π splits x1, . . . , xm into cycles of length k1, . . . , kr, which by hypothesis are prime to ℓ.
So the eigenvalues of π in its action on Fm
ℓare the union (as multisets) Sr
j=1 µk j. Now the composition
factors of Fm
ℓas a representation of the cyclic group ⟨π⟩are J(C)[λ], Fℓdiv(y), and the π-trivial one-
dimensional representation onto which Fm
ℓmaps by summing coordinates. But π acts trivially on the latter
two factors. We conclude that the eigenvalues of π in its action on J(C)[λ] are the multiset Ss
j=1 µ′
k j
together with r −2 copies of 1, where µ′
n denotes the nontrivial n’th roots of unity.3
If the zeta function ZC had a zero at 1
2, then √q would be a Frobenius eigenvalue of C, which would
mean that √q modulo ℓwas an eigenvalue of the action of π on J(C)[λ]. If q is congruent to 1 modulo
ℓand r = 2, this is ruled out by the fact that r −2 = 0 and Sr
j=1 µ′
k j contains no copy of 1. If q is not
congruent to 1 mod ℓ, then √q cannot be contained in Sr
j=1 µ′
k j because of our hypothesis on qκi. Thus
we have proved that s = 1
2 is not a root of ZC.
3What if r = 1? This isn’t possible. If π is an m-cycle, then the coefﬁcients of the Fq-rational divisor D must all be equal to
the same constant a, which means am is congruent to 0 mod ℓ, which means m is a multiple of ℓ; but by hypothesis no cycle has
length a multiple of ℓ.
