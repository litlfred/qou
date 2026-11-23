---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-034-10-quantum-computation-of-colored-jones-polynomi
section_title: "Quantum Computation of Colored Jones Polynomials and the Witten-Reshetikhin- Turaev Invariant"
section_number: 10
pages: 80-83
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Polynomials and the Witten-Reshetikhin-
Turaev Invariant
In this section we make some brief comments on the quantum computation
of colored Jones polynomials. This material will be expanded in a subsequent
publication.
= 0
a
b
if b = 0
Σ
=
0
0
0
=
x
y
,
x
y
0
B(x,y)
0
0
0
=
a
a
a
a a a
a
a
a
a
Σ
=
x
y
,
x
y
0
B(x,y)
a
a
=
0
a
a
B(0,0)
0
0
= B(0,0) ∆a
(     ) 2
B
P(B)
Figure 57 - Evaluation of the Plat Closure of a Braid
First, consider Figure 57. In that ﬁgure we illustrate the calculation of the
evalutation of the (a) - colored bracket polynomial for the plat closure P(B) of
a braid B. The reader can infer the deﬁnition of the plat closure from Figure
57. One takes a braid on an even number of strands and closes the top strands
with each other in a row of maxima. Similarly, the bottom strands are closed
with a row of minima. It is not hard to see that any knot or link can be
represented as the plat closure of some braid.
δ
A
4
-4
= A
+
+
δ
A
4
-4
=
A
+
+
-
=
4
A
A-4
-
(
)
-
(
)
-
=
4
A
A-4
-
(
)
-
(
)
=
A8
Figure 58 - Dubrovnik Polynomial Specialization at Two Strands
The (a) - colored bracket polynonmial of a link L, denoted < L >a, is the
evaluation of that link where each single strand has been replaced by a parallel
strands and the insertion of Jones-Wenzl projector (as discussed in Section 7).
We then see that we can use our discussion of the Temperley-Lieb recoupling
theory as in sections 7,8 and 9 to compute the value of the colored bracket
polynomial for the plat closure PB. As shown in Figure 57, we regard the
braid as acting on a process space V a,a,···,a
0
and take the case of the action on
the vector v whose process space coordinates are all zero. Then the action of
the braid takes the form
Bv(0, · · ·, 0) = Σx1,···,xnB(x1, · · · , xn)v(x1, · · ·, xn)
where B(x1, · · · , xn) denotes the matrix entries for this recoupling transforma-
tion and v(x1, · · ·, xn) runs over a basis for the space V a,a,···,a
0
. Here n is even
and equal to the number of braid strands. In the ﬁgure we illustrate with
n = 4. Then, as the ﬁgure shows, when we close the top of the braid action
to form PB, we cut the sum down to the evaluation of just one term. In the
general case we will get
< PB >a= B(0, · · ·, 0)∆n/2
a
.
The calculation simpliﬁes to this degree because of the vanishing of loops in
the recoupling graphs. The vanishing result is stated in Figure 57, and it is
proved in the case a = 2 in Figure 49.
The colored Jones polynomials are normalized versions of the colored bracket
polymomials, diﬀering just by a normalization factor.
In order to consider quantumn computation of the colored bracket or col-
ored Jones polynomials, we therefore can consider quantum computation of
the matrix entries B(0, · · ·, 0). These matrix entries in the case of the roots of
unity A = eiπ/2r and for the a = 2 Fibonacci model with A = e3iπ/5 are parts
of the diagonal entries of the unitary transformation that represents the braid
group on the process space V a,a,···,a
0
. We can obtain these matrix entries by us-
ing the Hadamard test as described in section 4. As a result we get relatively
eﬃcient quantum algoritms for the colored Jones polynonmials at these roots
of unity, in essentially the same framework as we described in section 4, but
for braids of arbitrary size. The computational complexity of these models is
essentially the same as the models for the Jones polynomial discussed in [1].
We reserve discussion of these issues to a subsequent publication.
It is worth remarking here that these algorithms give not only quantum
algorithms for computing the colored bracket and Jones polynomials, but also
for computing the Witten-Reshetikhin-Turaev (WRT) invariants at the above
roots of unity. The reason for this is that the WRT invariant, in unnormalized
form is given as a ﬁnite sum of colored bracket polynomials:
WRT(L) = Σr−2
a=0∆a < L >a,
and so the same computation as shown in Figure 57 applies to the WRT. This
means that we have, in principle, a quantum algorithm for the computation
of the Witten functional integral [78] via this knot-theoretic combinatorial
topology. It would be very interesting to understand a more direct approach
to such a computation via quantum ﬁeld theory and functional integration.
Finally, we note that in the case of the Fibonacci model, the (2)-colored
bracket polynomial is a special case of the Dubrovnik version of the Kauﬀman
polynomial [38]. See Figure 58 for diagammatics that resolve this fact. The
skein relation for the Dubrovnik polynomial is boxed in this ﬁgure. Above the
box, we show how the double strands with projectors reproduce this relation.
This observation means that in the Fibonacci model, the natural underlying
knot polynomial is a special evaluation of the Dubrovnik polynomial, and the
Fibonacci model can be used to perform quantum computation for the values
of this invariant.
