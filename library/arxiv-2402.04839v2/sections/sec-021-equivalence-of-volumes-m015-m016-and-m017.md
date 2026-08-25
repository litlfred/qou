---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-021-equivalence-of-volumes-m015-m016-and-m017
section_title: "Equivalence of volumes: m015, m016 and m017"
section_number: null
pages: 27-28
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
SnapPy gives the following output for
C=Manifold(‘m015’),D=Manifold(‘m016’)andE=Manifold(‘m017’):
In: C.gluing_equations(form=‘rect’)
Out:
[([1, 1, 1], [-1, 1, -1], -1),
([0, 0, 0], [1, -2, 1], 1),
([-1, -1, -1], [0, 1, 0], -1),
([0, 0, 0], [-1, 1, 0], 1),
([3, 1, -1], [0, -1, 0], -1)]
In: D.gluing_equations(form=‘rect’)
Out:
[([1, 0, 1], [-1, 1, 0], -1),
([-1, -1, 0], [2, -1, -2], -1),
([0, 1, -1], [-1, 0, 2], 1),
([-2, 0, -1], [2, 0, 0], 1),
([0, 0, 0], [-2, 2, 2], 1)]
In: E.gluing_equations(form=‘rect’)
Out:
[([1, 0, -2], [-1, 1, 1], -1),
([0, -1, 2], [1, 0, 0], 1),
([-1, 1, 0], [0, -1, -1], -1),
([-1, 0, -2], [-1, 1, 0], -1),
([0, -1, 0], [-1, 0, 0], 1)]
Usingu,v,was variables for each system, respectively, we useSageto find the unique solution
consisting of complex numbers with positive imaginary part for each system. In approximate
values, these solutions are
u1 =u 2 =u 3 = 0.662359 + 0.56228i
v1 = 0.78492 + 1.30714i,v2 =v 3 = 0.122561 + 0.744862i
w1 = 0.662359 + 0.56228i,w2 =w 3 = 0.78492 + 1.30714i
We therefore expect to find that the exact values for all ofu 1,u 2,u 3 andw 1 are identical.
Additionally, we expectv 1 =w 2 =w 3 = 1
1−u1
andv 2 =v 3 = u1−1
u1
.
27
Again, we compute a Groebner basis for all three sets of gluing equations along with the hy-
pothesised relations between shapes. The output is the following:
{1−z1 +z1 3,
−z1 +z2,−z1 +z3,
w3−z1 2,
w2−z1 2,
w1−z1−z1 2,
v3−z1−z1 2,
v2−z1−z1 2,
v1−z1}
This is confirmation that the geometry of the tetrahedra used to triangulate the manifoldsm015,
m016 andm017 are identical, and the manifolds do indeed have the same hyperbolic volume.
28
