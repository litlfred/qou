---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-005-14-kuniba-nakanishis-dilogarithm-conjecture
section_title: "Kuniba-Nakanishi’s dilogarithm conjecture."
section_number: 1.4
pages: 26-31
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
Recall that the dilogarithm function is deﬁned by
Li2(z) =
∞
X
n=1
zn
n2 ,
(|z| < 1).
By using the integral representation
Li2(z) = −
Z z
0
log(1 −t)
t
dt,
(1.32)
Li2(z) can be analytically continued as a multivalued complex function to the complex
plane cut along the real axis from 1 to +∞. In the sequel the principal branch of diloga-
rithm which can be deﬁned by taking the principal branch of logarithm function
−π < Im(log(z)) = arg(z) ≤π
in the previous integral is used. The integration contour in (1.32) does not pass through
the branch cut of log z. Let us consider also the principal branch of Rogers’ dilogarithm
using the integral representation
L(z) = −1
2
Z z
0
log(1 −x)
x
+ log x
1 −x

dx,
(1.33)
where the principal branch of logarithm function is taken.
The integration contour in
(1.33) is assumed to be located in the branch of log x.
Let us set
Qm(ϕ) = sin(m + 1)ϕ
sin ϕ
,
fm(ϕ) = 1 −Qm+1(ϕ)Qm−1(ϕ)
Q2m(ϕ)
=
1
Q2m(ϕ),
Dilogarithm identities
27
where ϕ = π(j + 1)
r + 2
, 1 ≤j ≤r and g.c,d. (j + 1, r + 2) = 1.
Following [KN] and [KNS], let us deﬁne c0(ϕ), dm(ϕ), and y(ϕ) as
π2
6 c0(ϕ) =
r−1
X
m=1

L(fm(ϕ)) −πi
2 dm(ϕ) log(1 −fm(ϕ))

,
πidm(ϕ) = log fm(ϕ) −2
r−1
X
k=1
Amk log(1 −fk(ϕ)),
where
Amk = min(k, m) −km
r ,
1 ≤m, k ≤r −1,
y(ϕ) = 1
πi
(r−1
X
k=1
k log(1 −fk(ϕ)) + r log Qr−1(ϕ) −(r −1) log Qr(ϕ)
)
.
1.4.1. Kuniba-Nakanishi’s conjecture for sl(2).
N(j, r) := 1
24
 3r
r + 2 −1 −6j(j + 2)
(r + 2)
+ 6y2
r
−c0(ϕ)

∈Z.
Remarks. 1) One can show that y := y(ϕ) is an integer for any ϕ, whereas dm(ϕ) is
an integer if ϕ = π(j + 1)
r + 2
. Namely, it follows from deﬁnition that (fm := fm(ϕ),
Qm :=
Qm(ϕ))
1 −fm = Qm+1Qm−1
Q2m
.
Consequently,
r−1
Y
k=1
(1 −fk)kQr
r−1Q−(r−1)
r
= 1,
that is equivalent to exp(2πiy(ϕ)) = 1. Now, if ϕ = π(j + 1)
r + 2
, then Qr = fr = 1 and
(1 −fm)2 =
f 2
m
fm−1fm+1
.
Using the fact that the matrix A := (Amk) appears to be the inverse to the Cartan matrix
Cr−1 = (2δi,j −δi+1,j −δi,j+1), 1 ≤i, j ≤r −1, one can check
fm =
r−1
Y
k=1
(1 −fk)2Amk.
Consequently, log(2πidm(ϕ)) = 1, as it was claimed.
28
Anatol N. Kirillov
2) If ϕ = π(j + 1)
r + 2
, 0 ≤j ≤r, and g.c.d.(j + 1, r + 2) = 1, it can be shown that
y(ϕ) = r min(j, r −j + (−1)j).
3) It follows from the deﬁnitions that (x ∈R)
L(x) = π2
3 −L(x−1) −πi
2 log x,
if x ≥1,
(1.34)
L(x) = −π2
6 + L

1
1 −x

+ πi
2 log(1 −x),
if x ≤0.
Thus (see (1.5)), the single-valued dilogarithm is the real part of L(x), if x ∈R.
Before stating our main results of this section, let us consider an explanatory example.
Example. Assume r = 3 and j = 1, then we have ϕ = 2π
5 and
f1 = f2 =

2 sec 2π
5
2
= ρ−2 = 3 +
√
5
2
;
1 −f1 = −ρ−1.
First of all, πid1 = log f1 −2 log(1 −f1) = −2πi. Thus, d1 = d2 = −2. Further, using the
fact Q2 = 1 −Q2
1 =
1
f1 −1, one can ﬁnd
y = 1
πi {log(1 −f1) + 2 log(1 −f2) + 3 log Q2} = 3
πi(log(1 −f1) −log(f1 −1)) = 3.
Consequently,
π2
6 c0(ϕ) = 2(L(f1) + πi log(1 −f1)) = 2(π2
3 −L(ρ2) −πi
2 log f1 + πi log(f1 −1) −π2)
= 2π2
1
3 −1
15 −1

