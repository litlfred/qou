---
doc_id: s0002-9947-96-01660-1
doc_title: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS"
section_id: sec-013-37-this-tensor-product-is-composed-with-the-uniq
section_title: "This tensor product is composed with the unique iterate of the twist map P"
section_number: 3.7
pages: 14-16
source_pdf: S0002-9947-96-01660-1.pdf
source_sha256: aa63e62b78aa5045
doc_brief: "AMERICAN MATHEMATICAL SOCIETY INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS — This paper presents an algebraic framework for constructing in- variants of closed oriented 3-manifolds by taking a state"
---
which has its range the state space of U.
Lemma 3.11. The partition function of the standard labelled tetrahedra A and
−A are elements of the state spaces of their boundary. Let Σ∈ S4 be an even
permutation. The element Σ determines combinatorial maps A→ A′ and−A→
−A′,w h e r eA′ is labelled by a compatible labelling {e′
ij}. Under the linear map of
state spaces,
{
e01 e02 e12
e23 e13 e03
}
+
↦→
{
e′
01 e′
02 e′
12
e′
23 e′
13 e′
03
}
+
and
{e01 e02 e12
e23 e13 e03
}
−
↦→
{e′
01 e′
02 e′
12
e′
23 e′
13 e′
03
}
−
.
INVARIANTS OF PIECEWISE-LINEAR 3-MANIFOLDS 4011
If Σ is an odd permutation, then
{e01 e02 e12
e23 e13 e03
}
+
↦→
{e′
01 e′
02 e′
12
e′
23 e′
13 e′
03
}
−
and {
e01 e02 e12
e23 e13 e03
}
−
↦→
{
e′
01 e′
02 e′
12
e′
23 e′
13 e′
03
}
+
.
Proof. The ﬁrst statement follows from the isomorphism Hom(X,Y )∼=X∗⊗Y for
vector spaces X,Y .
In the deﬁnition of the partition function of the tetrahedron, each factor
Hom(ˆb,a⊗c) in the tensor product is identiﬁed with Hom∗(a⊗c,ˆb), using the non-
degenerate symmetric pairing ( α,β )↦→ trL(αβ) in the spherical category. Using
these isomorphisms, the action of the odd and even permutations can be computed
by the following commutative diagrams:
Hom(ˆb,a⊗c)
θ(σ+)
−−−−→ Hom(ˆc,b⊗a)
α↦→trL(α−)
↓
↓α↦→trL(α−)
Hom∗(a⊗c,ˆb)
φ∗
−−−−→ Hom∗(b⊗a, ˆc)
in which φ: β↦→ ˆθ(σ+) ˆβ,a n d
Hom(ˆb,a⊗c)
θ(σ−)
−−−−→ Hom∗(b, ˆc⊗ ˆa)
α↦→trL(α−)
↓
‖‖‖
Hom∗(a⊗c,ˆb)−−−−→
(ˆ )∗
Hom∗(b, ˆc⊗ ˆa).
The map (ˆ )∗ is the adjoint of the linear map ˆ .
From these diagrams, the action of the elements of S4 on the linear functionals
in the deﬁnition of the partition function can be computed. The maps φ andθ(σ+)
correspond, as diagrams, to rotations by one third of a turn, and ˆ corresponds
to one half of a turn. For even permutations in S4, the symmetry property of the
partition function follows from the fact that any even permutation of the vertices
of a tetrahedron can be extended to an isotopy of the sphere. The deﬁnition of
spherical category was constructed to give invariants of isotopy classes of graphs
on the sphere. For odd elements of S4, the symmetry property follows from the
fact that any odd permutation of the vertices of a tetrahedron can be extended to
an isotopy of the sphere which takes the tetrahedron to its image under some ﬁxed
reﬂection in a diameter. The diagrams corresponding to A and−A diﬀer by such
a reﬂection.
Alternatively, the symmetry property can be checked algebraically. As an ex-
ample, consider the odd permutation (0, 1, 2, 3)↦→ (3, 1, 2, 0). The state space of A
is
H(e23,e 13,e 12)⊗H∗(e23,e 03,e 02)⊗H(e13,e 03,e 01)⊗H∗(e12,e 02,e 01)
and the state space of A′ is
H∗(e′
23,e′
13,e′
12)⊗H(e′
23,e′
03,e′
02)⊗H∗(e′
13,e′
03,e′
01)⊗H(e′
12,e′
02,e′
01).
4012 JOHN W. BARRETT AND BRUCE W. WESTBURY
The linear map of state spaces is
x⊗y⊗z⊗t↦→θ∗−1(σ−1)t⊗ θ∗−1(τ)y⊗θ(τ)z⊗θ(σ)x,
whereσ is the permutation (0, 1, 2)↦→ (1, 2, 0), andτ is the permutation (0, 1, 2)↦→
(2, 1, 0). As a map of linear functionals, this is the adjoint of the map
α⊗β⊗γ⊗δ↦→θ(σ)δ⊗ ˆβ⊗ ˆγ⊗ˆθ(σ)ˆα.
The symmetry property is equivalent to the identity
trL
(
ˆγ
(
θ(σ)δ⊗ 1
)(
1⊗ˆθ(σ)ˆα
) ˆβ
)
=t rL
(
β
(
1⊗δ
)(
α⊗ 1
)
γ
)
,
which holds in any spherical category.
