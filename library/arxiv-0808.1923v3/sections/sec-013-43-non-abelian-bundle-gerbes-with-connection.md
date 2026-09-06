---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-013-43-non-abelian-bundle-gerbes-with-connection
section_title: "Non-Abelian Bundle Gerbes with Connection"
section_number: 4.3
pages: 36-41
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
In this section we generalize the equivalence of the previous section to so-called non-abelian bundle
gerbes, as deﬁned in [ACJ05]. The diﬀerence between abelian and no n-abelian bundle gerbes can
roughly be summarized as follows:
1. The Lie group S1 is replaced by some connected Lie group H.
2. Principal S1-bundles are replaced by principal H-bibundles , bundles with commuting left and
right principal H-action. Morphisms between H-bibundles are bi-equivariant bundle morphisms.
3. Connections on S1-bundles are replaced by so-called twisted connections on bibundles.
– 36 –
Non-abelian H-bundle gerbes with connection over M form a 2-category which we denote by
H-BGrb∇(M ); some details are reviewed below. There is a sub-2-category H-BGrb∇f f(M ) of fake-ﬂat
non-abelian H-bundle gerbes, related to Remark 4.1.7.
On the side of transport 2-functors, we write H-BiTor for the category whose objects are smooth
manifolds with commuting, free and transitive, smooth left and right H-actions, and whose morphisms
are smooth bi-equivariant maps. Using the product over H this is naturally a (non-strict) monoidal
category, and we write B(H-BiTor) for the corresponding one-object (non-strict) 2-cate gory. Let
AUT(H) be the Lie 2-group associated to H via Example 3.3.3 (iii). A 2-functor
i : BAUT(H) /d47/d47 B(H-BiTor) (4.3.1)
is deﬁned as follows. It sends a 1-morphism ϕ ∈ Aut(H) to the H-bitorsor ϕH which is the group H
on which an element h acts from the right by multiplication and from the left by multiplication w ith
ϕ(h). The compositors of i are given by the canonical identiﬁcations
cg1,g2 : g1H ×H g 2H /d47/d47 g2g1H,
and the unitor is the identity. The 2-functor i further sends a 2-morphism h : ϕ1 /d43/d51 ϕ2 to the
bi-equivariant map
ϕ1H /d47/d47 ϕ2H :x ✤ /d47/d47 hx.
While the bi-equivariance with respect to the right action is obvious, t he one with respect to the left
action follows from the condition ϕ2(x) = hϕ1(x)h−1 we have for the 2-morphisms in AUT( H) for all
x ∈ H.
The main result of this section is:
Theorem 4.3.1. There is a canonical injective map
h0(H-BGrb∇f f(M )) /d47/d47 h0(Trans2
BAUT(H)(M, B(H-BiTor)))
from isomorphism classes of fake-ﬂat non-abelian H-bundle gerbes to transport 2-functors with values
in B(H-BiTor) and BAUT(H)-structure.
That we do not achieve a bijection or an equivalence of 2-categories is due to the fact that the
category of bibundles with twisted connections – as deﬁned in [ACJ05 ] – oversees a class of morphisms,
which in principle should be allowed and arise naturally from the theory o f transport functors.
Anyway, Theorem 4.3.1 provides non-trivial examples of transport 2-functors. The injective map
of Theorem 4.3.1 is constructed as
H-BGrb∇f f(M ) /d47/d47 Des2(i)∞
M ∼= Trans2
BAUT(H)(M, B(H-BiTor)),
where the ﬁrst 2-functor is constructed in Proposition 4.3.8 and th e equivalence is the one of Theorem
3.2.2. We ﬁrst review necessary material.
4.3.1 Twisted Connections on Bibundles
Let P be a principal H-bibundle over X. We denote the left and right actions by an element h ∈ H
on P bylh and rh, respectively. Measuring the diﬀerence between the left and the r ight action in the
sense of lh(p) = rg(h)(p) furnishes a smooth map
g :P /d47/d47 Aut(H). (4.3.2)
– 37 –
In the following we denote by aut(H) the Lie algebra of Aut( H). Further, we denote by t :
H /d47/d47 Aut(H) the assignment of inner automorphisms and by α : Aut(H) ×H /d47/d47 H the evaluation.
Deﬁnition 4.3.2 ([ACJ05]). Letp :P /d47/d47 X be a principal H-bibundle, and let A ∈ Ω 1(X, aut(H))
be a 1-form on the base space. An A-twisted connection on P is a 1-form φ ∈ Ω 1(P, h) satisfying
φρh
( d
dt (ρh)
)
= Ad −1
h
(
φρ
(dρ
dt
))
− (rh ◦αh)∗ ◦ (p∗A) +θh
(dh
dt
)
(4.3.3)
for all smooth curves ρ : [0, 1] /d47/d47 P and h : [0, 1] /d47/d47 H. A morphism f : P /d47/d47 P ′ respects
A-twisted connections φ on P and φ′ on P ′ if f ∗φ′ =φ.
We write Bibun∇
H (X,A ) for the category of principal H-bibundles with A-twisted connection over
X, and Bibun∇
H (X) for the union of these categories over all 1-forms A.
Remark 4.3.3. ForA = 0 an A-twisted connection on P is the same as an ordinary connection on P
regarded as a right principal bundle.
Lemma 4.3.4 ([ACJ05]). Let A ∈ Ω 1(X, aut(H)) be a 1-form and let p : P /d47/d47 X be a principal
H-bibundle. For any A-twisted connection φ on P there exists a unique 1-form Aφ ∈ Ω 1(X, aut(H))
satisfying
p∗Aφ = Adg(p∗A) −g∗ ¯θ −t∗ ◦φ,
whereg is the map from (4.3.2).
A twisted connection in a principal bibundle P gives rise to parallel transport maps
τγ :Px /d47/d47 Py
between the ﬁbres of P over points x,y associated to any path γ :x /d47/d47 y. It is obtained in the same
way as in an ordinary principal bundle but using equation (4.3.3) instea d of the usual one. As a result
of the twist, the maps τγ are not bi-equivariant; they satisfy
τγ(lFφ (γ)(h)(p)) = lh−1 (τγ(p)) and τγ(rh(p)) = rF (γ)−1(h−1)τγ(p) (4.3.4)
where F,Fφ :PX /d47/d47 Aut(H) are the parallel transport maps associated to the 1-forms A and Aφ;
see [SW09, Proposition 4.7]. These complicated relations have a very e asy interpretation, as we will
see in the next section.
Finally, an A-twisted connection φ on a principal H-bundle P has a curvature: this is the 2-form
curv(φ) := dφ + [φ ∧φ] +α∗(A ∧φ) ∈ Ω 2(P, h).
For two principal H-bibundles P and P ′ over X one can ﬁbrewise take the tensor product of P
and P ′ yielding a new principal H-bibundle P ×HP overX. If the two bibundles are equipped with
twisted connections, the bibundle P ×HP ′ inherits a twisted connection only if the two twists satisfy an
appropriate matching condition. Suppose the principal H-bibundle P is equipped with an A-twisted
connection φ, and P ′ is equipped with an A′-twisted connection φ′, and suppose that the matching
condition
A′
φ′ =A (4.3.5)
– 38 –
is satisﬁed. Then, the tensor product bibundle P ×HP ′ carries anA′-twisted connectionφtot ∈ Ω 1(P ×H
P, h) characterized uniquely by the condition that
pr∗φtot = (g ◦p′)∗ ◦p∗φ +p′∗φ′,
where pr : P ×XP ′ /d47/d47 P ×HP ′ is the projection to the tensor product and p andp′ are the projections
to the two factors. This tensor product, deﬁned only between ap propriate pairs of bibundles with
twisted connections, turns Bibun∇
H (X) into a “monoidoidal” category.
A better point of view is to see it as a 2-category: the objects are t he twists, i.e. 1-forms
A ∈ Ω 1(X, aut(H)), a 1-morphism A /d47/d47 A′ is a principal H-bibundleP withA′-twisted connection φ
such that A′
φ′ =A, and a 2-morphism ( P,φ ) /d43/d51 (P ′,φ ′) is just a morphism of principal H-bibundles
that respects the A′-twisted connections.
4.3.2 T ransport F unctors for Bibundles with Twisted Connec tions
We are now going to relate the category Bibun∇
H (X) of principal H-bibundles with twisted connections
overX to a category of transport functors. Using the terminology of Se ction 3.1, we have:
Proposition 4.3.5. There is a surjective and faithful functor
Bibun∇
H (X) /d47/d47 Trans1
Λ BAUT(H)(X, ΛiB(H-BiTor)).
Proof. Given a principal H-bibundleP withA-twisted connection, we deﬁne the associated transport
functor by
traP : x
γ /d47/d47y ✤ /d47/d47
i(∗)
Px
/d15/d15
i(F (γ)) /d47/d47i(∗)
τ −1
γ
②②②②②
②②②②②
/d120/d0 ②②②②②②②②
Py
/d15/d15
i(∗)
i(Fφ (γ))
/d47/d47i(∗).
Here F,Fφ : PX /d47/d47 Aut(H) are the maps deﬁned by A and Aφ that we have already used in
the previous section. The deﬁnition contains the claim that the para llel transport map τγ gives a
bi-equivariant map
τ −1
γ :Py ×H F (γ)H /d47/d47 Fφ (γ)H ×H Px;
it is indeed easy to check that this is precisely the meaning of equation s (4.3.4). A morphism
f : P /d47/d47 P ′ between bibundles with A-twisted connections induces a natural transformation
ηf : tra P /d47/d47 traP ′ between the associated functors, whose component at a point x is the bi-
equivariant map fx : Px /d43/d51 P ′
x. This is a particular morphism in Λ iB(H-BiTor) for which the
horizontal 1-morphisms are identities. Here it becomes clear that t he assignments
(P,φ ) ✤ /d47/d47 traP and f ✤ /d47/d47 ηf
deﬁne a functor which is faithful but not full.
It remains to check that the functor tra P is a transport 2-functor. We leave it as an exercise for
the reader to construct a local trivialization ( t, triv) of tra P with smooth descent data. Hint: use an
ordinary local trivialization of the bibundle P and follow the proof of Proposition 5.2 in [SW09]. □
– 39 –
Both categories in Proposition 4.3.5 have the feature that they hav e tensor products between
appropriate objects. Concerning the bibundles with twisted conne ctions, we have described this in
terms of the matching condition (4.3.5) on the twists. Concerning th e category of transport functors,
this tensor product is inherited from the one on Λ iB(H-BiTor), which has been discussed in Section
3.1.
Lemma 4.3.6. The matching condition (4.3.5) corresponds to the required condition for tensor prod-
ucts in ΛiB(H-BiTor) under the functor of Proposition 4.3.5. Moreover, the funct or respects tensor
products whenever they are well-deﬁned.
Proof. Suppose that the matching condition A′
φ′ = A holds, so that principal H-bibundles P and
P ′ with connections φ and φ have a tensor product. It follows that the map Fφ′ which labels the
horizontal 1-morphisms at the bottom of the images of tra P ′ is equal to the map F which labels the
ones at the top of the images of tra P ; this is the required condition for the existence of the tensor
product traP ′ ⊗ traP . That the tensor products are respected follows from the deﬁnit ion of the twisted
connection φtot on the tensor product bibundle. □
An alternative formulation of Lemma 4.3.6 would be that the functor o f Proposition 4.3.5 respects
the “monoidoidal structures”, or, that it is a double functor betw een (weak) double categories.
4.3.3 Non-Abelian Bundle Gerbes as T ransport 2-F unctors
Let π :Y /d47/d47 M be a surjective submersion. We recall:
Deﬁnition 4.3.7 ([ACJ05]). A non-abelian H-bundle gerbe with connection with respect to π is a
2-form B ∈ Ω 2(Y, h), a 1-form A ∈ Ω 1(Y, aut(H)), a principal H-bibundle p : P /d47/d47 Y [2] with
A-twisted connection φ such that
curv(φ) = (π1 ◦p)∗B − (αg)∗ ◦ (π2 ◦p)∗B, (4.3.6)
and an associative morphism
µ :π∗
23P ×H π∗
12P /d47/d47 π∗
13P
of bibundles over Y [3] that respects the twisted connections.
In (4.3.6), g is the smooth map (4.3.2) and α : Aut(H)×H /d47/d47 H is the evaluation. The deﬁnitions
of 1-morphisms and 2-morphisms generalize in a straightforward wa y the deﬁnitions from the abelian
case. This deﬁnes the 2-category H-BGrb∇(π). The 2-category H-BGrb∇(M ) of non-abelian H-
bundle gerbes over M is deﬁned as the direct limit,
H-BGrb∇(M ) := lim− →π
H-BGrb∇(π).
We remark:
(i) A non-abelian S1-bundle gerbe is not the same as an abelian S1-bundle gerbe: for the non-
abelian bundle gerbes also the automorphisms are important, and Au t(S1) ∼= Z2. For transport
2-functors this is even more obvious: the Lie 2-groups BS1 and AUT(S1) are not equivalent.
(ii) The non-abelian bundle gerbes of Deﬁnition 4.3.7 are a priori not “f ake-ﬂat”, i.e. the relation
t∗(B) = dA + [A ∧A]
– 40 –
may not be satisﬁed, see Remark 4.1.7. We denote the sub-2-categ ories of fake-ﬂat non-abelian
H-bundle gerbes by H-BGrb∇f f(−).
Proposition 4.3.8. For every surjective submersion π :Y /d47/d47 M , there is a 2-functor
H-BGrb∇f f(π) /d47/d47 Des2
π(i)∞.
which is surjective and faithful on Hom-categories. In part icular, it induces an injective map on
isomorphism classes of objects.
Proof. All relations concerning the bimodules are analogous to thos e in the abelian case, upon
generalizing Lemma 4.2.3 to Proposition 4.3.5 and Lemma 4.3.6. Relation (4 .3.6) for the 2-form B can
be proved in the same way as Lemma 4.2.4, but now using the full versio n of equation (4.1.4). The
comments concerning the descent datum ψ also remain valid. □
In the direct limit, the 2-functors of Proposition 4.3.8 induce a 2-fun ctor
H-BGrb∇f f(M ) /d47/d47 Des2(i)∞
M . (4.3.7)
Since the direct limit respects the operation of forming isomorphism c lasses of objects, and on the level
of sets a direct limit of injective maps is injective, the 2-functor (4.3 .7) induces an injective map on
isomorphism classes of objects. This completes the proof of Theor em 4.3.1.
