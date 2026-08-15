---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-118-3-application-to-nonvanishing-of-l-functions
section_title: "Application to nonvanishing of L-functions"
section_number: 3
pages: 238-242
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
We can use the above reasoning to bound the number of quadratic L-functions over function ﬁelds
which vanish at a speciﬁed point on the critical line. For the rest of this section we ﬁx an odd prime p
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds 1905
and consider only ﬁelds of characteristic p. We note that, ifχ f is a quadratic character of Fq(x), then
L(s,χ f) can vanish only at a point s such that qs is a q-Weil number of weight 1. We ﬁrst recall the
following lemma relating the vanishing of theL-function of a quadratic character in terms of the Frobenius
eigenvalues of a hyperelliptic curve;
Lemma 3.1. Let f be a monic squarefree polynomial in Fq[x] andχ f be the quadratic character with
conductor f . Let C be the hyperelliptic curve deﬁned by y2= f(x) and let P∈ Z[x] be the characteristic
polynomial of geometric Frobenius acting on the Jacobian ofC. Then for any s⁄= 0, L(s,χ f)= 0 if and
only if P(qs)= 0.
This is immediate from the description of P as the numerator of the zeta function of C, and the
connection of the latter to L(s,χ f) (see, for instance, [Rudnick 2010, Section 2]).
Theorem 3.2. For any squarefree polynomial f∈ Qn,q, let L(s,χ f) be the Dirichlet L-function associ-
ated to the quadratic characterχ f as was deﬁned in Section 2A. Then for any s⁄= 0,
lim sup
n→∞
|{ f∈ Qn,q| L(s,χ f)= 0}|
|Qn,q| ≪ q−1/276
where the limit is taken over all powers q of a ﬁxed odd prime number p.
Proof. Fix an odd prime number p, and let q be a power of p. By Lemma 3.1, L(s,χ f)= 0 is equivalent
to P(q−s)= 0 where P(x)∈ Z[x] is the characteristic polynomial of Frobenius acting on the Jacobian of
the hyperelliptic curve deﬁned by y2= f(x). Thus, the set{ f∈ Qn,q| L(s,χ f)= 0} is the same as Qqs
n,q.
By Chebotarev’s density theorem, we can (for large enough q) ﬁnd a prime
𝓁= 1
4
(q
4
)1/276
(1+ o(1))
mod which gps, the minimal polynomial of ps, splits completely. Let a∈ Z/lZ such that gps(a)= 0 mod𝓁.
If q= pt, then any f with L(χ f, s)= 0 has mat( f)> 0. So
|Qqs
n,q|
|Qn,q|≤
|Qat,𝓁
n,q|
|Qn,q|
and now we can apply Corollary 2.6 to conclude using the second equation of Section 2A that, for all
sufﬁciently large t, we have
lim sup
n→∞
|Qqs
n,q|
|Qn,q|≤ 1
𝓁− 1+ C′
𝓁q−1/2.
The required bound follows from Proposition 2.7. □
Results on the vanishing of quadratic L-functions over function ﬁelds can be used to study the rank
distribution of quadratic twist families of constant abelian varieties. In the following corollary, we show
that as the constant ﬁeld grows (so the characteristic is not changing), the probability for a quadratic twist
of a constant abelian variety to have positive rank goes to 0. In the elliptic curve case, this agrees with
1906 Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
the general “minimalist conjecture” philosophy, which holds that positive ranks should be a density 0
phenomenon except when forced by parity considerations from the functional equation (in this setting the
functional equation never forces positive rank, and the rank is always even.)
Corollary 3.3. Let A be an abelian variety deﬁned over a ﬁnite ﬁeld Fq of odd characteristic. For each
f∈ Qn,qm, denote by A f the quadratic twist of A×Fq Fqm(x) by f . Let Rn,m be the set{ f∈ Qn,qm:
A f has positive rank}. Then
lim
m→∞
lim sup
n→∞
|Rn,m|
|Qn,qm|= 0.
Proof. Let P(x) be the characteristic polynomial of Frobenius acting on the Tate module of A and let q−s
be one of its roots. Then rank A f > 0 is equivalent to L(s,χ f)= 0. (See [Li 2018, Proposition 4.6] for a
similar statement with the same proof.) Thus, the statement is a direct application of Theorem 3.2. □
We now prove Theorem 1.5, which makes use of the mod 2 Galois representations on J(C) rather
than the representations modulo odd primes.
Proof of Theorem 1.5. Let x1,..., x2g+2 be the set of Weierstrass points of C. The 2-torsion subgroup
J(C)[2] is spanned by the degree-0 2-torsion divisors xi− x j. That is, the group of divisors of the form∑ ai xi with∑ ai= 0 surjects onto J(C)[2]. Note also that x1+···+ x2g+2−(2g+ 2)x1 is a principal
divisor and thus x1+···+ x2g+2 is 0 in J(C)[2]. See [Gross 2012, Section 4] for detailed discussion.
This identiﬁes J(C)[2] with an explicit subquotient of F2g+2
2 ; namely, J(C)[2] is the quotient of the
subspace(a1,..., a2g+2):∑ ai= 0 by the 1-dimensional subspace spanned by (1,..., 1).
This identiﬁcation is equivariant for the Frobenius action on both sides, so it allows us to describe the
mod 2 Galois representation afforded by J(C) in terms of the permutationπ which Frobenius induces on
x1,..., x2g+2. To be precise, the action of S2g+2 on J(C)[2] is a representationρ: S2g+2→ Sp2g(Z/2Z),
and the action of Frobenius on J(C)[2] is given byρ(π) .
The conditions on π given in Theorem 1.5 are equivalent to the condition that π 2 is a product of
two disjoint odd cycles. Thus, the action of π 2 in its permutation representation F2g+2
2 has eigenvalues
given byµk andµ2g+2−k for some odd 1≤ k≤ 2g+ 1; passing to the subquotient J(C)[2] removes two
eigenspaces ofρ(π 2) with the eigenvalue 1. So the eigenvalues of Frob2 on J(C)[2] are the multiset
µ′
k∪µ′
2g+2−k, whereµ′
n denotes the nontrivial n-th roots of unity. We see in particular that ρ(π 2) does
not have 1 as an eigenvalue. But if the zeta function ZC had a zero at 1
2, then√q would be a Frobenius
eigenvalue on C, which would mean that q was an eigenvalue of Frob2; we have shown that Frob2 has no
eigenvalue congruent to 1 mod 2, which rules this out. This proves (1).
What’s more, the multisetµ′
k∪µ′
2g+2−k contains any eigenvalue at most twice, and if(k, 2g+2−k)= 1,
no eigenvalue appears more than once. This proves (2) (or rather, it proves (2) for the zeta function of
C/Fq2, from which (2) is immediate.) □
Proof of Corollary 1.6. By assumption, f is an irreducible polynomial over Fq. So when deg f= n is
even, Frobenius acts on the set of Weierstrass points of C f: y2= f(x) as a n-cycle. If deg f= n is odd,
then Frobenius acts on the set of Weierstrass points of C f as a disjoint union of a (n−1)-cycle and a
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds 1907
1-cycle. In either case, when 4∤ deg f we can apply Theorem 1.5 to conclude that ZC f does not vanish at
1
2 and so behaves L(s,χ f).
For any X= q2g+2, the set of irreducible polynomials of odd degree at most 2g+ 1 gives quadratic
characters with bounded conductor whose L-function does not vanish at the central point s= 1
2. By the
prime number theorem for function ﬁelds, the number of irreducible polynomials in Fq[x] of degree at
most n is≫ qn/n. This gives the lower bound in statement. □
The proof of Theorem 1.7 is very similar to that of Theorem 1.5, but we treat it separately in order to
make the hyperelliptic case above more readable.
Proof of Theorem 1.7. Let x1,..., xm be the ramiﬁcation points of the (Z/𝓁Z)-cover of P1 in S, where
m= k1+···+ kr. The Jacobian J(C) of C carries an action of Z[(Z/𝓁Z)]; write λ∈ Z[(Z/𝓁Z)] for
ζ𝓁− 1, whereζ𝓁 is a generator of(Z/𝓁Z). A Riemann–Hurwitz computation shows that the genus of C is
(m− 2)(𝓁− 1)/2, so the Tate module T𝓁 J(C) is a free Z𝓁[ζ𝓁]-module of rank m− 2, and J(C)[λ] has
dimension m− 2.
Theλ-torsion subgroup of J(C) is spanned by the degree- 0λ-torsion divisors xi− x j. That is, the
group of divisors of the form ∑ ai xi with∑ ai= 0 surjects onto J(C)[λ]. This surjection is not an
isomorphism; there is a 1-dimensional kernel, which we can describe as follows. Over Fq, the curve C
has an afﬁne model of the form y𝓁= f(x) with f a rational function with no zeroes or poles at∞. Then
the principal divisor associated to y is∑ ai xi where ai= ordxi f . We have now expressed J(C)[λ] as
an explicit subquotient of Fm
𝓁 .
This identiﬁcation is equivariant for the Frobenius action on both sides, so it allows us to describe the
mod𝓁 Galois representation afforded by J(C) in terms of the permutationπ which Frobenius induces on
x1,..., xm.
The action ofπ splits x1,..., xm into cycles of length k1,..., kr, which by hypothesis are prime to 𝓁.
So the eigenvalues ofπ in its action on Fm
𝓁 are the union (as multisets) ⋃r
j=1µk j . Now the composition
factors of Fm
𝓁 as a representation of the cyclic group⟨π⟩ are J(C)[λ], F𝓁div(y), and theπ-trivial one-
dimensional representation onto which Fm
𝓁 maps by summing coordinates. Butπ acts trivially on the latter
two factors. We conclude that the eigenvalues ofπ in its action on J(C)[λ] are the multiset⋃s
j=1µ′
k j
together with r− 2 copies of 1, where µ′
n denotes the nontrivial n’th roots of unity.3
If the zeta function ZC had a zero at 1
2, then√q would be a Frobenius eigenvalue of C, which would
mean that√q modulo𝓁 was an eigenvalue of the action of π on J(C)[λ]. If q is congruent to 1 modulo
𝓁 and r= 2, this is ruled out by the fact that r− 2= 0 and⋃r
j=1µ′
k j contains no copy of 1. If q is not
congruent to 1 mod𝓁, then√q cannot be contained in ⋃r
j=1µ′
k j because of our hypothesis on qκi . Thus
we have proved that s= 1
2 is not a root of ZC.
3What if r= 1? This isn’t possible. Ifπ is an m-cycle, then the coefﬁcients of the Fq-rational divisor D must all be equal to
the same constant a, which means am is congruent to 0 mod𝓁, which means m is a multiple of𝓁; but by hypothesis no cycle has
length a multiple of𝓁.
1908 Jordan S. Ellenberg, Wanlin Li and Mark Shusterman
If k1,..., kr are mutually coprime, then⋃r
j=1µ′
k j has no repeated values. So the only possible multiple
eigenvalue of Frobenius on J(C)[𝓁] is 1, and this eigenvalue appears multiple times only if r≥ 3. This
completes the proof. □
Proof of Corollary 1.8. Consider curves over Fq with deﬁning equations of the form y𝓁= f(x) where
f∈ Fq[x] is monic, squarefree of degree n and n is a multiple of 𝓁. This gives 𝓁− 1 cyclic Dirichlet
characters of conductor f and order𝓁. Such a curve C f admits a Z/𝓁Z cover of P1
Fq branched at the
vanishing loci of f .
Let d be the order of the image of q in(Z/𝓁Z)∗ and let k1, k2,..., kr be the degrees of the factors of f .
By Theorem 1.7, if d ∤ki for any i∈{ 1, 2,..., r}, then the point s= 1
2 is not a zero of ZC thus not a zero
for the Dirichlet L-functions corresponding to the curve. Thus, a count on this family of polynomials
would give a lower bound on the set of desired Dirichlet characters.
By [Bolker and Gleason 1980, Theorem 2], the number of elements in Sn with no cycle length divisible
by d is
Td(n)=
n∏
j=1
( j−θd( j))
whereθd( j)= 0 if d ∤ j and 1 if d| j. So the number of monic, squarefree polynomials of degree n over
Fq where none of its factor has degree divisible by d is≫(Td(n)/n!)(qn− qn−1). Since Td(n)≥ T2(n)
for any d≥ 2, we have
Td(n)
n! ≥((n− 1)!!)2
n! ≥ C
n1/2
where!! stands for double factorial and C is a nonzero constant. As X= qn, we get the desired result. □
