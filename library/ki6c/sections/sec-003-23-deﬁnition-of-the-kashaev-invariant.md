---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings Tomotada Ohtsuki and Yoshiyuki Yokota Introduction"
section_id: sec-003-23-deﬁnition-of-the-kashaev-invariant
section_title: "Deﬁnition of the Kashaev invariant"
section_number: 2.3
pages: 7-8
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings Tomotada Ohtsuki and Yoshiyuki Yokota Introduction — We give presentations of the asymptotic expansions of the"
---
Deﬁnition of the Kashaev invariant
In this section, we review the deﬁnition of the Kashaev invariant of oriented knots.
Following Yokota [33],3 we review the deﬁnition of the Kashaev invariant. We put
N = {0, 1, · · · , N −1}.
For i, j, k, l ∈N, we put
Ri j
k l =
N q−1
2 +i−k θi j
k l
(q)[i−j](q)[j−l](q)[l−k−1](q)[k−i]
,
R
i j
k l =
N q
1
2 +j−l θi j
k l
(q)[i−j](q)[j−l](q)[l−k−1](q)[k−i]
,
where [m] ∈N denotes the residue of m modulo N, and we put
θi j
k l =
{
1
if [i −j] + [j −l] + [l −k −1] + [k −i] = N −1,
0
otherwise.
Let K be an oriented knot. We consider a 1-tangle whose closure is isotopic to K such
that its string is oriented downward at its end points. Let D be a diagram of the 1-tangle.
We present D by a union of elementary tangle diagrams shown in (12). We decompose
the string of D into edges by cutting it at crossings and critical points with respect to the
height function of R2. A labeling is an assignment of an element of N to each edge. Here,
we assign 0 to the two edges adjacent to the end points of D. For example, see (28). We
deﬁne the weights of labeled elementary tangle diagrams by
W
(
i
j
k
l
)
= Ri j
k l ,
W
(
k
l
)
= q−1/2δk,l−1 ,
W
(
k
l
)
= δk,l ,
W
(
i
j
k
l
)
= R
i j
k l ,
W
( i
j )
= q1/2δi,j+1 ,
W
( i
j )
= δi,j .
(12)
3We make a minor modiﬁcation of the deﬁnition of weights of critical points from the deﬁnition in [33], in order to make
⟨K ⟩N invariant under Reidemeister moves.
7
Then, the Kashaev invariant ⟨K ⟩N of K is deﬁned by
⟨K ⟩N =
∑
labelings
∏
crossings
of D
W(crossings)
∏
critical
points of D
W(critical points) ∈C.
