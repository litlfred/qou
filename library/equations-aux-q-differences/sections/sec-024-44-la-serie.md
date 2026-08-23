---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-024-44-la-serie
section_title: "La s´erie (∑"
section_number: 4.4
pages: 24-26
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
n≥0 qn(n−1)/2xn)2 n ’est pas sommable d’un seul
niveau !
Posons ˆY =( ∑
n≥0 qn(n−1)/2xn)2 et consid´erons sa transform´ee de q-Borel
ˆBq;1ˆY . Par un calcul simple, on peut v´ eriﬁer la formule suivante : si ˆf =∑
n≥0 anxn et ˆg ∈ C[[x]], alors
ˆBq;1(ˆfˆg)=
∑
n≥0
anq−n(n−1)/2ξn ˆBq;1ˆg(q−nξ).
Il s’ensuit que, si P(ξ)= ˆBq;1ˆY (ξ)∏
n≥0(1 − q−nξ), alors P est une fonction
enti`ere telle que
(4.11.5) P(qm)=( −1)mqm(3m+1)/2(q−1; q−1)m(q−1; q−1)∞.
On en d´eduit que P admet `a l’inﬁni une croissanceq-exponentielle d’ordre ≥ 3.
SMF – Gazette – 96, Avril 2003
44 L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Remarque 4.12. La transform´ee de q-Borel de (∑
n≥0 qn(n−1)/2xn)2 repr´esente
une fonction m´eromorphe dans C,`ap ˆoles (simples) dans qN et ayant `a l’inﬁni
dans C/integerdivideqN une croissance q-exponentielle d’ordre exactement deux.
Par cons´equent, la s´erie (ˆy)2 n’est pas q-Borel-Laplace sommable comme ˆy
elle-mˆeme. Ce ph´enom`ene est li´ea uf a i ts u i v a n t:l ’ ´equation de (ˆy)2 contient
deux pentes non triviales alors que (4.0.2) n’en a qu’une seule. En eﬀet, avec
l’´equation (4.0.2), on peut ´ecrire σq ˆY – qui n’est autre que (σqˆy)2 –e nt e r m e s
de ˆY et ˆy ; cela nous conduit `al ’ ´equation suivante :
(4.12.1) ∆ ˆY =1+ x, ∆= q2x3σ2
q − x(1 +x)σq +1 .
Th´eor`eme 4.13. Dans (4.12.1), on a ∆=( xσq − 1)(x2σq − 1) et la s´erie ˆY
est (1, 1/2)-sommable par le proc´ed´es u i v a n t:
ˆf =
∑
n≥0
anxn
ˆBq;1
−→ ϕ =
∑
n≥0
anq−n(n−1)/2ξn
A∗
q;1,1/2
−→ f ∗
1
L∗
q;1/2
−→ f ∗
(1,1/2).(4.13.1)
Ici, Aq;1,1/2 = Lq
1
2 ;1 = Lq;1/2 et, si l’on suit la m´ethode (4.9.3) (resp. (4.9.4)),
on pose ∗ = α (resp. ∗ =[ λ; q
1
2 ]).
Dans [MZ00] et [RSZ03], on d´emontre que toutes les s´eries enti`eres solutions
formelles d’une ´equation aux q-diﬀ´erences lin´eaire analytique sont multisom-
mables par des proc´ed´es g´en´eralisant celui ´evoqu´e ci-dessus. Ce r´esultat uti-
lise de fa¸con essentielle la factorisation analytique des op´erateurs analytiques
aux q-diﬀ´erences (cf. §3). L’utilisation du proc´ed´e de multisommation bas´e
sur des transformations de Laplace q-analogues discr`etes donne naissance `au n
ph´enom`ene de Stokes q-analogue (par comparaison entre des sommations dans
des q-directions [λ; q]d i ﬀ ´erentes). Comme dans le cas de la sommation simple
d´ecrit ci-dessus, les multiplicateurs de Stokes ne sont plus constants mais ` a
coeﬃcients elliptiques, comme ceux de la matrice de Birkhoﬀ (cf.§3). Ces mul-
tiplicateurs de Stokes sont, dans le cas irr´egulier, parmi les « transcendental
invariants » souhait´es par Birkhoﬀ (cf. §1). Inversement on peut reconstituer
un germe d’´equation aux q-diﬀ´erences lin´eaire analytique locale (`a transfor-
mation de jauge pr`es) `a partir des invariants formels et des q-multiplicateurs
de Stokes. C’est la solution du probl`eme de Riemann-Hilbert q-analogue local
dans le cas irr´egulier qui r´epond `a une autre question de Birkhoﬀ ( « inverse
Riemann theory for the neighborhood of x = ∞ »). Pour passer au cas global
irr´egulier, il suﬃt d’ajouter aux invariants locaux en 0 et∞ une g´en´eralisation
convenable de la matrice de Birkhoﬀ.
5. ´Equations aux q-diﬀ´erences arithm´etiques
L’´etude des ´equations aux q-diﬀ´erences complexes a d´ej`ap o r t ´es e sf r u i t s ,
mˆeme si beaucoup reste `a faire. Lorsque l’on pense aux d´eveloppements r´ecents
de la th´eorie p-adique et arithm´etique des ´equations diﬀ´erentielles, il est clair
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 45
que, relativement aux ´equations aux q-diﬀ´erences, ces points de vue sont moins
avanc´es.
La litt´erature sur les ´equations aux q-diﬀ´erences p-adiques est assez pauvre.
Lorsque |q| ⁄=1l e sr ´esultats existants (cf. les th´eor`emes d’indice dans [BB92]
et la construction des solutions canoniques dans [Sau00b]) indiquent que la
th´eorie est plutˆot semblable `al at h ´eorie complexe. La grande diﬀ´erence avec
le cas complexe est que, en vue de l’´etude de la conﬂuence, on est oblig´ed e
traiter le cas |q| = 1 : en eﬀet dans un corps ultram´etrique la norme de q est 1
lorsque q est proche de 1. Le travail ne fait que commencer mais il est clair que
la th´eorie p-adique des ´equations aux q-diﬀ´erences avec |q| = 1 est une parfaite
d´eformation de la th´eorie des ´equations diﬀ´erentielles p-adiques, ce qui laisse
entrevoir d’int´eressantes implications g´eom´etriques [And02c].
Ici, nous parlerons plutˆot du point de vue arithm´etique et en particulier du
probl`eme « schwarzien » de la recherche des solutions alg´ebriques d’´equations
fonctionnelles lin´eaires. Dans ce contexte on obtient plutˆ ot des r´esultats de
rationalit´e. En particulier, pour les ´equations hyperg´eom´etriques, on d´emontre :
Th´eor`eme 5.1. ([Gou36], Ch. III, et [DV02a], Appendix) Soit q ∈ C∗
un nombre complexe non racine de l’unit´ e. Les assertions suivantes sont
´equivalentes :
(1) L’´equation hyperg´eom´etrique basique (2.2.2) de param`etres a, b, cadmet
une base de solutions dans C(x).
(2) Il existe α, β, γ ∈ Z tels que a = qα, b = qβ et c = qγ et l’´equation
hyperg´eom´etrique classique (2.2.4) de param`etres α, β, γ admet une base de
solutions dans C(x).
(3) Il existe α, β, γ∈ Z tels que a = qα, b = qβ et c = qγ et |1−γ|, |γ −α−β|
et |α − β| sont les longueurs des cˆot´es d’un triangle.
Dans la suite q est un nombre alg´ebrique non nul et il n’est pas une racine
de l’unit´e:` a notre connaissance, ce choix de q est d´eterminant pour tous les
r´esultats qui se situent autour des probl`emes d’alg´ebricit´e et rationalit´el i ´es
aux ´equations aux q-diﬀ´erences. En eﬀet, cela implique qu’il existe une norme
(archim´edienne ou ultram´etrique) telle que|q| ⁄= 1 et permet d’utiliser les fortes
propri´et´es des ´equations auxq-diﬀ´erences, que nous avons vues plus haut. C’est,
par exemple, le cas du th´eor`eme de B´ezivin et Boutabaa :
Th´eor`eme 5.2. ([BB92]) Soit y(x) une s´erie formelle `a coeﬃcients dans
la clˆoture alg´ebrique
 Q de Q, solution d’un syst`eme d’equations L1y(x)=
L2y(x)=0 , tel que Liy(x)=0 ,p o u ri =1 , 2,e s tu n e´equation aux qi-
diﬀ´erences lin´eaire `a coeﬃcients dans
 Q(x),a v e cq1,q2 ∈
 Q multiplicativement
ind´ependants3.A l o r sy(x) est la s´erie de Taylor d’une fonction rationnelle.
Dans [B´ez91] B´ezivin conjecture un ´ enonc´ep o u rl e s´equations aux q-
diﬀ´erences dans le sillage de la c´ el`ebre conjecture de Grothendieck sur
l’alg´ebricit´e des solutions des ´equations diﬀ´erentielles :
