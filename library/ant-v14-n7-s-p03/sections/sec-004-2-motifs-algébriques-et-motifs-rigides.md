---
doc_id: ant-v14-n7-s-p03
doc_title: "Nouvelles cohomologies de Weil en caractéristique positive"
section_id: sec-004-2-motifs-algébriques-et-motifs-rigides
section_title: "Motifs algébriques et motifs rigides"
section_number: 2
pages: 8-29
source_pdf: ant-v14-n7-s-p03.pdf
source_sha256: e32fde16c3ce0940
doc_brief: "Nouvelles cohomologies de Weil en caractéristique positive — periods” admitting an explicit description by generators and relations."
---
On commence cette section avec des rappels sur les motifs (algébriques et rigides) qui serviront dans
la suite. On donne ensuite la construction du foncteur ~Rig∗ (voir (1-7)) et on démontre le théorème 1.7.
On termine avec une construction de foncteurs de réalisation à valeurs dans les modules sur certaines
dg-algèbres. On ﬁxe une Q-algèbre commutative3 et on écrit souvent «⊗ » au lieu de «⊗3 ».
2A. Rappels sur les motifs algébriques et leurs cohomologies. Soit S un schéma de base. On dispose
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
2B. Rappels sur les motifs rigides et leurs cohomologies. Dans cette sous-section on ﬁxe un corps k
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
2C. Foncteurs entre motifs algébriques et motifs rigides. Nous rappelons ici la construction de certains
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
2D. Une équivalence remarquable. On garde les notations et les hypothèses de la sous-section 2C.
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
2E. Constructions principales. On garde les hypothèses et les notations de la sous-section 2C. On utilise
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
