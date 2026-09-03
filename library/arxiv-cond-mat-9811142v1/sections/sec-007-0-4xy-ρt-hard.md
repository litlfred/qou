---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges"
section_id: sec-007-0-4xy-ρt-hard
section_title: "(4XY ) ρT hard"
section_number: 0
pages: 30-36
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
doc_brief: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges — For the orthogonal-unitary and symplectic-unitary transitions in random matrix the- ory, the"
---
(1+1)

X2, Y 2; t

cos(kX) cos(kY ) dX dY
∼
k→0
t→∞
|k|
2β e−2t|k|
(5.31)
(eq. (80) of [15] with πρδu2/γ = 2t). On the other hand we can easily check that
Re
 
1
(v + u + 2it)2 +
1
(v −u −2it)2
!
= −2
Z ∞
0
dk ke−2kt cos(kv) cos(ku) .
(5.32)
Taking the inverse transform of this result and comparing with (5.31) shows that the
latter formula is equivalent to
(4XY )ρT hard
(1+1)

X2, Y 2; t

∼
X,Y,t→∞−1
π2β Re
 
1
(X + Y + 2it)2 +
1
(X −Y + 2it)2
!
(5.33)
for the leading non-oscillatory behaviour.
The prediction (5.1) can readily be checked on the exact formula (5.29) with β = 1, 2
and 4 initial conditions. The simplest case is β = 2 initial conditions, when the product
˜Ihard
β
˜Dhard
β
in (5.29) vanishes. To analyze Shard
2
and ˜Shard
2
we make use of the asymptotic
expansion (5.17), and furthermore expand the integrands about their endpoint u = 1.
Integration by parts then gives
Shard
2

X2, Y 2; 0, t

∼
et
2π(XY )1/2 Re
 
ei(X−Y )
−i(X −Y ) −2t + ei((X+Y )−πα/2−π/2)
−i(X + Y ) −2t
!
,
(5.34)
˜Shard
2

Y 2, X2; t, 0

∼
e−t
2π(XY )1/2 Re
 
ei(X−Y )
i(X −Y ) −2t + ei((X+Y )−πα/2−π/2)
i(X + Y ) −2t
!
,
(5.35)
and these formulas when substituted in (5.29) imply the result (5.33 ) with β = 2. In the
case of β = 1 and β = 4 initial conditions, similar analysis shows
˜Ihard
β

X2, Y 2; 0, t

Dhard
β

X2, Y 2; 0, t

∼
χβ ˜Shard
β
(X, Y ; 0, t) ˜Shard
β
(Y, X; t, 0)
∼
χβ
1
4XY
1
2π2Re
 
1
(X + Y + 2it)2 +
1
(X −Y + 2it)2
!
,
(5.36)
where χβ = −1 for β = 1 and χβ = 1/2 for β = 4, and the asymptotics refer to the
leading non-oscillatory term. Thus (5.33) again remains valid.
Let us now turn our attention to the same asymptotic limit for the soft edge. There
it is known that the asymptotic form (5.33) for X, Y →∞is valid in the static theory
(t = 0) [22]. It turns out that the exact results for (5.30) satisfy (5.33) for X, Y →∞
30
and t →∞, as just demonstrated for the hard edge correlations. Thus, for β = 2 initial
conditions, use of the asymptotic expansion (5.24) in (5.7) and (5.8) shows
Ssoft
2

−X2, −Y 2; 0, t

∼
1
2π(XY )1/2 Re
 e2i(X3+Y 3)/3−iv(X+Y )−πi/2
i(X + Y ) + t
+ e2i(X3−Y 3)/3−iv(X−Y )
i(X −Y ) + t
!
,
˜Ssoft
2

−Y 2, −X2; t, 0

∼
1
2π(XY )1/2 Re
 e2i(X3+Y 3)/3−iv(X+Y )−πi/2
i(X + Y ) −t
+ e2i(X3−Y 3)/3−iv(X−Y )
i(X −Y ) −t
!
,
and these formulas when substituted in (5.30) (with ˜Isoft
2
Dsoft
2
= 0) gives the asymptotic
form (5.33) (although t therein must be rescaled by replacing 2t with t).
The same
conclusion is reached for β = 1 and 4 initial conditions, where we ﬁnd the analogue of the
formula (5.36).
As pointed out in [15], a consequence of the asymptotic form (5.33) is a universal
formula for the time displaced covariance of two linear statistics
At =
N
X
j=1
a

