---
doc_id: sigma12-065
doc_title: ""
section_id: sec-008-52-symmetries-and-the-vector-of-riemann-constant
section_title: "Symmetries and the vector of Riemann constants"
section_number: 5.2
pages: 16-19
source_pdf: sigma12-065.pdf
source_sha256: a6e0e0da5cc5ff9b
doc_brief: "Bring’s Curve: its Period Matrix and the Vector of Riemann Constants ⋆ — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
---
We now describe how symmetries may be used to restrict the vector of Riemann constants by
recalling some results we have established elsewhere.
Suppose that a curve has a nontrivial group of symmetries Aut( C). Then the holomorphic
differentials of the curve,H1,0(C, C), and the homology groupH1(C, Z) are both Aut(C)-modules.
Let σ∈ Aut(C) and denote the actions on these spaces by
σ∗vj =
∑
k
vkLk
j, σ ∗
(ai
bi
)
=M
(ai
bi
)
:=
(A B
C D
)( ai
bi
)
,
where L ∈ GL(g, C), M ∈ Sp(2g, Z) and {vi} is a (not necessarily normalized) basis of
H1,0(C, C). Denote by Π =
(A
B
)
the matrix of periods, where Aij =
∫
ai
vj andBij =
∫
bi
vj.
Then τ =BA−1 and ω = vA−1. The identity
∮
σ∗γv =
∮
γσ∗v (for any γ∈H1(C, Z)) yields the
relation
MΠ = ΠL (5.3)
which restricts the period matrix τ. Now using (5.1) and (5.2) we have that (with ˆL =ALA−1,
so as to be working with normalized differentials))
2KQ ˆL≡
∫ 2∆
∗
σ∗ω− 2(g− 1)
∫ Q
∗
σ∗ω
which yields
2KQ
[ˆL− Id
]
≡
∫ σ(2∆)
2∆
ω− 2(g− 1)
∫ σ(Q)
Q
ω.
IfKC is the divisor of a differentialv thenσ−1(KC) is the divisor ofσ∗(v), whence the uniqueness
of the canonical class means that σ(KC)∼KC and consequently σ(2∆)∼ 2∆. This shows that
we have an action of Aut(C) on the theta characteristics and
KQ ˆL≡Kσ(Q) +
∫ σ(∆)
∆
ω,
the last integral also being a theta characteristic. We have then the identity on the Jacobian
2KQ
[
ˆL− Id
]
≡− 2(g− 1)
∫ σ(Q)
Q
ω.
This then establishes
Lemma 1. Suppose the automorphism σ has order N > 1. If L− Id is invertible and Q is
a ﬁxed point of σ then KQ is a 2N-torsion point.
Remark 1. We have the mapπ :C→C /⟨σ⟩. Any holomorphic differential on C/⟨σ⟩ pulls back
to an invariant differential onC, and so the assumption that L− Id is invertible is equivalent to
C/⟨σ⟩∼= P1.
Corollary 1. Assuming the conditions of Lemma 1 and that ψ ∈ Aut(C), then
∫ψ(Q)
Q ω is
a 2N(g− 1)-torsion point.
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 17
Although these simple results do not necessarily give the best bound on the order of the
torsion point for the vectors involved, we see that, given a suitable symmetry and fixed point,
we have that KQ is a torsion point:
2KQA = nΠ [L− Id]−1 = n(M− Id)−1Π = n
(
1
N
N−1∑
k=1
kMk
)
Π.
The additional (we think) new idea we brought to this was to use some number theory associated
with M to restrict the form of KQ. Suppose there exist l, m∈ Z2g such that
m = l(M− Id), (5.4)
then
mΠ = l(M− Id)Π = lΠ [L− Id]
and
(2KQA + lΠ) [L− Id] = (n + m)Π∈ Cg.
The idea is to use the freedom in choosing l here in (5.4) to make n + m as simple as possible;
as we are only interested in 2KQ modulo the lattice we will have further restricted the choice of
the vector of Riemann constants. For example, if m could be chosen arbitrarily then we could
make n + m = 0 and so 2KQ would be a lattice point. We implement the idea using the Smith
normal form of M− Id. Recall this means in the present context that we may write
M− Id =USV, S = Diag(d1,...,d 2g), d i|di+1, U,V ∈GL(2g, Z).
The invertibility of L− Id means that di≥ 1 and that (5.4) becomes
mV−1 = (lU)S.
Here we view l′ = lU as arbitrary and we are interested in the constraints this places on m.
We have ( mV−1)i = l′
idi and clearly the only constraints arise for di⁄= 1. Given our earlier
observation that here di≥ 1, we find that m is constrained only by
(
mV−1)
i≡ 0 mod di, d i> 1.
Thus, given a suitable symmetry and fixed pointQ, the Smith normal form ofM−Id enables us
to restrict the possible torsion points for 2KQ. Considering further automorphisms and making
use of Corollary 1 may yield further restrictions. The final step in evaluating KQ is the choice
of the appropriate half-period when taking the square root. This again may be restricted by the
symmetry but may also be decided numerically from the 2 2g half-periods.
5.3 Application to Bring’s curve
For Bring’s curve we find that everything follows from study of the single (order 5) automorphism
given in the Hulek–Craig representation by
φ : [¯x, ¯y, ¯z]↦→
[
ζ2¯x,ζ 4¯y, ¯z
]
.
This has fixed point [0, 0, 1], or Q = (0, 0) in affine coordinates.
18 H.W. Braden and T.P. Northover
The first and easiest calculation is deriving its action on the differentials. We fix the ordered
basis of (unnormalized) holomorphic differentials
v1 = (¯y3− ¯x)d¯x
∂yC(¯x, ¯y, 1), v 2 = (¯y2¯x− 1)d¯x
∂yC(¯x, ¯y, 1), v 3 = (¯y− ¯x2)d¯x
∂yC(¯x, ¯y, 1), v 4 = ¯y(¯x2− ¯y)d¯x
∂yC(¯x, ¯y, 1).
The construction of such holomorphic differentials is algorithmic (see [7]). It is easy to check
that
φ∗(v1) =ζv1, φ ∗(v2) =ζ4v2, φ ∗(v3) =ζ3v3, φ ∗(v4) =ζ2v4,
and so φ∗vj =vkLk
j where
L =


