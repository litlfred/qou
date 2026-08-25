---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-077-2e-constructions-principales
section_title: "2E. Constructions principales"
section_number: null
pages: 104-109
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
ici le théorème 2.28 pour construire certains foncteurs monoïdaux de RigDA´et(ˆK;3) à valeurs dans
des catégories de modules sur des dg-algèbres commutatives. Pour cela, on doit d’abord généraliser la
construction de la réalisation homologique associée à une cohomologie de Weil.
Construction 2.32. Soit0W (resp.0W′) une cohomologie de Weil (resp. de Weil rigide) à coefﬁcients
dans une 3-algèbre A (resp. A′) déﬁnie sur Sm/K (resp. SmRig/ˆK ). Soit R (resp. R′) une algèbre
commutative dans
Spt♯
T(Cpl(PSh(Sm/K;3))) ( resp. Spt♯
T(Cpl(PSh(SmRig/K;3)))).
On ﬁxe un remplacement coﬁbrant (0W)cof (resp.(0W′)cof) de l’algèbre commutative 0W (resp. 0W′),
et on ﬁxe ensuite un remplacement (A1,´et)-ﬁbrant (resp. un remplacement (B1,´et)-ﬁbrant) 0W, R (resp.
0W′, R′) de l’algèbre commutative(0W)cof⊗ Rcof (resp.(0′
W)cof⊗ R′
cof). On pose :
B=0(K; 0W, R) (resp. B′=0(ˆK; 0W′, R′)).
Par construction, B (resp. B′) est une 3-dg-algèbre commutative et, en tant qu’objet de D(A) (resp.
D(A′)), elle est donnée par la réalisation homologiqueRW(R) (resp. RW′(R′)) de R (resp. R′). On dispose
d’une adjonction de Quillen
0W(′), R(′)⊗R(′)−: Mod(R(′)) //oo Mod(0W(′), R(′)): Oub (2-41)
et le foncteur 0W(′), R(′)⊗R(′)− est monoïdal. On dispose d’une autre adjonction de Quillen
0W(′), R(′)⊗B(′)−: Mod(B(′)) //oo Mod(0W(′), R(′)): R0(K;−) (resp. R0(ˆK;−)) (2-42)
et le foncteur 0W(′), R(′)⊗B(′)− est monoïdal. En fait, il découle aussitôt de la proposition 2.8 (resp. la
proposition 2.20) que l’adjonction (2-42) est une équivalence de Quillen. Ceci étant, on déﬁnit un foncteur
monoïdal
RW, R: DA´et(K; R)→ Ho(Mod(B)) (2-43)
en prenant la composition de
DA´et(K; R)
0W, R⊗R− // DA´et(K; 0W, R)
R0(K;−) // Ho(Mod(B)).
(De même, dans le cas respé, on déﬁnit un foncteur monoïdal
RW′, R′: RigDA´et(ˆK; R′)→ Ho(Mod(B′)) (2-44)
en prenant la composition analogue.)
On note le résultat technique suivant.
Lemme 2.33. On reprend les hypothèses et les notations des constructions 2.24 et 2.32. De plus , on
suppose donné un morphisme de cohomologies de Weil
0W→0W′◦(−)anr (2-45)
Nouvelles cohomologies de Weil en caractéristique positive 1771
(voir la remarque 2.16). Alors, il existe un morphisme de A-dg-algèbres B→ B′ tel que le carré
DA´et(K; R)
θ Rig∗

RW, R // Ho(Mod(B))
B′⊗B−

RigDA´et(ˆK; R′)
RW, R′
// Ho(Mod(B′))
commute à un isomorphisme naturel près.
Démonstration. Le morphisme (2-45) induit un morphisme d’algèbres 0W→ Rig∗0W′ et, par adjonction,
un morphisme d’algèbres Rig∗0W→ 0W′. Quitte à choisir convenablement les remplacements coﬁbrants
des algèbres commutatives 0W et 0W′, on peut supposer l’existence d’un carré commutatif
Rig∗(0W)cof

α //(0W′)cof

Rig∗0W // 0W′
Quitte à choisir convenablement les remplacements ﬁbrants, on peut supposer l’existence d’un diagramme
commutatif
Rig∗((0W)cof⊗ R)
∼ //

Rig∗(0W)cof⊗ Rig∗(R)
α⊗θ //(0W′)cof⊗ R′

Rig∗0W, R
θ′
// 0W′, R′
Le morphismeθ′ induit un morphisme de A-dg-algèbres B→ B′, et les deux carrés suivants
Mod(R) //
θ Rig∗

Mod(0W, R)
θ′
Rig∗

Mod(R′) // Mod(0W′, R′)
et
Mod(B) //

Mod(0W, R)
θ′
Rig∗