x2
j(t)

,
Bt =
N
X
j=1
b

x2
j(t)

.
Thus, if in the general formula
Cov(A0, Bt) =
Z ∞
0
dx a(x2)
Z ∞
0
dy b(y2)(4xy)ρT
(1+1)(x2, y2; t)
we suppose a(x2) and b(x2) are made slowly varying by writing
a(x2) 7→a((x/α)2) ,
b(x2) 7→b((x/α)2) ,
where α ≫1, and if we scale t according to
t 7→α t ,
then a simple change of variables and use of (5.33) shows that for α →∞
Cov(A0, Bt)
∼
−1
π2β
Z ∞
0
dx a(x2)
Z ∞
0
dy b(y2)Re
 
1
(X + Y + 2it)2 +
1
(X −Y + 2it)2
!
=
2
π2β
Z ∞
0
dk k ˜a(k)˜b(k) e−2kt ,
(5.37)
where the equality follows from (5.32), and
˜a(k) :=
Z ∞
0
a(x2) cos(kx) dx
and similarly the meaning of ˜b(k).
31
5.5
Empirical density of eigenvalues at the soft edge
The dynamical distribution functions at the soft edge calculated in Section 4 can be real-
ized by parameter dependent random matrices of the type (1.3). Thus we can numerically
construct random matrices and empirically compute eigenvalue distributions for compar-
ison against the theoretical prediction. The simplest distribution to compute empirically
is the density (one-point function). Here we will undertake such a calculation for the
orthogonal to unitary transition at the soft edge.
As deduced from (2.24), (2.26) and (3.31) the theoretical prediction for the scaled
density at the soft edge of the orthogonal to unitary transition is
ρsoft
(1) (X; t)
=
Ssoft
1
(X, X; t, t)
=
Z ∞
0

Ai(X + v)
2 dv + 1
2
Z ∞
0
e−stXAi(X −s) ds.
(5.38)
The theory of Section 1 tells us that the parameter dependent random matrices (1.3), for
an appropriate X(0) have, in the inﬁnite dimension limit, a scaled density at the soft edge
given by (5.38). Since we are considering the orthogonal to unitary transition, X(0) must
be chosen as a real symmetric matrix with joint p.d.f. for the elements
P(X(0)) =
N
Y
j=1
 1
2π
1/2e−X(0) 2
jj
/2 Y
j<k
1
π1/2e−X(0) 2
jk .
The joint distribution of the elements of X, P(X; τ) say, is obtained by integrating over
X(0)
jj and X(0)
jk . Thus
P(X; τ)
=
N
Y
j=1
Z ∞
−∞dX(0)
jj
Y
j<k
Z ∞
−∞dX(0)
jk P(X(0))P(X(0); X; τ)
=
N
Y
j=1
e−X2
jj/(1 + e−2τ)
q
π(1 + e−2τ)
Y
j<k
2
π
√
1 −e−4τ e−2(ReXjk)2/(1+e−2τ )e−2(ImXjk)2/(1−e−2τ ),
(5.39)
which tells us that the diagonal and the real and imaginary parts of the upper triangular
elements are all independent, having Gaussian distributions with mean zero and variances
2/(1 + e−2τ), 4/(1 + e−2τ) and 4/(1 −e−2τ) respectively. Hence, for a given value of N
and τ such matrices are simple to generate numerically. For each such random matrix the
eigenvalues λj are computed and scaled according to λ 7→(λj −(2N)1/2)21/2N1/6. For N
large enough and with τ related to t by (4.9) the corresponding empirical density should
approach (5.38). The situation for a relative small value of N (recall the occurence of
N1/6) is illustrated in Figure 1, where good agreement with the inﬁnite dimension limit
is observed.
Also of interest is the possibility of providing a realization of the hard edge results.
Unfortunately here it seems that the initial conditions used do not precisely correspond to
a situation in which X in (1.6) can be generated from a formula analogous to (5.39). The
problem is that if X(0) is a real n × m matrix with independent Gaussian entries, then
the square of the eigenvalues of X(0)†X(0) has p.d.f. (1.2) with a = n −m −1. However in
32
-4
-3
-2
-1
1
x
0.1
0.2
0.3
0.4
0.5
0.6
density
Figure 1: Empirical histogram of the scaled soft edge density for 500 parameter dependent
random matrices of the form (5.39) with τ = .05 and N = 100, compared against the
inﬁnite dimension form (5.38).
deducing (1.4) from (1.6) in the case of transitions to unitary symmetry (β = 2) we must
take a = n −m, which is thus incompatible with the sought initial condition.
5.6
Distribution functions in the initial state
With m = 0 and τ1 →0 the dynamical distribution (1.8) reduces to the n-point distribu-
tion function in the initial state. At β = 1 the formulas (2.24), (2.30), (2.31) and (2.33)
reclaim the well known [12, 10, 6, 23] general formula
ρ(n)(x1, . . . , xn) = Tdet


