---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds"
section_id: sec-003-3-application-to-nonvanishing-of-l-functions
section_title: "Application to nonvanishing of L-functions"
section_number: 3
pages: 10-12
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 7 sections: Introduction; For the similar Theorem 1.7, the 𝓁; Main theorem and proof"
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
