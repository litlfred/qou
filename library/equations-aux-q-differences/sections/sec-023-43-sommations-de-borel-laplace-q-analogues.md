---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-023-43-sommations-de-borel-laplace-q-analogues
section_title: "Sommations de Borel-Laplace q-analogues"
section_number: 4.3
pages: 22-24
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Rappelons que la transform´ee de Laplace de la fonction ϕ dans la direction
d = R+eiα,d ’ a r g u m e n tα, issue de l’origine dans le plan complexe de la variable
ξ,e s t( s o u sr ´eserve d’existence) Ldϕ(x)=
∫
d e−ξ/x ϕ(ξ) dξ.
La m´ethode classique de sommation de Borel-Laplace est d´ecrite par le dia-
gramme suivant.
ˆf =
∑
n≥1
anxn ˆB−→ ϕ =
∑
n≥1
an
(n − 1)!ξn−1
Lα
−→ fα =
∫∞eiα
0
e−ξ/xϕ (ξ) dξ.(4.9.2)
Elle fonctionne pour la s´erie formelle ˆf si celle-ci est Gevrey 1, ce qui ´equivaut
`a la convergence de ϕ, et si cette derni`ere se prolonge analytiquement le long
de d avec une croissance convenable.
Si l’on appelle transform´ee de q-Laplace de ϕ dans la direction d’argument
α l’int´egrale de (4.6.2), le th´eor`eme 4.7 fait apparaˆıtre la version q-analogue
suivante de la m´ethode de sommation exponentielle de Borel-Laplace (version
continue) :
ˆf =
∑
n≥0
anxn
ˆBq;1
−→ ϕ =
∑
n≥0
anq−n(n−1)/2ξn
Lα
q;1
−→ fα = 1
√
2π log q
∫∞eiα
0
q− 1
2 (logq(ξ/x)+1/2)2
ϕ(ξ) dξ
ξ .(4.9.3)
SMF – Gazette – 96, Avril 2003
42 L. DI VIZIO, J.-P. RAMIS, J. SAULOY, C. ZHANG
De mani`ere analogue, le th´eor`eme 4.9 nous conduit au diagramme suivant :
ˆf =
∑
n≥0
anxn
ˆBq;1
−→ ϕ =
∑
n≥0
anq−n(n−1)/2ξn
L[λ;q]
q;1
−→ f[λ;q] =
∑
ξ∈[λ;q]
ϕ(ξ)
θq(ξ/x),(4.9.4)
qui permet de d´eﬁnir une versionq-analogue discr`ete de la sommation de Borel
Laplace. Dans les diagrammes ci-dessus, la s´erie ϕ doit ˆetre convergente (i.e. ˆf
doit ˆetre q-Gevrey d’ordre 1) et le prolongement analytique de ϕ doit exister
dans la direction d’argument α et admettre `a l’inﬁni au plus une croissance
du type θ|q|(A|ξ|) ou, de fa¸con ´equivalente, du type |ξ|µe
(ln |ξ|)2
2l n |q| :c ’ e s tc eq u e
l’on appelle une croissance q-exponentielle d’ordre un. S’il en est ainsi, on note
f[λ;q] = S[λ;q] ˆf. C’est cette q-somme de ˆf dans la q-direction [λ; q] (que l’on
peut identiﬁer `a un point de la courbe elliptique Eq) que nous privil´egierons.
D´eﬁnition 4.10. Soit U ⊂ C un ouvert non born´ee t ϕ une fonction d´eﬁnie
dans U.S o i tk> 0. On dit que f admet `a l’inﬁni dans U une croissance
q-exponentielle d’ordre k si, pour tout ρ> 0, il existe des constantes C, A> 0
telles que, pour tout ξ ∈ U /integerdivide{0} v´eriﬁant infχ∈C/integerdivideU |1 − χ
ξ |≥ ρ,o na i t|ϕ(ξ)| <
Cθ|q|
1
k
(A|ξ|).
Exemple 4.11.
(1) Avec la formule de Cauchy, on v´eriﬁe qu’une fonction enti`ere∑
n≥0 anxn
est `a croissance q-exponentielle d’ordre un si et seulement si
|an| <C An|q|−n(n−1)/2,
o`u C, A> 0 sont des constantes [Ram92].
(2) En particulier, la fonction ξ ↦→ ∏
n≥0(1 − q−nξ)e s t`ac r o i s s a n c e
q-exponentielle d’ordre un, car son d´ eveloppement de Taylor `a l’origine est∑
n≥0
1
(q−1;q−1)n
q−n(n−1)/2ξn.
Soit maintenant ∆ ∈ C{x}[σq]u no p ´erateur lin´eaire aux q-diﬀ´erences `a
coeﬃcients convergents. Nous supposerons que le polygone de Newton de ∆ n’a
qu’une pente non nulle et que celle-ci vaut 1. Ceci ´equivaut (c’est un exercice
facile `ap a r t i rd e sd ´eﬁnitions du paragraphe 3) `a dire qu’il s’´ecrit :
(4.11.1) ∆ = P(xσq)+ x~∆
o`u ~∆ ∈ C{x}[xσq]. L’´equation P(X)=0p e u ta l o r sˆetre consid´er´ee comme
l’´equation caract´eristique de ∆ pour la pente 1.
On d´emontre [Zha02] que toute solution formelle de ∆ ˆy = c (avec c
convergent) est sommable par la sommation de q-Borel-Laplace discr`ete S[λ,q]
si λ n’est pas dans la q-orbite d’une racine de l’´ equation caract´eristique.
La somme y v´eriﬁe l’´equation ∆y = c. Dans la situation analogue pour un
syst`eme, une solution fondamentale formelle (bien ´ecrite...) ˆF est sommable
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 43
dans les mˆeme conditions. Deux sommes S[λ,q] ˆF et S[µ,q] ˆF se correspondent
par multiplication `a droite par une matrice elliptique Sλ,µ (qui, par analogie
avec le cas diﬀ´erentiel [Ram93] m´erite de s’appeler q-multiplicateur de Stokes).
On notera que les images de λ et µ dans Eq doivent ´eviter un nombre ﬁni de
valeurs.
On peut appliquer ces r´esultats aux s´eries hyperg´eom´etriques conﬂuentes
basiques du type 2Φ0 [Zha02] :
(4.11.2) 2Φ0(a, b; −; q,x )=
def
∑
n≥0
(a; q)n(b; q)n
(q; q)n
qn(n−1)/2(−x)n
Posons a = qα,b = qβ et x = z/(1 − q). La s´erie divergente 2Φ0(a, b; −; q,x )
converge formellement, lorsqueq → 1, vers la s´erie hyperg´eom´etrique conﬂuente
classique 2F0(α, β; −; −z), qui est ´egalement divergente.
Nous avons introduit, dans l’exemple 2.2, la s´erie hyperg´eom´etrique basique
2Φ1(a, b; c; q,x )e ts o n´equation fonctionnelle. Posons z = cx et supposons que
c →∞ dans (2.2.1). On obtient la s´erie divergente2Φ0(a, b; −; q,x )e tl ’ ´equation
(2.2.2) devient
(4.11.3)
{
(c − abqx)σq2 − (1 − (a + b)qx)σq − qx
}
2Φ0(a, b; −; q,x )=0 .
Soit ϕ la transform´ee de q-Borel de 2Φ0(a, b; −; q,x ). On a
(4.11.4) ϕ(ξ)= 2Φ1(a, b;0 ;q, −ξ) ∈ C{ξ}.
La s´erie 2Φ0(a, b; −; q,x ) est sommable par l’op´erateur S[λ,q] si λ ∈ C∗ /integerdivide[−1; q].
En jouant sur des formules de connection et leursq-analogues, on peut mon-
trer que la S[λ,q] somme de la s´erie divergente 2Φ0(a, b; −; q,x ) tend, quand
q tend vers 1 ( x = z/(1 − q)), vers la somme de Borel de la s´erie divergente
2F0(α, β; −; −z) dans la direction passant par λ.O ne nd ´eduit que « le » mul-
tiplicateur de Stokes [Ram93] associ´e`a 2F0(α, β; −; −z)p e u tˆetre interpr´et´e
comme limite du q-multiplicateur de Stokes Sλ,µ associ´e`a 2Φ0(a, b; −; q,x )
pourvu que les nombres complexes λ et µ,n ir ´eels n´egatifs, ni nuls, ne soient
pas sur une mˆeme direction issue de 0.
