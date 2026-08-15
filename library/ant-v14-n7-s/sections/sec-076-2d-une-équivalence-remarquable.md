---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-076-2d-une-équivalence-remarquable
section_title: "2D. Une équivalence remarquable"
section_number: null
pages: 102-104
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Notre but ici est de démontrer le résultat remarquable suivant qui est aussi un ingrédient principal de la
construction de la nouvelle cohomologie de Weil0new(−/K) (voir le théorème 1.5 de l’introduction).
Théorème 2.28. Reprenons les notations de la situation 2.25. L’adjonction
δRig∗: Mod(Rig∗3ﬁb) //oo Mod(3ﬁb):δRig∗ (2-38)
est une équivalence de Quillen. En particulier, le foncteur
~Rig∗: RigDA´et(ˆK;3)→ DA´et(K; Rig∗3ﬁb)
est une équivalence monoïdale.
Pour la preuve du théorème 2.28, on utilise le résultat suivant.
Lemme 2.29. (Formule de coprojection) Le morphisme évident
(Rig∗M′)⊗ N→ Rig∗(M′⊗ Rig∗N) (2-39)
est un isomorphisme pour tout M′∈ RigDA´et(ˆK;3) et N∈ DA´et(K;3).
Démonstration. On se ramène aussitôt au cas où N est constructible, et donc fortement dualisable d’après
[Riou 2005] (voir aussi [Ayoub 2015a, Lemme 1.3.29]). Le résultat recherché est alors une conséquence
formelle du fait que Rig∗ est monoïdal, voir [Ayoub 2014b, Lemme 2.8]. □
Proposition 2.30. Le foncteur~Rig∗ dans (2-32) est pleinement ﬁdèle.
Démonstration. Il s’agit de montrer que le morphisme d’unité
E→δRig∗
δRig∗E (2-40)
est un isomorphisme pour tout E∈ DA´et(K; Rig∗3ﬁb). Il sufﬁt de montrer cela pour E appartenant à une
classe d’objets qui engendre la catégorie triangulée avec sommes inﬁnies DA´et(K; Rig∗3ﬁb). On peut
donc supposer que E=(Rig∗3ﬁb)⊗ N pour un certain N∈ DA´et(K;3). Dans ce cas, le morphisme
(2-40) s’identiﬁe au morphisme de coprojection
(Rig∗3ﬁb)⊗ N→ Rig∗(3ﬁb⊗ Rig∗N)
qui est bien inversible d’après le lemme 2.29. □
Pour terminer la preuve du théorème 2.28, il reste à voir que l’image du foncteur~Rig∗ engendre toute la
catégorie triangulée avec sommes inﬁnies RigDA´et(ˆK;3). Or, la sous-catégorie triangulée avec sommes
inﬁnies engendrée par l’image de~Rig∗ coïncide avec celle engendrée par l’image du foncteur Rig∗ (dans
(2-28)). Le théorème 2.28 découle donc du résultat suivant.
Proposition 2.31. La catégorie triangulée avec sommes inﬁnies RigDA´et(ˆK;3) est engendrée par
l’image du foncteurRig∗: DA´et(K;3)→ RigDA´et(ˆK;3).
Nouvelles cohomologies de Weil en caractéristique positive 1769
Démonstration. Aﬁn de faciliter les références, nous utiliserons dans cette preuve les motifs avec transferts
(voir les remarques 2.1 et 2.13). Étant données les équivalences de catégories
DA´et(K;3)≃ DM(K;3) et RigDA´et(ˆK;3)≃ RigDM(ˆK;3),
il sufﬁt de démontrer la proposition pour les motifs effectifs avec transferts. Lorsque K= ˆK , il s’agit de
[Ayoub 2015a, Théorème 2.5.35]. Le cas plus général dont on a besoin n’est guère plus difﬁcile et on se
contente de survoler la preuve de [loc. cit., Théorème 2.5.35] en signalant les quelques modiﬁcations
qu’il faut apporter.
On note provisoirement S(K)⊂ RigDMeff(ˆK;3) la sous-catégorie triangulée avec sommes inﬁnies
engendrée par l’image de Rig∗ ou, ce qui revient au même, par les motifs effectifs de la forme Meff(X anr)
avec X un K -schéma projectif et lisse. D’après [loc. cit., Théorème 2.5.34], il sufﬁt de montrer que
Meff(U) appartient à S(K) pour U une ˆK -variété rigide quasi-compacte admettant potentiellement bonne
réduction. On raisonne par récurrence sur la dimension de U.
Soit L/K une extension ﬁnie séparable. Posons ˆL= ˆK⊗K L ; c’est uneˆK -algèbre étale, qui s’écrit
donc comme un produit ﬁni de corps valués complets ˆL=∏
i∈ IˆLi. ChaqueˆLi contient une copie Li
de L et s’identiﬁe en fait à la complétion de Li pour une valuation qui étend celle de K . On se ramène
facilement à montrer que le motif effectif Meff(U⊗ˆKˆL)∈ RigDMeff(ˆL;3) est dans la sous-catégorie
triangulée avec sommes inﬁnies S(L)⊂ RigDMeff(ˆL;3) engendrée par l’image de
Rig∗: DMeff(L;3)→ RigDMeff(ˆL;3).
(Remarquer que le foncteur (ˆL/L)♯ envoie S(L) dans S(K).) Il revient au même de montrer que le
motif effectif Meff(U⊗ˆKˆLi)∈ RigDMeff(ˆLi;3) est dans la sous-catégorie S(Li), i.e., il est loisible de
remplacer K par les Li et ˆK parˆL. De même, si K′/K est une extension ﬁnie purement inséparable,
on peut aussi remplacer K par K′ et ˆK parˆK′ ; voir [loc. cit., page 335] pour un argument. Au ﬁnal,
ceci montre qu’il est loisible de remplacer K par L, pour une extension ﬁnie quelconque L/K , quitte à
considérer tous les prolongements possibles de la valuation de K à L. Comme application de ce principe,
on peut supposer que U admet bonne réduction, i.e., qu’il existe un isomorphisme U≃ Uη avec U un
ˆK◦-schéma formel lisse.
Comme dans l’étape 1 de la preuve de [loc. cit., Théorème 2.5.35], on se ramène au cas où la valuation
de K est discrète. L’étape 2 de la preuve de [loc. cit., Théorème 2.5.35] s’étend littéralement et permet
de remplacer Uη par(U r Z)η pour un tout fermé Z⊂ Uσ de codimension partout non nulle. (Ceci
utilise l’hypothèse de récurrence sur la dimension de U.) Dans l’étape 3 de la preuve de [loc. cit.,
Théorème 2.5.35], on fera attention à choisir les polynômes fi∈ ˆK◦[t1,..., tn, u1,..., ur] à coefﬁcients
dans K◦, ce qui est clairement possible. Le reste de l’étape 3 s’étend alors pour fournir un K◦-schéma
projectif X à réduction semi-stable de type (1,..., 1) et tel que U est un ouvert lisse du complété adique
X de X. Grâce à l’étape 2, on peut même supposer que U est le lieu lisse de X. L’étape 4 de la preuve de
[loc. cit., Théorème 2.5.35] s’étend alors littéralement et permet de conclure. □
1770 Joseph Ayoub
