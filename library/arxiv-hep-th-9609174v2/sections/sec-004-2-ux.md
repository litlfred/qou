---
doc_id: arxiv-hep-th-9609174v2
doc_title: "Universality of random matrices in the microscopic limit and the Dirac operator spectrum"
section_id: sec-004-2-ux
section_title: "(ux)"
section_number: 2
pages: 13-14
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
doc_brief: "Universality of random matrices in the microscopic limit and the Dirac operator spectrum — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom"
---
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
3.2
Universal correlations
The integration kernel associated with the eigenvalue problem of M is (for brevity we set N =
odd = 2N + 1)
KN(λ, µ)=(λ µ)α e−N
