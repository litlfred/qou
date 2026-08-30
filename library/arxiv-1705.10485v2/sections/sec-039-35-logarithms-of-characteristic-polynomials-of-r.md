---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-039-35-logarithms-of-characteristic-polynomials-of-r
section_title: "Logarithms of characteristic polynomials of random matrices"
section_number: 3.5
pages: 26-28
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In [KN12, Sections 3 and 4] and [FMN16, Section 7.5], the mod-Gaussian convergence of the following
random variables was proven:
random matrixMn random variableXn parameters tn residue θ(ξ)
Haar(U(n)) Re(log det(In−Mn)) logn
2
(G(1+ iξ
2 ))2
G(1+iξ)
Haar(USp(n)) log det(I2n−Mn)− 1
2 log πn
2 log n
2
G( 3
2 )
G( 3
2 +iξ)
Haar(SO(2n)) log det(I2n−Mn)− 1
2 log 8π
n log n
2
G( 1
2 )
G( 1
2 +iξ)
T able 1 Mod-Gaussian convergence of the characteristic polynomials of Haar-distributed random matrices in compact Lie
groups.
Here,G is Barnes’ function, which is the unique entire solution of the equationsG(1) = 1 andG(z + 1) =
G(z)Γ (z). Moreover, the mod-Gaussian convergence holds in fact on an half-planeH ={z∈ C| Re(z)>
−α}. In the sequel, we denoteXA
n,XC
n andXD
n the mod-Gaussian convergent random variables, according
to the type of the classical group (A for unitary groups,C for compact symplectic groups andD for even
orthogonal groups). Before computing zones of control for these variables, let us make the following
essential remark:
Remark 26.Let (Xn)n∈N be a sequence of random variables that is mod-Gaussian convergent on a domain
D⊂ C which contains a neighborhood of0 (this ensures thatθn and all its derivatives converge towards
those ofθ). We denote(tn)n∈N the parameters of mod-Gaussian convergence of(Xn)n∈N. Then, without
generality, one can assumeθ′
n(0) =θ′′
n(0) = 0 and θ′(0) =θ′′(0) = 0. Indeed, set
~Xn =Xn + iθ′
n(0) ; ~tn =tn−θ′′
n(0).
We then have
~θn(ξ) := E[eiξ~Xn] e~tn
ξ2
2 =θn(ξ) e−θ′
n(0)ξ−θ′′
n(0)ξ2
2
and this new residue satisﬁes~θ′
n(0) =~θ′′
n(0) = 0. For the construction of zones of control, it allows us to
force v = 3, up to a translation ofXn and of the parametertn.
In the following, we only treat the case of unitary groups, the two other cases being totally similar (one
could also look at the imaginary part of the log-characteristic polynomial). There is an exact formula for
the Fourier transform ofXA
n [KS00, Formula (71)]:
E[eiξX A
n ] =
n∏
k=1
Γ (k)Γ (k + iξ)
(
Γ (k + iξ
2 )
)2 .
We haveE[XA
n ] = 0, and
~tn = E[(XA
n )2] = 1
2
n∑
k=1
Γ′′(k)
Γ (k) −
(Γ′(k)
Γ (k)
)2
= 1
2
n∑
k=1
ψ1(k),
Mod-φ convergence, II: Estimates on the speed of convergence 27
where ψ1(z) is the trigamma function d2
dz2 (logΓ (z)), and is given on integers by the remainder of the
series ζ(2):
ψ1(k) =
∞∑
m=k
1
m2.
Therefore,~tn = 1
2
∑∞
m=1
min(n,m)
m2 = 1
2(logn +γ + 1 +O(n−1)). So,(XA
n )n∈N is mod-Gaussian convergent
with parameters (~tn)n∈N and limit
~θ(ξ) =
(
G(1 + iξ
2 )
)2
G(1 + iξ) e
(γ+1)ξ2
4 ,
which satisﬁes~θ′(0) =~θ′′(0) = 0. With these conventions, we can write the residues~θn(ξ) as
~θn(ξ) =


n∏
k=1
Γ (k)Γ (k + iξ)
(
Γ (k + iξ
2 )
)2

 e
~tnξ2
2 =
n∏
k=1

Γ (k)Γ (k + iξ)
(
Γ (k + iξ
2 )
)2 e
ψ1 (k)ξ2
4

.
Denoteϑk(ξ) the terms of the product on the right-hand side; we use a similar strategy as in Section 3.1
for computing a zone of control. The functionϕk(ξ) = logϑk(ξ) vanishes at0, has its two ﬁrst derivatives
that also vanish at0, and therefore writes as
ϕk(ξ) =
(∫ 1
0
ϕ′′′
k (tξ) (1−t)2dt
)ξ3
2 .
The third derivative ofϕk(ξ) is given by
ϕ′′′
k (ξ) =−iψ2(k + iξ) + i
2ψ2
(
k + iξ
2
)
,
with ψ2(z) =−2∑∞
j=0
1
(j+z)3. As a consequence,ϕ′′′
k (ξ) is uniformly boundedon R by
3
∞∑
j=0
1
(j +k)3≤ 3ζ(3)
k2 .
Therefore,
|ϕk(ξ)|≤ ζ(3)|ξ|3
2k2 ;
|ϑk(ξ)|≤ e
ζ(3)|ξ|3
2k2 ;
|ϑk(ξ)− 1|≤ ζ(3)|ξ|3
2k2 e
ζ(3)|ξ|3
2k2 .
It follows that for anyn and anyξ∈ R,|~θn(ξ)− 1|≤ S expS with S =∑∞
k=1
ζ(3)|ξ|3
2k2 = 3ζ(3)|ξ|3
π2 . Set
K1 = K2 = 3ζ(3)
π2 , andK = 1
4K2
= π2
12ζ(3). We have a zone of control[−Ktn,Ktn] of index (3, 3), with
constantsK1 and K2. We conclude with Theorem 20:
Proposition 27.LetMn be a random unitary matrix taken according to the Haar measure. Forn large
enough,
dKol
(
Re(log det(In−Mn))√
Var(Re(log det(In−Mn)))
,NR(0, 1)
)
≤ C
(logn)3/2
with a constant C ≤ 18. Up to a change of the constant, the same result holds if one replaces
Re(log det(In−Mn)) by Im(log det(In−Mn)), or by
