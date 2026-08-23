---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-001-2-david-futer-and-francoisgu-eritaud
section_title: "DAVID FUTER AND FRANC¸OISGU ´ERITAUD"
section_number: 2
pages: 2-2
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifoldM with"
---
of dihedral angles of the individual tetrahedra. In order for the tetrahedra to ﬁt
together in M, the dihedral angles at each edge ofM must sum to 2π;i no r d e r
for the tetrahedra to be positively oriented, all the angles must be positive. For
a given triangulationτ, the space of solutions to this linear system of equations
and inequalities is a convex polytopeA(τ), with compact closure
A(τ). A point of
A(τ), corresponding to an assignment of tetrahedron shapes that satisﬁes the angle
conditions, is called anangle structureon τ. See Deﬁnition 3.1 for details.
An angle structure onτ is weaker than a hyperbolic metric, because the linear
equations that deﬁneA(τ) impose a strictly weaker condition on tetrahedra than
do Thurston’s gluing equations. Nevertheless, Casson proved
Theorem 1.1. Let M be an orientable 3–manifold with boundary consisting
of tori, and letτ be an ideal triangulation ofM.I f A(τ) ⁄=∅,t h e nM admits a
complete hyperbolic metric.
In other words, the existence of an angle structure implies the existence of a
hyperbolic structure. Finding this hyperbolic structure requires solving the non-
linear part of the gluing equations. To do this, Casson and Rivin introduced a
volume functional V : A(τ) → R, which assigns to every angle structure onτ the
sum of the hyperbolic volumes of the tetrahedra in this structure. See Deﬁnition 5.2
for a precise deﬁnition. As we shall see in Section 5, the functionV has a number of
pleasant properties: it is smooth and strictly concave down onA(τ), and extends
continuously to
A(τ). Casson and Rivin independently proved
Theorem 1.2. Let M be an orientable3–manifold with boundary consisting of
tori, and letτ be an ideal triangulation ofM.T h e nap o i n tp ∈A (τ) corresponds
to a complete hyperbolic metric on the interior ofM if and only ifp is a critical
point of the functionalV : A(τ) → R.
All told, the Casson–Rivin program can be summarized as follows. Solving
the linear part of Thurston’s gluing equations produces the convex polytopeA(τ).
Solving this linear system is straightforward and algorithmic; by Theorem 1.1,
the existence of a solution implies that a hyperbolic structure also exists. By
Theorem 1.2, solving the non-linear part of the gluing equations amounts to ﬁnding
a critical point (necessarily a global maximum) of the functionalV : A(τ) → R.I n
practice, the search for this maximum point can be accomplished by gradient–ﬂow
algorithms. It is worth emphasizing that a critical point ofV does not always exist:
the maximum ofV over the compact closure
A(τ) will occur at a critical point in
A(τ) if and only all the tetrahedra ofτ are positively oriented in the hyperbolic
metric onM.
