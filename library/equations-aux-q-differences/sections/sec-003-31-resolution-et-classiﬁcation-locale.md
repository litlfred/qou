---
doc_id: equations-aux-q-differences
doc_title: "Équations aux q-différences"
section_id: sec-003-31-resolution-et-classiﬁcation-locale
section_title: "R´esolution et classiﬁcation locale"
section_number: 3.1
pages: 8-12
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
toc_source: inferred
doc_brief: "Équations aux q-différences — 14 sections: Front matter; Introduction; Br´eviaire"
---
3.1. R´esolution et classiﬁcation locale
Les seuls points invariants de l’automorphisme x →qx sur la sph`ere de
Riemann S sont 0 et ∞et ils jouent un rˆole sym´etrique. Nous aborderons donc
l’´etude locale en 0, celle en ∞s’en d´eduisant par le changement de variable
w = 1/x. La plupart des r´esultats locaux gardent un sens (et restent valides)
pour des op´erateurs et des ´equations `a coeﬃcients analytiques.
`A l’op´erateur aux q-diﬀ´erences P ou mieux, `a l’´equation correspondante
P.f(x) = a0(x)f(qnx) + a1(x)f(qn−1x) + · · · + an(x)f(x) = 0,
on peut associer un polygone de Newton en 0, qui est l’enveloppe convexe dans
R2 de
{(i, j) | i = 0, 1, . . . , n, j ⩾v0(ai)}
o`u v0(a) d´esigne la valuation x-adique de a, c’est-`a-dire son ordre d’annulation
en 0. Ce polygone est invariant par ´equivalence locale. On peut ainsi d´eﬁnir
le polygone de Newton d’un syst`eme, ou d’un module aux q-diﬀ´erences, ainsi
que ses pentes : ce sont les pentes des segments ﬁnis qui bordent le convexe
ci-dessus.
On parle de syst`eme ou de module pur lorsqu’il y a une seule pente et
de syst`eme ou de module fuchsien (en 0) lorsqu’elle est de plus nulle. Les
syst`emes fuchsiens sont pr´ecis´ement ceux pour lesquels on peut supposer, `a
´equivalence rationnelle pr`es, que A(0) ∈GLn(C)1. C’est ici l’analogue des
´equations fuchsiennes de la th´eorie diﬀ´erentielle, dont les points singuliers sont
r´eguliers [In56], [Was65] : `a ´equivalence rationnelle pr`es, un syst`eme diﬀ´erentiel
δX = AX suppos´e fuchsien en 0 serait tel que A(0) ∈Mn(C).
La th´eorie des ´equations aux q-diﬀ´erences suit alors assez ﬁd`element la
th´eorie diﬀ´erentielle. En alternant des transformation de jauge constantes, qui
permettent de se ramener au cas o`u A(0) est triangulaire sup´erieure, et des
« transformations de cisaillement » (shearing transformations), c’est-`a-dire de
transformation de jauge de la forme


Ir1
xIr2
Ir3

