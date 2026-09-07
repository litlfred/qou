---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-003-13-prior-work-and-our-contributions
section_title: "Prior work and our contributions"
section_number: 1.3
pages: 4-4
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
folds have been considered in [29], although optimization is not its main focus and only analytic
expressions for tangent spaces and gradients have been obtained. In particular, no actual algorithm
appears in [29] — note that a Riemannian steepest descent algorithm in the spirit of [16] would at
least require analytic expressions for geodesics and, to the best of our knowledge, they have never
been derived; in fact prior to this article it is not even known if such expressions exist.
The main contribution of our article is in providing all necessary ingredients for optimization
algorithms on ﬂag manifolds in full details, and from two diﬀerent perspectives — representing a ﬂag
manifold as (i) a homogeneous space, where a ﬂag is represented as an equivalence class of matrices;
and as (ii) a compact submanifold of Rn×n, where every ﬂag is uniquely represented by a matrix.
We will provide four systems of extrinsic coordinates for representing a ﬂag manifold that arise
from (i) and (ii) — while modern diﬀerential geometry invariably adopts an intrinsic coordinate-
free approach, we emphasize that such suitable extrinsic coordinate systems are indispensable for
performing computations on manifolds.
In particular, the analytic expressions for various diﬀerential geometric objects and operations
required for our optimization algorithms will rely on these coordinate systems. We will supply
ready-to-use formulas and algorithms, rigorously proven but also made accessible to applied math-
ematicians and practitioners. For the readers’ convenience, the following is a road map to the
formulas and algorithms:
object on flag manifold results
point Propositions 4.1, 4.10, 5.1, 5.5
tangent vector Propositions 4.3, 4.11, 5.2, 5.6, Corollary 4.12
metric Propositions 4.4, 4.13, 5.7
geodesic Propositions 4.5, 4.7, 4.14, 5.3
arclength Corollary 4.6, Proposition 4.14
geodesic distance Proposition 4.8
parallel transport Propositions 4.9, 4.15, 5.4
gradient Proposition 6.1
Hessian Proposition 6.2
steepest descent Algorithm 1
conjugate gradient Algorithm 2