S1(xj, xk)
1
2
R sgn(xk −y)S1(xj, y) dy −1
2sgn(xk −xj)
∂
∂xj S1(xj, xk)
S1(xk, xj)

,
(5.40)
where S1(xj, xk) := S(xj, xk; 0, 0) as speciﬁed by (2.20) with {Rj} corresponding to the
β = 1 initial condition. We remark that the integral in (5.40) can be rewritten according
to
1
2
Z
sgn(xk −y)S1(xj, y) dy = −
Z xk
xj
S1(xj, y) dy.
At β = 4 these same formulas (with (2.33) replaced by (2.34)) give that
ρ(n)(x1, . . . , xn) = Tdet


S4(xj, xk)
∂
∂xk S1(xk, xj)
−
R xj
xk S4(y, xk) dy
S4(xk, xj)

,
(5.41)
where S4(x, y) := S(x, y; 0, 0) as speciﬁed by (2.20) with {Rj} therein corresponding to
the β = 4 initial condition, again in accordance with the known result. In deriving (5.41)
from (2.24) we assumed that none of the points x1, . . . , xn are coincident; this is necessary
because of the delta functions in (2.7) with β = 4.
We can take the limit tX, tY →0 in the formulas obtained for Sedge
1
(X, Y ; tX, tY )
(here edge denotes hard or soft) obtained in Section 3 and 4 to obtain the explicit form
33
of Sedge
1
(X, Y ) in the scaled limit at the hard and soft edges. Thus from (3.31), (3.49),
(4.22) and (4.40) we ﬁnd
Shard
1
(X, Y )
=
Khard(X, Y ) −Ja+1(
√
Y )
4
√
Y
 Z √
X
0
Ja+1(u) du −1

(5.42)
Shard
4
(X, Y )
=
Khard(X, Y ) −
1
4X1/2Ja−1(X1/2)
Z Y 1/2
0
Ja+1(s) ds
(5.43)
Ssoft
1
(X, Y )
=
Ksoft(X, Y ) + 1
2Ai(Y )

1 −
Z ∞
X Ai(t) dt

(5.44)
Ssoft
4
(X, Y )
=
Ksoft(X, Y ) −1
2Ai(X)
Z ∞
Y
Ai(s) ds
(5.45)
where
Khard(X, Y )
:=
X1/2Ja+1(X1/2)Ja(Y 1/2) −Y 1/2Ja+1(Y 1/2)Ja(X1/2)
2(X −Y )
Ksoft(X, Y )
:=
Ai(X)Ai′(Y ) −Ai(Y )Ai′(X)
X −Y
.
(5.46)
In obtaining these formulas we have used (5.2) and (5.7) together with the known facts
that [16]
Shard
2
(X, Y ) = Khard(X, Y ),
Ssoft
2
(X, Y ) = Ksoft(X, Y )
to rewrite the ﬁrst of the integrals in the expressions (3.31), (3.49), (4.22) and (4.40).
Also, Bessel function identities have been used in obtaining the second term in (5.42) and
(5.43), while in the second term of (5.44) use has been made of the deﬁnite integral
Z ∞
−∞Ai(x) dx = 1.
We remark that in previous studies [6, 24] expression have been obtained for (5.42) and
(5.43) which are of a more complicated structure. Also the expressions obtained in [16]
for (5.44) and (5.45) are now seen to be in error.
Some caution must be exercised in applying these results at β = 4. In particular,
the one body weight function used in (2.7) at β = 4 is that corresponding to β = 2 in
(1.1) and (1.2). To obtain from the above results expressions corresponding to the weight
functions as written in (1.1) and (1.2) we must make the replacements
Shard
4
(X, Y ) 7→2Shard
4
(4X, 4Y )

