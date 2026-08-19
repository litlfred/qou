---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-004-3-sl-oriented-motivic-spectra
section_title: "SL-oriented motivic spectra"
section_number: 3
pages: 13-21
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
doc_brief: "Motivic Gauss–Bonnet formulas — 18 sections: Duality and Euler characteristics; TX/B(1X×B X); TX/B(p∗"
---
In this section, we discuss the deﬁnition and basic features of SL-oriented motivic spectra. This is treated
in [Ananyevskiy 2016a] in the context of the motivic stable homotopy category SH(k) for k a ﬁeld.
Essentially all of the constructions in [op. cit.] go through without change in the setting of a separated
noetherian base-scheme B of ﬁnite Krull dimension; the most one needs to do is replace a few arguments
that rely on Jouanolou covers with some properties coming out of the six-functor formalism. We will
recall and suitably extend Ananyevskiy’s treatment here without any claim of originality.
Deﬁnition 3.1. A motivic commutative ring spectrum in SH(B) is a triple (E,µ, u) with E in SH(B),
andµ: E∧B E→ E, u: 1B→ E morphisms in SH(B), deﬁning a commutative monoid object in the
symmetric monoidal category SH(B). We usually drop the explicit mention of the multiplication µ and
unit u unless these are needed.
1814 Marc Levine and Arpon Raksit
Notation 3.2. Recall that, given a motivic spectrum E∈ SH(B), we have a notion of E-cohomology
E∗∗(X) for X∈ H(B): this is the bigraded abelian group deﬁned by
Ea,b(X):= HomSH(B)(6∞
T X+, Sa,b∧ E)
for a, b∈ Z, where Sa,b∈ SH(B) denotes the usual bigraded stable motivic sphere. This of course
specializes to give the E-cohomology of objects X∈ SmB. It also specializes to give E-cohomology with
supports E∗∗
Z (X) for X∈ SmB and Z⊆ X a closed subset: namely, we deﬁne
Ea,b
Z (X):= Ea,b(X/(X\ Z)).
For instance, if V→ X is a vector bundle, then Ea,b
0V (V)= Ea,b(Th(V)), where 0V⊂ V is the image of
the zero-section. We further deﬁne
Ea,b
Z (Th(V)):= Ea,b
0V∩q−1(Z)(V)
for Z⊆ X a closed subset and q: V→ X a vector bundle.
A commutative ring spectrum structure onE determines a natural cup product structure onE-cohomology
and E-cohomology with supports in the usual manner; we refrain from spelling it out in detail here.
Notation 3.3. For a scheme X and a rank r vector bundle V→ X, we let det V→ X denote the
determinant line bundle, deﬁned by det V:=3r V. Given two vector bundles V1→ X and V2→ X, we
have a canonical isomorphism
αV1,V2: det(V1⊕ V2)→(det V1)⊗OX(det V2),
characterized by requiring that, for a local basis of sections s1
1,..., s1
n of V1 and s2
1,..., s2
m of V2, we have
αV1,V2(((s1
1, 0)∧···∧ (s1
n, 0)∧(0, s2
1)∧···∧ (0, s2
m)))=(s1
1∧···∧ s1
n)⊗(s2
1∧···∧ s2
m).
This extends to a canonical natural isomorphism
αE: det V→(det V1)⊗OX(det V2)
for each exact sequence E of vector bundles on X,
0→ V1→ V→ V2→ 0;
one can deﬁne αE by choosing local splittings and noting that the resulting isomorphism is independent
of the choice of splitting.
Deﬁnition 3.4. An SL-orientation of a motivic commutative ring spectrum E in SH(B) is an assignment
of elements thV,θ∈ E2r,r(Th(V)) for each pair(V,θ) consisting of a rank r vector bundle V→ X (for any
r≥ 0) with X∈ SmB and an isomorphismθ: det V→ OX of line bundles, satisfying the following axioms:
(i) Naturality: Let(V→ X,θ: det V→ OX) be as above and let f: Y→ X be a morphism in SmB.
Consider the vector bundle f∗V→ Y and isomorphism f∗θ: det f∗V≃ f∗ det V→ OY . Then we
have f∗(thV,θ)= th f∗V, f∗θ.
Motivic Gauss–Bonnet formulas 1815
(ii) Products: Let (V1→ X,θ 1: det V1→ OX) and(V2→ X,θ 2: det V2→ OX) be two pairs as above.
Consider the vector bundle V1⊕V2→ X and the isomorphismθ1∧θ2: det(V1⊕V2)→ OX deﬁned by
θ1∧θ2:=(θ1⊗θ2)◦αV1,V2.
Then thV1⊕V2,θ1∧θ2= thV1,θ1∪ thV2,θ2.
(iii) Normalization: For X∈ SmB, consider the trivial vector bundle V= OX and the identity iso-
morphismθ: V→ OX. Then, under the canonical identiﬁcation Th(V)≃6TX+, the element
thV,θ∈ E2,1(Th(V)) is the image of the unit 1∈ E0,0(B) under the composition
E0,0(B) π∗
X−→E0,0(X)
suspension
≃ E2,1(6TX+).
An SL-oriented motivic spectrum is a pair(E, th(−)) with E a motivic commutative ring spectrum and
th(−) an SL-orientation on E.
Variant 3.5. A GL-orientation, or simply orientation, on a motivic commutative ring spectrum E is an
assignment(V→ X)↦→ thV∈ E2r,r(Th(V)), where V→ X is a rank r vector bundle (for any r≥ 0) on
X∈ SmB, satisfying the evident modiﬁcations of the axioms (i)–(iii) in Deﬁnition 3.4, i.e., omitting the
conditions on the determinant line bundle. The pair (E, th(−)) is called a GL-oriented motivic spectrum,
or more simply, an oriented motivic spectrum.
For the remainder of the section, we ﬁx an SL-oriented motivic spectrum E. Let us ﬁrst observe that
the SL-orientation determines Thom isomorphisms in E-cohomology for oriented vector bundles:
Lemma 3.6. Let(E, th(−)) be an SL-oriented motivic spectrum and let q: V→ X be a rank r vector
bundle on X∈ SmB with an isomorphismθ: det V→ OX. Then sending x∈ Ea,b
Z (X) to q∗(x)∪ thV,θ
deﬁnes an isomorphism
ϑV,θ: Ea,b
Z (X)→ Ea+2r,b+r
Z (Th(V))
natural in(X, V,θ) .
Proof. The naturality of the maps ϑV,θ follows from the naturality of the Thom classes, i.e., property (i)
in their deﬁnition.
It follows from properties (i)–(iii) of the Thom class that for V=⨁r
i=1 OXei andθ: det V→ OX the
canonical isomorphism given byθ(e1∧···∧ en)= 1, the mapϑV,θ is the suspension isomorphism
Ea,b
Z (X)≃ Ea+2r,b+r(6r
T X+/6r
T(X\ Z)+)≃ Ea+2r,b+r
Z (Th(V)).
The naturality of the maps ϑV,θ allow one to use a Mayer–Vietoris sequence for a trivializing open cover
of X for V to show thatϑV,θ is an isomorphism in general. □
The above Thom isomorphism may be extended to vector bundles without orientation by introducing
twists to E-cohomology, as follows.
1816 Marc Levine and Arpon Raksit
Deﬁnition 3.7. For X∈SmB and q:L→ X a line bundle, we deﬁne thetwisted E-cohomology E∗∗(X;L) by
Ea,b(X; L):= Ea+2,b+1(Th(L))= Ea+2,b+1
0L (L).
We also have a version with supports: given in addition a closed subset Z⊆ X, we deﬁne
Ea,b
Z (X; L):= Ea+2,b+1
0L∩q−1(Z)(L).
Finally, when we also have a vector bundle V→ X, we similarly deﬁne
Ea,b(Th(V); L):= Ea,b
0V (V; q∗L), Ea,b
Z (Th(V); L):= Ea,b
0V∩q−1(Z)(V; q∗L);
these deﬁnitions may be rewritten a bit, e.g., for the former we have
Ea,b(Th(V); L)= Ea,b
0V (V; q∗L)= Ea+2,b+1
0V⊕L (V⊕ L)= Ea+2,b+1(Th(V⊕ L)).
Remark 3.8. The product structure on E-cohomology extends to a product structure on twisted E-
cohomology: namely, for X∈ SmB and L, M two line bundles on X, combining the cup product
∪: Ea+2,b+1
0L (L)⊗ Ec+2,d+1
0M (M)→ Ea+c+4,b+d+2
0L⊕M (L⊕ M),
the canonical isomorphismαL,M: det(L⊕ M)→ L⊗ M, and the Thom isomorphismϑL⊕M, we get a map
∪: Ea,b(X; L)⊗ Ec,d(X; M)→ Ea+c,b+d(X; L⊗ M),
as well as a version with supports.
Remark 3.9. The deﬁnitions of twisted E-cohomology given in Deﬁnition 3.7 are instances of a more
general deﬁnition. Namely, for X∈ SmB, L→ X a line bundle, and any T∈ SH(B) equipped with an
identiﬁcation T≃πX♯(T′) for some T′∈ SH(X), we may deﬁne the twisted E-cohomology E∗∗(T; L) by
Ea,b(T; L):= HomSH(X)(6L T′, Sa+2,b+1∧π∗
X E).
Of course, this notation is abusive since E∗∗(T; L) really depends on T′∈ SH(X). This construction
recovers the notions introduced in Deﬁnition 3.7 as follows:
– We have E∗∗(X; L)≃ E∗∗(T; L) for T=6∞
T X+≃πX♯(1X).
– We have E∗∗
Z (X; L)≃ E∗∗(T; L) for T= X Z/B≃πX♯(X Z/ X).
– We have E∗∗(Th(V); L)≃ E∗∗(T; L) for T= Th(V)≃πX♯(ThX(V)).
The extra generality will be invoked later on (see Lemma 4.3) for the case
T= X Z/BB.M.=πX!(X Z/ XB.M.)≃πX♯(6−TX/B X Z/ XB.M.),
where the last identiﬁcation is by Atiyah duality (Remark 2.7).
The following construction is due to Ananyevskiy [2016a, Corollary 1].
Motivic Gauss–Bonnet formulas 1817
Construction 3.10. Let X∈ SmB, let q: V→ X be a rank r vector bundle, and let p: L→ X denote the
determinant bundle det V ; let p′: L−1→ X denote the inverse ofL. Then we have canonical isomorphisms
αV,L−1: det(V⊕ L−1)→ OX, α L−1⊕L: det(L−1⊕ L)→ OX.
Consider now the two pullback bundles
pV: q∗(L−1⊕ L)→ V, qL⊕ p′
L: p∗(V⊕ L−1)→ L,
which inherit trivializations of their determinants. For (E, th(−)) an SL-oriented motivic spectrum,
Lemma 3.6 gives us isomorphisms
ϑq∗(L−1⊕L),q∗αL−1⊕L
: Ea+2r,b+r
0V (V)→ Ea+2r+2,b+r+1
q−1(0L−1⊕0L)∩p−1
V (0V)(q∗(L−1⊕ L))
and
ϑp∗(V⊕L−1),p∗αV⊕L−1: Ea+2,b+1
0L (L)→ Ea+2r+2,b+r+1
p−1(0V⊕0L−1)∩p′−1
L (0V)(p∗(V⊕ L−1)).
However, as X-schemes q∗(L−1⊕ L) and p∗(V⊕ L−1) are both canonically isomorphic to
V⊕ L−1⊕ L→ X,
and via this isomorphism, the closed subsets q−1(0L−1⊕ 0L)∩ p−1
V (0V) and p−1(0V⊕ 0L−1)∩ p′−1
L (0V)
are both equal to 0 V⊕L−1⊕L. We thus have a canonical isomorphism
φ: Ea+2r+2,b+r+1
q−1(0L−1⊕0L)∩p−1
V (0V)(q∗(L−1⊕ L))→ Ea+2r+2,b+r+1
p−1(0V⊕0L−1)∩p′−1
L (0V)(p∗(V⊕ L−1))
Combining all of the above the, we obtain the Thom isomorphism
ϑV: Ea,b(X; L)→ Ea+2r,b+r(Th(V)), (3.10.1)
deﬁned by
ϑV:=ϑ−1
q∗(L−1⊕L),q∗αL−1⊕L
◦φ◦ϑp∗(V⊕L−1),p∗αV⊕L−1.
This construction extends to cohomology with supports in an evident manner.
We next discuss the Thom classes in twisted E-cohomology governing this more general Thom
isomorphism.
Deﬁnition 3.11. Let X∈ SmB and let q: V→ X be a rank r vector bundle. The canonical Thom class
thV∈ E2r,r(Th(V); det−1 V) is deﬁned as follows. As noted in Deﬁnition 3.7, we have
E2r,r(Th(V); det−1 V)= E2r+2,r+1(Th(V⊕ det−1 V)).
The isomorphism
α:=αV,det−1 V: det(V⊕ det−1 V)→ OX
gives us the Thom class thV⊕det−1 V,α∈ E2r+2,r+1(Th(V⊕ det−1 V)), and we deﬁne thV to be the corre-
sponding element of E2r,r(Th(V); det−1 V) under the above identiﬁcation.
1818 Marc Levine and Arpon Raksit
Remark 3.12. Let X and V be as in Deﬁnition 3.11. Let πX: X→ B denote the structure morphism.
Then the Thom class th V is an element of
E2r,r(Th(V); det−1 V)= E2r+2,r+1(πX♯(6V⊕det−1(V)(1X))
= HomSH(B)(πX♯(6V⊕det−1(V)(1X), S2r+2,r+1∧ E)
≃ HomSH(X)(6V⊕det−1(V)(1X), S2r+2,r+1∧π∗
X E)
≃ HomSH(X)(1X, S2r+2,r+1∧6−(V⊕det−1(V))π∗
X E).
Thus, via the multiplication on E, the class th V induces a map
×thV:π∗
X E→ S2r+2,r+1∧6−(V⊕det−1(V))π∗
X E
in SH(X).
Lemma 3.13. The map×thV deﬁned above is an isomorphism in SH(X).
Proof. For each object x∈ SH(X),×thV induces a map
ϑV,x: HomSH(X)(x,π∗
X E)→ HomSH(X)(x, S2r+2,r+1∧6−(V⊕det−1(V))π∗
X E)
By the Yoneda lemma, it sufﬁces to show that ϑV,x is an isomorphism for all x∈ SH(X).
The collection of objects x for whichϑV,x is an isomorphism is closed under arbitrary direct sums,
hence is a localizing subcategory of SH(X). The objects x= Sa,b∧ 1X are contained in this subcategory,
since for these objects the map ϑV,x identiﬁes with the Thom isomorphism θV⊕det−1(V),α (whereα is
as in Deﬁnition 3.11). For p: Y→ X in SmX, applying p∗ and using the adjunction with p♯ shows
that furthermore ϑV,x is an isomorphism for x= Sa,b∧ Y/ X. As SH(X) is generated as a localizing
subcategory by the objects Sa,b∧ Y/ X, this proves the lemma. □
Deﬁnition 3.14. For X∈ SmB and V→ X a rank r vector bundle, we deﬁne
ϑ E
V:61−det Vπ∗
X E→6r−Vπ∗
X E
to be the composition of isomorphisms
61−det Vπ∗
X E
6det V−1(×thdet V⊕det−1 V)−1
−−−−−−−−−−−−−−−→6det−1 V−1π∗
X E
61−det−1 V(×thV)
−−−−−−−−−→6r−Vπ∗
X E.
Remark 3.15. Let X∈ SmB and let V→ X be a rank r vector bundle. Under the identiﬁcation
Th(V)=πX#6V(1X) and the isomorphisms
Ea,b(X, det V)≃ HomSH(X)(1X, Sa+2,b+1∧6− det Vπ∗
X E)
and
E2r+a,r+b(Th(V))≃ HomSH(X)(1X, S2r+a,r+b∧6−Vπ∗
X E),
the Thom isomorphismϑV: Ea,b(X, det V)→ E2r+a,r+b(Th(V)) is the map induced by ϑ E
V .
Motivic Gauss–Bonnet formulas 1819
Remark 3.16. Let X∈ SmB and let V→ X and W→ X be vector bundles of respective ranksrV and rW .
We have the multiplication map
Ea,b(Th(V), det−1 V)⊗ Ec,d(Th(W), det−1 W)→ Ea+c,b+d(Th(V⊕ W), det−1(V⊕ W))
induced by the isomorphism
V/(V\{ 0V})∧X W/(W\{ 0W})→(V⊕ W)/(V⊕ W\{ 0V⊕W})
in H•(X) and our canonical isomorphism det(V)⊗ det(W)≃ det(V⊕ W). The multiplicative property
of the Thom classes (Deﬁnition 3.4(ii)) implies a similar multiplicativity for the canonical Thom classes:
thV⊕W= thV∪ thW.
This then implies, roughly speaking, that
“ϑ E
W⊕V=ϑ E
W◦ϑ E
V.”
More precisely, after using properties of6(−) to make the necessary identiﬁcations, the following diagram
commutes:
61−det(W⊕V)π∗
X E
ϑ E
det W⊕det V //
ϑ E
W⊕V

62−(det W⊕det V)π∗
X E ∼ //61−det W61−det Vπ∗
X E
61−det Wϑ E
E

6rW+rV−(W⊕V)π∗
X E 6rV−V61−det Wπ∗
X E
6rV−Vϑ E
W
oo 61−det W6rV−Vπ∗
X E∼
oo
Remark 3.17. Using Remark 3.16, the deﬁnition of ϑ E
− extends to virtual bundles by settingϑ E
V−W:=
ϑ E
V◦(ϑ E
W)−1=(ϑ E
W)−1◦ϑ E
V (with these identities understood as in Remark 3.16), giving the isomorphism
ϑ E
V−W:61−det V⊗det−1 Wπ∗
X E−→∼ 6rV−rW−V+Wπ∗
X E.
Remark 3.16 then extends directly to virtual bundles.
If we have an exact sequence 0→ V′→ V→ V′′→ 0, then the corresponding isomorphisms
6V≃6V′⊕V′′
and det V≃ det(V′⊕ V′′) transformϑ E
V toϑ E
V′⊕V′′.
Remark 3.18. If the SL-orientation on E extends to a GL-orientation, then all the results of this section for
SL-oriented theories hold for E in simpliﬁed form: we can omit all the twisting by line bundles and replace
61−det Vπ∗
X E withπ∗
X E using the Thom class th det V to deﬁne an isomorphism 6Tπ∗
X E≃6det Vπ∗
X E.
We close this section with one last result about twisted E-cohomology in the SL-oriented setting.
Proposition 3.19. Let X∈ SmB, let L, M be two line bundles on X, and let Z⊆ X a closed subset. Then
there is a natural isomorphism
ψL,M: E∗,∗
Z (X; L)→ E∗,∗
Z (X; L⊗ M⊗2).
1820 Marc Levine and Arpon Raksit
Proof. Let s: X→ L⊕ M be the zero-section. We have the Thom isomorphisms
E∗,∗
Z (X; L)≃ E∗+4,∗+2
s(Z) (L⊕ M; M−1), E∗,∗
Z (X; L⊗ M⊗2)≃ E∗+4,∗+2
s(Z) (L⊕ M; M).
Replacing L⊕ M by X and M by L, this reduces us to showing that there is a natural isomorphism
ψL: E∗,∗
Z (X; L)→ E∗,∗
Z (X; L−1)
For this, we follow the proof of [Ananyevskiy 2016a, Lemma 2]. We have the morphism of X-schemes
L⊕ L−1= L×X L−1 µ→ X×B A1
deﬁned byµ(x, y)= x· y; let Y:=µ−1(X×1). Setting L0:= L\0L and L−1
0 := L−1\0L, we see that Y
is a closed subscheme of L×X L−1 projecting isomorphically to L0 via p1 and isomorphically to L−1
0
via p2.
Consider the commutative diagram
Y //
p1

L×X L−1
p1

// L×X L−1/Y
¯p1

L0 // L // L/L0
whose rows are coﬁber sequences. As the ﬁrst two vertical maps are isomorphisms in H(B), the map ¯p1
induces an isomorphism
¯p1/B:(L×B L−1/Y)/B→ Th(L)/B
in SH(B). Similarly, we have the isomorphism
¯p2/B:(L×B L−1/Y)/B→ Th(L−1)/B
in SH(B). Replacing X with U:= X\ Z, we have the isomorphisms
¯p1U/B:(L×B L−1×X U/Y×X U)/B→ Th(L×X U)/B.
and
¯p2U/B:(L×B L−1×X U/Y×X U)/B→ Th(L−1×X U)/B
It follows that the arrows in following diagram are isomorphisms in SH(B) after applying−/B:
Th(L)/Th(L×X U)
(L×X L−1/Y)/(L×X L−1×X U/Y×X U)
p1
33
p2 ++
Th(L−1)/Th(L−1×X U)
Motivic Gauss–Bonnet formulas 1821
Finally, applying HomSH(B)(−,6∗+2,∗+1E) gives the desired isomorphism
ψL: E∗,∗
Z (X; L)→ E∗,∗
Z (X; L−1). □
