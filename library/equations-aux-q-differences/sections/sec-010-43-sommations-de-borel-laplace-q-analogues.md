---
doc_id: equations-aux-q-differences
doc_title: "Équations aux q-différences"
section_id: sec-010-43-sommations-de-borel-laplace-q-analogues
section_title: "Sommations de Borel-Laplace q-analogues"
section_number: 4.3
pages: 22-25
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
toc_source: inferred
doc_brief: "Équations aux q-différences — 14 sections: Front matter; Introduction; Br´eviaire"
---
Rappelons que la transform´ee de Laplace de la fonction ϕ dans la direction
d = R+eiα, d’argument α, issue de l’origine dans le plan complexe de la variable
ξ, est (sous r´eserve d’existence) Ldϕ(x) =
!
d e−ξ/x ϕ(ξ) dξ.
La m´ethode classique de sommation de Borel-Laplace est d´ecrite par le dia-
gramme suivant.

f =

n≥1
anxn

B
−→
ϕ =

n≥1
an
(n −1)!ξn−1
Lα
−→
f α =
 ∞eiα
0
e−ξ/xϕ (ξ) dξ.
(4.9.2)
Elle fonctionne pour la s´erie formelle 
f si celle-ci est Gevrey 1, ce qui ´equivaut
`a la convergence de ϕ, et si cette derni`ere se prolonge analytiquement le long
de d avec une croissance convenable.
Si l’on appelle transform´ee de q-Laplace de ϕ dans la direction d’argument
α l’int´egrale de (4.6.2), le th´eor`eme 4.7 fait apparaˆıtre la version q-analogue
suivante de la m´ethode de sommation exponentielle de Borel-Laplace (version
continue) :

f =

n≥0
anxn

Bq;1
−→
ϕ =

n≥0
anq−n(n−1)/2ξn
Lα
q;1
−→
f α =
1
√2π log q
 ∞eiα
0
q−1
2 (logq(ξ/x)+1/2)2 ϕ(ξ) dξ
ξ .
(4.9.3)
SMF – Gazette – 96, Avril 2003
42
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
De mani`ere analogue, le th´eor`eme 4.9 nous conduit au diagramme suivant :

f =

n≥0
anxn

Bq;1
−→
ϕ =

n≥0
anq−n(n−1)/2ξn
L[λ;q]
q;1
−→
f [λ;q] =

ξ∈[λ;q]
ϕ(ξ)
θq(ξ/x),
(4.9.4)
qui permet de d´eﬁnir une version q-analogue discr`ete de la sommation de Borel
Laplace. Dans les diagrammes ci-dessus, la s´erie ϕ doit ˆetre convergente (i.e. 
f
doit ˆetre q-Gevrey d’ordre 1) et le prolongement analytique de ϕ doit exister
dans la direction d’argument α et admettre `a l’inﬁni au plus une croissance
du type θ|q|(A|ξ|) ou, de fa¸con ´equivalente, du type |ξ|µe
(ln |ξ|)2
2 ln |q| : c’est ce que
l’on appelle une croissance q-exponentielle d’ordre un. S’il en est ainsi, on note
f [λ;q] = S[λ;q] 
f. C’est cette q-somme de 
f dans la q-direction [λ; q] (que l’on
peut identiﬁer `a un point de la courbe elliptique Eq) que nous privil´egierons.
D´eﬁnition 4.10. Soit U ⊂C un ouvert non born´e et ϕ une fonction d´eﬁnie
dans U. Soit k > 0. On dit que f admet `a l’inﬁni dans U une croissance
q-exponentielle d’ordre k si, pour tout ρ > 0, il existe des constantes C, A > 0
telles que, pour tout ξ ∈U ∖{0} v´eriﬁant infχ∈C∖U |1 −χ
ξ | ≥ρ, on ait |ϕ(ξ)| <
Cθ|q|
1
k (A|ξ|).
Exemple 4.11.
(1) Avec la formule de Cauchy, on v´eriﬁe qu’une fonction enti`ere 
n≥0 anxn
est `a croissance q-exponentielle d’ordre un si et seulement si
|an| < CAn|q|−n(n−1)/2,
o`u C, A > 0 sont des constantes [Ram92].
(2) En particulier, la fonction ξ
→

