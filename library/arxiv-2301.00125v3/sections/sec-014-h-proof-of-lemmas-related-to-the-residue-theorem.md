---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-014-h-proof-of-lemmas-related-to-the-residue-theorem
section_title: "H Proof of lemmas related to the residue theorem"
section_number: null
pages: 29-31
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
Proof of Lemma 4.1: For any ǫ∈ (0,b 1(x,w )− 1), the integrand,
I(ξ) = w·ξ +~g(x;ξ)
x2·
(
ξ−A 1(x,w )
)(
ξ−A 2(x,w )
)(
ξ−b1(x,w )
)(
ξ−b2(x,w )
)· 1
2πi, (226)
is analytic in the open domain U(0; 1 +δ)\
(
{A1(x,w ),A2(x,w )}∪ [c1(x),c 2(x)]
)
. The value of the contour
integral is independent of the choice of rectiﬁable arc/contour, o r in our case, independent of the sum of
contours as long as that sum is homotopic to C(0; 1) in the domain of analyticity. (See for example [1] or
[27].) Therefore, for δ∈ (0, 1) suﬃciently small we deform to the union of three contours
Γ 1(δ) = C(A1(x,w );δ) and Γ 2(δ) = C(A2(x,w );δ), (227)
Γ 3(δ) = Γ 1(δ) + Γ 2(δ) +γ3(δ) +γ4(δ),
γk(δ) : ξ(t) = ~ck(δ)· (1−t) +~ck+1(δ)·t,
for 0 ≤t≤ 1, for k∈{ 1, 2, 3, 4}, (228)
~c1(δ) =~c5(δ) = c1(x,w )−δ, ~c2(δ) = c2(x,w )−δ,
~c3(δ) = c2(x,w ) +δ, ~c4(δ) = c1(x,w ) +δ.
See Figure 4, cited previously. (Note that one can add and subtrac t line segments along the real axis external
to these three contours and internal to C(0; 1) joining these contours to each other, and to C(0; 1). In the
appropriate sense, the sum of these three contours is homotopic toC(0; 1).) Technically the rectangle Γ 3(δ)
does intersect the boundary of the domain at ( ~c2(δ) +~c3(δ))/2 = c2(x) and at (~c4(δ) +~c5(δ))/2 = c1(x). But
I is continuous at those points so that this introduces no diﬃculty. (I t suﬃces to consider Γ 3(δ) as a limit of
contours strictly inside the domain of analyticity.)
For Γ 1(δ) and Γ 2(δ) as we shrink δ we obtain the residues (as in Theorem 6, page 119 of [1])
∀k∈{ 1, 2} we have lim
δ→0+
∮
Γ k(δ)
I(ξ)dξ = 2πi· lim
ξ→ak(x,w)
(
ξ−ak(x,w )
)
·I (ξ), (229)
29
where we use the slightly unusual formula for the residues because , in the lemmas of the last section, we have
already established that there are simple poles at A1(x,w ) andA2(x,w ). I.e., there are no higher-order poles.
Combining the two contributions from equation (229) gives the form ula forA1(x,w ) in (75).
For the contribution to the integral coming from the rectangle Γ 3(δ), we may neglect the left and right
sides Γ 2(δ) and γ3(δ) because their arclengths vanish in the limit and I is continuous at c1(x) and c2(x). The
eﬀect of taking the δ→ 0+ limit for Γ 1(δ) and Γ 2(δ) is as follows:
lim
δ→0+
∮
Γ 3(δ)
I(ξ)dξ =
∫ c2(x)
c1(x)
(
I(ξ−i· 0)−I (ξ +i· 0)
)
dξ, (230)
where, as is standard convention, we denote
I(ξ +i· 0) = lim
δ→0+
I(ξ +i·δ) and I(ξ−i· 0) = lim
δ→0+
I(ξ−i·δ). (231)
In the next paragraph, and following, we will show that the limits from the upper half plane and from the lower
half plane do exist, that they are continuous functions on the inter val [c1(x),c 2(x)] and that the limits are
obtained uniformly on [ c1(x),c 2(x)] as δ→ 0+. Therefore, there are no technical diﬃculties in interchanging
the order of taking the δ→ 0+ limits and taking the integral, using the dominated convergence theo rem. The
reason that the limiting integrand is I(ξ−i· 0)−I (ξ +i· 0) (instead of its opposite) is because of the positive
orientation of the contour Γ 3(δ).
Before calculating the limits I(ξ±i· 0), we note that the integrand may be written as
I(ξ) = w·ξ +~g(x;ξ)
2πiQ2(x,w ;ξ), (232)
as an alternative to equation (226). But then the term w·ξ/Q2(x,w ;ξ) is analytic in a neighborhood of
[c1(x),c 2(x)] since it merely has poles at A1(x,w ) andA2(x,w ) withinU(0; 1), and we have established that
A1(x,w )<c 1(x) and c2(x)<A2(x,w ) in the lemmas of the last section. Therefore,
I(ξ±i· 0) = w·ξ
2πiQ2(x,w ;ξ) +~I(ξ±i· 0), (233)
where we deﬁne
~I(ξ) = ~g(x;ξ)
2πiQ2(x,w ;ξ). (234)
Clearly the limits of the ﬁrst summand on the right hand side of (233) a re the same, are continuous, and are
attained uniformly by Weierstrass’s M-test for local uniform conve rgence (see Section 2.3 of [1]) since that
function is analytic in an open neighborhood of the whole interval [ c1(x),c 2(x)]. □
Proof of : Now considering~I, the denominator is also analytic an non-vanishing in a neighborhood o f the
interval [c1(x),c 2(x)], for the same reason as before: that A1(x,w )<c 1(x) and c2(x)<A2(x,w ). Therefore,
~I(ξ±i· 0) = 1
2πiQ2(x,w ;ξ) ·~g(x;ξ±i0). (235)
Finally, we turn attention to the key point of the calculation, which is t he jump discontinuity of the square-root
type functon ~g(x;ξ±i0) across its branch-cut [ c1(x),c 2(x)]. Since we are going to focus on ξ∈ [c1(x),c 2(x)]
we change the symbol to r to indicate better that it is a real number. That frees the symbol ξ to be the
point ξ =r +iδ (or ξ =r−iδ) for the complex variable converging to r from the upper half-plane (or lower
half-plane).
Suppose that we have r∈ (c1,c 2) and δ >0. We are seeking the limits from both the upper half-plane
and lower half-plane of the phases, which we denote as
ζ±(r) = lim
δ→0+
~g(x;r±iδ)
|~g(x;r±iδ)|. (236)
We focus on just the limit from the upper half-plane, ﬁrst, since the other limit is obtained by similar
(symmetric) considerations. We may refer to Figure 4 to determine the phase of ~g(x;ξ) for ξ = r +iǫ. We
have
ξ−c1(x) =
√ (
r−c1(x)
)2
+δ2·eiθ1 and ξ−c2(x) =
√ (
c2(x)−r
)2
+δ2·eiθ2, (237)
30
where θ1∈ (0,π/ 2) and θ1∈ (π/2,π ). But in the limit δ→ 0+, we have θ1→ 0 while θ2→π. So we have
lim
δ→0+
ξ−c1(x)
|ξ−c1(x)| = 1 and lim
δ→0+
ξ−c2(x)
|ξ−c2(x)| =−1. (238)
But then taking the square-root, we have eiθ1/2 converges to 1 while eiθ2/2 converges to i. Multiplying these
together, we get
∀r∈ (c1,c 2) we have ζ+(r) = i. (239)
Note that d1−r> 0 and d2−r> 0 for r throughout [−1, 1], which is why we did not consider those factors.
Of course if we replace ǫ by−ǫ then the angles are reﬂected: θ1←− θ1 and θ2←− θ2 using replacement
notation (as in APL). So the phase changes from ζ+(r) = i to its reciprocal
∀r∈ (c1,c 2) we have ζ−(r) = 1
i =−i. (240)
From this we see that
~g(x;r±i· 0) = ζ±(r) lim
δ→0
|~g(x;r +i·δ)|, (241)
where the ﬁnal limit of the absolute value occurs uniformly and is the s ame from both the upper and lower
half-planes. More precisely,
~g(x;r±i· 0) = xζ±(r)·
√
r−c1(x)·
√
c2(x)−r·
√
d1(x)−r·
√
d2(x)−r. (242)
Sinceζ±(r) =±i, combining this with (230) gives the formula (76) for the contributio n to the contour integral
arising from Γ 3(δ). Note that ζ−(r)−ζ+(r) = −2i. This cancels the 2 i in the 2 πi with the quotient being
equal to−1. But since Q2(r) is negative on the interval [ c1(x),c 2(x)] (owing to the fact, stated several times
before, that A1(x,w )<c 1(x) and c2(x)<A2(x,w )) we have put the −1 with that term in (76) so that the
integrand on [c1(x),c 2(x)] is manifestly positive. □
