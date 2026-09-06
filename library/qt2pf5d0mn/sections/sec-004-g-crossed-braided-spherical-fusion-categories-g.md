---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-004-g-crossed-braided-spherical-fusion-categories-g
section_title: "G-crossed Braided Spherical Fusion Categories (G-BSFC)"
section_number: null
pages: 32-36
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
doc_brief: "UC Santa Barbara — 18 sections: Abstract; Introduction; Higher Categories"
---
2.2 G-crossed Braided Spherical Fusion Categories
(G-BSFC)
G-BSFCs are the main ingredients we wish to introduce. In [47], they are called
G-equivariant fusion categories. Let ( C,⊗, 1,a,l,r ) be a tensor category and G be a
ﬁnite group. Recall in Section 2.1.1 that Aut⊗(C) is the monoidal category where objects
are auto tensor equivalences of C, morphisms are natural transformations, and tensor
product of two tensor equivalences are compositions of functors. Also recall that G is the
monoidal category where the objects are elements of G, the only morphism between two
elements is either the identity map if they are the same or none otherwise, and tensor
product is given by group multiplication.
Deﬁnition 2.2.1 A G-action onC is a monoidal functor (F,δ,ϵ ) :G−→Aut⊗(C).
The above deﬁnition is a highly concise way to describe a G-action. To be more
clear about it, we unpack the deﬁnition as follows. For g ∈ G,X ∈ C0,f ∈ C1,
F (g)(X),F (g)(f) are often written as Xg , fg , respectively, to indicate F is an action.
For each object g∈G0, i.e., g∈G, F (g) is an auto monoidal equivalence, and thus
it comes with natural isomorphisms:
γg;X,Y : ( X⊗Y )g −→ Xg ⊗ Yg , and σg : 1g −→1
These natural isomorphisms satisfy the axioms in Equations 2.3 2.4 2.5.
Since (F,δ,ϵ ) is a monoidal functor, there is a natural isomorphism δg,h :F (gh)−→
F (g)◦F (h) and a natural isomorphism ϵ :F (e)−→IdC. Or more speciﬁcally, for each
X∈C 0, there is an isomorphism δg,h;X : Xgh −→ ( Xh )
g
and ϵX : Xe −→X, such that
23
Section 2.2 G-crossed Braided Spherical Fusion Categories (G-BSFC)
the following diagrams commute:
Xgh ( Xh )
g
Ygh ( Yh )
g
δg,h;X
fgh ( fh )g
δg,h;Y
Xe X
Ye Y
ϵX
fe f
ϵY
(2.12)
(X⊗Y )gh ( (X⊗Y )h )
g
( Xh ⊗ Yh )
g
Xgh ⊗ Ygh ( Xh )
g
⊗ ( Yh )
g
δg,h;X⊗Y
γgh;X,Y
(γh;X,Y )g
γg; Xh , Yh
δg,h;X⊗δg,h;Y
(X⊗Y )e X⊗Y
Xe ⊗ Ye
ϵX⊗Y
γe;X,Y ϵX⊗ϵY
(2.13)
Xghk ( Xk )
gh
( Xhk )
g
( ( Xk )
h
)
g
δgh,k;X
δg,hk;X δg,h; Xk
(δh,k;X)g
(2.14)
Xge ( Xe )g
Xg
δg,e;X
I Xg
(ϵX)g
Xeg ( Xg )e
Xg
δe,g;X
I Xg
ϵ Xg (2.15)
Deﬁnition 2.2.2 A G-action on a strict monoidal category is strict if all the isomor-
phisms γg;X,Y,σg,δg,h;X,ϵX are identity maps.
AG-crossed braided spherical fusion category is a G-graded spherical fusion category
D = ⨁
g∈G
Cg together with a G-action and a family of natural isomorphisms {cX,Y :
X⊗Y−→ Yg ⊗X| X∈C g,Y ∈D} such that the following conditions are satisﬁed.
1. Each Cg is a full subcategory, and it is called the g-sector. There is only zero
morphism between two objects from diﬀerent sectors.
2.Cg⊗Cg′⊂C gg′.
24
Section 2.2 G-crossed Braided Spherical Fusion Categories (G-BSFC)
3. ( Cg′)g ⊂C gg′g−1.
4. The cX,Y ′s, called crossed braiding, are self consistent, namely, for X∈C g,Y ∈
Ch,Z ∈C k,
(X⊗Y )⊗Z
( Yg ⊗X)⊗Z X⊗ (Y⊗Z)
Yg ⊗ (X⊗Z) (Y⊗Z)g ⊗X
Yg ⊗ ( Zg ⊗X) ( Yg ⊗ Zg )⊗X
cX,Y⊗I αX,Y,Z
α Yg ,X,Z cX,Y⊗Z
I⊗cX,Z γg;Y,Z⊗I
α Yg , Zg ,X
(2.16)
( ( Xk )
h
⊗Y )⊗Z
(Y⊗ Xk )⊗Z ( Xhk ⊗Y )⊗Z
Y⊗ ( Xk ⊗Z) Xhk ⊗ (Y⊗Z)
Y⊗ (Z⊗X) (Y⊗Z)⊗X
c−1
Y, Xk ⊗I (δ−1
h,k;X⊗I)⊗I
αY, Xk ,Z α Xhk ,Y,Z
I⊗c−1
Z,X c−1
Y⊗Z,X
αY,Z,X
(2.17)
5. The G-action is consistent with the crossed braiding, namely, for X∈C g,Y ∈D ,
the diagram commutes:
(X⊗Y )g′
Xg′
⊗ Yg′
( Yg ⊗X)g′
( Yg )g′
⊗ Xg′
Yg′g ⊗ Xg′
( Yg′
)
g′g ¯g′
⊗ Xg′
(cX,Y )g′
γg′;X,Y
c Xg′ , Yg′
γg′; Yg ,X δ−1
g′,g;Y⊗I δg′g ¯g′,g′;Y⊗I
(2.18)
25
Section 2.2 G-crossed Braided Spherical Fusion Categories (G-BSFC)
B
Bg
A
A
B
B¯g
A
A
Figure 2.11: cA,B (Left) and c−1
A,B (Right) for A∈C g
Note that if G is trivial, then the deﬁnitions above are the same as those of spherical
braided fusion categories, so a {e}-crossed braided spherical fusion category is simply a
ribbon fusion category.
EveryG-BSFC is equivalent to a strict one as indicated the following theorem. Rough-
ly speaking, an equivalence of G-BSFCs is an equivalence as a monoidal functor and it
preserves all additional structures, e.g., crossed braiding, G-action, etc. For the rigorous
deﬁnition, see [48].
Theorem 2.2.3 [48] LetD be a G-BSFC, then there exist a strict G-BSFCD′ with a
strict G-action and an equivalence F :D−→D ′ of G-crossed braided categories.
Thus there is no loss of generality to restrict the study on strict G-BSFCs with strict
G-actions, which is the assumption for the rest of the paper. Namely, one can assume
that the αX,Y,Z,lX,rX,γg;X,Y,σg,δg,h;X,ϵX are identities.
Following [47], we can use the same picture for a regular braiding to represent the
G-crossed braiding as shown in Figure 2.11.
Similar to braided spherical fusion categories, here we can also deﬁne the twist θA :
A−→ Ag for g∈C A by the same picture:
The following proposition is parallel to the properties of the regular twist.
Proposition 2.2.4 [47] In a G-crossed braided spherical fusion category, the twist θ(·)
satisﬁes the following properties:
1. θA⊗B = (θ Agh¯g ⊗θ Bg )◦c Bg ,A◦cA,B, A∈C g,B∈C h;
26
