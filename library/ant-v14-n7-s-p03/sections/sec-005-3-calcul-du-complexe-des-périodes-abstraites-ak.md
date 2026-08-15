---
doc_id: ant-v14-n7-s-p03
doc_title: "Nouvelles cohomologies de Weil en caractéristique positive Joseph Ayoub"
section_id: sec-005-3-calcul-du-complexe-des-périodes-abstraites-ak
section_title: "Calcul du complexe des périodes abstraites AK et applications"
section_number: 3
pages: 29-38
source_pdf: ant-v14-n7-s-p03.pdf
source_sha256: e32fde16c3ce0940
doc_brief: "Nouvelles cohomologies de Weil en caractéristique positive Joseph Ayoub — periods” admitting an explicit description by generators and relations."
---
Tout au long de la section, on ﬁxe un corps K muni d’une valuation de hauteur 1 et on note ˆK son
complété. On désigne par K◦ et ˆK◦ les anneaux de valuation de K et ˆK , et on note k le corps résiduel de
K◦ qu’on identiﬁe à celui de ˆK◦. Sauf mention explicite du contraire, on suppose que la caractéristique
de K est nulle ; on ne fait pas d’hypothèses sur la caractéristique de k.
Notre but ici est d’expliciter le complexe AK , à quasi-isomorphisme près, et de montrer qu’il est(−1)-
connexe. Ceci nous permettra d’achever la construction de la nouvelle réalisation (1-3). On rappelle que,
en tant que complexe de K -vectoriels, AK est la réalisation de de Rham du motif Rig∗1∈ DA´et(K; K) ;
voir les constructions 2.32 et 2.34, ainsi que l’exemple 2.36. Ainsi, en utilisant la formule de coprojection
du lemme 2.29, on obtient :
AK= R0(K; ⊗ Rig∗1)
≃ R0(K; Rig∗Rig∗())
≃ R0(ˆK; Rig∗()). (3-1)
Pour expliciter le complexe AK , on utilise un modèle explicite du foncteur R0(ˆK; Rig∗(−)) qu’on décrit
dans la première sous-section ci-dessous.
3A. Un modèle explicite du foncteur R0( ˆK , Rig∗(−)). Il sera nécessaire ici d’utiliser la version avec
transferts des catégories triangulées de motifs (voir les remarques 2.1 et 2.13). On ﬁxe une Q-algèbre3.
Nous allons expliquer comment calculer, à quasi-isomorphisme près, le complexe R0(ˆK; Rig∗M) pour
M un objet de DM(K;3). Il s’agit en fait d’assembler plusieurs résultats de [Ayoub 2015a, Chapitre 2].
Notation 3.1. Pour m∈ N, on note∂B∧m (resp. E∧m) la paire(∂B1, 1)∧m (resp.(E1, 1)∧m) au sens de
[Ayoub 2014b, Déﬁnition 2.29]. Ainsi,∂B∧m (resp. E∧m) est la paire formée de la ˆK -variété rigide∂Bm
(resp. du K -schéma Em) et du diviseur à croisements normaux déﬁni par l’équation(t1−1)··· (tm−1)= 0.
1776 Joseph Ayoub
Théorème 3.2. Soit E un T -spectre en complexes de préfaisceaux avec transferts sur Sm/K à valeurs
dans les3-modules. Alors, le complexe de3-modules R0(ˆK; Rig∗ E) est naturellement quasi-isomorphe
à
colim
m∈ N
Tot□ Rig∗ Em(∂B∧m× B)[m]. (3-2)
Ci-dessus, B désigne la ˆK -variété rigide cocubique qui à n∈ N associe Bn et Tot□ est le foncteur
« complexe simple associé à un complexe cubique ». Les morphismes de transition sont induits par les
morphismes
Rig∗ Em→ Rig∗ Em+1(∂B∧1×−)[1]
adjoints des morphismes d’assemblage du T -spectreRig∗ E.
Démonstration. Ceci découle directement de [Ayoub 2015a, Théorème 2.5.32]. En effet, considérons le
T -spectre
(3∞SgB1
Rig∗(E))´et-ﬁb (3-3)
où SgB1
= Tot□Hom(B,−), 3∞= colimm∈ N 3◦m est le foncteur de stabilisation des T -spectres (comme
dans [Ayoub 2007, Théorème 4.3.61]) et(−)´et-ﬁb désigne un remplacement´et-ﬁbrant niveau par niveau.
D’après [Ayoub 2015a, Théorème 2.5.32(1)], leT -spectre(SgB1
Rig∗ E)´et-ﬁb est un remplacement(B1,´et)-
ﬁbrant niveau par niveau deRig∗ E. (Dans [Ayoub 2015a], on utilise la version simpliciale du foncteurSgB1
,
mais les deux versions simpliciale et cubique fournissent des complexes quasi-isomorphes.) Il s’ensuit,
grâce à [Ayoub 2007, Théorème 4.3.61], que 3∞((SgB1
Rig∗ E)´et-ﬁb) est un remplacement stablement
(B1,´et)-ﬁbrant de Rig∗ E. Or, d’après [Ayoub 2015a, Théorème 2.5.32(2)], le morphisme évident
(3∞SgB1
Rig∗ E)´et-ﬁb→ 3∞((SgB1
Rig∗ E)´et-ﬁb)
est un quasi-isomorphisme niveau par niveau. Au ﬁnal, ceci montre que le T -spectre (3 -3) est un
remplacement stablement(B1,´et)-ﬁbrant de Rig∗ E. On en déduit des quasi-isomorphismes
R0(ˆK; Rig∗ E)≃ 0(ˆK;(3∞SgB1
Rig∗ E)´et-ﬁb)
≃ 0(ˆK; 3∞SgB1
Rig∗ E).
(En effet, le foncteur0(ˆK;−) transforme une équivalence´et-locale entre complexes de préfaisceaux avec
transferts en un quasi-isomorphisme.) Le résultat recherché s’ensuit car0(ˆK; 3∞SgB1
Rig∗ E) s’identiﬁe
au complexe (3-2) par la construction même des foncteurs 3∞ et SgB1
. □
Le théorème 3.2 ne sufﬁra pas pour la suite, et il nous faut une description plus « économique » du
complexe R0(ˆK; Rig∗ E). On introduit d’abord quelques notations.
Notation 3.3. Pour m, n∈ N, on note(∂Bm× Bn)´et le pro-K -schéma des voisinages étales de∂Bm× Bn
dans le K -schéma Em× An. Plus précisément, considérons la catégorie Vm, n
´et ayant pour objets les couples
(U, u) où U est un Em× An-schéma étale et u:∂Bm× Bn→ U anr est un morphisme de ˆK -variétés rigides
Nouvelles cohomologies de Weil en caractéristique positive 1777
faisant commuter le triangle
∂Bm× Bn u //
))
U anr

