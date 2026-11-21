---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-005-31-asymptotics-of-orthogonal-polynomials
section_title: "Asymptotics of orthogonal polynomials"
section_number: 3.1
pages: 11-14
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
Asymptotics of orthogonal polynomials
We shall prove the following theorem‡ on the asymptotic behavior of these orthogonal polynomi-
als:
Theorem 2: Let {P (α)
n
(λ)}n=0,1,··· be the set of polynomials orthogonal with respect
to the measure
dλ λ2α e−NV (λ2),
V (λ2) =
X
k≥1
gk
2k λ2k,
α = 0, 1, · · ·
over the range (−∞, ∞), whose moments are all ﬁnite. If the polynomials can be
normalized according to P (α)
2n (0) = P (α)
2n+1
′(0) = 1, then, for ﬁxed x = N λ and t =
2n/N, the following limiting relations hold:
lim
N→∞P (α)
2n ( x
N )

n=Nt/2
= Γ(α + 1
2)
Jα−1
2 (u(t)x)
(u(t)x/2)α−1
2
,
(3.4a)
lim
N→∞N P (α)
2n+1( x
N )

n=Nt/2
= x Γ(α + 3
2)
Jα+ 1
2 (u(t)x)
(u(t)x/2)α+ 1
2
,
(3.4b)
where u(t) is determined by
u(t) =
Z t
0
dt′
2
p
r(t′),
t =
X
k
gk
2
2k
k

r(t)k.
‡ Theorem 2 can be regarded as an extension of Theorem 1 for half-integer α.
10
The proof of this theorem for α = 0 was sketched in ref. [14], and below we shall elaborate it in
a rigorous form. The recursion relation for monically normalized polynomial
Pn(λ) ≡P (0)
n (λ) = λn + · · ·
(3.5)
takes the form
λ Pn(λ) = Pn+1(λ) + rn Pn−1(λ),
(3.6)
with
rn =
hn
hn−1
.
(3.7)
Since the monic normalization (3.5) does not distinguish the parity of n, neither does rn. Eq. (3.6)
immediately implies
0 = P2n+2(0) + r2n+1 P2n(0).
(3.8)
Due to the Z2 symmetry of the weight function, the polynomials have deﬁnite parities. Therefore
we are lead to change the normalization of polynomials as follows:
P2n(λ)
P2n(0) →P2n(λ) = 1 + · · · ,
P2n+1(λ)
P2n+1′(0) →P2n+1(λ) = λ + · · · .
(3.9)
Then the recursion relation (3.6) in this normalization, applied twice to P2n(λ), takes the form
λ2 P2n(λ)
=
−r2n+1 (P2n+2(λ) −P2n(λ)) + r2n (P2n(λ) −P2n−2(λ))
≡
X
m
(ˆλ2)2n,2m P2m(λ).
(3.10)
Here use is made of eq. (3.8). A similar equation for P2n+1(λ) expresses the matrix elements
(ˆλ2)2n+1,2m+1 in terms of the rn’s. The coeﬃcients {rn} are iteratively determined by
0 = −1
hn
Z ∞
−∞
dλ d
dλ
n
e−N V (λ2)λ Pn(λ) Pn(λ)
o
= 2N(ˆλ2V ′(ˆλ2))nn −2n −1.
(3.11)
The asymptotic behavior of rn is determined in the large-N limit,
n, N →∞
while
2n
N = t
is kept ﬁxed,
(3.12)
to be
rn = r
 n
N

+ higher orders in 1
N .
(3.13)
Here r(t) is given by
1
2
X
k
gk
2k
k

r(t)k = t.
(3.14)
Next we expand the right hand side of the recursion relation (3.10) in terms of 1/N to get
(P(2n, N, λ) ≡P2n(λ))
N 2λ2 P(2n, N, λ) = −
 
4r(t)d2P
dt2 + 2dr(t)
dt
dP
dt
!
= −

