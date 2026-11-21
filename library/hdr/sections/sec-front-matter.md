---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-16
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
toc_source: outline
doc_brief: "Hecke algebras, generalisations and representation theory — 31 sections: Front matter; Algebras of Finite Type; Blocks"
---
HAL Id: tel-01411063
https://hal.science/tel-01411063v1
Submitted on 6 Dec 2016
HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.
HAL Authorization
Hecke algebras, generalisations and representation theory
Maria Chlouveraki
To cite this version:
Maria Chlouveraki. Hecke algebras, generalisations and representation theory. Mathematics [math]. Uni-
versite de Versailles, 2016. ⟨tel-01411063⟩
UNIVERSIT´E DE VERSAILLES - SAINT-QUENTIN-EN-YVELINES
UNIVERSIT´E PARIS-SACLAY
M´emoire des travaux en vue de l’obtention d’une
HABILITATION `A DIRIGER DES RECHERCHES
Sp´ecialit´e : Math´ematiques
Pr´esent´ee par
MARIA CHLOUVERAKI
Alg`ebres de Hecke, g´en´eralisations
et th´eorie des repr´esentations
e
Hecke algebras, generalisations
and representation theory
Soutenue le 25 novembre 2016 devant le jury compos´e de
M. Martin ANDLER
UVSQ
M. C´edric BONNAF´E
Universit´e Montpellier 2
M. Tam´as HAUSEL
IST Austria
Mme. Soﬁa LAMBROPOULOU
NTUA Gr`ece
M. C´edric LECOUVEY
Universit´e de Tours
M. Jean MICHEL
Universit´e Paris 7
M. Vincent S´ECHERRE
UVSQ
Rapporteurs : M. C´edric Bonnaf´e, M. C´edric Lecouvey, M. Andrew Mathas
Introduction en Fran¸cais
Les alg`ebres de Iwahori–Hecke associ´ees aux groupes de Weyl apparaissent naturellement dans l’´etude
des groupes r´eductifs ﬁnis comme des alg`ebres d’endomorphismes de la repr´esentation de permuta-
tion par rapport `a un sous-groupe de Borel. Elles peuvent aussi ˆetre d´eﬁnies ind´ependamment comme
d´eformations des alg`ebres de groupe des groupes de Coxeter ﬁnis. L’objectif de ce m´emoire est d’´etudier
certains aspects de la th´eorie des repr´esentations des alg`ebres de Iwahori–Hecke et la fa¸con dont elles se
g´en´eralisent dans le cas des :
• alg`ebres de Hecke cyclotomiques, qui sont obtenues comme d´eformations des alg`ebres de groupe
des groupes de r´eﬂexions complexes,
• alg`ebres de Ariki–Koike, qui sont obtenues comme g´en´eralisations des alg`ebres de Iwahori–Hecke
de types A et B,
• alg`ebres de Yokonuma–Hecke, qui sont obtenues lors de l’´etude des groupes r´eductifs ﬁnis comme
des alg`ebres d’endomorphismes de la repr´esentation de permutation par rapport `a un sous-groupe
unipotent maximal.
Au cours de ce m´emoire, nous allons aussi ´etudier une autre famille d’alg`ebres associ´ees aux groupes
de r´eﬂexions complexes, les alg`ebres de Cherednik rationnelles, dont la th´eorie des repr´esentations a
beaucoup de liens avec la th´eorie des repr´esentations des alg`ebres de Hecke.
Les aspects de la th´eorie des repr´esentations de ces alg`ebres sur lesquelles nous allons nous concentrer
seront la param´etrisation et description des repr´esentations irr´eductibles dans les cas semisimple et non-
semisimple, les blocs, la structure d’alg`ebre sym´etrique et la d´etermination de la matrice de d´ecomposition
associ´ee `a une sp´ecialisation.
Les groupes de Coxeter ﬁnis sont des groupes ﬁnis de matrices r´eelles qui sont engendr´es par des
r´eﬂexions.
Ils incluent les groupes de Weyl, qui sont des objets fondamentaux pour la classiﬁca-
tion des alg`ebres de Lie simples sur C et des groupes alg´ebriques simples. Les alg`ebres de Iwahori–
Hecke associ´ees aux groupes de Weyl apparaissent naturellement comme des alg`ebres d’endomorphismes
des repr´esentations induites dans l’´etude des groupes r´eductifs ﬁnis. Elles peuvent aussi ˆetre d´eﬁnies
ind´ependamment comme d´eformations des alg`ebres de groupes des groupes de Coxeter ﬁnis, o`u la
d´eformation d´epend d’un param`etre q et une fonction de poids L. Pour q = 1, nous obtenons l’alg`ebre de
groupe. Pour un groupe de Coxeter ﬁni W, nous d´esignerons par Hq(W, L) l’alg`ebre de Iwahori–Hecke
associ´ee.
Lorsque q est une ind´etermin´ee, l’alg`ebre de Iwahori–Hecke Hq(W, L) est semisimple.
Suivant le
th´eor`eme de d´eformation de Tits, il existe une bijection entre l’ensemble des repr´esentations irr´eductibles
de Hq(W, L) et l’ensemble Irr(W) des repr´esentations irr´eductibles de W. Grˆace `a cette bijection, Lusztig
associe `a chaque repr´esentation irr´eductible de W un entier qui d´epend de L, en d´eﬁnissant ainsi la
fameuse fonction a. Ici nous d´eﬁnissons la fonction a en utilisant la structure d’alg`ebre sym´etrique et
les ´el´ements de Schur de Hq(W, L). La fonction a intervient dans la d´eﬁnition de Lusztig des familles de
caract`eres, une partition de Irr(W) qui joue un rˆole central dans l’organisation des familles de caract`eres
unipotents dans le cas des groupes r´eductifs ﬁnis.
La th´eorie de Kazhdan–Lusztig est une clef pour la compr´ehension de la th´eorie des repr´esentations de
l’alg`ebre de Iwahori–Hecke Hq(W, L). Il existe une base sp´eciale de Hq(W, L), appel´e la base de Kazhdan–
Lusztig, qui nous permet de d´eﬁnir des cellules de Kazhdan–Lusztig pour Hq(W, L), un certain ensemble
de classes d’´equivalence sur W. Les cellules de Kazhdan–Lusztig aident `a construire les repr´esentations
1
de Hq(W, L). Elles permettent aussi une deuxi`eme d´eﬁnition ´equivalente, plus combinatoire, des familles
de caract`eres de Lusztig.
Lorsque q se sp´ecialise en un nombre complexe η diﬀ´erent de z´ero, et plus sp´eciﬁquement en une racine
de l’unit´e, l’alg`ebre de Iwahori–Hecke sp´ecialis´ee Hη(W, L) n’est pas n´ecessairement semisimple et nous
n’avons plus une bijection entre ses repr´esentations irr´eductibles et Irr(W). Nous obtenons donc une
matrice de d´ecomposition qui d´ecrit comment les repr´esentations irr´eductibles de l’alg`ebre semisimple
se d´ecomposent apr`es la sp´ecialisation. Un ensemble basique canonique est un sous-ensemble de Irr(W)
en bijection avec les repr´esentations irr´eductibles de Hη(W, L) (et ainsi un ensemble qui param`etre les
colonnes de la matrice de d´ecomposition) avec de bonnes propri´et´es. Ces bonnes propri´et´es impliquent
que la matrice de d´ecomposition a une forme unitriangulaire inf´erieure alors que la fonction a croˆıt (au
sens large) le long des colonnes. Les ensembles basiques canoniques ont ´et´e d´eﬁnis par Geck et Rouquier
[GeRo], qui ont prouv´e leur existence dans quelques cas en utilisant la th´eorie de Kazhdan–Lusztig.
Grˆace `a un travail collectif, il est maintenant prouv´e que des ensembles basiques canoniques existent et
sont explicitement d´ecrits pour tous les groupes de Coxeter ﬁnis et tout choix de L (en caract´eristique
0).
Les groupes de Coxeter ﬁnis sont des cas particuliers de groupes de r´eﬂexions complexes, c’est-`a-dire
des groupes ﬁnis de matrices complexes engendr´es par des “pseudo-r´eﬂexions”.
La classiﬁcation des
groupes de r´eﬂexions complexes est due `a Shephard et Todd [ShTo] : si W est un groupe de r´eﬂexions
complexe (irr´eductible), alors soit W appartient `a la s´erie inﬁnie G(l, p, n) soit W est un des 34 groupes
exceptionnels G4, . . . , G37 (voir Th´eor`eme 3.1). D’importants d´eveloppements durant les deux derni`eres
d´ecennies ont sugg´er´e que les groupes de r´eﬂexions complexes jouent un rˆole crucial, mais seulement
partiellement compris, en th´eorie de repr´esentations, et pourraient mˆeme devenir aussi importants que
les groupes de Coxeter ﬁnis dans l’´etude d’autres structures math´ematiques. En eﬀet, ils se comportent
de fa¸con tellement analogue aux groupes de r´eﬂexions r´eels que Brou´e, Malle et Michel [BMM1] ont
conjectur´e qu’ils pourraient jouer le rˆole de groupes de Weyl pour des objets, toujours myst´erieux, qui
g´en´eralisent les groupes r´eductifs ﬁnis. Ces objets s’appellent “Spetses”.
Brou´e, Malle et Rouquier [BMR] ont d´eﬁni des alg`ebres de Hecke pour les groupes de r´eﬂexions
complexes comme d´eformations de leurs alg`ebres de groupe.
Dans le cas des groupes de r´eﬂexions
complexes de type G(l, 1, n), elle co¨ıncident avec les alg`ebres de Ariki–Koike, d´ej`a d´eﬁnies par Ariki
et Koike [ArKo] comme g´en´eralisations des alg`ebres de Iwahori–Hecke de types A et B. Une th´eorie
des cellules de Kazhdan–Lusztig g´en´eralis´ee pour ces alg`ebres, connues sous le nom d’alg`ebres de Hecke
cyclotomiques, permettrait de se diriger vers une d´eﬁnition des Spetses. Malheureusement, nous n’avons
pas de base de Kazhdan–Lusztig pour les groupes de r´eﬂexions complexes. N´eanmoins, nous pouvons
d´eﬁnir des familles de caract`eres en utilisant la d´eﬁnition de Rouquier : dans [Ro1], Rouquier a donn´e
une d´eﬁnition alternative pour les familles de caract`eres de Lusztig en prouvant que, dans le cas des
groupes de Weyl, elles co¨ıncident avec les blocs de l’alg`ebre de Iwahori–Hecke sur un certain anneau,
qui s’appelle l’anneau de Rouquier. Cette d´eﬁnition se g´en´eralise naturellement au cas des groupes de
r´eﬂexions complexes et leurs alg`ebres de Hecke cyclotomiques, en produisant les familles de Rouquier.
Ces familles sont maintenant d´etermin´ees pour toutes les alg`ebres de Hecke cyclotomiques de tous les
groupes de r´eﬂexions complexes, voir [Ch3, Ch4, Ch5]. Un rˆole-clef dans cette d´etermination est jou´e
par la structure d’alg`ebre sym´etrique (toujours conjectur´ee dans certains cas) des alg`ebres de Hecke
cyclotomiques et les ´el´ements de Schur correspondants.
En utilisant les ´el´ements de Schur, nous pouvons aussi d´eﬁnir une fonction a et des ensembles basiques
canoniques pour les alg`ebres de Hecke cyclotomiques. Mˆeme s’il n’existe pas de th´eorie de Kazhdan–
Lusztig dans le cas complexe, il est maintenant prouv´e que des ensembles basiques existent pour les
groupes de la s´erie inﬁnie G(l, p, n) et pour quelques groupes exceptionnels. Aﬁn d’obtenir des ensembles
basiques canoniques pour les alg`ebres de Ariki–Koike, Geck et Jacon ont utilis´e le th´eor`eme d’Ariki sur la
cat´egoriﬁcation des repr´esentations des alg`ebres de Hecke et le travail de Uglov sur les bases canoniques
pour des espaces de Fock de plus haut niveau [GeJa1, Ja2, Ja3, GeJa2]. Le r´esultat pour G(l, p, n) est
d´eduit du r´esultat pour G(l, 1, n) avec l’utilisation de la th´eorie de Cliﬀord [GenJa, ChJa2].
Les alg`ebres de r´eﬂexions symplectiques ont ´et´e introduites par Etingof et Ginzburg [EtGi] pour
l’´etude des r´esolutions symplectiques de l’espace d’orbites V/G, o`u V est un espace vectoriel complexe
symplectique et G est un groupe de r´eﬂexions symplectique agissant sur V , i.e., G est un groupe ﬁni
engendr´e par des r´eﬂexions symplectiques. Un groupe de r´eﬂexions complexe W ⊂GL(h), o`u h est
un espace vectoriel complexe, peut ˆetre vu comme un groupe de r´eﬂexions symplectique agissant sur
V = h ⊕h∗. Les alg`ebres de r´eﬂexions symplectiques associ´ees aux groupes de r´eﬂexions complexes
2
sont connues sous le nom d’alg`ebres de Cherednik rationnelles. Elles d´ependent de fa¸con cruciale d’un
param`etre t, et leur th´eorie des repr´esentations varie beaucoup selon si t est nul ou non.
Si t̸ = 0, il existe une cat´egorie de repr´esentations de l’alg`ebre de Cherednik rationnelle importante,
la cat´egorie O, et un foncteur exact, le foncteur de Knizhnik–Zamalodchikov ou simplement KZ, de O
vers la cat´egorie de repr´esentations d’une certaine alg`ebre de Hecke cyclotomique sp´ecialis´ee Hη(W) (la
sp´ecialisation d´epend du choix des param`etres de l’alg`ebre de Cherednik rationnelle; toute alg`ebre de
Hecke sp´ecialis´ee peut ˆetre obtenue de cette fa¸con). La cat´egorie O est une cat´egorie de plus haut poids, et
elle contient un ensemble des modules standards {∆(E) | E ∈Irr(W)}, un ensemble des modules simples
{L(E) | E ∈Irr(W)} et une matrice de d´ecomposition qui d´ecrit le nombre de fois que L(E) apparaˆıt dans
la s´erie de composition de ∆(E′) pour E, E′ ∈Irr(W). L’exactitude de KZ nous permet de d´eduire la
matrice de d´ecomposition de Hη(W) de la matrice de d´ecomposition de la cat´egorie O. En utilisant cette
propri´et´e, nous avons prouv´e dans [CGG] l’existence des ensembles basiques canoniques pour tous les
groupes de Coxeter ﬁnis et pour les groupes de r´eﬂexions complexes de type G(l, 1, n) (en caract´eristique
0). En particulier, nous avons montr´e que E appartient `a l’ensemble basique canonique pour Hη(W) si et
seulement si KZ(L(E))̸ = 0. Notre preuve de leur existence est assez g´en´erale et n’utilise pas le th´eor`eme
d’Ariki pour le type G(l, 1, n). N´eanmoins la description explicite des ensembles basiques canoniques
dans ces cas par des travaux ant´erieurs permet de d´eterminer quels modules simples sont envoy´es sur
z´ero par le foncteur KZ. Nous avons aussi d´emontr´e que les images des modules standards via le foncteur
KZ sont isomorphes aux modules cellulaires des alg`ebres de Hecke.
En ce qui concerne le cas t = 0, Gordon [Go] a introduit et ´etudi´e un quotient de dimension ﬁnie de
l’alg`ebre de Cherednik rationnelle, l’alg`ebre de Cherednik rationnelle restreinte, dont les modules simples
sont param´etr´es par Irr(W). La d´ecomposition de cette alg`ebre en blocs induit une partition de Irr(W),
connue sous le nom de partition de Calogero–Moser. Nous pensons qu’il existe un lien entre la partition
de Calogero–Moser et les familles de caract`eres, d’abord sugg´er´e par Gordon et Martino [GoMa] pour
le type B. Dans tous les cas ´etudi´es jusqu’`a maintenant, la partition en familles de Rouquier (pour une
alg`ebre de Hecke cyclotomique choisie convenablement) rend la partition de Calogero–Moser plus ﬁne
(“la conjecture de Martino”), alors que pour les groupes de Coxeter ﬁnis les deux partitions co¨ıncident.
Ce lien n’est pas encore expliqu´e, ´etant donn´e qu’il n’y a pas de connexion ´evidente entre les alg`ebres
de Hecke et les alg`ebres de Cherednik rationnelles `a t = 0. Motiv´es par cette id´ee, et aﬁn de pouvoir
construire une th´eorie des cellules de Kazhdan–Lusztig g´en´eralis´ee, Bonnaf´e et Rouquier ont utilis´e la
partition de Calogero–Moser pour d´evelopper une th´eorie des “cellules de Calogero–Moser” qui peut ˆetre
appliqu´ee `a tous les groupes de r´eﬂexions complexes [BoRo1, BoRo2]. Il reste `a voir les fruits de cette
approche tr`es r´ecente.
Les alg`ebres de Yokonuma–Hecke ont ´et´e introduites par Yokonuma [Yo] dans le contexte des groupes
r´eductifs ﬁnis comme g´en´eralisations des alg`ebres de Iwahori–Hecke. Elle sont d´eﬁnies comme des alg`ebres
d’endomorphismes de la repr´esentation de permutation par rapport `a un sous-groupe unipotent maximal,
et peuvent ainsi ˆetre vues comme des cas particuliers des alg`ebres de Hecke unipotentes. Nous allons nous
int´eresser ici aux alg`ebres de Yokonuma–Hecke de type A, qui peuvent ˆetre aussi d´eﬁnies ind´ependamment
comme d´eformations des alg`ebres de groupe des groupes de r´eﬂexions complexes de type G(l, 1, n). Nous
obtenons ainsi un autre type d’alg`ebres de Hecke associ´ees `a G(l, 1, n), diﬀ´erentes des alg`ebres de Ariki–
Koike. Ayant ´etudi´e la th´eorie des repr´esentations des alg`ebres de Yokonuma–Hecke dans [ChPdA1],
nous avons d´ecouvert beaucoup de similarit´es avec la th´eorie des repr´esentations des alg`ebres de Iwahori–
Hecke de type A; ces similarit´es sont expliqu´ees par un r´esultat de Lusztig [Lu7], qui a d´emontr´e que
les alg`ebres de Yokonuma–Hecke sont isomorphes `a des sommes directes des alg`ebres matricielles sur des
produits tensoriels de certaines sous-alg`ebres des alg`ebres de Iwahori–Hecke.
Nous avons aussi introduit et ´etudi´e beaucoup de nouvelles alg`ebres int´eressantes dans le contexte des
alg`ebres de Yokonuma–Hecke, qui sont obtenues comme g´en´eralisations (ou, comme elles sont appel´ees
dans [JuLa5], “pond´erisations”) d’alg`ebres importantes dans le contexte des alg`ebres de Iwahori–Hecke.
Tout d’abord, nous avons les alg`ebres de Yokonuma–Hecke aﬃnes et cyclotomiques, qui g´en´eralisent
respectivement les alg`ebres de Hecke aﬃnes de type A et les alg`ebres de Ariki–Koike [ChPdA2]. En fait,
nous avons montr´e dans [ChSe] que les alg`ebres de Yokonuma–Hecke aﬃnes apparaissent aussi naturelle-
ment dans l’´etude des groupes r´eductifs p-adiques, avec une construction analogue `a la construction
de Yokonuma, alors que les alg`ebres de Yokonuma–Hecke cyclotomiques produisent en mˆeme temps les
alg`ebres de Ariki–Koike et les alg`ebres de Yokonuma–Hecke de type A, comme des quotients et des
cas particuliers. De plus, nous avons trois g´en´eralisations possibles de l’alg`ebre de Temperley–Lieb :
l’alg`ebre de Yokonuma–Temperley–Lieb [GJKL1], l’alg`ebre de Temperley–Lieb `a poids (“Framisation of
3
the Temperley–Lieb algebra”)[GJKL2] et l’alg`ebre de Temperley–Lieb de r´eﬂexions complexe [GJKL2].
Notre ´etude de la structure et la th´eorie des repr´esentations de ces trois alg`ebres dans [ChPo1, ChPo2]
indique que l’alg`ebre de Temperley–Lieb `a poids est l’analogue le plus naturel de l’alg`ebre de Temperley–
Lieb dans ce contexte.
Une des raisons pour lesquelles l’int´erˆet port´e aux alg`ebres de Yokonuma–Hecke s’est accru r´ecemment
est leurs applications topologiques. Suivant la m´ethode de Jones [Jo2, Jo3], la trace de Ocneanu sur
l’alg`ebre de Iwahori–Hecke de type A et son quotient, l’alg`ebre de Temperley–Lieb, peut ˆetre utilis´ee
pour la d´eﬁnition des invariants de noeuds classiques, connues sous le nom de polynˆome Homﬂypt (ou
polynˆome de Jones en 2 variables) et de polynˆome de Jones respectivement.
De fa¸con similaire, en
utilisant la trace de Markov sur l’alg`ebre de Yokonuma–Hecke de type A d´eﬁnie par Juyumaya [Ju2],
nous pouvons d´eﬁnir des invariants en 2 variables de noeuds `a poids (“framed”), classiques et singuliers
(voir [JuLa1]–[JuLa4], [CJKL]).
Durant les ann´ees derni`eres, nous travaillions sur la comparaison entre les invariants en 2 variables de
noeuds classiques obtenus par les alg`ebres de Yokonuma–Hecke et le polynˆome Homﬂypt, qui apparaˆıt
dans cette famille (voir [ChLa]). Tr`es r´ecemment, nous avons r´eussi `a prouver que nous avons en eﬀet
obtenu une nouvelle famille d’invariants, qui ne sont pas topologiquement ´equivalents au polynˆome
Homﬂypt [CJKL]. En fait, nous avons montr´e que nos invariants sont topologiquement ´equivalents au
polynˆome Homﬂypt sur les noeuds, mais qu’ils distinguent des entrelacs (c’est `a dire, des enchevˆetrements
de plusieurs noeuds) que le polynˆome Homﬂypt ne peut pas distinguer. En plus des donn´ees calcul´ees par
ordinateur, nous avons donn´e une preuve diagrammatique bas´ee sur le r´esultat suivant : les invariants
provenant des alg`ebres de Yokonuma–Hecke peuvent ˆetre d´eﬁnis de fa¸con diagrammatique via une relation
d’´echeveau (“skein relation”) qui est appliqu´ee seulement `a des croisements de composantes diﬀ´erentes.
Ce fait est tr`es important en lui-mˆeme, puisque il existe tr`es peu d’invariants de noeuds qui sont d´eﬁnis
via des relations d’´echeveau. Enﬁn, nous avons g´en´eralis´e cette famille d’invariants `a un nouvel invariant
d’´echeveau en 3 variables qui est plus fort que le polynˆome Homﬂypt.
Dans [ChPdA2], nous avons d´eﬁni des traces de Markov sur les alg`ebres de Yokonuma–Hecke aﬃnes et
cyclotomiques. Appliquant la m´ethode de Jones, nous avons obtenu des invariants de noeuds classiques et
`a poids dans le tore solide. ´Etant donn´es les r´esultats de [CJKL], ces invariants ne sont pas topologique-
ment ´equivalents aux invariants de noeuds classiques dans le tore solide de type Homﬂypt obtenus des
alg`ebres de Hecke aﬃnes et cyclotomiques dans [La1, GeLa, La2]. De fa¸con similaire, des invariants en 1
variable de noeuds `a poids et classiques peuvent ˆetre obtenus grˆace `a l’alg`ebre de Temperley–Lieb `a poids
en utilisant la trace de Juyumaya; ces invariants ne sont pas topologiquement ´equivalents au polynˆome
de Jones sur les entrelacs classiques [GJKL2].
Ce m´emoire est organis´e de la fa¸con suivante : dans le premier chapitre, nous pr´esentons quelques
r´esultats pr´eliminaires sur les blocs, les formes sym´etrisantes et les ´el´ements de Schur, les applications
et les matrices de d´ecomposition. Dans le deuxi`eme chapitre, nous ´etudions les alg`ebres de Iwahori–
Hecke associ´ees aux groupes de Coxeter ﬁnis et leur th´eorie des cellules de Kazhdan–Lusztig.
Nous
d´eﬁnissons les familles de caract`eres de trois fa¸cons diﬀ´erentes, et les ensembles basiques canoniques en
caract´eristique 0. Dans le troisi`eme chapitre, nous ´etudions les alg`ebres de Hecke associ´ees aux groupes
de r´eﬂexions complexes et explorons quelles propri´et´es se g´en´eralisent du cas r´eel au cas complexe.
Nous donnons la d´eﬁnition des alg`ebres de Hecke g´en´eriques et cyclotomiques associ´ees aux groupes de
r´eﬂexions complexes. Puis nous utilisons la d´eﬁnition de Rouquier aﬁn de g´en´eraliser la notion de familles
de caract`eres au cas des groupes de r´eﬂexions complexes, et nous expliquons comment nous pouvons
d´eterminer les familles de Rouquier dans tous les cas. Un rˆole-clef dans cette d´etermination est jou´e par
la forme des ´el´ements de Schur, qui ont ´et´e calcul´es, sous certaines hypoth`eses, pour tous les groupes
de r´eﬂexions complexes. Ces ´el´ements de Schur sont aussi utilis´es pour la d´eﬁnition d’une fonction a et
des ensembles basiques canoniques dans ce cas, et nous pr´esentons nos r´esultats dans cette direction, qui
concernent plutˆot les groupes de la s´erie inﬁnie. Dans le chapitre 4, nous nous concentrons sur les alg`ebres
de Ariki–Koike, i.e., les alg`ebres de Hecke associ´ees aux groupes de r´eﬂexions complexes de type G(l, 1, n).
Mˆeme si elles sont des cas particuliers d’alg`ebres de Hecke ´etudi´ees dans le chapitre pr´ecedent, les alg`ebres
de Ariki–Koike ont ´et´e d´eﬁnies ind´ependamment plus tˆot et ´etudi´ees combinatoirement par plusieurs
personnes. Elles constituent le cas le mieux explor´e jusqu’`a pr´esent. Nous donnons de jolies formules
combinatoires pour les ´el´ements de Schur des alg`ebres de Ariki–Koike et la fonction a. Nous montrons
aussi que les familles de caract`eres dans ce cas peuvent ˆetre compl`etement d´etermin´ees par les familles
de caract`eres des groupes de Weyl de type B. Enﬁn, nous discutons les applications de d´ecomposition
4
pour les alg`ebres de Ariki–Koike (non-gradu´ees et gradu´ees), et la preuve de Geck et Jacon de l’existence
des ensembles basiques canoniques via l’utilisation du th´eor`eme d’Ariki. Dans le cinqui`eme chapitre,
nous introduisons les alg`ebres de Cherednik rationnelles associ´ees aux groupes de r´eﬂexions complexes,
qui d´ependent d’un param`etre t. Si t̸ = 0, alors il existe un lien entre la th´eorie des repr´esentations des
alg`ebres de Cherednik rationnelles et celle des alg`ebres de Hecke cyclotomiques via le foncteur KZ, et nous
montrons comment on peut utiliser des informations sur l’un pour obtenir des informations sur l’autre, en
particulier en ce qui concerne les matrices de d´ecomposition et les ensembles basiques canoniques. Nous
obtenons l’existence des ensembles basiques canoniques pour plusieurs alg`ebres de Hecke cyclotomiques,
parmi lesquelles les alg`ebres de Iwahori–Hecke associ´ees aux groupes de Coxeter ﬁnis et les alg`ebres
de Ariki–Koike (sans l’utilisation du th´eor`eme d’Ariki).
Si t = 0, il existe aussi un lien (qui n’est
pas encore bien compris) entre la th´eorie des repr´esentations des alg`ebres de Cherednik rationnelles et
celle des alg`ebres de Hecke cyclotomiques, qui pourrait permettre le d´eveloppement d’une th´eorie des
cellules de Kazhdan–Lusztig pour les groupes de r´eﬂexions complexes. Dans le dernier chapitre, nous
´etudions les alg`ebres de Yokonuma–Hecke, qui sont obtenues dans le contexte des groupes r´eductifs
ﬁnis comme g´en´eralisations des alg`ebres de Iwahori–Hecke, et nous nous concentrons sur l’alg`ebre de
Yokonuma–Hecke de type A. Nous ´etudions sa th´eorie des repr´esentations, nous construisons une forme
sym´etrisante sur celle-ci et nous d´eterminons ses ´el´ements de Schur. Puis nous d´emontrons des r´esultats
similaires pour les alg`ebres de Yokonuma–Hecke aﬃnes et cyclotomiques, que nous introduisons comme
g´en´eralisations des alg`ebres de Yokonuma–Hecke de type A. Nous ´etudions ´egalement la th´eorie des
repr´esentations et construisons des bases pour les trois quotients de type Temperley–Lieb des alg`ebres
de Yokonuma–Hecke: l’alg`ebre de Yokonuma–Temperley–Lieb, l’alg`ebre de Temperley–Lieb `a poids et
l’alg`ebre de Temperley–Lieb de r´eﬂexions complexe. Nous d´eduisons que l’alg`ebre de Temperley–Lieb `a
poids est l’analogue le plus naturel de l’alg`ebre de Temperley–Lieb dans ce cas. Enﬁn, nous parlons des
applications topologiques de toutes ces alg`ebres, qui peuvent ˆetre utilis´ees pour la d´eﬁnition des invariants
de noeuds `a poids, classiques et singuliers avec l’utilisation des traces de Markov que nous d´eﬁnissons
sur celles-ci et la m´ethode de Jones. Nous montrons que les invariants de noeuds classiques provenant
des alg`ebres de Yokonuma–Hecke sont en eﬀet nouveaux, et ne sont pas topologiquement ´equivalents
aux fameux invariants polynomiaux obtenus dans le contexte classique des alg`ebres de Iwahori–Hecke
de type A (notamment, le polynˆome Homﬂypt, les invariants de noeuds classiques dans le tore solide de
type Homﬂypt et le polynˆome de Jones).
5
6
Introduction in English
Iwahori–Hecke algebras associated to Weyl groups appear naturally in the study of ﬁnite reductive groups
as endomorphism rings of the permutation representation with respect to a Borel subgroup. They can
also be deﬁned independently as deformations of group algebras of ﬁnite Coxeter groups. The aim of
this memoir is to study some aspects of the representation theory of Iwahori–Hecke algebras and the
way they generalise in the cases of
• cyclotomic Hecke algebras, which are obtained as deformations of group algebras of complex reﬂec-
tion groups,
• Ariki–Koike algebras, which are obtained as generalisations of Iwahori–Hecke algebras of types A
and B,
• Yokonuma–Hecke algebras, which are obtained in the study of ﬁnite reductive groups as endomor-
phism rings of the permutation representation with respect to a maximal unipotent subgroup.
In the process, we will also study another family of algebras associated to complex reﬂection groups, the
rational Cherednik algebras, whose representation theory has many connections with the representation
theory of Hecke algebras.
The aspects of the representation theory of these algebras on which we will focus will be the parametri-
sation and description of the irreducible representations in the semisimple and non-semisimple case, the
block structure, the symmetric algebra structure and the determination of the decomposition matrix
with respect to a specialisation.
Finite Coxeter groups are ﬁnite groups of real matrices that are generated by reﬂections.
They
include the Weyl groups, which are fundamental in the classiﬁcation of simple Lie algebras over C as
well as simple algebraic groups. Iwahori–Hecke algebras associated to Weyl groups appear naturally as
endomorphism algebras of induced representations in the study of ﬁnite reductive groups. They can
also be deﬁned independently as deformations of group algebras of ﬁnite Coxeter groups, where the
deformation depends on a parameter q and a weight function L. For q = 1, we recover the group algebra.
For a ﬁnite Coxeter group W, we will denote by Hq(W, L) the associated Iwahori–Hecke algebra.
When q is an indeterminate, the Iwahori–Hecke algebra Hq(W, L) is semisimple. By Tits’s defor-
mation theorem, there exists a bijection between the set of irreducible representations of Hq(W, L) and
the set Irr(W) of irreducible representations of W. Through this bijection, Lusztig attaches to every
irreducible representation of W an integer depending on L, thus deﬁning the famous a-function. Here we
deﬁne the a-function using the symmetric algebra structure and the Schur elements of Hq(W, L). The
a-function is used in Lusztig’s deﬁnition of families of characters, a partition of Irr(W) which plays a
principal role in the organisation of families of unipotent characters in the case of ﬁnite reductive groups.
Kazhdan–Lusztig theory is a key to understanding the representation theory of the Iwahori–Hecke
algebra Hq(W, L). There exists a special basis of Hq(W, L), called the Kazhdan–Lusztig basis, which
allows us to deﬁne the Kazhdan–Lusztig cells for Hq(W, L), a certain set of equivalence classes on W.
The construction of Kazhdan–Lusztig cells yields the construction of representations for Hq(W, L). It
also gives another, more combinatorial, deﬁnition for Lusztig’s families of characters.
Now, when q specialises to a non-zero complex number η, and more speciﬁcally to a root of unity, the
specialised Iwahori–Hecke algebra Hη(W, L) is not necessarily semisimple and we no longer have a bijec-
tion between its irreducible representations and Irr(W). We obtain then a decomposition matrix which
records how the irreducible representations of the semisimple algebra decompose after the specialisation.
7
A canonical basic set is a subset of Irr(W) in bijection with the irreducible representations of Hη(W, L)
(and thus a labelling set for the columns of the decomposition matrix) with good properties. These good
properties ensure that the decomposition matrix has a lower unitriangular form while the a-function
increases (roughly) down the columns. Canonical basic sets were deﬁned by Geck and Rouquier [GeRo],
who also proved their existence in certain cases with the use of Kazhdan–Lusztig theory. Thanks to the
work of many people, canonical basic sets are now proved to exist and explicitly described for all ﬁnite
Coxeter groups and for any choice of L (in characteristic 0).
Finite Coxeter groups are particular cases of complex reﬂection groups, that is, ﬁnite groups of
complex matrices generated by “pseudo-reﬂections”. Their classiﬁcation is due to Shephard and Todd
[ShTo]: if W is an (irreducible) complex reﬂection group, then either W belongs to the inﬁnite series
G(l, p, n) or W is one of the 34 exceptional groups G4, . . . , G37 (see Theorem 3.1). Important work in
the last two decades has suggested that complex reﬂection groups play a crucial, but not yet understood
role in representation theory, and may even become as ubiquitous as ﬁnite Coxeter groups in the study of
other mathematical structures. In fact, they behave so much like real reﬂection groups that Brou´e, Malle
and Michel [BMM1] conjectured that they could play the role of Weyl groups for, as yet mysterious,
objects generalising ﬁnite reductive groups. These objects are called “Spetses”.
Brou´e, Malle and Rouquier [BMR] deﬁned Hecke algebras for complex reﬂection groups as defor-
mations of their group algebras. In the case of complex reﬂection groups of type G(l, 1, n), these co-
incide with the Ariki–Koike algebras, already deﬁned by Ariki and Koike [ArKo] as generalisations of
Iwahori–Hecke algebras of types A and B. A generalised Kazhdan–Lusztig cell theory for these algebras,
known as cyclotomic Hecke algebras, is expected to help ﬁnd Spetses. Unfortunately, we do not have a
Kazhdan–Lusztig basis for complex reﬂection groups. However, we can deﬁne families of characters using
Rouquier’s deﬁnition: in [Ro1], Rouquier gave an alternative deﬁnition for Lusztig’s families of characters
by proving that, in the case of Weyl groups, they coincide with the blocks of the Iwahori–Hecke algebra
over a certain ring, called the Rouquier ring. This deﬁnition generalises naturally to the case of complex
reﬂection groups and their cyclotomic Hecke algebras, producing the so-called Rouquier families. These
families have now been determined for all cyclotomic Hecke algebras of all complex reﬂection groups,
see [Ch3, Ch4, Ch5]. A key role in this determination is played by the (still conjectural in some cases)
symmetric algebra structure of cyclotomic Hecke algebras and the corresponding Schur elements.
Using the Schur elements, we can also deﬁne an a-function and canonical basic sets for cyclotomic
Hecke algebras. Although there is no Kazhdan–Lusztig theory in the complex case, canonical basic sets
are now known to exist for the groups of the inﬁnite series G(l, p, n) and for some exceptional ones. In
order to obtain canonical basic sets for Ariki–Koike algebras, Geck and Jacon used Ariki’s Theorem on
the categoriﬁcation of Hecke algebra representations and Uglov’s work on canonical bases for higher level
Fock spaces [GeJa1, Ja2, Ja3, GeJa2]. The result for G(l, p, n) derives from that for G(l, 1, n) with the
use of Cliﬀord Theory [GenJa, ChJa2].
Symplectic reﬂection algebras were introduced by Etingof and Ginzburg [EtGi] for the study of
symplectic resolutions of the orbit space V/G, where V is a symplectic complex vector space and G is a
symplectic reﬂection group acting on V , that is, G is a ﬁnite group generated by symplectic reﬂections.
A complex reﬂection group W ⊂GL(h), where h is a complex vector space, can be seen as a symplectic
reﬂection group acting on V = h ⊕h∗. Symplectic reﬂection algebras associated with complex reﬂection
groups are known as rational Cherednik algebras. They depend on a parameter t, and their representation
theory varies a lot according to whether t is zero or not.
If t̸ = 0, there exists an important category of representations of the rational Cherednik algebra, the
category O, and an exact functor, the Knizhnik–Zamalodchikov functor or simply KZ, from O to the
category of representations of a certain specialised cyclotomic Hecke algebra Hη(W) (the specialisation
depends on the choice of parameters for the rational Cherednik algebra; every specialised Hecke algebra
can arise this way). Category O is a highest weight category, and it comes equipped with a set of standard
modules {∆(E) | E ∈Irr(W)}, a set of simple modules {L(E) | E ∈Irr(W)} and a decomposition matrix
that records the number of times that L(E) appears in the composition series of ∆(E′) for E, E′ ∈Irr(W).
The exactness of KZ allows us to read oﬀthe decomposition matrix of Hη(W) from the decomposition
matrix of category O. Using this, we proved in [CGG] the existence of canonical basic sets for all ﬁnite
Coxeter groups and for complex reﬂection groups of type G(l, 1, n) (in characteristic 0). In particular,
we showed that E belongs to the canonical basic set for Hη(W) if and only if KZ(L(E))̸ = 0. Our proof
of existence is quite general and it does not make use of Ariki’s Theorem for type G(l, 1, n). However,
the explicit description of canonical basic sets in these cases by previous works answers simultaneously
8
the question of which simple modules are killed by the KZ-functor. We also proved that the images of
the standard modules via the KZ-functor are isomorphic to the cell modules of Hecke algebras.
As far as the case t = 0 is concerned, Gordon [Go] introduced and studied extensively a ﬁnite-
dimensional quotient of the rational Cherednik algebra, called the restricted rational Cherednik algebra,
whose simple modules are parametrised by Irr(W). The decomposition of this algebra into blocks induces
a partition of Irr(W), known as Calogero–Moser partition. It is believed that there exists a connection
between the Calogero–Moser partition and the families of characters, ﬁrst suggested by Gordon and
Martino [GoMa] for type B. In every case studied so far, the partition into Rouquier families (for a
suitably chosen cyclotomic Hecke algebra) reﬁnes the Calogero–Moser partition (“Martino’s conjecture”),
while for ﬁnite Coxeter groups the two partitions coincide. The reasons for this connection are still
unknown, since there is no apparent connection between Hecke algebras and rational Cherednik algebras
at t = 0. Inspired by this, and in an eﬀort to construct a generalised Kazhdan–Lusztig cell theory, Bonnaf´e
and Rouquier have used the Calogero–Moser partition to develop a “Calogero–Moser cell theory” which
can be applied to all complex reﬂection groups [BoRo1, BoRo2]. The fruits of this very recent approach
remain to be seen.
Yokonuma–Hecke algebras were introduced by Yokonuma [Yo] in the context of ﬁnite reductive groups
as generalisations of Iwahori–Hecke algebras. They are deﬁned as endomorphism rings of the permutation
representation with respect to a maximal unipotent subgroup, and can thus be regarded as particular
cases of unipotent Hecke algebras. We will focus here on Yokonuma–Hecke algebras of type A, which
can be also deﬁned independently as deformations of group algebras of complex reﬂection groups of type
G(l, 1, n). We thus obtain another type of Hecke algebras associated to G(l, 1, n), diﬀerent from Ariki–
Koike algebras. Having studied the representation theory of Yokonuma–Hecke algebras in [ChPdA1],
we have discovered many similarities with the representation theory of Iwahori–Hecke algebras of type
A; these similarities are explained by a result of Lusztig [Lu7], who has proved that Yokonuma–Hecke
algebras are isomorphic to direct sums of matrix algebras over tensor products of certain subalgebras of
Iwahori–Hecke algebras.
We have now introduced and studied many interesting new algebras in the Yokonuma–Hecke algebra
setting, which are obtained as generalisations (or, as called in [JuLa5], “framisations”) of important
algebras in the Iwahori–Hecke algebra setting. First of all, we have the aﬃne and cyclotomic Yokonuma–
Hecke algebras, which generalise respectively the aﬃne Hecke algebras of type A and the Ariki–Koike
algebras [ChPdA2].
In fact, we have shown in [ChSe] that aﬃne Yokonuma–Hecke algebras appear
also naturally in the study of p-adic reductive groups, arising from a construction analogous to the one
used by Yokonuma, while cyclotomic Yokonuma–Hecke algebras give rise to both Ariki–Koike algebras
and classical Yokonuma–Hecke algebras of type A, both as quotients and as particular cases. Further,
we have three possible generalisations of the Temperley–Lieb algebra: the Yokonuma–Temperley–Lieb
algebra [GJKL1], the Framisation of the Temperley–Lieb algebra [GJKL2] and the Complex Reﬂection
Temperley–Lieb algebra [GJKL2]. Our study of the structure and the representation theory of these
three algebras in [ChPo1, ChPo2] indicates that the Framisation of the Temperley–Lieb algebra is the
most natural analogue of the Temperley–Lieb algebra in this setting.
One of the reasons that Yokonuma–Hecke algebras have attracted a lot of interest recently is their
topological applications.
After Jones’s method [Jo2, Jo3], the Ocneanu trace on the Iwahori–Hecke
algebra of type A and its quotient, the Temperley–Lieb algebra, can be used to deﬁne isotopy invariants
for classical knots and links, known as the Homﬂypt polynomial (or 2-variable Jones polynomial) and
the Jones polynomial respectively. In a similar way, using the Markov trace on the Yokonuma–Hecke
algebra of type A deﬁned by Juyumaya [Ju2], one can deﬁne 2-variable isotopy invariants for framed,
classical and singular knots and links (see [JuLa1]–[JuLa4], [CJKL]).
For the past years, we have been trying to compare the family of 2-variable isotopy invariants of
oriented classical links arising from Yokonuma–Hecke algebras with the Homﬂypt polynomial, which
is included in this family (see [ChLa]).
Very recently, we were successful in proving that we have
indeed obtained a new family of invariants, which are not topologically equivalent to the Homﬂypt
polynomial [CJKL].
In fact, we have shown that our invariants are topologically equivalent to the
Homﬂypt polynomial on knots, but they distinguish links that the Homﬂypt polynomial does not. Besides
computational data, we have given a diagrammatic proof based on the following result: the invariants
from Yokonuma–Hecke algebras can be deﬁned diagrammatically via a special skein relation involving
only crossings between diﬀerent components. This fact is very important in its own right, since there
are very few link invariants deﬁned through skein relations. Finally, we have generalised this family of
9
invariants to a new 3-variable skein link invariant which is stronger than the Homﬂypt polynomial.
In [ChPdA2], we have deﬁned Markov traces on aﬃne and cyclotomic Yokonuma–Hecke algebras.
Applying Jones’s method, we have obtained invariants for framed and classical links in the solid torus.
In view of the results of [CJKL], these invariants are not topologically equivalent to the Homﬂypt-type
invariants for classical links in the solid torus obtained from aﬃne and cyclotomic Hecke algebras in
[La1, GeLa, La2]. Similarly, 1-variable isotopy invariants of oriented framed and classical links can be
obtained from the Framisation of the Temperley–Lieb algebra with the use of Juyumaya’s trace; these
invariants are not topologically equivalent to the Jones polynomial on classical links [GJKL2].
This memoir is organised as follows: In the ﬁrst chapter, we present some preliminary results on
blocks, symmetrising forms and Schur elements, decomposition maps and matrices. In the second chapter,
we discuss Iwahori–Hecke algebras associated with ﬁnite Coxeter groups and their Kazhdan–Lusztig cell
theory. We deﬁne families of characters in three diﬀerent ways, and canonical basic sets in characteristic 0.
In the third chapter, we study the Hecke algebras associated with complex reﬂection groups and explore
which properties generalise from the real case to the complex case. We give the deﬁnition of generic and
cyclotomic Hecke algebras associated with complex reﬂection groups. We then use Rouquier’s deﬁnition
in order to generalise the notion of families of characters to the case of complex reﬂection groups, and
we explain how we can determine the Rouquier families in all cases. A key role in this determination is
played by the form of the Schur elements, which have been calculated, under certain assumptions, for
all complex reﬂection groups. These Schur elements are also used for the deﬁnition of an a-function and
canonical basic sets in this case, and we present our results in this direction, which mostly concern the
groups of the inﬁnite series. In Chapter 4, we focus on Ariki–Koike algebras, that is, Hecke algebras
associated with complex reﬂection groups of type G(l, 1, n). Even though these are included in the Hecke
algebras studied in the previous chapter, Ariki–Koike algebras were deﬁned earlier independently and
studied combinatorially by many people, so this is the best understood case. We give nice combinatorial
formulas for the Schur elements of Ariki–Koike algebras and the a-function. We also prove that the
families of characters in this case can be completely determined by the families of characters of Weyl
groups of tye B. Finally, we discuss decomposition maps for Ariki–Koike algebras (ungraded and graded),
and Geck and Jacon’s proof of existence of canonical basic sets with the use of Ariki’s Theorem. In the
ﬁfth chapter, we introduce rational Cherednik algebras associated with complex reﬂection groups, which
depend on a parameter t. If t̸ = 0, then there is a connection between the representation theory of
rational Cherednik algebras and that of cyclotomic Hecke algebras through the KZ-functor, and we show
how we can use information on the former to obtain information on the latter and vice versa, especially
in regard to decomposition matrices and canonical basic sets. We obtain the existence of canonical basic
sets for many cyclotomic Hecke algebras, including Iwahori–Hecke algebras associated with ﬁnite Coxeter
groups and Ariki–Koike algebras (without the use of Ariki’s Theorem). If t = 0, there is also a (not
yet understood) connection between the representation theory of rational Cherednik algebras and that
of cyclotomic Hecke algebras, which could allow the development of a Kazhdan–Lusztig cell theory for
complex reﬂection groups. In the last chapter, we study Yokonuma–Hecke algebras, which are obtained
in the context of ﬁnite reductive groups as generalisations of Iwahori–Hecke algebras, and we focus on
the Yokonuma–Hecke algebra of type A. We study its representation theory, construct a symmetrising
form on it and determine its Schur elements. We then provide similar results for aﬃne and cyclotomic
Yokonuma–Hecke algebras, which we introduce as generalisations of Yokonuma–Hecke algebras of type
A. We also study the representation theory and construct bases for the three suggested Temperley–Lieb
type quotients of Yokonuma–Hecke algebras: the Yokonuma–Temperley–Lieb algebra, the Framisation
of the Temperley–Lieb algebra and the Complex Reﬂection Temperley–Lieb algebra. We deduce that the
Framisation of the Temperley–Lieb algebra is the most natural analogue of the Temperley–Lieb algebra
in this case. Finally, we discuss the topological applications of all these algebras, which can be used
to deﬁne invariants for framed, classical and singular knots and links using the Markov traces that we
deﬁne on them and Jones’s recipe. We show that the classical link invariants arising from Yokonuma–
Hecke algebras are actually new, and not topologically equivalent to the famous polynomial invariants
obtained in the classical setting of Iwahori–Hecke algebras of type A (namely, the Homﬂypt polynomial,
the Homﬂypt-type invariants of links in the solid torus and the Jones polynomial).
10
Contents
1
Algebras of Finite Type
13
1.1
Blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
1.2
Symmetrising forms and Schur elements . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
1.3
Decomposition maps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
2
Iwahori–Hecke Algebras
17
2.1
Kazhdan–Lusztig cells . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
2.2
Schur elements and the a-function
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
2.3
Families of characters and Rouquier families . . . . . . . . . . . . . . . . . . . . . . . . . .
20
2.4
Decomposition maps and canonical basic sets . . . . . . . . . . . . . . . . . . . . . . . . .
21
3
Cyclotomic Hecke Algebras
23
3.1
Hecke algebras for complex reﬂection groups . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.2
Schur elements and the a-function
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3.3
Families of characters and Rouquier families . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.4
Decomposition maps and canonical basic sets . . . . . . . . . . . . . . . . . . . . . . . . .
27
4
Ariki–Koike Algebras
29
4.1
Combinatorics of partitions and multipartitions . . . . . . . . . . . . . . . . . . . . . . . .
29
4.2
Schur elements and the a-function
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
4.3
Families of characters and Rouquier families . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.4
Decomposition maps and canonical basic sets . . . . . . . . . . . . . . . . . . . . . . . . .
33
5
Rational Cherednik Algebras
35
5.1
Rational Cherednik Algebras at t = 1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
5.2
Canonical basic sets for Hecke algebras from rational Cherednik algebras . . . . . . . . . .
38
5.3
Rational Cherednik Algebras at t = 0
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
5.4
Families of characters for Hecke algebras from rational Cherednik algebras . . . . . . . . .
42
6
Yokonuma–Hecke Algebras
45
6.1
Representation theory of Yokonuma–Hecke algebras
. . . . . . . . . . . . . . . . . . . . .
46
6.2
Aﬃne and Cyclotomic Yokonuma–Hecke algebras . . . . . . . . . . . . . . . . . . . . . . .
48
6.3
Temperley–Lieb quotients of Yokonuma–Hecke algebras
. . . . . . . . . . . . . . . . . . .
51
6.4
Knot invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
Bibliography
65
11
12
Chapter 1
