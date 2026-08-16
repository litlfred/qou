---
doc_id: arxiv-0901.1612v1
doc_title: "TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INV ARIANTS"
section_id: sec-000-1-statement-of-results
section_title: "Statement of results"
section_number: 1
pages: 2-4
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
doc_brief: "Matemática Contemporânea, Vol. 34, 251–283 © 2008, Sociedade Brasileira de Matemática TRIPLE LINKING NUMBERS, AMBIGUOUS HOPF INVARIANTS — Three-component links in the 3-dimensional sphere were"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
Consider the conﬁguration space
Conf3S3⊂S3×S3×S3
of ordered triples (x,y,z ) of distinct points in the unit 3-sphere S3 in R4. Since x, y
andz are distinct, they span a 2-plane in R4. Orient this plane so that the vectors from
x to y and from x to z form a positive basis, and then move it parallel to itself until
it passes through the origin. The result is an element G(x,y,z ) of the Grassmann
manifold G 2R4 of all oriented 2-planes through the origin in R4. This deﬁnes the
Grassmann map
G : Conf3S3−→G2R4.
It is equivariant with respect to the diagonal O(4) action on S3×S3×S3 and the
usual O(4) action on G 2R4.
G(x,y,z )
x
y zX
Y Z
S3R4
Figure 1. The Grassmann map
The Grassmann manifold G 2R4 is isometric (up to scale) to the product S2×S2 of
two unit 2-spheres. Let π : G2R4→S2 denote orthogonal projection to either factor.
Given any ordered oriented link L in S3 with three parametrized components
X ={x(s)| s∈S1} , Y ={y(t)| t∈S1} and Z ={z(u)| u∈S1},
where S1 is the unit circle in R2, we deﬁne the characteristic map of L
gL : T 3 =S1×S1×S1−→S2
bygL(s,t,u ) =π(G(x(s),y (t),z (u))). In Section 3 we give an explicit formula for this
map as the unit normalization of a vector ﬁeld on T 3 whose components are quadratic
polynomials in the components of x(s), y(t) and z(u).
The homotopy class of gL is unchanged under any link homotopy ofL, meaning a
deformation during which each component may cross itself, but diﬀerent components
may not intersect.
2
Triple linking numbers, ambiguous Hopf invariants and integral formulas
Theorem A. The pairwise linking numbers p, q and r of the link L are
equal to the degrees of its characteristic map gL on the 2-dimensional
coordinate subtori ofT 3, while twice Milnor’s µ-invariant for L is equal to
Pontryagin’sν-invariant for gL.
Remark. Milnor’sµ-invariant, typically denotedµ123, is descriptive of a single three-
component link. In contrast, Pontryagin’s ν-invariant is the cohomology class of a
diﬀerence cocycle comparing two maps from T 3 to S2 that are homotopic on the
2-skeleton of T 3. In particular, it assigns to any pair g,g′ of such maps whose degrees
on the coordinate 2-tori are p, q and r, an integer ν(g,g′) that is well-deﬁned modulo
2 gcd(p,q,r ). With this understanding, the last statement in Theorem A asserts that
2(µ(L)−µ(L′)) ≡ ν(gL,gL′) mod 2 gcd( p,q,r ),
for any two links L and L′ with the same pairwise linking numbers p, q and r.
We will sketch here two quite diﬀerent proofs of Theorem A, a topological one in
Section 4 using framed cobordism of framed links in the 3-torus, and an algebraic one
in Section 5 using the group of link homotopy classes of three-component string links
and the fundamental groups of spaces of maps of the 2-torus to the 2-sphere.
To state the integral formula for Milnor’s µ-invariant when the pairwise linking
numbers are zero, let ω denote the Euclidean area 2-form on S2, normalized so that
the total area is 1 instead of 4 π. Then ω pulls back under the characteristic map gL
to a closed 2-form on T 3, which can be converted in the usual way to a divergence-free
vector ﬁeld VL on T 3. In Section 6 we give explicit formulas for VL, and also for the
fundamental solution ϕ of the scalar Laplacian on the 3-torus as a Fourier series in
three variables. These are the key ingredients in the integral formula below.
Theorem B. If the pairwise linking numbers p, q and r of the three com-
ponents of L are all zero, then Milnor’s µ-invariant of L is given by the
formula
µ(L) = 1
2
∫
T 3×T 3
VL(σ)×VL(τ ) •∇σϕ (σ−τ ) dσdτ.
Here∇σ indicates the gradient with respect to σ, the diﬀerence σ−τ is taken in
the abelian group structure of the torus, and dσ and dτ are volume elements. The
integrand is invariant under the action of the group SO(4) of orientation-preserving
rigid motions of S3 on the link L, attesting to the naturality of the formula. We will
see in the next section that the integral above expresses the “helicity” of the vector
ﬁeld VL on T 3.
3
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
