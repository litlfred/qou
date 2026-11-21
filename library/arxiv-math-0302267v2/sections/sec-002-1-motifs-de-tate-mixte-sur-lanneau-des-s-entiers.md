---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-002-1-motifs-de-tate-mixte-sur-lanneau-des-s-entiers
section_title: "Motifs de Tate mixte sur l’anneau des S-entiers de k"
section_number: 1
pages: 5-15
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
toc_source: inferred
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
1.1. Soit k un corps. Nombre de r´esultats cit´es d´ependant de la r´esolution des singularit´es,
nous supposons k de caract´eristique 0. Hanamura (1995), Levine (1998) et Voevodsky
(2000) ont chacun d´eﬁni une cat´egorie triangul´ee de motifs sur k, et Levine (1998) VI 2.5.5
construit une ´equivalence entre sa cat´egorie triangul´ee et celle de Voevodsky. Cette derni`ere
sera pour nous la plus commode. Nous la noterons DM(k) et noterons DM(k)Q celle qui s’en
d´eduit par tensorisation avec Q. On dispose dans DM(k) d’objets de Tate Z(n) (n ∈Z),
dont les images dans DM(k)Q seront not´ees Q(n). Seule nous importera la sous-cat´egorie
triangul´ee DMT(k)Q de DM(k)Q engendr´ee par les Q(n): celle des “extensions it´er´ees”
de Q(n)[m]. Rappelons que E est extension de B par A s’il existe un triangle distingu´e
A →E →B →A[1].
On dispose dans DM(k) d’un produit tensoriel associatif et commutatif `a unit´e ⊗,
compatible `a la structure triangul´ee. L’automorphisme de sym´etrie de Z(1) ⊗Z(1) est
l’identit´e (Voevodsky (2000) 2.1.5), M 7→M(1) := M ⊗Z(1) est une ´equivalence (loc.
cit. 4.1.3), et Z(n) est Z(1)⊗n (n ∈Z). Le produit tensoriel ⊗est rigide (loc. cit. 4.3.7):
existence pour tout objet M d’un dual M ∗muni de ev: M ∗⊗M →Z(0) et δ: Z(0) →
M ⊗M ∗tels que les compos´es M →M ⊗M ∗⊗M →M et M ∗→M ∗⊗M ⊗M ∗→M ∗
soient l’identit´e.
Rappelons, d’apr`es Levine (1993), comment, lorsque la conjecture d’annulation de
Beilinson Soul´e est v´eriﬁ´ee pour k, on peut extraire de DMT(k)Q une cat´egorie tannakienne
MT(k) qui m´erite le nom de cat´egorie des motifs de Tate mixte sur k.
Ecrivons Homj(M, N) pour Hom(M, N[j]). Les Hom∗(Z(a), Z(b)) ne d´ependant que
de i = b−a. Ils sont donn´es par les groupes de Chow sup´erieurs convenablement num´erot´es
de Spec(k) (loc. cit. 4.2.9 pour X = Spec(k)). Pour i < 0 ils sont nuls. Pour i = 0,
Homj(Z(0), Z(0))
= Z
si j = 0,
0
sinon.
(1.1.1)
Pour i = 1,
Homj(Z(0), Z(1))
= k∗
si j = 1,
0
sinon.
(1.1.2)
3
Apr`es tensorisation avec Q, ces groupes sont encore donn´ees par les sous-espaces pro-
pres des op´erations d’Adams dans les groupes de K-th´eorie de k (Levine (1998) II 3.6.6;
r´ef´erence originale: Bloch (1986) compl´et´e par Bloch (1994); voir aussi Levine (1994)). La
conjecture d’annulation de Beilinson-Soul´e est que
(1.1.3)
Homj(Q(0), Q(i)) = 0
pour
i > 0
et
j ≤0.
Lorsque tel est le cas, Beilinson Bernstein Deligne (1982) 1.3.14, appliqu´e `a la sous-cat´egorie
pleine de DMT(k)Q d’objets les Q(n), montre que les extensions it´er´ees de Q(n) (n ∈Z)
forment une cat´egorie ab´elienne, coeur d’une t-structure sur DMT(k)Q. On l’appelle la
cat´egorie MT(k) des motifs de Tate mixte sur k. Elle est stable par produit tensoriel et
passage au dual. Ces foncteurs ´etant exacts, cela r´esulte de ce que Q(n)⊗Q(m) = Q(n+m)
et que Q(n)∗= Q(−n). On obtient ainsi sur MT(k) un produit tensoriel exact en chaque
variable, associatif, commutatif, `a unit´e et rigide.
De ce que MT(k) est le coeur d’une t-structure sur DMT(k)Q r´esulte que pour A et
B dans MT(k), on a
Ext1(A, B) = Hom1(A, B)
et
(1.1.4)
Ext2(A, B)֒ →Hom2(A, B).
(1.1.5)
En particulier,
(1.1.6)
Ext1(Q(n), Q(m)) = 0
pour
m ≤n.
Pour A dans MT(k), il r´esulte de (1.1.6), par induction sur une description de A comme
extension it´er´ee, que A admet une unique ﬁltration “par le poids” W, ﬁnie, croissante et
index´ee par les entiers pairs, telle que
GrW
−2n(M) := W−2n(M)/W−2(n+1)(M)
soit une somme de copies de Q(n). Posons
ωn(M) := Hom(Q(n), GrW
−2n(M)).
4
On a donc
GrW
−2n(M) = Q(n) ⊗Q ωn(M).
La ﬁltration W est fonctorielle, exacte et compatible au produit tensoriel. Parce que
l’automorphisme de symm´etrie de Q(1) ⊗Q(1) est l’identit´e, on dispose d’isomorphismes
Q(n) ⊗Q(m)
∼
−→Q(n + m) compatibles `a l’associativit´e et `a la commutativit´e de ⊗. Le
foncteur exact M 7→ω(M) := ⊕ωn(M) est donc un ⊗-foncteur: c’est un foncteur ﬁbre et
la cat´egorie MT(k) est tannakienne.
1.2. Pour M un motif de Tate mixte, le sous-quotient W−2n(M)/W−2(n+2)(M) de M est
une extension Mn,n+1 de GrW
−2n(M) = Q(n) ⊗ωn(M) par GrW
−2(n+1)(M) = Q(n + 1) ⊗
ωn+1(M). La classe de cette extension est un ´el´ement
en ∈Ext1(Q(n), Q(n + 1)) ⊗Hom(ωn(M), ωn+1(M)).
La tensorisation avec Q(n) est un isomorphisme
(1.2.1)
Ext1(Q(0), Q(1))
∼
−→Ext1(Q(n), Q(n + 1))
et les en d´eﬁnissent
(1.2.2)
eM: ω∗(M) →Ext1(Q(0), Q(1)) ⊗ω∗(M).
Pour x: Q(n) →GrW
−2n(M) dans ωn(M), l’image inverse par x de l’extension Mn,n+1
est une extension de Q(n) par GrW
−2(n+1)(M) = Q(n+1)⊗ωn+1(M), et eM(x) est la classe
de cette extension dans
Ext1(Q(0), Q(1)) ⊗ωn+1(M) = Ext1(Q(n), Q(n + 1)) ⊗ωn+1(M).
On regardera eM comme une coaction, au sens des coalg`ebres de Lie. Plus pr´ecis´ement,
comme une coaction, sur ω(M) := ⊕ω∗(M), de la coalg`ebre de Lie librement coengendr´ee
par Ext1(Q(0), Q(1)).
5
Proposition 1.3. La coaction eM est fonctorielle en M et compatible au produit tensoriel.
Preuve. La v´eriﬁcation de la fonctorialit´e en M est laiss´ee au lecteur. Pour x ∈ωm(M) et
y ∈ωn(N), on doit montrer que
(1.3.1)
eM⊗N(x ⊗y) = eM(x) ⊗y + x ⊗eN(y).
Par fonctorialit´e, on peut pour le v´eriﬁer remplacer M par W−2m(M), une extension
de Q(m) ⊗ωm(M) par W−2(m+1)(M), puis par l’image inverse de cette extension par
x: Q(m) →Q(m) ⊗ωm(M). De mˆeme pour N, n et y. On se ram`ene ainsi `a supposer que
M = W−2m(M), ωm(M) = Q, x = 1, et de mˆeme pour N, n et y. On a alors
ωm+n+1(M ⊗N)
∼
−→ωm+n+1(M ⊗(quotient Q(n) de N))
⊕ωm+n+1((quotient Q(m) de M) ⊗N).
et, par fonctorialit´e en M et N de eM⊗N, il suﬃt de v´eriﬁer (1.3.1) pour M remplac´e par
son quotient Q(m), ainsi que pour N remplac´e par son quotient Q(n). Ces cas se r´eduisent
`a la d´eﬁnition de l’isomorphisme (1.2.1).
Si E est une extension de Q(0) par Q(1), il r´esulte de 1.3 que la classe de l’extension
E∗(1) de Q(0) par Q(1) est l’oppos´ee de la classe de E.
Deﬁnition 1.4. Pour Γ un sous-espace vectoriel de Ext1(Q(0), Q(1)), MT(k)Γ est la
cat´egorie des motifs de Tate mixte tels que la coaction (1.2.2) se factorise par une coaction
de Γ.
Pour que M soit dans MT(k)Γ, il faut et il suﬃt que pour tout sous-quotient E de M
qui est une extension d’un Q(n) par Q(n + 1), la classe de E dans
Ext1(Q(0), Q(1)
∼
−→Ext1(Q(n), Q(n + 1))
soit dans Γ. D’apr`es 1.3, cette sous-cat´egorie de MT(k), qui contient l’objet unit´e Q(0),
est stable par sous-quotients, produits tensoriels et duaux. C’est une sous-cat´egorie tan-
nakienne de MT(k).
6
1.5. Quel que soit k (de caract´erisque 0), on dispose d’un foncteur “r´ealisation” de DM(k)
dans la cat´egorie triangul´ee “syst`emes de r´ealisations” de Huber (1995). L’´etat de la
litt´erature `a ce sujet n’est pas satisfaisant, sp´ecialement en ce qui concerne la r´ealisation
de Hodge. Dans Huber (2000), il est suppos´e `a tort dans la preuve de 2.1.4, p. 775 que
les hyperrecouvrements propres de X forment une cat´egorie ﬁltrante. Cette erreur est cor-
rig´ee dans un erratum dat´e d’octobre 2002. Dans Levine (1998) V. 2.3.7 le foncteur Dec de
d´ecalage d’une ﬁltration par le poids est appliqu´e `a un complexe de faisceaux, alors qu’il
devrait ˆetre appliqu´e apr`es passage `a RΓ.
Nous esquissons ci-dessous une fa¸con possible de proc´eder, adapt´ee `a la d´eﬁnition
de Voevodsky de DM(k), que nous commen¸cons par rappeler. Le foncteur obtenu sera
contravariant (cohomologique). Dans la suite de l’article, c’est sa variante covariante (ho-
mologique), d´eduite par passage au dual, qui nous sera utile.
Soit SmCor(k) la cat´egorie d’objets les sch´emas s´epar´es lisses sur k, un morphisme de
X dans Y ´etant une correspondance ﬁnie de X vers Y : Hom(X, Y ) est le groupe ab´elien
librement engendr´e par les sous-sch´emas r´eduits irr´eductibles ferm´es Z de X × Y , ﬁnis sur
X et dominant une composante connexe de X. La cat´egorie SmCor(k) est additive (avec
⊕= `). La cat´egorie triangul´ee DM(k) se d´eduit de la cat´egorie triangul´ee de complexes
born´es Kb(SmCor(k)) par
(a) localisation: on divise par la sous-cat´egorie ´epaisse engendr´ee par les [X × A1] →[X]
(invariance d’homotopie) et les [U ∩V ] →[U] ⊕[V ] →[X] pour X la r´eunion des ouverts
U et V (Mayer-Vietoris);
(b) adjonction de facteurs directs images d’endomorphismes idempotents;
(c) inversion formelle de Q(1).
Il r´esulte de Voevodsky (2000) 3.2.6 et de (a), Mayer Vietoris, qu’on obtiendrait une
cat´egorie ´equivalente si dans SmCor(k) on se limitait aux sch´emas lisses et quasi-projectifs
sur k. Pour d´eﬁnir le foncteur r´ealisation, l’essentiel est de d´eﬁnir la r´ealisation d’un com-
plexe born´e X∗d’objets de SmCor(k), et par la remarque ci-dessus, on peut se ramener
au cas o`u les Xi sont quasi-projectifs.
7
Lemme 1.5.1. Soit Γ: X →Y dans SmCor(k). Si ¯Y est une compactiﬁcation projective et
lisse de Y , il existe une compactiﬁcation projective et lisse ¯X de X telle que Γ se prolonge
en ¯Γ: ¯X →¯Y . quand elle existe, l’extension ¯Γ est unique.
Preuve. Il suﬃt de traiter du cas o`u X est connexe et o`u Γ est un sous-sch´ema ferm´e Z
de X × Y , r´eduit, irr´eductible, ﬁni et dominant sur X. Si d est le degr´e de Z sur X, Z
d´eﬁnit un morphisme de sch´emas z de X dans Symd(Y ). D’apr`es Hironaka, il existe une
compactiﬁcation projective et lisse ¯X de X telle que z se prolonge en ¯z: ¯X →Symd( ¯Y ).
Pour un tel ¯X, l’adh´erence ¯Z de Z dans ¯X × ¯Y est encore ﬁnie sur ¯X. Elle fournit le pro-
longement cherch´e. L’unicit´e est claire. Noter que, par Hironaka encore, on peut supposer
que X est le compl´ement dans ¯X d’un diviseur `a croisements normaux.
Pour X∗un complexe born´e d’objets de SmCor(k), on d´eduit de 1.5.1 l’existence d’un
syst`eme de compactiﬁcations ¯Xn des Xn tel que (a) ¯Xn est projectif et lisse, et Xn est le
compl´ement dans ¯Xn d’un diviseur `a croisements normaux Dn; (b) la diﬀ´erentielle d se
prolonge de X∗`a ¯X∗. Par unicit´e du prolongement, le prolongement v´eriﬁe encore d2 = 0.
Les syst`emes de compactiﬁcations ¯X forment une cat´egorie ﬁltrante. Pour f: X∗→Y ∗
un morphisme de complexes, et pour ¯Y ∗une compactiﬁcation de Y ∗v´eriﬁant (a), (b), il
existe une compactiﬁcation ¯X∗de X∗v´eriﬁant (a), (b) et telle que f se prolonge en un
morphisme de complexes de ¯X∗dans ¯Y ∗.
D´eﬁnissons la r´ealisation de de Rham de X∗– ingr´edient essentiel de la r´ealisation de
Hodge relative `a un plongement complexe de k dans C. L’id´ee est de choisir une compacti-
ﬁcation ¯X∗de X∗comme ci-dessus et de prendre sur chaque ¯Xn le complexe de de Rham
`a pˆoles logarithmiques Ω∗
¯
Xn(log Dn). Ce complexe est biﬁltr´e: par le ﬁltration de Hodge
F p = σ ≥p, et par la ﬁltration par le poids W∗, qui compte le nombre de facteurs dzi
zi pour zi
une ´equation locale d’une composante lisse de Dn. Il s’agit ensuite d’obtenir des complexes
biﬁltr´es (K(n), W, F) repr´esentant les RΓ( ¯Xn, Ω∗(log Dn)) et d’utiliser la diﬀ´erentielle de
¯X∗pour en faire un complexe double biﬁltr´e, avec K(n) comme colonne de premier indice
−n. La diﬃcult´e sera de d´eduire de d2 = 0 pour ¯X∗que d′2 = 0 identiquement. Ceci fait,
il reste `a
8
(i) remplacer la ﬁltration W de K(n) par son translat´e W ′ d´eﬁni par W ′m = W m−n;
(ii) passer au complexe simple associ´e; on notera que son GrW
est la somme des
GrW (K(n))[n];
(iii) remplacer la ﬁltration W par sa d´ecal´ee Dec W.
Nous travaillerons avec la topologie ´etale. Celle de Nisnevitch ferait aussi bien l’aﬀaire,
mais non celle de Zariski. Pour un faisceau quasi-coh´erent, la cohomologie est la mˆeme.
L’hypercohomologie d’un complexe de de Rham aussi. Gain: pour p: Z →X un morphisme
ﬁni, le foncteur p∗est exact. Ceci est faux pour Zariski. Soit Γ: X →Y dans SmCor(k):
Γ = P niZi et Zi ⊂X × Y est ﬁni sur X. Soient des compactiﬁcations X et Y en ¯X et ¯Y ,
avec `a l’inﬁni un diviseur `a croisement normaux, et supposons que Γ se prolonge en ¯Γ, i.e.
que chaque adh´erence ¯Zi de Zi dans ¯X × ¯Y soit ﬁnie sur ¯X. Soit enﬁn |¯Γ| le support ∪¯Zi
de ¯Γ. La correspondance ¯Γ d´eﬁnit alors un morphisme de complexes de faisceaux sur |Γ|
[¯Γ]: pr∗
2Ω∗(log) →pr∗
1Ω∗(log).
Ici aussi que la topologie soit ´etale ou de Nisnevitch est essentiel. Prendre garde que pr∗
2
est une image inverse au sens des faisceaux, et non pas au sens des faisceaux coh´erents
(pour laquelle l’image inverse de la diﬀ´erentielle de de Rham d ne serait pas d´eﬁnie).
Ce morphisme s’´etend aux r´esolutions ﬂasques canoniques C∗et il suﬃt de repr´esenter
RΓ( ¯Xn, Ω∗(log)) par Γ( ¯Xn, C∗Ω∗(log)).
1.6. En caract´eristique z´ero, les seuls corps pour lesquels la conjecture d’annulation de
Beilinson-Soul´e soit d´emontr´ee sont les corps de nombres (= extensions ﬁnies de Q), les
corps de fonctions rationelles d’une courbe de genre 0 sur un corps de nombres, et les
limites inductives de tels corps. Le cas qui nous importe est celui des corps de nombres.
Pour ceux-ci, Kn(k) ⊗Q est nul pour n pair > 0 et on a
Ext1(Q(0), Q(n)) = K2n−1(k) ⊗Q,
et
Ext2(Q(0), Q(n)) = 0,
car Hom2(Q(0), Q(n)) = 0 dans DM(k)Q.
9
Soit k un corps de nombres. Le foncteur “r´ealisation” sur DM(k) induit sur MT(k) un
⊗-foncteur `a valeurs dans les syst`emes de r´ealisations au sens de Deligne (1989) (aspect
cristallin exclus) ou Jannsen (1990).
Rappelons que Ext1(Q(0), Q(1)) = k∗⊗Q. Si S est un ensemble de places ﬁnies de k,
et que OS est l’ensemble des S-entiers de k (int´egralit´e en dehors de S), nous d´eﬁnissons
artiﬁciellement la cat´egorie des motifs de Tate mixte sur OS comme ´etant MT(k)Γ pour
Γ = O∗
S ⊗Q ⊂k∗⊗Q∗. Cas particulier: pour S le compl´ement d’une place ﬁnie v, OS est
le localis´e O(v) en v de l’anneau des entiers O de k, et on parle de motifs de Tate mixte
non ramiﬁ´es en v. Un motif de Tate mixte sur OS est donc un motif de Tate mixte sur k
non ramiﬁ´e en chaque place ﬁnie v /∈S.
Proposition 1.7. Soit ℓun nombre premier distinct de la caract´eristique r´esiduelle de v.
Pour qu’un motif de Tate mixte M sur k soit non ramiﬁ´e en v, il faut et il suﬃt que sa
r´ealisation ℓ-adique Mℓsoit non ramiﬁ´ee en v.
Preuve. La r´ealisation ℓ-adique est un Qℓ-espace vectoriel d´ependant fonctoriellement du
choix d’une clˆoture alg´ebrique ¯k de k. La fonctorialit´e en ¯k en fait une repr´esentation
continue de Gal(¯k/k). Nous utiliserons que
(a) la r´ealisation l-adique de Q(1) est Qℓ(1) := Zℓ(1) ⊗ZℓQℓ, avec Zℓ(1) = lim µℓn(¯k);
(b) Pour n̸ = m, puisque Hom(Q(n), Q(m)) = 0, une extension de Q(n) par Q(m) est
d´etermin´ee `a isomorphisme unique pr`es par sa classe dans Ext1(Q(n), Q(m)). Pour x ∈
k∗⊂Ext1(Q(0), Q(1)), notons K(x) l’extension de Q(0) par Q(1), dite de Kummer, de
classe x. Sa r´ealisation l-adique est d´eduite, par tensorisation avec Qℓ, de l’extension de
Kummer Kℓ(x) de Zℓpar Zℓ(1). La donn´ee d’une extension
0 →Zℓ(1) →E
f
−→Zℓ→0
de Zℓpar Zℓ(1) ´equivaut `a celle du Zℓ(1)-torseur f −1(1), et Kℓ(x) correspond au Zℓ(1)
torseur limite projective des µℓn(¯k)-torseurs des racines (ℓn)i`emes de x dans ¯k.
La repr´esentation ℓ-adique Kℓ(x) est non ramiﬁ´ee en v si et seulement si x est une
unit´e en v, i.e. est dans O∗
(v). Pour M de Tate mixte, il r´esulte donc de (b) que M est
10
dans MT(Ov) si et seulement si les repr´esentations ℓ-adiques W−2n(Mℓ)/W−2(n+2)(Mℓ)
sont non ramiﬁ´ees. Il reste `a v´eriﬁer le lemme suivant.
Lemme 1.8. Soient Kv le corps des fractions de l’hens´elis´e Oh
(v) de Ov et H une repr´e-
sentation ℓ-adique de Gal( ¯Kv/Kv), munie d’une ﬁltration ﬁnie croissante index´ee par
les entiers pairs W, telle que GrW
−2n(H) soit somme de copies de Qℓ(n). Pour que la
repr´esentation H soit non ramiﬁ´ee, il suﬃt que les repr´esentations W−2n/W−2(n+2) le
soient.
Preuve. Soit Iv ⊂Gal( ¯Kv/Kv) le groupe d’inertie. On sait que son plus grand pro-ℓ-
quotient est canoniquement isomorphe `a Zℓ(1). Soit tℓ: Iv →Zℓ(1) le morphisme de passage
au quotient. Il est Gal( ¯Kv/Kv)-´equivariant.
Supposons que Iv agisse trivialement sur les W−2n/W−2(n+2) et prouvons par r´e-
currence sur r ≥2 qu’il agit trivialement sur les W−2n/W−2(n+r). Pour r = 2, c’est l’hypo-
th`ese. Pour r > 2, l’hypoth`ese de r´ecurrence assure que l’action de Iv est triviale sur
W−2n/W−2(n+r−1) et sur W−2(n+1)/W−2(n+r). L’action de σ ∈Iv est donc de la forme
1 + ν(σ), avec pour ν(σ) un compos´e
W−2n/W−2(n+r) →GrW
−2n
n(σ)
−−−−−→GrW
−2(n+r−1) →W−2n/W−2(n+r),
et n(σ1σ2) = n(σ1) + n(σ2). L’application σ 7→n(σ) se factorise donc par Zℓ(1), et est de
la forme
n(σ) = n · tℓ(σ), pour n: GrW
−2n(1) →GrW
−2(n+r−1).
Le morphisme n est Gal( ¯Kv/Kv)-equivariant. Puisque r > 2, HomGal( ¯
Kv/Kv)(Qℓ(n + 1 ),
Qℓ(n + r −1)) = 0 et n est nul, ce qui conclut la r´ecurrence.
Proposition 1.9. Soit Γ un sous-espace vectoriel de Ext1(Q(0), Q(1)).
(i) Pour r ≥2, Ext1(Q(n), Q(n + r)) est le mˆeme dans MT(k) et dans MT(k)Γ.
(ii) Les Ext2 de Yoneda sont nuls dans MT(k)Γ.
Preuve.
(i) Si r ≥2, une extension de Q(n) par Q(n + r) est en eﬀet automatiquement
dans MT(k)Γ.
11
(ii) Il suﬃt de v´eriﬁer la nullit´e des Ext2(Q(n), Q(m)). Pour toute classe c dans cet Ext2,
il existe dans MT(k)Γ une extension
(1.8.1)
0 →F →E1 →Q(n) →0,
de classe not´ee c1, et une extension E2 de F par Q(m), de classe c2, telle que c soit le
produit de Yoneda c2c1. Ce produit est l’image de c2 par le cobord
∂: Ext1(F, Q(m)) →Ext2(Q(n), Q(m))
d´eﬁni
par
(1.8.1).
C’est
aussi
l’obstruction
`a
l’existence
dans
MT(k)Γ
de
X = X0 ⊃X1 ⊃X2 ⊃X3 = 0 de quotients successifs Xi/Xi+1 (i = 0, 1, 2) munis
d’isomorphismes avec Q(n), F et Q(m), tel que la classe de l’extension X/X2 de Q(n)
par F soit c1, et que la classe de l’extension X1 de F par Q(m) soit c2.
Relevons Q(n) dans GrW
−2n(E1) et soit E′
1 l’image inverse dans W−2n(E1) de ce
rel`evement. C’est une extension de Q(n) par F ′ := F ∩E′
1 = W−2(n+1)(F). Si E′
2 est
l’image inverse de F ′ dans E2, c est encore le produit de Yoneda c′
2c′
1 de la classe c′
1 de
E′
1 par la classe c′
2 de E′
2. On a gagn´e que F ′ = W−2(n+1)(F ′). Un argument dual permet
ensuite de se ramener au cas o`u F = W−2(n+1)(F) et W−2m(F) = 0. Le Ext2 ne peut
donc ˆetre non nul que si m ≥n + 2. Puisque le Ext2 est nul dans MT(k), il existe dans
MT(k) une extension it´er´ee X = X0 ⊃X1 ⊃X2 ⊃X3 = 0 du type consid´er´e plus haut,
le sous-quotient W−2a/W−2(a+2) de X coincide avec le mˆeme sous-quotient de X0/X3 si
a + 2 ≤m, et avec le mˆeme sous-quotient de X1 si a > n. Si, comme on peut le supposer,
m ≥n + 2, on est pour tout a dans un de ces deux cas, X est donc dans MT(k)Γ, et c = 0.
12
