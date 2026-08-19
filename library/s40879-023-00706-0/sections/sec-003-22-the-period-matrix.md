---
doc_id: s40879-023-00706-0
doc_title: "RESEARCH ARTICLE"
section_id: sec-003-22-the-period-matrix
section_title: "The period matrix"
section_number: 2.2
pages: 11-14
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
We record now a result from the literature. Recall that given a choice of a basis of
differentials{ωi} on a curve and a choice of homology basis{ai, bj} on the same curve
such that the intersection pairing is given by ai ◦bj = δij (we call such a homology
basis canonical), we deﬁne the associated period matrix (also called the matrix of
periods) to be the g× 2 g block matrix /Omega1= (A | B) where
A
ij =
∫
a j
ωi, Bij =
∫
b j
ωi.
It is the case that A will always be invertible, and we can then deﬁne the associated
Riemann matrix to be τ = A−1 B.
Theorem 2.10 ([29, 54]) Deﬁne the matrices M, M S by
M =
⎛
⎜⎜⎝
41 −11
141 −1
−11 4 1
1 −11 4
⎞
⎟⎟⎠ , MS =
⎛
⎜⎜⎝
4 −1 −1 −1
−14 −1 −1
−1 −14 −1
−1 −1 −14
⎞
⎟⎟⎠.
A Riemann matrix for Bring’s curve is given byτB = τ0 M, where the complex number
τ0 is given by the conditions
j(τ0) =− 293 × 5
25 , j(5τ0) =− 25
2 ,
with j the elliptic- j function on the upper half plane. Then
τ0 =− 0.5 + 0.186676i (6.d.p).
Further, there exists a symplectic transformation such thatτB = τ0 MS.
Proof This is known, and has been proven in multiple different ways. We summarise
these and highlight a numerical approach.
1. This was ﬁrst shown in [ 54], but the equations for j(τ0), j(5τ0) were incorrectly
swapped as ﬁrst noted 8 in [8].
2. It was calculated in [ 8] going via the HC-model.
8 Note the approximation of τ0 in [8] contains a typographic error.
123
3 Page 12 of 46 H.W. Braden, L. Disney-Hogg
3. In [66], by viewing the curve as a cyclic cover of P1, a period matrix is constructed
with respect to a homology basis with intersection matrix
IW =
⎛
⎜⎜⎜⎜
⎜
⎜
⎜
⎜⎜⎜⎝
011 −1 −10 0 1
−10 1 1 0 1 0 −1
−1 −10 1 0 −10 0
1 −1 −1 00010
1000011 −1
0 −11 0 −10 1 1
000 −1 −1 −10 1
−11 0 0 1 −1 −10
⎞
⎟⎟⎟⎟
⎟
⎟
⎟
⎟⎟⎟⎠
,
that is given as /Omega1= (A, B) where the columns A
k, Bk 9 are
Ak =
⎛
⎜⎜⎝
ζ k(1 − ζ 2)
ζ 2k+3/2(1 − ζ 4)(l/Phi1− 1)
ζ 4k+3(1 − ζ 3)/Phi1(1 − l)
ζ 3k+2(1 − ζ) l
⎞
⎟⎟⎠ , Bk =
⎛
⎜⎜⎝
ζ 2k+3/2(1 − ζ 4)(l/Phi1− 1)
ζ 4k+3(1 − ζ 3)/Phi1(1 − l)
ζ 3k+2(1 − ζ) l
ζ k(1 − ζ 2)
⎞
⎟⎟⎠ ,
for k = 0,..., 3, /Phi1= (1+
√
5)/2, and l =| I(−1, 0)/I(−∞,−1)|≈ 0.848641
where
I(a, b) =
∫b
a
(t − 1)−1/5t−3/5(t + 1)−4/5dt.
One can ﬁnd (using Sage) the matrix
C =
⎛
⎜⎜
⎜
⎜⎜⎜
⎜
⎜
⎜
⎜⎝
01 −2111 0 −1
01 −1100 −10
00 −1001 1 0
11 −2201 −1 −1
00 0 000 1 1
00 1 000 0 0
00 0 000 0 1
00 0 100 0 0
⎞
⎟⎟
⎟
⎟⎟⎟
⎟
⎟
⎟
⎟⎠
such that C
T IW C = Jg =
( 0I d g
− Idg 0
)
, i.e. C transforms the homology basis to one
which is canonical. This means we get a Riemann matrix τW = (AC)−1(BC) =
9 Note [66, Lemma 5.1] uses ζ = exp(2πi/10), whereas we take ζ = exp(2πi/5). As such, the columns
of /Omega1look different to those of Weber in terms of the exponent of ζ , but they do indeed agree.
123
Bring’s curve: old and new Page 13 of 46 3
C−1 A−1 BC , and one can numerically ﬁnd that the matrix
R =
( δβ
γα
)
=
⎛
⎜⎜
⎜
⎜⎜⎜
⎜
⎜
⎜
⎜⎝
00 0 1
00 1 2
0 −11 0 −1 −21 1
10 1 0 21 1 1
01 0 0 12 0 0
1 000 21 0 1
10 1 −1 11 1 −1
−1001 −1 −11 2
10 1 −1 12 1 −1
⎞
⎟⎟
⎟
⎟⎟⎟
⎟
⎟
⎟
⎟⎠
relates τ
W to τB by
τB = (δ + τW γ)−1(β + τW α). (6)
Here R is a symplectic transform with respect the standard symplectic form Jg .
4. For a numerical approach, we may consider the Riemann matrix calculated by
SageMath, and ﬁnd a transform to τB, as is done in the corresponding notebook.
Riera and Rodriguez (hereafter abbreviated to R&R) constructed the constraints
on τ0 via j-invariants by considering the quotients by group actions of the curve to
elliptic curves [54]. They show that these constraints give a unique value ofτ0 modulo
/Gamma10(5), or equivalently in the language of [29] that τ0 gives a distinguished point in the
modular curve X0(5). As we will see later in Sect. 4.4, there are additional quotients
to elliptic curves not considered by R&R, which have j-invariants
j(15τ0) =− 52 × 2413
23 , (7)
j(3τ0) = 5× 2113
215 . (8)
The latter is identiﬁed in relation to Bring’s curve in [ 57, Exercise 8.3.2c]. Serre says
that this curve (50 H) and 50E (using the naming convention of [ 6]) with j(5τ0) are
15-isogenous over Q. This isogeny is not too mysterious when we think on the level
of the corresponding elliptic curves over C as C/⟨1, 3τ0⟩and C/⟨1, 5τ0⟩, wherein the
isogeny C/⟨1, 3τ0⟩→ C/⟨1, 5τ0⟩is the composition of the quotients by the maps
z ↦→ z + τ0 and z ↦→ z + 1/5 respectively. There is a complete Q-isogeny class of
elliptic curves of order four with periods τ0, 3τ0, 5τ0 and 15τ0 [6].
It follows from the above thatτ0 is transcendental. By a theorem of Schneider [4], if
j(z) is rational, z is either transcendental or an element of a quadratic imaginary ﬁeld
with class number 1. However, the j-invariants of elements of these ﬁelds are known
to be integers, which does not occur in the case of τ0. In Weber’s form of the period
matrix, the transcendentality comes about because of the constant l, which is a ratio of
Schwarz–Christoffel integrals which arise from the map of a Euclidean quadrilateral
to a hyperbolic quadrilateral.
123
3 Page 14 of 46 H.W. Braden, L. Disney-Hogg
