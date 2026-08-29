---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-013-71-from-principal-2-bundles-to-bundle-gerbes
section_title: "From Principal 2-Bundles to Bundle Gerbes"
section_number: 7.1
pages: 39-48
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
In this section we deﬁne the 2-functor EM : 2-BunΓ (M ) /d47/d47 GrbΓ (M ).
Deﬁnition of EM on objects
Let P be a principal Γ-2-bundle over M , with projection π : P /d47/d47 M and right action R of Γ on
P. The ﬁrst ingredient of the Γ-bundle gerbe EM (P) is the surjective submersion π : P0 /d47/d47 M .
The second ingredient is a principal Γ-bundle P over P [2]
0 . We put
P := P1 × Γ 0.
Bundle projection, anchor and Γ-action are given, respectively, b y
χ(ρ,g ) := ( t(ρ),R (s(ρ),g −1)) , α(ρ,g ) := g and ( ρ,g ) ◦γ := (R(ρ, idg−1 ·γ),s (γ)).
(7.1.1)
These deﬁnitions are motivated by Remark 7.1.2 below.
Lemma 7.1.1. This deﬁnes a principal Γ -bundle over P [2]
0 .
Proof. First we check that χ :P /d47/d47 P [2]
0 is a surjective submersion. Since the functor τ = (id,R )
is a weak equivalence, we know from Theorem 2.3.13 that
f : (P0 × Γ 0)τ ×t ×t P [2]
1 /d47/d47 P [2]
0 : (p,g,ρ 1,ρ 2) ✤ /d47/d47 (s(ρ1),s (ρ2))
is a surjective submersion. Now consider the smooth surjective ma p
g : (P0 × Γ 0)τ ×t ×t P [2]
1 /d47/d47 P1 × Γ 0 : (p,g,ρ 1,ρ 2) ✤ /d47/d47 (ρ−1
1 ◦R(ρ2, idg−1 ),g −1).
We have χ ◦g = f ; thus, χ is a surjective submersion. Next we check that we have deﬁned an
action. Suppose ( ρ,g ) ∈ P and γ ∈ Γ 1 such that α(ρ,g ) = g = t(γ). Then, α((ρ,g ) ◦γ) = s(γ).
Moreover, suppose γ1,γ 2 ∈ Γ 1 with t(γ1) = g and t(γ2) = s(γ1). Then,
((ρ,g )◦γ1)◦γ2 = (R(ρ, idg−1 ·γ1),s (γ1))◦γ2 = (R(ρ, idg−1 ·γ1·ids(γ 1)−1 ·γ2),s (γ2)) = (ρ,g )◦(γ1◦γ2),
– 39 –
where we have used that γ1 ◦γ2 = γ1 · ids(γ 1)−1 ·γ2 in any 2-group. It remains to check that the
smooth map
˜τ :P α ×t Γ 1 /d47/d47 P χ ×χ P : ((ρ,g ),γ ) ✤ /d47/d47 ((ρ,g ), (ρ,g ) ◦γ)
is a diﬀeomorphism. For this purpose, we consider the diagram
P [2]
1
s×t
/d15/d15
(P0 × Γ 0) × (P0 × Γ 0) τ ×τ
/d47/d47 P [2]
0 × P [2]
0
(7.1.2)
and claim that (a) N1 := P α ×t Γ 1 is a pullback of (7.1.2), (b) N2 := P χ ×χ P is a pullback of
(7.1.2), and (c) the unique map N1 /d47/d47 N2 is ˜τ . Thus, ˜τ is a diﬀeomorphism.
In order to prove claim (a) we use again that the functor τ = (id,R ) is a weak equivalence, so
that by Theorem 2.3.13 the triple ( P1 × Γ 1,τ,s ×t) is a pullback of (7.1.2). We consider the smooth
map
ξ :N1 /d47/d47 P1 × Γ 1 : ((ρ,g ),γ ) ✤ /d47/d47 (R(ρ, idg−1 ),γ )
which is a diﬀeomorphism because (ρ,γ ) ✤ /d47/d47 ((R(ρ, idt(γ )),t (γ)),γ ) is a smooth map which is inverse
to ξ. Thus, putting f1 :=τ ◦ξ and g1 := (s ×t) ◦ξ we see that ( N1,f 1,g 1) is a pullback of (7.1.2).
In order to prove claim (b), we put
f2((ρ1,g 1), (ρ2,g 2)) := ( R(ρ1, idg−1
1
),ρ 2)
g2((ρ1,g 1), (ρ2,g 2)) := ( R(s(ρ),g −1
1 ),g 2,R (t(ρ1),g −1
1 ),g 1),
and it is straightforward to check that the cone ( N2,f 2,g 2) makes (7.1.2) commutative. The
triple ( N2,f 2,g 2) is also universal: in order to see this suppose N ′ is any smooth manifold
with smooth maps f ′ : N ′ /d47/d47 P [2]
1 and g′ : N ′ /d47/d47 (P0 × Γ 0) × (P0 × Γ 0) so that (7.1.2)
is commutative. For n ∈ N ′, we write f ′(n) = ( ρ1,ρ 2) and g′(n) = ( p1,g 1,p 2,g 2). Then,
σ(n) := ((R(ρ1, idg−1
2
),g 2), (ρ2,g 1)) deﬁnes a smooth map σ : N ′ /d47/d47 P χ ×χ P . One checks that
f2 ◦σ = f ′ and g2 ◦σ = g′, and that σ is the only smooth map satisfying these equations. This
proves that (N2,f 2,g 2) is a pullback. We are left with claim (c). Here one only has to check tha t
τ :N1 /d47/d47 N2 satisﬁes f2 =f1 ◦τ and g2 =g1 ◦τ . □
Remark 7.1.2. The smooth functor τ = (id,R ) : P × Γ /d47/d47 P ×M P is a weak equivalence, and
so has a canonical inverse anafunctor τ −1 (Remark 2.3.14). The anafunctor
P [2]
0
ι /d47/d47 P ×M P c /d47/d47 P ×M P τ −1
/d47/d47 P × Γ
pr2 /d47/d47 Γ,
wherec is the functor that switches the factors, corresponds to a princ ipal Γ-bundle over P [2]
0 that
is canonically isomorphic to the bundle P deﬁned above.
– 40 –
It remains to provide the bundle gerbe product
µ :π∗
23P ⊗π∗
12P /d47/d47 π∗
13P ,
which we deﬁne by the formula
µ((ρ23,g 23), (ρ12,g 12)) := (ρ12 ◦R(ρ23, idg12 ),g 23g12). (7.1.3)
Lemma 7.1.3. Formula (7.1.3) deﬁnes an associative isomorphism µ :π∗
23P ⊗π∗
12P /d47/d47 π∗
13P of
principal Γ -bundles over P [3]
0 .
Proof. First of all, we recall from Example 2.4.7 (b) that an element in t he tensor product
π∗
23P ⊗π∗
12P is represented by a triple (p23,p 12,γ ) where p23,p 12 ∈P withπ1(χ(p23)) = π2(χ(p12)),
andα(p23)·α(p12) = t(γ). In (7.1.3) we refer to triples where γ = idg23g12 , and this deﬁnition extends
to triples with general γ ∈ Γ 1 by employing the equivalence relation
(p1,p 2,γ ) ∼ (p1 ◦ (γ · idα (p2)−1 ),p 2, ids(γ )). (7.1.4)
The complete formula for µ is then
µ((ρ23,g 23), (ρ12,g 12),γ ) = (ρ12 ◦R(ρ23, idg−1
23
·γ),s (γ)). (7.1.5)
Next we check that (7.1.5) is well-deﬁned under the equivalence relat ion (7.1.4):
µ(((ρ23,g 23), (ρ12,g 12),γ )) = ( ρ12 ◦R(ρ23, idg−1
23
·γ),s (γ))
= ( ρ12 ◦R(ρ23 ◦R(idR(s(ρ 23),g −1
23 ),γ · idg−1
12
), idg12 ),s (γ))
= µ((ρ23 ◦R(idR(s(ρ 23),g −1
23 ),γ · idg−1
12
),s (γ)g−1
12 ), (ρ12,g 12), ids(γ )))
= µ(((ρ23,g 23) ◦ (γ · idg−1
12
), (ρ12,g 12), ids(γ ))).
Now we have shown that µ is a well-deﬁned map from π∗
23P ⊗π∗
12P toπ∗
13P , and it remains to prove
that it is a bundle morphism. Checking that it preserves ﬁbres and an chors is straightforward. It
remains to check that (7.1.5) preserves the Γ-action. We calculate
µ(((ρ23,g 23), (ρ12,g 12),γ ) ◦ ˜γ) = µ((ρ23,g 23), (ρ12,g 12),γ ◦ ˜γ)
= ( ρ23 ◦R(ρ12, idg12 ·i(γ ◦ ˜γ)),s (˜γ))
= ( ρ23 ◦R(R(ρ12, idg12 ),i (γ) ◦i(˜γ)),s (˜γ))
= ( ρ23 ◦R(R(ρ12, idg12 ),i (γ)) ◦R(idR(s(ρ 12),g ),i (˜γ)),s (˜γ))
= ( ρ23 ◦R(ρ12, idg12 ·i(γ)) ◦R(idR(s(ρ 12),g ),i (˜γ)),s (˜γ))
= ( ρ23 ◦R(ρ12, idg12 ·i(γ)),s (γ)) ◦ ˜γ
= µ((ρ23,g 23), (ρ12,g 12),γ ) ◦ ˜γ.
Summarizing, µ is a morphism of Γ-bundles over P [3]
0 . The associativity of µ follows directly from
the deﬁnitions. □
– 41 –
Deﬁnition of EM on 1-morphisms
We deﬁne a 1-morphism EM (F ) : EM (P) /d47/d47 EM (P ′) between Γ-bundle gerbes from a 1-morphism
F : P /d47/d47 P ′ between principal Γ-2-bundles. The reﬁnement of the surjective submersions π :
P /d47/d47 M and π′ : P ′ /d47/d47 M is the ﬁbre product Z := P0 ×M P ′
0. Its principal Γ-bundle has the
total space
Q :=F × Γ 0,
and its projection, anchor and Γ-action are given, respectively, b y
χ(f,g ) := (αl(f ),R (αr(f ),g −1)) , α(f,g ) := g and ( f,g ) ◦γ := (ρ(f, idg−1 ·γ),s (γ)),
(7.1.6)
where ρ : F × Γ 1 /d47/d47 F denotes the Γ 1-action on F that comes from the given Γ-equivariant
structure on F (see Appendix A).
Lemma 7.1.4. This deﬁnes a principal Γ -bundle Q over Z.
Proof. We show ﬁrst the the projection χ :Q /d47/d47 Z is a surjective submersion. Since the functor
τ ′ : P ′ × Γ /d47/d47 P ×M P is a weak equivalence, we have by Theorem 2.3.13 a pullback
X /d47/d47
ξ
/d15/d15
(P ′
0 × Γ 0)R ×t (P ′
1 ×M P ′
1)
s◦pr2
/d15/d15
F π ′◦α l(f ) ×π ′ P ′
0 /d47/d47 P ′
0 ×M P ′
0
along the bottom map ( f,p ′) ✤ /d47/d47 (αr(f ),p ′), which is well-deﬁned because the anafunctor F pre-
serves the projections to M (see Remark 6.1.6 (b)). In particular, the map ξ is a surjective sub-
mersion. It is easy to see that the smooth map
k :X /d47/d47 F × Γ 0 : ((f,p ′), (p′
0,g,ρ, ˜ρ)) ✤ /d47/d47 (f ◦ρ−1 ◦R(˜ρ, idg−1 ),g −1)
is surjective. Now we consider the commutative diagram
X
ξ
/d15/d15
k /d47/d47F × Γ 0
χ
/d15/d15
F π ′◦α l(f ) ×π ′ P0 α l ×id
/d47/d47 P0 ×M P ′
0.
The surjectivity of k and the fact that ξ andαl × id are surjective submersions shows that χ is one,
too.
– 42 –
Next, one checks (as in the proof of Lemma 7.1.1) that the Γ-action on Q deﬁned above is
well-deﬁned and preserves the projection. Then it remains to chec k that the smooth map
ξ : Qα ×t Γ 1 /d47/d47 Q ×P0 ×M P ′
0 Q : (f,g,γ ) ✤ /d47/d47 (f,g,ρ (f, idg−1 ·γ),s (γ))
is a diﬀeomorphism. An inverse map is given as follows. Given an element ( f1,g 1,f 2,g 2) on the
right hand side, we have αl(f1) = αl(f2), so that there exists a unique element ρ′ ∈ P ′
1 such
that f1 ◦ρ′ = f2. One calculates that ( ρ′,g 2) and (id α r(f1),g 1) are elements of the principal Γ-
bundle P ′ × Γ 0 over P ′[2]
0 of Lemma 7.1.1. Thus, there exists a unique element γ ∈ Γ 1 such that
(ρ′,g 2) = (idα r(f1),g 1) ◦γ. Clearly, t(γ) = g1 ands(γ) = g2, and we have ρ′ =R(idα r (f1), idg−1
1
·γ).
We deﬁne ξ−1(f1,g 1,f 2,g 2) := (f1,g 1,γ ). The calculation that ξ−1 is an inverse for ξ uses property
(ii) of Deﬁnition A.1 for the action ρ, and is left to the reader. □
The next step in the deﬁnition of the 1-morphism E (F ) is to deﬁne the bundle morphism
β :P ′ ⊗ζ∗
1Q /d47/d47 ζ∗
2Q ⊗P
overZ ×MZ. We use the notation of Example 2.4.7 (b) for elements of tensor pro ducts of principal
Γ-bundles; in this notation, the morphism β in the ﬁbre over a point (( p1,p ′
1), (p2,p ′
2)) ∈ Z ×M Z
is given by
β : ((ρ′,g ′), (f,g ),γ ) ✤ /d47/d47 (( ˜f,g ′gh), (˜ρ,h −1),γ ),
where h ∈ Γ 0 and ˜ρ ∈ P ′
1 are chosen such that s(˜ρ) = R(p2,h −1) and t(˜ρ) = p1, and
˜f :=ρ(˜ρ−1 ◦f ◦R(ρ′, idg), idh). (7.1.7)
Lemma 7.1.5. This deﬁnes an isomorphism between principal Γ -bundles.
Proof. The existence of choices of ˜ ρ,h follows because the functor τ ′ : P ′ × Γ /d47/d47 P ′ ×M P ′ is
smoothly essentially surjective (Theorem 2.3.13); in particular, one can choose them locally in a
smooth way. We claim that the equivalence relation on ζ∗
2Q ⊗P identiﬁes diﬀerent choices; thus, we
have a well-deﬁned smooth map. In order to prove this claim, we assu me other choices ˜ρ′,h ′. The
pairs (˜ρ,h −1) and (˜ρ′,h ′−1) are elements in the principal Γ-bundle P ′ over P ′
0 ×M P ′
0 and sit over
the same ﬁbre; thus, there exists a unique ˜ γ ∈ Γ 1 such that (˜ρ,h −1) ◦ ˜γ = (˜ρ′,h ′−1), in particular,
R(˜ρ, idh · ˜γ) = ˜ρ′. Now we have
(( ˜f,g ′gh), (˜ρ,h −1),γ ) = (( ˜f,g ′gh), (˜ρ,h −1), (idt(γ )·i(˜γ)·˜γ)◦γ) ∼ (( ˜f,g ′gh)◦(idt(γ )·i(˜γ)), (˜ρ,h −1)◦˜γ,γ )
so that it suﬃces to calculate
( ˜f,g ′gh) ◦ (idt(γ ) ·i(˜γ)) = ( ρ( ˜f, idh−1 ·i(˜γ)),g ′gh′)
= ( ρ(˜ρ−1 ◦f ◦R(ρ′, idg),i (˜γ)),g ′gh′)
= ( ρ(R(˜ρ−1,i (˜γ) · idh′−1 ) ◦f ◦R(ρ′, idg), idh′),g ′gh′),
– 43 –
where the last step uses the compatibility condition for ρ from Deﬁnition A.1 (ii). In any 2-group,
we have i(˜γ) · ids(˜γ ) = (idt(˜γ )−1 · ˜γ)−1, in which case the last line is exactly the formula (7.1.7) for
the pair (˜ρ′,h ′).
Next we check that β is well-deﬁned under the equivalence relation on the tensor product
P ′ ⊗ζ∗
1Q. We have
x := ((ρ′,g ′), (f,g ), (γ1 ·γ2) ◦γ) ∼ ((ρ′,g ′) ◦γ1, (f,g ) ◦γ2,γ ) =: x′
for γ1,γ 2 ∈ Γ 1 such that t(γ1) = g′, t(γ2) = g and s(γ1)s(γ2) = t(γ). Taking advantage of the fact
that we can make the same choice of (˜ ρ,h ) for both representatives x and x′, it is straightforward
to show that β(x) = β(x′). Finally, it is obvious from the deﬁnition of β that it is anchor-preserving
and Γ-equivariant. □
In order to show that the triple (Z,Q,β ) deﬁnes a 1-morphism between bundle gerbes, it remains
to verify that the bundle isomorphism β is compatible the with the bundle gerbe products µ1 and
µ2 in the sense of diagram (5.1.1). This is straightforward to do and left for the reader.
Deﬁnition of EM on 2-morphisms, compositors and unitors
Let F1,F 2 : P /d47/d47 P ′ be 1-morphisms between principal Γ-bundles over M , and let η : F /d43/d51 G
be a 2-morphism. Between the Γ-bundles Q1 andQ2, which live over the same common reﬁnement
Z = P0 ×M P ′
0, we ﬁnd immediately the smooth map
η :Q1 /d47/d47 Q2 : (f1,g ) ✤ /d47/d47 (η(f1),g )
which is easily veriﬁed to be a bundle morphism. Its compatibility with the bundle morphisms β1
andβ2 in the sense of the simpliﬁed diagram (5.1.4) is also easy to check. Thus , we have deﬁned a
2-morphism EM (η) : EM (F1) /d43/d51 EM (F2).
The compositor for 1-morphisms F1 : P /d47/d47 P ′ and F2 : P ′ /d47/d47 P ′′ is a bundle gerbe 2-
morphism
cF1,F 2 : EM (F2 ◦F1) /d47/d47 EM (F2) ◦ EM (F1).
Employing the above constructions, the 1-morphism EM (F2 ◦F1) is deﬁned on the common reﬁne-
mentZ12 := P0 ×M P ′′
0 and has the Γ-bundle Q12 = (F1 ×P ′
0F2)/P ′
1 × Γ 0, whereas the 1-morphism
EM (F2) ◦ EM (F1) is deﬁned on the common reﬁnement Z := P0 ×M P ′
0 ×M P ′′
0 and has the Γ-bundle
Q2 ⊗Q1 with Qk = Fk × Γ 0. The compositor cF1,F 2 is deﬁned over the reﬁnement Z with the
obvious reﬁnement maps pr 13 :Z /d47/d47 Z12 and id : Z /d47/d47 Z making diagram (5.1.3) commutative.
It is thus a bundle morphism cF1,F 2 : pr ∗
13Q12 /d47/d47 Q2 ⊗Q1. For elements in a tensor product of
Γ-bundles we use the notation of Example 2.4.7 (b). Then, we deﬁne cF1,F 2 by
((p,p ′,p ′′), (f1,f 2,g )) ✤ /d47/d47 ((ρ2(˜ρ−1 ◦f2, idh),gh ), (f1 ◦ ˜ρ,h −1), idg), (7.1.8)
– 44 –
whereh ∈ Γ 0 and ˜ρ :R(p′,h −1) /d47/d47 αr(f1) = αl(f2) are chosen in the same way as in the proof of
Lemma 7.1.5. The assignment (7.1.8) does not depend on the choices o fh and ˜ρ, nor on the choice
of the representative (f1,f 2) in (F1 ×P ′
0F2)/P ′
1. It is obvious that (7.1.8) is anchor-preserving, and
its Γ-equivariance can be seen by choosing (˜ ρ,h ) in order to compute cF1,F 2((p,p ′,p ′′), (f1,f 2,g ))
and (˜ρ′,h ) with ˜ρ′ := R(˜ρ, idg−1 ·γ−1) in order to compute cF1,F 2(((p,p ′,p ′′), (f1,f 2,g )) ◦γ). In
order to complete the construction of the bundle gerbe 2-morphis m cF1,F 2 we have to prove that
the bundle morphism cF1,F 2 is compatible with the isomorphisms β12 of EM (F2 ◦F1) and (id ⊗
β1) ◦ (β2 ⊗ id) of EM (F2) ◦ EM (F1) in the sense of diagram (5.1.4). We start with an element
((ρ′′,g ′′), (f12,g )) ∈ EM (P ′′) ⊗ζ∗
1Q12, where f12 = (f1,f 2). We have
β12((ρ′′,g ′′), (f12,g )) = ( ~f12,g ′′gh, ˜ρ,h −1)
upon choosing (˜ρ,h ) as required in the deﬁnition of EM (F2 ◦F1). Writing ~f12 = ( ˜f1, ˜f2) further we
have
(ζ∗
2cF1,F 2 ⊗ id)( ~f12,g ′′gh, ˜ρ,h −1) = (ρ2(˜ρ−1
2 ◦ ˜f2, idh2 ),g ′′ghh2, ˜f1 ◦ ˜ρ2,h −1
2 , ˜ρ,h −1) (7.1.9)
upon choosing appropriate (˜ρ2,h 2) as required in the deﬁnition of cF1,F 2. This is the result of the
clockwise composition of diagram (5.1.4). Counter-clockwise, we ﬁrs t get
(id ⊗ζ∗
1cF1,F 2)((ρ′′,g ′′), (f12,g )) = (ρ′′,g ′′,f ′′,gh 1,f ′,h −1
1 )
for choices (˜ρ1,h 1), where f ′′ :=ρ2(˜ρ−1
1 ◦f2, idh1) and f ′ :=f1 ◦ ˜ρ1. Next we apply the isomorphism
β2 of EM (F2) and get
(β2 ⊗ id)(ρ′′,g ′′,f ′′,gh 1,f ′
1,h −1
1 ) = ( ~f ′′,g ′′ghh2, ˆρ, ˆh−1,f ′
1,h −1
1 )
where we have used the choices (ˆρ, ˆh) deﬁned by ˆρ :=R(˜ρ−1
1 ,h 1) ◦R(˜ρ2,h −1h1) and ˆh :=h−1
1 hh2.
The last step is to apply the isomorphism β1 of EM (F2) which gives
(id ⊗β1)(~f ′′,g ′′ghh2, ˆρ, ˆh−1,f ′
1,h −1
1 ) = ( ~f ′′,g ′′ghh2, ~f ′,h −1
2 , ˜ρ,h −1), (7.1.10)
where we have used the choices (˜ρ,h ) from above. Comparing (7.1.9) and (7.1.10), we have obvious
coincidence in all but the ﬁrst and the third components. For these remaining factors, coincidence
follows from the deﬁnitions of the various variables.
Finally, we have to construct unitors. The unitor for a principal Γ-2 -bundle P over M is a
bundle gerbe 2-morphism
uP : EM (idP ) /d43/d51 idEM (P).
Abstractly, one can associate to id EM (P) the 1-morphism idFP
EM (P) constructed in the proof of Lemma
5.2.8, and then notice that id FP
EM (P) and EM (idP ) are canonically 2-isomorphic. In more concrete
terms, the unitor uP has the reﬁnement W := P [3]
0 with the surjective submersions r := pr 12
– 45 –
and r′ := pr 3 to the reﬁnements Z = P [2]
0 and Z ′ = P0 of the 1-morphisms EM (idP ) and id EM (P),
respectively. The relevant maps xW andyW are pr 13 and pr 23, respectively. The principal Γ-bundle
of the 1-morphism id EM (P) is the trivial bundle Q′ = I1. We claim that the principal Γ-bundle Q
of EM (idP ) is the bundle P of the bundle gerbe EM (P). Indeed, the formulae (7.1.6) reduce for the
identity anafunctor id P to those of (7.1.1). Now, the bundle isomorphism of the unitor uP is
y∗
WP ⊗r∗Q = pr ∗
23P ⊗ pr∗
12P
µ /d47/d47 pr∗
13P ∼=r′ ∗Q′ ⊗x∗
WP ,
whereµ is the bundle gerbe product of EM (P). The commutativity of diagram (5.1.2) follows from
the associativity of µ.
Proposition 7.1.6. The assignments EM for objects, 1-morphisms and 2-morphisms, together with
the compositors and unitors deﬁned above, deﬁne a 2-functor
EM : 2-BunΓ (M ) /d47/d47 GrbΓ (M ).
Proof. A list of axioms for a 2-functor with the same conventions as we use here can be found in
[SW, Appendix A]. The ﬁrst axiom requires that the 2-functor EM respects the vertical composition
of 2-morphisms – this follows immediately from the deﬁnition.
The second axiom requires that the compositors respect the horiz ontal composition of 2-
morphisms. To see this, let F1,F ′
1 : P /d47/d47 P ′ and F2,F ′
2 : P ′ /d47/d47 P ′′ be 1-morphisms between
principal Γ-2-bundles, and let η1 : F1 /d43/d51 F ′
1 and η2 : F2 /d43/d51 F ′
2 be 2-morphisms. Then, the
diagram
EM (F2 ◦F1)
cF1,F 2
/d11/d19
EM (η 1◦η 2) /d43/d51 EM (F ′
2 ◦F ′
1)
cF ′
1,F ′
2
/d11/d19
EM (F2) ◦ EM (F1)
EM (η 1)◦EM (η 2)
/d43/d51 EM (F ′
2) ◦ EM (F ′
1)
has to commute. Indeed, in order to compute cF1,F 2 and cF ′
1,F ′
2 one can make the same choice of
(˜ρ,h ), because the transformations η and η2 preserve the anchors. Then, commutativity follows
from the fact that η1 and η2 commute with the groupoid actions and the Γ 1-action according to
Deﬁnition A.1.
The third axiom describes the compatibility of the compositors with th e composition of 1-
morphisms in the sense that the diagram
EM (F3 ◦F2 ◦F1)
cF2◦F1,F 3 /d43/d51
cF3◦F2,F 1
/d11/d19
EM (F3) ◦ EM (F2 ◦F1)
id◦cF2,F 1
/d11/d19
EM (F3 ◦F2) ◦ EM (F1) cF3,F 2 ◦id
/d43/d51 EM (F3) ◦ EM (F2) ◦ EM (F1).
– 46 –
is commutative. In order to verify this, one starts with an element ( f1,f 2,f 3,g ) in EM (F3 ◦F2 ◦F1).
In order to go clockwise, one chooses pairs (˜ρ12, 3,h 12, 3) and (˜ρ1, 2,h 1, 2) and gets from the deﬁnitions
CW = ((ρ3(˜ρ−1
12, 3 ◦f3, idh12, 3 ),gh 12, 3), (ρ2(˜ρ−1
1, 2 ◦f2 ◦ ˜ρ12, 3, idh1, 2 ),h −1
12, 3h1, 2), (f1 ◦ ˜ρ1, 2,h −1
1, 2)).
Counter-clockwise, one can choose ﬁrstly again the pair (˜ ρ1, 2,h 1, 2) and then the pair (˜ ρ2, 3,h 2, 3)
with ˜ρ2, 3 = R(˜ρ12, 3, idh1, 2 ) and h2, 3 =h−1
1, 2h12, 3. Then, one gets
CCW = ((ρ3(˜ρ−1
2, 3◦ρ3(f3, idh1, 2 ), idh2, 3 ),gh 1, 2h2, 3), (ρ2(˜ρ−1
1, 2◦f2, idh1, 2)◦ ˜ρ2, 3,h −1
2, 3), (f1◦ ˜ρ1, 2,h −1
1, 2)),
where one has to use formula (A.2) for the Γ 1-action on the composition of equivariant anafunctors.
Using the deﬁnitions of h2, 3 and ˜ρ2, 3 as well as the axiom of Deﬁnition A.1 (ii) one can show that
CW = CCW.
The fourth and last axiom requires that compositors and unitors ar e compatible with each other
in the sense that for each 1-morphism F : P /d47/d47 P ′ the 2-morphisms
EM (F ) ∼= EM (F ◦ idP )
cidP ,F
/d43/d51 EM (F ) ◦ EM (idP )
id◦uP /d43/d51 EM (F ) ◦ idEM (P) ∼= EM (F )
and
EM (F ) ∼= EM (idP ′ ◦F )
cF, idP′
/d43/d51 EM (idP ′ ) ◦ EM (F )
uP′ ◦id /d43/d51 idEM (P ′) ◦ EM (F ) ∼= EM (F )
are the identity 2-morphisms. We prove this for the ﬁrst one and lea ve the second as an exercise.
Using the deﬁnitions, we see that the 2-morphism has the reﬁnemen tW := P0 ×M P0 ×M P ′
0 with
r = pr 13 and r′ = pr 23. The maps xW : W /d47/d47 P0 ×M P0 and yW : W /d47/d47 P ′
0 ×M P ′
0 are pr 12
and ∆ ◦ pr3, respectively, where ∆ is the diagonal map. Its bundle morphism is a m orphism
ϕ : pr ∗
13Q /d47/d47 pr∗
23Q ⊗ pr∗
12P ,
where Q =F × Γ 0 is the principal Γ-bundle of EM (F ), and P = P1 × Γ 0 is the principal Γ-bundle
of EM (P). Over a point ( p1,p 2,p ′) and (f,g ) ∈ pr∗
13Q, i.e. αl(f ) = p1 and R(αr(f ),g −1) = p′, the
bundle morphism ϕ is given by
(f,g ) ✤ /d47/d47 (ρ(˜ρ−1 ◦f, idh),gh, ˜ρ,h −1),
where h ∈ Γ 0, and ˜ρ ∈ P 1 with s(˜ρ) = R(p2,h −1) and t(˜ρ) = αl(f ). We have to compare ( W,ϕ )
with the identity 2-morphism of EM (F ), which has the reﬁnement Z with r = r′ = id and the
identity bundle morphism. According to the equivalence relation on bu ndle gerbe 2-morphisms we
have to evaluate ϕ over a point w ∈ W withr(w) = r′(w), i.e. w is of the form w = (p,p,p ′). Here
we can choose h = 1 and ˜ρ = idp, in which case we have ϕ(f,g ) = ((f,g ), (idp, 1)). This is indeed
the identity on Q. □
– 47 –
Properties of the 2-functor EM
For the proof of Theorem 7.1 we provide the following two statement s.
Lemma 7.1.7. The 2-functor EM is fully faithful on Hom-categories.
Proof. Let P, P ′ be principal Γ-2-bundles over M , and let F1,F 2 : P /d47/d47 P ′ be 1-morphisms. By
Lemma 5.2.8 every 2-morphism η : EM (F1) /d43/d51 EM (F2) can be represented by one whose reﬁnement
is P0 ×M P ′
0, so that its bundle isomorphism is η :Q1 /d47/d47 Q2, where Qk := Fk × Γ for k = 1, 2.
We can read oﬀ a map η :F1 /d47/d47 F2, and it is easy to see that this is a 2-morphism η :F1 /d43/d51 F2.
This procedure is clearly inverse to the 2-functor EM on 2-morphisms. □
Proposition 7.1.8. The 2-functors EM form a 1-morphism between pre-2-stacks.
Proof. For a smooth map f :M /d47/d47 N , we have to look at the diagram
2-BunΓ (N )
EN
/d15/d15
f ∗
/d47/d47 2-BunΓ (M )
EM
/d15/d15
GrbΓ (N )
f ∗
/d47/d47 GrbΓ (M )
of 2-functors. For P a principal Γ-2-bundle over N , the Γ-bundle gerbe EM (f ∗P) has the surjective
submersion pr 1 : Y := M ×N P0 /d47/d47 M , the principal Γ-bundle P := M ×N P1 × Γ 0 over
Y [2], and a bundle gerbe product µ deﬁned as in (7.1.3) that ignores the M -factor. On the other
hand, the Γ-bundle gerbe f ∗EN (P) has the same surjective submersion, and – up to canonical
identiﬁcations between ﬁbre products – the same Γ-bundle and the same bundle gerbe product.
These canonical identiﬁcations make up a pseudonatural transfo rmation that renders the above
diagram commutative. □
