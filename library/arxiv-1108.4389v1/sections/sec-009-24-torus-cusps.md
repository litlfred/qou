---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-009-24-torus-cusps
section_title: "Torus cusps"
section_number: 2.4
pages: 17-19
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
The cusp boundaries of a 3-manifold M arise from the resolution of line defects, and have
the topology of annuli or tori, depending on whether the defects are open or closed. For
simplicity, we will only consider the closed, toroidal case in the present paper, though we
note that annular cusps share many of the the same properties, and can be analyzed in a
similar way.
Suppose, then, that ∂M contains a toroidal cusp
￿
±1
m
±1
Figure 13: Holonomy eigenvalues on
a torus boundary.
boundary T 2. For example, M could be the comple-
ment of a knot in S3. To describe the associated phase
spacePT 2, we can choose a basis of “A and B cycles”
on the torus — typically called meridian and longi-
tude cycles in the case of knot complements. 6 Since
the fundamental group π1(T 2) is abelian, the SL(2, C)
holonomies along these cycles are simultaneously di-
agonalizable, andPT 2 is simply parametrized by their
eigenvalues, cf. [19]:
PT 2 =
{
(m,𝓁 )∈ C∗× C∗}/
Z2, (2.26)
where the Weyl groupZ2 acts by inversion (m,𝓁 )↦→ (m−1,𝓁−1). As above, it is also convenient
to take logarithms7 u≡ logm and v +iπ≡ log𝓁 and to lift the phase space to
PT 2 =
{
(u,v )∈ C× C
}
/Z2. (2.27)
Then the symplectic structure of PT 2 becomes ωT 2 = 2
ℏdv∧du [8], or
{v,u} = ℏ/2. (2.28)
The logarithmic eigenvalues u and v can both be computed as linear combinations of
edge parameters Zi, Z′
i, Z′′
i of tetrahedra in a triangulation of M. To see this, recall that
a cusp boundary T 2 is composed of small truncated-vertex triangles of the tetrahedra ∆ i.
Thus, it comes with a (Euclidean) 2d triangulation, as illustrated in Figure 14. The dihedral
angles of tetrahedra ∆i become actual (complexiﬁed) angles in the 2d triangles. Logarithmic
holonomies can be computed by adding and subtracting the angles subtended by a given
path, then dividing by two [ 14, 20]. For example, in Figure 14 we have drawn the meridian
and longitude of the ﬁgure-eight knot complement on a boundary T 2. The corresponding
6For a knot complement in S3, M =S3\K, there is actually a canonical choice of cycles. The meridian is
an inﬁnitesimally small loop linking the knot K once, while the longitude intersects the meridian once and is
nullhomologous in M (in particular, it has zero linking number with the knot). Presently, however, we will
allow ourselves the freedom of choosing any basis of cycles whatsoever.
7As discussed in [12], the shift byiπ inv+iπ = log𝓁 characterizes the correct lift fromPSL (2, C) structures
(most naturally computed by triangulation data) to SL(2, C).
– 16 –
D
B
z￿￿
zz￿
z￿￿
z z￿
AC
C
A
ww￿
w￿￿
w w￿
w￿￿
B
D
w w
￿
w
￿￿
z z
￿
z
￿￿
w
w
￿
w
￿￿
z
z
￿
z
￿￿
w
w
￿
w
￿￿
z
z
￿
z
￿￿
ww
￿
w
￿￿
zz
￿
z
￿￿
m
￿
glue
Figure 14: Gluing two tetrahedra, as indicated by calligraphic letters on the faces, to form the ﬁgure-
eight knot complement. On the right is a map of the resulting torus cusp boundary, triangulated by
Euclidean vertex triangles.
holonomies are
U≡ 2u =Z′−W (2.29a)
2v = 2(Z−Z′) (2.29b)
As functions on the product phase space P{∂∆i} ≃ {(Z,Z′Z′′,W,W ′Z′′)|Z +Z′ +Z′′ =
W +W′ +W′′ =iπ}, these satisfy the expected commutation relation {v,U} = ℏ.
Continuing with the example of the ﬁgure-eight knot complement, we ﬁnd that the tri-
angulation of Figure 14 has two internal edges, with corresponding gluing constraints
C1 = 2Z +Z′′ + 2W +W′′→ 2πi, C 2 = 2Z′ +Z′′ + 2W′ +W′′→ 2πi. (2.30)
(It is easy to read these oﬀ from the map of the cusp, since every internal edge begins and ends
at a “vertex” on the cusp triangulation. One just adds the angles surrounding the vertex.)
Note thatC1 andC2 both commute withU andv. Moreover, prior to enforcing the condition
C1 =C2 = 2πi, there is an automatic relation C1 +C2 = 4πi, so that one of the two gluing
constraints is redundant. In general, for every closed torus cusp in a 3-manifold M, there
will be one such redundant gluing constraint. In the end, for our ﬁgure-eight example, we see
thatP∂M =PT 2 =P{∂∆i}
//
(C1 = 2πi) =P{∂∆i}
//
(C2 = 2πi).
The Lagrangian submanifold for the ﬁgure-eight knot complement is obtained by the
symplectic reduction procedure described at the end of Section 2.2 above. One starts with
the product Lagrangian
L{∆i} ={z +z′−1− 1 = 0, w+w′−1− 1 = 0} ⊂ P{∂∆i}, (2.31)
where z = eZ,z = eZ′
,w = eW, and w′ = eW′
; rewrites the equations in terms of m2 = eU,
𝓁 =−ev, and one of the gluing monomials cj = eCI; eliminates all remaining variables that
do not commute with cj; and sets cj = 1. The end result is
LM ={𝓁− (m4−m2− 2−m−2 +m−4) +𝓁−1 = 0} ⊂ PM, (2.32)
and this equation is the well known “A-polynomial” of the ﬁgure-eight knot [ 19, 8].
– 17 –
