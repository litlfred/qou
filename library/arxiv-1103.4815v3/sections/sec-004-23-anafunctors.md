---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-004-23-anafunctors
section_title: "Anafunctors"
section_number: 2.3
pages: 9-13
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
An anafunctor is a generalization of a smooth functor between Lie g roupoids, similar to a Morita
equivalence, and also known as a Hilsum-Skandalis morphism. The idea g oes back to Benabou
[B´ en73], also see [Joh77]. The references for the following deﬁnition s are [Ler, Met].
Deﬁnition 2.3.1. Let X and Y be Lie groupoids.
1. An anafunctor F : X /d47/d47 Y is a smooth manifold F , a left action (αl,ρl) of X on F , and
a right action (αr,ρr) of Y on F such that the actions commute and αl : F /d47/d47 X0 is a
principal Y-bundle over X0.
2. A transformation between anafunctors f :F /d43/d51 F ′ is a smooth map f :F /d47/d47 F ′ which is
X -equivariant, Y-equivariant, and satisﬁes α′
l ◦f =αl and α′
r ◦f =αr.
The smooth manifold F of an anafunctor is called its total space. Notice that the condition that
the two actions on F commute implies that each respects the anchor of the other. For ﬁ xed Lie
– 9 –
groupoids X and Y, anafunctors F : X /d47/d47 Y and transformations form a category Ana∞(X, Y).
Since transformations are in particular morphisms between principa l Y-bundles, every transforma-
tion is invertible so that Ana∞(X, Y) is in fact a groupoid.
Example 2.3.2 (Anafunctors from ordinary functors) . Given a smooth functor φ : X /d47/d47 Y, we
obtain an anafunctor in the following way. We set F := X0φ ×t Y1 with anchors αl :F /d47/d47 X0 and
αr :F /d47/d47 Y0 deﬁned by αl(x,g ) := x and αr(x,g ) := s(g), and actions
ρl : X1s ×α lF /d47/d47 F and ρr :F α r ×t Y1 /d47/d47 F
deﬁned by ρl(f, (x,g )) := (t(f ),φ (f ) ◦g) and ρr((x,g ),f ) := (x,g ◦f ). In the same way, a smooth
natural transformation η :φ /d43/d51 φ′ deﬁnes a transformation fη :F /d43/d51 F ′ byfη (x,g ) := (x,η (x) ◦
g). Conversely, one can show that an anafunctor comes from a smo oth functor, if its principal
Γ-bundle has a smooth section.
Example 2.3.3 (Anafunctors with discrete source) . For M a smooth manifold and Γ a Lie
groupoid, we have an equality of categories
BunΓ (M ) = Ana∞(Mdis, Γ).
Further, trivial principal Γ-bundles correspond to smooth functors. In particular, with Example
2.2.2 we have,
(a) For G a Lie group and M a smooth manifold, an anafunctor F :Mdis /d47/d47 BG is the same as
an ordinary principal G-bundle over M .
(b) For M and X smooth manifolds, an anafunctor F : Mdis /d47/d47 Xdis is the same as a smooth
map.
Example 2.3.4 (Anafunctors with discrete target). For Γ a Lie groupoid and M a smooth manifold,
we have an equivalence of categories
C∞(Γ 0,M )Γ
dis ∼= Ana∞(Γ,Mdis)
where C∞(Γ 0,M )Γ denotes the set of smooth maps f : Γ 0 /d47/d47 M such that f ◦s =f ◦t as maps
Γ 1 /d47/d47 M . The equivalence is induced by regarding a map f ∈ C∞(Γ 0,M )Γ as a smooth functor
f : Γ /d47/d47 Mdis, which in turn induces an anafunctor. Conversely, an anafunctor F : Γ /d47/d47 Mdis
is in particular an Mdis-bundle over Γ 0, which is nothing but a smooth function f : Γ 0 /d47/d47 M by
Example 2.2.4. The additional Γ-action assures the Γ-invariance of f .
Example 2.3.5 (Anafunctors between one-object Lie groupoids) . Let G and H be Lie groups,
and let BG and BH be the associated one-object Lie groupoids (Example 2.1.1 b). Then , there is
an equivalence of categories
Hom(G,H )/ /H∼= Ana∞(BG, BH),
– 10 –
where the action of H on Hom(G,H ) is by point-wise conjugation. The functor which establishes
this equivalence sends a smooth group homomorphism α :G /d47/d47 H to the evident smooth functor
Fα : BG /d47/d47 BH and converts this into an anafunctor (Example 2.3.2). A morphism h :α1 /d47/d47 α2
is sent to the natural transformation ηh :Fα 1
/d47/d47 Fα 2 whose component at the single object is the
morphism h ∈ H. In order to see that this is essentially surjective, it suﬃces to not ice that the
principal H-bundle of any smooth anafunctor F : BG /d47/d47 BH has a section. The proof that the
functor is full and faithful is straightforward.
For the following deﬁnition, we suppose X , Y and Z are Lie groupoids, and F : X /d47/d47 Y and
G : Y /d47/d47 Z are anafunctors given by F = (F,αl,ρl,αr,ρr) and G = (G,βl,τl,βr,τr).
Deﬁnition 2.3.6. The composition G ◦F : X /d47/d47 Z is the anafunctor deﬁned in the following
way:
1. Its total space is
E := (F α r ×β lG)/ ∼
where (f,τl(h,g )) ∼ (ρr(f,h ),g ) for all h ∈ Y 1 with αr(f ) = t(h) and βl(g) = s(h).
2. The anchors are (f,g ) ✤ /d47/d47 αl(f ) and (f,g ) ✤ /d47/d47 βr(g).
3. The actions X1s ×α E /d47/d47 E and Eβ ×t Z1 /d47/d47 E are given, respectively, by
(γ, (f,g )) ✤ /d47/d47 (ρl(γ,f ),g ) and ((f,g ),γ ) ✤ /d47/d47 (f,τr(g,γ )).
Remark 2.3.7. Lie groupoids, anafunctors and transformations form a bicatego ry. This bicategory
is equivalent to the bicategory of diﬀerentiable stacks (also known a s geometric stacks) [Pro96].
In this article, anafunctors serve two purposes. The ﬁrst is that one can use conveniently the
composition of anafunctors to deﬁne extensions of principal groupoid bundles:
Deﬁnition 2.3.8. If P : Mdis /d47/d47 Γ is a principal Γ -bundle over M , and Λ : Γ /d47/d47 Ω is an
anafunctor, then the principal Ω -bundle
ΛP := Λ ◦P :Mdis /d47/d47 Ω
is called the extension of P along Λ .
Unwinding this deﬁnition, the principal Ω-bundle Λ P has the total space
ΛP = (P α ×α l Λ) / ∼ (2.3.1)
where (p,ρl(γ,λ )) ∼ (ρ(p,γ ),λ ) for all p ∈P ,λ ∈ Λ and γ ∈ Γ 1 withα(p) = t(γ) and αl(λ) = s(γ).
Here α is the anchor and ρ is the action of P , and Λ = (Λ ,αl,αr,ρl,ρr). The bundle projection
– 11 –
is (p,λ ) ✤ /d47/d47 π(p), where π is the bundle projection of P , the anchor is ( p,λ ) ✤ /d47/d47 αr(λ), and the
action is (p,λ ) ◦ω = (p,ρr(λ,ω )).
Extensions of bundles are accompanied by extensions of bundle mor phisms. If ϕ :P1 /d47/d47 P2 is a
morphism between Γ-bundles, a morphism Λ ϕ : ΛP1 /d47/d47 ΛP2 is deﬁned by Λ ϕ(p1,λ ) := (ϕ(p1),λ )
in terms of (2.3.1). Summarizing, we have
Lemma 2.3.9. Let M be a smooth manifold and Λ : Γ /d47/d47 Ω be an anafunctor. Then, extension
along Λ is a functor
Λ : BunΓ (M ) /d47/d47 BunΩ (M ).
Moreover, it commutes with pullbacks and so extends to a morp hism between stacks.
Next we suppose that t :H /d47/d47 G is a Lie group homomorphism, and G/ /His the associated
action groupoid of Example 2.1.1 (d). We look at the functor Θ : G/ /H /d47/d47 BH which is deﬁned
by Θ( h,g ) := h. Combining Lemma 2.2.9 with the extension along Θ, we obtain
Lemma 2.3.10. The category BunG/ /H(M ) of principal G/ /H-bundles over a smooth manifold M
is equivalent to a category with
• Objects: principal H-bundles PH over M together with a section of Θ(PH ).
• Morphisms: morphisms ϕ of H-bundles so that Θ(ϕ) preserves the sections.
The second motivation for introducing anafunctors is that they pr ovide the inverses to certain
smooth functors which are not necessarily equivalences of catego ries.
Deﬁnition 2.3.11. A smooth functor or anafunctor F : X /d47/d47 Y is called a weak equivalence, if
there exists an anafunctor G : Y /d47/d47 X together with transformations G◦F ∼= idX andF ◦G ∼= idY .
We have the following immediate consequence for the stack morphism s of Lemma 2.3.9.
Corollary 2.3.12. Let Λ : Γ /d47/d47 Ω be a weak equivalence between Lie groupoids. Then, extensio n
of principal bundles along Λ is an equivalence Λ : BunΓ (M ) /d47/d47 BunΩ (M ) of categories. Moreover,
these deﬁne an equivalence between the stacks BunΓ and BunΩ .
Concerning the claimed generalization of invertibility, we have the following well-known theorem,
see [Ler, Lemma 3.34], [Met, Proposition 60].
Theorem 2.3.13. A smooth functor F : X /d47/d47 Y is a weak equivalence if and only if the following
two conditions are satisﬁed:
(a) it is smoothly essentially surjective: the map
s ◦ pr2 : X0F0 ×t Y1 /d47/d47 Y0
is a surjective submersion.
– 12 –
(b) it is smoothly fully faithful: the diagram
X1
F /d47/d47
s ×t
/d15/d15
Y1
s ×t
/d15/d15
X0 × X0 F ×F
/d47/d47 Y0 × Y0
is a pullback diagram.
Remark 2.3.14. One can show that any smooth functor F : X /d47/d47 Y that is a weak equivalence
actually has a canonical inverse anafunctor.
