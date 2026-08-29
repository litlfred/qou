---
doc_id: arxiv-hep-th-9711057v2
doc_title: "The microscopic spectrum of the QCD Dirac operator with finite quark masses"
section_id: sec-001-ii-random-matrix-theory-for-finite-quark-masses
section_title: "RANDOM-MATRIX THEORY FOR FINITE QUARK MASSES"
section_number: II
pages: 2-6
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
doc_brief: "The microscopic spectrum of the QCD Dirac operator with finite quark masses — 7 sections: INTRODUCTION; RANDOM-MATRIX THEORY FOR FINITE QU; CALCULATION OF OBSERVABLES"
---
In Sec. II A, we formulate the chiral random-matrix model by introducing the probability density function and the
partition function in the presence of ﬁnite quark masses. In Sec. II B, we construct the orthogonal polynomials of the
model. An alternative construction is presented in Sec. II C which is based on a certain duality between models in
diﬀerent matrix spaces.
A. Formulation of the model
The statistical properties of the random-matrix model for the massive Dirac operator with Nf ﬂavors and dynamical
quark masses Mf (f = 1, . . . , Nf) which was introduced above are given by the probability density function
2
P (Nf)
N
(W, M) =
1
eZ(Nf)
N
(M)
Nf
Y
f=1
det(WW † + M 2
f ) exp(−NΣ2tr WW †)
(3)
with M = (M1, . . . , MNf ). Here, W is a complex matrix of dimension N. Apart from a Gaussian, this distribution
contains Nf fermionic determinants. Eventually, we are mainly interested in the microscopic limit. Hence, it suﬃces
to take into account a Gaussian in the total distribution (3) since various authors [8,9] have given proofs of universality
in related problems. Note that even for nonzero topological charge ν it is suﬃcient to consider only square matrices
W in the calculation because of the duality between topology and ﬂavor [5,4]. A nonzero ν is obtained by introducing
ν additional massless ﬂavors at the end of the calculation. The normalization constant
eZ(Nf)
N
(M) =
Z
d[W]
Nf
Y
f=1
det(WW † + M 2
f ) exp(−NΣ2tr WW †)
(4)
depends on the quark masses and plays the role of a partition function. Since both of the above expressions depend on
the matrices W only through invariant functions of WW †, they can be reduced to integrals over radial coordinates. We
write W = UΛ ¯V with U ∈U(N), ¯V ∈U(N)/UN(1), and Λ = diag(λ1, . . . , λN), where the radial coordinates λi are
restricted to the positive real axis. Thus, we have WW † = UΛ2U † suggesting the introduction of new variables xi = λ2
i .
The measure transforms as d[W] = ∆2
N(X)d[X]dµ(U)dµ( ¯V ), where X = diag(x1, . . . , xN), ∆N(X) = Q
i<j(xi −xj)
is the Vandermonde determinant, and dµ is the Haar measure. After integrating over the unitary groups, we obtain
P (Nf)
N
(X, M) =
1
Z(Nf)
N
(M)
∆2
N(X)
N
Y
i=1
w(Nf)(xi, M)
(5)
for the probability density and
Z(Nf)
N
(M) =
Z
d[X] ∆2
N(X)
N
Y
i=1
w(Nf )(xi, M)
(6)
for the partition function Z(Nf)
N
(M) which diﬀers from eZ(Nf)
N
(M) by the group volumes. The expression
w(Nf )(x, M) = exp(−NΣ2x)
Nf
Y
f=1
(x + M 2
f )
(7)
will be referred to as the weight function.
Because of a main result of RMT [21], all spectral correlation functions R(Nf)
k
(x1, . . . , xk, M) of our model can
readily be written in terms of the polynomials p(Nf)
n
(x, M) which are orthogonal with respect to the weight function
w(Nf )(x, M),
Z ∞
0
dx w(Nf )(x, M)p(Nf)
n
(x, M)p(Nf)
m
(x, M) =
Z(Nf)
n+1 (M)
(n + 1) Z(Nf)
n
(M)
δnm .
(8)
The correlation functions are given as the determinant
R(Nf)
k
(x1, . . . , xk, M) = det
h
K(Nf)
N
(xi, xj, M)
i
i,j=1,...,k
(9)
with a kernel given by
K(Nf)
N
(x, y, M) =
q
w(Nf)(x, M)w(Nf )(y, M)
N−1
X
n=0
(n + 1) Z(Nf)
n
(M)
Z(Nf)
n+1 (M)
p(Nf)
n
(x, M)p(Nf)
n
(y, M) .
(10)
With the help of the Christoﬀel-Darboux formula the kernel can be expressed as
K(Nf)
N
(x, y, M) = N Z(Nf)
N−1
Z(Nf)
N
q
w(Nf )(x, M)w(Nf )(y, M)
×p(Nf)
N
(x, M)p(Nf)
N−1(y, M) −p(Nf)
N−1(x, M)p(Nf)
N
(y, M)
x −y
,
(11)
provided that the coeﬃcient of the power xn in p(Nf)
n
(x, M) is unity. Eventually, we will take the microscopic limit
as discussed in the Introduction.
3
B. Construction of orthogonal polynomials
The polynomials p(Nf)
n
(x, M) can be constructed by applying a standard formula [22] in the theory of orthogonal
polynomials. In our case, it reads
p(Nf)
n
(x, M) =
1
Z(Nf)
n
(M)
Z
d[X]∆2
n(X)
n
Y
i=1
w(Nf)(xi, M)(x −xi) .
(12)
This is an integral over n variables xi (i = 1, . . . , n). We notice that n replaces the dimension N of the matrices W
in the partition function Z(Nf)
n
(M) and in the Vandermonde determinant ∆n(X). Moreover, by construction, the
coeﬃcient in front of xn is unity.
Fortunately, there is a further result, the Christoﬀel formula [22], which allows us to immediately write down the
polynomials explicitly: The weight function w(Nf)(x, M) is a product of the weight function w(0)(x) and a polynomial
whose zeros are the negative squared quark masses −M 2
f and which is nonnegative on the real axis. Therefore, the
polynomials p(Nf)
n
(x, M) can be written in terms of the polynomials which are orthogonal with respect to the weight
w(0)(x) = exp(−NΣ2x). These are precisely the Laguerre polynomials L(0)
n (NΣ2x). The application of the Christoﬀel
formula then yields
p(Nf)
n
(x, M) =
1
C(Nf)
n
(M)
1
QNf
f=1(x + M 2
f )
(n + Nf)!
(NΣ2)n+Nf
×

