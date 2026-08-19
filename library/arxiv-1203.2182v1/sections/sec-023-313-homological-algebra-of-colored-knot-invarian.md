---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-023-313-homological-algebra-of-colored-knot-invarian
section_title: "Homological algebra of colored knot invariants"
section_number: 3.1.3
pages: 26-28
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
Our next goal is to describe a very rich structure of the color ed superpolynomials that can be
used either as an alternative way to compute them or as a tool to verify their correctness. As in
the previous discussion and in most of the literature on this subject [53, 54, 27], P R(K;a,q,t )
stands for the reducedsuperpolynomial of a knot K colored by R, and its unreduced version
is denoted with a bar.
Suppose, for example, that we wish to compute the S2-colored HOMFLY homology
HS2
i,j,k(T 2,5) and the corresponding superpolynomial P S2
(T 2,5;a,q,t ) of the (2, 5) torus knot,
also known as the knot 51. By deﬁnition (3.7), at t = −1 the colored superpolynomial reduces
to the colored HOMFLY polynomial (3.6), which for the knot T 2,5 has 25 terms, see e.g. [55]:
P S2
(T 2,5;a,q ) = a6(
q +q4 +q5 +q7)
(3.72)
+a5(
−q−2 −q−1 −q − 2q2 −q3 −q4 − 2q5 −q6 −q7 −q8)
+a4(
q−4 +q−1 + 1 +q2 +q3 +q4 +q5 +q6 +q8)
.
Each terms in this expression comes from a certain generator of the triply-graded colored
HOMFLY homology HS2
i,j,k(T 2,5), cf. Figure 2. Therefore, we conclude that HS2
i,j,k(T 2,5) must
be at least 25-dimensional. How can we restore the homologic al t-grading?
There are many ways to do that, based on the structure of the co mmuting diﬀerentials
(3.54). For instance, one way is to pick a relation in the inﬁn ite set (3.53) labeled by N ∈ Z,
and to study its implications. Thus, in our present example, the relation (3.53) with N = 2
says that the homology of HS2
i,j,k(T 2,5) with respect to the diﬀerential d2 should be isomorphic
to the S2 colored sl(2) homology Hsl(2),S2
i,j (T 2,5),
(
HS2
∗,∗,∗(K),d 2
)
∼
= Hsl(2),S2
∗,∗ (K) ∼
= Hso(3),V
∗,∗ (K), (3.73)
where in the last isomorphism we used the identiﬁcation between the symmetric representation
R = S2 of sl(2) and the 3-dimensional vector representation of so(3). The latter homology
was studied in [43], where explicit answers were tabulated f or all prime knots with up to 7
crossings.4 In particular, for the (2, 5) torus knot T 2,5 the homology Hso(3),V
i,j (K) is also 25-
dimensional, and by matching the results of [43] with the spe cialization P S2
(T 2,5;a =q2,q,t )
one can restore the t-grading of every term in (3.72):
P S2
(T 2,5;a,q,t ) = a6(
qt6 +q4t8 +q5t8 +q7t10)
(3.74)
+ a5(
q−2t3 +q−1t3 +qt5 + 2q2t5 +q3t5 +q4t7 + 2q5t7 +q6t7 +q7t9 +q8t9)
+ a4(
q−4 +q−1t2 +t2 +q2t4 +q3t4 +q4t4 +q5t6 +q6t6 +q8t8)
,
where we tacitly assumed that the entire S2-colored homology HS2
i,j,k(T 2,5) is indeed 25-
dimensional, so that Qsl(2),S2
= 0 in (3.9) for the present example. This can be easily
4It is not diﬃcult to extend these calculations to larger knot s, see e.g. [44] for the calculation of the
Kauﬀman homology for the (3 ,4) torus knot T 3,4 = 819.
– 25 –
justiﬁed by looking at the other diﬀerentials in (3.53) or the corresponding Poincar´ e polyno-
mials (3.9)–(3.10).
Everything we saw in this simple example can be easily genera lized to other knots (in
fact, not just torus knots) and other representations. As th e knot K is getting bigger, the
size of the colored HOMFLY homology HR
i,j,k(K) typically grows as well. At the same time,
for larger knots and larger homology more diﬀerentials act on HR
i,j,k(K) in an interesting way,
thus providing non-trivial constraints. Among the inﬁnite set of diﬀerentials in (3.54) there
are some special ones, which always act non-trivially, no ma tter how large or small the knot
K is. These are the so-called canceling diﬀerentials which get their name after the fact that,
when acting on HR
i,j,k(K), they cancel almost all of the terms, except a single one, i.e.
dim
(
HR(K),d canceling
)
= 1 . (3.75)
At ﬁrst, even the very existence of such diﬀerentials might se em very surprising. However,
they all usually have a simple origin and interpretation.
Let us consider, for example, the Sr-colored HOMFLY homology HSr
i,j,k(K) relevant to
the present paper. Then, as we already pointed out in the disc ussion below (3.8), the sl(1)
homology Hsl(1),Sr
i,j (K) should be trivial ( i.e. one-dimensional) for every knot K. When
combined with (3.53), this basic property implies that the d iﬀerential d1 must be canceling
for the Sr-colored HOMFLY homology HSr
i,j,k(K).
Another canceling diﬀerential in the same theory is d−r, whose origin is very similar:
the representation R = Λr of sl(N) is trivial when N = r. As a result, Hsl(r),Λ r
i,j (K) should
also be one-dimensional for every knot K, and from (3.56) it follows that d−r is also a
canceling diﬀerential for HSr
i,j,k(K). To summarize, in our standard conventions the canceling
diﬀerentials in the Sr-colored HOMFLY theory have degree
deg(d1) = (−1, 1, −1) and deg( d−r) = (−1, −r, −3). (3.76)
These canceling diﬀerentials pair up almost all of the terms in the Poincar´ e polynomial of the
homology HSr
i,j,k(K) which, therefore, has the structure (3.9):
P Sr
(K;a,q,t ) = arsq−rst0 + (1 +a−1qt−1)Q1(K;a,q,t )
= arsqr2st2rs + (1 +a−1q−rt−3)Q−r(K;a,q,t ), (3.77)
with a monomial “remainder” R(a,q,t ) = aiqjtk and (α,β,γ ) = ( −1, 1, −1) or ( −1, −r, −3)
for d1 or d−r, respectively. Since (3.77) is obtained by taking the Poinc ar´ e polynomial of
both sides in (3.75), the polynomials Q1 and Q−r have non-negative integer coeﬃcients.
Furthermore, the (a,q,t )-degrees of the “remainder” are determined by a single integers(K),
the so-called S-invariant of the knot K (see [44] for details).
The structure (3.77) is a “colored generalization” of the familiar property of the ordinary
HOMFLY homology [27] that corresponds to r = 1 and comes equipped with two canceling
diﬀerentialsd1 andd−1. In that context, the S-invariant is expected to provide a lower bound
– 26 –
on the slice 5 genusg∗(K) of the knot, which in our normalization reads
|s(K)| ≤ g∗(K) (3.78)
and is often tight. The slice genus of the ( p,q ) torus knot is [56, 57]:
g∗(T p,q) = (p − 1)(q − 1)
