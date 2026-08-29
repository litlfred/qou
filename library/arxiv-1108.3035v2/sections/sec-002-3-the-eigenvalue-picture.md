---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-002-3-the-eigenvalue-picture
section_title: "The eigenvalue picture"
section_number: 3
pages: 5-15
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
In this section we will derive an eigenvalue representation of our partition function eq. (2.3). It can
be obtained by the following change of variables from H to /D5,
H =
/D5 −
 m11n
W
W †
−m11n+ν

,
(3.1)
then diagonalising /D5 and W, using the HCIZ formula, and then ﬁnally integrating out the W-
eigenvalues.
1In [20, 21] all matrix elements are rescaled by
√
N to have compact support at N = ∞. This will modify these
scaling relations on the RMT side by
√
N for z and m.
5
The Jacobian of the change of variables eq. (3.1) is a constant and we get for the partition function
Z(Nf )
ν
(m; {zf}; a)
∼
Z
d /D5dW
Nf
Y
f=1
det[ /D5 + zf11N]P1(W)P2

/D5 −
 m11n
W
W †
−m11n+ν

=
e−
Nm2
4a2
Z
d /D5
Nf
Y
f=1
det[ /D5 + zf11N] exp
h
−
1
4a2 Tr[ /D2
5]
i
×
Z
dW exp

−
1
2a2(1 −a2)Tr
h
WW †i
+
1
2a2 Tr

/D5
 m11n
W
W †
−m11n+ν

.
(3.2)
Now we can diagonalise /D5 by a unitary transformation U ∈U(N),
/D5
=
UDU † ,
D = diag(d1, . . . , dn) , dj ∈R ,
(3.3)
and the chiral matrix W by a singular value decomposition (or equivalently a diagonalisation of WW †):
W
=
uY v ⇔
 m11n
W
W †
−m11n+ν

=
 0
v†
u
0
  m11n
Y
Y T
−m11n+ν
  0
u†
v
0

,
(3.4)
where Y is a rectangular n × (n + ν) matrix with real positive diagonal elements {y1, . . . , yn}, yj ≥0.
Note the diﬀerent numbers N = 2n + ν and n of these eigenvalues dj and yj , respectively. Including
the Jacobians of these transformations, which contain the standard Vandermonde determinants,
∆N({d}) ≡
N
Y
j>l
(dj −dl) ,
∆n({y2}) =
n
Y
j>l
(y2
j −y2
l ),
(3.5)
we get
Z(Nf )
ν
(m; {zf}; a)
∼
e−
Nm2
4a2
Z ∞
−∞
N
Y
j=1
ddj
Nf
Y
f=1
(dj + zf)e−
d2
j
4a2 ∆N({d})2
Z ∞
0
n
Y
b=1
dyby2ν+1
b
e
−y2
b
2a2(1−a2)
×∆n({y2})2
Z
dUdudv exp

+ 1
2a2 Tr
h
UDU †
 m11n
Y
Y T
−m11n+ν
 i
, (3.6)
where we have used the invariance of the Haar measure under the transformation
U →
 0
v†
u
0

U .
(3.7)
The unitary integrations can now be carried out and we obtain from the HCIZ integral
Z
dU exp
 1
2a2 Tr
h
UDU †
 m11n
Y
Y T
−m11n+ν
 i
=
det1≤i,j≤N
h
exp[ 1
2a2 diwj]
i
∆N({d})∆N({w})
.
(3.8)
Here wk, k = 1, . . . , N are the N eigenvalues of the matrix
 m11n
Y
Y T
−m11n+ν

which we will now
relate to the eigenvalues yb in order to partly cancel the Vandermonde determinants.
From the
solutions of the characteristic equation
0
=
det

λ11N −
 m11n
Y
Y T
−m11n+ν

= (λ + m)ν
n
Y
b=1

λ2 −m2 −y2
b

