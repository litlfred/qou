---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-082-4-action-du-groupe-de-galois-motivique
section_title: "Action du groupe de Galois motivique"
section_number: 4
pages: 118-121
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
Tout au long de la section, on ﬁxe un corps K muni d’une valuation de hauteur 1 et on note ˆK son
complété. On désigne par K◦ et ˆK◦ les anneaux de valuation de K et ˆK , et on note k le corps résiduel
de K◦ qu’on identiﬁe à celui de ˆK◦. On suppose que la caractéristique de K est nulle et on ne fait pas
d’hypothèses sur la caractéristique de k. On ﬁxe une Q-algèbre3.
Ici, nous allons munir la nouvelle réalisation de type Betti Rnew, B d’une action du groupe de Galois
motivique de K . On ﬁxe une fois pour toute un plongement complexe σ: K ↪→ C et on note Gmot(K)=
Gmot(K,σ; Q) le groupe de Galois motivique associé à σ ; voir [Ayoub 2014b, Déﬁnition 2.106].
Rappelons que Gmot(K) est un Q-schéma en groupes afﬁne (i.e., un pro-groupe algébrique linéaire
déﬁni sur Q) qui agit sur les 3-modules Hi(RB(M)) pour tout M∈ DA´et(K;3) et i∈ Z. En particulier,
Gmot(K) agit sur la 3-algèbre AK, B= H0(RB(Rig∗3)). Étant donné M∈ RigDA´et(ˆK;3), Gmot(K)
agit également sur les Hi(Rnew, B(M))= Hi(RB(Rig∗M)), pour i∈ Z, et cette action est compatible
à la structure de AK, B-module sur Hi(Rnew, B(M)). (Ceci découle aussitôt du fait que ladite structure
de module provient de l’action naturelle de l’algèbreRig∗3 sur Rig∗M.) On obtient ainsi un foncteur
homologique
H0(Rig∗(−)): RigDA´et(ˆK;3)→ Rep(Gmot(K); AK, B) (4-1)
à valeurs dans la catégorie abélienne des AK, B-modules munis d’une action semi- AK, B-linéaire de
Gmot(K). Ladite catégorie abélienne est équivalente à la catégorie QCoh(XK, B) des modules quasi-
cohérents sur le champs d’Artin
XK, B=[ Gmot(K)\Spec(AK, B)]. (4-2)
L’objectif principal de cette section est de montrer que le foncteur homologique (4-1) provient naturelle-
ment d’un foncteur triangulé monoïdal
~Rnew, B: RigDA´et(ˆK;3)→ DQC(XK, B) (4-3)
à valeurs dans la catégorie homotopique des dg-modules quasi-cohérents sur le champs XK, B.
4A. Rappels et compléments sur [Ayoub 2017]. Dans [Ayoub 2017], nous avons construit un foncteur
Bti∗: DA´et(K;3)→ HocoMod(Hmot(K);3) (4-4)
à valeurs dans les comodules homotopiques sur l’algèbre de Hopf motivique. Dans cette sous-section,
nous allons rappeler et généraliser la construction de (4-4). (Il convient de noter ici qu’un foncteur comme
ci-dessus a été construit par Nori [Fakhruddin 2000], et on s’attend bien entendu à ce que les deux
foncteurs soient compatibles modulo l’isomorphisme des groupes de Galois motiviques de [Choudhury et
Gallauer Alves de Souza 2017, Theorem 9.1].)
Nouvelles cohomologies de Weil en caractéristique positive 1785
Notation 4.1. Dans [Ayoub 2017, §7], on a construit une monade pseudo-monoïdale aSingD
´et de la
catégorie
Spt♯
T
(
Cpl(PSh(Sm/K;3))
)
(4-5)
qui modélise la monade pseudo-monoïdale Bti∗Bti∗ de la catégorie homotopique DA´et(K;3) ; voir
[Ayoub 2017, Lemma 7.14, Theorem 7.16]. Dans la suite, nous écrivons « SgD
´et » au lieu de « aSingD
´et »
aﬁn d’alléger les notations. La description explicite de SgD
´et ne sera pas utile ici et nous nous abstenons de
la rappeler. On note ˆSgD
´et l’endofoncteur pseudo-monoïdal consimplicial de la catégorie (4-5) associé à
SgD
´et comme dans [Ayoub 2017, Construction 3.9].
Soit 1ﬁb un remplacement stablement(A1,´et)-ﬁbrant de l’algèbre commutative Sus0
T,♯(Qcst) dans la
catégorie (4-5). D’après [Ayoub 2017, Theorem 8.3], la dg-algèbre cosimpliciale
Hmot(K;3)=0(K;ˆSgD
´et(1ﬁb)) (4-6)
est une Q-algèbre de Hopf homotopique au sens de [Ayoub 2017, Deﬁnition 2.1]. De plus, étant donné un
1ﬁb-module E qui est stablement(A1,´et)-ﬁbrant (en tant que T -spectre commutatif), le Hmot(K)-module
Bti∗(E)=0(K;ˆSgD
´et(E)) (4-7)
est un comodule homotopique. Ceci permet de déﬁnir un foncteur monoïdal (4-4) qui factorise la réalisation
de Betti. On utilisera la généralisation suivante de cette construction.
Construction 4.2. On suppose donnée une algèbre commutative R dans la catégorie (4 -5). Quitte à
remplacer R par une algèbre stablement (A1,´et)-localement équivalente, on peut supposer que R est une
3ﬁb-algèbre stablement (A1,´et)-ﬁbrante. (Ici 3ﬁb est un remplacement stablement (A1,´et)-ﬁbrant de
l’algèbre commutative Sus0
T,♯(3cst) qu’on suppose muni d’une structure de1ﬁb-algèbre.)
Le comodule homotopique Bti∗(R)=0(K;ˆSgD
´et(R)) est naturellement une algèbre commutative dans
la catégorie des comodules homotopiques sur Hmot(K). De plus, étant donné un R-module E stablement
(A1,´et)-ﬁbrant, le comodule homotopique Bti∗(E) est naturellement un module sur Bti∗(R). Autrement
dit, on dispose d’un foncteur triangulé monoïdal
Bti∗: DA´et(K; R)→ HocoMod(Hmot(K); Bti∗(R)) (4-8)
vers la catégorie homotopique des comodules homotopiques sur Hmot(K) munis d’une action de l’algèbre
cosimpliciale Bti∗(R) compatible à celle de Hmot(K).
Pour aller plus loin, on fait l’hypothèse suivante sur R.
Hypothèse 4.3. Le complexe Bti∗(R) est(−1)-connexe, i.e., Hi(Bti∗(R))= 0 pour i⩽−1.
Proposition 4.4. (i) Le complexe Hmot(K)(n) est(−1)-connexe pour tout n∈ N.
(ii) Sous l’hypothèse 4.3, le complexe Bti∗(R)(n) est(−1)-connexe pour tout n∈ N.
1786 Joseph Ayoub
Démonstration. Étant donné que l’algèbre cosimpliciale Hmot(K) est une algèbre de Hopf homotopique,
on a des quasi-isomorphismes canoniques
Hmot(K)(n)≃ Hmot(K)
L⊗n.
L’assertion (i) découle alors de la(−1)-connexité du complexe Hmot(K) ; voir [Ayoub 2014b, Corol-
laire 2.105]. Par ailleurs, étant donné que Bti∗(R) est un comodule homotopique sur Hmot(K), on a des
quasi-isomorphismes canoniques
Bti∗(R)(n)≃ Bti∗(R) L⊗ Hmot(K)(n),
ce qui fournit l’assertion (ii). □
Construction 4.5. Grâce à la proposition 4.4(i), on dispose de deux morphismes de Q-algèbres de Hopf
homotopiques :
Hmot(K)
q.-i.oo τ>0Hmot(K)→ H0(Hmot(K))= B(Hmot(K)) (4-9)
et le premier est un quasi-isomorphisme. Bien entendu,Hmot(K)= H0(Hmot(K)) et B(−) désigne le fonc-
teur « objet cosimplicial classiﬁant associé à une bialgèbre » comme dans [Ayoub 2017, Construction 1.1].
On pose :
Bti′∗(−)= B(Hmot(K)) L⊗τ>0Hmot(K) Bti∗(−). (4-10)
On déduit de (4-9) un foncteur monoïdal
B(Hmot(K))
L
⊗
τ>0Hmot(K)
−: HocoMod(Hmot(K); Bti∗(R))→ HocoMod
(
B(Hmot(K)); Bti′∗(R)
)
.
(4-11)
En composant (4-8) et (4-11), on obtient un foncteur monoïdal
Bti′∗: DA´et(K; R)→ HocoMod
(
B(Hmot(K)); Bti′∗(R)
)
. (4-12)
Supposons maintenant que l’hypothèse 4.3 est satisfaite. Le complexe cosimplicial Bti′∗(R) est alors
(−1)-connexe en chaque degré cosimplicial (utiliser la proposition 4.4(ii)). Ainsi, on dispose de deux
morphismes de comodules homotopiques sur B(Hmot(K)) :
Bti′∗(R)
q.-i.oo τ>0Bti′∗(R)→ H0(Bti′∗(R)) (4-13)
et le premier est un quasi-isomorphisme. On pose :
A= H0(Bti′∗(R)). (4-14)
On déduit de (4-13) un foncteur monoïdal
A L⊗τ>0Bti′∗(R)−: HocoMod
(
B(Hmot(K)); Bti′∗(R)
)
→ HocoMod
(
B(Hmot(K)); A
)
. (4-15)
En composant (4-12) et (4-15), on obtient un foncteur monoïdal
Bti′′∗: DA´et(K; R)→ HocoMod
(
B(Hmot(K)); A
)
. (4-16)
Nouvelles cohomologies de Weil en caractéristique positive 1787
Par construction, les foncteurs (4-12) et (4-16) commutent aux sommes directes quelconques.
À ce stade, il convient de noter le résultat bien connu suivant.
Lemme 4.6. Soit k un corps de caractéristique nulle et soit G un k-schéma en groupes afﬁne agissant sur
une k-algèbre A. Alors , on dispose d’un foncteur triangulé monoïdal
B: D(Rep(G); A)→ HocoMod
(
B(O(G)); B(A)
)
(4-17)
qui commute aux sommes quelconques. De plus, les catégories source et but dans (4-17) possèdent des
t-structures naturelles pour lesquelles le foncteurB est t-exact. Enﬁn, le foncteur B induit une équivalence
B: D(Rep(G); A)+→ HocoMod
(
B(O(G)); B(A)
)+ (4-18)
entre les sous-catégories des complexes bornés à gauche.
Démonstration. Il s’agit d’un cas particulier de [Gaitsgory et Rozenblyum 2017, Chapter I.3, §2.4,
Proposition 2.4.3]. En effet, la catégorieHocoMod(B(O(G)); B(A)) s’identiﬁe à la catégorie homotopique
des dg-modules quasi-cohérents sur le champs d’ArtinX=[ G\Spec(A)] désignée par « QCoh(X) » dans
[Gaitsgory et Rozenblyum 2017]. □
Dans [Ayoub 2017, page 1508] nous avons afﬁrmé que le foncteur
D
(
Rep(Gmot(K);3)
)
→ HocoMod
(
B(Hmot(K));3
)
était pleinement ﬁdèle, ce qui n’est pas justiﬁé. (La pleine ﬁdélité découlerait de la ﬁnitude de la dimension
cohomologique de Gmot(K) conjecturée si l’extension K/Q est de type ﬁni.) Le lemme 4.6 permet de
réparer cette afﬁrmation si l’on se restreint aux complexes bornés à gauche. En particulier, on a le résultat
suivant.
Corollaire 4.7. On suppose que l’hypothèse 4.3 est satisfaite et on poseA= H0(Bti∗(R)). Alors, Gmot(K)
agit sur la3-algèbre A et on dispose d’un foncteur triangulé monoïdal
~RB: DA´et
ct(K; R)→ Db(
Rep(Gmot(K); A)
)
(4-19)
qui factorise la restriction de (4-16) aux motifs constructibles.
Démonstration. Le foncteur (4-16) commute aux sommes quelconques et il associe à un motif constructible
M∈ DA´et(K; R) un comodule homotopique Bti′′∗(M) sur B(Hmot(K)) tel que Bti′′∗(M)(0)= Bti∗(M)
est un complexe parfait de A-modules et en particulier borné à gauche. Le résultat recherché est alors une
conséquence immédiate du lemme 4.6. □
