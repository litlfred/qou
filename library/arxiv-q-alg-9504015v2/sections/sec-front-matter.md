---
doc_id: arxiv-q-alg-9504015v2
doc_title: "arXiv:q-alg/9504015v2 24 Apr 1995"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-32
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
toc_source: inferred
---
arXiv:q-alg/9504015v2  24 Apr 1995
UMTG-183-95
q-alg/9504015
Witten’s Invariants of Rational Homology Spheres at Prime
Values of K and Trivial Connection Contribution.
L. Rozansky1
Physics Department, University of Miami
P. O. Box 248046, Coral Gables, FL 33124, U.S.A.
E-mail address: rozansky@phyvax.ir.miami.edu
Abstract
We establish a relation between the coeﬃcients of asymptotic expansion of
the trivial connection contribution to Witten’s invariant of rational homology
spheres and the invariants that T. Ohtsuki extracted from Witten’s invariant
at prime values of K. We also rederive the properties of prime K invariants
discovered by H. Murakami and T. Ohtsuki. We do this by using the bounds
on Taylor series expansion of the Jones polynomial of algebraically split links,
studied in our previous paper. These bounds are enough to prove that Ohtsuki’s
invariants are of ﬁnite type. The relation between Ohtsuki’s invariants and trivial
connection contribution is veriﬁed explicitly for lens spaces and Seifert manifolds.
1Work supported by the National Science Foundation under Grant No. PHY-92 09978.
1
Introduction
Witten’s invariant of 3d manifolds deﬁned in [1] by a path integral over the SU(2) connections
Aµ on a 3d manifold M
Z(M; k) =
Z
[DAµ]e
ik
2π SCS[Aµ],
(1.1)
SCS = 1
2 Tr ǫµνρ
Z
M d3x

Aµ∂νAρ + 2
3AµAνAρ

(1.2)
(k ∈ZZ, Tr is the trace taken in the fundamental representation of SU(2)) can also be
calculated combinatorially with the help of the surgery formula. Let M be a 3d manifold
constructed by (pj, 1) surgeries on the components Lj of an N-component link L in S3. A
(p, 1) surgery means that the meridian of the tubular neighborhood is glued to the parallel
plus p meridians on the boundary of the knot complement (in other words, a Dehn’s surgery
is performed on a knot with framing number p). The invariant of M can be expressed in
terms of the framing independent colored Jones polynomial Jα1,...,αN(L; k) of the link L:
Z(M; k)
Z(S3; k) =
 2
K
 N
2 exp

3
4πi
 2
K −1
 N
X
j=1
sign (pj)


(1.3)
×
X
0≤αj ≤K−1
(1≤j≤N)
Jα1,...,αN(L; k) exp

iπ
2K
N
X
j=1
pj(α2
j −1)


N
Y
j=1
sin
 π
K αj

,
Z(S3; k) =
s
2
K sin π
K ,
K = k + 2.
(1.4)
The Jones polynomial Jα1,...,αN(L; k) is normalized in such a way that it is multiplicative for
unlinked links and J(empty link; k) = 1, Jα(unknot; k) =
sin( π
K α)
sin( π
K) .
Although N. Reshetikhin and V. Turaev proved [2] that eq. (1.3) indeed deﬁnes an in-
variant of M (i.e. the l.h.s. of eq. (1.3) is invariant under Kirby moves), the topological
origin of this invariant remains somewhat obscure. The question is: which of the “classical”
topological invariants of M are contained inside Z(M; k)? Two distinct approaches to this
problem have been tried. The ﬁrst one is to study Z(M; k) for some particular values of
K. R. Kirby and P. Melvin discovered [3] that if K is odd, then Z(M; k) is proportional to
1
Z(M; 1):
Z(M; k)
Z(S3; k) = Z′(M; k) ×





Z(M;1)
Z(S3;1),
if K = −1 (mod 4)
Z(M;1)
Z(S3;1),
if K = 1 (mod 4),
(1.5)
If M is a rational homology sphere (ZZHS ), then Z(M; 1) = Z(S3; 1) so that Z′(M; k) =
Z(M;k)
Z(S3;k).
The new invariant Z′(M; k) can be calculated by the following surgery formula
Z′(M; k) = K−N
2 exp

−πi
4

3 + κ −6
K
 N
X
j=1
sign (pj)


(1.6)
×
X′
−K≤αj ≤K
αj∈2ZZ+1
(1≤j≤N)
Jα1,...,αN(L; k) exp

iπ
2K
N
X
j=1
pj(α2
j −1)


N
Y
j=1
sin
 π
K αj

,
here
κ =





1
if K = −1 (mod 4)
−1
if K = 1 (mod 4),
(1.7)
while
P′ means that we add an extra factor of 1
2 to the terms corresponding to the boundary
values of summation index (αj = ±K in this case). We changed slightly the original formula
of [3]: instead of taking a sum over 1 ≤αj ≤K−1
2
we sum over odd αj between 1 and K −1.
This allows us to get rid of some phase factors. We also double the range of summation to
1 −K ≤αj ≤K −1 by using the fact that Jα1,...,αN(L; k) is an odd function of its indices
(we use the 2K periodicity in αj in order to extend Jα1,...,αN(L; k) to negative values of αj).
Note that the whole summand of eq. (1.6) has a periodicity of 2K.
S. Garoufalidis [4] used nice properties of the gaussian sum PK−1
α=0 exp

2πi
K α2
for prime
values of K in order to study Witten’s invariant of lens spaces and Seifert manifolds. H. Mu-
rakami and T. Ohtsuki [5]–[8] carried out a detailed study of the invariant Z′(M; k) of
rational homology spheres (RHS ) for prime K.
Theorem 1.1 (H. Murakami, [5], [6]) For a RHS M and a prime K > 2
Z′(M; k) ∈ZZ[ˇq],
ˇq = e
2πi
K ,
(1.8)
ZZ[ˇq] being a cyclotomic ring.
2
We need more notations in order to present the results of Ohtsuki’s papers [7], [8]. We
introduce a new variable
x = q −1.
(1.9)
A polynomial from ZZ[ˇq] can be reexpressed as a polynomial in x with integer coeﬃcients. It
is deﬁned modulo the polynomial
(1 + x)K −1
x
=
K−1
X
n=0
K(K −1) · · ·(K −n)
(n + 1)!
xn,
(1.10)
which is identically equal to zero for x = e
2πi
K −1. All the coeﬃcients of this polynomial
except the one at xK−1, are divisible by K. As a result, all the coeﬃcients at xn, n ≤K−2 for
a polynomial of x coming from ZZ[ˇq] are well deﬁned modulo K. We will limit our attention
to the powers of x up to x
K−1
2 . They are all well deﬁned as elements of ZZK if K ≥3. Thus
there is a homomorphism of rings:
⋄:
ZZ[ˇq] →ZZ′
K[x] def.
= ZZK[x]/x
K+1
2 ZZK[x].
(1.11)
There is another homomorphism from polynomials (of maybe inﬁnite degree) of x with
rational coeﬃcients to ZZ′
K[x]:
∨: Q[[x]] →ZZ′
K[x].
(1.12)
The action of the operation ∨on rational numbers was introduced in relation to Witten’s
invariants at prime values of K by S. Garoufalidis [4]:
∨: Q →ZZK,
 p
q
!∨
= pq∗,
(1.13)
here q∗is the inverse of q modulo K: qq∗= 1 (mod K). The homomorphism ∨acts on
polynomials (inﬁnite series) by removing all powers of x higher than K−1
2
and converting the
remaining coeﬃcients to ZZK.
Now we can present (a slightly stronger version of) Ohtsuki’s results:
3
Theorem 1.2 (T. Ohtsuki [7], [8]) For any RHS M there exists a sequence of rational
numbers λn(M) ∈ZZ
h
1
2, 1
3, . . . , 1
2n,
1
|H1(M,ZZ)|
i
⊂Q, n ≥0 so that for any prime number K
such that |H1(M, ZZ)|̸ = 0 (mod K)
"
|H1(M, ZZ)|
 |H1(M, ZZ)|
K
!
Z′(M; k)
#⋄
=
" ∞
X
n=0
λn(M)xn
#∨
,
(1.14)
here

·
K

