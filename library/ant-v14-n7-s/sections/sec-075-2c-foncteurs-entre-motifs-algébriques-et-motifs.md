---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-075-2c-foncteurs-entre-motifs-algébriques-et-motifs
section_title: "2C. Foncteurs entre motifs algébriques et motifs rigides"
section_number: null
pages: 99-102
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
foncteurs entre motifs algébriques et motifs rigides. Tout au long de la sous-section, on ﬁxe un corps K
muni d’une valuation de hauteur 1 et on note ˆK son complété. On désigne par K◦ et ˆK◦ les anneaux de
valuation de K et ˆK , et on note k le corps résiduel de K◦ qu’on identiﬁe à celui de ˆK◦.
On dispose d’un foncteur d’analytiﬁcation
Rig: Sm/K→ SmRig/ˆK (2-26)
qui envoie un K -schéma lisse X sur la ˆK -variété analytique rigide associée à X⊗K ˆK et qu’on notera
simplement X anr. Ce foncteur induit une adjonction de Quillen
Rig∗: Spt♯
T
(
Cpl(PSh(Sm/K;3))
) //oo Spt♯
T anr
(
Cpl(PSh(SmRig/ˆK;3))
)
: Rig∗ (2-27)
relativement aux structures(A1,´et)-locale et(B1,´et)-locale stables. En passant aux catégories homoto-
piques, on obtient donc une adjonction triangulée
Rig∗: DA´et(K;3) //oo RigDA´et(ˆK;3): Rig∗. (2-28)
1766 Joseph Ayoub
Les foncteurs Rig∗ dans (2-27) et (2 -28) sont monoïdaux, et leurs adjoints à droite Rig∗ sont donc
pseudo-monoïdaux. Dans la construction ci-dessous, on généralise l’adjonction de Quillen (2-27) à des
catégories de modules ; cette généralisation jouera un rôle clef dans la suite.
Construction 2.24. On suppose donnés :
— une algèbre commutative R dans la catégorie monoïdale des T -spectres commutatifs sur Sm/K
(i.e., dans la source de l’adjonction (2-27)),
— une algèbre commutative R′ dans la catégorie monoïdale des T anr-spectres commutatifs sur
SmRig/ˆK (i.e., dans le but de l’adjonction (2-27)),
— un morphisme d’algèbres θ: Rig∗(R)→ R′.
On dispose alors d’un couple de foncteurs adjoints
θRig∗: Mod(R) //oo Mod(R′):θRig∗ (2-29)
où le foncteur θRig∗ envoie un R-module M sur le R′-module R′⊗Rig∗(R) Rig∗(M). En fait, grâce à
[White 2017, Theorem 3.2, Theorem 4.1], les catégories Mod(R) et Mod(R′) héritent des structures de
modèles(A1,´et)-locale et(B1,´et)-locale stables, et l’adjonction (2-29) est alors de Quillen. On pose :
DA´et(K; R)= HoA1-´et-st(Mod(R)) et RigDA´et(ˆK; R′)= HoB1-´et-st(Mod(R′)). (2-30)
L’adjonction de Quillen (2-29) induit ainsi une adjonction triangulée
θRig∗: DA´et(K; R) //oo RigDA´et(ˆK; R′):θRig∗. (2-31)
Les foncteurs θRig∗ dans (2-29) et (2-31) sont monoïdaux, et leurs adjoints à droite θRig∗ sont donc
pseudo-monoïdaux.
Situation 2.25. Plus tard, nous utiliserons la construction 2.24 avec un choix particulier des données
R, R′ etθ, que nous décrivons maintenant. On prendra R= Rig∗3ﬁb et R′= 3ﬁb, où 3ﬁb désigne un
remplacement stablement(B1,´et)-ﬁbrant de l’objet unité6∞
T anr,♯(3cst) vu comme algèbre commutative.
On prendra pourθ le morphisme de counité
δ: Rig∗Rig∗3ﬁb→ 3ﬁb.
Étant donné que l’algèbre 3ﬁb est(B1,´et)-localement stablement équivalente à l’objet unité, il découle
de [White 2017, Theorem 4.1(2)] que la catégorie RigDA´et(ˆK; 3ﬁb) est équivalente à RigDA´et(ˆK;3).
L’adjonction (2-31) induit donc une adjonction triangulée
~Rig∗: DA´et(K; Rig∗3ﬁb) //oo RigDA´et(ˆK;3):~Rig∗ (2-32)
avec~Rig∗ la composition de δRig∗ et l’équivalence susmentionnée. Le foncteur~Rig∗ est monoïdal et son
adjoint à droite~Rig∗ est donc pseudo-monoïdal.
On passe maintenant à la construction d’un autre foncteur reliant motifs algébriques et motifs rigides,
à savoir le foncteur « relèvement ». La construction de ce foncteur passe par la catégorie FDA´et(ˆK◦;3)
Nouvelles cohomologies de Weil en caractéristique positive 1767
des motifs de ˆK◦-schémas formels qu’on rappelle d’abord. SoitSmF/ˆK◦ la catégorie des ˆK◦-schémas
formels, adiques et lisses qu’on munit de la topologie étale. On note B1,◦ et∂B1,◦ les complétés formels
adiques des K◦-schémas A1
K◦ et E1
K◦. La catégorie FDA´et(ˆK◦;3) est déﬁnie comme étant la catégorie
homotopique de
Spt♯
T rig,◦
(
Cpl(PSh(SmF/ˆK◦;3))
)
(2-33)
munie de sa structure(B1,◦,´et)-locale stable, avec
T rig,◦=(∂B1,◦, 1)⊗3[−1]. (2-34)
On dispose de deux foncteurs
η: SmF/ˆK◦→ SmRig/ˆK et σ: SmF/ˆK◦→ Sm/k
qui à un ˆK◦-schéma formel adique lisse X associent sa ﬁbre générique Xη et sa ﬁbre spéciale Xσ
respectivement. Ces foncteurs induisent des adjonctions de Quillen
η∗: Spt♯
T rig,◦
(
Cpl(PSh(SmF/ˆK◦;3))
) //oo Spt♯
T rig
(
Cpl(PSh(SmRig/ˆK;3))
)
:η∗ (2-35)
et σ∗: Spt♯
T rig,◦
(
Cpl(PSh(SmF/ˆK◦;3))
) //oo Spt♯
T
(
Cpl(PSh(Sm/k;3))
)
:σ∗ (2-36)
relativement aux structures (B1,◦,´et)-locale,(B1,´et)-locale et (A1,´et)-locale stables. En passant aux
catégories homotopiques, on obtient deux adjonctions triangulées
η∗: FDA´et(ˆK◦;3) //oo RigDA´et(ˆK;3):η∗ et σ∗: FDA´et(ˆK◦;3) //oo DA´et(k;3):σ∗. (2-37)
Les foncteursη∗ etσ∗ ci-dessus sont monoïdaux. La construction du foncteur « relèvement » repose sur
le résultat suivant.
Proposition 2.26. L’adjonction(2-36) est une équivalence de Quillen. En particulier, le foncteur
σ∗: DA´et(k;3)→ FDA´et(ˆK◦;3)
est une équivalence monoïdale.
Démonstration. Il s’agit d’un cas particulier de [Ayoub 2015a, Corollaire 1.4.24]. □
Notation 2.27. La composition de
DA´et(k;3)
σ∗
∼
// FDA´et(ˆK◦;3)
η∗
// RigDA´et(ˆK;3)
est le foncteur « relèvement » qu’on note rel: DA´et(k;3)→ RigDA´et(ˆK;3). Ce foncteur est monoïdal
d’après la proposition 2.26.
1768 Joseph Ayoub
