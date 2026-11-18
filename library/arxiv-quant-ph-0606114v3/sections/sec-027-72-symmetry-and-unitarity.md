---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-027-72-symmetry-and-unitarity
section_title: "Symmetry and Unitarity"
section_number: 7.2
pages: 58-64
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Symmetry and Unitarity
The formula for the recoupling coeﬃcients given in Figure 35 has less symmetry
than is actually inherent in the structure of the situation. By multiplying all
the vertices by an appropriate factor, we can reconﬁgure the formulas in this
theory so that the revised recoupling transformation is orthogonal, in the sense
that its transpose is equal to its inverse. This is a very useful fact. It means
that when the resulting matrices are real, then the recoupling transformations
are unitary. We shall see particular applications of this viewpoint later in the
paper.
Figure 37 illustrates this modiﬁcation of the three-vertex. Let V ert[a, b, c]
denote the original 3-vertex of the Temperley-Lieb recoupling theory.
Let
ModV ert[a, b, c] denote the modiﬁed vertex. Then we have the formula
ModV ert[a, b, c] =
q√∆a∆b∆c
q
Θ(a, b, c)
V ert[a, b, c].
Lemma. For the bracket evaluation at the root of unity A = eiπ/2r the factor
f(a, b, c) =
q√∆a∆b∆c
q
Θ(a, b, c)
is real, and can be taken to be a positive real number for (a, b, c) admissible
(i.e. a + b + c ≤2r −4).
Proof. By the results from the previous subsection,
Θ(a, b, c) = (−1)(a+b+c)/2 ˆΘ(a, b, c)
where ˆΘ(a, b, c) is positive real, and
∆a∆b∆c = (−1)(a+b+c)[a + 1][b + 1][c + 1]
where the quantum integers in this formula can be taken to be positive real.
It follows from this that
f(a, b, c) =
v
u
u
u
t
q
[a + 1][b + 1][c + 1]
ˆΘ(a, b, c)
,
showing that this factor can be taken to be positive real.
✷
In Figure 38 we show how this modiﬁcation of the vertex aﬀects the non-
zero term of the orthogonality of trivalent vertices (compare with Figure 32).
We refer to this as the “modiﬁed bubble identity.” The coeﬃcient in the mod-
iﬁed bubble identity is
s
∆b∆c
∆a
= (−1)(b+c−a)/2
v
u
u
t[b + 1][c + 1]
[a + 1]
where (a, b, c) form an admissible triple. In particular b + c −a is even and
hence this factor can be taken to be real.
We rewrite the recoupling formula in this new basis and emphasize that
the recoupling coeﬃcients can be seen (for ﬁxed external labels a, b, c, d) as a
matrix transforming the horizontal “double-Y ” basis to a vertically disposed
double-Y basis.
In Figures 39, 40 and 41 we have shown the form of this
transformation,using the matrix notation
M[a, b, c, d]ij
for the modiﬁed recoupling coeﬃcients.
In Figure 39 we derive an explicit
formula for these matrix elements. The proof of this formula follows directly
from trivalent–vertex orthogonality (See Figures 32 and 35.), and is given in
Figure 39. The result shown in Figure 39 and Figure 40 is the following formula
for the recoupling matrix elements.
M[a, b, c, d]ij = ModTet
 
a
b
i
c
d
j
!
/
q
∆a∆b∆c∆d
where √∆a∆b∆c∆d is short-hand for the product
s
∆a∆b
∆j
s
∆c∆d
∆j
∆j
= (−1)(a+b−j)/2(−1)(c+d−j)/2(−1)j
v
u
u
t[a + 1][b + 1]
[j + 1]
v
u
u
t[c + 1][d + 1]
[j + 1]
[j + 1]
= (−1)(a+b+c+d)/2q
[a + 1][b + 1][c + 1][d + 1]
In this form, since (a, b, j) and (c, d, j) are admissible triples, we see that this
coeﬃent can be taken to be real, and its value is independent of the choice of
i and j. The matrix M[a, b, c, d] is real-valued.
It follows from Figure 33 (turn the diagrams by ninety degrees) that
M[a, b, c, d]−1 = M[b, d, a, c].
In Figure 42 we illustrate the formula
M[a, b, c, d]T = M[b, d, a, c].
It follows from this formula that
M[a, b, c, d]T = M[a, b, c, d]−1.
Hence M[a, b, c, d] is an orthogonal, real-valued matrix.
a
b
c
a
b
c
=
∆    ∆    ∆    
Θ(     ,     ,     )
a
b
c
c
a
b
Figure 37 - Modiﬁed Three Vertex
=
Θ(   ,   ,   )
∆
a
b
a
c
a
c
a
b
a
a
b
c
a
=
∆    ∆    ∆    
a
b
c
a
b
c
a
=
a
Θ(   ,   ,   )
a
c
b
a
b
c
∆
∆
∆
a
b
c
a
Figure 38 - Modiﬁed Bubble Identiy
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
k
Σ
=
∆j δ j
k
k
=
d
=
[
]
ModTet
a b
c d
i
a b
c d i j =
b
c
d
a
i
j
∆    ∆    ∆    ∆   
a
b
c
d
a b
c d i
a b
c d i
j
a
b
c
∆
∆
∆
∆
∆
∆
j
j
k
k
k
∆j
j
d
a b
c d i
a
b
c
∆
∆
∆
∆
∆
∆
j
j
j
∆j
d
a
b
c
∆
∆
∆
∆
∆
∆
j
j
Figure 39 - Derivation of Modiﬁed Recoupling Coeﬃcients
a b
c d i j
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
Figure 40 - Modiﬁed Recoupling Formula
a b
c d i j =
b
c
d
a
i
j
∆    ∆    ∆    ∆   
a
b
c
d
M[a,b,c,d]i j =
a b
c d i j
Figure 41 - Modiﬁed Recoupling Matrix
a b
c d
=
b
c
d
a
i
j
∆    ∆    ∆    ∆   
a
b
c
d
b
c
d
a
i
j
∆    ∆    ∆    ∆   
a
b
c
d
a b
c d
T
-1
=
=
Figure 42 - Modiﬁed Matrix Transpose
Theorem 2.
In the Temperley-Lieb theory we obtain unitary (in fact real
orthogonal) recoupling transformations when the bracket variable A has the
form A = eiπ/2r for r a positive integer. Thus we obtain families of unitary
representations of the Artin braid group from the recoupling theory at these
roots of unity.
Proof. The proof is given the discussion above.
✷
In Section 9 we shall show explictly how these methods work in the case of
the Fibonacci model where A = e3iπ/5.