is the Legendre symbol.
We have slightly modiﬁed the theorem of
[8]: Ohtsuki required that K > |H1(M, ZZ)|,
he estimated that λn(M) ∈ZZ
h
1
2, 1
3, . . . ,
1
2n+1,
1
|H1(M,ZZ)|
i
⊂Q, n > 0 and he used ZZ′
K[x] =
ZZK[x]/x
K−1
2 ZZ[x] instead of (1.11) (in other words, he did not ﬁx the coeﬃcient at x
K−1
2 ).
Murakami showed that
λ0 = 1,
λ1 = λCW,
(1.15)
here λCW is the Casson-Walker invariant of RHS .
The second approach to the search of the topological meaning of Witten’s invariant
Z(M; k) is based on the path integral representation (1.1).
According to quantum ﬁeld
theory, this integral can be calculated by stationary phase approximation when K →∞.
The invariant is presented as a sum of contributions coming from connected components c
of the moduli space of ﬂat connections on the manifold M:
Z(M; k) =
X
c
Z(c)(M; k).
(1.16)
Each contribution has a general form
Z(c)(M; k) =
 4π2
K
! Nzero
2
1
Vol(Hc) exp
"
2πikS(c)
CS +
∞
X
n=0
S(c)
n (M)
iπ
K
n#
,
(1.17)
here Hc is the isotropy group, Nzero = dim H0
c −dim H1
c , H0,1
c
being the cohomologies of
0,1-forms taking values in the adjoint su(2) bundle, S(c)
CS is the Chern-Simons action and
P∞
n=0 S(c)
n (M)

iπ
K
n is an asymptotic series. The coeﬃcients S(c)
n (M) are called (n + 1)-loop
corrections. They might be related to “classical” topological invariants of M. Indeed, the
1-loop correction S(c)
0
is related to the Reidemeister-Ray-Singer torsion. An attempt to relate
4
the asymptotic properties of the surgery formula (1.3) for lens spaces and Seifert manifolds
to the quantum ﬁeld theory predictions of eqs. (1.16), (1.17) was initiated by D. Freed and
R. Gompf [9] and carried out further by L. Jeﬀrey [10], S. Garoufalidis [4] and also in the
papers [11, 12]. A complete agreement between the surgery formula and 1-loop predictions
was observed.
If the manifold M is a RHS , then the trivial connection is a separate point in the moduli
space of ﬂat connections. According to quantum ﬁeld theory, its contribution is of the form
Z(tr)(M; k) =
√
2π
K
3
2|H1(M, ZZ)|
3
2 exp
" ∞
X
n=1
Sn(M)
iπ
K
n#
.
(1.18)
A representation of the coeﬃcients Sn(M) in terms of (n + 1)-loop Feynman diagrams was
carried out by S. Axelrod and I. Singer [13], M. Kontsevich [14], C. Taubes [15] and others.
We studied how the trivial connection contribution can be extracted from the surgery for-
mula (1.3). We derived a knot surgery formula [16] and a link surgery formula [17] for it.
The knot formula allowed us to show that
S1(M) = 6λCW.
(1.19)
The link surgery formula of [17] was much less explicit than the knot formula of [16],
because it did not express Z(tr)(M; k) directly in terms of derivatives of the Jones polynomial
Jα1,...,αN(L; k). However we derived an explicit surgery formula [18] for algebraically split
links (ASL ).
In this paper we are going to prove the following:
Proposition 1.1 Ohtsuki’s invariants λn(M) of eq. (1.14) and loop corrections to the trivial
connection contribution Sn(M) of eq. (1.18) can be expressed in terms of each other through
the following relation
∞
X
n=0
λn(M)xn = exp
" ∞
X
n=1
(Sn(M) −Sn(S3))
iπ
K
n#
≡

π
K

sin

π
K
 exp
" ∞
X
n=1
Sn(M)
iπ
K
n#
(1.20)
by substituting either
x = e
2πi
K −1 = 2πi
K
∞
X
n=0
1
(n + 1)!
2πi
K
n
,
(1.21)
5
or
iπ
K = 1
2 log(1 + x) = x
2
∞
X
n=0
(−1)n xn
n + 1.
(1.22)
In other words, we will show that
"
|H1(M, ZZ)|
 |H1(M, ZZ)|
K
!
Z′(M; k)
#⋄
=
"
|H1(M, ZZ)|
3
2 Z(tr)(M; k)
Z(S3; k)
#∨
.
(1.23)
In process of doing this we will rederive the results of [5]-[8] maybe in a somewhat more
explicit way.
Our proof of the Proposition 1.1 will be based on the following two propositions derived
in [19] and [18] by using some “physical” considerations:
Proposition 1.2 Let L be an algebraically split link (ASL ) in S3.
Then its framing-
independent colored Jones polynomial has the following Taylor series expansion in powers of
K:
Jα1,...,αN(L; k) =


N
Y
j=1
αj


∞
X
n=0
X
m≤3
4n
Dm,n(α1, . . . , αN)
iπ
K
n
,
(1.24)
here Dm,n(α1, . . . , αN) are even homogeneous polynomials of degree 2m:
Dm,n(α1, . . . , αN) =
X
m1,...,mN ≥0
m1+···+mN =m
D(m,n)
m1,...,mNα2m1
1
· · · α2mN
N
(1.25)
and
mj ≤n −m,
1 ≤j ≤N.
(1.26)
Proposition 1.3 Let M be a rational homology sphere (RHS ) constructed by (pj, 1) surg-
eries on the components of an N-component link L in S3. Then the loop corrections to the
trivial connection contribution (1.18) to Witten’s invariant of M are given by the formula:
exp
" ∞
X
n=1
(Sn(M) −Sn(S3))
iπ
K
n#
(1.27)
= exp

3
4πi
 2
K −1
 N
X
j=1
sign (pj)

exp

−iπ
2K
N
X
j=1
 
pj + 1
pj
!

iN
(2K)
N
2

N
Y
j=1
pj

3
2
×
+∞
Z
−∞
[αj =0]
dα1 · · · dαN exp

iπ
2K
N
X
j=1
pjα2
j

Jα1+ 1
p1 ,...,αN+
1
pN (L; k).
6
The symbol
+∞
R
−∞
[αj=0]
means that the integral has to be calculated in the following way: ﬁrst, an
expansion (1.24) has to be substituted and then the gaussian integrals over αj have to be
calculated for each polynomial
QN
j=1

αj + 1
pj

Dm,n

α1 + 1
p1, . . . , αN +
1
pN

separately (for
more details see [18]).
The Proposition 1.2 is essential for all our calculations. The Proposition 1.4 is needed only
for the derivation of eq. (1.23). In other words, we could use eq. (1.27) as a deﬁnition of
Sn(M) and then prove eq. (1.20) which amounts to proving the Theorem 1.2.
In Section 2 we modify the surgery formula (1.6) and prove the Theorem 1.1. Our main
tool is the observation that the gaussian sum PK−1
α=0 ˇqα2 is proportional to x
K−1
2 , while the
sum PK−1
α=0 ˇqα2α2m for m ≤K−1
2
is only proportional to x
K−1
2
−m. This is similar to the be-
havior of gaussian integrals: each two extra powers of α in the integral
R +∞
−∞e
2πi
K α2α2m dα
bring a power of K to denominator. In Section 3 we prove the Proposition 1.1 and thus
also the Theorem 1.2. We use again the similarities of the formulas for
PK−1
α=0 ˇqα2α2m and
R +∞
−∞e
2πi
K α2α2m dα. These similarities are due to the fact that both the sum PK−1
α=0 ˇqα2+2nα
and the integral
R +∞
−∞e
2πi
K (α2+2nα) dα can be calculated by completing the square in the ex-
ponents. In Section 4 we derive a rational surgery formula for Z′(M; k) which is similar to
the formula (4.1) of [10] for the original Witten’s invariant Z(M; k). We use this formula to
verify the Proposition 1.1 for lens spaces and Seifert manifolds which are rational homology
spheres. In Section 5 we discuss the properties of Ohtsuki’s invariants λn(M) as related to
the properties of invariants Sn(M) studied in [18].
2
Gaussian Sums and Divisibility in Cyclotomic Ring
We start by modifying the surgery formula (1.6). Since 1
4(α2
j −1) ∈ZZ, then
exp

iπ
2K
N
X
j=1
pj(α2
j −1)

= ˇq
1
4
PN
j=1 pj(α2
j−1) = ˇq4∗PN
j=1 pj(α2
j−1).
(2.1)
7
Also since 1
2(αj ± sign (pj)) ∈ZZ,
sin
 π
K αj

