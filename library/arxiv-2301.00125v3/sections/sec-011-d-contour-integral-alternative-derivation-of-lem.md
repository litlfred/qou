---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-011-d-contour-integral-alternative-derivation-of-lem
section_title: "D Contour integral alternative derivation of Lemma 2.2"
section_number: null
pages: 23-25
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
By the equation (28) we may write
γ(2)(x2,y 2) =
∮
C(0;1)
∮
C(0;1)
γ(xξ,yζ )γ
(x
ξ , y
ζ
) dξ
2πiξ · dζ
2πiζ , (149)
which may be rewritten as
γ(2)(x2,y 2) =
∮
C(0;1)
∮
C(0;1)
1
1− (xξ +yζ ) · 1
1− (xξ−1 +yζ −1) · dξ
2πiξ · dζ
2πiζ . (150)
This may be rewritten as
γ(2)(x2,y 2) = − 1
4π2
∮
C(0;1)
∮
C(0;1)
1
1− (xξ +yζ ) · 1
ξζ− (xζ +yξ)dξdζ. (151)
Let us ﬁrst integrate over ζ. Therefore, we use the partial fraction expansion for ζ:
1
1− (xξ +yζ ) · 1
ξζ− (xζ +yξ) = 1
1−xξ−yζ · 1
(ξ−x)ζ−yξ
= 1
(ξ−x)(1−xξ)−y2ξ
( y
1−xξ−yζ + ξ−x
(ξ−x)ζ−yξ
) (152)
Therefore, considering the integrand of (151) as a function of ζ, the poles are at
α = 1−xξ
y , and β = yξ
ξ−x. (153)
For|x| and|y| suﬃciently small, and for |ξ| = 1, we see that |α|> 1 and|β|< 1. Therefore, from the residue
theorem (see for example Theorem 17 in Section 4.5 of Ahlfors [1])
γ(2)(x2,y 2) = 1
2πi
∮
C(0;1)
1
(ξ−x)(1−xξ)−y2ξdξ. (154)
Now we may factorize the denominator in the integrand of this integr al, as a polynomial in ξ in order to ﬁnd
the locations of the poles and calculate the residues. Note that if we hadx = 0 the integral (2πi)−1∮
C(0;1)(ξ−
y2ξ)−1dξ would give (1−y2)−1 by the residue theorem. Let us assume x⁄= 0, and then note
(ξ−x)(1−xξ)−y2ξ = ξ−x−xξ2 +x2ξ−y2ξ
=−x
(
ξ2− 1 +x2−y2
x ξ + 1
) (155)
By the formulas from Section C we have for k = (1 + x2−y2)/x, the roots are at
ξ± = 1
4
(√
k + 2±
√
k− 2
)2
= 1
4
(√
1 +x2−y2 + 2x
x ±
√
1 +x2−y2− 2x
x
)2
, (156)
as long as we assume
k = 1 +x2−y2
x ∈ C\ (−2, 2). (157)
Note that we are justiﬁed in assuming that x,y∈ [0,∞) and are small, since determining the power series for
x andy in that regime determines it elsewhere by the identity theorem of com plex analysis and the discussion
of the Fubini-Tonelli theorem before, between equations (22) and (23) Note that for x> 0 suﬃciently small,
we know that ξ+ > 1 and ξ− < 1. (Note that ξ+ξ− = 1.) Therefore, by the residue theorem, we have
γ(2)(x2,y 2) = − 1
x· 1
ξ−−ξ+
= 1
x· 1
ξ+−ξ−
. (158)
But it is easy to see the algebraic simpliﬁcation
x· (ξ+−ξ−) = x
4
((√
k + 2 +
√
k− 2
)2
−
(√
k + 2−
√
k− 2
)2)
= x
4
(
2
√
k + 2
)(
2
√
k− 2
)
.
(159)
23
Therefore, this may be further simpliﬁed as
x· (ξ+−ξ−) =
√ (
(1 +x)2−y2)(
(1−x)2−y2)
=
√ (
(1 +x2−y2) + 2x
)(
(1 +x2−y2)− 2x
)
=
√
(1 +x2−y2)2− 4x2
(160)
Then we expand
(1 +x2−y2)2− 4x2 = 1 + 2(x2−y2) + (x2−y2)2− 4x2
= 1 + (2x2− 2y2) + (x4− 2x2y2 +y4)− 4x2
= 1− 2x2− 2y2 +x4 + 2x2y2 +y4− 4x2y2
= 1− 2(x2 +y2) + (x2 +y2)2− 4x2y2
= (1− (x2 +y2))2− 4x2y2.
(161)
Therefore, we have,
γ(2)(x2,y 2) = 1√ (
1− (x2 +y2)
)2
− 4x2y2
. (162)
Recall that it suﬃces to assume that we have x,y∈ [0,∞) both suﬃciently small to specify the actual power
series in complex x andy. Therefore, we obtain the desired result by replacing x≥ 0 by√x≥ 0 and replacing
y≥ 0 by√y≥ 0.
E Pochhamer identities for −1/2 and negative integers
Here we state what needs to be used to derive the equivalence of (3 5) and (36). Note that
(−1/2)n =
(
− 1
2
)(
− 3
2
)
···
(
− 1 + 2(n− 1)
2
)
, (163)
which equals
(−1/2)n = (−1)n
2n (1) (3)··· (2n− 1) , (164)
which in turn may be rewritten as
(−1/2)n = (−1)n
2n · (2n)!
(2)(4)··· (2n) = (−1)n
22n · (2n)!
n! . (165)
This well-known fact is easily found, for example on Wikipedia it can be de duced from the formula Γ(1 /2) =√π and Γ( 1
2−n) = (−1)n22nn!√π/(2n)!.
We also know that for the Pochhammer symbol at a negative integer we have
(−n)k = (−n)(−n− 1)··· (−n−k + 1) = ( −1)k(n)(n + 1)(n +k− 1) = (−1)k (n +k− 1)!
(n− 1)! . (166)
Hence, in particular replacing n by 2n + 1 we have
(−2n− 1)k = (−1)k (2n +k)!
(2n)! . (167)
Therefore, putting these two together, we see that the summan ds in (35) are simpliﬁed by using the formula
(−1/2)n
n! · (−2n− 1)k
k! = (−1)n
22n · (2n)!
(n!)2 · (2n +k)!
(2n)!k! = (−1)n+k
22n
(2n +k
n,n,k
)
. (168)
Hence, the left-hand-side of equals (35)
∞∑
n=0
(−1/2)n
n! · (−2n− 1)k
k!
(k
j
)
(−1)n+k4n =
∞∑
n=0
(−1)n+k
22n
(2n +k
n,n,k
)(k
j
)
(−1)n+k4n, (169)
24
which may be further simpliﬁed using
(2n +k
n,n,k
)(k
j
)
=
( 2n +k
n,n,j,k −j
)
. (170)
So, the left-hand-side of equals (35) may be rewritten as
∞∑
n=0
(−1/2)n
n! · (−2n− 1)k
k!
(k
j
)
(−1)n+k4n =
∞∑
n=0
( 2n +k
n,n,j,k −j
)
. (171)
In (35) we wanted to verify that, when we replace j←ℓ−n and k−j←m−n (using replacement notation
as in APL) then we get
(ℓ+m
ℓ,m
)(ℓ+m
ℓ,m
)
. So this equation may be rewritten as
∞∑
n=0
( 2n +ℓ +m
n,n,ℓ −n,m−n
)
=
(ℓ +m
ℓ,m
)(ℓ +m
ℓ,m
)
. (172)
We then take account of the fact that in the multinomial coeﬃcient n otation, the multinomial coeﬃcient
equals 0 unless all the terms in the bottom are nonnegative integers . So we require ℓ−n≥ 0 and m−n≥ 0.
Then the inﬁnite sum for n∈{ 0, 1,... } may be restricted to n∈{ 0,..., min(ℓ,m )}. That is how we reduce
equation (35) to (36) or its even more direct version
min(m,n)∑
n=0
( 2n +ℓ +m
n,n,ℓ −n,m−n
)
=
(ℓ +m
ℓ,m
)(ℓ +m
ℓ,m
)
. (173)
