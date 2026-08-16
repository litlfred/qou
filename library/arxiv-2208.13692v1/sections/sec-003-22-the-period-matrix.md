---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-003-22-the-period-matrix
section_title: "The Period Matrix"
section_number: 2.2
pages: 8-10
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
Theorem 2.12 ([RR92], [GAR00]). Deﬁne the matrices M, MS by
M =


4 1 −1 1
1 4 1 −1
−1 1 4 1
1 −1 1 4

, M S =


4 −1 −1 −1
−1 4 −1 −1
−1 −1 4 −1
−1 −1 −1 4

.
A Riemann matrix for Bring’s curve is given byτB =τ0M, whereτ0 =−0.5+0.186676i (6.d.p)
is given by the conditions
j(τ0) =−293× 5
25 , j (5τ0) =−25
2 .
Further, there exists a symplectic transformation such that τB =τ0MS.
Proof. This was ﬁrst shown in [RR92], but the equations for j(τ0), j(5τ0) were incorrectly
swapped as ﬁrst noted 6 in [BN12], where the above period matrix was also calculated via
the HC-model.
Moreover, in [Web05], a period matrix is constructed with respect to a homology basis
with intersection matrix
IW =


0 1 1 −1 −1 0 0 1
−1 0 1 1 0 1 0 −1
−1 −1 0 1 0 −1 0 0
1 −1 −1 0 0 0 1 0
1 0 0 0 0 1 1 −1
0 −1 1 0 −1 0 1 1
0 0 0 −1 −1 −1 0 1
−1 1 0 0 1 −1 −1 0


,
that is given as Ω = (A,B ) where the columns Ak,Bk are
Ak =


ζk(1−ζ 2)
ζ 2k+3/2(1−ζ 4)(lΦ− 1)
ζ 4k+3(1−ζ 3)Φ(1−l)
ζ 3k+2(1−ζ)l

, B k =


ζ 2k+3/2(1−ζ 4)(lΦ− 1)
ζ 4k+3(1−ζ 3)Φ(1−l)
ζ 3k+2(1−ζ)l
ζk(1−ζ 2)

,
6Note the approximation of τ0 in [BN12] contains a typographic error.
BRING’S CUR VE: OLD AND NEW 9
for k = 0,..., 3, Φ = 1
2(1 +
√
5), and l =
⏐⏐⏐ I(−1,0)
I(−∞,−1)
⏐⏐⏐≈ 0.848641 where
I(a,b ) =
∫ b
a
(t− 1)−1/5t−3/5(t + 1)−4/5dt.
Note [Web05, Lemma 5.1] uses ζ = exp(2πi/10), whereas we take ζ = exp(2πi/5). As such,
the columns of Ω look diﬀerent to those of Weber in terms of the exponent of ζ, but they
do indeed agree.
One can ﬁnd (using Sage) the matrix
C =


0 1 −2 1 1 1 0 −1
0 1 −1 1 0 0 −1 0
0 0 −1 0 0 1 1 0
1 1 −2 2 0 1 −1 −1
0 0 0 0 0 0 1 1
0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 0


such that CTIWC = Jg =
( 0 Id g
− Idg 0
)
, i.e. C ‘canonicalises’ the homology basis. This
means we get a Riemann matrixτW = (AC)−1(BC) =C−1A−1BC, and one can numerically
ﬁnd that the matrix
R =
(δ β
γ α
)
=


0 0 0 1 0 0 1 2
0 −1 1 0 −1 −2 1 1
1 0 1 0 2 1 1 1
0 1 0 0 1 2 0 0
1 0 0 0 2 1 0 1
1 0 1 −1 1 1 1 −1
−1 0 0 1 −1 −1 1 2
1 0 1 −1 1 2 1 −1


relates τW to τB by
(5) τB = (δ +τWγ)−1(β +τWα).
Here R is a symplectic transform with respect the standard symplectic form Jg.
For a fourth proof, we may consider the Riemann matrix numerically calculated by Sage-
Math, and ﬁnd a transform to τB, as is done in the corresponding notebook. □
Riera and Rodriguez (hereafter abbreviated to R&R) constructed the constraints on τ0
viaj-invariants by considering the quotients by group actions of the curve to elliptic curves
[RR92]. They show that these constraints give a unique value of τ0 modulo Γ 0(5), or
equivalently in the language of [GAR00] that τ0 gives a distinguished point in the modular
curve X0(5). As we will see later in §4.4, there are additional quotients to elliptic curves
not considered by R&R, which have j-invariants
j(15τ0) =−52× 2413
23 ,(6)
j(3τ0) = 5× 2113
215 .(7)
The latter is identiﬁed in relation to Bring’s curve in [Ser08, Exercise 8.3.2c]. Serre says
that this curve (50H) and 50E (using the naming convention of [BK75]) with j(5τ0) are
10 H. W. BRADEN AND LINDEN DISNEY-HOGG
15-isogenous over Q. This isogeny is not too mysterious when we think on the level of
the corresponding elliptic curves over C as C/⟨1, 3τ0⟩ and C/⟨1, 5τ0⟩, wherein the isogeny
C/⟨1, 3τ0⟩→ C/⟨1, 5τ0⟩ is the composition of the quotients by the maps z↦→ z +τ0 and
z↦→z + 1/5 respectively. There is a complete Q-isogeny class of elliptic curves of order four
with periods τ0, 3τ0, 5τ0 and 15τ0 [BK75].
It follows from the above that τ0 is transcendental. By a theorem of Schneider [BW08],
if j(z) is rational, z is either transcendental or an element of a quadratic imaginary ﬁeld
with class number 1. However, the j-invariants of elements of these ﬁelds are known to
be integers, which doesn’t occur in the case of τ0. In Weber’s form of the period matrix,
the transcendentality comes about because of the constant l, which is a ratio of Schwarz-
Christoﬀel integrals which arise from the map of a Euclidean quadrilateral to a hyperbolic
quadrilateral.