= i
2
X
µj=±1
µje−iπ
K µjαj = i
2
X
µj=±1
µjˇq−2∗µjαj ˇq(2∗−1
2) sign(pj).
(2.2)
The Jones polynomial Jα1,...,αN(L; k) is odd and e
iπ
2K pjα2
j is even as a function of αj.
Therefore we can drop the factor 1
2 and put µj = 1 in eq. (2.2) upon substituting it into
eq. (1.6):
Z′(M; k) = K−N
2 iNe−iπ
4 (3+κ)PN
j=1 sign(pj)ˇq( 1
4+2∗)PN
j=1 sign(pj)ˇq−4∗PN
j=1 pj
(2.3)
×
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq
PN
j=1(4∗pjα2
j−2∗αj)Jα1,...,αN(L; k).
After completing the square
4∗pjα2
j −2∗αj = 4∗pj(αj −p∗
j)2 −4∗p∗
j (mod K),
(2.4)
we shift the summation variable αj by p∗
j (we assume that p∗
j is even in order to preserve the
parity of αj, we can always make such choice of p∗
j since K is odd). Then
Z′(M; k) = K−N
2 iNe−iπ
4 (3+κ)PN
j=1 sign(pj)ˇq( 1
4+2∗)PN
j=1 sign(pj)ˇq−4∗PN
j=1(pj+p∗
j)
(2.5)
×
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
jJα1+p∗
1,...,αN+p∗
N(L; k).
Next we use the identities
ie−iπ
2 sign(pj) = sign (pj) ,
(2.6)
1 −κK
4
= 4∗
(2.7)
in order to rearrange the phase factors preceding the sum in eq. (2.5):
Z′(M; k) = K−N
2 e
iπ
4 (κ−1) PN
j=1 sign(pj)


N
Y
j=1
sign (pj)

ˇq4∗PN
j=1(3 sign(pj)−pj−p∗
j )
×
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
jJα1+p∗
1,...,αN+p∗
N(L; k).
(2.8)
8
Since the values of the Jones polynomial Jα1,...,αN(L; k) belong to the cyclotomic ring
ZZ[ˇq] when all the indices αj are odd, we can apply to it a combination of Proposition 1.2
and Lemma 2.3 of [5]:
Proposition 2.1 For odd values of its indices αj, the unframed colored Jones polynomial
of an N-component ASL L in S3 can be presented as the following sum:
Jα1,...,αN(L; k) =


N
Y
j=1
αj


(N+1) K−1
2
X
n=0
X
m≤3
4n
˜Dm,n(α1, . . . , αN)xn
(2.9)
+x(N+1) K−1
2
+1J(res)
α1,...,αN(L; k),
J(res)
α1,...,αN(L; k) ∈ZZ[ˇq],
here ˜Dm,n(α1, . . . , αN) are homogeneous polynomials of degree 2m:
˜Dm,n(α1, . . . , αN) =
X
m1,...,mN ≥0
m1+···+mN =m
˜D(m,n)
m1,...,mNα2m1
1
· · · α2mN
N
,
(2.10)
mj ≤n −m,
(2.11)
and the polynomials
QN
j=1 αj
 P
m≤3
4n ˜Dm,n(α1, . . . , αN) take integer values when αj are odd.
The latter property of the polynomials ˜Dm,n allows us to express them in terms of “binomial
coeﬃcient” polynomials:


N
Y
j=1
αj

X
m≤3
4 n
˜Dm,n(α1, . . . , αN) =
X
1≤mj ≤2 ¯
mj +1
(1≤j≤N)
C(n)
m1,...,mNPm1
α1 −1
2

· · · PmN
αN −1
2

,
C(n)
m1,...,mN ∈ZZ,
(2.12)
here
Pm(α) = α(α −1) · · ·(α −m + 1)
m!
(2.13)
and ¯mj are the maximum values of mj in the representation (2.10) of all the polynomials
˜Dm,n appearing in the l.h.s. of eq. (2.12).
The following proposition is a reﬂection of the inequality (2.11) for the representa-
tion (2.12):
9
Proposition 2.2 There is an upper bound on the indices of the coeﬃcients C(n)
m1,...,mN of
eq. (2.12):
mj
2

≤n −
N
X
i=1
mi
2

,
(2.14)
here
h
m
2
i
denotes the integer part of m
2 .
The proof is completely similar to that of the Proposition 3.4 of [18]. Suppose that there is
a coeﬃcient C(n)
m1,...,mN for which (2.14) is not true, say, for m1. If all indices mj of C(n)
m1,...,mN
are odd, then the highest degree monomial of the corresponding polynomial
C(n)
m1,...,mNPm1
α1 −1
2

· · · PmN
αN −1
2

(2.15)
violates the inequality (2.11). Therefore it has to be canceled by monomials of other poly-
nomials
C(n)
m′
1,...,m′
NPm′
1
α1 −1
2

· · · Pm′
N
αN −1
2

(2.16)
for which
m′
j ≥mj, 1 ≤j ≤N,
N
X
j=1
m′
j >
N
X
j=1
mj.
(2.17)
If some mj are even, then the highest degree monomial of the polynomial (2.15) is incom-
patible with the structure of the l.h.s. of eq. (2.12) and it also has to be canceled. The
inequalities (2.17) show that the index m1 of the polynomials (2.15) again violates (2.14), so
we need to go to higher values of PN
j=1 mj for further cancelation. Since PN
j=1 mj ≤n, this
process can not be completed. This contradiction proves the proposition.
Now we begin to prove the Theorem 1.1. Following [5], we use the relations
K−1
X
α=0
ˇqα2 = ei π
4 (1−κ)√
K,
(2.18)
K−1
X
α=0
ˇqα2 = x
K−1
2 u−1,
u, u−1 ∈ZZ[ˇq]
(2.19)
in order to present K−N
2 in the following form:
K−N
2 = ei π
4 N(1−κ)
uN
xN K−1
2 .
(2.20)
10
Substituting this expression into eq. (2.8) we ﬁnd that
Z′(M; k) = e
iπ
4 (κ−1)PN
j=1(sign(pj)−1)


N
Y
j=1
sign (pj)

ˇq4∗PN
j=1(3 sign(pj)−pj−p∗
j)
×
uN
xN K−1
2
X′
−K≤αj ≤K
αj∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
jJα1+p∗
1,...,αN+p∗
N(L; k).
(2.21)
Since 1
4(κ −1)(sign (pj) −1) ∈ZZ, we conclude that to prove Theorem 1.1 it is enough to
show that
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
jJα1+p∗
1,...,αN+p∗
N(L; k) = xN K−1
2 w,
w ∈ZZ[ˇq].
(2.22)
We will substitute the expansion (2.9) and check the property (2.22) for every polynomial
QN
j=1 αj
 P
m≤3
4n ˜Dm,n(α1, . . . , αN) separately. The remainder term x(N+1) K−1
2 J(res)
α1,...,αN(L; k)
obviously satisﬁes eq. (2.22). Moreover, for some w ∈ZZ[ˇq],


1
xN K−1
2
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
jJ(res)
α1,...,αN(L; k) x(N+1) K−1
2
+1


⋄
=
h
x
K+1
2 w
i⋄= 0,
(2.23)
so that we can neglect the contribution of this term in all further calculations.
To estimate the contribution of a polynomial
QN
j=1 αj
 P
m≤3
4 n ˜Dm,n(α1, . . . , αN) xn we
need the following simple lemma:
Lemma 2.1 For p, m ∈ZZ, m ≥0
X′
−K≤α≤K
α∈2ZZ+1
ˇqpα2α2m = xmax{0, K−1
2
−m}w,
w ∈ZZ[ˇq].
(2.24)
The lemma needs a proof only for m < K−1
2 . To prove that an element u ∈ZZ[ˇq] is divisible
by xn, n ≤K −1 one may present it as an integer coeﬃcient polynomial of x and check
that the coeﬃcients in front of all xn′, n′ < n are divisible by K. We substitute ˇq = x + 1 in
eq. (2.24) and express the powers of ˇq in terms of “binomial” polynomials
X′
−K≤α≤K
α∈2ZZ+1
ˇqpα2α2m =
X
n≥0
X′
−K≤α≤K
α∈2ZZ+1
Pn(pα2)α2mxn =
X
n≥0
X
0≤m′≤n
X′
−K≤α≤K
α∈2ZZ+1
Cn,m′
n! p2m′α2(m+m′)xn,(2.25)
11
here
α(α −1) · · ·(α −n + 1) =
X
m′≤n
Cn,m′αm′,
Cn,m′ ∈ZZ.
(2.26)
It is well known in number theory that
X′
−K≤α≤K
α∈2ZZ+1
α2m = 0 (mod K)
for
0 ≤m < K −2.
(2.27)
Therefore the numerator of the contribution of a term
Cn,m′
n! p2m′α2(m+m′)xn will be divisible
by K for all m + m′ < K−1
2
≤K −2, that is, for all n < K−1
2
−m. The denominator n! is
harmless, because since n < K, it is not divisible by K and can not cancel the factors of K
coming from the sum over α. This proves the lemma.
This lemma can be easily generalized to the “binomial” polynomials (2.13):
Lemma 2.2 For p, p′, m ∈ZZ, p′ ∈2ZZ, m ≥0
X′
−K≤α≤K
α∈2ZZ+1
ˇqpα2Pm
 α + p′ −1
