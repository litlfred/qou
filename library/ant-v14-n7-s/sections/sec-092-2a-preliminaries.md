---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-092-2a-preliminaries
section_title: "2A. Preliminaries"
section_number: null
pages: 139-143
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
will be used throughout.
Notation 2.1. Throughout, we let B denote a noetherian separated base scheme of ﬁnite Krull dimension.
Let SchB denote the category of quasiprojective B-schemes, that is, B-schemes X→ B that admit a
closed immersion i: X↪→ U over B, with U an open subscheme of PN
B for some N. Let Schpr
B denote the
subcategory of SchB with the same objects as SchB but with morphisms the proper morphisms. Let SmB
denote the full subcategory of SchB with objects the smooth (quasiprojective) B-schemes. (The same
notation will be used when working over schemes other than B.) For X a B-scheme, we will usually
denote the structure morphism by πX: X→ B.
Notation 2.2. Given X∈ SchB, we let SH(X) denote the stable motivic homotopy category over X. We
will rely on the six-functor formalism for this construction, as established in [Ayoub 2007; Hoyois 2017].
In particular, for each morphism f: Y→ X in SchB, one has the adjoint pairs of functors
SH(X)
f∗
// SH(Y)
f∗
oo and SH (Y)
f! // SH(X)
f!
oo ;
natural isomorphisms
(g f)∗≃ f∗g∗, ( g f)!≃ f!g!, ( g f)∗≃ g∗ f∗, ( g f)!≃ g! f!
for composable morphisms, with the usual associativity; a natural transformation η f
!∗: f!→ f∗, which is
an isomorphism if f is proper. There are various base-change morphisms, which we will recall as needed.
In addition, for f smooth, there is a further adjoint pair
SH(Y)
f♯ // SH(X)
f∗
oo .
There is also the symmetric monoidal structure on SH(X); we denote the tensor product by ∧X and
the unit by 1X∈ SH(X). For f a closed immersion, we have the adjoint pair f∗⊢ f! arising from a
corresponding adjoint pair in the unstable setting, so we will take f!= f∗ withη f
!∗= id. Similarly, if f is
an open immersion, we have a canonical isomorphism of adjoint pairs ( f#⊢ f∗)∼=( f!⊢ f!), so we take
f!= f# and f!= f∗.
We also have the unstable motivic homotopy category H•(X), which we recall is a localization of the
category Spc•(X) of presheaves of pointed simplicial sets on SmX. For Y→ X in SmX, we write Y+
for the presheaf represented by the X-scheme Y∐ X→ X, that is, the presheaf Z↦→ HomSmX(X, Y)+
(here(−)+ denotes addition of a disjoint basepoint to a set and we regard a set as a constant simplicial
set). The category Spc•(X) has a canonical symmetric monoidal structure with unit object X+, and
H•(X) inherits this structure via the localization functor. Finally, we have the inﬁnite suspension functor
6∞
T: H•(X)→ SH(X), which is canonically symmetric monoidal, so that in particular we have a canonical
identiﬁcation 1 X≃6∞
T X+.
1806 Marc Levine and Arpon Raksit
For f: Y→ X a smooth morphism in SchB, the adjoint pair f♯⊢ f∗ mentioned above for stable
motivic homotopy categories arises from an adjoint pair in the unstable setting,
H•(Y)
f♯ // H•(X)
f∗
oo ,
where the left adjoint is induced by the functor f#: Spc•(Y)→ Spc•(X) obtained as the left Kan extension
of the functor f#: SmY→ Spc•(X) sending p: W→ Y to( f◦ p: W→ X)+.
We often write−/ X for the functor 6∞
T : H•(X)→ SH(X), and if πX: X→ B is smooth, then
we write−/B for the functor πX#◦6∞
T : H•(X)→ SH(B). We use the same notation to denote the
precompositions of these functors with the functor (−)+: SmX→ H•(X).
Remark 2.3. For p: E→ X an afﬁne space bundle in SchB (that is, a torsor in the Zariski topology
for a vector bundle), the composition p♯◦ p∗ is an autoequivalence of SH(X) (this is a formulation of
homotopy invariance).
Notation 2.4 (the localization triangle). Let j: U→ X be an open immersion in SchB with (reduced)
complement i: Z→ X. We have the localization distinguished triangle of endofunctors on SH(X)
j! j!→ idSH(X)→ i∗i∗→ j! j![1], (2.4.1)
where the morphism j! j!→ idSH(X) is the counit of the adjunction j!⊢ j! and the morphism idSH(X)→ i∗i∗
is the unit of the adjunction i∗⊢ i∗. Moreover i∗= i!, j!= j# and j!= j∗.
We often write X Z/ X for i∗(1Z)∈ SH(X). With this notation (and that of Notation 2.2), applying
(2.4.1) to 1 X gives us the distinguished triangle in SH(X),
U/ X j/ X−−→X/ X→ X Z/ X→ U/ X[1];
in other words, we have a canonical isomorphism X Z/ X≃6∞
T (X/U); accordingly, we often write X Z
for the quotient presheaf X/U in H•(X).
Notation 2.5 (suspension and Thom spaces). Let p: V→ X be a vector bundle over some X∈ SchB,
with zero-section s: X↪→ V. We have the endofunctors
6−V,6 V: SH(X)→ SH(X)
deﬁned by 6−V:= s! p∗ and6V:= p♯◦ s∗. These are in fact inverse autoequivalences.
The endofunctor6V can also be written in terms of Thom spaces. Setting 0V:= s(X)⊂ V, the Thom
space of the vector bundle is deﬁned as
ThX(V):= V/(V\ 0V)∈ H•(X).
To lighten the notation, we often write ThX(V) for ThX(V)/ X=6∞
T (ThX(V))∈ SH(X), when the
context makes the meaning clear. For πX: X→ B in SmB, we set Th(V):=πX#(ThX(V)) in H•(B),
and we similarly write Th(V) for Th(V)/B≃πX#(ThX(V)/ X)∈ SH(B) when appropriate.
Motivic Gauss–Bonnet formulas 1807
To see the relation between the Thom space ThX(V) and the suspension functor 6V, consider the
localization distinguished triangle
j! j!→ idV→ s∗s∗→ j! j![1],
where s still denotes the zero section and j denotes the open complement V\ 0V ↪→ V. Evaluating the se-
quence at 1V and noting that j! j!= j# j∗ and s∗= s!, we obtain an identiﬁcation between ThX(V)∈ SH(X)
and p#s∗(1X)=6V(1X). Consequently, we have identiﬁcations πV #(s∗(1X))≃πX#(6V(1X))≃ Th(V).
In parallel, we shall writeThX(−V) for6−V(1X) and Th(−V) forπX#6−V(1X). With these notational
conventions, there are canonical natural isomorphisms
6V(−)≃ ThX(V)∧X(−), 6 −V(−)≃ ThX(−V)∧X(−). (2.5.1)
Remark 2.6. Let Dperf(X)iso denote the subcategory of isomorphisms in the perfect derived category
Dperf(X) and let K(X) denote the groupoid associated to the K-theory space of X. Then the assignment
V↦→6V extends to a functor
6(−): Dperf(X)iso→ Aut(SH(X)),
and moreover factors through the canonical functor Dperf(X)iso→ K(X), so that a distinguished triangle
E′→ E→ E′′→ E′[1] in Dperf(X) determines a natural isomorphism6 E′
◦6 E′′
≃6 E. See for example
[Riou 2010, Proposition 4.1.1] for a proof of this last statement in the special case concerning the functor
ThX(−)=6(−)(1X): Dperf(X)iso→ SH(X) (which in fact implies the general statement by (2.5.1)).
In this context, for an integer n, we sometimes write n for the trivial bundle of virtual rank n; for
example,6n+E≃6n
P1◦6 E for E in Dperf(X).
Remark 2.7 (Atiyah duality). For f: Y→ X a smooth morphism in SchB with relative tangent bundle
T f→ Y, there are canonical natural isomorphisms
f!≃ f♯◦6−T f, f!≃6T f◦ f∗;
see [Hoyois 2017, Theorem 6.18(2)]. In addition, for f as above and V→ X a vector bundle, there are
canonical natural isomorphisms
f♯◦6± f∗V≃6±V◦ f♯, f∗◦6±V≃6±V◦ f∗,
the latter valid for an arbitrary morphism f: Y→ X in SmB. Moreover, for f: Y→ X an arbitrary
morphism in Sch B and V→ X a vector bundle, there is a canonical natural isomorphism
f!◦6±V≃6± f∗V◦ f!;
see the beginning of [Hoyois 2017, §5.2]. Finally, for f: Y→ X a regular embedding in SchB with
normal bundle N f→ Y, there is a canonical natural isomorphism
f!≃6−N f◦ f∗.
1808 Marc Levine and Arpon Raksit
In fact, the isomorphism f!≃6T f◦ f∗ for smooth f extends to the case of an lci morphism, as
follows. For f: Y→ X an lci morphism in SchB, we factor f as f= p◦ i with i: Y→ Z a regular
embedding and p: Z→ X a smooth morphism (both in SchB). This gives the relative virtual normal
bundleν f:=[ Ni]−[ i∗TZ/ X] in K(Y), independent up to canonical isomorphism on the choice of the
factorization. Thus, we have the canonically deﬁned suspension automorphism 6−ν f and a canonical
natural isomorphism
f!= i!◦ p!≃6−Ni◦ i∗◦6TZ/ X◦ p∗≃6−ν f◦ f∗.
One can then construct a left adjoint f♯ to f∗ by setting
f♯:= f!◦6ν f.
The functoriality (g f)∗= f∗◦ g∗ gives rise to the functoriality on the adjoints (g f)♯= g♯◦ f♯ for
composable lci morphisms.
Notation 2.8. Letπ: Z→ X be a morphism in Sch B. For Y∈ H•(Z), we set
Y/ XB.M.:=π!(6∞
T Y)∈ SH(X),
and for Y∈ SmZ, we make the abbreviation Y/ XB.M. for Y+/ XB.M.=π!(6∞
T Y+). In particular, we by
deﬁnition have Z/ XB.M.=π!(1Z)∈ SH(X).
Furthermore, for i: W↪→ Z the inclusion of a reduced closed subscheme, we set
ZW/ XB.M.:=π!(i∗(1W)).
We observe two facts about this object. Firstly, lettingπ′ denote the compositeπ◦i: W→ X, the isomor-
phismπ′
!=π!◦i∗ determines an isomorphism ZW/ XB.M.≃ W/ XB.M.. Secondly, let j: U:= Z\ W→ Z
denote the open complement of W and consider the localization distinguished triangle
j! j!→ idSH(Z)→ i∗i∗.
Then the identities j!= j∗ and i∗= i! give a canonical distinguished triangle in SH(X),
U/ XB.M.→ Z/ XB.M.→ ZW/ XB.M.→ U/ XB.M.[1].
Remark 2.9. The assignment Z↦→ Z/ XB.M. extends to a functor
(−)/ XB.M.:(Schpr
X)op→ SH(X).
This is described in a number of places, for example [Levine 2017a, §1]; we recall the construction for
the reader’s convenience, referring to [loc. cit.] for details.
Let g: Z→ Y be a proper morphism in SchX. Let πY: Y→ X andπZ: Z→ X denote the structural
morphisms. As mentioned in Notation 2.2, we have a natural isomorphism ηg
!∗: g!≃ g∗. We may then
deﬁne a natural transformation g∗:πY!→πZ!g∗ as the composition
πY!
ug−→πY!g∗g∗(ηg
!∗)−1
−−→πY!g!g∗≃πZ!g∗,
Motivic Gauss–Bonnet formulas 1809
where ug: idSH(Y)→ g∗g∗ is the unit of the adjunction. Evaluating this natural transformation at1Y gives a
map g∗= g/ XB.M.: Y/ XB.M.→ Z/ XB.M., and it follows directly from the deﬁnitions that this construction
satisﬁes(gh)∗= h∗g∗ for composable proper morphisms g, h. This establishes the claimed functoriality.
