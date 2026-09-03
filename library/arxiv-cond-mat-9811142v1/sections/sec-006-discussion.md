---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges"
section_id: sec-006-discussion
section_title: "Discussion"
section_number: null
pages: 25-30
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
doc_brief: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges — For the orthogonal-unitary and symplectic-unitary transitions in random matrix the- ory, the"
---
5.1
Connection with β = 2 initial conditions
We have calculated exact formulas for the dynamical distribution function (2.8) in the
case of β = 1 and β = 4 initial conditions, with the ﬁnal state corresponding to a β = 2
equilibrium. If in these formulas we take the limit tX, tY →∞with tX −tY ﬁxed, then
we would expect no memory of the initial state to be retained, but rather the distribution
functions corresponding to a β = 2 initial condition (i.e. the equilibrium state) to result.
Consider ﬁrst the hard edge. Inspection of (3.31), (3.37), (3.49) and (3.50) shows that
in this limit
Shard
1
(X, Y ; tX, tY ) ∼Shard
4
(X, Y, ; tX, tY )
∼Shard
2
(X, Y, ; tX, tY ) := 1
4
Z 1
0 Ja
√
uX

Ja
√
uY

e−u(tX−tY ) du ,
(5.1)
˜Shard
1
(X, Y ; tX, tY ) ∼˜Shard
4
(X, Y, ; tX, tY )
∼˜Shard
2
(X, Y, ; tX, tY ) := −1
4
Z ∞
1
Ja
√
uX

Ja
√
uY

e−u(tX−tY ) du ,
(5.2)
while from (3.33), (3.54), (3.38) and (3.57) we see that
e(tX+tY ) ˜Ihard
1
(X, Y ; tX, tY ) ∼e(tX+tY ) ˜Ihard
4
(X, Y ; tX, tY ) ∼0 ,
(5.3)
e−(tX+tY ) Dhard
1
(X, Y ; tX, tY ) ∼e−(tX+tY ) Dhard
4
(X, Y ; tX, tY ) ∼0 .
(5.4)
Substituting these values in (2.24) and then using (2.26), and the formula
Pf(ZX) = (det(ZX))1/2,
we see by interchanges of particular rows and columns that ZX is equivalent to a block
matrix of the form
 
0n+m
A
−A
0n+m
!
,
25
where
A =


h
Shard
2

X(1)
j , X(1)
k ; t1, t1
i
n×n
h ˜Shard
2

X(1)
j , X(2)
k ; t1, t2
i
n×m
h ˜Shard
2

X(2)
j , X(1)
k ; t2, t1
i
m×n
h
Shard
2

X(2)
j , X(2)
k ; t2, t2
i
m×m

.
(5.5)
Thus the limiting form of the dynamical distribution is given by
ρ(n+m)

x(1)
1 , . . . , x(1)
n ; τ1; x(2)
1 , . . . , x(2)
m ; τ2

= det A .
(5.6)
The analysis in the soft edge case is very similar. The formulas (5.3) and (5.4) again
apply, as do the formulas (5.1) and (5.2) with Shard
2
, ˜Shard
2
replaced by
Ssoft
2
(X, Y ; tX, tY )
:=
Z ∞
0
Ai(X + v)Ai(Y + v)e−v(tY −tX)dv ,
(5.7)
˜Ssoft
2
(X, Y ; tX, tY )
:=
−
Z 0
−∞Ai(X + v)Ai(Y + v)e−v(tY −tX)dv .
(5.8)
We remark that in the case n = m = 1, the resulting formula for ρ(n+m) implied by (5.6)
and (5.5) in both the hard and soft edge theories agrees with that computed by Mˆacedo
[14, 15].
5.2
Connection between the soft and hard edges
For the hard edge distribution function of the Laguerre ensemble at β = 2 and τ = 0, it
is known that by taking the limit a →∞and introducing new scaled coordinates, the
distribution function of the soft edge of the Gaussian ensemble results [16]. Speciﬁcally,
the new scaled variable x is related to the scaled variable X of the hard edge by
X = a2 −2 a (a/2)1/3 x
(5.9)
and the distribution functions are related by
lim
a→∞

−2a(a/2)1/3n ρhard
(n)

a2 −2a(a/2)1/3x1, . . . , a2 −2a(a/2)1/3xn

= ρsoft
(n) (x1, . . . , xn) .
(5.10)
As noted in [16, 17] this property should persist for general β. Further, with appropriate
scaling of τ, the result would be expected to generalize to the dynamical distributions.
Let us ﬁrst check this latter point for the dynamical distribution with a β = 2 initial
condition (5.6). For this purpose we require the asymptotic expansion [18]
Ja(x) ∼
2
x
1/3
Ai
 21/3(a −x)
