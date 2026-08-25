---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-554-651-rather-than-2-4-8-we-now-prefer-to-work-with
section_title: "Rather than ∆(2 , 4, 8), we now prefer to work with ∆(6 , 2, 4) (this"
section_number: 6.5.1
pages: 206-209
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
amounts to permute 0, 1,∞ byt↦→z = 1
1−t , and is more faithful to the ﬁrst
picture of this section which places the vertex O at the center of the disk).
The triangle group ∆(6 , 2, 4) is the projective monodromy group of the
hypergeometric diﬀerential operator L 1
24 , 7
24 , 5
6
. More precisely, L 1
24 , 7
24 , 5
6
(y) =
0 is a uniformizing diﬀerential equation for the orbifold X∗ viewed as the
Schwarz orbifold
(
P1, 0 1 ∞
e0 = 6 e1 = 2 e∞ = 4
)
More explicitly, F ( 1
24, 7
24, 5
6 ;z) and z1/6F ( 5
24, 11
24, 7
6 ;z) are independent solu-
tions of L 1
24 , 7
24 , 5
6
and for a suitable constant κ, the mapping
τ (z) = κ−1.z1/6F ( 5
24, 11
24, 7
6 ;z)
F ( 1
24, 7
24, 5
6 ;z)
sends the upper half plane bijectively to the basic triangle OQP of the
Schwarz tesselation, and τ (0) = O, τ(1) = Q, τ(∞) = P .
•
0
•
1
✲τ
O Q
P
Figure 12
6. THE TALE OF F ( 1
24 , 7
24 , 5
6 ; z). 203
It extends to a multivalued analytic function on P1\{ 0, 1,∞} with value in
D(0, 1−). The inverse mapping z(τ ) : D(0, 1−)→ P1 is the (single-valued)
∆(2 , 4, 6)-automorphic uniformizing mapping of the Shimura orbifo ldX∗.
6.5.2. Actually,τ expresses the period mapping P for “fake elliptic curves”
with multiplication by B2.3, cf. II.1.2 and II.7.4: more precisely, the multi-
valued function τ (z) is related to the commutative diagram
~X∗
C
an
P
∼
−−−→ D= D(0, 1−) ⊂ D∨ = P1
Q


↓


↓
(
P1, 0 1 ∞
6 2 4
)
=X∗
C
an −−−→ D/∆(2 , 4, 6)
by
τ (z) =P◦Q −1, z(τ ) =Q◦P −1.
6.5.3. Using Gauss’ formula for the value of hypergeometric functi ons at 1,
one can compute the constant κ, cf. [Car61, 392]:
κ = Γ( 7
6 )
Γ( 5
6 )
√
Γ( 1
24 )Γ( 7
24 )Γ( 13
24 )Γ( 19
24 )
Γ( 5
24 )Γ( 11
24 )Γ( 17
24 )Γ( 23
24 ).
Using the functional equations of Γ, one checks that κ ∼
(Γ( 1
3 )
Γ( 2
3 )
)3
(mod Q
×
), in conformity with II.7.6.4 (taking into account the fact that
z = 0 corresponds to a fake elliptic curve with complex multipl ication by an
order in M2(Q(√−3))).
6.5.4. Forp⁄= 2, 3, the p-adic radius of convergence of F ( 1
24, 7
24, 5
6 ;z) and
F ( 5
24, 11
24, 7
6 ;z) is 1. The unit disk |z|p < 1 is ordinary or supersingular
according to whether p ≡ 1 (mod 3) or not. The ratio
z1/ 6F ( 5
24 , 11
24 , 7
6 ;z)
F ( 1
24 , 7
24 , 5
6 ;z)
expresses a local p-adic period mapping.
The p-divisible group of the fake elliptic curve parametrized by z is
isogenous to the square of the p-divisible group of an elliptic curve; the period
mapping is thus completely analogous to one of those studied in II.6.3.1,
6.3.3 (Dwork, Gross-Hopkins). From the viewpoint of analyt ic continuation,
this is essentially the situation studied in I.3 (for F ( 1
2, 1
2, 1;z)).
6.5.5. Forp = 3 ( resp. p = 2), the situation is radically diﬀerent; the p-
adic radius of convergence of F ( 1
24, 7
24, 5
6 ;z) andF ( 5
24, 11
24, 7
6 ;z) is 3−3/2 (resp.
2−6).
The ratio
z1/ 6F ( 5
24 , 11
24 , 7
6 ;z)
F ( 1
24 , 7
24 , 5
6 ;z) expresses the Drinfeld 3-adic period mapping:
204 III. p-ADIC ORBIFOLDS AND MONODROMY.
P
∼~X +(2)an
C3
❄
X +(2)an
C3
❄
X∗ an
C3 2
✲ D ⊂ D∨ = P1
❄
D/∆ 3(2, 4, 6)✲
HereD is the image of the Drinfeld space Ω C3 by a suitable homography
(it would be interesting to determine this homography expli citly). That
this homography is actually deﬁned over Q comes from II.7.6.4 (ramiﬁed
variant), I.4.6.4, 5.3.9 (the point is that the triadic peri ods, in the sense of
I.5.3, of the abelian surface with complex multiplication b y M2(Q[√−3])
parametrized by z = 0, belong to Q).
Although F ( 5
24, 11
24, 7
6 ;z)/F ( 1
24, 7
24, 5
6 ;z) has very small triadic radius of
convergence, its pull-back on the Shimura curve X +(2) extend to a global
multivalued meromorphic function, with poles only above 0 , 1,∞ (in other
words, its pull-back on ~X +(2)C3
∼
= Ω C3 is single-valued).
Note however that the same is not true forF ( 1
24, 7
24, 5
6 ;z) andF ( 5
24, 11
24, 7
6 ;z)
individually, for reasons of exponents at ∞. Nevertheless, they enjoy a sim-
ilar property, on replacing X +(2) by a suitable ramiﬁed ﬁnite covering.
Similarly, in the diadic case: the pull-back of F ( 5
24, 11
24, 7
6 ;z)/F ( 1
24, 7
24, 5
6 ;z)
on the Shimura curve X +(3) extends to a global multivalued meromorphic
functions (with poles only above 0 , 1,∞).
6.6. A triadic analogue of Gauss’ formula, and special value s of
F ( 1
24, 7
24, 5
6 ;z) at CM points.
6.6.1. For our hypergeometric function, Gauss’ formula reads
F
( 1
24, 7
24, 5
6 ; 1
)
= Γ( 5
6 )Γ( 1
2 )
Γ( 19
24 )Γ( 13
24 ).
If one considers F ( 1
24, 7
24, 5
6 ;z) as a multivalued analytic function on P1\
{0, 1,∞}, the values at 1 generate a Q-subspace of C of dimension ≤ 2,
namely:
Γ( 5
6 )Γ( 1
2 )
Γ( 19
24 )Γ( 13
24 ) Q + Γ( 5
6 )Γ(− 1
2 )
Γ( 1
24 )Γ( 7
24 ) Q.
Similarly, its values at ∞ generate the Q-subspace
Γ( 5
6 )Γ( 1
4 )
Γ( 19
24 )Γ( 7
24 ) Q + Γ( 5
6 )Γ(− 1
4 )
Γ( 1
24 )Γ( 13
24 ) Q.
6. THE TALE OF F ( 1
24 , 7
24 , 5
6 ; z). 205
