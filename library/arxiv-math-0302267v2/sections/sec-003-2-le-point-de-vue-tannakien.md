---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-003-2-le-point-de-vue-tannakien
section_title: "Le point de vue tannakien"
section_number: 2
pages: 15-28
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
toc_source: inferred
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
2.1. Soient k un corps de nombres et S un ensemble ﬁni de places ﬁnies de k. Le foncteur
ω, d´eduit du foncteur gradu´e ω∗de 1.1 par oubli de la graduation, est un foncteur ﬁbre de la
cat´egorie `a produit tensoriel MT(OS) d´eﬁnie en 1.6. Cette cat´egorie est donc tannakienne,
et si Gω est le sch´ema en groupe des automorphismes du ⊗-foncteur ω, le foncteur ω induit
une ´equivalence de MT(OS) avec la cat´egorie des repr´esentations (lin´eaires, de dimension
ﬁnie) de Gω.
L’action de Gω sur ω(Q(1)) = Q d´eﬁnit un morphisme
(2.1.1)
Gω →Gm.
Soit Uω son noyau. Le groupe multiplicatif Gm agit sur le ⊗-foncteur ω, λ ∈Gm agissant
sur ωn par multiplication par λn. Cette action est une section Gm →Gω de (2.1.1). Elle
fait de Gω un produit semi-direct
(2.1.2)
Gω = Gm ⋉Uω.
Si cela est n´ecessaire pour ´eviter une ambigu¨ıt´e, on ´ecrira Gω ⟨MT(OS)⟩et
Uω ⟨MT(OS)⟩au lieu de Gω et Uω.
L’action de Gω est fonctorielle en M. Pour tout M dans MT(OS), elle respecte donc
la ﬁltration par le poids, index´ee par les entiers pairs, de ω(M) par les
ω(W−2nM) =
⊕
m ≥n ωm(M).
Le sous-groupe Uω agit trivialement sur ω(Q(1)), donc sur les ω(Q(n)), ainsi que
sur GrW (ω(M)) = ω(GrW (M)). Il en r´esulte que le sous-groupe alg´ebrique Uω ⟨M⟩de
GL(ω(M)) image de Uω est unipotent. L’action de Gm ⊂Gω sur ω(M) normalise cette
image. L’alg`ebre de Lie uω ⟨M⟩de Uω ⟨M⟩est donc une sous-alg`ebre de Lie gradu´ee de
gl(ω(M)). Puisque l’action de Uω ⟨M⟩sur ω(M) respecte la ﬁltration par le poids et est
l’identit´e sur le gradu´e associ´e, l’alg`ebre de Lie uω ⟨M⟩est `a degr´es > 0.
Pour M un motif de Tate mixte, notons ⟨M⟩la sous-cat´egorie tannakienne de MT(OS)
engendr´ee par M, d’objets les sous-quotients de sommes de M ⊗p ⊗(M ∨)⊗q. Si M ′ est
13
dans ⟨M⟩, Uω ⟨M ′⟩est un quotient de Uω ⟨M⟩, et le sch´ema en groupe Uω est la limite
projective des Uω ⟨M⟩pour ⟨M⟩de plus en plus grand. Le sch´ema en groupe Uω est donc
pro-unipotent.
Les alg`ebres de Lie uω ⟨M⟩sont `a degr´e > 0 et, par 1.6 et 1.7, les groupes
Ext1(Q(0), Q(n)) = 0
si n ≤0,
(2.1.3)
O∗
S ⊗Q
si n = 1,
K2n−1(k) ⊗Q
si n ≥2.
sont de dimension ﬁnie. On est donc dans la situation consid´er´ee en A.14. En chaque degr´e
n, le syst`eme projectif des (uω ⟨M⟩)n est stationnaire et on d´eﬁnit l’alg`ebre de Lie gradu´ee
ugr
ω comme ´etant la somme sur n des lim(uω ⟨M⟩)n. L’alg`ebre de Lie uω de Uω est la limite
projective des uω ⟨M⟩; c’est le produit des (ugr
ω )n. Appliquant A.15, on obtient:
Proposition 2.2.
(i) L’alg`ebre de Lie gradu´ee ugr
ω est `a degr´es > 0 et est en chaque
degr´e de dimension ﬁnie. Elle d´etermine Uω par
Uω = lim exp(ugr
ω /partie de degr´e ≥N).
(ii) Le foncteur ω induit une ´equivalence de MT(OS) avec la cat´egorie des espaces vectoriels
de dimension ﬁnie gradu´es, munis d’une action de ugr
ω compatible aux graduations.
Que les Ext2(Q(0), Q(n)) soient nuls admet la traduction suivante.
Proposition 2.3. L’alg`ebre de Lie ugr
ω est libre.
On en obtient un syst`eme g´en´erateur homog`ene libre en relevant une base de chaque
(2.3.1)
(ugr
ω )ab
n = dual de (2.1.3)
dans (ugr
ω )n.
2.4 Mise en garde. On ne dispose pas d’un rel`evement canonique de (ugr
ω )ab
n dans (ugr
ω )n.
On ne dispose donc pas d’un isomorphisme canonique de ugr
ω avec l’alg`ebre de Lie librement
engendr´ee par l’espace vectoriel gradu´e
(2.4.2)
(ugr
ω )ab = ⊕(Ext1(Q(0), Q(n))
∨en degr´e n).
14
2.5. La cat´egorie tannakienne MT(k) est la r´eunion ﬁltrante des sous-cat´egories pleines
MT(OS), pour S de plus en plus grand. On a donc pour MT(k)
Gω ⟨MT(k)⟩:= Aut⊗(ω) = lim Gω ⟨MT(OS)⟩=
= Gm ⋉lim Uω ⟨MT(OS)⟩.
2.6. Rappelons quelques d´eﬁnitions fondant la g´eom´etrie alg´ebrique dans une cat´egorie
tannakienne T.
La cat´egorie Ind T des Ind-objets de T est munie d’un produit tensoriel associatif
commutatif `a unit´e h´erit´e de T. Ceci permet de d´eﬁnir la notion d’alg`ebre commutative
`a unit´e de Ind T: c’est un objet A muni d’un produit A ⊗A →A et d’une unit´e 1 →A
v´eriﬁant les axiomes usuels. On d´eﬁnit la cat´egorie des T-sch´emas aﬃnes, aussi appel´es
sch´emas aﬃnes en T, comme ´etant la duale de celle des alg`ebres commutatives `a unit´e de
Ind T. On note Spec(A) le T-sch´ema aﬃne correspondant `a l’alg`ebre A, et on appelle A
son alg`ebre aﬃne.
Un T-sch´ema en groupe aﬃne est un objet en groupe de la cat´egorie des T-sch´emas
aﬃnes, i.e. le spectre G = Spec(A) d’une alg`ebre de Hopf commutative A de Ind T. Une
action de G sur un objet M de T est une structure de comodule M →A ⊗M.
Pour M un object de T, on notera encore M le T-sch´ema vectoriel Spec(Sym∗M ∨), o`u
Sym∗N := colimA ⊕
n ≤A Symn(N). Un pro-objet lim Mi de T d´eﬁnit de mˆeme le T-sch´ema
provectoriel Spec(colimi,A ⊕
n ≤A Symn(M ∨
i )).
Pour un expos´e plus d´etaill´e, nous renvoyons `a Deligne (1989) §5. Par loc. cit. 5.8,
de nombreux ´enonc´es connus en g´eom´etrie alg´ebrique restent valables en T-g´eom´etrie
alg´ebrique. Nous les utiliserons librement.
2.7. Rappelons Deligne (1990) qu’on dispose, dans toute cat´egorie tannakienne T, d’un
T-sch´ema en groupe aﬃne canonique, le groupe fondamental π(T) de T. Il agit sur tout
objet M de T, cette action est fonctorielle en M, et pour tout foncteur ﬁbre F elle d´eﬁnit
un isomorphisme
(2.7.1)
F(π(T))
∼
−→Aut⊗(F).
15
2.8. Certaines des constructions 2.1–2.5 sont motiviques, i.e. l’image par ω de construc-
tions dans MT(OS). D’autres d´ependent de ce que le foncteur ﬁbre ω est gradu´e.
Notons G le groupe fondamental π(MT(OS)). Les constructions suivantes sont mo-
tiviques:
(a) le morphisme (2.1.1) de Gω dans Gm. C’est l’image par ω du morphisme
(2.8.1)
G →Gm
donnant l’action du groupe fondamental G de MT(OS) sur Q(1). Pour donner un sens
`a (2.8.1), observer que la cat´egorie des espace vectoriels de dimension ﬁnie est une sous-
cat´egorie de MT(OS), par V 7→V ⊗Q(0), et qu’un sch´ema en groupe aﬃne peut donc ˆetre
consid´er´e comme un sch´ema en groupe de MT(OS).
(b) le groupe Uω est motivique: c’est l’image par ω du noyau U de (2.8.1). De mˆeme pour
sa pro-alg`ebre de Lie u
(c) la formule (2.4.2) se rel`eve en un isomorphisme de pro-objets de MT(OS)
(2.8.2)
Lie(U ab) =
Y
n
Ext1(Q(0), Q(n))
∨⊗Q(n).
Dans (2.8.2), la projecton sur le ni`eme facteur donne l’action de Lie U sur les extensions de
Q(0) par Q(n).
Par contre, la structure de produit semi-direct (2.1.2) et la graduation de uω (i.e.,
la d´ecomposition de ce provectoriel en produit des (ugr
ω )n) ne sont pas motiviques. La
graduation de uab
ω
l’est, image de (2.8.2) par ω, car l’action int´erieure de G sur uab se
factorise par le quotient Gm de G.
Si cela est n´ecessaire pour ´eviter une ambiguit´e, on ´ecrira G ⟨MT(OS)⟩et U ⟨MT(OS)⟩
au lieu de G et U.
2.9. La r´ealisation de de Rham MDR de M dans MT(k) est un k-espace vectoriel, muni
d’une ﬁltration par le poids W image de celle de M, et d’une ﬁltration d´ecroissante F,
la ﬁltration de Hodge. Ces ﬁltrations sont fonctorielles en M, exactes et compatibles au
produit tensoriel.
16
On a
Q(1)DR = k en poids −2 et ﬁltration de Hodge −1,
et Q(n)DR est donc k en poids −2n et ﬁltration de Hodge −n. Pour M quelconque, les
ﬁltrations W et F sont donc oppos´ees, et d´eﬁnissent une graduation de MDR telle que
W−2n(MDR) =
⊕
m ≥n(MDR)m
F −n(MDR) =
⊕
m ≤n(MDR)m.
On a
(MDR)n = GrW
−2n(MDR) = (GrW
−2n(M))DR
= (ωn(M) ⊗Q(n))DR = ωn(M) ⊗k.
On en d´eduit la
Proposition 2.10. Le foncteur ﬁbre DR sur MT(k) est canoniquement isomorphe au
foncteur d´eduit du foncteur ﬁbre ω par extension des scalaires de Q `a k.
2.11. Pour C une clˆoture alg´ebrique de R et σ un plongement de k dans C, `a la th´eorie
de cohomologie
X sur k 7−→H∗(espace topologique X(C), Q)
correspond un foncteur ﬁbre M 7→Mσ, fonctoriel en C. Parler de “plongement dans
C” plutˆot que de plongement complexe (i.e. dans C) a l’avantage que la fonctorialit´e en
C fournit un isomorphisme Mσ →M¯σ. Pour un plongement r´eel, i.e. pour σ = ¯σ, cet
isomorphisme est une involution de Mσ, le Frobenius r´eel.
Un isomorphisme de comparaison canonique d’un foncteur ﬁbre α vers un foncteur
ﬁbre β sera not´e compβ,α, et son inverse compα,β. La relation entre la cohomologie de de
Rham et la cohomologie singuli`ere fournit
(2.11.1)
compσ,DR: MDR ⊗k,σ C
∼
−→Mσ ⊗Q C,
17
fonctoriel en C. Il induit
(2.11.2)
compσ,ω: Mω ⊗C
∼
−→Mσ ⊗C
et permet de voir Mσ comme une Q-structure sur MDR ⊗k,σ C = Mω ⊗C. On a
Q(1)σ = 2πiQ ⊂C = Q(1)DR ⊗k,σ C
et donc Q(n)σ = (2πi)nQ ⊂C. Dans ces formules, le choix de la racine carr´ee i de −1
n’importe pas.
On reconstitue la Q-structure Mω de l’espace vectoriel gradu´e MDR `a partir de Mσ
et compσ,DR par
(2.11.3)
(Mω)n ⊂(MDR)n ⊂(MDR ⊗k,σ C)n
est
1
(2πi)n compDR,σGrW
−2n(Mσ).
Ecrivons Gω = Gm⋉Uω pour Gω ⟨MT(k)⟩et sa d´ecomposition 2.5, et τ pour l’inclusion
de Gm dans Gω.
Proposition 2.12. Il existe aσ dans Gω(C) tel que
(2.12.1)
Mσ = compσ,ω(aσMω).
Si i est une racine carr´ee de −1 dans C, on peut choisir les aσ de la forme
(2.12.2)
aσ = a0
στ(2πi)
avec a0
σ ∈Uω(C) et a0
¯σ = (a0
σ)−, d’o`u pour σ r´eel,
(2.12.3)
a0
σ ∈Uω(R)
(pour σ = ¯σ)
La preuve est la mˆeme que celle de Deligne (1989) 8.10. Noter que (2.12.1) d´etermine
aσ `a multiplication `a droite pr`es par un ´el´ement de Gω(Q). Choisissons i dans C. La
fonctorialit´e en C montre que si aσ v’eriﬁe (2.12.1), alors ¯aσ v´eriﬁe (2.12.1) pour ¯σ. Si
on impose `a aσ d’ˆetre de la forme (2.12.2), avec a0
σ dans Uω(C), alors ¯aσ = ¯a0
στ(−2πi) =
18
¯a0
στ(2πi)τ(−1) et ¯a0
σ est bien un choix possible pour a¯σ. Pour la v´eriﬁcation qu’on peut
mˆeme prendre a0
σ ∈Uω(R) si σ = ¯σ, on renvoie `a loc. cit. Si on impose `a aσ d’ˆetre de la
forme (2.12.2), son ind´etermination est r´eduite `a Uω(Q). Si σ est r´eel et qu’on impose en
outre (2.12.3), elle est r´eduite `a
U +(Q) : = U(Q) ∩τ(2πi)−1U(R)τ(2πi)
= exp
Y
u2n

.
2.13. Appelons “syst`eme de r´ealisations de Hodge de Tate mixte” (sur k) la donn´ee
suivante.
(a) un k-espace vectoriel gradu´e VDR. La ﬁltration (croissante et index´ee par les entiers
pairs) W−2n :=
⊕
m ≥n(VDR)m est la ﬁltration par le poids et la ﬁltration d´ecroissante F −n =
⊕
m ≤n(VDR)m la ﬁltration de Hodge.
(b) pour tout plongement σ de k dans une clˆoture alg´ebrique C de R, un Q-espace vectoriel
Vσ muni d’une ﬁltration croissante W index´ee par les entiers pairs, fonctoriel en C.
(c) pour σ comme in (b), un isomorphisme de comparaison compσ,DR: VDR⊗k,σC
∼
−→Vσ⊗
C, respectant la ﬁltration par le poids et fonctoriel en C. Son inverse est not´e compDR,σ.
On suppose ces donn´ees telles que le sous-espace
(Vω)n :=
1
(2πi)n compDR,σ(GrW
−2n(Vσ)) ⊂(VDR)n ⊗k,σ C
soit contenu dans (VDR)n et ind´ependant de σ.
La cat´egorie RH
k , ou simplement RH, de ces syst`emes, munie du produit tensoriel
´evident, est une cat´egorie tannakienne, et 2.9 `a 2.11 fournissent un ⊗-foncteur realH de
MT(k) dans RH
k .
La remarque suivante permettra de v´eriﬁer `a peu de frais le caract`ere motivique
d’objets qui nous int´eressent.
Proposition 2.14. Le foncteur realH: MT(k) →RH
k est pleinement ﬁd`ele, d’image es-
sentielle stable par sous-objet.
19
Le point essentiel est que le foncteur realH induit une injection de Ext1(Q(0), Q(n))
dans Ext1(realH(Q(0)), realH(Q(n))). Pour n = 1, cette injectivit´e est celle de
(log σ): k∗⊗Q →
Y
σ: k→C
C/2πiQ
(et un σ suﬃt `a l’injectivit´e). Pour n > 1, elle est une cons´equence de l’injectivit´e de
l’application r´egulateur sur K2n−1(k).
Preuve. Le foncteur ﬁbre ω identiﬁe la cat´egorie RH
k `a celle des repr´esentations d’un groupe
alg´ebrique Gm ⋉U H
ω , et le foncteur realH au foncteur Rep(Gm ⋉Uω) →Rep(Gm ⋉U H
ω )
d´eﬁni par un homomorphisme
Gm ⋉U H
ω →Gm ⋉Uω.
L’injectivit´e sur Ext1 assure que ce morphisme est surjectif, et 2.14 en r´esulte.
2.15 Variantes. (i) Puisque MT(OS) est une sous-cat´egorie pleine de MT(k) stable par
sous-objet, 2.14 vaut ´egalement pour le foncteur
(2.15.1)
realH: MT(OS) →RH
k
(ii) Supposons donn´ee une factorisation du foncteur 2.15.1 par une cat´egorie ab´elienne R :
realH = F ◦realR: MT(OS) →R →RH
k ,
avec realR et F exacts et F ﬁd`ele. Le foncteur realR est alors pleinement ﬁd`ele d’image
essentielle stable par sous-objet. “Pleinement ﬁd`ele” r´esulte formellement de “F ﬁd`ele” et
“F ◦realR pleinement ﬁd`ele”. Que F soit exact et ﬁd`ele implique que pour R dans R, F
induit une injection
{sous-objets de R} −→{sous-objets de F(R)}
et “image essentielle stable par sous-objet” r´esulte formellement de la mˆeme propri´et´e pour
F ◦realR.
20
On peut par exemple prendre pour R la cat´egorie RH+ℓsuivante de syst`emes de
r´ealisations: un objet est la donn´ee de (a) (b) (c) comme en 2.13, plus les donn´ees ℓ-adiques
suivantes:
(d) pour ℓun nombre premier et ¯k une clˆoture alg´ebrique de k, un Qℓ-espace vectoriel
Vℓ, muni d’une ﬁltration ﬁnie croissante W index´ee par les entiers pairs, la ﬁltration par
le poids, d´ependant fonctoriellement de ¯k. La fonctorialit´e en ¯k doit d´eﬁnir une action
continue de Gal(¯k/k), et on demande que la repr´esentation GrW
−2n(Vℓ) de Gal(¯k/k) soit
isomorphe `a une somme de copies de Qℓ(n).
(e) pour σ un plongement de k dans une clˆoture alg´ebrique C de R, et pour ¯k la clˆoture
alg´ebrique de k dans C, un isomorphisme de comparaison
compℓ,σ: Vσ ⊗Qℓ
∼
−→Vℓ
fonctoriel en C.
On suppose l’existence d’un syst`eme de r´eseaux Mσ,Z ⊂Mσ tels que les
compℓ,σ(Mσ,Z ⊗Zl) ⊂Vℓ
soient stables sous Gal(¯k/k) et ind´ependants de σ.
Tant dans RH que dans RH+ℓ, les seuls objets simples sont les r´ealisations des Q(n).
2.16. Pour k′ une extension ﬁnie de k, on dispose d’un ⊗-foncteur “extension du corps de
base `a k′”: M 7→M(k′) de MT(k) dans MT(k′). L’existence et les propri´et´es du morphisme
“norme” en K-th´eorie assurent par application de (0.4) que
(2.16.1)
Ext1
MT(k)(Q(n), Q(m)) →Ext1
MT(k′)(Q(n), Q(m))
est injectif et que, pour k′/k une extension galoisienne, l’image est form´ee des invariants
sous Galois:
(2.16.2)
Ext1
MT(k)(Q(n), Q(m))
∼
−→Ext1
MT(k′)(Q(n), Q(m))Gal(k′/k).
21
Par les arguments de la preuve de 2.14, l’injectivit´e de (2.16.1) implique que le foncteur
M 7→M(k′) est pleinement ﬁd`ele, d’image essentielle stable par sous-objet. En particulier,
si un motif de Tate mixte M ′ sur k′ provient d’un motif de Tate mixte M sur k, ce dernier
est d´etermin´e `a isomorphisme unique pr`es par M ′. Si la place ﬁnie v′ de k′ domine la place
v de k, M ′ est non ramiﬁ´e en v′ si et seulement si M l’est en v.
2.17. Par 2.16, les cat´egories tannakiennes MT(k), pour k variable, forment un pr´echamp
sur le site ´etale de Spec(Q). On note MAT le champ associ´e et on appelle MAT(k) la
cat´egorie des motifs d’Artin-Tate mixte sur k. Explicitons cette d´eﬁnition.
Soit k1 une extension galoisienne de k. Notons C(k1/k) la cat´egorie des extensions
ﬁnies k′ de k dans lesquelles peut se plonger k1. Soit MAT(k1/k) la cat´egorie des sections
de MT au-dessus de C(k1/k): la cat´egorie des syst`emes d’objets M(k′) ∈MT(k′) pour
k′ ∈C(k1/k), et d’isomorphismes M(k′)(k′′)
∼
−→M(k′′) pour k′ →k′′ dans C(k1/k), v´eriﬁant
une compatibilit´e pour k′ →k′′ →k′′′. La cat´egorie MAT(k) est la limite inductive des
MAT(k1/k), pour C(k1/k) de plus en plus petit.
La ﬁltration par le poids des objets des MT(k′) ´etant fonctorielle et compatible aux
extensions de corps de base, elle fournit une ﬁltration par le poids sur chaque objet de
MAT(k1/k), ou de MAT(k).
La cat´egorie MAT(k) h´erite de MT(k′) de foncteurs ﬁbre ω, DR, σ et ℓ, et d’isomor-
phismes de comparaison.
Foncteur ﬁbre ω: le foncteur M = (M(k′))k′∈C(k1/k) 7→M(k1) est une ´equivalence de
MAT(k1/k) avec la cat´egorie des objets de MT(k1) munis d’une action semi-lin´eaire de
Gal(k1/k) (donn´ee de descente galoisienne). Cette donn´ee de descente induit une action de
Gal(k1/k) sur ω(M) := ω(M(k1)) et le groupe de Galois motivique Aut(ω) de MAT(k1/k)
est le produit semi-direct de Gal(k1/k) par le groupe de Galois motivique de MT(k1).
Soit ¯k une clˆoture alg´ebrique de k et passons `a la limite sur k1 ⊂¯k. On d´eﬁnit
ω(M) := ω(M(k1))
pour k1 ⊂¯k assez grand.
Ce Q-espace vectoriel gradu´e est muni d’une action continue de Gal(¯k/k).
22
Foncteur ﬁbre DR: d´eﬁni par descente galoisienne `a partir des foncteurs ﬁbres DR des
MT(k′). Pour M dans MAT(k1/k) et k′ ∈C(k1/k), on a fonctoriellement en k′
MDR ⊗k k′
∼
−→(M(k′))DR,
et l’isomorphisme 2.10 fournit un isomorphisme de comparaison
MDR = (ω(M(k1)) ⊗k1)Gal(k1/k).
Foncteur ﬁbre σ: pour σ un plongement de k dans une clˆoture alg´ebrique C de R. C’est
Mσ := (M(k′))σ′
pour σ le compos´e k ⊂k′
σ′֒
−→C et k′ assez grand pour que M(k′) soit dans MT(k′).
Foncteur ﬁbre ℓ: il d´epend du choix d’une clˆoture alg´ebrique ¯k de k, et est d´eﬁni comme
´etant (M(k′))ℓpour k′ ⊂¯k assez grand.
Cas particulier. Les objets purement de poids 0 de MT(k′), i.e. tels que Gr−2nW = 0 pour
n̸ = 0, sont les sommes de copies de Q(0), et ω0 identiﬁe leur cat´egorie `a celle des Q-espaces
vectoriels. En cons´equence, pour ¯k une clˆoture alg´ebrique de k, le foncteur ω identiﬁe la
cat´egorie des objets purement de poids 0 de MAT(k) avec celle des Q-espaces vectoriels
munis d’une action continue de Gal(¯k/k) (motifs d’Artin).
Soit k1 une extension galoisienne ﬁnie de k. Il r´esulte de 2.16 que le foncteur MT(k) →
MAT(k1/k) est pleinement ﬁd`ele d’image essentielle stable par sous-objet. L’image essen-
tielle est aussi stable par extensions:
Proposition 2.18. Pour qu’un objet M de MAT(k1/k) soit dans MT(k), il faut et il suﬃt
que l’action de Gal(k1/k) sur ω(M) soit triviale.
Si M est purement de poids 0, la proposition r´esulte du “cas particulier” ci-dessus.
Le cas o`u M est pur, i.e. purement d’un seul poids, en r´esulte par tensorisation avec un
Q(n). Il reste `a v´eriﬁer une stabilit´e par extensions.
23
1ere preuve. Une suite spectrale d’Hochschild-Serre fournit, pour M et N dans MT(k), des
isomorphismes
Extp
MAT(k1/k)(M, N)
∼
−→Extp(M(k1), N(k1))Gal(k1/k).
Pour v´eriﬁer que
Extp
MT(k)(M, N) →Extp
MAT(k′/k)(M, N) = Extp
MT(k1)(M(k1), N(k1))Gal(k1/k)
est bijectif pour p = 0, 1 et injectif pour p = 2, il suﬃt par d´evissage de le v´eriﬁer pour M
et N de la forme Q(m) et Q(n). Le cas p = 2 r´esulte de la nullit´e des Ext2, le cas p = 0
r´esulte de ce que Hom = 0, sauf pour m = n, o`u End(Q(n)) = Q, et p = 1 est 2.16.
Plutot que de d´eﬁnir la suite spectrale d’Hochschild-Serre requise, on peut la para-
phraser:
2`eme preuve. Si M est une extension de Q(n) par Q(n+r), que M(k1) admette une donn´ee
de descente de k1 `a k, respectant la structure d’extension de Q(n) par Q(n + r), implique
que la classe de M(k1) dans Ext1
MT(k1)(Q(n), Q(n+r)) est ﬁxe sous Gal(k1/k). Elle provient
donc de la classe d’une extension f
M de Q(n) par Q(n+r) dans MT(k). On v´eriﬁe, utilisant
que HomMT(k1)(Q(n), Q(n + r)) = 0, que M est isomorphe `a l’image de f
M.
Prouvons par r´ecurrence sur r ≥0 que 2.18 est vrai sous l’hypoth`ese additionnelle que
pour un n on ait M = W−2nM et W−2(n+r+1)M = 0.
Le cas o`u r = 0 (M pur) a d´ej`a ´et´e trait´e. Le cas r = 1 se r´eduit `a celui d’une extension
de Q(n) par Q(n + 1).
Pour r ≥1, l’hypoth`ese de r´ecurrence assure que M ′ = M/W−2(n+r)M et M ′′ =
W−2(n+1)M proviennent de f
M ′ et f
M ′′ dans MT(k). Ce sont des extensions de la forme:
GrW
−2nM par N et N par GrW
−2(n+r)M. Par nullit´e des Ext2 dans MT(k), il existe dans
MT(k) un objet f
M, extension it´er´ee de GrW
−2nM par N par GrW
−2(n+r)M, redonnant f
M ′
et f
M ′′. L’image de f
M dans MAT(k1/k) diﬀ`ere de M par une extension de GrW
−2nM par
GrW
−2(n+r)M.
24
Cette derni`ere provient d’une extension dans MT(k), par r´eduction au cas d’une ex-
tension de Q(n) par Q(n + r), et ceci permet de corriger f
M pour que son image devienne
isomorphe `a M.
25
