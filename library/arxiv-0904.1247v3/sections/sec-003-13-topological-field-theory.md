---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-003-13-topological-field-theory
section_title: "Topological field theory"
section_number: 1.3
pages: 9-12
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
of topological ﬁeld theory (TFT). We will not give a formal introduction to TFT but rather remind
the reader of its broad outline informally and illustrate it via the example of ﬁnite group gauge
theory. We refer to [L3] for a detailed overview of the ∞-categorical setting for TFT (including
the ∞-version of n-categories) and the Cobordism Hypothesis. We only use the (∞, 2)-categorical
language for motivation and it does not recur elsewhere in the paper.
1.3.1. 2-dimensional TFT. An extended framed 2-dimensional TFT is a symmetric monoidal func-
tor out of the symmetric monoidal (∞, 2)-category 2Bordfr of 2-dimensional framed bordisms (with
monoidal structure given by disjoint union):
• objects: (2-dimensionally framed) 0-manifolds,
• 1-morphisms: (2-dimensionally framed) 1-dimensional bordisms between 0-manifolds,
• 2-morphisms: classifying spaces of (framed) 2-dimensional bordisms between 1-bordisms.
In other words, all n-morphisms for n > 2 are invertible, and together form (the fundamental
∞-groupoid of) classifying spaces of framed bordisms.
One can similarly deﬁne the oriented bordism l (∞, 2)-category 2Bord, in which one extends
from framed manifolds to all oriented manifolds and their bordisms.
In general, if the target is a plain discrete 2-category, then one obtains an ordinary functor out
of the 2-category with the same objects and 1-morphisms but 2-morphisms given by 2-dimenisonal
bordisms up to diﬀeromorphism. This setting is studied in detail in [Sch].
In [L3], Lurie outlines the proof of a general ∞-categorical version of the Cobordism Hypothesis
formulated by Baez-Dolan [BDo]. The 2-dimensional case which we use was inspired by work of
Costello [C] and Kontsevich-Soibelman [KS] on open-closed ﬁeld theory. The Cobordism Hypothesis
speciﬁes increasingly strong ﬁniteness conditions, known as d-dualizability, that allow an object of
a symmetric monoidal (∞, d)-category to be “integrated” over framed manifolds of dimension at
most d, thus deﬁning an extended d-dimensional TFT. Moreover, the space of d-dualizable objects
carries an action of O(d), and objects on which the action of SO(d) has been trivialized give rise to
ﬁeld theories deﬁned on all oriented manifolds of dimension at most d.
1.3.2. Toy model: ﬁnite group gauge theory. To place our results in the framework of TFT, it is
illuminating to return to the toy model of a ﬁnite group Γ. There is an oriented 2-dimensional TFT
ZΓ called Dijkgraaf-Witten theory [DW] which eﬃciently encodes all of the familiar structures in
the complex representation theory of Γ discussed earlier. (One could consult [Sch] for details in all
of the discussion to follow, in particular for the construction of 2-dimensional oriented TFTs from
symmetric Frobenius algebras. See also [F] for a detailed study of ZΓ, and [FHLT] for a discussion
of ZΓ in the setting of the Cobordism Hypothesis.)
The target of ZΓ is the Morita 2-category of algebras AlgC with the following structure:
• objects: associative algebras over C,
• 1-morphisms: bimodules (ﬂat over the source),
• 2-morphisms: morphisms of bimodules.
The symmetric monoidal structure of AlgC is given by tensor product of algebras with unit C. By
assigning to an algebra A its category PerfA of perfect modules (summands of ﬁnite colimits of
free modules), we can identify the Morita 2-category AlgC with a full subcategory of the 2-category
AbCatC of small C-linear abelian categories, exact functors and natural transformations.
9
The ﬁeld theory ZΓ assigns to each cobordism M a linearization of the space of Γ-gauge ﬁelds on
M, or in other words, the orbifold of principal Γ-bundles or Galois Γ-covers over M. In particular,
it assigns the following to closed 0, 1 and 2-manifolds:
• To a point, ZΓ assigns the group algebra:
ZΓ(pt) = C[Γ] ∈AlgC.
Alternatively, we can pass to the category of ﬁnite-dimensional complex modules:
ZΓ(pt) = Repfd
C (Γ) ∈AbCatC.
This is the category of ﬁnite-dimensional algebraic vector bundles on the orbifold of Γ-
bundles on a point.
• To a circle, ZΓ assigns class functions:
ZΓ(S1) = C[Γ]Γ = C[Γ/ad Γ] ∈Vectfd
C = 1 HomAbCatC(Vectfd
C , Vectfd
C ),
This is the vector space of functions on the orbifold of Γ-bundles on the circle.
• To a closed surface, ZΓ counts Γ-bundles:
ZΓ(Σ) = #{Hom(π1(Σ), Γ)/Γ} ∈C = 2 HomAbCatC(C, C)
where as usual a bundle P is weighted by 1/ Aut(P). This is the volume of the orbifold of
Γ-bundles on the surface.
From the point of view of the Cobordism Hypothesis, we only have to specify that we assign the
group algebra C[Γ] to a point to determine the rest of the TFT structure. Any object of AlgC is
1-dualizable, with dual given by the opposite algebra. The requirement of 2-dualizability however
is extremely restrictive: as proven in [Sch], 2-dualizable objects of AlgC are precisely separable
algebras, i.e., algebras for which A is projective as an A-bimodule. Over C, separable algebras are
precisely ﬁnite-dimensional semi-simple algebras. Invariance under SO(2) amounts to the data of a
non-degenerate trace, or in other words, the structure of a symmetric Frobenius algebra.
1.3.3. TFTs from semi-rigid categories. Our main results can be viewed as the construction and
partial description of an oriented 2-dimensional TFT valued in a categoriﬁed analogue of the Morita
2-category AlgC. Namely, we replace C-algebras by C-linear monoidal categories, or more precisely,
algebra objects in the symmetric monoidal ∞-category StC. We denote by Alg(1)(StC) the Morita
(∞, 2)-category with objects algebras in StC, 1-morphisms bimodule categories and 2-morphisms
the spaces of intertwiners between bimodule categories. (See [L3] for a more precise description; we
reiterate that we only use the (∞, 2)-language for informal motivation).
As with AlgC, any object of Alg(1)(StC) is 1-dualizable, with dual given by the monoidal opposite.
The much stronger condition of 2-dualizability of A ∈Alg(1)(StC) breaks down into two parts. First,
the underlying category of A must be dualizable as a plain category. In practice, this is an easily
satisﬁed condition, guaranteed for example by the compact generation of A, in which case the dual
is a modiﬁcation of the opposite category of A. Second, one needs A to be dualizable as an A-
bimodule, a natural analogue of separability. Dualizability as a bimodule is closely related to the
abundance of monoidal duals of objects of A:
Theorem 1.17 (Theorem 3.18). Any semi-rigid category A ∈Alg(1)(StC) is 2-dualizable.
It follows that any semi-rigid monoidal category A ∈Alg(1)(StC), in particular the Hecke cate-
gories HG and e
HG, deﬁnes a framed 2-dimensional TFT ZA valued in Alg(1)(StC) which makes the
following assignments:
• To a point, ZA assigns A ∈Alg(1)(StC).
• To a circle with cylinder framing, ZA assigns the trace Tr(A) ∈StC with its cyclic S1-action.
• To the circle with annulus framing, ZA assigns the center Z(A) ∈StC with its E2-structure.
• To a framed surface, ZA assigns an object of VectC.
10
1.3.4. Oriented TFTs from Calabi-Yau monoidal categories. To extend the TFT ZA from framed
to oriented manifolds, the Cobordism Hypothesis requires A ∈Alg(1)(StC) be a ﬁxed point for the
SO(2)-action on 2-dualizable objects.
Part of this action can be described very explicitly:
following [L3, Proposition 4.2.3], a 2-
dualizable object A ∈Alg(1)(StC) admits a Serre automorphism SA characterized by
evR
A = (SA ⊗idAop) ◦coevA
It can be interpreted as the monodromy of A around the SO(2)-action, or in other words, the ﬁrst
obstruction to SO(2)-invariance of A. Thus a trivialization of SA as an automorphism makes A a
ﬁxed point of the action of the free group (James construction) on the circle ΩS2 = ΩΣSO(2). This
suﬃces to identify the values of ZA on diﬀerent framed circles, for example the monoidal center and
trace of A.
Following [L3, Section 4.2], the stronger condition of SO(2)-invariance of A can be encoded by
the notion of Calabi-Yau monoidal category (as recalled in Deﬁnition 1.7 above).
Corollary 1.18 (Theorem 3.18). A Calabi-Yau (respectively, pivotal) structure on a semi-rigid
category A ∈Alg(1)(StC) deﬁnes an oriented (respectively, a weakly oriented) 2-dimensional TFT
so that ZA(S1) is identiﬁed with both the monoidal center and trace of A.
Example 1.19 (Fusion categories and 3-dimensional Dijkgraaf-Witten theory). For a ﬁnite group Γ,
the categories Vectfd
C (Γ) of ﬁnite-dimensional vector bundles on Γ and Repfd
C (Γ) of ﬁnite-dimensional
complex representations of Γ are key examples of fusion categories, monoidal categories satisfying
strong ﬁniteness conditions. In fact, it is proved in [DSS] that fusion categories are 3-dualizable
objects of a natural 3-category of monoidal categories, bimodule categories, intertwines and nat-
ural transformations. (They also show that pivotal structures give ΩS2-ﬁxed structures on these
theories.) The monoidal categories Vectfd
C (Γ) and Repfd
C (Γ) are Morita equivalent and so deﬁne
the same 3-dimensional TFT, an untwisted version of 3-dimensional Dijkgraaf-Witten theory [DW]
and a natural categoriﬁcation of the ﬁnite group gauge theory discussed earlier. Since Repfd
C (Γ) is
symmetric monoidal, it is easy to evaluate this TFT on any manifold. For example, to a surface Σ,
one attaches the vector space of functions on the orbifold of Γ-principal bundles over Σ, while to a
3-manifold M, one attaches the volume of the orbifold of Γ-principal bundles over M.
Example 1.20 (Quasicoherent 3-dimensional theories). For a perfect stack X, the symmetric monoidal
category Q(X) of quasicoherent sheaves is rigid and pivotal. For example, for G a reductive group,
its classifying stack BG is perfect, and the category Q(BG) comprises algebraic representations
of G.
One can calculate the resulting categoriﬁed 2-dimensional TFT explicitly by the theory of topo-
logical chiral homology [L2, Section 5.3], or from the direct constructions of [BFN]. In particular,
it makes the following assignments, stated in general, then spelled out when X = BG:
• Zqc
X (pt) = Q(X) = Rep(G), algebraic representations.
• Zqc
X (S1) = Q(LX) = Q(G/ad G), adjoint-equivariant quasicoherent sheaves.
• Zqc
X (Σ) = O(XΣ) = RΓ(CharG(Σ), O), functions on the character variety.
As explained in [BFN2], the rigid category Q(BG) is in fact Morita equivalent to the quasicoherent
group algebra Q(G), and any intermediate Hecke category Q(H\G/H), for H ⊂G, so that all deﬁne
equivalent TFTs.
Furthermore, Q(X) is naturally a Calabi-Yau monoidal category, and hence Zqc
X extends to an
oriented TFT. However, unlike the case of fusion categories, Q(X) is not typically 3-dualizable,
and hence Zqc
X does not typically extend to 3-manifolds. Nonetheless, it is natural to think of our
constructions as intrinsically 3-dimensional as they correspond to supersymmetric 3-dimensional
quantum gauge theories in physics.
1.3.5. Character Theory. Finally, let us turn to TFTs built out of D-modules on the complex re-
ductive group G. In analogy with the above results for quasicoherent sheaves, one might expect
11
to construct a single TFT starting from a Morita equivalent class of algebras including the “com-
mutative algebra” D(BG), the “smooth group algebra” D(G), or any intermediate Hecke algebra
D(H\G/H), for H ⊂G. Furthermore, one might expect this TFT to attach to the circle the cate-
gory D(G/G) of adjoint-equivariant D-modules on G, and to a surface Σ the de Rham cohomology
Γ(CharG(Σ), Ω•) of the character variety.
This expectation turns out to be wrong on several counts, starting with the failure of Morita
equivalence. The symmetric monoidal category D(BG) is indeed 2-dualizable, however it is too
small to see the rich geometry of G/ad G, as discussed in Section 1.2.2 above.
It only sees the
homotopy type of G, and in particular assigns to the circle the category of adjoint-equivariant
unipotent local systems on G. At the other extreme, the monoidal category D(G) ∈Alg(StC) is
not 2-dualizable, so does not deﬁne a 2-dimensional TFT, though its center is indeed D(G/G).
There is a sweet spot in between these two extremes given by Hecke categories. The main results
of this paper allow for the following deﬁnition and calculate the resulting TFTs on a circle.
Deﬁnition 1.21. The equivariant character theory χG of a reductive group G is the oriented 2d
TFT valued in Alg(1)(StC) deﬁned by the Hecke category HG. Likewise, the monodromic character
theory eχG is the oriented 2d TFT valued in Alg(1)(StC) deﬁned by e
HG.
It follows from the Koszul duality of [S, S, BY] that there is a Langlands duality for the two-
periodic versions of the above TFTs.
Corollary 1.22. The invariants assigned by eχper
G
and χper
G∨to any oriented manifold are identiﬁed.
In particular, unipotent character sheaves with their TFT structures are identiﬁed by Langlands
duality. In another direction, boundary conditions for the character theory are given by module
categories for the corresponding Hecke categories, for example, by categories D(K\G/B) of Harish
Chandra (g, K)-modules.
The Langlands duality of boundary conditions in particular encodes
Soergel’s conjecture [S] on a categorical Langlands classiﬁcation for real groups. In another direction,
it would be highly interesting to describe the vector spaces χG(Σ) that the character theory attaches
to a surface Σ. It is natural to conjecture a relation with the de Rham cohomology of character
varieties, and hence with the fascinating conjectures of Hausel, Letellier and Rodriguez-Villegas
[HRV, HLRV, H]. Such a relation would imply a Langlands duality for the cohomology of character
varieties, one of our original motivations and a subject of ongoing work with Sam Gunningham.
