---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-074-2b-rappels-sur-les-motifs-rigides-et-leurs-cohom
section_title: "2B. Rappels sur les motifs rigides et leurs cohomologies"
section_number: null
pages: 95-99
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
complet pour une valuation de hauteur1. Soit S une k-variété analytique rigide. On dispose d’une catégorie
triangulée de motifs rigides sur S à coefﬁcients dans 3, notée RigDA´et(S;3). Aﬁn de ﬁxer les notations,
nous rappelons brièvement la construction de cette catégorie.
On commence d’abord par la variante effective, notéeRigDAeff,´et(S;3). C’est une catégorie triangulée
déﬁnie comme étant la catégorie homotopique de
Cpl(PSh(SmRig/S;3)) (2-14)
munie de sa structure de modèles(B1,´et)-locale. Ladite structure s’obtient à partir de la structure´et-locale
par localisation de Bousﬁeld suivant la classe des morphismes de la forme B1
X⊗3[n]→ X⊗3[n],
pour X∈ SmRig/S et n∈ Z. Les équivalences faibles de la structure(B1,´et)-locales sont appelées les
équivalences(B1,´et)-locales. La catégorie (2-14) est monoïdale et sa structure monoïdale est compatible
à ses deux structures de modèles susmentionnées. En particulier, la catégorie trianguléeRigDAeff,´et(S;3)
est monoïdale.
Passons maintenant à la variante stable, notée RigDA´et(S;3). C’est une catégorie triangulée déﬁnie
comme étant la catégorie homotopique de
Spt♯
T
(
Cpl(PSh(SmRig/S;3))
)
(2-15)
1762 Joseph Ayoub
munie de sa structure de modèles (B1,´et)-locale stable. Il y a plusieurs choix équivalents pour T , et dans
cet article on prendra T= T rig ou T= T anr avec
T rig=(∂B1, 1)⊗3[−1] et T anr=(E1, anr, 1)⊗3[−1]. (2-16)
(Bien entendu, E1, anr désigne la variété analytique rigide associée E1.) La catégorie (2 -15) est celle
des T -spectres commutatifs en complexes de préfaisceaux sur SmRig/S. La structure (B1,´et)-locale
stable est la structure projective stable sur (2 -15) déduite de la structure (B1,´et)-locale ; voir [Ayoub
2017, Deﬁnition 4.16]. Les équivalences faibles de la structure (B1,´et)-locale stable sont appelées les
équivalences(B1,´et)-locales stables. La catégorie (2 -15) est monoïdale et sa structure monoïdale est
compatible à la structure (B1,´et)-locale stable d’après [Ayoub 2017, Proposition 4.20]. En particulier, la
catégorie triangulée RigDA´et(S;3) est monoïdale.
On dispose d’un foncteur de Quillen à gauche
6∞
T,♯: Cpl(PSh(SmRig/S;3))→ Spt♯
T
(
Cpl(PSh(SmRig/S;3))
)
(2-17)
qui à un complexe de préfaisceauxF associe le T -spectre de suspension inﬁnie6∞
T,♯(F)={ Sn(T)⊗F}n∈N.
Le foncteur (2-17) est monoïdal et il induit un foncteur triangulé
6∞
T,♯: RigDAeff,´et(S;3)→ RigDA´et(S;3) (2-18)
qui est aussi monoïdal.
Remarque 2.13. Plus tard et notamment dans la sous-section 3A, on aura aussi besoin des variantes avec
transferts des catégories RigDAeff,´et(S;3) et RigDA´et(S;3) introduites ci-dessus. Ces catégories sont
notées respectivement
RigDMeff(S;3) et RigDM(S;3).
La catégorie RigDM(eff)(S;3) est construite de la même manière que RigDA(eff,)´et(S;3) en utilisant
les préfaisceaux avec transferts sur SmRig/S au lieu des préfaisceaux ordinaires, i.e., en remplaçant
partout dans la construction « PSh(SmRig/S;3) » par « PST(SmRig/S;3) ». Lorsque S est normal,
on dispose d’une équivalence de catégories RigDA´et(S;3)≃ RigDM(S;3) ; voir [Bambozzi et Vezzani
2019, Theorem 3.8].
Remarque 2.14. Comme dans le cas des motifs algébriques, la catégorie RigDA´et(S;3) est originelle-
ment construite en utilisant les T -spectres symétriques. Comme dans la remarque 2.2, le théorème 2.3
entraîne que l’approche via les T -spectres commutatifs et celle via les T -spectres symétriques mènent à
des catégories de motifs rigides équivalentes. (En effet, la validité de la condition (i) du théorème 2.3
pour les objets (2-16) découle de la validité de la même condition pour l’objet (2-3).)
Dans la suite de la sous-section, on se restreint au cas où S= Spm(k). On peut facilement adapter la
déﬁnition d’une cohomologie de Weil au contexte rigide.
Déﬁnition 2.15. Soit A une Q-algèbre. Une cohomologie de Weil rigide à coefﬁcients dans A (on dira
aussi déﬁnie sur A) est un préfaisceau de A-dg-algèbres0W sur SmRig/k vériﬁant les conditions suivantes.
Nouvelles cohomologies de Weil en caractéristique positive 1763
(1) Le morphisme unité A→0W(X) est un quasi-isomorphisme pour X= Spm(k) et X= B1.
(2) Le complexe de A-modules0W(P1, anr,∞) est quasi-isomorphe à A[−2].
(3) (Formule de Künneth) Pour tout X, Y∈ SmRig/k, le morphisme évident
0W(X)
L
⊗A0W(Y)→0W(X×k Y)
est un quasi-isomorphisme.
(4) Le complexe de préfaisceaux 0W est ﬁbrant pour la topologie étale (i.e., admet la descente étale).
Étant donnée une cohomologie de Weil rigide0W , on pose H∗
W(X)= H∗(0W(X)) pour X∈ SmRig/k.
Remarque 2.16. Il découle des conditions (1) et (4) de la déﬁnition 2.15 que le morphisme unité
A→0W(A1, anr) est aussi un quasi-isomorphisme. En particulier, une cohomologie de Weil rigide 0W
déﬁnit, par restriction suivant le foncteur d’analytiﬁcation (−)anr: Sm/k→ SmRig/k, une cohomologie
de Weil au sens de la déﬁnition 1.1.
On ﬁxe une cohomologie de Weil rigide 0W à coefﬁcients dans une 3-algèbre A. Comme dans la
sous-section 2A, nous allons maintenant expliquer comment représenter la théorie cohomologique 0W
dans les catégories de motifs rigides. On commence avec une remarque évidente.
Remarque 2.17. La cohomologie de Weil rigide 0W , vue comme un complexe de préfaisceaux sur
SmRig/k, déﬁnit un objet de RigDAeff,´et(k;3). En fait, le complexe de préfaisceaux 0W est(B1,´et)-
ﬁbrant comme il découle aussitôt de la déﬁnition 2.15. Il s’ensuit que 0W∈ RigDAeff,´et(k;3) représente
la théorie cohomologique0W au sens suivant : il existe un quasi-isomorphisme
0W(X)≃ RHom RigDAeff,´et(k;3)(Meff(X),0 W) (2-19)
naturel en X∈ SmRig/k. (Bien entendu, Meff(X) est le motif effectif associé à X, i.e., le préfaisceau
X⊗3[0] considéré comme un objet de RigDAeff,´et(k;3).)
Construction 2.18. On associe à la cohomologie de Weil rigide0W un T -spectre 0W sur SmRig/k de
la manière suivante. En niveau n∈ N, le T -spectre 0W est donné par le complexe de préfaisceaux 0W(n).
Le A-module libre H2
W(P1, anr)(1)≃ H1
W(E1, anr)(1)≃ H1
W(∂B1)(1) admet un générateur canonique, et
on ﬁxe un morphisme de complexes de préfaisceaux γ: T→0W(1) qui représente ce générateur. Le
morphisme d’assemblage en niveau n du T -spectre 0W est alors le morphisme composé
γn: T⊗0W(n)
γ // 0W(1)⊗0W(n)
µ // 0W(n+ 1)
oùµ désigne la multiplication de0W . Étant donné que l’algèbre0W est supposée commutative, il découle
aussitôt de la construction que le T -spectre 0W est commutatif. De plus, 0W est une algèbre commutative
de la catégorie monoïdale (2 -15) (avec S= Spm(k)) et déﬁnit donc une algèbre commutative dans la
catégorie monoïdale RigDA´et(k;3).
1764 Joseph Ayoub
Remarque 2.19. Le T -spectre commutatif 0W est stablement (B1,´et)-ﬁbrant : on a déjà vu dans la
remarque 2.17 qu’il était (B1,´et)-ﬁbrant niveau par niveau, et il découle des conditions (2) et (3) de
la déﬁnition 2.15 que 0W est un-spectre. Il s’ensuit que 0W∈ RigDA´et(k;3) représente la théorie
cohomologique0W au sens suivant : il existe un quasi-isomorphisme
0W(X)≃ RHom RigDA´et(k;3)(M(X), 0W) (2-20)
naturel en X∈ SmRig/k. (Bien entendu, M(X) est le motif associé à X, i.e., le T -spectre6∞
T,♯(X⊗3[0])
considéré comme un objet de RigDA´et(k;3).)
On peut également associer à 0W une réalisation homologique.
Proposition 2.20. Soit R un objet de RigDA´et(k;3) muni d’une structure de 0W -module. Alors, la
composition de
0W⊗A R0(k; R)→ 0W⊗A R→ R (2-21)
est un isomorphisme. (La première ﬂèche est induite par le morphisme évident6∞
T,♯ R0(k; R)cst→ R et
la seconde ﬂèche est donnée par l’action de0W sur R. )
Démonstration. Il s’agit de la variante analytique rigide de la proposition 2.8. La preuve de [Ayoub
2019, Proposition 2.11] et l’esquisse de preuve de la proposition 2.8 s’étendent littéralement au contexte
rigide. □
Corollaire 2.21. L’association M↝ R0(k; 0W⊗ M) s’étend en un foncteur monoïdal
RW: RigDA´et(k;3)→ D(A). (2-22)
(C’est la réalisation homologique associée à0W .)
Démonstration. Il s’agit de la variante analytique rigide du corollaire 2.9 qui découle de la proposition 2.20
de la même manière que ledit corollaire découle de la proposition 2.8. □
On termine la sous-section avec deux exemples classiques de cohomologies de Weil rigides.
Exemple 2.22. Lorsque k est de caractéristique nulle, on dispose d’une cohomologie de Weil rigide0†
dR
à coefﬁcients dans k appelée la cohomologie de de Rham surconvergente0†
dR (voir [Große-Klönne 2004]).
Pour la construire, nous reposons sur un travail de Vezzani [2018]. Notons SmRig†/k la catégorie des
k-variétés analytiques rigides lisses avec structure de surconvergence (au sens de [Große-Klönne 2000,
§2]). On dispose d’un complexe de de Rham surconvergent• sur SmRig†/k. Soit0dR un remplacement
´et-ﬁbrant de • considéré comme une algèbre commutative dans la catégorie monoïdale
Cpl(PSh(SmRig†/k; k)). (2-23)
(On utilise ici [White 2017, Theorem 3.2].) Alors,0dR est une cohomologie de Weil rigide sur SmRig†/k,
i.e., satisfait aux conditions de la déﬁnition 2.15 en remplaçant « SmRig/k » par « SmRig†/k ». (La
formule de Künneth pour 0dR est établie dans [Große-Klönne 2000, Theorem 4.12].) En particulier,
Nouvelles cohomologies de Weil en caractéristique positive 1765
le complexe de préfaisceaux 0dR est (B1,´et)-ﬁbrant. (Bien entendu, B1 est muni de sa structure de
surconvergence évidente induite par l’inclusion B1⊂ A1, anr.)
On dispose d’un foncteurl: SmRig†/k→ SmRig/k donné par l’oubli de la structure de surconvergence.
Ce foncteur induit une adjonction de Quillen
l∗: Cpl(PSh(SmRig†/k; k)) //oo Cpl(PSh(SmRig/k; k)): l∗. (2-24)
relativement aux structures(B1,´et)-locales et, d’après [Vezzani 2018, Theorem 4.23], cette adjonction
est en fait une équivalence de Quillen, i.e., induit une équivalence
RigDAeff,´et(k; k)≃ RigDAeff,´et, †(k; k) (2-25)
entre les catégories de motifs rigides construites à partir deSmRig/k et SmRig†/k. Ceci étant, il est naturel
de prendre pour0†
dR un remplacement(B1,´et)-ﬁbrant de l∗(•)cof, où(•)cof désigne un remplacement
coﬁbrant de •. (Bien entendu, les remplacements ﬁbrants et coﬁbrants sont pris dans les catégories
d’algèbres commutatives, ce qui est possible grâce à [White 2017, Theorem 3.2, Proposition 3.5].) Par
construction, l’équivalence de catégories (2 -25) échange 0†
dR et 0dR. Ceci entraîne que 0†
dR est une
cohomologie de Weil rigide et que, pour X∈ SmRig/k, le complexe0†
dR(X) calcule bien la cohomologie
de de Rham surconvergente de X (comme déﬁnie dans [Große-Klönne 2004]).
Exemple 2.23. Soit𝓁 un nombre premier différent de la caractéristique résiduelle de k. En ﬁxant une
clôture séparable ksep/k, on dispose d’une cohomologie de Weil rigide0𝓁 à coefﬁcients dans Q𝓁 appelée
la cohomologie𝓁-adique. On peut construire 0𝓁 en adaptant la construction donnée dans l’exemple 2.12.
Les détails sont laissés au lecteur.
