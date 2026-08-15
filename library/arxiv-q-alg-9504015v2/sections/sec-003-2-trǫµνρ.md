---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten’s Invariants of Rational Homology Spheres at Prime"
section_id: sec-003-2-trǫµνρ
section_title: "Trǫµνρ"
section_number: 2
pages: 2-4
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten’s Invariants of Rational Homology Spheres at Prime — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial connection contribution to Witten’s invariant of"
---
∫
M
d3x
(
Aµ∂νAρ + 2
3AµAνAρ
)
(1.2)
(k ∈ Z Z, Tr is the trace taken in the fundamental representation of SU (2)) can also be
calculated combinatorially with the help of the surgery formula. Let M be a 3d manifold
constructed by ( pj, 1) surgeries on the components Lj of an N-component link L in S3. A
(p, 1) surgery means that the meridian of the tubular neighborhood is g lued to the parallel
plus p meridians on the boundary of the knot complement (in other words, a Dehn’s surgery
is performed on a knot with framing number p). The invariant of M can be expressed in
terms of the framing independent colored Jones polynomial Jα1,...,αN (L; k) of the link L:
Z(M; k)
Z(S3; k) =
( 2
K
) N
2
exp

3
4 πi
( 2
K − 1
) N∑
j=1
sign (pj)

 (1.3)
×
∑
0≤α j ≤K−1
(1≤j≤N)
Jα1,...,αN (L; k) exp

 iπ
2K
N∑
j=1
pj(α2
j − 1)


N∏
j=1
sin
( π
K αj
)
,
Z(S3; k) =
√
2
K sin π
K , K = k + 2. (1.4)
The Jones polynomial Jα1,...,αN (L; k) is normalized in such a way that it is multiplicative for
unlinked links and J(empty link; k) = 1, Jα(unknot; k) =
sin( π
K α)
sin( π
K ) .
Although N. Reshetikhin and V. Turaev proved [2] that eq. (1.3) inde ed deﬁnes an in-
variant of M (i.e. the l.h.s. of eq. (1.3) is invariant under Kirby moves), the topological
origin of this invariant remains somewhat obscure. The question is: w hich of the “classical”
topological invariants of M are contained inside Z(M; k)? Two distinct approaches to this
problem have been tried. The ﬁrst one is to study Z(M; k) for some particular values of
K. R. Kirby and P. Melvin discovered [3] that if K is odd, then Z(M; k) is proportional to
1
Z(M; 1):
Z(M; k)
Z(S3; k) = Z ′(M; k) ×





Z(M ;1)
Z(S3;1) , if K = −1 (mod 4)
Z(M ;1)
Z(S3;1) , if K = 1 (mod 4) ,
(1.5)
If M is a rational homology sphere ( Z ZHS ), then Z(M; 1) = Z(S3; 1) so that Z ′(M; k) =
Z(M ;k)
Z(S3;k).
The new invariant Z ′(M; k) can be calculated by the following surgery formula
Z ′(M; k) = K − N
2 exp

−πi
4
(
3 + κ − 6
K
) N∑
j=1
sign (pj)

 (1.6)
×
∑ ′
−K≤α j ≤K
α j ∈2Z Z+1
(1≤j≤N)
Jα1,...,αN (L; k) exp

 iπ
2K
N∑
j=1
pj(α2
j − 1)


N∏
j=1
sin
( π
K αj
)
,
here
κ =





1 if K = −1 (mod 4)
−1 if K = 1 (mod 4) ,
(1.7)
while
∑ ′ means that we add an extra factor of 1
2 to the terms corresponding to the boundary
values of summation index ( αj = ±K in this case). We changed slightly the original formula
of [3]: instead of taking a sum over 1 ≤ αj ≤ K−1
2 we sum over odd αj between 1 and K − 1.
This allows us to get rid of some phase factors. We also double the ran ge of summation to
1 − K ≤ αj ≤ K − 1 by using the fact that Jα1,...,αN (L; k) is an odd function of its indices
(we use the 2 K periodicity in αj in order to extend Jα1,...,αN (L; k) to negative values of αj).
Note that the whole summand of eq. (1.6) has a periodicity of 2 K.
S. Garoufalidis [4] used nice properties of the gaussian sum ∑ K−1
α=0 exp
(
2πi
K α2
)
for prime
values of K in order to study Witten’s invariant of lens spaces and Seifert manifo lds. H. Mu-
rakami and T. Ohtsuki [5]–[8] carried out a detailed study of the inva riant Z ′(M; k) of
rational homology spheres (RHS ) for prime K.
Theorem 1.1 (H. Murakami, [5], [6]) For a RHS M and a prime K > 2
Z ′(M; k) ∈ Z Z[ˇq], ˇq = e
2πi
K , (1.8)
Z Z[ˇq] being a cyclotomic ring.
2
We need more notations in order to present the results of Ohtsuki’s papers [7], [8]. We
introduce a new variable
x = q − 1. (1.9)
A polynomial from Z Z[ˇq] can be reexpressed as a polynomial in x with integer coeﬃcients. It
is deﬁned modulo the polynomial
(1 + x)K − 1
x =
K−1∑
n=0
K(K − 1) · · ·(K − n)
(n + 1)! xn, (1.10)
which is identically equal to zero for x = e
2πi
K − 1. All the coeﬃcients of this polynomial
except the one at xK−1, are divisible by K. As a result, all the coeﬃcients at xn, n ≤ K −2 for
a polynomial of x coming from Z Z[ˇq] are well deﬁned modulo K. We will limit our attention
to the powers of x up to x
K−1
2 . They are all well deﬁned as elements of Z ZK if K ≥ 3. Thus
there is a homomorphism of rings:
⋄ : Z Z[ˇq] → Z Z′
K[x] def.= Z ZK[x]/x
K+1
