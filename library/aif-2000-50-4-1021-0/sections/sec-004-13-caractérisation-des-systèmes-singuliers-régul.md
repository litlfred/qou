---
doc_id: aif-2000-50-4-1021-0
doc_title: ""
section_id: sec-004-13-caractérisation-des-systèmes-singuliers-régul
section_title: "Caractérisation des systèmes singuliers réguliers par la"
section_number: 1.3
pages: 18-33
source_pdf: AIF_2000__50_4_1021_0.pdf
source_sha256: a7ca398590a266d8
doc_brief: "ANNALES DE L ’ INSTITUT FOURIER JACQUES SAULOY Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie — 7 sections: Cas d'une matrice unipotente. — So; No"
---
forme des solutions.
Il s'agit plus ou moins d'une réciproque aux résultats de 1.1.
1.3.1. Un algorithme de réduction.
Appelons uniformisante un élément u e M.(C) dont 0 est zéro simple,
autrement dit dont la valuation voÇu) en 0 vaut 1. Nous établirons d'abord
un lemme très utile. Il s'agit en fait d'un algorithme de réduction analogue
à l'algorithme du pivot de Gauss, valable dans tout anneau de valuation
discrète.
LEMME. — Toute matrice M e GLn(M(C)) peut s'écrire sous la
forme M = CR^ avec des matrices (7, R ç GL^A^C)) telles que :
(i) R est régulière en 0 (i.e. R(0) e GLn(C)) ;
(ii) C est produit :
1) d'une puissance u^, —k e N d'une uniformisante u arbitraire'^
2) de matrices Ti^a d'opérations élémentaires sur les lignes',
3) de matrices de dilatation P^, où les uniformisantes v sont
arbitraires (et choisies indépendamment les unes des autres).
Pour être précis, les matrices mentionnées sont définies comme suit.
La matrice T^a (a ç C77', 0.1 -^ 0) est égale à l'identité, sauf en ce qui
TOME 50 (2000), FASCICULE 4
1038 JACQUES SAULOY
concerne la ligne de rang i :
T.
/ 1
0
ai
V o
0
1
<^2
0
... 0
... 0
... Oi
... 0
... 0 \
... 0
... an
... 1 1
L'inverse d'une telle matrice est une matrice de même forme. La matrice de
dilatation D^y est diagonale et est égale à l'identité, sauf en ce qui concerne
le coefficient de rang i :
D
1
0
0
0
0
1
0
0
... 0
... 0
V
... 0
... 0 \
... 0
... 0
... 1 1
Le lemme dit alors que l'on peut écrire :
C=ukT^D^^^T^D^
où u, z»i,..., v^ sont des uniformisantes arbitrairement choisies.
On commence par multiplier M par une puissance v^ d'uniformisante,
de manière à la rendre holomorphe en 0 : cela revient à se ramener à ce cas,
et l'on doit alors prouver le lemme avec k = 0 dans la conclusion. Puis l'on
fait une récurrence sur î;o(det M). Si cette valuation vaut 0, M est régulière
en 0 et l'on prend R = M et C = 1^ (produit vide).
Si î;o(det M) > 0, la matrice M(0) est singulière et il existe donc
(3 e C71 - {0} tel que /3M(0) = 0 e C71.
Soit i un indice tel que ^ ^ 0 et soit v une uniformisante quelconque. Alors
M! = ^J^,^ es^ holomorphe en 0 et detMi = (A/^)detM; Mi est
meilleure que M : vo(det Mi) = vo(det M) - 1, ce qui achève la récurrence.
Les Ti^ de l'énoncé sont alors les T^ (qui sont bien de cette forme !). D
COROLLAIRE 1. — Dans le lemme, on peut obtenir C e GLn(C(z)) et
de plus régulière en oo, Le. G(oo) e GL^(C).
Il suffit pour cela de prendre chaque ^ égal à z/(l 4- z). n
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1039
COROLLAIRE 2 («double réduction))). — Soient C'.C" € GLn(C(z)).
Il existe alors U e GLn(C(z)) telle que UC' est régulière en 0 et VC11 est
régulière en oo.
On applique ce qui précède à M == (C'^^C' que l'on écrit donc sous
la forme CR avec C, R ç. GLn(C(^)), C régulière en oo et R régulière en 0.
On prend alors U == C-1^")-1 : UC' == R est régulière en 0, UC11 = C-1
est régulière en oo et, bien sur, U 6 GLn(C(z)). D
Outre ce qui suit, ce lemme et ses corollaires nous serviront au
paragraphe 2 pour caractériser globalement les systèmes singuliers réguliers.
1.3.2. Caractérisation des systèmes singuliers réguliers.
THÉORÈME. — Si 2e système aux q-différences à coefficients rationnels
(TqX == AX admet une solution fondamentale de la forme MN, où M est
méromorphe sur C et où N est une matrice log-car, alors c'est un système
singulier régulier en 0.
Appliquons le corollaire 1 du lemme de 1.3.1 à M, que l'on écrit
donc M == CR. Alors Y = RN est solution du système OqY -=- BY,
avec B == (o•qC)~lAC. La matrice B est rationnellement équivalente à A,
puisque C e GLn(C(z)). Mais
B = ((Tq(RN))(RN)~1 = OqR^NN-^R-1
est le produit de trois matrices régulières en 0, donc l'est elle-même; le
système correspondant est donc fuchsien en 0. D
II serait intéressant d'obtenir une caractérisation par la croissance
des solutions. Le critère le plus probable semble celui-ci : croissance et
décroissance modérées le long de toute demi-spirale logarithmique dis-
crète q^zo.
2. Matrice de connexion et classification.
Le changement de coordonnées w == 1/z permet d'appliquer ces
considérations au cas où le système (1) est singulier régulier sur S,
c'est-à-dire singulier régulier en 0 et en oo. Soient X^ == M^N^ et
X^ == M^N^ des solutions canoniques en forme normale : cette
dernière s'obtient par le changement de variable w == 1/z, donc comme
solution du système de matrice (A(l/gw))~1.
TOME 50 (2000), FASCICULE 4
1040 JACQUES SAULOY
2.1. Caractérisation globale des systèmes singuliers réguliers.
THÉORÈME. — Un système singulier régulier est rationnellement
équivalent à un système fuchsien en 0 et oo à la fois.
Soient X^ = M^N^ et X^ = M^N^ des solutions
canoniques en formes normales en 0 et en oo respectivement. Appliquant le
lemme, on écrit
MW = (7(0)^(0) ^ M^ = C^R^.
Il suffit maintenant de trouver U e GLn{C(z)) telle que UC^ et ^7(7(oc)
soient régulières en 0 et en oo respectivement : on pourra alors conclure
comme dans le théorème précédent. On applique pour cela le corollaire 2
du lemme de 1.3.1 avec C' = C^ et C" = C^°°\ D
2.2. Classification des systèmes singuliers réguliers sur §.
Sous les hypothèses de ce paragraphe, il est clair que la matrice de
connexion de Birkhoff
p = (X^)-1^
est à coefficients elliptiques, autrement dit
PçGLn(M(E)).
Comme indiqué dans l'introduction, on associe à un système
singulier régulier o-qX = AX, la matrice de connexion P assortie des
structures de Jordan en 0 et en oo, ou, de façon équivalente, le triple!
(A^°°\ P, N^). Celui-ci n'est cependant pas défini de manière univoque : P
peut être remplacé par (R^^PR^ si R^°\R^ ç GL^(C) commutent
respectivement avec N^ et N^. Ceci justifie l'introduction des notations
suivantes.
Sur l'ensemble des triplets (7Vi,P,A^), où P e GLn(.M(E)) et où
Ni, 7V2 sont des matrices log-car en forme normale, on définit une relation :
(^i.P,^)-^,?',^)
si et seulement si
Nï = N[, 7V2 = N^ R^P' = PR^
où Ri, R^ e GL^(C) et [Pi, M] = [R^N^} = 0.
C'est bien une relation d'équivalence, et l'on notera Tn l'ensemble
quotient.
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1041
L'image dans Jn du triplet (A^.P.TV^) est alors bien définie
d'après le paragraphe 1.2. On va maintenant prouver le
THÉORÈME. — On obtient ainsi une bijection de l'ensemble En <^s
classes d'équivalence rationnelle de systèmes singuliers réguliers de rang n
dans l'ensemble J^n-
On pourrait rapprocher ce codage de l'esprit de Birkhoff en lui
donnant une allure un peu plus algébrico-combinatoire. Birkhoff pose en
effet le problème «inverse» à partir de la donnée de P et de celle des
exposants en 0 et en oo : n'étudiant que le cas générique semi-simple,
cela lui tient lieu de structure de Jordan. Dans notre cas, la donnée de
N^ (resp. de 7V(°°)) équivaut à celle de K^ (resp. de K^), qui est à
son tour déterminée par la donnée des exposants et des tailles des blocs
correspondants.
Si B = {aqU)~lAU et si les solutions fondamentales choisies pour A
sont M^N^ et A^00)^00), on peut choisir pour B les solutions
(UM^N^ et (UM^^N^, ce qui associe à B les mêmes parties
log-car et la même matrice de connexion, donc le même triplet codant
qu'à A. Ainsi, on a une application bien définie de En dans Fn'
Réciproquement, supposons que A et B ont fourni des triplets équi-
valents. Quitte à modifier le choix des solutions pour l'un de ces deux
systèmes, on peut alors supposer que l'on a associé à A et B le même
triplet (Tv^.P.A^). Ainsi, on a des solutions fondamentales M^N^
et M^N^ pour A, et M^N^ et M^N^ pour B. De plus,
(M^)-1^0^^^)'1^
car ces deux matrices sont égales à N^PÇN^)'1. On a donc
M^ÇM^'^M^ÇM^Y1.
Notant U cette matrice, on voit qu'elle est inversible et méromorphe à la fois
sur C et sur § — {0}, donc rationnelle : et il est clair que B == {aqU)~lAU,
autrement dit, on a équivalence rationnelle. Ceci prouve l'injectivité.
Notons qu'en omettant les parties log-car dans le codage, on n'aurait
plus l'injectivité. Par exemple, en dimension l,A=letB=cGC*— q^
ne sont pas équivalentes, mais on peut à toutes deux associer la matrice de
connexion P = 1.
TOME 50 (2000), FASCICULE 4
1042 JACQUES SAULOY
Reste à établir le seul point non trivial, la surjectivité. On part d'un
triplet (TV^),?,^0)) (P elliptique, N^ et N^ des matrices log-car)
et l'on écrit P = {N^^MN^ où M € GL^(A-f(C*)). On invoque
alors la «trivialité des fibres méromorphes sur §» (voir [19], p. 158, ainsi
que 2.3.1 ci-dessous) : cela entraîne que M s'écrit (M^^M^, où
MW ç GLn(M(C)) et M^ e GLn(M(S - {0})).
Les matrices X^ = M^N^ et X^ = M^N^ sont connectées
par la matrice elliptique P : X^°°^ = PX^°\ et sont donc solutions du même
système OqX == AX, en prenant pour A la matrice
aqX^\X^)-1 =a^°°\X^)-\
La première écriture implique que A = OçM^X^^M^)"1, où l'on
a encore posé K^ = (aqN^)(N^)~1 € GLn(C), ce qui montre que A est
méromorphe sur C. Le raisonnement analogue à l'infini montre que A est
méromorphe sur § — {0} et l'on conclut que A € GLn(C(z)).
Le système aux ç-différences linéaire à coefficients rationnels o~qX =
AX admettant les deux solutions en formes normales X^ == M^N^ et
Xe00 ) = M^W^, il résulte de 1.3.2 qu'il est singulier régulier et ceci
achève la preuve du théorème. D
2.3. Précisions diverses.
2.3.1. Polarité.
Le théorème 2.1 affirme que notre système est rationnellement
équivalent à un système fuchsien en 0 et oo; cela revient à dire que
l'on peut obtenir M^ et M^ respectivement régulières en 0 et en oo.
En vue des applications à la théorie de Galois (voir [24], [25]), il
est utile de pouvoir préciser la position des singularités. Celles de N^ et
de N^ sont totalement déterminées par la structure de Jordan de A(0)
et de A(oo). En ce qui concerne M, on déduit facilement ce qui suit de
la preuve du théorème. Soit une partie finie S C C* ; pour simplifier la
formulation, nous supposerons que deux éléments distincts de E ne sont
pas congrus modulo ç^
• Sens direct : partant d'un système (1) tel que S(A) C S, on voit
que les singularités de M appartiennent à ^E.
• Sens inverse : supposons que les singularités de M appartiennent à
^E. L'invocation du «Preliminary Theorem» de [6] (lemme de Birkhoff;
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1043
voir ci-dessous) à la place de l'argument de trivialité des fibres méromorphes
permet de choisir les singularités de M^ et M^ respectivement dans
ç^S et dans ç^S ; le système (1) correspondant est alors tel que S'(A) C S
(voir également [3]).
Sous la forme simplifiée utilisée p. 566-567 de loc. cit. (un seul contour,
une seule matrice; la forme complète se trouve p. 533), voici l'énoncé du
« Preliminary Theorem » ^.
Soit C une courbe analytique fermée simple de C qui entoure 0 et
soit M(z) une matrice holomorphe inversible dans un voisinage de C.
Soient DQ et Doo les composantes connexes de §> — C contenant respec-
tivement 0 et oo. Il existe alors un voisinage ouvert VQ de DQ, un voisinage
ouvert Voo de Doo et des matrices M^^M^ holomorphes inversibles
respectivement sur VQ et sur V^o — {oo}, Voo étant de plus holomorphe
(mais pas nécessairement inversible) en oo, telles que, sur VQ D Voo :
M^ = M^M.
Pour appliquer ce théorème, nous choisissons une courbe C qui passe
entre z et qz pour chaque z € E.
2.3.2. Interprétation catégorique.
La normalisation un peu artificielle de la forme des matrices log-car
a pour but d'obtenir un énoncé pas trop compliqué. Si on relaxe cette
condition, la relation d'équivalence qui sert à définir F^ se traduit, pour les
parties log-car, par les conditions R\N\ = N[R^ et R^N^ = N^R^.
Les couples (R-^.R^) correspondent, dans la version catégorique du
théorème d'équivalence (voir [24], [25]) à des isomorphismes. Ce théorème
est donc le premier indice de la possibilité d'obtenir par cette voie (c'est-à-
dire, en travaillant avec de «vraies fonctions ») un groupe de Galois qui soit
un groupe algébrique sur C, question qui est restée longtemps pendante.
3. Comportement des solutions lorsque q —^ 1.
Nous supposons maintenant donnés 7-0 tel que Im(ïo) > 0 et
qo = e"2271^0. Nous posons q = çg, c'est-à-dire r = 7-oe, e étant un réel
strictement positif que l'on va faire tendre vers 0. Les spirales et demi-
spirales logarithmiques discrètes ^z, q^ se condensent alors en des coupures
spirales ç^, q^ de S.
(3) Nous notons ici M,M<°),M(00) les matrices A,£/o,î7oo de Birkhoff.
TOME 50 (2000), FASCICULE 4
1044 JACQUES SAULOY
Afin d'alléger les notations, toutes les dépendances en e ne seront pas
dénotées explicitement.
3.1. Estimation asymptotique de e<^c et de tq.
PROPOSITION.
(i) lim^o+(ç - 1)W = log(-^).
(ii) Si (c - 1)/(<7 - 1) -^ 7, alors lim^o+ <°g,c(^) = (-^)7-
II s'agit des déterminations principales sur l'ouvert simplement
connexe ^ = S - q^ = C* - q^ (resp. -1 i-^ 0, -1 »-^ 1).
Pour prouver cette proposition, on introduit la fonction
ë(r,;r)=9,(e2—),
qui vérifie l'équation fonctionnelle (voir [15], [17])
©(^) = ^^^i^ ©( - ^ ^)-
Soit a G C; on cherche un équivalent de Qq(qoiz) = 6(r,.r — ra)
lorsque e = T/TO ^ O^ L'équation fonctionnelle se réécrit
Q(r,x-ra) = . , ., v i, .n^Qf- -'-^ +û-).v 7 ç(î7r/T)(a;-ra-^(r+l))2 \ T T /
Le « facteur d'automorphie » vaut
/^^-Çi^/r){x- \ )2 ç2t7r(a+ ^ )(o:- \ )(l+0(r))
avec un 0(r) uniforme en x ç C.
Si l'on écrit x = u + iv (qui n'est déterminé qu'à un entier près) et
7-0 = ri + îï2, il est loisible de supposer que u — vr-t/r^ appartient à [0 ; 1[ :
supposons que ce n'est pas 0. Cela revient simplement à supposer que l'on
a pris z e fl. et 2i7r(x - | ) = log(-^).
La série qui définit le facteur Q(-l/r, -x/r 4- a) ne comprend alors,
hors le terme constant 1, que des termes de la forme
ç2z7rm(a+ è ) . e- ^ (m2+2m(a;- è )) ^ ç Z - {Q}
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1045
et ceux-ci convergent normalement vers 0 lorsque e —> 0"1", en vertu de
l'égalité
K.(-^^4))) ,-^(,^,,.(,.4-^))
et de majorations aisées. On en déduit les estimations suivantes :
1) Pour z ç. f2 et a ç. C, on a, lorsque e —> O"1" :
QqÇq^z) ~ ./ie-^7^^-^2-^2^0'4-^^"^.
2) Si de plus /3 e C :
lim ^S= (-^6-.0+ 9g (q^z)
Cette dernière notation désigne bien sûr e^0'"^10^""^.
Ces conclusions demeurent si l'on perturbe les hypothèses au premier
ordre :
1) Si ZQ ç ^ et, si, pour j = 1,2, ^ = zo(l — 2î7rroû^e -j- o(e)), alors
lim e^^/e,^!)^^)"2-"1.e—>-0+
2) Si c = 1 — 2i7rroae + o(e) et si z = 2:0 + o(e), alors
\ïm e^{z)=(-z)a.€—)•()+
L'assertion (ii) de la proposition découle du deuxième point ci-dessus,
qui découle du premier, lequel est conséquence du
TQ)
LEMME. — On suppose que z\ et z^ tendent vers ZQ e f^o = § — QQ^ =
C — (^ O12 suppose de plus que zcl|z\ =14- o(e). Alors
lim ^2'PJOC = 1 (cf. (0.1) pour cette notation).e^0+ (Zi ;p)cx)
Soit en effet Uq = z^ — z^ : c'est un o(e). On part de l'égalité :
(^2;P)oo ^ TT /. Ç'^g \
(^;P)oo nv ^-^-^l^
TOME 50 (2000), FASCICULE 4
1046 JACQUES SAULOY
o
II existe un disque ouvert D(zo^p) sur lequel, quel que soit À >: 0,
|1 — z/q^\ > 6 > 0. Pour q proche de 1, z\ et z^, sont dans ce disque et
(^2;P)oo 1 ^ ^ 1 q^Uq 1 ^ Kl M, (^2;P)oo . Y-^l
^T^- <E|î(^;p)ool-^ll-ç-^il- 6 \q\-l
Ce dernier majorant est un 0{uq/(q — 1)) uniformément en q. Comme
Uq = 0(6) et q — 1 ~ —2î7TTo€, cette estimation est suffisante pour achever
la preuve du lemme.
Pour démontrer l'assertion (i) de la proposition, on introduit
J (r\-P (.}- 1  ^^^w-w- ^ -^
Dérivant logarithmiquement l'équation fonctionnelle déjà invoquée, on
trouve que
x\ 1
7)^-21
Lorsque e —>• O"^, (q — l)£q(z) est équivalent à —2i7rrLr(x). On choisit
x ç. ]0 ; 1[ 4- RT-O (x n'est déterminé qu'à un entier près et z ç. Ci). Le même
argument de convergence normale que précédemment, appliqué à la série
qui définit L^/^—x/r) :
-rL^x)=L_^(- ^)+.r- ^(r+1).
2î7r x~r 2î7T ~x~r
x\ _ Y^ e-6" T- ^ ç,T ( ^_v-_e_^__ v^ e— T
L-1/TV ~ ~r} ~ ^ i ^^ ~ 2. , _ ^^r~T ) ~ ^ 1^x^r- ~ ^ 1p2î7r -T-^1 i — e ^ y>n i — er>l -L — ^ ' r>0
(dérivée logarithmique de la formule du triple produit de Jacobi), permet
de montrer que ce terme tend vers 0 ; la conclusion est alors immédiate. D
On peut ajouter une interprétation géométrique. Le lieu polaire de
e^c est la spirale discrète c^, c'est-à-dire l'image par x i—> e2^^x du réseau
translaté (Z + Zr) + 7(ç)e (ici, c = ç7^ et 7(9) —^ 7). Lorsque e —^ O4',
celui-ci se condense en le sous-groupe fermé Z + MTQ de C, dont l'image
dans C* est la spirale logarithmique continue q^ : la barrière de pôles
(discrète) se transforme en coupure. Du point de vue numérique, Oq a un
comportement «chaotique» le long de la barrière des pôles (dans le plan
des x : le réseau Z + Zr), lorsque celle-ci se condense en une coupure spirale
(dans le plan des x : le sous-groupe fermé non discret Z 4- IKïo). Il est
raisonnable de conjecturer que toutes les conclusions de cette section et de
la suivante demeurent valides si l'on impose simplement à q de tendre vers 1
en respectant cette géométrie, c'est-à-dire tangentiellement à une spirale
logarithmique.
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1047
3.2. Comportement des solutions canoniques.
Supposons maintenant le système différentiel (2) (défini au § 0.3)
fuchsien sur § et non résonnant en 0 (deux valeurs propres de B(0) ne
peuvent différer d'un entier non nul). On notera X^ la solution canonique
de (2) obtenue en appliquant la méthode de Frobenius en 0, avec, pour
fonctions de base, (-2:)7 comme solution^ de 6f = ^f et logÇ—z) comme
solution de 6f = 1 (mêmes déterminations que ci-dessus). Notons enfin
i?i,..., Zr les pôles de B (ils sont simples et dans C*).
Nous allons déployer (2) en une famille de systèmes aux g-diffé-
rences (1) soumis aux contraintes suivantes :
1) A = Aç = J^ + (ç — l)Bç, où Bç converge vers B uniformément
sur tout compact de l'ouvert simplement connexe f^o = C — Ui<7<r ^9? 5
cette hypothèse peut d'ailleurs être affaiblie (voir [23], [24])).
2) Une trigonalisation J = Q~1B(0)Q se déploie en une trigonalisation
J, = Q^B,(Q)Q,, où lim,_o+ Qe = Q'
Cette dernière condition n'est pas automatiquement vérifiée, comme
le montre l'exemple suivant :
5 —/^ ^\ D _ ( cos2 e~1 —sine"1 cos e~1 \
B=\0 07' ^^-sinc^cose-1 sm2 e-\ )'
On voit ici que liniç_^o+ Bç = B. Mais B^/e est la matrice de la
projection orthogonale sur le vecteur de coordonnées (cosl/e,—sinl/e).
Toute trigonalisation de Bç sera donc obtenue dans une base tournant
infiniment vite lorsque e •—>• O4', et l'on ne peut déployer aucune
trigonalisation de B en une trigonalisation de Be.
THÉORÈME. — Pour e proche de 0, le système (1) est non résonnant
en 0. Soit X'^ = M^eq^ço) lo- solution canonique donnée par le théorème
de 1.1. Alors, sur tout compact de QQ = ^o — ç^ X' est holomorphe
pour e assez petit et elle y tend vers X^.
Pour le prouver, on traite séparément la partie holomorphe Me et la
partie log-car eq^çoy
1) Pour étudier Mç, on la caractérise par les conditions :
(<r,M,)A,(0) = A,M,, M,(0) = In.
(4) Rappelons que 6 désigne l'opérateur différentiel zd/dz.
TOME 50 (2000), FASCICULES 4
1048 JACQUES SAULOY
De même, X^ = MÇ—z)3^, où M est caractérisé par les conditions :
6M = BM - MB(0), M(0) = In.
Ces équations matricielles peuvent être considérées comme des équa-
tions vectorielles dans Mn(C) avec condition initiale (en 0) indépendante
du paramètre e. C'est donc un cas particulier du théorème. Il est traité au
paragraphe 3.3.
2) Le comportement de Cç,Ae(o) résulte encore d'un cas particulier du
théorème, celui où le système (1) est à coefficients constants (dépendant
de e). Cela revient donc à supposer que, pour chaque valeur de g, B
appartient à Mn(C). On note
A = In + (q - 1)B
et l'on se propose de préciser le comportement de C^A lorsque e —> O4' et
que B —> B avec sa triangularisation. On reprend les notations précédentes.
Soit D + N la décomposition de Dunford additive de B. La
décomposition de Dunford multiplicative DU de A s'obtient en prenant
D = In + (q - 1)D^ U = In + (q - l)?-1^.
Alors la matrice diagonale A == SDS~1 et la matrice diagonale A = SDS~1
(qui est la partie diagonale de T) sont liées par la relation A == In-\-(c[— 1)A.
Soient D + N la décomposition de Dunford additive de B et
À = SDS~1 la partie diagonale de T. Donc (A - Jn)/(ç - 1) tend vers A.
Il est alors immédiat, d'après les résultats de 3.1, que êq^ tend vers (—^A
et donc Cq^ tend vers (—.z)^
Comme D~~1N tend vers 7V, il résulte pareillement de 3.1 que
U^ = (In + (ç - l)?"1^)^ tend vers (-z)1^ : cela revient en effet à
dire que (g - l)^ tend vers (logÇ-z^/kl.
On voit donc que e^A tend vers (—^z^^
Module le résultat de 3.3, ceci achève la preuve du théorème. D
3.3. Comportement des solutions à valeur initiale fixe.
On considère le système aux g-différences à coefficients rationnels
fuchsien en 0, « avec conditions initiales » :
(7qX = AX, X(0) = XQ.
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX Ç-DIFFÉRENCES SINGULIERS RÉGULIERS 1049
Ici, XQ est un vecteur fixé non nul de C71 et A est fonction de ç. On veut
faire confluer ce système vers le système différentiel à coefficients rationnels
avec conditions initiales
6X = BX, X(fi} = XQ.
Selon les conventions précédentes, q tend vers 1 le long d'une spirale
logarithmique, autrement dit, q = QQ et e —> O"1". Nous supposons que la
matrice B = (A — In)/(q — 1) tend, lorsque e —> O4', vers la matrice à
coefficients rationnels B e Mn(C(z)) et nous n'indiquons pas explicitement
les dépendances en q et en e.
Nous imposerons en outre les conditions suivantes :
1) Notons ^i,..., Zr les pôles de B. Ce sont donc des éléments de C*
(le système différentiel étant fuchsien). On suppose que «les pôles de A
tendent vers ceux de B», c'est-à-dire que, quel que soit z ^ {^i,..., Zr},
A est définie en z pour e assez petit. Ceci donne un sens à l'hypothèse
B->B.
2) Quel que soit ç, XQ est point fixe de A(0).
3) Le système différentiel 6X = BX est fuchsien sur S et non réson-
nant en 0, autrement dit Sp(B(0))n(N* +Sp(B(0))) = 0. On verra que cette
condition entraîne que, pour e assez petit, Sp(A(0)) H q^ Sp(A(0)) = 0 : A
est non résonnante en 0.
Sous des hypothèses précisées de convergence, nous prouverons alors
que l'unique solution X du système aux ç-différences tend vers l'unique
solution X du système différentiel. Nous procéderons en deux étapes :
• Etude locale : il s'agit de reprendre la résolution formelle et la preuve
de convergence «en famille», et, en parallèle, l'algorithme correspondant
pour le système différentiel.
• Etude globale : on sort d'un voisinage de 0 (dans lequel la conver-
gence a été établie) le long de demi-spirales q^ . Ceci nous ramène à un
problème de variable réelle (on pose z = zoq^) et équivaut à l'emploi de la
méthode d'Euler pour approcher les solutions d'une équation différentielle.
Nous notons dorénavant f^o l'ouvert simplement connexe
C- |J z^\
^<J<r
TOME 50 (2000), FASCICULE 4
1050 JACQUES SAULOY
3.3.1. Étude locale.
Il découle des hypothèses précédentes, que B est holomorphe en 0,
ainsi que B pour e assez petit : on écrit donc
B = Bo+Bi^+— et B=Bo+Bi^+—
(les Bi dépendent donc de q). On suppose en outre que la convergence de B^ 0 ^
vers B est normale dans un disque ouvert non vide D(0^ p) C f^o-
La résolution formelle des deux systèmes se mène en parallèle : leurs
solutions respectives sont
X = Xo + zX^ + • • • et X = Xo + zX^ + • • •,
où Xo = XQ est une donnée et où les autres termes se calculent par
récurrence :
Xm = {q^In - Ao)-\A^Xm-i + ... + A^Xo),
Xm = (min - Bo)-\B^Xm-i + ... + B^Xo).
Mais la première relation se réécrit :
Xm = ((ç" - !)/(<? - l)^n - Bo)~\B,Xm-i + • • • + ^mXo).
On voit donc par récurrence que, quel que soit m, Xm tend vers Xm sur Qo-
Par ailleurs, on peut borner uniformément
((r-l)/(ç-l)^-^o)~1 et (mIn-Bo)-1
pour e assez petit et m >, 1. La combinaison de l'hypothèse de convergence
normale et de la méthode des majorants permet alors de conclure :
PROPOSITION. — X converge uniformément vers X sur un disque0
ouvert non vide D{0, r) C f^o- D
3.3.2. Étude globale.
0
On va maintenant sortir du disque -D(0,r) le long de segments de
spirales de la forme %' qui ne rencontrent pas les pôles zi. On suppose
dorénavant que B converge vers B uniformément sur tout tel segment (c'est
par exemple le cas si la convergence est uniforme sur tout compact de ^o).
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 1051
Fixons un point z\ ç SÎQ où l'on veut démontrer que X —> X.
—\ °Pour un certain A > 0, et un certain a > 0, ZQ = q^ z\ € D(0,r) et
r— • i °q^°° ZQ C D(0,r) (c'en est un compact). On passe aux variables réelles
en posant z = q^Zo et Y^(t) = X(z), Y(t) = X(z). Notre but est donc de
démontrer que Y(,(\) —> Y (A).
On note Ce(t) = (q-l)/eB(z) et C(t) = -2mB(z). Ainsi, Ce
converge uniformément vers C sur [0 ; A].
On peut maintenant traduire le système différentiel Y1 (y) = C(t)Y(t)
et le système aux ^-différences YçÇt+e) = (In -\-eC e(t))Y^(t). Nous n'aurons
pas besoin des conditions initiales. La proposition ci-dessus implique
que Yç(t) converge vers Y(t) uniformément sur [0 ; a].
On invoquera maintenant la méthode d'Euler pour la résolution
approchée d'équations différentielles linéaires (vectorielles, d'ordre 1), dans
sa version multiplicative et à pas non constant. Faute d'une référence
exactement appropriée à nos besoins, nous invoquerons [18] (problème
d'analyse, III.5 et IV.l).
THÉORÈME. — Soit A e C( }a ; &[, Mn(C)) et soient to < ti dans }a ; b[.
On se donne^ pour p entier > 1, une subdivision
fo=^)<^)<...<4^<^)=^
de diamètre e? := maxo<i<p-i A^^ (012 note A^^ = s^\ — s' ). On
suppose que linip-^oo ^p = 0- AJors, la résolvante du système différentiel
^' = ^[^ est donnée par la formule :
UÇt^to) = ^{In + ^(^A^i) • • • {In + A^AS^).
Appliquons ce théorème pour calculer la résolvante U(\, u) du système
différentiel Y' = CY : nous aurons donc V(A) = U(\0)Y{0). On subdivise
[0 ; A] avec le pas ve puis 7V fois le pas e, où N = E( ^ ) et v = A/e — N. On
trouve :
U(\ 0) = lim (In + eC(\ - e)) • • • (in + eC(\ - Ne)) (in + ^G(O)).
Mais nous voulons utiliser C et non C. Nous remplacerons donc [18], III.6
par une version améliorée que l'on déduit du
TOME 50 (2000), FASCICULE 4
1052 JACQUES SAULOY
LEMME. — Soient Ai,..., Am, ^i,..., Em des éléments de Mn(C) et
notons A'i = Ai + fa,..., A^ = A^ + Em. Alors
||(J,+Ai)...(J,+A^)-(J,+A'i)...(J,+A^)||
m m
<(^||^|l)exp(^(||A,||+H^ID).
î=l i=l
COROLLAIRE. — Soient (Ap^) et (Bp^) deux familles de matrices
indexées par des couples d'entiers (p,i) tels que 1 ^ i < p. On
considère les suites de terme général Up = (In + Ap^) • • • (In + Ap^p) et
Vp = (In + Bp^) ' • • (In + -Bp^). Oïl suppose que, lorsque p —^ oo :
(i) Ja suite de terme général Ei<î<p 11^^11 est bornée',
(ii) Ja suite de terme général ^i<,<p ||Ap^ - Bp^\\ converge vers 0.
AJors limp-^ ||[7p - VpH = 0.
Nous utiliserons ce corollaire avec pour matrices Ap^ et Bp^ les valeurs
respectives de C et C aux points de la subdivision introduite plus haut.
La preuve du lemme est immédiate, ainsi que celles du corollaire et du fait
que les conditions de celui-ci sont remplies dans notre situation. On conclut
donc que Yç{\) —> V(A), ce qui achève la preuve. D