=
N
Y
j=1
(λ −wj) , (3.9)
6
the eigenvalues wk are given by2
wj
=
q
m2 + y2
j
, j = 1, . . . , n
wj+n
=
−
q
m2 + y2
j , j = 1, . . . , n
wj+2n
=
−m + ǫj , j = 1, . . . , ν .
(3.10)
Here we have lifted the degeneracy of the last ν eigenvalues by adding small parameters ǫ1, . . . , ǫν
which will be sent to zero later (for ν = 1 this is not necessary, but we will keep ǫ1̸ = 0 for symmetry
reasons). Making the ǫ-dependence explicit in the Vandermonde we can write
∆N(w)
=
∆ν({ǫ −m})
2n
Y
l=1
νY
h=1
(ǫh −m −wl)
n
Y
i>j
(wi+n −wj+n)(wi −wj)
n
Y
o,q=1
(wo+n −wq)
=
(−)
1
2n(3n−1)2n∆ν({ǫ})
n
Y
l=1
ν
Y
h=1
(ǫ2
h −2mǫh −y2
l ) ∆n({y2})2
n
Y
i=1
q
m2 + y2
i ,
(3.11)
after some algebra. The ﬁrst Vandermonde determinant ∆ν({ǫ}) will cancel the zeros from the numer-
ator in eq. (3.8) when we take the limit of degenerate eigenvalues ǫk →0, whereas in the remaining
factors in eq. (3.11) this limit is smooth.
Using induction one can easily obtain the following limiting result. For ν = 3 we have to Taylor
expand the next column to one order higher, when taking ǫ3 →ǫ1, etc., and so we end up with the
following result to leading order
lim
ǫk→0
1
∆ν({ǫ})

ex1w1
. . .
ex1w2n
ex1(−m+ǫ1)
· · ·
ex1(−m+ǫν)
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
exNw1
. . .
exNw2n
exN(−m+ǫν)
· · ·
exN(−m+ǫν)

(3.12)
=
ν−1
Y
j=0
1
j!

ex1w1
. . .
ex1w2n
e−x1m
x1e−x1m
· · ·
xν−1
1
e−x1m
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
exNw1
. . .
exNw2n
e−xNm
xNe−xNm
· · ·
xν−1
N
e−xNm

,
where we have deﬁned xi =
1
2a2 di for i = 1, . . . , N for later use.
We can now write the full answer of our partition function eq. (3.6) in term of the two sets of
eigenvalues only:
Z(Nf )
ν
(m; {zf}; a) ∼e
−−m2(2n+N(1−a2))
4a2(1−a2)
Z ∞
−∞
N
Y
j=1
ddj
Nf
Y
f=1
(dj + zf)e−
d2
j
4a2 ∆N({d})
Z ∞
m
n
Y
b=1
dube
−u2
b
2a2(1−a2)
×

ex1u1 . . . ex1un
e−x1u1 . . . e−x1un
e−x1m
x1 e−x1m . . . xν−1
1
e−x1m
· · ·
· · ·
· · ·
· · ·
exNu1 . . . exNun
e−xNu1 . . . e−xNun
e−xNm
xNe−xNm . . . xν−1
N
e−xNm

,
(3.13)
after dropping m-independent constants and changing variables uj =
q
m2 + y2
j . For ν = 0 the last ν
columns that are independent of uj have to be dropped.
2From this it can be seen that at a = 0 there is an accumulation of eigenvalues at −m. Note that our convention
diﬀers from [20, 21].
7
We will now apply a generalisation of the de Bruijn integration formula in order to integrate out
the set of variables uk. It is given by [34] (see appendix C.2 therein)
n
Y
q=1
Z
duqw(uq)
det
1≤b≤2n+ν; 1≤j≤n; 1≤i≤ν
h
{φb(uj), ψb(uj)} Abi
i
=
(−)ν(ν−1)/2n!
Pf
1≤b,c≤2n+ν; 1≤i≤ν
R
du w(u)[φb(u)ψc(u) −φc(u)ψb(u)]
	
