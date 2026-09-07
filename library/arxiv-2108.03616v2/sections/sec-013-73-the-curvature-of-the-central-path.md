---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-013-73-the-curvature-of-the-central-path
section_title: "The curvature of the central path"
section_number: 7.3
pages: 28-28
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
The condition number ¯χ∗
A also has an interesting connection to the geometry of the cen tral path.
In this context, Sonnevend, Stoer, and Zhao [ SSZ91] introduced a primal-dual curvature notion.
Monteiro and Tsuchiya [ MT08] reveal strong connections between the curvature integral , the
Mizuno-Todd-Ye predictor-corrector algorithm, and the Va vasis-Ye algorithm. In particular,
they prove a bound O(n3.5 log( ¯χ∗
A +n)) on the curvature integral.
Besides the above primal-dual curvature, one can also study the total curvature of the central
path, a standard notion in algebraic geometry. De Loera, Stu rmfels, and Vinzant [ DLSV12]
studied the central curve deﬁned as the solution of the polynomial equations
Ax =b, A ⊤y−s =c x isi =λ ∀i∈ [n], (22)
This includes the usual central path in the region x,s> 0, but also includes the central path of
all other LPs with objective c in the hyperplane arrangement in {x∈ Rn : Ax =b} deﬁned by
the hyperplanes xi = 0; i.e., all LPs where some nonnegativity constraints xi≥ 0 are ﬂipped to
xi≤ 0. In fact, [ DLSV12] shows thato ( 22) deﬁnes the smallest algebraic variety containing the
central path.
They consider the average curvature taken over the bounded r egions in the hyperplane
arrangement, and show a bound 2 π(n−m− 1) for the primal central path (i.e., the projection of
(22) to thex space), and 2π(m−1) for the dual central path (the projection to the s space). Their
argument crucially relies on circuit polynomials deﬁned vi a elementary vectors. See [ DLSV12]
for further pointers to the literature on the total curvatur e of the central path.
