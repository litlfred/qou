---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-033-34-loop-groups-primary-fields-tensor-product-theor
section_title: "Loop groups, primary fields, tensor product theorem for initial terms"
section_number: 34
pages: 214-220
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
34. Loop groups, primary fields, tensor product theorem for initial
terms 34.7
In Sect. 33, Subsect. 33.1 we recalled the basis of affine Lie algebras, the connection
with affine vertex operator algebras and the classification and correspondence between
their irreducible representations. In this section we recall the basic elements of affine Lie
algebra CFT.
A first main result of this section is Theorem 34.7, where we relate the spaces of initial
terms of primary fields with the tensor product bifunctor constructed in Theorem 2.8 a).
The constructions of Verma modules for affine Lie algebras, see V.G. Kac [103] (10.4.6),
and proofs of Prop. 2.1 and Theorem 2.3 in Tsuchiya and Kanie [170] should be regarded
as helpful and preliminary material.
Then with Remark 38.16. we identify the braiding of Rep(Vgk) constructed in Cor.
2.9 and described explictly in Theorem 33.11 with that arising from the setting of CFT,
following the work of Knizhnik-Zamolodchikov [114] and Tsuchiya-Kanie [170] and focusing
on the subsequent developments by Wassermann [181] and Toledano-Laredo, [169], in the
analytic functional setting. It will suffice to apply this identification to special pairs of

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 215
the form (V, Vλ) and (Vλ, V ). These works are in the setting of loop groups, and we start
recalling the basic terminology and some of their results. (See also the works by Gui, [73],
[74], [75], [76], [77] which expand these results and include the setting of vertex operator
algebras.)
The comparison between the braided symmetry of Rep(A(Vgk
)) and the braiding properties in the setting of loop groups will be achieved using the following Corollary 35.1,
discussed in [169], [181],38.16.
The tensor product bifunctor of Huang-Lepowsky [87] (W1, W2) → W1 ⊠HL W2 is explicitly determined by the irreducible modules and intertwining operators between irreducible
modules, and in the case of interest Rep(Vgk
), this is in turn closely related to the study
of initial terms of primary fields. We shall describe these connections in Sect. 37, 38.
34.1. Classification of simple projective unitary representations of LG, connection with the VOA setting. A simple Vgk
-modules Lλ,k corresponds to a projective
unitary representation π of the loop group LG = C
∞(G, T) on a Hilbert space H of positive energy. This is a strongly continuous representation π : LG → PU(H) that extends to
the semidirect product LG⋊Rot(T), where Rot(T) is the rotation group of the circle which
acts on LG by translation. It is required that the infinitesimal generator d of rotations acts
with spectrum bounded below and has finite dimensional subspaces. A simple projective
representation π is uniquely determined by an integer k, the level, and the top level H[0],
a simple representation of G, called the lowest energy subspace in [169]. For the sake of
completeness we summarize the classification result. We have a decomposition of H as a
Hilbert space direct sum
H =
M
HS
n∈N
H[n],
with H[n] is the subspace of H such that the rotation π(Rθ) by θ acts as multiplication
by e
inθ. Consider the algebraic direct sum
Hfin =
M
n∈N
H[n]
as a representation of the Kac-Moody algebra, the semidirect product gˆ⋊Cd (it corresponds
to gC in Kac book [103] and gˆC in [169]). This space is a core for the infinitesimal selfadjoint
generator d of the rotation group π(Rθ) = e
iθd. The operator d acts as multiplication by
n on H[n]. We write
a(m) := a ⊗ t
m, a ∈ g.
An element X ∈ g ⊗ C[t, t−1] gives rise to a one-parameter projective group in LG and
therefore to an operator π(X) via Stones’ theorem which has Hfin as a core and is determined up to a constant. The constant may be fixed by a suitable convention, see Theorem
1.2.1 of [169]. X → π(X), d → d is a unitarizable representation of the Kac-Moody algebra
on Hfin. Thus relation (33.2) holds in the representation space, and the central element k
acts as a positive integer k, the level. Fusion tensor product in this setting has been studied
by Wassermann [181] for G = SU(N), Toledano Laredo for G = Spin(2n) [169]. The other