n≥0(1 −q−nξ) est `a croissance
q-exponentielle d’ordre un, car son d´eveloppement de Taylor `a l’origine est

n≥0
1
(q−1;q−1)n q−n(n−1)/2ξn.
Soit maintenant ∆∈C{x}[σq] un op´erateur lin´eaire aux q-diﬀ´erences `a
coeﬃcients convergents. Nous supposerons que le polygone de Newton de ∆n’a
qu’une pente non nulle et que celle-ci vaut 1. Ceci ´equivaut (c’est un exercice
facile `a partir des d´eﬁnitions du paragraphe 3) `a dire qu’il s’´ecrit :
(4.11.1)
∆= P(xσq) + x
∆
o`u 
∆∈C{x}[xσq]. L’´equation P(X) = 0 peut alors ˆetre consid´er´ee comme
l’´equation caract´eristique de ∆pour la pente 1.
On d´emontre [Zha02] que toute solution formelle de ∆
y = c (avec c
convergent) est sommable par la sommation de q-Borel-Laplace discr`ete S[λ,q]
si λ n’est pas dans la q-orbite d’une racine de l’´equation caract´eristique.
La somme y v´eriﬁe l’´equation ∆y = c. Dans la situation analogue pour un
syst`eme, une solution fondamentale formelle (bien ´ecrite...) 
F est sommable
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES
43
dans les mˆeme conditions. Deux sommes S[λ,q] 
F et S[µ,q] 
F se correspondent
par multiplication `a droite par une matrice elliptique Sλ,µ (qui, par analogie
avec le cas diﬀ´erentiel [Ram93] m´erite de s’appeler q-multiplicateur de Stokes).
On notera que les images de λ et µ dans Eq doivent ´eviter un nombre ﬁni de
valeurs.
On peut appliquer ces r´esultats aux s´eries hyperg´eom´etriques conﬂuentes
basiques du type 2Φ0 [Zha02] :
(4.11.2)
2Φ0(a, b; −; q, x) =
def

n≥0
(a; q)n(b; q)n
(q; q)n
qn(n−1)/2(−x)n
Posons a = qα, b = qβ et x = z/(1 −q). La s´erie divergente 2Φ0(a, b; −; q, x)
converge formellement, lorsque q →1, vers la s´erie hyperg´eom´etrique conﬂuente
classique 2F0(α, β; −; −z), qui est ´egalement divergente.
Nous avons introduit, dans l’exemple 2.2, la s´erie hyperg´eom´etrique basique
2Φ1(a, b; c; q, x) et son ´equation fonctionnelle. Posons z = cx et supposons que
c →∞dans (2.2.1). On obtient la s´erie divergente 2Φ0(a, b; −; q, x) et l’´equation
(2.2.2) devient
(4.11.3)
"
(c −abqx)σq2 −(1 −(a + b)qx)σq −qx
#
2Φ0(a, b; −; q, x) = 0.
Soit ϕ la transform´ee de q-Borel de 2Φ0(a, b; −; q, x). On a
(4.11.4)
ϕ(ξ) = 2Φ1(a, b; 0; q, −ξ) ∈C{ξ}.
La s´erie 2Φ0(a, b; −; q, x) est sommable par l’op´erateur S[λ,q] si λ ∈C∗∖[−1; q].
En jouant sur des formules de connection et leurs q-analogues, on peut mon-
trer que la S[λ,q] somme de la s´erie divergente 2Φ0(a, b; −; q, x) tend, quand
q tend vers 1 (x = z/(1 −q)), vers la somme de Borel de la s´erie divergente
2F0(α, β; −; −z) dans la direction passant par λ. On en d´eduit que « le » mul-
tiplicateur de Stokes [Ram93] associ´e `a 2F0(α, β; −; −z) peut ˆetre interpr´et´e
comme limite du q-multiplicateur de Stokes Sλ,µ associ´e `a 2Φ0(a, b; −; q, x)
pourvu que les nombres complexes λ et µ, ni r´eels n´egatifs, ni nuls, ne soient
pas sur une mˆeme direction issue de 0.
4.4. La s´erie (
n≥0 qn(n−1)/2xn)2 n’est pas sommable d’un seul
niveau !
Posons 
Y = (
n≥0 qn(n−1)/2xn)2 et consid´erons sa transform´ee de q-Borel

Bq;1 
Y . Par un calcul simple, on peut v´eriﬁer la formule suivante : si 
f =

n≥0 anxn et 
g ∈C[[x]], alors

Bq;1( 
f
g) =

n≥0
anq−n(n−1)/2ξn 
Bq;1
g(q−nξ).
Il s’ensuit que, si P(ξ) = 
Bq;1 
Y (ξ)
n≥0(1 −q−nξ), alors P est une fonction
enti`ere telle que
(4.11.5)
P(qm) = (−1)mqm(3m+1)/2(q−1; q−1)m(q−1; q−1)∞.
On en d´eduit que P admet `a l’inﬁni une croissance q-exponentielle d’ordre ≥3.
SMF – Gazette – 96, Avril 2003
44
L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
Remarque 4.12. La transform´ee de q-Borel de (
n≥0 qn(n−1)/2xn)2 repr´esente
une fonction m´eromorphe dans C, `a pˆoles (simples) dans qN et ayant `a l’inﬁni
dans C ∖qN une croissance q-exponentielle d’ordre exactement deux.
Par cons´equent, la s´erie (
y)2 n’est pas q-Borel-Laplace sommable comme 
y
elle-mˆeme. Ce ph´enom`ene est li´e au fait suivant : l’´equation de (
y)2 contient
deux pentes non triviales alors que (4.0.2) n’en a qu’une seule. En eﬀet, avec
l’´equation (4.0.2), on peut ´ecrire σq 
Y – qui n’est autre que (σq
y)2 – en termes
de 
Y et 
y ; cela nous conduit `a l’´equation suivante :
(4.12.1)
∆
Y = 1 + x,
∆= q2x3σ2
q −x(1 + x)σq + 1.
Th´eor`eme 4.13. Dans (4.12.1), on a ∆= (xσq −1)(x2σq −1) et la s´erie 
Y
est (1, 1/2)-sommable par le proc´ed´e suivant :

