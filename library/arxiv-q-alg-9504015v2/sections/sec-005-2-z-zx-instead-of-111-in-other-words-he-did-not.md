---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-005-2-z-zx-instead-of-111-in-other-words-he-did-not
section_title: "Z Z[x] instead of (1.11) (in other words, he did not ﬁx the coeﬃcient at x"
section_number: 2
pages: 5-8
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
K−1
2 ).
Murakami showed that
λ0 = 1, λ 1 = λCW, (1.15)
here λCW is the Casson-Walker invariant of RHS .
The second approach to the search of the topological meaning of W itten’s invariant
Z(M; k) is based on the path integral representation (1.1). According to quantum ﬁeld
theory, this integral can be calculated by stationary phase appro ximation when K → ∞ .
The invariant is presented as a sum of contributions coming from con nected components c
of the moduli space of ﬂat connections on the manifold M:
Z(M; k) =
∑
c
Z (c)(M; k). (1.16)
Each contribution has a general form
Z (c)(M; k) =
(
4π2
K
) Nzero
2 1
Vol(Hc) exp
[
2πikS (c)
CS +
∞∑
n=0
S(c)
n (M)
( iπ
K
) n]
, (1.17)
here Hc is the isotropy group, Nzero = dim H 0
c − dim H 1
c , H 0,1
c being the cohomologies of
0,1-forms taking values in the adjoint su(2) bundle, S(c)
CS is the Chern-Simons action and
∑ ∞
n=0 S(c)
n (M)
(
iπ
K
) n
is an asymptotic series. The coeﬃcients S(c)
n (M) are called ( n + 1)-loop
corrections. They might be related to “classical” topological invaria nts of M. Indeed, the
1-loop correction S(c)
0 is related to the Reidemeister-Ray-Singer torsion. An attempt to r elate
4
the asymptotic properties of the surgery formula (1.3) for lens sp aces and Seifert manifolds
to the quantum ﬁeld theory predictions of eqs. (1.16), (1.17) was in itiated by D. Freed and
R. Gompf [9] and carried out further by L. Jeﬀrey [10], S. Garoufalid is [4] and also in the
papers [11, 12]. A complete agreement between the surgery formu la and 1-loop predictions
was observed.
If the manifold M is a RHS , then the trivial connection is a separate point in the moduli
space of ﬂat connections. According to quantum ﬁeld theory, its c ontribution is of the form
Z (tr)(M; k) =
√
2π
K
3
2 |H1(M, Z Z)|
3
2
exp
[ ∞∑
n=1
Sn(M)
( iπ
K
) n]
. (1.18)
A representation of the coeﬃcients Sn(M) in terms of ( n + 1)-loop Feynman diagrams was
carried out by S. Axelrod and I. Singer [13], M. Kontsevich [14], C. Tau bes [15] and others.
We studied how the trivial connection contribution can be extracte d from the surgery for-
mula (1.3). We derived a knot surgery formula [16] and a link surgery f ormula [17] for it.
The knot formula allowed us to show that
S1(M) = 6 λCW. (1.19)
The link surgery formula of [17] was much less explicit than the knot fo rmula of [16],
because it did not express Z (tr)(M; k) directly in terms of derivatives of the Jones polynomial
Jα1,...,αN (L; k). However we derived an explicit surgery formula [18] for algebraica lly split
links (ASL ).
In this paper we are going to prove the following:
Proposition 1.1 Ohtsuki’s invariants λn(M) of eq. (1.14) and loop corrections to the trivial
connection contribution Sn(M) of eq. (1.18) can be expressed in terms of each other through
the following relation
∞∑
n=0
λn(M)xn = exp
[ ∞∑
n=1
(Sn(M) − Sn(S3))
( iπ
K
) n]
≡
(
π
K
)
sin
(
π
K
) exp
[ ∞∑
n=1
Sn(M)
( iπ
K
) n]
(1.20)
by substituting either
x = e
2πi
K − 1 = 2πi
K
∞∑
n=0
1
(n + 1)!
( 2πi
K
) n
, (1.21)
5
or
iπ
K = 1
2 log(1 + x) = x
2
∞∑
n=0
(−1)n xn
n + 1 . (1.22)
In other words, we will show that
[
|H1(M, Z Z)|
(
|H1(M, Z Z)|
K
)
Z ′(M; k)
] ⋄
=
[
|H1(M, Z Z)|
3
2
Z (tr)(M; k)
Z(S3; k)
] ∨
. (1.23)
In process of doing this we will rederive the results of [5]-[8] maybe in a somewhat more
explicit way.
Our proof of the Proposition 1.1 will be based on the following two prop ositions derived
in [19] and [18] by using some “physical” considerations:
Proposition 1.2 Let L be an algebraically split link (ASL ) in S3. Then its framing-
independent colored Jones polynomial has the following Tay lor series expansion in powers of
K:
Jα1,...,αN (L; k) =


