---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ R´ esum´ e.Nous d´ eﬁnissons la cat´ egorie des motifs de Tate mixte sur l’anneau des S-entiers d’un c"
section_id: sec-007-12-pour-m-un-motif-de-tate-mixte-le-sous-quotien
section_title: "Pour M un motif de Tate mixte, le sous-quotient W−2n(M )/W−2(n+2)(M ) de M est"
section_number: 1.2
pages: 7-14
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte P. Deligne et A. B. Goncharov ∗ Résumé.Nous définissons la catégorie des motifs de Tate mixte sur l’anneau des S-entiers d’un corps de nombres, et le grou"
---
une extension Mn,n+1 de Gr W
−2n(M ) = Q(n) ⊗ ωn(M ) par Gr W
−2(n+1)(M ) = Q(n + 1) ⊗
ωn+1(M ). La classe de cette extension est un ´ el´ ement
en ∈ Ext1(Q(n), Q(n + 1)) ⊗ Hom(ωn(M ), ωn+1(M )).
La tensorisation avec Q(n) est un isomorphisme
(1.2.1) Ext 1(Q(0), Q(1)) ∼− →Ext1(Q(n), Q(n + 1))
et les en d´ eﬁnissent
(1.2.2) eM : ω∗(M ) → Ext1(Q(0), Q(1)) ⊗ ω∗(M ).
Pour x: Q(n) → GrW
−2n(M ) dans ωn(M ), l’image inverse par x de l’extension Mn,n+1
est une extension de Q(n) par Gr W
−2(n+1)(M ) = Q(n + 1)⊗ ωn+1(M ), et eM (x) est la classe
de cette extension dans
Ext1(Q(0), Q(1)) ⊗ ωn+1(M ) = Ext 1(Q(n), Q(n + 1)) ⊗ ωn+1(M ).
On regardera eM comme une coaction, au sens des coalg` ebres de Lie. Plus pr´ ecis´ ement,
comme une coaction, sur ω(M ) := ⊕ω∗(M ), de la coalg` ebre de Lie librement coengendr´ ee
par Ext 1(Q(0), Q(1)).
5
Proposition 1.3. La coaction eM est fonctorielle en M et compatible au produit tensoriel.
Preuve. La v´ eriﬁcation de la fonctorialit´ e enM est laiss´ ee au lecteur. Pourx ∈ ωm(M ) et
y ∈ ωn(N ), on doit montrer que
(1.3.1) eM ⊗N (x ⊗ y) = eM (x) ⊗ y + x ⊗ eN (y).
Par fonctorialit´ e, on peut pour le v´ eriﬁer remplacer M par W−2m(M ), une extension
de Q(m) ⊗ ωm(M ) par W−2(m+1)(M ), puis par l’image inverse de cette extension par
x: Q(m) → Q(m) ⊗ ωm(M ). De mˆ eme pourN , n et y. On se ram` ene ainsi ` a supposer que
M = W−2m(M ), ωm(M ) = Q, x = 1, et de mˆ eme pour N , n et y. On a alors
ωm+n+1(M ⊗ N ) ∼− →ωm+n+1(M ⊗ (quotient Q(n) de N ))
⊕ ωm+n+1((quotient Q(m) de M ) ⊗ N ).
et, par fonctorialit´ e enM et N de eM ⊗N , il suﬃt de v´ eriﬁer (1.3.1) pour M remplac´ e par
son quotient Q(m), ainsi que pour N remplac´ e par son quotientQ(n). Ces cas se r´ eduisent
` a la d´ eﬁnition de l’isomorphisme (1.2.1).
Si E est une extension de Q(0) par Q(1), il r´ esulte de 1.3 que la classe de l’extension
E∗(1) de Q(0) par Q(1) est l’oppos´ ee de la classe de E.
Deﬁnition 1.4. Pour Γ un sous-espace vectoriel de Ext1(Q(0), Q(1)), M T(k)Γ est la
cat´ egorie des motifs de Tate mixte tels que la coaction (1.2 .2) se factorise par une coaction
de Γ.
Pour que M soit dans MT( k)Γ , il faut et il suﬃt que pour tout sous-quotient E de M
qui est une extension d’un Q(n) par Q(n + 1), la classe de E dans
Ext1(Q(0), Q(1) ∼− →Ext1(Q(n), Q(n + 1))
soit dans Γ. D’apr` es 1.3, cette sous-cat´ egorie de M T(k), qui contient l’objet unit´ e Q(0),
est stable par sous-quotients, produits tensoriels et duau x. C’est une sous-cat´ egorie tan-
nakienne de M T(k).
6
1.5. Quel que soit k (de caract´ erisque 0), on dispose d’un foncteur “r´ ealisation” de DM( k)
dans la cat´ egorie triangul´ ee “syst` emes de r´ ealisations” de Huber (1995). L’´ etat de la
litt´ erature ` a ce sujet n’est pas satisfaisant, sp´ ecialement en ce qui concerne la r´ ealisation
de Hodge. Dans Huber (2000), il est suppos´ e ` a tort dans la pr euve de 2.1.4, p. 775 que
les hyperrecouvrements propres de X forment une cat´ egorie ﬁltrante. Cette erreur est cor-
rig´ ee dans un erratum dat´ e d’octobre 2002. Dans Levine (1998) V. 2.3.7 le foncteur Dec de
d´ ecalage d’une ﬁltration par le poids est appliqu´ e ` a un complexe de faisceaux, alors qu’il
devrait ˆ etre appliqu´ e apr` es passage ` aRΓ.
Nous esquissons ci-dessous une fa¸ con possible de proc´ ede r, adapt´ ee ` a la d´ eﬁnition
de Voevodsky de DM( k), que nous commen¸ cons par rappeler. Le foncteur obtenu ser a
contravariant (cohomologique). Dans la suite de l’article , c’est sa variante covariante (ho-
mologique), d´ eduite par passage au dual, qui nous sera util e.
Soit SmCor( k) la cat´ egorie d’objets les sch´ emas s´ epar´ es lisses surk, un morphisme de
X dans Y ´ etant une correspondance ﬁnie de X vers Y : Hom( X, Y ) est le groupe ab´ elien
librement engendr´ e par les sous-sch´ emas r´ eduits irr´ eductibles ferm´ esZ de X × Y , ﬁnis sur
X et dominant une composante connexe de X. La cat´ egorie SmCor(k) est additive (avec
⊕ = ∐ ). La cat´ egorie triangul´ ee DM(k) se d´ eduit de la cat´ egorie triangul´ ee de complexes
born´ esK b(SmCor(k)) par
(a) localisation: on divise par la sous-cat´ egorie ´ epaisse engendr´ ee par les [X × A1] → [X]
(invariance d’homotopie) et les [ U ∩ V ] → [U ] ⊕ [V ] → [X] pour X la r´ eunion des ouverts
U et V (Mayer-Vietoris);
(b) adjonction de facteurs directs images d’endomorphismes id empotents;
(c) inversion formelle de Q(1).
Il r´ esulte de Voevodsky (2000) 3.2.6 et de (a), Mayer Vietor is, qu’on obtiendrait une
cat´ egorie ´ equivalente si dans SmCor(k) on se limitait aux sch´ emas lisses et quasi-projectifs
sur k. Pour d´ eﬁnir le foncteur r´ ealisation, l’essentiel est ded´ eﬁnir la r´ ealisation d’un com-
plexe born´ eX ∗ d’objets de SmCor( k), et par la remarque ci-dessus, on peut se ramener
au cas o` u les X i sont quasi-projectifs.
7
Lemme 1.5.1. Soit Γ: X → Y dans SmCor(k). Si ¯Y est une compactiﬁcation projective et
lisse de Y , il existe une compactiﬁcation projective et lisse ¯X de X telle que Γ se prolonge
en ¯Γ: ¯X → ¯Y . quand elle existe, l’extension ¯Γ est unique.
Preuve. Il suﬃt de traiter du cas o` u X est connexe et o` u Γ est un sous-sch´ ema ferm´ e Z
de X × Y , r´ eduit, irr´ eductible, ﬁni et dominant sur X. Si d est le degr´ e de Z sur X, Z
d´ eﬁnit un morphisme de sch´ emasz de X dans Sym d(Y ). D’apr` es Hironaka, il existe une
compactiﬁcation projective et lisse ¯X de X telle que z se prolonge en ¯z: ¯X → Symd( ¯Y ).
Pour un tel ¯X, l’adh´ erence¯Z de Z dans ¯X × ¯Y est encore ﬁnie sur ¯X. Elle fournit le pro-
longement cherch´ e. L’unicit´ e est claire. Noter que, par Hironaka encore, on peut supposer
que X est le compl´ ement dans ¯X d’un diviseur ` a croisements normaux.
Pour X ∗ un complexe born´ e d’objets de SmCor(k), on d´ eduit de 1.5.1 l’existence d’un
syst` eme de compactiﬁcations ¯X n des X n tel que (a) ¯X n est projectif et lisse, et X n est le
compl´ ement dans ¯X n d’un diviseur ` a croisements normaux Dn; (b) la diﬀ´ erentielle d se
prolonge de X ∗ ` a ¯X ∗. Par unicit´ e du prolongement, le prolongement v´ eriﬁe encore d2 = 0.
Les syst` emes de compactiﬁcations ¯X forment une cat´ egorie ﬁltrante. Pour f : X ∗ → Y ∗
un morphisme de complexes, et pour ¯Y ∗ une compactiﬁcation de Y ∗ v´ eriﬁant (a), (b), il
existe une compactiﬁcation ¯X ∗ de X ∗ v´ eriﬁant (a), (b) et telle que f se prolonge en un
morphisme de complexes de ¯X ∗ dans ¯Y ∗.
D´ eﬁnissons la r´ ealisation de de Rham deX ∗ – ingr´ edient essentiel de la r´ ealisation de
Hodge relative ` a un plongement complexe de k dans C. L’id´ ee est de choisir une compacti-
ﬁcation ¯X ∗ de X ∗ comme ci-dessus et de prendre sur chaque ¯X n le complexe de de Rham
` a pˆ oles logarithmiques Ω∗
¯Xn (log Dn). Ce complexe est biﬁltr´ e: par le ﬁltration de Hodge
F p = σ ≥ p, et par la ﬁltration par le poids W∗, qui compte le nombre de facteurs dzi
zi
pour zi
une ´ equation locale d’une composante lisse deDn. Il s’agit ensuite d’obtenir des complexes
biﬁltr´ es (K (n), W, F) repr´ esentant lesRΓ( ¯X n, Ω ∗(log Dn)) et d’utiliser la diﬀ´ erentielle de
¯X ∗ pour en faire un complexe double biﬁltr´ e, avec K (n) comme colonne de premier indice
−n. La diﬃcult´ e sera de d´ eduire ded2 = 0 pour ¯X ∗ que d′2 = 0 identiquement. Ceci fait,
il reste ` a
8
(i) remplacer la ﬁltration W de K (n) par son translat´ eW ′ d´ eﬁni parW ′m = W m−n;
(ii) passer au complexe simple associ´ e; on notera que son Gr W est la somme des
GrW (K (n))[n];
(iii) remplacer la ﬁltration W par sa d´ ecal´ ee DecW .
Nous travaillerons avec la topologie ´ etale. Celle de Nisnevitch ferait aussi bien l’aﬀaire,
mais non celle de Zariski. Pour un faisceau quasi-coh´ erent , la cohomologie est la mˆ eme.
L’hypercohomologie d’un complexe de de Rham aussi. Gain: pour p: Z → X un morphisme
ﬁni, le foncteur p∗ est exact. Ceci est faux pour Zariski. Soit Γ: X → Y dans SmCor( k):
Γ = ∑ niZi et Zi ⊂ X × Y est ﬁni sur X. Soient des compactiﬁcations X et Y en ¯X et ¯Y ,
avec ` a l’inﬁni un diviseur ` a croisement normaux, et suppos ons que Γ se prolonge en ¯Γ, i.e.
que chaque adh´ erence¯Zi de Zi dans ¯X × ¯Y soit ﬁnie sur ¯X. Soit enﬁn |¯Γ | le support ∪ ¯Zi
de ¯Γ. La correspondance ¯Γ d´ eﬁnit alors un morphisme de complexes de faisceaux sur |Γ |
[¯Γ]: pr ∗
2Ω ∗(log) → pr∗
1Ω ∗(log).
Ici aussi que la topologie soit ´ etale ou de Nisnevitch est es sentiel. Prendre garde que pr ∗
2
est une image inverse au sens des faisceaux, et non pas au sens des faisceaux coh´ erents
(pour laquelle l’image inverse de la diﬀ´ erentielle de de Rh am d ne serait pas d´ eﬁnie).
Ce morphisme s’´ etend aux r´ esolutions ﬂasques canoniques C∗ et il suﬃt de repr´ esenter
RΓ( ¯X n, Ω ∗(log)) par Γ( ¯X n, C∗Ω ∗(log)).
1.6. En caract´ eristique z´ ero, les seuls corps pour lesquels la conjecture d’annulation de
Beilinson-Soul´ e soit d´ emontr´ ee sont les corps de nombres (= extensions ﬁnies de Q), les
corps de fonctions rationelles d’une courbe de genre 0 sur un corps de nombres, et les
limites inductives de tels corps. Le cas qui nous importe est celui des corps de nombres.
Pour ceux-ci, Kn(k) ⊗ Q est nul pour n pair > 0 et on a
Ext1(Q(0), Q(n)) = K2n−1(k) ⊗ Q, et
Ext2(Q(0), Q(n)) = 0 ,
car Hom 2(Q(0), Q(n)) = 0 dans DM( k)Q.
9
Soit k un corps de nombres. Le foncteur “r´ ealisation” sur DM(k) induit sur MT( k) un
⊗-foncteur ` a valeurs dans les syst` emes de r´ ealisations au sens de Deligne (1989) (aspect
cristallin exclus) ou Jannsen (1990).
Rappelons que Ext 1(Q(0), Q(1)) = k∗ ⊗ Q. Si S est un ensemble de places ﬁnies de k,
et que OS est l’ensemble des S-entiers de k (int´ egralit´ e en dehors deS), nous d´ eﬁnissons
artiﬁciellement la cat´ egorie des motifs de Tate mixte sur OS comme ´ etant MT(k)Γ pour
Γ = O∗
S ⊗ Q ⊂ k∗ ⊗ Q∗. Cas particulier: pour S le compl´ ement d’une place ﬁniev, OS est
le localis´ eO(v) en v de l’anneau des entiers O de k, et on parle de motifs de Tate mixte
non ramiﬁ´ esen v. Un motif de Tate mixte sur OS est donc un motif de Tate mixte sur k
non ramiﬁ´ e en chaque place ﬁnie v /∈ S.
Proposition 1.7. Soit ℓ un nombre premier distinct de la caract´ eristique r´ esiduelle de v.
Pour qu’un motif de Tate mixte M sur k soit non ramiﬁ´ e en v, il faut et il suﬃt que sa
r´ ealisationℓ-adique Mℓ soit non ramiﬁ´ ee en v.
Preuve. La r´ ealisationℓ-adique est un Qℓ-espace vectoriel d´ ependant fonctoriellement du
choix d’une clˆ oture alg´ ebrique¯k de k. La fonctorialit´ e en ¯k en fait une repr´ esentation
continue de Gal( ¯k/k). Nous utiliserons que
(a) la r´ ealisation l-adique deQ(1) est Qℓ(1) := Zℓ(1) ⊗Zℓ Qℓ, avec Zℓ(1) = lim µℓn (¯k);
(b) Pour n ⁄= m, puisque Hom( Q(n), Q(m)) = 0, une extension de Q(n) par Q(m) est
d´ etermin´ ee ` a isomorphisme unique pr` es par sa classe dans Ext 1(Q(n), Q(m)). Pour x ∈
k∗ ⊂ Ext1(Q(0), Q(1)), notons K(x) l’extension de Q(0) par Q(1), dite de Kummer, de
classe x. Sa r´ ealisation l-adique est d´ eduite, par tensorisation avec Qℓ, de l’extension de
Kummer Kℓ(x) de Zℓ par Zℓ(1). La donn´ ee d’une extension
0 → Zℓ(1) → E
f
− →Zℓ → 0
de Zℓ par Zℓ(1) ´ equivaut ` a celle du Zℓ(1)-torseur f −1(1), et Kℓ(x) correspond au Zℓ(1)
torseur limite projective des µℓn (¯k)-torseurs des racines ( ℓn)i` emes de x dans ¯k.
La repr´ esentationℓ-adique Kℓ(x) est non ramiﬁ´ ee en v si et seulement si x est une
unit´ e env, i.e. est dans O∗
(v). Pour M de Tate mixte, il r´ esulte donc de (b) que M est
10
dans M T(Ov) si et seulement si les repr´ esentations ℓ-adiques W−2n(Mℓ)/W−2(n+2)(Mℓ)
sont non ramiﬁ´ ees. Il reste ` a v´ eriﬁer le lemme suivant.
Lemme 1.8. Soient Kv le corps des fractions de l’hens´ elis´ eOh
(v) de Ov et H une repr´ e-
sentation ℓ-adique de Gal( ¯Kv/Kv), munie d’une ﬁltration ﬁnie croissante index´ ee par
les entiers pairs W , telle que GrW
−2n(H) soit somme de copies de Qℓ(n). Pour que la
repr´ esentationH soit non ramiﬁ´ ee, il suﬃt que les repr´ esentations W−2n/W−2(n+2) le
soient.
Preuve. Soit Iv ⊂ Gal( ¯Kv/Kv) le groupe d’inertie. On sait que son plus grand pro- ℓ-
quotient est canoniquement isomorphe ` a Zℓ(1). Soit tℓ: Iv → Zℓ(1) le morphisme de passage
au quotient. Il est Gal( ¯Kv/Kv)-´ equivariant.
Supposons que Iv agisse trivialement sur les W−2n/W−2(n+2) et prouvons par r´ e-
currence sur r ≥ 2 qu’il agit trivialement sur les W−2n/W−2(n+r). Pour r = 2, c’est l’hypo-
th` ese. Pour r > 2, l’hypoth` ese de r´ ecurrence assure que l’action de Iv est triviale sur
W−2n/W−2(n+r−1) et sur W−2(n+1)/W−2(n+r). L’action de σ ∈ Iv est donc de la forme
1 + ν(σ), avec pour ν(σ) un compos´ e
W−2n/W−2(n+r) → GrW
−2n
n(σ)
− − − − − →GrW
−2(n+r−1) → W−2n/W−2(n+r),
et n(σ1σ2) = n(σ1) + n(σ2). L’application σ ↦→n(σ) se factorise donc par Zℓ(1), et est de
la forme
n(σ) = n · tℓ(σ), pour n: Gr W
−2n(1) → GrW
−2(n+r−1).
Le morphisme n est Gal( ¯Kv/Kv)-equivariant. Puisque r > 2, Hom Gal( ¯Kv /Kv )(Qℓ(n + 1 ) ,
Qℓ(n + r − 1)) = 0 et n est nul, ce qui conclut la r´ ecurrence.
Proposition 1.9. Soit Γ un sous-espace vectoriel de Ext1(Q(0), Q(1)).
(i) Pour r ≥ 2, Ext1(Q(n), Q(n + r)) est le mˆ eme dans M T(k) et dans M T(k)Γ .
(ii) Les Ext2 de Yoneda sont nuls dans M T(k)Γ .
Preuve. (i) Si r ≥ 2, une extension de Q(n) par Q(n + r) est en eﬀet automatiquement
dans M T(k)Γ .
11
(ii) Il suﬃt de v´ eriﬁer la nullit´ e des Ext2(Q(n), Q(m)). Pour toute classe c dans cet Ext 2,
il existe dans M T(k)Γ une extension
(1.8.1) 0 → F → E1 → Q(n) → 0,
de classe not´ ee c1, et une extension E2 de F par Q(m), de classe c2, telle que c soit le
produit de Yoneda c2c1. Ce produit est l’image de c2 par le cobord
∂: Ext 1(F, Q(m)) → Ext2(Q(n), Q(m))
d´ eﬁni par (1.8.1). C’est aussi l’obstruction ` a l’existen ce dans M T(k)Γ de
X = X0 ⊃ X1 ⊃ X2 ⊃ X3 = 0 de quotients successifs Xi/Xi+1 (i = 0 , 1, 2) munis
d’isomorphismes avec Q(n), F et Q(m), tel que la classe de l’extension X/X2 de Q(n)
par F soit c1, et que la classe de l’extension X1 de F par Q(m) soit c2.
Relevons Q(n) dans Gr W
−2n(E1) et soit E′
1 l’image inverse dans W−2n(E1) de ce
rel` evement. C’est une extension de Q(n) par F ′ := F ∩ E′
1 = W−2(n+1)(F ). Si E′
2 est
l’image inverse de F ′ dans E2, c est encore le produit de Yoneda c′
2c′
1 de la classe c′
1 de
E′
1 par la classe c′
2 de E′
