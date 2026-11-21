---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-005-4-le-groupe-fondamental-unipotent-motivique-dune
section_title: "Le groupe fondamental unipotent motivique d’une vari´et´e rationnelle"
section_number: 4
pages: 43-53
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
toc_source: inferred
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
4.1. Soient k un corps de nombres, P une droite projective sur k, X le compl´ement d’un
ensemble ﬁni S de points rationnels et x, y ∈X(k). Dans Deligne (1989) §13, nous avons
d´eﬁni un “espace de (classes d’homotopie de) chemins motivique” not´e Py,x. Sous les
hypoth`eses ci-dessus, et apr`es oubli de l’aspect cristallin de loc. cit., c’est un sch´ema aﬃne
en la cat´egorie tannakienne RH+ℓde 2.15. Nous le noterons ici P H+ℓ
y,x , ou P H+ℓ
y,x (X) s’il y a
lieu de pr´eciser X. On dispose d’une “composition des chemins” P H+ℓ
z,y
× P H+ℓ
y,x
→P H+ℓ
z,x .
Posons πH+ℓ
1
(X, x) := P H+ℓ
x,x . Pour la composition des chemins, c’est un RH+ℓ-sch´ema
en groupes aﬃne et P H+ℓ
y,x
est un espace principal homog`ene `a droite sous πH+ℓ
1
(X, x),
`a gauche sous πH+ℓ
1
(X, y): un (πH+ℓ
1
(X, x), πH+ℓ
1
(X, y))-bitorseur. Pour σ un plongement
de k dans une clˆoture alg´ebrique C de R, la r´ealisation σ de πH+ℓ
1
(X, x) est l’enveloppe
alg´ebrique prounipotente de π1(X(C), x). Si I est l’id´eal d’augmentation de l’alg`ebre de
groupe Q[π1(X(C), x)], c’est le spectre de l’alg`ebre de Hopf commutative
colim(Q[π1(X(C), x)]/IN)
∨.
i.e. c’est l’enveloppe alg´ebrique pro-unipotente de π1(X(C), x).
4.2. Soit AH+ℓ
y,x
l’alg`ebre aﬃne (2.6) de P H+ℓ
y,x . D’apr`es 3.12, 3.13, le Ind-objet AH+ℓ
y,x
de
RH+ℓest l’image par le foncteur r´ealisation d’un Ind-objet Ay,x de MT(k). D’apr`es 2.14,
2.15 (ii), le produit AH+ℓ
y,x
⊗AH+ℓ
y,x
→AH+ℓ
y,x
provient d’un produit sur Ay,x, et P H+ℓ
y,x
est
la r´ealisation du MT(k)-sch´ema aﬃne Py,x := Spec(Ay,x). De mˆeme, la composition des
chemins est d´eﬁnie par un coproduit AH+ℓ
z,x
→AH+ℓ
z,y
⊗AH+ℓ
y,x , ce coproduit se rel`eve `a
MT(k) et d´eﬁnit un morphisme Pz,y × Py,x →Pz,x.
Nous appellerons ici Py,x l’espace de chemins de x `a y motivique. Nous appelerons
Px,x le groupe fondamental motivique de X en x et le noterons πmot
1
(X, x) ou simplement
π1(X, x). Mise en garde: bien que la notation ne l’indique pas, il s’agit de π1 rendus
unipotents.
4.3. Appelons “point base de X” soit un point rationnel de X = P −S, soit un vecteur
tangent non nul en un point de S (“points base `a l’inﬁni”). Pour x et y deux points-base
41
de X, Deligne (1989) d´eﬁnit §15 un “espace de chemins motivique de x `a y”. Comme en
4.1, c’est, apr`es oubli d’un aspect cristallin, un RH+ℓ-sch´ema aﬃne. Nous le noterons ici
P H+ℓ
y,x , et, pour x = y, πH+ℓ
1
(X, x).
Th´eor`eme 4.4. Avec les notations de 4.1 et 4.3, si x et y sont deux points-base de X, le
RH+ℓ-sch´ema P H+ℓ
y,x
est motivique, i.e. la r´ealisation d’un MT(k)-sch´ema Py,x.
Si S est vide ou r´eduit `a un point, X = P −S est simplement connexe, les P H+ℓ
y,x
sont r´eduits `a un point et 4.4 est trivial. Nous pouvons donc supposer, et supposerons, que
|S| ≥2. Le cas o`u x et y sont `a distance ﬁnie ayant d´ej`a ´et´e trait´e, nous supposerons au
moins l’un de x et y `a l’inﬁni.
Cas 1. x ∈X(k) et y est un vecteur tangent non nul en ¯y ∈S.
Soit Z le MT(k)-sch´ema des homomorphismes de Q(1) dans πmot
1
(X, x). Identiﬁant ho-
momorphismes de sch´emas en groupe unipotents, et homomorphismes entre leurs alg`ebres
de Lie, on peut en donner la description suivante: Lie πmot
1
(X, x) est une pro-alg`ebre de
Lie dans MT(k), en particulier un pro-objet de MT(k) (c’est la limite projective des
Lie (πmot
1
(X, x)/ZN), pour Z la s´erie centrale descendante), et on d´eﬁnit Z comme ´etant
le MT(k)-sch´ema pro-vectoriel (2.6) Lie πmot
1
(X, x)(−1).
Dans ZH+ℓ:= realH+ℓ(Z), on dispose du sous-sch´ema ferm´e “classe de conjugai-
son de la monodromie locale autour de ¯y ”. Voici sa d´eﬁnition. Ecrivons Q(1)H+ℓpour
realH+ℓ(Q(1)). On dispose d’un morphisme “monodromie locale autour de ¯y ”:
(4.4.1)
Q(1)H+ℓ→πH+ℓ
1
(X, y).
Dans (4.4.1), Q(1)H+ℓest vu comme un RH+ℓ-sch´ema vectoriel, avec sa structure de
groupe. Si T¯y est l’espace tangent en ¯y, et que T ∗
¯y := T¯y −{0}, il y a lieu de voir (4.4.1)
comme un morphisme
πH+ℓ
1
(T ∗
¯y , y) →πH+ℓ
1
(X, y).
La donn´ee de (4.4.1) ´equivaut `a celle de
(4.4.2)
Q(1)H+ℓ→Lie πH+ℓ
1
(X, y).
42
Dans (4.4.2), Q(1)H+ℓest un objet de RH+ℓ, muni de sa structure d’alg`ebre de Lie com-
mutative.
On dispose aussi de l’espace de chemins P H+ℓ
y,x
et, par composition des chemins, de
(p, γ) 7−→p−1γp: P H+ℓ
y,x
× πH+ℓ
1
(X, y) →πH+ℓ
1
(X, x).
Composant avec (4.4.1), on en d´eduit
(4.4.2)
P H+ℓ
y,x
× Q(1)H+ℓ→πH+ℓ
1
(X, x).
Le groupe πH+ℓ
1
(X, y) agit par composition `a gauche sur P H+ℓ
y,x . Divisant `a gauche par
Q(1)H+ℓ, vu par (4.4.1) comme sous-groupe de πH+ℓ
1
(X, y), on d´eﬁnit
P H+ℓ
¯y,x
:= Q(1)H+ℓ\ P H+ℓ
y,x
et (4.4.2) se factorise par P H+ℓ
¯y,x
× Q(1)H+ℓ, d´eﬁnissant
(4.4.3)
P H+ℓ
¯y,x
→ZH+ℓ
Lemme 4.5. Le morphisme (4.4.3) est un plongement ferm´e de RH+ℓ-sch´emas.
Preuve. Il suﬃt de le v´eriﬁer en r´ealisation de de Rham, o`u l’assertion se r´eduit `a la
suivante.
Lemme 4.6. Soit L l’alg`ebre de Lie sur k engendr´ee par des ´el´ements (es)s∈S soumis `a
la seule relation que P es = 0. On suppose |S| ≥2, on ﬁxe ¯y ∈S et on pose e := e¯y. Soit G
le sch´ema en groupe prounipotent limite projective des GN := exp(L/ZN). Le morphisme
de G/ exp(ke) dans Lie(G): g 7→ad g(e), identiﬁe G/ exp(ke) `a un sous-sch´ema ferm´e de
Lie(G), l’orbite adjointe de e.
Dans 4.6, Lie(G) est le sch´ema pro-vectoriel limite projective des sch´emas vectoriels
Lie(GN).
Preuve. Les orbites de l’action d’un groupe unipotent sur un sch´ema aﬃne sont ferm´ees
Demazure, Gabriel (1970) IV 2.2.7). Si eN est l’image de e dans L/ZN et ZN ⊂GN son
43
ﬁxateur, l’application g 7→ad g(eN) de GN/ZN dans Lie(GN) est donc un plongement
ferm´e. Par passage `a la limite projective, l’application g 7→ad g(e) de lim GN/ZN dans
Lie(G) = lim Lie(GN) est ´egalement un plongement ferm´e.
L’alg`ebre de Lie du sous-groupe ZN de GN est le centralisateur de eN dans L/ZN.
Fixons b dans S distinct de ¯y. L’alg`ebre de Lie L est librement engendr´ee par les es (s̸ = b).
D’apr`es 4.7 ci-dessous, le centralisateur de e est r´eduit `a ke. Munissons L de la graduation
pour laquelle les es sont de degr´e 1. La sous-alg`ebre ZN est la sous-alg`ebre “degr´e ≥N”.
L’application lin´eaire ad e: L →L ´etant de degr´e 1 et de noyau r´eduit `a ke, on a
Lie ZN = Ker(ad eN: L/ZN →L/ZN) = keN + ZN−1/ZN.
La projection de GN+1/ZN+1 sur GN/ZN se factorise donc par GN/ exp(keN) et
G/ exp(ke) = lim GN/ exp(keN)
∼
−→lim GN/ZN(e).
Lemme 4.7. Dans une alg`ebre de Lie libre L sur k, le centralisateur d’un g´en´erateur e
est r´eduit aux multiples de ce g´en´erateur.
D’apr`es Reutenauer (1993) 2.10, dans une alg`ebre de Lie libre, deux ´el´ements non nuls
quelconques qui commutent sont multiples l’un de l’autre. Le cas particulier 4.7 est, plus
simplement, cons´equence de ce que l’alg`ebre de Lie libre Lib({e} ∪A) est le produit semi-
direct de ke et de Lib((ad en(a))a∈A,n ≥0 et de ce que la d´erivation ad en(a) 7→ad en+1(a)
de l’alg`ebre associative libre engendr´ee par les ad en(a) est injective.
Il r´esulte de 4.5 que P H+ℓ
¯y,x
est motivique. Soient en eﬀet A l’alg`ebre de Z et AH+ℓ:=
realH+ℓ(A) celle de ZH+ℓ. D’apr`es 4.5, P H+ℓ
¯y,x
est isomorphe `a un sous-sch´ema ferm´e de
ZH+ℓ, d´eﬁni par un id´eal aH+ℓde AH+ℓ. D’apr`es 2.14, 2.15, cet id´eal est la r´ealisation
d’un id´eal a de A, et P H+ℓ
¯y,x
est isomorphe `a la r´ealisation de Spec(A/a).
4.8 Fin du cas 1 de la preuve de 4.4. Soit b ∈S distinct de ¯y, et X′ := P −{¯y, b}.
Identiﬁons P et P1, par un isomorphisme envoyant ¯y sur 0 et b sur ∞, donc X′ sur A∗=
Spec k[u, u−1]. Soit t := du (y) la coordonn´ee du vecteur tangent y en u = 0, et notons
encore t le point de Gm de coordonn´ee t. Les espaces de chemins P H+ℓ
y,x (X′) et P H+ℓ
t,x
(Gm)
44
sont canoniquement isomorphes (Deligne (1989) §14). Puisque t et x sont des points-base
`a distance ﬁnie de Gm, P H+ℓ
y,x
est motivique. C’est d’ailleurs simplement un torseur de
Kummer: on a πmot
1
(Gm, x) = Q(1), t/x ∈k∗d´eﬁnit une extension de Q(0) par Q(1), donc
un Q(1)-torseur, et P H+ℓ
y,x
est la r´ealisation de ce torseur.
Lemme 4.9. Le morphisme
P H+ℓ
y,x (X) →P H+ℓ
y,x (X′) × P H+ℓ
¯y,x (X)
(1en facteur: fonctorialit´e en X; 2e facteur: passage ou quotient) est un isomorphisme.
Puisque tant P H+ℓ
y,x (X′) que P H+ℓ
¯y,x (X) sont motiviques 4.9 implique que P H+ℓ
y,x (X) est
motivique.
Preuve de 4.9. Il suﬃt de v´eriﬁer 4.9 en r´ealisation de de Rham. Avec les notations de 3.6,
l’assertion se r´eduit `a la suivante.
Lemme 4.10. Regardons Ga = exp(ke) comme un quotient de G par e 7→e, ea 7→0 pour
a̸ = ¯y, b. L’application
G →exp(ke) × exp(ke) \ G
est un isomorphisme.
Preuve. G est le produit semi-direct de exp(ke) par le noyau de la projection sur exp(ke),
cf. la preuve de 4.7.
4.11. Pour ﬁnir la preuve de 4.4 il reste, compte tenu de ce que P H+ℓ
y,x , est isomorphe
comme RH+ℓ-sch´ema `a P H+ℓ
x,y , `a traiter le
Cas 2. x et y sont des points base `a l’inﬁni.
Choisissons un point base z ∈X(k). On a une expression de P H+ℓ
y,x
comme compos´e
de bitorseurs
P H+ℓ
y,x
= P H+ℓ
y,z
×πH+ℓ
1
(X,z) P H+ℓ
z,x
o`u au second membre chaque RH+ℓ-sch´ema est motivique. Que P H+ℓ
y,x
soit motivique en
r´esulte.
45
4.12. Soit X une vari´et´e alg´ebrique lisse sur un corps de nombres k, et x, y ∈X(k). On
suppose X s´epar´e. Sous l’hypoth`ese que H1( ¯X, O) = 0 pour ¯X une compactiﬁcation lisse
de X, nous avons d´eﬁni dans Deligne (1989) §13 un “espace de chemins” Py,x qui est un
sch´ema en une cat´egorie de syst`emes de r´ealisations. Nous le noterons ici, apr`es omission
de l’aspect cristallin, P real
y,x . Comme pr´ec´edemment, les P real
y,x forment un groupo¨ıde.
Th´eor`eme 4.13. Si la vari´et´e X est unirationnelle, P real
y,x est motivique, r´ealisation d’un
MAT(k)-sch´ema.
Les cat´egories de syst`emes de r´ealisations consid´er´es sont des champs sur Spec(k)et. Le
th´eor`eme ´equivaut donc `a dire qu’il existe une extension galoisienne k1 de k telle qu’apr`es
extension du corps de base `a k′ dans C(k1/k), P real
y,x (Xk′) est motivique, r´ealisation d’un
MT(k′)-sch´emas.
Preuve pour X un ouvert de Pn. Soit D ⊂Pn une droite, assez g´en´erale pour que le
morphisme de sch´emas en groupe unipotents
πreal
1
(X ∩D, x) →πreal
1
(X, x)
(x quelconque dans X ∩D) soit surjectif.
Si X ∩D est le compl´ement dans D d’un ensemble ﬁni de points rationnels,
πreal
1
(X ∩D, x) est dans RH+ℓet, d’apr`es 4.4, motivique, r´ealisation de πmot
1
(X ∩D, x)
dans MT(k). L’alg`ebre aﬃne de πreal
1
(X, x) est une sous-alg`ebre de celle de πreal
1
(X ∩D, x),
donc est ´egalement motivique, dans MT(k). En g´en´eral, pour k′ assez grand (i.e., dans
un C(k1/k) convenable), X ∩D deviendra apr`es extension du corps de base de k `a k′ le
compl´ement d’un ensemble de points rationnels sur k′, et la construction ci-dessus nous
fournit πmot
1
(Xk′, x) dans MT(k′), fonctoriel en k′, i.e. πmot
1
(X, x) dans MAT(k).
Soit y ∈X(k), distinct de x. Prouvons que P real
y,x est motivique. Soit D la droite de
Pn passant par x et y. Comme pr´ec´edemment, on se ram`ene `a supposer que X ∩D est le
compl´ement, dans D, d’un ensemble ﬁni de points rationnels. Le RH+ℓ-sch´ema P real
y,x (X ∩D)
est alors la r´ealisation de P mot
y,x (X ∩D) dans MT(k). On obtient P mot
y,x (X) en poussant le
46
π1(D ∩X, x)-torseur P mot
y,x (D ∩X) par
π1(D ∩X, x) →π1(X, x).
Pour y, z ∈X(k), P mot
y,z
est d´eduit des πmot
1
(X, x)-torseurs P mot
y,x et P mot
z,x .
Preuve de 4.13 (cas g´en´eral). La vari´et´e X, ´etant unirationelle, est domin´ee par un ou-
vert U de Pn. Fixons x ∈U(k). Pour σ un plongement complexe de k, le morphisme
π1(U(C), x) →π1(X(C), x) a une image d’indice ﬁni. Le morphisme induit sur les en-
veloppes alg´ebriques unipotentes est donc surjectif, et l’alg`ebre aﬃne de πreal
1
(X, x) est
motivique en tout que sous-alg`ebre de l’alg`ebre aﬃne de πreal
1
(X, x), que nous savons d´ej`a
ˆetre motivique. Le cas des Py,x se traite ensuite comme plus haut, en utilisant que deux
points de X peuvent ˆetre connect´es par une chaˆıne de courbes rationnelles.
Remarque 4.14. Utilisant 4.4, on pourrait aussi dans 4.13 prendre pour x et y des
points-base `a l’inﬁni, au sens de Deligne (1989) §15.
Proposition 4.15. Supposons que ¯X soit une compactiﬁcation normale de la vari´et´e uni-
rationelle X, et soient x, y ∈X. Si les composantes irr´eductibles de codimension un dans
X de Y := ¯X −X sont absolument irr´eductibles, alors P mot
y,x est un MT(k)-sch´ema.
Preuve. Supposons d’abord que x = y. Pour que π1(X, x) soit un MT(k)-sch´ema il suﬃt
que Lie π1(X, x) soit dans MT(k). D’apr`es 2.18, il suﬃt mˆeme que son gradu´e par le poids
le soit. Ce gradu´e ´etant engendr´e par H1(X), purement de poids −2, il suﬃt que l’action
de Gal(¯k/k) sur ωH1(X) soit triviale. Ce groupe est
O∗(X¯k)/¯k∗⊗Q
et ses ´el´ements sont d´etermin´es par leurs valuations le long des composantes irr´eductibles
de codimension un de Y¯k. Si le groupe Gal(¯k/k) ne les permute pas, il agit donc trivialement
sur O∗(X¯k)/¯k∗⊗Q.
Le cas g´en´eral r´esulte du
47
Lemme 4.16. Si un MAT(k)-sch´ema P est un torseur sous un MT(k)-sch´ema en groupes
unipotent G, il est lui-mˆeme un MT(k)-sch´ema.
Preuve. Le groupe G ´etant unipotent, si on le fait agir sur son alg`ebre aﬃne A par trans-
lations `a droite, celle-ci admet une ﬁltrations exhaustive Fil par des sous-motifs stables
sous G, et tels que G agisse trivialement sur le gradu´e associ´e. L’alg`ebre aﬃne AP de P,
d´eduite de A en poussant par le G-torseur P, admet donc une ﬁltration, encore not´ee Fil,
telle que GrFil(A)
∼
−→GrFil(AP). Il reste `a appliquer 2.18.
Proposition 4.17. Soit S un ensemble ﬁni de places ﬁnies de k et supposons que la
vari´et´e unirationelle X est la ﬁbre g´en´erale du compl´ement XO, dans ¯XO propre et lisse
sur Spec(OS), d’un diviseur `a croisements normaux relatif, r´eunion de diviseurs lisses,
chacun de ﬁbre g´en´erale absolument irr´eductible. Si x et y dans X(k) proviennent de xO,
yO dans XO(OS), alors P mot
y,x est dans MT(OS).
Preuve. Pour tout nombre premier ℓ, l’hypoth`ese assure que la r´ealisation ℓ-adique de
P mot
y,x est non ramiﬁ´ee en dehors de S et des places au-dessus de ℓ, et on applique 1.5.
4.18 Remarque. Un ´enonc´e analogue vaut pour x ou y `a l’inﬁni.
4.19. Soit X une vari´et´e lisse unirationnelle sur un corps de nombres k. Le th´eor`eme 4.13
permet de d´eﬁni la cat´egorie MAT(X/k) des syst`emes locaux unipotents de motifs d’Artin-
Tate mixtes sur X. On choisit x ∈X(k) et on d´eﬁnit un objet M de MAT(X/k) comme
´etant la donn´ee de Mx dans MAT(k) muni d’une action de π1(X, x). Il y a lieu de voir Mx
comme ´etant la ﬁbre de M en x. Le choix de x n’importe pas: pour y dans X(k), on d´eﬁnit
My comme ´etant le tordu de Mx par le π1(X, x)-torseur Py,x. Il reviendrait au mˆeme de
d´eﬁnir MAT(X/k) comme la cat´egorie des repr´esentations, dans MAT(k), du groupo¨ıde
des Py,x pour x, y ∈X(k). On pourrait aussi prendre des points base `a l’inﬁni.
Puisque Lie π1(X, x) est en poids < 0, π1(X, x) agit trivialement sur GrW (Mx) et, pour
x et y deux points base de X, GrW (Mx) et GrW (My) sont canoniquement isomorphes.
Le foncteur ﬁbre ω(M) := ω(Mx) est donc ind´ependant de x. On d´eﬁnit la sous-cat´egorie
MT(X) de MAT(X/k) par la condition “Mx est dans MT(k)”. Le choix de x n’importe
pas (2.18).
48
4.20. Soit σ un plongement de k dans une clˆoture alg´ebrique C de R. Pour M dans
MAT(X/k), (Mx)σ est une structure de Hodge-Tate mixte, munie d’une action de Hodge
mixte de π1(X, x)σ. D’apr`es Hain and Zucker (1987) (5.21), ces donn´ees d´eﬁnissent une
variation admissible Mσ de structures de Hodge mixtes sur X(C).
Le torseur (Py,x)σ tord (Mσ)x en (Mσ)y et la variation Mσ ne d´epend donc pas du
choix de x.
De mˆeme, M d´eﬁnit un Qℓ-faisceaux lisse sur X.
4.21. R´eciproquement, supposons donn´e sur X un syst`eme de r´ealisations M, candidat `a
ˆetre la r´ealisation d’un syst`eme local unipotent de motifs de Tate mixtes, de gradu´e par
le poids constant. Alors, si en un point x de X ce syst`eme est motivique, il est lui-mˆeme
motivique. En eﬀet, dans les diverses r´ealisations, il d´eﬁnit une repr´esentation de π1(X, x).
Appliquant 2.14, on obtient une repr´esentation de πmot
1
(X, x) sur le motif de r´ealisation
Mx, et cette repr´esentation d´eﬁnit le syst`eme local voulu.
4.22. Si K est le corps des fonctions rationnelles sur X, il est raisonnable de d´eﬁni MT(K)
comme la limite inductive des cat´egorie MT(U), pour U un ouvert non vide de plus en plus
petit de X. La relation entre cette cat´egorie et la cat´egorie d´eriv´ee motivique DM(K) de
Voevodsky n’est pas claire. Faute de disposer de la conjecture d’annulation de Beilinson-
Soul´e pour K, on ne sait pas extraire de DM(K) une cat´egorie ab´elienne de motifs de
Tate mixtes sur K. Pour X rationnelle de dimension un, la conjecture d’annulation est
vraie, mais nous n’avons pas prouv´e l’´equivalence des deux constructions. Pour la cat´egorie
MT(K) d´eﬁnie ici, on a
Ext1(Q(0), Q(1)) = K∗⊗Q
et
Ext1(Q(0), Q(n)) = K2n−1(k)
pour n ≥2.
4.23 Remarque. Soit ¯Q une clˆoture alg´ebrique de Q et d´eﬁnissons MT(¯Q) comme la
limite inductive des MT(F), pour F une extension ﬁnie de Q dans ¯Q. Goncharov (1994)
conjecture que, dans cette limite, les Py,x(P1−S) engendrent tous les motifs de Tate mixte.
En d’autres termes: que tout motif de Tate mixte sur ¯Q est un sous-quotient d’un produit
tensoriel de sous-motifs d’alg`ebres aﬃnes O(Py,x(P1 −S)) et de duaux de tels sous-motifs.
49
Les remarques suivantes montrent qu’il est en tout cas diﬃcile de sortir de la sous-
cat´egorie tannakienne T de MT(¯Q) engendr´ee par les Py,x(P1 −S).
(a) Pour X lisse unirationnelle, les Py,x(X) sont dans T. Cela r´esulte de la preuve de 4.13.
(b) Si M est un syst`eme local unipotent de motifs de Tate mixte sur X lisse unirationnelle,
et si en un point M est dans T, alors M est en chaque point dans T. En eﬀet, My est tordu
de Mx par Py,x. Il se plonge donc dans Mx ⊗O(Py,x), et est dans T puisque Mx et O(Py,x)
le sont.
50
