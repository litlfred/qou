---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-073-2a-rappels-sur-les-motifs-algébriques-et-leurs-c
section_title: "2A. Rappels sur les motifs algébriques et leurs cohomologies"
section_number: null
pages: 88-95
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
d’une catégorie triangulée de motifs sur S à coefﬁcients dans 3, notée DA´et(S;3). Aﬁn de ﬁxer les
notations, nous rappelons brièvement la construction de cette catégorie.
On commence d’abord par la variante effective, notée DAeff,´et(S;3). C’est une catégorie triangulée
déﬁnie comme étant la catégorie homotopique de
Cpl(PSh(Sm/S;3)) (2-1)
munie de sa structure de modèles(A1,´et)-locale. Ladite structure s’obtient à partir de la structure´et-locale
par localisation de Bousﬁeld suivant la classe des morphismes de la forme A1
X⊗3[n]→ X⊗3[n],
pour X∈ Sm/S et n∈ Z. Les équivalences faibles de la structure (A1,´et)-locales sont appelées les
équivalences(A1,´et)-locales. La catégorie (2-1) est monoïdale et sa structure monoïdale est compatible à
ses deux structures de modèles susmentionnées. En particulier, la catégorie triangulée DAeff,´et(S;3) est
monoïdale.
Nouvelles cohomologies de Weil en caractéristique positive 1755
Passons maintenant à la variante stable, notée DA´et(S;3). C’est une catégorie triangulée déﬁnie
comme étant la catégorie homotopique de
Spt♯
T
(
Cpl(PSh(Sm/S;3))
)
(2-2)
munie de sa structure de modèles (A1,´et)-locale stable. Il y a plusieurs choix équivalents pour T et dans
cet article on prendra
T=(E1, 1)⊗3[−1]. (2-3)
La catégorie (2-2) est celle des T -spectres commutatifs en complexes de préfaisceaux sur Sm/S. (Pour la
notion de spectres commutatifs, on renvoie le lecteur à [Ayoub 2017, §4].) La structure (A1,´et)-locale
stable est la structure projective stable sur (2 -2) déduite de la structure (A1,´et)-locale ; voir [Ayoub
2017, Deﬁnition 4.16]. Les équivalences faibles de la structure (A1,´et)-locale stable sont appelées les
équivalences(A1,´et)-locales stables. La catégorie (2 -2) est monoïdale et sa structure monoïdale est
compatible à la structure (A1,´et)-locale stable d’après [Ayoub 2017, Proposition 4.20]. En particulier, la
catégorie triangulée DA´et(S;3) est monoïdale.
On dispose d’un foncteur de Quillen à gauche
6∞
T,♯: Cpl(PSh(Sm/S;3))→ Spt♯
T
(
Cpl(PSh(Sm/S;3))
)
(2-4)
qui à un complexe de préfaisceauxF associe le T -spectre de suspension inﬁnie6∞
T,♯(F)={ Sn(T)⊗F}n∈N.
(Ici et ailleurs dans le texte, Sn(−) désigne le foncteur « n-ième puissance symétrique ».) Le foncteur
(2-4) est monoïdal et il induit un foncteur triangulé
6∞
T,♯: DAeff,´et(S;3)→ DA´et(S;3) (2-5)
qui est aussi monoïdal.
Remarque 2.1. Plus tard et notamment dans la sous-section 3A, on aura aussi besoin des variantes avec
transferts des catégories DAeff,´et(S;3) et DA´et(S;3) introduites ci-dessus. Ces catégories sont notées
respectivement
DMeff(S;3) et DM(S;3).
La catégorie DM(eff)(S;3) est construite de la même manière que DA(eff,)´et(S;3) en utilisant les
préfaisceaux avec transferts sur Sm/S au lieu des préfaisceaux ordinaires, i.e., en remplaçant partout
dans la construction « PSh(Sm/S;3) » par « PST(Sm/S;3) ». Lorsque S est normal, on dispose d’une
équivalence de catégories DA´et(S;3)≃ DM(S;3) ; voir [Ayoub 2014a, Théorème B.1].
Remarque 2.2. Originellement, la catégorie DA´et(S;3) est construite en utilisant les T -spectres symé-
triques (au lieu des T -spectres commutatifs) ; voir [Ayoub 2007, Déﬁnition 4.5.21]. Lorsque S est un
Q-schéma, il a été montré dans [Ayoub 2017, Remark 4.26] que l’approche via lesT -spectres commutatifs
et celle via les T -spectres symétriques mènent à des catégories monoïdales équivalentes. En fait, ceci
reste vrai sans hypothèses sur S. Toutefois, l’argument donné dans [Ayoub 2017, Remark 4.26] ne sufﬁt
plus dans le cas général car il repose sur le fait que la permutation des facteurs de T⊗ T est l’identité dans
1756 Joseph Ayoub
DAeff,´et(S;3), et la preuve de ceci utilise l’équivalence de catégories DAeff,´et(S;3)≃ DMeff(S;3) qui
est valable uniquement sous l’hypothèse que S est un Q-schéma. Pour un schéma de base général S, on
dispose néanmoins de la version stable de cette équivalence ; voir [Ayoub 2014a, Théorème B.1]. Ceci
permet de montrer que la permutation des facteurs induit l’identité sur 6∞
T (T⊗ T) dans la catégorie
homotopique de
SptT
(
Cpl(PSh(Sm/S;3))
)
relativement à la structure (A1,´et)-locale stable. (Plus précisément, on utilise [Ayoub 2014a, Propo-
sition 3.24] pour se ramener au cas où S est le spectre d’un corps et [Ayoub 2014a, Théorème B.1]
pour se ramener à la question analogue pour les motifs avec transferts sur un corps qui est traitée dans
[V oevodsky 2010, Lemma 4.8].) Ceci étant, l’équivalence entre l’approche via lesT -spectres commutatifs
et celle via les T -spectres symétriques découle maintenant de la généralisation suivante de [Ayoub 2017,
Theorem 4.24] qui peut être omise en première lecture.
Théorème 2.3. Soit M une catégorie de modèles monoïdale vériﬁant [Ayoub 2017, Hypothesis 4.1] et
soit T∈ M un objet coﬁbrant. On suppose que les conditions suivantes sont satisfaites.
(i) Le cycle(123)∈63 agit par l’identité surT⊗3 dans Ho(M) et la transposition(12)∈62 agit par
l’identité sur6∞
T (T⊗2) dans Host(SptT(M)).
(ii) Le foncteur RHom(T,−) commute aux colimites ﬁltrantes dans M.
(iii) L’objet T est isomorphe à une suspension dans Ho(M).
Alors, le foncteur
−/6: Spt6
T(M)→ Spt♯
T(M)
est une équivalence de Quillen à gauche relativement aux structures projectives stables.
Démonstration. Comme dans la preuve de [Ayoub 2017, Theorem 4.24], l’adjoint à droite
Rι: Host(Spt♯
T(M))→ Host(Spt6
T(M))
est pleinement ﬁdèle et il reste à voir qu’il est essentiellement surjectif. D’après [Ayoub 2007, Théo-
rème 4.3.79], le foncteur d’oubli
Oub6: Spt6
T(M)→ SptT(M)
est une équivalence de Quillen à droite. Il est donc sufﬁsant de montrer que le foncteur composé
Host(Spt♯
T(M)) Rι // Host(Spt6
T(M)) ROub6
// Host(SptT(M)) (2-6)
est essentiellement surjectif. Pour ce faire, nous allons montrer que le morphisme de T -spectres
Susp
T(M)→ Susp
T,♯(M) (2-7)
est une équivalence stable pour tout p∈ N et M∈ M coﬁbrant. Expliquons d’abord pourquoi ceci sufﬁt
pour conclure. Le fait que les morphismes (2 -7) soient des équivalences stables entraîne aussitôt que le
Nouvelles cohomologies de Weil en caractéristique positive 1757
foncteur composé Oub6◦ι préserve les équivalences stables et il se dérive donc trivialement. En particulier,
ROub6◦ Rι(Susp
T,♯(M)) est isomorphe à Susp
T,♯(M) vu comme un T -spectre non symétrique. Puisque
(2-7) est une équivalence stable, il s’ensuit que Susp
T,♯(M) est dans l’image du foncteur composé (2-6).
Or, d’après [Ayoub 2017, Lemma 4.21 ; Ayoub 2007, Proposition 4.3.77, Théorème 4.3.79], les foncteurs
Rι et ROub6 sont triangulés et commutent aux sommes inﬁnies. Puisque le foncteur composé (2 -6) est
pleinement ﬁdèle et que les objets de la forme Susp
T(M), pour p∈ N et M∈ M coﬁbrant, engendrent la
catégorie triangulée avec sommes inﬁnies Host(SptT(M)), l’essentielle surjectivité de (2-6) s’ensuit.
Pour terminer la preuve, il reste à voir que le morphisme (2-7) est une équivalence stable. Pour ce faire,
on remarque que le but de ce morphisme s’écrit comme la colimite ﬁltrante de T -spectres M(r), pour
r∈ N, qui sont donnés au niveau n par :
M(r)
n =