, o`u r1, r2, r3 ∈N et r1 + r2 + r3 = n,
on obtient un syst`eme non r´esonnant : cela signiﬁe que le quotient de deux
valeurs propres distinctes de A(0) n’est pas une puissance enti`ere de q (la
condition analogue pour un syst`eme diﬀ´erentiel serait que la diﬀ´erence de deux
valeurs propres distinctes ne soit pas un entier).
Dans les deux th´eories, les valeurs propres de A(0) jouent un rˆole sp´ecial
et sont appel´ees exposants du syst`eme. Les exposants (en fait, leurs classes
modulo Z dans le cas diﬀ´erentiel, modulo qZ dans notre cas) sont des invariants
importants. Plus g´en´eralement, on peut attacher `a chaque pente du polygone
de Newton une ´equation caract´eristique : il s’agit d’une ´equation polynomiale
dont les racines sont les exposants attach´es `a cette pente. Elles servent en g´en´eral
1
On peut ´egalement caract´eriser de tels syst`emes par la croissance mod´er´ee de solutions
locales, ou par l’existence, dans le module (M, Φ) associ´e, d’un r´eseau stable par Φ et Φ−1.
SMF – Gazette – 96, Avril 2003
28
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
`a produire des solutions formelles (comme au §4). Sans surprise, dans le cas
fuchsien, ces solutions formelles convergent.
Exemple 3.1.
(1) L’´equation diﬀ´erentielle (1.0.1) est fuchsienne en 0, d’exposant 0 et
l’´equation aux q-diﬀ´erences (1.0.2) est fuchsienne en 0 d’exposant 1 : elles sont
en fait r´eguli`eres en 0. Il en est de mˆeme dans l’exemple 2.1.
(2) Dans l’exemple 2.2, l’´equation diﬀ´erentielle est fuchsienne en 0, d’expo-
sants 0 et 1 −γ et l’´equation aux q-diﬀ´erences est fuchsienne en 0 d’exposants
1 et q/c. On peut de mˆeme (par le changement de variables z = 1/x) constater
qu’elles sont fuchsiennes `a l’inﬁni (exposants respectifs : α, β et a, b).
Lemme 3.2. [Sau00a] Pour un syst`eme fuchsien σqX = AX non r´esonnant,
il existe une unique transformation de jauge formelle tangente `a l’identit´e :
F(x) = In + xF1 + · · · ,
telle que (σqF)−1 AF = A(0). De plus elle est convergente (donc prolongeable
en une matrice m´eromorphe sur C).
Les coeﬃcients de la matrice F(x) sont construits inductivement `a partir
de la relation AF = (σqF)A(0). Il s’ensuit qu’une matrice Y de rang maximal
v´eriﬁe l’´equation σqY = A(0)Y si et seulement si la matrice X = FY est solu-
tion du syst`eme σqX = AX. Ce lemme permet donc de ramener la r´esolution
des syst`emes fuchsiens `a celle des syst`emes `a coeﬃcients constants. En fait,
associ´e aux consid´erations pr´ec´edentes, il permet facilement de d´emontrer que,
comme pour les ´equations diﬀ´erentielles, tout syst`eme fuchsien est localement
´equivalent `a un syst`eme `a coeﬃcients constants.
Nous nous sommes donc ﬁnalement ramen´es `a r´esoudre un syst`eme aux q-
diﬀerences σqX = AX `a coeﬃcients constants, i.e. tel que A ∈GLn(C). Pour
ce faire, ´ecrivons A = DU la d´ecomposition de Dunford multiplicative de A,
autrement dit, D est semi-simple, U est unipotente et elles commutent. Il suﬃt,
pour conclure, de construire deux matrices eq,D et eq,U qui commutent entre
elles et avec D et U et telles que σqeq,D = Deq,D, σqeq,U = Ueq,U : en fait
eq,A = eq,Deq,U est alors une solution de σqX = AX. Le lecteur est invit´e `a
essayer les cas les plus simples dans chaque classe :
(1) Si A = D et n = 1, A est une constante c ∈C∗et l’on veut savoir
r´esoudre l’´equation σqf = cf.
(2) Si A = U est unipotente de rang 2, on peut prendre par exemple :
A =
1
1
0
1

,
et l’on voit qu’il faut savoir r´esoudre l’´equation σqf = f + 1.
Cela peut se faire `a l’aide de la fonction thˆeta de Jacobi :
θq(x) =

