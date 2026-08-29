---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-015-a-equivariant-anafunctors-and-group-actions
section_title: "A Equivariant Anafunctors and Group Actions"
section_number: null
pages: 57-59
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
In this section we are concerned with a Lie 2-group Γ and Lie groupoid s X and Y with actions
R1 : X × Γ /d47/d47 X and R2 : Y × Γ /d47/d47 Y.
Deﬁnition A.1. An action of the 2-group Γ on an anafunctor F : X /d47/d47 Y is an ordinary smooth
action ρ :F × Γ 1 /d47/d47 F of the group Γ 1 on the total space F that
(i) preserves the anchors in the sense that the diagrams
F × Γ 1
α l ×t
/d15/d15
ρ /d47/d47F
α l
/d15/d15
X0 × Γ 0 R1
/d47/d47 X0
and
F × Γ 1
ρ /d47/d47
α r ×s
/d15/d15
F
α r
/d15/d15
Y0 × Γ 0 R2
/d47/d47 Y0
are commutative.
(ii) is compatible with the Γ -actions in the sense that the identity
ρ(χ ◦f ◦η,γl ◦γ ◦γr) = R1(χ,γl) ◦ρ(f,γ ) ◦R2(η,γr)
holds for all appropriately composable χ ∈ X 1, η ∈ Y 1, f ∈ F , and γl,γ,γ r ∈ Γ 1.
– 57 –
If F1,F 2 : X /d47/d47 Y are anafunctors with Γ -action, a transformation η : F1 /d43/d51 F2 is called Γ -
equivariant if the map η :F1 /d47/d47 F2 between total spaces is Γ 1-equivariant in the ordinary sense.
Anafunctors X /d47/d47 Y with Γ-actions together with Γ-equivariant transformations form a
groupoid Ana∞
Γ (X, Y). On the other hand, there is another groupoid Γ- Ana∞(X, Y) consisting of
Γ-equivariant anafunctors (Deﬁnition 6.1.3) and Γ-equivariant tra nsformations (Deﬁnition 6.1.4).
Lemma A.2. The categories Ana∞
Γ (X, Y) and Γ -Ana∞(X, Y) are canonically isomorphic.
Proof. We construct a functor
E : Ana∞
Γ (X, Y) /d47/d47 Γ- Ana∞(X, Y). (A.1)
Let F : X /d47/d47 Y be an anafunctor with Γ-action ρ. We shall deﬁne a transformation
λρ :F ◦R1 /d43/d51 R2 ◦ (F × id).
First of all, the composite
X × Γ
R1 /d47/d47 X F /d47/d47 Y
is given by the total space ( X0 × Γ 0)R1 ×α l F , left and right anchors send an element ( x,g,f ) to
(x,g ) and αr(f ), respectively, and the actions are
(χ,γ ) ◦ (x,g,f ) = (t(χ),t (γ),R 1(χ,γ ) ◦f ) and ( x,g,f ) ◦η = (x,g,f ◦η).
On the other hand, the composite
X × Γ
F ×id /d47/d47 Y × Γ
R2 /d47/d47 Y
is given by the total space (( F × Γ 1)R2◦(α r ×s) ×t Y1)/ ∼ with the equivalence relation
(f ◦η′,γ ◦γ′,η ) ∼ (f,γ,R 2(η′,γ ′) ◦η).
The left and right anchors send an element ( f,γ,η ) to (αl(f ),t (γ)) and s(η), respectively, and the
actions are
(χ,γ ′) ◦ (f,γ,η ) = (χ ◦f,γ ′ ◦γ,η ) and ( f,γ,η ) ◦η′ = (f,γ,η ◦η′).
The inverse of the following map will deﬁne the transformation λ:
(F × Γ 1)R2◦(α r ×s) ×t Y1 /d47/d47 (X0 × Γ 0)R1 ×α lF : (f,γ,η ) ✤ /d47/d47 (αl(f ),t (γ),ρ (f,γ ) ◦η).
Condition (i) ensures that this map ends in the correct ﬁbre produc t, and condition (ii) assures that
it is well-deﬁned under the equivalence relation ∼. The left anchors are automatically respected,
and the right anchors require condition (i). Similarly, the left action is respected automatically,
– 58 –
and the right actions due to condition (ii). The axiom for a transform ation is satisﬁed because ρ
is a group action. This deﬁnes the functor E on objects. On morphisms, it is straightforward to
check that the conditions on both hand sides coincide; in particular, E is full and faithful.
In order to prove that the functor E is an isomorphism, we start with a given Γ-equivariant
structure λ on the anafunctor F . Then, an action ρ :F × Γ 1 /d47/d47 F is deﬁned by
(f,γ ) ✤ /d47/d47 pr3(λ−1(f,γ, idR2(α r (f ),s (γ ))))
with pr 3 : (X0 × Γ 0)R1 ×α lF /d47/d47 F the projection. The axiom for an action is satisﬁed due to the
identityλ obeys. It is straightforward to verify conditions (i) and (ii) of Deﬁn ition A.1. To close
the proof it suﬃces to notice that the two procedures we have deﬁ ned are (strictly) inverse to each
other. □
We are also concerned with the composition of anafunctors with Γ-a ction. Suppose that Z is a
third Lie groupoid with a Γ-action R3, and F : X /d47/d47 Y and G : Y /d47/d47 Z are anafunctors with
Γ-actions ρ :F × Γ 1 /d47/d47 F and τ :G × Γ 1 /d47/d47 G. Then, the composition G ◦F is equipped with
the Γ-action deﬁned by
(F ×Y0G) × Γ 1 /d47/d47 (F ×Y0G) : ((f,g ),γ ) ✤ /d47/d47 (ρ(f,γ ),τ (g, ids(γ ))). (A.2)
We leave it to the reader to check
Lemma A.3. Let X , Y and Z be Lie groupoids with Γ -actions R1, R2 and R3.
(a) Let F : X /d47/d47 Y andG : Y /d47/d47 Z be Γ -equivariant anafunctors. If Γ -equivariant structures on
F andG correspond to Γ 1-actions under the isomorphism of Lemma A.2, then the Γ -equivariant
structure on the composite F ◦G corresponds to the Γ 1-action deﬁned above.
(b) The isomorphism of Lemma A.2 identiﬁes the trivial Γ -equivariant structure on the identity
anafunctor id : X /d47/d47 X with the Γ 1-action R1 : X1 × Γ 1 /d47/d47 X1 on its total space X .