Mod(B′) // Mod(0W′, R′)
sont commutatifs. Ceci permet de conclure. □
On spécialise maintenant la construction 2.32 à la situation 2.25 et on combine avec le théorème 2.28.
Construction 2.34. Soit0W une cohomologie de Weil déﬁnie sur Sm/K et à coefﬁcients dans une
3-algèbre A. D’après la construction 2.32 appliquée à R= Rig∗3ﬁb (voir la situation 2.25), on dispose
d’un foncteur monoïdal
RW, Rig∗3ﬁb: DA´et(K; Rig∗3ﬁb)→ Ho(Mod(AK,0 W))
avec AK,0 W=0(K; 0W, Rig∗3ﬁb)= R0
(
K;(0W)cof⊗Rig∗3ﬁb
)
. Grâce au théorème 2.28, la composition
de
RigDA´et(ˆK;3)
~Rig∗
∼
// DA´et(K; Rig∗3ﬁb)
RW, Rig∗3ﬁb // Ho(Mod(AK,0 W)),
1772 Joseph Ayoub
fournit un foncteur monoïdal
RK,0 W: RigDA´et(ˆK;3)→ Ho(Mod(AK,0 W)). (2-46)
En précomposant avec le foncteur « relèvement », on obtient également un foncteur monoïdal
RK,0 W◦ rel: DA´et(k;3)→ Ho(Mod(AK,0 W)). (2-47)
Remarquons aussi que AK,0 W , en tant qu’objet de D(A), est donnée par RW(Rig∗3ﬁb), i.e., par la
réalisation homologique du motif Rig∗3.
Proposition 2.35. Soit0W (resp.0W′) une cohomologie de Weil (resp. de Weil rigide) à coefﬁcients dans
une3-algèbre A (resp. A′) déﬁnie sur Sm/K (resp. SmRig/ˆK ). On suppose donné un morphisme de
cohomologies de Weil
0W→0W′◦(−)anr (2-48)
(voir la remarque 2.16). Alors, il existe un morphisme de A-dg-algèbres AK,0 W→ A′ tel que le triangle
RigDA´et(ˆK;3)
RK,0 W //
RW′ ,,
Ho(Mod(AK,0 W))
A′⊗AK,0 W
−

D(A′)
commute à un isomorphisme naturel près.
Démonstration. Le lemme 2.33 fournit un carré commutatif à un isomorphisme naturel près
DA´et(K; Rig∗3ﬁb)
~Rig∗

RW, Rig∗3ﬁb // Ho(Mod(AK,0 W))
A′⊗AK,0 W
−

RigDA´et(ˆK;3)
RW′
// D(A′)
Le résultat recherché découle maintenant de la construction du foncteur RK,0 W . □
On termine la sous-section en discutant quelques exemples.
Exemple 2.36. Supposons que K est de caractéristique nulle et ﬁxons un morphisme d’anneaux3→ K .
Dans la construction 2.34, on peut utiliser la cohomologie de Weil 0dR sur Sm/K de l’exemple 2.10.
La K -dg-algèbre AK,0 dR ne dépend que du corps valué K et sera simplement notée AK . De même, le
foncteur RK,0 dR sera simplement noté RK . Ainsi, on a un foncteur monoïdal
RK: RigDA´et(ˆK;3)→ Ho(Mod(AK)). (2-49)
De plus, quitte à choisir convenablement les remplacements ﬁbrants, on dispose d’un morphisme de
cohomologies de Weil
0dR→0†
dR◦(−)anr
Nouvelles cohomologies de Weil en caractéristique positive 1773
avec0†
dR la cohomologie de Weil rigide de l’exemple 2.22. La proposition 2.35 fournit alors un morphisme
de K -dg-algèbres ∫
: AK→ ˆK (2-50)
ainsi qu’un triangle commutatif
RigDA´et(ˆK;3)
RK //
RdR ++
Ho(Mod(AK))
ˆK⊗AK−

