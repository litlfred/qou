---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3–manifolds"
section_id: sec-020-equivalence-of-volumes-m006-and-m007
section_title: "Equivalence of volumes: m006 and m007"
section_number: null
pages: 26-27
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
SnapPy gives the following output for
A=Manifold(‘m006’)andB=Manifold(‘m007’):
In: A.gluing_equations(form=‘rect’)
Out:
[([-1, 1, 1], [2, -2, -2], 1),
([0, -1, -1], [-2, 1, 1], 1),
([1, 0, 0], [0, 1, 1], 1),
([-1, 0, 0], [0, -2, 0], 1),
([0, 1, -1], [0, 0, 0], 1)]
In: B.gluing_equations(form=‘rect’)
Out:
[([1, 2, 1], [0, 0, 0], 1),
([-1, -2, -1], [-1, 1, -1], 1),
([0, 0, 0], [1, -1, 1], 1),
([0, -1, -1], [-1, 0, 1], -1),
([1, 1, 0], [1, 0, -1], -1)]
Note that ([a,b,c],[d,e,f],g) translates to the equation
za
1(1−z 1)dzb
2(1−z 2)ezc
3(1−z 3)f =g.
For clarity, we usezvariables for m006 andwvariables for m007.
UsingSage[ Sag23Sag23], we find that both systems of equations have multiple solutions, but only one
solution consisting of complex numbers with positive imaginary part, which is the one we are
interested in. The approximate solutions arez 1 = 0.7733 + 1.4677i,z2 =z 3 = 0.3352 + 0.4011i,
andw 1 =w 3 =−0.1027 + 0.6654i,w 2 = 0.2266 + 1.4677i. As such, we expect the exact values
to satisfyw 2 =z 1−1,w 1 =z 2/(z2−1) andw 3 =z 3/(z3−1). To confirm this, we compute a
Groebner basis from the union of the two sets of gluing equations along with the conjectured
relations betweenwandzvariables. The output is
{z3
1−3z2
1 + 5z1−4,
−z2
1 +z 1 + 2z2−3,
−z2
1 +z 1 + 2z3−3,
w3−z 2
1 + 2z1−3,
w2 +z 1−1,
w1−z 2
1 + 2z1−3}
26
Since the Gr¨ obner basis does not contain 1, the corresponding ideal is proper and hence the
system of equations admits a solution. In particular, the first polynomial in the Gr¨ obner basis
hasz 1≈0.7733+1.4677ias a root, and the remaining polynomials allow us to express the other
variables in terms ofz 1.
This confirms that the geometry of the tetrahedra used to triangulate the manifoldsm006 and
m007 are identical, and the manifolds do indeed have the same hyperbolic volume.
