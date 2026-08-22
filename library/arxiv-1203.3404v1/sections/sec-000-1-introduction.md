---
doc_id: arxiv-1203.3404v1
doc_title: "On local solutions of the Ramanujan equation and their connection formulae"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1203.3404v1.pdf
source_sha256: 2318b14fb2702665
doc_brief: "On local solutions of the Ramanujan equation and their connection formulae — We show connection formulae of local solutions of the Ramanu jan equation between the origin and the inﬁnity."
---
In this papar, we show two essentially diﬀerent connection formulae of some
basic hypergeometric series between the origin and the inﬁnity. In 1 846,
E. Heine [5] introduced the basic hypergeometric series 2ϕ 1(a,b ;c;q,x ) as
follows;
2ϕ 1(a,b ;c;q,x ) :=
∑
n≥0
(a,b ;q)n
(c;q)n(q;q)n
xn, c ⁄∈q−N. (1)
Here, (a;q)n is the q-shifted factorial;
(a;q)n :=
{
1, n = 0,
(1 −a)(1 −aq)... (1 −aqn−1), n ≥ 1,
moreover, (a;q)∞ := lim n→∞(a;q)n and
(a1,a 2,...,a m;q)∞ := (a1;q)∞(a2;q)∞... (am;q)∞.
∗ Graduate School of Information Science and Technology, Osaka U niversity, 1-1
Machikaneyama-machi, Toyonaka, 560-0043, Japan.
1
The q-shifted factorial (a;q)n is a q-analogue of the shifted factorial ( α )n;
(α )n :=
{
1, n = 0,
α (α + 1)... {α + (n − 1)}, n ≥ 1.
The basic hypergeometric series (1) is a q-analogue of the hypergeometric
series 2F1(α,β ;γ,z )[3];
2F1(α,β ;γ,z ) :=
∑
n≥0
(α )n(β )n
(γ)nn! zn. (2)
This series (2) has the following famous degeneration diagram
Gauss Kummer
Bessel
Weber
Airy✲ ✟✟✟✟ ✯
❍❍❍❍ ❥✟✟✟✟ ✯
❍❍❍❍ ❥
(3)
Recently, Y. Ohyama [11] shows that there exists “the digeneratio n dia-
gram” of Heine’s series (1) as follows:
2ϕ 1(a,b ;c;z) 1ϕ 1(a;c;z)
1ϕ 1(a; 0;z)
J (3)
ν
J (1)
ν ,J (2)
ν
q-Airy
Ramanujan
✲ ✑✑✑ ✸
✲
✲
◗◗◗ s ✟✟ ✯
PPP q
We remark that there exist three diﬀerent q-Bessel functionsJ (j)
ν ,j = 1, 2, 3[2]
and two q-analogues of the Airy function. In this point, this diagram is
essentially diﬀerent from the diagram (3).
Ismail has pointed out that the Ramanujan function is one of q-analogues
of the Airy function [6]. The Ramanujan function appears in the third iden-
tity on p.57 of Ramanujan’s “Lost notebook” [12] as follows (with x replaced
byq):
Aq(−a) =
∑
n≥0
anqn2
(q;q)n
=
∏
n≥1
(
1 + aq2n−1
1 −qny1 −q2ny2 −q3ny3 − · · ·
)
2
where
y1 = 1
(1 −q)ψ 2(q),
y2 = 0,
y3 = q +q3
(1 −q)(1 −q2)(1 −q3)ψ 2(q) −
∑
n≥0
(2n+1)q2n+1
1−q2n+1
(1 −q)3ψ 6(q) ,
y4 =y1y3,
ψ (q) =
∑
n≥0
q
n(n+1)
2 = (q2;q2)∞
(q;q2)∞
.
To be precise, the Ramanujan function is given by
Aq(x) :=
∑
n≥0
qn2
(q;q)n
(−x)n.
This function satisﬁes the following second order linear q-diﬀerence equation;
qxu(q2x) −u(qx) +u(x) = 0. (4)
The equation (4) has another solution which is given by a divergent se ries
θq(x)2ϕ 0
(
0, 0; −;q, −x
q
)
=θq(x)
∑
n≥0
1
(q;q)n
{
(−1)nq
n(n− 1)
2
} −1(
−x
q
) n
.
Here, θq(·) is the theta function of Jacobi (see the section 2).
An asymptotic formula for the Ramanujan function is obtained by M. E. H. Is-
mail and C. Zhang as follows[7];
Aq(x) = (qx,q/x ;q2)∞
(q;q2)∞
1ϕ 1
(
0;q;q2, q2
x
)
−q(q2x, 1/x ;q2)∞
(1 −q)(q;q2)∞
1ϕ 1
(
0;q3;q2, q3
x
)
.
(5)
From the viewpoint of connection problems on q-diﬀerence equations, we
can regard the formula (5) as one of connection formulae of the Ra manujan
function.
3
The other q-analogue of the Airy function is known as the q-Airy function
Aiq(·). The q-Airy function has found in the study of the second q-Painlev´ e
equation[4]. The function Ai q(·) is deﬁned by
Aiq(x) :=
∑
n≥0
1
(−q;q)n(q;q)n
{
(−1)nq
n(n− 1)
2
}
(−x)n
and satisﬁes the following q-diﬀerence equation
u(q2x) +xu(qx) −u(x) = 0. (6)
The other solution of the equation (6) around the origin is given by
u(x) = θq(q2x)
θq(−q2x) Aiq(−x).
Ismail also has pointed out the Ramanujan function and the q-Airy function
are diﬀerent. But the relation between them has not known. In the section
3, we give the connection formula between these functions with usin g the
q-Borel-Laplace transformations of the second kind.
Theorem For any x ∈ C∗, we have
Aq2
(
−q3
x2
)
= 1
(q, −1;q)∞
{
θ
(x
q
)
Aiq(−x) +θ
(
−x
q
)
Aiq(x)
}
.
Connection problems on linear q-diﬀerence equations between the origin
and the inﬁnity are studied by G. D. Birkhoﬀ [1]. The ﬁrst example of th e
connection formula was found by G. N. Watson [14] in 1912. This form ula is
known as “Watson’s formula for 2ϕ 1(a,b ;c;q,x )” as follows [2];
2ϕ 1 (a,b ;c;q;x) = (b,c/a ;q)∞(ax,q/ax ;q)∞
(c,b/a ;q)∞(x,q/x ;q)∞
2ϕ 1 (a,aq/c ;aq/b ;q;cq/abx )
+ (a,c/b ;q)∞(bx,q/bx ;q)∞
(c,a/b ;q)∞(x,q/x ;q)∞
2ϕ 1 (b,bq/c ;bq/a ;q;cq/abx ).
(7)
But other connection formulae had not found for a long time. Recen tly,
C. Zhang gives connection formulae for some conﬂuent type basic h yper-
geometric series [15, 16, 17]. In [16], Zhang gives a connection formu la of
Jackson’s ﬁrst and second q-Bessel function J (j)
ν (x;q), (j = 1, 2);
J (1)
ν (x;q) := (qν+1;q)∞
(q;q)∞
(x
2
) ν∑
n≥0
1
(qν+1;q)n
(
−x2
4
) n
4
and
J (2)
ν (x;q) := (qν+1;q)∞
(q;q)∞
(x
2
) ν∑
n≥0
qn2
(qν+1;q)n
(
−qνx2
4
) n
with using the q-Borel-Laplace transformations of the second kind B−
q and
L−
q . These transformations are deﬁned for a formal power series f (x) =∑
n≥0anxn, a0 = 1 as follow;
1. The q-Borel transformation of the second kind is
(B−
qf )(ξ) :=
∑
n≥0
anq− n(n− 1)
2 ξn (=:g(ξ)).
2. The q-Laplace transformation of the second kind is
(
L−
qg
)
(x) := 1
2πi
∫
|ξ|=r
g(ξ)θq
(x
ξ
) dξ
ξ ,
where r >0 is enough small number.
In [9] and [10], we obtained connection formulae of the Hahn-Exton q-
Bessel function
J (3)
ν (x;q) := (qν+1;q)∞
(q;q)∞
xν
∑
n≥0
q
n(n+1)
2
(qν+1;q)n
(
−x2) n
and the q-conﬂuent type basic hypergeometric function
1ϕ 1(a;b;q,x ) :=
∑
n≥0
(a;q)n
(b;q)n(q;q)n
(−1)nq
n(n− 1)
2 xn
by these transformations. In section 3, we use these transform ations to obtain
connection formula between the Ramanujan function and the q-Airy function.
On the other hand, the q-Borel-Laplace transformations of the ﬁrst kind
are deﬁned for a formal power series as follow;
1. The q-Borel transformation of the ﬁrst kind is
(
B+
qf
)
(ξ) :=
∑
n≥0
anq
n(n− 1)
2 ξn (=:ϕ (ξ)).
5
2. The q-Laplace transformation of the ﬁrst kind is
(
L+
qϕ
)
(x) := 1
1 −q
∫ λ ∞
0
ϕ (ξ)
θq
(ξ
x
) dqξ
ξ =
∑
n∈Z
ϕ (λq n)
θq
(λq n
x
) ,
here, this transformation is given by Jackson’s q-integral [2].
These two diﬀerent types of q-Borel-Laplace transformations are introduced
by J. Sauloy [13] and stusied by C. Zhang. We remark that each q-Borel
transformation is formal inverse of each q-Laplace transformation, i.e.,
L±
q ◦ B±
qf =f.
The application of the q-Borel-Laplace transformations of the ﬁrst kind is
found in [15, 17]. Zhang gives the connection formula of the divergen t basic
hypergeometric series 2ϕ 0(a,b ; −;q,x ) as follows;
Theorem (Zhang, [15]) For any x ∈ C∗, we have
2f0(a,b ;λ,q,x )
= (b;q)∞
(b/a ;q)∞
θq(aλ)
θq(λ)
θq(qax/λ )
θq(λ/x ) 2ϕ 1
(
a, 0;aq
b ;q, q
abx
)
+ (a;q)∞
(a/b ;q)∞
θq(bλ)
θq(λ)
θq(qbx/λ )
θq(λ/x )
2ϕ 1
(
b, 0;bq
a ;q, q
abx
)
whereλ ∈ C∗ \ {−qn;n ∈ Z}.
Here, 2f0(a,b ;λ,q,x ) in the left-hand side is the q-Borel-Laplace trans-
form of the function 2ϕ 0(a,b ; −;q,x ). But other application of this method
(of the ﬁrst kind ) has not known. In the section 4, we show the con nection
formula of the divergent series
2ϕ 0(a,b ; −;q,x ) =
∑
n≥0
1
(q;q)n
{
(−1)nq
n(n− 1)
2
} −1
xn.
This formula is given by the following theorem;
Theorem For any x ∈ C∗ \ [−λ;q],
θq(x)2f0
(
0, 0; −;q, −x
q
)
= (q;q)∞
θq(x)θq2
(
− λ 2
qx
)
θq
(
− λ
q
)
θq
(λ
x
) 1ϕ 1
(
0;q;q2, q2
x
)
+ (q;q)∞
1 −q
θq(x)θq2
(
− λ 2
x
)
θq
(
− λ
q
)
θq
(λ
x
)
λ
x 1ϕ 1
(
0;q3;q2, q3
x
)
.
6