216 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Lie types and connections between Connes fusion tensor product of the category of finite
projective representations of LG of finite energy and the tensor product of the category
of Vgk
-modules of the corresponding affine vertex algebra with tensor product structure
of Huang and Lepowsky of affine vertex operator algebras has been given by Gui [73],
[74], [75], [76], [77]. Gui described applications to a comparison between representation
categories of conformal nel and VOAs. In the setting of loop groups we shall need some
formulas regarding the braiding that may be found in [181] and [169]. These formulas hold
also in the other cases by the mentioned developments by Gui.
34.2. The conformal Hamiltonian L0. Let C ∈ U(g) be the Casimir element, that is
C =
P
i XiXi
, where Xi ∈ g is a basis, Xi a dual basis with respect to the form ⟨⟨ξ, η⟩⟩.
Since C is a central element, for any representation π of g
Cπ = π(C) ∈ (π, π).
On an irreducible highest weight representation Vλ, CVλ
acts as the positive scalar
Cλ = ⟨⟨λ, λ + 2ρ⟩⟩.
For X ∈ g, we define the formal Laurent series
X(t) = X
n∈Z
X(n)t
−n−1
.
A construction by Segal-Sugawara ([163], [167]) gives gives the Virasoro (or energy-momentum)
field,
T(t) = X
n∈Z
Lnt
−n−2
.
Then the endomorphisms act on the representation space and satisfy the Virasoro algebra
relations
[Lm, Ln] = (m − n)Lm+n +
ck
12
(m3 − m)δ−m,n,
where ck is called the central charge and is a known constant [61]. The element
L0
is the conformal Hamiltonian, and in our case is given by a special case of the SegalSugawara construction, Sect. 9.4 in [152], see also Sect. 1.2 in [169],
L0 =
1
k + h
∨
(
1
2
X
i
Xi(0)X
i
(0) + X
m>0
X
i
Xi(−m)X
i
(m)).
On the lowest energy space H[0] of a simple level k projective positive energy representation of LG corresponding to the weight λ in the alcove Λ+
k
, (previously denoted the top
space Lk,λ[0] = L(λ) of the semple Vgk-module Lk,λ, in the VOA setting) the conformal
Hamiltonian L0 acts as the scalar
∆λ =
Cλ
2(k + h
∨)
. (34.1)

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 217
Moreover, L0 satisfies the same commutation relation as d, that is [L0, X(n)] = −nX(n),
thus
L0 = d + ∆λ
on Lk,λ. It follows that ∆λ is the minimal eigenvalue of L0 on Lk,λ.
34.3. Primary field, initial term. The important notion of primary field was introduced by Knizhnik and Zamolodchikov [114], continued by Tsuchiya and Kanie [170]. Our
exposition in the setting of loop groups is influenced by Toledano-Laredo thesis [169].
Let V be a finite dimensional unitary representation of G. Then V [t, t−1] is a representation of g ⊗ C[t, t−1
] that extends to g ⊗ C[t, t−1] ⋊ Rot(T) by Rθf(t) = e
−iθt,
X(m)v(n) = (Xv)(m + n) dv(n) = −nv(n).
Definition 34.1. Let Hi, Hj be simple (positive energy) representations of LG of level
k ∈ N and let Vh be a unitary simple G-module. A primary field is a linear map
ϕ : Vh[t, t−1] ⊗ Hfin
i → Hfinj
that intertwines the action of g⊗C[t, t−1]⋊Rot(T). The G-module Vh is called the charge
of ϕ, the representations Hi and Hj are called the source and target respectively.
We set, for v ∈ Vh,
ϕ(v, n) = ϕ(v ⊗ t
n
) : Hfin
i → Hfinj
.
We represent ϕ as a formal operator-valued distribution
ϕ(v, t) = X
n∈Z
ϕ(v, n)t
−n−∆ϕ
,
where
∆ϕ := ∆i + ∆h − ∆j,
is called the conformal weight (or conformal dimension, scaling dimension) of the field ϕ,
and ∆i, ∆h, ∆j are defined as in (34.1). The intertwining relation of ϕ can be written as
[X(m), ϕ(v, t)] = ϕ(Xv, t)t
m, [d, ϕ(v, t)] = (t
d
dt + ∆ϕ)ϕ(v, t). (34.2)
The following form for (34.2) is also useful,
[X(m), ϕ(v, n)] = ϕ(Xv, m + n), [d, ϕ(v, n)] = −nϕ(v, n). (34.3)
Definition 34.2. The equation on the left hand side of (34.2) or (34.3) is called gauge
condition, see [170].
The equation of the right hand side of (34.2) or (34.3) also has an interesting interpretation, see Remark 34.6. It implies the following important grading relations,
ϕ(v, n) : Hi[k] → Hj[k − n], k ∈ Z≥0, n ∈ Z. (34.4)
It follows in particular that ϕ(v, 0) restricts to a G-intertwiner
Tϕ : Vh ⊗ Hi[0] → Hj[0].

