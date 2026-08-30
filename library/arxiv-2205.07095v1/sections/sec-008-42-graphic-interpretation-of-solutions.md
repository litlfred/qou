---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko"
section_id: sec-008-42-graphic-interpretation-of-solutions
section_title: "Graphic interpretation of solutions."
section_number: 4.2
pages: 10-13
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical"
---
As in the case of the Kirkwood-Salzburg equations for a large canonical
ensemble (see details in [21]) the analytical expression of the kernel T (η|γ)
can be given as contributions of forest-graphs. The number N (m|n),m =
10
|η|,n = |γ| all forest graphs can be calculated by solving the following
recurrent equation:
N (m|n) =
n∑
k=0
(n
k
)
N (m+k−1|n−k)+
n∑
k=1
(n
k
)
N (m|n−k)
k∑
l=1
(k
l
)
N (l|k−l).
(4.50)
If we reject the nonlinear term, the recurrent equation can b e solved ex-
actly: N (m|n) = m(m +n)n−1 (see [21]). This formula makes it possible to
prove the convergence of the integral (4.34) at j = 1 and small density val-
ues. But the nonlinear term apparently signiﬁcantly increa ses the number
of forest graphs. But according to the formula (4.47), each c ontribution of
the forest graph, which contains a tree with the contributio n of the factor
K(x1;ξ),ξ ∈ γ, which appears from the second sum in (4.47) is included
with a minus sign. So, for example calculating
T (x1|y) = ̺2 [K(x1;y) − K(x1;y)] = 0. (4.51)
Therefore, it is necessary to analyze this recurrent relati onship in more
detail. It is easy to get the following proposition.
Proposition 4.1 From initial conditions (4.48)-(4.49) it follows that
T (x1|∅) = ̺, T (x1|γ) = 0 forγ ⁄= ∅. (4.52)
It gives the needed equality for density ρ(x1) = ̺.
In addition T (η|∅) = ̺|η| exp[−βU (η)].
The proof follows from (4.47) by induction procedure. To obtain the so lu-
tion of (4.47) in the language of graph theory [24, 4] deﬁne th e set graphs
D(η;γ).
Remark 4.1 The set D(η;γ) is the set of rooted graph, connected compo-
nents of which are 2-connected graphs with respect to conﬁgu rationγ. Any
graph G ∈ D (η;γ) has m = |η| vertices of conﬁguration η and n = |γ|
vertices of conﬁguration γ. Every vertex of η can be free of lines or can
connect only with vertices y of conﬁgurationγ. Every vertex y ∈γ connects
with vertices x or y by at least two lines. This deﬁnitions is very close to
deﬁnitions of the set of white and black vertices D(W ;B) in [5], Section 2.
The role of the roots of the graph is performed by the conﬁgura tion η. A
singleton G ∈ D (x1; ∅). The contribution of any vertex is ̺. The contri-
bution of line w(lxy), which connected two vertices x and y or yi and yj is
K(x;y).
11
Remark 4.2 According to (4.34), integration is performed at the points of
conﬁguration γ, and according to equation (4.47), in the kernels T (θ;ξ),
the conﬁguration ξ ⊆γ, and the conﬁguration θ can contain both variables
from η and γ. Therefore, the corresponding graphs of sets D(θ;ξ) can
contain only black vertices.
The main statement of the section is
Proposition 4.2 The solution of the recurrence relation (4.47) can be
rewritten by contributions from the graphs of the set D(η;γ):
T (η|γ) = ̺|η|+|γ| exp[−βU (η)]
∑
G∈D(η;γ)
wG(L;η,γ ), (4.53)
whereL is a conﬁguration of lines(edges).
The main points of proof. The proof is based on the induction procedure. It
is very easy to see the cancellation of the contributions of t he correspond-
ing graphs, for example, for kernels T (x1,x 2|y1) and T (x1,x 2|y1,y 2). To
facilitate these calculations, it is better to consider ins tead of the equation
(4.47) the equation for kernels that are integrated in varia blesy1,...,y n:
ˆT (η|n) :=
∫
Γ (n)
T (η|γ)dγ =
∫
Rdn
(dy)nT (η|{y}n
1), (4.54)
especially since this is the value that must be substituted i nto the formula
for the solution (4.34).
ˆT (η|n) = ̺e−βW (x1;η(ˆx1))
n∑
k=0
(n
k
) ∫
(dy)kK(x1; {y}k
1) ˆT (η(ˆx1) ∪ {y}k
1)|n −k)−
−
n∑
k=1
(n
k
) k∑
l=1
(k
l
) ∫
(dy)lK(x1; {y}l
1) ˆT (η|n −k) ˆT ({y}l
1|k −l).
(4.55)
Fork = 0 in the ﬁrst line of formula (4.55), the term ˆT (η(ˆx1)|n) corresponds
to the analytical contribution of all graphs D(η;γ), in which the vertex x1
has no edges. For k ≥ 1 the set of graphs for ˆT (η(ˆx1) ∪ {y}k
1)|n −k) is
arranged in such a way that k vertices from n vertices of the conﬁgura-
tion γ are transformed into vertices, which are connected to the gr aphs of
ˆT (η(ˆx1)|n −k) either by means of lines or as free vertices. If a vertex yi
is already connected by at least one line, then joining a line with vertex
12
x1 leaves this graph in the set D(η;γ). If the vertex did not have edges,
then operation
∫
(dy)lK(x1; {y}l
1) does not ensure that it belongs to the
set D(η;γ), and such a diagram should be reduced.This is ensured by the
presence of a similar contribution in the second line of the f ormula (4.55).
This variant occurs in l ofk cases for each of the graphs in ˆT (η|n −k). ■