2
!
= xmax{0, K−1
2
−[ m
2 ]} w,
w ∈ZZ[ˇq].
(2.28)
The proof is similar to that of the previous lemma. The choice of summation range for α
obviates the fact that odd powers of α in Pm

α+p′−1
2

can be ignored. The numerators of
the contributions of even powers of α are divisible by K. The coeﬃcients of Pm have a
denominator m!, but we may assume that m < K −1 (otherwise eq. (2.28) is obvious) so
that the denominator does not cancel the factors of K.
Let ¯m(n) be the maximum value of m appearing in the l.h.s. of eq. (2.12). Then for every
coeﬃcient C(n)
m1,...,mN from the r.h.s. of that equation
m1 + · · · + mN ≤¯m(n).
(2.29)
Therefore we can combine eqs. (2.12) and (2.28) into the following estimate of the contribu-
tion of polynomials ˜Dm,n to the sum (2.22):
X′
−K≤α≤K
α∈2ZZ+1
ˇq4∗PN
j=1 pjα2
j


N
Y
j=1

αj + p∗
j


X
m≤3
4n
˜Dm,n(α1 + p∗
1, . . . , αN + p∗
N) xn
= xN K−1
2
+n−¯m(n) w,
w ∈ZZ[ˇq]. (2.30)
12
Since ¯m(n) ≤3
4n ≤n, this estimate is enough to prove eq. (2.22) and also the Theorem 1.1.
Note that the proof required only a weaker bound m ≤n for ˜Dm,n rather than a stronger
bound m ≤3
4n of [18]. However the bound m ≤3
4n is necessary to prove that only a ﬁnite
number of polynomials ˜Dm,n contribute to the coeﬃcients of xn′, n′ ≤K−1
2
in the expansion
of [Z′(M; k)]⋄. Indeed, since ¯m(n) ≤3
4n, then n −¯m(n) ≥1
4n and eq. (2.30) suggests that
we may limit our attention to only those polynomials (2.15) for which
n ≤2(K −1).
(2.31)
3
Gaussian Sums and Integrals
We are going to derive a surgery formula for [Z′(M; k)]⋄which would express it in terms
of the derivatives ˜Dm,n of the colored Jones polynomial.
As we will see, this requires a
calculation of the gaussian sum
G(p, q; m) = ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇqq∗pα2α2mxm,
m ≤K −1
2
.
(3.1)
More precisely, we need to ﬁnd only [G(p, q; m)]⋄. We already know that G(p, q; m) ∈ZZ[ˇq].
Proposition 3.1 The sum of eq. (3.1) is related to the gaussian integral. For p, q ∈ZZ,
p, q̸ = 0 (mod K), 0 ≤m ≤K−1
2 ,
[G(p, q; m)]⋄=
pq∗
K
 
e−i π
4 sign(
p
q)
 2
K
 1
2

p
q

1
2 Z +∞
−∞dα e
2πi
K
p
q α2α2m xm


∨
(3.2)
+x
K+1
2
−mw, w ∈ZZ[ˇq].
To prove the proposition we calculate the following sum:
ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗α2 ˇq2nα = ei π
4 (κ−1)
√
K
ˇq−p∗qn2
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗(α+np∗q)2.
(3.3)
13
Since (for p∗∈ZZ)
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗(α+np∗q)2 =
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗α2 =
X
3−K
2
<˜α≤K−1
2
ˇqpq∗(2˜α+1)2
=
X
3−K
2
<˜α≤K−1
2
ˇq4pq∗(˜α+2∗)2 =
√
Kei π
4 (1−κ)
pq∗
K

,
(3.4)
we ﬁnd that
ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇqpq∗α2 ˇq2nα =
pq∗
K

ˇq−p∗qn2.
(3.5)
We substitute ˇq = 1 + x in ˇq2nα and ˇq−p∗qn2.
After going from ZZ[ˇq] to the factor-ring
ZZ′
K[x] = ZZK[x]/x
K+1
2 ZZK[x] and using the “checked binomial polynomial”
P ∨
m(α) = (m!)∗α(α −1) · · ·(α −m + 1) = (m!)∗
m
X
l=0
Cm,lαl,
(3.6)
we ﬁnd that


K−1
X
m=0
[ m
2 ]
X
l=0
(m!)∗Cm,2lG(p, q; l)4ln2lxm−l


⋄
=
pq∗
K



K−1
2
X
m=0
xm
m
X
l=0
(m!)∗Cm,l(−1)l(p∗q)ln2l


⋄
(3.7)
We limited the sum over m in the l.h.s. of this equation to m ≤K −1 because for m ≥K
the minimum power of xm−l is greater that K−1
2 . Note that since m ≤K −1, then (m!)∗is
well deﬁned.
If we substitute the expansion
[G(p, q; l)]⋄=
K−1
2
−l
X
m=0
Gm(p, q; l) xm + x
K+1
2
−lw,
w ∈ZZ[ˇq]
(3.8)
into eq. (3.7), then we can ﬁnd all the coeﬃcients Gm(p, q; l) by equating the coeﬃcients of
l.h.s. and r.h.s. of eq. (3.7) at equal powers of x and n. These coeﬃcients have to be equal
due to the following simple lemma:
Lemma 3.1 If a degree of a polynomial P(n) ∈ZZK[n] is less than K and P(n) = 0 for all
n ∈ZZK, then all the coeﬃcients of P(n) are zero modulo K.
14
The proof follows from the fact that the K × K Van-der-Monde determinant in ZZK is
non-zero.
Each gaussian sum G(p, q; l) appears in the l.h.s. of eq. (3.7) with its own power of n:
n2l. Therefore the coeﬃcients Gm′(p, q; l) of eq. (3.8) can be calculated by “dividing” the
polynomial (−1)l(p∗q)l P K−1
2
m=l (m!)∗Cm,lxm appearing at n2l in the r.h.s. of eq. (3.7) by the
polynomial
PK−1
m=2l Cm,2l4lxm−l appearing in the r.h.s. of that equation at the same power
on n. The division is not quite well-deﬁned, hence the indeterminacy in the elements w of
eq. (3.8).
This whole calculation of dividing the polynomials can be made more explicit if we go
back to eq. (3.5) and make the following substitutions:
ˇq2nα = e2nα log(1+x) =
∞
X
l=0
(2nα)l
l!
(log(1 + x))l,
(3.9)
ˇq−pq∗n2 = e−pq∗n2 log(1+x) =
∞
X
l=0
(−1)l (pq∗n2)l
l!
(log(1 + x))l.
(3.10)
After “checking” the logarithm
log∨(1 + x) = x
K−2
X
n=0
(−1)n(n + 1)∗xn
(3.11)
we see that eq. (3.7) transforms into


K−1
2
X
l=0
G(p, q; l)(2n)2l((2l)!)∗(log∨(1 + x))l
 log∨(1 + x)
x
!l


⋄
(3.12)
=
pq∗
K



K−1
2
X
l=0
(−1)ln2l(pq∗)l(l!)∗(log∨(1 + x))l


⋄
.
Thus we ﬁnd that
[G(p, q; m)]⋄= (−1)m
pq∗
K

(2∗)2m(2m)!(m!)∗
" 
x
log∨(1 + x)
!m#⋄
+x
K+1
2
−mw,
w ∈ZZ[ˇq].
(3.13)
Consider now the following identity which is an integral analog of eq. (3.5):
Z +∞
−∞dα ˇq
p
q α2 ˇq2nα = ei π
4 sign( p
q)
K
2
 1
2 

q
p

1
2
ˇq−q
p n2.
(3.14)
15
After substituting eqs. (3.9), (3.10) we ﬁnd that
Z +∞
−∞dα ˇq
p
q α2α2mxm = ei π
4 sign( p
q)
K
2
 1
2 

q
p

1
2 (−1)m(2m)!
4mm!
 
x
log(1 + x)
!m
(3.15)
Eq. (3.2) follows from comparing eq. (3.15) to eq. (3.13).
The formula (3.2) can be generalized to the type of summands that appear in eq. (2.8)
after the substitutions (2.9) and (2.12).
Proposition 3.2 For p̸ = 0 (mod K), 0 ≤m ≤K


ei π
4 (κ−1)
√
K
X′
−K≤α≤K
α∈2ZZ+1
ˇq4∗pα2Pm
α −1 + p∗
2

x[ m
2 ]


⋄
(3.16)
=
 p
K
 
e−i π
4 sign(q)
 |p|
2K
! 1
2 Z +∞
−∞dα e
iπ
2K pα2Pm

α −1 + 1
p
2