N∏
j=1
αj


∞∑
n=0
∑
m≤ 3
4 n
Dm,n(α1, . . . , αN )
( iπ
K
) n
, (1.24)
here Dm,n(α1, . . . , αN ) are even homogeneous polynomials of degree 2m:
Dm,n(α1, . . . , αN ) =
∑
m1,...,m N ≥0
m1+···+mN =m
D(m,n)
m1,...,mN α2m1
1 · · · α2mN
N (1.25)
and
mj ≤ n − m, 1 ≤ j ≤ N. (1.26)
Proposition 1.3 Let M be a rational homology sphere (RHS ) constructed by (pj, 1) surg-
eries on the components of an N-component link L in S3. Then the loop corrections to the
trivial connection contribution (1.18) to Witten ’s invari ant of M are given by the formula:
exp
[ ∞∑
n=1
(Sn(M) − Sn(S3))
( iπ
K
) n]
(1.27)
= exp

3
4 πi
( 2
K − 1
) N∑
j=1
sign (pj)

 exp

− iπ
2K
N∑
j=1
(
pj + 1
pj
) 
 iN
(2K)
N
2
⏐
⏐
⏐
⏐
⏐
⏐
N∏
j=1
pj
⏐
⏐
⏐
⏐
⏐
⏐
3
2
×
+∞∫
−∞
[α j =0]
dα1 · · · dαN exp

 iπ
2K
N∑
j=1
pjα2
j

 Jα1+ 1
p1
,...,αN + 1
pN
(L; k).
6
The symbol
+∞∫
−∞
[α j =0]
means that the integral has to be calculated in the following way: ﬁrst, an
expansion (1.24) has to be substituted and then the gaussian integrals over αj have to be
calculated for each polynomial
( ∏ N
j=1
(
αj + 1
pj
))
Dm,n
(
α1 + 1
p1
, . . . , αN + 1
pN
)
separately (for
more details see [18]).
The Proposition 1.2 is essential for all our calculations. The Proposit ion 1.4 is needed only
for the derivation of eq. (1.23). In other words, we could use eq. ( 1.27) as a deﬁnition of
Sn(M) and then prove eq. (1.20) which amounts to proving the Theorem 1 .2.
In Section 2 we modify the surgery formula (1.6) and prove the Theo rem 1.1. Our main
tool is the observation that the gaussian sum ∑ K−1
α=0 ˇqα2
is proportional to x
K−1
2 , while the
sum ∑ K−1
α=0 ˇqα2
α2m for m ≤ K−1
2 is only proportional to x
K−1
2 −m. This is similar to the be-
havior of gaussian integrals: each two extra powers of α in the integral
∫ +∞
−∞ e
2πi
K α2
α2m dα
bring a power of K to denominator. In Section 3 we prove the Proposition 1.1 and thus
also the Theorem 1.2. We use again the similarities of the formulas for
∑ K−1
α=0 ˇqα2
α2m and
∫ +∞
−∞ e
2πi
K α2
α2m dα. These similarities are due to the fact that both the sum ∑ K−1
α=0 ˇqα2+2nα
and the integral
∫ +∞
−∞ e
2πi
K (α2+2nα) dα can be calculated by completing the square in the ex-
ponents. In Section 4 we derive a rational surgery formula for Z ′(M; k) which is similar to
the formula (4.1) of [10] for the original Witten’s invariant Z(M; k). We use this formula to
verify the Proposition 1.1 for lens spaces and Seifert manifolds which are rational homology
spheres. In Section 5 we discuss the properties of Ohtsuki’s invaria nts λn(M) as related to
the properties of invariants Sn(M) studied in [18].
