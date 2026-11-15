---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-008-6-some-q-normal-surface-theory
section_title: "Some Q-normal surface theory"
section_number: 6
pages: 10-11
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.991
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
In this section we discuss surfaces in general position with respect to
an ideal triangulation. This discussion is similar to the one of Haken
who studied and encoded normal surfaces in general position with respect
to a triangulation of a closed 3-manifold. A major difference is that amongst surfaces 
in general position with respect to an ideal triangulation is the class of embedded
spun normal surfaces (a concept introduced by Thurston, \cite{Th,Wa}), 
which intersect each tetrahedron 
in a finite number of quadrilaterals, and a possibly infinite number of triangles.
Also, just as in the closed case, a spun normal surface can be reconstructed from its quadrilateral data and the quadrilaterals satisfy the $Q$-matching equations.


Let $M$ be an orientable 3-manifold with boundary consisting of $r$ tori, 
and let $\T$ be an {\em oriented} ideal triangulation with $n$ tetrahedra.
Let $\calE$ denote the set of edges of $\T$, and recall that $\square$ 
denotes the set of quad types in the tetrahedra of $\T$. 
Of course, $|\calE|=n$ and $|\square|=3n$.

Recall that the {\em $Q$-normal surface solution space} $Q(\T;\R)$ for 
$\T$ is a subset of $\R^\square \cong \R^{3n}$ consisting of real quad 
coordinates assigned to the quad types in $\T$
satisfying the $Q$-matching equations of Tollefson. 
After choosing a cyclic ordering of quad types in each tetrahedron, 
compatible with the orientation on $\T$, 
we can write the quad coordinates of $S \in Q(\T;\R)$ as a vector
$$
S=(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n) \in(\R^3)^n= \R^{3n}
$$
where $(a_j,b_j,c_j)$ are the quad coordinates of $S$ in tetrahedron $j$.

Let $Q(\T;\Z) = Q(\T;\R) \cap \Z^{3n}$ be the sublattice of $Q(\T;\R)$ of 
integer solutions, and  let $Q(\T;\Z_+) = Q(\T;\Z) \cap \R_+^{3n} $ denote 
the set of integer solutions with non-negative quad coordinates. Then 
each element $x$ of $Q(\T;\Z_+)$ determines a (possibly singular) 
{\em spun normal surface} in $\T$ obtained by taking $x_A$ disjoint copies 
of the quad $q_A$ together with additional normal triangles. 
The resulting surface  is a (possibly singular) {\em closed normal surface} 
if only finitely many triangles are added, and is {\em embedded} if there 
is at most one non-zero quad coordinate in each tetrahedron.
(See Kang \cite{Kang},  Tillmann \cite{Ti}.)