Abi
−AT
ic
0

.
(3.14)
Here Abi = di−1
b
e−dbm/2a2 is a matrix of size N × ν. When ν = 0 it is absent and we are back to the
standard de Bruijn formula. In our case we have
Z(Nf )
ν
(m; {zf}; a)
∼
exp
h
Nm2
2a2(1 −a2)
i Z ∞
−∞
2n+ν
Y
j=1
ddj
Nf
Y
f=1
(dj + zf) exp
h
−
d2
j
4a2
i
∆2n+ν({d}) (3.15)
×Pf1≤i,j≤2n+ν; 1≤q≤ν

F(dj −di)
d q−1
i
e−dim
2a2
−d q−1
j
e−
dj m
2a2
0ν×ν

,
where we have deﬁned the antisymmetric weight
F(x)
≡
e
x2(1−a2)
8a2
"
erf
x
√
1 −a2
√
8a2
+
m
p
2a2(1 −a2)

+ erf
x
√
1 −a2
√
8a2
−
m
p
2a2(1 −a2)
#
(3.16)
=
4
p
2πa2(1 −a2)
Z ∞
m
du e
−
u2
2a2(1−a2) sinh
h xu
2a2
i
.
We have also used the antisymmetry of erf(x) =
2
√π
R x
0 ds e−s2 = −erf(−x). Eq. (3.15) is the partition
function in terms of the joint probability distribution functions (jpdf) of its eigenvalues.
Let us give the two examples that we will solve explicitly in the following sections. For Nf = ν = 0
we have
Z(Nf =0)
ν=0
(m; a) ≡
Z ∞
−∞
2n
Y
j=1
ddj exp
h
−
d2
j
4a2
i
∆2n({d})Pf1≤i,j≤2n[F(dj −di)] .
(3.17)
Here we have omitted all constants that will drop out in expectation values and density correlation
functions to be considered in the next section. For ν = 1 and Nf = 0 we have
Z(Nf =0)
ν=1
(m; a) ≡
Z ∞
−∞
2n+1
Y
j=1
ddj exp
h
−
d2
j
4a2
i
∆2n+1({d})Pf1≤i,j≤2n+1

F(dj −di)
e−dim
2a2
−e−
djm
2a2
0

. (3.18)
Let us add one remark on the universality of our model. In order to be able to use the HCIZ
formula it was crucial that we started with a Gaussian distribution of matrix elements. However, after
having arrived at an eigenvalue representation eq. (3.15) we could take this as a starting point and
we would obtain the same results below, if we were to replace the Gaussian distribution exp[−d2
j/4a2]
by a more general weight function w(dj). The same general framework to compute density correlation
functions to be presented in the next section could be applied.
8
4
All density correlation functions for ﬁnite-N
The partition function eq. (3.17) is very much reminiscent of the one for the GUE-GOE transition in
[28], apart from the diﬀerent function F(x) inside the Pfaﬃan. We can therefore apply the general
method of solving this two-matrix model developed in [32] for general weight functions, which applies
equally to eq. (3.18) with ν = 1. From now on we will restrict ourselves to ν = 0, 1 and Nf = 0.
The k-point density correlation functions that we will determine are deﬁned as follows for ν = 0
ρk(d1, . . . , dk) ≡
1
Z(0)
ν=0
N!
(N −k)!
Z ∞
−∞
ddk+1 . . . ddN
N
Y
j=1
w(dj) ∆N({d})Pf1≤i,j≤N[F(dj −di)] ,
(4.1)
with even N = 2n, and for ν = 1 as
ρν=1
k
(d1, · · · , dk) =
1
Z(0)
ν=1
N!
(N −k)!
Z ∞
−∞
ddk+1 · · · ddN
N
Y
j=1
w(dj)∆N({d})Pf1≤i,j≤N
F(dj −di)
f(di)
−f(dj)
0

