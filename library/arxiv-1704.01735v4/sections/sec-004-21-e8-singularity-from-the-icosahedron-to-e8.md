---
doc_id: arxiv-1704.01735v4
doc_title: "Modular curves, invariant theory and E 8"
section_id: sec-004-21-e8-singularity-from-the-icosahedron-to-e8
section_title: "E8-singularity: from the icosahedron to E8"
section_number: 2.1
pages: 8-10
source_pdf: 1704.01735v4.pdf
source_sha256: 3935747ae9291f76
toc_source: inferred
doc_brief: "Modular curves, invariant theory and E 8 — The E8 root lattice can be constructed from the modular curve X(13) by the invariant theory for the simple group PSL(2, 13)."
---
Let us recall some classical result on the relation between the icosahedron
and the E8-singularity (see [31]). Starting with the polynomial invariants of
the ﬁnite subgroup of SL(2, C), a surface is deﬁned from the single syzygy
8
which relates the three polynomials in two variables.
This surface has a
singularity at the origin; the singularity can be resolved by constructing a
smooth surface which is isomorphic to the original one except for a set of
component curves which form the pre-image of the origin. The components
form a Dynkin curve and the matrix of their intersections is the negative of
the Cartan matrix for the appropriate Lie algebra. The Dynkin curve is the
dual of the Dynkin graph. For example, if Γ is the binary icosahedral group,
the corresponding Dynkin curve is that of E8, and C2/Γ ⊂C3 is the set of
zeros of the equation
x2 + y3 + z5 = 0.
(2.1)
The link of this E8-singularity, the Poincar´e homology 3-sphere (see [22]),
has a higher dimensional lifting:
z5
1 + z3
2 + z2
3 + z2
4 + z2
5 = 0,
5
X
i=1
zizi = 1,
zi ∈C
(1 ≤i ≤5),
(2.2)
which is the Brieskorn description of one of Milnor’s exotic 7-dimensional
spheres. In fact, it is an exotic 7-sphere representing Milnor’s standard gen-
erator of Θ7 (see [3], [4] and [20]).
In his celebrated book [23], Klein gave a parametric solution of the above
singularity (2.1) by homogeneous polynomials T, H, f in two variables of
degrees 30, 20, 12 with integral coeﬃcients, where
f = z1z2(z10
1 + 11z5
1z5
2 −z10
2 ),
H =
1
121

∂2f
∂z2
1
∂2f
∂z1∂z2
∂2f
∂z2∂z1
∂2f
∂z2
2

 = −(z20
1 + z20
2 ) + 228(z15
1 z5
2 −z5
1z15
2 ) −494z10
1 z10
2 ,
T = −1
20

∂f
∂z1
∂f
∂z2
∂H
∂z1
∂H
∂z2

 = (z30
1 +z30
2 )+522(z25
1 z5
2 −z5
1z25
2 )−10005(z20
1 z10
2 +z10
1 z20
2 ).
They satisfy the famous (binary) icosahedral equation
T 2 + H3 = 1728f 5.
(2.3)
In fact, f, H and T are invariant polynomials under the action of the binary
icosahedral group. The above equation (2.3) is closely related to Hermite’s
celebrated work (see [19], pp.5-12) on the resolution of the quintic equations.
Essentially the same relation had been found a few years earlier by Schwarz
9
(see [33]), who considered three polynomials ϕ12, ϕ20 and ϕ30 whose roots
correspond to the vertices, the midpoints of the faces and the midpoints of
the edges of an icosahedron inscribed in the Riemann sphere. He obtained the
identity ϕ3
20−1728ϕ5
12 = ϕ2
30. Thus we see that from the very beginning there
was a close relation between the E8-singularity and the icosahedron. More-
over, the icosahedral equation (2.3) can be interpreted in terms of modular
forms which was also known by Klein (see [26], p. 631). Let x1(z) = η(z)a(z)
and x2(z) = η(z)b(z), where
a(z) = e−3πi
10 θ
 3
5
1

(0, 5z),
b(z) = e−πi
10θ
 1
5
1

(0, 5z)
are theta constants of order ﬁve and η(z) := q
1
24 Q∞
n=1(1 −qn) with q = e2πiz
is the Dedekind eta function which are all deﬁned in the upper-half plane
H = {z ∈C : Im(z) > 0}. Then





f(x1(z), x2(z)) = −∆(z),
H(x1(z), x2(z)) = −η(z)8∆(z)E4(z),
T(x1(z), x2(z)) = ∆(z)2E6(z),
where
E4(z) := 1
2
X
m,n∈Z,(m,n)=1
1
(mz + n)4,
E6(z) := 1
2
X
m,n∈Z,(m,n)=1
1
(mz + n)6
are Eisenstein series of weight 4 and 6, and ∆(z) = η(z)24 is the discriminant.
The relations
j(z) := E4(z)3
∆(z) = H(x1(z), x2(z))3
f(x1(z), x2(z))5 ,
j(z) −1728 = E6(z)2
∆(z) = −T(x1(z), x2(z))2
f(x1(z), x2(z))5
give the icosahedral equation (2.3) in terms of theta constants of order ﬁve.
