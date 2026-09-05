---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-001-11-homotopical-algebra-of-hecke-categories
section_title: "Homotopical algebra of Hecke categories"
section_number: 1.1
pages: 3-13
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
in Theorem 1.8, from the perspective of representation theory. W e ﬁrst recall two categories of
D-modules of fundamental interest in representation theory and o f primary focus in this paper.
1.1.1. Hecke categories.
Deﬁnition 1.1. 1) The Hecke category is the dg category
HG =DG(G/B×G/B)≃D (B\G/B)
of all B-biequivariantD-modules on G.
2) The monodromic Hecke category is the full dg subcategory
~HG⊂D G(G/N×G/N)≃D (N\G/N)
generated (under colimits) by pullbacks from HG.
3
Both Hecke categories carry natural monoidal structures given by convolution. Thus they form
algebra objects in the symmetric monoidal ∞-category StC.
1.1.2. Character sheaves. The traditional deﬁnition [Lu] of character sheaf (see also [La] for a review
and [Gi, MV, Gr] for geometric approaches to the theory) is based on the horocycle correspondence
G/adG G/ adB
p/d111/d111 δ /d47/d47B\G/B.
The map p is the natural projection with ﬁbers isomorphic to the ﬂag variety G/B, and the map δ
is the natural projection with ﬁbers isomorphic to B. Pulling back and pushing forward D-modules
gives a functor called the Harish Chandra transform (in the termino logy of [Gi])
F =p∗δ! :HG =D(B\G/B) /d47/d47D(G/adG)
A traditional unipotent character sheaf is a (shift of a) G-equivariantD-module on G that is a
simple constituent of a D-module obtained by applying the transform F to a simple D-module (in
the heart of the standard t-structure on HG). All unipotent character sheaves can be character-
ized geometrically as the simple adjoint-equivariant D-modules on G with singular support in the
nilpotent cone and unipotent central character. Lusztig showed that the collection of all character
sheaves provides a construction of the characters of ﬁnite grou ps of Lie type, and gave a detailed
classiﬁcation in relation with the structure of the ﬁnite Hecke algebr a.
With the above in mind, we make the following deﬁnition in the homotopica l setting.
Deﬁnition 1.2. The dg category Ch G of unipotent character sheaves is deﬁned to be the full sub-
category ofD(G/adG) generated (under colimits) by the image of the Harish Chandr a transform F .
Note that traditional unipotent character sheaves are simple obj ects of the heart of Ch G with
respect to the standard t-structure.
Example 1.3. The above correspondence can be viewed as a collection of Weyl gro up twisted versions
of the Grothendieck-Springer simultaneous resolution. Namely, if w e restrict to the support
pt/B =B\B/B⊂B\G/B
of the monoidal unit of HG, then we recover (an equivariant global version of) the Grothend ieck-
Springer correspondence
G/adG ~G/G
p/d111/d111 δ /d47/d47B\B/B≃pt/B.
Here ~G/G denotes the simultaneous resolution
~G/G ={(g,B ′)|g∈B′}/G≃B/adB,
and the map p forgets the ﬂag B′, while the map δ forgets the group element g.
The global version of the Springer sheaf
SG =F (Opt/B) = p∗δ!Opt/B
is the fundamental example of a character sheaf. (Some might pre fer to shift SG so that it lies
in the heart of the standard t-structure.) According to [HK], it coincides with Harish Chandra’s
adjoint-equivariant holonomic system of diﬀerential equations obt ained by setting all of the Casimir
operators to zero.
1.1.3. Prelude to results: analogy with ﬁnite groups. Our results are perhaps most easily understood
in analogy with the following well-known properties of a ﬁnite group Γ, a nd speciﬁcally its complex
group algebra C[Γ] and category of ﬁnite-dimensional complex modules Rep fd
C (Γ).
1) The group algebra C[Γ] is a ﬁnite-dimensional semi-simple symmetric Frobenius algebra with
nondegenerate functional
τ : C[Γ] /d47/d47 C τ (f ) = f (e)/|Γ|
4
where e∈ Γ is the unit.
2) The class functions C[Γ] Γ are the center of the group algebra
z : C[Γ] Γ /d31 /d127 /d47/d47 C[Γ]
and in particular form a commutative algebra. Equivalently, they are the endomorphisms of the
identity functor of Rep fd
C (Γ), and so act universally on any M∈ Repfd
C (Γ).
3) The class functions C[Γ] Γ are the target of a universal trace map
tr : C[Γ] /d47/d47 /d47/d47 C[Γ] Γ
initial among all maps that are equal on ab,ba ∈ C[Γ], for a,b ∈ C[Γ]. Equivalently, they are
the universal recipient of a functorial trace map from endomorph isms of any M∈ Repfd
C (Γ) which
assigns to the identity the character χM∈ C[Γ] Γ .
The symmetric property of the Frobenius algebra is equivalent to th e fact that the functional τ
is a trace so admits a factorization
τ : C[Γ] tr /d47/d47 C[Γ] Γ /d47/d47 C
It follows that class functions themselves form a commutative Frob enius algebra, with multipli-
cation and functional induced by those of C[Γ] via the center and trace maps.
1.1.4. Results: Hecke categories and character sheaves. To begin, we work with monoidal categories,
by which we mean algebra objects C ∈Alg(StC) in the symmetric monoidal ∞-category of dg
(or stable presentable) categories StC, as categoriﬁed analogues of C-algebras. There are natural
categorical analogues of center and trace
Z(C) = End C⊗C op(C) Tr( C) =C⊗ C⊗C opC
The ﬁrst is naturally braided, i.e., an E2-algebra inStC, by the general form of the Deligne conjecture
(see [L2]) and comes with a universal central map
z : Z(C) /d47/d47C
The second has a natural S1-action, a generalization of the Connes cyclic structure on Hochsc hild
chains, and comes with a universal trace map
tr :C /d47/d47 Tr(C)
We propose the following notion of a semi-rigid monoidal category as a categoriﬁed analogue of
ﬁnite-dimensional semi-simple algebra (see Section 1.3 for further j ustiﬁcation of this analogy).
Deﬁnition 1.4. A monoidal category C is called a semi-rigid category ifC is compactly generated,
and all of its compact objects (or equivalently, a collectio n of compact generators) are both left and
right dualizable.
Remark 1.5. If in addition the unit of C is compact (or equivalently, its compact and dualizable
objects coincide), then C is also rigid in the sense of [G] (note however that [G] does not require C
to be compactly generated). For example, a quasi-compact derive d stack X with aﬃne diagonal is
perfect in the sense of [BFN] when its category Q(X) of quasicoherent sheaves is rigid. We have
introduced the notion of semi-rigid category to accommodate our m ain example, the Hecke category,
whose unit is not compact.
There are natural weak and strong analogues of the notion of sym metric Frobenius algebra for
semi-rigid monoidal categories, namely pivotal and Calabi-Yau struc tures.
Deﬁnition 1.6. A pivotal structure on a semi-rigid monoidal categoryC is a monoidal identiﬁcation
of the operations of taking left and right duals.
5
A pivotal structure equips C with a trace
τ : Tr(C) /d47/d47 Vect
factoring the functional given on compact objects (and all objec ts if 1 C is compact) by the pairing
HomC(1C,−) :C /d47/d47 Vect
We show in Section 3 that a pivotal structure on a semi-rigid categor y induces a canonical identiﬁ-
cation of its monoidal center and trace. Pivotal structures howe ver have the disadvantage that they
are not manifestly Morita invariant notions.
Deﬁnition 1.7. A Calabi-Yau structure on a monoidal category C is a trace map
Tr(C) /d47/d47 Vect
that is S1-invariant and so that the natural composition
C⊗C /d47/d47 Tr(C) /d47/d47 Vect
is the evaluation of a self-duality of C.
The notion of Calabi-Yau category is a Morita invariant notion, howev er we are not aware of a
“classical” monoidal category interpretation of this strong notion of cyclic trace.
With these deﬁnitions in mind, here is an abstract statement of our m ain results, in parallel to
the above highlighted statements for ﬁnite groups.
Theorem 1.8. 1) (Theorems 3.18, 6.2, 6.3) The Hecke categories HG and ~HG are semi-rigid, and
carry canonical pivotal and Calabi-Yau structures.
2) (Theorem 6.9) The dg category Ch G of unipotent character sheaves is canonically equivalent
to the monoidal center and trace of both Hecke categories HG and ~HG.
Remark 1.9. Perhaps the most interesting aspect of the identiﬁcation of Ch G with the monoidal
trace ofHG is the consequence that every dualizable Hecke module M has a character χM∈Ch G.
In other words, character sheaves arise as characters of such Hecke modules. To illustrate this point,
consider a spherical subgroup K⊂G (for example, K a parabolic subgroup, or the ﬁxed points of
an involution). Harish Chandra ( g,K )-modules with trivial inﬁnitesimal character are equivalent to
K-equivariantD-modules on G/B. The latter naturally provide a Hecke module where the Hecke
category acts via convolution on the right. The character of this H ecke module is the object of Ch G
given by pushing forward the structure sheaf of K/adK along the natural projection to G/adG, and
then projecting it onto Ch G. For example, the Springer sheaf SG discussed in Example 1.3 is the
character of the left regular representation of the Hecke categ ory.
Remark 1.10. The identiﬁcations of the theorem endow Ch G with rich algebraic structures. As a
monoidal center, Ch G is naturally an E2-algebra. As a monoidal trace, Ch G comes equipped with
an S1-action. In fact, the S1-action is compatible with the loop rotation action on all D-modules
on the loop space G/adG =L(BG). This is part of the topological ﬁeld theory structure we discuss
in Section 1.3 below.
Remark 1.11. It is interesting to compare the theorem with the independent resu lts of Bezrukavnikov,
Finkelberg and Ostrik [BFO] on the level of abelian categories. Namely , they show that the Drinfeld
center of the abelian category of Harish Chandra bimodules is equiva lent to the abelian category
generated by character sheaves. On the one hand, we do not che ck the compatibility of our con-
structions with t-structures; on the other hand, the derived categories we cons ider are richer than
the derived categories of their hearts.
6
1.1.5. Langlands duality for character sheaves. The Hecke categoriesHG and ~HG are connected by a
Langlands duality, namely the Koszul duality of Beilinson-Ginzburg-S oergel [BGS], in the Langlands
dual form developed by Soergel [S] with monoidal structure estab lished by Bezrukavnikov-Yun [BY].
It is most naturally stated in the mixed setting, but since such struc tures are beyond the scope of this
paper, we will state an equivalence of underlying two-periodic categ ories. Passing to two-periodic
localizations is a symmetric monoidal functor
{−}per :StC /d47/d47StC[u,u−1] C ✤ /d47/d47Cper =C⊗ C C[u,u −1] deg u = 2
compatible with the formation of monoidal traces. For G and its Langlands dual group G∨, the
Koszul duality of [BGS, S, BY] localizes to an equivalence of two-perio dic Hecke categories
~Hper
G ≃H per
G∨
Thus Theorem 1.8 implies a two-periodic equivalence between unipoten t character sheaves on Lang-
lands dual groups.
Corollary 1.12. There is a canonical equivalence of two-periodic dg categor ies of character sheaves
on Langlands dual groups
Ch per
G ≃Ch per
G∨.
1.2. F unctional analysis of D-module categories. The proof of Theorem 1.8 relies on the
formalism of D-module on stacks, as developed in [DrG1, GR], see Section 4. Our ma in interest is
in results relating functors between D-module categories with integral transforms: given varieties
X,Y and a D-moduleK on the product X×Y , one deﬁnes a functor on derived categories of
D-modules
D(X) /d47/d47D(Y ) F ✤ /d47/d47πY ∗(π!
XF⊗K ).
by pulling back from X to the product X×Y , tensoring with the integral kernel K, and then
pushing forward to Y via the natural diagram
X X ×Y
πX/d111/d111 πY /d47/d47Y.
1.2.1. Integral transforms for quasicoherent sheaves. In the context of quasicoherent sheaves, there
is a very tight connection between categorical operations and geo metric operations on the underlying
stacks. In our paper [BFN] with John Francis, we studied the homot opical algebra of categories
of quasicoherent sheaves, and in particular proved a result identif ying functors on quasicoherent
sheaves with integral transforms, generalizing results of Orlov [O ], Bondal, Larsen and Lunts [BLL]
and To¨ en [To]. Namely, we introduced the class of perfect stacks X, which as mentioned above
are characterized (among quasi-compact stacks with aﬃne diagon al) by the property that Q(X) is
compactly generated and rigid. This class includes all (quasi-compac t and separated) schemes as
well as most common stacks in characteristic zero, and is closed und er natural operations such as
ﬁber products. For perfect stacks X1, X2 over a perfect stack Y we showed that the natural maps
are equivalences
Q(X1)⊗Q(Y )Q(X2) ∼ /d47/d47Q(X1×Y X2) ∼ /d47/d47 FunL
Q(Y )(Q(X1),Q(X2)).
In other words,Q(Y )-linear integral transforms between Q(X1) andQ(X2) are identiﬁed both with
allQ(Y )-linear functors and with the relative tensor product of the resp ective categories.
When X = X1 = X2, we also studied the algebra structure of convolution on such “ma-
trix” algebras of quasicoherent sheaves. The dg category of inte gral transforms Q(X×Y X)≃
FunQ(Y )(Q(X),Q(X)) has a natural multiplication, given by convolution, or equivalently b y com-
position of functors, making it into a monoidal dg category. In the c ase Y is a point, this is a
categoriﬁed version of the algebra of matrices with entries labelled b y X, while in general it is a
version of Y -block diagonal matrices. Thus one expects the monoidal center a nd trace of such an
algebra to be a categoriﬁed version of functions on Y . Indeed, we showed that they are identiﬁed
7
with the category Q(LY ) of sheaves on the derived loop space of Y . (In fact Q(X×Y X) is Morita
equivalent toQ(Y ) under mild hypotheses, see [BFN2].)
Example 1.13. If we take X = pt/B to be the classifying stack of the Borel and Y = pt/G, the
center and trace of the quasicoherent Hecke categoryQ(B\G/B) are identiﬁed with all quasicoherent
sheavesQ(G/adG).
1.2.2. Integral transforms for equivariant D-modules. A modiﬁcation of the techniques of [BFN]
provides an analogous description of integral transforms in the D-module setting when the base Y
is a scheme and the projection X1→ Y is a relative Deligne-Mumford stack, or more generally, a
safe morphism in the sense of [DrG1].
Theorem 1.14 (Corollary 5.3) . LetX1→Y denote a Deligne-Mumford stack over a scheme, and
X2→Y an arbitrary stack. Then the natural maps are equivalences
D(X1)⊗D(Y )D(X2) ∼ /d47/d47D(X1×Y X2) ∼ /d47/d47 FunL
D(Y )(D(X1),D(X2))
The identiﬁcation of tensors, integral transforms and functors as above fails badly when the base
is a stack, as in our motivating case Y =BG. The fundamental obstruction is the inherently topo-
logical nature of D-modules. Pushing forward along an aﬃne map almost always loses info rmation
(that is, it fails to be conservative): for example, unlike quasicoher ent sheaves, many nontrivial
D-modules have no global ﬂat sections at all. Thus even for stacks wit h aﬃne diagonal, one can
not reconstruct D-modules on a ﬁber product from algebraic operations on D-modules on the fac-
tors (for stacks with ﬁnite diagonal, for example for schemes, this problem disappears). In short,
the Tannakian theory of D-modules is not rich enough to capture the geometric theory. As a r e-
sult, tensor and functor categories are not identiﬁed with all integ ral kernels: there are adjunctions
exhibiting the former as pale shadows of the latter. For example, th e category D(G) cannot be
reconstructed from D(pt) = Mod C as a module category for D(BG) = C∗(G) -mod where C∗(G) is
the algebra of singular chains on G.
In Section 5.2, we prove the following partial result. We make the ver y strong assumption that
the stack Y is a classifying stack of an aﬃne group, thus ensuring that the tech nical conditions
that Y is smooth with aﬃne diagonal. This setup suﬃces for D(Y ) to be semi-rigid under tensor
product, a condition which typically fails for schemes: compact obje cts in D(Y ) for a scheme are
coherentD-modules, but only ﬂat vector bundles are dualizable. In this restric ted setting, we then
ﬁnd that tensor products and linear functors with source a relativ e Deligne-Mumford stack, or more
generally safe stack, are identiﬁed with each other via the natural map factoring through a full
inclusion into integral transforms.
Theorem 1.15 (Corollary 5.6, Proposition 5.7) . LetX1→Y =BG be a relative Deligne-Mumford
stack over the classifying stack of an aﬃne group, and X2 → Y an arbitrary stack. Then the
natural map from tensors to functors is an equivalence, and f actors through the integral transform
construction
D(X1×Y X2)
Φ
/d41/d41❙❙❙❙❙❙❙❙❙❙❙❙❙❙
D(X1)⊗D(Y )D(X2) ∼ /d47/d47
Ψ
/d53/d53❧❧❧❧❧❧❧❧❧❧❧❧❧❧
FunL
D(Y )(D(X1),D(X2))
Moreover, Φ has a fully faithful left adjoint.
Example 1.16. IfX1 =X2 =pt→Y =BG, so that X×Y X =G, we ﬁnd that the tensor product
and functor categories are identiﬁed with the full subcategory
EndD(BG)(D(pt))≃⟨O G⟩⊂D (G)
generated by the structure sheaf.
8
Using this more subtle understanding of the relation between integr al transforms and functors,
we calculate the center and trace of Hecke categories. Unlike the q uasicoherent case, we do not see
all sheaves onL(BG) = G/adG as the center and trace, but precisely the full subcategory of sh eaves
that can be accessed through the horocycle correspondence, o r in other words, unipotent character
sheaves.
1.3. T opological ﬁeld theory. Our results naturally ﬁt into and were motivated by the structure
of topological ﬁeld theory (TFT). We will not give a formal introduct ion to TFT but rather remind
the reader of its broad outline informally and illustrate it via the examp le of ﬁnite group gauge
theory. We refer to [L3] for a detailed overview of the ∞-categorical setting for TFT (including
the∞-version of n-categories) and the Cobordism Hypothesis. We only use the ( ∞, 2)-categorical
language for motivation and it does not recur elsewhere in the paper .
1.3.1. 2-dimensional TFT. An extended framed 2-dimensional TFT is a symmetric monoidal func -
tor out of the symmetric monoidal (∞, 2)-category 2Bordf r of 2-dimensional framed bordisms (with
monoidal structure given by disjoint union):
• objects: (2-dimensionally framed) 0-manifolds,
• 1-morphisms: (2-dimensionally framed) 1-dimensional bordisms bet ween 0-manifolds,
• 2-morphisms: classifying spaces of (framed) 2-dimensional bordis ms between 1-bordisms.
In other words, all n-morphisms for n > 2 are invertible, and together form (the fundamental
∞-groupoid of) classifying spaces of framed bordisms.
One can similarly deﬁne the oriented bordism l ( ∞, 2)-category 2Bord, in which one extends
from framed manifolds to all oriented manifolds and their bordisms.
In general, if the target is a plain discrete 2-category, then one ob tains an ordinary functor out
of the 2-category with the same objects and 1-morphisms but 2-m orphisms given by 2-dimenisonal
bordisms up to diﬀeromorphism. This setting is studied in detail in [Sch].
In [L3], Lurie outlines the proof of a general ∞-categorical version of the Cobordism Hypothesis
formulated by Baez-Dolan [BDo]. The 2-dimensional case which we use was inspired by work of
Costello [C] and Kontsevich-Soibelman [KS] on open-closed ﬁeld theor y. The Cobordism Hypothesis
speciﬁes increasingly strong ﬁniteness conditions, known as d-dualizability, that allow an object of
a symmetric monoidal ( ∞,d )-category to be “integrated” over framed manifolds of dimension at
most d, thus deﬁning an extended d-dimensional TFT. Moreover, the space of d-dualizable objects
carries an action of O(d), and objects on which the action of SO(d) has been trivialized give rise to
ﬁeld theories deﬁned on all oriented manifolds of dimension at most d.
1.3.2. Toy model: ﬁnite group gauge theory. To place our results in the framework of TFT, it is
illuminating to return to the toy model of a ﬁnite group Γ. There is an o riented 2-dimensional TFT
ZΓ called Dijkgraaf-Witten theory [DW] which eﬃciently encodes all of th e familiar structures in
the complex representation theory of Γ discussed earlier. (One co uld consult [Sch] for details in all
of the discussion to follow, in particular for the construction of 2-d imensional oriented TFTs from
symmetric Frobenius algebras. See also [F] for a detailed study of ZΓ , and [FHLT] for a discussion
of ZΓ in the setting of the Cobordism Hypothesis.)
The target of ZΓ is the Morita 2-category of algebras AlgC with the following structure:
• objects: associative algebras over C,
• 1-morphisms: bimodules (ﬂat over the source),
• 2-morphisms: morphisms of bimodules.
The symmetric monoidal structure of AlgC is given by tensor product of algebras with unit C. By
assigning to an algebra A its category Perf A of perfect modules (summands of ﬁnite colimits of
free modules), we can identify the Morita 2-category AlgC with a full subcategory of the 2-category
AbCat C of small C-linear abelian categories, exact functors and natural transfor mations.
9
The ﬁeld theory ZΓ assigns to each cobordism M a linearization of the space of Γ-gauge ﬁelds on
M , or in other words, the orbifold of principal Γ-bundles or Galois Γ-co vers over M . In particular,
it assigns the following to closed 0, 1 and 2-manifolds:
• To a point, ZΓ assigns the group algebra:
ZΓ (pt) = C[Γ]∈AlgC.
Alternatively, we can pass to the category of ﬁnite-dimensional co mplex modules:
ZΓ (pt) = Rep fd
C (Γ)∈AbCat C.
This is the category of ﬁnite-dimensional algebraic vector bundles o n the orbifold of Γ-
bundles on a point.
• To a circle, ZΓ assigns class functions:
ZΓ (S1) = C[Γ] Γ = C[Γ/ad Γ]∈ Vectfd
C = 1 HomAbCat C(Vectfd
C, Vectfd
C ),
This is the vector space of functions on the orbifold of Γ-bundles on the circle.
• To a closed surface, ZΓ counts Γ-bundles:
ZΓ (Σ) = #{Hom(π1(Σ), Γ)/Γ}∈ C = 2 HomAbCat C(C, C)
where as usual a bundle P is weighted by 1 / Aut(P). This is the volume of the orbifold of
Γ-bundles on the surface.
From the point of view of the Cobordism Hypothesis, we only have to s pecify that we assign the
group algebra C[Γ] to a point to determine the rest of the TFT structure. Any obje ct of AlgC is
1-dualizable, with dual given by the opposite algebra. The requireme nt of 2-dualizability however
is extremely restrictive: as proven in [Sch], 2-dualizable objects of AlgC are precisely separable
algebras, i.e., algebras for which A is projective as an A-bimodule. Over C, separable algebras are
precisely ﬁnite-dimensional semi-simple algebras. Invariance under SO(2) amounts to the data of a
non-degenerate trace, or in other words, the structure of a sy mmetric Frobenius algebra.
1.3.3. TFTs from semi-rigid categories. Our main results can be viewed as the construction and
partial description of an oriented 2-dimensional TFT valued in a cate goriﬁed analogue of the Morita
2-categoryAlgC. Namely, we replace C-algebras by C-linear monoidal categories, or more precisely,
algebra objects in the symmetric monoidal ∞-category StC. We denote by Alg(1)(StC) the Morita
(∞, 2)-category with objects algebras in StC, 1-morphisms bimodule categories and 2-morphisms
the spaces of intertwiners between bimodule categories. (See [L3] for a more precise description; we
reiterate that we only use the ( ∞, 2)-language for informal motivation).
As withAlgC, any object of Alg(1)(StC) is 1-dualizable, with dual given by the monoidal opposite.
The much stronger condition of 2-dualizability of A∈Alg(1)(StC) breaks down into two parts. First,
the underlying category of A must be dualizable as a plain category. In practice, this is an easily
satisﬁed condition, guaranteed for example by the compact gener ation of A, in which case the dual
is a modiﬁcation of the opposite category of A. Second, one needs A to be dualizable as an A-
bimodule, a natural analogue of separability. Dualizability as a bimodule is closely related to the
abundance of monoidal duals of objects of A:
Theorem 1.17 (Theorem 3.18) . Any semi-rigid category A∈Alg(1)(StC) is 2-dualizable.
It follows that any semi-rigid monoidal category A∈ Alg(1)(StC), in particular the Hecke cate-
goriesHG and ~HG, deﬁnes a framed 2-dimensional TFT ZA valued in Alg(1)(StC) which makes the
following assignments:
• To a point, ZA assigns A∈Alg(1)(StC).
• To a circle with cylinder framing,ZA assigns the trace Tr(A)∈StC with its cyclic S1-action.
• To the circle with annulus framing, ZA assigns the center Z(A)∈StC with itsE2-structure.
• To a framed surface, ZA assigns an object of Vect C.
10
1.3.4. Oriented TFTs from Calabi-Yau monoidal categories. To extend the TFT ZA from framed
to oriented manifolds, the Cobordism Hypothesis requires A∈Alg(1)(StC) be a ﬁxed point for the
SO(2)-action on 2-dualizable objects.
Part of this action can be described very explicitly: following [L3, Prop osition 4.2.3], a 2-
dualizable object A∈Alg(1)(StC) admits a Serre automorphism SA characterized by
evR
A = (SA⊗ idAop)◦coevA
It can be interpreted as the monodromy of A around the SO(2)-action, or in other words, the ﬁrst
obstruction to SO(2)-invariance of A. Thus a trivialization of SA as an automorphism makes A a
ﬁxed point of the action of the free group (James construction) o n the circle Ω S2 = ΩΣ SO(2). This
suﬃces to identify the values of ZA on diﬀerent framed circles, for example the monoidal center and
trace of A.
Following [L3, Section 4.2], the stronger condition of SO(2)-invariance of A can be encoded by
the notion of Calabi-Yau monoidal category (as recalled in Deﬁnition 1 .7 above).
Corollary 1.18 (Theorem 3.18) . A Calabi-Yau (respectively, pivotal) structure on a semi-r igid
categoryA∈ Alg(1)(StC) deﬁnes an oriented (respectively, a weakly oriented) 2-dim ensional TFT
so that ZA(S1) is identiﬁed with both the monoidal center and trace of A.
Example 1.19 (Fusion categories and 3-dimensional Dijkgraaf-Witten theor y). For a ﬁnite group Γ,
the categories Vectfd
C (Γ) of ﬁnite-dimensional vector bundles on Γ and Rep fd
C (Γ) of ﬁnite-dimensional
complex representations of Γ are key examples of fusion categorie s, monoidal categories satisfying
strong ﬁniteness conditions. In fact, it is proved in [DSS] that fusio n categories are 3-dualizable
objects of a natural 3-category of monoidal categories, bimodu le categories, intertwines and nat-
ural transformations. (They also show that pivotal structures give Ω S2-ﬁxed structures on these
theories.) The monoidal categories Vect fd
C (Γ) and Rep fd
C (Γ) are Morita equivalent and so deﬁne
the same 3-dimensional TFT, an untwisted version of 3-dimensional Dijkgraaf-Witten theory [DW]
and a natural categoriﬁcation of the ﬁnite group gauge theory dis cussed earlier. Since Rep fd
C (Γ) is
symmetric monoidal, it is easy to evaluate this TFT on any manifold. For example, to a surface Σ,
one attaches the vector space of functions on the orbifold of Γ-p rincipal bundles over Σ, while to a
3-manifold M , one attaches the volume of the orbifold of Γ-principal bundles ove rM .
Example 1.20 (Quasicoherent 3-dimensional theories). For a perfect stackX, the symmetric monoidal
categoryQ(X) of quasicoherent sheaves is rigid and pivotal. For example, for G a reductive group,
its classifying stack BG is perfect, and the category Q(BG) comprises algebraic representations
of G.
One can calculate the resulting categoriﬁed 2-dimensional TFT explic itly by the theory of topo-
logical chiral homology [L2, Section 5.3], or from the direct construc tions of [BFN]. In particular,
it makes the following assignments, stated in general, then spelled ou t when X =BG:
• Z qc
X (pt) =Q(X) = Rep(G), algebraic representations.
• Z qc
X (S1) =Q(LX) =Q(G/adG), adjoint-equivariant quasicoherent sheaves.
• Z qc
X (Σ) = O(X Σ ) = RΓ(CharG(Σ),O), functions on the character variety.
As explained in [BFN2], the rigid categoryQ(BG) is in fact Morita equivalent to the quasicoherent
group algebraQ(G), and any intermediate Hecke categoryQ(H\G/H), forH⊂G, so that all deﬁne
equivalent TFTs.
Furthermore,Q(X) is naturally a Calabi-Yau monoidal category, and hence Z qc
X extends to an
oriented TFT. However, unlike the case of fusion categories, Q(X) is not typically 3-dualizable,
and hence Z qc
X does not typically extend to 3-manifolds. Nonetheless, it is natural to think of our
constructions as intrinsically 3-dimensional as they correspond to supersymmetric 3-dimensional
quantum gauge theories in physics.
1.3.5. Character Theory. Finally, let us turn to TFTs built out of D-modules on the complex re-
ductive group G. In analogy with the above results for quasicoherent sheaves, on e might expect
11
to construct a single TFT starting from a Morita equivalent class of a lgebras including the “com-
mutative algebra” D(BG), the “smooth group algebra” D(G), or any intermediate Hecke algebra
D(H\G/H), for H⊂G. Furthermore, one might expect this TFT to attach to the circle th e cate-
goryD(G/G) of adjoint-equivariantD-modules on G, and to a surface Σ the de Rham cohomology
Γ(CharG(Σ), Ω •) of the character variety.
This expectation turns out to be wrong on several counts, start ing with the failure of Morita
equivalence. The symmetric monoidal category D(BG) is indeed 2-dualizable, however it is too
small to see the rich geometry of G/adG, as discussed in Section 1.2.2 above. It only sees the
homotopy type of G, and in particular assigns to the circle the category of adjoint-equ ivariant
unipotent local systems on G. At the other extreme, the monoidal category D(G)∈ Alg(StC) is
not 2-dualizable, so does not deﬁne a 2-dimensional TFT, though its center is indeed D(G/G).
There is a sweet spot in between these two extremes given by Hecke categories. The main results
of this paper allow for the following deﬁnition and calculate the resultin g TFTs on a circle.
Deﬁnition 1.21. The equivariant character theory χG of a reductive group G is the oriented 2d
TFT valued in Alg(1)(StC) deﬁned by the Hecke category HG. Likewise, the monodromic character
theory ~χG is the oriented 2d TFT valued in Alg(1)(StC) deﬁned by ~HG.
It follows from the Koszul duality of [S, S, BY] that there is a Langlan ds duality for the two-
periodic versions of the above TFTs.
Corollary 1.22. The invariants assigned by ~χper
G and χper
G∨ to any oriented manifold are identiﬁed.
In particular, unipotent character sheaves with their TFT struct ures are identiﬁed by Langlands
duality. In another direction, boundary conditions for the charac ter theory are given by module
categories for the corresponding Hecke categories, for example , by categories D(K\G/B) of Harish
Chandra ( g,K )-modules. The Langlands duality of boundary conditions in particula r encodes
Soergel’s conjecture [S] on a categorical Langlands classiﬁcation f or real groups. In another direction,
it would be highly interesting to describe the vector spaces χG(Σ) that the character theory attaches
to a surface Σ. It is natural to conjecture a relation with the de Rh am cohomology of character
varieties, and hence with the fascinating conjectures of Hausel, L etellier and Rodriguez-Villegas
[HR V, HLR V, H]. Such a relation would imply a Langlands duality for the co homology of character
varieties, one of our original motivations and a subject of ongoing w ork with Sam Gunningham.
1.4. F urther discussion. We conclude the introduction with a brief discussion of twisted versio ns
of our results and relations with supersymmetric gauge theory.
1.4.1. TwistedD-modules and families version. The results of this paper have natural analogues in
whichD-modules on ﬂag varieties are replaced by twisted D-modules. The requisite arguments are
formally identical, but we will only brieﬂy summarize the picture here. W e expect a more detailed
account to appear in forthcoming work with Sam Gunningham.
The monodromic Hecke category ~HG ﬁts into a family of twisted monodromic Hecke categories
~HG,λ, indexed by characters λ∈ h∨. Likewise, the dg category Ch G of unipotent character sheaves
ﬁts into a family of dg categories Ch G,[λ] of character sheaves with central character [ λ]∈H ∨/W .
Expectation 1.23. Fix any λ∈ h∨, with image [λ]∈H ∨/W .
1) The twisted monodromic Hecke category ~HG,λ is a semi-rigid Calabi-Yau monoidal category.
2) The monoidal center and trace of ~HG,λ are both identiﬁed with character sheaves Ch G,[λ] with
central character [λ]∈H ∨/W .
The Koszul duality of Hecke categories extends in an interesting wa y to other characters λ∈ h∨.
On the monodromic side, one has the twisted monodromic Hecke cate gory ~HG,λ. On the equivariant
side, one introduces the centralizer G∨
λ⊂G∨ of a semi-simple representative of λ, a Borel subgroup
B∨
λ⊂G∨
λ , and the equivariant Hecke category HG∨
λ
=D(B∨
λ\G∨
λ/B∨
λ ). The results of [BGS, S, BY]
give an equivalence of monoidal categories
~Hper
G,λ≃H per
G∨
λ
12
Now if the above expectation is realized, then one can introduce a tw isted 2-dimensional character
theory ~χG,λ. It will satisfy a Langlands duality
~χper
G,λ≃χper
G∨
λ
and in particular, its value on the circle will provide an equivalence
Ch per
G,[λ]≃Ch per
G∨
λ
.
relating character sheaves on G with central character [ λ] and unipotent character sheaves on the
centralizerG∨
λ in the dual group.
Remark 1.24. At ﬁrst encounter, the idea (derived from Koszul duality) to cons ider the Hecke
categoriesHG∨
λ
as a family might seem bizarre. However, in [BN3] we establish (using th e techniques
developed in [BN2]) that the family of Hecke categories HG∨
λ
arises naturally by S1-equivariant
localization from an evident family of aﬃne Hecke categories. One can then see its Koszul duality
with ~HG,λ as a shadow of the Langlands duality for aﬃne Hecke categories due to Bezrukavnikov [Be].
1.4.2. Relation with gauge theory and geometric Langlands. The character theory has an expected
physical interpretation due to Witten [W, Section 3.3], roughly coming from a topological twist
of a certain maximally supersymmetric three-dimensional gauge the ory. This relation is a dimen-
sional reduction of the groundbreaking interpretation of the geo metric Langlands correspondence
as Montonen-Olive S-duality for maximally supersymmetric four-dime nsional gauge theory due to
Kapustin and Witten [KW]. In particular, the Langlands duality for cha racter theories should arise
as a dimensionally reduced version of the geometric Langlands corre spondence. Namely, Witten
considers 4-dimensionalN = 4 super-Yang-Mills in the “geometric Langlands” topological twist a s
studied in [KW] (for any value of the twist and coupling parameter) re duced on 4-manifolds of
the form M 3×S1. The supercharge in this theory has a perturbation which squares to rotation
along the S1-factor (this is closely related to the “Ω-background” in the form s tudied in [NW], or
to the appearance of D-modules from cyclic homology discovered in [BN1]). This supercharge still
deﬁnes a diﬀerential when restricted to S1-invariant modes, and can be used to deﬁne a Z/2-graded
3-dimensional TFT (independent of parameters), which is the phys ical construction of the character
theory. The parameter λ∈ h∨ has the physical interpretation as a vacuum expectation value (ve v)
of a scalar ﬁeld, so that h∨/W appears as the moduli of vacua of the theory (much as the Hitchin
base appears as the moduli of vacua or Seiberg-Witten base for su persymmetric gauge theories in
four dimensions), with the unipotent version studied here arising at the conformal point.
