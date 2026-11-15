---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-005-321-the-thermodynamic-limit
section_title: "The thermodynamic limit"
section_number: 3.2.1
pages: 15-18
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
---
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
