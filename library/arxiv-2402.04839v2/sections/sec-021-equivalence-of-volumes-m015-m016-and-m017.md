---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-021-equivalence-of-volumes-m015-m016-and-m017
section_title: "Equivalence of volumes: m015, m016 and m017"
section_number: null
pages: 27-28
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
Equivalence of volumes: m015, m016 and m017
SnapPy gives the following output for
C=Manifold(‘m015’), D=Manifold(‘m016’) and E=Manifold(‘m017’):
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
Using u, v, w as variables for each system, respectively, we use Sage to find the unique solution
consisting of complex numbers with positive imaginary part for each system. In approximate
values, these solutions are
u1 = u2 = u3 = 0.662359 + 0.56228i
v1 = 0.78492 + 1.30714i, v2 = v3 = 0.122561 + 0.744862i
w1 = 0.662359 + 0.56228i, w2 = w3 = 0.78492 + 1.30714i
We therefore expect to find that the exact values for all of u1, u2, u3 and w1 are identical.
Additionally, we expect v1 = w2 = w3 =
1
1−u1 and v2 = v3 = u1−1
u1 .
27
Again, we compute a Groebner basis for all three sets of gluing equations along with the hy-
pothesised relations between shapes. The output is the following:
{1−z1 + z13,
−z1 + z2, −z1 + z3,
w3 −z12,
w2 −z12,
w1 −z1 −z12,
v3 −z1 −z12,
v2 −z1 −z12,
v1 −z1}
This is confirmation that the geometry of the tetrahedra used to triangulate the manifolds m015,
m016 and m017 are identical, and the manifolds do indeed have the same hyperbolic volume.
28
