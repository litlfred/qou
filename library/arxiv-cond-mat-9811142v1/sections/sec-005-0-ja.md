---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges"
section_id: sec-005-0-ja
section_title: "Ja("
section_number: 0
pages: 11-25
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
doc_brief: "Correlations for the orthogonal-unitary and symplectic-unitary transitions at the hard and soft edges — For the orthogonal-unitary and symplectic-unitary transitions in random matrix the- ory, the"
---
q
w(x)
ν!
(ν + a/2)!

La
2ν(x)e−γ2ντ −La
2ν+1(x)e−γ2ν+1τ

 x=X/4N
τ=t/2N
∼
−ν−a/2e−(2ν/N)t
s
X
4N (2ν)(a−1)/2Ja−1

s
2jX
N

+ t
N (2ν)a/2Ja

s
2jX
N

=
−2a/2
N u−a/2 d
du

e−utua/2Ja
√
uX

,
u := 2ν/N .
(3.22)
(The equality is obtained by making use of a suitable diﬀerentiation formula for the Bessel
function).
Substituting (3.22) in (3.18) gives the leading order behaviour of the sum over ν as a
Riemann integral. Furthermore, use of (3.21) gives
q
w(x)
La
2k−1(x)
(2k −1 + a)! e−γ2k−1τ

 x=X/4N
τ=t/2N
∼
N−a/2
(2k −1)! s−a/2Ja
√
sX

e−st,
(3.23)
11
s := 2k/N, so in total we have
Φ2k−2
 X
4N ; t
2N

eγ2k−2t/2N
∼
rk−1(0) N−a/2
(2k −1)!
1
2

1 −2s−a/2
Ja
√
sX

e−st
−a
4
Z ∞
s
e−ut
u Ja
√
uX

du

.
(3.24)
The expansions (3.23) and (3.24) with 2k = N and thus s = 1 suﬃce to specify the
x-dependent factor in (3.9). Thus we have
 ΦN−2(x; τx)
rN/2−1(0)
−
q
w(x) CN−1(x)e−γN−1τx
hN−1
!

x=X/4N
τx=tX/2N
∼
N−a/2
2(N −1)!
 
Ja
√
X

e−tX −a
2
Z ∞
1
e−utX
u
Ja
√
uX

du
!
.
(3.25)
Next we will compute the asymptotic form of R2j(y; τy). In the case 2j = N −2 this
is required for the y-dependent factor in (3.9). From (2.14), (3.2) and (3.1) we see that
R2j(y; τ) eγ2jτ = (2j)!
2j
X
l=0
La
l (y) eγlτ .
(3.26)
The asymptotic form of this expression is deduced by using (3.21) to approximate the
summand, which leads to the result
q
w(y)R2j(y; τy)eγ2jτy

y=Y/4N
τy=tY /2N
∼(2j)! N1+a/2
Z s
0 va/2Ja
√
vY

evtY dv ,
(3.27)
where here s = 2j/N. Setting s = 1 and making further use of (3.23) we see that
q
w(y) (CN−1(y)eγN−1τy −(N −1)RN−2(y; τy)eγN−2τy)
∼−(N −1)!N1+a/2
Z 1
0 va/2Ja
√
vY

evtY dv .
(3.28)
Combining (3.25) and (3.28) in the formula (3.9) for S2 gives
S2
 X
4N , Y
4N ; tX
2N , tY
2N

∼
N
2
 
−e−tXJa
√
X

+ a
2
Z ∞
1
e−utX
u
Ja
√
uX

du
!
×
Z 1
0 va/2Ja
√
vY

evtY dv

.
(3.29)
The asymptotics of S1 can be determined by using (3.21) and Stirling’s formula to
approximate the integrand. This gives
S1
 X
4N , Y
4N ; tX
2N , tY
2N

∼N
Z 1
0 Ja
√
uX

Ja
√
uY

e−u(tX−tY ) du .
(3.30)
Since S is deﬁned as the sum of S1 and S2, its asymptotic form is given by the sum of
(3.29) and (3.30). Substituting into (3.12) gives
Shard
1
(X, Y ; tX, tY ) = 1
4
Z 1
0 Ja(
√
uX)Ja(
√
uY )e−u(tX−tY ) du
+1
8

−e−tXJa(
√
X) + a
2
Z ∞
1
e−utX
u
Ja(
√
uX) du
 Z 1
