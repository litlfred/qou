---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-014-72-from-bundle-gerbes-to-principal-2-bundles
section_title: "From Bundle Gerbes to Principal 2-Bundles"
section_number: 7.2
pages: 48-57
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
We now provide the data we will feed into Lemma B.1 in order to produce a 2-functor
RM : GrbΓ (M ) /d47/d47 2-BunΓ (M ) that is inverse to the 2-functor EM constructed in the previous
section. These data are:
1. A principal Γ-2-bundle RG for each Γ-bundle gerbe G overM .
2. A 1-isomorphism AG : G /d47/d47 EM (RG) for each Γ-bundle gerbe G overM .
3. A 1-isomorphism RA : P /d47/d47 P ′ and a 2-isomorphism ηA : A /d43/d51 EM (RA) for all principal
Γ-2-bundles P, P ′ overM and all bundle gerbe 1-morphisms A : EM (P) /d47/d47 EM (P ′).
– 48 –
Construction of the principal Γ -2-bundle RG
We assume that G consists of a surjective submersion π : Y /d47/d47 M , a principal Γ-bundle P over
Y [2] and a bundle gerbe product µ. Let α :P /d47/d47 Γ 0 be the anchor of P , and let χ :P /d47/d47 Y [2]
be the bundle projection.
The Lie groupoid P of the principal 2-bundle RG is deﬁned by
P0 :=Y × Γ 0 and P1 :=P × Γ 0;
source map, target maps, and composition are given by, respectiv ely,
s(p,g ) := (π2(χ(p)),g ) , t(p,g ) := (π1(χ(p)),α (p)−1·g) and ( p2,g 2)◦(p1,g 1) := (µ(p1,p 2),g 1).
(7.2.1)
The identity morphism of an object ( y,g ) ∈ P 0 is (ty,g ) ∈ P 1, where ty denotes the unit element in
P over the point (y,y ), see Lemma 5.2.5. The inverse of a morphism ( p,g ) ∈ P 1 is (i(p),α (p)−1g),
where i : P /d47/d47 P is the map from Lemma 5.2.5. The bundle projection is π(y,g ) := π(y). The
action is given on objects and morphisms by
R0((y,g ),g ′) := (y,gg ′) and R1((p,g ),γ ) :=
(
p ◦
(
idg ·γ · idt(γ )−1g−1α (p)
)
,g ·s(γ)
)
. (7.2.2)
Lemma 7.2.1. This deﬁnes a functor R : P × Γ /d47/d47 P, and R is an action of Γ on P.
Proof. We assume that t : H /d47/d47 G is a smooth crossed module, and that Γ is the Lie 2-group
associated to it, see Example 2.4.2 and Remark 2.4.3. Then we use the c orrespondence between
principal Γ-bundles and principal H-bundles with H-anti-equivariant maps to G of Lemma 2.2.9.
Writingγ = (h,g ′), we have
R1((p,g ),γ ) = (p⋆ gh,gg ′).
With this simple formula at hand it is straightforward to show that R respects source and tar-
get maps and satisﬁes the axiom of an action. For the composition, w e assume composable
(p2,g 2), (p1,g 1) ∈ P 1, i.e. g2 =α(p1)−1g1, and composable ( h2,g ′
2), (h1,g ′
1) ∈ Γ 1, i.e. g′
2 =t(h1)g′
1.
Then we have
R((p2,g 2) ◦ (p1,g 1), (h2,g ′
2) ◦ (h1,g ′
1)) = R((µ(p1,p 2),g 1), (h2h1,g ′
1))
= ( µ(p1,p 2)⋆g1(h2h1),g 1g′
1)
= ( µ(p1⋆g1h2,p 2)⋆g1h1,g 1g′
1)
= ( µ(p1,p 2⋆g2h2)⋆g1h1,g 1g′
1)
= ( µ(p1⋆g1h1,p 2⋆g2h2),g 1g′
1)
= ( p2⋆g2h2,g 2g′
2) ◦ (p1⋆g1h1,g 1g′
1)
= R((p2,g 2), (h2,g ′
2)) ◦R((p1,g 1), (h1,g ′
1)),
– 49 –
ﬁnishing the proof. □
It is obvious that the action R preserves the projection π. Thus, in order to complete the
construction of the principal 2-bundle RG it remains to show that the functor τ = (pr 1,R ) is a
weak equivalence. This is the content of the following two lemmata in co nnection with Theorem
2.3.13.
Lemma 7.2.2. τ is smoothly essentially surjective.
Proof. The condition we have to check is whether or not the map
(Y × Γ 0 × Γ 0)τ ×t ((P × Γ 0) ×M (P × Γ 0))
(s×s)◦pr2 /d47/d47 (Y × Γ 0) ×M (Y × Γ 0)
is a surjective submersion. The left hand side is diﬀeomorphic to ( P × Γ 0)π 1 ×π 1 (P × Γ 0) via pr 2,
so that this is equivalent to checking that
s ×s : (P × Γ 0)π 1◦χ ×π 1◦χ (P × Γ 0) /d47/d47 (Y × Γ 0) ×M (Y × Γ 0)
is a surjective submersion. Since the Γ 0-factors are just spectators, this is in turn equivalent to
checking that
(π2 ×π2) ◦ (χ ×χ) : P π 1◦χ ×π 1◦χ P /d47/d47 Y [2]
is a surjective submersion. It ﬁts into the pullback diagram
P π 1◦χ ×π 1◦χ P /d31 /d127 /d47/d47
χ ×χ
/d15/d15
P ×P
χ ×χ
/d15/d15
Y [2]π 1 ×π 1Y [2]
π 2 ×π 2
/d15/d15
/d31 /d127 /d47/d47Y [2] ×Y [2]
π 2 ×π 2
/d15/d15
Y [2] /d31 /d127 /d47/d47Y ×Y
which has a surjective submersion on the right hand side; hence, als o the map on the left hand side
must be a surjective submersion. □
Lemma 7.2.3. τ is smoothly fully faithful.
Proof. We assume a smooth manifold N with two smooth maps
f :N /d47/d47 (P0 × Γ 0) × (P0 × Γ 0) and g :N /d47/d47 P1 ×M P1
– 50 –
such that the diagram
N
f
/d15/d15
g /d47/d47 P1 ×M P1
s×t
/d15/d15
(P0 × Γ 0) × (P0 × Γ 0) τ ×τ
/d47/d47 (P0 ×M P0) × (P0 ×M P0)
is commutative. For a ﬁxed point n ∈ N we put
((p1,g 1), (p2,g 2)) := g(n) ∈ (P × Γ 0) ×M (P × Γ 0)
and
((y,g, ˜g), (y′,g ′, ˜g′)) := f (n) ∈ (Y × Γ 0 × Γ 0) × (Y × Γ 0 × Γ 0).
The commutativity of the diagram implies χ(p1) = χ(p2) = ( y′,y ), so that there exists γ′ ∈ Γ 1
with p2 =p1 ◦γ′. We deﬁne γ := idg−1
1
·γ′ · idα (p2)−1g2 , which yields a morphism γ ∈ Γ 1 satisfying
τ (p1,g 1,γ ) = (p1,g 1,p 2,g 2) = g(n). On the other hand, we check that
(s(p1,g 1,γ ),t (p1,g 1,γ )) = (π2(p1),g 1,s (γ),π 1(p1),α (p1)−1g1,t (γ)) = f (n),
using that s(γ) = g−1
1 g2 and t(γ) = g−1
1 α(p1)α(p2)−1g2. Summarizing, we have deﬁned a smooth
map
σ :N /d47/d47 P1 × Γ 1 :n ✤ /d47/d47 (p1,g 1,γ )
such that τ ◦σ = g and (s ×t) ◦σ = f . Now let σ′ : N /d47/d47 P1 × Γ 1 be another such map, and
let σ′(n) =: ( p′
1,g ′
1,γ ′). The condition that τ (σ(n)) = g(n) = τ (σ′(n)) shows immediately that
p1 =p′
1 and g1 = g′
1, and then that p1 ◦γ = p1 ◦γ′. But since the Γ-action on P is principal, we
haveγ =γ′. This shows σ =σ′. Summarizing, P1 × Γ 1 is a pullback. □
Example 7.2.4. Suppose Γ = BU(1) (see Example 2.1.1 (b)) and suppose G is a Γ-bundle gerbe over
M , also known as a U(1)-bundle gerbe, see Example 5.1.7. Then, the as sociated principal BU(1)-
2-bundle RG has the groupoid P with P0 =Y and P1 =P , source and target maps s =π2 ◦χ and
t = π1 ◦χ, and composition p2 ◦p1 = µ(p1,p 2). The action of BU(1) on P is trivial on the level
of objects and the given U(1)-action on P on the level of morphisms. The same applies for general
abelian Lie groups A instead of U(1).
Construction of the 1-isomorphism AG : G /d47/d47 EM (RG)
The Γ-bundle gerbe EM (RG) has the surjective submersion ˜Y :=Y × Γ 0 with ˜π(y,g ) := π(y). The
total space of its Γ-bundle ˜P is ˜P := P × Γ 0 × Γ 0; it has the anchor α(p,g,h ) = h, the bundle
projection
˜χ : ˜P /d47/d47 ˜Y [2] : (p,g,h ) ✤ /d47/d47 ((π1(χ(p)),α (p)−1g), (π2(χ(p)),gh −1)),
– 51 –
the Γ-action is
(p,g,h ) ◦γ
(7.1.1)
= (( p,g ) ◦R((tπ 2(χ (p)),gh −1),γ ),s (γ))
(7.2.2)
= (( p,g ) ◦ (tπ 2(χ (p)) ◦ (idgh−1 ·γ · idg−1 ),gh −1s(γ)),s (γ))
(7.2.1)
= ( µ(tπ 2(χ (p)) ◦
(
idgh−1 ·γ · idg−1
)
,p ),gh −1s(γ),s (γ))
(2.4.3)
= ( p ◦
(
idgh−1 ·γ · idg−1α (p)
)
,gh −1s(γ),s (γ)),
and its bundle gerbe product ˜µ is given by
˜µ((p23,g 23,h 23), (p12,g 12,h 12))
(7.1.3)
= (( p12,g 12) ◦R((p23,g 23), idh12 ),h 23h12)
(7.2.2)
= (( p12,g 12) ◦ (p23,g 23h12),h 23h12)
(7.2.1)
= ( µ(p23,p 12),g 23h12,h 23h12).
In order to compare the bundle gerbes G and EM (RG) we consider the smooth maps σ :Y /d47/d47 Y ×Γ 0
and ˜σ :P /d47/d47 ˜P that are deﬁned by σ(y) := (y, 1) and ˜σ(p) := (p,α (p),α (p)).
Lemma 7.2.5. ˜σ deﬁnes an isomorphism ˜σ :P /d47/d47 (σ ×σ)∗ ˜P of Γ -bundles over Y [2]. Moreover,
the diagram
π∗
23P ⊗π∗
12P
µ
/d15/d15
˜σ ⊗˜σ /d47/d47 ˜π∗
23 ˜P ⊗ ˜π∗
12 ˜P
˜µ
/d15/d15
π∗
13P ˜σ
/d47/d47 ˜π∗
13 ˜P
is commutative.
Proof. For the ﬁrst part it suﬃces to prove that ˜ σ is Γ-equivariant, preserves the anchors, and that
the diagram
P
χ
/d15/d15
˜σ /d47/d47 ˜P
˜χ
/d15/d15
Y [2]
σ ×σ
/d47/d47 ˜Y [2]
is commutative. Indeed, the commutativity of the diagram is obvious , and also that the anchors
are preserved. For the Γ-equivariance, we have
˜σ(p ◦γ) = (p ◦γ,s (γ),s (γ)) = (p,α (p),α (p)) ◦γ = ˜σ(p) ◦γ.
Finally, we calculate
˜µ((p23,α (p23),α (p23)), (p12,α (p12),α (p12))) = ( µ(p23,p 12),α (p23)α(p12),α (p23)α(p12))
= ( µ(p23,p 12),α (µ(p23,p 12)),α (µ(p23,p 12)))
– 52 –
which shows the commutativity of the diagram. □
Via Lemma 5.2.7 the bundle morphism ˜σ deﬁnes the required 1-morphism AG, and Lemma 5.2.3
guarantees that AG is a 1- isomorphism.
Construction of the 1-morphism RA : P /d47/d47 P ′
Let A : EM (P) /d47/d47 EM (P ′) be a 1-morphism between Γ-bundle gerbes obtained from principal
Γ-2-bundles P and P ′ over M . By Lemma 5.2.8 we can assume that A consists of a principal
Γ-bundle χ :Q /d47/d47 Z withZ = P0 ×M P ′
0, and some isomorphism β overZ [2]. For preparation, we
consider the ﬁbre products Zr := P0 ×M P ′[2]
0 and Zl := P [2]
0 ×M P ′
0 with the obvious embeddings
ιl :Zl /d47/d47 Z andιr :Zr /d47/d47 Z obtained by doubling elements. Together with the trivialization of
Corollary 5.2.6, the pullbacks of β along ιl and ιr yield bundle morphisms
βl :=ι∗
lβ : pr ∗
13Q /d47/d47 pr∗
23Q ⊗ pr∗
12P and βr :=ι∗
rβ : pr ∗
23P ′ ⊗ pr∗
12Q /d47/d47 pr∗
13Q,
where P := P1 × Γ 0 and P ′ := P ′ × Γ 0 are the principal Γ-bundles of the Γ-bundle gerbes EM (P)
and EM (P ′), respectively.
Lemma 7.2.6. The bundle morphisms βl and βr have the following properties:
(i) They commute with each other in these sense that the diagr am
P ′
p′
1,p ′
2
⊗Qp1,p ′
1
β❘❘❘❘❘❘❘❘❘
/d41/d41❘❘❘❘❘❘❘❘❘❘❘
β r /d47/d47
id ⊗β l
/d15/d15
Qp1,p ′
2
β l
/d15/d15
P ′
p′
1,p ′
2
⊗Qp2,p ′
1 ⊗Pp1,p 2 β r ⊗id
/d47/d47Qp2,p ′
2 ⊗Pp1,p 2
is commutative for all ((p1,p ′
1), (p2,p ′
2)) ∈ Z [2].
(ii) βl is compatible with the bundle gerbe product µ in the sense that
βl|p1,p 3,p ′ = (id ⊗µp1,p 2,p 3) ◦ (βl|p2,p 3,p ′ ⊗ id) ◦βl|p1,p 2,p ′
for all (p1,p 2,p 3,p ′) ∈ P [3]
0 ×M P ′
0.
(iii) βr is compatible with the bundle gerbe product µ′ in the sense that
βr|p,p ′
1,p ′
3 ◦ (µ′
p′
1,p ′
2,p ′
3
⊗ id) = βr|p,p ′
2,p ′
3 ◦ (id ⊗βr|p,p ′
1,p ′
2)
for all (p,p ′
1,p ′
2,p ′
3) ∈ P 0 ×M P ′[3]
0 .
– 53 –
Proof. The identities (ii) and (iii) follow by restricting the commutative diagram (5.1.1) to the
submanifolds P [3]
0 ×M P ′
0 and P0 ×M P ′[3]
0 of Z [3], respectively. Similarly, the commutativity of
the two triangular subdiagrams in (i) follows by restricting (5.1.1) alon g appropriate embeddings
Z [2] /d47/d47 Z [3]. □
Now we are in position to deﬁne the anafunctor RA. First, we consider the left action
β0 : Γ 0 ×Q /d47/d47 Q : (g,q ) ✤ /d47/d47 βr((id,g ),q )
that satisﬁes α(β0(g,q )) = gα(q). The action β0 is properly discontinuous and free because βr is a
bundle isomorphism. The quotient F :=Q/Γ 0 is the total space of the anafunctor RA we want to
construct. Left and right anchors of an element q ∈ F with χ(q) = (p,p ′) are given by
αl(q) := p and αr(q) := R(p′,α (q)).
The actions are deﬁned by
ρl(ρ,q ) := β−1
l (q, (ρ, 1)) and ρr(q,ρ ′) := βr((R(ρ′, idα (q)−1 ), 1),q ).
The left action is invariant under the action β0 because of Lemma 7.2.6 (i). For the right action,
invariance follows from Lemma 7.2.6 (ii) and the identity
µ′((R(ρ′, idα (q)−1g−1 ), 1), (id,g ))
(7.1.3)
= µ′((id,g ), (R(ρ′, idα (q)−1 ), 1)).
Lemma 7.2.7. The above formulas deﬁne an anafunctor F : P /d47/d47 P ′.
Proof. The compatibility between anchors and actions is easy to che ck. The axiom for the actions
ρl andρr follows from Lemma 7.2.6 (ii) and (iii). Lemma 7.2.6 (i) shows that the actio ns commute.
It remains to prove that αl : F /d47/d47 P0 is a principal P ′-bundle. Since αl is a composition of
surjective submersions, we only have to show that the map
τ :F α r ×t P ′ /d47/d47 F α l ×α l F : (q,ρ ′) ✤ /d47/d47 (q,ρr(q,ρ ′))
is a diﬀeomorphism. We construct an inverse map τ −1 as follows. For ( q1,q 2) with χ(q1) = (p,p ′)
and χ(q2) = (p, ˜p′), choose a representative
((˜ρ′,g ′), ˜q) := βr|−1
p,p ′, ˜p′(q2).
Such choices can be made locally in a smooth way, and the result will not depend on them. We
haveχ(˜q) = (p,p ′) that that there exists a unique γ ∈ Γ 1 such that q1 = ˜q ◦γ. Now we put
τ −1(q1,q 2) := (q1,R (˜ρ′,γ −1)).
– 54 –
The calculation of τ −1 ◦τ is straightforward. For the calculation of ( τ ◦τ −1)(q1,q 2) we have to
compute in the second component
βr((R(˜ρ′,γ −1 · idα (q1)−1 ), 1),q 1) = βr((R(˜ρ′,γ −1 · idα (q1)−1 ), 1) ◦ (γ · idα (˜q)−1), ˜q)
= βr((˜ρ′,α (q1)α(˜q)−1), ˜q)
= β0(α(q1)α(˜q)−1g′−1,βr((˜ρ′,g ′), ˜q))
= β0(α(q1)α(˜q)−1g′−1,q 2),
and this is equivalent to q2. □
In order to promote the anafunctor F to a 1-morphism between principal 2-bundles, we have
to do two things: we have to check that F commutes with the projections of the bundle P1 and
P2, and we have to construct a Γ-equivariant structure on F . For the ﬁrst point we use Remark
6.1.6 (b), whose criterion π ◦αl = π ◦αr is clearly satisﬁed. For the second point we provide a
smooth action ρ :F × Γ 1 /d47/d47 F in the sense of Deﬁnition A.1 and use Lemma A.2, which provides
a construction of a Γ-equivariant structure. The action is deﬁned by
ρ(q,γ ) := β−1
l (q ◦ (idα (q) ·γ · idt(γ )−1), (idR(α l(q),t (γ )),t (γ))). (7.2.3)
Lemma 7.2.8. This deﬁnes a smooth action of Γ 1 on F in the sense of Deﬁnition A.1.
Proof. Smoothness is clear from the deﬁnition. The identity
ρ(ρ(q,γ 1),γ 2) = β−1
l (q ◦ (idα (q) ·γ1 ·γ2 · idt(γ 2)−1t(γ 1)−1), (id,t (γ1 ·γ2))) = ρ(q,γ 1 ·γ2)
follows from the deﬁnition and the two identities
α(ρ(q,γ )) = α(q)s(γ) and ( γ1·idt(γ 1)−1)·(ids(γ 1)·γ2·idt(γ 2)−1t(γ 1)−1) = γ1·γ2·idt(γ 2)−1t(γ 1)−1 .
(7.2.4)
The latter can easily be veriﬁed upon substituting a crossed module f or Γ. Checking condition (i)
of Deﬁnition A.1 just uses the deﬁnitions. We check condition (ii) in two steps. First we prove the
identity
ρ(ρl(ρ,q ),γl ◦γ) = ρl(R(ρ,γl),ρ (q,γ )).
The main ingredient is the decomposition
idα (q) · (γl ◦γ) · idt(γ l)−1 = (idα (q) ·γ · idt(γ )−1) ◦ (idα (q)s(γ )t(γ )−1 ·γl · idt(γ l)−1 ) (7.2.5)
that can e.g. be veriﬁed in the crossed module language. Now we comp ute
ρ(ρl(ρ,q ),γl ◦γ) = β−1
l (q ◦ (idα (q) · (γl ◦γ) · idt(γ l)−1 ), (R(ρ,t (γl)),t (γl)))
(7.2.5)
= β−1
l (q ◦ (idα (q) ·γ · idt(γ )−1), (R(ρ,γl),t (γl)))
= ρl(R(ρ,γl),ρ (q,γ )).
– 55 –
The second step is to show the identity
ρ(ρr(q,ρ ′),γ ◦γr) = ρr(ρ(q,γ ),R (ρ′,γr)).
Here we use the decomposition
idα (q) · (γ ◦γr) · idt(γ )−1 = (idα (q) ·γ · idt(γ )−1) ◦ (idα (q) ·γr · idt(γ )−1). (7.2.6)
Then we compute
ρ(ρr(q,ρ ′),γ ◦γr)
= β−1
l (βr((R(ρ′, idα (q)−1 ), 1),q ◦ (idα (q) · (γ ◦γr) · idt(γ )−1)), (id,t (γ)))
(7.2.6)
= β−1
l (βr((R(ρ′,γr · ids(γ )−1α (q)−1 ), 1),
β0(α(q)s(γr)s(γ)−1α(q)−1,q ◦ (idα (q) ·γ · idt(γ )−1))), (id,t (γ)))
(7.2.4)
= β−1
l (βr((R(ρ′,γr · idα (ρ(q,γ ))−1 )),q ◦ (idα (q) ·γ · idt(γ )−1)), (id,t (γ)))
= ρr(ρ(q,γ ),R (ρ′,γr)),
where we have employed the equivalence relation on F that was generated by the action of β0. □
Construction of a 2-isomorphism ηA : A /d43/d51 EM (RA)
We may again assume that the common reﬁnement of A is the ﬁbre product P0 ×M P ′
0; otherwise,
the proof of Lemma 5.2.8 provides a 2-isomorphism between A and one of these. Now, A and
EM (RA) have the same common reﬁnement, and ηA is given by the map
η :Q /d47/d47 F × Γ 0 :q ✤ /d47/d47 (q,α (q)).
This is obviously smooth and respects the projections to the base: if χ(q) = (p,p ′), then
χ(q,α (q))
(7.1.6)
= ( αl(q),R (αr(q),α (q)−1)) = (p,p ′).
Further, it respects the Γ-actions:
η(q ◦γ) = (q ◦γ,s (γ)) = β−1
l (q ◦γ, (id, 1))
(7.2.3)
= ( ρ(q, idα (q)−1 ·γ),s (γ))
(7.1.6)
= η(q) ◦γ,
so thatη is a bundle morphism. It remains to verify the commutativity of the co mpatibility diagram
(5.1.4). Let ((ρ′,g ′),q ′) ∈P ′⊗ζ∗
1Q, and let (q, (ρ,g )) ∈ζ∗
2Q⊗P be a representative for β((ρ′,g ′),q ′).
In particular, we have α(q)g =g′α(q′), since βr is anchor-preserving. Then, we get clockwise
(η ⊗ id)(β((ρ′,g ′),q ′)) = ((q,α (q)), (ρ,g )). (7.2.7)
– 56 –
Counter-clockwise, we have to use the isomorphism of Lemma 7.1.5 th at we call ˜β here. Then,
˜β((id ⊗η)((ρ′,g ′),q ′)) = ˜β((ρ′,g ′), (q′,α (q′))) = ((˜q,g ′α(q′)g−1), (ρ,g )) (7.2.8)
where the choices (˜ρ,h ) we have to make for the deﬁnition of ˜β are here (ρ,g −1), and ˜q is deﬁned
in (7.1.7), which gives here
˜q =β−1
l (βr((ρ′, 1),q ′), (R(ρ−1, idg−1 ),g −1)).
Comparing (7.2.7) and (7.2.8) it remains to prove q = ˜q in F . As F was the quotient of Q by the
action β0, it suﬃces to have
β0(g′, ˜q)
(i)
= β−1
l (βr((id,g ′),βr((ρ′, 1),q ′)), (R(ρ−1, idg−1 ),g −1))
(iii)
= β−1
l (βr((ρ′,g ′),q ′), (R(ρ−1, idg−1 ),g −1))
= β−1
l (β−1
l (q, (ρ,g )), (R(ρ−1, idg−1 ),g −1))
(ii)
= β−1
l (q, (id, 1))
= q.
This ﬁnishes the construction of the 2-isomorphism ηA.