(Em× An)anr
(Bien entendu, la ﬂèche oblique est l’inclusion évidente.) La catégorie Vm, n
´et est coﬁltrante et le foncteur
qui à(U, u) associe U déﬁnit le pro- K -schéma(∂Bm× Bn)´et qui est pro-étale sur Em× An.
On note(∂B∧m× Bn)´et la pro-K -paire formée de(∂Bm× Bn)´et et de l’image inverse du diviseur deEm
déﬁni par l’équation(t1− 1)··· (tm− 1)= 0. En faisant varier n, on obtient un pro- K -schéma cocubique
(∂Bm× B)´et ainsi qu’une pro-K -paire cocubique(∂B∧m× B)´et.
Théorème 3.4. Soit E un T -spectre en complexes de préfaisceaux avec transferts sur Sm/K à valeurs
dans les3-modules. Alors, le complexe de3-modules R0(ˆK; Rig∗ E) est naturellement quasi-isomorphe
à
colim
m∈ N
Tot□ Em((∂B∧m× B)´et)[m]. (3-4)
Les morphismes de transition dans cette colimite sont donnés par les compositions de
Em((∂B∧m× B)´et)→ Em+1(E∧1∧(∂B∧m× B)´et)[1]→ Em+1((∂B∧m+1× B)´et)[1]
où la première ﬂèche est déduite du morphisme d’assemblage du T -spectreE.
Démonstration. Vu le théorème 3.2, il sufﬁt de montrer que le complexe Tot□Rig∗F(∂Bm× B) est
naturellement quasi-isomorphe au complexe Tot□F((∂Bm× B)´et) pour tout complexe de préfaisceaux
avec transferts F sur Sm/K . Ceci découle immédiatement de (la version cubique de) [Ayoub 2015a,
Théorème 2.4.16]. Plus précisément, on se ramène aussitôt au cas où F=3tr(X) pour X un K -schéma
lisse. Ensuite, on spécialise la situation considérée dans [Ayoub 2015a, Notation 2.4.14] en prenant
B=∂Bm et B0= Em. □
3B. Calcul du complexe AK et du morphisme
∫
. Le théorème 3.4 appliqué au T -spectre  qui repré-
sente la cohomologie de de Rham sur Sm/K permet d’obtenir le résultat suivant.
Corollaire 3.5. Le complexe AK est quasi-isomorphe à
colim
m∈ N
Tot□((∂ B∧m× B)´et)[m] (3-5)
où désigne le complexe de de Rham sur Sm/K et où les morphismes de transition sont donnés par la
composition de
((∂ B∧m× B)´et)
dln tm+1∧− // (E∧1×(∂B∧m× B)´et)[1]→ ((∂ B∧m+1× B)´et)[1]
avec t1,..., tm+1 les coordonnées sur Em+1.
Démonstration. Modulo (3-1), il s’agit du théorème 3.4 appliqué au T -spectre . □
1778 Joseph Ayoub
On peut calculer le complexe Tot□((∂ B∧m× B)´et) à quasi-isomorphisme près en utilisant la méthode
développée dans [Ayoub 2014b, pages 97–102]. En effet, on dispose d’un complexe de W(K)-modules
cubiques6-enrichis (au sens de [Ayoub 2014b, Déﬁnition 2.94]) :
M•
m=•
/A((∂B∧m× B)´et)
concentré en degrés cohomologiques 0⩽ e⩽ m où il est donné par
Me
m=e
/A((∂B∧m× B)´et)=
⨁
I⊂[[1, m]], card(I)=m−e
O(I)((∂Bm× B)´et)· dlnˆtI.
Ci-dessus, O(I)((∂Bm× B)´et) est le sous- K -vectoriel de O((∂Bm× B)´et) formé des fonctions g telles
que g|ti=1= 0 pour tout i∈ I et dlnˆtI est le produit extérieur dans l’ordre décroissant des dln tu, pour
u∈[[1, m]]r I . Avec la notation de [Ayoub 2014b, Déﬁnition 2.97], on a tautologiquement :
Tot□((∂ B∧m× B)´et)= Tot(DR•(M•
m)).
De plus, modulo cette identiﬁcation, les morphismes de transition dans (3 -5) sont induits par les mor-
phismes de complexes de W(K)-modules dln tm+1∧−: M•
m→ M•
m+1[1]. D’après [Ayoub 2014b,
Proposition 2.100], il existe un quasi-isomorphisme canonique
Tot DR•(M•
m)≃ Tot(~∞−•(M•
m)).
En explicitant ce dernier complexe, on obtient l’énoncé suivant.
Théorème 3.6. Le complexe AK est canoniquement quasi-isomorphe à
colim
m∈ N
~∞−•((∂Bm× B∞)´et) (3-6)
où~∞−•((∂Bm× B∞)´et) sont des complexes concentrés en degrés homologiques positifs et qui admettent
la description suivante. Pour d> 0, on a
~∞−d((∂Bm× B∞)´et)=
⨁
card(I)+card(J)=d
I⊂[[1, m]], J⊂ Nr{0}
O(I),( J)((∂Bm× B∞)´et)· dlnˆtI∧ dˆz J,
où :
— O(I),( J)((∂Bm× B∞)´et) est le sous-K -vectoriel de O((∂Bm× B∞)´et) formé des fonctions g telles
que g|ti=1= 0 pour i∈ I et g|z j=ϵ= 0 pour j∈ J et ϵ∈{ 0, 1} ;
— le symbole dlnˆtI désigne le produit extérieur des dln tu, pour u∈[[1, m]]r I , dans l’ordre décrois-
sant ;
— le symbole dˆz J désigne le produit extérieur inﬁni des dzv, pourv⁄∈ J, dans l’ordre croissant.
La différentielle du complexe~∞−•((∂Bm× B∞)´et) est la différentielle de de Rham multipliée par(−1)m.
Enﬁn, les morphismes de transition dans la colimite (3-6) sont donnés par dln tm+1∧− .
Remarque 3.7. On peut facilement adapter la preuve de [Ayoub 2014b, Proposition 2.102] pour montrer
que la K -algèbre O((∂Bm× Bn)´et) coïncide avec la sous-K -algèbre de Oalg(∂Bm× Bn)⊂ O(∂Bm× Bn)
Nouvelles cohomologies de Weil en caractéristique positive 1779
formée des éléments qui sont algébriques sur le corps des fractions rationnelles K(t1,..., tm, z1,..., zn).
(V oir la construction 1.3 dans l’introduction.)
Corollaire 3.8. Le complexe AK est(−1)-connexe et, en tant que K -vectoriel, H0(AK) est le quotient de
Oalg(∂B∞× B∞)=⋃
m, n∈ N Oalg(∂Bm× Bn) par le sous-K -vectoriel engendré par les éléments:
ti·∂g
∂ti
, pour g∈ Oalg(∂B∞× B∞) et i> 1;
∂h
∂z j
− h|z j=1+ h|z j=0, pour h∈ Oalg(∂B∞× B∞) et j> 1.
Corollaire 3.9. Étant donné un plongement complexeσ: K ↪→ C, le complexe AK, B est(−1)-connexe.
De même, étant donnés un nombre premier 𝓁 et une clôture algébrique de K , le complexe AK,𝓁 est
(−1)-connexe.
Démonstration. Ceci découle aussitôt du corollaire 3.8 et des quasi-isomorphismes (2-58). □
Notation 3.10. On pose AK= H0(AK). De même, sous les hypothèses du corollaire 3.9, on pose
AK, B= H0(AK, B) et AK,𝓁= H0(AK,𝓁).
Remarque 3.11. Puisque le complexe AK est(−1)-connexe, on dispose d’un morphisme canonique
AK→ AK dans la catégorie homotopique des K -dg-algèbres qui est donné par le zigzag
AK
q.-i.oo τ>0AK→ AK. (3-7)
Il s’ensuit un foncteur monoïdal
AK⊗AK−: Ho(Mod(AK))→ D(AK). (3-8)
La même chose s’applique également aux dg-algèbres AK, B et AK,𝓁 .
Par construction, le morphisme de K -dg-algèbres (2 -50) se factorise par AK et fournit donc un
morphisme de K -algèbres ∫
: AK→ ˆK. (3-9)
On termine la sous-section avec le résultat suivant qui fournit une description explicite de ce morphisme.
Proposition 3.12. Modulo la description de AK fournie par le corollaire 3.8, le morphisme (3-9) envoie
la classe d’une fonction f∈ Oalg(∂Bm× Bn) sur
∫ 1
0
···
∫ 1
0
cc( f)· dz1··· dzn (3-10)
où cc( f)∈ O(Bn) est le coefﬁcient det0
1··· t0
m dans f vue comme un élément de O(Bn){t1,t−1
1 ,..., tm,t−1
m}.
(Voir la ﬁn de la construction 1.3 pour la signiﬁcation de l’intégrale multiple(3-10).)
Démonstration. On divise la preuve en deux étapes.
1780 Joseph Ayoub
Étape 1. On rappelle d’abord la construction du morphisme deK -dg-algèbres AK→ˆK . On dispose d’un
morphisme de cohomologies de Weil0dR(−)≃0†
dR(−)anr induisant un morphisme 0dR→ Rig∗0†
dR dans
DA´et(K; K). Le morphisme AK→ ˆK qui nous intéresse s’obtient, modulo les identiﬁcations évidentes,
en appliquant R0(K;−) à la composition de
0dR⊗ Rig∗1→ Rig∗0†
dR⊗ Rig∗1
m
− →Rig∗0†
dR; (3-11)
voir la preuve du lemme 2.33. Le morphisme 0dR→ Rig∗0†
dR correspond par adjonction à un morphisme
Rig∗0dR→ 0†
dR (3-12)
dans RigDA´et(ˆK; K). De plus, modulo l’isomorphisme de coprojection 0dR⊗ Rig∗1≃ Rig∗Rig∗0dR, la
composition (3-11) s’identiﬁe au morphisme Rig∗((3-12)): Rig∗Rig∗0dR→ Rig∗0†
dR. Au ﬁnal, on voit
que le morphisme AK→ ˆK est donné par
R0(ˆK; (3-12)): AK= R0(ˆK; Rig∗0dR)→ R0(ˆK; 0†
dR)= ˆK. (3-13)
Étape 2. Modulo l’identiﬁcation fournie par le corollaire 3.5, le morphisme (3 -13) est donné par le
morphisme évident
colim
m∈ N
Tot□((∂ B∧m× B)´et)[m]→ colim
m∈ N
Tot□0†
dR(∂B∧m× B)(m)[m]. (3-14)
Notons(∂Bm× Bn)† la ˆK -variété rigide∂Bm× Bn avec sa structure de surconvergence évidente et que
l’on considère comme une pro-ˆK -variété rigide. Par la construction de 0†
dR (voir l’exemple 2.22), le
morphisme (3-14) se factorise par le morphisme évident
colim
m∈ N
Tot□((∂ B∧m× B)´et)[m]→ colim
m∈ N
Tot□((∂ B∧m× B)†)[m] (3-15)
et le membre à droite est encore quasi-isomorphe à ˆK . Le calcul qui mène au théorème 3.6 permet de
réécrire le morphisme (3-15) comme suit :
colim
m∈ N
~∞−•((∂Bm× B∞)´et)→ colim
m∈ N
~∞−•((∂Bm× B∞)†). (3-16)
Le résultat recherché découle maintenant du lemme 3.13 ci-dessous. □
Lemme 3.13. Considérons le ˆK -vectoriel Pm, n égal au quotient de O((∂Bm× Bn)†) par les éléments :
ti·∂g
∂ti
, pour g∈ O((∂Bm× Bn)†) et i∈[[1, m]];
∂h
∂z j
− h|z j=1+ h|z j=0, pour h∈ O((∂Bm× Bn)†) et j∈[[1, n]].
Alors, dans Pm, n, la classe d’une fonction f∈ O((∂Bm× Bn)†) est égale à celle de la fonction constante
donnée par ∫ 1
0
···
∫ 1
0
cc( f)· dz1··· dzn.
Nouvelles cohomologies de Weil en caractéristique positive 1781
Démonstration. Étant donnée une fonction f∈ O((∂Bm× Bn)†), on note cm( f)∈ O((∂Bm−1× Bn)†) le
coefﬁcient de t0
m dans f vue comme élément de O((∂Bm−1× Bn)†){tm, t−1
m}. Clairement, f− cm( f) est
dans l’image de l’opérateurtm· ∂
∂tm
. Une récurrence simple montre alors que f et cc( f)= c1◦···◦ cm( f)
ont même classe dans Pm, n. Ainsi, on peut supposer que m= 0.
L’opérateur ∂
∂zn
est surjectif sur O((Bn)†). On peut donc trouver h∈ O((Bn)†) tel que ∂h
∂zn
= f . Il
s’ensuit que la classe de f dans P0, n est égale à celle de h|zn=1− h|zn=0∈ O((Bn−1)†). Une récurrence
simple permet maintenant de conclure. □
3C. Constructions des nouvelles réalisations. On achève ici les constructions des nouvelles réalisations
en combinant les constructions de la sous-section 2E avec la (−1)-connexité des complexes AK , AK, B et
AK,𝓁 . On rappelle que K est de caractéristique nulle et qu’on ne fait pas d’hypothèses sur la caractéristique
de k. On ﬁxe une Q-algèbre3.
Déﬁnition 3.14. Fixons un morphisme d’anneaux3→ K . La nouvelle réalisation de type de Rham sur
RigDA´et(ˆK;3) est le foncteur
Rnew: RigDA´et(ˆK;3)→ D(AK) (3-17)
déﬁni comme étant la composition de
RigDA´et(ˆK;3)
RK
(2-49)
// Ho(Mod(AK))
AK⊗AK−
(3-8)
// D(AK) (3-18)
où RK est le foncteur de l’exemple 2.36 ; voir la remarque 3.11. La nouvelle réalisation de type de Rham
sur DA´et(k;3) est le foncteur
Rnew◦ rel: DA´et(k;3)→ D(AK). (3-19)
Les deux foncteurs (3 -17) et (3-19) sont monoïdaux. Lorsque cela n’entraîne pas confusion, on écrit
« Rnew » au lieu de « R new◦ rel ».
Remarque 3.15. Les réalisations nouvelles de type de Rham permettent de retrouver la réalisation de
de Rham surconvergente sur RigDA´et(ˆK;3) ainsi que la réalisation rigide à la Berthelot sur DA´et(k;3).
Plus précisément, on a des triangles commutatifs
RigDA´et(ˆK;3)
Rnew //
RdR **
D(AK)
ˆK⊗AK−

