---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-012-f-elementary-proofs-from-the-quadratic-formula
section_title: "F Elementary proofs from the quadratic formula"
section_number: null
pages: 25-28
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
Here we state the proofs of elementary lemmas in Section 3 which rely mainly on the quadratic formula for
the roots of a quadratic equation in a single variable. We prove the ele mentary lemmas, using the notation
introduced in Section C.
Proof of Lemma 3.2: The two factors in (46) are
(
x· (ξ2 + 1)− (1 + 2x)ξ
)
and
(
x· (ξ2 + 1)− (1− 2x)ξ
)
. (174)
So the roots of Q1(x;·) are the solutions of
(ξ2 + 1)− 1 + 2x
x ·ξ = 0 , (175)
and the solutions of
(ξ2 + 1)− 1− 2x
x ·ξ = 0 . (176)
Let us denote
κ+(x) = 1 + 2x
x and κ−(x) = 1− 2x
x . (177)
These are both elements of (2 ,∞) because we assumed x∈ (0, 1/4) (so that 1 − 2x > 2x). Let us deﬁne
ρ(+)
+ (x), ρ(+)
− (x), ρ(−)
+ (x), and ρ(−)
+ (x) as
ρ(+)
± (x) =
√
κ+(x)± 2 and ρ(−)
± (x) =
√
κ−(x)± 2. (178)
Then we have
c1(x) = 1
4
(
ρ(+)
+ (x)−ρ(+)
− (x)
)2
, c 2(x) = 1
4
(
ρ(−)
+ (x)−ρ(−)
− (x)
)2
, (179)
d1(x) = 1
4
(
ρ(−)
+ (x) +ρ(−)
− (x)
)2
, d 2(x) = 1
4
(
ρ(+)
+ (x) +ρ(+)
− (x)
)2
. (180)
(This can be checked by expanding.) Therefore, by (148), these a re the roots of Q1(x;·). Since the leading
coeﬃcient of Q1(x;·) is x2, the lemma is proved. □
Proof of Lemma 3.3: The proof is much like the proof of Lemma 3.2. The two factors in (49) are
(
x· (ξ2 + 1)− (1 +
√
4x2 +w2)ξ
)
and
(
x· (ξ2 + 1)− (1−
√
4x2 +w2)ξ
)
. (181)
25
So the roots of Q2(x,w ;·) are the solutions of
(ξ2 + 1)− 1 +
√
4x2 +w2
x ·ξ = 0 , (182)
and the solutions of
(ξ2 + 1)− 1−
√
4x2 +w2
x ·ξ = 0 . (183)
Let us denote
~κ+(x,w ) = 1 +
√
4x2 +w2
x and ~κ−(x,w ) = 1−
√
4x2 +w2
x . (184)
These are both elements of (2 ,∞) because we assumed x∈ (0, 1/4) and 0 <w< √1− 4x; hence,
1−
√
4x2 +w2 < 2x. (185)
Let us deﬁne ~ρ(+)
+ (x,w ), ~ρ(+)
− (x,w ), ~ρ(−)
+ (x,w ), and ~ρ(−)
− (x,w ) as
~ρ(+)
± (x,w ) =
√
~κ+(x,w )± 2 and ~ρ(−)
± (x,w ) =
√
~κ−(x,w )± 2. (186)
Then we have
A1(x,w ) = 1
4
(
~ρ(+)
+ (x,w )−~ρ(+)
− (x,w )
)2
, A2(x,w ) = 1
4
(
~ρ(−)
+ (x,w )−~ρ(−)
− (x,w )
)2
, (187)
b1(x,w ) = 1
4
(
~ρ(−)
+ (x,w ) +~ρ(−)
− (x,w )
)2
, b 2(x,w ) = 1
4
(
~ρ(+)
+ (x,w ) +~ρ(+)
− (x,w )
)2
. (188)
Therefore, by (148), these are the roots of Q2(x,w ;·). □
Proof of Lemma 3.4: We use the notation from the proofs of Lemmas 3.2 and Lemma 3.3. Co nsidering
the function ∆ : (2 ,∞)→ (0,∞) as
∆( κ) =
√
κ + 2−
√
κ− 2, (189)
we see that
∆ ′(κ) = −
√κ + 2−√κ− 2
2
√
κ2− 4 , (190)
which is negative. Therefore, ∆ is a decreasing function. Note that its range is actually (0 , 2) with ∆( ∞) =
limκ→∞ ∆( κ) = 0. Let us also deﬁne ∆(0) = 2, which is its value by continuous exten sion. Then all this
means
∀κ1,κ 2∈ [2,∞)∪{∞} , we have κ1<κ 2⇒ ∆(~κ2) < ∆( κ1). (191)
Then, by a diﬀerence of squares, or monotonicity of the square fu nction on the nonnegative domain
∀κ1,κ 2∈ [2,∞)∪{∞} , we have κ1<κ 2⇒ (∆(~κ2))2 < (∆( κ1))2 . (192)
But now notice that
0 = 1
4 (∆(∞))2 , A1(x,w ) = 1
4 (∆(~κ+(x,w )))2 ,
c1(x) = 1
4 (∆( κ+(x)))2 , c 2(x) = 1
4 (∆( κ−(x)))2 , (193)
A2(x,w ) = 1
4 (∆(~κ−(x,w )))2 , 1 = 1
4 (∆(2)) 2 .
Therefore, we will know
0 <A1(x,w ) < c1(x) < c2(x) <A2(x,w ) < 1, (194)
if we can establish
0 < ~κ−(x,w ) < κ−(x) < κ+(x) < ~κ+(x,w ) <∞. (195)
But clearly ~κ+(x,w )<∞ and~κ−(x,w )> 2 as we showed in the proof of Lemma 3.3. Now
~κ+(x,w )−κ+(x) = (2 x)−1(
√
4x2 +w2− 2x) > 0, (196)
26
because we assumed w> 0. We have the identical positive quantity for
κ−(x)−~κ−(x,w ) = (2 x)−1(
√
4x2 +w2− 2x). (197)
Finally, we note that κ+(x)−κ−(x) = 4 which is positive. Therefore, equation (195) is established. Now the
order
1 < b1(x,w ) < d1(x) < d2(x) < b2(x,w ) <∞, (198)
follows from (194) and equations (53) and (53). □
Proof of Lemma 3.5: To see that f (x;·) is analytic, let us deﬁne h(x;·) : C\{ 0}→ C as
h(x;ξ) =
(
1−x· (ξ +ξ−1)
)2
− 4x2. (199)
Then we may write f (x;ξ) =
√
h(x;ξ), which is analytic, as long as we prove
h(x;·)
(
U(0;d1(x))\U(0;c1(x))
)
=
{
h(x;ξ) : U(0;d1(x))\U(0;c1(x))
}
(200)
is a subset of C\ (−∞, 0]. Since 4 x2 + 1∈ R, then h(x;ξ)∈ (−∞, 0] only if
1−x· (ξ +ξ−1)∈ R∪iR, (201)
where iR means{iy : y∈ R}. If we decompose ξ into its modulus and phase as
ξ = reiθ, (202)
for r∈ [0,∞) and θ∈ R, then we have
1−x· (ξ +ξ−1) = 1 −x· (r +r−1) cos(θ)−ix· (r−r−1) sin(θ). (203)
So, in order to have this quantity be in R requires r = 1 or θ∈πZ, which means |ξ| = 1 or ξ∈ R. To have
the right-hand-side of (203) be an element of iR would require x· (r +r−1) cos(θ) = 1.
Let us ﬁrst consider the case that (203) is an element of iR. This requires
r +r−1 ≥ 1
x, (204)
and cos(θ) = 1/
(
x· (r +r−1)
)
. The inequality in (204) may be rewritten as r2 + 1− 1
x ·r≥ 0. Consulting
Appendix C, we see that
r2 + 1− 1
x ·r = (r− R+(x)) (r− R−(x)) , (205)
for the two real roots:
R+(x) = 1 +
√
1− 4x2
2x and R−(x) = 1−
√
1− 4x2
2x . (206)
They are real and 0 < R−(x) < R+(x) because we have assumed that x∈ (0, 1/4). (It would have suﬃced
to have 0 <x< 1/2.) Therefore, equation (204) is equivalent to
r∈ R\ (R−(x), R+(x)) . (207)
That is the condition for the left-hand-side of equation (203) to be an element of iR, as long as ξ =reiθ where
cos(θ) = 1/
(
x· (r +r−1)
)
. In other words,
∀ξ∈ C, we have |ξ|∈ (R−(x), R+(x))⇒ 1−x· (ξ +ξ−1)⁄∈iR (208)
Next, let us change attention to the condition for 1 −x· (ξ +ξ−1) to be in R. We must have |ξ| = 1 or
ξ∈ R. But if |ξ| = 1 then 1 −x· (ξ +ξ−1) = 1− 2x· cos(θ)> 2x since we assumed x∈ (0, 1/4). So in this
caseh(x;ξ) is in D1 from Remark 2.3. So, instead, consider the case that ξ is in R. Then we prefer changing
the notation to ξ =t∈ R (which could potentially be negative, which is why we avoid recycling the letter r
which was positive before). Then to have h(x;t)≤ 0 requires
h(x,t ) = Q1(x;t)
t2 ≤ 0, (209)
27
which requires, by Lemma 3.2,
t∈ R\ (c2(x),d 1(x)) . (210)
So combining this with (208) we have
∀ξ∈ C, we have |ξ|∈ (c2(x),d 1(x))∩ (R−(x), R+(x))⇒h(x;ξ)∈D 1. (211)
It is easy to see that
R−(x)<c 2(x)<d 1(x)< R+(x), (212)
for x∈ (0, 1/4). For instance 1 − 2x≥√1− 4x hence
√
1− 4x2≥ 2x +√1− 4x because
(1− 2x)(1 + 2x)≥ (1− 2x)2 + 4x
√
1− 4x = (2x +
√
1− 4x)2. (213)
Therefore, for analyticity of
√
h(x;·) equation (211) reduces to just |ξ|∈ (c2(x),d 1(x)). □
