---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-024-n-strands
section_title: "n strands"
section_number: null
pages: 52-56
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
=
n
n
=
(A    )
-3 t(   )
σ
~σ
(1/{n}!) Σ
σ ε Sn
~
=
A
A-1
= -A2
-2
- A
=
+
{n}! = Σ
σ ε Sn
(A    )t(   )
σ
-4
=
n
n
= 0
= d
Figure 29 - Basic Projectors
=
−1/δ
=
−∆    /∆
n
n+1
n 1 1
n 1
1
n
1
=
2
δ
∆
1
∆
=
-1= 0
∆0
∆n+1 =
∆n -
n-1
Figure 30 - Two Strand Projector
a
b
c
i
j
k
a
b
c
i + j = a
j + k = b
i + k = c
Figure 31 -Vertex
In Figure 29 we indicate how the basic projector (symmetrizer, Jones-Wenzl
projector)
is constructed on the basis of the bracket polynomial expansion. In this tech-
nology a symmetrizer is a sum of tangles on n strands (for a chosen integer n).
The tangles are made by summing over braid lifts of permutations in the sym-
metric group on n letters, as indicated in Figure 29. Each elementary braid is
then expanded by the bracket polynomial relation as indicated in Figure 29 so
that the resulting sum consists of ﬂat tangles without any crossings (these can
be viewed as elements in the Temperley-Lieb algebra). The projectors have the
property that the concatenation of a projector with itself is just that projector,
and if you tie two lines on the top or the bottom of a projector together, then
the evaluation is zero. This general deﬁnition of projectors is very useful for
this theory. The two-strand projector is shown in Figure 30. Here the formula
for that projector is particularly simple. It is the sum of two parallel arcs and
two turn-around arcs (with coeﬃcient −1/d, with d = −A2 −A−2 is the loop
value for the bracket polynomial. Figure 30 also shows the recursion formula
for the general projector. This recursion formula is due to Jones and Wenzl
and the projector in this form, developed as a sum in the Temperley–Lieb
algebra (see Section 5 of this paper), is usually known as the Jones–Wenzl
projector.
The projectors are combinatorial analogs of irreducible representations of a
group (the original spin nets were based on SU(2) and these deformed nets are
based on the corresponding quantum group to SU(2)). As such the reader can
think of them as “particles”. The interactions of these particles are governed
by how they can be tied together into three-vertices. See Figure 31. In Figure
31 we show how to tie three projectors, of a, b, c strands respectively, together
to form a three-vertex. In order to accomplish this interaction, we must share
lines between them as shown in that Figure so that there are non-negative
integers i, j, k so that a = i + j, b = j + k, c = i + k. This is equivalent to the
condition that a+ b+ c is even and that the sum of any two of a, b, c is greater
than or equal to the third. For example a + b ≥c. One can think of the vertex
as a possible particle interaction where [a] and [b] interact to produce [c]. That
is, any two of the legs of the vertex can be regarded as interacting to produce
the third leg.
There is a basic orthogonality of three vertices as shown in Figure 32. Here
if we tie two three-vertices together so that they form a “bubble” in the middle,
then the resulting network with labels a and b on its free ends is a multiple of
an a-line (meaning a line with an a-projector on it) or zero (if a is not equal to
b). The multiple is compatible with the results of closing the diagram in the
equation of Figure 32 so the two free ends are identiﬁed with one another. On
closure, as shown in the Figure, the left hand side of the equation becomes a
Theta graph and the right hand side becomes a multiple of a “delta” where ∆a
denotes the bracket polynomial evaluation of the a-strand loop with a projector
on it. The Θ(a, b, c) denotes the bracket evaluation of a theta graph made from
three trivalent vertices and labeled with a, b, c on its edges.
There is a recoupling formula in this theory in the form shown in Figure 33.
Here there are “6-j symbols”, recoupling coeﬃcients that can be expressed, as
shown in Figure 35, in terms of tetrahedral graph evaluations and theta graph
evaluations. The tetrahedral graph is shown in Figure 34. One derives the
formulas for these coeﬃcients directly from the orthogonality relations for the
trivalent vertices by closing the left hand side of the recoupling formula and
using orthogonality to evaluate the right hand side. This is illustrated in Figure
35.
=
Θ(   ,   ,   )
∆
a
b
a c
a
c
d
d
a
δ a
b
a
c
d
a =
a
= Θ(   ,   ,   )
a c d
a
a
=
= ∆a
Figure 32 - Orthogonality of Trivalent Vertices
{ }
a b
c d
i
j
Σ
=
j
a
a
b
b
c
c
d
d
i
j
Figure 33 - Recoupling Formula
b
c
d
a
=
k
[
]
