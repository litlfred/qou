---
doc_id: aif-2000-50-4-1021-0
doc_title: "Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie"
section_id: sec-013-131-un-algorithme-de-réduction
section_title: "Un algorithme de réduction"
section_number: 1.3.1
pages: 18-20
source_pdf: AIF_2000__50_4_1021_0.pdf
source_sha256: a7ca398590a266d8
toc_source: inferred
doc_brief: "Systèmes aux q-différences singuliers réguliers : classification, matrice de connexion et monodromie — 41 sections: Front matter; Comportement de la matrice de conn; Introduction et notations"
---
Appelons uniformisante un élément u e M.(C) dont 0 est zéro simple,
autrement dit dont la valuation voÇu) en 0 vaut 1. Nous établirons d'abord
un lemme très utile. Il s'agit en fait d'un algorithme de réduction analogue
à l'algorithme du pivot de Gauss, valable dans tout anneau de valuation
discrète.
LEMME. — Toute matrice M e GLn(M(C)) peut s'écrire sous la
forme M = CR^ avec des matrices (7, R ç GL^A^C)) telles que :
(i) R est régulière en 0 (i.e. R(0) e GLn(C)) ;
(ii) C est produit :
1) d'une puissance u^, —k e N d'une uniformisante u arbitraire'^
2) de matrices Ti^a d'opérations élémentaires sur les lignes',
3) de matrices de dilatation P^, où les uniformisantes v sont
arbitraires (et choisies indépendamment les unes des autres).
Pour être précis, les matrices mentionnées sont définies comme suit.
La matrice T^a (a ç C77', 0.1 -^ 0) est égale à l'identité, sauf en ce qui
TOME 50 (2000), FASCICULE 4
1038
JACQUES SAULOY
concerne la ligne de rang i :
T.
/ 1
0
ai
V o
0
1
<^2
0
... 
0
... 
0
... 
Oi
... 
0
... 
0 \
... 
0
... an
... 
1 
1
L'inverse d'une telle matrice est une matrice de même forme. La matrice de
dilatation D^y est diagonale et est égale à l'identité, sauf en ce qui concerne
le coefficient de rang i :
D
1
0
0
0
0
1
0
0
... 
0
... 
0
V
... 
0
... 
0 \
... 
0
... 
0
... 
1 
1
Le lemme dit alors que l'on peut écrire :
C=ukT^D^^^T^D^
où u, z»i,..., v^ sont des uniformisantes arbitrairement choisies.
On commence par multiplier M par une puissance v^ d'uniformisante,
de manière à la rendre holomorphe en 0 : cela revient à se ramener à ce cas,
et l'on doit alors prouver le lemme avec k = 0 dans la conclusion. Puis l'on
fait une récurrence sur î;o(det M). Si cette valuation vaut 0, M est régulière
en 0 et l'on prend R = M et C = 1^ (produit vide).
Si î;o(det M) > 0, la matrice M(0) est singulière et il existe donc
(3 e C71 - {0} tel que /3M(0) = 0 e C71.
Soit i un indice tel que ^ ^ 0 et soit v une uniformisante quelconque. Alors
M! = ^J^,^ es^ holomorphe en 0 et detMi = (A/^)detM; Mi est
meilleure que M : vo(det Mi) = vo(det M) - 1, ce qui achève la récurrence.
Les Ti^ de l'énoncé sont alors les T^ (qui sont bien de cette forme !). 
D
COROLLAIRE 1. — Dans le lemme, on peut obtenir C e GLn(C(z)) et
de plus régulière en oo, Le. G(oo) e GL^(C).
Il suffit pour cela de prendre chaque ^ égal à z / ( l 4- z). 
n
ANNALES DE L'INSTITUT FOURIER
SYSTÈMES AUX ^-DIFFÉRENCES SINGULIERS RÉGULIERS 
1039
COROLLAIRE 2 («double réduction))). — Soient C ' . C " € GLn(C(z)).
Il existe alors U e GLn(C(z)) telle que UC' est régulière en 0 et VC11 est
régulière en oo.
On applique ce qui précède à M == (C'^^C' que l'on écrit donc sous
la forme CR avec C, R ç. GLn(C(^)), C régulière en oo et R régulière en 0.
On prend alors U == C-1^")-1 : UC' == R est régulière en 0, UC11 = C-1
est régulière en oo et, bien sur, U 6 GLn(C(z)). 
D
Outre ce qui suit, ce lemme et ses corollaires nous serviront au
paragraphe 2 pour caractériser globalement les systèmes singuliers réguliers.
