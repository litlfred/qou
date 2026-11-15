---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-003-skein-relation
section_title: "Skein relation"
section_number: null
pages: 7-8
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Skein relation
To construct an explicit example of a Markov trace it is convenient to introduce another structure, the
Temperley-Lieb algebra TLn [48]. Similarly the to the braid group, it can be introduced via generators
as follows:
TLn := {uk, k = 1, . . . , n −1| u2
i = d · ui, i = 1, . . . n −1; uiui+1ui = ui, i = 1, . . . , n −2;
ui+1uiui+1 = ui+1, i = 1, . . . , n −2; uiuj = ujui, |i −j| > 1} ,
(18)
where d is a C-number. Since the above relations define an algebra, all its elements belong to a vector
space. The first relation makes this space finite-dimensional. The dimension of TLn is given by the n-th
Catalan number,
Cn =
(2n)!
n!(n + 1)! .
(19)
Note that this algebra also contains the identity element.
As in the case of the braid group it is convenient to think of the Temperley-Lieb algebra in terms of
diagrams, which make explicit the defining relations. In this case one has
u1 =
· · ·
,
u2 =
· · ·
,
u3 =
· · ·
,
· · ·
(20)
Identity is added to the set of generators and is represented by the diagram with the trivial evolution of
points:
I =
· · ·
.
(21)
7
The multiplication is organized in the same way as for braids. The first defining relation can be cast as
u2
k =
· · ·
· · ·
= d ·
· · ·
· · ·
(22)
Note that in the multiplication a closed loop is formed. We will always think of a closed loop as of a
C-number, while lines with open ends correspond to matrices or tensors. A heuristic explanation for this
property is that a disconnected circle can be freely moved around the diagram (in particular, removed)
unlike the lines, which are fixed at the endpoints.
It is straightforward to check that the diagrams respect the remaining defining relations. The diagrams
also explain the finiteness of the number of the generator words and reduce the counting to a combinatorial
problem. Any word should correspond to n pairs of points connected in a way without line intersection.
There is only a finite number of such ways, computed by the Catalan numbers.
Given a generator of the Temperley-Lieb algebra, one can construct an element of the braid group.
The following set of algebra elements,
rk = AI + A−1uk ,
(23)
for some C-number A, satisfy the braid group relations if
d = −A2 −A−2 .
(24)
Note that relation (23) can be represented diagrammatically as
= A
+ A−1
.
(25)
We will refer to this diagrammatic identity as the skein relation.
Let us make the following faithfulness assumption. Assume that the skein relation holds even if we
simultaneously rotate all the diagrams by 90 degrees. We will get
= A
+ A−1
.
(26)
Note that this rotation takes the braid generator to its inverse and exchanges the identity and the
Temperley-Lieb generator.
Our assumption imposes an additional relation on the braid group.
For
example, eliminating the Temperley-Lieb generator from relations (25) and (26) we get a purely braid
group relation
A
−A−1
= (A2 −A−2)
,
(27)
which can also be cast as quadratic relation on the group generators:
(bk)2 = (A −A−3)bk + A−2I .
(28)
With this additional relation bk are said to generate the Hecke algebra.