,
(4.2)
with odd N = 2n + 1. Here we have used the abbreviations
w(x) ≡exp[−x2/(4a2)] ,
f(x) ≡exp[−mx/(2a2)] .
(4.3)
The expressions for the solution in terms of three kernels will hold for a general weight functions
w(x), f(x) and F(x) though. Here and in the following we will drop the label ν = 0 and only index
ν = 1. Furthermore we also suppress the dependence on the parameters m, a in the arguments for
simplicity.
The correlation functions deﬁned above can be expressed as the Pfaﬃan of the following matrix
[32]
ρν
k(d1, . . . , dk) = Pf1≤i,j≤k

Iν
n(di, dj)
Sν
n(di, dj)
−Sν
n(dj, di)
−Dν
n(di, dj)

,
(4.4)
given in terms of three kernels.
Let us begin with the case ν = 0 where we have [32]
Sn(x, y)
=
n
X
j=1
w(y)
rj−1

φ2j−2(x)R2j−1(y) −φ2j−1(x)R2j−2(y)

,
Dn(x, y)
=
n
X
j=1
w(x)w(y)
rj−1

R2j−2(x)R2j−1(y) −R2j−1(x)R2j−2(y)

,
In(x, y)
=
−
n
X
j=1
1
rj−1

φ2j−2(x)φ2j−1(y) −φ2j−1(x)φ2j−2(y)

−F(x −y) .
(4.5)
In our speciﬁc case of weights eqs. (3.16) and (4.3) these kernels are given by the following monic
skew-orthogonal polynomials Rj(x) = xj + . . . and their integral transforms,
R2j(x)
=
j! 2j(1 −a2)j
(−1)j√π
Z ∞
−∞
ds e−s2Lj
(x + 2ias)2 −m2
2(1 −a2)

,
(4.6)
R2j+1(x)
=
−2a2w(x)−1 d
dx
h
w(x)R2j(x)
i
=
j! 2j(1 −a2)j
(−1)j√π
Z ∞
−∞
ds e−s2(x + 2ias)Lj
(x + 2ias)2 −m2
2(1 −a2)

,
φj(x)
=
Z ∞
−∞
dy w(y)F(x −y)Rj(y) .
(4.7)
9
Here we have used an integration by parts to simplify the expression for the odd polynomials. The
polynomials have parity, Rj(−x) = (−)jRj(x), as can be easily seen from the integral representations.
These skew-orthogonal polynomials satisfy the following relations as it is shown in appendix C in
detail:
⟨R2j, R2l+1⟩= rjδjl ,
⟨R2j, R2l⟩= 0 = ⟨R2j+1, R2l+1⟩
(4.8)
with the skew product deﬁned as
⟨h, g⟩≡
Z ∞
−∞
dxdy w(x)w(y)F(x −y)h(y)g(x) .
(4.9)
The squared norms read
rj ≡⟨R2j, R2j+1⟩= 8
√
2πa2(1 −a2)2j+ 1
222j(j!)2e
−
m2
2(1−a2) ,
(4.10)
are also derived in appendix C. The quenched partition function can now be expressed in term of
these norms and is given by
Z(Nf =0)
ν=0
= N!
n−1
Y
j=0
rj .
(4.11)
Because of the special form of our polynomials the kernels can be simpliﬁed. We start with the
kernel Dn(x, y), the other two easily follow from the relations
Sn(x, y)
=
Z ∞
−∞
dz F(x −z)Dn(z, y) ,
In(x, y) + F(x −y)
=
−
Z ∞
−∞
dz F(x −z)Sn(x, z) .
(4.12)
Inserting eq. (4.6) into the deﬁnition we obtain
Dn(x, y)
=
e−x2+y2
4a2
e
m2
2(1−a2)
8π
p
2πa2(1 −a2)
Z ∞
−∞
ds dr e−s2−r2[(y + 2ias) −(x + 2iar)]
×
n−1
X
j=0
Lj
(x + 2iar)2 −m2
2(1 −a2)