f =

n≥0
anxn

Bq;1
−→
ϕ =

n≥0
anq−n(n−1)/2ξn
A∗
q;1,1/2
−→
f ∗
1
L∗
q;1/2
−→
f ∗
(1,1/2).
(4.13.1)
Ici, Aq;1,1/2 = Lq
1
2 ;1 = Lq;1/2 et, si l’on suit la m´ethode (4.9.3) (resp. (4.9.4)),
on pose ∗= α (resp. ∗= [λ; q
1
2 ]).
Dans [MZ00] et [RSZ03], on d´emontre que toutes les s´eries enti`eres solutions
formelles d’une ´equation aux q-diﬀ´erences lin´eaire analytique sont multisom-
mables par des proc´ed´es g´en´eralisant celui ´evoqu´e ci-dessus. Ce r´esultat uti-
lise de fa¸con essentielle la factorisation analytique des op´erateurs analytiques
aux q-diﬀ´erences (cf. §3). L’utilisation du proc´ed´e de multisommation bas´e
sur des transformations de Laplace q-analogues discr`etes donne naissance `a un
ph´enom`ene de Stokes q-analogue (par comparaison entre des sommations dans
des q-directions [λ; q] diﬀ´erentes). Comme dans le cas de la sommation simple
d´ecrit ci-dessus, les multiplicateurs de Stokes ne sont plus constants mais `a
coeﬃcients elliptiques, comme ceux de la matrice de Birkhoﬀ(cf. §3). Ces mul-
tiplicateurs de Stokes sont, dans le cas irr´egulier, parmi les « transcendental
invariants » souhait´es par Birkhoﬀ(cf. §1). Inversement on peut reconstituer
un germe d’´equation aux q-diﬀ´erences lin´eaire analytique locale (`a transfor-
mation de jauge pr`es) `a partir des invariants formels et des q-multiplicateurs
de Stokes. C’est la solution du probl`eme de Riemann-Hilbert q-analogue local
dans le cas irr´egulier qui r´epond `a une autre question de Birkhoﬀ(« inverse
Riemann theory for the neighborhood of x = ∞»). Pour passer au cas global
irr´egulier, il suﬃt d’ajouter aux invariants locaux en 0 et ∞une g´en´eralisation
convenable de la matrice de Birkhoﬀ.