2
q
r(t) d
dt
2
P(2n, N, λ).
(3.15)
11
It tells us that that the arguments of P appear only in the combinations t = 2n/N and x = Nλ
in the large-N limit. After the change of variables
t 7→u(t) ≡
Z t
0
dt′
2
p
r(t′),
(3.16)
we equivalently have
 
d2
du2 + x2
!
P(u, x) = 0.
(3.17)
The unique solution to this trigonometric diﬀerential equation which satisﬁes the boundary and
parity conditions
P(0, x) = 1,
P(u, −x) = P(u, x)
(3.18)
is
P(u, x) = lim
N→∞P2n( x
N )

n=Nt/2
= cos ux = Γ(1
2)
J−1
2 (ux)
(ux/2)−1
2
.
(3.19)
The odd-order polynomials are constructed out of normalized even-order ones as follows.
˜P2n+1(λ) ≡P2n+2(λ) −P2n(λ)
λ
(3.20)
are odd polynomials of order 2n + 1, and are orthogonal to λ2k+1, k = 0, · · · , n −1:
Z ∞
−∞
dλ e−NV (λ) ˜P2n+1(λ) λ2k+1
=
Z ∞
−∞
dλ e−NV (λ) (P2n+2(λ) −P2n(λ)) λ2k = 0.
(3.21)
The microscopic limit of (3.20) reads
˜P2n+1( x
N )

n=Nt/2
= 2
x
∂
∂t P2n( x
N )

n=Nt/2
.
(3.22)
Under the assumption that ˜P2n+1′(0)̸ = 0, change of normalization to P2n+1′(0) = 1 is imple-
mented by
P2n+1(λ) =
˜P2n+1(λ)
˜P2n+1′(0).
(3.23)
By inserting the asymptotic form of even-order polynomials (3.19) into (3.22) and normalizing
according to (3.23), we conclude
lim
N→∞N P2n+1( x
N )

n=Nt/2
= sin ux
u
= x Γ(3
2)
J 1
2 (ux)
(ux/2)
1
2
.
(3.24)
12
Now we proceed for a generic α by induction. Given a set of polynomials {P (α)
n
(λ)} which are
orthogonal with respect to the measure dλ λ2α e−NV (λ2) on [−∞, ∞], and are normalized by
P (α)
2n (0) = P (α)
2n+1
′(0) = 1, we note that
˜P (α+1)
n
(λ) ≡P (α)
n+2(λ) −P (α)
n
(λ)
λ2
(3.25)
are polynomials of order n.
They are orthogonal to each other with respect to the measure
dλ λ2(α+1) e−NV (λ2). Under the assumption that ˜P (α+1)
2n
(0), ˜P (α+1)
2n+1
′(0)̸ = 0, the correctly normal-
ized orthogonal polynomials are given by
P (α+1)
2n
(λ) =
˜P (α+1)
2n
(λ)
˜P (α+1)
2n
(0)
,
P (α+1)
2n+1 (λ) =
˜P (α+1)
2n+1 (λ)
˜P (α+1)
2n+1 ′(0)
.
(3.26)
If we substitute eqs. (3.4) for a given α into the microscopic limit of eq. (3.25), we conﬁrm that
˜P (α+1)
2n
( x
N )

n=Nt/2
=
−N Γ(α + 1
2)
p
r(t)
Jα+ 1
2 (u(t)x)
(u(t)/2)α−1
2 xα+ 1
2
,
(3.27a)
˜P (α+1)
2n+1 ( x
N )

n=Nt/2
=
−Γ(α + 3
2)
p
r(t)
Jα+ 3
2 (u(t)x)
(u(t)x/2)α+ 1
2
,
(3.27b)
˜P (α+1)
2n
(0)

n=Nt/2
=
−N
u(t)
(2α + 1)
p
r(t),
(3.28a)
˜P (α+1)
2n+1
′(0)

n=Nt/2
=
−N
u(t)
(2α + 3)
p
r(t).
(3.28b)
Thus eqs. (3.4) hold also for α+1 after normalizing according to (3.26). Together with the results
(3.19) and (3.24) for α = 0, this completes the proof of Theorem 2.
