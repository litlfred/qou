---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-001-2-calculation-of-the-kashaev-invariant-of-the-52
section_title: "Calculation of the Kashaev invariant of the 52 knot"
section_number: 2
pages: 5-7
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "DOI 10.4171/QT/83 — We give a presentation of the asymptotic expansion of the Kashaev invariant of the 52 knot."
duplicate_of: "104171-qt-83"
---
In this section, we review the deﬁnition of the Kashaev invariant and the calculation of the
Kashaev invariant ⟨52 ⟩N of the 52 knot in Section 2.1. Further, we continue to calculate
the value of ⟨52 ⟩N toward its asymptotic expansion in Section 2.2.
2.1
The Kashaev invariant of the 52 knot
In this section, we review the deﬁnition of the Kashaev invariant of oriented knots, and
review the calculation of the Kashaev invariant ⟨52 ⟩N of the 52 knot, which are due to
Yokota [43]. The aim of this section is to show (7) which gives the value of ⟨52 ⟩N.
Let N be an integer ≥2. We put q = exp(2π√−1/N), and put
(x)n = (1 −x)(1 −x2) · · · (1 −xn)
for n ≥0. It is known [24] that, for any n, m with n ≤m,
(q)n(q)N−n−1 = N,
(3)
∑
n≤k≤m
1
(q)m−k(q)k−n
= 1.
(4)
Following Yokota [43],3 we review the deﬁnition of the Kashaev invariant. We put
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
3We make a minor modiﬁcation of the deﬁnition of weights of critical points from the deﬁnition in [43], in order to make
⟨K ⟩N invariant under Reidemeister moves.
5
Let K be an oriented knot. We consider a 1-tangle whose closure is isotopic to K such
that its string is oriented downward at its end points. Let D be a diagram of the 1-tangle.
We present D by a union of elementary tangle diagrams shown in (5). We decompose the
string of D into edges by cutting it at crossings and critical points with respect to the
height function of R2. A labeling is an assignment of an element of N to each edge. Here,
we assign 0 to the two edges adjacent to the end points of D. For example, see (6). We
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
(5)
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
Following Yokota [43],4 we review the calculation of the Kashaev invariant ⟨52 ⟩N of
the 52 knot, where the 52 knot is the closure of the following 1-tangle.
0
a
k
j
c
i
c+1
b
i−1
d
l
e
e+1
0
(6)
We consider the above labeling. Then, it is shown by arguments in [43] that the labelings
of edges adjacent to the unbounded regions vanish, i.e., a = b = c = d = e = 0. Hence,
the Kashaev invariant of the 52 knot is given by
⟨52 ⟩N =
∑
i,j,k,l
q1/2 R
0 0
0 k R
0 k
0 j R
i j
0 1 R
0 0
i−1 l R
0 l
0 1
4Our resulting formula (7) in this section is q times the corresponding formula in [43]. This diﬀerence is because of the
diﬀerence of the deﬁnitions of ⟨K ⟩N between ours and [43].
6
=
∑
i,j,k,l
q1/2 ·
Nq
1
2 −k
(q)[−k](q)[k−1]
·
Nq
1
2 +k−j
(q)[−k](q)[k−j](q)[j−1]
·
Nq−1
2 +j
(q)[i−j](q)[j−1](q)[−i]
×
Nq
1
2 −l
(q)[−l](q)[l−i](q)[i−1]
·
Nq−1
2 +l
(q)[−l](q)[l−1]
=
∑
i,j,k,l
N 3q
(q)[−k](q)[k−j](q)[j−1](q)[i−j](q)[j−1](q)[−i](q)[−l](q)[l−i](q)[i−1]
,
where we obtain the last equality from (3). Further, by (4), the above formula is rewritten,
⟨52 ⟩N =
∑
1≤j≤i≤N
N 3q
(q)i−1(q)N−i(q)j−1(q)j−1(q)i−j
=
∑
0≤j≤i<N
N 3q
(q)i(q)N−i−1(q)j(q)j(q)i−j
=
∑
0 ≤i,j
i+j < N
N 3q
(q)i+j(q)N−i−j−1(q)j(q)j(q)i
,
(7)
where we obtain the second equality by replacing i and j with i + 1 and j + 1, and obtain
the last equality by replacing i with i+j. Hence, we obtain the presentation (7) of ⟨52 ⟩N.
2.2
