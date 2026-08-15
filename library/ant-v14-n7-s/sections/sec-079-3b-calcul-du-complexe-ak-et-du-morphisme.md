---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-079-3b-calcul-du-complexe-ak-et-du-morphisme
section_title: "3B. Calcul du complexe AK et du morphisme"
section_number: null
pages: 111-115
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
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
