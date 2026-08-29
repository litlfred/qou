---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-008-5-version-iii-groupoid-bundle-gerbes
section_title: "Version III: Groupoid Bundle Gerbes"
section_number: 5
pages: 21-27
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
Several deﬁnitions of non-abelian bundle gerbes have appeared in lit erature so far [ACJ05, Jur11,
MRS]. The approach we give here not only shows a conceptually clear w ay to deﬁne non-abelian
bundle gerbes, but also produces systematically a whole bicategory . Moreover, these bicategories
form a 2-stack over smooth manifolds (with the Grothendieck topo logy of surjective submersions).
5.1 Deﬁnition via the Plus Construction
Recall that the stack BunΓ of principal Γ-bundles is monoidal if Γ is a Lie 2-group (Proposition
2.4.8). Associated to the monoidal stack BunΓ we have a pre-2-stack
TrivGrbΓ := B(BunΓ )
of trivial Γ -gerbes. Explicitly, there is one trivial Γ-gerbe I over every smooth manifold M . The
1-morphisms from I to I are principal Γ-bundles over M , and the 2-morphisms between those
are morphisms of principal Γ-bundles. Horizontal composition is give n by the tensor product of
principal Γ-bundles, and vertical composition is the ordinary compo sition of Γ-bundle morphisms.
Now we apply the plus construction of [NS11] in order to stackify this pre-2-stack. The resulting
2-stack is by deﬁnition the 2-stack of Γ -bundle gerbes , i.e.
GrbΓ := (TrivGrbΓ )+ .
Unwinding the details of the plus construction, we obtain the following deﬁnitions:
Deﬁnition 5.1.1. LetM be a smooth manifold. A Γ -bundle gerbe overM is a surjective submersion
π : Y /d47/d47 M , a principal Γ -bundle P over Y [2] and an associative morphism
µ :π∗
23P ⊗π∗
12P /d47/d47 π∗
13P
of Γ -bundles over Y [3].
– 21 –
The morphism µ is called the bundle gerbe product . Its associativity is the evident condition for
bundle morphisms over Y [4].
In order to proceed with the 1-morphisms, we say that a common reﬁnement of two surjective
submersions π1 : Y1 /d47/d47 M and π2 : Y2 /d47/d47 M is a smooth manifold Z together with surjective
submersions Z /d47/d47 Y1 and Z /d47/d47 Y2 such that the diagram
Z
/d32/d32❇❇❇❇❇❇
/d126/d126⑤⑤⑤⑤⑤⑤
Y1
π 1 /d32/d32❇❇❇❇❇ Y2
π 2/d126/d126⑤⑤⑤⑤⑤
M
is commutative.
We ﬁx the following convention: suppose P1 and P2 are Γ-bundles over surjective submersions
U1 and U2, respectively, and V is a common reﬁnement of U1 and U2. Then, a bundle morphism
ϕ :P1 /d47/d47 P2 is understood to be a bundle morphism between the pullbacks of P1 and P2 to the
common reﬁnement V . For example, in the following deﬁnition this convention applies to U1 =Y [2]
1 ,
U2 =Y [2]
2 and V = Z [2].
Deﬁnition 5.1.2. Let G1 and G2 be Γ -bundle gerbes over M . A 1-morphism A : G1 /d47/d47 G2 is a
common reﬁnement Z of the surjective submersions of G1 and G2 together with a principal Γ -bundle
Q over Z and a morphism
β :P2 ⊗ζ∗
1Q /d47/d47 ζ∗
2Q ⊗P1
of Γ -bundles over Z [2], where ζ1,ζ 2 :Z [2] /d47/d47 Z are the two projections, such that α is compatible
with the bundle gerbe products µ1 and µ2.
The compatibility of α with µ1 and µ2 means that the diagram
π∗
23P2 ⊗π∗
12P2 ⊗ζ∗
1Q
id⊗ζ ∗
12β
/d15/d15
µ 2 ⊗id /d47/d47π∗
13P2 ⊗ζ∗
1Q
ζ ∗
13β
/d15/d15
π∗
23P2 ⊗ζ∗
2Q ⊗π∗
12P1
ζ ∗
23β ⊗id
/d15/d15
ζ∗
3Q ⊗π∗
23P1 ⊗π∗
12P1 id⊗µ 1
/d47/d47ζ∗
3Q ⊗π∗
13P1
(5.1.1)
of morphisms of Γ-bundles over Z [3] is commutative.
– 22 –
If A12 : G1 /d47/d47 G2 and A23 : G2 /d47/d47 G3 are 1-morphisms between bundle gerbes over M , the
composition A23 ◦ A12 : G1 /d47/d47 G3 is given by the ﬁbre product Z := Z23 ×Y2 Z12, the principal
Γ-bundle Q :=Q23 ⊗Q12 overZ, and the morphism
P3 ⊗ζ∗
1Q
β 23 ⊗id /d47/d47ζ∗
2Q23 ⊗P2 ⊗ζ∗
1Q12
id ⊗β 12 /d47/d47ζ∗
2Q ⊗P1.
The identity 1-morphism id G associated to a Γ-bundle gerbe G is given by Y regarded as a common
reﬁnement of π : Y /d47/d47 M with itself, the trivial Γ-bundle I1 (the tensor unit of BunΓ (Y )), and
the evident morphism I1 ⊗P /d47/d47 P ⊗ I1.
In order to deﬁne 2-morphisms, suppose that π1 :Y1 /d47/d47 M and π2 :Y2 /d47/d47 M are surjective
submersions, and that Z and Z ′ are common reﬁnements of π1 and π2. Let W be a common
reﬁnement of Z and Z ′ with surjective submersions r : W /d47/d47 Z and r′ : W /d47/d47 Z ′. We obtain
two maps
s1 :W r /d47/d47Z /d47/d47Y1 and t1 :W r′
/d47/d47Z ′ /d47/d47Y1,
and analogously, two maps s2,t 2 :W /d47/d47 Y2. These patch together to maps
xW := (s1,t 1) : W /d47/d47 Y1 ×M Y1 and yW := (s2,t 2) : W /d47/d47 Y2 ×M Y2.
Deﬁnition 5.1.3. Let G1 and G2 be Γ -bundle gerbes over M , and let A, A′ : G1 /d47/d47 G2 be 1-
morphisms. A 2-morphism ϕ : A /d43/d51 A′ is a common reﬁnement W of the common reﬁnements
Z and Z ′, together with a morphism
ϕ :y∗
WP2 ⊗r∗Q /d47/d47 r′∗Q′ ⊗x∗
WP1
of Γ -bundles over W that is compatible with the morphisms β and β′.
The compatibility means that a certain diagram over W [2] commutes. Fibrewise over a point
(w,w ′) ∈ W ×M W this diagram looks as follows:
P2|s2(w′),t 2(w′) ⊗P2|s2(w),s 2(w′) ⊗Q|r(w)
id ⊗β /d47/d47
µ 2 ⊗id
/d15/d15
P2|s2(w′),t 2(w′) ⊗Q|r(w′) ⊗P1|s1(w),s 1(w′)
ϕ ⊗id
/d15/d15
P2|s2(w),t 2(w′) ⊗Q|r(w)
µ −1
2 ⊗id
/d15/d15
Q′|r′(w′) ⊗P1|s1(w′),t 1(w′) ⊗P1|s1(w),s 1(w′)
id ⊗µ 1
/d15/d15
P2|t2(w),t 2(w′) ⊗P2|s2(w),t 2(w) ⊗Q|r(w)
id⊗ϕ
/d15/d15
Q′|r′(w′) ⊗P1|s1(w),t 1(w′)
id ⊗µ −1
1
/d15/d15
P2|t2(w),t 2(w′) ⊗Q′|r′(w) ⊗P1|s1(w),t 1(w) β ′ ⊗id
/d47/d47Q′|r′(w′) ⊗P1|t1(w),t 1(w′) ⊗P1|s1(w),t 1(w)
(5.1.2)
– 23 –
Finally we identify two 2-morphisms ( W1,r 1,r ′
1,ϕ 1) and (W2,r 2,r ′
2,ϕ 2) if the pullbacks of ϕ1 and
ϕ2 to W ×Z × ×Z′ W ′ agree. Explicitly, this condition means that for all w1 ∈ W1 and w2 ∈ W2
with r1(w1) = r2(w2) and r′
1(w1) = r′
2(w2), and for all p2 ∈ y∗
W1P2 =y∗
W2P2 and q ∈ r∗
1Q =r∗
2Q
we have ϕ1(p2,q ) = ϕ2(p2,q ).
Remark 5.1.4.
• In the above situation of a common reﬁnement W of two common reﬁnements Z,Z ′ of sur-
jective submersions Y1,Y 2, the diagram
Z
/d32/d32❆❆❆❆❆❆❆
/d126/d126⑥⑥⑥⑥⑥⑥⑥
Y1 W
r
/d79/d79
r′
/d15/d15
Y2
Z ′
/d96/d96❆❆❆❆❆❆❆
/d62/d62⑥⑥⑥⑥⑥⑥⑥
(5.1.3)
is not necessarily commutative. In fact, diagram (5.1.3) commutes if and o nly if the two
maps xW : W /d47/d47 Y1 ×M Y1 and yW :W /d47/d47 Y2 ×M Y2 factor through the diagonal maps
Y1 /d47/d47 Y1 ×M Y1 and Y2 /d47/d47 Y2 ×M Y2, respectively.
• In the case that a 2-morphism ϕ is deﬁned on a common reﬁnement Z for which diagram
(5.1.3) does commute, Deﬁnition 5.1.3 can be simpliﬁed. As remarked before, the t wo maps
xW and yW factor through the diagonals, over which the bundles P1 and P2 have canonical
trivializations (see Corollary 5.2.6). Under these trivializations, ϕ can be identiﬁed with a
bundle morphism
ϕ :Q /d47/d47 Q′.
Furthermore, the compatibility diagram (5.1.2) simpliﬁes to the diagra m
P2 ⊗η∗
1Q
β /d47/d47
id⊗η ∗
1ϕ
/d15/d15
η∗
2Q ⊗P1
η ∗
2ϕ ⊗id
/d15/d15
P2 ⊗η∗
1Q′
β ′
/d47/d47η∗
2Q′ ⊗P1.
(5.1.4)
Next we deﬁne the vertical composition ϕ23 •ϕ12 : A1 /d43/d51 A3 of 2-morphisms ϕ12 : A1 /d43/d51 A2
and ϕ23 : A2 /d43/d51 A3. The reﬁnement is the ﬁbre product W :=W12 ×Z2W23 of the covers of ϕ12
and ϕ23. The bundle gerbe products induce isomorphisms
x∗
WP1 ∼=x∗
W23P1 ⊗x∗
W12P1 and y∗
WP2 ∼=y∗
W23P2 ⊗y∗
W12P2
– 24 –
overW . Under these identiﬁcations, the morphism y∗
WP2 ⊗Q1 /d47/d47 Q3 ⊗x∗
WP1 for the 2-morphism
ϕ23 •ϕ12 is deﬁned as
y∗
W23P2 ⊗y∗
W12P2 ⊗Q1
id ⊗ϕ 12 /d47/d47y∗
W23P2 ⊗Q2 ⊗x∗
W12P1
ϕ 23 ⊗id /d47/d47Q3 ⊗x∗
W23P1 ⊗x∗
W12P1.
The identity for vertical composition is just the identity reﬁnement and the identity morphism.
Finally we come to the horizontal composition
ϕ23 ◦ϕ12 : A23 ◦ A12 /d43/d51 A′
23 ◦ A′
12
of 2-morphisms ϕ12 : A12 /d43/d51 A′
12 and ϕ23 : A23 /d43/d51 A′
23: its reﬁnement W is given by
W12×(Y2 ×Y2)W23. We look at the three relevant maps xW :W /d47/d47 Y1×MY1,yW :W /d47/d47 Y2×MY2
and zW :W /d47/d47 Y3 ×M Y3. The morphism ϕ of the 2-morphism ϕ23 ◦ϕ12 is deﬁned as the com-
position
z∗
WP3 ⊗Q23 ⊗Q12
ϕ 23 ⊗id /d47/d47Q′
23 ⊗y∗
WP2 ⊗Q12
id ⊗ϕ 12 /d47/d47Q′
23 ⊗Q′
12 ⊗x∗
WP1.
It follows from the properties of the plus construction [NS11] that (a) these deﬁnitions ﬁt together
into a bicategory GrbΓ (M ), and that (b) these form a pre-2-stack GrbΓ over smooth manifolds. That
means, there are pullback 2-functors
f ∗ : GrbΓ (N ) /d47/d47 GrbΓ (M )
associated to smooth maps f :M /d47/d47 N , and that these are compatible with the composition of
smooth maps. Pullbacks of Γ-bundle gerbes, 1-morphisms, and 2-m orphisms are obtained by just
taking the pullbacks of all involved data. Finally, the plus constructio n implies (c):
Theorem 5.1.5 ([NS11, Theorem 3.3]) . The pre-2-stack GrbΓ of Γ -bundle gerbes is a 2-stack.
Remark 5.1.6. Every 2-stack over smooth manifolds deﬁnes a 2-stack over Lie gr oupoids [NS11,
Proposition 2.8]. This way, our approach produces automatically bica tegories GrbΓ (X ) of Γ-bundle
gerbes over a Lie groupoid X . In particular, for an action groupoid X =M/ /Gwe have a bicategory
GrbΓ (M/ /G) of G-equivariant Γ -bundle gerbes overM .
In the remainder of this section we give some examples and describe r elations between the
deﬁnitions given here and existing ones.
Example 5.1.7. Let A be an abelian Lie group, for instance U(1). Then, BA-bundle gerbes are
the same as the well-known A-bundle gerbes [Mur96]. For more details see Remark 5.1.10 below.
Example 5.1.8. Let (G,H,t,α ) be a smooth crossed module, and let G/ /Hbe the associated
action groupoid. Then, a ( G/ /H)-bundle gerbe is the same as a crossed module bundle gerbe in
– 25 –
the sense of Jurco [Jur11]. The equivalence relation “stably isomorp hic” of [Jur11] is given by
“1-isomorphic” in terms of the bicategory constructed here. The se coincidences come from the
equivalence between (G/ /H)-bundles and so-called G-H-bundles used in [Jur11, ACJ05] expressed
by Lemma 2.3.10. In particular, in case of the automorphism 2-group AUT(H) of a connected
Lie group H, a AUT(H)-bundle gerbe is the same as a H-bibundle gerbe in the sense of Aschieri,
Cantini and Jurco [ACJ05].
Example 5.1.9. LetG be a Lie group, so that Gdis is a Lie 2-group. Then, there is an equivalence
of 2-categories
GrbGdis (M ) ∼= BunBG(M )dis.
Indeed, if G is a Gdis-bundle gerbe over M , its principal Gdis-bundle over Y [2] is by Example
2.2.4 just a smooth map α :Y [2] /d47/d47 G, and its bundle gerbe product degenerates to an equality
π∗
23α ·π∗
12α = π∗
13α for functions on Y [3]. In other words, a Gdis-bundle gerbe is the same as
a so-called “ G-bundle 0-gerbe”. These form a category that is equivalent to the one of ordinary
principal G-bundles, as pointed out in Section 1.
Remark 5.1.10. There are two diﬀerences between the deﬁnitions given here (for Γ = BA) and
the ones of Murray et al. [Mur96, MS00, Ste00]. Firstly, we have a slig htly diﬀerent ordering of
tensor products of bundles. These orderings are not essential in the case of abelian groups because
the tensor category of ordinary A-bundles is symmetric. In the non-abelian case, a consistent
theory requires the conventions we have chosen here. Secondly, the deﬁnitions of 1-morphisms and
2-morphisms have been generalized step by step:
1. In [Mur96], 1-morphisms did not include a common reﬁnement, but rather required that the
surjective submersion of one bundle gerbe reﬁnes the other. This deﬁnition is too restrictive
in the sense that e.g. U(1)-bundle gerbes are not classiﬁed by H 3(M, Z), as intended.
2. In [MS00], 1-morphisms were deﬁned on the canonical reﬁnement Z := Y1 ×M Y2 of the
surjective submersions of the bundle gerbes. This deﬁnition solves the previous problems
concerning the classiﬁcation of bundle gerbes, but makes the comp osition of 1-morphisms
quite involved [Ste00].
3. In [Wal07], 1-morphisms were deﬁned on reﬁnements ζ :Z /d47/d47 Y1 ×MY2. This generalization
allows the same elegant deﬁnition of composition we have given here, a nd results in the same
isomorphism classes of bundle gerbes. Moreover, 2-morphisms are deﬁned with commutative
diagrams (5.1.3) – this makes the structure of the bicategory outm ost simple (see Remark
5.1.4).
4. In the present article we have allowed for a yet more general reﬁ nement in the deﬁnition of
1-morphisms. Its achievement is that bundle gerbes come out as an example of a more general
concept – the plus construction – and we get e.g. Theorem 5.1.5 for f ree.
– 26 –
Despite these diﬀerent deﬁnitions of 1-morphisms and 2-morphisms , the resulting bicategories of
BA-bundle gerbes in 2., 3. and 4. are all equivalent (see [Wal07, Theorem 1], [NS11, Remark 4.5]
and Lemma 5.2.8 below).
