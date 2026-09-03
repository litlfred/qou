---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-007-3-positively-multiplicative-graphs-random-walks
section_title: "Positively multiplicative graphs, random walks and Fourier transform"
section_number: 3
pages: 14-15
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
In this section, we introduce the notion of integrable positively multiplicative graph which is the
central property of the family of graph {Bk,n; 1≤ k≤ n}. We also introduce a general Fourier
transform formalism to study a class of Markov chains naturally constructed from those graphs.
Although some results of the present section are needed in the sequel of the paper, its content is
quite general to enlighten a universal behavior.
Let us recall the deﬁnition of a positively multiplicative graph from [28]. In this paper, a
(directed) graph is the data of a ﬁnite setV and a adjacency matrixA on the vector spaceL2(V ) =⨁
v∈V ev, by which we mean an operator A ∈ B(L2(V )) such that Aev = ∑
v′∈V Av′vev′ with
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 15
avv′ ≥ 0 for all v,v′∈ V . We add a Hilbert space structure on L2(V ) with the scalar product
⟨ev,ev′⟩ = δvv′. The Hilbert space L2(V ) can be seen as the algebra of L2-functions on V with
respect to the counting measure, and for x∈L2(V ), we writex(v) for the coordinate of x alongev.
Deﬁnition 3.1 (See [28]). A ﬁnite graph Γ = (V,A ) is said positively multiplicative (abbreviated
PM) at v0∈ V if there is a commutative algebra A such that C[A]⊂A⊂ End(L2(V )) and such
thatA admits a basis B ={sv,v∈V} with svev0 =ev,
Asv =
∑
v′∈V
Av′vsv′, svsv′∈
∑
v′′∈V
R+sv′′.
A PM graph is said integrable if A is diagonalizable on L2(V ).
The algebraA is called the enveloping algebra of Γ in the sequel. Remark that in general A is
bigger that C[A], since A may for example have eigenvalues with multiplicities larger than 1. For
a PM-graph there is a isomorphism
(6) S :
{
L2(V )→ A
ev↦→ sv
(which reﬂects the fact that dim A =|V|. It can then be deduced that sv0 = IdL2(V ) (see [28,
Theorem 3.12]).
