---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-001-11-summary
section_title: "Summary"
section_number: 1.1
pages: 1-6
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
1.2. Inspirations and motivations 6
1.3. Acknowledgements 6
2. Overview 7
2.1. Traces in category theory 7
2.2. Traces in geometry 9
2.3. Trace formulas via sheaf theories 12
3. Traces in category theory 16
3.1. Preliminaries 16
3.2. Dualizability 17
3.3. Traces and dimensions 19
3.4. Functoriality of dimension 21
3.5. Functoriality of traces 23
4. Traces in Geometry 24
4.1. Categories of correspondences 24
4.2. Traces of correspondences 25
4.3. Geometric functoriality of dimension 27
4.4. Geometric functoriality of trace 29
5. Traces for sheaves 29
5.1. Dimensions and traces of sheaf categories: 1-categorical co nsequences 30
5.2. Integration formulas for traces: 2-categorical consequen ces 31
5.3. Ind-coherent sheaves and D-modules 33
1
2 DA VID BEN-ZVI AND DA VID NADLER
References 36
1. Introduction
This paper is devoted to traces and characters in homotopical alge bra and their application to
algebraic geometry and representation theory. We observe that many geometric ﬁxed point and
trace formulas can be expressed as linearizations of fundamental nonlinear identities, describing
dimensions and traces directly in the setting of correspondence ca tegories of varieties or stacks.
This gives a simple uniform perspective on (and useful generalization s of) geometric character
and ﬁxed point formulas of Grothendieck-Riemann-Roch and Atiyah -Bott-Lefschetz type. In
addition, one can also specialize the universal geometric formulas to higher categorical settings
not captured within a linear framework, such as characters of gro up actions on categories.
The paper is organized as follows: after a brief summary in Section 1.1 , we give a detailed
overview in Section 2, in three sections: ﬁrst, the abstract funct oriality of traces in higher
category theory; second, their calculation in correspondence ca tegories in derived algebraic
geometry; and third, their specialization via sheaf theories. The re st of the paper follows the
same structure with more details provided. We emphasize the forma l nature and appealing
simplicity of the constructions in any suﬃciently derived setting. For example, in the second
part, we work within derived algebraic geometry, but the statemen ts and proofs should hold in
any setting (for example, derived manifolds) with a suitable notion of ﬁber product to handle
non-transversal intersections. The main objects appearing in tr ace formulas are the derived loop
space (the self-intersection of the diagonal in its role as the nonline ar trace of the identity map)
and more general derived ﬁxed point loci. The importance of a derive d setting also appears
prominently in the third part, where the sheaf theories we apply mus t have good functorial
properties with respect to ﬁber products. As a result, the theor y of characters in Hochschild
and cyclic homology is expressed directly by the geometry, resulting in simpler formulations.
For example, the Todd genus in Grothendieck-Riemann-Roch and th e denominators in the
classical Atiyah-Bott formula arise naturally from derived calculatio ns.
1.1. Summary. We now describe the main theorem, extending classical trace and dim ension
formulas to a very general setting in derived algebraic geometry (in cluding equivariance for
arbitrary Lie algebroids or aﬃne algebraic groups) without any smoo thness or transversality
assumptions, while emphasizing that the main contribution of the pap er is the simple geometric
formalism underlying these formulas. For our general and formal n onlinear results, we need
not assume anything about what classes of derived stacks and mor phisms we work with. For
applications, we need to be in a setting in which the powerful mechanis m of sheaf theory is
fully developed [G1, DG, GR2].
Setting 1.1. Throughout this paper, we work over a ﬁeld k of characteristic zero. A stack X
connotes either
(1) a QCA derived stack in the sense of [DG]. In other words X is quasicompact with
aﬃne diagonal and the underived inertia of X is ﬁnite presentation over the underlying
underived stack Xcl.
(2) an ind-inf-scheme, in the sense of [GR2]. These include (derived) schemes of ﬁnite (or
locally almost of ﬁnite) type and ind-schemes built out of un ions of the former along
closed embeddings, as well as their quotients by arbitrary L ie algebroids, or equivalently
formal groupoids.
NONLINEAR TRACES 3
By a proper map we indicate a proper and schematic map, while for ind-pro per indicates ind-
proper and ind-inf-schematic. All appearances of proper ma ps in this paper may be replaced by
ind-proper ones.
Thus the class of spaces we consider includes all k-derived schemes of ﬁnite type and their
quotients by either Lie algebroids or ﬁnite type aﬃne group schemes .
Given a derived stack πX : X→ Speck, we denote by πLX :LX = Map(S1,X )→ Speck
its derived loop space. In general, the derived loop space is a derived thickening of the inertia
stack. For a map f :X→Y , we will denote by Lf :LX→LY the induced map on loops.
Example 1.2. For many applications, the following two special cases are notewort hy.
When X is a smooth scheme, LX≃ TX [−1] is the total space of the shifted tangent space
by the HKR theorem. The same holds for an arbitrary scheme, if we r eplace the tangent
space by the tangent complex, see for example [BN10b]. For f : X→ Y a map of schemes,
Lf : TX [−1]→ TY [−1] is (the shift of) the usual tangent map.
WhenY =BG is a classifying stack, LY ≃G/G is the adjoint quotient. For X aG-scheme,
and f : X/G→ BG the corresponding classifying map, Lf :L(X/G)→L BG≃ G/G is the
universal family of derived ﬁxed point loci. More precisely, for any ele mentg∈G, the derived
ﬁxed point locus Xg⊂X is precisely the derived ﬁber Xg≃L (X/G)×G/G{g}
We will measure stacks X by diﬀerential graded (dg) enhancements of derived categories o f
sheaves.
The most familiar is the assignment X↦→Q(X) of the (unbounded) category of quasicoherent
sheaves. However, we will make essential use of Grothendieck-Se rre duality, in the guise of
an adjunction ( f∗,f !) between push-forward and extraordinary pullback for proper m aps X.
This duality is most naturally expressed in the setting of ind-coherent sheaves X ↦→Q!(X)
as developed in [G1, GR2]. Ind-coherent sheaves agree with quasico herent sheaves for smooth
schemes but diﬀer on singular schemes, where [bounded complexes o f] coherent sheaves (the
compact objects of Q!) diﬀer from perfect complexes (the compact objects of Q). In other
words, ind-coherent sheaves are to coherent sheaves and G-theory (the setting of Grothendieck-
Riemann-Roch theorems) as quasicoherent sheaves are to perfe ct complexes and K-theory.
Another sheaf theory to which the general formalism developed in [G R2] applies is the
theory ofD-modules X→D (X), which for smooth schemes agrees with the classical notion of
quasicoherent complexes of modules for the sheaf of diﬀerential o peratorsDX (i.e. with compact
objects given by bounded coherent complexes of DX -modules). In general [GR1, GR2] D(X) is
deﬁned as the category of crystals, i.e., as ind-coherent complexe s on the de Rham space of X
D(X) :=Q!(XdR).
The compact objects in D(X) for X a scheme are the coherent D-modules, while for X a stack
they form a smaller class, the safeD-modules of [DG].
The book [GR2] develops the theories Q! andD in particular as functors out of 2-categories
of correspondences of schemes and stacks, with 1-morphisms fr om X to Y given by correspon-
dences representable over Y and 2-morphisms given by ind-proper ind-schematic morphisms of
correspondences. This theory encodes a huge amount of struct ure, including in particular pull-
back and pushforward functorsf ! andf∗ satisfying base change, as well as the (f∗,f !) adjunction
for proper (or even ind-proper) maps. They also establish symmet ric monoidal properties of
the sheaf theory. 1 (See Sections 2.3 and 5 for more background and precise statemen ts.)
LetS =Q! orS =D denote either of these sheaf theories.
1W e will also need from [DG] the construction of continuous pu shforward functors for all maps of QCA stacks
(such as the non-representable projection π X : X → pt from a stack) and their base-change property.
4 DA VID BEN-ZVI AND DA VID NADLER
We let ωX = π!
XOSpeck ∈ S(X) denote the appropriate dualizing sheaf. Thus for ind-
coherent sheaves, ωX∈Q !(X) is the algebraic dualizing sheaf, and for D-modules, ωX∈D (X)
is the Verdier dualizing sheaf. Let ω(X) = πX∗ωX denote the corresponding complex of global
volume forms: for ind-coherent sheaves, ω(X)∈k-mod consists of algebraic volume forms, and
forD-modules, ω(X)∈ k-mod consists of locally constant distributions (Borel-Moore chains )
for X a scheme.
For X a stack we use the continuous “renormalized” pushforward funct or on D-modules
of [DG], which roughly replaces equivariant cohomology (derived invar iants) by a shift of equi-
variant homology (derived coinvariants, see [DG, Example 9.1.6]), so that ω(Y/G ) for a G-
varietyY is given by a shift of G-coinvariants on Borel-Moore chains on Y . (Note that even for
X =BG this diﬀers from the standard deﬁnition of equivariant Borel-Moore homology, which
is identiﬁed in this case with equivariant cohomology.)
For a proper (or ind-proper) map f : X → Y , adjunction provides an integration map∫
f :ω(X)→ω(Y ).
Example 1.3. Let us continue with the special cases of Example 1.2, and focus in pa rticular
on algebraic distributions ωLX∈Q !(LX) on the loop space.
When X is a smooth scheme, LX≃ TX [−1] is naturally Calabi-Yau, and its global volume
forms are identiﬁed with diﬀerential forms ω(TX [−1])≃ O(TX [−1])≃ Sym•(ΩX [1]). The
canonical “volume form” on LX is given by the Todd genus (as explained by Markarian [Ma]):
the resulting integration of functions on LX diﬀers from the integration of diﬀerential forms on
X by the Todd genus.
WhenY =BG is a classifying stack, LY ≃G/G is naturally Calabi-Yau, and its global vol-
ume forms are invariant functions ω(G/G)≃O (G/G)≃O (G)G. If G is reductive with Cartan
subgroup T⊂ G and Weyl group W , the naive invariants O(G)G≃O (T )W are equivalent to
the derived invariants, but in general there may be higher cohomolo gy.
Theorem 1.4. LetS =Q! orS =D denote either the theory of ind-coherent sheaves or
D-modules. Recall our conventions for stacks and morphisms, Setting 1.1.
• For a stack X, there is a canonical identiﬁcation HH ∗(S(X))≃ω(LX) of the Hochschild
homology of sheaves on X with distributions (or renormalized Borel-Moore chains) o n the loop
space.
• For a proper (or ind-proper) map of stacks f : X→ Y the induced map HH ∗(S(X))→
HH ∗(S(Y )) is given by integration along the loop map Lf :LX→LY .
• Grothendieck-Riemann-Roch: In particular, for any compact object M∈S (X) (co-
herent sheaf or safe coherent D-module) with character [M ]∈HH ∗(S(X))≃ω(LX), there is
a canonical identiﬁcation
[f∗M]≃
∫
Lf
[M ]∈HH ∗(S(Y ))≃ω(LY )
In other words, the character of a pushforward along a proper map is the integral of the character
along the induced loop map.
• Atiyah-Bott-Lefschetz: LetG be an aﬃne group, and X a proper stack with G-action,
or equivalently, a proper map f :X/G→BG. Then for any compact object M∈S (X/G) (G-
equivariant coherent sheaf or safely equivariant coherent D-module on X), and element g∈G,
there is a canonical identiﬁcation
[f∗M ]|g≃
∫
Lf
[M ]|X g
NONLINEAR TRACES 5
In other words, under the identiﬁcation of invariant functi ons and volume forms on the group,
the value of the character of an induced representation at a g roup element is given by the integral
of the original character along the corresponding ﬁxed poin t locus of the group element.
• Extension to traces: The trace Tr (S(Z)) of the endofunctor of S(X) given by a self-
correspondence (e.g. a self-map) X ← Z → X is given by distributions on the ﬁxed points
ω(Z|∆ ).
• For a map f : (X,Z )→ (Y,W ) of stacks with self-correspondences 2, the induced map
Tr (S(Z))→Tr (S(W )) is given by integration along ﬁxed points Z|∆ X→W∆ Y .
Example 1.5 (F robenius-Weyl Character F ormula). Here is a reminder of a well-known
application of the Atiyah-Bott-Lefschetz formula in representat ion theory.
• If G is a ﬁnite group, and X =G/K is a homogeneous set, and M =k[G/K] the ring of
functions, one recovers the Frobenius character formula for th e induced representation k[G/K].
• If G is a reductive group, X = G/B is the ﬂag variety, X/G = pt/B→ pt/G. The loop
map
L(X/G) = B/B≃ ~G/G→G/G
is the (group) Grothendieck-Springer simultaneous resolution, wit h ﬁbers giving ﬁxed point
loci on the ﬂag variety. For M =L an equivariant line bundle on G/B, and g ∈ G runs
over a maximal torus, one recovers the Weyl character formula f or the induced representation
H ∗(G/B,L).
Remark 1.6. The reader will note no explicit appearance of the Todd genus in the a bove
formulas. In other words as for K-theory, pushforward of shea ves naturally agrees with the
pushforward in Hochschild homology. The Todd genus arises in compa ring these natural push-
forwards with the pushforward in cohomology, i.e., integration of fo rms. It arises when one
unwinds the integration map
∫
Lf :ω(LX)→ω(LY ), given by Grothendieck duality, in terms
of functions (or diﬀerential forms) using the Hochschild-Kostant -Rosenberg theorem. In par-
ticular, the familiar denominators in the Atiyah-Bott formula are implic it in the integration
measure on the ﬁxed point locus.
For instance, as mentioned above, when X is a smooth scheme, a geometric version of the
HKR theorem asserts that the loop space is the total space of the shifted tangent complex
LX ≃ TX [−1], and global volume forms are canonically functions ω(LX)≃O (TX [−1])≃
Sym•(ΩX [1]). Under this identiﬁcation (as explained by Markarian [Ma]), the res ulting inte-
gration of functions on LX diﬀers from the integration of diﬀerential forms on X by the Todd
genus.
Remark 1.7. The paper [KP] carries out the program described in this paper (i.e. r ecovering
classical identities from non-linear ones) by calculating explicitly the d erived contributions in
the case of the Atiyah-Bott formula.
Remark 1.8. The main contribution of this paper is hidden in the statement of this t heorem: we
establish nonlinear versions of character formulas in the setting of derived stacks, and deduce
classical formulas and new higher categorical analogues formally by applying suitable sheaf
theories. Thanks to the great generality of sheaf theory in derive d algebraic geometry [GR2],
the resulting applications hold with remarkably few assumptions.
We are particularly interested in the higher categorical variants wh ere one considers sheaves
of categories, in particular Frobenius-Weyl character formulas f or group actions on categories.
Since the requisite foundations are not yet fully developed, we post pone details of this to future
2i.e., we lift f to an identiﬁcation Z ≃ X ×Y W of correspondences from X to Y
6 DA VID BEN-ZVI AND DA VID NADLER
works. Applications include an identiﬁcation of the character of the category of D-modules
on the ﬂag variety with the Grothendieck-Springer sheaf, and of t he trace of a Hecke functor
on the category of D-modules on the moduli of bundles on a curve with the cohomology of a
Hitchin space.
