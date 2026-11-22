---
doc_id: arxiv-1112.0030v2
doc_title: "Homological Algebra of Knots and BPS States"
section_id: sec-007-appendix-b-kauffman-and-s2-homologies-of-the-kno
section_title: "Appendix B. Kauffman and S2 homologies of the knots 819 and 942"
section_number: null
pages: 37-41
source_pdf: 1112.0030v2.pdf
source_sha256: 745f143c2df4734b
toc_source: outline
doc_brief: "Homological Algebra of Knots and BPS States — It is known that knot homologies admit a physical description as spaces of open BPS states. We study operators and algebras acting on these spaces."
---
(B.1) P (942)(a, q, t) = a(q−1t2+qt4)+(q−2t−1+1+2t+q2t3)+a−1(q−1t−2+q).
In particular, the reduced sl(2) Khovanov homology of 942 is:
Kh(942)(q, t)
=
P (942)(a = q2, q, t) =
The S invariant is S(942) = 0. Moreover, the δ-grading of a generator x of the
homology H (K) in our conventions is given by:
δ(x) = t(x) −2a(x) −q(x).
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES
37
N (K)(q) .
• The corresponding polynomials and homologies for the anti-symmetric rep-
resentations are denoted in the same way with Sr replaced by Λr.
Remark A.1. Conventions for the superpolynomial in the vector rep-
resentation:
The case r = 1 corresponds to the (ordinary) HOMFLY polynomial
and the Khovanov-Rozansky homology. The corresponding superpolynomial, to-
gether with the structure of the triply-graded homology was studied in [3].
Here we shall use slightly diﬀerent conventions: in the superpolynomial, we
replace a and q from [3] with a1/2 and q1/2, respectively. For example, the super-
polynomial of the trefoil knot becomes:
Also, by S(K), or just S, we mean half of the value of S(K) from [3].
This way, the degrees of canceling diﬀerentials d1 and d−1 from [3] become
(−1, 1, −1) and (−1, −1, −3), respectively. Also, from now on we denote these two
diﬀerentials by d1 and d−1, respectively.
In this appendix we compute the S2 and Kauﬀman homologies of 819 and 942.
Since both knots are homologically thick knots, these computations give highly
non-trivial examples of our main Conjecture 4.2 (as well as Conjecture 2 of [6] for
the Kauﬀman homology), especially because the size of both homologies is rather
large and because they have to obey a large list of structural properties described
in sections 4 and 5.
Before we start our computations, we point out that knot 942 here is the mirror
image of 942 from [56]. The superpolynomial of 942 is given by17 [3]:
=
q−6t−2 + q−4t−1 + q−2 + 1 + 2t + q2t2 + q4t3 + q6t4 .
All generators of the homology of thin knots have the same value of the δ-grading.
However, for 942, the generator 1(= a0q0t0) has δ-grading 0, while the remaining 8
generators have δ-grading equal to −1.
17Note that the a and q gradings that we are using in this paper are half of those from [3],
see Remark A.1
38
SERGEI GUKOV AND MARKO STOˇSI´C
As for 819, here it is the mirror image of 819 from the Knot Atlas [56]. This
knot is also known as the positive (3,4)-torus knot. Its superpolynomial is given
by:
P (819)(a, q, t)
=
a3q−3 + a4q−2t3 + a3q−1t2 + a4t5 + a3qt4 + a4q2t7 + a4q3t6 +
+a5t8 + a4q−1t5 + a4q1t7 + a3t4.
The ﬁrst seven generators have δ-degree equal to −3, while the remaining four have
δ-grading equal to −2.
Before explaining the result for the S2-homology, we ﬁrst consider the Kauﬀman
homologies.
B.0.1. Kauﬀman homology of 819 and 942. The Kauﬀman polynomial of 942
can be written as:
(B.2)
F(942)(a, q) = 1+(1−a−1q)(1+a−1q−1)(1−a−2)·a2(q−6−q−4+q−2+q2−q4+q6).
The Kauﬀman homology of 942 that we have computed has 209 generators. We
present its Poincar´e polynomial in a structured form:
PKauﬀ(942)(a, q, t)
=
1 + (1 + a−1qt−1)(1 + a−1q−1t−2)(1 + a−2t−3) ×
×{a2(q−6t2 + q−4t3 + q−2t4 + q2t6 + q4t7 + q6t8) +
+(1 + t)

(a3 + at−3)(q−3t4 + q−1t5 + qt6 + q3t7) + 2a2t4
}
The Kauﬀman polynomial of 819 can be written as:
F(819)(a, q) = (a6 −a8)(q−6 + q−2 + 1 + q2 + q6) + (a7 −a9)(q−5 −q5) + a10.
The Kauﬀman homology of 819 that we have computed has 89 generators. Its
Poincar´e polynomial is given by:
PKauﬀ(819)(a, q, t)
=
(a6 + a8t3)(q−6 + q−2t2 + t4 + q2t4 + q6t6) +
+(a7 + a9t3)(q−5t2 + q5t7) + a10t10 +
+(1 + t−1)(a7q−1t5 + a7q1t6 + a8t7 + a9q−1t8 + a9q1t9) +
+(1 + t−1)(1 + a−1qt−1)(1 + a−2t−3)(1 + a−1q−1t−2) ×
×(a13q−1t14 + a13q1t15 + a11q−3t10 + a11q3t13).
Both results meet the desired properties of the Kauﬀman homology (see Section
6 of [6]):
• Specialization to t = −1 gives the Kauﬀman polynomial:
PKauﬀ(a, q, t = −1) = F(a, q).
• There exist three canceling diﬀerentials d2, d1 and d0 of degrees (−1, 1, −1),
(−2, 0, −3) and (−1, −1, −2), respectively. Indeed, from the form we write
PKauﬀ(942), it is obvious that only 1 = a0q0t0 survives in the homology
with respect to any of these diﬀerentials. As for HKauﬀ(819), the surviving
generators for d2, d1 and d0 respectively have degrees (6, −6, 0), (12, 0, 12)
and (6, 6, 6), as expected since the S-invariant for 819 is S(819) = 6.
• There exist two universal diﬀerentials d→and d←of degrees (0, 2, 1) and
(0, −2, −1), such that the homology with respect to these diﬀerentials is
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES
39
−6
−5
−4
−3
−2
−1
0
1
2
3
4
5
q
6
a
11
12
13
7
8
9
6
10
Figure 5. The reduced Kauﬀman homology of the knot T3,4 =
819. To avoid clutter, we show only canceling diﬀerentials d2, d1
and d0 (represented by red, green, and blue arrows, respectively).
isomorphic (up to regrading) to the triply-graded HOMFLY homology.
More precisely, they satisfy:
(HKauﬀ, d→) = P (a2q−2, q2, t),
(HKauﬀ, d←) = P (a2q2t2, q2, t).
Again, it is straightforward to check that such diﬀerentials exist in both
homologies HKauﬀ(942) and HKauﬀ(819).
• There exists a diﬀerential d−2 of degree (−1, −3, −3), such that the a =
q−3 specialization of the homology (HKauﬀ, d−2) is isomorphic to the ho-
mology Hsp(2),V .
Moreover, the triply-graded version holds: the Poincar´e polynomial
of the triply-graded homology (HKauﬀ, d−2) is equal to tSR(a1/2q−1/2, t),
where R(q, t) = P (a = q2, q, t). This is true for 819, 942 and for all prime
knots with up to 6 crossings.
Note that this generalizes and corrects the value predicted in [6]. We
also note that (HKauﬀ, d−2) is signiﬁcantly smaller than HKauﬀ: for 819 it
has only 11 generators, and for 942 it has only 9 generators.
• Finally, although not explicitly stated in [6], the Kauﬀman homology
enjoys the symmetry q ↔q−1:
HKauﬀ
i,j,∗
∼= HKauﬀ
i,−j,∗.
40
SERGEI GUKOV AND MARKO STOˇSI´C
B.0.2. S2-colored homologies of 819 and 942. In order to present the Poincar´e
polynomial of the S2-colored homology of 942 in a nice form and to show that all
the expected properties are satisﬁed, we write it in the following structured form:
P
(942)(a, q, t) =
= {1 + (1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3)(1 + a−1t−1)(a2q6t8 + a2t4)} +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3)(a2q2t6 + aq3t5) +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(aq−1t2 + aqt4) +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3) ×
×(a2q2t6 + aq3t6 + aq3t5 + 2aqt5 + at4 + qt4 + t3) +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3)(1 + t−1) ×
×(a2q4t8 + aq4t7 + a2qt6 + aq2t5 + q3t5 + at4 + t3).
Similarly, for 819 we have
P
(819)(a, q, t) =
= {(1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3)(a10q8t16 + a9q8t15) +
+(1 + a−1qt−1)(1 + a−1q−2t−3)(a8q−1t6 + a8q5t10 + a8q11t14) + a6q−6 +
+(1 + a−1qt−1)(a7q−4t3 + a7q−1t5 + a7q2t7 + a7q5t9 + a7q8t11 + a7q11t13)} +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(a8q2t8 + a8q6t10 + a8q8t12 + a8q9t14) +
+(1 + q)(1 + a−1qt−1)(1 + a−1q−2t−3)(1 + a−1q−3t−3)(a9q3t11 + a9q6t13 + a9q9t15).
The two homologies from above and their mirror images satisfy a large part
of the properties of the S2-colored homology from Conjecture 4.2 and of the Λ2
homology from Section 5:
• There exist canceling diﬀerentials d1
and d−2 of degrees (−1, 1, −1) and
(−1, −2, −3), respectively. The remaining generator for both diﬀerentials
is a0q0t0 = 1 in the case of 942, whereas for 819 the remaining generators
have degrees (6, −6, 0) and (6, 12, 12), respectively.
• There exists colored diﬀerential d2→1 of degree (0, 1, 0), such that the
homology with respect to it is equal to P (a2, q2, t2q).
• P
(a, q, t = −1) is equal to the S2-colored HOMFLY polynomial.
• There exists a diﬀerential d−3 of degree (−1, −3, −3), such that the ho-
mology with respect to it is very small. In the case of 942 it has only 9
generators:
(B.3) (H
(942), d−3) = a(q−1t2+qt4)+(q−2t−1+1+2t+q2t3)+a−1(q−1t−2+q),
while in the case of 819 we have
(H
(819), d−3)
=
(a6q12t12 + a7q11t13 + a6q10t10 + a7q9t11 + a6q8t8 + a7q7t9 +
+a6q6t6) + (a8q10t14 + a7q9t11 + a7q11t13 + a6q10t10).
(B.4)
Note that from the formulas for P
, for both knots, the last two lines
have a factor (1 + a−1q−3t−3) and so the corresponding homology gets
canceled automatically by d−3. Thus, it is enough to check the above for-
mulas only for the remaining part, which is a straightforward computation.
HOMOLOGICAL ALGEBRA OF KNOTS AND BPS STATES
41
• There exists a diﬀerential d0
of degree (−1, 0, −1) such that the homol-
ogy with respect to it is equal to aSP (a, q2, t).
• There exists a diﬀerential d2
of degree (−1, 2, −1) such that the homology
with respect to it, after specializing a = q2, is isomorphic to Hsl(2),
.
The latter one is isomorphic to Hso(3),V , where V denotes the vector
representation of so(3), and to obtain its Poincare polynomial we use
the result for the Kauﬀman homology we computed in section B.0.1. In
particular, for both knots we have that
P2 (q, t) = Pso(3),V (q, t) = PKauﬀ(a = q2, q, t).
Now, the “mirror image” of H
is also behaving quite well. To that end, let
H
be a homology obtained from H
as in Section 5:
Hi,j,k ∼= Hi,−j,k′.
The transformation k 7→k′ depends also on δ′-grading.
Since for H
of 942 and 819 the properties of the S2-colored homology listed
above are satisﬁed, it can be easily seen (by “mirroring” the diﬀerentials) that
the mirror homology H
obtained in this way satisﬁes the properties of the anti-
symmetric Λ2-colored homology:
• There exist canceling diﬀerentials d−1 and d2 of degrees (−1, −1, −3) and
(−1, 2, −1), respectively.
• There exists colored diﬀerential d2→1 of degree (0, 1, 0), such that the ho-
mology with respect to it has Poincar´e polynomial equal to P (a2, q4, t2q−1).
• P (a, q, t = −1) is equal to the Λ2-colored HOMFLY polynomial.
• There exists a diﬀerential d3 of degree (−1, 3, −1) such that the homology
of H
with respect to it is isomorphic to H , both specialized to a = q3.
The last property in fact holds even on the level of triply-graded
homologies (without specialization a = q3), as can be seen from (B.3)
and (B.4). We also note that the isomorphism of (H , d3 ) and H
as
triply-graded theories, also holds for all prime knots with up to 6 crossings.
