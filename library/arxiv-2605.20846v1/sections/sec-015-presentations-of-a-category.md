---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li"
section_id: sec-015-presentations-of-a-category
section_title: "Presentations of a Category"
section_number: null
pages: 90-92
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere Chris Li — We give two presentations for bordisms ofS 2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
Definition A.1.1.(Free Category) LetGbe a directed graph. Thefree category
F(G) has objects the vertices ofGand morphisms all composable arrows. The empty
path is the identity of a vertex.
Definition A.1.2.(Binary Relation) LetCbe a category anda,b∈obj(C). Abi-
nary relationR a,b on HomC(a,b) is a subsetR a,b⊂Hom C(a,b)×Hom C(a,b). We
writefR a,bgif (f,g)∈R a,b. We sayRis abinary relation on homsofCif
R={R a,b|a,b∈obj(C)}is a collection of binary relations on all pairs of objects ofC.
If a pair of morphisms (f,f ′) is inR a,b, we writefR a,bf′, orf=f ′ if the context is
clear.
Definition A.1.3.(Congruence) AcongruenceRon a categoryCis an assignment
to each pair of objectsa,b∈obj(C) an equivalence relationR a,b on HomC(a,b) that is
compatible with compositions: iffR a,bf′, meaning if (f,f ′) are equivalent, then for all
g:a ′→aand allh:b→b ′ one has (hfg)R a′,b′(hf′g); ifeR b,ce′, then (ef)R a,c(e′f′).
We sometimes writef∼ R f′ instead to denote the fact thatRis a congruence rather
than a binary relation.
Theorem A.1.4.(First isomorphism theorem of category theory) LetH:C → D
be a functor. ThenHdefines a congruence≡ H onCbyf≡ H f′ if and only if
H(f) =H(f ′). Moreover,Hfactors uniquely through the quotient:H= H◦Qwhere
Q:C→C/≡ H and H:C/≡ H→Dwhere H(a) =H(a)and H([f]) =H(f).
Proof.≡ H is obviously symmetric, reflexive, and transitive. Functoriality ofHguar-
antees that≡ H is compatible with compositions. The functor His well defined by
definition, and His unique since any functorH ′ withH=H ′◦Qmust satisfy
H′([f]) =H ′(Q(f)) =H(f) for any morphism inC/≡ H. SinceQis identity on
objects,H ′ must coincide withH(and hence H) on objects also. This completely
determinesH ′ as the same as H.
Lemma A.1.5.(Least Congruence) Given any binary relationsRon homs ofC, there
is a least congruenceR ′ onCwithR⊂R ′.
90
Definition A.1.6.(Quotient Category) LetCbe a category andRa congruence on
C. Then thequotient categoryC/Rhas the same objects asCand the morphisms
HomC/R(a,b) = HomC(a,b)/Ra,b are those ofCmodulo the equivalence relationR a,b.
IfRis a binary relation, the quotient categoryC/Ris defined asC/R ′ whereR′ is
the least congruence containingR.
Proposition A.1.7.(Universal Property of Quotient Category) [Mac94] LetCbe a
category withRa binary relation on the homs. LetC/Rbe the quotient category.
Then the quotient functorQ=Q R :C → C/R, which is identity on objects and
sends a morphism to its equivalence class, 1 satisfy the following universal property: If
H:C→Dis any functor such thatfR a,bf′ impliesHf=Hf ′ for allfandf ′, then
there exists a unique functorH ′ :C/R→DwithH ′◦QR =H.
Definition A.1.8.(Generators and Relations) LetGbe a directed graph andRa
binary relation onF(G), the free category ofG. Then we sayF(G)/Rhasgenerators
GandrelationsR. An isomorphismF(G)/R→Cand⟨G|R⟩form apresentation
ofC. We say the morphisms ofCaregeneratedby the edges ofGand the objects by
the vertices, and that the binary relationRissufficient.
RemarkA.1.9.Sufficiency of relations is equivalent to the following more convenient
description: LetGbe a directed graph andRa binary relation onF(G). Let H:
F(G)/R→Cbe a functor, whereF(G)/Rdenotes the quotient categoryF(G)/∼ R
for∼ R the least congruence containingR. Consider the functorH:F(G)→Cwhich
is the compositionH= H◦Q. ThenRbeing sufficient (equivalently Hbeing an
isomorphism) is the same as Hbeing bijective on objects and on homs. But sinceQ
is bijective on objects, the former is equivalent toHbeing bijective on objects. The
injectivity part of the later says H([f]) = H([f′]) if and only if [f] = [f ′], i.e.f∼ R f′.
Notice that the congruence “kernel”≡ H defined byf≡ H f′⇔H(f) =H(f ′) can be
equivalently defined asf≡ H f′⇔H([f]) = H([f′]). So Hbeing fully faithful implies
that∼ R=≡H.
Translating the abstract nonsense into English, a relationRis sufficient if every
morphism inCis induced by at least one morphism inF(G) and every equality of
morphisms inCis due to equivalence induced byRinF(G).
Note that this does not speak of whetherRis the most efficient way of achieving
sufficiency.
Definition A.1.10.(Smaller Relations) LetR,R ′ be binary relations on homs of
F(G). We sayR ′ is smaller thanR, denotedR ′ ⊊R, ifR ′
a,b⊆R a,b for all pairs of
objectsa,band there exists at least one pair of objectsX,Ysuch thatR ′
X,Y ⊊R X,Y .
In English,R′ is smaller thanRif it can be obtained fromRby removing some binary
relations.
Definition A.1.11.(Necessary Relations) Let H,G,Rbe a presentation ofC. Let
H:F(G)→ Cbe the composition H◦Q R. We sayRis necessary if for anyR ′
smaller thanR, the unique functor H
′
:F(G)/∼ R′→C, through whichHfactors as
H= H
′
◦QR′ is no longer an isomorphism.
RemarkA.1.12.In this case, H
′
will fail faithfulness while still remaining full and
bijective on objects. A pair of morphisms (f,f ′)∈R X,Y will be mapped to two
1HenceQis surjective on hom sets, and is therefore a full functor.
91
distinct equivalence classes inF(G)/∼ R′, but sent to the same morphism inCunder
H. Hence the two distinct equivalence classes will be sent to the same morphism by
H
′
.
Heuristically, the least congruence containingR ′ will be too small, resulting in a
quotientF(G)/∼ R′ being too big.
This paper is concerned with constructing presentations of Cob(3)S2. There are two
presentations– both having non-negative integers (or equivalently⊔ n≥0S2 )as vertices,
but one graph hasG 1 (and all tensor products) as edges, while the other graph has
G2 (and all tensor products) as edges. By abuse of notation we shall refer to the
two graphs asG 1 andG 2. Since their edges are morphisms, the free category is just
Cob(3)S2 except one forgets if two compositions are equal. The two binary relations on
homs are commutative Frobenius relations for theG1 case, and commutative Frobenius
relations + legs relations for theG 2 case.
The first section is largely concerned with showing that the functorsF(G 1,2)→
Cob(3)S2 are bijective on objects and full, so whatever relations we plan on choosing
has a chance to result in presentations. The second section explicitly constructs two
binary relationsR 1,2 onF(G 1,2). We then show that these relations are sufficient,
namely they give rise to presentations of Cob(3)S2. Then we show that these relations
can be thinned down to be necessary. Hence we obtain two minimal presentations of
the category Cob(3)S2.
