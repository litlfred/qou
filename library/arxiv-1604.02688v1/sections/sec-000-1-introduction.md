---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.996
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Recently, the physicists Dimofte, Gaiotto and Gukov \cite{DGG1,DGG2}
introduced a powerful new invariant for a compact orientable 3-manifold $M$ 
with non-empty boundary $\bd M$ consisting of tori, called the 
\emph{3D-index}. This invariant arises from a gauge theory with $N=2$ 
supersymmetry under a low energy limit, and seems to contain a great deal 
of information about the geometry and topology of the manifold. The 
3D-index is a collection of $q$-series, i.e. formal Laurent series in 
$q^{1/2}$, defined as an infinite sum over integer weights attached to 
the edges of a chosen ideal triangulation $\CT$ of $M$. The $q$-series 
$I_\CT(b)$ are parametrised by a choice of peripheral homology class 
$b \in H_1(\bd M;\Z)$.

 Our goal is to explain how the 3D-index can be viewed as a generating
series of normal surfaces on $\CT$; see Definition \ref{def.Iab} and
Corollary \ref{cor.Izero} below. Normal surfaces depend heavily
on the ideal triangulation whereas the 3D-index should not. Our results
show a connection of the 3D-index with classical normal surface theory, 
and fulfill a `folk dream' of constructing topological invariants of 
3-manifolds using normal surfaces. 

In this paper we first recall how the 3D-index of an ideal triangulation 
is defined, following \cite{GHRS}, and discuss some of its key properties. 
Throughout the paper, by a triangulation of a compact 3-manifold we mean an 
{\em ideal triangulations} in the sense of Thurston \cite{Th} 
(see also \cite{NZ,N}). 
Physics predicts that 
the 3D-index should give a {\em topological invariant} of the underlying 
manifold $M$, but this is not known in general. In fact, the sum defining 
the 3D-index need not even converge (as a formal Laurent series) for all 
ideal triangulations $\tri$.  But we can characterise the good 
triangulations using the {\em normal surface theory} developed by Haken 
\cite{Ha1,Ha2}. (Haken's theory applies to ideal triangulations, when 
restricting to closed normal surfaces.) 
In fact, the work of \cite{GHRS} shows the index sum 
for $I_\CT(b)$ converges for all $b \in H_1(\bd M;\Z)$ if and only
if the triangulation is {\em $1$-efficient}, i.e. contains no embedded 
closed normal surfaces $S$ of Euler characteristic $\chi(S) \ge 0$ 
except peripheral tori. 

By work of Matveev and Piergallini, (see \cite{Ma1, Ma2, Pi, Petronio}), 
any two ideal triangulations $\CT, \CT'$ (with at least 2 tetrahedra) 
of a given compact 3-manifold $M$ with non-empty boundary can be connected 
by a sequence of 2-3 and 3-2 Pachner moves. 
Similarly, we can also consider 0-2 and 2-0 moves on a triangulation as 
shown in Figure \ref{2-3 and 0-2 moves} below.

The work of \cite{Gar,GHRS} shows that the index is invariant under 
2-3/3-2 and 0-2/2-0 moves provided all ideal triangulations involved are 
1-efficient. However it is not currently known whether any two 1-efficient 
triangulations of a given manifold can be connected by 2-3/3-2 and 
0-2/2-0 moves preserving 1-efficiency. 

We then give a new formulation of the definition of index as a sum over 
certain \emph{singular normal surfaces}. The minimum degree of each term 
in this sum then has a simple geometric interpretation involving the 
\emph{Euler characteristic} and the number of \emph{double arcs} of the 
corresponding surface. This leads to new, more direct proofs of results on
the convergence of the series for the 3D-index. We also introduce a class 
of embedded \emph{generalised normal surfaces}, and show how to express the 
index as a sum over terms corresponding to these embedded surfaces.

Next we show that the work of Neumann \cite{N} on combinatorics of ideal 
triangulations can be reinterpreted to give a precise description of the 
set $Q(\T;\Z)$ of all {\em integer solutions} to the $Q$-matching equations 
of Tollefson \cite{To}. Each such solution $S$ represents a 
(possibly singular) \emph{spun normal surface} \cite{KR1,Ti} with 
well-defined homology class $[S]_2  \in H_2(M,\bd M;\Z/2\Z)$ and boundary 
$[\bd S] \in H_1(\bd M;\Z)$ such that the mod $2$ reduction of $[\bd S]$ is
the image of $[S]$ under the boundary map 
$\bd_* : H_1(M;\Z/2\Z) \to H_1(\bd M;\Z/2\Z)$. Further, each pair 
$(a,b) \in H_2(M,\bd M;\Z/2\Z) \times  H_1(\bd M;\Z)$ such that 
$\bd_* a = b \bmod 2$ arises in this way, and the $Q$-normal classes $S$ with 
$[S]_2=0$ and $[\bd S]=0$ are the integer linear combinations of the 
``edge solutions'' and the ``tetrahedral solutions'' constructed by 
Kang-Rubinstein \cite{KR1}.

We then show that the definition of 3D-index can be extended to give a 
$q$-series $I^a_\CT(b)$ for each $(a,b)$ as above; this is a sum over 
$Q$-normal classes $S$ with $[S]=a$ and $[\bd S]=b$ modulo tetrahedral 
solutions. The previous definition of 3D-index only applies to the cases 
where $a=0$ and $b \in H_1(\bd M; 2 \Z)$; we have $I^0_\CT(b) = I_\CT(2b)$ 
in the notation of \cite{GHRS}. Here $I^0_\T(b)$ is also defined for 
$b \in  {\mathcal K} = \Ker\left(H_1(\bd M; \Z) \to H_1(M;\Z/2\Z)\right)$.

We then give some computations of the 3D-index, including an example 
showing that that the series for the 3D-index $I^a_\CT(b)$ can sometimes 
converge for $b \ne 0$ even when the triangulation $\T$ is not 1-efficient 
(so the series for $I_\CT^0(0)$ does not converge).

We conclude with some discussion of experimental results on the 
connectedness of the set of 1-efficient ideal triangulations of a given 
manifold under 2-3/3 and 0-2/2-0 Pachner moves. (Recall that such moves
do not change the 3D-index.) In particular, we find examples of 1-efficient 
triangulations of the solid torus with six tetrahedra that cannot be 
connected by sequences of 2-3/3-2 moves through 1-efficient triangulations. 
These triangulations can, however, be connected via 1-efficient 
triangulations if 0-2 and 2-0 moves are also allowed; hence they have the 
same 3D-index.

Finally, the appendix gives some results on generalised angle structures 
and Euler characteristic for Q-normal surfaces; these extend well-known 
results of Luo-Tillmann \cite{LT} for closed normal surfaces.
