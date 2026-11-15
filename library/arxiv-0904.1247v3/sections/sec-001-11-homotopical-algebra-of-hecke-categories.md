---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-001-11-homotopical-algebra-of-hecke-categories
section_title: "Homotopical algebra of Hecke categories"
section_number: 1.1
pages: 3-7
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
in Theorem 1.8, from the perspective of representation theory. We ﬁrst recall two categories of
D-modules of fundamental interest in representation theory and of primary focus in this paper.
1.1.1. Hecke categories.
Deﬁnition 1.1. 1) The Hecke category is the dg category
HG = DG(G/B × G/B) ≃D(B\G/B)
of all B-biequivariant D-modules on G.
2) The monodromic Hecke category is the full dg subcategory
e
HG ⊂DG(G/N × G/N) ≃D(N\G/N)
generated (under colimits) by pullbacks from HG.
3
Both Hecke categories carry natural monoidal structures given by convolution. Thus they form
algebra objects in the symmetric monoidal ∞-category StC.
1.1.2. Character sheaves. The traditional deﬁnition [Lu] of character sheaf (see also [La] for a review
and [Gi, MV, Gr] for geometric approaches to the theory) is based on the horocycle correspondence
G/ad G
G/ad B
p
o
δ
/ B\G/B.
The map p is the natural projection with ﬁbers isomorphic to the ﬂag variety G/B, and the map δ
is the natural projection with ﬁbers isomorphic to B. Pulling back and pushing forward D-modules
gives a functor called the Harish Chandra transform (in the terminology of [Gi])
F = p∗δ! : HG = D(B\G/B)
/ D(G/ad G)
A traditional unipotent character sheaf is a (shift of a) G-equivariant D-module on G that is a
simple constituent of a D-module obtained by applying the transform F to a simple D-module (in
the heart of the standard t-structure on HG). All unipotent character sheaves can be character-
ized geometrically as the simple adjoint-equivariant D-modules on G with singular support in the
nilpotent cone and unipotent central character. Lusztig showed that the collection of all character
sheaves provides a construction of the characters of ﬁnite groups of Lie type, and gave a detailed
classiﬁcation in relation with the structure of the ﬁnite Hecke algebra.
With the above in mind, we make the following deﬁnition in the homotopical setting.
Deﬁnition 1.2. The dg category ChG of unipotent character sheaves is deﬁned to be the full sub-
category of D(G/ad G) generated (under colimits) by the image of the Harish Chandra transform F.
Note that traditional unipotent character sheaves are simple objects of the heart of ChG with
respect to the standard t-structure.
Example 1.3. The above correspondence can be viewed as a collection of Weyl group twisted versions
of the Grothendieck-Springer simultaneous resolution. Namely, if we restrict to the support
pt/B = B\B/B ⊂B\G/B
of the monoidal unit of HG, then we recover (an equivariant global version of) the Grothendieck-
Springer correspondence
G/ad G
eG/G
p
o
δ
/ B\B/B ≃pt/B.
Here eG/G denotes the simultaneous resolution
eG/G = {(g, B′) | g ∈B′}/G ≃B/ad B,
and the map p forgets the ﬂag B′, while the map δ forgets the group element g.
The global version of the Springer sheaf
SG = F(Opt/B) = p∗δ!Opt/B
is the fundamental example of a character sheaf. (Some might prefer to shift SG so that it lies
in the heart of the standard t-structure.) According to [HK], it coincides with Harish Chandra’s
adjoint-equivariant holonomic system of diﬀerential equations obtained by setting all of the Casimir
operators to zero.
1.1.3. Prelude to results: analogy with ﬁnite groups. Our results are perhaps most easily understood
in analogy with the following well-known properties of a ﬁnite group Γ, and speciﬁcally its complex
group algebra C[Γ] and category of ﬁnite-dimensional complex modules Repfd
C (Γ).
1) The group algebra C[Γ] is a ﬁnite-dimensional semi-simple symmetric Frobenius algebra with
nondegenerate functional
τ : C[Γ]
/ C
τ(f) = f(e)/|Γ|
4
where e ∈Γ is the unit.
2) The class functions C[Γ]Γ are the center of the group algebra
z : C[Γ]Γ 
/ C[Γ]
and in particular form a commutative algebra. Equivalently, they are the endomorphisms of the
identity functor of Repfd
C (Γ), and so act universally on any M ∈Repfd
C (Γ).
3) The class functions C[Γ]Γ are the target of a universal trace map
tr : C[Γ]
/ / C[Γ]Γ
initial among all maps that are equal on ab, ba ∈C[Γ], for a, b ∈C[Γ].
Equivalently, they are
the universal recipient of a functorial trace map from endomorphisms of any M ∈Repfd
C (Γ) which
assigns to the identity the character χM ∈C[Γ]Γ.
The symmetric property of the Frobenius algebra is equivalent to the fact that the functional τ
is a trace so admits a factorization
τ : C[Γ]
tr
/ C[Γ]Γ
/ C
It follows that class functions themselves form a commutative Frobenius algebra, with multipli-
cation and functional induced by those of C[Γ] via the center and trace maps.
1.1.4. Results: Hecke categories and character sheaves. To begin, we work with monoidal categories,
by which we mean algebra objects C ∈Alg(StC) in the symmetric monoidal ∞-category of dg
(or stable presentable) categories StC, as categoriﬁed analogues of C-algebras. There are natural
categorical analogues of center and trace
Z(C) = EndC⊗Cop(C)
Tr(C) = C ⊗C⊗Cop C
The ﬁrst is naturally braided, i.e., an E2-algebra in StC, by the general form of the Deligne conjecture
(see [L2]) and comes with a universal central map
z : Z(C)
/ C
The second has a natural S1-action, a generalization of the Connes cyclic structure on Hochschild
chains, and comes with a universal trace map
tr : C
/ Tr(C)
We propose the following notion of a semi-rigid monoidal category as a categoriﬁed analogue of
ﬁnite-dimensional semi-simple algebra (see Section 1.3 for further justiﬁcation of this analogy).
Deﬁnition 1.4. A monoidal category C is called a semi-rigid category if C is compactly generated,
and all of its compact objects (or equivalently, a collection of compact generators) are both left and
right dualizable.
Remark 1.5. If in addition the unit of C is compact (or equivalently, its compact and dualizable
objects coincide), then C is also rigid in the sense of [G] (note however that [G] does not require C
to be compactly generated). For example, a quasi-compact derived stack X with aﬃne diagonal is
perfect in the sense of [BFN] when its category Q(X) of quasicoherent sheaves is rigid. We have
introduced the notion of semi-rigid category to accommodate our main example, the Hecke category,
whose unit is not compact.
There are natural weak and strong analogues of the notion of symmetric Frobenius algebra for
semi-rigid monoidal categories, namely pivotal and Calabi-Yau structures.
Deﬁnition 1.6. A pivotal structure on a semi-rigid monoidal category C is a monoidal identiﬁcation
of the operations of taking left and right duals.
5
A pivotal structure equips C with a trace
τ : Tr(C)
/ Vect
factoring the functional given on compact objects (and all objects if 1C is compact) by the pairing
HomC(1C, −) : C
/ Vect
We show in Section 3 that a pivotal structure on a semi-rigid category induces a canonical identiﬁ-
cation of its monoidal center and trace. Pivotal structures however have the disadvantage that they
are not manifestly Morita invariant notions.
Deﬁnition 1.7. A Calabi-Yau structure on a monoidal category C is a trace map
Tr(C)
/ Vect
that is S1-invariant and so that the natural composition
C ⊗C
/ Tr(C)
/ Vect
is the evaluation of a self-duality of C.
The notion of Calabi-Yau category is a Morita invariant notion, however we are not aware of a
“classical” monoidal category interpretation of this strong notion of cyclic trace.
With these deﬁnitions in mind, here is an abstract statement of our main results, in parallel to
the above highlighted statements for ﬁnite groups.
Theorem 1.8. 1) (Theorems 3.18, 6.2, 6.3) The Hecke categories HG and e
HG are semi-rigid, and
carry canonical pivotal and Calabi-Yau structures.
2) (Theorem 6.9) The dg category ChG of unipotent character sheaves is canonically equivalent
to the monoidal center and trace of both Hecke categories HG and e
HG.
Remark 1.9. Perhaps the most interesting aspect of the identiﬁcation of ChG with the monoidal
trace of HG is the consequence that every dualizable Hecke module M has a character χM ∈ChG.
In other words, character sheaves arise as characters of such Hecke modules. To illustrate this point,
consider a spherical subgroup K ⊂G (for example, K a parabolic subgroup, or the ﬁxed points of
an involution). Harish Chandra (g, K)-modules with trivial inﬁnitesimal character are equivalent to
K-equivariant D-modules on G/B. The latter naturally provide a Hecke module where the Hecke
category acts via convolution on the right. The character of this Hecke module is the object of ChG
given by pushing forward the structure sheaf of K/ad K along the natural projection to G/ad G, and
then projecting it onto ChG. For example, the Springer sheaf SG discussed in Example 1.3 is the
character of the left regular representation of the Hecke category.
Remark 1.10. The identiﬁcations of the theorem endow ChG with rich algebraic structures. As a
monoidal center, ChG is naturally an E2-algebra. As a monoidal trace, ChG comes equipped with
an S1-action. In fact, the S1-action is compatible with the loop rotation action on all D-modules
on the loop space G/ad G = L(BG). This is part of the topological ﬁeld theory structure we discuss
in Section 1.3 below.
Remark 1.11. It is interesting to compare the theorem with the independent results of Bezrukavnikov,
Finkelberg and Ostrik [BFO] on the level of abelian categories. Namely, they show that the Drinfeld
center of the abelian category of Harish Chandra bimodules is equivalent to the abelian category
generated by character sheaves. On the one hand, we do not check the compatibility of our con-
structions with t-structures; on the other hand, the derived categories we consider are richer than
the derived categories of their hearts.
6
1.1.5. Langlands duality for character sheaves. The Hecke categories HG and e
HG are connected by a
Langlands duality, namely the Koszul duality of Beilinson-Ginzburg-Soergel [BGS], in the Langlands
dual form developed by Soergel [S] with monoidal structure established by Bezrukavnikov-Yun [BY].
It is most naturally stated in the mixed setting, but since such structures are beyond the scope of this
paper, we will state an equivalence of underlying two-periodic categories. Passing to two-periodic
localizations is a symmetric monoidal functor
{−}per : StC
/ StC[u,u−1]
C ✤
/ Cper = C ⊗C C[u, u−1]
deg u = 2
compatible with the formation of monoidal traces. For G and its Langlands dual group G∨, the
Koszul duality of [BGS, S, BY] localizes to an equivalence of two-periodic Hecke categories
e
Hper
G
≃Hper
G∨
Thus Theorem 1.8 implies a two-periodic equivalence between unipotent character sheaves on Lang-
lands dual groups.
Corollary 1.12. There is a canonical equivalence of two-periodic dg categories of character sheaves
on Langlands dual groups
Chper
G
≃Chper
G∨.
