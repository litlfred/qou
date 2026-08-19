---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ R´ esum´ e.Nous d´ eﬁnissons la cat´ egorie des motifs de Tate mixte sur l’anneau des S-entiers d’un c"
section_id: sec-068-514-remarque-i-on-a
section_title: "Remarque. (i) On a"
section_number: 5.14
pages: 60-63
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ Résumé.Nous définissons la catégorie des motifs de Tate mixte sur l’anneau des S-entiers d’un corps de nombres, et le grou"
---
{a, e1} = [a, e1] + ∂a(e1) − ∂e1(a) = [ a, e1] − [a, e1] + 0 = 0 :
e1 est dans le centre de ( L
∧
, { , }).
58
(ii) On prendra garde que l’application exponentielle de Li e Vω dans Vω, identiﬁ´ ee par 5.11
et 5.12 ` a une application de L
∧
dans ∏ , n’est pas l’application exponentielle de L
∧
dans
∏ . Il resulte de 5.12.4 que, si µa est la multiplication ` a gauche par a, c’est
exp: Lie Vω → Vω: L
∧
→
∏
⊂ Q ≪ e0, (eζ) ≫:
a ↦− →
∑
(µa + ∂a)n/n! appliqu´ e ` a 1 .
Premiers termes:
a + (a2 + ∂a(a))/2 + (a3 + 2a · ∂a(a) + ∂a(a) · a + ∂2
a(a))/6 + · · ·
Remarque 5.15. Ainsi que la notation le sugg` ere, le groupe Hω (resp. Vω) est la r´ ealisation
ω d’un MT(O[1/N])-sch´ ema en groupe H (resp. V ). On peut d´ eﬁnir H par la propri´ et´ e
que pour tout foncteur ﬁbre F , F (H) est, fonctoriellement en F , le sch´ ema en groupe des
automorphismes de la structure 5.7 correspondante. Il agit sur Q(1), P0,0, et P0,1 et V est
le noyau de l’homomorphisme H → Q(1) donnant l’action de H sur Q(1). Il reste vrai
dans MT( O[1/N]) que P1,0 est un espace principal homog` ene sous V .
Comme en 5.10, le groupe G := π(MT(O[1/N])) s’envoie dans H, et ce morphisme
induit un morphisme
(5.15.1) U → V
de MT( O[1/N])-sch´ emas en groupes. Sa r´ ealisationω est induite par (5.10.3).
5.16. Fixons un plongement σ de k dans C, i.e. un isomorphisme de µN (k) avec µN (C).
Le droit chemin du point base 1 0 de C∗ − µN vers le point base ( −1)1 va par segments
de droite successifs (a) dans l’espace tangent en 0, de 1 ` a ε > 0; (b) de ε ` a 1 − ε dans
C∗ − µN ; (c) de −ε ` a−1 dans l’espace tangent ` a un. Ce droit chemin a une image dch d ans
(P(−1)1,10)σ. Via l’isomorphisme de comparaison comp σ,ω, il correspond ` a un ´ el´ ement de
dch(σ) ∈ (P(−1)1,10)ω ⊗ C =
∏
(C) ⊂ C ≪ e0, (eζ)ζ∈µN (k) ≫ .
59
Les coeﬃcients de dch( σ) sont donn´ es par
coeﬃcient de ex1 . . . exn =(5.16.1)
= int´ egrale it´ er´ ee de 0 ` a 1 de dz
z − σ(x1) · · · dz
z − σ(xn)
=
∫ 1
0
( dz1
z1 − σ(x1)
∫ z1
0
( dz2
z2 − σ(x2) · · ·
∫ zn−1
0
dzn
zn − σ(xn)
)
. . .
)
.
Si xn = 0 ou si x1 = 1, l’int´ egrale diverge et doit ˆ etre r´ egularis´ ee: remplacer les limites
d’int´ egration 0 et 1 parε et 1 − η; l’int´ egrale it´ er´ ee convergente obtenue a pour comporte-
ment asymptotique pour ε, η → 0
Int´ egrale it´ er´ ee = polynˆ ome (logε, log η)
+ O(sup(ε| log ε|A, η| log η|B))
pour A and B convenables, et on prend le terme constant du polynˆ ome.
Les valeurs multizeta et leur analogue cyclotomique appara issent quand dans (5.16.1)
on d´ eveloppedz/z − ζ en s´ erie g´ eom´ etrique:
dz
z − ζ = −ζ −1z
1 − ζ −1z
dz
z = −
∑
n ≥ 1
(ζ −1z)n. dz
z .
Proposition 5.17. (i) Pour ζ1, . . . , ζm dans µN (k) et des entiers s1, . . . , sm ≥ 1, si s1 ⁄= 1,
le coeﬃcient de es1−1
0 eζ1 . . . esm−1
0 eζm dans dch(σ) est
(−1)m ∑
n1>...>nm>0
σ
(
ζ n2−n1
1 ζ n3−n2
2 . . . ζ−nm
m
)
ns1
1 . . . nsm
m
(ii) dch( σ) est caract´ eris´ e par les propri´ et´ es d’ˆ etre un ´ el´ ement groupal (terme constant 1,
et ∆dch( σ) = dch( σ) ⊗ dch(σ)) ayant les coeﬃcients (i) et dont les coeﬃcients de e0 et e1
sont nuls.
Notons τ l’application de Gm dans Hω d´ eﬁnie par les graduations (5.10.2) et ⟨g⟩
l’´ el´ ement deVω(C) correspondant par 5.11 ` a g ∈ ∏ (C).
60
Proposition 5.18. L’´ el´ ement⟨dch(σ)⟩τ (2πi) de Hω(C) transforme les Q-formes (P0,0)ω
et (P1,0)ω de (P0,0)ω ⊗ C et (P1,0)ω ⊗ C en les Q-formes (P0,0)σ et (P1,0)σ.
Preuve. Les ´ el´ ements deπ1(X(C), 10) ont dans ∏ (C) une image rationnelle pour la Q-
forme ( P0,0)σ. Ce π1 contient la monodromie locale en 0 et le chemin allant droit p r` es de
1, tournant autour de 1, et revenant. Images: exp(2 πi e0) et dch( σ)−1 exp(2πi e1)dch(σ).
Ce sont les images de exp( e0) et exp( e1) par ⟨dch(σ)) τ (2πi). La Q-forme ( P0,0)σ est µN -
´ equivariante. Les images des exp(eζ) par ⟨dch(σ)⟩τ (2πi) sont donc elles aussi rationnelles.
La pro-alg` ebre de Lie L
∧
est l’unique Q-forme de L
∧
C pour laquelle les e0 et eζ sont ra-
tionnels, et ∏ est donc l’unique Q-forme du groupe ∏
C pour laquelle exp( e0) et les exp( eζ)
sont rationnels. Transportant par ⟨dch(σ)⟩τ (2πi), on obtient l’assertion pour ( P0,0)ω.
Montrons que la Q-forme ( P1,0)σ de ( P1,0)ω ⊗ C est l’image de la Q-forme ( P1,0)ω
par ⟨dch(σ)⟩τ (2πi). Ces deux Q-formes sont des ( P0,0)σ-torseurs. Il suﬃt donc de montrer
qu’elles admettent un point rationnel commun. L’image dch( σ) de 1 par ⟨dch(σ)⟩τ (2πi)
est en eﬀet dans ( P1,0)ω(Q) car image du droit chemin de 1 0 ` a (−1)1.
