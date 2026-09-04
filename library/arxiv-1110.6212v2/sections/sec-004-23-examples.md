---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗"
section_id: sec-004-23-examples
section_title: "Examples"
section_number: 2.3
pages: 11-14
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
doc_brief: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗ — This paper has two main purposes."
---
Remark 2.7. Recently [6] Ram’s construction has been applied to study th e representation
theory of 1-parameter rank 2 aﬃne Hecke algebras with q a root of the Poincar´ e polynomial,
and analogously the above construction could be applied to t he study of such representations in
the multi-parameter case.
2.3 Examples
Let us give some concrete examples of the construction from T heorem 2.6. Most of these
examples will arise in the Plancherel Theorems in the later p arts of this paper (see Section 3).
Of interest, we see in the third and fourth examples that some non-calibrated modules (in the
single parameter case) can be constructed from calibrated m odules (of multi-parameter algebras)
by making an appropriate change of basis and taking a limit.
11
Example 1. Let H be a ˜C2 Hecke algebra with L = P and with parameters q1 and q2
(see Section 3.5). Let t ∈ Hom(P, C×) be the character with tω1 = −q−1
1 and tω2 = q−1/2
1 ,
so that tα∨
1 = q−1
1 and tα∨
2 = −1. Thus N (t)∨ = {α∨
1 , α∨
1 + 2 α∨
2 } and D(t) = ∅. Thus
there are 4 choices for subsets J ⊆ N (t). Let J ∨
1 = ∅, J ∨
2 = {α∨
1 }, J ∨
3 = {α∨
1 + 2α∨
2 }, and
J ∨
4 = {α∨
1 , α∨
1 +2α∨
2 }. We compute FJ1(t) = {1, s2}, FJ2(t) = {s1, s2s1}, FJ3(t) = {s1s2, s2s1s2},
and FJ4(t) = {s1s2s1, s1s2s1s2}, and so the calibration graph is as in Figure 1(a). Thus by
Theorem 2.6 and Proposition 2.3 there are 4 irreducible modu les with central character t, each
with dimension 2. For example, the matrices for the module MJ1(t) with respect to the basis
{et, es2t} are π(T1) = −q−1/2
1 I, π(xω1) = −q−1
1 I, and
π(T2) = q1/2
2
2
(1 − q−1
2 1 + q−1
2
1 + q−1
2 1 − q−1
2
)
π(xω2) = diag( q−1/2
1 , −q−1/2
1 ).
Note that π(xα∨
1 ) = q−1
1 I and π(xα∨
2 ) = −I, and it follows that the restriction π|HQ is not
irreducible (indeed π|HQ is the direct sum of the representations π4 and π5 from Section 3.4).
This does not contradict the irreducibility statement of Th eorem 2.6, because the calibration
graph changes if we use the lattice Q instead of P (see Example 2).
Example 2. Now let H be a ˜C2 Hecke algebra with L = Q. Let t ∈ Hom(Q, C×) be the
character with tα∨
1 = q−1
1 and tα∨
2 = −1 (note the similarity to Example 1). Then N (t) and
D(t) are as in Example 1. Let J1, J2, J3, J4 be as in Example 1, and then the sets FJi(t) are
as computed in Example 1. However now s2t = t, and so the calibration graph is as shown in
Figure 1(b). Thus Theorem 2.6 constructs 2 irreducible 1-di mensional modules, and 1 irreducible
2-dimensional module with central character t.
•
•
•
•
•
•
•
•
t
s1t
s2s1t
s1s2s1t
s2t
s1s2t
s2s1s2t
s1s2s1s2t
(a) Example 1: L = P
•
•
•
•
t = s2t
s1t = s1s2t
s2s1t = s2s1s2t
s1s2s1t = s1s2s2s1t
(b) Example 2: L = Q
Figure 1: Calibration graphs for Examples 1 and 2
Example 3. Let H be a ˜G2 Hecke algebra with L = Q = P and with parameters q1 and q2
(see Section 3.6). Let t ∈ Hom(Q, C×) be the character with tα∨
1 = q1 and tα∨
2 = q−1/2
1 q1/2
2 . If
q1 ⁄= q2 and q1 ⁄= q3
2 then this character is regular, and we compute N (t)∨ = {α∨
1 , α∨
1 + 2α∨
2 }.
Thus there are 4 choices for J ⊆ N (t), and the connected components of the calibration graph
are given by {wt | w ∈ FJ (t)} for these choices of J. Consider the case J ∨ = {α∨
1 + 2α∨
2 }. We
12
compute FJ (t) = {s2s1s2s1, s1s2s1s2s1, s2s1s2s1s2s1}. The matrices for π = MJ (t) are
π(T1) = q
1
2
1