D(ˆK)
(2-51)
à un isomorphisme naturel près. (L’utilisation du symbole d’intégration dans (2-50) anticipe sur le fait
que AK est un complexe de « périodes abstraites adiques », ce qui sera démontré plus tard.)
Exemple 2.37. On ﬁxe un plongement complexeσ: K↪→ C. Dans la construction 2.34, on peut utiliser la
cohomologie de Weil0B sur Sm/K de l’exemple 2.11. La dg-algèbreAK,0 B sera simplement notée AK, B.
De même, le foncteur RK,0 B sera simplement noté RK, B. Ainsi, on a un foncteur monoïdal
RK, B: RigDA´et(ˆK;3)→ Ho(Mod(AK, B)). (2-52)
Fixons un morphisme d’anneaux3→ K . Grâce au théorème de comparaison de Grothendieck [1966] et
en choisissant convenablement les remplacements ﬁbrants, on a un quasi-isomorphisme de cohomologies
de Weil C⊗30B(−)≃ C⊗K0dR(−). On en déduit aussitôt un quasi-isomorphisme de C-dg-algèbres
C⊗3 AK, B≃ C⊗K AK ainsi que des isomorphismes naturels
C⊗3 RK, B(−)≃ C⊗K RK(−) (2-53)
entre foncteurs déﬁnis sur RigDA´et(ˆK;3).
Exemple 2.38. Soit𝓁 un nombre premier différent de la caractéristique de K (mais qui peut être égal à
celle de k) et soit K/K une clôture algébrique de K . Fixons un morphisme d’anneaux3→ Q𝓁. Dans la
construction 2.34, on peut utiliser la cohomologie de Weil0𝓁 sur Sm/K de l’exemple 2.12. La dg-algèbre
AK,0𝓁 sera simplement notée AK,𝓁 . De même, le foncteur RK,0𝓁 sera simplement noté RK,𝓁 . Ainsi, on a
un foncteur monoïdal
RK,𝓁: RigDA´et(ˆK;3)→ Ho(Mod(AK,𝓁)). (2-54)
On ﬁxe un plongementσ: K↪→ C. Grâce au théorème de comparaison d’Artin [SGA 43 1973, exposé XI] et
en choisissant convenablement les remplacements ﬁbrants, on a un quasi-isomorphisme de cohomologies
de Weil Q𝓁⊗30B(−)≃ 0𝓁(−). On en déduit aussitôt un quasi-isomorphisme de Q𝓁-dg-algèbres
Q𝓁⊗3 AK, B≃ AK,𝓁 ainsi que des isomorphismes naturels
Q𝓁⊗3 RK, B(−)≃ RK,𝓁(−) (2-55)
entre foncteurs déﬁnis sur RigDA´et(ˆK;3).
1774 Joseph Ayoub
Supposons de plus que𝓁 est différent de la caractéristique dek et ﬁxons une extension de la valuation de
K à K (ce qui revient au même de se donner une clôture algébrique de ˆK contenant K ). La cohomologie
de Weil 0𝓁 susmentionnée s’identiﬁe alors à la restriction de la cohomologie de Weil rigide 0𝓁 de
l’exemple 2.23. (Ceci découle de [Huber 1996, Theorem 3.8.1].) La proposition 2.35 fournit alors un
morphisme de Q𝓁-dg-algèbres
AK,𝓁→ Q𝓁 (2-56)
ainsi qu’un triangle commutatif
RigDA´et(ˆK;3)
RK,𝓁 //
R𝓁 ++
Ho(Mod(AK,𝓁))
Q𝓁⊗AK,𝓁−

D(Q𝓁)
(2-57)
à un isomorphisme naturel près.
Remarque 2.39. Supposons que K est de caractéristique nulle. Alors, les théorèmes de comparaison entre
cohomologies de Weil classiques fournissent, après extension des scalaires, des quasi-isomorphismes entre
les dg-algèbres AK , AK, B et AK,𝓁 ainsi que des isomorphismes naturels entre les foncteurs RK , RK, B
et RK,𝓁 . Plus précisément, en choisissant un morphisme d’anneaux3→ K , un plongement complexe
σ: K ↪→ C et un isomorphisme Q𝓁≃ C, on a une chaîne de quasi-isomorphismes
C⊗K AK≃ C⊗3 AK, B≃ Q𝓁⊗3 AK, B≃ Q𝓁⊗Q𝓁 AK,𝓁 (2-58)
ainsi qu’une chaîne d’isomorphismes naturels
C⊗K RK(−)≃ C⊗3 RK, B(−)≃ Q𝓁⊗3 RK, B(−)≃ Q𝓁⊗Q𝓁 RK,𝓁(−) (2-59)
entre foncteurs déﬁnis sur RigDA´et(ˆK;3).
Remarque 2.40. Supposons que K est d’inégales caractéristiques(0, p) et ﬁxons un morphisme d’an-
neaux3→ K . Alors, le foncteur composé
RBert: DA´et(k;3) rel // RigDA´et(ˆK;3)
RdR // D(ˆK)
est la réalisation rigide à la Berthelot. (En effet, d’après [Vezzani 2018, Proposition 5.12], ce foncteur
envoie le motif d’un k-schéma lisse X sur le dual de la cohomologie rigide de X.) En précomposant avec
rel dans le triangle (2-51), on obtient un triangle commutatif
DA´et(k;3)
RK◦rel //
RBert ++
Ho(Mod(AK))
ˆK⊗AK−

D(ˆK)
(2-60)
à un isomorphisme naturel près.
Nouvelles cohomologies de Weil en caractéristique positive 1775
Soit 𝓁 un nombre premier différent de la caractéristique de k et ﬁxons un morphisme d’anneaux
3→ Q𝓁. Alors, la composition de
DA´et(k;3) rel // RigDA´et(ˆK;3)
R𝓁 // D(Q𝓁)
coïncide avec la réalisation𝓁-adique sur DA´et(k;3). En précomposant avec rel dans le triangle (2-57),
on obtient un triangle commutatif
DA´et(k;3)
RK,𝓁◦rel //
R𝓁 ++
Ho(Mod(AK,𝓁))
Q𝓁⊗AK,𝓁−

D(Q𝓁)
(2-61)
à un isomorphisme naturel près.