D(ˆK)
et DA´et(k;3)
Rnew //
RBert ))
D(AK)
ˆK⊗AK−

D(ˆK)
(3-20)
à isomorphismes naturels près. Ceci découle aussitôt des triangles (2 -51) et (2 -60). Les réalisations
nouvelles de type de Rham permettent aussi de retrouver les réalisations 𝓁-adiques, pour𝓁 différent de la
caractéristique de k. Plus précisément, en ﬁxant certaines données comme dans la remarque 2.39, on a
1782 Joseph Ayoub
également des triangles commutatifs
RigDA´et(ˆK;3)
Rnew //
Q𝓁⊗Q𝓁 R𝓁 **
D(AK)
Q𝓁⊗AK−

D(Q𝓁)
et DA´et(k;3)
Rnew //
Q𝓁⊗Q𝓁 R𝓁 ))
D(AK)
Q𝓁⊗AK−

D(Q𝓁)
(3-21)
à isomorphismes naturels près.
Déﬁnition 3.16. (1) On ﬁxe un plongement complexeσ: K↪→ C. On déﬁnit les nouvelles réalisations
de type Betti
Rnew, B: RigDA´et(ˆK;3)→ D(AK, B) et R new, B◦ rel: DA´et(k;3)→ D(AK, B) (3-22)
en remplaçant « RK », « AK » et « AK » par « RK, B », « AK, B » et « AK, B » dans la déﬁnition 3.14.
(2) On ﬁxe une clôture algébrique K/K , un nombre premier𝓁 et un morphisme d’anneaux3→ Q𝓁.
On déﬁnit les nouvelles réalisations de type𝓁-adique
Rnew,𝓁: RigDA´et(ˆK;3)→ D(AK,𝓁) et R new,𝓁◦ rel: DA´et(k;3)→ D(AK,𝓁) (3-23)
en remplaçant « RK », « AK » et « AK » par « RK,𝓁 », « AK,𝓁 » et « AK,𝓁 » dans la déﬁnition 3.14.
Lorsque cela n’entraîne pas confusion, on écrit « Rnew, B/𝓁 » au lieu de « R new, B/𝓁◦ rel ».
Remarque 3.17. Soit𝓁 un nombre premier différent de la caractéristique de k et ﬁxons une clôture
algébrique de ˆK (ce qui détermine une clôture algébrique de K ). Fixons aussi un morphisme d’anneaux
3→ Q𝓁. Alors les nouvelles réalisations de type 𝓁-adique permettent de retrouver les réalisations
𝓁-adiques sur RigDA´et(ˆK;3) et DA´et(k;3). Plus précisément, on a des triangles commutatifs
RigDA´et(ˆK;3)
Rnew,𝓁 //
R𝓁 **
D(AK,𝓁)
Q𝓁⊗AK,𝓁−

