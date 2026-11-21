---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-007-6-profondeur
section_title: "Profondeur"
section_number: 6
pages: 70-84
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
toc_source: inferred
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
6.1. Avec les notations de 5.1, pour tout point base x, l’inclusion de X dans A∗induit un
morphisme du groupe fondamental motivique de X dans celui, Q(1), de A∗. On d´eﬁnit la
ﬁltration par la profondeur D de π1(X, x) par
D0π1(X, x) := π1(X, x)
(6.1.1)
D1π1(X, x) := Ker(π1(X, x) →π1(A∗, x)
et, pour n ≥1,
Dnπ1(X, x) :=le ni`eme groupe de la
s´erie centrale descendante de D1π1(X, x).
On ﬁltre de mˆeme les alg`ebres de Lie:
(6.1.2)
DnLie π1(X, x) = Lie Dnπ1(X, x).
Si on pousse le π1(X, x)-torseur Py,x par π1 →π1/Dn, les Py,x/Dn obtenus forment
un groupo¨ıde quotient du groupo¨ıde des Py,x.
Appliquons A.10, A.11. La ﬁltration par la profondeur induit une ﬁltration de l’alg`ebre
enveloppante compl´et´ee U∧Lie π1(X, x) ainsi que de l’alg`ebre aﬃne O(π1(X, x)), qui en est
duale. Elle induit aussi une ﬁltration sur les alg`ebres aﬃnes des torseurs Py,x. L’alg`ebre
aﬃne du quotient π1(X, x)/Dn+1 de π1(X, x) est la sous-alg`ebre de l’alg`ebre aﬃne de
π1(X, x) engendr´ee par D−nO(π1(X, x)). De mˆeme pour les Py,x.
6.2. En r´ealisation ω, l’alg`ebre de Lie de π1(X, x) est L
∧(5.8), le compl´et´e de l’alg`ebre
de Lie libre L engendr´ee par e0 et les eζ (ζ ∈µN). La ﬁltration de profondeur est d´eduite
la graduation par le degr´e en les eζ, appel´e le D-degr´e. Cette graduation est compatible
`a la graduation provenant de celle de ω pour laquelle e0 et les eζ sont de degr´e un et
est µN-´equivariante. Elle se propage aux alg`ebres enveloppantes, aux alg`ebres aﬃnes et
aux alg`ebres aﬃnes des torseurs triviaux (Py,x)ω. L’action correspondante ρD de Gm pour
laquelle ρD(λ) ﬁxe e0 et transforme eζ en λeζ sera appell´ee action “D-degr´e”.
68
On prendra garde que les ﬁltrations D sont motiviques et stables par l’automorphisme
u 7→u−1 de X, mais que le D-degr´e est d´eﬁni seulement en r´ealisation ω et n’est pas stable
par u 7→u−1. L’automorphisme de L∧induit par u 7→u−1 ´echange e0, qui est homog`ene
de D-degr´e 0, et e∞= −e0 −P eζ, qui ne l’est pas.
6.3. Le MT(O[1/N])-sch´ema en groupe V de 5.15 agit sur P0,0 et P1,0. On d´eﬁnit la
ﬁltration D de Lie V par la condition que DpLie V soit maximal tel que l’action de Lie V sur
O(P0,0) et O(P0,1) envoie DpLie V ⊗DqO(P0,0) dans Dp+qO(P0,0) et DpLie V ⊗DqO(P1,0)
dans Dp+qO(P1,0).
Passons `a la r´ealisation ω, o`u Vω s’identiﬁe `a (Q, ◦) agissant sur les copies Q
0 et Q
1,0
de Q par g 7→⟨g⟩0 et ⟨g⟩1,0.
Proposition 6.4. L’action “D-degr´e” ρD de Gm sur Q respecte les actions ⟨g⟩0 et ⟨g⟩10
de (Q, ◦) sur Q. Elle respecte donc la loi de groupe ◦sur Q et le crochet { , } de L∧.
L’action ⟨g⟩0 de g ∈Q sur le groupe Q est caract´eris´ee par les propri´et´es de commuter
`a l’action de µN sur Q, de ﬁxer exp(e0) et d’envoyer exp(e1) sur g−1 exp(e1)g. Son conjugu´e
par
ρD(λ)
commute
encore
`a
µN,
ﬁxe
exp(e0)
et
envoie
exp(λe1)
sur
ρD(λ)(g)−1 exp(λe1)ρD(λ)(g). Cette derni`ere propri´et´e ´equivaut `a envoyer exp(e1) sur
ρD(λ)(g)−1 exp(e1)ρD(λ)(g): ρD(λ) conjugue ⟨g⟩0 en ⟨ρD(λ)(g)⟩0. Conjugant ⟨g⟩10 : x 7→
g ⟨g⟩0 (x) par ρD(λ), on en d´eduit que ρD(λ) transforme ⟨g⟩10 en ⟨ρD(λ)(g)⟩10.
6.5. Puisque l’action de Lie Vω = (L∧, { , }) sur O(P1,0)ω est ﬁd`ele, il r´esulte de 6.4 que
la ﬁltration D de Lie Vω co¨ıncide avec la ﬁltration D de L∧d´eduite de la graduation par
le D-degr´e de L. En particulier, D0Lie Vω = Lie Vω.
Transportons `a Vω l’action “D-degr´e” ρD de Gm sur (Q, ◦). Cette action gradue
Lie(Vω), son alg`ebre enveloppante universelle compl´et´ee et l’alg`ebre aﬃne O(Vω). Les ﬁl-
trations correspondantes co¨ıncident avec celles d´eﬁnie par la ﬁltration D de Lie Vω par les
DpLie Vω. Il en r´esulte que l’isomorphisme de sch´emas de Vω avec Q induit un isomor-
phisme de Vω/DpVω avec Q /Dp Q, les alg`ebres aﬃnes des quotients ´etant dans les deux
cas les sous-alg`ebres engendr´ees par D−p des alg`ebres aﬃnes (A.10). Plus pr´ecis´ement,
l’action de Vω sur Q
10 fait de Q
10 un espace principal homog`ene sous Vω, trivialis´e par
69
110 ﬁxe sous ρD, et induit une action principale homog`ene de Vω/DpVω sur Q
10 /Dp.
Ind´ependamment du foncteur ﬁbre, il reste vrai que l’action de V sur P0,0 et P1,0 induit
une action de V/DpV sur P0,0/Dp et P1,0/Dp, et que P1,0/Dp est un espace principal
homog`ene sous V/DpV .
Proposition 6.6. Le morphisme 5.15 de U dans V se factorise par D1V .
Le quotient D1V/D2 ´etant ab´elien, ce morphisme induit
(6.6.1)
U ab →D1V/D2V.
Preuve. D’apr`es 6.5, il suﬃt de v´eriﬁer que U agit trivialement sur P1,0/D1, le Q(1)-
torseur des chemins, dans A∗, de 10 `a 1. En eﬀet, Pµ,λ0 (A∗) est canoniquement isomorphe
`a Pµ,λ(A∗), et, faisant λ = µ, on voit que P1,0/D1 est le Q(1)-torseur trivial, sur lequel U
agit trivialement.
6.7. Nous nous proposons de montrer que (6.6.1) est injectif et de calculer son image.
Noter que l’action de U sur U ab, ainsi que l’action de U sur D1V/D2V (d´eduite de l’action
int´erieure de V sur lui-mˆeme), sont triviales. Les deux membres de (6.6.1) sont donc des
produits de sch´emas en groupe vectoriels Q(n), et le passage `a la r´ealisation ω ne perd
aucune information.
En r´ealisation ω, le noyau D1L de Lib(e0, (eζ)) →Lib(e0): e0 7→e0, eζ 7→0, est,
pour le crochet [
], l’alg`ebre de Lie libre engendr´ee par les (ad e0)n(eζ) (n ≥0, ζ ∈µN),
de D-degr´e 1. Le quotient D1L/D2L a donc pour base les images des (ad e0)n(eζ), ad e0
´etant pris au sens du crochet [ , ].
Notons En la composante de poids −2n de D1L/D2L, de base les images des
(ad e0)n−1(eζ). Le quotient Gr1
D(L∧) est le produit des En. Quand n sera ﬁx´e, nous ´ecrisons
simplement E pour En, et Eζ pour la base des (ad e0)n−1(eζ).
Fixons un plongement complexe σ de k. L’´el´ement dch(σ) de Vω(C) ⊂C ≪e0, (eζ) ≫
a un coeﬃcient de e0 nul (5.17). Il est donc dans D1Vω(C). Calculons sa projection dans
D1Vω/D2Vω, d’alg`ebre de Lie D1L∧/D2L∧. Pour
x =
X
λn,ζ(ade0)n−1(eζ) + termes de D-degr´e ≥2,
70
l’exponentielle de x dans Vω = Q est donn´ee par 5.14 (ii). On a
exp(x) = 1 + x + termes de D-degr´e ≥2,
et λn,ζ est donc le coeﬃcient de en−1
0
eζ dans x.
D’apr`es 5.17, la projection de dch(σ) dans D1Vω/D2Vω est donc l’exponentielle de
l’´el´ement
dch1(σ) =
X
n,ζ
X
m
σ(ζ−m)
mn

(ad e0)n−1(eζ)
de son alg`ebre de Lie Q En. Pour n = 1, ζ = 1, la somme sur m diverge et est `a remplacer
par 0.
Identiﬁons U ab et D1V/D2V `a leurs alg`ebre de Lie par l’application exponentielle et
projetons sur U ab et D1V/D2V . On obtient qu’il existe aσ dans uab
ω b⊗C v´eriﬁant
Image de aσ dans

Lie D1Vω/D2Vω =
Y
En
b⊗C
(6.7.1)
= dch1(σ)+ ´el´ement de
Y
(2πi)nEn.
Notons I l’image de Lie Uω dans Lie Vω. La ﬁltration D de Lie V induit une ﬁltration
D de I. On prendra garde que l’action “D-degr´e” de Gm sur Lie Vω n’a aucune raison de
respecter I (et en fait ne respecte pas I).
Th´eor`eme 6.8.
(i) Le morphisme (6.6.1) est injectif; il induit donc un isomorphisme
de uab
ω avec I/D2I.
(ii) En r´ealisation ω et en poids −2n, l’image dans E := En de ωn(uab) est le sous-espace
E+
distr des P xζEζ v´eriﬁant la relation de parit´e
(6.8.1)
xζ−1 = (−1)n−1xζ
et la relation de distribution de poids n −1 (resp. de distribution trou´ee si n = 1): si
N = Md avec d ≥1 et que ηM = 1, on a
(6.8.2)
xη =
1
dn−1
X
ζd=η
xζ
71
(resp. x1 = 0 et (6.8.2) seulement pour η̸ = 1 si n = 1).
Remarque 6.9 (i). La relation de parit´e (6.8.1) est la relation (6.8.2) pour d = −1.
(ii) Le Q-espace vectoriel E+
distr est muni de formes lin´eaires x 7→xζ v´eriﬁant les
relations de parit´e et de distribution de 6.8 (ii), et est universel pour cette propri´et´e. Son
dual D+
distr est muni d’une application µN →D+
distr v´eriﬁant les mˆemes identit´es, et est
universel pour cette propri´et´e: c’est l’espace dans lequel prend ses valeurs la distribution
de poids n −1 (resp. trou´ee si n = 1) de parit´e (−1)n−1 universelle.
6.10 Preuve de 6.8. Pour σ un plongement complexe de k, posons
(6.10.1)
dσ :=
X
ζ
X
m
σ(ζ−m)
mn
Eζ.
Pour n = 1, le coeﬃcient, divergent, de E1 est `a remplacer par z´ero.
D’apr`es 6.7.1, il existe aσ dans l’image de ωn(uab) tel que
(6.10.2)
dσ ≡aσ
(mod (2πi)nE).
Cas n = 1. Fixons σ et identiﬁons k `a son image dans C par σ. En particulier, ´ecrivons ζ
pour σζ. Avec cette notation, (6.10.1) se r´ecrit
(dσ)ζ = −log(1 −ζ).
D’apr`es (2.3.1), ωn(uab) est le dual de ON[1/N]∗⊗Q. Si O+
N est la partie r´eelle de
ON, c’est encore le dual de O+
N[1/N]∗⊗Q. Soit F son image dans E.
Puisque aσ est dans FC, sa partie r´eelle est dans FR. Prenant la partie r´eelle de (6.10.2),
on obtient que
−
X
log |1 −ζ| Eζ
est dans FR.
D’apr`es un th´eor`eme de Bass (1966) (cf. Washington (1997) 8.9 et 12.18), ON[1/N]∗⊗
Q, muni de ζ 7→1 −ζ (resp. 1 si ζ = 1) est la distribution trou´ee paire universelle sur
72
µN. Puisque O+
M[1/N]∗⊗Q
∼
−→ON[1/N]∗⊗Q, l’application x 7→log |x| est injective sur
ON[1/N]∗/torsion et il n’y a donc d’autres relations rationnelles entre les log |1 −ζ| que
celles d´eduites de (6.8.1) et (6.8.2). L’image F contient donc E+
distr. Puisque E+
distr a le
mˆeme rang que O∗
N[1/N]∗⊗Q, (i) et (ii) en r´esultent.
Cas n > 1. Soit F l’image de ωn ∗(uab) dans E. Prenant, selon la parit´e de n, la partie
r´eelle ou la partie imaginaire de (6.10.2), on obtient que pour tout σ
dσ + (−1)n−1 ¯dσ
est dans FC. Il r´esulte de (6.10.1) et des identit´es
X
ζd=η
ζm =
 0
si d ∤m
dηm/d
si d | m
ζ−1 = ¯ζ
que les dσ + (−1)n−1 ¯dσ sont dans (E+
distr)C.
Lemme 6.11. Le sous-espace W de EC engendr´e par les dσ ±(−1)n−1 ¯dσ est de dimension
au moins ´egale au nombre de caract`eres de (Z/NZ)∗de parit´e (−1)n−1.
D´eduisons 6.8 de 6.11. La borne inf´erieure 6.11 pour la dimension de W co¨ıncide tant
avec la dimension de ω(uab)n (2.3.1) qu’avec la dimension de E+
distr (Kubert (1979) App.).
Puisque W est contenu dans l’image complexiﬁ´ee FC, W est ´egal `a cette image, (6.1.1) est
injectif. De mˆeme, puisque S est contenu dans (E+
distr)C, on a ´egalit´e, prouvant 6.8.
Preuve de 6.11. On peut supposer que k = Q(exp(2πi/N)) ⊂C. On identiﬁe l’ensemble
des plongements complexes de k `a (Z/N)∗par ζ 7→ζa, et µN `a Z/N par b 7→exp(2πi b/N).
Avec ces notations, W est l’image de l’application
F: C(Z/N)∗→CZ/N
de matrice
X
m
exp(−2πi abm)
mn
+ (−1)n−1 exp(−2πi abm)
mn
.
73
Il nous faut minorer le rang de F. Il sera plus commode de consid´erer l’application trans-
pos´ee tF. Les applications F et tF sont ´equivariantes, pour les actions ex 7→e−1
ax et
ex 7→eax de (Z/N)∗sur les deux membres, et il suﬃt de v´eriﬁer que pour tout caract`ere χ
de (Z/N)∗de parit´e (−1)n−1, la χ-partie de tF est non nulle. Soient M le diviseur de N tel
que χ provienne d’un caract`ere primitif χ0 de (Z/M)∗, et prolongeant χ0 par 0 sur Z/M.
V´eriﬁons que l’image par tF du vecteur (χ0(b))b∈Z/N est non nulle. Prenant la composante
a = 1, on se ram`ene `a v´eriﬁer que
X
b,m
exp(2πi bm).χ0(b)
mn̸
= 0
C’est en eﬀet N/M fois le produit de la somme de Gauß P exp(2πi b)χ0(b) (somme sur
(Z/M)∗) par L(χ0, n).
Remarque 6.12. L’argument utilis´e pour n > 1, utilisant tous les plongements complexes
et (6.10.2) modulo (2πi)nE ⊗R plutˆot qu’un seul plongement et (6.10.2) modulo 2πiE,
s’applique aussi pour n = 1 si N n’a qu’un seul facteur premier. Dans ce cas en eﬀet,
l’application r´egulateur de O∗
N[1/N] dans Rm, m le nombre de places `a l’inﬁni, a un noyau
ﬁni et une image discr`ete.
Remarque 6.13. Combinant les r´esultats de cet article avec ceux de Goncharov (2001),
on obtient imm´ediatement l’analogue motivique de r´esultats de loc. cit. sur les alg`ebres de
Lie de Galois: remplacer syst´ematiquement l’alg`ebre de Lie de Galois gℓ
N par Im(Lie Uω →
Lie Vω) (voir 10.5.3) qui est son analogue motivique, et travailler sur Q plutˆot que Qℓ.
74
Appendice. Rappels sur les groupes alg´ebriques unipotents.
Dans tout cet appendice, nous supposons ˆetre en caract´eristique z´ero.
A.1. En caract´eristique z´ero, le th´eor`eme de Poincar´e-Birkhoﬀ-Witt peut ˆetre ´enonc´e
comme suit. Pour L une alg`ebre de Lie sur K, soit ϕn: SymnL →UL le produit sym´etris´e,
de la puissance symm´etrique ni`eme de L dans l’alg`ebre enveloppante de L. Pour x dans L,
il envoie xn ∈SymnL sur xn ∈UL. Le morphisme d’espaces vectoriels
(A.1.1)
ϕ∗: Sym∗L →U L
est un isomorphisme de cog`ebres. Il transforme la ﬁltration croissante de Sym∗L par les
⊕
n ≤p SymnL en la ﬁltration de UL par les images des
⊕
n ≤p ⊗nL.
Sous cette forme, le th´eor`eme est valable dans toute cat´egorie tensorielle (de car-
act´eristique 0) pseudo-ab´elienne (pour donner un sens `a Symn) qui admet des sommes
d´enombrables. Le cas qui nous int´eresse est celui des espaces vectoriels ﬁltr´es. Soit L une
alg`ebre de Lie munie d’une ﬁltration d´ecroissante F. La ﬁltration correspondante de U L
est caract´eris´ee par la propri´et´e qu’une ﬁltration sur un L-module M est compatible `a
la ﬁltration de L si et seulement si elle l’est `a celle de U L. La version cat´egorique de
Poincar´e-Birkhoﬀ-Witt implique la compatibilit´e de (A.1.1) aux ﬁltrations.
Une ﬁltration F sur un L-module M est compatible la ﬁltration centrale descendante
Z de L, si et seulement si les F pM sont des sous-modules et que L agit trivialement sur
les Grp
F M. La ﬁltration de U L induite par le ﬁltration Z de L est donc la ﬁltration par les
puissances de l’id´eal d’augmentation I. Par compatibilit´e de (A.1.1) aux ﬁltrations, on a
Corollaire A.2. Si l’alg`ebre de Lie L, de s´erie centrale descendante Z, est nilpotente de
classe c (Zc+1 = 0), alors, si on identiﬁe Sym∗L et U L par (A.1.1), on a
(A.2.1)
In ⊃
⊕
p ≥n SympL ⊃Inc
Notons U
∧L le compl´et´e I-adique de U L.
75
Corollaire A.3. Si l’alg`ebre de Lie L est nilpotente, l’isomorphisme (A.1.1) induit par
compl´etion un isomorphisme d’espace vectoriels
(A.3.1)
Y
n ≥0
SymnL →U
∧L.
L’isomorphisme (A.3.1) est compatible aux topologies des deux membres. A gauche,
la topologie est la topologie produit (d’espaces discrets). A droite, celle de limite projective
des (espaces discrets) U L/In.
A.4. Le foncteur “alg`ebre de Lie” est une ´equivalence de la cat´egorie des groupes alg´ebriques
unipotents avec celle des alg`ebres de Lie nilpotentes de dimension ﬁnie. De plus, le fonc-
teur ρ 7→dρ est une ´equivalence de la cat´egorie des repr´esentations lin´eaires (de dimension
ﬁnie) de V , suppos´e unipotent, avec celle des repr´esentations nilpotentes de son alg`ebre de
Lie v.
On dispose d’une application exponentielle
(A.4.1)
exp: v →V
caract´eris´ee par la propri´et´e que pour toute repr´esentation lin´eaire ρ de V , on ait
(A.4.2)
ρ(exp(x)) = exp(dρ(x)).
C’est un isomorphisme de v, muni de la loi de groupe de Campbell-Hausdorﬀ, avec V .
A.5. Soit V un groupe alg´ebrique unipotent d’alg`ebre de Lie v. L’alg`ebre enveloppante Uv
est l’alg`ebre des op´erateurs diﬀ´erentiels sur V invariants par translations `a gauche. Comme
cog`ebre, c’est le dual topologique du compl´et´e de l’anneau local de V en 1. L’application
exponentielle (A.4.1) induit un isomorphisme de la cog`ebre Uv avec la cog`ebre Sym∗v des
op´erateurs diﬀ´erentiels en 0 sur l’espace aﬃne v.
Par r´eduction au cas o`u v est de dimension un, on v´eriﬁe que cet isomorphisme envoie
xn ∈Symnv sur xn ∈Uv. C’est donc l’isomorphisme (A.1.1). Pour l’espace aﬃne v,
l’alg`ebre aﬃne de v est le dual topologique de la cog`ebre compl´et´ee Q
n>0
Symnv. Appliquant
A3, on obtient:
76
Proposition A.6. L’alg`ebre aﬃne de V est le dual topologique de la cog`ebre Uv, compl´et´ee
pour la topologie I-adique.
Dualement, le dual (muni de la topologie faible) de l’alg`ebre aﬃne de V est U
∧v. Les
points de V `a valeurs dans une alg`ebre A (homomorphismes de l’alg`ebre aﬃne dans A)
sont les ´el´ements groupaux g de Ab⊗U
∧v: les ´el´ements d’augmentation 1 tels que ∆g =
g ⊗g. Compatibilit´es: l’application exponentielle (A.4.1) est l’exponentielle, de A ⊗g dans
V (A) ⊂Ab⊗U
∧v. La loi de groupe est le produit dans U
∧v.
A.7. Un sch´ema en groupe aﬃne G est la limite projective de ses quotients Gα qui sont
des groupes alg´ebriques. Il y a lieu de d´eﬁnir son alg`ebre de Lie Lie(G) comme ´etant
la pro-alg`ebre de Lie limite projective des Lie(Gα). De fa¸con ´equivalente, c’est la limite
projective des Lie(Gα), qui sont de dimension ﬁnie, munie de sa topologie de limite pro-
jective d’espaces discrets. C’est le dual de la limite inductive colim(Lie(Gα)∨), muni de sa
topologie faible.
A.8. Un sch´ema en groupe aﬃne G est pro-unipotent s’il est limite projective de groupes
alg´ebriques unipotents, i.e. si les Gα de A.7 sont unipotents. On d´eﬁnit l’alg`ebre envelop-
pante compl´et´ee U
∧Lie(G) de Lie(G) par
U
∧Lie G = limα U
∧Lie(Gα) = limα,n U(Lie(Gα))/In,
cette limite ´etant munie de sa topologie de limite projective. Avec ces d´eﬁnitions, A.6 reste
valable, comme on le v´eriﬁe par passage aux limites.
A.9. Cas particulier. Soit Lib((xi)i∈I) l’alg`ebre de Lie libre sur K engendr´ee par une
famille ﬁnie de g´en´erateurs xi. Notons-la simplement Lib. Son alg`ebre enveloppante est
l’alg`ebre associative libre K ⟨(xi)i∈I⟩.
Soit Lib
∧le compl´et´e de Lib pour la ﬁltration centrale descendante. C’est l’alg`ebre de
Lie du sch´ema en groupe pro-unipotent
exp(Lib
∧) = lim exp(Lib/Zn).
77
Son alg`ebre enveloppante compl´et´ee est l’alg`ebre des s´eries formelles associatives K ⟨⟨(xi)⟩⟩.
Les points de exp(Lib
∧) `a valeurs dans une K-alg`ebre A sont les ´el´ements groupaux
g de K ⟨⟨(xi)⟩⟩: terme constant 1 et ∆g = g ⊗g, ∆´etant le coproduit K ⟨⟨(xi)⟩⟩→
K ⟨⟨(xi)⟩⟩b⊗K ⟨⟨(xi)⟩⟩tel que ∆xi = xi ⊗1 + 1 ⊗xi.
A.10. Soit v l’alg`ebre de Lie d’un groupe alg´ebrique nilpotent V , et soit D une ﬁltration
d´ecroissante ﬁnie de l’alg`ebre de Lie v, telle que D0(v) = v. On notera encore D la ﬁltration
de V par les sous-groupes d’alg`ebres de Lie les Dpv. Puisque [Dpv, Dqv] ⊂Dp+qv, ce sont
des sous-groupes distingu´es, et pour p ≥1, DpV/Dp+1V est ab´elien.
On notera encore D les ﬁltrations induites sur Uv, U
∧v et son dual O(V ). La ﬁltration
n 7→D−nO(V ) de O(V ) est croissante, et D1O(V ) = 0.
Pour v muni du crochet nul, exp(v, crochet 0) est le sch´ema pro-vectoriel v.
Par A.1, l’application exponentielle exp: v →V respecte les ﬁltrations D des alg`ebres
aﬃnes. Par r´eduction au cas lin´eaire, on en d´eduit que l’alg`ebre aﬃne de V/Dn+1V est la
sous-alg`ebre de O(V ) engendr´ee par D−nO(V ). En particulier, D0O(V ) est l’alg`ebre aﬃne
de V/D1V .
Si M est une repr´esentation de V , les conditions suivantes sur une ﬁltration F de M
sont ´equivalentes:
compatiblit´e `a D sur v: Dpv ⊗F qM →F p+qM,
compatibilit´e `a D sur Uv: DpUv ⊗F qM →F p+qM,
compatibilit´e `a D sur O(V ): F pM →P D−rO(V ) ⊗F p+rM
La ﬁltration D de O(V ) est stable par translations `a gauche et `a droite. Si P est un
V -torseur, elle fournit encore une ﬁltration D sur l’alg`ebre aﬃne O(P) de P.
A.11 Fonctorialit´es. (i) Soient v1 une sous-alg`ebre de Lie de v (resp. un quotient)
et V1 le sous-groupe (resp. quotient) correspondant de V . Notons D1 la ﬁltration de v1
induite par (resp. quotient de) la ﬁltration D de v, et les ﬁltrations qui s’en d´eduisent
sur Sym∗v1, Uv1, U
∧v1 et O(V1). La puissance symm´etrique Symn(v1) est un sous-espace
(resp. quotient) de Symn(v), et sa ﬁltration D1 est induite par (resp. quotient de) la
ﬁltration D de Symn(v). Il r´esulte de A.1 que la mˆeme assertion vaut pour Uv1 et U
∧v1 et
78
que dualement, la ﬁltration D1 du quotient (resp. sous-espace) O(V1) de O(V ) est quotient
de (resp. induite par) la ﬁltration D de O(V ).
(ii) Supposons que la ﬁltration D de v provienne d’une graduation v =
⊕
n ≥0 vn. Cette
graduation se propage `a Sym∗(v), Uv, U
∧v et O(V ). Pour U
∧v, “graduation” et `a prendre
au sens de “d´ecomposition en produit” plutˆot que “d´ecomposition en somme”. La ﬁltration
D de Symn(v) provient de la graduation de Symn(v). Par A.1, la mˆeme assertion vaut
pour Uv, U
∧v et O(V ).
(iii) Par passage `a la limite, A.10 et A.11 restent valable dans le cas pro-unipotent.
A.12 Exemples. (i) Prenons l’alg`ebre de Lie pro-unipotente Lib
∧de A.9, et la ﬁltration
centrale descendante Z. Elle provient de la graduation pour laquelle les xi sont de degr´e 1.
Chaque monˆome m en les xi d´eﬁnit sur exp(Lib
∧) ⊂k ⟨⟨(xi⟩⟩une fonction cm “coeﬃcient
de m dans g”, et l’alg`ebre aﬃne a pour base les cm. Le produit est le produit de m´elange.
Le degr´e de cm est l’oppos´e de celui de m.
(ii) Parmi les g´en´erateurs xi, distinguons en un, not´e x0, et posons I = {0} ∐J. On a
Lib := Lib((xi)i∈I) = k.x0 ⋉Lib((ad x0)n(xj), (n ≥0, j ∈J)).
Soit D la ﬁltration de Lib pour laquelle Dp est, pour p ≥1, la s´erie centrale descendante
du second facteur. La ﬁltration D provient de la graduation pour laquelle x0 est de degr´e
0 et les xj (j ∈J) de degr´e 1. Compl´etant cette ﬁltration, on obtient une ﬁltration, encore
not´ee D, de Lib
∧. La ﬁltration correspondante de l’alg`ebre aﬃne
O(exp(Lib
∧))
est d´eduite de la graduation pour laquelle le degr´e de cm est l’oppos´e du degr´e du monˆome
m en les xj (j ∈J).
A.13. Soit G un groupe alg´ebrique produit semi-direct du groupe multiplicatif Gm par
un groupe alg´ebrique unipotent V , d’alg`ebre de Lie v. L’action de Gm sur v gradue cette
alg`ebre de Lie; sur vn, λ ∈Gm agit par multiplication par λn.
Supposons v `a degr´es > 0. Le foncteur ρ 7→dρ est alors une ´equivalence de la cat´egorie
des repr´esentations lin´eaires de G avec celle des espaces vectoriels gradu´es E, muni d’une
79
action compatible aux graduations de l’alg`ebre de Lie v. La graduation de E donne l’action
de Gm et l’action de v, automatiquement nilpotente, donne celle de V .
Notons k(a) l’espace vectoriel k plac´e en degr´e a. Pour a < b, une extension de k(a)
par k(b) dans la cat´egorie des repr´esentations de G est donn´ee par un homomorphisme
v →Hom(k(a), k(b)), i.e. par un ´el´ement du dual de la partie homog`ene de degre´e b −a
de vab := v/[v, v]:
(A.13.1)
Ext1
Rep(G)(k(a), k(b)) = (vab)b−a
∨.
A.14. Soit G un sch´ema en groupes produit semi-direct de Gm par V pro-unipotent.
Ecrivons-le comme limite projective de quotients par des sous-groupes distingu´es contenus
dans V :
G = Gm ⋉V = lim Gm ⋉Vα.
Supposons les alg`ebres de Lie gradu´ees vα des Vα (A.13) `a degr´e > 0. Passant `a la
limite, on d´eduit de (A.13.1) que
(A.14.1)
Ext1
Rep(G)(k(a), k(b)) = colim(vab
α )b−a
∨.
Supposons en outre que pour tout,
dim Ext1(k(0), k(n)) < ∞.
Les limites projectives (A.14.1) sont alors stationnaires et, puisque si on rel`eve dans les
(vα)n des bases des (vab
α )n, on obtient un syst`eme g´en´erateur de vα, la dimension de
(vα)n est, pour chaque n, born´ee ind´ependamment de n. On notera vgr l’alg`ebre de Lie
gradu´ee de composantes homog`enes les limites projectives (stationnaires) des composantes
homog`enes des vα. Passant `a la limite dans A.13, on obtient:
Proposition A.15. Sous les hypoth`eses de A.14: G = Gm ⋉V , Lie V `a degr´es > 0,
Ext1
Rep(G)(k(0), k(n)) de dimension ﬁnie, le foncteur ρ 7→dρ est une ´equivalence de la
cat´egorie des repr´esentations de G avec celle des espaces vectoriels gradu´es munis d’une
action de l’alg`ebre de Lie gradu´ee vgr. On a
Ext1
Rep(G)(k(0), k(n)) = (vab
gr )
∨
n.
80
Bibliographie
H. Bass. Generators and relations for cyclotomic units, Nagoya Math. J. 27 (1966),
p. 401–407.
A. Beilinson, J. Bernstein, et P. Deligne. Faisceaux pervers, in: Analyse et topologie sur
les espaces singuliers, Ast´erisque 100, SMF (1982).
S. Bloch. Algebraic cycles and algebraic K-theory, Adv. in Math. 61, 3 (1986), p. 267–304.
. The moving lemma for higher Chow groups, J. Alg. Geom. 3, 3 (1994), p. 537–
568.
K. T. Chen. Iterated integrals of diﬀerential forms and loop space homology, Ann. of Math.
97 (1973), p. 217–246.
. Reduced Bar Constructions on de Rham complexes, in: Algebra, Topology and
Category Theory, a collection of papers in honor of Samuel Eilenberg, p. 19–32, Academic
Press (1976).
P. Deligne. Le groupe fondamental de la droite projective moins trois points in: Galois group
over Q, MSRI Publ. 16, p. 79–313, Springer Verlag (1989).
. Cat´egories tannakiennes in: Grothendieck Festschrift vol. 2, p. 111–195. Progress
in Math. 87, Birkh¨auser (1990).
M. Demazure et P. Gabriel. Groupes alg´ebriques, Masson (1970).
A. B. Goncharov. Polylogarithms in arithmetic and geometry, Proc. ICM Zurich 1994,
p. 374–387, Birkhauser.
A. B. Goncharov. The dihedral Lie algebras and Galois symmetries of π1(P1−{0, ∞} ∪µN),
Duke Math. J. 110 3 (2001), p. 397–487.
R. Hain and M. Matsumoto. Weighted completion of Galois groups and Galois actions on
the fundamental group of P1 −{0, 1, ∞}, preprint (2001).
R. Hain and S. Zucker. Unipotent variations of mixed Hodge structure, Inv. Math. 88,
(1987) p. 83–124.
M. Hanamura. Mixed motives and algebraic cycles I., Math. Res. Lett. 2, 6 (1995), p. 811–
821. See also II, preprint (1996).
A. Huber. Mixed Motives and their Realization in Derived Categories, Lecture Notes in
Math. 1604, Springer Verlag (1995).
. Realization of Voevodsky’s motives, J. Alg. Geom. 9 (2000), p. 755–799.
81
U. Jannsen. Mixed motives and algebraic K-theory, Lecture Notes in Math. 1400, Springer
Verlag (1990).
D. Kubert. The universal ordinary distribution, Bull. SMF 107 (1979), p. 179–202.
M. Levine. Tate motives and the vanishing conjectures for algebraic K-theory, in: Algebraic
K-theory and algebraic topology (Lake Louise, 1991), p. 167–188. NATO Adv. Sci. but.
Ser. C Math. Phys. 407, Kluwer (1993).
. Bloch’s higher Chow groups revisited, in: K-theory (Strasbourg 1992), p. 235–320,
Ast´erisque 226, SMF (1994).
. Mixed Motives, Math. Surveys and Monographs 57, AMS (1998).
Chr. Reutenauer. Free Lie algebras, LMS monographs new ser. 7, Oxford University Press
(1993).
T. Terasoma. Multiple zeta values and mixed Tate motives.
V. Voevodsky. Triangulated categories of motives over a ﬁeld, in: Cycles, transfer and
motivic homology theories, p. 188–238, Ann. of Math. Studies 143, Princeton University
Press (2000).
L. C. Washington. Introduction to cyclotomic ﬁelds – graduate texts in Math. 81, Springer
Verlage (1997).
Z. Wojtkowiak. Cosimplicial objects in algebraic geometry, in Algebraic K-theory and
algebraic topology (Lake Louise, 1991), p. 287–327. NATO Adv. Sci. but. Ser. C Math.
Phys. 407, Kluwer (1993).
82