Lj
(y + 2ias)2 −m2
2(1 −a2)

.
(4.13)
Using the Christoﬀel-Darboux identity
n−1
X
j=0
Lj(X)Lj(Y ) = −n Ln(X)Ln−1(Y ) −Ln(Y )Ln−1(X)
X −Y
,
(4.14)
we obtain the following ﬁnal expression
Dn(x, y)
=
e−x2+y2
4a2 e
m2
2(1−a2) n
√
1 −a2
4π
√
2πa2
Z ∞
−∞
ds dr e−s2−r2
(4.15)
×
Ln

(x+2iar)2−m2
2(1−a2)

Ln−1

(y+2ias)2−m2
2(1−a2)

−Ln−1

(x+2iar)2−m2
2(1−a2)

Ln

(y+2ias)2−m2
2(1−a2)

(y + 2ias) + (x + 2iar)
.
10
The simplest examples for the correlation functions at ﬁnite-N are the spectral density and the spectral
two-point function. These are given by
ρ1(x)
=
Sn(x, x) =
Z ∞
−∞
dz F(x −z)Dn(z, x) ,
ρ2(x, y)
=
Sn(x, x)Sn(y, y) + In(x, y)Dn(x, y) −Sn(x, y)Sn(y, x) ,
(4.16)
with the insertion of eq. (4.15) and (4.12), see eq. (4.25) below. This ends the general solution of our
model for ﬁnite-N for ν = 0.
For ν = 1 the skew-orthogonal polynomials can be expressed in terms of those for ν = 0. Following
[32] we introduce new polynomials
Rν=1
j
(x) ≡Rj(x) −
sj
sN−1
RN−1(x),
j = 0, 1, · · · , N −2 ,
(4.17)
and for the largest polynomial
Rν=1
N−1(x) ≡RN−1(x) ,
(4.18)
with coeﬃcients
sj =
Z ∞
−∞
dx w(x)f(x)Rj(x).
(4.19)
Moreover we deﬁne the integral transforms of the polynomials as in the previous case eq. (4.7)
φν=1
j
(x) ≡
Z ∞
−∞
dy F(x −y)w(y)Rν=1
j
(y).
(4.20)
The kernels for ν = 1 to be inserted in eq. (4.4) read [32]
Sν=1
n
(x, y)
=
n
X
j=1
w(y)
rj−1
 φν=1
2j−2(x)Rν=1
2j−1(y) −φν=1
2j−1(x)Rν=1
2j−2(y)

+
1
sN−1
f(x)w(y)Rν=1
N−1(y),
Dν=1
n
(x, y)
=
n
X
j=1
w(x)w(y)
rj−1
 Rν=1
2j−2(x)Rν=1
2j−1(y) −Rν=1
2j−1(x)Rν=1
2j−2(y)

,
Iν=1
n
(x, y)
=
−
n
X
j=1
1
rj−1
 φν=1
2j−2(x)φν=1
2j−1(y) −φν=1
2j−1(x)φν=1
2j−2(y)

+
1
sN−1
 φν=1
N−1(x)f(y) −φν=1
N−1(y)f(x)

−F(x −y).
(4.21)
The partition function is also evaluated as
Z(Nf =0)
ν=1
= N! sN−1
n−1
Y
j=0
rj.
(4.22)
As a last step we still have to determine the new coeﬃcients sj. We can readily ﬁnd
s2j
=
Z ∞
−∞
dx e−x(x+2m)/(4a2)R2j(x)
=
j!2j(1 −a2)jem2/(4a2)
(−1)j√π
Z ∞
−∞
dxds e−(x+m)2/(4a2)−s2Lj
(x + 2ias)2 −m2
2(1 −a2)

