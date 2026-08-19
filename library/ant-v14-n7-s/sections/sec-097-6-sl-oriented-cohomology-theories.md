---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-097-6-sl-oriented-cohomology-theories
section_title: "SL-oriented cohomology theories"
section_number: 6
pages: 161-165
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Our ultimate goal is to apply the Gauss–Bonnet theorem of Section 5 when projective pushforwards are
deﬁned on a representable cohomology theory in some concrete manner, not necessarily relying on the
six-functor formalism. For this, we need a suitable axiomatization for such theories; we use a modiﬁcation
of the axioms of Panin and Smirnov [Panin 2003; 2009]. As before, our base-scheme B is a noetherian,
separated scheme of ﬁnite Krull dimension.
Deﬁnition 6.1. We let Sm-LB denote the category of triples(X, Z, L) with X in SmB, Z⊂ X a closed
subset and L→ X a line bundle. A morphism( f, ˜f):(X, Z, L)→(Y, W, M) is a morphism f: X→ Y
with Z⊃ f−1(W), together with an isomorphism of line bundles ˜f: L→ f∗M. We let Sm-Lpr
B denote
the category with the same objects as Sm-LB, but with morphisms ( f; ˜f):(X, Z, L)→(Y, W, M) a
proper morphism f: X→ Y in SmB, with f(Z)⊂ W, and ˜f: L→ f∗M an isomorphism of line bundles.
Deﬁnition 6.2. An SL-oriented cohomology theory on SmB consists of the following data:
(D1) A functor H∗,∗: Sm-Lop
B→ BiGrAb,(X, Z, L)↦→ H∗,∗
Z (X; L); we often write f∗ for H∗,∗( f, ˜f).
(D2) A functor H∗,∗: Sm-Lpr
B→ GrAb,(X, Z, L)↦→ H Z
∗,∗(X, L); we often write f∗ for H∗,∗( f, ˜f).
(D3) Natural isomorphisms, for X of dimension dX
H 2dX−n,dX−m
Z (X,ω X/B⊗ L) αX,Z,L
−−−→H Z
n,m(X, L).
(D4) An element 1∈ H 0,0
B (B; OB). For x:=(X, Z, L), y:=(Y, W, M) in Sm-LB, a bigraded cup
product map
∪x,y: H∗,∗
Z (X, L)⊗ H∗,∗
W (Y, M)→ H∗,∗
Z×W(X×B Y, p∗
1 L⊗ p∗
2 M)
1828 Marc Levine and Arpon Raksit
(D5) For Z⊂ W closed subsets of an X∈ SmB a bigraded boundary map
δ∗,∗
X,W,Z: H∗,∗
Z\W(X\ W; j∗
W L)→ H∗+1,∗
W (X, L)
We write H∗,∗(X, L) for H∗,∗
X (X, L) and H∗,∗
Z (X) for H∗,∗
Z (X, OX); we use the analogous notation
for H∗,∗. We write∪ for∪x,y andδ forδX,Z,L when the context makes the meaning clear.
For f: Y→ X a proper map of relative dimension d in SmB, with Z⊂ X, W⊂ Y closed subsets with
f(W)⊂ Z and L→ X a line bundle, combining (D2) and (D3) gives us pushforward maps
f∗: H∗,∗
W (Y,ω Y/B⊗ f∗L)→ H∗−2d,∗−d
Z (X,ω X/B⊗ L)
deﬁned as the composition
H∗,∗
W (Y,ω Y/B⊗ f∗L)
α−1
Y,W, f∗ L
−−−−→H W
2dY−∗,dY−∗(Y, f∗L)
f∗−→ H Z
2dY−∗,dY−∗(X, L) αX,Z,L−−−→H∗−2d,∗−d
Z (X,ω X/B⊗ L).
These data are required to satisfy the following axioms:
(A1) H∗,∗ and H∗,∗ are additive: H∗,∗ transforms disjoint unions to products andH∗,∗ transforms disjoint
unions to coproducts; in particular, H∗,∗
Z (∅, L)= 0 and H Z
∗,∗(∅, L)= 0.
(A2) Let
Y′
f′

g′
// Y
f

X′
g
// X
be a cartesian diagram in SchB, with X, Y, X′, Y′ in SmB (sometimes called a transverse cartesian
diagram in Sm B) and with f, f′ proper of relative dimension d. This gives us the isomorphism
f′∗ωX′/ X≃ωY′/Y.
Let Z⊂ X be a closed subset, let W⊂ Y be a closed subset with f(W)⊂ Z, let Z′= g−1(Z),
W′= g′−1(W). Let L→ X be a line bundle on X and let L′= g′∗(L). Then the diagram
H∗,∗
W′(Y′,ω Y′/B⊗ω−1
Y′/Y⊗ g′∗L′)
f′
∗

H∗,∗
W (Y,ω Y/B⊗ f∗L)
g′∗
oo
f∗