218 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Definition 34.3. The G-intertwiner Tϕ is called the initial term of ϕ. We denote by
IG(Vh⊗Hi[0], Hj[0]) the subspace of HomG(Vh⊗Hi[0], Hj[0]) of initial terms Tϕ of primary
fields with charge the irreducible G-representation Vh, source Hi and target Hj.
Proposition 34.4. (Prop. 2.1 in [170]) The initial term Tϕ of a primary field
ϕ : Vh[t, t−1] ⊗ Hfin
i → Hfinj
of fixed charge Vh acting between fixed irreducible representations uniquely determines ϕ.
Thus the linear map
ϕ → Tϕ ∈ HomG(Vh ⊗ Hi[0], Hj[0])
is faithful.
Remark 34.5. By Theorem 2.3 in [170] and Theorem 3.2.3 in [61], a quotient relation is
well known that describes morphisms of HomG(Vh⊗Hi[0], Hj[0]) that arise as initial terms
of primary fields. This quotient relation is a property of the irreducible representation Hfin
i
.
It is derived from a presentation of the ideal of a Verma module at level the positive integer
k with quotient the irreducible Hfin
i
(or Hfin
j
).
For all g, the linear space IG(Vh ⊗ Hi[0], Hj[0]) has dimension given by the dimension
of the corresponding primary fields by Prop. 34.4. The term fusion rules in the setting
of vertex operator algebras is used to denote this dimension, see Def. 37.2, but also the
linear space to which it refers.
Following [170], only for this section, we use the notation of ϕ as a vertex, on top we put
the charge of ϕ.
ϕ
h
j,i, or 
h
ji
to represent a primary field with initial term in HomG(Vh⊗Vi, Vj ). In the sections regarding
vertex operator algebras Sect. 37, 38, we shall conform to the notation of intertwining
operators, with the charge on the bottom left of the vertex, the source on the bottom right
and the target on top.
Remark 34.6. The equation on the right hand side of of (34.2) (or 34.3) appears in the
literature written in terms of L0, as
[L0, ϕ(v, t)] = (t
d
dt + ∆h)ϕ(v, t), (34.5)
with ∆h the minimal eigenvalue of L0 on the level k representation with top space Vh. This
equation is the part for m = 0 of the equation of motion of [114], [170] that involves the
whole Virasoro field Lm, m ∈ Z. In the case of vertex operator algebras, the corresponding equation involving the Virasoro field follows from the Jacobi identity for intertwining
operators. We shall comment more on this in Sect. 38, see (38.1).
The classification of irreducible representations of the affine Lie algebra gˆ at level k ∈
N via their restriction to (irreducible) representations of the corresponding classical Lie
algebra with dominant weights in the open Weyl alcove Λ+
k
, is discussed in [61].

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 219
34.4. The tensor product Theorem 34.7.
Theorem 34.7. a) There is a connection between
i) the subspace IG(Vh ⊗Hi[0], Hj[0]) of HomG(Vh ⊗Hi[0], Hj[0]) of initial terms of charged
primary fields with charge an irreducible G-representation Vh ∈ Λ
+
k
, associated to simple
positive energy representations of L(G) at level k ∈ N and
ii) the tensor product bifunctor ⊠ of the representation category of the Zhu algebra A(Vgk
)
defined by the weak quasitensor structure (F0, G0) of the forgetful functor of Rep(A(Vgk
))
derived from the weak quasi-bialgebra structure of A(Vgk
) arising from the corresponding
quantum group at a root of unity Uq0(g) as in Theorem 2.8. The connection is given as
follows.
b) The choice of a weak quasi-tensor structure (F0, G0) for Zhu functor Z as in Theorem
2.8 induces the following description of spaces of initial terms,
{T ∈ HomG(Vh ⊗ Hi[0], Hj[0]) : T G0F0 = T} ≃ IG(Vh ⊗ Hi[0], Hj[0]). (34.6)
An element T ∈ IG(Vh ⊗ Hi[0], Hj[0]) decomposes as
T = T Fˆ
0,
with
Tˆ = T G0 ∈ HomA(Vgk
)(Vh ⊠ Hi
[0], Hj[0]) ⊂ Rep(A(Vgk)).
The linear map
T ∈ IG(Vh ⊗ Hi[0], Hj[0]) → Tˆ = T G0 ∈ HomA(Vgk
)(Vh ⊠ Hi
[0], Hj[0])
is an isomorphism with inverse
Tˆ → T = T Fˆ
0.
c) Assume that one of the charge Vh or the eigenspace Hi[0] of the source with minimal
eigenvalue of L0 is the fundamental representation V of g, chosen as in [185] and that g ̸=
E8. Then G0F0 is the unique (selfadjoint) idempotent corresponding to Wenzl idempotent
onto the unique maximal non-negligible addendum of Vh(q0)⊗Vi(q0) of Uq0(g) via the twist
construction and continuous path as described in Sect. 33. We have
IG(Vh ⊗ Hi[0], Hj[0]) = HomG(Vh ⊗ Hi[0], Hj[0]). (34.7)
Proof. a) A characterization of IG(Vh ⊗ Hi[0], Hj[0]) is given in Theorem 2.3 in [170] for
g = sl2, [181] for g = slN , Prop. 4.1. in [169] for the other Lie types in the setting of
affine Lie algebras or loop groups; and Theorem 3.2.3 in [61] in the setting of affine vertex
operator algebras. It follows automatically that charge space Vh belongs to the Weyl alcove
Λ
+
k
.
b) The fact that Tˆ is a morphism in the category of modules of the Zhu algebra follows
from the identification of the Zhu algebra recalled in Sect. 33, Subsect. 33.1, and the
isomorphism property is a consequence of F0G0 = 1.
c) It follows from the characterization result that if one of the charge Vh or the eigenspace
Hi[0] of the source with minimal eigenvalue of L0 is the fundamental representation V of