=
(−1)j j! 2j+1(1 −a2)j√π a em2/(4a2) ,
(4.23)
11
for the even coeﬃcients, using an argument as in eq. (C.19), and
s2j+1
=
−2a2
Z ∞
−∞
dxe−mx/(2a2) d
dx
h
e−x2/(4a2)R2j(x)
i
=
−m
Z ∞
−∞
dx e−x(x+2m)/(4a2)R2j(x)
=
−m s2j ,
(4.24)
for the odd coeﬃcients. This ends our general solution for ν = 1.
In order to check that the limit a →0 correctly reproduces the chGUE let us spell out the densities
explicitly, where we start with ν = 0. Here we use eq. (4.13) rather than eq. (4.15) and we obtain
ρ1(x)
=
Z ∞
−∞
dz e
−(z+x)2
8a2
+ (z−x)2
8
+
m2
2(1−a2)
8πa
p
2π(1 −a2)
"
erf
(x −z)(1 −a2) + 2m
2a
p
2(1 −a2)

+ erf
(x −z)(1 −a2) −2m
2a
p
2(1 −a2)
#
×
Z ∞
−∞
dsdr e−s2−r2(x −z + 2ia(s −r))
n−1
X
j=0
Lj
(z + 2iar)2 −m2
2(1 −a2)

Lj
(x + 2ias)2 −m2
2(1 −a2)

.
(4.25)
Because of the delta-function that we obtain from
lim
a→0
1
2a
√
2π
e−(z+x)2
8a2
= δ(z + x) ,
(4.26)
we get the following from the error-functions (cf. B.9)
lim
a→0 erf
 
2x(1 −a2) ± 2m
2a
p
2(1 −a2)
!
= sign(x ± m) .
(4.27)
The resulting expression we can rewrite as
x(sign(x + m) + sign(x −m)) = |x|2Θ(|x| −m) .
(4.28)
In the second line in eq.
(4.25) the integrals decouple and we obtain a simple sum of Laguerre
polynomials. The ﬁnal answer is thus
lim
a→0 ρ1(x)
=
|x| e−x2
2 + m2
2
n−1
X
j=0
Lj
x2 −m2
2
2
Θ(|x| −m)
(4.29)
=
|x|
√
x2 −m2 ρchGUE
1
p
x2 −m2

Θ(|x| −m) ,
(4.30)
which corresponds to the shifted density of the chGUE for ﬁnite-n, due to the extra mass in our Dirac
operator deﬁnition eq. (2.1),
ρchGUE
1
(y) = |y| e−y2/2
n−1
X
l=0
Ll(y2/2)2 .
(4.31)
As an illustration we have plotted the densities in ﬁgure 1. For comparison we also display the
ﬁnite-n density of the chGUE eq. (4.31) in the limit a →0. Switching on a > 0 the smoothening of
the hard wall provided by the Heaviside-Theta functions is nicely seen in ﬁgure 1.
12
0
1
2
3
4
5
6
0.5
1.0
1.5
2.0
0
1
2
3
4
5
6
0.5
1.0
1.5
2.0
Figure 1: Example for the ν = 0 quenched density at ﬁnite n = 4 at diﬀerent masses: m = 0.4 (top
left plots) and m = 1 (top right plots): the top black curves correspond to the shifted chGUE density
eq. (4.29) at a = 0 (which is clipped for m = 1) ending at a sharp cutoﬀfor m > 0, see eq. (4.30).
The density ρ1(x) eq. (4.25) is plotted at various values of the deformation parameter a: at a = 0.1
(top smooth blue curve), a = 0.3 (middle smooth red curve), and at a = 0.9 (lowest yellow curve)
which is already indistinguishable from the GUE curve. Because the spectral density is symmetric
due to ν = 0 we only show the positive eigenvalues. The lower plots show the same curves at m = 0,
the chGUE-GUE transition. Here a = 0 and a = 0.1 are already indistinguishable.
Let us now spell out the density for ν = 1 explicitly and perform the limit a →0 there. In view of
the relation between the polynomials eq. (4.17) it is useful to express the kernels for ν = 1 in terms
of those with ν = 0 as well. We begin with the simplest kernel containing only polynomials and no
integral transforms. After some algebra we obtain
Dν=1
n
(x, y)
=
Dn(x, y) + e−(x2+y2)
4a2
e
m2
2(1−a2)
1
8aπ
p
2π(1 −a2)
Z ∞
−∞
ds e−s2Ln
(y + 2ias)2 −m2
2(1 −a2)

