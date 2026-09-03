---
doc_id: arxiv-2509.04267v3
doc_title: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY"
section_id: sec-012-24-masahico-saito-and-emanuele-zappala
section_title: "MASAHICO SAITO AND EMANUELE ZAPPALA"
section_number: 24
pages: 24-26
source_pdf: 2509.04267v3.pdf
source_sha256: 9843b9dd71d1ec74
doc_brief: "QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY — Yang-Baxter operators (YBOs) have been employed to construct quantum knot invari- ants."
---
the bracket skein relation. In the second line, the skein relation for the YB 2-cocycleϕis applied.
This computation is carried out for all the eight terms of the 2-cocycle condition in Figure 4, and
set equal to zero. The expressions is written in like terms with respect to the basis elements of
the Temperley-Lieb algebra (e.g. [13]) as depicted in Figure 20, and the coefficient of each basis
element is set equal to zero. The coefficients of the elements (A), (D) and (E) cancel. Those for
(B) and (C) each gives the identical condition 2(A 4−1)B= 0, which is among the hypotheses for
the choice ofAandB. The case for ˜R−1 is the same due to the symmetry in the definitions.□
A−2
A2
B BB B BA−2B B B
A2
Figure 19
(E)(A) (B) (C) (D)
Figure 20
Proposition 7.4.Letkbe a unital ring that contains an invertibleAandB, ¯B,C, ¯C. The YBOs
˜Rand ˜R−1, together with undeformed ˜∪=∪and ˜∩=∩define a quantum cocycle knot invariant
up to regular isotopy if the following hold:
B=C, ¯B= ¯C, ¯B=−A −2B,2(A 4−1)B= 0.
Proof.This follows from Lemma 7.1, Lemma 7.2 and Lemma 7.3.□
ΒΑ −1 h Α −2 Β
Α −1 h Α −2 ΒΑ Β
Α
Figure 21
Definition 7.5.We normalize the regular isotopy invariant defined in Proposition 7.4 by dividing
it by the valueδ=−A 2−A−2 of the unknot , and denote the normalized regular isotopy invariant
by ΦM
( ˜R,˜∪,˜∩)(K). Therefore, we have that Φ M
( ˜R,˜∪,˜∩)( ) = 1.
QUANTUM COCYCLE INVARIANTS OF KNOTS FROM YANG-BAXTER COHOMOLOGY 25
The supersctript M stands for maxima/minima. We note that since ˜∪and ˜∩are undeformed, the
value of does not contain any terms inℏ, and therefore no new restrictions onAandBare added,
as the invertibility of the normalizing factor does not depend on the deformation coefficients.
We examine the effect of writhe to normalize the regular isotopy invariant to obtain an isotopy
invariant for oriented knot diagrams, as in the case of the bracket polynomial. LetDbe an oriented
diagram.
It has been assumed in this section that knots are unoriented. To make a normalization by
writhe, from here on we pick and fix an orientation. In Figure 21 left-hand side, two types of small
kinks are depicted. For the top figure, either choice of orientation gives a positive crossing for
oriented diagrams, and a negative crossing for the bottom figure.
Lemma 7.6.LetDbe a diagram of an oriented knot obtained fromD ′ by type I Reidemeister
move of removing a small kink as in Figure 21 top (resp. bottom) left. Set
w+ :=−A 3−ℏBA−2(A4 + 2),andw − :=−A−3 +ℏB(A−4 + 2).
Then we have, respectively,Φ M
( ˜R,˜∪,˜∩)(D′) =w +ΨM
( ˜R,˜∪,˜∩)(D)andΦ M
( ˜R,˜∪,˜∩)(D′) =w−ΨM
( ˜R,˜∪,˜∩)(D).
Proof.Diagrammatic computations are shown in Figure 21 top and bottom right, respectively.□
We note that the above two coefficients should yield 1 when multiplied, and indeed we find
w+·w− = [−A 3−ℏBA−2(A4 + 2)][−A−3 +ℏB(A−4 + 2)]
= 1−ℏB(A 3((A−4 + 2)−A −3A−2(A4 + 2))
= 1−ℏB[2A −5(A8−1)],
moduloℏ 2, and 2(A 8−1)Bis divisible by 2(A 4−1)B, one of the equalities in Lemma 7.4, as
expected. Hence we treat thatw + andw− are inverses each other ink.
By the writhe normalization argument, we obtain the following.
Theorem 7.7.LetDbe an oriented knot diagram with the number of positive (resp. negative)
crossingsp(D)(resp.n(D)). Then
ΦW
( ˜R,˜∪,˜∩)(D) =w−p(D)
+ w−n(D)
− ΦM
( ˜R,˜∪,˜∩)(D)
is independent of choice ofDand indeed is an invariant up to isotopy, thus denoted byΦ W
( ˜R,˜∪,˜∩)(K)
and simplyΦ W(K).
The superscript W stands for writhe-normalized. We also use the notation Φ W(K) = ΦW0(K) +
ℏΦW1(K). Sincew + andw− are inverses of each other, we can also write the prefix powers to be
wp(D)
− wn(D)
+ .
Lemma 7.8.LetT m be a(2,m)torus knot or knot for positive integersm, as depicted in Figure 9.
Then we haveΦ M(T1) =w +,Φ W(T1) = 1and
ΦM(Tm+1) = (A+ℏB)Φ M(Tm) + (A−1−ℏA 2B)wm
+,(16)
ΦW(Tm+1) = (A+ℏB)w −ΦW(Tm) + (A−1−ℏA 2B)w−.(17)
Proof.Equation (16) follows from the definitions and the deformed bracket skein. Since
ΦW(Tm) =w−m
+ ΦM(Tm) =w m
− ΦM(Tm),
by multiplying both sides byw m+1
− , we obtain Equation (17).□
