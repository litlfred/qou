---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
toc_source: outline
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance measures associated with linear spaces."
---
arXiv:2108.03616v2  [math.CO]  14 Dec 2021
Circuit imbalance measures and linear programming ∗
Farbod Ekbatani, Bento Natura, and L´aszl´o A. V´egh
London School of Economics and Political Science
{F.Ekbatani, B.Natura, L.Vegh}@lse.ac.uk
15th December, 2021
Abstract
We study properties and applications of various circuit imbalance measures associated
with linear spaces.
These measures describe possible ratios between nonzero entries of
support-minimal nonzero vectors of the space.
The fractional circuit imbalance measure
turns out to be a crucial parameter in the context of linear programming, and two integer
variants can be used to describe integrality properties of associated polyhedra.
We give an overview of the properties of these measures, and survey classical and recent
applications, in particular, for linear programming algorithms with running time dependence
on the constraint matrix only, and for circuit augmentation algorithms. We also present new
bounds on the diameter and circuit diameter of polyhedra in terms of the fractional circuit
imbalance measure.
Contents
Introduction
3
2
Preliminaries
5
3
Properties of the imbalance measures
6
3.1
Bounds on subdeterminants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
Fractional integrality characterization
. . . . . . . . . . . . . . . . . . . . . . . .
9
3.3
Self-duality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3.4
Matrix representations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3.5
The triangle inequality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
4
Connections to other condition numbers
15
4.1
The condition number ¯χ and the lifting operator . . . . . . . . . . . . . . . . . .
15
4.2
The condition number δ and bounds on diameters of polyhedra . . . . . . . . . .
16
5
Optimizing circuit imbalances
18
5.1
Perfect balancing: κ∗
W = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
6
Hoﬀman proximity theorems
22
∗This project has received funding from the European Research Council (ERC) under the European Union’s
Horizon 2020 research and innovation programme (grant agreement ScaleOpt–757481)
1
7
Linear programming with dependence on the constraint matrix only
24
7.1
A black box algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
7.2
Layered least squares interior point methods . . . . . . . . . . . . . . . . . . . . .
26
7.3
The curvature of the central path . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
8
Circuit diameter bounds and circuit augmentation algorithms
28
8.1
An improved circuit diameter bound . . . . . . . . . . . . . . . . . . . . . . . . .
29
8.2
Circuit augmentation algorithms
. . . . . . . . . . . . . . . . . . . . . . . . . . .
29
8.2.1
Augmenting directions for ﬂow problems . . . . . . . . . . . . . . . . . . .
30
8.2.2
Convergence bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
8.3
A circuit augmentation algorithm with log κA dependence . . . . . . . . . . . . .
32
8.4
An improved bound for steepest-descent augmentation . . . . . . . . . . . . . . .
33
9
Circuits, integer proximity, and Graver bases
36
10 A decomposition conjecture
37
A Appendix: Proof of Proposition 3.20
44