a→2a,
Ssoft
4
(X, Y ) 7→
1
21/3Ssoft
4
(22/3X, 22/3Y ).
Acknowledgement
The ﬁnancial support of the ARC is acknowledged.
Appendix A
In the case τx = τy = 0, the formula (3.9) for S2 at β = 1 reads
S2(x, y; 0, 0) =
q
w(y)
ΦN−2(x; 0)
rN/2−1(0) −
q
w(x)CN−1(x)
hN−1

CN−1(y)−(N−1)RN−2(y)

. (A.1)
34
Use of the explicit formulas (3.1) and (3.2) gives
CN−1(y) −(N −1)RN−2(y) = −(N −1)!

La
N−1(y) −d
dyLa
N−1(y)

= (N −1)! d
dyLa
N(y),
(A.2)
where the second equality follows from an appropriate Laguerre polynomial identity [13].
For the x-dependent factor in (A.1), we require an explicit formula for ΦN−2(x; 0).
Now (2.31) substituted in (2.16) gives
Φk(x; 0) =
Z
sgn(x −y)
q
w(y)Rk(y).
Making use of the explicit formulas (3.2) and (3.3) then gives
ΦN−2(x; 0)
rN/2−1(0) = −
1
4Γ(a + N)
Z ∞
0
sgn(x −y)ya/2e−y/2 d
dyLa
N−1(y) dy.
Integrating by parts, and making use of the Laguerre polynomial identity
(y −a)La
N−1(y) = y d
dyLa
N−1(y) −N

La
N(y) −La
N−1(y)

,
we see from this that
ΦN−2(x; 0)
rN/2−1(0) =
q
w(x)CN−1(x)
hN−1
+
N
4Γ(a + N)
Z ∞
0
sgn(x −y)ya/2−1e−y/2
La
N(y) −La
N−1(y)

dy.
(A.3)
Substituting (A.2) and (A.3) in (A.1) shows
S2(x, y; 0, 0) =
N!
4Γ(N + a)
q
w(y)
×
 d
dyLa
N(y)
 Z ∞
0
sgn(x −y)ya/2−1e−y/2
La
N(y) −La
N−1(y)

dy,
(A.4)
which is the formula recently given by Widom [8].
Consider next the expression (3.42) for S2 at β = 4 with τx = τy = 0. To simplify this
expression, we note that the formula in (3.39) for R2j(x) can be written in the simpliﬁed
form
R2j(x) =
1
a + 2j + 1

C2j+1(x) + 1
2(2j + 1)!x−a/2ex/2
Z x
0 ta/2e−t/2 d
dtL2j+2(t)

dt

.(A.5)
This formula can be checked by multiplying both sides by xa/2e−x/2 and diﬀerentiating.
(We also verify that the x →∞behaviour of both sides agrees.) Now, according to the
deﬁnition (2.16) of Φk and the second formula in (2.32)
ΦN−2(x; 0)
rN/2−1(0) = −
2
rN/2−1(0)
d
dx

xa/2e−x/2RN−2(x)

35
Substituting (A.5), and making use of the diﬀerentiation formulas
y d
dyLa
n(y) = nLa
n(y) −(n + a)La
n−1(y) = (n + 1)La
n+1(y) −(n + a + 1 −y)La
n(y)
and the fact that
(a + N −1)rN/2+1(0) = hN−1 = Γ(N)Γ(N + a)
we readily ﬁnd
ΦN−2(x; 0)
rN/2−1(0) −
q
w(x)CN−1(x)
hN−1
= −
q
w(x)
N
Γ(N + a)
(La
N(x) −La
N−1(x))
x
(A.6)
which thus simpliﬁes the x-dependent factor in (3.42). For the y-dependent factor, we see
from (A.5) that
q
w(y)

CN−1(y) −(a + N −1)RN−2(y)

= −1
2(N −1)!
Z y
0 ta/2e−t/2 d
dtLa
N(t) dt. (A.7)
Multiplying (A.6) and (A.7) shows
S2(x, y; 0, 0) =
N!
q
w(x)
2Γ(N + a)
La
N(x) −La
N−1(x)
x
Z y
0 ta/2e−t/2 d
dtLa
N(t) dt,
(A.8)
in agreement with the formula given recently by Widom [8].