H∗−2d,∗−d
Z′ (X′,ω X′/B⊗ω−1
X′/ X⊗ L′) H∗−2d,∗−d
Z (X,ω X/B⊗ L)
g∗
oo
commutes.
Motivic Gauss–Bonnet formulas 1829
(A3) For Z⊂ W closed subsets of an X∈ SmB, let U= X\ Z with inclusion j: U→ X. For L→ X a
line bundle, this gives us the morphisms
(id, id):(X, W, L)→(X, Z, L) and ( j, id):(U, W\ Z, j∗L)→(X, W, L).
Then the sequence
··· δZ,W,X−−−→H∗,∗
Z (X, L)→ H∗,∗
W (X, L) j∗
→ H∗,∗
W\Z(U, j∗L) δZ,W,X−−−→H∗+1,∗
Z (X, L)→···
is exact. Moreover, the maps δZ,W,X are natural with respect to the pullback maps g∗ and the
proper pushforward maps f∗.
(A4) Let i: Y→ X be a closed immersion in SmB, let W⊂ Y be a closed subset, L→ X a line bundle.
Let Z= i(W), giving the morphism(i, id):(Y, W, i∗L)→(X, Z, L) in Sm-Lpr
B . Then
i∗: H W
∗,∗(Y, i∗L)→ H Z
∗,∗(X, L)
is an isomorphism.
(A5) The cup products∪ of (D4) are associative with unit 1. The maps f∗ and f∗ are compatible with
cup products: ( f× g)∗(α∪x,yβ)= f∗(α)∪x,y g∗(β). Moreover, using the isomorphisms of (D3),
the cup products induce products∪x,y on H∗,∗ and one has( f× g)∗(α∪x,yβ)= f∗(α)∪x,y g∗(β).
Finally, the boundary maps δZ,W,X are module morphism: retaining the notation of (D4), for
α∈ H∗,∗
Z\W(X\ W; j∗
W L) andβ∈ H∗,∗
T (Y, M), we have
δX×Y,Z×T,W×T(α∪β)=δX,Z,W(α)∪β.
(A6) Let i: Y→ X be a closed immersion in SmB of codimension c, πY: Y→ B the structure map.
Let 1H
Y ∈ H 0,0(Y) be the element π∗
Y(1). Then ϑ(i):=αX,Y(i∗(1H
Y))∈ H 2c,c
Y (X, det−1 Ni) is
central, that is, for each (U, T, M)∈ Sm-LB, and eachβ∈ H∗,∗
T (U, M), we have
τ∗(β∪ϑ(i))=ϑ(i)∪β
whereτ: X×B U→ U×B X is the symmetry isomorphism.
(A7) Let( f, id):(Y, W, f∗L)→(X, Z, L) be a morphism in Sm-LB. Suppose that the induced map
f: YW/B→ X Z/B is an isomorphism in SH(B). Then
f∗: H∗,∗
Z (X, L)→ H∗,∗
W (Y, f∗L)
is an isomorphism.
Remark 6.3. It may seem strange that the proper pushforward maps respect products in the sense of (A5);
one might rather expect a projection formula. However, (A5) asks that the proper pushforward maps
respect external products, not cup products, and in fact, having the pushforward and pullback maps
1830 Marc Levine and Arpon Raksit
respect products as in (A5) implies the projection formula, as one sees by considering the commutative
pentagon associated to a proper morphism f: Y→ X in SmB of relative dimension d:
Y
f

γ f:=( f×idX)◦1Y

1Y
// Y×B Y
f×idY %%
X×B Y
idX× fyy
X 1X
// X×B X
Note that the square
Y
γ f //
f

X×B Y
idX× f

X 1X
// X×B X
is transverse cartesian. If we have closed subsets Z⊂ X, W⊂ Y with f(W)⊂ Z, and line bundle L→ X,
the pentagon diagram induces the diagram in cohomology
H∗,∗
W (Y,ω Y/B⊗ f∗L)Y
f∗

H∗,∗
W×W(Y×B Y,ω Y/B⊗ f∗L)
1∗
Y
oo
H∗,∗
Z×W(X×B Y,ω Y/B⊠ L)
γ∗
f
ww
( f×idY)∗jj
(idX× f)∗uu
H∗−2d,∗−d
Z (X,ω X/B⊗ L) H∗−2d,∗−d
Z×Z (X×B X,ω X/B⊗ L)
1∗
X
oo
Takeα∈ H a,b
Z (X, M),β∈ H c,d
W (Y,ω Y/B⊗ f∗(L⊗ M−1)). By functoriality of (−)∗ and (A5) for(−)∗
we haveγ∗
f(α∪X,Yβ)= f∗(α)∪Yβ and by (A2) and (A5) for (−)∗ we have
f∗( f∗(α)∪Yβ)=1∗
X(idX× f)∗(α∪X,Yβ)=α∪X f∗(β).
Similarly, in the presence of (A2) and (A5) for (−)∗, functoriality for(−)∗ and(−)∗ and the projection
formula implies (A5) for(−)∗.
Motivic Gauss–Bonnet formulas 1831
Deﬁnition 6.4. A twisted cohomology theory on SmB is given by the data (D1), (D4), (D5) above,
satisfying the parts of the axioms (A1), (A3)–(A7) that only involve H∗,∗. Given an SL-oriented coho-
mology theory(H∗,∗, H∗,∗,...) on SmB, one has the underlying twisted cohomology theory (H∗,∗,...)
by forgetting the proper pushforward maps.
Example 6.5. The primary example of an SL-oriented cohomology theory on SmB is the one induced by
an SL-oriented motivic spectrum E∈ SH(B):
(X, Z, L)↦→ E∗,∗
Z (X; L).
One deﬁnes, for X∈ SmB of dimension dX over B,
E Z
m,n(X; L):= E2dX−m,dX−n
Z (X;ωX/B⊗ L);
we extend the deﬁnition to arbitrary X∈ SmB by taking the sum over the connected components of X
and write this also as E2dX−m,dX−n
Z (X;ωX/B⊗ L) by considering dX as a locally constant functor on X.
The pushforward maps for a proper morphism of relative dimension d, f: Y→ X, closed subsets
W⊂ Y, Z⊂ X with f(W)⊂ Z and line bundle L→ X are given by the pushforward
f∗: E2dY−m,2dY−n
W (Y;ωY/B⊗ f∗L)→ E2dX−m,2dX−n
Z (X;ωX/B⊗ L).
