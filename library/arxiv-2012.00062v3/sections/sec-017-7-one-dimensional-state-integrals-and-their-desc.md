---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-017-7-one-dimensional-state-integrals-and-their-desc
section_title: "One-dimensional state-integrals and their descendants"
section_number: 7
pages: 62-65
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
In a sense, the results of our paper are not about the asymptotics and resurgence of com-
plex Chern–Simons theory, but rather involve power series andq-diﬀerence equations that
arise fromK2-Lagrangians (clearly advocated in Kontsevich’s talks [Kon20]), or from sym-
plectic matrices (advocated in [GZb, Sec.7]). The connection with complex Chern–Simons
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 63
theory comes via ideal triangulations of a 3-manifold with torus boundary components, a
concept introduced by Thurston for the study of complete hyperbolic structures and their
deformations [Thu77]. The gluing equations of such triangulations are encoded by matrices
which are the upper half of a symplectic matrix (see Neumann-Zagier [NZ85]). The up-
per half of these symplectic matrices deﬁne state-integrals, as well as the asymptotic series
Φ(x;τ) (this was the approach taken in [DG13]) and the 3D-index (see [DGG14]).
In this section we discuss brieﬂy general one-dimensional state-integrals and their descen-
dants, and their asymptotic series. We will not aim for maximum generality, but instead
consider the one-dimensional state-integral
ZA,r(u,t ;τ) =
∫
R +i0
( r∏
j=1
Φb(v +uj)
)
e−Aπiv2+2πivtdv, (321)
whereu = (u1,...,u r)∈ C r with|Imuj|<|Imcb| (this ensures that all poles of the integrand
are above the real axis),t∈ C andA andr integers withr >A> 0. (This ensures that the
integrand decays exponentially at inﬁnity, hence the integral is absolutely convergent.) We
have already encountered two special cases in Equations (125) and (240):
41 : (A,r ) = (1, 2), (u1,u 2) = (u, 0), w =−2u, (322)
52 : (A,r ) = (2, 3), (u1,u 2,u 3) = (0,u,−u), w = 0. (323)
We are interested in the descendants ofZ deﬁned by
zA,r,m,µ(u,t ;τ) = (−1)m+µq− 1
2m ˜q− 1
2µZA,r(u,t−mib +µib−1;τ) (324)
for integersm and µ, where the extra factor was inserted to simplify the formulas below.
We will express the factorization of the state-integral (324) in terms of the auxiliary
function
GA,r(y,z ;q) = 1
(q;q)∞
∞∑
n=0
(−1)Anq
A
2n(n+1)zn
r∏
j=1
(q1+nyj;q)∞ (325)
for y = (y1,...,y r) and its specialization
b(k)
m (x,w ;q) = 1
xm
k
GA,r
( 1
xk
x,x−A
k w−1qm;q
)
q (326)
for x = (x1,...,x r) and its renormalization
B(k)
m (x,w ;q) =θ(−q−1/2xk;q)−A+1θ(−q−1/2xkw;q)−1θ(w;q)b(k)
m (x,w ;q) (327)
for k = 1,...,r .
Theorem 28.(a) The descendant state-integral can be expressed in terms of the descendant
holomorphic blocks by
zA,r,m,µ(u,t ;τ) =B−µ(˜x, ˜w; ˜q−1)T ∆(τ)Bm(x,w ;q), (m,µ∈ Z ) (328)
where
xj = e2πbuj, ˜xj = e2πb−1uj, w = e2πbt, ˜w = e2πb−1t. (329)
and
∆(τ) = e− iπ
4 + (A−2)iπ
12 (τ+τ−1)1 (330)
64 STA VROS GAROUF ALIDIS, JIE GU, AND MARCOS MARIÑO
and Bm(x,w ;q) = ( B(1)
m (x,w ;q),...,B (r)
m (x,w ;q))T. Consider the matrix Wm(x,w ;q) de-
ﬁned by
Wm(x,w ;q) =


B(1)
m (x,w ;q) ... B (r)
m (x,w ;q)
... ...
B(1)
m+r−1(x,w ;q) ... B (r)
m+r−1(x,w ;q)

 (331)
(b) The entries ofWm(x,w ;q) are holomorphic functions of|q|⁄ = 1 and meromorphic func-
tions of (x,w )∈ (C ∗)r× C ∗ with poles inxj∈qZ (for j = 1,...,r ) andw∈qZ of order at
most r.
(c) The columns ofWm(x,w ;q) are a basis of solutions of the linearq-diﬀerence equation
ˆB(Sm,qm,x,w,q )fm(x;q) = 0 for|q|⁄ = 1 and m∈ Z where
ˆB(Sm,qm,x,w,q ) =
r∏
k=1
(1−xiSm)− (−q)Aw−1qmSA
m. (332)
In particular,m↦→zA,r,m,µ(u,t ;τ) is annihilated by the operatorˆB(Sm,qm,x,w,q ).
Proof. For part (a), summing up all the residues of the integrand of (321) in the upper
half-plane as in [GK17], we ﬁnd that
zA,r,m,µ(u,t ;τ) = e−πi
12 + 1
3πic2
b+2πicbt
r∑
k=1
e−Aπi(uk−cb)2−2πiuktb(k)
m (x,w ;q)b(k)
µ (˜x, ˜w; ˜q−1) (333)
= e−πi
12 + 1
3πic2
b+πi
12 (A−1)(τ+τ−1)
r∑
k=1
B(k)
m (x,w ;q)B(k)
µ (˜x, ˜w; ˜q−1) (334)
The last equation follows from (111a) (which takes care ofe−Aπi(uk−cb)2
) and (111b) (which
takes care of thet-terms under the assumption thatukt =ρku andt =ρu for integersρ and
ρk)
For part (b), note that GA,r(y,z ;q) is symmetric with respect to permutation of the
coordinates ofy and that the specialization toyr = 1 is given by
GA,r(y,z ;q)|yr=1 =
∞∑
n=0
(−1)Anq
A
2n(n+1)
(q;q)n
zn
r−1∏
j=1
(q1+nyj;q)∞, (|q|⁄ = 1). (335)
It follows thatGA,r(y,z ;q)|yr=1 is holomorphic for(y,z )∈ C r−1×{ 1}× C when|q|< 1 and
meromorphic in (y,z )∈ (C ∗)r−1×{ 1}× C ∗ with poles inyj∈ qN for j = 1,...,r . Since
b(k)
m (x,w ;q) are expressed in terms of a specialization ofGA,r(y,z ;q)|yr=1, part (b) follows.
Part (c) follows from Equation (326) and the fact (proven by a standard creative telescop-
ing argument) that the functionz↦→GA,r(y,z ;q) is annihilated by the operator
r∏
k=1
(1−ykLz)− (−q)AzLA
z (336)
where Lz shifts z to qz. □
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY 65
