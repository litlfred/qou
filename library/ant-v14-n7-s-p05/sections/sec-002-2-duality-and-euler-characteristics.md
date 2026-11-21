---
doc_id: ant-v14-n7-s-p05
doc_title: "Motivic Gauss–Bonnet formulas"
section_id: sec-002-2-duality-and-euler-characteristics
section_title: "Duality and Euler characteristics"
section_number: 2
pages: 4-13
source_pdf: ant-v14-n7-s-p05.pdf
source_sha256: 1c8e94ff62a8d920
toc_source: inferred
doc_brief: "Motivic Gauss–Bonnet formulas — 12 sections: Front matter; Introduction; X+ ∈SH(k) is dualizable. In partic"
---
In this section, we review the strong dualizability of smooth projective schemes as objects of the stable
motivic homotopy category, which supplies a notion of Euler characteristic for these schemes. We also
recall a result from [Levine 2017b] that gives an alternative characterization of this Euler characteristic.
Motivic Gauss–Bonnet formulas
1805
2A. Preliminaries. Let us ﬁrst recall the basic framework of stable motivic homotopy theory, which
will be used throughout.
Notation 2.1. Throughout, we let B denote a noetherian separated base scheme of ﬁnite Krull dimension.
Let SchB denote the category of quasiprojective B-schemes, that is, B-schemes X →B that admit a
closed immersion i : X ,→U over B, with U an open subscheme of PN
B for some N. Let Schpr
B denote the
subcategory of SchB with the same objects as SchB but with morphisms the proper morphisms. Let SmB
denote the full subcategory of SchB with objects the smooth (quasiprojective) B-schemes. (The same
notation will be used when working over schemes other than B.) For X a B-scheme, we will usually
denote the structure morphism by πX : X →B.
Notation 2.2. Given X ∈SchB, we let SH(X) denote the stable motivic homotopy category over X. We
will rely on the six-functor formalism for this construction, as established in [Ayoub 2007; Hoyois 2017].
In particular, for each morphism f : Y →X in SchB, one has the adjoint pairs of functors
SH(X)
f ∗
/ SH(Y)
f∗
o
and
SH(Y)
f!
/ SH(X)
f !
o
;
natural isomorphisms
(g f )∗≃f ∗g∗,
(g f )! ≃f !g!,
(g f )∗≃g∗f∗,
(g f )! ≃g! f!
for composable morphisms, with the usual associativity; a natural transformation η f
!∗: f! →f∗, which is
an isomorphism if f is proper. There are various base-change morphisms, which we will recall as needed.
In addition, for f smooth, there is a further adjoint pair
SH(Y)
f♯
/ SH(X)
f ∗
o
.
There is also the symmetric monoidal structure on SH(X); we denote the tensor product by ∧X and
the unit by 1X ∈SH(X). For f a closed immersion, we have the adjoint pair f∗⊣f ! arising from a
corresponding adjoint pair in the unstable setting, so we will take f! = f∗with η f
!∗= id. Similarly, if f is
an open immersion, we have a canonical isomorphism of adjoint pairs ( f# ⊣f ∗) ∼= ( f! ⊣f !), so we take
f! = f# and f ! = f ∗.
We also have the unstable motivic homotopy category H•(X), which we recall is a localization of the
category Spc•(X) of presheaves of pointed simplicial sets on SmX. For Y →X in SmX, we write Y+
for the presheaf represented by the X-scheme Y ⨿X →X, that is, the presheaf Z 7→HomSmX(X, Y)+
(here (−)+ denotes addition of a disjoint basepoint to a set and we regard a set as a constant simplicial
set). The category Spc•(X) has a canonical symmetric monoidal structure with unit object X+, and
H•(X) inherits this structure via the localization functor. Finally, we have the inﬁnite suspension functor
6∞
T :H•(X)→SH(X), which is canonically symmetric monoidal, so that in particular we have a canonical
identiﬁcation 1X ≃6∞
T X+.
1806
Marc Levine and Arpon Raksit
For f : Y →X a smooth morphism in SchB, the adjoint pair f♯⊣f ∗mentioned above for stable
motivic homotopy categories arises from an adjoint pair in the unstable setting,
H•(Y)
f♯
/ H•(X)
f ∗
o
,
where the left adjoint is induced by the functor f# : Spc•(Y) →Spc•(X) obtained as the left Kan extension
of the functor f# : SmY →Spc•(X) sending p : W →Y to ( f ◦p : W →X)+.
We often write −/X for the functor 6∞
T : H•(X) →SH(X), and if πX : X →B is smooth, then
we write −/B for the functor πX# ◦6∞
T : H•(X) →SH(B). We use the same notation to denote the
precompositions of these functors with the functor (−)+ : SmX →H•(X).
Remark 2.3. For p : E →X an afﬁne space bundle in SchB (that is, a torsor in the Zariski topology
for a vector bundle), the composition p♯◦p∗is an autoequivalence of SH(X) (this is a formulation of
homotopy invariance).
Notation 2.4 (the localization triangle). Let j : U →X be an open immersion in SchB with (reduced)
complement i : Z →X. We have the localization distinguished triangle of endofunctors on SH(X)
j! j! →idSH(X) →i∗i∗→j! j![1],
(2.4.1)
where the morphism j! j! →idSH(X) is the counit of the adjunction j! ⊣j! and the morphism idSH(X) →i∗i∗
is the unit of the adjunction i∗⊣i∗. Moreover i∗= i!, j! = j# and j! = j∗.
We often write X Z/X for i∗(1Z) ∈SH(X). With this notation (and that of Notation 2.2), applying
(2.4.1) to 1X gives us the distinguished triangle in SH(X),
U/X
j/X
−−→X/X →X Z/X →U/X[1];
in other words, we have a canonical isomorphism X Z/X ≃6∞
T (X/U); accordingly, we often write X Z
for the quotient presheaf X/U in H•(X).
Notation 2.5 (suspension and Thom spaces). Let p : V →X be a vector bundle over some X ∈SchB,
with zero-section s : X ,→V. We have the endofunctors
6−V, 6V : SH(X) →SH(X)
deﬁned by 6−V := s! p∗and 6V := p♯◦s∗. These are in fact inverse autoequivalences.
The endofunctor 6V can also be written in terms of Thom spaces. Setting 0V := s(X) ⊂V, the Thom
space of the vector bundle is deﬁned as
ThX(V ) := V/(V \ 0V ) ∈H•(X).
To lighten the notation, we often write ThX(V ) for ThX(V )/X = 6∞
T (ThX(V )) ∈SH(X), when the
context makes the meaning clear. For πX : X →B in SmB, we set Th(V ) := πX#(ThX(V )) in H•(B),
and we similarly write Th(V ) for Th(V )/B ≃πX#(ThX(V )/X) ∈SH(B) when appropriate.
Motivic Gauss–Bonnet formulas
1807
To see the relation between the Thom space ThX(V ) and the suspension functor 6V, consider the
localization distinguished triangle
j! j! →idV →s∗s∗→j! j![1],
where s still denotes the zero section and j denotes the open complement V \0V ,→V. Evaluating the se-
quence at 1V and noting that j! j! = j# j∗and s∗= s!, we obtain an identiﬁcation between ThX(V ) ∈SH(X)
and p#s∗(1X) = 6V (1X). Consequently, we have identiﬁcations πV #(s∗(1X)) ≃πX#(6V (1X)) ≃Th(V ).
In parallel, we shall write ThX(−V ) for 6−V (1X) and Th(−V ) for πX#6−V (1X). With these notational
conventions, there are canonical natural isomorphisms
6V (−) ≃ThX(V ) ∧X (−),
6−V (−) ≃ThX(−V ) ∧X (−).
(2.5.1)
Remark 2.6. Let Dperf(X)iso denote the subcategory of isomorphisms in the perfect derived category
Dperf(X) and let K(X) denote the groupoid associated to the K-theory space of X. Then the assignment
V 7→6V extends to a functor
6(−) : Dperf(X)iso →Aut(SH(X)),
and moreover factors through the canonical functor Dperf(X)iso →K(X), so that a distinguished triangle
E′ →E →E′′ →E′[1] in Dperf(X) determines a natural isomorphism 6E′ ◦6E′′ ≃6E. See for example
[Riou 2010, Proposition 4.1.1] for a proof of this last statement in the special case concerning the functor
ThX(−) = 6(−)(1X) : Dperf(X)iso →SH(X) (which in fact implies the general statement by (2.5.1)).
In this context, for an integer n, we sometimes write n for the trivial bundle of virtual rank n; for
example, 6n+E ≃6n
P1 ◦6E for E in Dperf(X).
Remark 2.7 (Atiyah duality). For f : Y →X a smooth morphism in SchB with relative tangent bundle
T f →Y, there are canonical natural isomorphisms
f! ≃f♯◦6−T f ,
f ! ≃6T f ◦f ∗;
see [Hoyois 2017, Theorem 6.18(2)]. In addition, for f as above and V →X a vector bundle, there are
canonical natural isomorphisms
f♯◦6± f ∗V ≃6±V ◦f♯,
f ∗◦6±V ≃6±V ◦f ∗,
the latter valid for an arbitrary morphism f : Y →X in SmB. Moreover, for f : Y →X an arbitrary
morphism in SchB and V →X a vector bundle, there is a canonical natural isomorphism
f ! ◦6±V ≃6± f ∗V ◦f !;
see the beginning of [Hoyois 2017, §5.2]. Finally, for f : Y →X a regular embedding in SchB with
normal bundle N f →Y, there is a canonical natural isomorphism
f ! ≃6−N f ◦f ∗.
1808
Marc Levine and Arpon Raksit
In fact, the isomorphism f ! ≃6T f ◦f ∗for smooth f extends to the case of an lci morphism, as
follows. For f : Y →X an lci morphism in SchB, we factor f as f = p ◦i with i : Y →Z a regular
embedding and p : Z →X a smooth morphism (both in SchB). This gives the relative virtual normal
bundle ν f := [Ni] −[i∗TZ/X] in K(Y), independent up to canonical isomorphism on the choice of the
factorization. Thus, we have the canonically deﬁned suspension automorphism 6−ν f and a canonical
natural isomorphism
f ! = i! ◦p! ≃6−Ni ◦i∗◦6TZ/X ◦p∗≃6−ν f ◦f ∗.
One can then construct a left adjoint f♯to f ∗by setting
f♯:= f! ◦6ν f .
The functoriality (g f )∗= f ∗◦g∗gives rise to the functoriality on the adjoints (g f )♯= g♯◦f♯for
composable lci morphisms.
Notation 2.8. Let π : Z →X be a morphism in SchB. For Y ∈H•(Z), we set
Y/XB.M. := π!(6∞
T Y) ∈SH(X),
and for Y ∈SmZ, we make the abbreviation Y/XB.M. for Y+/XB.M. = π!(6∞
T Y+). In particular, we by
deﬁnition have Z/XB.M. = π!(1Z) ∈SH(X).
Furthermore, for i : W ,→Z the inclusion of a reduced closed subscheme, we set
ZW/XB.M. := π!(i∗(1W)).
We observe two facts about this object. Firstly, letting π′ denote the composite π ◦i : W →X, the isomor-
phism π′
! = π! ◦i∗determines an isomorphism ZW/XB.M. ≃W/XB.M.. Secondly, let j : U := Z \W →Z
denote the open complement of W and consider the localization distinguished triangle
j! j! →idSH(Z) →i∗i∗.
Then the identities j! = j∗and i∗= i! give a canonical distinguished triangle in SH(X),
U/XB.M. →Z/XB.M. →ZW/XB.M. →U/XB.M.[1].
Remark 2.9. The assignment Z 7→Z/XB.M. extends to a functor
(−)/XB.M. : (Schpr
X )op →SH(X).
This is described in a number of places, for example [Levine 2017a, §1]; we recall the construction for
the reader’s convenience, referring to [loc. cit.] for details.
Let g : Z →Y be a proper morphism in SchX. Let πY : Y →X and πZ : Z →X denote the structural
morphisms. As mentioned in Notation 2.2, we have a natural isomorphism ηg
!∗: g! ≃g∗. We may then
deﬁne a natural transformation g∗: πY! →πZ!g∗as the composition
πY!
ug
−→πY!g∗g∗(ηg
!∗)−1
−−→πY!g!g∗≃πZ!g∗,
Motivic Gauss–Bonnet formulas
1809
where ug : idSH(Y) →g∗g∗is the unit of the adjunction. Evaluating this natural transformation at 1Y gives a
map g∗= g/XB.M. :Y/XB.M. →Z/XB.M., and it follows directly from the deﬁnitions that this construction
satisﬁes (gh)∗= h∗g∗for composable proper morphisms g, h. This establishes the claimed functoriality.
2B. Duality for smooth projective schemes. Let (C, ⊗, 1, µ, τ) be a symmetric monoidal category.
Recall that the dual of an object x of C is a triple (y, δ, ϵ) with δx : 1 →x ⊗y and ϵx : y ⊗x →1 maps
such that the two compositions
x µ−1
−→1 ⊗x δx⊗idx
−−−→x ⊗y ⊗x idx⊗ϵx
−−−→x ⊗1 µ→x
and
y µ−1
−→y ⊗1 idy⊗δx
−−−→y ⊗x ⊗y ϵx⊗idy
−−−→1 ⊗y µ→y
are equal to the respective identity maps (this notion goes back to [Dold and Puppe 1980]; see [May
2001] for details). In this subsection, we recall from [Hoyois 2017] the construction of the dual of a
smooth projective scheme in the stable motivic homotopy category.
Remark 2.10. Let (C, ⊗, 1, µ, τ) be a symmetric monoidal category and let x ∈C. If a triple (y, δ, ϵ)
satisfying the above deﬁnition of the dual exists, then it is unique up to unique isomorphism. We often
omit speciﬁc mention of δ and ϵ and denote the dual object y by x∨.
When x admits a dual (x∨, δ, ϵ), then it is immediate that x∨is also dualizable, with dual (x, τ ◦δ, τ ◦ϵ),
so that x is canonically isomorphic to (x∨)∨.
Sending x 7→x∨extends to a contravariant functor (−)∨on the full subcategory of C consisting
of those objects x that admit a dual with canonical isomorphism, and the above determines a natural
isomorphism ((−)∨)∨≃id. For f : x →z a morphism of dualizable objects in C, the dual morphism
f ∨: z∨→x∨is the composition
z∨µ−1
−→z∨⊗1
idz∨⊗δx
−−−−→z∨⊗x ⊗x∨id⊗f ⊗id
−−−−→z∨⊗z ⊗x∨ϵz⊗idx∨
−−−→1 ⊗x∨µ→x∨.
Lemma 2.11. Let πX : X →B be an object of SmB. View X ×B X as a X-scheme via the projection
p2 : X ×B X →X onto the second factor. Then there are canonical isomorphisms
π∗
X(X/BB.M.) ≃p2♯6−p∗
1TX/B(1X×B X) ≃X ×B X/XB.M.
in SH(X) and a canonical isomorphism
πX♯(X ×B X/XB.M.) ≃X/BB.M. ∧B X/B
in SH(B).
Proof. Consider the commutative square
X ×B X
p2
/
p1

X
πX

X
πX
/ B
1810
Marc Levine and Arpon Raksit
This gives us the canonical isomorphism
TX×B X/X ≃p∗
1TX/B.
We have the identities and canonical isomorphisms
π∗
X(X/BB.M.) = π∗
XπX!(1X) ≃π∗
XπX♯6−TX/B(1X)
(base change)
≃
p2♯p∗
16−TX/B(1X)
≃p2♯6−p∗
1TX/B(p∗
11X) = p2♯6−p∗
1TX/B(1X×B X)
which gives us the ﬁrst isomorphism in SH(X). The second follows from
p2♯6−p∗
1TX/B(1X×B X) ≃p2♯6−TX×B X/X(1X×B X) ≃p2!(1X×B X) = X ×B X/XB.M..
Finally, to give the isomorphism in SH(B), we have
πX♯(X ×B X/XB.M.) ≃πX♯(p2♯(6−TX×B X/X(1X×B X)) ≃πX♯p1♯(6−TX×B X/X(1X×B X))
≃πX♯p1♯(6−p∗
1TX/B(1X×B X)) ≃πX♯6−TX/B p1♯(1X×B X) ≃πX! p1♯p∗
2(1X)
(base change)
≃
πX!π∗
XπX♯(1X) ≃πX!(1X ∧X π∗
X(X/B))
(projection formula)
≃
πX!(1X) ∧B (X/B) = X/BB.M. ∧B X/B.
The base change isomorphisms follow from [Hoyois 2017, Theorem 6.18(3)] and the projection formula
is [Hoyois 2017, Theorem 6.18(7)].
□
Construction 2.12. Let πX : X →B be an object of SmB that is proper (i.e., a smooth projective scheme
over B). We recall (from [Hoyois 2017], but see also the constructions of [Riou 2005; Ayoub 2007]) the
construction of a duality between the objects X/B and X/BB.M. in SH(B).
We ﬁrst construct the coevaluation map δX/B : 1B →X/B ∧B X/BB.M.. Applying the functoriality of
(−)/BB.M. from Remark 2.9 to the proper map πX gives the map
π∗
X : 1B = B/BB.M. →X/BB.M. = πX!(1X) ≃πX♯(6−TX/B(1X))
in SH(B), and the diagonal 1X/B : X →X ×B X induces via the functoriality of (−)/X : SmX →SH(X)
the map
1X/B∗:= 1X/B/X : 1X = X/X →X ×B X/X
in SH(X). We may put together these two maps to obtain the composition
1B
π∗
X
−→πX♯(6−TX/B(1X))
πX♯6−TX/B (1X/B∗)
−−−−−−−−−−→πX♯6−TX/B(X ×B X/X),
Using the identiﬁcation πX♯6−TX/B(X ×B X/X) ≃X/B ∧B X/BB.M. from Lemma 2.11, this gives the
desired map δX/B.
Motivic Gauss–Bonnet formulas
1811
We now construct the evaluation map ϵX/B : X/BB.M.∧B X/B →1B (which does not require properness
of πX). Here we apply the functoriality of (−)/XB.M. to the proper map 1X/B to obtain the map
1∗
X/B : X ×B X/XB.M. →X/XB.M. = 1X
in SH(X), and the functoriality of (−)/B to the map πX to obtain the map
πX∗: X/B →B/B = 1B.
Putting these together yields the composition
πX♯(X ×B X/XB.M.) πX/B♯(1∗)
−−−−−→πX/B♯(1X) = X/B πX∗
−→1B.
Now using the identiﬁcation X/BB.M. ∧B X/B ≃πX♯(X ×B X/XB.M.) from Lemma 2.11, we get the
desired map ϵX/B.
It is shown in [Hoyois 2017, Corollary 6.13] that the triple (X/BB.M., δX/B, ϵX/B) is the dual of X/B
in SH(B). Using our notation for Thom spaces, we have
X/BB.M. = πX!(1X) ≃πX# ◦6−TX/B(1X) = ThX(−TX/B)/B,
the coevaluation map is
δX/B : 1B →X/B ∧B ThX(−TX/B)/B
and the evaluation map is
ϵX/B : ThX(−TX/B)/B ∧B X/B →1B
The dualizability of X/B as above allows one to deﬁne an Euler characteristic for smooth projective
schemes:
Deﬁnition 2.13. For X →B in SmB and proper, the Euler characteristic χ(X/B) ∈EndSH(B)(1B) is the
composition
1B
δX/B
−−→X/B ∧B ThX(−TX/B)/B τ→ThX(−TX/B)/B ∧B X/B
ϵX/B
−−→1B,
where τ denotes the symmetry isomorphism, and δX/B and ϵX/B are as in Construction 2.12.
To ﬁnish this section, we give an alternative characterization of the Euler characteristic χ(X/B) just
deﬁned (Lemma 2.15 below). We proved this result in the case B = Spec k for k a ﬁeld in [Levine 2017b];
the proof in this more general setting is exactly the same.
Construction 2.14. We consider X ×B X as a smooth X-scheme via the projection p2. The diagonal
1X : X →X ×B X gives a section to p2. Let q : X ×B X →X ×B X/(X ×B X \1X(X)) be the quotient
map. We have the Morel–Voevodsky purity isomorphism [1999, Theorem 3.2.23], which gives the
isomorphism in H•(X)
mv1 : X ×B X/(X ×B X \ 1X(X)) −→
∼
ThX(N1X).
1812
Marc Levine and Arpon Raksit
Composing the 0-section sN :X →N1X with the quotient map N1X →Th(N1X) deﬁnes ¯sN :X →ThX(N1X).
It follows from the proof of the purity isomorphism that we have the commutative diagram in H•(X)
X ×B X+
q
/ X ×B X/(X ×B X \ 1X(X))
mv1 / ThX(N1X)
X+
q◦1X
O
¯sN
5
1X
h
(2.14.1)
Finally, we have the isomorphism N1X ≃TX/B of vector bundles over X furnished by the composition
TX/B −→
∼
1∗
X p∗
2TX/B
i2→1∗
X(p∗
1TX/B ⊕p∗
2TX/B) ≃1∗
XTX×B X/B
π→N1X,
where π : 1∗
XTX×B X/B →N1X is the canonical projection. Putting these maps together gives us the
composition in H•(X)
X+
1X
−→X ×B X q→X ×B X/(X ×B X \ 1X(X)) mv1
−−→ThX(N1X) −→
∼
ThX(TX/B);
the commutativity of (2.14.1) shows that this composition is equal to the map ¯sTX/B : X+ →ThX(TX/B),
induced as for ¯sN1X by the zero-section sTX/B : X →TX/B.
Applying 6−TX/B6∞
P1(−) and the isomorphism
6−TX/BTh(TX/B) ≃6−TX/B ◦6TX/B(1X) ≃1X
gives the morphism
˜βX/B : 6−TX/B(1X) →1X
in SH(X). Finally, applying πX# gives the morphism
βX/B : Th(−TX/B) →X/B
in SH(B).
Summarizing our construction, βX/B is given by applying πX# to the composition in SH(X)
6−TX/B(1X) 6−TX/B (1X)
−−−−−−→6−TX/B(X ×B X/X) 6−TX/B (q)
−−−−−→6−TX/B([X ×B X/(X ×B X \1X)]/X)
6−TX/B (mv1X )
−−−−−−−→6−TX/B(ThX(N1X)) ≃6−TX/B(ThX(TX/B)) ≃6−TX/B ◦6TX/B(1X) ≃1X
(2.14.2)
or equivalently, to the composition
6−TX/B(1X)
6−TX/B (¯sTX/B )
−−−−−−−→6−TX/B(ThX(TX/B)) ≃6−TX/B ◦6TX/B(1X) ≃1X
(2.14.3)
Lemma 2.15. For X smooth and proper over B, χ(X/B) is equal to the composition
1B
π∗
X
−→Th(−TX/B)
βX/B
−−→X/B
πX∗
−→1B
Motivic Gauss–Bonnet formulas
1813
Proof. Let pi : X ×B X →X, i = 1, 2, be the projections. The map
evX : X/B∨∧B X/B →1B
is the composition
X/B∨∧B X/B = Th(−TX/k) ∧B X/B = Th(−p∗
1TX/k) q→Th(−p∗
1TX/B)/Th(−j∗p∗
1TX/B)
≃Th(−TX/B ⊕N1X) ≃Th(−TX/B ⊕TX/B) ≃X/B πX
−→1B.
From our description of βX/B as πX# applied to the composition (2.14.2), we see that πX∗◦βX/B =
evX/B ◦Th(1X). Also, π∗
X = π∨
X and π∨
X is given by
1B
δX/B
−−→X/B ∧B X/B∨= Th(−p∗
2TX/B)
p2
−→Th(−TX/B)
It follows from the construction of the map δX/B described above that
δX/B = Th(1X) ◦π∗
X.
This gives us the commutative diagram
X/B ∧B X/B∨
τX,X∨
/ X/B∨∧B X/B
evX
'
1B
δX/B
7
π∗
X
'
Th(−p∗
2TX/B)
τX,X∨
/ Th(−p∗
1TX/B)
1B
Th(−TX/B)
Th(1X)
5
Th(1X)
O
βX/B
/ X/B
πX∗
7
□