D(Q𝓁)
et DA´et(k;3)
Rnew,𝓁 //
R𝓁 **
D(AK,𝓁)
Q𝓁⊗AK,𝓁−

D(Q𝓁)
(3-24)
à isomorphismes naturels près. Ceci découle aussitôt des triangles (2-57) et (2-61).
Remarque 3.18. Les nouvelles réalisations introduites dans les déﬁnitions 3.14 et 3.16 se comparent
entre elles. En effet, sous les hypothèses de la remarque 2.39, on a une chaîne de quasi-isomorphismes
C⊗K AK≃ C⊗3 AK, B≃ Q𝓁⊗3 AK, B≃ Q𝓁⊗Q𝓁 AK,𝓁 (3-25)
ainsi qu’une chaîne d’isomorphismes naturels
C⊗K Rnew(−)≃ C⊗3 Rnew, B(−)≃ Q𝓁⊗3 Rnew, B(−)≃ Q𝓁⊗Q𝓁 Rnew,𝓁(−) (3-26)
entre foncteurs déﬁnis sur RigDA´et(ˆK;3). Ceci découle aussitôt de (2-58) et (2-59).
Nouvelles cohomologies de Weil en caractéristique positive 1783
3D. Quelques conjectures. Dans cette sous-section, on énonce trois conjectures. La première porte sur
le complexe AK et les deux autres sur l’anneau AK .
Conjecture 3.19. L’homologie du complexeAK est nulle sauf en degré zéro.
Conjecture 3.20. L’anneauAK est intègre.
Conjecture 3.21. Le morphisme
∫
: AK→ ˆK est injectif lorsque l’extension K/Q est algébrique.
V oici quelques remarques sur ces conjectures.
Remarque 3.22. La conjecture 3.19 est une variante de [Ayoub 2014b, §2.4, Conjecture A]. Si l’on
suppose que DA´et(K; K) et RigDA´et(ˆK; K) possèdent des t-structures motiviques pour lesquelles le
foncteur Rig∗ ainsi que les foncteurs de réalisation RdR et R†
dR sont t-exacts, alors la conjecture 3.19 est
vraie. L’argument est le même que celui qui a servi dans la preuve de [Ayoub 2014b, Lemme 2.145] : AK
est la réalisation de de Rham de Rig∗1∈ DA´et(K; K) qui est un objet t-négatif puisque Rig∗ est t-exact
et que 1∈ RigDA´et(ˆK; K) est dans le cœur. Ceci entraîne que Hi(AK)= 0 pour i> 0 ce qui sufﬁt pour
conclure car AK est(−1)-connexe d’après le corollaire 3.8.
Remarque 3.23. La conjecture 3.19 est connue dans le cas suivant : k est de caractéristique nulle et
K= k(ϖ) muni de la valuationϖ -adique. Il s’agit alors de la première assertion dans [Ayoub 2014c,
Théorème 2.49]. (V oir aussi le deuxième erratum.)
Remarque 3.24. Une version plus faible de la conjecture 3.20 afﬁrmerait que l’anneau AK est connexe.
Malheureusement, même la connexité semble hors de porté (pour K d’inégales caractéristiques). Il
convient de noter ici que la K -algèbre AK contient une clôture algébrique de K dans ˆK . Ainsi, la
K -algèbre AK n’est pas géométriquement connexe en général, mais il est raisonnable de conjecturer
qu’elle est géométriquement connexe (et même géométriquement intègre) lorsque K est algébriquement
clos dans ˆK .
Remarque 3.25. La conjecture 3.21 est évidement une version p-adique (avec p la caractéristique de k)
de la fameuse conjecture des périodes de Kontsevich et Zagier [2001, §4.1] comme reformulée dans
[Ayoub 2015b, Conjecture 1.1]. Il s’agit donc d’une conjecture de transcendance p-adique qui, de nos
jours, semble des plus difﬁciles. Cependant, remarquons que
∫
: AK→ ˆK est bien injectif lorsque k est
de caractéristique nulle et que K= k(ϖ) muni de la valuationϖ -adique ; il s’agit en effet de [Ayoub
2019, Théorème 1.7].
Remarque 3.26. La conjecture 3.21 entraîne la conjecture 3.20 pour K algébrique sur Q et on peut bien
imaginer que le cas général s’y ramène, du moins pour K d’inégales caractéristiques. Remarquons aussi
que [Ayoub 2019, Théorème 1.7] entraîne que la conjecture 3.20 est vraie lorsque k est de caractéristique
nulle et que K= k(ϖ) muni de la valuationϖ -adique.
1784 Joseph Ayoub
