---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-020-141-le-paysage-discret
section_title: "Le paysage discret"
section_number: 14.1
pages: 79-112
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
14.1.1. Le cas non mono¨ıdal. Soit A une petite K-cat´egorie de Wedderburn. Con-
sid´erons la cat´egorie G(A) dont les objets sont les sections de πA, un morphisme de
s vers s′ ´etant une famille (uA)A∈A comme dans le th´eor`eme 12.1.1 b) et le com-
pos´e de deux morphismes (uA), (vA) ´etant (vAuA). (Comme nous l’a fait remarquer
A. Brugui`eres, les morphismes de G(A) s’interpr`etent aussi comme les transforma-
tions naturelles entre sections de πA se projetant sur l’identit´e dans ¯
A.) Alors G(A)
est un petit groupo¨ıde : le groupo¨ıde des sections de πA. Le contenu du th´eor`eme
12.1.1 a) (resp. b)) est que ce groupo¨ıde est non vide (resp. connexe).
L’interpr´etation de la proposition 12.2.1 dans ce langage est le peu satisfaisant
principe de fonctorialit´e suivant : si sA ∈G(A) et sB ∈G(B), d´eﬁnissons le trans-
porteur de sA vers sB comme l’ensemble T(sA, sB) des (uX) v´eriﬁant les con-
ditions de ladite proposition : ce sont aussi les transformations naturelles de sA ¯T
vers TsB se projetant sur l’identit´e. Alors, pour tout couple (sA, sB), l’ensemble
T(sA, sB) est non vide.
Toutefois, si A →B est pleinement ﬁd`ele, alors on a un foncteur canonique
G(B) →G(A) dans l’autre sens. Cette correspondance s’´etend en un 2-foncteur :
notons
Wed{K}
la sous-2-cat´egorie non pleine de {K} (voir §1.2) dont
– les objets sont les petites K-cat´egories de Wedderburn
– les 1-morphismes sont les K-foncteurs pleinement ﬁd`eles
– les 2-morphismes sont les isomorphismes naturels.
D’autre part, notons Gr la 2-cat´egorie des petits groupo¨ıdes (tous les foncteurs
et toutes les transformations naturelles sont autoris´es). Alors on v´eriﬁe au prix d’un
petit calcul :
14.1.1. Sorite. La construction A 7→G(A) d´eﬁnit un 2-foncteur 1-contravariant et
2-covariant
G : Wed{K} →Gr .
Le th´eor`eme 12.1.1 ´enonce que son image est contenue dans la 2-sous-cat´egorie
pleine des groupo¨ıdes non vides connexes.
□
En particulier, toute K-´equivalence de cat´egories A
∼
−→B d´eﬁnit une ´equivalence
de cat´egories G(B)
∼
−→G(A), qui n’est pas en g´en´eral un isomorphisme de cat´e-
gories. Toutefois :
80
YVES ANDR´E ET BRUNO KAHN
14.1.2. Sorite. Pour toute K-cat´egorie de Wedderburn A, les foncteurs
G(A⊕)
ր
ց
G(A⊕♮)
G(A)
ց
ր
G(A♮)
sont des isomorphismes de groupo¨ıdes.
□
(On peut s’en convaincre en remarquant que ces foncteurs d´eﬁnissent des inverses
partiels des foncteurs du sorite 1.2.1.)
14.1.2. Le cas mono¨ıdal. Supposons maintenant que A soit mono¨ıdale, et que son
radical soit un id´eal mono¨ıdal. De mˆeme que dans 14.1.1, on peut introduire le
groupo¨ıde G⊗(A) des sections mono¨ıdales de πA (les morphismes ´etant les mor-
phismes de foncteurs mono¨ıdaux se projetant sur l’identit´e dans ¯
A). C’est un sous-
groupo¨ıde de G(A), lui aussi connexe non vide20. La proposition 13.7.1 admet la
mˆeme interpr´etation que la proposition 12.2.1 du paragraphe 12. Si A →B est
pleinement ﬁd`ele, on a un foncteur canonique G⊗(B) →G⊗(A) dans l’autre sens.
Notons
Wed⊗{K}
la 2-cat´egorie dont
– les objets sont les petites K-cat´egories de Wedderburn mono¨ıdales, `a radical
mono¨ıdal
– les 1-morphismes sont les K-foncteurs mono¨ıdaux pleinement ﬁd`eles
– les 2-morphismes sont les isomorphismes naturels mono¨ıdaux.
On a un 2-foncteur ´evident
(14.1)
Ω: Wed⊗{K} →Wed{K}
(oubli des structures mono¨ıdales). Comme au §14.1.1, on obtient en fait :
14.1.3. Sorite. La construction A 7→G⊗(A) d´eﬁnit un 2-foncteur 1-contravariant
et 2-covariant
G⊗: Wed⊗{K} →Gr .
Le th´eor`eme 13.2.1 ´enonce que son image est contenue dans la 2-sous-cat´egorie
pleine des groupo¨ıdes non vides connexes.
Il existe une 2-transformation naturelle canonique
G⊗⇒G ◦Ω
o`u G est comme dans le sorite 14.1.1 et Ωest comme en (14.1).
□
20Tout foncteur d’un groupo¨ıde connexe non vide vers un autre est essentiellement surjectif. . .
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
81
14.1.4. Sorite. Pour toute K-cat´egorie de Wedderburn A, les foncteurs
G⊗(A⊕)
ր
ց
G⊗(A⊕♮)
G⊗(A)
ց
ր
G⊗(A♮)
sont des isomorphismes de groupo¨ıdes.
□
14.1.3. Objets compacts, duaux et limites inductives. Supposons A stable par lim-
ites inductives quelconques, et soit Acomp sa sous-cat´egorie pleine form´ee des objets
compacts. Alors on a un foncteur de restriction G(A) →G(Acomp). Si tout objet
de A est isomorphe `a une limite inductive d’objets compacts, on a un foncteur en
sens inverse : ces deux foncteurs sont des ´equivalences de cat´egories, quasi-inverses
l’une de l’autre.
Mˆeme sorite dans le cas mono¨ıdal sym´etrique, en supposant 1 compact et en
remplac¸ant “compact” par “ayant un dual”.
14.1.4. Extension des scalaires. Si L/K est une extension, on a des foncteurs “ex-
tension des scalaires” (na¨ıve et `a la Saavedra) G(A) →G(AL) et G(A) →G(A(L)),
et de mˆeme dans le cas mono¨ıdal. Si L/K est (ﬁnie) s´eparable, ces foncteurs sont
isomorphes en vertu du th´eor`eme 5.3.2. Dans le cas g´en´eral et en supposant A sta-
ble par limites inductives quelconques, on a un foncteur de restriction G(A(L)) →
G(AL) commutant naturellement aux deux foncteurs ci-dessus. Mˆeme sorite dans
le cas mono¨ıdal.
14.2. Objets en cat´egories, en groupo¨ıdes et en actions de groupe.
14.2.1. Objets en cat´egories et en groupo¨ıdes. Soit X une cat´egorie avec limites
projectives ﬁnies. Rappelons qu’un objet en cat´egories dans X est la donn´ee Γ de
deux objets E, S ∈X, d’un morphisme
(β, σ) : E →S × S
“but” et “source” et d’un morphisme “loi de composition”
◦: E ×βSσ E →E
telles que, pour tout objet X ∈X, le couple (X(X, E), X(X, S)) et les morphis-
mes correspondants d´eﬁnissent une petite cat´egorie Γ(X) (objets : S(X) ; morphis-
mes : E(X)). Par le lemme de Yoneda, cela revient `a exiger que β, σ, ◦v´eriﬁent les
identit´es habituelles. Un objet en cat´egories Γ est un objet en groupo¨ıdes si, pour
tout X ∈X, Γ(X) est un groupo¨ıde (mˆeme remarque).
Si Γ = (E, S, β, σ, ◦) et Γ′ = (E′, S′, β′, σ′, ◦′) sont deux objets en cat´egories
de X, un morphisme de Γ vers Γ′ est un couple T = (f, g), avec f ∈X(E, E′),
82
YVES ANDR´E ET BRUNO KAHN
g ∈X(S, S′), tels que les diagrammes
E
(β,σ)
−−−−→S × S
f
y
g×g
y
E′
(β′,σ′)
−−−−→S × S
E ×βSσ E
◦
−−−−→E
f×f
y
f
y
E′ ×β′S′σ′ E′
◦′
−−−−→E′
soient commutatifs (ou, de mani`ere ´equivalente, que T(X) : Γ(X) →Γ′(X) soit
un foncteur pour tout X ∈X).
Si T = (f, g) et T ′ = (f ′, g′) sont deux tels morphismes, une homotopie de T
vers T ′ est un morphisme u ∈X(S, E′) tel que les diagrammes
S
u
−−−−→
E′
(g′,g) ց
(β′,σ′)
y
S′ × S′
E
(f,uβ)
−−−−→E′ ×β′S′σ′ E′
(uσ,f′)
y
◦′
y
E′ ×β′S′σ′ E′
◦′
−−−−→
E′
soient commutatifs (ou, ce qui revient au mˆeme, que u(X) soit une transformation
naturelle quel que soit X ∈X).
Les objets en cat´egories, morphismes et homotopies d´eﬁnissent une 2-cat´egorie
Cat(X). Sa sous-cat´egorie 1-pleine et 2-pleine form´ee desobjets en groupo¨ıdes est
not´ee Gr(X).
14.2.2. Objets en actions de groupe. Un objet en groupes dans X est un couple
(G, µG) avec G ∈X, µG ∈X(G × G, G) tel que G(X) = X(X, G) d´eﬁnisse un
groupe pour la loi µG(X) = X(X, µG) quel que soit X ∈X. De mˆeme, un objet
en actions de groupe est un syst`eme ∆= (G, S, µG, µS), o`u (G, µG) est un objet
en groupes, S ∈X, µS ∈X(G × S, S), tel que (µG(X), µS(X)) d´eﬁnisse une
action de G(X) sur S(X) pour tout X ∈X.
´Etant donn´e deux objets en actions de groupe ∆= (G, S, µG, µS), ∆′ =
(G′, S′, µG′, µS′), un morphisme de ∆vers ∆′ est un couple T = (f, g), avec
f ∈X(G, G′), g ∈X(S, S′), tels que les diagrammes
G × G
µG
−−−−→G
f×f
y
f
y
G′ × G′
µG′
−−−−→G′
G × S
µS
−−−−→S
g×g
y
g
y
G′ × S′
µS′
−−−−→S′
soient commutatifs.
Il y a une notion ´evidente de composition de tels morphismes.
Enﬁn, ´etant donn´e deux tels morphismes T = (f, g), T ′ = (f ′, g′), une homo-
topie de T vers T ′ est un morphisme u ∈X(S, G′) tel que les diagrammes
S
(u,g)
−−−−→G′ × S′
g′ ց
µS′
y
S′
G × S
(u◦µS,f◦p1)
−−−−−−−→G′ × G′
f′×u
y
µG′
y
G′ × G′
µG′
−−−−→
G′
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
83
soient
commutatifs
(en
formules
:
g′(s)
=
u(s)g(s) ;
u(γs)
=
f ′(γ)u(s)f(γ)−1). La composition de deux homotopies est donn´ee par u′ ◦u :=
µG′ ◦(u′, u) (u′ ◦u(s) = u′(s)u(s)).
Les objets en actions de groupe, morphismes et homotopies forment une autre
2-cat´egorie not´ee Acg(X).
14.2.3. Actions de groupe et groupo¨ıdes. Pour obtenir un groupo¨ıde Γ, il sufﬁt de se
donner un objet en actions de groupe ∆= (G, S, µG, µS). On d´eﬁnit E = G × S,
β = µS, σ = seconde projection. On v´eriﬁe (par exemple `a l’aide du lemme de
Yoneda) que le morphisme
G × G × S
(p23,1G×µS)
−−−−−−−−→E ×βSσ E,
o`u p23 est la projection oubliant le premier facteur, est un isomorphisme. On d´eﬁnit
alors ◦comme le morphisme
E ×βSσ E( ∼
←−)−1G × G × S
µG×1S
−−−−→G × S = E.
Un tel groupo¨ıde est dit scind´e.
La r`egle ci-dessus s’´etend en un 2-foncteur
Acg(X) →Gr(X).
14.2.1. Exemple. X
= Sch/K est la cat´egorie des K-sch´emas (dans notre
univers). Un K-groupo¨ıde est un objet en groupo¨ıdes Γ = (S, E) dans X. Il est
dit transitif sur S s’il existe T ′ ﬁd`element plat quasi-compact sur S ×K S tel que
HomS×KS(T ′, E)̸ = ∅(le champ associ´e `a T 7→(S(T), E(T), β, σ, ◦) est alors
une gerbe, cf. [14, 3.3]). Il est dit unipotent (resp. r´eductif. . . ) si la restriction de E `a
la diagonale de S ×K S est un S-groupe afﬁne pro-unipotent (resp. pro-r´eductif. . . ).
Un K-espace homog`ene est un objet en actions de groupe (G, S) dans X telle
que G op`ere transitivement sur S. On note
Hmg(Sch/K) ⊂Acg(Sch/K) la sous-cat´egorie 2-pleine et 1-pleine des K-
espaces homog`enes.
´Etant donn´e un objet en actions de groupe (G, S) dans X, pour que le mor-
phisme (β, γ) du K-groupo¨ıde Γ associ´e par 14.2.3 soit fpqc, il sufﬁt que (G, S)
soit un espace homog`ene. Cela implique que Γ est transitif sur S (prendre T ′ =
E ci-dessus). Si G est pro-unipotent (resp. pro-r´eductif. . . ), Γ est unipotent (resp.
r´eductif. . . ) : en effet, la restriction de E `a la diagonale est un sous-S-groupe ferm´e
du S-groupe constant G ×K S.
14.3. Repr´esentabilit´e alg´ebrique. Soient A une K-cat´egorie de Wedderburn et
L une extension de K. Par le corollaire 4.1.4, AL est encore de Wedderburn, de
radical RL = R ⊗L, ce qui sugg`ere la pr´esence d’un K-groupo¨ıde (au sens des
sch´emas) dont le groupo¨ıde G(A) du §14.1.1 serait le groupo¨ıde des K-points. De
mˆeme, si A est mono¨ıdale `a radical mono¨ıdal, on peut esp´erer que le groupo¨ıde
G⊗(A) du §14.1.2 est repr´esentable.
Nous allons montrer que c’est bien le cas, sous une hypoth`ese de ﬁnitude con-
venable. En fait, nous allons obtenir encore mieux.
84
YVES ANDR´E ET BRUNO KAHN
14.3.1. Le cas non mono¨ıdal.
14.3.1. Th´eor`eme. Soit Wedf{K} la sous-2-cat´egorie 1-pleine et 2-pleine de
Wed{K} form´ee des cat´egories A telles que dimK A(A, B) < ∞pour tout
(A, B) ∈A × A.
a) Soit A ∈Wedf{K}. Alors il existe un K-groupo¨ıde afﬁne scind´e unipotent
Γ(A) = (E, S), transitif sur S, tel que pour toute extension L de K, on ait
S(L) = Ob(G(AL)) et E(s1, s2)(L) = G(AL)(s1, s2) pour tout couple de sec-
tions (s1, s2) de πAL.
b) Cette construction provient d’un 2-foncteur 1-contravariant et 2-covariant
∆: Wedf{K} →Hmg(Sch/K)
`a
valeurs
dans
les
K-espaces
homog`enes
unipotents,
via
le
2-foncteur
Hmg(Sch/K) →Gr(Sch/K) de 14.2.3.
c) Les 2-foncteurs ∆et Γ commutent `a l’extension des scalaires.
D´emonstration. Compte tenu de l’hypoth`ese de ﬁnitude, pour tout objet A le fonc-
teur des K-alg`ebres commutatives vers les groupes
R 7→(1A + R(A, A) ⊗K R, ◦)
est repr´esentable par un K-sch´ema en groupes afﬁne unipotent UA. Soit UA =
Y
A
UA leur produit ; c’est un K-groupe pro-unipotent, i.e. une limite projective
ﬁltrante lim
←−Uα de K-groupes unipotents ; en tant que sch´ema, c’est juste un produit
d’espaces afﬁnes.
Pour tout couple (A, B) d’objets de A, soit Sec(A, B) l’ensemble des sections
K-lin´eaires de la projection A(A, B) →¯
A(A, B) : il est repr´esentable par un K-
espace afﬁne Sec(A, B). Posons SecA = Q
A,B Sec(A, B) : c’est aussi un produit
d’espaces afﬁnes.
Consid´erons le sous-sch´ema ferm´e de Sec
SA = {(sA,B) | ∀A, B, C ∈A, ∀(f, g) ∈¯
A(A, B) × ¯
A(B, C),
sA,C(g ◦f) = sB,C(g) ◦sA,B(f)}.
On a une action ´evidente de UA sur SA
µ : UA ×K SA →SA
(u, s) 7→usu−1
qui est transitive grˆace au th´eor`eme 12.1.1 b). Notons ∆(A) ce K-espace homog`ene
unipotent : le groupo¨ıde Γ(A) cherch´e est l’image de ∆(A) par le foncteur de
14.2.3.
Il reste `a voir que ∆d´eﬁnit un 2-foncteur. Soit T : B →A un foncteur pleine-
ment ﬁd`ele : il induit un ´epimorphisme UA →
→UB de K-sch´emas afﬁnes grˆace au
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
85
diagramme
Y
A∈A
UA
y
Y
B∈B
UB
∼
−−−−→
Y
B∈B
UT(B)
et de mˆeme un ´epimorphisme SecA →
→SecB, ce dernier envoyant SA dans SB.
Ces morphismes d´eﬁnissent clairement un morphisme de K-espaces homog`enes
∆(T) : ∆(A) →∆(B).
Soit T ′ un autre tel foncteur, et u : T ⇒T ′ un isomorphisme naturel, d’o`u un
autre ¯u : ¯T ⇒¯T ′, o`u ¯T, ¯T ′ : ¯B →¯
A sont les foncteurs induits. Pour tout B ∈B
et toute section s de πA, l’´el´ement s(¯uB)−1uB appartient `a 1 + R(T(B), T(B)) :
on en d´eduit un ´el´ement T −1(s(¯uB)−1uB) ∈1 + R(B, B). Cette r`egle d´eﬁnit un
morphisme
∆(u) : SA →UB
dont on v´eriﬁe facilement qu’il satisfait les conditions d’une homotopie ∆(T) ⇒
∆(T ′).
□
14.3.2. Exemple. Le th´eor`eme 14.3.1 montre que, pour deux K-cat´egories de Wed-
derburn A et B K-´equivalentes, les groupo¨ıdes Γ(A) et Γ(B) ont en g´en´eral mˆeme
type d’homotopie (au sens ci-dessus), mais ne sont pas n´ecessairement isomorphes.
La mˆeme remarque vaut pour les invariants plus ﬁns ∆(A) et ∆(B). La remarque
12.1.3 va nous permettre de d´ecrire un repr´esentant explicite du type d’homotopie
de ∆(A) et Γ(A) lorsque K est alg´ebriquement clos (ou plus g´en´eralement parfait,
si tout ind´ecomposable de A le reste dans A♮apr`es toute extension ﬁnie L/K).
Il sufﬁt de supposer que tout objet de A est ind´ecomposable et que deux objets
diff´erents sont non isomorphes. On a alors S = Spec K et G est le produit des
1 + R(A, A), o`u A d´ecrit l’ensemble des objets de A. En particulier, le sch´ema des
objets de Γ(A) est ici r´eduit `a un point.
14.3.2. Le cas mono¨ıdal.
14.3.3. Th´eor`eme. Soit Wedf ⊗{K} la sous-2-cat´egorie 1-pleine et 2-pleine de
Wed⊗{K} form´ee des cat´egories A telles que dimK A(A, B) < ∞pour tout
(A, B) ∈A × A.
a) Soit A ∈Wedf ⊗{K}. Alors il existe un K-groupo¨ıde afﬁne scind´e unipotent
Γ⊗(A) = (E⊗, S⊗), transitif sur S⊗, tel que pour toute extension L de K, on ait
S⊗(L) = Ob(G⊗(AL)) et E⊗(s1, s2)(L) = G⊗(AL)(s1, s2) pour tout couple de
sections mono¨ıdales (s1, s2) de πAL.
b) Cette construction provient d’un 2-foncteur 1-contravariant et 2-covariant
∆⊗: Wedf ⊗{K} →Hmg(Sch/K)
`a
valeurs
dans
les
K-espaces
homog`enes
unipotents,
via
le
2-foncteur
Hmg(Sch/K) →Gr(Sch/K) de 14.2.3.
86
YVES ANDR´E ET BRUNO KAHN
c) On a une 2-transformation naturelle
∆⊗⇒∆◦Ω
comme dans le sorite 14.1.3.
d) Les 2-foncteurs ∆⊗et Γ⊗commutent `a l’extension des scalaires.
D´emonstration. On reprend les notations de la preuve du theor`eme 14.3.1. Con-
sid´erons le nouvel espace de param`etres
Sec⊗= S ×
Y
A,B
(1 + R(A • B, A • B)).
Les ´equations que doivent v´eriﬁer la contrainte mono¨ıdale ˜s d’une section mono¨ı-
dale s d´eﬁnissent un sous-sch´ema ferm´e S⊗⊂Sec⊗. Soit U1 le sous-groupe ferm´e
de U form´e des (uA) tels que u1 = 1. Le groupe U1 op`ere cette fois-ci sur S⊗par
la formule
µ⊗: U1 ×K S⊗→S⊗
(u, (s, ˜s)) 7→(usu−1, ˜s′)
o`u ˜s′ est d´eﬁni par le diagramme (13.1). Le th´eor`eme 13.2.1 b) montre que cette
action est transitive. D’o`u ∆⊗(A).
On a un morphisme ´evident ∆⊗(A) →∆(A), donn´e par le plongement de U1
dans U et par l’oubli des structures mono¨ıdales. Ceci d´eﬁnit la 2-transformation
naturelle de c) au niveau des objets (cat´egories). Le reste se v´eriﬁe facilement.
□
15. SECTIONS ET TRESSAGES
15.1. Tressages. On renvoie `a [27] pour les notions de tressage et de foncteur mo-
no¨ıdal tress´e. Contentons-nous de les rappeler bri`evement.
Un tressage sur une cat´egorie mono¨ıdale (A, •) est la donn´ee, pour tout couple
d’objets (A, B) ∈A × A, d’un ´el´ement
RA,B ∈A(A • B, B • A)
tel que le diagramme
(15.1)
A • B
f•g
−−−−→C • D
RA,B
y
RC,D
y
B • A
g•f
−−−−→D • C
soit commutatif pour tous A, B, C, D ∈A et tout couple (f, g) ∈A(A, C) ×
A(B, D). On demande de plus que les RA,B v´eriﬁent les identit´es de tressage
RA,B•C = aB,C,A(1B • RA,C)a−1
B,A,C(RA,B • 1C)aA,B,C
(15.2)
RA•B,C = a−1
C,A,B(RA,C • 1B)aA,C,B(1A • RB,C)a−1
A,B,C
(15.3)
o`u a est la contrainte d’associativit´e.
On dit que le tressage R est sym´etrique si on a de plus l’identit´e
(15.4)
RB,A = R−1
A,B.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
87
Si (B, ⊤) et (A, •) sont tress´ees, un foncteur mono¨ıdal (s, ˜s) : (B, ⊤) →(A, •)
est dit tress´e s’il est compatible avec les tressages. En d’autres termes, pour tous
A, B ∈B, on demande que le diagramme
(15.5)
s(A) • s(B)
˜sA,B
−−−−→s(A⊤B)
Rs(A),s(B)
y
s(RA,B)
y
s(B) • s(A)
˜sB,A
−−−−→s(B⊤A)
soit commutatif.
Notons que si s est strict, la condition devient simplement s(RA,B) = Rs(A),s(B).
Notons aussi qu’imposer que les tressages de B et A soient sym´etriques n’im-
pose aucune condition suppl´ementaire sur s (et mˆeme en retire). Par contre, si les
tressages de B et A sont compatibles via s, et si s est essentiellement surjective, l’un
est sym´etrique si et seulement si l’autre l’est.
15.2. Sorites. Le sorite suivant compl`ete le sorite 13.3.1 :
15.2.1. Sorite. Soit (s, ˜s) : (B, ⊤, R) →(A, •, S) un foncteur mono¨ıdal tress´e
entre deux cat´egories mono¨ıdales tress´ees, et soit u : s ⇒t un isomorphisme
naturel de s sur un autre foncteur t. Alors l’unique structure mono¨ıdale ˜t sur t
faisant de u un morphisme de foncteurs mono¨ıdaux (sorite 13.3.1) est tress´ee.
□
On a aussi :
15.2.2. Sorite. Tout tressage R satisfait les identit´es
RA,B⊕C = diag(RA,B, RA,C)
RA⊕B,C = diag(RA,C, RB,C).
(Cela r´esulte du sorite 1.1.3, en consid´erant R comme une transformation na-
turelle • ⇒• ◦T, o`u T est l’´echange des facteurs.)
□
Rappelons ´egalement le sorite suivant [27, rem. 2.3] :
15.2.3. Sorite. Notons Asym la cat´egorie sym´etrique de A (mˆemes objets, mˆemes
morphismes mais produit d´eﬁni par A •′ B := B • A, cf. [53, I.0.1.4]). Alors tout
tressage R sur A d´eﬁnit une structure mono¨ıdale sur le foncteur identique IdA :
Asym →A.
□
Enﬁn :
15.2.4. Sorite. Soient (B, ⊤, R) une cat´egorie mono¨ıdale tress´ee, (A, •) une cat´ego-
rie mono¨ıdale et (s, ˜s) : (B, ⊤) →(A, •) un foncteur mono¨ıdal. Pour A, B ∈B,
posons
Rs
A,B = ˜s−1
B,As(RA,B)˜sA,B : s(A) • s(B) →s(B) • s(A).
Soit a la contrainte d’associativit´e de A. Alors on a les identit´es
(˜sB,C • 1s(A))−1Rs
A,B•C(1s(A) • ˜sB,C) =
as(B),s(C),s(A)(1s(B) • Rs
A,C)a−1
s(B),s(A),s(C)(RA,B • 1s(C))as(A),s(B),s(C)
88
YVES ANDR´E ET BRUNO KAHN
(1s(C) • ˜sA,B)−1Rs
A•B,C(˜sA,B • 1s(C)) =
a−1
s(C),s(A),s(B)(RA,C • 1s(B))as(A),s(C),s(B)(1s(A) • Rs
B,C)a−1
s(A),s(B),s(C).
□
En d’autres termes, Rs v´eriﬁe “presque” les relations de tressage (15.2) et (15.3).
15.3. Sections. Reprenons maintenant les notations et hypoth`eses du th´eor`eme 13.2.1,
en pr´esence d’un tressage21. Ce dernier reste muet sur la compatibilit´e des sections
mono¨ıdales `a un tressage ´eventuel. Nous allons voir que, dans ce cas, la situation
est tr`es “rigide”.
Soit R un tressage sur A. On en d´eduit un tressage ¯R = πA(R) sur ¯
A.
Soit (s, ˜s) une section mono¨ıdale de πA.
15.3.1. Proposition. a) Il existe un automorphisme (non mono¨ıdal) u de s tel que,
pour tout couple d’objets A, B ∈A, on ait
(15.6)
s( ¯RA,B) = u−1
B•A˜sB,ARA,B(uA • uB)˜s−1
A,B.
b) On a l’identit´e
(15.7)
s( ¯RB,A)s( ¯RA,B) = ˜sA,BRB,ARA,B(u2
A • u2
B)˜s−1
A,Bu−2
A•B.
D´emonstration. a) En tenant compte du sorite 15.2.3, on applique la proposition
13.7.1 dans la situation B = Asym, T = (IdA, R), sA = sB = s.
b) Remarquons les relations de commutation
uB•As( ¯RA,B) = s( ¯RA,B)uA•B,
due au fait que u est un automorphisme du foncteur s, et
RA,B(uA • uB) = (uB • uA)RA,B,
due au fait que R est un tressage. On d´eduit alors de (15.6)
(15.8)
s( ¯RA,B) = ˜sB,ARA,B(uA • uB)˜s−1
A,Bu−1
A•B
d’o`u
s( ¯RB,A)s( ¯RA,B)
= u−1
A•B˜sA,BRB,A(uB • uA)˜s−1
B,A˜sB,ARA,B(uA • uB)˜s−1
A,Bu−1
A•B
= u−1
A•B˜sA,BRB,A(uB • uA)RA,B(uA • uB)˜s−1
A,Bu−1
A•B
= u−1
A•B˜sA,BRB,ARA,B(u2
A • u2
B)˜s−1
A,Bu−1
A•B
= ˜sA,BRB,ARA,B(u2
A • u2
B)˜s−1
A,Bu−2
A•B
comme annonc´e.
□
15.3.2. Remarques.
21On rappelle que l’hypoth`ese de commutativit´e des End(1)-bimodules A(A, B) est alors au-
tomatiquement satisfaite.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
89
a) On prendra garde au fait que les relations de commutation apparaissant dans
la preuve de la proposition 15.3.1 a) n’ont pas de raison d’ˆetre vraies en
´echangeant RA,B et s( ¯RA,B). De mˆeme, uA•B et uA • uB n’ont pas de
raison de commuter.
b) Dans le sorite 15.2.3, la condition, pour un isomorphisme naturel R : • ⇒
• ◦T, de d´eﬁnir une structure mono¨ıdale sur le foncteur identique Asym →
A, est plus faible que les conditions de tressage. Il en r´esulte que l’automor-
phisme u n’est pas arbitraire : il v´eriﬁe deux conditions suppl´ementaires du
type “cross-effects” non commutatifs d’ordre 3, qui reviennent `a dire que
la fonction A 7→uA est “de degr´e ≤2” pour la structure mono¨ıdale. Nous
laissons au lecteur le soin d’expliciter ces relations, que nous n’utiliserons
pas.
15.3.3. Proposition. Pour une section mono¨ıdale (s, ˜s), les conditions suivantes
sont ´equivalentes :
(i)
¯Rs est un tressage (notation du sorite 15.2.4).
(ii)
Il existe un automorphisme (non mono¨ıdal) v de IdA tel qu’on ait, pour u
comme dans la proposition 15.3.1, l’identit´e
(uA • uB)˜s−1
A,Bu−1
A•B˜sA,B = (vA • vB)v−1
A•B.
Si ces conditions sont v´eriﬁ´ees, le tressage ¯Rs ne d´epend pas du choix de s : pour
un choix de v comme dans (ii), il est donn´e par la formule
˜RA,B = RA,B(vA • vB)v−1
A•B.
D´emonstration. En utilisant la formule (15.8), on obtient l’identit´e
R−1
A,B ¯Rs
A,B = (uA • uB)˜s−1
A,Bu−1
A•B˜sA,B.
Si (i) est v´eriﬁ´e, le premier membre de cette identit´e d´eﬁnit une structure mono¨ı-
dale sur IdA : Asym →Asym couvrant la structure mono¨ıdale triviale sur Id ¯
A. (ii)
r´esulte alors de la proposition 13.8.1. Pour la r´eciproque, remarquons que l’identit´e
de (ii) implique que ¯Rs fait commuter le diagramme (15.1) pour tous morphismes
de A. En particulier, dans le sorite 15.2.4 le premier membre des deux identit´es se
r´eduit respectivement `a ¯Rs
A,B•C et `a ¯Rs
A•B,C : ¯Rs est donc bien un tressage.
Soit (t, ˜t) une autre section mono¨ıdale. D’apr`es le th´eor`eme 13.2.1 b), s et t
sont mono¨ıdalement conjugu´ees. En d’autres termes, il existe une famille (vA) con-
juguant s et t et v´eriﬁant l’identit´e
vA•B˜sA,B = ˜tA,BvA • vB.
On a alors
¯Rt
A,B = (v−1
B • v−1
A ) ¯Rs
A,B(vA • vB).
Ainsi, si ¯Rs est un tressage, on a ¯Rt = ¯Rs.
La derni`ere assertion est claire `a partir de la formule (15.8).
□
Nous ne connaissons pas de crit`ere pour que les conditions de la proposition
15.3.3 soient v´eriﬁ´ees, `a l’exception d’un cas : celui o`u le tressage r´esiduel ¯R est
sym´etrique. Rappelons la d´eﬁnition suivante [27, §6] :
90
YVES ANDR´E ET BRUNO KAHN
15.3.4. D´eﬁnition. Une structure balanc´ee sur une cat´egorie mono¨ıdale tress´ee
(A, •, R) est un automorphisme θ = (θA)A∈A du foncteur identique de A v´eriﬁant
l’identit´e
RB,ARA,B = (θA • θB)θ−1
A•B.
15.3.5. Th´eor`eme. Soit (A, •, R) une cat´egorie mono¨ıdale tress´ee. On suppose que
le radical est un id´eal mono¨ıdal, et on note ( ¯
A, •, ¯R) la cat´egorie mono¨ıdale tress´ee
obtenue en quotientant par le radical.
a) Si ¯R est sym´etrique, R est balanc´e via un automorphisme θ v´eriﬁant πA(θ) = 1.
b) Si de plus car K̸ = 2, les conditions de la proposition 15.3.3 sont v´eriﬁ´ees. Le
tressage ˜R correspondant est l’unique tressage sym´etrique de A tel que
(i)
πA( ˜R) = ¯R ;
(ii)
(IdA, ˜R) est mono¨ıdalement isomorphe `a (IdA, R) (cf. sorite 15.2.3).
c) Si de plus R est sym´etrique, on a s( ¯R) = R pour toute section mono¨ıdale s.
D´emonstration.
a) On applique la proposition 13.8.1 au foncteur mono¨ıdal (IdA, RA,BRB,A).
b) L’identit´e (15.7) de la proposition 15.3.1 donne une nouvelle identit´e
(θA • θB)θ−1
A•B = ˜s−1
A,Bu2
A•B˜sA,B(u−2
A • u−2
B ).
Comme car K̸ = 2, l’´el´evation au carr´e est bijective dans 1+R. En particulier, θ
a une unique racine carr´ee v. Comme θA•B et θA •θB sont centraux dans A(A•B),
˜s−1
A,Bu2
A•B˜sA,B et (u−2
A • u−2
B ) commutent. On a donc
(vA • vB)v−1
A•B = ˜s−1
A,BuA•B˜sA,B(u−1
A • u−1
B )
ce qui n’est autre que la condition (iii) de la proposition 15.3.3.
Ceci d´emontre que ˜R v´eriﬁe les conditions (i) et (ii) du th´eor`eme. Pour voir l’u-
nicit´e, soit ˜R′ un autre tressage sym´etrique v´eriﬁant ces conditions. En particulier,
(IdA, ˜R′) est mono¨ıdalement isomorphe `a (IdA, ˜R). Il existe donc µ ∈1 + R tel
que
˜R′
A,B = ˜RA,BµA•B(µ−1
A • µ−1
B )
pour tout couple d’objets (A, B). La sym´etrie de ˜R et de ˜R′ donne maintenant
l’identit´e
µ2
A•B = µ2
A • µ2
B.
En en prenant la racine carr´ee, on trouve bien que ˜R′ = ˜R.
c) Cela r´esulte de la derni`ere assertion de la proposition 15.3.3.
□
15.3.6. Exemple. Consid´erons la quantiﬁcation de Drinfeld-Cartier ¯
A[[h]] d’une
cat´egorie mono¨ıdale stricte sym´etrique ¯
A munie d’un “tressage inﬁnit´esimal” tA,B,
cf. [28, ch. 9]. Rappelons seulement que ¯
A[[h]] a les mˆemes objets que ¯
A, et que
¯
A[[h]](A, B) = ( ¯
A(A, B))[[h]] ; le tressage de ¯
A[[h]] est de la forme RA,B =
¯RA,B exp(h
2tA,B) (et la contrainte d’associativit´e est construite `a partir de tA,B au
moyen d’un associateur de Drinfeld). En g´en´eral ce tressage n’est pas sym´etrique,
mˆeme modulo h2. Toutefois, le th´eor`eme 15.3.5 b) montre par un passage `a la limite
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
91
que ( ¯
A[[h]], R) admet une structure balanc´ee, et mˆeme que ¯
A[[h]] admet un unique
tressage sym´etrique ˜R se r´eduisant en ¯R et tel que (Id, ˜R) soit mono¨ıdalement
isomorphe `a (Id, R) dans le cadre du sorite 15.2.3.
En particulier il n’est pas n´ecessaire de supposer l’existence de duaux dans ¯
A
pour construire une structure balanc´ee sur R, comme dans [12].
15.3.7. Remarque. Il est probable que les parties b) et c) du th´eor`eme sont fausses
en caract´eristique 2. Il serait int´eressant d’exhiber un contre-exemple.
15.4. Compl´ements. Pour ﬁnir, examinons de plus pr`es le d´efaut de validit´e des
conditions de la proposition 15.3.3 et le d´efaut de commutation du diagramme
(15.5). On pose uA,B = R−1
A,B(˜sB,A)−1s( ¯RA,B)˜sA,B et nA,B = 1A•B −uA,B.
On a nA,B ∈C1
s(AB) (cf. §13.6.9 pour la notation).
Soient
e = e(R) = sup{r | nA,B ∈Cr
s(AB) pour tout (A, B) ∈A × A}
¯e = ¯e( ¯R) = sup{r | [1A • mB + mA • 1B, nA,B] ∈R(A • B)r
pour tout (A, B) ∈A × A et tout (mA, mB) ∈R(A, A) × R(B, B)}.
Notons ¯nA,B l’image de nA,B dans C[e](AB) (notation du §13.6.9).
15.4.1. Proposition. a) L’´el´ement e = e(R) ∈N ∪{∞} et les ´el´ements ¯nA,B de
C[e](AB) ne d´ependent pas du choix de s : ils ne d´ependent que de R. Si A est
stricte, on a les identit´es
¯nA,B•C = ( ¯RA,B • 1C)−1(1B • ¯nA,C)( ¯RA,B • 1C) + ¯nA,B • 1C
(15.9)
¯nA•B,C = (1A • ¯RB,C)−1(¯nA,C • 1B)(1A • ¯RB,C) + 1A • ¯nB,C
(15.10)
la seconde pouvant aussi s’´ecrire
¯nA•B,C = ( ¯RB,A • 1C)(1B • ¯nA,C)( ¯RB,A • 1C)−1 + 1A • ¯nB,C.
(15.11)
b) L’´el´ement ¯e ∈N ∪{∞} ne d´epend pas du choix de s : il ne d´epend que de ¯R.
On a ¯e > e, et ¯e = ∞si et seulement si les conditions de la proposition 15.3.3 sont
v´eriﬁ´ees.
c) Soit T : (A′, •, R′) →(A, •, R) un foncteur mono¨ıdal strict tress´e radiciel (avec
(A′, •) stricte). Alors e(R′) ≤e(R).
D´emonstration. a) Soit s′ une autre section mono¨ıdale. D’apr`es le th´eor`eme
13.2.1 b), s et s′ sont conjugu´ees par une famille (vA)A∈A d’´el´ements de 1 +
R(A) v´eriﬁant l’identit´e (vA•B)˜sA,B = ˜tA,B(vA • vB). Si on note u′
A,B
=
R−1
A,B(˜s′
B,A)−1s′( ¯RA,B)˜s′
A,B, on en d´eduit l’identit´e
u′
A,B = (vA • vB)uA,B(vA • vB)−1.
Si on pose n′
A,B = 1A•B −u′
A,B, cette identit´e implique d’abord que n′
A,B ∈
R(A • B)e, ensuite que que n′
A,B ≡nA,B (mod R(A • B)e+1), et enﬁn que son
image
mod R(A • B)e+1 est dans C[e](AB).
92
YVES ANDR´E ET BRUNO KAHN
Pour ´etablir (15.9) et (15.10), on peut supposer s stricte par le point c) de la
proposition 13.4.2. En appliquant s `a (15.2) et (15.3), on obtient les identit´es
s( ¯RA,B•C) = (1B • s( ¯RA,C))(s( ¯RA,B) • 1C)
s( ¯RA•B,C) = (s( ¯RA,C) • 1B)(1A • s( ¯RB,C)).
On en d´eduit
uA,B•C = (RA,B • 1C)−1(1B • uA,C)(RA,B • 1C)(uA,B • 1C)
uA•B,C = (1A • RB,C)−1(uA,C • 1B)(1A • RB,C)(1A • uB,C)
Les identit´es (15.9) et (15.10) s’en d´eduisent facilement. En utilisant l’identit´e
RB,A•C = (1A • RB,C)(RB,A • 1C) et l’´egalit´e nA,C • 1B =
¯RB,A•C(1B •
¯nA,C) ¯R−1
B,A•C, on peut r´e´ecrire le premier terme du membre de droite de (15.10) :
( ¯RB,A • 1C)(1B • ¯nA,C)( ¯RB,A • 1C)−1.
b) r´esulte facilement des calculs de a).
c) Soit s (resp. s′) une section mono¨ıdale stricte de πA (resp. πA′) (il en existe
d’apr`es la proposition 13.4.2). Posons
uT(A),T(B) = (RT(A),T(B))−1s( ¯RT(A),T(B)), u′
A,B = (R′
A,B)−1s′( ¯R′
A,B).
D’apr`es la proposition 13.7.1, Ts′ et s ¯T sont conjugu´ees par une famille (wA)A∈A′
d’´el´ements de 1 + R(T(A)) v´eriﬁant l’identit´e
wA•B = wA • wB.
On d´eduit de ces formules que
Tu′
A,B = (wA • wB)uT(A),T(B)(wA • wB)−1.
d’o`u il est ais´e de conclure.
□
15.4.2. Remarque. Les identit´es (15.9) et (15.10) ne sont autres que les relations
de tressage inﬁnit´esimales de Drinfeld-Cartier (cf. [28, ch. 9]), v´eriﬁ´ees par htA,B
de l’exemple 15.3.6. Toutefois, ¯nA,B est “antisym´etrique” si R est sym´etrique, alors
que htA,B est “sym´etrique” dans la quantiﬁcation de Drinfeld-Cartier.
16. PREMI`ERE APPLICATION : CAT´EGORIES DE KIMURA
16.1.
Rappelons (d´eﬁnition 9.1.16) qu’une cat´egorie de Kimura sur un corps de
caract´eristique nulle K est une cat´egorie K-lin´eaire mono¨ıdale sym´etrique rigide,
v´eriﬁant End(1) = K, pseudo-ab´elienne, et dont tout objet est de dimension ﬁnie
au sens de Kimura.
16.1.1. Th´eor`eme. Soit A une cat´egorie de Kimura, de radical R. Alors
a) Le foncteur de projection A →A/R admet des sections mono¨ıdales, qui en-
voient le tressage r´esiduel ¯R de A/R sur le tressage R de A. Deux telles sections
sont mono¨ıdalement conjugu´ees.
b) Soit R′ la contrainte de commutativit´e de A/
⊗√
0 modiﬁ´ee `a l’aide de la Z/2-
graduation canonique de A/
⊗√
0 (cf. th´eor`eme 9.2.1). Par ailleurs, soit π+
A ∈
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
93
A/
⊗√
0(A, A) l’idempotent (central) associ´e canoniquement `a tout objet A de A
(ibid.) Notons ¯R′ et ¯π+
A leurs images dans A/R. Alors, pour toute section mono¨ı-
dale s : A/R →A comme en a),
(i)
L’image de s( ¯R′) (resp. de s(¯π+
A) pour tout A) dans A/
⊗√
0 est ´egale `a R′
(resp. `a π+
A).
(ii)
La famille des s(¯π+
A) d´eﬁnit une Z/2-graduation sur A, dont le tressage
modiﬁ´e associ´e est s( ¯R′). Pour ce tressage sym´etrique, la cat´egorie A reste
rigide et la dimension de tout objet A est ´egale `a kimA ; en particulier, c’est
un entier ≥0.
D´emonstration. a) r´esulte des th´eor`emes 13.2.1 et 15.3.5, appliqu´es `a A en vertu
du th´eor`eme 9.2.2. De mˆeme, b) r´esulte des mˆemes r´ef´erences, appliqu´ees `a A/
⊗√
0
munie de R′, en notant que la donn´ee de R′ est ´equivalente `a celle de (R et) des π+
A.
□
94
YVES ANDR´E ET BRUNO KAHN
IV. Enveloppes
Dans cette partie, on expose quelques applications “concr`etes” des th´eor`emes de
scindage de la partie pr´ec´edente `a la th´eorie des repr´esentations ind´ecomposables
des alg`ebres artiniennes et des groupes alg´ebriques lin´eaires. Dans ce dernier cas, le
r´esultat-cl´e 19.3.1 est une vaste g´en´eralisation du th´eor`eme classique de Jacobson-
Morosov-Kostant.
17. LE CAS NON MONO¨IDAL : ENVELOPPES PRO-SEMI-SIMPLES
Dans cette section, nous tirons les fruits du th´eor`eme 12.1.1 ; elle peut ˆetre con-
sid´er´ee comme un ´echauffement pr´eparatoire aux sections suivantes.
17.1. Enveloppes pro-semi-simples. Soient A une petite K-cat´egorie et πA : A →
¯
A le foncteur de projection sur le quotient de A par son radical. On a alors un fonc-
teur canonique
¯
A–Modf →A–Modf
entre cat´egories de modules `a gauche de K-dimension ﬁnie (nous dirons bri`evement :
K-ﬁnis), induit par M 7→M ◦πA, cf. d´eﬁnition 1.3.3. Ce foncteur est pleinement
ﬁd`ele (du fait que πA est plein et surjectif). Il en est de mˆeme du foncteur compos´e
avec πA–Mod
¯
A–Modf →A–Modf
si ¯
A-Mod est ab´elienne semi-simple22.
Prenons pour A une alg`ebre A (associative unitaire) sur un corps K parfait. On
a le foncteur d’oubli, ﬁd`ele et exact
ω : A–Modf →V ecK.
La situation ne change pas si l’on remplace A par sa compl´etion proﬁnie (com-
pl´etion eu ´egard aux id´eaux bilat`eres de K-codimension ﬁnie). On peut donc la
supposer, et on la supposera, proﬁnie, ce qui permet d’´enoncer :
17.1.1. Lemme. Si A est proﬁnie, le quotient ¯A de A par son radical est semi-simple
(proﬁnie, non n´ecessairement de K-dimension ﬁnie). A fortiori, le foncteur
¯A–Modf →A–Modf
est pleinement ﬁd`ele.
22Il y a lieu ´eventuellement de prendre un second univers pour ne travailler qu’avec de petites
cat´egories.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
95
D´emonstration. ´Ecrivons A comme limite projective ﬁltrante lim
←−Aα `a ﬂ`eches de
transition surjectives. Comme un ´el´ement inversible de A s’identiﬁe `a une collection
d’´el´ements inversibles compatibles de Aα, on obtient, en revenant `a la d´eﬁnition des
radicaux, que le radical R de A est la limite lim
←−Rα des radicaux de Aα. On a alors
un plongement A/R֒ →lim
←−(Aα/Rα), le compos´e avec la projection sur chaque
alg`ebre semi-simple Aα/Rα ´etant surjective. Comme A/R est proﬁnie (R ´etant un
id´eal ferm´e), cette injection est donc un isomorphisme, d’o`u le r´esultat.
□
On sait que A–Modf est une K-cat´egorie de Wedderburn (proposition 2.4.4).
On peut donc appliquer le th´eor`eme 12.1.1, et obtenir une section fonctorielle s :
A–Modf →A–Modf, deux telles sections ´etant conjugu´ees.
D’apr`es [53, II.2.6.3] ou [54, 2.2], il existe une K-alg`ebre pro-semi-simple As,
non n´ecessairement de K-dimension ﬁnie, telle que le compos´e ω ◦s induise une
´equivalence de cat´egories A–Modf →As–Modf, et un homomorphisme A →As.
On rappelle qu’´etant donn´e un homomorphisme f : A′ →A de K-alg`ebres
proﬁnies et le foncteur associ´e f ∗: A–Modf →A′–Modf, on a (cf. [53, II.2.6.3]
pour l’´enonc´e dual) :
– f est surjectif si et seulement si f ∗est pleinement ﬁd`ele, et pour tout A-
module K-ﬁni M, tout sous-objet de f ∗(M) provient d’un sous-objet de
M ;
– f est injectif si et seulement si tout A′-module K-ﬁni M′ est sous-quotient
d’un module de la forme f ∗(M).
En particulier, le morphisme A →As est une injection. Comme deux sections s
sont conjugu´ees, As est bien d´eﬁnie `a isomorphisme pr`es. Il d´ecoule par ailleurs du
lemme pr´ec´edent, et de loc. cit., que l’on a une surjection As →A/R.
On peut consid´erer As comme une “enveloppe pro-semi-simple” de l’alg`ebre
proﬁnie A : d’apr`es le lemme 12.1.2, les classes d’isomorphismes de A-modules
ind´ecomposables sont en bijection avec les classes d’isomorphismes de As-modules
simples.
Cette bijection est donn´ee de la mani`ere suivante : `a tout ind´ecomposable M dans
A-Modf, on peut donner une structure de As-module ´etendant celle de A-module.
On le note alors Ms ; il est simple, et EndAsMs est le corps gauche EndA(M) =
EndAM/rad(EndAM).
L’alg`ebre pro-semi-simple As est semi-simple, i.e. de dimension ﬁnie sur K, si
et seulement si A est de type de repr´esentation ﬁni. Dans ce cas, si Mα parcourt un
syst`eme de repr´esentants des classes d’isomorphismes de A-modules ind´ecomposa-
bles K-ﬁnis, notons nα la dimension de Mα sur le corps gauche Dα = EndA(Mα).
On a As ∼= Q
α Mnα(Do
α).
17.1.2. Remarques.
a) D’apr`es [14, 2.17], toute K-cat´egorie ab´elienne dont tout objet est de longueur
ﬁnie, dont toute alg`ebre d’endomorphismes est de K-dimension ﬁnie, et ad-
mettant un g´en´erateur, est ´equivalente `a une cat´egorie A–Modf pour une
K-alg`ebre A convenable de dimension ﬁnie sur K.
96
YVES ANDR´E ET BRUNO KAHN
b) Pour l’alg`ebre proﬁnie A = K[[T1, . . . , Tn]], la cat´egorie A–Modf est na-
turellement ´equivalente `a la cat´egorie RepK(Gn
a) des repr´esentations de
dimension ﬁnie du groupe vectoriel Gn
a. En effet, la cog`ebre duale de A s’i-
dentiﬁe naturellement `a la cog`ebre sous-jacente `a la big`ebre afﬁne O(Gn
a),
et on conclut par [54, 3].
c) Soit J l’id´eal de A = A-Modf form´e des morphismes qui se factorisent `a
travers un objet projectif de A-Modf. Le quotient A/J s’appelle la cat´e-
gorie stable des A-modules ﬁnis, cf. [3, p.23], et se note A–Modf. On a un
diagramme commutatif
A–Modf
pr
−−−−→A–Modf
y
y
A–Modf
pr
−−−−→A–Modf.
Le foncteur du bas pr est un foncteur plein surjectif entre cat´egories
semi-simples, donc admet une section. En fait, on peut partitionner les classes
d’isomorphismes d’objets simples de A–Modf en deux ensembles : les pro-
jectifs (P) et les autres (NP) ; pr envoie les objets dans P sur 0, et la re-
striction de pr `a la sous-cat´egorie K-lin´eaire pleine de A–Modf engendr´ee
par les objets dans NP est une ´equivalence de cat´egories. On en d´eduit que
A–Modf ∼= As–Modf pour un quotient As de As “correspondant” `a NP.
On peut alors former le “push-out” A′ = As ×As A/R.
Auslander a conjectur´e que si A et B sont deux K-alg`ebres de dimen-
sion ﬁnie telles que A–Modf et B–Modf sont ´equivalentes (´equivalence
de Morita stable), alors il y a le mˆeme nombre de modules simples non-
projectifs sur A et sur B, cf. [3, p.223]. Cela ´equivaut donc `a dire que les
alg`ebres push-out A′ et B′ sont Morita-´equivalentes.
Rappelons d’autre part que si A est de dimension globale ﬁnie (au sens
de [11]), on peut lui associer une K-alg`ebre ˆA dite r´ep´etitive (de dimension
inﬁnie sur K), et une ´equivalence de cat´egories
Db(A–Modf) →ˆA–Modf
cf. [50, 5], [22] ; on peut d’ailleurs replacer ˆA par sa compl´etion proﬁnie.
Ce qui pr´ec`ede permet alors de “d´ecrire” le quotient de Db(A–Modf) par
son radical.
17.2. Lien avec l’alg`ebre d’Auslander. L’alg`ebre d’Auslander d’une K-alg`ebre
A est
Aus(A) := EndA(
M
α
Mα),
o`u Mα parcourt un syst`eme (en g´en´eral inﬁni) de repr´esentants des classes d’isomor-
phismes de A-modules ind´ecomposables K-ﬁnis. Lorsque A est de dimension ﬁnie
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
97
sur K, elle partage avec As la propri´et´e que les classes d’isomorphismes de A-
modules ind´ecomposables sont en bijection avec les classes d’isomorphismes de
Aus(A)-modules simples, cf. [3, 4.9.5].
Cette bijection est la suivante : `a tout ind´ecomposable M dans A–Modf, on
associe le Aus(A)-module simple SM := EndA(M). En tant que K-alg`ebre,
EndA(M) s’identiﬁe `a EndAus(A)SM (loc. cit.).
L’alg`ebre Aus(A) est de dimension ﬁnie sur K si et seulement si A est de type
de repr´esentation ﬁni. Dans ce cas,
Aus(A) := Aus(A)/rad(Aus(A)) =
Y
α
Dα.
Ainsi, Aus(A) est Morita-´equivalente `a As23.
17.3. Cas des alg`ebres h´er´editaires. Rappelons qu’une K-alg`ebre est dite h´er´edi-
taire (`a gauche) si les conditions ´equivalentes suivantes sont satisfaites cf. [11, I.5] :
– tout id´eal `a gauche est projectif,
– tout sous-module d’un module projectif (`a gauche) est projectif.
C’est une condition Morita-invariante.
Supposons pour simpliﬁer K alg´ebriquement clos et A de dimension ﬁnie sur
K, minimale dans sa classe d’´equivalence de Morita (ce qui revient `a dire que ¯A =
A/R est commutative). Alors A est h´er´editaire si et seulement si A = K⃗∆est
l’alg`ebre des chemins d’un carquois ﬁni⃗∆(et sans boucle orient´ee), cf. [3, 4.2],
[13, 6]. Un A-module n’est donc rien d’autre qu’une repr´esentation K-lin´eaire de⃗
∆, et A s’identiﬁe en fait `a l’alg`ebre tensorielle sur un ¯A-bimodule ﬁni, cf. [13, 6].
Supposons en outre A de type de repr´esentation ﬁni et connexe. Alors par le
th´eor`eme de Gabriel (cf. [3, 4.7.6], [51, 2.9]), le graphe non-orient´e ∆sous-jacent
`a⃗∆est un diagramme de Dynkin des s´eries ADE. En outre, les ind´ecomposables
Mα sont en bijection avec les racines positives, et les nα ne sont autres que leurs
“longueurs” respectives (somme des coefﬁcients dans la base de racines standard).
Cela d´etermine As dans ce cas.
Voici deux exemples. Soit d’abord A la K-alg`ebre des matrices triangulaires
sup´erieures de taille n. C’est l’alg`ebre K⃗∆pour le diagramme de Dynkin⃗∆= An
(orient´e de gauche `a droite). Dans la base standard de racines α1, . . . , αn, les racines
positives sont les αij =
X
i≤k<j
αk, 0 < i < j ≤n + 1. On en d´eduit que
As ∼=
Y
1≤k≤n
(Mk(K))n+1−k.
23Aus(A) s’identiﬁe d’ailleurs au quotient par son radical de l’alg`ebre des chemins du carquois
d’Auslander-Reiten de A dont il a ´et´e question au §3.1.2, cf. e.g. [3, 4.1.11].
98
YVES ANDR´E ET BRUNO KAHN
Prenons maintenant A = KE6, l’alg`ebre des chemins du carquois de Dynkin
(orient´e) `a six sommets⃗∆= E6. `A l’aide des planches de racines [6], on trouve
As ∼= K6 × M2(K)3 × M5(K) × M6(K)2 × M7(K)3
× M8(K)2 × M9(K) × M10(K) × M11(K).
17.3.1. Remarque. Dans le cas des alg`ebres de chemins A = K⃗∆, un avatar de As
a ´et´e construite par voie g´eom´etrique dans [52].
18. SECTIONS MONO¨IDALES ET FONCTEURS FIBRES
Dans ce paragraphe, nous appliquons le th´eor`eme de scindage mono¨ıdal sym´etri-
que au cas des cat´egories tannakiennes.
18.1. Un contexte g´en´eral.
18.1.1. Th´eor`eme. Soient K un corps de caract´eristique nulle et L une extension
de K. Soit A une (petite) cat´egorie K-lin´eaire, pseudo-ab´elienne, mono¨ıdale sy-
m´etrique rigide avec K = End(1). On suppose qu’il existe un K-foncteur ﬁd`ele
mono¨ıdal sym´etrique ω : A →V ecL.
Alors R = rad(A) est mono¨ıdal, et ¯
A = A/R est tannakienne semi-simple sur K.
En particulier, si A est une cat´egorie tannakienne sur K, de radical R, alors A/R
est encore tannakienne sur K ; elle est neutre si A est neutre.
D´emonstration. On sait par le th´eor`eme 8.2.1 que A est de Wedderburn. Comme
¯
A est K-lin´eaire pseudo-ab´elienne, elle est mˆeme ab´elienne (semi-simple) ; elle est
par ailleurs rigide (cf. 6.1.4). D’autre part, la tensorialit´e du radical a ´et´e d´emontr´ee
dans le th´eor`eme 8.2.2.
Les hypoth`eses des th´eor`emes 13.2.1 et 15.3.5 sont satisfaites. On peut donc
trouver une section K-lin´eaire mono¨ıdale s de πA, qui est automatiquement sym´e-
trique. Une telle section est clairement ﬁd`ele, donc le K-foncteur mono¨ıdal sym´e-
trique ωs = ω◦s : ¯
A →V ecL l’est aussi. Comme c’est un foncteur mono¨ıdal ﬁd`ele
entre cat´egories mono¨ıdales ab´eliennes semi-simples, il est exact (les suites exactes
se scindent) ; c’est donc un foncteur ﬁbre.
La seconde assertion d´ecoule de l`a.
□
18.1.2. Remarques.
a) On pourrait aussi prouver que ¯
A est tannakienne si A l’est en utilisant la
caract´erisation interne de Deligne [14]. En effet, comme R = N, la dimen-
sion d’un objet de A ne change pas si on la calcule dans ¯
A ; c’est donc un
entier naturel. Mais cet argument ne montre pas que ¯
A est neutre quand A
l’est.
b) L’exemple de cat´egorie mono¨ıdale K-lin´eaire non strictement semi-primaire
vu plus haut (contre-exemple 3.1.4) fournit, en caract´eristique nulle, un ex-
emple d’application du th´eor`eme ci-dessus (le foncteur ω ´etant induit par
x 7→K pour tout x ∈E).
Dans cet exemple, la cat´egorie tannakienne ¯
A n’est autre que la cat´egorie
des repr´esentations du groupe diagonalisable de groupe de caract`eres E.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
99
c) L’exemple 10.1.3 montre que le th´eor`eme de scindage mono¨ıdal sym´etri-
que ne s’´etend pas, en remplac¸ant R par N, au cas o`u le radical R n’est
pas mono¨ıdal. Dans cet exemple, A/N est ´equivalente `a la cat´egorie des
super-espaces vectoriels de dimension ﬁnie, qui n’est pas tannakienne (on a
un objet de carr´e tensoriel isomorphe `a 1, mais de dimension̸ = 1).
d) Dans [1] nous d´eduisons de ce th´eor`eme, ind´ependamment de toute con-
jecture, un groupe de Galois motivique pro-r´eductif attach´e `a toute coho-
mologie de Weil “classique” d´eﬁnie sur les vari´et´es projectives lisses sur un
corps quelconque.
18.2. Le cas tannakien neutralis´e. Ce sous-paragraphe est pr´eparatoire au para-
graphe 19.
On suppose encore K de caract´eristique 0. Soient G un K-sch´ema en groupes
afﬁne (en bref : un K-groupe afﬁne) et A = RepK(G) la cat´egorie des K-repr´e-
sentations de dimension ﬁnie de G. On note πG au lieu de πA, RG le radical de A,
et ωG le foncteur ﬁbre canonique de A (`a valeurs dans V ecK).
Le lemme suivant est fort utile :
18.2.1. Lemme. Soient B une (petite) cat´egorie K-lin´eaire mono¨ıdale sym´etrique
et f : B →RepK(G) un foncteur mono¨ıdal. Pour toute K-alg`ebre commutative R,
notons f R (resp. ωR) le foncteur mono¨ıdal f (resp. ω) compos´e avec
V ecK →R −Modf
(resp.
RepK(G) →RepR(G)).
Notons Aut⊗f (resp. Aut⊗(ω ◦f)) le faisceau fpqc associ´e au foncteur R 7→
Aut⊗f R (resp. R 7→Aut⊗(ωR ◦f)). Alors
1) Aut⊗(ω ◦f) est repr´esentable par un K-sch´ema en groupes afﬁne,
2) Aut⊗(f) est repr´esentable par le centralisateur de l’image de G
∼
−→Aut⊗(ω)
dans Aut⊗(ω ◦f),
3) l’homomorphisme
Aut⊗(f) →Aut⊗(ω ◦f)
(uR) 7→(ωR(u))
(vu comme homomorphisme de groupes afﬁnes) est un monomorphisme, i.e. une
immersion ferm´ee.
D´emonstration. 1) Aut⊗(ω ◦f) est repr´esentable par le sous-sch´ema en groupes
ferm´e de G := Q
B∈B GL(ω ◦f(B)) qui ﬁxe ceux des morphismes de RepKG
qui sont de la forme ω ◦f(u), o`u u est un morphisme de B.
2) Il est clair que l’image de Aut⊗(f) dans Aut⊗(ω ◦f) centralise Aut⊗(ω). In-
versement, soit v ∈Aut⊗(ω ◦f)(R) centralisant l’image de Aut⊗(ω)(R′) pour
toute extension R′/R. Pour tout B ∈B et tout g ∈G(R′), l’´el´ement vB ∈
EndR′(ωR′(f(B))) commute `a gB. Il lui correspond donc un unique ´el´ement uB ∈
A(f R(B), f R(B)) tel que ωR(uB) = vB. La ﬁd´elit´e de ωR implique de plus que
uB est inversible et mono¨ıdal. Cela montre que Aut⊗(ω ◦f) est le centralisateur de
l’image de Aut⊗(ω) dans Aut⊗(ω ◦f), donc repr´esentable.
3) d´ecoule de ce que les ωR sont ﬁd`eles.
□
100
YVES ANDR´E ET BRUNO KAHN
Choisissons une section mono¨ıdale s de πA, et posons comme ci-dessus ωs =
ωG ◦s. Soit Gs = Aut⊗(ωs) : c’est un K-groupe pro-r´eductif. On a un homomor-
phisme ´evident :
s♯: G
∼
−→Aut⊗(ωG) →Aut⊗(ωs) = Gs
d’o`u un foncteur mono¨ıdal
(s♯)∗: RepK(Gs) →RepK(G).
18.2.2. Lemme. L’homomorphisme s♯est un monomorphisme (i.e. une immersion
ferm´ee).
D´emonstration. Soit N = Ker s♯. On a un diagramme commutatif de cat´egories et
foncteurs :
RepK(G/N)
g∗
−−−−→
RepK(G)
տ
(s♯)∗ր
RepK(Gs)
Le foncteur g∗est pleinement ﬁd`ele. Comme (s♯)∗est ´evidemment essentielle-
ment surjectif, il en est de mˆeme de g∗, qui est donc une ´equivalence de cat´egories,
d’o`u N = 1.
□
18.2.3. Remarque. Le foncteur
θs : ¯
A →RepK(Gs)
X 7→(Gs →GL(ωs(X)))
est une ´equivalence de cat´egories mono¨ıdales, mais pas en g´en´eral un isomorphisme
de cat´egories. Il poss`ede n´eanmoins un quasi-inverse canonique. On a un diagramme
strictement commutatif de cat´egories et foncteurs :
RepK(G)
ωG
−−−−→
V ecK
s
x
ωs ր
ωGs
x
¯
A
θs
−−−−→RepK(Gs)
On a ´evidemment (s♯)∗◦θs = s. En particulier, σs := πG ◦(s♯)∗est un inverse
`a gauche de θs ; c’en est donc aussi un quasi-inverse `a droite, par un isomorphisme
naturel mono¨ıdal.
Si t est une autre section mono¨ıdale de πG, elle d´eﬁnit un autre foncteur ﬁbre,
donc un autre groupe Gt. D’apr`es la th´eorie g´en´erale des cat´egories tannakiennes,
Gs et Gt sont des formes int´erieures l’un de l’autre. On a mieux, puisque t est mo-
no¨ıdalement conjugu´ee `a s. En effet, choisissons une telle conjugaison u, de sorte
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
101
que t = usu−1. On a alors un diagramme commutatif
(18.1)
Gs
s♯ր
G
ˆu
y≀
t♯ց
Gt
o`u ˆu : Aut⊗(ωs)(R) →Aut⊗(ωt)(R) est donn´e par g 7→ugu−1 pour toute K-
alg`ebre R. Cette construction donne :
18.2.4. Proposition. On a un foncteur canonique TG du groupo¨ıde connexe G⊗
u (G)
des sections mono¨ıdales de πG vers la cat´egorie des monomorphismes de G vers
un groupe pro-r´eductif, qui associe `a la section s le monomorphisme G֒ →Gs.
En particulier, pour deux sections mono¨ıdales s, t, les groupes Gs et Gt sont K-
isomorphes.
□
18.2.5. ´Eclairons et compl´etons cette construction `a l’aide des r´esultats du para-
graphe 14. Notons Γu(G) = (Eu, Su) le groupo¨ıde afﬁne scind´e unipotent transitif
sur S⊗associ´e `a A = RepK(G) par le th´eor`eme 14.3.3 : on a Γu(G)(K) = G⊗(G).
Par ailleurs, la cat´egorie tannakienne ¯
A ´etant neutre, sa gerbe est repr´esent´ee par un
K-groupo¨ıde afﬁne que nous noterons Γred(G) : la cat´egorie Γred(G)(K) est le
groupo¨ıde des K-foncteurs ﬁbres sur ¯
A. Consid´erons G comme groupo¨ıde `a un
objet. On a alors un (bi)morphisme de K-groupo¨ıdes afﬁnes
Γu(G) ×K G →Γred(G)
qui au niveau des R-points est d´ecrit de la mani`ere suivante :
Hom⊗(s, t)(R) × Aut⊗(ω)(R) →Hom⊗(ωs, ωt)(R)
(s, ∗) 7→ωs = ω ◦s.
Si l’on ﬁxe une section (K-rationnelle) s, on obtient en particulier un monomor-
phisme de K-sch´emas en groupes afﬁnes
Us = Us(G) := Eu(s, s)֒ →Gs
avec Us pro-unipotent, o`u Us centralise G. Le diagramme (18.1) se compl`ete en un
diagramme commutatif :
Us ×K G −−−−→Gs
ˆu×1
y≀
ˆu
y≀
Ut ×K G −−−−→Gt.
18.2.6. Proposition. Pour tout ´epimorphisme ϕ : Gs →
→H, le centralisateur de
ϕ ◦s♯(G) dans H est ´egal au produit ϕ(Us) × Z(H).
102
YVES ANDR´E ET BRUNO KAHN
[Noter que ce produit est direct, puisque l’intersection de ϕ(Us) et de Z(H) est
un groupe unipotent de type multiplicatif.]
D´emonstration. Par souci de clart´e, notons plus pr´ecis´ement ω = ωG. Consid´erons
le foncteur f = (s♯)∗◦ϕ∗: RepK(H) →RepK(G) : on remarque que ωG ◦f =
ωH. Appliquons le lemme 18.2.1 : on obtient que l’homomorphisme Aut⊗(f) →
Aut⊗(ωH) = H est injectif, d’image le centralisateur de l’image de Aut⊗(ωG) =
G dans H. Il reste `a calculer Aut⊗(f), que nous identiﬁons ci-dessous `a un sous-
groupe de H.
Soit h ∈Aut⊗(f)(R), o`u R est une K-alg`ebre commutative (on peut d’ailleurs
se limiter qu cas d’un corps, et mˆeme d’une extension alg´ebrique de K, puisque K
est de caract´eristique nulle). Alors πG(h) ∈Aut⊗(πG ◦(s♯)∗◦ϕ∗)(R). Comme
les foncteurs πG ◦(s♯)∗et ϕ∗sont pleinement ﬁd`eles, leur compos´e l’est aussi et
Aut⊗(πG ◦(s♯)∗◦ϕ∗)(R) s’identiﬁe canoniquement `a Aut⊗(IdRepK(H))(R) =
Z(H)(R)). Autrement dit, il existe un unique z ∈Z(H)(R) tel que πG(h) =
πG(z). Alors u = h · z−1 v´eriﬁe πG(u) = 1 ; autrement dit, u ∈ϕ(Us(R)). D’o`u
l’assertion.
□
18.2.7. Proposition. a) Pour toute section s comme ci-dessus, tout homomorphisme
ϕ de G vers un groupe pro-r´eductif H se prolonge en un homomorphisme ψ : Gs →
H.
D´emonstration. On a un diagramme commutatif
RepK(G)
ωG
−−−−→V ecK
ϕ∗ր
πG
y
RepK(H)
¯ϕ∗
−−−−→RepK(G)/RG
o`u par souci de clart´e on note ωG le foncteur ﬁbre canonique de RepK(G). On a
ωH = ωG ◦ϕ∗.
Remarquons que ¯ϕ∗est exact, puisque la cat´egorie RepK(H) est semi-simple.
Il est aussi ﬁd`ele : si A ∈RepK(H), le noyau de l’homomorphisme induit par ¯ϕ∗
de l’anneau R des endomorphismes de A vers l’anneau des endomorphismes de
¯ϕ∗(A) est l’image r´eciproque dans R du radical de l’anneau des endomorphismes
de ϕ∗(A) ; cette image r´eciproque est nulle, comme id´eal nilpotent d’une alg`ebre
semi-simple. Donc ωG ◦s ◦¯ϕ∗est un foncteur ﬁbre sur RepK(H).
Le foncteur ¯ϕ∗induit un homomorphisme
( ¯ϕ∗)♯: Gs →H′
avec H′ := Aut⊗(ωG ◦s ◦¯ϕ∗).
Appliquons la proposition 13.7.1, en remarquant que RepK(H) est semi-simple
(et mˆeme s´eparable) : il existe un isomorphisme naturel mono¨ıdal u : ϕ∗⇒s ◦¯ϕ∗,
d’o`u un isomorphisme
H
∼
−→Aut⊗(ωG ◦ϕ∗)
\
ωG(u)
−−−−→H′
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
103
faisant commuter le diagramme
G
ϕ
−−−−→H
s♯
y
\
ωG(u)
y≀
Gs
( ¯ϕ∗)♯
−−−−→H′.
D’o`u la proposition.
□
18.2.8. Lemme. Soient f, g ∈Hom(G, H), o`u G et H sont deux K-groupes
afﬁnes. Alors f et g sont conjugu´es par un ´el´ement de H(K) si et seulement s’il
existe un isomorphisme naturel mono¨ıdal f ∗
⊗≃g∗au niveau des cat´egories de
repr´esentations.
D´emonstration. Soit θ un tel isomorphisme. Alors θ induit un isomorphisme ωH =
ωG◦f ∗⊗≃ωG◦g∗= ωH. Un tel isomorphisme correspond `a un ´el´ement h ∈H(K).
Cet ´el´ement conjugue f et g.
□
18.2.9. Proposition. Soient G un K-groupe afﬁne s, t deux sections mono¨ıdales de
πG, Gs et Gt les K-groupes r´eductifs attach´es s et t, u un isomorphisme mono¨ıdal
de s sur t et ˆu : Gs
∼
−→Gt l’isomorphisme correspondant (cf. (18.1)). Soient enﬁn
H un autre K-groupe afﬁne H et f : Gs →H, g : Gt →H deux homomorphis-
mes.
Supposons que f ◦s♯et g ◦t♯soient conjugu´es par un ´el´ement de H(K). Alors il
en est de mˆeme de f et g ◦ˆu.
D´emonstration. On se ram`ene imm´ediatement au cas o`u s = t, puis au cas o`u
f ◦s♯= g ◦s♯. On a, au niveau des cat´egories de repr´esentations, une ´egalit´e de
foncteurs :
(s♯)∗◦f ∗= (s♯)∗◦g∗
d’o`u, en composant `a gauche avec πG :
σs ◦f ∗= σs ◦g∗
(cf. remarque 18.2.3).
Comme σs est un quasi-inverse mono¨ıdal de θs (ibid.), on en d´eduit l’existence
d’un isomorphisme naturel f ∗⊗≃g∗. On conclut par le lemme 18.2.8.
□
18.2.10. Scolie. Avec les notations de 10.2, on a
HH0(RepK(G)) ∼= RK(Gs) ⊗Z K.
D´emonstration. On a vu dans 10.2 que HH0(A) = HH0( ¯
A), d’o`u HH0(A) ∼=
HH0(RepK(Gs)) d’apr`es ce qui pr´ec`ede, et d’autre part et dans l’exemple 10.2.1
que HH0(RepK(Gs)) ∼= RK(Gs) ⊗Z K.
□
104
YVES ANDR´E ET BRUNO KAHN
19. AU-DEL `A DE JACOBSON-MOROZOV : ENVELOPPES PRO-R´EDUCTIVES
Dans toute ce paragraphe, K est un corps de caract´eristique 0 sauf mention ex-
presse du contraire.
Soit g une K-alg`ebre de Lie semi-simple. Le th´eor`eme de Jacobson-Morozov-
Kostant ([24], [39], [33], [7, p. 162, prop. 2 et 4]) ´enonce que tout ´el´ement nilpotent
non nul de g est contenu dans un sl2-triplet de g et que les orbites de ces deux
types d’objets sous l’action adjointe du groupe adjoint G de g sont en bijection. En
termes de groupes alg´ebriques, cet ´enonc´e se traduit ainsi : ´etant donn´e un K-groupe
alg´ebrique semi-simple G, tout homomorphisme non trivial Ga →G se prolonge
en un homomorphisme SL2 →G couvrant l’injection canonique
ϕ : Ga →SL2
(19.1)
a 7→

1
a
0
1

;
De plus, deux tels prolongements sont conjugu´es sous l’action d’un ´el´ement de
G(K).
Nous allons retrouver ce r´esultat en appliquant le th´eor`eme 18.1.1 `a la cat´egorie
tannakienne neutralis´ee des K-repr´esentations de Ga, et explorer ce qui joue le rˆole
de SL2 lorsque Ga est remplac´e par un K-groupe afﬁne quelconque, dans le ﬁl des
r´esultats du paragraphe pr´ec´edent.
19.1. Groupes `a conjugaison pr`es. Soit GaﬀK la cat´egorie dont les objets sont
les K-groupes afﬁnes et les morphismes sont les homomorphismes de K-groupes
afﬁnes. Notons GredK la sous-cat´egorie pleine de GaﬀK form´ee des groupes pro-
r´eductifs. Ces cat´egories ne sont pas bien adapt´ees `a l’interpr´etation des r´esultats du
paragraphe pr´ec´edent : nous devons les remplacer par des cat´egories plus grossi`eres.
19.1.1. D´eﬁnition. a) Soient G, H deux K-groupes afﬁnes. On note H1
K(G, H)
l’ensemble quotient de HomK(G, H) par la relation d’´equivalence ∼telle que
f ∼g s’il existe h ∈H(K) tel que g = hfh−1 (on dit aussi que f et g sont
H(K)-conjugu´es).
b) On note GaﬀK la cat´egorie dont les objets sont les K-groupes afﬁnes et dont les
morphismes sont donn´es par les ensembles H1
K(G, H) (ces morphismes se com-
posant de mani`ere ´evidente) : c’est la cat´egorie des K-groupes afﬁnes `a conjugai-
son pr`es. Sa sous-cat´egorie pleine form´ee des K-groupes pro-r´eductifs est not´ee
Gred(K) et s’appelle cat´egorie des K-groupes pro-r´eductifs `a conjugaison pr`es.
19.1.2. Remarques.
a) Notons AﬀK la cat´egorie des K-sch´emas afﬁnes. On a un diagramme com-
mutatif
GredK
ι
−−−−→GaﬀK −−−−→AﬀK
y
y
GredK
¯ι
−−−−→GaﬀK
o`u les foncteurs horizontaux sont pleinement ﬁd`eles et les foncteurs verti-
caux sont pleins et surjectifs.
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
105
b) Un certain nombre de notions “passent” aux groupes `a conjugaison pr`es (via
les foncteurs de projection ci-dessus) : immersions ferm´ees, morphismes ﬁ-
d`element plats, connexit´e, simple connexit´e, (pro-)unipotence, (pro)-semi-
simplicit´e. . .
c) La notion de sous-groupe n’a pas de sens dans Gaﬀ(K) et Gred(K) : elle
doit ˆetre remplac´ee par celle de classe de conjugaison de sous-groupes. Par
contre, la notion de sous-groupe distingu´e a un sens. De mˆeme, si H est un
sous-groupe ferm´e (`a conjugaison pr`es) de G, le sous-groupe (distingu´e)
(19.2)
H⊳= {⟨gHg−1⟩| g ∈G(K)}
a un sens.
d) On a un foncteur ﬁd`ele ´evident
Gaﬀ(K) →Lien(K)
o`u Lien(K) d´esigne la cat´egorie des liens sur K [18, II.2.1.3]. Mais ce
foncteur n’est pas plein si K n’est pas alg´ebriquement clos.
19.2. Exactitude. Peu de limites inductives existent dans GaﬀK et dans GaﬀK. Il
faut aussi prendre garde `a ce que les limites inductives calcul´ees dans GaﬀK, AﬀK
et GaﬀK, quand elles existent, ne co¨ıncident pas n´ecessairement.
Une limite inductive qui existe toujours dans GaﬀK est le co´egalisateur d’un
homomorphisme f : G →H et de l’homomorphisme trivial 1 : G →H : ce
co´egalisateur existe aussi dans GaﬀK et co¨ıncide avec le pr´ec´edent. Dire que ce
co´egalisateur est trivial est plus faible que de dire que f est un ´epimorphisme. Nous
adopterons la terminologie suivante :
19.2.1. D´eﬁnition. a) Soient f : G1 →G2 et g : G2 →G3 deux morphismes de
K-groupes afﬁnes tels que g ◦f = 1. On dit que la suite
(19.3)
G1
f
−−−−→G2
g
−−−−→G3
est exacte (resp. faiblement exacte) si Ker g = Im f (resp. si Ker g = (Im f)⊳, cf.
(19.2)).
b) Si G3 = 1 dans a), on dit que f est ´epi (resp. faiblement ´epi) si la suite (19.3) est
exacte (resp. faiblement exacte).
On remarquera que, dans b), dire que f est ´epi ´equivaut `a dire que le morphisme
associ´e de faisceaux fpqc d’ensembles est un ´epimorphisme, ou encore que f est
ﬁd`element plat.
19.2.2. Lemme. a) Un morphisme f : G1 →G2 de K-groupes afﬁnes est faible-
ment ´epi si et seulement si, pour tout K-groupe afﬁne N, l’application d’ensembles
point´es f ∗: H1
K(G2, N) →H1
K(G1, N) est de noyau trivial. Si G1, G2 ∈GredK,
il sufﬁt de prendre N dans GredK.
b) Une suite
G1
f
−−−−→G2
g
−−−−→G3 −−−−→1
106
YVES ANDR´E ET BRUNO KAHN
de K-groupes afﬁnes (avec g ◦f = 1) est faiblement exacte si et seulement si, pour
tout K-groupe afﬁne N, la suite d’ensembles point´es
1 →H1
K(G3, N)
g∗
−−−−→H1
K(G2, N)
f∗
−−−−→H1
K(G1, N)
est exacte). Si G1, G2, G3 ∈GredK, il sufﬁt de prendre N dans GredK.
c) L’exactitude faible d’une suite comme dans b) ne d´epend que des classes de f et
g dans GaﬀK.
□
D´emonstration. c) est imm´ediat.
a) : G1
f→G2 est faiblement ´epi ⇐⇒
f(G1)⊳= G2 ⇐⇒
[∀G2
h→N (avec
N pro-r´eductif si G2 l’est), h◦f = 1 =⇒h = 1] ⇐⇒
(∀¯h ∈H1
K(G2, N), f ∗¯h =
1 =⇒¯h = 1).
b) : Compte tenu de a), nous n’avons `a examiner que l’exactitude au milieu.
Or G1
f→G2
g→G3 est faiblement exacte
⇐⇒
f(G1)⊳= ker g
⇐⇒
[∀G2
h→N (avec N pro-r´eductif si G2 l’est), h|f(G1)⊳= 1 =⇒h| ker g = 1] ⇐⇒
[∀G2
h→N, h|f(G1)⊳= 1 =⇒∃G3
i→N tel que h = i ◦g)]
⇐⇒
[∀¯h ∈
H1
K(G2, N), f ∗¯h = 1 =⇒∃¯i ∈H1
K(G3, N), tel que ¯h = g∗¯i].
□
Nous nous autoriserons de ce lemme pour parler de suites faiblement exactes
dans GaﬀK.
19.3. L’enveloppe pro-r´eductive.
19.3.1. Th´eor`eme. Le foncteur d’inclusion ¯ι : GredK →GaﬀK admet un adjoint
`a gauche G 7→pRed(G). Ce foncteur est un quasi-inverse `a gauche de ¯ι.
D´emonstration. Pour chaque G ∈GaﬀK, choisissons une section mono¨ıdale s(G)
∈G⊗
u (G). On d´eﬁnit pRed(G) comme ´etant Gs(G). Soit f : G →H un homomor-
phisme. En appliquant la proposition 18.2.7 `a G et ϕ = s(H)♯◦f : G →Hs(H),
on obtient un homomorphisme ¯ϕ : Gs(G) →Hs(H). La proposition 18.2.9 montre
que son image dans H1
K(pRed(G), pRed(H)) ne d´epend pas du choix de ¯ϕ : c’est
pRed(f). La proposition 18.2.9 montre aussi que pRed est un foncteur. Les plonge-
ments G →Gs(G) d´eﬁnissent un morphisme de foncteurs IdGaﬀK →¯ι ◦pRed. Le
fait que ce morphisme fasse de pRed un adjoint `a gauche de ¯ι r´esulte de la construc-
tion pr´ec´edente et des propositions 18.2.7 et 18.2.9. Enﬁn, le fait que pRed ◦¯ι ≃Id
est ´evident.
□
19.3.2. D´eﬁnition. Le K-groupe `a conjugaison pr`es pRed(G) (muni de l’injection
canonique G֒ →pRed(G)) s’appelle l’enveloppe pro-r´eductive de G.
Son sous-groupe pU(G) (donn´e par le sous-groupe unipotent Us d´eﬁni juste avant
la prop. 18.2.6) s’appelle le compl´ement unipotent de G.
19.3.3. Remarques. a) Si f : G →H est un morphisme, nous ignorons si
pRed(f)(pU(G)) ⊂pU(H) en g´en´eral. C’est vrai si le foncteur f ∗: RepK(H)
→RepK(G) est pleinement ﬁd`ele, en vertu du d´ebut du §14.1.2 (en particulier si
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
107
f est un ´epimorphisme, mais aussi dans le cas d’un sous-groupe parabolique d’un
groupe connexe, voir la d´emonstration de la proposition 19.4.7 b)). On pourrait aussi
le d´eduire de la proposition 18.2.6. Dans ce cas, nous ignorons si le morphisme cor-
respondant est ´epi.
b) Le th´eor`eme montre que l’homomorphisme ΛG : G →pRed(G) est la limite
projective des morphismes G →H (dans GaﬀK), avec H ∈GredK (de type ﬁni si
l’on veut). En revanche, on ne pourrait pas construire pRed(G) par une telle limite
projective dans GaﬀK au lieu de GaﬀK.
Par exemple, si G = Ga, on verra plus loin que pRed(G) ∼= SL2. Consid´erons la
limite du syst`eme projectif des groupes SL2, avec pour morphismes de transition
les isomorphismes donn´es par les ´el´ements de PGL2(K) : cette limite vaut SL2
dans GredK, mais dans GredK, elle est r´eduite au centre {±1} de SL2.
19.3.4. Proposition. Supposons K alg´ebriquement clos. `A isomorphisme unique
pr`es dans Gaﬀ(K), l’homomorphisme ΛG : G →pRed(G) est caract´eris´e par les
deux propri´et´es suivantes :
(i)
pRed(G) est pro-r´eductif ;
(ii)
ΛG induit une bijection entre les classes d’isomorphismes de repr´esenta-
tions ind´ecomposables de G et de pRed(G).
D´emonstration. Il est clair que ΛG a les propri´et´es annonc´ees. Pour la r´eciproque,
la propri´et´e universelle de pRed(G) nous ram`ene `a d´emontrer l’´enonc´e suivant :
si f : H →M est un homomorphisme de groupes pro-r´eductifs qui induit une
bijection sur les classes d’isomorphismes de repr´esentations irr´eductibles, alors f
est un isomorphisme.
En effet, les cat´egories RepK(H) et RepK(M) sont semi-simples. L’hypoth`ese
implique que le foncteur f ∗: RepK(M) →RepK(H) est essentiellement sur-
jectif. D’autre part, pour deux M-repr´esentations irr´eductibles S, S′, l’application
HomM(S, S′) →HomH(S, S′) est bijective : si S et S′ ne sont pas isomorphes,
les deux membres sont nuls, et si S = S′ on a EndM(S) = EndH(S) = K
(c’est ici qu’on utilise l’hypoth`ese que K est alg´ebriquement clos). Par cons´equent,
f ∗est pleinement ﬁd`ele, donc c’est une ´equivalence de cat´egories et f est bien un
isomorphisme.
□
19.3.5. Remarque. Nous ignorons si l’hypoth`ese que K est alg´ebriquement clos
est n´ecessaire dans la proposition 19.3.4.
19.4. Quelques propri´et´es de l’enveloppe pro-r´eductive.
19.4.1. Lemme. Si G est connexe, pRed(G) est connexe.
Soit (Gs)0 la composante neutre de Gs, et soit Γ = Gs/(Gs)0 : (Gs)0 est pro-
r´eductif connexe et Γ est un groupe proﬁni (de dimension 0). Comme G est connexe,
Hom(G, Γ) = 1 ; la proposition 18.2.9 implique alors que Hom(Gs, Γ) = 1. Donc
Γ = 1.
□
19.4.2. Proposition. Si G est pro-unipotent, pRed(G) est pro-semi-simple simple-
ment connexe.
108
YVES ANDR´E ET BRUNO KAHN
D´emonstration. D’apr`es le lemme 19.4.1, Gs est connexe. Pour montrer qu’il est
semi-simple, on raisonne de mˆeme : soit G′
s son groupe d´eriv´e. Alors Γ = Gs/G′
s
est un pro-tore. Comme G est pro-unipotent, Hom(G, Γ) = 1 ; la proposition 18.2.9
implique alors que Hom(Gs, Γ) = 1. Donc Γ = 1.
Enﬁn, soit H un groupe pro-semi-simple connexe quelconque, et soit ˜H son
revˆetement universel. On a un diagramme commutatif :
H1
K(Gs, ˜H) −−−−→H1
K(G, ˜H)
y
y
H1
K(Gs, H) −−−−→H1
K(G, H).
Les propositions 18.2.7 et 18.2.9 montrent que les ﬂ`eches horizontales sont des
isomorphismes. Comme G est unipotent, il en est de mˆeme de la ﬂ`eche verticale
de droite. On en d´eduit que la ﬂ`eche verticale de gauche est un isomorphisme pour
tout H. En appliquant ceci `a H = Gs, cela implique que la projection ˜H →H
admet une section `a conjugaison pr`es. Mais ceci n’est possible que si H est pro-
simplement connexe.
□
19.4.3. Contre-exemple. On pourrait se demander si pRed(U) est mˆeme d´eploy´e.
Le contre-exemple suivant, pour U ≃G4
a, nous a ´et´e aimablement fourni par Ulf
Rehmann. Soit D une alg`ebre de quaternions sur K. Le groupe G = SL2,D con-
tient U (avec U(R) = R ⊗K D pour toute K-alg`ebre commutative R) comme
sous-groupe triangulaire sup´erieur strict. Si pRed(U) ´etait d´eploy´e, son image H
dans G le serait ´egalement. Mais un tore maximal de G est donn´e par un tore
maximal du sous-groupe diagonal form´e des ´el´ements (x, y) ∈D∗× D∗tels que
Nrd(x)Nrd(y) = 1 ; de ceci on d´eduit facilement que le rang d’un tore d´eploy´e
contenu dans G est ≤1. Ainsi H serait de rang ≤1 ; mais alors il ne peut pas
contenir U.
Par contre, un groupe semi-simple anisotrope ne peut pas ˆetre un quotient de
pRed(U), cf. [37, 1.5.3].
19.4.4. Proposition. a) Soit G2 →G1 un morphisme faiblement ´epi de K-sch´emas
en groupes afﬁnes. Alors le morphisme pRed(G2) →pRed(G1) correspondant est
faiblement ´epi.
b) Soit G3 →G2 →G1 →1 une suite faiblement exacte de K-sch´emas en groupes
afﬁnes. Alors on a un diagramme commutatif de suites faiblement exactes dans
GaﬀK :
G3
−−−−→
G2
−−−−→
G1
−−−−→1
y
y
y
pRed(G3) −−−−→pRed(G2) −−−−→pRed(G1) −−−−→1.
D´emonstration. Cela r´esulte imm´ediatement du th´eor`eme 19.3.1 et du lemme 19.2.2
(comme un adjoint `a gauche commute aux limites inductives quelconques, le th´eo-
r`eme 19.3.1 fournit des propri´et´es d’exactitude du foncteur pRed).
□
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
109
19.4.5. Corollaire. Si U est le radical unipotent de G et si Gred = G/U, on a une
suite faiblement exacte
pRed(U) →pRed(G) →Gred →1.
□
Voici quelques r´esultats structurels suppl´ementaires sur pRed(G) :
19.4.6. Lemme. Soit f : G →H un homomorphisme de K-groupes afﬁnes. Sup-
posons que le foncteur f ∗associ´e soit pleinement ﬁd`ele. Alors
(i)
pRed(f) est ´epi.
(ii)
pRed(f) est un isomorphisme si et seulement si f est un isomorphisme.
D´emonstration. (i) Si f ∗est pleinement ﬁd`ele, ¯f ∗l’est aussi ; comme c’est un
foncteur entre cat´egories semi-simples, le foncteur associ´e sur les K-goupes afﬁnes
est bien ´epi.
(ii) f est un isomorphisme ⇐⇒f ∗est une ´equivalence de cat´egories ⇐⇒f ∗
est essentiellement surjectif ; de mˆeme pour pRed(f) et ¯f ∗. Si f ∗est essentiellement
surjectif, il en est ´evidemment de mˆeme de ¯f ∗. La r´eciproque est vraie puisque le
foncteur de projection πG est plein et conservatif.
□
19.4.7. Proposition. a) Pour tout G alg´ebrique, on a une suite exacte
1 →pRed(G0)⊳→pRed(G) →G/G0 →1
o`u G0 est la composante neutre de G.
b) Si G est connexe, soit P un K-sous-groupe parabolique de G. Alors pRed(P) →
pRed(G) est ´epi.
c) Si G →H est ´epi, pRed(G) →pRed(H) est ´epi.
D´emonstration. a) ´Ecrivons G = lim
←−Gi, o`u les Gi = G/Ni sont de dimension
ﬁnie : alors, pour tout i, G0
i est l’image de G0 dans Gi. Comme le syst`eme des G0
i
est de Mittag-Lefﬂer, on a un diagramme commutatif de suites exactes courtes :
1 −−−−→
G0
−−−−→
G
−−−−→
G/G0
−−−−→1
A
y
y
B
y
1 −−−−→lim
←−G0
i −−−−→lim
←−Gi −−−−→lim
←−Gi/G0
i −−−−→1.
Comme Ker B est proﬁni et que Coker A est connexe, ce diagramme montre que
A et B sont des isomorphismes. En particulier, on a G0 = lim
←−G0/(G0 ∩Ni), et
N 0
i := G0 ∩Ni est de codimension ﬁnie dans G0 et distingu´e dans G.
Soit maintenant ρ : G0 →GL(V ) une repr´esentation de G0 (de dimension
ﬁnie) : nous allons montrer qu’elle est isomorphe `a un facteur direct d’une repr´e-
sentation W provenant de G. Ceci impliquera que pRed(G0) →pRed(G) est un
monomorphisme, d’o`u l’´enonc´e en appliquant la proposition 19.4.4 et le lemme
19.4.6.
110
YVES ANDR´E ET BRUNO KAHN
Notons U = Ker ρ : alors U est de codimension ﬁnie dans G0, et d’apr`es ce
qui pr´ec`ede il existe V ⊂G0, de codimension ﬁnie et distingu´e dans G. Notons
Γ0 = G0/V , de sorte qu’on a une suite exacte
1 →Γ0 →G/V →G/G0 →1.
Il existe un quotient ﬁni ∆de G/G0 tel que G/V soit l’image r´eciproque d’une
extension Γ de ∆par Γ0. Ainsi, on s’est ramen´e au cas o`u G est alg´ebrique. Dans
ce cas, il sufﬁt de prendre pour W la restriction `a G0 de IndG
G0V .
b) Grˆace au lemme 19.4.6 (i), il sufﬁt de prouver que le foncteur RepK(G) →
RepK(P) est pleinement ﬁd`ele. Soient V, W deux repr´esentations de G. Le groupe
G op`ere sur l’espace afﬁne Hom(V, W) via un de ses quotients alg´ebriques Γ. Soit
¯P l’image de P dans Γ : c’est un sous-groupe parabolique de Γ. Comme Γ/ ¯P est
propre et connexe, il en r´esulte que HomG(V, W) →HomP (V, W) est surjectif.24
c) Cela r´esulte encore du lemme 19.4.6 (i).
□
19.4.8. Corollaire. Pour tout K-groupe afﬁne G, on a pRed(G0) = (pRed(G)0)⊳.
D´emonstration. En effet, d’apr`es le lemme 19.4.1, pRed(G0) est connexe, donc
aussi (pRed(G)0)⊳.
□
Enﬁn, on a le r´esultat suivant.
19.4.9. Proposition. Pour tout K-groupe G et tout K-groupe pro-r´eductif H, on a
pRed(G × H) = pRed(G) × H.
D´emonstration. On peut raisonner dans Gaﬀ(K). Soit M une repr´esentation de
G × H. Comme H est r´eductif, la restriction de M `a H est semi-simple, donc
l’alg`ebre EndH(M) est semi-simple et AutH(M) = EndH(M)∗est le groupe des
K-points d’un groupe r´eductif H′ ; on a un homomorphisme G →H′. Ce dernier
se prolonge en un homomorphisme pRed(G) →H′, ce qui veut dire que l’action
de G × H sur M s’´etend en une action de pRed(G) × H.
Consid´erons le morphisme canonique (dans GredK) f :
pRed(G × H) →
pRed(G)×H. En consid´erant s´epar´ement les morphismes pRed(G) →pRed(G×
H) et H →pRed(G × H), on voit que c’est un ´epi. D’autre part, on vient de voir
que, pour toute repr´esentation M de pRed(G × H), l’application
H1
K(pRed(G) × H, GL(M)) →H1
K(pRed(G × H), GL(M))
est surjective. Par cons´equent, la restriction de M `a Ker f est triviale pour tout M ;
mais alors on a Ker f = {1}.
□
19.5. Le cas du groupe additif. `A titre d’exemple embl´ematique, calculons
pRed(G) et pU(G) pour G = Ga. Le th´eor`eme qui suit est une reformulation
pr´ecis´ee du th´eor`eme de Jacobson-Morozov25.
24Nous remercions Michel Brion de nous avoir indiqu´e ce type d’argument ; cf. aussi [53,
II.4.3.3.2].
25La preuve que nous donnons de ce r´esultat classique n’est sans doute ni la plus courte ni la plus
simple !
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
111
19.5.1. Th´eor`eme. On a pU(Ga) = Ga et pRed(Ga) = SL2. Plus pr´ecis´ement,
pour toute section mono¨ıdale s de πGa, il existe un isomorphisme de (Ga)s sur SL2
tel que s♯= ϕ, o`u ϕ est comme en (19.1).
D´emonstration. Soient V ∈A la repr´esentation ϕ de (19.1), et ¯V son image dans
¯
A. C’est une repr´esentation de rang 2 de Gs, et elle est non triviale puisque sa re-
striction `a Ga via s∗est non triviale. Comme Gs est semi-simple et connexe (propo-
sition 19.4.2), son image dans GL2 est contenue dans SL2, donc est ´egale `a SL2.
Nous allons montrer que l’homomorphisme f : Gs →SL2 correspondant est un
isomorphisme.
Pour cela, consid´erons le foncteur f ∗: RepK(SL2) →RepK(Gs) : comme f est
un ´epi, il est pleinement ﬁd`ele. Son compos´e avec s n’est autre que le foncteur de re-
striction Φ : RepK(SL2) →RepK(Ga). Comme K est de caract´eristique z´ero, les
repr´esentations irr´eductibles de SL2 sont les puissances sym´etriques de V . D’autre
part, la th´eorie des blocs de Jordan montre que les repr´esentations ind´ecomposables
de Ga sont ´egalement les puissances sym´etriques SnV de V . Ainsi, Φ induit une
bijection entre les classes d’isomorphismes de repr´esentations irr´eductibles de SL2
et les classes d’isomorphismes de repr´esentations ind´ecomposables de Ga. D’apr`es
le lemme 12.1.2, f ∗induit donc une bijection entre les classes d’isomorphismes
d’objets irr´eductibles de RepK(SL2) et celles de RepK(Gs). Comme RepK(Gs)
est semi-simple, f ∗est essentiellement surjectif, donc est une ´equivalence de cat´e-
gories, d’o`u l’assertion.
Enﬁn, l’´egalit´e s♯= ϕ et l’´egalit´e Us = Ga sont claires.
□
19.5.2. Remarque. L’espace des Ga-homomorphismes SmV →SnV est de di-
mension |P(m, n)|, avec P(m, n) = {j| |m −n| ≤j ≤m + n, j ≡m + n
mod 2}.
En effet, comme SmV est auto-dual, ces homomorphismes s’identiﬁent aux in-
variants sous Ga dans SmV ⊗SnV . Or on a la d´ecomposition de SL2-modules
SmV ⊗SnV ∼= ⊕j∈P (m,n)SjV (Clebsch-Gordan), et chaque SjV n’a qu’une droite
de vecteurs invariants sous Ga.
Pour compl´eter l’´etude de RepKGa, mentionnons le r´esultat suivant, qui nous
servira ult´erieurement.
19.5.3. Proposition. RepKGa est strictement de Wedderburn.
D´emonstration. Il s’agit de montrer que le radical inﬁni est nul. Commenc¸ons par
quelques remarques sur les ind´ecomposables de RepKGa. Ils sont de la forme
SmV , o`u V est la repr´esentation fondamentale de dimension 2, et admettent une
unique suite de composition (`a crans de dimension 1). Tout homomorphisme f de
SmV vers SnV envoie le vecteur invariant de SmV sur 0 si m > n ou si m = n et
f n’est pas un isomorphisme.
Soient alors W, W ′ deux repr´esentations, et f1, . . . fN une chaˆıne d’homomorphis-
mes dans le radical reliant W et W ′. Quitte `a remplacer f1 (resp. le compos´e f des
fi) par le morphisme correspondant ˜f1 : 1 →W ∨⊗W1 (resp. ˜f : 1 →W ∨⊗W ′),
et fi, pour i > 1, par ˜fi = 1W ∨⊗fi (qui sont tous dans le radical puisque le radical
112
YVES ANDR´E ET BRUNO KAHN
est un id´eal mono¨ıdal), on se ram`ene au cas W = 1 (noter que ˜f est le compos´e des
˜fi).
En outre, par additivit´e, on peut supposer les sources et buts des fi ind´ecompo-
sables, i.e. de la forme SnV . On a donc une chaˆıne de non-isomorphismes
1
f1
→Sn1V
f2
→Sn2V →· · ·
fN
→SnN V
o`u nN est ﬁx´e (et inf´erieur au produit des dimensions des W et W ′ originaux). Si
N > nN, on aura donc ni+1 ≤ni pour au moins l’un des i, et alors le compos´e des
fj de 1 `a i s’annulera d’apr`es l’observation pr´ec´edente.
□
19.5.4. Remarques.
a) Il suit de l’exemple 14.3.2 et du th´eor`eme 14.3.3 que le groupo¨ıde
Γ⊗(RepKGa) a le mˆeme type d’homotopie que Ga →Spec K (au sens
de loc. cit. ).
b) Supposons K de caract´eristique p > 0. Alors le radical de RepK(Ga)
n’est pas mono¨ıdal. En effet, consid´erons la repr´esentation ind´ecomposa-
ble standard W de dimension p de Ga donn´ee par t 7→exp tnp−1, o`u np−1
est l’endomorphisme nilpotent d’´echelon p (un seul bloc de Jordan). Les
endomorphismes de cette repr´esentation sont donn´es par des matrices tri-
angulaires dont les coefﬁcients diagonaux sont tous ´egaux ; leur trace est
donc nulle, ce qui montre qu’avec les notations de §4, W devient nul dans
RepK(Ga)/N. Ainsi R̸ = N, et R n’est pas mono¨ıdal d’apr`es 8.2.2.
c) Revenons `a la caract´eristique nulle. Consid´erons la cat´egorie tannakienne
A = RepKZ des repr´esentations de dimension ﬁnie sur K du groupe dis-
cret Z. Un r´esultat de ‘folklore’, bas´e sur la d´ecomposition de Jordan, dit
que son enveloppe pro-alg´ebrique est le produit de Ga par un K-groupe
afﬁne de type multiplicatif T × µ∞(T est un pro-tore, µ∞est le groupe de
torsion, cyclique). Il d´ecoule de l`a, du th´eor`eme pr´ec´edent et du corollaire
19.4.4, que ¯
A est ⊗-´equivalente `a RepK(SL2 × T × µ∞).