1−q−1
1
1−q
1
2
1 q
− 3
2
2
1−q
− 3
2
1 q
3
2
2
1−q
− 1
2
1 q
3
2
2
0
1−q
− 1
2
1 q
− 3
2
2
1−q
1
2
1 q
− 3
2
2
1−q−1
1
1−q
− 1
2
1 q
3
2
2
0
0 0 −q−1
1


π(T2) = q
1
2
2


−q−1
2 0 0
0 1−q−1
2
1−q
1
2
1 q
− 1
2
2
1−q
1
2
1 q
− 3
2
2
1−q
− 1
2
1 q
1
2
2
0 1−q
− 1
2
1 q
− 1
2
2
1−q
1
2
1 q
− 1
2
2
1−q−1
2
1−q
− 1
2
1 q
1
2
2


π(xα∨
1 ) = diag( q
− 1
2
1 q
3
2
2 , q
1
2
1 q
− 3
2
2 , q−1
1 ) π(xα∨
2 ) = diag( q−1
2 , q
− 1
2
1 q
1
2
2 , q
1
2
1 q
− 1
2
2 )
The construction breaks down when q1 = q2 or when q1 = q3
2. These cases can be dealt with by
a suitable change of basis in the module MJ (t). Let
A =


1 0 0
0 1 −q
1
2
1 q
− 1
2
2
0 −1 1

 B =


1 −q
1
2
1 q
− 3
2
2 0
−1 1 0
0 0 1 − q
1
2
1 q
− 3
2
2

 .
After conjugating each representing matrix by A (respectively B) it is observed that the resulting
matrices are deﬁned at q1 = q2 (respectively q1 = q3
2). Setting q1 = q2 = q (respectively
q1 = q3 with q2 = q) gives a (non-calibrated) irreducible representation of t he algebra H (q, q)
(respectively the algebra H (q, q3)). For example, the matrices in the q1 = q2 = q case become
π(T1) = q
1
2


1 3
q−1
3
q−1
q+1
q
2q+1
q(q−1)
3
q−1
− q+1
q − 3
q−1 − 4q−1
q(q−1)

 π(T2) = q
1
2


−q−1 0 0
0 1 0
0 −2q−1 −q−1


π(xα∨
1 ) =


q 0 0
0 −2q−1 −3q−1
0 3 q−1 4q−1

 π(xα∨
2 ) =


q−1 0 0
0 3 2
0 −2 −1

 .
Example 4. Let H be a ˜C2 aﬃne Hecke algebra with either L = Q or L = P and with
parameters q1 and q2 (see Sections 3.4 and 3.5). Let t ∈ Hom(L, C×) be a character with tα∨
1 =
q−1
1 and tα∨
2 = q2. If q1 ⁄= q2 and q1 ⁄= q2
2 then the character t is regular, since tα∨
1 +α∨
2 = q−1
1 q2
and tα∨
1 +2α∨
2 = q−1
1 q2
2. Thus we compute N (t) = {α1, α2} and D(t) = ∅. There are 4 choices for
J ⊆ N (t), namely J1 = ∅, J2 = {α1}, J3 = {α2}, and J4 = {α1, α2}. We compute
FJ1(t) = {1}, F J2(t) = {s1, s2s1, s1s2s1}, F J3(t) = {s2, s1s2, s2s1s2}, F J4(t) = {s1s2s1s2}.
The sets {wt | w ∈ FJi(t)} with i = 1 , 2, 3, 4 are the connected components of the calibration
graph of t. Thus there are 4 irreducible modules MJi(t) ( i = 1, 2, 3, 4) with central character t,
with dimensions 1 , 3, 3, 1 respectively.
Consider the module MJ3(t) (this module will appear in the Plancherel Theorem for ˜C2).
The matrices of T1, T2, xα∨
1 and xα∨
2 relative to the basis es2t, es1s2t, es2s1s2t are
π(T1) = q
1
2
1


1−q−1
1
1−q1q−2
2
1−q−2
1 q2
2
1−q−1
1 q2
2
0
1−q−2
2
1−q1q−2
2
1−q−1
1
1−q−1
1 q2
2
0
0 0 −q−1
1

 π(T2) = q
1
2
2


−q−1
2 0 0
0 1−q−1
2
1−q1q−1
2
1−q−1
1
1−q−1
1 q2
0 1−q1q−2
2
1−q1q−1
2
1−q−1
2
1−q−1
1 q2


π(xα∨
1 ) = diag( q−1
1 q2
2, q1q−2
2 , q−1
1 ) π(xα∨
2 ) = diag( q−1
2 , q−1
1 q2, q1q−1
2 ).
13
If L = P then ω1 = α∨
1 + α∨
2 and ω2 = α∨
1 /2 + α∨
