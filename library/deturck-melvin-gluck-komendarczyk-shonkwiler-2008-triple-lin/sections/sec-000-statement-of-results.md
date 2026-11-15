---
doc_id: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-000-statement-of-results
section_title: "Statement of results"
section_number: null
pages: 3-5
source_pdf: deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-linking-numbers.pdf
source_sha256: db149864ce367da2
toc_source: outline
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
---
Statement of results
Consider the configuration space
Conf3S3 ⊂S3 × S3 × S3
of ordered triples (x, y, z) of distinct points in the unit 3-sphere S3 in R4.
Since x, y and z are distinct, they span a 2-plane in R4. Orient this plane
so that the vectors from x to y and from x to z form a positive basis, and
then move it parallel to itself until it passes through the origin. The result
is an element G(x, y, z) of the Grassmann manifold G2R4 of all oriented
2-planes through the origin in R4. This defines the Grassmann map
G : Conf3S3 −→G2R4.
It is equivariant with respect to the diagonal O(4) action on S3 × S3 × S3
and the usual O(4) action on G2R4.
Figure 1: The Grassmann map
The Grassmann manifold G2R4 is isometric (up to scale) to the product
S2 × S2 of two unit 2-spheres.
Let π: G2R4 →S2 denote orthogonal
projection to either factor.
Given any ordered oriented link L in S3 with three parametrized com-
ponents
X = {x(s) | s ∈S1} , Y = {y(t) | t ∈S1} and Z = {z(u) | u ∈S1},
254
DETURC, GLUCK, KOMENDARCZYK, MELVIN et al
where S1 is the unit circle in R2, we define the characteristic map of L
gL : T 3 = S1 × S1 × S1 −→S2
by gL(s, t, u) = π(G(x(s), y(t), z(u))). In Section 3 we give an explicit
formula for this map as the unit normalization of a vector field on T 3
whose components are quadratic polynomials in the components of x(s),
y(t) and z(u).
The homotopy class of gL is unchanged under any link homotopy of
L, meaning a deformation during which each component may cross itself,
but different components may not intersect.
Theorem A. The pairwise linking numbers p, q and r of the link L are
equal to the degrees of its characteristic map gL on the 2-dimensional
coordinate subtori of T 3, while twice Milnor’s µ-invariant for L is equal
to Pontryagin’s ν-invariant for gL.
Remark 1. Milnor’s µ-invariant, typically denoted µ123, is descriptive of
a single three-component link. In contrast, Pontryagin’s ν-invariant is the
cohomology class of a difference cocycle comparing two maps from T 3 to
S2 that are homotopic on the 2-skeleton of T 3. In particular, it assigns to
any pair g, g′ of such maps whose degrees on the coordinate 2-tori are p,
q and r, an integer ν(g, g′) that is well-defined modulo 2 gcd(p, q, r). With
this understanding, the last statement in Theorem A asserts that
2(µ(L) −µ(L′)) ≡ν(gL, gL′)
mod 2 gcd(p, q, r),
for any two links L and L′ with the same pairwise linking numbers p, q
and r.
We will sketch here two quite different proofs of Theorem A, a topologi-
cal one in Section 4 using framed cobordism of framed links in the 3-torus,
and an algebraic one in Section 5 using the group of link homotopy classes
of three-component string links and the fundamental groups of spaces of
maps of the 2-torus to the 2-sphere.
TRIPLE LINKING NUMBERS AND INTEGRAL FORMULAS
255
To state the integral formula for Milnor’s µ-invariant when the pairwise
linking numbers are zero, let ω denote the Euclidean area 2-form on S2,
normalized so that the total area is 1 instead of 4π. Then ω pulls back
under the characteristic map gL to a closed 2-form on T 3, which can
be converted to a divergence-free vector field VL on T 3 via the formula
(g∗
Lω)(X, Y ) = (X × Y )  VL. In Section 6 we give explicit formulas for
VL, and also for the fundamental solution φ of the scalar Laplacian on the
3-torus as a Fourier series in three variables. These are the key ingredients
in the integral formula below.
Theorem B. If the pairwise linking numbers p, q and r of the three
components of L are all zero, then Milnor’s µ-invariant of L is given by
the formula
µ(L) = 1
2
Z
T 3×T 3 VL(σ) × VL(τ)  ∇σφ (σ −τ) dσ dτ.
Here ∇σ indicates the gradient with respect to σ, the difference σ −τ
is taken in the abelian group structure of the torus, and dσ and dτ are
volume elements. The integrand is invariant under the action of the group
SO(4) of orientation-preserving rigid motions of S3 on the link L, attesting
to the naturality of the formula. We will see in the next section that the
integral above expresses the “helicity” of the vector field VL on T 3.
