---
doc_id: ant-v14-n7-s-p07
doc_title: "Nonvanishing of hyperelliptic zeta functions over finite fields"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: ant-v14-n7-s-p07.pdf
source_sha256: c5a749ef6be194fd
toc_source: undetermined
doc_brief: "Nonvanishing of hyperelliptic zeta functions over finite fields — 16 sections: Page 1; Page 2; Page 3"
---
Nonvanishing of hyperelliptic zeta functions over ﬁnite ﬁelds
1905
and consider only ﬁelds of characteristic p. We note that, if χ f is a quadratic character of Fq(x), then
L(s, χ f ) can vanish only at a point s such that qs is a q-Weil number of weight 1. We ﬁrst recall the
following lemma relating the vanishing of the L-function of a quadratic character in terms of the Frobenius
eigenvalues of a hyperelliptic curve;
Lemma 3.1. Let f be a monic squarefree polynomial in Fq[x] and χ f be the quadratic character with
conductor f . Let C be the hyperelliptic curve deﬁned by y2 = f (x) and let P ∈Z[x] be the characteristic
polynomial of geometric Frobenius acting on the Jacobian of C. Then for any s̸ = 0, L(s, χ f ) = 0 if and
only if P(qs) = 0.
This is immediate from the description of P as the numerator of the zeta function of C, and the
connection of the latter to L(s, χ f ) (see, for instance, [Rudnick 2010, Section 2]).
Theorem 3.2. For any squarefree polynomial f ∈Qn,q, let L(s, χ f ) be the Dirichlet L-function associ-
ated to the quadratic character χ f as was deﬁned in Section 2A. Then for any s̸ = 0,
lim sup
n→∞
|{ f ∈Qn,q | L(s, χ f ) = 0}|
|Qn,q|
≪q−1/276
where the limit is taken over all powers q of a ﬁxed odd prime number p.
Proof. Fix an odd prime number p, and let q be a power of p. By Lemma 3.1, L(s, χ f ) = 0 is equivalent
to P(q−s) = 0 where P(x) ∈Z[x] is the characteristic polynomial of Frobenius acting on the Jacobian of
the hyperelliptic curve deﬁned by y2 = f (x). Thus, the set { f ∈Qn,q | L(s, χ f ) = 0} is the same as Qqs
n,q.
By Chebotarev’s density theorem, we can (for large enough q) ﬁnd a prime
ℓ= 1
4
q
4
1/276
(1 + o(1))
mod which gps, the minimal polynomial of ps, splits completely. Let a ∈Z/lZ such that gps(a)=0 mod ℓ.
If q = pt, then any f with L(χ f , s) = 0 has mat( f ) > 0. So
|Qqs
n,q|
|Qn,q| ≤
|Qat,ℓ
n,q |
|Qn,q|
and now we can apply Corollary 2.6 to conclude using the second equation of Section 2A that, for all
sufﬁciently large t, we have
lim sup
n→∞
|Qqs
n,q|
|Qn,q| ≤
1
ℓ−1 + C′
ℓq−1/2.
The required bound follows from Proposition 2.7.
□
Results on the vanishing of quadratic L-functions over function ﬁelds can be used to study the rank
distribution of quadratic twist families of constant abelian varieties. In the following corollary, we show
that as the constant ﬁeld grows (so the characteristic is not changing), the probability for a quadratic twist
of a constant abelian variety to have positive rank goes to 0. In the elliptic curve case, this agrees with
