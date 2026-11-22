---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-002-3-the-eigenvalue-picture
section_title: "The eigenvalue picture"
section_number: 3
pages: 5-9
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
The eigenvalue picture
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
