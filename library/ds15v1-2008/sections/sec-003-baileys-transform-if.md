---
doc_id: ds15v1-2008
doc_title: "Rogers-Ramanujan-Slater Type Identities"
section_id: sec-003-baileys-transform-if
section_title: "Bailey’s transform. If"
section_number: null
pages: 4-7
source_pdf: ds15v1-2008.pdf
source_sha256: aef155a324c6fdf4
toc_source: inferred
---
βn =
n
X
r=0
αrun−rvn+r
(1.2.3)
and
γn =
∞
X
r=n
δrur−nvr+n,
(1.2.4)
then
∞
X
n=0
αnγn =
∞
X
n=0
βnδn.
Proof.
∞
X
n=0
αnγn =
∞
X
n=0
∞
X
r=n
αnδrur−nvr+n =
∞
X
r=0
r
X
n=0
δrαnur−nvr+n =
∞
X
r=0
δrβr
Bailey does not use his transform in the most general setting, but rather specializes
un = 1/(q)n and vn = 1/(xq)n. Such a pair (αn, βn) which satisﬁes (1.2.3) is called a
Bailey pair in the subsequent literature.
Bailey’s lemma. If (αn(x, q), βn(x, q)) satisﬁes (1.2.3), again with un = 1/(q)n and
vn = 1/(xq)n, then so does (α′
n(x, q), β′
n(x, q)), where
α′
r(x, q) =
(ρ1)r(ρ2)r
(xq/ρ1)r(xq/ρ2)r
 xq
ρ1ρ2
r
αr
(1.2.5)
and
β′
n(x, q) =
1
(xq/ρ1)n(xq/ρ2)n
n
X
j=0
(ρ1)j(ρ2)j(xq/ρ1ρ2)n−j
(q; q)n−j
 xq
ρ1ρ2
j
βj(x, q).
(1.2.6)
Equivalently, if (αn(x, q), βn(x, q)) is a Bailey pair, then
1
(xq/ρ1)n(xq/ρ2)n
n
X
j=0
(ρ1)j(ρ2)j(xq/ρ1ρ2)n−j
(q)n−j
 xq
ρ1ρ2
j
βj(x, q)
=
n
X
r=0
(ρ1)r(ρ2)r
(q)n−r(xq)n+r(xq/ρ1)r(xq/ρ2)r
 xq
