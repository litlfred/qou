---
doc_id: arxiv-1404.2541v1
doc_title: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1404.2541v1.pdf
source_sha256: edb7c9b2b1561ac3
doc_brief: "The Stokes phenomenon for the Ramanujan’s q-difference equation and its higher order extension — We show connection formulae of local solutions of the Ramanu - jan equation between the origin and the"
---
In this papar, we deal with the Ramanujan equation
qxu(q2x) −u(qx) +u(x) = 0, ∀x ∈ C∗. (1)
We assume that 0 < |q|< 1. The Ramanujan equation (1) has solutions
u1(x) = 0ϕ 1(−; 0;q, −qx), (2)
u2(x) = θq(x)2ϕ 0
(
0, 0; −;q, −x
q
)
(3)
∗ Graduate School of Information Science and Technology, Osaka U niversity, 1-1
Machikaneyama-machi, Toyonaka, 560-0043, Japan.
1
around the origin. The equation (1) also has a fundamental system of solu-
tions around the inﬁnity [7]:
v1(x) = θq(x)
θq2(x) 1ϕ 1
(
0;q;q2, q2
x
)
(4)
v2(x) = q
q − 1
θq(x/q )
θq2(x/q )
1
x 1ϕ 1
(
0;q3;q2, q3
x
)
. (5)
Here, the function rϕ s(a1,...,a r;b1,...,b s;q,x ) is the basic hypergeometric
series with the base q [2]:
rϕ s(a1,...,a r;b1,...,b s;q,x )
:=
∑
n≥0
(a1,...,a r;q)n
(b1,...,b s;q)n(q;q)n
{
(−1)nq
n(n− 1)
2
} 1+s−r
xn.
The notation (a;q)n is the q-shifted factorial;
(a;q)n :=
{
1, n = 0,
(1 −a)(1 −aq)... (1 −aqn−1), n ≥ 1,
moreover, (a;q)∞ := lim n→∞(a;q)n and
(a1,a 2,...,a m;q)∞ := (a1;q)∞(a2;q)∞... (am;q)∞.
The basic hypergeometric series has radius of convergence ∞, 1 or 0 according
to whether r −s <1,r −s = 1 or r −s >1. We remark that the solution
u2(x) contains a divergent series and other solutions u1(x), v1(x) and v2(x)
are convergent series. We study the relation between these solut ions from
the viewpoint of connection problems on linear q-diﬀerence equations. The
functionθq(x) is the theta function of Jacobi with the base q (see section two
for more details).
The solution u1(x) is called the Ramanujan function, which has found by
Ramanujan [12]. M. E. H. Ismail [7] has introduced the notation
Aq(x) :=
∑
n≥0
qn2
(q;q)n
(−x)n = 0ϕ 1(−; 0;q, −qx).
2
He shows that A q(x) is one of q-analogues of the Airy function [6]. The Ra-
manujan function A q(x) appears in the third identity on p.57 of Ramanujan’s
“Lost notebook” [12] as follows (with x replaced by q):
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
Strictly speaking, Ramanujan has not shown that the Ramanujan f unction
Aq(x) satisﬁes the equation (1). But we propose that the equation (1) is
named “the Ramanujan equation” after his study.
We review someq-special functions and connection formulae of these func-
tions. Recently, Y. Ohyama [11] shows that there exists “the digen eration
diagram” for Heine’s series 2ϕ 1(a,b ;c;q,x ):
2ϕ 1(a,b ;c;z) q-conﬂuent
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
(6)
We remark that there exist three diﬀerent types of q-Bessel functions
J (j)
ν ,j = 1, 2, 3 [2] and twoq-analogues of the Airy function. These q-analogue
are solutions of diﬀerent types of linear q-diﬀerence equations. In this point,
3
this diagram is essentially diﬀerent from the diﬀerential case:
Gauss Kummer
Bessel
Weber
Airy✲ ✟✟✟✟ ✯
❍❍❍❍ ❥✟✟✟✟ ✯
❍❍❍❍ ❥
The Ramanujan function is the most degenerated case in the diagra m
(6). We study connection problems on linear q-diﬀerence equations between
around the origin and around the inﬁnity with irregular singular points . The
irregularity of q-diﬀerence equations and q-diﬀerence modules for some cases
of slopes of the Newton polygons are studied by J.-P. Ramis, J. Saulo y and
C. Zhang [13]. Graphically, these (formal) invariants are the height o f the
right part of the Newton polygon, from the bottom to the upper rig ht end.
In this paper, we show connection formulae for the Ramanujan equ ation.
Connection problems on linear q-diﬀerence equations between the origin and
the inﬁnity are studied by G. D. Birkhoﬀ [1].
Connection formulae of second order linear q-diﬀerence equations are lin-
ear relations in a matrix form:
(u1(x)
u2(x)
)
=
(C11(x) C12(x)
C21(x) C22(x)
)( v1(x)
v2(x)
)
.
Here, u1(x) and u2(x) are solutions around the origin, v1(x) and v2(x) are
solutions around inﬁnity and Cij (1 ≤i,j ≤ 2) are doubly periodic functions
such that
σqCij(x) = Cij(x), C ij(e2πix) = Cij(x),
namely,q-elliptic functions. The ﬁrst example of the connection formula with
regular singular points was found by G. N. Watson [15] in 1912:
2ϕ 1 (a,b ;c;q;x) = (b,c/a ;q)∞(ax,q/ax ;q)∞
(c,b/a ;q)∞(x,q/x ;q)∞
2ϕ 1 (a,aq/c ;aq/b ;q;cq/abx )
+ (a,c/b ;q)∞(bx,q/bx ;q)∞
(c,a/b ;q)∞(x,q/x ;q)∞
2ϕ 1 (b,bq/c ;bq/a ;q;cq/abx ).
But connection formulae for irregular singular case had not found f or a long
time. Recently, C. Zhang gives connection formulae for some conﬂu ent type
basic hypergeometric series [16, 17, 18]. In [17], Zhang gives a conne ction
4
matrix of Jackson’s ﬁrst and second q-Bessel function J (j)
ν (x;q), (j = 1, 2) [2]
with using the q-Borel-Laplace transformations of the second kind. Zhang
also gives the connection formula for the divergent seties 2ϕ 0(a,b ; −;q,x )
in [16, 18] with using the q-Borel-Laplace transformations of the ﬁrst kind.
These resummation method are powerful tools for connection pro blems with
irregular singular points. We deﬁne these transformations later.
The connection formula for the solution (3), i.e., u2(x) has not known.
We remark that the basic hypergeometric part 2ϕ 0(0, 0; −;q, −x/q ) in this
solution is a divergent series around the origin and the q-Stokes phenomenon
occurs [14]. Therefore, we need a suitale resummation method, whic h is
the q-Borel-Laplace transformations of the ﬁrst kind. By this resumma tion
method, we obtain the following connection formula in the matrix form ex-
actly and solve the connection problem on the Ramanujan equation.
Theorem. For any x ∈ C∗ \ [−λ;q], we have
(
u1(x)
˜u2(x,λ )
)
=
(C11(x) C12(x)
˜C21(x) ˜C22(x)
)(
v1(x)
v2(x)
)
,
provided that
C11(x) = θq2(qx)θq2(x)
(q,q 2;q2)∞θq(x), C 12(x) = θq2(x)θq2(x/q )
(q,q 2;q2)∞θq(x/q ),
˜C21(x) = (q;q)∞θq2(−qx/λ 2)θq2(x)
θq(−q/λ )θq(x/λ )θq(x)
and
˜C22(x) = (q;q)∞θq2(−x/λ 2)θq2(x/q )
θq(−1/λ )θq(x/λ )θq(x/q ) .
Here, the function ˜u2(x,λ ) is
˜u2(x,λ ) = θq(x)2f0(0, 0; −;q,λ, −x/q )
which is meromorphic function on C∗ \ [−λ;q] and the set [λ;q] is the q-
spiral(see section two). We denote 2f0(0, 0; −;q,λ, −x/q ) as the resummation
of 2ϕ 0(0, 0; −;q, −x/q ).
We show this formula with the using of the q-Borel-Laplace method of
the ﬁrst kind. The connection formula between the Ramanujan fun ction and
5
the q-Airy function has given with the using of the q-Borel-Laplace method
of the second kind.
Theorem (Morita[9]) For any x ∈ C∗, we have
Aq2
(
−q3
x2
)
= 1
(q, −1;q)∞
{
θq
(x
q
)
Aiq(−x) +θq
(
−x
q
)
Aiq(x)
}
. (7)
Here, the function Ai q(x) is the q-Airy function, which is another q-
analogue of the Airy function. The q-Airy function Ai q(x) is found as a
special solution of the second q-Painlev´ e equation by K. Kajiwara, T. Ma-
suda, M. Noumi, Y. Ohta and Y. Yamada [4, 8] . The function Ai q(x) is
deﬁned by
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
(−x)n.
These functions A q(x) and Ai q(x) are most degenerated case in the dia-
gram for Heine’s 2ϕ 1(a,b ;c;q,x ) series (6) and satisfy diﬀerent two types of
second order q-diﬀerence equations. The Ramanujan function A q(x) satisﬁes
qxu(q2x) −u(qx) +u(x) = 0
and the q-Airy function Ai q(x) satisﬁes
u(q2x) +xu(qx) −u(x) = 0.
Ismail also has pointed out the Ramanujan function and the q-Airy func-
tion are diﬀerent. But the relation between them has not known. Ou r con-
nection formula (7) shows that the Ramanujan function can be rep resented
by the q-Airy functions.
We remark that the connection formula for u1(x) is essentially given by
Ismail and C. Zhang as follows [7]:
Aq(x) = (qx,q/x ;q2)∞
(q;q2)∞
1ϕ 1
(
0;q;q2, q2
x
)
− q(q2x, 1/x ;q2)∞
(1 −q)(q;q2)∞
1ϕ 1
(
0;q3;q2, q3
x
)
. (8)
They give (8) as an asymptotic formula for the Ramanujan function . But
from the viewpoint of connection problems on q-diﬀerence equations, we
6
can regard the formula (8) as one of connection formulae of the Ra manujan
function. In fact, we can rewrite this formula as follows:
u(x) = θq2(qx)θq2(x)
(q,q 2;q2)∞θq(x)v1(x) + θq2(x)θq2(x/q )
(q,q 2;q2)∞θq(x/q )v2(x).
Here, connection coeﬃcients are q2-elliptic functions. In [9], we derive Ismail-
Zhang’s formula (8) from (7) by suitable algebraic transformation.
In the last section, we introduce the q-Borel-Laplace transformations of
levelr − 1. These transformations are higher order extension of the q-Borel-
Laplace transformations. We also apply these new method to a diver gent
series rϕ 0(0, 0,..., 0; −;q,x ) and give the asymptotic formula as follows:
Theorem. For any C∗ \ [−λ;qr−1], we have
(
L+
qr− 1,λ ◦ B+
qr− 1 rϕ 0(0, 0,..., 0; −;q,x )
)
= 1
θqr− 1
(λ
x
) (q;q)∞
θq(−λ)θ
qr(r− 1)
(
(−1)r− 1q
(r− 1)(r− 2)
2 ( λ
x )
r
)
× r−1ϕ r−1
(
0, 0,..., 0;q,q 2,...,q r−1;qr,q
(r− 1)(r− 2)
2 /x
)
+...
+ 1
θqr− 1
(λ
x
) (q;q)∞
θq(−λ)θ
qr(r− 1)
(
(−1)r− 1q
3r(r− 1)
2 ( λ
x )
r
)
× (−1)r−1q
(r− 1)(r− 2)
2
(1 −q)(1 −q2)... (1 −qr−1)
(q
λ
) r−1
× r−1ϕ r−1
(
0, 0,..., 0;qr,q r+1,...,q 2r−1;qr,q
3r(r− 1)
2 /x
)