0 dv Ja(
√
vY )etY vva/2. (3.31)
12
Asymptotics of ˜I(x, y; τx, τy)
So as to induce a cancellation at leading order, we ﬁrst perform some minor manipulation
to the deﬁnition (2.21), by way of subtracting and adding (2l+1)eγ2l(τx+τy)Φ2l(x; τx)Φ2l(y; τy)
to the summand, so that it reads
˜I(x, y; τx, τy)
=
∞
X
l=N/2
1
rl(0) {eγ2lτxΦ2l(x; τx) (eγ2l+1τyΦ2l+1(y; τy)
−(2l + 1)eγ2lτyΦ2l(y; τy)) −(x ↔y)} .
(3.32)
The asymptotics of eγ2lτxΦ2l(x; τx) can be read oﬀfrom (3.24). For the y-dependent factor
of the ﬁrst term of the summand we note from the deﬁnitions (2.18) and the explicit
formulas (3.1) and (3.5) that
eγ2l+1τΦ2l+1(y; τ) −(2l + 1)eγ2lτΦ2l(y; τ)
=
q
w(y) rl(0)
 
(2l + 1)La
2l+1(y)e−γ2l+1τ
(2l + 1 + a)!
−La
2l(y)e−γ2lτ
(2l + a)!
!
.
Thus, using (3.3) and the asymptotic formula (3.21) we have

eγ2l+1τΦ2l+1(y; τ) −(2l + 1)eγ2lτΦ2l(y; τ)


 y=Y/4N
τ=t/2N
∼4(2l + 1)!N−1+a/2
( d
ds

e−stJa
√
sY

−as−1+a/2Ja
√
sY

e−st
)
,
s = 2l/N .
Substituting this result, together with (3.24) (after replacing k by l + 1) in (3.32) shows
that
˜Ihard
1
(X, Y ; tX, tY ) =
Z ∞
1
ds
(
1 −
2
sa/2

Ja
√
sX

e−stX −a
4
Z ∞
s
e−utX
u
Ja
√
uX

du
)
×
( d
ds

e−styJa
√
sY

−as−1+a/2Ja
√
sY

e−stY
)
−(X ↔Y ) .
(3.33)
Asymptotics of g(x, y; τ)
According to (2.3) and (2.5)
g(x, y; τ) = (xy)a/2e−(x+y)/2
∞
X
j=0
j!
(j + a)!La
j(x)La
j(y)e−2(j+(a+1)/2)τ .
(3.34)
This summation can be evaluated in closed form [11], giving
g(x, y; τ) = e−(x+y)/2e−(2a+1)τ 
1 −e−2τ−1 exp
 
−
e−2τ
1 −e−2τ (x + y)
!
Ia
 
2
√xy e−τ
1 −e−2τ
!
,
where Ia denotes the Bessel function of pure imaginary argument. Consequently
g
 X
4N , Y
4N ; tX −tY
2N

∼
N
tX −tY
exp

−X + Y
tX −tY

Ia
 
√
XY
2(tX −tY )
!
.
(3.35)
13
Alternatively, proceeding as in the derivation of (3.30) we can deduce from (3.34) that
g
 X
4N , Y
4N ; tX −tY
2N

∼N
Z ∞
0
Ja(
√
uX)Ja(
√
uY )e−u(tX−tY ) du.
(3.36)
The immediate merit of this representation is that when substituted in (2.23), partial
cancellation occurs with (3.30). Adding the result to (3.29) and substituting in (3.13)
gives
˜Shard
1
(X, Y ; tX, tY ) = −1
4
Z ∞
1
Ja(
√
uX)Ja(
√
uY )e−u(tX−tY ) du
+1
8

−e−tXJa(
√
X) + a
2
Z ∞
1
e−utX
u
Ja(
√
uX) du

+
Z 1
0 dv Ja(
√
vY )etY vva/2.(3.37)
Asymptotics of D(x, y; τx, τy)
According to (2.22) D is deﬁned in terms of {Rj(x; τ)}. Now R2j(y; τ) is speciﬁed by
(3.26). Deriving the analogous formula for R2j+1(x; τ), which follows from (3.2), (2.14)
and (3.1), we see that
R2j+1(x; τ)eγ2j+1τ
=
−(2j + 1)!La
2j+1(x)eγ2j+1τ −(2j)!(2j + a + 1)La
2j(x)eγ2jτ
+(2j + a + 1)R2j(x; τ)eγ2jτ .
Hence
(eγ2j+1τxR2j+1(x; τx)eγ2jτyR2j(y; τy) −(x ↔y)) =

−(2j + 1)!La
2j+1(x)eγ2j+1τx −(2j)!(2j + a + 1)La
2j(x)eγ2jτx
R2j(y; τy)eγ2jτy −(x ↔y) .
Now the asymptotic form of R2j(y; τy) is speciﬁed by (3.27) while we see from (3.21) that
q
w(x)

−(2j + 1)!La
2j+1(x)eγ2j+1τx −(2j)!(2j + a + 1)La
2j(x)eγ2jτx 

x=X/4N
τx=tX/2N
∼−2(2j + 1)!estX(Ns)a/2Ja
√
sX

,
s = 2j/N .
Making use also of the explicit form (3.3) of rn(0) and using the deﬁnition (3.15) we thus
ﬁnd
Dhard
1
(X, Y ; tX, tY ) = −4−3
×
Z 1
0 ds estXs−a/2Ja
√
sX
 Z s