ρ1ρ2
r
αr(x, q).
(1.2.7)
the electronic journal of combinatorics 15 (2008), #DS15
4
Proof. See Andrews [8, pp. 25–27, Theorem 3.3].
Corollary 2.
∞
X
n=0
xnqn2βn(x, q) =
1
(xq)∞
∞
X
r=0
xrqr2αr(x, q)
(1.2.8)
∞
X
n=0
xnqn2(−q; q2)nβn(x, q2) = (−xq; q2)∞
(xq2; q2)∞
∞
X
r=0
xrqr2(−q; q2)r
(−xq; q2)r
αr(x, q2)
(1.2.9)
∞
X
n=0
xnqn(n+1)/2(−1)nβn(x, q) = (−xq)∞
(xq)∞
∞
X
r=0
xrqr(r+1)/2(−1)r
(−xq)r
αr(x, q)
(1.2.10)
Proof. Let n, ρ2 →∞in (1.2.7) to obtain
∞
X
j=0
(−1)jxjqj(j+1)/2(ρ1)j
ρj
1
βj(x, q)
= (xq/ρ1)∞
(xq)∞
∞
X
r=0
(−1)rxrqr(r+1)/2(ρ1)r
ρr
1(xq/ρ1)r
αr(x, q).
(1.2.11)
To obtain (1.2.9), let ρ1 →∞in (1.2.11). To obtain (1.2.9), in (1.2.11), set ρ1 = −√q
and replace q by q2 throughout. To obtain (1.2.10), in (1.2.11) set ρ1 = −q.
Corollary 3.
∞
X
n=0
qn2βn(1, q) =
1
f(−q)
∞
X
r=0
qr2αr(1, q)
(PBL)
∞
X
n=0
qn2(−q; q2)nβn(1, q2) =
1
ψ(−q)
∞
X
r=0
qr2αr(1, q2)
(TBL)
∞
X
n=0
qn(n+1)/2(−1)nβn(1, q) =
2
ϕ(−q)
∞
X
r=0
qr(r+1)/2
1 + qr αr(1, q)
(S1BL)
Proof. To obtain (PBL), (TBL), and (S1BL), set x = 1 in (1.2.8), (1.2.9), and (1.2.10)
respectively.
Corollary 4.
1
1 −q
∞
X
n=0
qn(n+1)/2(−q)nβn(q, q) =
1
ϕ(−q)
∞
X
r=0
qr(r+1)/2αr(q, q)
(S2BL)
1
1 −q
∞
X
n=0
(−1)nqn(n+1)/2(q)nβn(q, q) =
∞
X
r=0
(−1)rqr(r+1)/2αr(q, q).
(FBL)
the electronic journal of combinatorics 15 (2008), #DS15
5
Proof. To obtain (S2BL), set x = q and ρ2 = −q in (1.2.11).
To obtain (FBL), set
x = ρ2 = q in (1.2.11).
Example 5. The pair (αn(x, q), βn(x, q)), where
αn(x, q) = (−1)nxnqn(3n−1)/2(1 −xq2n)(x)n
(1 −x)(q)n
and
βn(x, q) =
1
(q)n
form a Bailey pair.
Proof.
βn(x, q) =
n
X
r=0
αr(x, q)
(q)n−r(xq)n+r
=
1
(q)n(xq)n
n
X
r=0
(q−n)r
(xqn+1)r
(−1)rqnr−r(r−1)/2αr(x, q)
=
1
(q)n(xq)n
n
X
r=0
(x)r(1 −xq2r)(q−n)r
(q)r(1 −x)(xqn+1)r
xrq2r2
=
1
(q)n(xq)n
lim
b→∞
n
X
r=0
(x)r(q√x)r(−q√x)r(q−n)r(b)2
r
(√x)r(−√x)r(xqn+1)r(xq/b)2r
xqn+1
b2
r
=
1
(q)n(xq)n
lim
b→∞
(xq)n(xq/b2)n
(xq/b)2n
(by Jackson’s 6φ5 sum; see [22, Eq. (II.21)])
=
1
(q)n
Now that we have a Bailey pair in hand, it can be inserted into the various limiting
cases of Bailey’s lemma to yield series-product identities. Notice that
βn(1, q) = 1/(q)n
(1.2.12)
and
αn(1, q) =

(−1)nqn(3n−1)/2(1 + qn)
when n > 0
1
when n = 0.
(1.2.13)
Upon inserting (1.2.12) and (1.2.13) into (PBL), we obtain
∞
X
n=0
qn2
(q)n
=
1
f(−q)
 
1 +
∞
X
n=1
(−1)nqn(5n−1)/2(1 + qn)
!
the electronic journal of combinatorics 15 (2008), #DS15
6
=
1
f(−q)
∞
X
n=−∞
(−1)nqn(5n−1)/2
= f(−q2, −q3)
f(−q)
(by (1.1.7))
the extremes of which are the ﬁrst Rogers-Ramanujan identity.
Upon inserting (1.2.12) and (1.2.13) into (TBL), we obtain
∞
X
n=0
qn2(−q; q2)n
(q2; q2)n
=
1
ψ(−q)
 
1 +
∞
X
n=1
(−1)nqn(4n−1)(1 + q2n)
!
=
1
ψ(−q)
∞
X
n=−∞
(−1)nqn(4n−1)
= f(−q3, −q5)
ψ(−q)
(by (1.1.7))
the extremes of which are the ﬁrst Ramanujan-Slater/G¨ollnitz-Gordon identity.
Finally, inserting (1.2.12) and (1.2.13) into (S1BL), we obtain
∞
X
n=0
qn(n+1)/2(−1)n
(q)n
=
2
ϕ(−q)
 
1 +
∞
X
n=1
(−1)nq2r2(1 + q2n)
!
=
1
ϕ(−q)
∞
X
n=−∞
(−1)nq2r2
= f(−q2, −q2)
ϕ(−q)
(by (1.1.7))
the extremes of which are a special case of Lebesgue’s identity (L), which appears in
Slater’s list [41] as Eq. (12).
1.3
