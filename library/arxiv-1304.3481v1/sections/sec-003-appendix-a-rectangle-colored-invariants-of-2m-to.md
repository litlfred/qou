---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots"
section_id: sec-003-appendix-a-rectangle-colored-invariants-of-2m-to
section_title: "Appendix A. Rectangle-colored invariants of (2,m) torus knots"
section_number: null
pages: 68-75
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
doc_brief: "Quadruply-graded colored homology of knots — W e conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
As we use the quantum invariants of (2 , m) torus knots colored by the represen-
tations labeled by the rectangular Young diagrams in many examples t hroughout
the paper, we would like to provide a reader with a handy formula for t hem.
Let us ﬁrst recall the general formula for the colored invariants o f torus knots
[61, 75, 79 ]. Deﬁne the coeﬃcients cµ
λ,n by the equation
(A.1) sλ(xn
1 , xn
2 , . . .) =
∑
|µ|=n|λ|
cµ
λ,nsµ.
The λ-colored invariant of the ( n, m) torus knot can be expressed via the colored
invariants of the unknot by the following formula (we omit an overall s caling factor):
(A.2) P λ(T (n, m)) =
∑
|µ|=n|λ|
q− m
n κ(µ)cµ
λ,nP µ(
),
where κ(µ) =∑
(i,j)∈µ(i− j) = 1
2
∑
j µj(µj− 2j + 1) is the content of µ.
Therefore to compute P λ(T (m, n)), one just has to determine the “plethysm”
coeﬃcients cµ
λ,n.There is no closed formula for them for general λ, µ and n. However,
for n = 2 and λ = (SR), a simple formula for the coeﬃcients cµ
λ,n was found in [ 12].
A Young diagram µ = (µ1, . . . , µ2R) is called ( S, R)–balanced, if
µi + µ2R+1−i = 2S for all 1 ≤ i≤ R
Balanced diagrams are in 1-to-1 correspondence with splittings of t he S× R rec-
tangle into pairs of complimentary diagrams, as shown on Figure 22.
For an ( S, R)–balanced diagram µ, let sgn( µ) = (−1)|β| = (−1)
∑ R
i=1 µi . Let
B(S, R) denote the set of ( S, R)–balanced diagrams. By [ 12, Theorem 1], one has
s(SR)(x2
1, x2
2, . . .) =
∑
µ∈B(S,R)
(−1)sgn(µ)sµ,
11e.g. the characteristic variety of the corresponding q-diﬀerence equations has a nice inter-
pretation as the moduli space of SUSY parameters, etc.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 69
α
β
α
β
Figure 22. Diagram µ is balanced if diagrams α and β ﬁll the rectangle
hence
(A.3) cµ
(SR),2 =
{
(−1)sgn(µ), if µ∈ B(S, R),
0, otherwise .
The equations (A.2) and (A.3) determine the invariant P (SR)(T (2, m)) completely.
Appendix B. Unreduced colored HOMFL Y homology
B.1. General structure. As explained in Section 2.1, the unreduced λ-colored
homology
H
λ
(K) for any rectangular diagram λ and any knot K is a free mod-
ule over the unreduced λ-colored homology of the unknot H
λ
(U ). Therefore, for
every knot K the unreduced homology H
λ
(K) is determined by the reduced ho-
mologyHλ(K) and the unreduced homology of the unknot H
λ
(U ). In terms of the
corresponding Poincare polynomials we have:
(B.1)
P
λ
(K) =P λ(K)P
λ
(U ).
Hence, the unreduced colored homology is determined by the reduc ed one.
In order to simplify the presentation, we focus on the symmetric re presentations
λ = Sr.
Some of the properties of reduced homology extend to the unredu ced case: these
include the existence and the behaviour of the positive colored diﬀer entials and the
totally reﬁned exponential growth property. By (B.1) these prop erties will follow
from the fact the unreduced homology of the unknot satisﬁes the se properties.
The unreduced colored homology of the unknot is described in Sectio n 2.2 in
terms of the bosonic and fermionic generators. Their expicit ( a, Q, tr, tc)-gradings
70 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
have been obtained, which gives the following Poincare polynomial of t he tilde-
version of the unreduced Sr-colored homology of the unknot:
(B.2) ~P
Sr
(U )(a, Q, tr, tc) = a−rQr
r∏
i=1
1 + a2trt2i−1
c
1− Q2t2i−2c
.
In “standard” ( a, q, tr, tc)-gradings we have (the same convention, Q = q + tr− tc,
holds for the symmetric representations as in the case of the redu ced homology):
(B.3) P
Sr
(U )(a, q, tr, tc) = a−rqr
r∏
i=1
1 + a2q2i−2trt2i−1
c
1− q2it2i−2c
.
The degrees of the positive colored diﬀerentials are as in the reduce d case:
(B.4) ( a, q, tr, tc)[dcol
1|k] = (−2, 2(1− k),−1,−2k− 1), 0≤ k < r.
They also have the “colored” property, i.e. we have:
(B.5) H∗(
H
Sr
(K), dcol
1|k)∼
=
H
Sk
(K), 0≤ k < r.
Indeed, the last follows from the following Lemma which shows that (B .5) holds
for the unknot and with the re-gradings in the corresponding isomo rphisms being
exactly the same as for the reduced homology (Section 3.5):
Lemma B.1. For all nonnegative integers r and k, with k < r , we have that
the following holds
(B.6) ~
P
Sr
(U )(a, Q, tr, tc)−~P
Sk
(U )(a, Qtr−k
c , tr, tc) = (1 + a−2Q2t−1
r t−2k−1
c )X,
for some Laurent polynomial X(a, Q, tr, tc) whose all coeﬃcients are nonnegative
integers, i.e. X∈ Z+[a±1, Q±1, t±1
r , t±1
c ].
Proof: Straightforward computation.
The totally reﬁned exponential growth property also holds for the unreduced
homology of the unknot. Indeed:
(B.7)
~
P
Sr
(U )(a, Q, tr = t, tc = 1) =
r∏
i=1
1 + a2t
1− Q2 =
(
~P (U )(a, Q, tr = t, tc = 1)
) r
.
On the other hand there are some diﬀerences between the reduce d and unre-
duced homology of any knot.
The ﬁrst clear distinction from the reduced case is that the unredu ced homology
is inﬁnite-dimensional, since such is the unreduced homology of the un knot. In
particular there can be no symmetry that inverts the Q, or q-grading and therefore
the selfsymmetry is not satisﬁed for the unreduced homology. Con sequently, there
are no negative colored diﬀerentials in this case (recall that selfsym metry exchanges
positive and negative colored diﬀerentials).
The second distinction from the reduced homology case is that all diﬀ erentials
dn|0, for n > 0, are nontrivial now, even for the unknot. This is the reason why
there is no such a simple relation like (B.1) between the unreduced and reduced
sl(n) homology. In the next section we compute sl(n) colored HOMFLY homology
for some simple knots.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 71
B.2. sl(n) colored HOMFL Y homology .The unreduced (sl(n), Sr)-colored
homology of a knot K, denoted H
sl(n),Sr
(K), is obtained as the homology of
H
Sr
(K) with respect to dn|0, followed by collapsing of grading by setting a = qn.
We observeH
Sr
(K) here as triply-graded theory in ( a, q, tc)-gradings, and also to
simplify the notation we denote tc simply by t. Therefore, H
sl(n),Sr
(K) becomes
doubly-graded theory in ( q, t)-degrees.
Unlike the reduced homology case, here all diﬀerentials dn|0, with n > 0, are
highly nontrivial, even for the unknot. Below we compute sl(2) homologies for the
fundamental and the second-symmetric representation of the u nknot, trefoil and
the ﬁgure-eight knot.
The (a, q, t)-degrees of the sl(n) diﬀerentials, dn|0, n > 0, are as for the reduced
homology:
(B.8) ( a, q, t)[dn|0] = (−2, 2n,−1), n > 0.
For all three knots we assume that dn|0 is such that it cancels all pairs of
generators of
H
Sr
(K) whose ( a, q, t)-degrees diﬀer by (−2, 2n,−1).
B.2.1. Unknot. In the fundamental representation, we have that the Poincare
polynomial of the unreduced uncolored HOMFLY homology is given by:
P (U )(a, q, t) = a−1q 1 + a2t
1− q2 .
Then the homology with respect to dn|0 is ﬁnite-dimensional for any n:
(B.9) ( H (U ), dn|0) = a−1q(1 + q2 + . . . + q2(n−1)).
Finally, after collapsing the tri-grading by setting a = qn, we get the familiar
expression for the uncolored sl(n) homology of the unknot:
(B.10) P
sl(n),
(U )(q, t) = (H (U ), dn|0)|a=qn = q1−n + q3−n + . . . + q(n−1).
The S2-colored unreduced homology of the unknot is given by:
(B.11) P (U ) = a−2q2 (1 + a2t)(1 + a2q2t3)
(1− q2)(1− q4t2) .
To simplify the further computation of the homology with respect to d2|0 in terms
of the Poincare polynomial, we say that P1 is equal to P2 modulo d2|0 if P1− P2 =
(1 + a−2q4t−1)Y for some Laurent polynomial Y in variables a, q and t whose all
coeﬃcients are nonnegative integers.
Then by using the result from the uncolored case, we have that mod ulo d2|0
the expression (B.11) equals to:
a−2q2(1 + q2) 1 + a2q2t3
1− q4t2 = (1 + q2 + q4t2 1 + a2t
1− q4t2 ) + (1 + a−2q4t−1) a2q2t3
1− q4t2 .
Therefore:
(B.12) (
H (U ), d2|0) = a−2q2(1 + q2 + q4t2 1 + a2t
1− q4t2 ),
and so
(B.13)
P
sl(2),
(U )(q, t) = (H (U ), d2|0)|a=q2 = q−2 + 1 + q2t2 1 + q4t
1− q4t2 .
72 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
B.2.2. Trefoil. For the trefoil, we have:
(B.14) P (31) =P (31)P (U ) = ( a2q−2 + a2q2t2 + a4t3)a−1q 1 + a2t
1− q2 .
Now after taking the homology with respect to d2|0 which cancels all pairs of gen-
erators which diﬀer in ( a, q, t)-degree by (−2, 4,−1), we are left with
(B.15) ( H (31), d2|0) = a(q−1 + q + q3t2) + a3q3t3,
which after setting a = q2 gives
P
sl(2),
(31)(q, t) = (H (31), d2|0)|a=q2 = q + q3 + q5t2 + q9t3,
which equals precisely the free part of the (unreduced) Khovanov homology of the
trefoil.
For the second-symmetric representation, we have:
(B.16) P (31) =P (31)P (U ),
where the reduced homology of the trefoil was computed in Section 4:
(B.17) P (31) = a4(q−4 +q2t4 +q4t6 +q8t8)+ a6(t5 +q2t7 +q6t9 +q8t11)+ a8q6t12.
As we have seen above, the Poincare polynomial of the unknot P (U ) modulo d2|0
equals
(B.18) (
H (U ), d2|0) = a−2(q2 + q4 + q6t2 1 + a2t
1− q4t2 ).
As for the the reduced S2-colored Poincare polynomial of the trefoil, P (31), we
split it according to the canceling diﬀerential dcol
0|2:
(B.19) P
(31) = (1 + a2q4t5)(a4q−4 + a4q2t4 + a4q4t6 + a6q2t7) + a4q8t8.
Multiplying the factor (1 + a2q4t5) with the RHS of (B.18) gives:
(1 + a2q4t5)a−2(q2 + q4 + q6t2 1 + a2t
1− q4t2 ) =
= (1 + a2q4t5)a−2(q2 + q4) + a−2q6t2(1 + a2q4t5) 1 + a2t
1− q4t2 ) =
= (1 + a2q4t5)a−2(q2 + q4) +
+ a−2q6t2(1 + a2t + q4t2 + a2q4t3 + (1 + a−2q4t−1)a2q4t5 1 + a2t
1− q4t2 ) =
= a−2q2(1 + q2 + q4t2 + a2q4t3 + a2q6t5 + a2q8t5) +
+ (1 + a−2q4t−1)(q6t5 + q10t7 1 + a2t
1− q4t2 ).
Therefore, after replacing this in (B.16), we have that P (31) modulo d2|0 equals:
a−2q2(1 + q2 + q4t2 + a2q4t3 + a2q6t5 + a2q8t5)(a4q−4 + a4q2t4 + a4q4t6 + a6q2t7) +
+a2q8t8(q2 + q4 + q6t2 1+a2t
1−q4t2 ).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 73
By canceling all possible remaining pairs of generators by d2|0 we get:
(H (31), d2|0) = a2(q−2 + 1) + a2q2t2 + a4q2t3 +a2(q4 + q6)t4 +a4(q4 + q6)t5 +
+ a4(q6 + q8)t7 + a2q10t8 + a4q10t9 + a4q12t11 + a6q12t12 +
+a2q6t6(1 + q2 + q4t2 1 + a2t
1− q4t2 ).
Finally, by setting a = q2, we obtain the following ( sl(2), S2)-colored homology of
the trefoil:
P sl(2), (31)(q, t) = ( H (31), d2|0)|a=q2 =
= (q2 + q4) + q6t2 + q10t3 + (q8 + q10)t4 + (q12 + q14)t5 +
+(q14 + q16)t7 + q14t8 + q18t9 + q20t11 + q24t12 +
+q10t6(1 + q2 + q4t2 1 + q4t
1− q4t2 ).
We note that this result for the free part of the homology coincides (up to an overall
shift) with the one obtained in [ 15]. 12
B.2.3. Figure-eight knot. Similarly, for the ﬁgure-eight knot, we have
(B.20) P (41) =P (41)P (U ) = ( a2t2 + q−2t−1 + 1 +q2t + a−2t−2)a−1q 1 + a2t
1− q2 .
After taking homology with respect to d2|0 (i.e. modulo (1 + a−2q4t−1)), we get
(B.21) ( H (41), d2|0) = a2qt2 + q−1(t−1 + 1) + q(1 + t) + a−2q−1t−2,
and after setting a = q2, we are left with
(H (41), d2|0)|a=q2 = q5t2 + qt + q + q−1 + q−1t−1 + q−5t−2,
which is the free part of the (unreduced) Khovanov homology of th e ﬁgure-eight
knot.
For the second-symmetric representation we have:
(B.22) P (41) =P (41)P (U ),
where the reduced S2-homology is already computed in Section 4
P (41) = 1 + (1 + q2t2)a−2q−2t−4(1 + a2q−2t)(1 + a2q4t5) +
+a−4q−4t−8(1 + a2q−2t)(1 + a2t3)(1 + a2q4t5)(1 + a2q6t7).
In the same way as above for the trefoil, after grouping all terms w ith the factor
1 + a2q4t5 and multiplying with the RHS of (B.18), we get that modulo d2|0 the
12Note that the so(3) homology corresponding to the fundamental representat ion that is
computed in [ 15] is indeed isomorphic to the homology Hsl(2), , due to the well-known iso-
morphism between the fundamental (vector) representation of so(3) and the second-symmetric
representation of sl(2).
74 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
polynomialP (41) equals to:
a−2q2(1+ q2+q4t2 +a2q4t3 +a2q6t5 +a2q8t8)((1 + q2t2)(1 + a2q−2t)a−2q−2t−4 +
+a−4q−4t−8(1 + a2q−2t)(1 + a2t3)(1 + a2q6t7)) +
+a−2(q2 + q4 + q6t2 1+a2t
1−q4t2 ).
Finally, by canceling by d2|0 all possible remaining pairs of generators we get:
(H (41), d2|0) = a−4(t−4 + (q2 + q4)t−2 + q6) +
+a−2(t−3 + 2q2t−1 + q4(t−1 + t) + 2q6t + q8t3) +
+(q2 + (q4 + q6)t2 + q8t4) +
+a−6q−2t−8 + a−4(q−2t−7 + t−5 + q2t−3 + q4t−1) +
+a−2(t−4 + q2t−2 + 2q4 + q6t2 + q8t4) +
+(q4t + q6t3 + q8t5 + q10t7) + a2q10t8 +
+a−2q2(1 + q2 + q4 1 + a2t
1− q4t2 ).
After setting a = q2 in the above expression, we get the ( sl(2), S2)-colored homology
of the ﬁgure-eight knot:
P sl(2), (41)(q, t) = ( H (41), d2|0)|a=q2 =
= q−14t−8 + q−10t−7 + q−8t−5 + (q−8 + q−4)t−4 +
+(q−6 + q−4)t−3 + (q−6 + q−4 + q−2)t−2 +
+(q−4 + 2q−2 + 1)t−1 + (q−2 + 2 + q2) +
+(1 + 2q2 + q4)t + (q2 + q4 + q6)t2 + (q4 + q6)t3 +
+(q4 + q8)t4 + q8t5 + q10t7 + q14t8 +
+q−2 + 1 + q2t2 1 + q4t
1− q4t2 .
Again, the obtained homology matches the result from [ 15].
B.3. Comparison with the algebraic model. Following Section 2.6 and
[38], we can compare the above computations with the corresponding a lgebraic
models. Recall that the Sr-colored triply graded homology of the unknot has even
generators u1, . . . , ur and odd generators ξ1, . . . , ξr such that
[a, q, tc]ui = (0, 2i, 2i− 2), [a, q, tc]ξi = (2, 2i− 2, 2i− 1).
The diﬀerential d2|0 is deﬁned by the equation d2|0(ξi) =∑ j+1
i=1 ujui+1−j, in partic-
ular,
(B.23)
d2|0(ξ1) = u2
1, d 2|0(ξ2) = 2 u1u2, d 2|0(ξ3) = u2
2 + 2u1u3, d 2|0(ξ4) = 2 u1u4 + 2u2u3.
The uncolored HOMFLY homology of the unknot is a free algebra gene rated
by u1 and ξ1, so the uncolored sl(2) homology is two-dimensional and spanned by
1 and u1.
Using (B.23), one can check that the ( S2, sl(2)) homology of the unknot is
spanned by
1, u 1, µ 1, u k
2, u k
2µ1, k ≥ 1,
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 75
where µ1 = 2 u2ξ1− u1ξ2. Note that the homology has nontrivial Z2-torsion that
we do not consider here, see [ 38] for more details.
The reduced triply graded homology of the trefoil is three-dimensio nal and
spanned by 1 , u2, ξ2. Therefore the uncolored sl(2) homology of the trefoil can be
considered as a quotient of ( S2, sl(2)) homology of the unknot by u2
2 and u2µ1,
hence it is spanned by 1 , u1, u2 and µ1.
Finally, let us consider the ( S2, sl(2)) homology of the trefoil. Following (5.13),
the reduced S2 HOMFLY homology of the trefoil is given by is spanned by
1, u 3, u 4, u 2
3, ξ 3, ξ 4, u 3ξ3, u4ξ3 =−u3ξ4, ξ 3ξ4.
For simplicity, let us focus on the bottom row. The unreduced S2 HOMFLY ho-
mology of the trefoil has form
⟨1, u 1, u k
2⟩⊗⟨ 1, u 3, u 4, u 2
3⟩.
Using (B.23), we can eliminate u1u3 and u1u4. Moreover,
u1u2
3 = d2|0
(1
2 u3ξ3− 1
4 x2ξ4 + 1
4 x4ξ2
)
,
u2
2u3 = d2|0
(1
2 x2ξ4− 1
2 x4ξ2
)
,
u2
2u4 = d2|0(ξ3u4− ξ4u3) + 2u2u2
3, u 3
2 = d2|0(u2ξ3− u3ξ2).
and can be eliminated too. Therefore the bottom row of the unredu ced ( S2, sl(2))
homology of the trefoil is spanned by
1, u 1, u 2, u 3, u 4, u 2
2, u 2u4, u 2u3, u k
2u2
3, k ≥ 0.
The homology of d2|0 on higher levels can be computed by similar methods.