ζ 0 0 0
0 ζ4 0 0
0 0 ζ3 0
0 0 0 ζ2

.
Thus there is no invariant differential and L− Id and so ˆL− Id are invertible. With Q = (0, 0)
we see the conditions of Lemma 1 are satisfied.
We note in passing that the differential v3 has a simple zero at a = [0, 0, 1], a double zero at
b = [0, 1, 0] and a triple triple zero at c = [1, 0, 0]2∼ [1,t,t 4] for the required total of 2g− 2 = 6.
Thus we haveKC∼a + 2b + 3c expressing the canonical divisor in terms of rational points of C.
To proceed with our strategy of determining KQ we first determine the action of φ on the
homology cycles. With the program extcurves at hand this is a simple computational matter,
complicated only slightly by the noncanonical nature of the paths we obtained in Section 4.4.
We obtainφ∗(γi) =∑
jMijγj where
M =


0 0 0 1 0 0 0 0
−1 0 0 −1 0 0 0 0
0 −1 0 1 0 0 0 0
0 0 −1 −1 0 0 0 0
0 0 0 0 −1 1 −1 1
0 0 0 0 −1 0 0 0
0 0 0 0 0 −1 0 0
0 0 0 0 0 0 −1 0


.
We remark that consideration of the equation (5.3) for this order five symmetry already imposes
that
AT =


a1 0 0 0
0 a2 0 0
0 0 a3 0
0 0 0 a4




1 −1−ζ4 1 +ζ4 +ζ3 ζ
1 −1−ζ 1 +ζ +ζ2 ζ4
1 −1−ζ2 1 +ζ2 +ζ4 ζ3
1 −1−ζ3 1 +ζ3 +ζ ζ 2

,
for some unknown ai. These ai are related by the remaining symmetries and ultimately the
period matrix (1.1).
Continuing with our determination of KQ, calculating the Smith normal form of M− 1 gives
us unimodular matrices U, V such that
M− Id =U Diag(1, 1, 1, 1, 1, 1, 5, 5)V
and our earlier constraint ( mV−1)i≡ 0 mod di, di> 1 takes the form
−m5 +m6−m7− 4m8≡ 0 (mod 5) ,
Bring’s Curve: its Period Matrix and the Vector of Riemann Constants 19
−m1 + 2m2− 3m3−m4− 11m5 + 6m6−m7− 34m8≡ 0 (mod 5) .
This gives 25 possible unique candidates for 2 KQ; we can vary ni arbitrarily (by adding an
appropriate l) without essentially changing 2KQ for (say) i = 2, 3, 4, 6, 7, 8 but then n1 and n5
are fixed. Explicitly, every 2KQ is equivalent to one generated by
n =
(
n1 0 0 0 n5 0 0 0
)
.
By considering a further symmetry we find further that n1 =n5 = 3 and at this stage we have
2KQ = 1
5
(
−12 −3 3 −3
)
+τ0
(
−6 −6 3 0
)
.
To determining the appropriate 2-torsion point for square root of the canonical bundle one could
further study the action of the symmetries on the spin structures or simply numerically test the
vanishing of the theta function. The latter approach yields that
Theorem 3. For the Riera and Rodr´ ıguez homology basis of Bring’s curve we have that the
vector of Riemann constants is
KQ = 1
10
(
3 2 −2 −3
)
+ Im(τ0)
(
1 −2 −2 1
)
i,
whereτ0 is deﬁned by (4.3).
The transformation of theta characteristics
g· (a, b) = (a, b)g−1 + 1
2
(
diag
(
CDT)
, diag
(
ABT))
for any g =
( A B
C D
)
∈ Sp(2g, Z) and characteristic ( a, b)∈ Q2g together with the explicit
representations of the symmetries yields
Theorem 4. Bring’s curve has a unique invariant spin-structure.
Remark 2. Klein’s curve has a unique invariant spin structure [14] and we have shown elsewhere
that the vector of Riemann constants is the Abel image of this. To show the analogous result
for Bring’s curve requires a better understanding of this spin-structure.
Acknowledgements
We are grateful to Maurice Craig for helpful email exchanges and also to an anonymous referee
for careful reading and suggested improvements to the paper.
