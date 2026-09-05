---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-011-41-d-modules-on-schemes
section_title: "D-modules on schemes"
section_number: 4.1
pages: 27-29
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
[DrG1]. As explained in [DrG1], while this material is well-known at the level of triangulated
categories (standard references include Bernstein’s lecture not es [B] and the books by Borel [Bo] and
Kashiwara [K] forD-modules on varieties, and Bernstein-Lunts’ book [BL] and Beilinso n-Drinfeld’s
manuscript [BD, Chapters 1 and 7] for D-modules on stacks), no comprehensive account seems to
exist yet at the level of dg categories (though the aspects of the theory that concern pullbacks are
developed in [GR]).
4.1. D-modules on schemes. Throughout what follows, by a scheme, we will always mean a
quasi-compact, separated derived scheme over C.
To any scheme X, there is attached a dg category D(X) ofD-modules on X, deﬁned by taking
ind-coherent sheaves on the de Rham stack of X. The category D(X) is insensitive to the derived
or non-reduced structure of X, so one may assume X is a reduced classical scheme for concreteness.
When X is smooth, D(X) can be canonically identiﬁed with the traditional dg derived categor y of
rightDX -modules (as well as that of left DX -modules).
Given a map f :X→Y of schemes, there are continuous functors
f∗ :D(X) /d47/d47D(Y ) f ! :D(Y ) /d47/d47D(X).
They satisfy standard composition identities: given a sequence of m aps
X
f /d47/d47Y
g /d47/d47Z
there are canonical equivalences of functors ( gf )∗≃g∗f∗, (gf )!≃ f !g!. (See Remark 4.1 for more
on the functoriality of the assignment X↦→D(X).)
Note thatD(pt)≃ VectC. For the map π :X→pt, we set ωX :=π!C∈D (X), so that f !ωY ≃ωX
for any map f :X→Y . By deﬁnition, the functor of de Rham cohomology is given by pushfo rward
along π :X→pt which we denote by
Γ dR :=π∗ :D(X) /d47/d47D(pt)≃ VectC
It is representable by an object denoted by CX ∈ D(X) in the sense that there is a functorial
isomorphism
Γ dR(M)≃ HomD(X)(CX, M) M∈D (X)
For a map f :X→Y of schemes, the functors f !,f ∗ satisfy the following standard properties:
• Base change: given a Cartesian square
X×Y Z
˜g /d47/d47
˜f
/d15/d15
X
f
/d15/d15
Z
g /d47/d47Y
there is a canonical equivalence of functors
˜g∗ ˜f !≃f !g∗.
• Projection formula: there is a functorial equivalence
f∗(f !(N)⊗ M)≃f∗(M)⊗ N M ∈D (X), N∈D (Y )
• If f is proper, there is an adjunction ( f∗,f !), and so in particular, f∗ is quasi-proper.
27
• Iff is an open embedding, there is an adjunction ( f !,f ∗). More generally, if f is smooth, there
exists a functor
f ∗ :D(Y ) /d47/d47D(X)
along with an adjunction ( f ∗,f ∗) and canonical isomorphism
f ∗≃f ![−2(dimX− dimY )]
In particular f ∗,f ! are quasi-proper, and moreover, f ∗CY≃ CX .
• Kashiwara’s lemma: for i : Z→ X a closed embedding, i∗ induces an equivalence between
D(Z) and the full subcategory DZ(X)⊂D (X) ofD-modules on X vanishing on X\Z. The inverse
is given by the restriction of i!.
Remark 4.1. As explained in [FG, DrG1], a natural setting for a complete formulatio n of the
structure carried by the functors f !,f ∗ onD-modules is to consider the assignment X↦→D(X) as
a functor on the ∞-category of derived schemes with morphisms given by correspond ences. This
automatically encodes base change (as the composition law) as well a s the proper and smooth
adjunctions and all the relevant compatibilities.
4.2. Coherence, tensor product, and V erdier duality. AD-module on a scheme X is coherent
if its cohomology sheaves are locally ﬁnitely generated DX -modules. We denote by Dcoh(X)⊂D (X)
the full subcategory of coherent D-modules.
CoherentD-modules are precisely the compact objects of D(X) and also generate D(X), so there
is a canonical identiﬁcation
D(X)≃ IndDcoh(X)
Since f∗ for proper morphisms is quasi-proper, it preserves coherence, a nd similarly since f ∗,f !
for smooth morphisms are quasi-proper, they preserve coheren ce. Moreover, the canonical objects
ωX, CX∈D (X) are coherent.
External tensor product provides a natural equivalence
⊠ :D(X)⊗D (Y ) ∼ /d47/d47D(X×Y )
which restricts to an equivalence
⊠ :Dcoh(X)⊗D coh(Y ) ∼ /d47/d47Dcoh(X×Y )
There is a symmetric monoidal structure on D(X) with multiplication
⊗ :D(X)⊗D (X) ⊠ /d47/d47D(X×X) ∆ !
/d47/d47D(X)
where ∆ : X→X×X is the diagonal map. The unit is ωX∈D (X). The pullback f ! is symmetric
monoidal.
Recall from Section 2.1.2 that for a category C = IndCcpt, we denote byC♦
cpt the opposite category
ofCcpt, and that the category C′ = Ind(C♦
cpt) is dual to C.
Verdier duality is the unique involutive equivalence
DX :Dcoh(X)♦ ∼ /d47/d47Dcoh(X)
such that there is a functorial equivalence
(1) Hom D(X)(DX (M), N)≃ HomD(X)(CX, M⊗ N) M, N∈D coh(X)
Note that equation (1) holds for any N∈D (X) by continuity.
The continuous extension of Verdier duality to all D-modules provides a canonical self-duality
DX :D(X)′ ∼ /d47/d47D(X)
28
Note that equation (1) now holds for any M, N∈D (X) by continuity. In particular, equation (1)
presents the counit of the canonical self-duality in the form
D(X)⊗D (X) /d47/d47D(X) M⊗ N ✤ /d47/d47 Γ dR(M⊗ N)
For a smooth morphism f : X → Y , there is a canonical equivalence f ∗≃ DXf !DY , and in
particular, DX exchanges CX and ωX . For a proper morphism f : X→ Y , there is a canonical
equivalencef∗≃ DYf∗DX .1
