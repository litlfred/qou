---
doc_id: ant-v14-n7-s-p03
doc_title: "Nouvelles cohomologies de Weil en caractéristique positive"
section_id: sec-003-4-action-du-groupe-de-galois-motivique-1784
section_title: "Action du groupe de Galois motivique 1784"
section_number: 4
pages: 1-8
source_pdf: ant-v14-n7-s-p03.pdf
source_sha256: e32fde16c3ce0940
doc_brief: "Nouvelles cohomologies de Weil en caractéristique positive — periods” admitting an explicit description by generators and relations."
---
Bibliographie 1789
1. Introduction
On ﬁxe un corps k de caractéristique p> 0. À un k-schéma de type ﬁni X, on sait associer :
— suivant Berthelot [1986] et moyennant le choix d’un corps valué completˆK de caractéristique nulle
et de corps résiduel k, sa cohomologie rigide H∗
rig(X/ˆK), qui est un ˆK -vectoriel gradué,
— suivant Grothendieck [SGA 5 1977] et moyennant le choix d’un nombre premier𝓁⁄= p et d’une
clôture séparable ksep de k, sa cohomologie𝓁-adique H∗
𝓁(X⊗k ksep), qui est un Q𝓁-vectoriel gradué.
L’auteur a bénéﬁcié du soutien du Fond National Suisse de la Recherche Scientiﬁque (NSF), projet 200020-178729.
MSC2010 : 14F42.
Mots-clefs : cohomologie de Weil, motifs, motifs rigides, groupe de Galois motivique, indépendance de𝓁.
1747
1748 Joseph Ayoub
Les dimensions des H∗
𝓁(X⊗k ksep) sont bornées indépendemment de 𝓁⁄= p. On obtient donc un module
gradué de type ﬁni sur l’anneau Atot= ˆK×∏
𝓁⁄= p Q𝓁 en posant :
H∗
tot(X)= H∗
rig(X/ˆK)×
∏
𝓁⁄= p
H∗
𝓁(X⊗k ksep).
La théorie cohomologique H∗
tot(−) ainsi obtenue est en fait déﬁnie sur le sous-anneau ˆK× Ap⊂ Atot,
avec Ap= Q⊗∏
𝓁⁄= p Z𝓁 l’anneau des « adèles en dehors de p », au sens suivant : le Atot-module gradué
H∗
tot(X) s’obtient naturellement, par extension des scalaires, d’un module gradué sur le sous-anneau
ˆK× Ap⊂ Atot ; voir [Milne et Ramachandran 2004, §2] dans le cas où X est projectif et lisse. Cependant,
on peut s’attendre à ce que la théorie cohomologique H∗
tot(−) soit déﬁnie sur des sous-anneaux de Atot
beaucoup plus petits que ˆK× Ap. En effet, si l’on croit à l’existence de la catégorie abélienne des motifs
sur k, le formalisme tannakien entraîne que H∗
tot(−) peut être déﬁnie, localement pour la topologie fpqc
sur Spec(Atot), sur une extension algébrique de Q. Ceci étant, il est naturel de s’intéresser à des théories
cohomologiques qui sont à coefﬁcients dans des anneaux relativement petits (comparés à ˆK× Ap) et qui
permettent de retrouver les théories cohomologiques classiques par extension des scalaires.
À ce stade, il est utile de préciser ce que l’on entend par « théorie cohomologique ». Dans ce travail on
considère uniquement des théories cohomologiques représentables dans la catégorie trianguléeDA´et(k; Q)
des motifs étales sur k. Ainsi, nous adoptons la déﬁnition suivante (voir aussi [Cisinski et Déglise 2012,
Deﬁnition 2.1.4]).
Déﬁnition 1.1. Soit A une Q-algèbre. Une cohomologie de Weil à coefﬁcients dans A (on dira aussi
déﬁnie sur A) est un préfaisceau de A-dg-algèbres0W sur Sm/k vériﬁant les conditions suivantes.
(1) Le morphisme unité A→0W(X) est un quasi-isomorphisme pour X= Spec(k) et X= A1.
(2) Le complexe de A-modules0W(P1,∞) est quasi-isomorphe à A[−2].
(3) (Formule de Künneth) Pour tout X, Y∈ Sm/k, le morphisme évident
0W(X)
L
⊗A0W(Y)→0W(X×k Y)
est un quasi-isomorphisme.
(4) Le complexe de préfaisceaux 0W est ﬁbrant pour la topologie étale (i.e., admet la descente étale).
Étant donnée une cohomologie de Weil0W , on pose H∗
W(X)= H∗(0W(X)) pour X∈ Sm/k.
Remarque 1.2. Lorsque la Q-algèbre A est un corps, la déﬁnition 1.1 est équivalente à [Cisinski et Déglise
2012, Deﬁnition 2.1.4]. (En effet, une cohomologie de Weil mixte au sens de [loc. cit., Deﬁnition 2.1.4]
satisfait automatiquement la descente étale.) La propriété (3), afﬁrmant que 0W vériﬁe la formule de
Künneth, est la propriété cruciale qui fait la différence entre les cohomologies de Weil et d’autres théories
cohomologiques comme la cohomologie motivique ou celle de Deligne–Beilinson. De plus, d’après les
résultats de [Cisinski et Déglise 2012, §2], la restriction de H∗
W(−) aux k-schémas projectifs lisses est
une cohomologie de Weil au sens classique de [Kleiman 1968, §1.2].
Nouvelles cohomologies de Weil en caractéristique positive 1749
Avant d’énoncer un des résultats obtenus dans cet article, nous introduisons un anneau de « périodes
abstraites p-adiques » du même type que les anneaux de « périodes abstraites complexes » considérés
dans [Ayoub 2014b, Remarque 2.107, Proposition 2.108] et, sous une autre forme, dans [Kontsevich et
Zagier 2001].
Construction 1.3. On ﬁxe un corps valué K de hauteur 1, d’inégales caractéristiques(0, p) et de corps
résiduel k. On note ˆK la complétion de K . Pour m, n∈ N, on considère les ˆK -espaces analytiques rigides :
∂Bm= Spm(ˆK{t1, t−1
1 ,..., tm, t−1
m}) et Bn= Spm(ˆK{z1,..., zn}).
On note Oalg(∂Bm× Bn)⊂ O(∂Bm× Bn) le sous-K -vectoriel formé des éléments algébriques sur le corps
des fractions rationnelles K(t1,..., tm, z1,..., zn). On pose :
Oalg(∂B∞× B∞)=
⋃
m, n∈ N
Oalg(∂Bm× Bn).
On déﬁnit alors le K -module AK comme étant le quotient de Oalg(∂B∞× B∞) par le sous-K -vectoriel
engendré par les éléments de la forme :
ti·∂g
∂ti
, pour g∈ Oalg(∂B∞× B∞) et i> 1,
∂h
∂z j
− h|z j=1+ h|z j=0, pour h∈ Oalg(∂B∞× B∞) et j> 1.
(En égales caractéristiques nulles, les relations ci-dessus ﬁgurent aussi dans [Ayoub 2019, Théorème 1.7].)
La classe de f∈ Oalg(∂B∞× B∞) dans AK sera notée[ f]. Le K -vectoriel AK est naturellement une K -
algèbre commutative : son produit est donné par la formule[ f1]·[ f2]=[ f1· f2] si f1, f2∈ Oalg(∂B∞×B∞)
ne dépendent pas d’une même variable (voir [Ayoub 2014b, Proposition 2.108(b)]). Les éléments de AK
seront appelés des « périodes abstraites p-adiques ». On dispose d’un morphisme de K -algèbres
∫
: AK→ ˆK (1-1)
déﬁni comme suit. Étant donnée f∈ Oalg(∂Bm× Bn), on note cc( f) le coefﬁcient du monôme t0
1··· t0
m
lorsqu’on écrit f comme une série de Laurent à coefﬁcients dans O(Bn), i.e., en considérant f comme
un élément de O(Bn){t1, t−1
1 ,..., tm, t−1
m}. Alors, le morphisme (1-1) envoie[ f] sur l’intégrale multiple
∫ 1
0
···
∫ 1
0
cc( f)· dz1··· dzn (1-2)
qu’on déﬁnit comme étant la somme
∑
(τ1,...,τn)∈{ 0,1}n
(−1)n−τ1−···−τn G(τ1,...,τ n)
avec G∈ O(Bn) telle que
∂nG
∂z1··· ∂zn
= cc( f).
1750 Joseph Ayoub
L’existence d’une telle fonctionG est assurée par le fait que cc( f) est une fonction surconvergente sur
Bn, ce qui est une conséquence du fait que f est algébrique sur K(t1,..., tm, z1,..., zn).
Remarque 1.4. L’expression « période p-adique » ﬁgure déjà en théorie de Hodge p-adique où les
anneaux de Fontaine [1994] sont aussi classiquement appelés des anneaux de périodes p-adiques. Bien
que les anneaux AK introduits ci-dessus n’ont pas grand-chose à voir avec les anneaux de Fontaine, il nous
semble approprié de parler de « périodes abstraites p-adiques » dans la construction 1.3 à cause de la forte
analogie avec le cas complexe, et on espère que le lecteur ne s’en offusquera pas. Il convient cependant
de noter que, contrairement au cas complexe (voir [Ayoub 2014b, Remarque 2.107]), les anneaux AK ne
sont pas des anneaux de fonctions sur un torseur d’isomorphismes entre deux foncteurs ﬁbres.
V oici maintenant un échantillon des résultats obtenus dans cet article.
Théorème 1.5. Gardons les hypothèses et les notations de la construction 1.3. Il existe une cohomologie
de Weil0new(−/K) à coefﬁcients dans la K -algèbre AK vériﬁant les propriétés suivantes.
(A) Il existe un isomorphisme dans la catégorie dérivée des préfaisceaux sur Sm/k :
0new(−/K)
L
⊗AK,
∫ ˆK−→∼ 0rig(−/ˆK)
où0rig(−/ˆK) désigne la cohomologie rigide de Berthelot (voir [Cisinski et Déglise 2012, Proposi-
tion 3.2.9]).
(B) Soit𝓁 un nombre premier différent de p et soit Q𝓁 une clôture algébrique de Q𝓁. Le choix d’un
plongement complexe K ↪→ C et d’un isomorphismeQ𝓁≃ C détermine un morphisme AK→ Q𝓁
ainsi qu’un isomorphisme dans la catégorie dérivée des préfaisceaux surSm/k :
0new(−/K)
L
⊗AK Q𝓁−→∼ 0𝓁(−)⊗Q𝓁 Q𝓁
où0𝓁(−) désigne la cohomologie𝓁-adique.
Remarque 1.6. Le théorème 1.5 fournit un anneau de coefﬁcients commun à toutes les cohomologies
de Weil classiques, à savoir AK , et cet anneau est bien plus petit que ˆK× Ap. Cependant, en dehors du
côté esthétique, l’intérêt du théorème 1.5 dépend beaucoup de ce que l’on sait dire sur la K -algèbre AK .
Malheureusement, à l’heure actuelle, nous n’avons que des conjectures à proposer au lecteur. On conjecture
par exemple que l’anneauAK est intègre (contrairement à ˆK× Ap), mais cette conjecture semble hors de
porté. Une conjecture qui semble encore beaucoup plus lointaine prédit que le morphisme d’intégration
(1-1) est injectif si K est un corps de nombres. Il s’agit là d’une version p-adique de la conjecture
des périodes de Kontsevich et Zagier [2001, §4.1] (voir aussi [Ayoub 2015b, Conjecture 1.1]). Dans la
sous-section 4C, nous proposons une autre conjecture qui concerne l’action naturelle du groupe de Galois
motivique de K sur AK , et nous avons des raisons de penser que cette conjecture est plus accessible que les
deux premières. (Strictement parlant, il s’agit d’une variante de laK -algèbre AK ; voir la conjecture 4.10.)
Nouvelles cohomologies de Weil en caractéristique positive 1751
Dans le reste de l’introduction, nous allons esquisser la construction de la nouvelle cohomologie de
Weil du théorème 1.5. En fait, nous construisons d’abord le pendant « homologique » de 0new(−/K)
sous forme d’un foncteur de réalisation (covariant)
Rnew: DA´et(k; Q)→ D(AK) (1-3)
de la catégorie des motifs étales vers la catégorie dérivée desAK -modules. La propriété cruciale du foncteur
Rnew est le fait qu’il est monoïdal (ce qui correspond à la formule de Künneth dans la déﬁnition 1.1). On
retrouve la cohomologie de Weil0new(−/K) en posant, pour X∈ Sm/k,
0new(X/K)= RHomAK(Rnew(M(X)), AK),
avec M(X)∈ DA´et(k; Q) le motif homologique de X. Autrement dit,0new(X/K) est simplement le dual
de Rnew(M(X)). Ceci est bien raisonnable car Rnew(M(X)) est un complexe parfait de AK -modules, ce
qui découle du fait que R new est monoïdal.
La construction du foncteur (1 -3) passe par la catégorie RigDA´et(ˆK; Q) des motifs étales rigides.
Rappelons que la construction de cette catégorie est calquée sur celle de la catégorie DA´et(k; Q) : il s’agit
de remplacer partout « Sm/k » par « SmRig/ˆK ». On dispose d’un foncteur monoïdal
rel: DA´et(k; Q)→ RigDA´et(ˆK; Q) (1-4)
vériﬁant la propriété suivante : pour tout ˆK◦-schéma formel lisse X, on a un isomorphisme canonique
rel(M(Xσ))≃ M(Xη), où Xσ et Xη désignent respectivement la ﬁbre spéciale et la ﬁbre générique de X.
On dispose aussi d’un foncteur monoïdal
Rig∗: DA´et(K; Q)→ RigDA´et(ˆK; Q) (1-5)
vériﬁant la propriété suivante : pour tout K -schéma lisse X, on a un isomorphisme canonique
Rig∗(M(X))≃ M(X anr),
où X anr désigne la ˆK -variété analytique rigide associée à X⊗K ˆK . En fait, nous utiliserons surtout
l’adjoint à droite
Rig∗: RigDA´et(ˆK; Q)→ DA´et(K; Q) (1-6)
de ce foncteur. Bien entendu, le foncteur Rig∗ n’est pas monoïdal. Cependant, on a le résultat suivant qui
est un ingrédient essentiel dans la construction du foncteur de réalisation (1-3).
Théorème 1.7. L’algèbre commutativeRig∗Q dans DA´et(K; Q) se relève en une algèbre commutative
~Rig∗Q dans la catégorie Spt♯
T
(
Cpl(PSh(Sm/K; Q))
)
et le foncteur Rig∗ s’enrichit en un foncteur
~Rig∗: RigDA´et(ˆK; Q)→ DA´et(K;~Rig∗Q) (1-7)
à valeurs dans la catégorie homotopique des~Rig∗Q-modules. De plus, le foncteur (1-7) est une équivalence
monoïdale.
1752 Joseph Ayoub
L’existence du foncteur~Rig∗ est relativement formelle et n’est guère surprenante. La propriété essentielle
est la monoïdalité (encore une fois !) de ce foncteur. Esquissons l’argument : le foncteur~Rig∗ est pseudo-
monoïdal, i.e., on dispose d’une transformation binaturelle
~Rig∗(M)⊗~Rig∗Q~Rig∗(N)→~Rig∗(M⊗ N), (1-8)
et il s’agit de montrer qu’elle est inversible. Il sufﬁt de vériﬁer cela pour un M et N appartenant à un
ensemble de générateurs de la catégorie triangulée RigDA´et(ˆK; Q). Or, on sait d’après [Ayoub 2015a,
Théorème 2.5.35] que l’image du foncteur Rig∗ engendre RigDA´et(ˆK; Q). On peut donc supposer que
M= Rig∗(M0) et N= Rig∗(N0),
avec M0 et N0 dans DA´et(K; Q). Le résultat recherché découle alors de la formule de coprojection
Rig∗Rig∗(−)≃ Rig∗Q⊗(−) (1-9)
appliquée à M0, N0 et M0⊗ N0. (V oir le lemme 2.29 ci-dessous.)
Vu le théorème 1.7, il est tentant de considérer la composition suivante :
DA´et(k; Q) rel // RigDA´et(ˆK; Q)
~Rig∗ // DA´et(K;~Rig∗Q)
RdR // Ho(Mod(AK)) (1-10)
où RdR désigne la réalisation de de Rham des motifs sur K et AK= RdR(~Rig∗Q) est la dg-algèbre déﬁnie
comme étant la réalisation de de Rham de ~Rig∗Q. Remarquons que tous les foncteurs dans (1 -10) sont
monoïdaux, et il en est donc de même de leur composition. Pour achever la construction du foncteur de
réalisation (1-3), on utilise le résultat suivant.
Théorème 1.8. Le complexe AK est(−1)-connexe (i.e., Hi(AK)= 0 pour i< 0) et la K -algèbre H0(AK)
s’identiﬁe canoniquement àAK .
Rappelons que le foncteur RdR est déﬁni par R0(K;−⊗ ), où  est le T -spectre représentant la
cohomologie de de Rham algébrique et qui est donné en chaque niveau par le complexe de de Rham
usuel. En utilisant la formule de coprojection (1-9), on trouve donc
AK= RdR(Rig∗Q)≃ R0(K; Rig∗Q⊗ )≃ R0(K; Rig∗Rig∗())≃ R0(ˆK; Rig∗()).
Le théorème 1.8 se démontre par un calcul direct du complexe R0(ˆK, Rig∗()). La méthode est la même
que celle utilisée dans [Ayoub 2015b, §3.6] et revisitée dans [Ayoub 2019, §2.4]. Une fois le théorème 1.8
établi, on dispose d’un foncteur monoïdal
AK
L
⊗AK−: Ho(Mod(AK))→ D(AK), (1-11)
et le foncteur de réalisation R new s’obtient alors en composant (1-10) et (1-11).
Nouvelles cohomologies de Weil en caractéristique positive 1753
Conventions et notations courantes.
Schémas et variétés rigides. Sauf mention explicite du contraire, les schémas et les schémas formels sont
supposés quasi-compacts et séparés. Les variétés rigides sont supposées séparées (mais non nécessairement
quasi-compactes). Si S est un schéma (resp. une variété rigide), on noteSm/S (resp. SmRig/S) la catégorie
des S-schémas lisses (resp. des S-variétés rigides lisses). Si S= Spec(A) (resp. S= Spm(A)), cette
catégorie est aussi désignée par Sm/A (resp. SmRig/A).
On note A1 la droite afﬁne et E1= A1 r o la droite afﬁne épointée. Pour n∈ N, on pose An=(A1)×n
et En=(E1)×n, et on note Pn l’espace projectif de dimension n. On note B1 la boule unité de Tate et∂B1
son bord. Pour n∈ N, on pose Bn=(B1)×n et∂Bn=(∂B1)×n.
Anneaux et modules. Sauf mention du contraire, tous les anneaux, algèbres et dg-algèbres sont commutatifs
et unitaires. Si A est une algèbre dans une catégorie monoïdale E, on note Mod(A) la catégorie des
A-modules dans E.
Complexes. Si A est une catégorie additive, on note Cpl(A) la catégorie des complexes dans A. Si A est
abélienne, on note D(A) sa catégorie dérivée. Si3 est un anneau, on note Cpl(3) et D(3) au lieu de
Cpl(Mod(3)) et D(Mod(3)).
Préfaisceaux et faisceaux. Si C est une catégorie essentiellement petite et3 un anneau, on notePSh(C;3)
la catégorie des préfaisceaux sur C à valeurs dans les3-modules. Si M est un3-module, on note Mcst
le préfaisceau constant de valeur M. Siτ est une topologie sur C, on note Shvτ(C;3) la sous-catégorie
pleine de PSh(C;3) formée desτ-faisceaux. On note aτ le foncteur deτ-faisceautisation. La topologie
étale sera désignée par «´et ».
Catégories monoïdales et spectres. Dans cet article, l’expression « catégorie monoïdale » signiﬁe « caté-
gorie monoïdale, symétrique et unitaire ». De même, l’expression « foncteur (pseudo-)monoïdal » signiﬁe
« foncteur (pseudo-)monoïdal, symétrique et (pseudo-)unitaire ».
Si M est une catégorie monoïdale et si T est un objet de M, on dispose de trois catégories deT -spectres,
à savoir SptT(M), Spt6
T(M) et Spt♯
T(M). Les objets de la deuxième et troisième catégories sont qualiﬁés
respectivement de « symétriques » et de « commutatifs ».
Catégories de modèles. Sauf mention explicite du contraire, on considère toujours les structures de
modèles projectives (et non pas injectives) sur les catégories Cpl(PSh(C;3)). On dispose de la structure
de modèles globale pour laquelle les équivalences faibles sont les quasi-isomorphismes et les ﬁbrations
sont les surjections. On dispose également de la structure de modèles τ-locale obtenue par localisation de
Bousﬁeld de la structure précédente et dont les équivalences faibles sont les équivalences τ-locales, i.e.,
celles qui induisent des isomorphismes en homologie après τ-faisceautisation.
Dans ce travail, on utilisera couramment le théorème d’existence de structures de modèles sur les
catégories d’algèbres commutatives de White [2017, Theorem 3.2]. Sauf mention explicite du contraire,
si A est une algèbre commutative dans une catégorie de modèles monoïdale M (vériﬁant certaines
1754 Joseph Ayoub
hypothèses), les remplacements ﬁbrants et coﬁbrants de A sont toujours pris dans la catégorie de modèles
des algèbres commutatives dans M.
Étant donnée une catégorie de modèles M, on note Ho(M) sa catégorie homotopique. Étant donnée
une sous-catégorie pleine N de M, on note Ho(N) la sous-catégorie pleine de Ho(M) ayant les mêmes
objets que N. Lorsque la structure de modèles considérée est obtenue par localisation de Bousﬁeld, nous
utilisons une version décorée pour signaler le passage à la catégorie homotopique : « Hoτ » pour les
structuresτ-locales, « Host » pour les structures stables, « HoA1-´et-st » pour les structures (A1,´et)-locales
stables, etc.
Motifs. Si S est un schéma (resp. une variété rigide), on note DA´et(S;3) (resp. RigDA´et(S;3)) la
catégorie des S-motifs (resp. S-motifs rigides) étales à coefﬁcients dans un anneau 3. C’est une catégorie
monoïdale fermée ; son objet unité est noté 3 ou simplement 1, et son bifoncteur « homomorphismes
internes » est noté Hom(−,−). Si X est un S-schéma lisse (resp. une S-variété rigide lisse), on note
M(X) son S-motif. On écrira souvent « Hom(X,−) » au lieu de « Hom(M(X),−) ». Le foncteur
« sections globales »
R0(S;−): DA´et(S;3)→ D(3)
est déﬁni par R0(S;−)= RHomDA´et(S;3)(3,−) et de même dans le cas respé. Enﬁn, on noteDA´et
ct(S;3)
(resp. RigDA´et
ct(S;3)) la sous-catégorie triangulée des motifs constructibles (i.e., compacts).
