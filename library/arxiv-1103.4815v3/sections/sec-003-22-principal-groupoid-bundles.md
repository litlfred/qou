---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-003-22-principal-groupoid-bundles
section_title: "Principal Groupoid Bundles"
section_number: 2.2
pages: 6-9
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
We give the deﬁnition of a principal bundle in exactly the same way as we are going to deﬁne
principal 2-bundles in Section 6.
Deﬁnition 2.2.1. LetM be a smooth manifold, and let Γ be a Lie groupoid.
– 6 –
1. A principal Γ -bundle over M is a smooth manifold P with a surjective submersion π :
P /d47/d47 M and a right Γ -action (α,ρ ) that respects the projection π, such that
τ :P α ×t Γ 1 /d47/d47 P ×M P : (p,g ) ✤ /d47/d47 (p,ρ (p,g ))
is a diﬀeomorphism.
2. Let P1 and P2 be principal Γ -bundles over M . A morphism ϕ :P1 /d47/d47 P2 is a Γ -equivariant
smooth map that respects the projections to M .
Principal Γ-bundles over M form a category BunΓ (M ). In fact, this category is a groupoid, i.e.
all morphisms between principal Γ-bundles are invertible. There is an evident notion of a pullback
f ∗P of a principal Γ-bundle P overM along a smooth map f :X /d47/d47 M , and similarly, morphisms
between principal Γ-bundles pull back. These deﬁne a functor
f ∗ : BunΓ (M ) /d47/d47 BunΓ (X).
These functors make principal Γ-bundles a prestack over smooth manifolds. One can easily show
that this prestack is a stack (for the Grothendieck topology of su rjective submersions).
Example 2.2.2 (Ordinary principal bundles) . ForG a Lie group, we have an equality of categories
BunBG(M ) = BunG(M ),
i.e. Deﬁnition 2.2.1 reduces consistently to the deﬁnition of an ordinar y principal G-bundle.
Example 2.2.3 (Trivial principal groupoid bundles) . ForM a smooth manifold and f :M /d47/d47 Γ 0
a smooth map, P :=M f×t Γ 1 andπ(m,g ) := m deﬁne a surjective submersion, and α(m,g ) := s(g)
and ρ((m,g ),h ) := (m,g ◦h) deﬁne a right action of Γ on P that preserves the ﬁbers. The map τ
we have to look at has the inverse
τ −1 :P ×M P /d47/d47 P π ×t Γ 1 : ((m,g 1), (m,g 2)) ✤ /d47/d47 ((m,g 1),g −1
1 ◦g2),
which is smooth. Thus we have deﬁned a principal Γ-bundle, which we d enote by If and which we
call the trivial bundle for the map f . Any bundle that is isomorphic to a trivial bundle is called
trivializable.
Example 2.2.4 (Discrete structure groupoids) . ForX a smooth manifold, we have an equivalence
of categories
BunXdis(M ) ∼=C∞(M,X )dis.
Indeed, for a given principal Xdis-bundle P one observes that the anchor α : P /d47/d47 X descends
along the bundle projection to a smooth map f :M /d47/d47 X, and that isomorphic bundles determine
the same map. Conversely, one associates to a smooth map f :M /d47/d47 X the trivial principal Xdis-
bundle If overM .
– 7 –
Example 2.2.5 (Exact sequences) . Let
1 /d47/d47H t /d47/d47G
p /d47/d47K /d47/d47 1 (2.2.1)
be an exact sequence of Lie groups, and let Γ := G/ /Hbe the action groupoid associated to the Lie
group homomorphismt :H /d47/d47 G as explained in Example 2.1.1 (d). In this situation, p :G /d47/d47 K
is a surjective submersion, and
α :G /d47/d47 Γ 0 :g ✤ /d47/d47 g and ρ :Gα ×t Γ 1 /d47/d47 G : (g, (h,g ′)) ✤ /d47/d47 g′
deﬁne a smooth right action of Γ on G that preserves p. The inverse of the map τ is
τ −1 :G ×KG /d47/d47 Gα ×t Γ 1 : (g1,g 2) ✤ /d47/d47 (g1, (t−1(g1g−1
2 ),g 2)),
which is smooth because t is an embedding. Thus, G is a principal Γ-bundle over K.
Next we provide some elementary statements about trivial principa l Γ-bundles.
Lemma 2.2.6. A principal Γ -bundle over M is trivializable if and only if it has a smooth section.
Proof. A trivial bundle If has the section
sf :M /d47/d47 If :x ✤ /d47/d47 (x, idf (x));
and so any trivializable bundle has a section. Conversely, suppose a p rincipal Γ-bundle P has a
smooth section s :M /d47/d47 P . Then, with f :=α ◦s,
ϕ : If /d47/d47 P : (m,g ) ✤ /d47/d47 ρ(s(m),g )
is an isomorphism. □
The following consequence shows that principal Γ-bundles of Deﬁnit ion 2.2.1 are locally trivial-
izable in the usual sense.
Corollary 2.2.7. Let P be a principal Γ -bundle over M . Then, every point x ∈ M has an open
neighborhoodU over which P has a trivialization: a smooth map f : U /d47/d47 Γ 0 and a morphism
ϕ : If /d47/d47 P |U .
Proof. One can choose U such that the surjective submersion π :U /d47/d47 P has a smooth section.
Then, Lemma 2.2.6 applies to the restriction P |U . □
We determine the Hom-set Hom(If1, If2 ) between trivial principal Γ-bundles deﬁned by smooth
mapsf1,f 2 :M /d47/d47 Γ 0. To a bundle morphism ϕ : If1
/d47/d47 If2 one associates the smooth function
g :M /d47/d47 Γ 1 which is uniquely deﬁned by the condition
(ϕ ◦sf1 )(x) = sf2 (x) ◦g(x).
for all x ∈ M . It is straightforward to see that
– 8 –
Lemma 2.2.8. The above construction deﬁnes a bijection
Hom(If1, If2 ) /d47/d47 {g ∈ C∞(M, Γ 1) |s ◦g =f1 and t ◦g =f2} ,
under which identity morphisms correspond to constant maps and the composition of bundle mor-
phisms corresponds to the point-wise composition of functi ons.
Finally, we consider the case of principal bundles for action groupoid s.
Lemma 2.2.9. SupposeX/ /His a smooth action groupoid. The category BunX/ /H(M ) is equivalent
to a category with
• Objects: principal H-bundles PH over M together with a smooth, H-anti-equivariant map
f : PH /d47/d47 X, i.e. f (p ·h) = h−1f (p).
• Morphisms: bundle morphisms ϕH :PH /d47/d47 P ′
H that respect the maps f and f ′.
Proof. For a principal X/ /H-bundle (P,α,ρ ) we set PH :=P with the given projection to M . The
action of H on PH is deﬁned by
p⋆h :=ρ(p, (h,h −1 ·α(p))).
This action is smooth, and it follows from the axioms of the principal bu ndleP that it is principal.
The map f : PH /d47/d47 X is the anchor α. The remaining steps are straightforward and left as an
exercise. □
