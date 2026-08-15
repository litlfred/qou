---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-078-3-calcul-du-complexe-des-périodes-abstraites-ak
section_title: "Calcul du complexe des périodes abstraites AK et applications"
section_number: 3
pages: 109-111
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