×
Z ∞
−∞
dr e−r2(x + 2iar + m)L(1)
n−1
(x + 2iar)2 −m2
2(1 −a2)

−(x ↔y)

,
(4.32)
where we used the following identity for generalised Laguerre polynomials [35]
n−1
X
j=0
Lj(z) = L(1)
n−1(z) .
(4.33)
For the kernel determining the density we obtain after inserting the deﬁnitions
Sν=1
n
(x, y)
=
Z ∞
−∞
dzF(x −z)Dν=1
n
(z, y) + e−y2+2xm+m2
4a2
1
2πa
Z ∞
−∞
ds e−s2Ln
(y + 2ias)2 −m2
2(1 −a2)

.
(4.34)
13
These two equations together with eq. (4.15) then determine the spectral density for ν = 1 shown in
ﬁgure 2,
ρν=1
1
(x) = Sν=1
n
(x, x) .
(4.35)
Figure 2: Example for the ν = 1 quenched density at ﬁnite n = 4 at diﬀerent masses: m = 0 (left
plots) and m = 1 (right plots). Because for m = 0 the density is still symmetric we only plot the
positive eigenvalues. The black curves correspond to the (shifted) chGUE density at a = 0. It can be
nicely seen how the delta-function at x = −m gets gradually smoothed out, where we show a = 0.1
(blue curve) and a = 0.3 (red curve).
We can now perform the limit a →0 as a check. The last term in eq. (4.34) gives a delta-function,
δ(x + m), the exact zero-eigenvalue of the ν = 1 chGUE shifted to x = −m. Using the result eq.
(4.29) and the above results for the limit at ν = 0 we obtain3
lim
a→0 ρν=1
1
(x)
=
|x| e−x2
2 + m2
2
n−1
X
j=0
Lj
x2 −m2
2
2
Θ(|x| −m)
−|x| e−x2
2 + m2
2 Ln
x2 −m2
2

L(1)
n−1
x2 −m2
2

Θ(|x| −m) + δ(x + m).(4.36)
This can be seen as follows to be equivalent to the density of the chGUE at ν = 1
ρchGUE
1, ν=1 (y) = |y|3e−y2/2
n−1
X
l=0
1
2(l + 1)L(1)
l
(y2/2)2 ,
(4.37)
shifted as in eq. (4.30). When using further identities [35]
XL(1)
l
(X) = (l + 1)

Ll(X) −Ll+1(X)

,
L(1)
l
(X) = Ll(X) + L(1)
l−1(X) ,
(4.38)
(and setting L−1 ≡0 here), we obtain the desired result, with X ≡1
2(x2 −m2),
X
n−1
X
l=0
1
l + 1L(1)
l
(X)2
=
n−1
X
l=0
L(1)
l
(X)

Ll(X) −Ll+1(X)

=
n−1
X
l=0

Ll(X) + L(1)
l−1(X)

Ll(X) −
n−1
X
l=0
L(1)
l
(X)Ll+1(X)
=
n−1
X
l=0
Ll(X)2 −L(1)
n−1(X)Ln(X) .
(4.39)
3From this we might speculate that the second term in eq. (4.34) leading to δ(x + m) describes the distribution of a
single eigenvalue at ﬁnite-N.
14
5
