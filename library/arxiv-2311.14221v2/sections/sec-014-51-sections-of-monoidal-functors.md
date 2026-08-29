---
doc_id: arxiv-2311.14221v2
doc_title: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS"
section_id: sec-014-51-sections-of-monoidal-functors
section_title: "Sections of monoidal functors"
section_number: 5.1
pages: 22-24
source_pdf: 2311.14221v2.pdf
source_sha256: 5aa4126bbb6df6eb
doc_brief: "FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS — The main objective of the present paper is to present a ver- sion of the Tannaka-Krein type reconstruction Theorems: If F : B → C is an exact"
---
Deﬁnition 5.4. LetC,B be tensor categories. If F :B→C is a tensor
functor, a section to F is a right exact tensor functor G :C→B such that
F◦G≃ Id C as monoidal functors.
Example 5.5. (1) Any (linear) tensor functor F :B →vect k has a
canonical section given by
G : vect k→B,
G(V ) = V• 1.
Here the action • : vect k×B→B , is the one presented in ( 1.1).
(2) The previous example can be generalized to other kinds of ﬁber func-
tors. If C is a tensor category that acts on another tensor category B
then, any monoidal functor F :B→C that is also a C-module func-
tor has a section given by G :C→B ,G(V ) = V ⊲1. See Proposition
5.6 below.
(3) If (C,σ ) is a braided tensor category, and H∈C is a Hopf algebra
with unit given by u : 1→H, then the forgetful functor f : HC→C
has a section given by G :C→ HC, G(V ) = ( V,ρ t
V ). Here ρt
V =
u⊗id V is the trivial comodule structure.
(4) Let H be a Hopf algebra and R be a Hopf algebra in the category
of Yetter-Drinfeld modules H
HYD. Consider the corresponding Hopf
algebra obtained by bosonization R#H. Let us consider the functor
F : Rep(R#H)→ Rep(H), F (V ) = V.
The action of H onV is given by h·v = (1#h)·v. The functor F has
a section given by G : Rep(H)→ Rep(R#H) given by G(V ) = V ,
where the action of R#H on V is given by
(r#h)·v =ε(r)h·v.
(5) Let (C,σ ) be a braided tensor category. The forgetful functor from
the center of C, f : Z(C)→C , has a section given by the inclusion
C֒→Z(C), V ↦→(V,σ ).
Proposition 5.6. LetB,C be tensor categories, and (F,ξ ) : B→C be a
monoidal functor. The following notions are equivalent:
(i) The functor F has a section;
(ii)B is a right monoidal C-module category (in the sense of Deﬁnition
5.1) and F is a monoidal module functor.
Proof. Let us only give a sketch of the proof. (i) implies (ii): Assum e that
(G,ζ ) :C→B is a monoidal section to F . Let α :F◦G→ Id be a natural
monoidal isomorphism. Deﬁne the right action of C onB as
B⊳V :=B⊗G(V ),
FIBRE FUNCTORS AND RECONSTRUCTION OF HOPF ALGEBRAS 23
for any B∈B , V ∈C . The associativity of this action is given by
mB,V,W :B⊳ (V⊗W )→ (B⊳V )⊳W,
mB,V,W = id B⊗ζ −1
V,W,
for any B∈B , V,W ∈C . Turns out that B is a monoidal module category
with isomorphisms
lB,V :B⊳V →B⊗(1⊳V ),
lB,V = id B⊗G(V ).
With this action, F is a module functor. The module structure of the
functor F is given by
cB,V :F (B⊳V )→F (B)⊗V,
cB,V = (id F (B)⊗αV )ξ−1
B,G(V )F (lB,V ).
Since c1,V = αV , then it follows that Equation ( 5.5) is fulﬁlled, that is
(F,ξ,c ) is a monoidal module functor.
Let us prove now that (ii) implies (i): Assume that ( F,ξ,c ) :B→C is a
monoidalC-module functor. Deﬁne G :C→B , G(V ) = 1⊳V . Axiom ( 5.4)
implies that isomorphisms
l−1
1⊳V,W :G(V )⊗G(W )→G(V⊗W ),
endow G with the structure of monoidal functor. Deﬁne natural isomo r-
phisms αV : F (G(V )) = F (1⊳V )→ V , αV = c1,V . Let us check that
they are monoidal natural isomorphisms. For this, we need to verify that
equation
(5.6) ( c1,V⊗c1,W ) = c1,V ⊗WF (l−1
1⊳V,W )ξ1⊳V,1⊳W
is satisﬁed. Using that c satisﬁes diagram ( 2.18), it follows that the right
hand side of Equation ( 5.6) is equal to
= (c1,V⊗id W )c1⊳V,WF (l−1
1⊳V,W )ξ1⊳V,1⊳W
= (c1,V⊗id W )(id F (1⊳V )⊗c1,W )ξ−1
1⊳V,1⊳WF (l1⊳V,W )F (l−1
1⊳V,W )ξ1⊳V,1⊳W
= (c1,V⊗c1,W ).
The second equation follows from ( 5.5) □
Remark 5.7. Constructions in Proposition 5.6 are reciprocal in the following
sense. If B is a right monoidal C-module category and G :C→B is the
monoidal functorG(V ) = 1⊳V , then one can endowB with a rightC-module
structure
B ◭V =B⊗G(V ),
for any B∈B , V ∈C . Turns out, that the identity functor Id : ( B,⊳ )→
(B, ◭) is an equivalence of module categories.
24 LENTNER AND MOMBELLI
