---
doc_id: equations-aux-q-differences
doc_title: "Équations aux q-différences"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
toc_source: inferred
doc_brief: "Équations aux q-différences — 14 sections: Front matter; Introduction; Br´eviaire"
---
Une ´equation diﬀ´erentielle ordinaire est une relation G(x; f, . . . , f (n)) = 0
entre une fonction inconnue f et ses transform´ees par it´eration de « l’automor-
phisme inﬁnit´esimal » f →
d
dxf. De fa¸con analogue on peut s’int´eresser au cas
o`u l’automorphisme inﬁnit´esimal est remplac´e par un v´eritable automorphisme
ϕ d’un domaine en x. Le cas le plus simple et le seul que nous consid´ererons
ici, est celui o`u x varie dans la sph`ere de Riemann (ou plus g´en´eralement un
ouvert de celle-ci invariant par ϕ ou un germe de voisinage d’un point ﬁxe
de cet automorphisme) et o`u de plus l’automorphisme ϕ est une homogra-
phie. On obtient alors des ´equations fonctionnelles G(x; f, . . . , σnf) = 0 (o`u
l’on a pos´e σf(x) = f(ϕ(x))). Nous nous int´eresserons uniquement au cas o`u
G(x; y0, . . . , yn) est analytique en toutes les variables sur un domaine r´eel ou
complexe ou p-adique. Nous parlerons alors d’´equations « aux diﬀ´erences » ana-
lytiques. Par conjugaison homographique sur x on se ram`ene imm´ediatement
aux deux cas suivants :
– ϕ(x) = qx, o`u q ∈C∗(C est le corps de base) : on a une ´equation aux
q-diﬀ´erences;
– ϕ(x) = x + 1 : on a une ´equation aux diﬀ´erences (on dit aussi aux diﬀ´erences
ﬁnies).
Le premier cas correspond `a une homographie ϕ `a deux points ﬁxes distincts,
le second `a une homographie ϕ `a point ﬁxe double. Le cas g´en´erique est donc
le premier et il est raisonnable qu’il soit (bien que moins classique) plus simple
que le second. Nous noterons
σqf(x) = f(qx) et τεf(x) = f(x + ε).
On retrouve le cas diﬀ´erentiel par « passage `a la limite continue » ou
« conﬂuence » :
δq = σq −1
q −1
−→x d
dx, lorsque q →1,
et
∆ε = τε −1
ε
−→
d
dx, lorsque ε →0.
∗∗∗
∗
Lucia Di Vizio, Jean-Pierre Ramis, Jacques Sauloy, Laboratoire ´Emile Picard, U.F.R.
M.I.G., 118, route de Narbonne, 31062 Toulouse CEDEX 4
†
Changgui Zhang, Laboratoire AGAT, U.F.R. de Math´ematiques Pures et Appliqu´ees,
59655 Villeneuve d’Ascq CEDEX
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
21
L’´etude des ´equations aux q-diﬀ´erences commence au xviiie si`ecle avec Euler
dans le cadre de probl`emes de d´enombrement en th´eorie des nombres (parti-
tio numerorum). Une ´etape importante est due `a Heine qui introduit les q-
analogues des fonctions hyperg´eom´etriques d’Euler et Gauss : les fonctions
hyperg´eom´etriques basiques qui sont solutions d’´equations aux q-diﬀ´erences
lin´eaires alg´ebriques du second ordre, analogues des ´equations diﬀ´erentielles
hyperg´eom´etriques classiques (cf. 2.2). Il faut citer ensuite les travaux de Ja-
cobi : ses fonctions thˆeta et sa c´el`ebre formule du triple produit jouent un rˆole
central dans la th´eorie (cf. §3 et §4).
Consid´erons, par exemple, la s´erie binomiale, que nous ´ecrivons ici en utili-
sant la notation classique des s´eries hyperg´eom´etriques :
1F0(α; −; x) =
def
+∞

n=0
(α)n
n! xn,
o`u (α)n = α(α + 1) · · · (α + n −1) est le symbole de Pochhammer. Elle est
solution de l’´equation diﬀ´erentielle
(1.0.1)
(1 −x)y′ −αy = 0,
ce qui permet de d´emontrer le th´eor`eme binomial :
1F0(α; −; x) = (1 −x)−α.
Il existe un q-analogue de cette identit´e (Cauchy 1843, Heine, cf. [GR90, 1.3]).
En eﬀet la s´erie 1F0(α; −; x) peut ˆetre « d´eform´ee » de la fa¸con suivante :
1Φ0(a; −; q, x) =
def
+∞

n=0
(a; q)n
(q; q)n
xn,
o`u l’on a pos´e, pour q ∈C, |q| < 1 et n ∈N ∪{∞} :
(a; q)n =
n−1

i=0
(1 −aqi).
Cette s´erie fait partie de la famille des s´eries hyperg´eom´etriques basiques intro-
duites par Heine. C’est une d´eformation de la pr´ec´edente en ce sens que, si l’on
impose a = qα, alors les coeﬃcients de 1Φ0 tendent terme `a terme vers ceux de
1F0 lorsque q →1. Par ailleurs, elle est solution de l’´equation aux q-diﬀ´erences
(1.0.2)
(1 −ax)y(qx) −(1 −x)y(x) = 0,
tout comme la fonction m´eromorphe d´eﬁnie par
(ax; q)∞
(x; q)∞
=
def lim
n→∞
(ax; q)n
(x; q)n
,
ce qui permet de d´emontrer le th´eor`eme q-binomial :
1Φ0(a; −; q, x) = (ax; q)∞
(x; q)∞
.
L’id´ee de « d´eformation » peut ˆetre pr´ecis´ee comme suit : pour |x| < 1, la
fonction 1Φ0(a; −; q, x) tend vers la fonction 1F0(α; −; x) lorsque q →1. On
SMF – Gazette – 96, Avril 2003
22
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
peut aussi remarquer que l’´equation fonctionnelle (1.0.2), r´e´ecrite en utilisant
l’op´erateur δq, tend vers l’´equation (1.0.1) lorsque q →1 (toujours avec a =
qα). Le lien g´en´eral entre ces deux « conﬂuences » (des ´equations et de leurs
solutions) sera explicit´e plus loin.
∗∗∗
Reprenons notre bref historique. Apr`es Jacobi, on retrouve les ´equations aux
q-diﬀ´erences chez Poincar´e et Picard, puis Ramanujan (cf. en particulier le Lost
Notebook), G. Watson... puis un peu plus tard (et apparemment dans le cadre de
motivations assez diﬀ´erentes) chez G. Birkhoﬀet certains de ses ´el`eves. On aura
une bonne id´ee de l’histoire du sujet, de son int´erˆet et de l’ampleur du travail
qu’il a suscit´e au cours des si`ecles en feuilletant la consid´erable bibliographie de
[GR90]. Ceci ´etant, il est clair que ce th`eme a ´et´e largement oubli´e et a presque
totalement disparu du courant dominant des math´ematiques pendant un bon
demi-si`ecle apr`es la ﬁn des ann´ees quarante.
La situation a commenc´e `a changer il y a environ dix ans et apparemment
pour des raisons tr`es vari´ees, dans le cadre de divers courants de recherche
´emergents (ou r´e´emergents...) :
– q-combinatoire, q-analogues des polynˆomes orthogonaux;
– ph´enom`enes al´eatoires discrets ;
– groupes quantiques, repr´esentations;
– physique th´eorique (travaux de Baxter, discr´etisations, d´eformations...);
– arithm´etique (q-identit´es, transcendance, exponentielles en caract´eristique
positive) ;
. . . . . . . . .
Il y a ainsi aujourd’hui un foisonnement impressionnant de travaux en
math´ematique et physique faisant intervenir des ´equations aux q-diﬀ´erences
(souvent `a plusieurs variables et parfois non lin´eaires). Il est donc assez
paradoxal de constater que le sujet manquait jusqu’`a une date tr`es r´ecente
de fondations solides, mˆeme dans le cas le plus simple des ´equations lin´eaires
ordinaires. Ceci est en fait similaire `a ce qui s’est pass´e pour les ´equations
diﬀ´erentielles ordinaires au xxe si`ecle : entre la ﬁn des ann´ees quarante et
le d´ebut des ann´ees soixante-dix le sujet fut consid´er´e comme clos et sans
grand int´erˆet autre qu’historique (cf. par exemple sa « densit´e bourbachique »
presque nulle). La th´eorie des ´equations diﬀ´erentielles ordinaires analytiques
a ´et´e d’abord renouvel´ee par la « red´ecouverte » des ´equations du type de
Fuchs, puis par celle des ´equations `a singularit´es irr´eguli`eres et de tous les
probl`emes diﬃciles et non r´esolus qu’elles posaient. Un retour `a des id´ees
essentielles de Birkhoﬀ(en particulier `a son article de 1913 sur le c´el`ebre
probl`eme de Riemann-Hilbert [Bir13]) a jou´e un rˆole central dans les progr`es
tr`es importants faits `a la ﬁn du xxe si`ecle sur le sujet. Pour les ´equations
aux q-diﬀ´erences l’histoire se r´ep`ete avec quelque retard. L`a aussi le retour `a
Birkhoﬀa jou´e un rˆole essentiel. Nous nous proposons d’expliquer dans cet
article comment la r´ecente r´esolution compl`ete d’une s´erie de questions pos´ees
par G. Birkhoﬀen 1941 (peu avant sa mort) fournit une base raisonnable pour
la th´eorie des ´equations aux q-diﬀ´erences lin´eaires analytiques et ouvre une
s´erie d’interrogations que nous trouvons assez passionnantes vers la th´eorie
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
23
de Galois, l’arithm´etique, la g´eom´etrie non-commutative... Nous voudrions en
particulier convaincre le lecteur qu’au del`a de formules que l’on peut trouver
un peu d´ecourageantes (faute d’avoir le talent de Ramanujan ou des outils
performants de calcul formel [Chy98]) se dessine une assez jolie g´eom´etrie
nouvelle greﬀ´ee sur la g´eom´etrie alg´ebrique classique.
Up to the present time, the theory of linear q-diﬀerence equa-
tions has lagged noticeably behind the sister theories of linear
diﬀerence and diﬀerential equations. In the opinion of the au-
thors, the use of the canonical system, as formulated above in
a special case, is destined to carry the theory of q-diﬀerence
equations to a comparable degree of completeness. This pro-
gram includes in particular the complete theory of convergence
and divergence of formal series, the explicit determination of
the essential transcendental invariants (constants in the cano-
nical form), the inverse Riemann theory both for the neighbo-
rhood of x = ∞and in the complete plane (case of rational
coeﬃcients), explicit integral representation of the solutions,
and ﬁnally the deﬁnition of q-sigma periodic matrices, so far
deﬁned essentially only in the case n = 1. Because of its ex-
tensiveness this material cannot be presented here.
G.D. Birkhoﬀet P.E. Guenther, 1941
Au del`a de l’ach`evement de ce programme, pour |q|̸ = 1, se posent de nom-
breuses questions naturelles. En voici deux :
– Quelle est la relation entre les invariants alg´ebriques et transcendants « de
Birkhoﬀ» (invariants locaux, matrice de connection de Birkhoﬀ, q-Stokes) et
la th´eorie de Galois aux q-diﬀ´erences ([vdPS97]) ? (Rappelons que dans le cas
diﬀ´erentiel la question est totalement ´elucid´ee : caract`ere galoisien de la mo-
nodromie et des multiplicateurs de Stokes, th´eor`emes de Zariski-densit´e de
Schlesinger et Ramis [Ram93].)
– Y a-t-il conﬂuence des q-invariants vers les invariants diﬀ´erentiels quand on
« passe `a la limite continue » pour q →1 dans des conditions raisonnables.
Ces deux probl`emes sont compl`etement r´esolus dans le cas fuchsien. (Notons
par exemple que dans ce cas la q-monodromie locale en 0 ou ∞s’interpr`ete `a
l’aide d’un ﬁbr´e plat sur la courbe elliptique C∗/qZ [Sau02c].) La th´eorie reste
incompl`ete dans le cas irr´egulier.
∗∗∗
Dans la derni`ere partie de cet article, nous changeons de point de vue
et dirigeons notre attention vers des probl`emes de nature arithm´etique.
L’´etude arithm´etique des s´eries solutions d’´equations aux q-diﬀ´erences n’est
pas compl`etement nouvelle ; cependant, nous ne disposons pas d’une th´eorie
syst´ematique. La question a ´et´e soulev´ee r´ecemment par Y. Andr´e dans
[And00a], [And00b], o`u plusieurs questions dans cette direction restent sans
r´eponse. Les r´esultats dont nous parlerons au §5 signiﬁent qu’un analogue na¨ıf
de la th´eorie diﬀ´erentielle ne donne que des objets triviaux. En autres termes,
une th´eorie arithm´etique des ´equations aux q-diﬀ´erence ne peut ˆetre un simple
SMF – Gazette – 96, Avril 2003
24
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
analogue de la th´eorie diﬀ´erentielle. Un objectif serait d’avoir un cadre dans
lequel ´etudier la s´erie de Kontsevitch
+∞

n=0
(1 −q)(1 −q2) . . . (1 −qn)
ou des s´eries provenant du Lost Notebook de Ramanujan, comme
+∞

n=0
qn(n−1)/2
(1 + q) . . . (1 + qn)·
