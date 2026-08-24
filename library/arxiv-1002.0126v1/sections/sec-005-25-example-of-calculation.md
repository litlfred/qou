---
doc_id: arxiv-1002.0126v1
doc_title: "An introduction to the volume conjecture"
section_id: sec-005-25-example-of-calculation
section_title: "Example of calculation"
section_number: 2.5
pages: 10-15
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "An introduction to the volume conjecture — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
2 σ1σ−1
2 . Its closure E is a knot
called the ﬁgure-eight knot (Figure 4). We will calculate JN (E; q).
Instead of calculating Tr1(Tr2(Tr3(Φ( β)µ⊗3)))∈ C, we will calculate Tr2(Tr3(Φ( β)(Id⊗µ⊗
µ)))∈ End(V ), which is a scalar multiple by Schur’s lemma (for a proof see [18,
Lemma 3.9]). See Figure 14.
⇒
Figure 14. We close all the strings except for the ﬁrst one.
Then Tr 1(Tr2(Tr3(Φ( β)µ⊗3))) coincides with the trace of µ times the scalar S.
Since
T(R,µ,q(N 2−1)/ 4,1)(β) = q−w(β)(N 2−1)/4 Tr1(Tr2(Tr3(Φ( β)µ⊗3)))
= q−w(β)(N 2−1)/4 Tr1(S IdV )
= q−w(β)(N 2−1)/4
N −1∑
i=0
S q(2i−N +1)/2
= q−w(β)(N 2−1)/4{N}
{1} S,
we have JN (L; q) = q−w(β)(N 2−1)/4S = S.
We need an explicit formula for the inverse of the R-matrix, which is given by
(R−1)ij
kl =
min(N −1−i,j)∑
m=0
δl,i−mδk,j+m
{k}!{N− 1− l}!
{j}!{m}!{N− 1− i}!
× (−1)mq−
(
i−(N −1)/2
)(
j−(N −1)/2
)
−m(i−j)/2+m(m+1)/4.
(2.4)
To calculate the scalar S, draw a diagram for the braid β and close it except for
the ﬁrst string (Figure 15). Fix a basis {e0, e1, . . . , eN −1} of CN .
Label each arc with a non-negative integer i less than N , which corresponds to a
basis element ei, where our braid diagram is divided into arcs by crossings so that
at each crossing four arcs meet. Since the homomorphism Tr 2(Tr1(Φ( β)⊗ 2)) is
a scalar multiple, we choose any basis for the ﬁrst (top-left) arc of Figure 15 and
AN INTRODUCTION TO THE VOLUME CONJECTURE 11
Figure 15. Draw the braid σ1σ−1
2 σ1σ−1
2 and close it except for
the left-most one.
Figure 16. Label the ﬁrst (top-left) arc with N− 1.
calculate the scalar. For simplicity we choose eN −1 and so we label the ﬁrst arc
with N− 1 (Figure 16).
Recall that we will associate the R-matrix or its inverse with each crossing as
follows.
⇒ Rij
kl , ⇒ (R−1)ij
kl
Therefore we will label the other arcs following the following two rules :
12 HITOSHI MURAKAMI
(i). At a positive crossing, the top-left label is less than or equal to the bottom-
right label, the top-right label is greater than or equal to the bott om-left
label, and their diﬀerences coincide (see (2.2)).
: i + j = k + l, l≥ i, k≤ j,
(ii). At a negative crossing, the top-left label is greater than or eq ual to the
bottm-right label, the top-right label is less than or equal to the bo ttm-left
label, and their diﬀerences coincide (see (2.4)).
: i + j = k + l, l≤ i, k≥ j.
From Rule (i), the next arc should be labeled with N− 1, and the diﬀerence at
the top crossing is 0 (Figure 17). This is why we chose N− 1 for the label of the
ﬁrst arc.
Figure 17. The label of the next arc should be N− 1, and the
diﬀerence at the top crossing is 0
Label the top-right arc with i with 0≤ i≤ N− 1 (Figure 18).
The label of the left-middle arc should be i since the diﬀerence at the top crossing
is 0.
Label the arcs indicated in Figure 20 with j and k with 0 ≤ j≤ N− 1 and
0≤ k ≤ N− 1. Then the diﬀerence at the second top crossing is N− k− 1.
Therefore the arc between the second top crossing and the seco nd bottom crossing
should be labeled with N− k + j− 1 from Rule (ii) (Figure 21). Since the label
should be less than N , we have j− k≤ 0.
Look at the bottom-most crossing and apply Rule (ii). We see that i≥ k and
the diﬀerence at the bottom-most crossing is i− k. So the label of the arc between
the second bottom crossing and the bottom-most crossing is i + j− k (Figure 22).
We also see that the label of the bottom-most arc is N− 1 as we expected.
AN INTRODUCTION TO THE VOLUME CONJECTURE 13
Figure 18. Label the top-right arc with i (0≤ i≤ N− 1).
Figure 19. The label of the left-middle arc should be i since the
diﬀerence at the top crossing is 0.
However from Rule (i) we have j− k≥ 0 and so k = j. Therefore we ﬁnally
have the labeling as indicated in Figure 23.
Now we can calculate the colored Jones polynomial. We have
JN (E; q) =
∑
i≥j
RN −1,i
i,N −1 (R−1)N −1,j
N −1,j Ri,N −1
N −1,i (R−1)i,j
i,j µj
j µi
i
=
∑
i≥j
(−1)N −1+i{N− 1}!{i}!{N− 1− j}!
({j}!)2{i− j}!{N− 1− i}!
× q(−i−i2−2ij−2j2+3N +6N i+2N j−3N 2)/4.
14 HITOSHI MURAKAMI
Figure 20. Choose j and k. Then the diﬀerence at the second
top crossing is N− k− 1.
Figure 21. The label of the arc between the second top arc and
the second bottom arc should be N−k +j−1. Note that j−k≤ 0.
In this formula we need two summations. To get a formula involving only one
summation we regard the ﬁgure-eight knot E as the closure of a tangle as shown in
Figure 24. In this case we need to put µ at each local minimum where the arc goes
from left to right, and µ−1 at each local maximum where the arc goes from right
to left. See [18, Theorem 3.6] for details.
