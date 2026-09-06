---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-004-2-overview
section_title: "Overview"
section_number: 2
pages: 7-16
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
2.1. T races in category theory. We highlight structures arising in the general theory of
dualizable objects in symmetric monoidal higher categories (see also [DP, M, PS]). For legibility,
we suppress all ∞-categorical notations and complications from the introduction. W e rely
on [GR2] for the theory of symmetric monoidal (∞, 2)-categories, though only the formal outline
of the theory is in fact needed for this paper. See [TV, HSS] for th orough treatments of the
theory of traces in higher category theory.
The basic notion in the theory is that of dimension of a dualizable object of a symmetric
monoidal categoryA. By deﬁnition, for such an object A there exists another A∨ together with
a coevaluation map ηA and evaluation map ǫA satisfying standard identities. By deﬁnition, the
dimension of A is the endomorphism of the the unit 1 A given by the composition
1A
ηA /d47/d47
dim(A)
/d55/d55A⊗A∨ ǫA /d47/d47 1A
Example 2.1. For V a vector space, V ∨ = Hom k(V,k ) is the vector space of functionals,
ǫV : V⊗V ∨→ k is the usual evaluation of functionals, ηV : k→ End(V )≃ V⊗V ∨ is the
identity map (which exists only for V ﬁnite-dimensional), and dim( V ) can be regarded as an
element of the ground ﬁeld (by evaluating it on the multiplicative unit).
Remark 2.2 (Duality and naiv¨ et´ e in∞-categories.). It is a useful technical observation that
the notion of dualizability in the setting of ∞-categories is a “naive” one: it is a property of
an object that can be checked in the underlying homotopy categor y. As a result, all of the
categorical and 2-categorical calculations in this paper are similarly naive and explicit (and
analogous to familiar unenriched categorical assertions), involving only small amounts of data
that can be checked by hand.
The notion of dimension is a special case of the trace of an endomorphism Φ of a dualizable
object A. By deﬁnition, the trace of Φ is the endomorphism of the unit 1 A given by the
composition
1A
ηA /d47/d47
Tr(Φ)
/d54/d54A⊗A∨ Φ ⊗idA∨
/d47/d47A⊗A∨ ǫA /d47/d47 1A
which recovers the dimension for Φ = id A.
A key feature of dimensions and traces is their cyclicity, which at the coarsest level is ex-
pressed by a canonical equivalence
m(Φ, Ψ) : Tr(Φ ◦ Ψ) ∼ /d47/d47 Tr(Ψ◦ Φ),
see Proposition 3.15. At a much deeper level, an important corollary o f the cobordism hy-
pothesis [L3] is the existence of an S1-action on dim( A) for any dualizable object A (and an
analogous structure for general traces, see Remark 3.28).
Remark 2.3 (Dimensions and traces are local) . It is useful for applications to note that the
notion of dualizability and the deﬁnition of dimension and are local in the categoryA. Namely,
they only require knowledge of the objects 1 A,A,A ∨,A ⊗ A∨, the morphisms ηA,ǫA, and
8 DA VID BEN-ZVI AND DA VID NADLER
standard tensor product and composition identities among them. L ikewise, the notion of trace
only requires the additional endomorphism Φ along with a handful of a dditional identities.
2.1.1. Functoriality of traces. Now suppose the ambient symmetric monoidal category A un-
derlies a 2-category, so there is the possibility of noninvertible 2-mo rphisms. This allows for
the notion of left and right adjoints to morphisms. Let us say a morp hism A→ B is contin-
uous, or right dualizable , if it has a right adjoint. (The terminology derives from the setting
of presentable categories, where the adjoint functor theorem g uarantees the existence of right
adjoints for colimit preserving functors.)
Here are natural functoriality properties of dimensions and trace s.
Proposition 2.4. Let A,B denote dualizable objects of A and f∗ : A → B a continuous
morphism with right adjoint f !.
(1) There is a canonical map on dimensions
dim(A)
dim(f∗)
/d51/d51
= /d47/d47 Tr(IdA) /d47/d47 Tr(f !f∗) ∼ /d47/d47 Tr(f∗f !) /d47/d47 Tr(IdB) = /d47/d47 dim(B)
compatible with compositions of continuous morphisms.
(2) Given endomorphisms Φ∈ End(A), Ψ ∈ End(B), and a commuting structure
α :f∗◦ Φ ∼ /d47/d47 Ψ◦f∗
there is a canonical map on traces
Tr(f∗,α ) : Tr(Φ) /d47/d47 Tr(Ψ)
compatible with compositions of continuous morphisms with commuting structures.
We refer to the compatibility with compositions stated in the proposit ion as abstract Grothendieck-
Riemann-Roch. To see its import more concretely, let us restrict the generality an d focus on
an object of A in the sense of a morphism V : 1 A→A.
Corollary 2.5. LetA,B denote dualizable objects ofA andf∗ :A→B a continuous morphism.
ForV : 1 A→A an object of A, we obtain a map on dimensions
dim(V ) : 1 A≃ dim(1A) /d47/d47 dim(A)
called the character of V and alternatively denoted by [V ]. It satisﬁes abstract Grothendieck-
Riemann-Roch in the sense that the following diagram commut es
1A
[V ] /d47/d47
[f∗V ]
/d54/d54dim(A)
dim(f∗) /d47/d47 dim(B)
Remark 2.6 (Functoriality of dimensions and traces is local) . As in Remark 2.3, it is useful to
note that the functoriality of dimension is local, depending only on a ha ndful of objects, mor-
phisms and identities, along with the additional adjunction data ( f∗,f !). A similar observation
applies to the functoriality of traces.
Remark 2.7. It follows from the cobordism hypothesis with singularities [L3] (see [T V]) that
the morphism dim( f∗) is S1-equivariant, and hence the character [ V ] is S1-invariant, though
we will not elaborate on this structure here. We refer to [HSS] for a thorough study of the
functoriality and cyclicity of traces.
NONLINEAR TRACES 9
Example 2.8. LetdgCatk denote the symmetric monoidal ∞-category of presentable k-linear
diﬀerential graded categories (or alternatively, stable presenta ble k-linear∞-categories), see
e.g. [GR2]. In this setting, any compactly generated category A is dualizable, and its dimension
is the Hochschild chain complex dim( A) = HH ∗(A). The S1-action on dim(A) corresponds to
Connes’ cyclic structure onHH ∗(A), so that in particular, the localized S1-invariants of dim(A)
form the periodic cyclic homology of A.
More generally, the trace of an endofunctor Φ : A→A is the Hochschild homology Tr(Φ) =
HH ∗(A, Φ). For example, if A = R-mod for a dg algebra R, then Φ is represented by an
R-bimodule M , and we recover the Hochschild homology HH ∗(R,M ).
Any compact object M∈A deﬁnes a continuous functor
1dgCat k =dgVect k
M /d47/d47A
whose character is a vector
dim(M )∈HH ∗(A)
in Hochschild homology (with reﬁnement in cyclic homology). The abstr act Grothendieck-
Riemann-Roch theorem expresses the natural functoriality of ch aracters in Hochschild homology
(or their reﬁnement in cyclic homology). In fact, the construction of characters factors through
the canonical Dennis trace map
Acpt /d47/d47K(A) /d47/d47HH ∗(A)
from the space Acpt of compact objects of A.
2.2. T races in geometry . To apply the preceding formalism to geometry, it is useful to orga-
nize spaces and maps within a suitable categorical framework. We th en arrive at loop spaces
and ﬁxed point loci as nonlinear expressions of dimensions and trace s. This simple observa-
tion provides the core of the paper. Throughout the discussion, w e continue to suppress all
∞-categorical notations and complications. Our reference for the correspondence 2-category of
stacks is Section V of [GR2] (see also [H1]).
To begin, consider the general setup of the symmetric monoidal ca tegory Corr (C) of cor-
respondences, or spans, in a category C such as stacks (or formally a symmetric monoidal
∞-category with ﬁnite limits; see [Ba, H1]). Here the objects X∈Corr (C) are the objects of
C, the morphisms Corr C (X,Y ) are arbitrary spans in C,
Z
/d126/d126⑦⑦⑦⑦⑦⑦⑦
/d31/d31❅❅❅❅❅❅❅
X Y
(more generally one can require the left and right legs to live in speciﬁe d subcategories of C as
in [GR2]). The composition of morphisms Z∈Corr C (X,Y ) and W∈Corr C (Y,U ) is given by
ﬁber product
Z×Y W
/d122/d122✈✈✈✈✈✈✈✈✈
/d36/d36■■■■■■■■■
Z
/d126/d126⑦⑦⑦⑦⑦⑦⑦
/d36/d36■■■■■■■■■■ W
/d122/d122✉✉✉✉✉✉✉✉✉✉
/d32/d32❆❆❆❆❆❆❆❆
X Y U
10 DA VID BEN-ZVI AND DA VID NADLER
and the symmetric monoidal structure is given in terms of that on C (Cartesian product in the
case of stacks). For the purpose of calculating dimensions and tra ces, we need not require any
further properties of the spaces of Corr (C), since we need only the modest local data discussed
in Remarks 2.3 and 2.6. (See [L3] and [FHLT], where the higher categor ies Famn of iterated
correspondences of manifolds are constructed and applied.)
With applications in mind, we will specialize to the correspondence cate gory Corrk =
Corr (Stk) of derived stacks over k. It would also be interesting to work with smooth manifolds
instead, for example through the theory of C∞-stacks [J] (see Remark 2.20).
It is natural to enhance Corr (C) to a 2-category Corr (C) by allowing non-invertible maps, or
more generally correspondences, between correspondences (s ee Section V of [GR2] or [H1] for full
details), so that maps from X toY form the category of objects over X×Y . Our constructions
naturally ﬁt into the 2-category Corrprop
k with non-invertible 2-morphisms restricted to be
proper (or more generally ind-proper) maps of correspondences.
Remark 2.9 (Correspondences are bimodules) . It is useful to view the correspondence category
Corr within the framework of coalgebras in symmetric monoidal categorie s. The diagonal map
X→X×X makes any space or stack into a cocommutative coalgebra object w ith respect to
the Cartesian product monoidal structure (or commutative coalg ebra in the opposite category).
Moreover, a map Z→X is equivalent to an X-comodule structure on Z. Thus correspondences
from X to Y may be interpreted as X−Y -bicomodules, with composition of correspondences
given by tensor product of bicomodules.
Furthermore, it is natural to enhance Corr to a 2-category by allowing non-invertible maps
between correspondences. This can be viewed as a special case of the Morita category of
coalgebras in a symmetric monoidal category. The 2-category Corr of spaces, correspondences,
and maps of correspondences is the Morita category on spaces re garded as coalgebra objects.
(In particular, the cocommutativity of the coalgebra objects implie s they are canonically self-
dual, and the transpose of a correspondence is the same corresp ondence read backwards.) If we
further keep track of theEn-coalgebra structure of spaces and consider the corresponding Morita
(n+1)-category, we recover the (n+1)-category of iterated correspondences of correspondenc es.
(See [H1, H2] for a thorough treatment of categories of spans an d Morita categories of En
algebras; see also for example the category Famn of [L3] and [FHLT] in the topological setting.)
2.2.1. Geometric dimensions and loop spaces. A crucial feature of the category Corrk is that
any object X ∈ Corrk is dualizable (in fact, canonically self-dual), thanks to the diagonal
correspondence.3 Note for this it is crucial that we allow all maps, including the map πX :X→
pt for any X, as possible legs in a span.
We have the following calculations of dimensions and their functoriality . Note that the point
pt = Speck is the unit of Corrk. We keep track of properness of maps of correspondences for
the later application of sheaf theory.
Proposition 2.10. Let Corrk be the category of derived stacks and correspondences, and
Corrprop
k the 2-category of derived stacks, correspondences, and pro per maps of correspondences.
(1) Any derived stack X is dualizable as an object of Corrk, and its dimension dim(X) is
identiﬁed with the loop space
LX =XS1
≃X×X×XX
regarded as a self-correspondence of pt = Speck.
3Likewise, if we wish to make a space n-dualizable for any n we may simply consider it as an object of
a higher correspondence category as in Remark 2.9, since En-(co)algebras are n + 1-dualizable objects of the
corresponding Morita category. In other words, a space X deﬁnes a topological ﬁeld theory of any dimension
valued in the appropriate correspondence category.
NONLINEAR TRACES 11
(2) A map f :X→Y regarded as a correspondence from X to Y is continuous in Corrprop
k
if and only if f is proper. Given a proper map f :X→Y , its induced map
dim(f ) : dim(X) /d47/d47 dim(Y )
is identiﬁed with the loop map
Lf :LX /d47/d47LY
Remark 2.11. All of the objects and maps of the proposition have natural S1-actions, on the
one hand coming from loop rotation, on the other hand coming from t he cyclic symmetry of
dimensions. One can check that the identiﬁcations of the propositio n are S1-equivariant (see
Remark 4.2).
Remark 2.12. Recall [To2, BN10b] that for a derived scheme X, the loop space LX≃TX[−1]
is the total space of the shifted tangent complex. The action map o f the S1-rotation action is
encoded by the de Rham diﬀerential. For an underived stack X, the loop space is a derived
enhancement of the inertia stack IX ={x∈X,γ ∈Aut(x)}. The action map of the S1-rotation
action is manifested by the “universal automorphism” of any sheaf onLX.
Example 2.13. Let G denote an algebraic group and BG =pt/G its classifying space. There
is a canonical identiﬁcation LBG≃G/G of the loop space and adjoint quotient.
Suppose we are given a G-derived stack X, or equivalently a morphism π : X/G→ BG,
from which one recovers X≃X/G×BGpt. (Note that if we want π proper we should take X
itself proper.)
Let us explain how the loop map Lπ :L(X/G)→L (BG) captures the ﬁxed points of G
acting on X. For any self-map g : X→ X, let us write Xg for the derived ﬁxed point locus
given by the derived intersection
Xg = Γg×X×XX.
of the graph Γ g⊂X×X with the diagonal. Then Lπ map ﬁts into a commutative square
L(X/G)
∼
/d15/d15
Lπ /d47/d47L(BG)
∼
/d15/d15
{g∈G,x∈Xg}/G
p /d47/d47G/G
where p projects to the group element.
In particular, ﬁx a group element g ∈ G, with conjugacy class Og ⊂ G, and centralizer
ZG(g)⊂ G, so that Og/G≃ BZG(g)∈ G/G. Then the corresponding ﬁber of Lπ is the
equivariant ﬁxed point locus Xg
G =Xg/ZG(g), or in other words we have a ﬁber diagram
Xg
G
/d15/d15
/d47/d47 Og/G
/d15/d15
L(X/G) Lπ /d47/d47L(BG)
Let us specialize to the case of a subgroup K⊂G, and the quotient X =G/K, so that we
have a map of classifying stacks π : BK≃ G\(G/K)→ BG. Here the loop map Lπ realizes
12 DA VID BEN-ZVI AND DA VID NADLER
the familiar geometry of the Frobenius character formula
L(BK )
∼
/d15/d15
Lπ /d47/d47L(BG)
∼
/d15/d15
K/K≃{g∈G,x∈ (G/K)g}/G
p /d47/d47G/G
The equivariant ﬁxed point loci express the equivariant inclusion of c onjugacy classes.
Specializing further, for G a reductive group, B⊂ G a Borel subgroup, and X = G/B the
ﬂag variety, we recover the group-theoretic Grothendieck-Spr inger resolution
L(BB)
∼
/d15/d15
Lπ /d47/d47L(BG)
∼
/d15/d15
B/B≃{g∈G,x∈ (G/B)g}/G
p /d47/d47G/G
2.2.2. Geometric traces of correspondences. More generally, we have the following calculations
of traces and their functoriality.
Proposition 2.14. Let Corrk be the category of derived stacks and correspondences, and
Corrprop
k the 2-category of derived stacks, correspondences, and pro per maps of correspondences.
(1) The trace of a self-correspondence Z ∈ Corrprop
k (X,X ) is its ﬁber product with the
diagonal
Tr(Z)≃Z|∆ =Z×X×XX≃Z×XLX
In particular, for the graph Γf→X×X of a self-map f :X→X, its trace is the ﬁxed point
locus of the map
Tr(Γg)≃Xf = Γf×X×XX
(2) Given a proper map f : X→ Y regarded as a correspondence from X to Y , and self-
correspondencesZ∈Corrprop
k (X,X ) and W∈Corrprop
k (Y,Y ), together with an identiﬁcation
α :Z ∼ /d47/d47X×Y W
of correspondences from X to Y , the induced abstract trace map
Tr(f,α ) : Tr(Z) /d47/d47 Tr(W )
is equivalent to the induced geometric map
τ (f,α ) : Z|∆ X
/d47/d47W|∆ Y
2.3. T race formulas via sheaf theories. Given any suﬃciently functorial method of mea-
suring derived stacks, the preceding calculations of geometric dime nsions, traces and their
functoriality immediately lead to trace and character formulas. To f ormalize the functorial-
ity needed, we will use the language of sheaf theories. Broadly spea king, a sheaf theory is a
representation (symmetric monoidal functor out) of a correspo ndence category in the way a
topological ﬁeld theory is a representation of a cobordism categor y.4 It provides an approach
to encoding the standard operations on coherent sheaves and D-modules, developed by Gaits-
gory and Rozenblyum in the book [GR2] (following a suggestion of Lurie and previous versions
in [FG, G1, DG, GR1]).
4Indeed a typical mechanism to construct “Lagrangian” ﬁeld t heories is as the composition of a sheaf theory
with a “classical ﬁeld theory” as in [FHLT, H1], a symmetric m onoidal functor from a cobordism category to a
correspondence category.
NONLINEAR TRACES 13
We will take the target of our sheaf theories to be the linear setting of the symmetric monoidal
(∞, 2)-category dgCatk of presentable k-linear diﬀerential graded categories with continuous
functors and natural transformations. (Recall from Setting 1.1 that for applications all stacks
are assumed to be QCA or ind-inf-schemes. Also all proper maps can be replaced by ind-proper
ones at no cost.)
Deﬁnition 2.15. A sheaf theory is a symmetric monoidal functor of ( ∞, 2)-categories
S :Corrprop
k /d47/d47dgCatk
from correspondences of stacks (with 2-morphisms given by prop er maps of correspondences)
to dg categories. We denote by
S :Corrk /d47/d47dgCatk
the underlying 1-categorical sheaf theory, i.e. the symmetric mon oidal functor on ( ∞, 1)-
categories obtained by forgetting noninvertible morphisms.
Let us ﬁrst spell out some of the structure encoded in a 1-catego rical sheaf theory S.
The graph of a map of stacks f : X→ Y provides a correspondence from X to Y and a
correspondence from Y to X. We denote the respective induced maps by f∗ :S(X)→S (Y )
and f ! :S(Y )→S (X). For π : X → pt = Spec k, we denote by ωX = π!k ∈S (X) the
S-analogue of the dualizing sheaf, and by ω(X) = π∗ωX∈S (pt) = dgVect k theS-analogue of
“global volume forms”. We adopt traditional notations whenever p ossible, for example writing
Γ(X,F ) = π∗(F ), forF∈S (X)
The functoriality of S concisely encodes base change for f∗ and f !. Its symmetric monoidal
structure provides equivalences
S(X×Y )≃S (X)⊗S (Y ),
as well as a symmetric monoidal structure on S(X) for any X (using pullback along diagonal
maps). The 2-categorical extension S further encodes an identiﬁcation of f ! with the right
adjoint of f∗ for f proper.
Since a sheaf theoryS is symmetric monoidal, it is automatically compatible with dimensions
and traces: for any X∈Corrk, and any endomorphism Z∈Corrk(X,X ), we have
dim(S(X))≃S (dim(X)) Tr( S(Z))≃S (Tr(Z))
Let us combine this with the calculation of the right hand sides and high light speciﬁc examples
of interest.
Proposition 2.16. Fix a sheaf theory S :Corrk→dgCatk.
(1) The S-dimension dim(S(X)) = HH ∗(S(X)) of any X ∈ Corrk is S1-equivariantly
equivalent withS-global volume forms on the loop space
dim(S(X))≃ω(LX).
In particular, for G an aﬃne algebraic group, characters of S-valued G-representations are
adjoint-equivariantS-global volume forms
dim(S(BG))≃ω(G/G)
(2) The S-trace of any endomorphism Z ∈ Corrk(X,X ) is equivalent to S-global volume
forms on the restriction to the diagonal
Tr(S(Z))≃ω(Z|∆ )
14 DA VID BEN-ZVI AND DA VID NADLER
In particular, the S-trace of a self-map f : X→ X is equivalent to S-volume forms on the
f -ﬁxed point locus
Tr(f∗)≃ω(Xf )
Remark 2.17 (Local sheaf theory) . To apply this proposition, far less structure than a full
sheaf theory is required. We only need the data of the functor S on the handful of objects
and morphisms involved in the construction of dimensions and traces as in Remark 2.3. In
particular, we only need base change isomorphisms for pullback and p ushforward along speciﬁc
diagrams, rather than the general base change provided by a fun ctor out of Corrk. This is often
easy to verify in practice, in particular for the examples Q,Q! andD (see for example [BFN]
for the quasicoherent setting).
2.3.1. Examples of sheaf theories. As we explain in Section 5, the work [GR2] (combined with
essential results from [DG]) construct two sheaf theories Q! andD:
• TheoryQ!: the theory of ind-coherent sheaves Q!(X). This is the “large” version Q!(X) =
Ind Coh(X) of the category of coherent sheaves, which by deﬁnition are the compact objects
inQ!(X). (For smooth X, ind-coherent and quasicoherent sheaves are equivalent.) Maps a re
given by the standard pushforward f∗ and exceptional pullback f !. The Q!-dualizing sheaf
is the usual dualizing complex ωX , and (for X proper) the Q!-global volume forms are its
sections RΓ(X,ωX) = RΓ(X,OX )∗. The K-theory of Q!(X) is algebraic G-theory G(X), the
homological version of algebraicK-theory for potentially singular spaces suited to Grothendieck-
Riemann-Roch theorems.
• TheoryD: the theory of D-modulesD(X) with the standard functors f∗ and f !. The
compact objects are necessarily coherent D-modules (this suﬃces for X a scheme; see [DG]
for a characterization in the case of a stack). The D-dualizing sheaf is the Verdier dualizing
complex ωX , and the D-global volume forms (for X smooth) are the Borel-Moore homology
RΓ(XdR,ωX ) = HdR(X)∗.
Remark 2.18. More precisely, [GR2] construct the sheaf theories Q! andD as lax symmetric
monoidal functors on a much broader class of stacks, with pullback s allowed for arbitrary maps
but pushforward only for schematic morphisms. The strictness fo llows from results of [DG], as
we explain in Section 5.3.1, as does the deﬁnition of pushforwards for arbitrary maps of QCA
stacks (without the functorial apparatus of [GR2] but suﬃcient for all the “local” constructions
we need, in the sense of Remarks 2.3, 2.6 and 2.17).
Remark 2.19 (Quasicoherent sheaves) . The theory of quasicoherent sheaves X ↦→Q(X) be-
haves similarly with respect to 1-categorical properties. It also de ﬁnes a symmetric monoidal
functor out of the (∞, 1)−category of correspondences of stacks, using standard pullbac kf ∗ and
pushforwardf∗ functors. Assuming X is perfect (in the sense of [BFN]), the compact objects of
Q(X) form the subcategory of perfect complexes Perf (X), and we have Q(X) = Ind Perf (X).
The analog of the dualizing sheaf is the structure sheaf OX , and the Q-“global volume forms”
are the global functions RΓ(X,OX ). The K-theory of Q(X) is the usual algebraic K-theory
K(X). However while we have (f ∗,f ∗) adjunction and f ∗ preserves perfection for arbitrary mor-
phisms, proper pushforward does not preserve perfection and w e do not have proper adjunction
of the form ( f∗,f ∗) (unless we add smoothness and twisting by relative dualizing sheave s). In
other words,Q andK-theory are better adapted to pullback, while Q! andG-theory are better
adapted to integration and character formulas.
Remark 2.20 (Sheaf theories in diﬀerential topology and elliptic operators) . It is tempting to
think of sheaf theories in algebraic geometry as analogues of elliptic o perators or complexes
NONLINEAR TRACES 15
in diﬀerential topology. In particular, the theory Q!(X) for a smooth variety X is a natural
setting for the study of the Dolbeault ∂-operator coupled to vector bundles, while the theory
D(X) is similarly a natural setting for the study of the de Rham operator d coupled to vector
bundles. The pushforward operation is the analogue of the index. I n this direction, it would be
interesting to develop sheaf theories on derived manifolds, for exa mpleC∞-schemes and stacks.
Quasicoherent sheaves in the sense of Joyce [J] are a natural can didate. Another interesting
setting is categories of elliptic complexes on manifolds. The general r esults below would then
provide an approach to generalizations of the classical Atiyah-Sing er and Atiyah-Bott theorems.
Let us spell out the main ingredients of Proposition 2.16 for our exam ples. Recall that for X
a smooth scheme, LX≃ SpecX Sym•(ΩX [1]), and for BG a classifying stack, L(BG)≃G/G.
• TheoryQ: For X a smooth scheme, we have the HKR identiﬁcation of functions on the loop
space (or the Hochschild chain complex) with diﬀerential forms, dim(Q(X))≃ Γ(X, Sym•(ΩX [1])),
or more generally,Q-global volume forms on Xf are the coherent cohomology O(Xf ). For BG
a classifying stack, Q-global volume forms on L(BG) are the coherent cohomology O(G/G),
which for G reductive are the underived invariants O(T )W .
• TheoryQ!: For X smooth, we have Q(X)≃Q !(X), and so we recover the above de-
scriptions. For X proper,Q-global volume forms on LX are the dual of the Hochschild chain
complex (see [P]).
• TheoryD: For X a smooth scheme, D-global volume forms on LX are the de Rham
cochains dim(D(X))≃ C∗
dR(X), or more generally, D-global volume forms on Xf are the de
Rham cochains C∗
dR(Xf ), or equivalently those of the underlying underived scheme of Xf . For
BG a classifying stack, D-global volume forms on L(BG) are the Borel-Moore homology of
G/G.
2.3.2. Integration formulas for traces. Now let us turn to the functoriality of dimensions and
traces, which is reﬂected in integration of volume forms along prope r maps.
For a sheaf theory
S :Corrprop
k →dgCatk,
the counit of the ( f∗,f !) adjunction for a proper map f : X → Y gives rise to a canonical
integration map ∫
f :ω(X) /d47/d47ω(Y )
Theorem 2.21. Fix a sheaf theory S :Corrk→dgCatk.
(1) For any proper map f :X→Y , the induced map on dimensions
dim(f∗) : dim(S(X)) /d47/d47 dim(S(Y ))
is identiﬁed ( S1-equivariantly) with integration along the loop map
dim(f∗)≃
∫
Lf :ω(LX) /d47/d47ω(LY )
(2) Given a proper map f : X→ Y regarded as a correspondence from X to Y , and self-
correspondencesZ∈Corrk(X,X ) and W∈Corrk(Y,Y ), together with an identiﬁcation
α :Z ∼ /d47/d47X×Y W
of correspondences from X to Y , the induced trace map is identiﬁed with integration along t he
natural map
Tr(f∗,α )≃
∫
τ (f,s) :ω(Z|∆ X ) /d47/d47ω(W|∆ Y )
16 DA VID BEN-ZVI AND DA VID NADLER
Remark 2.22. Similarly, in the case of the theory Q of quasicoherent sheaves, the standard
adjunction (f ∗,f ∗) leads to the evident contravariant functoriality of dimensions und er arbitrary
maps, given by pullback of functions on loop spaces.
Remark 2.23 (Categoriﬁed version) . For applications to categorical representation theory, in
particular the geometric Langlands program, it is interesting to hav e character formulas for
group actions on categories. Such formulas would follow from a good formalism of “stack theo-
ries”, the higher unstable analogs of sheaf theories, such as the a ssignmentX→ShvCatk(X).
Such stack theories could be formulated as symmetric monoidal fun ctorsS :Corrk→A out of
a correspondence (∞, 2) (or more naturally ( ∞, 3)) category with values in a category A such
as that of module categories for dgCatk. Namely, we are interested in categoriﬁed analogues of
D andQ, taking values in the ∞-category PrL of presentable∞-categories, in which we assign
to a scheme or stack X the∞-category of quasicoherent sheaves of module categories over D
orQ. Since such theories have not been fully constructed yet, we will on ly brieﬂy sketch the
idea.
For any stack X and sheaf theory S, the category of sheaves S(X) is naturally symmetric
monoidal, and so we may consider its ∞-category of (presentable, stable) module categories
S(X)-mod. To obtain a more meaningful geometric theory we should she aﬁfy this construction.
For example, strong or Harish-Chandra G-categories (in other words, module categories over
D(G) with convolution) are identiﬁed with sheaves of categories over th e de Rham stack of BG.
However, in the quasicoherent case, the “1-aﬃneness” theorem of Gaitsgory [G2] identiﬁes
Q(X)-modules with sheaves of categories on X for a large class of stacks (speciﬁcally, for X
an eventually coconnective quasi-compact algebraic stack of ﬁnite type with an aﬃne diagonal
over a ﬁeld of characteristic 0). In particular, Q(BG)-modules are identiﬁed with algebraic
G-categories.
In the quasicoherent case, the general formalism of this paper sh ould provide anS1-equivariant
equivalence dim(Q(X)-mod) =Q(LX), identifying the class [Q(X)] of the structure stack with
the structure sheafO(LX). In particular, the characters of quasicoherent G-categories are given
byQ(G/G). The induced map on dimensions dim( f∗) : dim(Q(X)-mod)→ dim(Q(Y )-mod) is
identiﬁed S1-equivariantly with the morphism given by pushforward along the loop map
dim(f∗) =Lf∗ :Q(LX) /d47/d47Q(LY )
In particular, for an algebraic group G and G-space X with π : X/G→ BG, the character
of the G-categoryQ(X/G) is given by the pushforward Lπ∗O(LX/G)∈Q (G/G). Analogous
results are expected for strong or Harish-Chandra G-categories (module categories for D(G)
with convolution) using the sheaﬁﬁcation of the theory of D(X)-module categories. We hope
to return to these applications in future works.
