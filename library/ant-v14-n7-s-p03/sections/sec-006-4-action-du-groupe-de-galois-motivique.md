---
doc_id: ant-v14-n7-s-p03
doc_title: "Nouvelles cohomologies de Weil en caractéristique positive"
section_id: sec-006-4-action-du-groupe-de-galois-motivique
section_title: "Action du groupe de Galois motivique"
section_number: 4
pages: 38-44
source_pdf: ant-v14-n7-s-p03.pdf
source_sha256: e32fde16c3ce0940
doc_brief: "Nouvelles cohomologies de Weil en caractéristique positive — periods” admitting an explicit description by generators and relations."
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
4B. Le cas de la nouvelle réalisation de type Betti. Ici, on spécialise les constructions décrites dans la
sous-section 4A au cas qui nous intéresse. On ﬁxe un plongement complexe σ: K↪→ C. On rappelle que
la nouvelle réalisation de type Betti
Rnew, B: RigDA´et(ˆK;3)→ D(AK, B)
1788 Joseph Ayoub
est déﬁnie comme étant la composition de
RigDA´et(ˆK;3)
~Rig∗
∼
// DA´et(K; Rig∗3ﬁb)
RB // Ho(Mod(AK, B))
AK, B⊗AK, B−
// D(AK, B).
On peut enrichir cette nouvelle réalisation d’une action du groupe de Galois motivique comme suit.
Construction 4.8. Considérons le3-champs d’Artin :
XK, B=[ Gmot(K)\Spec(AK, B)]. (4-20)
La catégorie homotopique DQC(XK, B) des dg-modules quasi-cohérents sur XK, B s’identiﬁe à celle des
comodules homotopiques sur B(Hmot(K)) munis d’une structure de modules sur B(AK, B) :
DQC(XK, B)= HocoMod(B(Hmot(K)); B(AK, B)). (4-21)
En prenant R= Rig∗3ﬁb dans la construction 4.5, on obtient donc un foncteur monoïdal
Bti′′∗: DA´et(K; Rig∗3ﬁb)→ DQC(XK, B). (4-22)
On déﬁnit le foncteur monoïdal
~Rnew, B: RigDA´et(ˆK;3)→ DQC(XK, B) (4-23)
comme étant la composition de
RigDA´et(ˆK;3)
~Rig∗
∼
// DA´et(K; Rig∗3ﬁb)
Bti′′∗
// DQC(XK, B). (4-24)
Par construction, le foncteur~Rnew, B factorise le foncteur Rnew, B.
Proposition 4.9. Il existe un foncteur monoïdal
~Rnew, B: RigDA´et
ct(ˆK;3)→ Db(QCoh(XK, B)) (4-25)
qui factorise la restriction de (4-24) aux motifs rigides constructibles.
Démonstration. Il s’agit d’un cas particulier du corollaire 4.7. □
4C. Quelques conjectures. On ﬁxe un plongement complexe σ: K ↪→ C et on suppose que 3= Q.
Dans cette sous-section, on énonce deux conjectures. La première porte sur l’action du groupe de Galois
motivique Gmot(K) sur Spec(AK, B). La deuxième concerne le foncteur (4-25).
Conjecture 4.10. L’action deGmot(K) sur le Q-schéma Spec(AK, B) est transitive.
Remarque 4.11. La conjecture 4.10 est équivalente à chacune des deux assertions suivantes.
(a) Le Q-champs d’Artin XK, B est une gerbe.
(b) La catégorie Coh(XK, B) des modules quasi-cohérents de type ﬁni sur XK, B est tannakienne.
Nouvelles cohomologies de Weil en caractéristique positive 1789
En fait, il est naturel de considérer la catégorie Coh(XK, B) comme un candidat pour la catégorie
tannakienne des motifs mixtes rigides sur ˆK . On s’attend aussi à ce que la catégorie tannakienne des
motifs mixtes sur k s’identiﬁe à la sous-catégorie pleine de Coh(XK, B) formée des objets à bonne
réduction. (Lorsque la valuation de K est discrète, on peut déﬁnir la notion de « bonne réduction » dans
Coh(XK, B) via les réalisations𝓁-adiques : on demande que le groupe d’inertie de ˆK agisse trivialement.)
Proposition 4.12. La conjecture 4.10 entraîne que les nombres de Betti𝓁-adiques des motifs mixtes sur k
ne dépendent pas de𝓁.
Démonstration. On ﬁxe un motif M∈ DA´et
ct(k; Q). Si le Q-champs d’Artin XK,B est une gerbe, les
AK, B-modules Hi(Rnew, B(M)), pour i∈ Z, sont libres de rang constant sur Spec(AK, B). Le résultat
recherché découle alors des théorèmes de comparaison (voir les remarques 3.18 et 3.17). □
Il est également naturel de faire la conjecture suivante qui renforce la remarque 4.11.
Conjecture 4.13. La catégorie Coh(XK, B) est abélienne (ce qui est le cas si la conjecture 4.10 est vraie)
et le foncteur (4-25) induit une équivalence de catégories :
RigDA´et
ct(ˆK; Q)−→∼ Db(Coh(XK, B)). (4-26)
Bibliographie
[Ayoub 2007] J. Ayoub, Les six opérations de Grothendieck et le formalisme des cycles évanescents dans le monde motivique, II,
Astérisque 315, Soc. Math. France, Paris, 2007. MR Zbl
[Ayoub 2014a] J. Ayoub, “La réalisation étale et les opérations de Grothendieck”, Ann. Sci. École Norm. Sup.(4) 47:1 (2014),
1–145. MR Zbl
[Ayoub 2014b] J. Ayoub, “L’algèbre de Hopf et le groupe de Galois motiviques d’un corps de caractéristique nulle, I”,J. Reine
Angew. Math. 693 (2014), 1–149. MR Zbl
[Ayoub 2014c] J. Ayoub, “L’algèbre de Hopf et le groupe de Galois motiviques d’un corps de caractéristique nulle, II”,J. Reine
Angew. Math. 693 (2014), 151–226. Corrections en 693 (2014), e1–e2 et 693 (2014), 227–230. MR Zbl
[Ayoub 2015a] J. Ayoub, Motifs des variétés analytiques rigides, Mém. Soc. Math. France (N.S.) 140-141, Soc. Math. France,
Paris, 2015. MR Zbl
[Ayoub 2015b] J. Ayoub, “Une version relative de la conjecture des périodes de Kontsevich–Zagier”,Ann. of Math.(2) 181:3
(2015), 905–992. MR Zbl
[Ayoub 2017] J. Ayoub, “From motives to comodules over the motivic Hopf algebra”, J. Pure Appl. Algebra 221:7 (2017),
1507–1559. MR Zbl
[Ayoub 2019] J. Ayoub, “La version relative de la conjecture des périodes de Kontsevich–Zagier revisitée”, Tohoku Math. J.(2)
71:3 (2019), 465–485. MR Zbl
[Bambozzi et Vezzani 2019] F. Bambozzi et A. Vezzani, “Rigidity for rigid analytic motives”,J. Inst. Math. Jussieu (publié en
ligne en septembre 2019).
[Berthelot 1986] P. Berthelot, “Géométrie rigide et cohomologie des variétés algébriques de caractéristique p”, pp. 7–32 dans
Introductions aux cohomologies p-adiques (Marseille, France, 1984), édité par D. Barsky et P. Robba, Mém. Soc. Math. France
(N.S.) 23, Soc. Math. France, Paris, 1986. MR Zbl
[Choudhury et Gallauer Alves de Souza 2017] U. Choudhury et M. Gallauer Alves de Souza, “An isomorphism of motivic
Galois groups”, Adv. Math. 313 (2017), 470–536. MR Zbl
1790 Joseph Ayoub
[Cisinski et Déglise 2012] D.-C. Cisinski et F. Déglise, “Mixed Weil cohomologies”, Adv. Math. 230:1 (2012), 55–130. MR
Zbl
[Deligne 1980] P. Deligne, “La conjecture de Weil, II”, Inst. Hautes Études Sci. Publ. Math. 52 (1980), 137–252. MR Zbl
[Fakhruddin 2000] N. Fakhruddin, “Notes of Nori’s lectures on mixed motives”, notes de cours, Tata Inst. Fund. Res., 2000.
[Fontaine 1994] J.-M. Fontaine, “Le corps des périodes p-adiques”, pp. 59–111 dans Périodes p-adiques (Bures-sur-Yvette,
France, 1988), édité par J.-M. Fontaine, Astérisque 223, Soc. Math. France, Paris, 1994. MR Zbl
[Friedlander 1982] E. M. Friedlander, Étale homotopy of simplicial schemes, Ann. Math. Studies 104, Princeton Univ. Press,
1982. MR Zbl
[Gaitsgory et Rozenblyum 2017] D. Gaitsgory et N. Rozenblyum, A study in derived algebraic geometry, I: Correspondences
and duality, Math. Surv. Monogr. 221, Amer. Math. Soc., Providence, RI, 2017. MR Zbl
[Große-Klönne 2000] E. Grosse-Klönne, “Rigid analytic spaces with overconvergent structure sheaf”, J. Reine Angew. Math.
519 (2000), 73–95. MR Zbl
[Große-Klönne 2004] E. Große-Klönne, “De Rham cohomology of rigid spaces”, Math. Z. 247:2 (2004), 223–240. MR Zbl
[Grothendieck 1966] A. Grothendieck, “On the de Rham cohomology of algebraic varieties”, Inst. Hautes Études Sci. Publ.
Math. 29 (1966), 95–103. MR Zbl
[Huber 1996] R. Huber, Étale cohomology of rigid analytic varieties and adic spaces , Aspects Math. 30, Vieweg & Sohn,
Braunschweig, 1996. MR Zbl
[Isaksen 2004] D. C. Isaksen, “Étale realization on the A1-homotopy theory of schemes”, Adv. Math. 184:1 (2004), 37–63. MR
Zbl
[Kleiman 1968] S. L. Kleiman, “Algebraic cycles and the Weil conjectures”, pp. 359–386 dans Dix exposés sur la cohomologie
des schémas, édité par A. Grothendieck et N. H. Kuiper, Adv. Stud. Pure Math. 3, North-Holland, Amsterdam, 1968. MR Zbl
[Kontsevich et Zagier 2001] M. Kontsevich et D. Zagier, “Periods”, pp. 771–808 dansMathematics unlimited : 2001 and beyond,
édité par B. Engquist et W. Schmid, Springer, 2001. MR Zbl
[Milne et Ramachandran 2004] J. S. Milne et N. Ramachandran, “Integral motives and special values of zeta functions”, J. Amer.
Math. Soc. 17:3 (2004), 499–555. MR Zbl
[Riou 2005] J. Riou, “Dualité de Spanier–Whitehead en géométrie algébrique”, C. R. Math. Acad. Sci. Paris 340:6 (2005),
431–436. MR Zbl
[SGA 43 1973] M. Artin, A. Grothendieck et J. L. Verdier, Théorie des topos et cohomologie étale des schémas, Tome 3:
Exposés IX–XIX (Séminaire de Géométrie Algébrique du Bois Marie 1963–1964), Lecture Notes in Math. 305, Springer, 1973.
MR Zbl
[SGA 5 1977] A. Grothendieck, Cohomologie l-adique et fonctions L (Séminaire de Géométrie Algébrique du Bois Marie
1965–1966), Lecture Notes in Math. 589, Springer, 1977. MR Zbl
[Vezzani 2018] A. Vezzani, “The Monsky–Washnitzer and the overconvergent realizations”,Int. Math. Res. Not. 2018:11 (2018),
3443–3489. MR Zbl
[V oevodsky 2010] V . V oevodsky, “Cancellation theorem”,Doc. Math. Suslin birthday volume (2010), 671–685. MR Zbl
[White 2017] D. White, “Model structures on commutative monoids in general model categories”, J. Pure Appl. Algebra 221:12
(2017), 3124–3168. MR Zbl
Communicated by Kiran S. Kedlaya
Received 2018-12-21 Revised 2019-12-17 Accepted 2020-02-06
joseph.ayoub@math.uzh.ch Institut für Mathematik, Universität Zürich, Switzerland
CNRS LAGA, Université Paris 13, France
mathematical sciences publishers msp
