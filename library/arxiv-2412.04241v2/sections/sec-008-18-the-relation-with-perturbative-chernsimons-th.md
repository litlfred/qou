---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-008-18-the-relation-with-perturbative-chernsimons-th
section_title: "The relation with perturbative Chern–Simons theory"
section_number: 1.8
pages: 15-17
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
symmetric matrix with integer entries and a non-degenerate solution z of the Nahm equa-
tions. As such, it looks removed from perturbative Chern–Simons theory with complex gauge
group. In this subsection, we briefly explain the relation betwee Theorem 5 and perturbative
complex Chern–Simons theory.
16 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
To begin with, Chern–Simons theory with a complex gauge group (such as SL 2(C)) was
formulated as a path integral by Witten [48], following his earlier work on a path integral
with compact gauge group (such as SU(2)) [47].
However, there is a crucial difference between complex versus compact Lie groups. The
path integral with compact gauge group satisfies cut-and-paste properties that lead to its ef-
fective computation, and to a combinatorial definition developed by Reshetikhin–Turaev [41,
44]. On the other hand, the path integral with complex gauge group is lacking cut and paste
properties and, to the best of our knowledge, it is unknown for instance how to compute it
for closed 3-manifolds.
For reasons that are not entirely understood, the partition function of Chern–Simons
theory with complex gauge group SL 2(C) for manifolds with torus boundary components
conjecturally reduces to a finite-dimensional integral (the so called-state integral) whose
integrand is a product of Faddeev’s quantum dilogarithm functions [18], assembled out of an
ideal triangulation of the manifold. This was the approach taken by Andersen-Kashaev [3, 2]
and Dimofte [12] following prior ideas of [29, 15]. Focusing for simplicity on the case of a
3-manifold with a single torus boundary component (such as the complement of a hyperbolic
knot in S3), the state-integral is a holomorphic function of τ∈ C′ = C\ (−∞, 0].
We now turn to perturbative Chern–Simons theory with complex gauge group SL 2(C).
Using the above mentioned (state-integral) partition function, in a series of papers the per-
turbation theory was defined first at q near 1 [13] and then for q near an arbitrary complex
root of unity [14]. This perturbation theory depends on the combinatorics of an ideal trian-
gulation of a cusped hyperbolic 3-manifold, a solution z of its Neumann–Zagier equations,
as well as some auxillary choices (of a quad of the tetrahedra and of an edge of the triangu-
lation). These choices lead to a so-called Neumann–Zagier datum, which is a the upper part
(A|B) of a symplectic N×N matrix with integer entries, a vector ν∈ ZN, and a solution
z of the Neumann–Zagier equations
NY
j=1
z
Aij
j (1− 1
zj
)Bij = (−1)νi, i = 1,...N. (45)
The solution z in turn defines a representation π1(M) → PSL2(C) up to conjugation,
which under mild hypotheses can be lifted to a representation ρz to SL2(C). Fixing such a
Neumann–Zagier datum, the complex Chern–Simons perturbative series around ρz are de-
fined in [13, 14] by formal Gaussian integration, and these are none other than the series
Φ(h) of Equation (1) for the case of the 4 1 knot, where ρz is an SL 2(C) lift of the discrete
faithful PSL2(C)-representation of the 4 1 knot.
The symplectic property of ( A|B) the Neumann–Zagier matrix implies that when B is
invertible over Z, then A = I− B−1A is a symmetric N×N matrix with integer entries.
Moreover, the Neumann–Zagier equations (45) are equivalent to the Nahm equations (41),
and what’s more the perturbative series at roots of unity defined by formal Gaussian integra-
tion syntactically matches that of the corresponding Nahm sum (when A is positive definite)
and of the admissible series for general A. This matching is discussed in detail in [24] and is
generalised in Theorem 3.
THE HABIRO RING OF A NUMBER FIELD 17
Putting everything together, it follows that Theorem 5 contains the asymptotics of com-
plex Chern–Simons theory when a 3-manifold with torus boundary has an (essential) ideal
triangulation and a choice of quad with unimodular matrix B. While such a choice is not
known to exist in general, it has been found for all knots with at most 14 crossings using
their default SnapPy triangulation.