= −44
5 L(1).
Here we used (1.34) and Landen’s result L(ρ2) = π2
15. Finally,
N(1, 3) = 1
24
9
5 −1 −18
5 + 18 + 44
5

= 1.
Even more, using the result (1.16) with j = 0, 1, r −1, r and r ≡1 (mod2), it can be shown
that N(1, r) = r −1
2
, N(r −1, r) = r and N(0, r) = N(r, r) = 0.
Dilogarithm identities
29
Theorem 3.
Let r be an odd positive integer and j be an integer such that
0 ≤2j + (−1)j+1 ≤r. Then
N(r −j, r) = N(j, r) + j(−1)j−1 r + (−1)j+1
2
.
To obtain an additional information about the numbers N(j, r) let us introduce a
function
bj(r) := j2(r −1)
2
−j3 −j
6

r
j + 1

−N(j, r),
where [x] is the integer part of a real number x.
Note that according to Theorem 3, it is suﬃcient to consider a behavior of the function
bj(r) only in the ”stable region”, namely when r ≥2j + (−1)j+1.
Theorem 4. Let r and j be the positive integers such that r ≥2j + (−1)j+1 and
r ≡1(mod 2). Then bj(r) is an integer depending only on the residue of r modulo j + 1.
If r ≡s(mod j + 1) and 0 ≤s ≤j, let us denote by ebj(s) the ”stable value” of the
function bj(r). Thus for a given positive integer j we reduced a problem of computing the
inﬁnite family of numbers N(j, r), r ≥2j + 1, to that for ﬁnite collection of quantities
ebj(s), 0 ≤s ≤j, only.
Theorem 5. i) (Duality) If 0 ≤s ≤j −3, then ebj(s) + ebj(j −3 −s) =

j
3

−

j
2

,
ii) ebj(j) = ebj(j −2) =

j
3

.
In principle, using the identity (1.16) it is possible to compute the functions ebj(s) ex-
actly (and consequently, to ﬁnd the remainder term N(j, r) in Kuniba-Nakanishi’s dilog-
arithm sum c0(ϕ)). We give here only partial results concerning the computation of the
numbers ebj(s).
Theorem 6. i) ebj(0) = −
"j −1
2
2#
,
ii) ebj(1) =
2j
3
 2j + 2
3

−j(j −1)
2
,
iii) ebj(2) = 2
j
4
 3j + 3
4

−
"j −1
2
2#
.
On the other hand (r ≡1(mod 2)),
iv) b1(r) = 0,
v) b2(r) = 0, if r ≥3,
vi) b3(r) = 1, if r ≥7.
Corollary 2 (of Theorem 4). If r is an odd positive integer, then N(j, r) is an integer
for any admissible value of j (i.e. g.c.d. (j + 1, r + 2) = 1).
30
Anatol N. Kirillov
Corollary 3 (of Theorem 6). We have (r ≡1(mod 2))
i) N(2, r) = 2(r −1) −
hr
3
i
, if r ≥3,
ii) N(3, r) = 9r −1
2
−4
hr
4
i
−1, if r ≥7.
Conjecture 1. If g.c.d. (j + 1, r + 2) = 1 and r̸ ≡0(mod j), then N(j, r) is a positive
integer.
1.5. General A1-type dilogarithm identity [Kir7].
Let p be a rational number and k be a natural number. Let us consider a decomposition
of p/k into continued fraction
p
k = br +
1
br−1 +
1
· · · +
1
b1 + 1
b0
,
(1.35)
where bi ∈N,
0 ≤i ≤r −1 and br ∈Z. Using the decomposition (1.35) we deﬁne:
y−1 = 0,
y0 = 1,
y1 = b0, . . ., yi+1 = yi−1 + biyi,
m0 = 0,
m1 = b0,
mi+1 = |bi| + mi,
r(j) := rk(j) = i,
if kmi ≤j < kmi+1 + δi,r,
nj := nk(j) = kyi−1 + (j −kmi)yi,
if kmi ≤j < kmi+1 + δi,r,
where 0 ≤i ≤r. Using the decomposition (1.35) let us consider the following dilogarithm
sum
kmr+1
X
j=1
(−1)r(j)Lk

yr(j)θ, (nj + yr(j))θ

= (−1)r π2
6 s(l, k + 1, p),
(1.36)
where θ =
(l + 1)π
kyr+1 + (k + 1)yr
, and
Lk(θ, ϕ) := 2L

sin θ · sin kθ
sin ϕ · sin(ϕ + (k −1)θ)

−
k−1
X
j=0
L
 
sin θ
sin(ϕ + jθ)
2!
.
(1.37)
Theorem 7. We have
(i)
s(0, k + 1, p) := ck = 3(p + 1 −k)
p + k + 1 ,
k ≥1,
(1.38)
(ii) s(l, k + 1, p) = ck −6k l(l + 2)
p + k + 1 + 6Z,
(1.39)
If k = 1 one can obtain an exact formula for the remainder term in (1.39) (see [Kir7]
or Exercise 11).
Dilogarithm identities
