---
doc_id: arxiv-1205.1453v2
doc_title: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1205.1453v2.pdf
source_sha256: 29d1b1fd9466a3d8
doc_brief: "An asymptotic formula of the divergent bilateral basic hypergeometric series Takeshi MORITA∗ — We show an asymptotic formula of the divergent bilateral bas ic hypergeometric series 1ψ 0(a; −;q, ·)"
---
In this paper, we show an asymptotic formula of the divergent bilate ral basic
hypergeometric series
1ψ 0(a; −;q;x) :=
∑
n∈ Z
(a;q)n
{
(−1)nq
n(n− 1)
2
} − 1
xn.
Here, (a;q)n is the q-shifted factorial;
(a;q)n :=



1, n = 0,
(1 −a)(1 −aq)... (1 −aqn− 1), n ≥ 1,
[(1 −aq− 1)(1 −aq− 2)... (1 −aqn)]− 1, n ≤ −1
moreover, (a;q)∞ := lim n→∞ (a;q)n and
(a1,a 2,...,a m;q)∞ := (a1;q)∞ (a2;q)∞ ... (am;q)∞ .
The q-shifted factorial (a;q)n is a q-analogue of the shifted factorial
(α )n =α {α + 1} · · · {α + (n − 1)}.
∗ Graduate School of Information Science and Technology, Osaka U niversity, 1-1
Machikaneyama-machi, Toyonaka, 560-0043, Japan.
1
The series 1ψ 0(a; −;q, ·) is related to the bilateral basic hypergeometric series
1ψ 1(a;b;q, ·). At ﬁrst, we review the series
1ψ 1(a;b;q,z ) :=
∑
n∈ Z
(a;q)n
(b;q)n
zn.
This series has Ramanujan’s summation formula [3]
1ψ 1(a;b;q,z ) = (q,b/a,az,q/az ;q)∞
(b,q/a,z,b/az ;q)∞
, |b/a |< |z|< 1, (1)
which was ﬁrst given by Ramanujan [4]. This formula is considered as a
extension of the q-binomial theorem [3, 1];
∑
n≥ 0
(a;q)n
(q;q)n
zn = (az;q)∞
(z;q)∞
, |z|< 1.
We also regard the summation (1) as a q-analogue of the bilateral binomial
theorem [6] discovered by M. E. Horn. If α and β are complex numbers
ℜ(β −α )> 1 and z is a complex number with |z| = 1, then
∑
n∈ Z
(α )n
(β )n
zn = (1 −z)β − α − 1
(−z)β − 1
Γ(1 −α )Γ(β )
Γ(β −α ) . (2)
We remark that the limit q → 1 − 0 of (1) with suitable condition gives the
bilateral binomial theorem (2).
The series 1ψ 1(a;b;q,z ) satisﬁes the following q-diﬀerence equation
( b
q −az
)
u(qz) + (z − 1)u(z) = 0.
In this paper, we study the degeneration of this equation as follows ;
( 1
q −ax
)
˜u(qx) +x˜u(x) = 0.
This equation has a formal solution
˜u(x) = 1ψ 0(a; −;q,x ). (3)
2
But ˜u(x) is a divergent around the origin [3] and its properties are not clear .
In section three, we show an asymptotic formula of the series (3) w ith using
the q-Borel-Laplace transformations. The q-Borel-Laplace transformations
are introduced in the study of connection problems on linear q-diﬀerence
equations between the origin and the inﬁnity.
Connection problems onq-diﬀerence equations with regular singular points
are studied by G. D. Birkhoﬀ [2]. The ﬁrst example of the connection f ormula
is given by G. N. Watson [13] in 1910 as follows;
2ϕ 1(a,b ;c;q,x ) = (b,c/a ;q)∞ (ax,q/ax ;q)∞
(c,b/a ;q)∞ (x,q/x ;q)∞
2ϕ 1 (a,aq/c ;aq/b ;q,cq/abx )
+ (a,c/b ;q)∞ (bx,q/bx ;q)∞
(c,a/b ;q)∞ (x,q/x ;q)∞
2ϕ 1 (b,bq/c ;bq/a ;q,cq/abx ). (4)
The function 2ϕ 1(a,b ;c;q,x ) is the basic hypergeometric series
2ϕ 1(a,b ;c;q,x ) =
∑
n≥ 0
(a,b ;q)n
(c;q)n(q;q)n
xn,
which is introduced by E. Heine [5]. This series satisﬁes the second ord er
linear q-diﬀerence equation
(c −abqx)u(q2x) − {c +q − (a +b)qx}u(qx) +q(1 −x)u(x) = 0. (5)
around the origin. On the other hand, the equation (5) has a funda mental
system of solutions
v1(x) = θ(−ax)
θ(−x) 2ϕ 1
(
a, aq
c ;aq
b ;q, cq
abx
)
, v 2(x) = θ(−bx)
θ(−x) 2ϕ 1
(
b, bq
c ;bq
a ;q, cq
abx
)
around the inﬁnity [14]. Here, θ(·) is the theta function of Jacobi (see sec-
tion two). In the connection formula (4), we remark that the conn ection
coeﬃcients are given by q-elliptic functions.
Other connection formulae, especially connection formulae of irreg ular
singular type q-special functions has not known for a long time. Recently,
C. Zhang gives some connection formulae by two diﬀerent types of q-Borel
transformations and q-Laplace transformations [14, 15, 16], which are in-
troduced by J. Sauloy[11]. We assume that f (x) is a formal power series
f (x) = ∑
n≥ 0anxn, a0 = 1.
3
Deﬁnition 1. For any power series f (x), the q-Borel transformation of the
ﬁrst kind B+
q is
(
B+
qf
)
(ξ) :=
∑
n≥ 0
anq
n(n− 1)
2 ξn =:ϕ (ξ).
For an entire function ϕ , the q-Laplace transformation of the ﬁrst kind L+
q,λ
is (
L+
q,λ ϕ
)
(x) :=
∑
n∈ Z
ϕ (λq n)
θ
( λq n
x
) , λ ⁄∈qZ.
Similarly, the q-Borel transformation of the second kind B−
q is
(
B−
qf
)
(ξ) :=
∑
n≥ 0
anq− n(n− 1)
2 ξn =:g(ξ)
and the q-Laplace transformation of the second kind L−
q is
(
L−
qg
)
(x) := 1
2πi
∫
|ξ|=r
g(ξ)θ
( x
ξ
) dξ
ξ .
We remark that each q-Borel transformation is a formal inverse of each
q-Laplace transformation;
L+
q,λ ◦ B+
qf =f, L−
q ◦ B−
qf =f.
We can ﬁnd applications of the q-Borel-Laplace method of the ﬁrst kind
in [14, 15, 10]. This summation method is powerful to deal with diverge nt
type basic hypergeometric series and to study the q-Stokes phenomenon. Ap-
plications of the method of the second kind can be found in [16, 8, 9, 1 0]. But
other examples, for example, applications to bilateral basic hyperg eometric
series, has not known.
In this paper, we study an asymptotic formula of the divergent bilat -
eral basic hypergeometric series 1ψ 0(a; −;q, ·) from viewpoint of connection
problems on linear q-diﬀerence equations. We show the following theorem.
Theorem. For any x ∈ C∗ \ [−λ;q] , we have
ˆ1ψ 0(a; −;λ;q,x ) = (q;q)∞
(q/a ;q)∞
θ(aqλ )
θ(qλ )
θ (ax/λ )
θ (x/λ )
1
(1/ax ;q)∞
,
where 1< |ax|.
4
Here, the function ˆ1ψ 0(a; −;λ;q,x ) is the q-Borel-Laplace transform of
the series 1ψ 0(a; −;q,x ) and the set [ −λ;q] is the q-spiral which is given
by [λ;q] := {λq k : k ∈ Z}. We also show the limit q → 1 − 0 of our
asymptotic formula in section four. If we take a suitable limit q → 1 − 0 of
the theorem above, we formally obtain the asymptotic formula of th e bilateral
hypergeometric series 1H0.