x[ m
2 ]


⋄
+ x
K+1
2
−[ m
2 ]w,
w ∈ZZ[ˇq].
To prove the proposition for m < K we substitute P ∨
m(2∗(α −1 + p∗)) for Pm
 α−1+p∗
2

in the l.h.s. of this equation and then take the sum for each monomial of P ∨
m(2∗(α −1 + p∗))
separately. If m is odd then the highest power αm does not contribute to the sum, therefore
the factor x[ m
2 ] is enough to apply eq. (3.2). We also used the multiplicativity of Legendre
symbol and

4∗
K

= 1, since 4∗= (2∗)2.
The case of m = K requires a special care. We start with the l.h.s. of eq. (3.16). We can
use the symmetry of the summation range and gaussian exponent in order to substitute
P (ev)
K
(α) = 1
2

PK
α −1 + p∗
2

+ PK
−α −1 + p∗
2

(3.17)
instead of PK

α−1+p∗
2

. The even polynomial (3.17) takes integer values for odd α and its
degree is equal to K −1. Therefore the highest divisor of denominators of its coeﬃcients is
K −1 and we can apply all our previous results to the calculation of the contribution of its
monomials. Eq. (3.16) indicates that we need to determine only the terms of order x0, hence
we are interested only in the contribution of the highest degree monomial
p∗−K
2K (K −1)!α
K−1
2 ,
(3.18)
16
which is determined with the help of eq. (3.13). Consider now the r.h.s. of eq. (3.16). Again
we substitute the even polynomial
P (ev)
K
(α) = 1
2

PK

α −1 + 1
p
2

+ PK

−α −1 + 1
p
2



.
(3.19)
Some of its denominators may have K as a divisor, but according to eq. (3.16) we are
interested only in the contribution of the highest power of α:
1
p −K
2K (K −1)!α
K−1
2 .
(3.20)
Comparing it to monomial (3.18) and applying eq. (3.2) to their contributions we arrive at
eq. (3.16). This ends the proof of the Proposition 3.2.
Next we move to the polynomials ˜Dm,n which participate in the expansion eq. (2.9):
Proposition 3.3 The gaussian sums and integrals of polynomials ˜Dm,n are related by the
equation


ei π
4 N(κ−1)
K
N
2
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
j


N
Y
j=1

αj + p∗
j


X
m≤3
4n
˜Dm,n(α1 + p∗
1, . . . , αN + p∗
N) xn


⋄
=
 QN
j=1 pj
K
! 
e−i π
4
PN
j=1 sign(pj)(2K)−N
2

N
Y
j=1
pj

1
2
(3.21)
×
Z +∞
−∞dα e
iπ
2K
PN
j=1 pjα2
j


N
Y
j=1
 
αj + 1
pj
!
X
m≤3
4 n
˜Dm,n(α1 + 1
p1
, . . . , αN + 1
pN
)


⋄
.
To prove this proposition we rearrange the representation (2.12) in the following form:


N
Y
j=1
αj

X
m≤3
4 n
˜Dm,n(α1, . . . , αN) xn
(3.22)
= xn−PN
j=1[
mj
2 ]
X
1≤mj ≤2 ¯
mj +1
(1≤j≤N)
C(n)
m1,...,mNx[
m1
2 ]Pm1
α1 −1
2

· · · x[
mN
2 ]PmN
αN −1
2

.
We know from Lemma 2.2 that the contribution of each polynomial x[
mj
2 ]Pmj
αj−1
2

to the
l.h.s. of eq. (3.21) belongs to ZZ[ˇq]. Therefore the contribution of the whole expression (3.22)
17
starts at xn−PN
j=1[
mj
2 ]. Hence we may assume that
n −
N
X
j=1
mj
2

≤K −1
2
,
(3.23)
otherwise the contribution of the polynomial
xn−PN
j=1[
mj
2 ]C(n)
m1,...,mNx[
m1
2 ]Pm1
α1 −1
2

· · ·x[
mN
2 ]PmN
αN −1
2

.
(3.24)
is annihilated by the homomorphism ⋄.
The inequalities (2.14) and (3.23) mean that mj ≤K−1
2 , so we can apply the Proposi-
tion 3.2 to every polynomial x[
mj
2 ]Pmj
 αj−1
2

. The terms x
K+1
2
−[
mj
2 ]w of eq. (3.16) can be
neglected because

xn−PN
i=1[
mi
2 ] x
K+1
2
−[
mj
2 ] w
⋄
=

x
K+1
2
+(n−PN
i=1[
mi
2 ]−[
mj
2 ]) w
⋄
= 0
(3.25)
in view of the inequality (2.14). This proves the Proposition 3.2.
Now we can prove the Proposition 1.1. We substitute eq. (2.9) into eq. (2.5), apply the
homomorphism ⋄and retain only the relevant terms from the sum of eq. (2.9). Since the
contribution of the l.h.s. of eq. (3.22) starts at xn−PN
j=1[
mj
2 ] and
PN
j=1
hmj
2
i
≤m ≤3
4n, it is
enough to retain only the terms with n ≤2(K −1):
[Z′(M; k)]⋄=

ei π
4 (κ−1)PN
j=1(sign(pj)−1)


N
Y
j=1
sign (pj)

ˇq4∗PN
j=1(3 sign(pj)−pj−p∗
j ) ei π
4 N(κ−1)
K
N
2
×
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
ˇq4∗PN
j=1 pjα2
j


N
Y
j=1

αj + p∗
j



2(K−1)
X
n=0
X
m≤3
4n
˜Dm,n(α1 + p∗
1, . . . , αN + p∗
N)xn


⋄
=
 QN
j=1 pj
K
!
ei π
4 (κ−1)PN
j=1(sign(pj)−1)
(3.26)
×

e−i π
4
PN
j=1 sign(pj)


N
Y
j=1
sign (pj)

ˇq
1
4
PN
j=1(3 sign(pj)−pj−p∗
j )

QN
j=1 pj

1
2
(2K)
N
2
×
Z +∞
−∞dα1 · · ·dαN e
iπ
2K
PN
j=1 pjα2
j
×


N
Y
j=1
 
αj + 1
pj
!

2(K−1)
X
n=0
X
m≤3
4n
˜Dm,n(α1 + 1
p1
, . . . , αN + 1
pN
)xn


∨
.
18
Here we used an identity

ˇq4∗PN
j=1(3 sign(pj)−pj−p∗
j)
⋄
=

ˇq
1
4
PN
j=1(3 sign(pj)−pj−p∗
j)
∨
.
(3.27)
We can extend the sum over n in the r.h.s. of eq. (3.27) to all n ≥0 because the
contribution of ˜Dm,nxn with n > 2(K −1) starts above x
K−1
2 . As a result, we obtain the full
Jones polynomial. Now using the identities
ei π
4 (κ−1)(sign(p)−1)
 p
K

=
 |p|
K
!
,
(3.28)

N
Y
j=1
pj

 = |H1(M, ZZ)|
(3.29)
sign (p) = ie−i π
2 sign(p),
(3.30)
we get the following formula
[Z′(M; k)]⋄=
 |H1(M, ZZ)|
K
! 
e−3
4iπ PN
j=1 sign(pj)
iN
(2K)
N
2 e
iπ
2K
PN
j=1

sign(pj)−pj−1
pj
 

N
Y
j=1
pj

1
2
×
+∞
Z
−∞
[αj =0]
dα1 · · ·dαN e
iπ
2K
PN
j=1 pjα2
jJα1+ 1
p1 ,...,αN+
1
pN (L; k)


∨
(3.31)
Combining it with eqs. (1.27) and (1.18) and using eq. (3.29) again we easily arrive at
eq. (1.23). Note that eq. (3.29) guarantees that pj̸ = 0 (mod K) if |H1(M, ZZ)|̸ = 0 (mod K).
This proves the Proposition 1.1.
4
A General Rational Surgery Formula
Up until this point we were working only with surgeries of the type (p, 1). This was enough
to prove the theorems of Section 1, because H. Murakami and T. Ohtsuki showed [6] that any
RHS M can be constructed by (pj, 1) surgeries on an ASL in S3 up to a connected sum of
lens spaces Lp′
j,1, that is, instead of M one might end up with M#Lp′
1,1# . . . Lp′n,1. However
from the technical point of view it would be better to have a formula for the invariant
19
Z′(M; k) of a manifold constructed by general rational surgeries (pj, qj) on the components
of an N-component link L in S3.
The formula for Witten’s invariant Z(M; k) was derived by L. Jeﬀrey [10]
Z(M; k) = Z(S3; k) exp

iπ
4
K −2
K