x1/3
!
(5.11)
valid for a and x large such that the argument of the Airy function is of order unity.
Changing variables u = 1 −w(2/a)2/3 in the integrals of (5.1) and (5.2) and introducing
the scaled coordinates (5.9), application of (5.11) shows
Ja
√ux

∼
2
a
1/3
Ai(x + w) .
(5.12)
26
Thus if we also scale t according to
tX 7→(a/2)2/3 tx
(5.13)
then we see that

−2a(a/2)1/3
Shard
2

a2 −2a(a/2)1/3x, a2 −2a(a/2)1/3y; (a/2)2/3tx, (a/2)2/3ty

∼e−(a/2)2/3(tx−ty)Ssoft
2
(x, y; tx, ty) ,

−2a(a/2)1/3 ˜Shard
2

a2 −2a(a/2)1/3x, a2 −2a(a/2)1/3y; (a/2)2/3tx, (a/2)2/3ty

∼e−(a/2)2/3(tx−ty)Ssoft
2
(x, y; tx, ty) .
Since, as seen from (2.24), the factors e−(a/2)2/3(tx−ty) do not aﬀect the value of ρ(n+m), we
thus have the dynamical extension of (5.10),
lim
a→∞

−2a(a/2)1/3n+m ρhard
(n+m)

a2 −2a(a/2)1/3x1, . . . , a2 −2a(a/2)1/3xn; (a/2)2/3tx;
a2 −2a(a/2)1/3y1, . . . , a2 −2a(a/2)1/3ym; (a/2)2/3ty

= ρhard
(n+m)(x1, . . . , xn; tx; y1, . . . , ym; ty) .(5.14)
Consider next β = 1 initial conditions. Inspection of (3.31), (3.37), (3.33) and (3.38)
shows that the analysis used above for β = 2 initial conditions again suﬃces to establish
the connection formula. For example, consider the formula (3.33) for ˜Ihard
1
. For large a
we see that
˜Ihard
1
(X, Y ; tX, tY )
∼
a2
4
Z ∞
1
s−1+a/2Ja
√
sY

e−stY
Z ∞
s
e−utX
u
Ja
√
uX

du −(X ↔Y ).
(5.15)
Use of the asymptotic expansion (5.12) ( after making the appropriate change of variables
in the integrals) shows

−2a(a/2)1/3 ˜Ihard
1

a2 −2a(a/2)1/3x, a2 −2a(a/2)1/3y; (a/2)2/3tx, (a/2)2/3ty

∼e−(a/2)2/3(tx+ty) ˜Isoft
1
(x, y; tx, ty) .
Similar formulas hold connecting Shard
1
, ˜Shard
1
and Dhard
1
to Ssoft
1
, ˜Ssoft
1
and Dsoft
1
respec-
tively, thus showing the formula (5.14) holds for β = 1 initial conditions. Repeating the
analysis for β = 4 initial conditions leads to the same conclusion.
5.3
Connection with the bulk
It is known [16] that after appropriate scaling of the variables, the static distributions at
the hard and soft edges tend to the bulk distributions at large distances from the edge of
the system. The required scaling is
X 7→α + 2π√α ρx ,
X 7→−

α + πρx/√α

,
(5.16)
27
with α →∞, for the hard and soft edges respectively. Here we will show that this feature
persists for the dynamical distributions.
Consider ﬁrst the hard edge with β = 2 initial conditions. Changing variables u 7→u2
and making use of the asymptotic expansion
Ja(x) ∼
x→∞
 2
πx
1/2
cos(x −πa/2 −π/4)
(5.17)
in the formulas (5.1) and (5.2), we see that
lim
α→∞2π√α ρ Shard
2

α + 2π√α ρx, α + 2π√α ρy; tx, ty

∼
ρ
Z 1
0 cos(πuρ(x −y)) e−u2(tx−ty) du ,
(5.18)
lim
α→∞2π√α ρ ˜Shard
2

α + 2π√α ρx, α + 2π√α ρy; tx, ty

=
−ρ
Z ∞
1
cos(πuρ(x −y)) e−u2(tx−ty) du .
(5.19)
Substituting these formulas in (5.5) and (5.6) and also making the change of scale t 7→
(πρ)2t/2 reclaims the known formula for the bulk dynamical distributions [19].
In fact the asymptotic behaviour (5.18) and (5.19) of Shard
β
and ˜Shard
β
for β = 2 initial
conditions persists for β = 1 and β = 4 initial conditions. This follows from application
of (5.27) in the exact results (3.31), (3.37) and (3.49), (3.50). It remains to consider ˜Iβ
and Dβ. For β = 1 initial conditions application of (5.17) in (3.33) and (3.38) shows
lim
α→∞2πρ ˜Ihard
1

α + 2π√α ρx, α + 2π√α ρy; tx, ty

