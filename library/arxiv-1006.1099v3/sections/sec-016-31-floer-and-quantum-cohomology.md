---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-016-31-floer-and-quantum-cohomology
section_title: "Floer and quantum cohomology"
section_number: 3.1
pages: 17-19
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
plectic manifold, meaning that the homomorphisms π2(M) →R deﬁned by the symplectic form
and the ﬁrst Chern class are positively proportional. Recall that a Lagrangian submanifold L is
monotone if the symplectic area and Maslov index homomorphisms π2(M, L) →R are positively
proportional. If M is spherically monotone and π1(L) = 0 then L is automatically monotone,
with minimal Maslov index given by twice the ﬁrst Chern class 2c1(M). We will always assume
that L is orientable and equipped with a Spin structure. Floer cohomology is particularly benign
in the monotone case, since energy and index of holomorphic curves are correlated. For general
background see [34, 76, 13]. Here we collect a number of more specialised results to be used later,
and ﬁx notation.
Monotonicity and orientability imply that L bounds no non-constant holomorphic disk of
Maslov index < 2; since the virtual dimension of unparametrised holomorphic disks with bound-
ary on L in a class β is
n + µ(β) −3
the cycle swept out by boundary values of such disks only contains contributions from Maslov
index 2 disks, and deﬁnes an obstruction class m0(L)[L] ∈Hn(L) which is a multiple of the
fundamental class (the multiple counts how many Maslov index 2 disks pass through the generic
point of L, weighted by their symplectic areas). If the Maslov number of L is > 2, m0(L) = 0 and
HF(L, L) is well-deﬁned as a K-vector space; moreover, one can take K = C (the Spin structures
give orientations of moduli spaces and hence induce a signed diﬀerential in the Floer complex,
so one can work in characteristic zero [36, Chapter 9]; moreover, there are no convergence issues
since only ﬁnitely many holomorphic curves contribute to any given diﬀerential). More generally,
HF(L, L′) is well-deﬁned provided m0(L) = m0(L′), since the square of the diﬀerential in the
complex CF(L, L′) is given by the diﬀerence between these two values, coming from bubbling
along either of the boundary components of the strip [0, 1]×R. The group HF(L, L) is naturally
a unital ring via the holomorphic triangle product, with the unit 1L ∈HF ev(L, L) deﬁned by
counting perturbed holomorphic half-planes with boundary on L.
The quantum cohomology QH∗(M) refers to the “small quantum cohomology”, namely the
vector space H∗(M; K) with grading reduced modulo 2 and with product ∗deﬁned by the 3-point
18
IVAN SMITH
Gromov-Witten invariants counting rational curves through appropriate cycles in M; see [66] for
the details of the construction. The Floer cohomology HF(L, L′) is a bimodule for the quantum
cohomology ring QH∗(M; K), in particular there is a natural map QH∗(M) →HF ∗(L, L), which
is a unital ring homomorphism. Quantum cohomology itself splits naturally as a ring
QH∗(M) =
M
λ∈Spec(∗c1)
QH∗(M; λ)
(3.1)
into the generalised eigenspaces (Jordan blocks) for the linear transformation given by quantum
product ∗c1(M) : QH∗(M) →QH∗(M). This splitting is into subrings which are mutually or-
thogonal for the quantum product. For later, we quote the following result of Auroux, Kontsevich
and Seidel [7] (recall we work with C-coeﬃcients):
Proposition 3.1. The map QH∗(M) →HF ∗(L, L) takes c1(M) 7→m0(L) · 1L.
Sketch. Counting holomorphic disks with one interior marked point, constrained to lie on a closed
cycle in M\L, and one boundary marked point deﬁnes a map
H∗(M, L) ∼= H∗
ct(M\L) −→HF ∗(L, L).
(3.2)
The Maslov class deﬁnes an element of H2(M, L), hence a class in H2n−2(M\L). Fix a cycle
D ⊂M\L representing this class (in [7] this cycle is taken to be a holomorphic anticanonical
divisor disjoint from L, which need not exist in general).
The argument of [7] implies that,
provided L bounds no Maslov index ≤0 disks, (3.2) takes D to twice the obstruction class
2m0(L). (This argument computes the quantum cap action of D on the fundamental class of
L; the fact that L ⊂M\D eliminates the possibility of a non-trivial contribution from constant
holomorphic disks.) On the other hand, over C the map in (3.2) factors through the natural map
H∗(M, L) →H∗(M), and the Maslov cycle maps to 2c1(M) ∈H∗(M). The result follows.
□
The map QH∗(M) →HF ∗(L, L) counts disks with an interior marked point, viewed as input,
and a boundary marked point, which is the output. Following Albers [4], see also [1], one can
reverse the roles of input and output to obtain a map HF ∗(L, L) →QH∗(M). (The domain of
this map would more naturally be the Floer homology of L, but we have used Poincar´e duality
to identify this with Floer cohomology; in particular, the second map is not a ring map, and not
of degree zero.)
Lemma 3.2. The composite map QH∗(M) →HF ∗(L, L) →QH∗(M) is given by quantum
cup-product with the fundamental class [L].
Sketch. The composite counts pairs of disks, each with one interior marked point, and with an
incidence condition at their boundary marked points on L.
Gluing, one obtains a disk with
boundary on L and two interior marked points lying on the real diameter, but no boundary
marked point. The relevant one-dimensional moduli space (with modulus the distance d between
the interior marked points) has another boundary component, where d →0 rather than d →∞;
this is geometrically realised by a degeneration to a disk attached to a sphere bubble which carries
the two interior marked points. Since the disk component has no boundary marked point and a
unique interior marked point, for rigid conﬁgurations it will actually be constant, so the sphere
passes through L. This shows the composite map is chain homotopic to quantum product with
[L]. (Compare to [14, Section 2.4] or [1, Section 6], which study the composite of the maps in
the other order via a similar degeneration argument.)
□
Let V ⊂M be a co-isotropic submanifold which is ﬁbred by circles S1֒ →V →B with reduced
space B. Suppose B and M are monotone and that viewed as a Lagrangian correspondence,
V ⊂B × M has minimal Maslov number k. If in addition k = 2, ﬁx a global angular chain
[σ] ⊂V , which by deﬁnition is a chain with boundary the pull-back π∗
B(eV ) of the Euler class of
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
19
the circle bundle V →B. Finally, let L1, L2 be Lagrangian submanifolds of B, and let ˜Li ⊂M
be the lifts of the Li via V , i.e. the circle bundles over the Li deﬁned by V |Li; note ˜Li ⊂M is
also Lagrangian. Then Perutz’ quantum Gysin sequence [80, Sections 1.4 & 6.1], together with
Wehrheim-Woodward quilt theory, implies:
Theorem 3.3 (Perutz). The Floer cohomology HF(˜L1, ˜L2) is the cohomology of the mapping
cone of quantum cup-product
∗(eV + σ) : CF(L1, L2) →CF(L1, L2)
with the sum of the Euler class of V →B and a correction term σ · 1 ∈QH∗(B), where σ is the
algebraic count of the number of Maslov index 2 disks meeting both a generic point of V and the
global angular chain [σ].
Under the same hypotheses, the Floer cohomology HF(V, V ) (computed in B × M) is the
(chain-level) mapping cone on quantum product by the same element on QH∗(B). If the co-
isotropic V has minimal Maslov number > 2 there is no correction term, and the relevant iso-
morphisms hold with the map being quantum product by the Euler class. The exact triangle
· · · −→HF(L1, L2)
∗(eV +σ)
−−−−−→HF(L1, L2) −→HF(˜L1, ˜L2)
[1]
−→· · ·
(3.3)
is an exact triangle of QH∗(B)-modules, and in particular one obtains analogous triangles for
particular generalised eigenspaces in the sense of Equation 3.1.
