---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ R´ esum´ e.Nous d´ eﬁnissons la cat´ egorie des motifs de Tate mixte sur l’anneau des S-entiers d’un c"
section_id: sec-077-610-preuve-de-68-pour-σ-un-plongement-complexe-d
section_title: "Preuve de 6.8. Pour σ un plongement complexe de k, posons"
section_number: 6.10
pages: 74-84
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ Résumé.Nous définissons la catégorie des motifs de Tate mixte sur l’anneau des S-entiers d’un corps de nombres, et le grou"
---
(6.10.1) dσ :=
∑
ζ
∑
m
σ(ζ −m)
mn Eζ.
Pour n = 1, le coeﬃcient, divergent, de E1 est ` a remplacer par z´ ero.
D’apr` es 6.7.1, il existe aσ dans l’image de ωn(uab) tel que
(6.10.2) dσ ≡ aσ (mod (2 πi)nE).
Cas n = 1. Fixons σ et identiﬁons k ` a son image dans C par σ. En particulier, ´ ecrivonsζ
pour σζ . Avec cette notation, (6.10.1) se r´ ecrit
(dσ)ζ = − log(1 − ζ).
D’apr` es (2.3.1), ωn(uab) est le dual de ON [1/N]∗ ⊗ Q. Si O+
N est la partie r´ eelle de
ON , c’est encore le dual de O+
N [1/N]∗ ⊗ Q. Soit F son image dans E.
Puisque aσ est dans FC, sa partie r´ eelle est dansFR. Prenant la partie r´ eelle de (6.10.2),
on obtient que
−
∑
log |1 − ζ| Eζ
est dans FR.
D’apr` es un th´ eor` eme de Bass (1966) (cf. Washington (1997) 8.9 et 12.18), ON [1/N]∗ ⊗
Q, muni de ζ ↦→1 − ζ (resp. 1 si ζ = 1) est la distribution trou´ ee paire universelle sur
72
µN . Puisque O+
M [1/N]∗ ⊗ Q ∼− →ON [1/N]∗ ⊗ Q, l’application x ↦→log |x| est injective sur
ON [1/N]∗/torsion et il n’y a donc d’autres relations rationnelles ent re les log |1 − ζ| que
celles d´ eduites de (6.8.1) et (6.8.2). L’image F contient donc E+
distr. Puisque E+
distr a le
mˆ eme rang queO∗
N [1/N]∗ ⊗ Q, (i) et (ii) en r´ esultent.
Cas n > 1. Soit F l’image de ωn ∗ (uab) dans E. Prenant, selon la parit´ e de n, la partie
r´ eelle ou la partie imaginaire de (6.10.2), on obtient que p our tout σ
dσ + (−1)n−1 ¯dσ
est dans FC. Il r´ esulte de (6.10.1) et des identit´ es
∑
ζd=η
ζ m =
{ 0 si d ∤ m
dηm/d si d | m
ζ −1 = ¯ζ
que les dσ + (−1)n−1 ¯dσ sont dans ( E+
distr)C.
Lemme 6.11. Le sous-espace W de EC engendr´ e par lesdσ ±(−1)n−1 ¯dσ est de dimension
au moins ´ egale au nombre de caract` eres de (Z/NZ)∗ de parit´ e(−1)n−1.
D´ eduisons 6.8 de 6.11. La borne inf´ erieure 6.11 pour la dimension de W co ¨ ıncide tant
avec la dimension de ω(uab)n (2.3.1) qu’avec la dimension de E+
distr (Kubert (1979) App.).
Puisque W est contenu dans l’image complexiﬁ´ eeFC, W est ´ egal ` a cette image, (6.1.1) est
injectif. De mˆ eme, puisqueS est contenu dans ( E+
distr)C, on a ´ egalit´ e, prouvant 6.8.
Preuve de 6.11. On peut supposer que k = Q(exp(2πi/N)) ⊂ C. On identiﬁe l’ensemble
des plongements complexes de k ` a (Z/N)∗ par ζ ↦→ζ a, et µN ` aZ/N par b ↦→exp(2πi b/N).
Avec ces notations, W est l’image de l’application
F : C(Z/N)∗
→ CZ/N
de matrice
∑
m
exp(−2πi abm)
mn + (−1)n−1 exp(−2πi abm)
mn .
73
Il nous faut minorer le rang de F . Il sera plus commode de consid´ erer l’application trans-
pos´ eetF . Les applications F et tF sont ´ equivariantes, pour les actions ex ↦→e−1
ax et
ex ↦→eax de (Z/N)∗ sur les deux membres, et il suﬃt de v´ eriﬁer que pour tout cara ct` ereχ
de (Z/N)∗ de parit´ e (−1)n−1, la χ-partie de tF est non nulle. Soient M le diviseur de N tel
que χ provienne d’un caract` ere primitif χ0 de ( Z/M)∗, et prolongeant χ0 par 0 sur Z/M.
V´ eriﬁons que l’image partF du vecteur ( χ0(b))b∈Z/N est non nulle. Prenant la composante
a = 1, on se ram` ene ` a v´ eriﬁer que
∑
b,m
exp(2πi bm).χ0(b)
mn ⁄= 0
C’est en eﬀet N/M fois le produit de la somme de Gauß ∑ exp(2πi b)χ0(b) (somme sur
(Z/M)∗) par L(χ0, n).
Remarque 6.12. L’argument utilis´ e pourn > 1, utilisant tous les plongements complexes
et (6.10.2) modulo (2 πi)nE ⊗ R plutˆ ot qu’un seul plongement et (6.10.2) modulo 2 πiE,
s’applique aussi pour n = 1 si N n’a qu’un seul facteur premier. Dans ce cas en eﬀet,
l’application r´ egulateur deO∗
N [1/N] dans Rm, m le nombre de places ` a l’inﬁni, a un noyau
ﬁni et une image discr` ete.
Remarque 6.13. Combinant les r´ esultats de cet article avec ceux de Gonchar ov (2001),
on obtient imm´ ediatement l’analogue motivique de r´ esultats de loc. cit. sur les alg` ebres de
Lie de Galois: remplacer syst´ ematiquement l’alg` ebre de Lie de Galois gℓ
N par Im(Lie Uω →
Lie Vω) (voir 10.5.3) qui est son analogue motivique, et travaille r sur Q plutˆ ot queQℓ.
74
Appendice. Rappels sur les groupes alg´ ebriques unipotent s.
Dans tout cet appendice, nous supposons ˆ etre en caract´ eristique z´ ero.
A.1. En caract´ eristique z´ ero, le th´ eor` eme de Poincar´ e-Birkhoﬀ-Witt peut ˆ etre ´ enonc´ e
comme suit. Pour L une alg` ebre de Lie sur K, soit ϕn: Sym nL → UL le produit sym´ etris´ e,
de la puissance symm´ etriqueni` eme de L dans l’alg` ebre enveloppante de L. Pour x dans L,
il envoie xn ∈ SymnL sur xn ∈ UL. Le morphisme d’espaces vectoriels
(A.1.1) ϕ∗: Sym ∗L → U L
est un isomorphisme de cog` ebres. Il transforme la ﬁltratio n croissante de Sym ∗L par les
⊕
n ≤ p
SymnL en la ﬁltration de UL par les images des ⊕
n ≤ p
⊗nL.
Sous cette forme, le th´ eor` eme est valable dans toute cat´ e gorie tensorielle (de car-
act´ eristique 0) pseudo-ab´ elienne (pour donner un sens ` a Symn) qui admet des sommes
d´ enombrables. Le cas qui nous int´ eresse est celui des espaces vectoriels ﬁltr´ es. Soit L une
alg` ebre de Lie munie d’une ﬁltration d´ ecroissante F . La ﬁltration correspondante de U L
est caract´ eris´ ee par la propri´ et´ e qu’une ﬁltration surun L-module M est compatible ` a
la ﬁltration de L si et seulement si elle l’est ` a celle de U L. La version cat´ egorique de
Poincar´ e-Birkhoﬀ-Witt implique la compatibilit´ e de (A.1.1) aux ﬁltrations.
Une ﬁltration F sur un L-module M est compatible la ﬁltration centrale descendante
Z de L, si et seulement si les F pM sont des sous-modules et que L agit trivialement sur
les Gr p
F M . La ﬁltration de U L induite par le ﬁltration Z de L est donc la ﬁltration par les
puissances de l’id´ eal d’augmentationI. Par compatibilit´ e de (A.1.1) aux ﬁltrations, on a
Corollaire A.2. Si l’alg` ebre de Lie L, de s´ erie centrale descendante Z, est nilpotente de
classe c (Zc+1 = 0), alors, si on identiﬁe Sym∗L et U L par (A.1.1), on a
(A.2.1) I n ⊃ ⊕
p ≥ n
SympL ⊃ I nc
Notons U
∧
L le compl´ et´ eI-adique de U L.
75
Corollaire A.3. Si l’alg` ebre de Lie L est nilpotente, l’isomorphisme (A.1.1) induit par
compl´ etion un isomorphisme d’espace vectoriels
(A.3.1)
∏
n ≥ 0
SymnL → U
∧
L.
L’isomorphisme (A.3.1) est compatible aux topologies des d eux membres. A gauche,
la topologie est la topologie produit (d’espaces discrets) . A droite, celle de limite projective
des (espaces discrets) U L/I n.
A.4. Le foncteur “alg` ebre de Lie” est une ´ equivalence de la cat´egorie des groupes alg´ ebriques
unipotents avec celle des alg` ebres de Lie nilpotentes de di mension ﬁnie. De plus, le fonc-
teur ρ ↦→dρ est une ´ equivalence de la cat´ egorie des repr´ esentationslin´ eaires (de dimension
ﬁnie) de V , suppos´ e unipotent, avec celle des repr´ esentations nilpotentes de son alg` ebre de
Lie v.
On dispose d’une application exponentielle
(A.4.1) exp: v → V
caract´ eris´ ee par la propri´ et´ e que pour toute repr´ esentation lin´ eaireρ de V , on ait
(A.4.2) ρ(exp(x)) = exp( dρ(x)).
C’est un isomorphisme de v, muni de la loi de groupe de Campbell-Hausdorﬀ, avec V .
A.5. Soit V un groupe alg´ ebrique unipotent d’alg` ebre de Liev. L’alg` ebre enveloppanteUv
est l’alg` ebre des op´ erateurs diﬀ´ erentiels surV invariants par translations ` a gauche. Comme
cog` ebre, c’est le dual topologique du compl´ et´ e de l’anneau local de V en 1. L’application
exponentielle (A.4.1) induit un isomorphisme de la cog` ebr e Uv avec la cog` ebre Sym∗v des
op´ erateurs diﬀ´ erentiels en 0 sur l’espace aﬃnev.
Par r´ eduction au cas o` uv est de dimension un, on v´ eriﬁe que cet isomorphisme envoie
xn ∈ Symnv sur xn ∈ Uv. C’est donc l’isomorphisme (A.1.1). Pour l’espace aﬃne v,
l’alg` ebre aﬃne de v est le dual topologique de la cog` ebre compl´ et´ ee∏
n>0
Symnv. Appliquant
A3, on obtient:
76
Proposition A.6. L’alg` ebre aﬃne de V est le dual topologique de la cog` ebre Uv, compl´ et´ ee
pour la topologie I-adique.
Dualement, le dual (muni de la topologie faible) de l’alg` eb re aﬃne de V est U
∧
v. Les
points de V ` a valeurs dans une alg` ebre A (homomorphismes de l’alg` ebre aﬃne dans A)
sont les ´ el´ ements groupauxg de A ˆ⊗U
∧
v: les ´ el´ ements d’augmentation 1 tels que ∆ g =
g ⊗ g. Compatibilit´ es: l’application exponentielle (A.4.1) est l’exponentielle, de A ⊗ g dans
V (A) ⊂ A ˆ⊗U
∧
v. La loi de groupe est le produit dans U
∧
v.
A.7. Un sch´ ema en groupe aﬃne G est la limite projective de ses quotients Gα qui sont
des groupes alg´ ebriques. Il y a lieu de d´ eﬁnir son alg` ebre de Lie Lie( G) comme ´ etant
la pro-alg` ebre de Lie limite projective des Lie( Gα). De fa¸ con ´ equivalente, c’est la limite
projective des Lie( Gα), qui sont de dimension ﬁnie, munie de sa topologie de limite pro-
jective d’espaces discrets. C’est le dual de la limite induc tive colim(Lie( Gα)∨), muni de sa
topologie faible.
A.8. Un sch´ ema en groupe aﬃne G est pro-unipotent s’il est limite projective de groupes
alg´ ebriques unipotents, i.e. si les Gα de A.7 sont unipotents. On d´ eﬁnit l’alg` ebre envelop-
pante compl´ et´ eeU
∧
Lie(G) de Lie( G) par
U
∧
Lie G = lim α U
∧
Lie(Gα) = lim α,n U(Lie(Gα))/I n,
cette limite ´ etant munie de sa topologie de limite projective. Avec ces d´ eﬁnitions, A.6 reste
valable, comme on le v´ eriﬁe par passage aux limites.
A.9. Cas particulier. Soit Lib(( xi)i∈I ) l’alg` ebre de Lie libre sur K engendr´ ee par une
famille ﬁnie de g´ en´ erateursxi. Notons-la simplement Lib. Son alg` ebre enveloppante est
l’alg` ebre associative libre K ⟨(xi)i∈I ⟩.
Soit Lib
∧
le compl´ et´ e de Lib pour la ﬁltration centrale descendante. C’est l’alg` ebre de
Lie du sch´ ema en groupe pro-unipotent
exp(Lib
∧
) = lim exp(Lib /Zn).
77
Son alg` ebre enveloppante compl´ et´ ee est l’alg` ebre des s´ eries formelles associativesK ⟨ ⟨(xi)⟩ ⟩.
Les points de exp(Lib
∧
) ` a valeurs dans une K-alg` ebre A sont les ´ el´ ements groupaux
g de K ⟨ ⟨(xi)⟩ ⟩: terme constant 1 et ∆ g = g ⊗ g, ∆ ´ etant le coproduit K ⟨ ⟨(xi)⟩ ⟩ →
K ⟨ ⟨(xi)⟩ ⟩ˆ⊗K ⟨ ⟨(xi)⟩ ⟩tel que ∆ xi = xi ⊗ 1 + 1 ⊗ xi.
A.10. Soit v l’alg` ebre de Lie d’un groupe alg´ ebrique nilpotentV , et soit D une ﬁltration
d´ ecroissante ﬁnie de l’alg` ebre de Liev, telle que D0(v) = v. On notera encore D la ﬁltration
de V par les sous-groupes d’alg` ebres de Lie les Dpv. Puisque [ Dpv, Dqv] ⊂ Dp+qv, ce sont
des sous-groupes distingu´ es, et pour p ≥ 1, DpV /Dp+1V est ab´ elien.
On notera encore D les ﬁltrations induites sur Uv, U
∧
v et son dual O(V ). La ﬁltration
n ↦→D−nO(V ) de O(V ) est croissante, et D1O(V ) = 0.
Pour v muni du crochet nul, exp( v, crochet 0) est le sch´ ema pro-vectoriel v.
Par A.1, l’application exponentielle exp: v → V respecte les ﬁltrations D des alg` ebres
aﬃnes. Par r´ eduction au cas lin´ eaire, on en d´ eduit que l’alg` ebre aﬃne de V /Dn+1V est la
sous-alg` ebre de O(V ) engendr´ ee parD−nO(V ). En particulier, D0O(V ) est l’alg` ebre aﬃne
de V /D1V .
Si M est une repr´ esentation deV , les conditions suivantes sur une ﬁltration F de M
sont ´ equivalentes:
compatiblit´ e ` aD sur v: Dpv ⊗ F qM → F p+qM ,
compatibilit´ e ` aD sur Uv: DpUv ⊗ F qM → F p+qM ,
compatibilit´ e ` aD sur O(V ): F pM → ∑ D−rO(V ) ⊗ F p+rM
La ﬁltration D de O(V ) est stable par translations ` a gauche et ` a droite. Si P est un
V -torseur, elle fournit encore une ﬁltration D sur l’alg` ebre aﬃne O(P ) de P .
A.11 F onctorialit´ es.(i) Soient v1 une sous-alg` ebre de Lie de v (resp. un quotient)
et V1 le sous-groupe (resp. quotient) correspondant de V . Notons D1 la ﬁltration de v1
induite par (resp. quotient de) la ﬁltration D de v, et les ﬁltrations qui s’en d´ eduisent
sur Sym ∗v1, Uv1, U
∧
v1 et O(V1). La puissance symm´ etrique Symn(v1) est un sous-espace
(resp. quotient) de Sym n(v), et sa ﬁltration D1 est induite par (resp. quotient de) la
ﬁltration D de Sym n(v). Il r´ esulte de A.1 que la mˆ eme assertion vaut pourUv1 et U
∧
v1 et
78
que dualement, la ﬁltration D1 du quotient (resp. sous-espace) O(V1) de O(V ) est quotient
de (resp. induite par) la ﬁltration D de O(V ).
(ii) Supposons que la ﬁltration D de v provienne d’une graduation v = ⊕
n ≥ 0
vn. Cette
graduation se propage ` a Sym ∗(v), Uv, U
∧
v et O(V ). Pour U
∧
v, “graduation” et ` a prendre
au sens de “d´ ecomposition en produit” plutˆ ot que “d´ ecomposition en somme”. La ﬁltration
D de Sym n(v) provient de la graduation de Sym n(v). Par A.1, la mˆ eme assertion vaut
pour Uv, U
∧
v et O(V ).
(iii) Par passage ` a la limite, A.10 et A.11 restent valable d ans le cas pro-unipotent.
A.12 Exemples. (i) Prenons l’alg` ebre de Lie pro-unipotente Lib
∧
de A.9, et la ﬁltration
centrale descendante Z. Elle provient de la graduation pour laquelle les xi sont de degr´ e 1.
Chaque monˆ omem en les xi d´ eﬁnit sur exp(Lib
∧
) ⊂ k ⟨ ⟨(xi⟩ ⟩une fonction cm “coeﬃcient
de m dans g”, et l’alg` ebre aﬃne a pour base les cm. Le produit est le produit de m´ elange.
Le degr´ e decm est l’oppos´ e de celui dem.
(ii) Parmi les g´ en´ erateursxi, distinguons en un, not´ e x0, et posons I = {0} ∐ J. On a
Lib := Lib(( xi)i∈I ) = k.x0 ⋉ Lib((ad x0)n(xj), (n ≥ 0, j ∈ J)).
Soit D la ﬁltration de Lib pour laquelle Dp est, pour p ≥ 1, la s´ erie centrale descendante
du second facteur. La ﬁltration D provient de la graduation pour laquelle x0 est de degr´ e
0 et les xj (j ∈ J) de degr´ e 1. Compl´ etant cette ﬁltration, on obtient une ﬁltration, encore
not´ eeD, de Lib
∧
. La ﬁltration correspondante de l’alg` ebre aﬃne
O(exp(Lib
∧
))
est d´ eduite de la graduation pour laquelle le degr´ e decm est l’oppos´ e du degr´ e du monˆ ome
m en les xj (j ∈ J).
A.13. Soit G un groupe alg´ ebrique produit semi-direct du groupe multip licatif Gm par
un groupe alg´ ebrique unipotentV , d’alg` ebre de Lie v. L’action de Gm sur v gradue cette
alg` ebre de Lie; sur vn, λ ∈ Gm agit par multiplication par λn.
Supposons v ` a degr´ es> 0. Le foncteur ρ ↦→dρ est alors une ´ equivalence de la cat´ egorie
des repr´ esentations lin´ eaires deG avec celle des espaces vectoriels gradu´ es E, muni d’une
79
action compatible aux graduations de l’alg` ebre de Lie v. La graduation de E donne l’action
de Gm et l’action de v, automatiquement nilpotente, donne celle de V .
Notons k(a) l’espace vectoriel k plac´ e en degr´ ea. Pour a < b , une extension de k(a)
par k(b) dans la cat´ egorie des repr´ esentations de G est donn´ ee par un homomorphisme
v → Hom(k(a), k(b)), i.e. par un ´ el´ ement du dual de la partie homog` ene de deg re´ eb − a
de vab := v/[v, v]:
(A.13.1) Ext 1
Rep(G)(k(a), k(b)) = ( vab)b−a
∨
.
A.14. Soit G un sch´ ema en groupes produit semi-direct de Gm par V pro-unipotent.
Ecrivons-le comme limite projective de quotients par des so us-groupes distingu´ es contenus
dans V :
G = Gm ⋉ V = lim Gm ⋉ Vα.
Supposons les alg` ebres de Lie gradu´ ees vα des Vα (A.13) ` a degr´ e> 0. Passant ` a la
limite, on d´ eduit de (A.13.1) que
(A.14.1) Ext 1
Rep(G)(k(a), k(b)) = colim( vab
α )b−a
∨
.
Supposons en outre que pour tout,
dim Ext 1(k(0), k(n)) < ∞.
Les limites projectives (A.14.1) sont alors stationnaires et, puisque si on rel` eve dans les
(vα)n des bases des ( vab
α )n, on obtient un syst` eme g´ en´ erateur de vα, la dimension de
(vα)n est, pour chaque n, born´ ee ind´ ependamment den. On notera vgr l’alg` ebre de Lie
gradu´ ee de composantes homog` enes les limites projectives (stationnaires) des composantes
homog` enes des vα. Passant ` a la limite dans A.13, on obtient:
Proposition A.15. Sous les hypoth` eses de A.14: G = Gm ⋉ V , Lie V ` a degr´ es> 0,
Ext1
Rep(G)(k(0), k(n)) de dimension ﬁnie, le foncteur ρ ↦→dρ est une ´ equivalence de la
cat´ egorie des repr´ esentations deG avec celle des espaces vectoriels gradu´ es munis d’une
action de l’alg` ebre de Lie gradu´ eevgr. On a
Ext1
Rep(G)(k(0), k(n)) = ( vab
gr )
∨
n.
80
Bibliographie
H. Bass. Generators and relations for cyclotomic units , Nagoya Math. J. 27 (1966),
p. 401–407.
A. Beilinson, J. Bernstein, et P. Deligne. Faisceaux pervers, in: Analyse et topologie sur
les espaces singuliers, Ast´ erisque 100, SMF (1982).
S. Bloch. Algebraic cycles and algebraic K-theory, Adv. in Math. 61, 3 (1986), p. 267–304.
. The moving lemma for higher Chow groups , J. Alg. Geom. 3, 3 (1994), p. 537–
568.
K. T. Chen. Iterated integrals of diﬀerential forms and loop space homo logy, Ann. of Math.
97 (1973), p. 217–246.
. Reduced Bar Constructions on de Rham complexes , in: Algebra, Topology and
Category Theory, a collection of papers in honor of Samuel Ei lenberg, p. 19–32, Academic
Press (1976).
P. Deligne. Le groupe fondamental de la droite projective moins trois po ints in: Galois group
over Q, MSRI Publ. 16, p. 79–313, Springer Verlag (1989).
. Cat´ egories tannakiennesin: Grothendieck Festschrift vol. 2, p. 111–195. Progress
in Math. 87, Birkh¨ auser (1990).
M. Demazure et P. Gabriel. Groupes alg´ ebriques, Masson (1970).
A. B. Goncharov. Polylogarithms in arithmetic and geometry , Proc. ICM Zurich 1994,
p. 374–387, Birkhauser.
A. B. Goncharov. The dihedral Lie algebras and Galois symmetries of π1(P1 −{0, ∞} ∪ µN ),
Duke Math. J. 110 3 (2001), p. 397–487.
R. Hain and M. Matsumoto. Weighted completion of Galois groups and Galois actions on
the fundamental group of P1 − {0, 1, ∞}, preprint (2001).
R. Hain and S. Zucker. Unipotent variations of mixed Hodge structure , Inv. Math. 88,
(1987) p. 83–124.
M. Hanamura. Mixed motives and algebraic cycles I. , Math. Res. Lett. 2, 6 (1995), p. 811–
821. See also II, preprint (1996).
A. Huber. Mixed Motives and their Realization in Derived Categories , Lecture Notes in
Math. 1604, Springer Verlag (1995).
. Realization of Voevodsky’s motives, J. Alg. Geom. 9 (2000), p. 755–799.
81
U. Jannsen. Mixed motives and algebraic K-theory, Lecture Notes in Math. 1400, Springer
Verlag (1990).
D. Kubert. The universal ordinary distribution , Bull. SMF 107 (1979), p. 179–202.
M. Levine. Tate motives and the vanishing conjectures for algebraic K-theory, in: Algebraic
K-theory and algebraic topology (Lake Louise, 1991), p. 167– 188. NATO Adv. Sci. but.
Ser. C Math. Phys. 407, Kluwer (1993).
. Bloch’s higher Chow groups revisited, in: K-theory (Strasbourg 1992), p. 235–320,
Ast´ erisque 226, SMF (1994).
. Mixed Motives , Math. Surveys and Monographs 57, AMS (1998).
Chr. Reutenauer. Free Lie algebras, LMS monographs new ser. 7, Oxford University Press
(1993).
T. Terasoma. Multiple zeta values and mixed Tate motives .
