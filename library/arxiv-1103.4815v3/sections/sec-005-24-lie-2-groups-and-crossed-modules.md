---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-005-24-lie-2-groups-and-crossed-modules
section_title: "Lie 2-Groups and crossed Modules"
section_number: 2.4
pages: 13-16
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
A (strict) Lie 2-group is a Lie groupoid Γ whose objects and morphisms are Lie groups, and
all of whose structure maps are Lie group homomorphisms. One can conveniently bundle the
multiplications and the inversions into smooth functors
m : Γ × Γ /d47/d47 Γ and i : Γ /d47/d47 Γ.
Example 2.4.1. ForA an abelian Lie group, the Lie groupoid BA from Example 2.1.1 (b) is a Lie
2-group. The condition that A is abelian is necessary.
Example 2.4.2. Let t : H /d47/d47 G be a homomorphism of Lie groups, and let G/ /Hbe the cor-
responding Lie groupoid from Example 2.1.1 (d). This Lie groupoid beco mes a Lie 2-group if the
following structure is given: a smooth left action of G onH by Lie group homomorphisms, denoted
(g,h ) ✤ /d47/d47 gh, satisfying
t(gh) = gt(h)g−1 and t(h)x =hxh−1
for all g ∈ G and h,x ∈ H. Indeed, the objects G of G/ /Halready form a Lie group, and the
multiplication on the morphisms H ×G of G/ /His the semi-direct product
(h2,g 2) · (h1,g 1) = (h2 g2h1,g 2g1). (2.4.1)
The homomorphism t : H /d47/d47 G together with the action of G on H is called a smooth crossed
module. Summarizing, every smooth crossed module deﬁnes a Lie 2-group.
Remark 2.4.3. Every Lie 2-group Γ can be obtained from a smooth crossed module. Indeed, one
putsG := Γ 0 andH := ker(s), equipped with the Lie group structures deﬁned by the multiplicatio n
functor m of Γ. The homomorphism t :H /d47/d47 G is the target map t : Γ 1 /d47/d47 Γ 0, and the action
of G on H is given by the formula gγ := idg ·γ · idg−1 for g ∈ Γ 0 and γ ∈ ker(s). These two
constructions are inverse to each other (up to canonical Lie grou p isomorphisms and strict Lie
2-group isomorphisms, respectively).
– 13 –
Example 2.4.4. Consider a connected Lie group H, so that its automorphism group Aut( H)
is again a Lie group [OV91]. Then, we have a smooth crossed module (Au t(H),H,i, ev), where
i :H /d47/d47 Aut(H) is the assignment of inner automorphisms to group elements, and e v : Aut(H) ×
H /d47/d47 H is the evaluation action. The associated Lie 2-group is denoted AUT( H) and is called
the automorphism 2-group of H.
Example 2.4.5. Let
1 /d47/d47H t /d47/d47G
p /d47/d47K /d47/d47 1
be an exact sequence of Lie groups, i.e. an exact sequence in which p is a submersion and t is an
embedding. The homomorphisms t :H /d47/d47 G andp :G /d47/d47 K deﬁne action groupoids G/ /Hand
K/ /Gas explained in Example 2.1.1. The ﬁrst one is even a Lie 2-group: the ac tion of G on H is
deﬁned by gh :=t−1(gt(h)g−1). This is well-deﬁned: since
p(gt(h)g−1) = p(g)p(t(h))p(g−1) = p(g)p(g)−1 = 1,
the element gt(h)g−1 lies in the image of t, and has a unique preimage. The action is smooth
because t is an embedding. The axioms of a crossed module are obviously satisﬁe d.
If a Lie groupoid Γ is a Lie 2-group in virtue of a multiplication functor m : Γ × Γ /d47/d47 Γ, then
the category BunΓ (M ) of principal Γ-bundles over a smooth manifold M is monoidal:
Deﬁnition 2.4.6. Let P : Mdis /d47/d47 Γ and Q : Mdis /d47/d47 Γ be principal Γ -bundles. The tensor
productP ⊗Q is the anafunctor
Mdis
diag /d47/d47Mdis ×Mdis
P ×Q /d47/d47 Γ × Γ m /d47/d47 Γ .
Example 2.4.7.
(a) Since trivial principal Γ-bundles If correspond to smooth functors f : Mdis /d47/d47 Γ (Example
2.3.3), it is clear that If ⊗ Ig = Ifg .
(b) Unwinding Deﬁnition 2.4.6 in the general case, the tensor produc t of two principal Γ-bundles
P1 and P2 with anchors α1 and α2, respectively, and actions ρ1 and ρ2, respectively, is given
by
P1 ⊗P2 = ((P1 ×M P2)m◦(α 1 ×α 2) ×t Γ 1)/ ∼ , (2.4.2)
where
(p1,p 2,m (γ1,γ 2) ◦γ) ∼ (ρ1(p1,γ 1),ρ 2(p2,γ 2),γ ) (2.4.3)
for all p1 ∈ P1, p2 ∈ P2 and morphisms γ,γ 1,γ 2 ∈ Γ 1 satisfying t(γi) = αi(pi) for i = 1, 2
and s(γ1)s(γ2) = t(γ). The bundle projection is ˜ π(p1,p 2,γ ) := π1(p1) = π2(p2), the anchor is
˜α(p1,p 2,γ ) := s(γ), and the Γ-action is given by ˜ ρ((p1,p 2,γ ),γ ′) := (p1,p 2,γ ◦γ′).
– 14 –
As a consequence of Lemma 2.3.9 and the fact that the composition o f anafunctors is associative
up to coherent transformations, we have
Proposition 2.4.8. ForM a smooth manifold and Γ a Lie 2-group, the tensor product
⊗ : BunΓ (M ) × BunΓ (M ) /d47/d47 BunΓ (M )
equips the groupoid of principal Γ -bundles over M with a monoidal structure. Moreover, it turns
the stack BunΓ into a monoidal stack.
Notice that the tensor unit of the monoidal groupoid BunΓ (M ) is the trivial principal Γ-bundle
I1 associated to the constant map 1 : M /d47/d47 Γ 0, or, in terms of anafunctors, the one associated to
the constant functor 1 : M /d47/d47 Γ.
A (weak) Lie 2-group homomorphism between Lie 2-groups (Γ,m Γ ) and (Ω,m Ω ) is an anafunctor
Λ : Γ /d47/d47 Ω together with a transformation
Γ × Γ
mΓ /d47/d47
Λ ×Λ
/d15/d15
Γ
Λ
/d15/d15
η ③③③③③
③③③③③
/d120/d0 ③③③③③③③③
Ω × Ω mΩ
/d47/d47 Ω
(2.4.4)
satisfying the evident coherence condition. Under the equivalence with smooth crossed modules
(Remark 2.4.3), Lie 2-group homomorphisms correspond to so-calle d butterﬂies [AN09]. A Lie 2-
group homomorphism is called weak equivalence, if the anafunctor Λ is a weak equivalence. Since
extensions and tensor products are both deﬁned via composition o f anafunctors, we immediately
obtain
Proposition 2.4.9. Extension along a Lie 2-group homomorphism Λ : Γ /d47/d47 Ω between Lie 2-
groups is a monoidal functor
Λ : BunΓ (M ) /d47/d47 BunΩ (M )
between monoidal categories. Moreover, these form a monoid al morphism between monoidal stacks.
Since a monoidal functor is an equivalence of monoidal categories if it is an equivalence of the
underlying categories, Corollary 2.3.12 implies:
Corollary 2.4.10. For Λ : Γ /d47/d47 Ω a weak equivalence between Lie 2-groups, the monoidal funct or
of Proposition 2.4.9 is an equivalence of monoidal categori es. Moreover, these form a monoidal
equivalence between monoidal stacks.
If we represent the Lie 2-group Γ by a smooth crossed module t : H /d47/d47 G as described in
Example 2.4.2, we want to determine explicitly what the tensor produc t looks like under the corres-
– 15 –
pondence of G/ /H-bundles and principal H-bundles with anti-equivariant maps to G, see Lemma
2.2.9.
Lemma 2.4.11. Lett :H /d47/d47 G be a crossed module and let P and Q beG/ /H-bundles over M .
Let (PH,f ) and (QH,g ) be the principal H-bundles together with their H-anti-equivariant maps
that belong to P and Q, respectively, under the equivalence of Lemma 2.2.9. Then, the principal
H-bundle that corresponds to the tensor product P ⊗Q is given by
(P ⊗Q)H =
(
P ×M Q
)
/ ∼ where (p⋆h,q ) ∼ (p,q⋆ (f (p)−1
h)).
The action of H on (P ⊗Q)H is [(p,q )]⋆h = [(p⋆h,q )], and the H-anti-equivariant map of (P ⊗Q)H
is [(p,q )] ✤ /d47/d47 f (p) ·g(q).
Similar to the tensor product of principal Γ-bundles, the dual P ∨ of a principal Γ-bundle P over
M is the extension of P along the inversion i : Γ /d47/d47 Γ of the 2-group, P ∨ :=i(P ). The equality
m ◦ (id,i ) = 1 of functors M /d47/d47 Γ induces a “death map” d : P ⊗P ∨ /d47/d47 I1. We are going to
use this bundle morphism in Section 5.2, but omit a further systematic al treatment of duals for the
sake of brevity.