L(0)
n (NΣ2x)
L(0)
n+1(NΣ2x)
· · · L(0)
n+Nf (NΣ2x)
L(0)
n (−NΣ2M 2
1 )
L(0)
n+1(−NΣ2M 2
1)
· · · L(0)
n+Nf (−NΣ2M 2
1)
...
...
...
L(0)
n (−NΣ2M 2
Nf ) L(0)
n+1(−NΣ2M 2
Nf) · · · L(0)
n+Nf (−NΣ2M 2
Nf)

(13)
with a function C(Nf )
n
(M) yet to be determined. In Sec. II C, we will present a very direct and highly convenient
computation of the polynomials (13) including all normalization factors.
Here we proceed as follows: Since the
polynomial p(Nf)
n
(x, M) has to be invariant under permutations of the masses Mf and must have a ﬁnite limit when
all quark masses are degenerate, a reasonable guess for the normalization function is
C(Nf )
n
(M) = det
h
L(0)
n+f−1(−NΣ2M 2
f ′)
i
f,f ′=1,...,Nf
,
(14)
see Sec. II C below, in particular Eq. (24).
With this ansatz, the partition function Z(Nf)
n
(M) is obtained
by studying the case of Nf + 1 ﬂavors.
On the one hand, Eqs. (6) and (12) yield p(Nf)
n
(−M 2
Nf+1, M) =
−Z(Nf+1)
n
(M, MNf+1)/Z(Nf)
n
(M), which, on the other hand, has to be equal to the right-hand side of Eq. (13)
for x = −M 2
Nf+1. Thus, we arrive at the recursion relation
Z(Nf+1)
n
(M, MNf+1)
C(Nf+1)
n
(M, MNf+1)
= Z(Nf)
n
(M)
C(Nf)
n
(M)
(n + Nf)!
(NΣ2)n+Nf
1
QNf
f=1(M 2
f −M 2
Nf+1)
(15)
which implies
Z(Nf)
n
(M) =
Nf
Y
f=1
(n + f −1)!
(NΣ2)n+f−1
C(Nf )
n
(M)
∆Nf (−M 2) .
(16)
The correctness of these results can be veriﬁed using the orthogonality relation (8). In the microscopic limit, the
partition function agrees with the result obtained in Ref. [18], see Sec. III, Eq. (27). (Note that in Ref. [18], the result
is expressed in terms of derivatives of modiﬁed Bessel functions. Using the recurrence relations for Bessel functions
[23] and the properties of the determinant, one can show that the results are identical.)
4
C. A duality of matrix ensembles
In this section, we present an alternative derivation of the orthogonal polynomials p(Nf)
n
(x, M) and of the partition
function Z(Nf)
N
(M). It employs a certain kind of duality between matrix ensembles and is therefore of conceptual inter-
est. On the practical side, this method advantageously yields all normalizations, particularly the function C(Nf)
n
(M)
and the partition function Z(Nf)
n
(M), in a very direct and convenient way. We consider the integral
X(K)
N
(a) =
Z
d[W] exp(−αtr WW †)
K
Y
f=1
det
 −iaf