0 dv evtY va/2Ja
√
vY

−(X ↔Y )

.
(3.38)
3.2
β = 4 initial conditions
The method of evaluation of the quantities S, ˜I, and D for the Laguerre ensemble in the
case of initial conditions with symplectic symmetry (β = 4) closely parallels that just
given for β = 1 initial conditions. First, we note from previous work [5] that the monic
14
skew orthogonal polynomials at τ = 0 have the explicit form
R2j(x)
=
22jj! (j + (a −1)/2)!
j
X
l=0
(2l)!
l! 22l
1
(l + (a −1)/2)!La−1
2l (x)
=
22jj! (j + (a −1)/2)!
j
X
l=0
1
l! 22l (l + (a −1)/2)! (C2l(x) + 2lC2l−1(x)) ,
R2j+1(x)
=
−(2j + 1)! La−1
2j+1(x)
=
C2j+1(x) + (2j + 1)C2j(x) ,
(3.39)
with corresponding normalization
rn(0) = Γ(2n + 2) Γ(a + 2n + 1) .
(3.40)
The inversion of these equations gives that the quantities βn j in (2.17) have the explicit
values
β2m 2m
=
β2m+1 2m+1 = 1 ,
β2m+1 2m = −(2m + 1) ,
βν 2j+1
=
(−1)ν+1
ν!
(2j + 1)! ,
βν 2j = a βν 2j+1 ,
(3.41)
for ν > 2j + 1. Thus the factorization formula (3.7) again holds, which when substituted
in (2.29) and after making use of the explicit value of βN−1 N−2 and βp N−1, and (2.17),
implies
S2(x, y; τx, τy)
=
q
w(x)w(y)
∞
X
p=N
Cp(x)
hp
e−γpτx βp N−1 {CN−1(y)eγN−1τy
+(a + N −1)RN−2(y; τy)eγN−2τy} .
The sum over p is, after minor manipulation, formally identical to the sum over p in (3.8),
so it can be summed using (2.18). Thus S2 has the explicit form
S2(x, y; τx, τy)
=
q
w(y)
 ΦN−2(x; τx)
rN/2−1(0) eγN−2τx −
q
w(x)CN−1(x)
hN−1
e−γN−1τx
!
× (CN−1(y)eγN−1τy + (a + N −1)RN−2(y; τy)eγN−2τy) .
(3.42)
As with (3.9), in the limit τx, τy →0 this reduces down to the form of S2 derived by Widom
[8] in the static β = 4 theory. The details of the veriﬁcation are given in Appendix A.
3.2.1
The thermodynamic limit
Although the scaled distribution function is still given by (3.11), the required scaling
of the elements of the quaternion determinant (2.24) diﬀers slightly from the formulas
(3.12)–(3.15) appropriate with β = 1 initial conditions. In particular (3.14) and (3.15)
should now read
˜Ihard
4
(X, Y ; tX, tY )
:=
lim
N→∞
 1
4N
2 ˜I
 X
4N , Y
4N ; tX
2N , tY
2N

(3.43)
Dhard
4
(X, Y ; tX, tY )
:=
lim
N→∞D
 X
4N , Y
4N ; tX
2N , tY
2N

(3.44)
while (3.12) and (3.13) remain the same, except that the subscripts 1 on the right hand
sides should be replaced by 4.
15
Asymptotics of S(x, y; τx, τy)
From the expansion (2.18) and the explicit formulas (3.1) and (3.41) we have
Φ2k−2(x; τ)eγ2k−2τ = −
rk−1(0)
q
w(x)
(2k −1)!
∞
X
ν=2k−1
La
ν(x) ν!
(ν + a)! e−γντ .
Applying the asymptotic expansion (3.21) and Stirling’s formula shows that
Φ2k−2
 X
4N ; t
2N

eγ2k−2t/2N ∼−rk−1(0)
(2k −1)!N1−a/2
Z ∞
u
dr r−a/2e−rtJa
√
rX

,
(3.45)
where u := 2k/N. Setting u = 1 gives the asymptotic form of ΦN−2(x; τx)/rN/2−1(0) as
required in (3.42), and comparison with (3.23) shows that this term dominates the one
involving CN−1(x). Thus here the formula (3.25) applies with the right hand side replaced
by
−N1−a/2
(N −1)!
Z ∞
u
dr r−a/2e−rtJa
√
rX

.
(3.46)
For the y-dependent factor in (3.42), we note from (2.14), (3.1), and (3.26) that
R2j(y; τ)eγ2jτ =
22jj! (j + (a −1)/2)!
j
X
l=0
(2l)!
l! 22l
1
(l + (a −1)/2)!

La
2l(y)eγ2lτ −La
2l−1(y)eγ2l−1τ
.
Use of (3.21) and Stirling’s formula gives for the corresponding asymptotic form
1
(2j + 1)!
q
w(y)R2j(y; τ)eγ2jτ

 y=Y/4N
