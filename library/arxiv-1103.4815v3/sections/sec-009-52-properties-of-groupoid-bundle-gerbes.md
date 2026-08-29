---
doc_id: arxiv-1103.4815v3
doc_title: "Four Equivalent Versions of Non-Abelian Gerbes"
section_id: sec-009-52-properties-of-groupoid-bundle-gerbes
section_title: "Properties of Groupoid Bundle Gerbes"
section_number: 5.2
pages: 27-33
source_pdf: 1103.4815v3.pdf
source_sha256: 28647b02ea1441e3
doc_brief: "Four Equivalent Versions of Non-Abelian Gerbes — We recall and partially improve four versions of smooth, non -abelian gerbes: ˇCech cocycles, classifying maps, bundle gerbes, and principal"
---
We recall that a homomorphism Λ : Γ /d47/d47 Ω between Lie 2-groups is an anafunctor together with a
transformation (2.4.4) describing its compatibility with the multiplicatio ns. We recall further from
Proposition 2.4.9 that extension along Λ is a 1-morphism
Λ : BunΓ /d47/d47 BunΩ
between monoidal stacks over smooth manifolds. That is, extensio n along Λ is compatible with pull-
backs, tensor products, and morphisms between principal Γ-bun dles. Applying it to the principal
Γ-bundle P of a Γ-bundle gerbe G, and also to the bundle gerbe product µ, we obtain immediately
an Ω-bundle gerbe Λ G. The same is evidently true for morphisms and 2-morphisms. Summar izing,
we get:
Proposition 5.2.1. Extension of bundle gerbes along a homomorphism Λ : Γ /d47/d47 Ω between Lie
2-groups deﬁnes a 1-morphism
Λ : GrbΓ /d47/d47 GrbΩ
of 2-stacks over smooth manifolds.
We recall that a weak equivalence between Lie 2-groups is a homomor phism Λ : Γ /d47/d47 Ω that
is a weak equivalence (see Deﬁnition 2.3.11). We have:
Theorem 5.2.2. Suppose Λ : Γ /d47/d47 Ω is a weak equivalence between Lie 2-groups. Then, the
1-morphism Λ : GrbΓ /d47/d47 GrbΩ of Proposition 5.2.1 is an equivalence of 2-stacks.
Proof. The monoidal equivalence Λ : BunΓ /d47/d47 BunΩ between the monoidal stacks (Corollary
2.4.10) induces an equivalence TrivGrbΓ (M ) /d47/d47 TrivGrbΛ (M ) between pre-2-stacks. Since the plus
construction is functorial, this induces in turn the claimed equivalenc e of 2-stacks. □
Next we generalize a couple of well-known results from abelian to non- abelian bundle gerbes.
We deﬁne a reﬁnement of a surjective submersion π :Y /d47/d47 M to be another surjective submersion
ω : W /d47/d47 M together with a smooth map f : W /d47/d47 Y such that ζ = π ◦f . Notice that such
a reﬁnement induces smooth maps fk : W [k] /d47/d47 Y [k] that commute with the various projections
ωi1...i k and πi1...i k .
Lemma 5.2.3. Suppose G1 = ( Y1,P 1,µ 1) and G2 = ( Y2,P 2,µ 2) are Γ -bundle gerbes over M ,
f : Y1 /d47/d47 Y2 is a reﬁnement of surjective submersions, and ϕ : f ∗
2P2 /d47/d47 P1 is an isomorphism
– 27 –
of Γ -bundles over Y [2]
1 that is compatible with the bundle gerbe products µ1 and µ2 in the sense that
the diagram
π∗
23f ∗
2P2 ⊗π∗
12f ∗
2P2
π ∗
23ϕ ⊗π ∗
12ϕ
/d15/d15
f ∗
3µ /d47/d47π∗
13f ∗
2P2
π ∗
13ϕ
/d15/d15
π∗
23P1 ⊗π∗
12P1 µ
/d47/d47π∗
13P1
is commutative. Then, G1 and G2 are isomorphic.
The proof works just the same way as in the abelian case: one const ructs the 1-isomorphism
over the common reﬁnement Z :=Y1 ×MY2 in a straightforward way. As a consequence of Lemma
5.2.3 we have
Proposition 5.2.4. Let G = (Y,P,µ ) be a Γ -bundle gerbe over M , and let f : W /d47/d47 Y be a
reﬁnement of its surjective submersion π :Y /d47/d47 M . Then, (W,f ∗
2P,f ∗
3µ) is a Γ -bundle gerbe over
M , and is isomorphic to G.
Lemma 5.2.5. Let G = (Y,P,µ ) be a Γ -bundle gerbe over M . Then, there exist unique smooth
maps i :P /d47/d47 P and t :Y /d47/d47 P such that
(i) the diagrams
P i /d47/d47
χ
/d15/d15
P
χ
/d15/d15
Y [2]
ﬂip
/d47/d47Y [2]
and
P
χ
/d15/d15
Y diag
/d47/d47
t
/d62/d62⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤⑤
Y [2]
are commutative.
(ii) the map t is neutral with respect to the bundle gerbe product µ, i.e.
µ(t(y2),p ) = p =µ(p,t (y1)).
for all p ∈ P with χ(p) = (y1,y 2).
(iii) the map i provides inverses with respect to the bundle gerbe product µ, i.e.
µ(i(p),p ) = t(y1) and µ(p,i (p)) = t(y2)
for all p ∈ P with χ(p) = (y1,y 2).
Moreover,α(t(y)) = 1 and α(i(p)) = α(p)−1 for all p ∈ P and y ∈ Y .
– 28 –
Proof. Concerning uniqueness, suppose ( t,i ) and ( t′,i ′) are pairs of maps satisfying (i), (ii) and
(iii). Firstly, we have t′(y) = µ(t(y),t ′(y)) = t(y) and so t =t′. Then, µ(i(p),p ) = t(y1) = t′(y1) =
µ(i′(p),p ) implies i(p) = i′(p), and so i = i′. In order to see the existence of t and i, denote by
Q := diag ∗P the pullback of P to Y , denote by Q∨ the dual bundle and by d :Q ⊗Q∨ /d47/d47 I1 the
death map. Consider the smooth map
Y s /d47/d47 I1
d−1
/d47/d47Q ⊗Q∨ µ −1 ⊗idQ∨
/d47/d47Q ⊗Q ⊗Q∨ id ⊗d /d47/d47 I1 ⊗Q ∼=Q
diag /d47/d47P
where s : Y /d47/d47 I1 is the canonical section (see the proof of Lemma 2.2.6). It is straigh tforward
to see that this satisﬁes the properties of the map t. Since all maps in the above sequence are
(anchor-preserving) bundle morphisms, it is clear that t ◦α = 1. □
Corollary 5.2.6. Let G = (Y,P,µ ) be a Γ -bundle gerbe over M , and let t andi be the unique maps
of Lemma 5.2.5. Then,
(i) t is a section of diag∗P , and deﬁnes a trivialization diag∗P ∼= I1.
(ii) i is a bundle isomorphism i :P ∨ /d47/d47 ﬂip∗P .
(iii) C0 := Y and C1 := P deﬁne a Lie groupoid with source and target maps π1 ◦χ and π2 ◦χ,
respectively, compositionµ, identity t and inversion i.
The following statement is well-known for abelian gerbes; the genera l version can be proved by
a straightforward generalization of the constructions given in the proof of [Wal07, Proposition 3].
Lemma 5.2.7. Every 1-morphism A : G /d47/d47 H between Γ -bundle gerbes over M is invertible.
The last statement of this section shows a way to bring 1-morphisms and 2-morphisms into
a simpler form (see Remark 5.1.10). For bundle gerbes G1 and G2 with surjective submersions
π1 :Y1 /d47/d47 M and π2 :Y2 /d47/d47 M we denote by Hom(G1, G2) the Hom-category in the bicategory
GrbΓ (M ), and by Hom(G1, G2)FP the category whose objects are those 1-morphisms whose commo n
reﬁnement is Z :=Y1 ×M Y2, and whose 2-morphisms are those 2-morphisms whose reﬁnement is
W :=Y1 ×M Y2 with the maps r,r ′ :W /d47/d47 Z the identity maps.
Lemma 5.2.8. The inclusion Hom(G1, G2)FP /d47/d47 Hom(G1, G2) is an equivalence of categories.
Proof. First we show that it is essentially surjective. We assume A : G1 /d47/d47 G2 is a general
1-morphism with a principal Γ-bundle Q over a common reﬁnement Z of the surjective submersions
π1 :Y1 /d47/d47 M and π2 :Y2 /d47/d47 M of the two bundle gerbes. We look at the principal Γ-bundle
˜Q :=κ∗
2P2 ⊗ pr∗
2Q ⊗κ∗
1P1
– 29 –
over ˜Z :=Y1 ×M Z ×M Y2, where
κ1 : ˜Z /d47/d47 Y [2]
1 : (y1,z,y 2) ✤ /d47/d47 (y1,y 1(z)) and κ2 : ˜Z /d47/d47 Y [2]
2 : (y1,z,y 2) ✤ /d47/d47 (y2(z),y 2).
The projection pr 13 : ˜Z /d47/d47 Y1 ×M Y2 is a surjective submersion, and over ˜Z ×Y1 ×MY2
˜Z we
have a bundle morphism α : pr ∗
1 ˜Q /d47/d47 pr∗
2 ˜Q deﬁned over a point (˜z, ˜z′) with ˜z = (y1,z,y 2) and
˜z′ = (y1,z ′,y 2) by
˜Q˜z P2|y2(z),y 2 ⊗Qz ⊗P1|y1,y 1(z)
µ −1
2 ⊗id⊗id
/d15/d15
P2|y2(z′),y 2 ⊗P2|y2(z),y 2(z′) ⊗Qz ⊗P1|y1,y 1(z)
id ⊗β ⊗id
/d15/d15
P2|y2(z′),y 2 ⊗Qz′ ⊗P1|y1(z),y 1(z′) ⊗P1|y1,y 1(z)
id ⊗id⊗µ 1
/d15/d15
P2|y2(z′),y 2 ⊗Qz′ ⊗P1|y1,y 1(z′) ˜Q˜z′.
The compatibility condition (5.1.1) implies a cocycle condition for α over the three-fold ﬁbre product
of ˜Z overY1 ×MY2, and since principal Γ-bundles form a stack, the pair ( ˜Q,α ) deﬁnes a principal Γ-
bundleQFP overZFP :=Y1 ×MY2. It is now straightforward to show that the bundle isomorphism
β itself descends to a bundle isomorphism βFP over ZFP ×M ZFP in such a way that the triple
(ZFP,QFP,βFP ) forms a 1-morphism AFP : G1 /d47/d47 G2.
In order to show that AFP is an essential preimage of A, it remains to construct a 2-morphism
ϕFP
A : A /d43/d51 AFP . In the terminology of Deﬁnition 5.1.3, we choose W = ˜Z with r := pr 2 :
W /d47/d47 Z and r′ := pr 13 : W /d47/d47 ZFP . Note that diagram (5.1.3) does not commute. The
maps xW : W /d47/d47 Y [2]
1 and yW : W /d47/d47 Y [2]
2 are given by xW = s ◦κ1 and yW = κ2, where
s : Y [2]
1 /d47/d47 Y [2]
1 switches the factors. Now, the bundle isomorphism of the 2-morph ism ϕFP
A we
want to construct is a bundle isomorphism
ϕ :y∗
WP2 ⊗r∗Q /d47/d47 ˜Q ⊗x∗
WP1
overW , and is ﬁbrewise over a point w = (y1,z,y 2) given by
P2|y2(z),y 2 ⊗Qz
id ⊗id⊗t−1
/d47/d47P2|y2(z),y 2 ⊗Qz ⊗Py1(z),y 1(z)
id⊗id ⊗µ −1
1
/d15/d15
P2|y2(z),y 2 ⊗Qz ⊗P1|y1,y 1(z) ⊗P1|y1(z),y 1
˜Qw ⊗P1|s(y1,y 1(z)),
where t is the trivialization of diag ∗P of Corollary 5.2.6. The compatibility condition (5.1.2) is
straightforward to check.
Now we show that the inclusion Hom(G1, G2)FP /d47/d47 Hom(G1, G2) is full and faithful. Since it is
clearly faithful, it only remains to show that it is full. Given a morphism A /d47/d47 A′ in Hom(G1, G2),
– 30 –
i.e. a common reﬁnement W of Y1 ×M Y2 with itself and a bundle morphism ϕ, we have to ﬁnd
a morphism in Hom(G1, G2)FP such that the two morphisms are identiﬁed under the equivalence
relation on bundle gerbe 2-morphisms. We denote the bundles over Y1 ×M Y2 corresponding to A
and A′ byQ andQ′. The reﬁnement maps are denoted as before by r = (s1,s 2) : W /d47/d47 Y1 ×MY2
and r′ = (t1,t 2) : W /d47/d47 Y1 ×M Y2. Then we obtain an isomorphism r∗Q /d47/d47 r∗Q′ ﬁbrewise over
a point w ∈ W by
Q|s1(w),s 2(w)
d−1 ⊗id /d47/d47P ∨
2 |s2(w),t 2(w) ⊗P2|s2(w),t 2(w) ⊗Q|s1(w),s 2(w)
id⊗ϕ
/d15/d15
P ∨
2 |s2(w),t 2(w) ⊗Q′|t1(w),t 2(w) ⊗P1|s1(w),t 1(w)
id⊗β ′−1
/d15/d15
P ∨
2 |s2(w),t 2(w) ⊗P2|s2(w),t 2(w) ⊗Q′|s1(w),s 2(w)
d ⊗id /d47/d47Q′|s1(w),s 2(w)
(5.2.1)
where d : P ∨
2 |s2(w),t 2(w) ⊗P2|s2(w),t 2(w) /d47/d47 I1 is the death map. One can use the compatibility
condition for ϕ to show that this morphism descends to a morphism ψ : Q /d47/d47 Q′ which is a
morphism in Hom(G1, G2)FP . The two morphisms ( W,ψ ) and (Y1 ×M Y2,ϕ ) are identiﬁed if their
pullbacks to
W ×(Y1 ×MY2 ×MY1 ×MY2) (Y1 ×M Y2) = {w ∈ W |r(w) = r′(w)} =:W0
are equal. On the one side, the map W0 /d47/d47 W is the inclusion and the map W0 /d47/d47 Y1 ×MY2 is
equal to r. The pullback of ψ along r is by construction the map r∗Q /d47/d47 r∗Q′ from (5.2.1). On
the other side, bundles x∗
WP1 and y∗
WP2 overW0 have canonical trivializations (Lemma 5.2.6 (i))
under which ϕ becomes also equal to the morphism (5.2.1). □
5.3 Classiﬁcation by ˇCech Cohomology
In this section we prove that Versions I ( ˇCech Γ-1-cocycles) and III (Γ-bundle gerbes) are equivalent.
For this purpose, we extract a ˇCech cocycle from a Γ-bundle gerbe G overM , and prove that this
procedure deﬁnes a bijection on the level of equivalence classes (T heorem 5.3.2). First we have to
ensure the existence of appropriate open covers.
Lemma 5.3.1. For every Γ -bundle gerbe G = (Y,P,µ ) over M there exists an open cover U =
{Ui}i ∈I ofM with sections σi :Ui /d47/d47 Y , such that the principal Γ -bundles (σi ×σj)∗P overUi ∩Uj
are trivializable.
Proof. One can choose an open cover such that the 2-fold interse ctions Ui ∩Uj are contractible.
Since every Lie 2-group is a crossed module G/ /H(Remark 2.4.3), and G/ /H-bundles are ordinary
H-bundles (Lemma 2.2.9), these admit sections over contractible smo oth manifolds. But a section
is enough to trivialize the original Γ-bundle (Lemma 2.2.6). □
– 31 –
Let G be a Γ-bundle gerbe over M , and let U = {Ui}i∈I be an open cover with the properties of
Lemma 5.3.1. We denote by MU the disjoint union of all the open sets Ui, and by σ :MU /d47/d47 Y
the union of the sections σi. Then, σ is a reﬁnement of π : Y /d47/d47 M , and we have a Γ-bundle
gerbe GU,σ that is isomorphic to G (Proposition 5.2.4).
The principal Γ-bundle Pij of GU,σ over the component Ui ∩Uj is by assumption trivializable.
Thus there exists a trivialization tij : Pij /d47/d47 Ifij for smooth functions fij :Ui ∩Uj /d47/d47 Γ 0. We
deﬁne an isomorphism µijk between trivial bundles such that the diagram
Pjk ⊗Pij
µ /d47/d47
tjk ⊗tij
/d15/d15
Pik
tik
/d15/d15
Ifjk ⊗ Ifij µ ijk
/d47/d47 Ifik
is commutative. Now we are in the situation of Lemma 5.2.3, which implies t hat the Γ-bundle gerbe
GU,σ,t := (MU, Ifij,µijk ) is still isomorphic to G.
Combining Lemma 2.2.8 with Example 2.4.7 (a), we see that the isomorphis msµijk correspond
to smooth maps gijk : Ui ∩Uj ∩Uk /d47/d47 Γ 1 such that s(gijk ) = fjk ·fij and t(gijk ) = fik. The
associativity condition for µijk implies moreover that
gαγδ ◦ (gαβγ · idfγδ ) = gαβδ ◦ (idfαβ ·gβγδ ).
Hence, the collection {fij,gijk } is a Γ-1-cocycle on M with respect to the open cover U .
Theorem 5.3.2. LetM be a smooth manifold and let Γ be a Lie 2-group. The above construction
deﬁnes a bijection { Isomorphism classes of
Γ -bundle gerbes over M
}
∼= ˇH1(M, Γ) .
Proof. We claim that Γ-bundle gerbes ( MU, Ifij,µijk ) and (MV, Ihij,νijk ) are isomorphic if and
only if the corresponding Γ-1-cocycles are equivalent. This proves at the same time that the
choices of open covers and sections we have made during the const ruction do not matter, that the
resulting map is well-deﬁned on isomorphism classes, and that this map is injective. Surjectivity
follows by assigning to a Γ-1-cocycle ( fij,gijk ) with respect to some cover U the Γ-bundle gerbe
(MU, Ifij,µijk ) with µijk determined by Lemma 2.2.8.
It remains to prove that claim. We assume A = (Z,Q,α ) is a 1-isomorphism between the Γ-
bundle gerbes ( MU, Ifij,µijk ) and ( MV, Ihij,νijk ). Similarly to Lemma 5.3.1 one can show that
there exists a cover W of M by open sets Wi that reﬁnes both U and V , and that allows smooth
sectionsωi :Wi /d47/d47 Z for which the Γ-bundle ω∗
iQ is trivializable. In the terminology of the above
construction, choosing a trivialization t :ω∗Q /d47/d47 Ihi with smooth maps hi :Wi /d47/d47 Γ 0 overMW
converts the isomorphism α into smooth functions sij :Wi ∩Wj /d47/d47 Γ 1 satisfying s(sij) = g′
ij ·hi
– 32 –
andt(sij) = hj ·gij. The compatibility diagram (5.1.1) implies the remaining condition that ma kes
(hi,sij) an equivalence between the Γ-2-cocycles ( fij,gijk ) and (f ′
ij,g ′
ijk ). □
