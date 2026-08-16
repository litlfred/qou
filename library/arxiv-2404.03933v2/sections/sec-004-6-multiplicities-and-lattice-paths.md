---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-004-6-multiplicities-and-lattice-paths
section_title: "Multiplicities and lattice paths"
section_number: 6
pages: 14-18
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
Here we reformulate the problem of tensor power decomposition over Uq(sl2) and uq(sl2)
resolved in the previous section in terms of counting lattice paths on the set of dominant
weights for the corresponding quantum groups and will give a combinatorial derivation of
multiplicity formulae for T (1)⊗N derived before.
6.1. Lattice path model for tensor power decomposition of Uq(sl2)-modules.
6.1.1. Elementary steps and lattice paths. Tensor product decomposition (4) can be regarded
as the description of a lattice walk on the set of integral dominant weights which is for Uq(sl2)
is Z≥0 ={0, 1, 2,... }.
Let us describe elementary steps of such a walk. We will refer to points of the weight space
Z≥0 also as nodes (of our lattice walk). We will say a step has multiplicity 2 if it is counted
twice (see below). If the multiplicity of a step is not specified, we assume it has multiplicity
one.
(a) From the node k, when k̸=ml− 2,ml− 1,ml there are two possible steps, one to k + 1
and one to k− 1.
(b) From the node ml− 2 (m≥ 3) only steps to ml− 1,ml− 3, (m− 2)l− 1 are possible.
From 2l− 2 there are only steps to 2 l− 1 and 2l− 3.
(c) From the node ml− 1 there is one step leading to the node ml.
(d) From the nodeml there is a multiplicity 2 step to the nodeml−1 and simple (multiplicity
one) step to ml + 1.
Denote the set of these elementary steps SU. They can be described by a diagram on Figure
1.
0
1
2
l − 2
l − 1
l
2l − 2
2l − 1
2l
3l − 2
3l − 1
3l
. . .
. . .
. . .
. . .
Figure 1. The set of elementary steps SU, where red arrows denote steps of
multiplicity 2.
A graph of such lattice walk is a lattice path in LU = Z≥0× Z≥0 with points (x,y ) where
x∈ Z≥0 is a dominant weight and y is the degree N is the tensor power T (1)⊗N. The set of
elementary steps SU for such lattice paths is
SU ={((x,y ), (x′,y + 1))| (x,x′)∈SU}
TENSOR POWERS 15
Note that multiplicities of elementary steps define weights on SU. For large k = lk1 +k0 the
graph of elementary steps is 2l-periodic.
Examples of such lattice paths are given on Figure 2. Using recursive formulae (4) for the
l − 1
2l − 1
3l − 1
0
k
N
Figure 2. Two paths with elementary steps from SU. Red lines indicate ele-
mentary steps with multiplicity 2. A vertex with coordinate ( k,N ) represents
the highest weight k of the tilting module T (k)⊂ T (1)⊗N. The number of
lattice paths from the origin to ( k,N ) is the multiplicity M (l)
k (N). Elementary
steps SU from a vertex on this lattice are represented by possible lines down
the lattice. Similarly, the number of paths starting at ( n, 0) and descending to
(k,N ) is the multiplicity of the tilting module T (k)⊂T (n)⊗T (1)⊗N.
decomposition of tensor products and the corresponding lattice path model, these multiplicities
can be described as follows:
Theorem 6.1. The multiplicity of the tilting Uq(sl2)-module T (k) in the decomposition of
T (1)⊗N is equal to the weighted number of lattice paths on LU connecting (0, 0) and (k,N )
with weights given by multiplicities of elementary steps SU.
16 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
Path counting formula for this lattice path model was derived in [Sol] where the number of
paths was computed explicitly in terms F (N )
k using combinatorial methods such as reflection
principle. This formula coincides with expressions (4).
6.2. Lattice path model for decomposition of tensor powers of uq(sl2)-modules.
6.2.1. Elementary steps and lattice paths. In this case the lattice isLu ={0, 1,..., 3l−2}×Z≥0.
The following set of elementary steps is determined by the decomposition rules (5).
(a) From the node 0 there is only one step to 1.
(b) From the node k, when k̸=ml− 2,ml− 1,ml there are two possible steps, one to k + 1
and one to k− 1.
(c) From the node 2l− 2 there is a step to 2 l− 1 with multiplicity 2 and a step to 2 l− 3.
(d) From the node 3l− 2 there is a step to l− 1 with multiplicity 2 and a step to 3 l− 3.
(e) From the node ml− 1 there is only step to ml.
(f) From the node ml there is a step to ml− 1 with multiplicity 2 and a step to ml + 1.
The set Su can be characterized by the diagram on Figure 3. A graph of such lattice walk is a
0
1
2
l − 2
l − 1
l
2l − 2
2l − 1
2l
3l − 2
. . .
. . .
. . .
Figure 3. The set of elementary steps Su, where red arrows denote steps of
multiplicity 2.
lattice path inLu with points (x,y ) wherex∈ Z≥0 is a dominant weight andy is the degree N
is the tensor power T (1)⊗N. Nodes of this graph are identified with tilting modules as follows:
• To each node 0≤m≤l− 2 we assign module T (m), where T (0) = C;
• To each node l− 1≤m≤ 2l− 2 we assign module T+(m);
• To each node 2l− 1≤m≤ 3l− 2 we assign module T−(m−l).
The set of elementary steps Su is given by
Su ={((x,y ), (x′,y + 1))| (x,x′)∈Su}
Multiplicities of elementary step define weights on Su.
Examples of such lattice paths are given on Figure 4. Using recursive formulae (5) we arrive
to the following theorem describing multiplicities in terms of lattice paths:
Theorem 6.2. The multiplicity of the tilting uq(sl2)-module T (k) in the decomposition of
T (1)⊗N is equal to the weighted number of lattice paths in Lu connecting (0, 0) and (k,N ) with
weights given by multiplicities of elementary steps Su.
Now we can compute multiplicities using the lattice path model and compare the formulae
with the ones that we already derived in Theorem 4.3
TENSOR POWERS 17
l − 1
2l − 1
0
k
N
Figure 4. Two paths with elementary steps from Su. Red arrows indicate
elementary steps with multiplicity 2. A vertex with coordinate (k,N ) represents
the highest weightk of the tilting moduleT (k)⊂T (1)⊗N. The number of lattice
paths from the origin to (k,N ) is the multiplicitym(l)
k (N). Elementary steps Su
from a vertex on this lattice are represented by possible lines down the lattice.
Similarly, the number of paths starting at (n, 0) and descending to (k,N ) is the
multiplicity of the tilting module T (k)⊂T (n)⊗T (1)⊗N.
18 ANNA LACHOWSKA, OLGA POSTNOV A, NICOLAI RESHETIKHIN, AND DMITRY SOLOVYEV
Theorem 6.3. (a) The number of lattice paths is given by the following formulae. For
k0̸=l− 1 we have
(6) m(l)
l+k0,+(N) =
⌊N
2l⌋X
k=1
k2F (N )
k0−l−2kl +
⌊N−l
2l ⌋X
k=0
(k + 1)2F (N )
k0+l+2kl
(7) m(l)
l+k0,−(N) =
⌊N−l
2l ⌋X
k=1
(k2 +k)F (N )
k0−2l−2kl +
⌊N−2l
2l ⌋X
k=0
((k + 1)2 + (k + 1))F (N )
k0+2l+2kl
ForT+(l− 1), T−(l− 1) the multiplicities are:
m(l)
l−1,+(N) =
⌊N
2l + 1
2⌋X
k=0
(2k + 1)F (N )
l−1+2kl,
m(l)
l−1,−(N) =
⌊N
2l +1⌋X
k=0
(2k + 2)F (N )
2l−1+2kl,
Note that in these formulae some F (N )
m can be negative.
(b) These numbers are exactly the same as in Theorem 4.3.
The proof of this theorem is given in Appendix B.
