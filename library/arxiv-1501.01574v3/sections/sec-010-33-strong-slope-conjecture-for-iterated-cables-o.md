---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-010-33-strong-slope-conjecture-for-iterated-cables-o
section_title: "Strong Slope Conjecture for iterated cables of adequate knots"
section_number: 3.3
pages: 14-17
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
link diagram, and x a crossing of D. Associated to D and x are two link diagrams, each
with one fewer crossing than D, called the A–resolution and B–resolution of the crossing.
See Figure 1.
A Kauﬀman state σ is a choice of A–resolution or B–resolution at each crossing of D.
Corresponding to every state σ is a crossing–free diagram sσ : this is a collection of circles
in the projection plane. We can encode the choices that lead t o the state σ in a graph
Gσ , as follows. The vertices of Gσ are in 1 − 1 correspondence with the state circles of
sσ . Every crossing x of D corresponds to a pair of arcs that belong to circles of sσ ; this
crossing gives rise to an edge in Gσ whose endpoints are the state circles containing those
arcs.
Every Kauﬀman state σ also gives rise to a surface Sσ , as follows. Each state circle of σ
bounds a disk in S3. This collection of disks can be disjointly embedded in the b all below
the projection plane. At each crossing of D, we connect the pair of neighboring disks by a
half-twisted band to construct a surface Sσ ⊂ S3 whose boundary is K. See Figure 2 for
an example where σ is the all– B state.
Deﬁnition 3.5. A link diagram D is called A–adequate if the state graph GA correspond-
ing to the all– A state contains no 1–edge loops. Similarly, D is called B–adequate if the
all–B graph GB contains no 1–edge loops. A link diagram is adequate if it is both A– and
B–adequate. A link that admits an adequate diagram is also cal led adequate.
The number of negative crossings c− of an A–adequate knot diagram is a knot invariant.
Similarly, the number of positive crossings c+ of a B-adequate knot diagram is a knot
invariant. Let vA (resp. vB) be the number of state circles in the all– A (resp. all– B) state
of the knot diagram D.
The following summarizes [24, Lemma 5.4], [22, Proposition 2.1] and [19, Theorem 3.1].
15
Lemma 3.6. Let D be a diagram of a knot K.
(1) We have
2 d−[JK (n)] ≥ −c−n2 + (c − vA)n + vA − c+.
Equality holds for all n ≥ 1 if D is A–adequate. Moreover, if equality holds for some n ≥ 3
then D is A–adequate.
(2) We have
2 d+[JK (n)] ≤ c+n2 + (vB − c)n + c− − vB.
Equality holds for all n ≥ 1 if D is B–adequate. Moreover, if equality holds for some n ≥ 3
then D is B–adequate.
The following theorem, which implies that the Slope Conject ure is true for adequate
knots, summarizes results proved in [4, 5].
Theorem 3.7. Let D be an A–adequate diagram of a knot K. Then the state surface SA
is essential in the knot complement MK, and it has boundary slope −2c−. Furthermore,
we have
−2c− = lim
n→∞
4 n−2d−[JK (n)].
Similarly, if D is a B–adequate diagram of a knot K, then SB is essential in the knot
complement MK , and it has boundary slope −2c+. Furthermore, we have
2c+ = lim
n→∞
4 n−2d+[JK (n)].
By Lemma 3.6, the highest degree of the colored Jones polynom ial of a B-adequate knot
is an actual quadratic polynomial in n. That is the period is one. The following lemma
shows that the term b ≤ 0 and thus non-trivial B-adequate knots satisfy the hypothesis of
Proposition 3.2.
Lemma 3.8. Suppose D is a diagram of a non-trivial knot K. Then vB ≤ c. Furthermore,
if vB = c then K is a torus knot.
Proof. Let D be a diagram of a non-trivial knot and let SB be the all- B state surface
obtained from D. Recall that SB is a surface with a single boundary component obtained
by starting with vB disks and attaching a half-twisted band for each crossing of D. Thus
the Euler characteristic of SB is χ(SB) = vB − c. Since D represents a non-trivial knot,
we have χ(SB) ≤ 0 and thus vB ≤ c.
If χ(SB) = vB − c = 0, then (since ∂SB has one component) SB must be a Mobius band.
This implies that D is the standard closed 2-braid diagram of a (2 , q)-torus knot. □
The above discussion shows that the ﬁrst part of Theorem 3.4 a pplies to non-trivial
B–adequate knots. Similarly the second part of the theorem ap plies to non-trivial A–
adequate knots. We are now ready to prove the following theor em that implies Theorem
1.4 stated in the introduction.
Theorem 3.9. Let K be a B-adequate knot and K ′ := K(p1,q 1), (p2,q 2), ··· , (pr,q r) an iterated
cable knot of K. Then we have jsK ′ ⊂ bsK ′. Furthermore, for n ≫ 0,
d+[JK ′(n)] = An2 + Bn + D(n),
16
is a quadratic quasi-polynomial of period ≤ 2, with 4A ∈ Z, 2B ∈ Z and B ≤ 0, and there
is an essential surface S′ in the complement of K ′ with boundary slope 4A and such that
χ(S′) = 2 B. In particular K ′ satisﬁes the Strong Slope Conjecture.
Proof. Suppose K is a B–adequate knot. First, we prove that the conclusion of Theor em
3.9 holds true for the cable knot Kp1,q 1. We will distinguish two cases according to whether
K is a non-trivial knot or not.
Case 1. Suppose that K is non-trivial. Then, by Lemmas 3.6 and 3.8 we have
d+[JK (n)] = an2 + bn + d
for n > 0, where a = c+/2, b = ( vB − c)/2 ≤ 0 and d = ( c− − vB)/2. By Theorem 3.7,
4a = 2 c+ is a boundary slope of K. Furthermore, an essential surface that realizes this
boundary slope is the state surface SB. Since SB is constructed by joining vB disks with
c bands we have |∂SB| = 1 and χ(SB) = vB − c = 2b. Thus the conclusion is true in this
case.
Now we consider a cable Kp1,q 1 of K. Since |q1| > 1, and the Jones slopes of K are
integers, we have p1
q1
/∈ jsK . Theorem 3.4 and the proof of Proposition 3.2 then imply that
d+[JKp1,q1 (n)] = A1n2 + B1n + D1(n)
is a quadratic quasi-polynomial of period ≤ 2, with 4 A1 ∈ Z, 2B1 ∈ Z and B1 ≤ 0. More-
over, since jsK ⊂ bsK we have jsKp1,q1 ⊂ bsKp1,q1 . Furthermore, the proof of Proposition
3.2 show that one of the following is true:
(1) We have 4 A1 = pq and B1 = 0.
(2) We have 4 A1 = 4q2a and 2 B1 = 2|q|b + (1 − |q|)|4aq − p|.
In case (1), the surface S with boundary slope pq is the cabling annulus; thus χ(S) = 0 =
2B1. In case (2), an essential surface S realizing the boundary slope 4 A1 = 4q2a = 2q2c+
is obtained by Theorem 2.2. By Corollary 2.8 we have |∂S | = |∂SB| = 1 and χ(S) =
|q|χ(SB) + (1 − |q|)|4aq − p| = 2B1. Thus the conclusion follows for Kp1,q 1.
Case 2. Suppose that K is the trivial knot. Then Kp1,q 1 is the ( p1, q1)-torus knot. Note
that 0 and p1q1 are boundary slopes of Kp1,q 1; realized by a Seifert surface and an annulus
respectively.
For n > 0, by [25] (or by equation (3)) we have
JKp1,q1 (n) = vp1q1(n2−1)/ 4 ∑
k∈Sn
v−p1k(q1k+1) v(2qk+1)/ 2 − v−(2qk+1)/ 2
v1/ 2 − v−1/ 2 .
By [10, Section 4.8], [30, Lemma 1.4] and [29, Lemma 2.1], we h ave the following. If p1 > 0
and q1 > 0 then
d+[JKp1,q1 (n)] =
(
p1q1n2 + d(n)
)
/4
where d(n) = −p1q1 − 1
2
(
1 + (−1)n)
(p1 − 2)(q1 − 2) is a periodic sequence of period ≤ 2.
In this case we have A1(n) = p1q1/4 and B1(n) = 0.
If p1 < 0 < q 1 then
d+[JKp1,q1 (n)] =
(
(p1q1 − p1 + q1)n − (p1q1 − p1 + q1)
)
/2.
17
K jsK ∪ js∗
K b(n) b∗(n)
819 {12, 0} 0 5/2
821 {1, −12} −1 3/2
942 {6, −8} −1/2 5/2
945 {1, −14} −1 2
946 {2, −12} −1/2 5/2
947 {9, −6} −1 2
948 {11, −4} −3/2 3/2
949 {15, 0} −3/2 3/2
Table 1. The knots up to nine crossings of period two.
In this case we have A1(n) = 0 and B1(n) = ( p1q1 − p1 + q1)/2. Note that p1q1 − p1 + q1 =
1 + (p1 + 1)(q1 − 1) ≤ 0.
In both cases we have that
d+[JKp1,q1 (n)] = A1n2 + B1n + D1(n)
is a quadratic quasi-polynomial of period ≤ 2, with 4 A1 ∈ Z, 2B1 ∈ Z and B1 ≤ 0.
Moreover, we have
jsKp1,q1 ⊂ bsKp1,q1 .
For p1 > 0 and q1 > 0, an essential surface with slope p1q1 for Kp1,q 1 is the cabling
annulus A; thus χ(A1) = 0 = 2 B1. For p1 < 0 < q 1, the genus of Kp1,q 1 is g = −(q1 −
1)(p1 + 1)/2. A Seifert surface S of minimal genus for Kp1,q 1 has boundary slope 0 and
χ(S) = 1 − 2g = p1q1 − p1 + q1 = 2 B1. This proves the desired conclusion for the torus
knot Kp1,q 1.
We have proved that the conclusion of Theorem 3.9 holds true f or the cable knot Kp1,q 1.
Now, applying the arguments in Case 1 repeatedly will ﬁnish t he proof of the theorem for
iterated cables. □
3.4. Proof of Theorem 1.4. Part (1) is immediate from Theorem 3.9. Suppose now
that K is A-adequate. Then the mirror image K ∗ is B-adequate. Furthermore, JK ∗(n) is
obtained from JK(n) by replacing v with v−1. Thus in this case the result will follow by
applying Theorem 3.9 to K ∗.