N
X
j=1
Φ(U(pj,qj) −3 sign (L)




(4.1)
×
X
1≤α1,...,αN≤K−1
Jα1,...,αN(L; k)
N
Y
j=1
˜U
(pj,qj)
αj1
,
here L is the linking matrix of L, pj
qj being the self-linking numbers. The matrices
U(pj,qj) =

pj
rj
qj
sj

∈SL(2, ZZ)
(4.2)
describe the surgeries (a meridian on the tubular neighborhood is glued to pj(meridian) +
qj(parallel) of the link complement),
Φ

p
r
q
s

= p + s
q
−12s(p, q),
(4.3)
s(p, q) being the Dedekind sum, and
˜U(p,q)
αβ
= i sign (q)
q
2K|q|
e−i π
4 Φ(U(p,q))
q−1
X
n=0
X
µ=±1
µ
× exp
" iπ
2Kq(pα2 −2α(2Kn + µβ) + s(2Kn + µβ)2)
#
.
(4.4)
Let us introduce some notations. A rational (pj, qj) surgery on Lj can be presented as
a combination of (m(j)
t , 1), 1 ≤t ≤¯t(j) surgeries on a chain of unknots simply linked to Lj
(see e.g. [9], [10] and references therein) such that
U(pj,qj) = T
m(j)
¯t(j)ST
m(j)
¯t(j)−1S · · · T m(j)
1 S,
(4.5)
here
S =

0
−1
1
0

,
T =

1
1
0
1

.
(4.6)
20
We denote this chain (including Lj itself) as ˜Lj and all the chains of L as ˜L. For 1 ≤t ≤¯t(j)
we set
U(p(j)
t
,q(j)
t
) = T m(j)
t S · · · T m(j)
1 S,
(4.7)
so that p(j)
¯t(j) = pj, q(j)
¯t(j) = qj. From now on we assume for simplicity that none of the numbers
q(j)
t
is divisible by K. Then we are going to prove the following:
Proposition 4.1 Let M be a manifold constructed by (pj, qj) surgeries on an N-component
link L in S3. Then
Z′(M; k) =



QN
j=1 qj

K


QN
j=1 sign (qj)
K
N
2
e−i π
4 κ sign(L)e−iπ 3
4
K−2
K
sign(L)
×ˇq−4∗PN
j=1 Φ(U(pj,qj ))ˇq(2∗−1
2)PN
j=1 sign

pj
qj

(4.8)
×
X′
−K≤αj ≤K
αj ∈2ZZ+1
(1≤j≤N)
Jα1,...,αN(L; k) ˇq4∗PN
j=1 q∗
j (pjα2
j+sj)
N
Y
j=1

i
2
X
µj=±1
µjˇq−2∗q∗
j µjαj


We could use the general surgery formula (4.8) instead of the (pj, 1) surgery formula (1.6)
throughout the Sections 2 and 3 in order to produce a somewhat more ﬂexible proof of
Theorems 1.1, 1.2 and Proposition 1.1.
We begin the proof of the Proposition 4.1 by recalling the Kirby-Melvin formula [3] which
expresses Z′(M; k) in terms of data associated to ˜L:
Z′(M; k) = e
i π
4
K−2
K
hPN
j=1 Φ(U(pj ,qj))−3 sign(L)
i
e−i π
4 κ sign(˜L)
×
X′
−K≤αj ≤K
αj∈2ZZ+1
(1≤j≤N)
Jα1,...,αN(L; k)
N
Y
j=1
ˇU
(pj,qj)
αj1
,
(4.9)
here (we drop the index j in eq. (4.5) )
ˇU(p,q)
αβ
=
 ˇT m¯t ˇS ˇT m¯t−1 ˇS · · · ˇT m1 ˇS

αβ ,
(4.10)
ˇTαβ = e−i π
4 ˇq
1
4 α2δαβ,
ˇSαβ =
1
√
K sin
 π
K αβ

(4.11)
and ˜L is the linking matrix of the “expanded” link ˜L.
21
The following lemma presents an explicit expression for ˇU(p,q)
αβ , which is similar to that of
eq. (4.4):
Lemma 4.1
ˇU(p,p)
αβ
=
 |q|
K
! sign (q)
√
K
e−i π
4 Φ(U(p,q)) e
−i π
4 κP¯t−1
t=0 sign

pt
qt

(4.12)
×ˇq( 1
4 −4∗)P¯t
t=1 mt +(2∗−1
2)P¯t
t=1 sign

pt
qt

ˇq4∗q∗(pα2+sβ2) i
2
X
µ=±1
µ ˇq−2∗q∗µαβ.
To prove the lemma we slightly change eq. (4.11):
ˇTαβ = e−i π
4 ˇq
1
4 −4∗ˇq4∗α2 δαβ,
ˇSαβ =
1
√
K
i
2 ˇq±(2∗−1
2) X
µ=±1
µ ˇq−2∗µαβ,
(4.13)
the choice of sign in ˇq±(2∗−1
2) is arbitrary.
We prove eq. (4.12) by induction on ¯t. If ¯t = 1, that is, if U(p,q) = T mS, then the check
is trivial if we recall that Φ(T mS) = m. It is also easy to check eq. (4.12) for U(p+mq,q) =
T mU(p,q). It remains to check eq. (4.12) for U(−q,p) = SU(p,q).
We have to calculate the sum:
ˇU(−q,p)
αβ
=
X′
−K≤γ≤K
γ∈2ZZ+1
ˇSαγ ˇU(p,q)
γβ .
(4.14)
The following gaussian sum is at the center of this calculation:
X′
−K≤γ≤K
γ∈2ZZ+1
X
µ1,2=±1
µ1µ2 ˇq4∗q∗pγ2−2∗γ(q∗µ1β+µ2α)+4∗q∗sβ2
(4.15)
=
X′
−K≤γ≤K
γ∈2ZZ+1
X
µ1,2=±1
µ1µ2 ˇq4∗q∗p(γ−p∗µ1β−p∗qµ2α)2−4∗q∗p∗(µ1β+qµ2α)2+4∗q∗sβ2
= 2
√
Kei π
4 (κ−1)
pq∗
K

ˇq4∗p∗(−qα2+rβ2) X
µ=±1
µ ˇq−2∗p∗µαβ,
here we used the following relations:
X′
−K≤γ≤K
γ∈2ZZ+1
ˇq4∗pq∗γ2 = ei π
4 (κ−1)√
K
pq∗
K

,
(4.16)
s −p∗= p∗qr,
(4.17)
22
the latter relation follows from ps −qr = 1. To complete the veriﬁcation of eq. (4.12) we
recall the following identities:
Φ(SU(p,q)) = Φ(U(p,q)) −3 sign
 p
q
!
,
(4.18)
i sign (q) = ei π
2 sign(
p
q) sign (p) ,
(4.19)
ei π
4 (κ−1)
 |q|
K
! pq∗
K

= ei π
4 (κ−1) sign( p
q)
 |p|
K
!
.
(4.20)
This ends the proof of the lemma.
To ﬁnish the proof of Proposition 4.1 we rearrange some phase factors of eqs. (4.9) and
(4.12). We substitute a relation
sign
˜L

= sign (L) +
N
X
j=1
t(j)−1
X
t=1
sign

p(j)
t
q(j)
t


(4.21)
into the factor e−i π
4 κ sign(˜L) of eq. (4.9). Then we calculate the combination of phases coming
from that factor and from eq. (4.12) (we drop the index j):
ˇq( 1
4−4∗)P¯t
t=1 mt+(2∗−1
2)P¯t
t=1 sign

pt
qt

e
−i π
2 κP¯t−1
t=1 sign

pt
qt

(4.22)
= ˇq( 1
4−4∗)
P¯t
t=1 mt+(2∗−1
2) sign(
p
q) ˇq(2∗−1
2−κK
4 )P¯t−1
t=1 sign

pt
qt

= ˇq( 1
4−4∗)
hP¯t
t=1 mt−3P¯t−1
t=1 sign

pt
qt
i
ˇq(2∗−1
2) sign( p
q)
= ˇq( 1
4−4∗)Φ(U(p,q)) ˇq(2∗−1
2) sign(
p
q)
We used here eq. (2.7) and the formula
Φ(U(p,q)) =
¯t
X
t=1
mt −3
¯t−1
X
t=1
sign
 pt
qt
!
(4.23)
(see [10] and references therein).
A combination of eqs. (4.9), (4.12), (4.21) and (4.22) leads to eq. (4.8). This concludes
the proof of Proposition 4.1.
As an application of the Proposition 4.1 let us calculate the invariant of a lens space Lp,q.
This manifold is constructed by a U(−p,q) surgery on an unknot in S3. Since
Jα(unknot; k) =
sin

π
Kα

sin

π
K
 ,
(4.24)
23
we can say that Lp,q is constructed by a chain surgery U(−q,−p) = SU(−p,q) applied to an
empty knot, times a factor
√
K
sin( π
K). Then we can read the result directly from eq. (4.8) by
setting there N = 1, sign (L) = 0, α = 1 and
U(−q,−p) =

−q
s
−p
r


(4.25)
instead of U(p,q):
Z′(Lp,q) =
 |p|
K
!
sign (p) ˇq4∗(p∗(q−r)−Φ(U(−q,−p))) ˇq2∗ˇq2∗p∗−ˇq−2∗p∗
ˇq −1
=
 |p|
K
!
sign (p) ˇq3s∨(q,p) ˇq2∗ˇq2∗p∗−ˇq−2∗p∗
ˇq −1
(4.26)
=
 |p|
K
!
sign (p) ˇq3s∨(q,p) (−1)p∗+1 ˇq
p∗
2 −ˇq−p∗
2
ˇq
1
2 −ˇq−1
2 ,
here s∨(q, p) is the “checked” Dedekind sum, that is, its denominator is inverted modulo K
as in eq. (1.13). We used the relation ˇq2∗= −ˇq
1
2 in order to derive the last expression in this
equation. Although it might look simpler than the previous one, it obscures the fact that
Z′(Lp,q) ∈ZZ[ˇq]. Also note that the expression ˇq
p∗
2 by itself is ambiguous since p∗is deﬁned
only modulo K.
Comparing the second expression in the r.h.s. of eq. (4.26) with the formula for the trivial
connection contribution to Witten’s invariant of the lens space
Z(tr)(Lp,q; k) = Z(S3; k)sign (p)
q
|p|
ˇq3s(p,q) ˇq
p
2 −ˇq−p
2
ˇq
1
2 −ˇq−1
2
(4.27)
derived in [10] we can easily check the relation (1.20).
The formula (4.8) also allows us to check the Proposition 1.1 for Seifert manifolds which
are rational homology spheres.
Consider an (N + 1)-component link L in S3 consisting
of N unknots Lj, 1 ≤j ≤N simply linked to a single unknot L0.
A Seifert manifold
X

p1
q1 , . . . , pn
qn

is constructed by performing (pj, qj) surgeries on the components Lj and a
(0, 1) surgery on L0 (see, e.g. [9]). The Jones polynomial of L is known [1] to be equal to
Jβ,α1,...,αN(L; k) =
1
sin

π
K

QN
j=1 sin

π
Kβαj

sinN−1 
π
Kβ

,
(4.28)
24
here β is the color of L0 and αj are the colors of Lj. The signature of L is equal to
sign (L) = −sign
H
P

+
N
X
j=1
sign
 qj
pj
!
(4.29)
Here we introduced notations
P =
N
Y
j=1
pj,
H = P
N
X
j=1
qj
pj
,
(4.30)
so that

H1
 
X
 p1
q1
, . . . , pn
qn
!!

 = |H|.
(4.31)
The Proposition 4.1 provides the following expression for the invariant of the Seifert
manifold X
 p1
q1 , . . . , pn
qn

:
Z′(X; k) =
i
2
√
K ei π
4 κ sign( H
P )eiπ 3
4
K−2
K
sign( H
P )ˇq( 1
2 −2∗) sign( H
P )
×
X′
−K≤β≤K
β∈2ZZ+1
(ˇq−2∗β −ˇq2∗β)Z′
β(L(con); k),
(4.32)
here
Z′
β(L(con); K) =

sin

π
K

sin

π
Kβ



N−1 N
Y
j=1
Z′
β(L−pj,qj; K),
(4.33)
Z′
β(L−pj,qj; K) =
 |qj|
K
! sign (qj)
√
K
e
−i π
K κ sign

qj
pj

e
−iπ 3
4
K−2
K
sign

qj
pj

(4.34)
×ˇq−4∗Φ(U(pj ,qj ))ˇq(2∗−1
2) sign

qj
pj

×
X′
−K≤αj ≤K
αj∈2ZZ+1
(1≤j≤N)
sin

π
Kβαj

sin

π
K

ˇq4∗q∗
j (pjα2
j+sj) i
2

ˇq−2∗q∗
j αj −ˇq2∗q∗
j αj
.
(4.35)
In these formulas Z′
β(L−pj,qj; k) is an invariant of the β-colored link L0 inside the lens space
L−pj,qj constructed by the (pj, qj) surgery on the unknot Lj. Z′
β(L(con); k) is the invariant of
the β-colored knot L0 inside the connected sum of lens spaces
L(con) = L−p1,q1# · · ·#L−pN,qN.
(4.36)
25
The calculation of invariants Z′
β(L−pj,qj; k) runs similar to that of Z′(Lp,q; k) of eq. (4.26).
The only diﬀerence is that by taking a sum over αj we go from ˜U
(pj,qj)
αj1
to ˜U
(−qj,pj)
β1
rather
than to ˜U
(−qj,pj)
11
. As a result,
Z′
β(L−pj,qj; k) =
 |pj|
K
!
sign (pj) ˇq4∗p∗
jqj−3s∨(qj,pj)ˇq−4∗p∗
jqjβ2 ˇq−2∗p∗
jβ −ˇq2∗p∗
j β
ˇq−2∗−ˇq2∗
(4.37)
and
Z′(X; k) =
i
2
√
K ei π
4 κ sign( H
P )eiπ 3
4
K−2
K
sign( H
P )ˇq( 1
2−2∗) sign( H
P )
(4.38)
×
 |p|
K
!
sign (P) ˇq4∗P ∗H−3PN
j=1 s∨(qj,pj)
×
1
ˇq−2∗−ˇq2∗
X′
−K≤β≤K
β∈2ZZ+1
ˇq−4∗P ∗Hβ2
QN
j=1(ˇq−2∗p∗
j β −ˇq2∗p∗
jβ)
ˇq−2∗−ˇq2∗
The preexponential factor of eq. (4.38) can be put in the form
J(β)(ˇq−2∗β −ˇq2∗β),
(4.39)
where
J(β) =
QN
j=1(ˇq−2∗p∗
j β −ˇq2∗p∗
jβ)
(ˇq−2∗−ˇq2∗)(ˇq−2∗β −ˇq2∗β)N−1.
(4.40)
It is easy to check that the function J(β) belongs to ZZ[ˇq] and satisﬁes the properties of the
Jones polynomial described in Proposition 1.2. Therefore the full machinery of Section 3
could be applied to the sum of eq. (4.38) in order to convert it to the integral and ultimately
prove the Proposition 1.1 for Seifert manifolds. However there is an easier way. The numbers
p∗
j, 1 ≤j ≤N determine a set of positive integer numbers Λ(p∗
1, . . . , p∗
N) ∈IN and multiplicity
factors Cn(p∗
1, . . . , p∗
N) ∈ZZ, n ∈Λ(p∗
1, . . . , p∗
N) such that
QN
j=1(ˇq−2∗p∗
jβ −ˇq2∗p∗
j β)
(ˇq−2∗β −ˇq2∗β)N−1
=
X
n∈Λ(p∗
1,...,p∗
N)
Cn(p∗
1, . . . , p∗
N)(ˇq−2∗nβ −ˇq2∗nβ).
(4.41)
Now we can apply eq. (3.5) to the calculation of the sum
1
ˇq−2∗−ˇq2∗
X′
−K≤β≤K
β∈2ZZ+1
ˇq−4∗P ∗Hβ2
QN
j=1(ˇq−2∗p∗
jβ −ˇq2∗p∗
j β)
(ˇq−2∗β −ˇq2∗β)N−2
(4.42)
26
=
2
ˇq−2∗−ˇq2∗
X
n∈Λ
Cn
X′
−K≤β≤K
β∈2ZZ+1
ˇq−4∗P ∗Hβ2(ˇq−2∗(n+1)β −ˇq−2∗(n−1)β)
= 2
√
K
P ∗H
K

ei π
4 (κ−1) X
n∈Λ
Cn
ˇq4∗P H∗(n+1)2 −ˇq4∗P H∗(n−1)2
ˇq−2∗−ˇq2∗
= 2
√
K
P ∗H
K

ei π
4 (κ−1) X
n∈Λ
Cnˇq4∗P H∗(n2+1) ˇq2∗P H∗n −ˇq−2∗P H∗n
ˇq−2∗−ˇq2∗
.
Combining eqs. (4.38) and (4.42) we ﬁnd the formula
Z′(X; k) =
 |H|
K
!
sign (H) ˇq4∗P ∗H−3·4∗sign( H
P )−3PN
j=1 s∨(qj,pj)
(4.43)
×
X
n∈Λ
Cnq4∗P H∗(n2+1) ˇq−2∗P H∗n −ˇq2∗P H∗n
ˇq−2∗−ˇq2∗
,
which demonstrates that Z′(X; k) ∈ZZ[ˇq].
Now we come back to eqs. (4.41), (4.42) and use the fact that for n ∈ZZ,
X′
−K≤β≤K
β∈2ZZ+1
ˇq−4∗P ∗Hβ2−2∗nβ =
√
K
P ∗H
K

ei π
4 (κ−1)ˇq4∗P H∗n2,
(4.44)
Z +∞
−∞dβ ˇq−
β2
4H∗P −2∗βn = e−i π
4 sign(P H∗)q
2K|PH∗|ˇq4∗P H∗n2,
(4.45)
so that
X′
−K≤β≤K
β∈2ZZ+1
ˇq−4∗P ∗Hβ2−2∗nβ =
P ∗H
K

ei π
4 (κ−1)ei π
4 sign(P H∗)
q
2|PH∗|
Z +∞
−∞dβ ˇq−
β2
4H∗P −2∗βn.
(4.46)
This equation allows us to convert the sum over β in eq. (4.42) into an integral. Then by
using eq. (4.41) backwards we arrive at eq. (4.38) with the integral instead of a sum:
Z′(X; k) =
 |H|
K
!
sign (H) ˇq4∗P ∗H−3·4∗sign( H
P )−3PN
j=1 s∨(qj,pj)I(ˇq),
(4.47)
I(ˇq) =
1
ˇq2∗−ˇq−2∗
ei π
4 sign(P H∗)
2
q
2K|PH∗|
Z +∞
−∞dβ ˇq−
β2
4P H∗
QN
j=1(ˇq−2∗p∗
jβ −ˇq2∗p∗
j β)
(ˇq−2∗β −ˇq2∗β)N−2
.
(4.48)
The integral over β is well deﬁned in view of eq. (4.43) (actually, one might add a regularizing
factor limǫ→0 e−ǫβ2.
It can also be calculated by expanding the preexponential factor in
powers of x = q −1 and integrating their coeﬃcients, which are polynomials in β, with the
27
gaussian exponential ˇq−
β2
4P H∗. This procedure leads to the following relation:
[I(ˇq)]⋄=


1
ˇq2∗−ˇq−2∗
ei π
4 sign( H
P )
2
√
2K
s

H
P

+∞
Z
−∞
[β=0]
dβ ˇq−1
4
H
P β2
QN
j=1

ˇq
−β
2pj −ˇq
β
2pj


ˇq−β
2 −ˇq
β
2
N−2


∨
(4.49)
=


1
q
2
K sin

π
K

sign

H
P

K
ei 3
4π sign( H
P )
s

H
P

+∞
Z
−∞
[β=0]
dβ e−iπ
2K
H
P β2
QN
j=1 sin

π
K
β
pj

sinN−2 
π
Kβ



∨
.
Since

ˇq4∗P ∗H−3·4∗sign( H
P )−3PN
j=1 s∨(qj,pj)
⋄
=

ˇq
1
4
H
P −3
4 sign( H
P )−3PN
j=1 s(qj,pj)
∨
(4.50)
and according to [11], [12], [16] (see, e.g. eq.(4.9) of [16])
Z(tr)(X; k) = eiπ 3
4 sign( H
P )
K
sign (P)
q
|P|
e
iπ
2K
h
H
P −3 sign( H
P )−12 PN
j=1 s(qj,pj)
i
×
+∞
Z
−∞
[β=0]
dβ e−iπ
2K
H
P β2
QN
j=1 sin

π
K
β
pj

sinN−2 
π
Kβ
 ,
(4.51)
we conclude that eq. (1.23) holds for Seifert manifolds which are rational homology spheres.
5
Discussion
As we have already mentioned in the Introduction, all results of this paper follow rigorously
from the “physical” input: Propositions 1.2 and 1.3. The Proposition 1.3 might be harder
to prove with mathematical rigor. Even its formulation uses the asymptotic structure (1.16)
of Witten’s invariant at large values of K. To our knowledge, this structure has not been
rigorously derived yet from the surgery formula (1.3). The Proposition 1.2 follows from the
properties of Reshetikhin’s formula [19] of the Jones polynomial of a link and seems to have
better chances for legitimization.
If we forget for a moment about the trivial connection contribution to Witten’s invariant,
then we can use eq. (1.27) as a deﬁnition of the manifold invariants Sn(M). The Proposi-
28
tion 1.2 gives us enough information in order to derive eq. (1.23) in the form
"
|H1(M, ZZ)|
 |H1(M, ZZ)|
K
!
Z′(M; k)
#⋄
(5.1)
=

|H1(M, ZZ)|
3
2 exp

(Sn(M) −Sn(S3))
iπ
K
n∨
.
This also proves Ohtsuki’s Theorem 1.2, since we can deﬁne the invariants λn(M) by
eq. (1.20). According to the comments of [7], [8], we may also conclude that Sn(M), as
deﬁned by the surgery formula (1.27), are indeed invariants of M.
In our previous paper [18] we studied the properties of Sn(M) as they follow from
eq. (1.27), Proposition 1.2 and some other properties of Reshetikhin’s formula [19]. Now
we use eq. (1.20) in order to extend them to λn(M):
Proposition 5.1 The invariants λn(M) are ﬁnite type invariants of RHS as deﬁned in [20]
and [21]. An invariant λn(M) is of Ohtsuki order 3n, Ohtsuki′ ( [18]) order 2n and at most
of Garoufalidis order n. Also
24n n! (2n)! (9n)! |H1(M, ZZ)|nλn(M) ∈ZZ,
(5.2)
|H1(M, ZZ)|nλn(M) ∈ZZ
1
2, 1
3, . . . , 1
2n

.
(5.3)
To see that λn(M) is of exactly Ohtsuki order 3n one has to ﬁnd an n-component link L
such that the alternating sum
X
L′⊂L
(−1)#L′λn(χL′(S3))
(5.4)
is non-zero (here χL(S3) denotes a manifold (RHS ) constructed by (1, 1) surgeries on the
components of a link L in S3). Recall that according to eq. (1.20)
λn(M) =
X
m1,...,mn≥0
m1+2m2+···+nmn=n
Cn
m1,...,mnSm1
1 (M) · · · Smn
n (M)
(5.5)
for some numbers Cm1,...,mn. Consider the n-loop diagram consisting of (n −1) small loops
sitting on one big loop, and the corresponding [20] link L. This diagram has no subdiagrams
29
with only trivalent vertices. Then according to [18], for any Sn′(M), n′ < n the alternating
sums are equal to zero
X
L′′⊂L′
(−1)#L′′Sn′(χL′′(M)) = 0,
(5.6)
if L′ ⊂L and #L′ ≥n′. Therefore an invariant Sn′(M) is of Ohtsuki order less than n′
with respect to L and its subdiagrams (of course, there exist other links for which the l.h.s.
of eq. (5.6) is non-zero if #L′ = n′). As a result, only the term C0,...,0,1Sn(M) in eq. (5.5)
matters for the calculation of the alternating sum (5.4). Since, according to [18], the sum
X
L′⊂L
(−1)#L′Sn(χL′(S3))
(5.7)
is non-zero, we conclude that the sum (5.4) is also non-zero. Hence λn(M) is of exactly
Ohtsuki order 3n.
Finally, let us comment on the relation (1.23) between the invariant Z′(M; k) at prime
values of K and the trivial connection contribution to Witten’s invariant. This relation is not
an obvious result in the sense that the contributions of non-trivial connections to Z′(M; k)
do not seem to cancel at prime K (one might expect that there is some cancelation leaving
only the contribution of the trivial connection). This can be seen at the example of a lens
space Lp,q for which
Z′(Lp,q) = sign (p)
 |p|
K
!
e
6πi
K s∨(q,p) (−1)p∗+1 sin

π
Kp∗
sin

π
K
 ,
(5.8)
Z(tr)(Lp,q; k)
Z(S3; k)
= sign (p)
q
|p|
e
6πi
K s(q,p)sin

π
K
1
p

sin

π
K
 .
(5.9)
Although these two expressions have many common features, which ultimately lead to the
relation (1.23), still their numerical values are quite diﬀerent. The p and K dependence of
Z′(Lp,q) is somewhat typical of contributions of U(1)-reducible connections. Besides, the
Dedekind sum s(q, p) is generally a fraction, so s∨(q, p)̸ = s(q, p).
We established the relation (1.23) by comparing directly the surgery formulas. It would
be much better to have a conceptual explanation for this phenomenon. One might speculate
that it would come from number theory and perhaps p-adic quantum ﬁeld theories.
30
