---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-251-1711-lemme-sia-est-proﬁnie-le-quotient-a-dea-par
section_title: "Lemme. SiA est proﬁnie, le quotient ¯A deA par son radical est semi-simple"
section_number: 17.1.1
pages: 94-96
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
(proﬁnie, non n´ecessairement deK-dimension ﬁnie). A fortiori, le foncteur
¯A–Modf→A–Modf
est pleinement ﬁd`ele.
22Il y a lieu ´ eventuellement de prendre un second univers pour ne travailler qu’avec de petites
cat´ egories.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 95
D´emonstration. ´EcrivonsA comme limite projective ﬁltrante lim
←−Aα ` a ﬂ` eches de
transition surjectives. Comme un ´ el´ ement inversible deA s’identiﬁe ` a une collection
d’´ el´ ements inversibles compatibles deAα, on obtient, en revenant ` a la d´ eﬁnition des
radicaux, que le radicalR deA est la limite lim
←−Rα des radicaux deAα. On a alors
un plongement֒→lim
←−(Aα/Rα), le compos´ e avec la projection sur chaque
alg` ebre semi-simpleAα/Rα ´ etant surjective. CommeA/R est proﬁnie (R ´ etant un
id´ eal ferm´ e), cette injection est donc un isomorphisme, d’o` u le r´ esultat. □
On sait que A–Modf est une K-cat´ egorie de Wedderburn (proposition 2.4.4).
On peut donc appliquer le th´ eor` eme 12.1.1, et obtenir une section fonctorielle s :
A–Modf→A–Modf, deux telles sections ´ etant conjugu´ ees.
D’apr` es [53, II.2.6.3] ou [54, 2.2], il existe uneK-alg`ebre pro-semi-simpleAs,
non n´ ecessairement deK-dimension ﬁnie, telle que le compos´ eω◦s induise une
´ equivalence de cat´ egoriesA–Modf→As–Modf, et un homomorphismeA→As.
On rappelle qu’´ etant donn´ e un homomorphismef : A′ → A de K-alg` ebres
proﬁnies et le foncteur associ´ ef∗ : A–Modf→ A′–Modf, on a (cf. [53, II.2.6.3]
pour l’´ enonc´ e dual) :
– f est surjectif si et seulement si f∗ est pleinement ﬁd` ele, et pour toutA-
module K-ﬁni M, tout sous-objet de f∗(M ) provient d’un sous-objet de
M ;
– f est injectif si et seulement si toutA′-moduleK-ﬁniM′ est sous-quotient
d’un module de la formef∗(M ).
En particulier, le morphismeA→As est une injection. Comme deux sections s
sont conjugu´ ees,As est bien d´ eﬁnie ` a isomorphisme pr` es. Il d´ ecoule par ailleurs du
lemme pr´ ec´ edent, et deloc. cit., que l’on a une surjectionAs→A/R.
On peut consid´ ererAs comme une “enveloppe pro-semi-simple” de l’alg` ebre
proﬁnie A : d’apr` es le lemme 12.1.2,les classes d’isomorphismes de A-modules
ind´ecomposables sont en bijection avec les classes d’isomorphismes deAs-modules
simples.
Cette bijection est donn´ ee de la mani` ere suivante : ` a toutind´ ecomposableM dans
A-Modf, on peut donner une structure de As-module ´ etendant celle deA-module.
On le note alors Ms ; il est simple, et EndAsMs est le corps gauche EndA(M ) =
EndAM/rad(EndAM ).
L’alg` ebre pro-semi-simpleAs est semi-simple, i.e. de dimension ﬁnie sur K, si
et seulement siA est de type de repr´esentation ﬁni. Dans ce cas, siMα parcourt un
syst` eme de repr´ esentants des classes d’isomorphismes deA-modules ind´ ecomposa-
blesK-ﬁnis, notonsnα la dimension deMα sur le corps gaucheDα =EndA(Mα).
On aAs∼
=∏
αMnα(Do
α).
17.1.2. Remarques.
a) D’apr` es [14, 2.17], touteK-cat´ egorie ab´ elienne dont tout objet est de longueur
ﬁnie, dont toute alg` ebre d’endomorphismes est deK-dimension ﬁnie, et ad-
mettant un g´ en´ erateur, est ´ equivalente ` a une cat´ egorie A–Modf pour une
K-alg` ebreA convenable de dimension ﬁnie surK.
96 YVES ANDR ´E ET BRUNO KAHN
b) Pour l’alg` ebre proﬁnieA =K[[T1,...,T n]], la cat´ egorieA–Modf est na-
turellement ´ equivalente ` a la cat´ egorieRepK(Gn
a ) des repr´ esentations de
dimension ﬁnie du groupe vectoriel Gn
a. En effet, la cog` ebre duale deA s’i-
dentiﬁe naturellement ` a la cog` ebre sous-jacente ` a la big` ebre afﬁneO(Gn
a ),
et on conclut par [54, 3].
c) SoitJ l’id´ eal deA =A-Modf form´ e des morphismes qui se factorisent ` a
travers un objet projectif de A-Modf. Le quotientA/J s’appelle la cat´ e-
gorie stable desA-modules ﬁnis, cf. [3, p.23], et se noteA–Modf
. On a un
diagramme commutatif
A–Modf
pr
−−−−→A–Modf

↓


↓
A–Modf
pr
−−−−→A–Modf.
Le foncteur du bas pr est un foncteur plein surjectif entre cat´ egories
semi-simples, donc admet une section. En fait, on peut partitionner les classes
d’isomorphismes d’objets simples deA–Modf en deux ensembles : les pro-
jectifs (P ) et les autres (NP ) ;pr envoie les objets dans P sur 0, et la re-
striction depr ` a la sous-cat´ egorieK-lin´ eaire pleine deA–Modf engendr´ ee
par les objets dansNP est une ´ equivalence de cat´ egories. On en d´ eduit que
A–Modf∼
=As
–Modf pour un quotientAs deAs “correspondant” ` aNP .
On peut alors former le “push-out”A′ =As×As A/R.
Auslander a conjectur´ e que siA etB sont deux K-alg` ebres de dimen-
sion ﬁnie telles que A–Modf et B–Modf sont ´ equivalentes (´ equivalence
de Morita stable), alors il y a le mˆ eme nombre de modules simp les non-
projectifs sur A et sur B, cf. [3, p.223]. Cela ´ equivaut donc ` a dire que les
alg` ebres push-outA′ etB′ sont Morita-´ equivalentes.
Rappelons d’autre part que siA est de dimension globale ﬁnie (au sens
de [11]), on peut lui associer uneK-alg` ebreˆA dite r´ ep´ etitive (de dimension
inﬁnie surK), et une ´ equivalence de cat´ egories
Db(A–Modf)→ ˆA–Modf
cf. [50, 5], [22] ; on peut d’ailleurs replacer ˆA par sa compl´ etion proﬁnie.
Ce qui pr´ ec` ede permet alors de “d´ ecrire” le quotient deDb(A–Modf) par
son radical.