n∈Z
q−n(n−1)/2xn.
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
29
La fonction θq est donc holomorphe sur C∗. Elle v´eriﬁe de plus l’´equation
fonctionnelle :
θq(qx) = qxθq(x).
Cette ´equation, qui s’´ecrit σqf = qxf, n’est pas fuchsienne : elle a une seule
pente, qui vaut 1. On peut donc consid´erer θq comme l’un des q-analogues de
l’exponentielle, car celle-ci v´eriﬁe l’´equation diﬀ´erentielle δy = xy qui n’est pas
fuchsienne en 0, o`u elle a pour seule pente 1. L’algorithme est maintenant le
suivant :
(1) Soit D = P diag(c1, · · · , cn)P −1. Pour chaque exposant ci, c’est-`a-dire
chaque valeur propre de A, l’´equation σqf = cif est fuchsienne, d’exposant ci.
Elle admet pour solution non triviale le « q-caract`ere »
eq,ci(x) =
θq(−x)
θq(−c−1
i x).
Son analogue diﬀ´erentiel est la solution xγ de l’´equation diﬀ´erentielle δf = γf
(fuchsienne d’exposant γ) : la diﬀ´erence essentielle ´etant que cette derni`ere
est en g´en´eral ramiﬁ´ee. On obtient une solution de σqX = DX en posant
eq,D = P diag(eq,c1, · · · , eq,cn)P −1. On v´eriﬁe ais´ement que cette matrice ne
d´epend pas du choix de la diagonalisation de D.
(2) Soit U = In + N (donc N est une matrice nilpotente). On pose eq,U =
U lq = exp(lq log(In + N)) (qui est donc un polynˆome en N et en U), o`u lq est
solution de σqf = f + 1. Nous prendrons pour lq le « q-logarithme » :
lq(x) = −xθ′
q(−x)
θq(−x).
Son analogue classique est la solution log x de l’´equation diﬀ´erentielle δf = 1.
Chacune des ´equations σqf −f = 1 et δf = 1 est une variante non homog`ene
d’une ´equation lin´eaire d’ordre 2, fuchsienne, d’exposant double 1 (cas d’une
´equation aux q-diﬀ´erences) ou 0 (cas d’une ´equation diﬀ´erentielle).
Les premiers auteurs (Adams, Birkhoﬀ, Carmichael...) utilisaient d’ailleurs
pour q-caract`eres et q-logarithme des fonctions ramiﬁ´ees et pouvaient r´esoudre
le syst`eme `a coeﬃcients constants σqX = AX en posant X = xlogq A, o`u
logq A est une matrice constante telle que qlogq A = A. Notre matrice eq,A n’est
pas ramiﬁ´ee, mais elle est m´eromorphe sur C∗: c’est cette propri´et´e, et plus
pr´ecis´ement le contrˆole de son lieu singulier, qui nous permettra d’obtenir une
bonne caract´erisation du ph´enom`ene de conﬂuence. Pour conclure, revenons au
cas g´en´eral :
Th´eor`eme 3.3. Tout syst`eme σqX = AX fuchsien en 0 admet une solu-
tion X = Meq,A(0) m´eromorphe sur C∗. En particulier, la matrice M est
m´eromorphe sur C et A(0) est une matrice constante non r´esonnante.
Si de plus le syst`eme σqX = AX est non r´esonnant, il y a un choix canonique
de X caract´eris´e par A(0) = A(0) et M(0) = In.
SMF – Gazette – 96, Avril 2003
30
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Appelons singularit´es de la solution fondamentale X les pˆoles de X et de
ceux de son inverse X−1. En vertu de la formule du triple produit de Jacobi :
θq(x) = (q−1; q−1)∞(−x; q−1)∞(−q−1
x ; q−1)∞,
o`u on a pos´e (a; q−1)∞= 
n⩾0(1 −q−na), tous les z´eros de θq sont des z´eros
simples et sont situ´es sur la spirale discr`ete [−1; q]. On en d´eduit ais´ement les
z´eros et les pˆoles de eq,c ainsi que les pˆoles de lq. Les singularit´es de eq,A(0) s’or-
ganisent en q-spirales discr`etes [c; q] (pour chaque exposant c) plus, si A(0) n’est
pas semi-simple, la q-spirale discr`ete [1; q]. Les singularit´es de M s’organisent
en demi-q-spirales discr`etes aqN caus´ees par les singularit´es de A, en vertu de
l’´equation fonctionnelle
σqM = σq(Meq,A(0)e−1
q,A(0)) = AM

A(0)−1
.
Une solution (matricielle) fondamentale X ayant ainsi ´et´e obtenue, les solu-
tions (vectorielles) m´eromorphes sur C∗sont alors toutes de la forme XV , o`u V
est un vecteur m´eromorphe q-constant, c’est-`a-dire `a coeﬃcients dans M(Eq),
d’apr`es l’exemple 2.1. Il ne serait pas diﬃcile d’exploiter ces solutions locales
pour classiﬁer les syst`emes fuchsiens, mais une description plus intrins`eque est
possible.
Rappelons que, dans le cas des ´equations diﬀ´erentielles, la classiﬁcation lo-
cale des syst`emes fuchsiens en 0 (par exemple) est totalement sp´eciﬁ´ee par la
matrice de monodromie d’une solution fondamentale lors d’un prolongement
analytique le long d’un petit lacet entourant la singularit´e 0. La matrice de
monodromie se calcule d’ailleurs `a partir de A(0). G´en´eriquement (si A(0) est
semi-simple) les exposants forment un syst`eme complet d’invariants locaux.
Dans tous les cas, l’objet g´eom´etrique sous-jacent est le germe (C∗, 0) : ce sont
les repr´esentations de son groupe fondamental qui interviennent.
Pour les q-diﬀ´erences, une telle description g´eom´etrique est encore possible.
Remarquons d’abord que tout syst`eme est localement ´equivalent `a un syst`eme
`a coeﬃcients constants (c’est le contenu du lemme 3.2). Pour une matrice
constante A ∈GLn(C), le syst`eme (2.3.1) peut s’interpr´eter comme d´eﬁnissant
une section ´equivariante du ﬁbr´e vectoriel trivial de rang n sur C∗. Pr´ecis´ement,
en quotientant C∗×Cn par la relation d’´equivalence engendr´ee par les relations
(x, X) ∼(qx, AX), on construit un ﬁbr´e vectoriel holomorphe FA sur la courbe
elliptique Eq.
Th´eor`eme 3.4. On obtient ainsi une bijection entre les classes d’´equivalence
locale de syst`emes rationnels fuchsiens en 0 et les classes d’isomorphie de ﬁbr´es
vectoriels holomorphes plats sur Eq.
Remarque 3.5. La correspondance de Weil [W38] dit que ces derni`eres sont
en bijection avec les classes de repr´esentations du groupe fondamental π1(Eq),
mais il faut prendre garde que l’´equivalence entre repr´esentations consid´er´ee ici
n’est pas la similitude `a coeﬃcients constants. On peut d´emontrer que la bijec-
tion ci-dessus provient en fait d’une ´equivalence entre cat´egories tannakiennes.
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
31
Celle-ci fournit une interpr´etation g´eom´etrique limpide de la th´eorie de Galois
locale des ´equations fuchsiennes, avec une notion de groupo¨ıde de monodromie
et un th´eor`eme de densit´e de type Schlesinger [Sau02c]. Cette interpr´etation
peut d’ailleurs ˆetre poursuivie dans le cas global (cf. infra la remarque 3.9).