0 si 0 ⩽ n⩽ p− 1,
Sn−p(T)⊗ M si p⩽ n⩽ p+ r,
T⊗n−p−r⊗ Sr(T)⊗ M si p+ r+ 1⩽ n.
Il est donc sufﬁsant de montrer que Susp
T(M)= M(0)→ M(r) est une équivalence stable. D’une part,
Susp
T(M) est stablement équivalent à Susp+r
T (T⊗r⊗ M) et, d’autre part, M(r) est stablement équivalent à
Susp+r
T (Sr(T)⊗ M). (On utilise ici [Ayoub 2007, Lemme 4.3.59].) La condition (i) de l’énoncé permet
maintenant de conclure. (Utiliser [Ayoub 2007, Théorème 4.3.79] pour se ramener à la question analogue
pour les T -spectres symétriques et utiliser le fait que Susp+r
T,6((−)⊗ M)≃ Sus0
T,6(−)⊗ Susp+r
T,6(M)
pour se ramener à montrer que Sus 0
T,6(T⊗r)→ Sus0
T,6(Sr(T)) est une équivalence stable.) □
Dans la suite de la sous-section, on se restreint au cas oùS est le spectre d’un corpsk. Nous expliquerons
comment représenter une cohomologie de Weil dans les catégories de motifs. Ceci est dû originellement
à Cisinski et Déglise [2012, §2.1.5] mais nous rappelons leur construction pour la commodité du lecteur.
Jusqu’à la ﬁn de la sous-section, on ﬁxe une cohomologie de Weil 0W à coefﬁcients dans une 3-algèbre
A au sens de la déﬁnition 1.1. (Contrairement à l’introduction, on ne suppose pas ici que k est de
caractéristique p> 0.) On commence avec une remarque évidente.
Remarque 2.4. La cohomologie de Weil0W , vue comme un complexe de préfaisceaux sur Sm/k, déﬁnit
un objet de DAeff,´et(k;3). En fait, le complexe de préfaisceaux0W est(A1,´et)-ﬁbrant comme il découle
aussitôt de la déﬁnition 1.1. Il s’ensuit que 0W∈ DAeff,´et(k;3) représente la théorie cohomologique 0W
au sens suivant : il existe un quasi-isomorphisme
0W(X)≃ RHom DAeff,´et(k;3)(Meff(X),0 W) (2-8)
naturel en X∈ Sm/k. (Bien entendu, Meff(X) est le motif effectif associé à X, i.e., le préfaisceau X⊗3[0]
considéré comme un objet de DAeff,´et(k;3).)
Notation 2.5. D’après la condition (ii) de la déﬁnition 1.1, le A-module H2
W(P1) est libre de rang 1 ; on
le note A(−1). On déﬁnit, pour n∈ Z, le A-module A(n) et le foncteur de twist à la Tate M↝ M(n),
pour M∈ Mod(A), de la manière usuelle.
1758 Joseph Ayoub
Construction 2.6. On associe à la cohomologie de Weil0W un T -spectre 0W sur Sm/k de la manière
suivante. En niveau n∈ N, le T -spectre 0W est donné par le complexe de préfaisceaux 0W(n). Le
A-module libre H2
W(P1)(1)≃ H1
W(E1)(1) admet un générateur canonique, et on ﬁxe un morphisme de
complexes de préfaisceauxγ: T→0W(1) qui représente ce générateur. Le morphisme d’assemblage en
niveau n du T -spectre 0W est alors le morphisme composé
γn: T⊗0W(n)
γ // 0W(1)⊗0W(n)
µ // 0W(n+ 1)
oùµ désigne la multiplication de0W . Étant donné que l’algèbre0W est supposée commutative, il découle
aussitôt de la construction que le T -spectre 0W est commutatif. De plus, 0W est une algèbre commutative
de la catégorie monoïdale (2 -2) (avec S= Spec(k)) et déﬁnit donc une algèbre commutative dans la
catégorie monoïdale DA´et(k;3).
Remarque 2.7. Le T -spectre commutatif 0W est stablement (A1,´et)-ﬁbrant : on a déjà vu dans la
remarque 2.4 qu’il était(A1,´et)-ﬁbrant niveau par niveau, et il découle des conditions (2) et (3) de la
déﬁnition 1.1 que 0W est un-spectre. Il s’ensuit que 0W∈ DA´et(k;3) représente la théorie cohomolo-
gique0W au sens suivant : il existe un quasi-isomorphisme
0W(X)≃ RHom DA´et(k;3)(M(X), 0W) (2-9)
naturel en X∈ Sm/k. (Bien entendu, M(X) est le motif associé à X, i.e., le T -spectre6∞
T,♯(X⊗3[0])
considéré comme un objet de DA´et(k;3).)
Suivant [Cisinski et Déglise 2012, §2.6], on peut associer à 0W une réalisation homologique. Pour
la commodité du lecteur, nous rappelons la construction de cette réalisation. Pour ce faire, on utilise le
résultat suivant.
Proposition 2.8. Soit R un objet deDA´et(k;3) muni d’une structure de0W -module. Alors, la composition
de
0W⊗A R0(k; R)→ 0W⊗A R→ R (2-10)
est un isomorphisme. (La première ﬂèche est induite par le morphisme évident6∞
T,♯ R0(k; R)cst→ R et
la seconde ﬂèche est donnée par l’action de0W sur R. )
Démonstration. Il s’agit d’une généralisation de [Ayoub 2019, Proposition 2.11] (qui elle-même est un cas
particulier de [Cisinski et Déglise 2012, Theorem 2.6.2]). La preuve de [Ayoub 2019, Proposition 2.11]
s’étend littéralement en remplaçant « /k » par « 0W ». Esquissons quand même l’argument.
On procède en deux étapes. Dans la première, on traite le cas où R= 0W⊗A M, avec M∈ DA´et(k; A).
On se ramène aussitôt au cas où M= Hom(X, 1) est le dual fort du motif d’un k-schéma lisse X. Dans
ce cas, on a des identiﬁcations canoniques
0W⊗A M≃ Hom(X, 0W)≃ 0W⊗A0W(X)
qui permettent de conclure. (La seconde identiﬁcation ci-dessus, découle de la formule de Künneth.)
Nouvelles cohomologies de Weil en caractéristique positive 1759
Dans la seconde étape, on construit une section au morphisme (2-10) en prenant la composition de
R→ 0W⊗A R≃ 0W⊗A R0(k; 0W⊗A R)→ 0W⊗A R0(k; R)
où l’isomorphisme au milieu est déduit de la première étape. On montre ensuite que cette composition
est un épimorphisme scindé. (Pour plus de détails, voir la partie B de la preuve de [Ayoub 2019,
Proposition 2.11].) □
Corollaire 2.9. L’association M↝ R0(k; 0W⊗ M) s’étend en un foncteur monoïdal
RW: DA´et(k;3)→ D(A). (2-11)
(C’est la réalisation homologique associée à0W .)
Démonstration. Le foncteur en question est pseudo-monoïdal car il en est ainsi des foncteurs R0(k;−)
et 0W⊗− . Montrons que la transformation binaturelle
R0(k; 0W⊗ M)⊗A R0(k; 0W⊗ N)→ R0(k; 0W⊗(M⊗ N)), (2-12)
est inversible pour tout M, N∈ DA´et(k;3). Pour ce faire, il sufﬁt de montrer que le morphisme
(
0W⊗A R0(k; 0W⊗ M)
)
⊗0W
(
0W⊗A R0(k; 0W⊗ N)
)
→ 0W⊗A R0(k; 0W⊗(M⊗ N)) (2-13)
est inversible. En effet, on retrouve (2-12) en appliquant R0(k;−) à (2-13). Or, grâce à la proposition 2.8,
le morphisme (2-13) s’identiﬁe au morphisme
(0W⊗ M)⊗0W(0W⊗ N)→(0W⊗(M⊗ N)),
et ce dernier est clairement inversible. □
On termine la sous-section avec trois exemples classiques de cohomologies de Weil.
Exemple 2.10. Lorsque k est de caractéristique nulle, on dispose d’une cohomologie de Weil 0dR à
coefﬁcients dans k appelée la cohomologie de de Rham. Elle est construite comme suit. On considère
le complexe de préfaisceaux• sur Sm/k qui associe à un k-schéma lisse les sections globales de son
complexe de de Rham algébrique, i.e.,•(X)=0(X;•
X/k) pour X∈ Sm/k. Le produit extérieur des
formes différentielles fait de• un préfaisceau de dg-algèbres. Le préfaisceau0dR est alors déﬁni comme
étant un remplacement´et-ﬁbrant de•. (On utilise ici l’existence d’une structure de modèles´et-locale
sur les algèbres commutatives dans la catégorie des complexes de préfaisceaux sur Sm/k ; voir [White
2017, Theorem 3.2].) Le T -spectre 0dR est étale localement équivalent niveau par niveau au T -spectre 
considéré dans [Ayoub 2014b, §2.3] et qui est donné en chaque niveau par le complexe de préfaisceaux
•. (V oir aussi [Cisinski et Déglise 2012, §3.1].)
Exemple 2.11. Étant donné un plongement complexeσ: k↪→ C, on dispose d’une cohomologie de Weil
0B à coefﬁcients dans 3 appelée la cohomologie de Betti. Pour expliquer la construction de 0B, on a
besoin d’une digression.
1760 Joseph Ayoub
Considérons l’espace topologique cocubique 6-enrichi□top donné par□n
top=[ 0, 1]n pour n∈ N.
(Pour la notion d’objet cocubique6-enrichi, on renvoie le lecteur à [Ayoub 2014b, Déﬁnition A.12].)
Pour un espace topologique E, on forme l’ensemble cubique 6-enrichi C0(□top, E) des applications
continues des□n
top dans E. On forme ensuite le 3-module cocubique6-enrichi fct(C0(□top, E),3) en
prenant les espaces de fonctions à valeurs dans 3. Enﬁn, on pose :
Asing(E)= A•(
fct(C0(□top, E),3)
)
où A•(−) désigne le complexe alterné associé à un objet cocubique 6-enrichi (voir [loc. cit., Déﬁni-
tion A.20]). Par construction, le3-module cocubique6-enrichi fct(C0(□top, E),3) est pseudo-monoïdal
symétrique au sens de [loc. cit., Déﬁnition A.29]. Il découle de [loc. cit., Lemme A.30] que Asing(E) est
une dg-algèbre commutative.
Ceci étant, le préfaisceau0B associe à un k-schéma lisse X la dg-algèbre Asing(X(C)). Le T -spectre 0B
est quasi-isomorphe niveau par niveau au T -spectre Bti∗3, où Bti∗ désigne l’adjoint à droite du foncteur
de réalisation de Betti noté Bti∗ ; voir [loc. cit., §2.1.2]. Il s’ensuit queBti∗ est naturellement isomorphe au
foncteur de réalisation homologique RB: DA´et(k;3)→ D(3) associé à0B par le corollaire 2.9. Enﬁn, on
rappelle qu’on dispose d’un modèle « explicite » duT -spectre Bti∗3 fourni par [loc. cit., Théorème 2.67].
Exemple 2.12. Soit 𝓁 un nombre premier différent de la caractéristique de k. En ﬁxant une clôture
séparable ksep/k, on dispose d’une cohomologie de Weil0𝓁 à coefﬁcients dans Q𝓁 appelée la cohomologie
𝓁-adique. Une construction de 0𝓁 est proposée dans [Cisinski et Déglise 2012, §3.3] et consiste à
rendre fonctorielle la construction de Deligne du Q𝓁-type d’homotopie d’un schéma [Deligne 1980,
§5.2]. Cependant, l’argument dans [Cisinski et Déglise 2012, §3.3.3] nous semble incomplet. V oici une
construction alternative de0𝓁.
On commence par rappeler quelques notions tirées de [Friedlander 1982] ; voir aussi [Isaksen 2004,
§5, §6] pour un résumé. On ne restreint pas la généralité en supposant que k est algébriquement clos. Un
recouvrement étale rigidiﬁé d’un k-schéma localement de type ﬁni X (non nécessairement quasi-compact)
est la donnée d’un morphisme étale e: Y→ X et d’une section ensemblisteσe: X(k)→ Y(k) telle que
l’application qui envoiex∈ X(k) sur la composante connexe de Y contenantσe(x) est une bijection entre
X(k) et l’ensemble des composantes connexes de Y ; la section σe est appelée une rigidiﬁcation de e.
Un hyper-recouvrement rigidiﬁé d’un k-schéma de type ﬁni X est la donnée d’un hyper-recouvrement
étale Y•→ X et, pour chaque p∈ N, d’une rigidiﬁcation du recouvrement étale Yp→ coskX
p−1(Y)p. La
catégorie des hyper-recouvrements rigidiﬁés de X est notée HRR(X) ; elle est équivalente à un ensemble
ordonné coﬁltrant. Le type d’homotopie étale de X (comme déﬁni par Friedlander [1982]) est le pro-
ensemble simplicial(π0(Y•))Y•∈HRR(X) ; on le note H´et(X). L’associationX↝ H´et(X) est un foncteur
de la catégorie des k-schémas localement de type ﬁni dans celle des pro-ensembles simpliciaux.
Par ailleurs, à un pro-ensemble simplicial E=(Eα)α, on peut associer une Q𝓁-dg-algèbre A𝓁(E) de
la manière suivante. Notons Etop=(Eα
top)α la réalisation topologique de E qui est un donc un pro-CW
complexe. On forme le pro-ensemble cubique 6-enrichi C0(□top, Etop) et, pour ν∈ N, on forme le
Nouvelles cohomologies de Weil en caractéristique positive 1761
Z/𝓁ν-module cocubique6-enrichi
fct
(
C0(□top, Etop), Z/𝓁ν)
= colim
α
fct
(
C0(□top, Eα
top), Z/𝓁ν)
.
(Pour les notations, voir l’exemple 2.11.) On pose ensuite
ˆfct
(
C0(□top, Etop), Q𝓁
)
= Q⊗ lim
ν∈ N
fct
(
C0(□top, Etop), Z/𝓁ν)
.
C’est un Q𝓁-vectoriel cocubique6-enrichi. Par construction, il est aussi pseudo-monoïdal symétrique au
sens de [Ayoub 2014b, Déﬁnition A.29]. Enﬁn, on pose :
A𝓁(E)= A•(ˆfct(C0(□top, Etop), Q𝓁)
)
.
D’après [Ayoub 2014b, Lemme A.30], A𝓁(E) est une Q𝓁-dg-algèbre commutative. De plus, elle est
fonctorielle en E.
Revenons à la construction de0𝓁. Pour X∈ Sm/k, on pose0𝓁(X)= A𝓁(H´et(X)). Il est facile de voir
que le complexe0𝓁(X) calcule la cohomologie𝓁-adique de X. On laisse au lecteur le soin de vériﬁer que
la réalisation homologique R𝓁: DA´et(k; Q𝓁)→ D(Q𝓁) associée à0𝓁 par le corollaire 2.9 est isomorphe,
après restriction à DA´et
ct(k; Q𝓁), à la réalisation 𝓁-adique construite par exemple dans [Ayoub 2014a,
Déﬁnition 9.6].