W
W †
−iaf

(17)
depending on K parameters af (f = 1, . . . , K). For α = NΣ2, K = Nf, and af = Mf, the integral (17) is just the
partition function (4). For N = n, K = Nf + 1, af = Mf (f = 1, . . . , Nf), and a2
Nf+1 = −x, the integral (17) is,
up to the group volumes, equal to Z(Nf)
n
(M)p(Nf)
n
(x, M) as deﬁned in Eq. (12). Thus, the function X(K)
N
(a) yields
all desired quantities. We deﬁne K 2N-component vectors ζf (f = 1, . . . , K) with complex Grassmannian entries ζfi
(i = 1, . . . , 2N) as well as the 2NK-component combination ζ = (ζ1, . . . , ζK)T . The determinants in the integrand of
Eq. (17) are represented as the integral
K
Y
f=1
det
 −iaf
W
W †
−iaf

= (2π)2NK
Z
d[ζ] exp

ζ†

11K ⊗
 0
W
W †
0

−ia ⊗112N

ζ

(18)
with a = diag(a1, . . . , aK). In this form, the Gaussian average over the matrices W can easily be performed. We
arrive at a four-fermion interaction which is then decoupled by a Hubbard-Stratonovitch transformation. In Ref. [24],
a very similar route was taken. In this study, however, a problem involving fermionic and bosonic determinants was
solved which led to the introduction of supervectors of commuting and anticommuting variables. In the present case,
the vectors ζf have only anticommuting entries. Fortunately, this diﬀerence has little inﬂuence on the structure of
the results. Instead of the supermatrices which were used in Ref. [24] for the Hubbard-Stratonovitch transformation,
we have to employ ordinary matrices here. We arrive at
X(K)
N
(a) =
α
π
K2 Z
d[σ] exp
 −αtr (σ −a)(σ† −a)

detNσσ† ,
(19)
where σ is an ordinary complex K×K matrix without further symmetries. Thus, we have mapped the original model of
Sec. II A in the form (17) in the space of the N ×N matrices W onto a dual model in the space of the K×K matrices σ.
This is highly convenient because, eventually, we wish to take the limit N →∞. Remarkably, these dual models diﬀer
with respect to rotation invariance. The model of Sec. II A is invariant under rotations in the sense that the integrand
of the partition functions in Eqs. (4) and (6) depends only on the radial coordinates of the matrices W, i.e., on the
variables xi. This is not true for the model (19). The presence of the matrices a breaks this kind of rotation invariance.
In Refs. [25] and [24], a procedure was developed to deal with models precisely of this kind. We introduce radial
coordinates by σ = us¯v with u ∈U(K), ¯v ∈U(K)/UK(1), and s = diag(s1, . . . , sK). Again, the radial coordinates
sf are restricted to the positive real axis. The measure transforms as d[σ] = ∆2
K(s2) QK
f=1 sfd[s]dµ(u)dµ(¯v). The
integral over the unitary groups is now nontrivial. The solution can be found in Ref. [25],
α
π
K2 Z
dµ(u)
Z
dµ(¯v) exp
 −αtr (us¯v −a)(¯v†su† −a)

=
1
K!
det [γ(sf, af ′)]f,f ′=1,...,K
∆K(s2)∆K(a2)
.
(20)
The entries of the determinant are given by
γ(sf, af ′) = 2α exp
 −α(s2
f + a2
f ′)

I0(2αsfaf ′) ,
(21)
where I0 is the modiﬁed Bessel function of the ﬁrst kind and zeroth order. Collecting everything, we obtain
X(K)
N
(a) =
1
K!
1
∆K(a2)
K
Y
f=1
Z ∞
0
dsf s2N+1
f
∆K(s2) det [γ(sf, af ′)]f,f ′=1,...,K .
(22)
This integral can be solved in a straightforward way. We write ∆K(s2) = det[s2(f ′−1)
f
]f,f ′=1,...,K and integrate this
determinant row by row. Using the representation
5
2α
Z ∞
0
dw w2n+2m+1 exp
 −α(z2 + w2)

I0(2αwz) = (n + m)!
αn+m
L(0)
n+m(−αz2)
(23)
for the Laguerre polynomials, we ﬁnd
X(K)
N
(a) =
1
∆K(a2)
K−1
Y
f=0
(N + f)!
αN+f
det
h
L(0)
N+f−1(−αa2
f ′)
i
f,f ′=1,...,K .
(24)
This result immediately yields the orthogonal polynomials p(Nf)
n
(x, M) and the partition function Z(Nf)
N
(M).