τ=t/2N
∼
Na/2−1
2
s−1+a/2
Z s
0 u−a/2 d
du

eutua/2Ja
√
uY

du ,
s := 2j/N .
(3.47)
Adding this with s = 1 to the asymptotic form of
q
w(y)CN−1(y)eγN−1τy/(N −1)! deduced
from (3.23), and multiplying the result by (3.46) gives that
S2
 X
4N , Y
4N ; tX
2N , tY
2N

∼−N
Z ∞
1
dr r−a/2e−rtXJa
√
rX

×
 
−Ja
√
Y

etY + 1
2
Z 1
0 u−a/2 d
du

eutY ua/2Ja
√
uY

du
!
.
(3.48)
The asymptotic form of S1 can be read oﬀfrom (3.30) since according to its deﬁnition
(2.28), its value is the same for β = 1 and 4. The asymptotic form of S itself is thus given
by the sum of (3.30) and (3.48). Thus we have
Shard
4
(X, Y ; tX, tY ) =
1
4
Z 1
0 Ja(
√
uX)Ja(
√
uY )e−u(tX−tY ) du −1
4
Z ∞
1
dr r−a/2e−rtXJa(
√
rX)
×

−Ja(
√
Y )etY + 1
2
Z 1
0 u−a/2 d
du

eutY ua/2Ja(
√
uY )

du

(3.49)
16
Asymptotics of ˜S(x, y; τx, τy)
The single particle Green function g as speciﬁed by (2.3) is independent of the initial
condition, so me can use the formula (3.36). Dividing by 4N and subtracting from (3.49)
shows
˜Shard
4
(X, Y ; tX, tY )
= −1
4
Z ∞
1
Ja(
√
uX)Ja(
√
uY )e−u(tX−tY ) du −1
4
Z ∞
1
dr r−a/2e−rtXJa(
√
rX)
×

−Ja(
√
Y )etY + 1
2
Z 1
0 u−a/2 d
du

eutY ua/2Ja(
√
uY )

du

(3.50)
Asymptotics of ˜I(x, y; τx, τy)
The deﬁnition (2.21) gives that ˜I is deﬁned in terms of {Φl(x; τ)}. The asymptotic form of
Φ2k−2(x; τ) is given by (3.45). Instead of deriving an analogous expression for Φ2k−1(y; τ),
we note from (2.18), (3.41), (3.1) and the formula (3.45) for Φ2k−2 that
Φ2k−1(y; τ)eγ2k−1τ =
−
q
w(y) rk−1(0)
(2k −2 + a)!

La
2k−2(y)e−γ2k−2τ + La
2k−1(y)e−γ2k−1τ
−aΦ2k−2(y; τ) . (3.51)
Thus
eγ2lτxΦ2l(x; τx)eγ2l+1τyΦ2l+1(y; τy) −(x ↔y) =
eγ2lτxΦ2l(x; τx)

−
q
w(y) rl(0)
(2l + a)!



La
2l(y)e−γ2lτy + La
2l+1(y)e−γ2l+1τy
−(x ↔y).
(3.52)
According to (3.21) and (3.40), the product of the second and third factors in the ﬁrst
term have the same leading asymptotic behaviour
−(2l + 1)! 4(vN)a/2Ja
√
vY

e−vτ ,
v = 2l/N .
(3.53)
Multiplying this by (3.45) (with k 7→l + 1) and substituting in (2.21) gives that the
desired asymptotic form is
Ihard
4
(X, Y ; tX, tY )
= 1
4
Z ∞
1
Z ∞
v
dr r−a/2e−rtXJa
√
rX

va/2Ja
√
vY

e−vtY dv −(X ↔Y ).(3.54)
Asymptotics of D(x, y; τx, τy)
Here we require the asymptotic form of {Rl(x; τ)}. For l even this is given by (3.47). On
the other hand, for l odd we see from (2.14), (3.1) and (3.39) that
R2j+1(y; τ)eγ2j+1τ = −(2j + 1)!

La
2j+1(y)eγ2j+1τ −La
2j(y)eγ2jτ
.
(3.55)
17
Use of (3.21) shows
q
w(y) R2j+1(y; τ)eγ2j+1τ

 y=Y/4N
τ=t/2N
∼−(2j + 1)!Na/2−1 d
ds

estsa/2Ja
√
sY

,
(3.56)
s := 2j/N. Multiplying this by (2j+1)! times (3.47) (with Y replaced by X) and dividing
by (3.40) we thus have
Dhard
4
(X, Y ; tX, tY )
∼
−1
4
Z 1
0 ds s−a/2
(Z s
0 u−a/2 d
du

eutXua/2Ja
√
uX

du
)
× d
ds

estY sa/2Ja
√
sY