220 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
g, chosen as in [185], and if i and j vary in Λ+
k
, then IG(Vh ⊗ Hi[0], Hj[0]) = HomG(Vh ⊗
Hi[0], Hj[0]) for g ̸= E8.
Proposition at page 274 in [185] gives a decomposition, for all g, of Vh ⊗ Hi[0] as a
direct sum of a complemented submodule that played a central role in Theorem 2.8 and
denoted by Vh ⊠ Hi[0]. This submodule is defined by the projection F0 and inclusion G0
corresponding to Wenzl construction in the setting of quantum groups via the twist and
continuous path. It follows that (34.6) holds. In particular, (34.7) follows from the fusion
rules of tensor product Vλ ⊗ V in Rep(g) where V denotes the fundamental representation
of g as explained in [185] and already used in this paper.
□
Remark 34.8. Primary fields play a central role in [114], [170], and are also called vertex
operators.
On the other hand, the notion of vertex operator is also used in the setting of vertex
operator algebras with a different but related meaning, see Sect. 22, 23. To avoid confusion
we shall use the term vertex operator only in the vertex operator algebra setting. (Please
note also the historical Remark 5.2 in [102] on vertex operators and reference to the original
articles.)
In Sect. 38, we shall describe the corresponding notion of primary field as in Def. 34.1,
in the setting of vertex operator algebras, see Def. 38.4.
In the case of affine vertex operator algebras, primary fields and their initial terms play a
central role for our purposes, the study of the connection between Huang-Leposwky tensor
product theory and tensor product of the representation category of the Zhu algebra as
described in Theorem 2.8. These developments are considered in Sect. 38.
More precisely, in Subsect. 38.1, we shall introduce a subclass of the class of primary
fields now in the setting of vertex operator algebras as defined in [102], [59]. This is the
subclass defined by a vector in the top space of the charge module and as said it corresponds
to Def. 34.1 in the setting of loop groups. We shall also introduce their initial term.
As said, in Subsect. 38.2 we briefly discuss how this notion reduces to Def. 34.1 and we
re-interpret Theorem 34.7 in the setting of vertex operator algebras.
In Subsect. 38.3 we complete the identification taking into account the associativity
morphisms.
Remark 34.9. Note that at this point of the paper, the notation V seems confusing, in
that it both denotes the fundamental representation of a complex Lie algebra g as in [185]
and a general vertex operator algebra as in Sect. 22. When the two notions are used
simultaneously, we shall refrain from using V for a vertex operator algebra. We hope that
consistent use of the notation Vgkfor the affine vertex operator algebra at level k associated
to g, clarifies the possible confusion.