=
ρ
Z ∞
1
du e−u2(tx+ty)
u
sin(πuρ(y −x)) ,
(5.20)
lim
α→∞2πρα Dhard
1

α + 2π√α ρx, α + 2π√α ρy; tx, ty

=
ρ
Z 1
0 du u eu2(tx+ty) sin(πuρ(y −x)) ,
(5.21)
while for β = 4 initial conditions application of (5.17) in (3.54) and (3.57) shows
lim
α→∞2πρα ˜Ihard
4

α + 2π√α ρx, α + 2π√α ρy; tx, ty

=
ρ
Z ∞
1
du u e−u2(tx+ty) sin(πuρ(y −x)) ,
(5.22)
lim
α→∞2πρ Dhard
4

α + 2π√α ρx, α + 2π√α ρy; tx, ty

=
ρ
Z 1
0 du eu2(tx+ty)
u
sin(πuρ(y −x)) .
(5.23)
After scaling t 7→(πρ)2t/2, the known formulas for ρ(1+1)(x, y; tx, ty) with β = 1 and
β = 4 initial conditions [20, 21] are reproduced by these results.
In the case of the soft edge connecting to the bulk, similar formulas are found to hold.
These formulas are derived from the asymptotic expansion
Ai(−x) ∼
x→∞
1
π1/2x1/4 cos(2x3/2/3 −π/4) .
(5.24)
28
Consider for example Ssoft
2
as speciﬁed by (5.7). We ﬁrst change variables v 7→α(1 −u)
for 0 < v < α, and replace the Airy functions in the integrand according to (5.24). Noting
that
2
3
n
(α + πρx/√α −v)3/2 −(α + πρy/√α −v)3/2o
∼πρu1/2(x −y) ,
we see that if we also scale t according to
t 7→t/α
(5.25)
then Ssoft
2
has the asymptotic form
lim
α→∞(−πρ/√α) Ssoft
2
(−(α + πρx/√α), −(α + πρy/√α); tx/α, ty/α)
∼
e−(tx−ty)ρ
Z 1
0 cos(πuρ(x −y)) e−u2(tx−ty) du .
(5.26)
Apart from the factor of e−(tx−ty) this is the same result as (5.18). A similar calculation
shows the asymptotic form of ˜Ssoft
2
is given by (5.19) except for an additional factor
of e−(tx−ty). This shows that this additional factor cancels from the formula (2.24) for
the distribution functions. The ﬁnal result is that the bulk dynamical distributions are
reclaimed from the soft edge results for each of the three distinct initial conditions. (As
in the hard edge case a ﬁnal rescaling t 7→(πρ)2t/2 is required).
5.4
Asymptotic form of ρT
(1+1)(X, Y ; t)
The dynamical density-density correlation function between an eigenvalue with value X
initially, and an eigenvalue with value Y and parameter τ is deﬁned in terms of the
distribution function (2.8) by
ρT
(1+1)(x, y; τ) = ρ(1+1)(x; 0; y; τ) −ρ(1)(x; 0) ρ(1)(y; τ) .
(5.27)
According to (2.24) and (2.26) we have that in the ﬁnite system
ρT
(1+1)(x, y; τ) = −

S(x, y; 0, τ) ˜S(y, x; τ, 0) −˜I(x, y; 0, τ) D(x, y; 0, τ)

.
(5.28)
For the Laguerre ensemble at the hard edge we deﬁne the corresponding scaled correlation
ρT hard
(1+1) by
ρT hard
(1+1) (X, Y ; t) = lim
N→∞
 1
4N
2
ρT
(1+1)
 X
4N , Y
4N ; t
2N

= −

Shard
β
(X, Y ; 0, t) ˜Shard
β
(Y, X; t, 0) −˜Ihard
β
(X, Y ; 0, t) Dhard
β
(X, Y ; 0, t)

,(5.29)
where β = 1, 2 or 4 depending on the initial conditions, while for the Gaussian ensemble
at the soft edge the scaled correlation ρT soft
(1+1) is deﬁned by
ρT soft
(1+1)(X, Y ; t)
=
lim
N→∞

1
21/2N1/6
2
ρT
(1+1)
√
2N +
X
21/2N1/6 ,
√
2N +
Y
21/2N1/6;
t
N1/3

=
−

Ssoft
β
(X, Y ; 0, t) ˜Ssoft
β
(Y, X; t, 0) −˜Isoft
β
(X, Y ; 0, t) Dsoft
β (X, Y ; 0, t)

.
(5.30)
29
The asymptotic form of ρhard
(1+1)(X, Y ; t) for large |X −Y | and t is of interest in applications
of the parameter dependent Laguerre ensemble to transport in mesoscopic systems [15].
To deduce this asymptotic form, a hydrodynamical approximation to the corresponding
Fokker-Planck equation was made which implied
Z ∞
0
Z ∞