−(X ↔Y ) .
(3.57)
4
Gaussian ensemble
For the Gaussian ensemble, we see from (2.4) that the corresponding monic orthogonal
polynomials and normalization are
Cn(x) = 2−n Hn(y),
hn = 2−n π1/4 n! .
(4.1)
The skew orthogonal polynomials for both β = 1 and β = 4 initial conditions at τ = 0 are
known in terms of the Cn(x) (see e.g. [12]). Using these expansions, the general formula
(2.14) then gives
R2m(x; τ)eγ2mτ
=
C2m(x)eγ2mτ
(4.2)
R2m+1(x; τ)eγ2m+1τ
=
C2m+1(x)eγ2m+1τ −mC2m−1(x)eγ2m−1τ
(4.3)
rm(0)
=
2−2m+1√πΓ(2m + 1)
(4.4)
for β = 1 initial conditions, and
R2m(x; τ)eγ2mτ
=
m!
m
X
l=0
eγ2lτ C2l(x)
l!
R2m+1(x; τ)eγ2m+1τ
=
C2m+1(x)eγ2m+1τ
(4.5)
rm(0)
=
2−2m√πΓ(2m + 2)
(4.6)
for β = 4 initial conditions. Inverting these formulas for {Rj(x)} in terms of {Cl(x)}
according to (2.17) gives
β2m j = δ2m,j,
β2m+1 j =
(
m!/l!,
j = 2l + 1, l = 0, 1, . . . , m
0,
j = 2l, l = 0, 1, . . . , m
(4.7)
for β = 1, while for β = 4 we ﬁnd
β2m j =





1,
j = 2m
−m,
j = 2m −2
0,
otherwise
β2m+1 j = δ2m+1,j.
(4.8)
Here we will use these explicit values in the general formulas of Section 2 to compute
the matrix elements in (2.24). In particular, we will give their asymptotic form in the
18
neighbourhood of the soft edge, which is speciﬁed by introducing the scaled variables X
and t according to
x =
√
2N +
X
21/2N1/6 ,
τ =
t
N1/3 .
(4.9)
The corresponding scaled distribution function (2.8), to be denoted ρsoft
(n+m), is given by
ρsoft
(n+m)(X(1)
1 , . . . , X(1)
n ; t(1); X(2)
1 , . . . , X(2)
m ; t(2))
= lim
N→∞

1
21/2N1/6
n+mρ(n+m)
√
2N +
X(1)
1
21/2N1/6 , . . . ,
√
2N +
X(1)
n
21/2N1/6; t(1)
N1/3 ;
√
2N +
X(2)
1
21/2N1/6, . . . ,
√
2N +
X(2)
m
21/2N1/6; t(2)
N1/3

(4.10)
Analogous to (3.12)–(3.15), the matrix elements of ρsoft
(n+m) are computed from the formulas
Ssoft
1
(X, Y ; tX, tY )
= lim
N→∞
e−N2/3(tY −tX)
21/2N1/6
S
√
2N +
X
21/2N1/6,
√
2N +
Y
21/2N1/6 ; tX
N1/3 , tY
N1/3

(4.11)
˜Ssoft
1
(X, Y ; tX, tY )
= lim
N→∞
e−N2/3(tY −tX)
21/2N1/6
˜S
√
2N +
X
21/2N1/6,
√
2N +
Y
21/2N1/6 ; tX
N1/3 , tY
N1/3

(4.12)
˜Isoft
1
(X, Y ; tX, tY )
= lim
N→∞eN2/3(tY +tX) ˜I
√
2N +
X
21/2N1/6 ,
√
2N +
Y
21/2N1/6 ; tX
N1/3, tY
N1/3

(4.13)
Dsoft
1
(X, Y ; tX, tY )
= lim
N→∞
e−N2/3(tY +tX)
2N1/3
D
√
2N +
X
21/2N1/6 ,
√
2N +
Y
21/2N1/6; tX
N1/3, tY
N1/3

.(4.14)
Here the scale factors in addition to 1/21/2N1/6 do not eﬀect the value of (2.24) because
they result from a transformation of the form (3.16).
4.1
β = 1 initial conditions
We see from (4.7) that for N even and p ≥N
βpl = βpN−1 βN−1l .
(4.15)
Substituting in the formula (2.29) for S2 and using (2.17) and (2.18) we thus have
S2(x, y; τx, τy)
=
q
w(y)
ΦN−2(x; τx)
rN/2−1(0) eγN−2τx −
q
w(x)CN−1(x)e−γN−1τx
hN−1

×CN−1(y)eγN−1τy.
(4.16)
19
To compute the scaled limit we make use of the asymptotic expansion [13]
e−x2/2Hn(x) = π−3/42n/2+1/4(n!)1/2n−1/12
πAi(−u) + O(n−2/3)

(4.17)
where x = (2n)1/2 −u/21/2n1/6. This gives
q
w(y)CN−1(y)

y=(2N)1/2+Y/21/2N1/6 ∼π1/42−(N−1)/2+1/4(N −1)!1/2N−1/12Ai(Y ). (4.18)
Also, from (2.18), (4.1) and (4.7)
f(x; τx)
:=
ΦN−2(x; τx)
rN/2−1(0) eγN−2τx −
q
w(x)CN−1(x)e−γN−1τx
hN−1
=
e−x2/2
(N/2 −1)!e−Nτx
∞
X
p=0
(N/2 + p)!
√π(N + 2p + 1)!HN+2p+1(x)e−(2p+3/2)τx.
Noting that for large N
(N/2 + p)!
((N + 2p + 1)!)1/2
((N −1)!)1/2
(N/2 −1)!
∼2−(p+1)
and making use of (4.18) with n = N + 2p + 1, −u ∼X −2p/N1/3 shows
((N −1)!)1/2f

(2N)1/2 +
X
21/2N1/6; tX
N1/3

∼e−N2/3t2(N−1)/221/4π−1/4N−1/12 N1/3
2
Z ∞
0
Ai(X −v)e−vtX dv.
(4.19)
Hence
S2

(2N)1/2 +
X
21/2N1/6, (2N)1/2 +
Y
21/2N1/6 ; tX
N1/3 , tY
N1/3

∼eN2/3(tY −tX)2−1/2N1/6Ai(Y )
Z ∞
0
Ai(X −v)e−vtX dv.
(4.20)
Now consider S1 as deﬁned by (2.28). Substituting (4.1) we see that the asymptotics
can be determined by writing the sum so that the sum index p is replaced by N −p, and
then using Stirling’s formula and (4.18). We thus ﬁnd
S1

(2N)1/2 +
X
21/2N1/6, (2N)1/2 +
Y
21/2N1/6; tX
N1/3, tY
N1/3

∼eN2/3(tY −tX)21/2N1/6
Z ∞
0
Ai(X + v)Ai(Y + v)e−v(tY −tX) dv.
(4.21)
Adding together (4.20) and (4.21) and substituting for S in (4.11) we thus have
Ssoft
1
(X, Y ; tX, tY ) =
Z ∞
0
Ai(X +v)Ai(Y +v)e−v(tY −tX) dv+ 1
2Ai(Y )
Z ∞
0
Ai(X −v)e−vtX dv.
(4.22)
20
Asymptotics of ˜I(x, y; τx, τy)
We know from (2.21) that ˜I is deﬁned in terms of {Φl(·; τ)}. The asymptotics of Φ2k−2 is
calculated in an analogous fashion to the expansion (4.19). Thus after noting
ΦN+2k−2(x; τ)eγN+2k−2τ
=
rN/2+k−1(0)
(N/2 + k −1)!e−Nτ
∞
X
m=k−1
H2m+N+1(x)(N/2 + m)!
π1/2(N + 2m + 1)!
e−(2m+3/2)τ
we ﬁnd
ΦN+2k−2

(2N)1/2 +
X
21/2N1/6 ; tX
N1/3

eγN+2k−2tX/N1/3 ∼rN/2+k−1(0)
((N −1)!)1/2
(N/2 −1)!
(N/2 + k −1)!
×e−N2/3tX2(N−1)/221/4π−1/4N−1/12N1/3
2
Z ∞
2k/N1/3 Ai(X −v)e−vtX dv.(4.23)
Consider now Φ2k−1. We note from (2.18), (4.1) and (4.7) that
ΦN+2k−1(y; τ)eγN+2k−1τ = −
q
w(y)rN/2+k−1(0)
HN+2k−2(y)
π1/2(N + 2k −2)!e−Nτe−(2k−3/2)τ
so use of (4.17) gives
ΦN+2k−1

(2N)1/2 +
Y
21/2N1/6 ; tY
N1/3

eγN+2k−1τY /N1/3 ∼−rN/2+k−1(0)e−N2/3tY
×e−2ktY /N1/3π−1/42(N+2k−2)/2+1/4((N + 2k −2)!)1/2N−1/12Ai(Y −
2k
N1/3).
(4.24)
Multiplying (4.23) and (4.24) together, substituting in (2.21) and making use of the
explicit value of rm(0) from (4.4), we then ﬁnd
˜Isoft
1
(X, Y ; tX, tY ) =
Z ∞
0
ds Ai(Y −s)e−stY
Z ∞
s
Ai(X −v)e−vtxdv −(X ↔Y )
(4.25)
Asymptotics of D(x, y; τx, τy)
Here the asymptotics of {Rm(·; τ)} are required. Now, from (2.14) and (4.4) we have
RN−2l−2(x; τ)eγN−2l−2τ = 2−(N−2l−2)HN−2l−2(x)eγN−2l−2τ.
Use of (4.17) then gives
q
w(x)RN−2l−2(x; τ)eγN−2l−2τ

 x=(2N)1/2+X/21/2N1/6
τ=tX/N1/3
∼eN2/3tX
×e−2ltX/N1/3π1/42−(N−2l−2)/221/4((N −2l −2)!)1/2N−1/12Ai

X +
2l
N1/3

. (4.26)
Furthermore
R2m+1(x; τ)eγ2m+1τ
=
2−(2m+1)H2m+1(x)eγ2m+1τ −m2−(2m−1)H2m−1(x)eγ2m−1τ
=
−eγ2m+1τex2/2 d
dx

e−x2/22−2mH2m(x)

−m2−(2m−1)H2m−1(x)eγ2m−1τ(1 −e2τ),
(4.27)
21
and use of (4.17) gives for the asymptotics
q
w(x)RN−2l−1(y; τ)eγN−2l−1τ

 y=(2N)1/2+Y/21/2N1/6
τ=tY /N1/3
∼eN2/3tY
×π1/42−(N−2l−2)/223/4((N −2l −2)!)1/2N1/12 d
ds

e−stY Ai(Y + s)

,
(4.28)
s := 2l/N. Multiplying together (4.26) and (4.28), dividing by r(N−2l−2)/2 and summing
over l (which is of the form of a Riemann integral) we thus obtain
Dsoft
1
(X, Y ; tX, tY ) = 1
4
Z ∞
0
ds e−stXAi(X + s) d
ds

e−stY Ai(Y + s)

−(X ↔Y ) (4.29)
Asymptotics of g(x, y; τy −τx)
According to (2.3) and (2.4)
g(x, y; τ) = e−(x2+y2)/2
∞
X
j=0
Hj(x)Hj(y)e−(j+1/2)τ
π1/22jj!
(4.30)
This summation can be evaluated in closed form [11] giving
g(x, y; τ) = e−(x2+y2)/2
e−τ/2
(1 −e−2τ)1/2 exp

−
e−2τ
1 −e−2τ (x −y)2
exp

2e−τ
1 −e−2τ xy

Hence
g

(2N)1/2 +
X
√
2N1/6, (2N)1/2 +
Y
√
2N1/6;
t
N1/3

∼N1/6
(2t)1/2e−tN2/3e−(X−Y )2/4t−t(X+Y )/2.
Alternatively, proceeding as in the derivation of (4.21), we can deduce from (4.30) that
g

(2N)1/2 +
X
√
2N1/6 , (2N)1/2 +
Y
√
2N1/6;
t
N1/3

∼e−N2/3t21/2N1/6
Z ∞
−∞Ai(X + v)Ai(Y + v)evt dv
(4.31)
Dividing by e−N2/3t21/2N1/6, replacing t by tX −tY and subtracting from (4.22) shows
˜Ssoft
1
(X, Y ; tX, tY )
=
−
Z 0
−∞Ai(X + v)Ai(Y + v)e−v(tY −tX) dv
+1
2Ai(Y )
Z ∞
0
Ai(X −v)e−vtX dv.
(4.32)
4.2
β = 4 initial conditions
Here we want to again compute the scaled distribution (4.10).
As for β = 4 initial
conditions in the Laguerre ensemble, we must modify the scale factor in (4.13) and (4.14)
so that
˜Isoft
4
(X, Y ; tX, tY )
= lim
N→∞
eN2/3(tX+tY )
2N1/3
˜I

(2N)1/2 +
X
√
2N1/6 , (2N)1/2 +
Y
√
2N1/6 ;
t
N1/3

(4.33)
22
Dsoft
4
(X, Y ; tX, tY )
= lim
N→∞e−N2/3(tX+tY )D

(2N)1/2 +
X
√
2N1/6, (2N)1/2 +
Y
√
2N1/6 ;
t
N1/3

(4.34)
Substituting (4.8) in (2.29) shows that in terms of {Cl(x)}, S2 only consists of a single
term, which reads explicitly
S2(x, y; τx, τy) =
q
w(x)w(y)CN(x)e−γN τx
hN

−N
2

RN−2(y; τy)eγN−2τy.
(4.35)
The explicit form of RN−2(y; τy)eγN−2τy is given by (4.6). This expression however does
not give a Riemann sum after substituting the asymptotic form of the integrand. Instead,
we make use of the identity
m
X
l=0
m!
l! 2−2lH2l(x)c−l = −α(4c)−meαx2 Z x
−∞e−αs2H2m+1(s) ds,
(4.36)
c = (1−α)/α. This can be veriﬁed by multiplying both sides by e−αx2 and diﬀerentiating
(we also verify that both sides have the same x →∞behaviour). Choosing c = e−2τ and
comparing with (4.6) we see that
R2m(y; τ)eγ2mτ
=
−
eτ/2
1 + e−2τ (2e−τ)−2mey2/(1+e−2τ )
Z y
−∞e−s2/(1+e−2τ )H2m+1(s) ds
=
eτ/2
1 + e−2τ (2e−τ)−2mey2/(1+e−2τ )
Z ∞
y
e−s2/(1+e−2τ )H2m+1(s) ds (4.37)
where to obtain the second equality the fact that the integrand is odd has been used.
With x = (2N)1/2 + X/21/2N1/6, making the change of variables s 7→(2N)1/2 + s and
using the asymptotic expansion (4.17) we see that
q
w(y)RN−2m

(2N)1/2 +
Y
21/2N1/6;
t
N1/3

eγN−2mt/N1/3 ∼2−3/4N−1/4π1/42−(N−2m)/2
×((N −2m + 1)!)1/2eN2/3teY t
Z ∞
Y +u e−stAi(s) ds,
u := 2m/N1/3(4.38)
For the x-dependent factor in (4.35), the asymptotic form of
q
w(x)CN(x) is given by
(4.18) with N −1 replaced by N. Making use of the explicit value of hN, we thus ﬁnd
S2

(2N)1/2 +
X
21/2N1/6, (2N)1/2 +
Y
21/2N1/6 ; tX
N1/3 , tY
N1/3

∼−N1/6
21/2 e−N2/3(tX−tY )Ai(X)eY t
Z ∞
Y
e−stAi(s) ds.
(4.39)
The asymptotic form of the quantity S1 as deﬁned by (2.28) is given by (4.21), since
S1 is the same for β = 1 and β = 4 initial conditions. Hence
Ssoft
4
(X, Y ; tX, tY )
=
Z ∞
0
Ai(X + v)Ai(Y + v)e−v(tY −tX) dv
(4.40)
−1
2Ai(X)eY t
Z ∞
Y
e−stAi(s) ds
(4.41)
23
Also, subtracting (4.31) divided by e−N2/3t21/2N1/6 (and with t 7→tX −tY ) gives
˜Ssoft
4
(X, Y ; tX, tY )
=
−
Z 0
−∞Ai(X + v)Ai(Y + v)e−v(tY −tX) dv
−1
2Ai(X)eY t
Z ∞
Y
e−stAi(s) ds
(4.42)
Asymptotics of ˜I(x, y; τx, τy)
First note from (2.18), (4.1), (4.6) and (4.8) that
Φ2k−1(x; τ)eγ2k−1τ
=
q
w(x)e−γ2k−2τ2−2(k−1)1
2H2k(x)e−2τ −(2k −1)H2k−2(x)

= −e−γ2k−2τ2−2(k−1)
 d
dx

e−x2/2H2k−1(x)

−
q
w(x)
2
H2k(x)(e−2τ −1)

(c.f. (4.27)). Use of (4.17) gives for the asymptotics
ΦN−2k−1

(2N)1/2 +
X
21/2N1/6;
t
N1/3

eγN−2k−1t/N1/3 ∼
−e−N2/3tXπ1/427/42−(N−2k−1)/2(N −2k −1)!1/2N1/12 d
ds

estXAi(X + s)

, (4.43)
s := 2k/N. Similarly
1
rk−1(0)Φ2k−2(y; τ)eγ2k−2τ =
q
w(y)H2k−1(y)e−γ2k−1τ
π1/2(2k −1)!
and so
1
rN/2−k−1(0)ΦN−2k−2

(2N)1/2 +
Y
21/2N1/6 ;
t
N1/3

eγN−2k−2t/N1/3 ∼
e−N2/3tY estY π−1/42(N−2k−1)/2+1/4(N −2k −1)!−1/2N−1/12Ai(Y + s).
(4.44)
Multiplying together (4.43) and (4.44) and summing according to (2.21) we see that
˜Isoft
4
(X, Y ; tX, tY ) =
Z ∞
0
ds estY Ai(Y + s) d
ds

estXAi(X + s)

−(X ↔Y )
(4.45)
Asymptotics of D(x, y; τx, τy)
Here we require the asymptotics of R2m(·; τ) and R2m+1(·; τ). The former is given by
(4.38). For the latter, we note from (4.6) that
1
rm(0)R2m+1(x; τ)eγ2m+1τ =
H2m+1(y)
2√πΓ(2m + 2)eγ2m+2τ
24
and thus according to (4.17)
q
w(x)
rN/2−m(0)RN−2m+1(x; τ)eγN−2m+1τ

 x=(2N)1/2+X/21/2N1/6
τ=t/N1/3
(4.46)
∼eNτx
2√π
e−utX
(Γ(N −2m + 2))1/2π1/42(N−2m+1)/2+1/4N−1/12Ai(X + u).
(4.47)
Multiplying (4.46) and (4.38) according to (2.22) we see that
D(X, Y ; tX, tY ) = 1
4eN2/3(tX+tY )
Z ∞
0
e−utY Ai(Y + u)eXtX
Z ∞
X+u e−stAi(s) ds −(X ↔Y ).
(4.48)
5
