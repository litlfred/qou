---
doc_id: equations-aux-q-differences
doc_title: "Équations aux q-différences"
section_id: sec-011-5-equations-aux-q-diﬀerences-arithmetiques
section_title: "´Equations aux q-diﬀ´erences arithm´etiques"
section_number: 5
pages: 25-28
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
toc_source: inferred
doc_brief: "Équations aux q-différences — 14 sections: Front matter; Introduction; Br´eviaire"
---
L’´etude des ´equations aux q-diﬀ´erences complexes a d´ej`a port´e ses fruits,
mˆeme si beaucoup reste `a faire. Lorsque l’on pense aux d´eveloppements r´ecents
de la th´eorie p-adique et arithm´etique des ´equations diﬀ´erentielles, il est clair
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
45
que, relativement aux ´equations aux q-diﬀ´erences, ces points de vue sont moins
avanc´es.
La litt´erature sur les ´equations aux q-diﬀ´erences p-adiques est assez pauvre.
Lorsque |q|̸ = 1 les r´esultats existants (cf. les th´eor`emes d’indice dans [BB92]
et la construction des solutions canoniques dans [Sau00b]) indiquent que la
th´eorie est plutˆot semblable `a la th´eorie complexe. La grande diﬀ´erence avec
le cas complexe est que, en vue de l’´etude de la conﬂuence, on est oblig´e de
traiter le cas |q| = 1 : en eﬀet dans un corps ultram´etrique la norme de q est 1
lorsque q est proche de 1. Le travail ne fait que commencer mais il est clair que
la th´eorie p-adique des ´equations aux q-diﬀ´erences avec |q| = 1 est une parfaite
d´eformation de la th´eorie des ´equations diﬀ´erentielles p-adiques, ce qui laisse
entrevoir d’int´eressantes implications g´eom´etriques [And02c].
Ici, nous parlerons plutˆot du point de vue arithm´etique et en particulier du
probl`eme « schwarzien » de la recherche des solutions alg´ebriques d’´equations
fonctionnelles lin´eaires. Dans ce contexte on obtient plutˆot des r´esultats de
rationalit´e. En particulier, pour les ´equations hyperg´eom´etriques, on d´emontre :
Th´eor`eme 5.1. ([Gou36], Ch. III, et [DV02a], Appendix) Soit q ∈C∗
un nombre complexe non racine de l’unit´e. Les assertions suivantes sont
´equivalentes :
(1) L’´equation hyperg´eom´etrique basique (2.2.2) de param`etres a, b, c admet
une base de solutions dans C(x).
(2) Il existe α, β, γ ∈Z tels que a = qα, b = qβ et c = qγ et l’´equation
hyperg´eom´etrique classique (2.2.4) de param`etres α, β, γ admet une base de
solutions dans C(x).
(3) Il existe α, β, γ ∈Z tels que a = qα, b = qβ et c = qγ et |1−γ|, |γ−α−β|
et |α −β| sont les longueurs des cˆot´es d’un triangle.
Dans la suite q est un nombre alg´ebrique non nul et il n’est pas une racine
de l’unit´e : `a notre connaissance, ce choix de q est d´eterminant pour tous les
r´esultats qui se situent autour des probl`emes d’alg´ebricit´e et rationalit´e li´es
aux ´equations aux q-diﬀ´erences. En eﬀet, cela implique qu’il existe une norme
(archim´edienne ou ultram´etrique) telle que |q|̸ = 1 et permet d’utiliser les fortes
propri´et´es des ´equations aux q-diﬀ´erences, que nous avons vues plus haut. C’est,
par exemple, le cas du th´eor`eme de B´ezivin et Boutabaa :
Th´eor`eme 5.2. ([BB92]) Soit y(x) une s´erie formelle `a coeﬃcients dans
la clˆoture alg´ebrique Q de Q, solution d’un syst`eme d’equations L1y(x) =
L2y(x) = 0, tel que Liy(x) = 0, pour i = 1, 2, est une ´equation aux qi-
diﬀ´erences lin´eaire `a coeﬃcients dans Q(x), avec q1, q2 ∈Q multiplicativement
ind´ependants3. Alors y(x) est la s´erie de Taylor d’une fonction rationnelle.
Dans [B´ez91] B´ezivin conjecture un ´enonc´e pour les ´equations aux q-
diﬀ´erences dans le sillage de la c´el`ebre conjecture de Grothendieck sur
l’alg´ebricit´e des solutions des ´equations diﬀ´erentielles :
3
Cela signiﬁe que pour tous m1, m2 ∈Z tels que qm1
1
= qm2
2
on a m1 = m2 = 0, ce qui
´equivaut `a : qZ
1 ∩qZ
2 = 1 et q1, q2 non racines de l’unit´e.
SMF – Gazette – 96, Avril 2003
46
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Conjecture 5.3. (Grothendieck) L’´equation diﬀ´erentielle
aµ(x)dµy
dxµ (x) + aµ−1(x)dµ−1y
dxµ−1 (x) + · · · + a0(x)y(x) = 0,
avec ai(x) ∈Q(x), admet un syst`eme complet des solutions alg´ebriques, i.e.
dans la clˆoture alg´ebrique de Q(x), si et seulement si sa r´eduction modulo p
admet un syst`eme complet de solutions dans Fp(x), pour presque tout p.
La conjecture peut ˆetre reformul´ee de plusieurs fa¸cons, en apparence plus
g´en´erales que l’´enonc´e 5.3, mais toutes ´equivalentes entre elles. En particulier
elle est ´equivalente `a une caract´erisation arithm´etique de l’alg`ebre de Lie du
groupe de Galois g´en´erique, conjectur´ee par N. Katz [Kat82]. De nombreux
travaux sont consacr´es `a la conjecture de Grothendieck (cf. par exemple les
travaux de T. Honda, D.V. et G.V. Chudnovsky, N. Katz, Y. Andr´e, J.-B.
Bost), mais elle n’a ´et´e prouv´ee que dans des cas particuliers. Pour les ´equations
aux q-diﬀ´erences le probl`eme est plus simple et nous disposons d’un th´eor`eme
qui peut ˆetre consid´er´e comme un q-analogue de (5.3).
Consid´erons un nombre rationnel q̸ = 0, 1, −1 et une ´equation aux q-
diﬀ´erences
Ly = aµ(x)y(qµx) + aµ−1(x)y(qµ−1x) + · · · + a0(x)y(x) = 0, a0(x)aµ(x)̸ = 0,
`a coeﬃcients ai(x) dans Q(x)4. Pour presque tout nombre premier p, la
r´eduction q de q modulo p est diﬀ´erente de z´ero et engendre un sous-groupe
cyclique de Fp d’ordre κp. Pour presque tout p, il existe donc un entier
positif maximal ℓp et deux entiers g, h tels que 1 −qκp = pℓp g
h et que p̸ | gh,
et on peut consid´erer la r´eduction Lpy = 0 de Ly = 0 modulo pℓp. Soit
A = Z
$
x,
1
P (qix), i ⩾1
%
, avec P(x) ∈Z[x], une sous-Z-alg`ebre de Q(x), telle
que ai(x) ∈A pour tout i = 0, . . . , µ. Le r´esultat est le suivant :
Th´eor`eme 5.4. [DV02a] L’´equation aux q-diﬀ´erences Ly = 0 admet un
syst`eme complet de solutions dans Q(x) si et seulement si, pour presque tout
nombre premier p, l’´equation Lpy = 0 admet un syst`eme complet de solutions
dans A ⊗Z Z/pℓpZ.
Le th´eor`eme 5.4 r´epond partiellement `a la conjecture de B´ezivin, qui pr´edit
le mˆeme type de r´esultat en consid´erant la r´eduction modulo p `a la place de la
r´eduction modulo pℓp.
Les techniques employ´ees dans la preuve du th´eor`eme 5.4 sont emprunt´ees
`a la th´eorie des G-fonctions (cf. [And89] et [DGS94]). Le fait que l’on puisse
prouver un tel ´enonc´e dans le cas des q-diﬀ´erences, alors que le cas diﬀ´erentiel
est ouvert, tient encore une fois aux ´etonnantes propri´et´es des ´equations aux
q-diﬀ´erences lorsque |q|̸ = 1 et au fait que q est un nombre rationnel non racine
de l’unit´e : en eﬀet, il existe toujours une norme sur Q telle que |q|̸ = 1 et l’on
4
Pour simpliﬁer les notations (mais cela ne simpliﬁe pas les d´emonstrations !) nous ne
consid´ererons que des ´equations aux q-diﬀ´erences `a coeﬃcients dans Q(x). En fait, les ´enonc´es
qui suivent sont prouv´es dans [DV02a] pour des ´equations aux q-diﬀ´erences d´eﬁnies sur Q(x).
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
47
peut alors construire une solution ayant un rayon de m´eromorphie inﬁni pour
cette norme.
Comme indiqu´e au §2, nous pouvons consid´erer un module aux q-diﬀ´erences
M = (M, Φ) sur Q(x). Pour un choix convenable du polynˆome P(x), il existe
un r´eseau 
M de M d´eﬁni sur l’alg`ebre A, stable par Φ. Le th´eor`eme 5.4 est
´equivalent `a l’´enonc´e suivant :
Th´eor`eme 5.5. Le module aux q-diﬀ´erences M = (M, Φ) est banal si et seule-
ment si pour presque tout nombre premier p l’op´erateur Φκp induit l’identit´e
sur 
M ⊗Z Z/pℓpZ.
Comme dans la th´eorie diﬀ´erentielle, nous pouvons attacher au module aux
q-diﬀ´erences M un sous-groupe alg´ebrique Gal(M) de GL(M), qu’on appelle
groupe de Galois (g´en´erique). Il s’agit du stabilisateur dans GL(M) des mo-
dules aux q-diﬀ´erences qui sont sous-quotients de sommes ﬁnies de la forme
⊕i,j(M ⊗i ⊗Q(x) (M ∗)⊗j), o`u M ∗est le dual de M, munis de l’op´erateur induit
par Φ. Le choix du r´eseau 
M permet d´eﬁnir la r´eduction modulo pℓp de Gal(M)
et de donner encore un autre ´enonc´e ´equivalent `a 5.4 :
Th´eor`eme 5.6. Le groupe alg´ebrique Gal(M) est le plus petit sous-groupe
alg´ebrique de GL(M), dont la r´eduction modulo pℓp contient la r´eduction de
Φκp modulo pℓp pour presque tout p.
La nature multiplicative de l’op´erateur Φ permet parfois de calculer tous
les op´erateurs Φn et, donc, de d´eterminer par voie arithm´etique le groupe de
Galois g´en´erique.
