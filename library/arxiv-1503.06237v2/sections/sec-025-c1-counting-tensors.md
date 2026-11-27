---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-025-c1-counting-tensors
section_title: "C.1 Counting tensors"
section_number: null
pages: 50-51
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
In this appendix we compute some basic properties of the pentagon code that we quoted
in the text. In these computations it is useful to “unwrap” the code, as in ﬁgure 20.
The central tensor is placed at the bottom, which we will refer to as the zeroth layer, the
ﬁrst ﬁve tensors as the ﬁrst layer, and so on, with the layer number n being equivalent
to the graph distance to the central tensor.
At each layer, it is clear that there are two kinds of tensors: those with one leg
connected to the previous layer and those with two. We will denote the numbers of
these at layer n as fn and gn, so for example f1 = 5 and g1 = 0. Moreover if we group
these together as a two component vector, we have the recursive equation
(fn+1
gn+1
)
=
(2 1
1 1
)(fn
gn
)
. (C.1)
– 48 –
Applying this equation repeatedly we can compute the number of tensors of either type
at any n via (fn
gn
)
=
(2 1
1 1
)n−1(5
0
)
. (C.2)
This is easily computed by diagonalizing the matrix M≡
(2 1
1 1
)
, at large n we have
fn = 5−
√
5
2
(
3 +
√
5
2
)n[
1 +O
((
3−
√
5
3 +
√
5
)n)]
gn = 3
√
5− 5
2
(
3 +
√
5
2
)n[
1 +O
((
3−
√
5
3 +
√
5
)n)]
. (C.3)
If we truncate at layer n, the total number of boundary qubits is
Nboundary = 4f(n) + 3f(n) (C.4)
and the total number of bulk tensors is
Nbulk = 1 +
n∑
k=1
(fk +gk). (C.5)
Asymptotically we have
Nbulk
Nboundary
→ 1√
5≈.447, (C.6)
which reproduces equation (3.1).
