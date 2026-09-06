---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-012-43-d-modules-on-stacks
section_title: "D-modules on stacks"
section_number: 4.3
pages: 29-30
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
compact stack over C with aﬃne diagonal. By a representable morphism, we will always mean a
quasi-compact schematic morphism.
For schemesX, the categoryD(X) satisﬁes smooth descent with respect to !-pullbacks. Thus for
a stack X, one may deﬁne the category D(X) as a limit over smooth covers.
More explicitly given a smooth cover U→X by a scheme, with induced augmented Cech sim-
plicial scheme U∗→X, one obtains a cosimplicial category D(U∗), with maps given by !-pullbacks,
such that its totalization satisﬁes
D(X)≃ limD(U∗)
(See [BD, Section 7.5] for a discussion in the language of derived cate gories.) Alternatively, one
may calculate D(X) as the limit over ∗-pullbacks (over the smooth face maps) in the above Cech
simplicial scheme.
For an arbitrary morphism f : X→ Y of stacks, composition identities provide a continuous
pullback functor f ! which can be calculated locally with respect to smooth covers. In par ticular,
there is an object ωX∈D (X) whose !-pullback along any smooth cover U→X is the corresponding
object ωU∈D (U ).
For a representable morphism f : X→ Y , base change provides a continuous functor f∗ which
can be calculated locally with respect to smooth covers.
For a smooth representable morphism f :X→Y , there is a functor f ∗ along with an adjunction
(f ∗,f ∗) and canonical isomorphism f ∗≃f ![−2(dimX− dimY )].
One can extend the deﬁnition of f∗ to arbitrary morphisms f : X → Y , but it is no longer
continuous. In particular, the de Rham cohomology functor Γ dR is not continuous in general. It is
however representable by an object CX∈D (X) whose∗-pullback along any smooth cover U→X
is the corresponding object CU∈D (U ).
4.4. More on coherence, tensor product, and V erdier duality . Since f ! for a smooth mor-
phism f :X→Y preserves coherence, one may deﬁne coherent D-modules on a stack by requiring
coherence locally on smooth covers. We denote by Dcoh(X)⊂D (X) the full subcategory of coherent
D-modules.
By [DrG1, Theorem 8.1.1], for any stack X, the category D(X) is compactly generated and all
compact objects are coherent. However, it is not necessarily tru e that all coherent D-modules are
compact. For example, the object CX∈D (X) representing the de Rham cohomology functor Γ dR
is coherent (and in fact holonomic) but not in general compact. The case of the classifying space
X = BG of an aﬃne group G is illuminating and worked out in detail in [DrG1, Section 7.2].
In this case, Γ dR calculates equivariant cohomology, which is not continuous even whe n G is the
multiplicative group. More generally, ﬁnite rank vector bundles with ﬂ at connection on a smooth
stack are coherent (and in fact holonomic) but not necessarily com pact.
In general, there is the notion of safe stacks characterized by the assumption that coherent D-
modules are compact. In [DrG1, Section 10.2], the following conditions are shown to be equivalent:
• all coherentD-modules on X are compact,
• the object CX is compact, i.e., the functor Γ dR is continuous,
• the identity component of the automorphism group of any geometr ic point of X is unipotent.
1W e thank N. Rozenblyum for pointing out this follows from the adjunction (f∗ , f!) for proper maps together with
the identiﬁcation of f ! with the transpose of f∗ for arbitrary maps.
29
For example, any Deligne-Mumford stack is safe.
More generally, there is the relative notion of safe morphism f :X→Y of stacks characterized
by the assumption that f∗ is continuous. It guarantees familiar properties such as the proje ction
formula hold.
We will make repeated use of [DrG1, Corollary 8.3.4] which asserts th at for any stacks (in fact,
for any prestacks), external tensor product provides a natur al equivalence
⊠ :D(X)⊗D (Y ) ∼ /d47/d47D(X×Y )
There is a resulting symmetric monoidal structure on D(X) whose multiplication can be calcu-
lated locally with respect to smooth covers.
One can extend Verdier duality to D-modules on stacks by applying it locally, intertwining the
realizations of D-modules in terms of descent under !- and ∗-pullbacks. Moreover, Verdier duality
restricts to compact objects, where as in equation (1), it is chara cterized by a functorial equivalence
(2) Hom D(X)(DX (M), N)≃ HomD(X)(CX, M⊗ N) M, N∈D (X)cpt
Here as elsewhere we write D(X)cpt for the compact objects of D(X). Its continuous extension to
allD-modules provides a canonical self-duality
DX :D(X)′ ∼ /d47/d47D(X)
Note that equation (2) does not necessarily hold for arbitrary M, N∈D (X). The left hand side is
continuous in each, but CX∈D (X) may not be compact and hence the right hand side may not be
continuous.
