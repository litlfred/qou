---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 3-9
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.942
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
En algèbre non commutative, on rencontre d'abord, par ordre de complexité croissant, les anneaux semi-simples, puis les anneaux semi-primaires, c'est-à-dire les extensions d'un anneau semi-simple par un idéal nilpotent (le radical). Parmi ces derniers, le cas où l'anneau semi-simple est en fait une algèbre séparable est particulièrement agréable puisque, d'après un théorème classique de Wedderburn, l'extension par le radical se scinde.

Par ailleurs, en renversant la tautologie qui identifie tout anneau à une catégorie additive à un seul objet, on peut considérer les catégories additives comme des anneaux à plusieurs objets. Ce point de vue, popularisé par B. Mitchell et R. Street, permet de s'inspirer largement de l'algèbre non commutative dans les questions catégoriques. Comme tous premiers exemples, on obtient la notion d'idéal, et celle de radical, d'une catégorie additive.

Suivant ce point de vue, le premier thème de cet article est l'étude des catégories semi-primaires, extensions d'une catégorie semi-simple par un idéal vérifiant une condition convenable de nilpotence (*cf.* définition [\[D4\]](#D4){reference-type="ref" reference="D4"}), et de l'analogue catégorique du théorème de Wedderburn. Le second thème est l'étude du radical en présence d'une structure monoı̈dale. Ces thèmes se rejoignent dans une version monoı̈dale du théorème de Wedderburn (théorèmes [\[T2\]](#T2){reference-type="ref" reference="T2"} et [\[t4\]](#t4){reference-type="ref" reference="t4"}).

Nous donnons deux applications principales de ces résultats. La première est la construction de l'*enveloppe pro-réductive* $\operatorname{{}^pRed}(G)$ d'un groupe algébrique linéaire quelconque $G$ en caractéristique nulle. Les représentations indécomposables de $G$ sont en bijection avec les représentations irréductibles de $\operatorname{{}^pRed}(G)$, et ceci caractérise $\operatorname{{}^pRed}(G)$ si $K$ est algébriquement clos (proposition [\[p14.1\]](#p14.1){reference-type="ref" reference="p14.1"}). Le prototype est $\operatorname{{}^pRed}(\mathbb{G}_a)=SL_2$ (théorème de Jacobson-Morozov). Toutefois, $\operatorname{{}^pRed}(G)$ n'est en général pas de dimension finie: cela arrive déjà pour $G=\mathbb{G}_a\times \mathbb{G}_a$. L'existence même de $\operatorname{{}^pRed}(G)$ n'en implique pas moins une série de résultats concrets sur les représentations indécomposables des groupes algébriques.

La seconde application concerne la catégorie des motifs purs construits en termes d'une équivalence adéquate quelconque (fixée) pour les cycles algébriques. Nous détaillerons ailleurs (voir déjà

[@{ak(note)}]), en nous contentant dans ce texte de brèves allusions, notamment dans la deuxième partie. Indiquons ici seulement que l'on s'attend à ce qu'une telle catégorie de motifs soit semi-primaire, de radical compatible à la structure monoı̈dale (cela découlerait de la conjecture de Beilinson-Murre et des conjectures standard de Grothendieck); par ailleurs, nous nous appuyons dans [@{ak(note)}] sur notre version monoı̈dale du théorème de Wedderburn pour construire inconditionnellement les groupes de Galois motiviques.

En fait, l'un des projets directeurs de ce travail a été de séparer nettement ce qui dans la théorie encore largement conjecturale des motifs purs est de nature purement catégorique, et ce qui est de nature géométrique.

Décrivons plus en détail les quatre parties de ce travail.

Les deux premiers paragraphes (et l'appendice) contiennent une discussion des notions catégoriques fondamentales d'idéal, de radical (noté ${\operatorname{rad}}{\mathcal{A}}$), semi-simplicité, semi-primarité, etc\...

On y introduit la notion de $K$-*catégorie de Wedderburn*, qui joue un rôle important dans la suite ($K$ étant un corps): en supposant pour simplifier l'existence de biproduits finis, il s'agit d'une catégorie ${\mathcal{A}}$ dont les ensembles de morphismes ${\mathcal{A}}(A,B)$ sont des $K$-espaces vectoriels (la composition étant $K$-linéaire), telle que les ${\operatorname{rad}}{\mathcal{A}}(A,A)$ soient des idéaux nilpotents des algèbres d'endomorphismes ${\mathcal{A}}(A,A)$, et telle que les $K$-algèbres $({\mathcal{A}}/{\operatorname{rad}}{\mathcal{A}})(A,A)$ soient séparables, *i.e.* absolument semi-simples.

Cette condition de nilpotence est assez faible, et on montre au § [\[radrenf\]](#radrenf){reference-type="ref" reference="radrenf"} qu'on ne peut guère la renforcer sans restreindre considérablement le champ d'application de la théorie. Dans le cas de catégories de modules, l'analyse de ces conditions de nilpotence s'avère intimement liée à celle des carquois d'Auslander-Reiten.

Bien que le radical se comporte "mal\" en général par extension des scalaires, on montre au §[\[s3\]](#s3){reference-type="ref" reference="s3"} que la situation est meilleure dans le cas d'une $K$-catégorie de Wedderburn. Cette première partie se termine par l'étude et la comparaison (§ [\[ext\]](#ext){reference-type="ref" reference="ext"}) de deux notions d'extensions des scalaires pour les $K$-catégories que l'on rencontre dans la littérature.

L'objectif de la seconde partie est d'étudier en détail le radical d'une catégorie monoı̈dale symétrique rigide (*i.e.* dont les objets ont des duaux). Il se trouve qu'il n'est pas compatible à la structure monoı̈dale en général (un exemple de ce phénomène est donné par la catégorie des représentations de $GL_p$ en caractéristique $p>0$). Nous comparons chemin faisant le radical au plus grand idéal propre compatible à la structure monoı̈dale, et analysons le quotient de la catégorie par son radical. Actions du groupe symétrique, puissances extérieures et symétriques sont mises en œuvre dans cette optique. Nous nous sommes largement inspirés du récent travail de Kimura [@ki] sur les motifs de Chow "de dimension finie\".

On montre que le radical d'une catégorie tannakienne sur un corps de caractéristique nulle est toujours monoı̈dal, et qu'une telle catégorie est toujours de Wedderburn. Les théorèmes [\[absJannsen\]](#absJannsen){reference-type="ref" reference="absJannsen"} et [\[nouveau\]](#nouveau){reference-type="ref" reference="nouveau"} de ce paragraphe, beaucoup plus généraux, contiennent une version abstraite des résultats de Jannsen sur les motifs numériques et de Kimura sur les motifs de Chow [@jannsen; @ki]. Une attention particulière a été portée aux variantes $\mathbf{Z}/2$-graduées, en vue des applications aux motifs. En particulier, nous faisons le lien entre la théorie de Kimura [@ki] et la question de l'algébricité des projecteurs de Künneth pairs (théorème [\[tkim.1\]](#tkim.1){reference-type="ref" reference="tkim.1"}). Notre résultat le plus abouti est le théorème suivant: si on définit une *catégorie de Kimura* comme étant une catégorie $K$-linéaire pseudo-abélienne monoı̈dale symétrique rigide, où $K$ est un corps de caractéristique zéro, dont tout objet est de dimension finie au sens de Kimura (voir section [\[kimura\]](#kimura){reference-type="ref" reference="kimura"}), on a (théorème [\[tctki\]](#tctki){reference-type="ref" reference="tctki"}):

::: Thm
[]{#Tkim label="Tkim"} Toute catégorie de Kimura ${\mathcal{A}}$ est de Wedderburn. Son radical ${\mathcal{R}}$ est monoı̈dal, et la catégorie quotient ${\mathcal{A}}/{\mathcal{R}}$ est semi-simple tannakienne, après changement convenable de la contrainte de commutativité.
:::

La troisième partie débute sur le rappel d'une version catégorique, due à Mitchell, de la cohomologie de Hochschild; elle nous sert à prouver le point a) de l'analogue catégorique suivant du théorème de Wedderburn-Malcev (*cf.* théorèmes [\[T1\]](#T1){reference-type="ref" reference="T1"}, [\[T2\]](#T2){reference-type="ref" reference="T2"} et [\[t4\]](#t4){reference-type="ref" reference="t4"}).

::: Thm
[]{#th1 label="th1"} a) Soit ${\mathcal{A}}$ une $K$-catégorie de Wedderburn, et soit $\pi: {\mathcal{A}}\to {\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ le foncteur de projection. Alors $\pi$ admet une section fonctorielle. Deux telles sections sont conjuguées.\
b) Si ${\mathcal{A}}$ est monoı̈dale avec $End({{\bf 1}})=K$, et si le radical est compatible à la structure monoı̈dale (de sorte que $\pi$ est un foncteur monoı̈dal), $\pi$ admet une section monoı̈dale. Deux telles sections sont conjuguées par un isomorphisme monoı̈dal.\
c) Si enfin ${\mathcal{A}}$ est symétrique, toute section monoı̈dale est symétrique (c'est-à-dire respecte les tressages) à condition que $\operatorname{car}
K\ne 2$.
:::

La preuve de b), très technique, se trouve au § [\[s6\]](#s6){reference-type="ref" reference="s6"}. Elle utilise aussi la cohomologie de Hochschild pour l'algèbre libre sur les objets de la catégorie. Ainsi, a) repose essentiellement sur le fait qu'une $K$-algèbre séparable est de dimension $0$ (au sens de [@ce ch. IX, §7]), tandis que b) repose sur le fait qu'une $K$-algèbre libre est de dimension $1$...

La compatibilité des sections monoı̈dales à des tressages, dont il s'agit au point c) du théorème [\[th1\]](#th1){reference-type="ref" reference="th1"}, est étudiée en détail au §[\[tre\]](#tre){reference-type="ref" reference="tre"}. Elle n'est pas automatique; toutefois, en caractéristique différente de $2$, si le tressage résiduel est symétrique, son image par toute section monoı̈dale $s$ donne lieu à un tressage symétrique canonique sur ${\mathcal{A}}$, indépendant du choix de $s$ et qui ne coı̈ncide avec le tressage originel que si celui-ci était symétrique. Ceci s'applique notamment, en caractéristique zéro, à la quantification de Drinfeld-Cartier d'une catégorie monoı̈dale symétrique munie d'un tressage infinitésimal (exemple [\[ex4\]](#ex4){reference-type="ref" reference="ex4"}).

Le théorème [\[th1\]](#th1){reference-type="ref" reference="th1"} s'applique en particulier aux catégories de Kimura, en vertu du théorème [\[Tkim\]](#Tkim){reference-type="ref" reference="Tkim"} (*cf.* théorème [\[kimsplit\]](#kimsplit){reference-type="ref" reference="kimsplit"}).

Au §[\[repr\]](#repr){reference-type="ref" reference="repr"}, on confère une structure géométrique aux constructions précédentes: groupoı̈des pro-unipotents des sections (*resp.* des sections monoı̈dales).

La dernière partie explore les conséquences des résultats précédents en théorie des représentations.

Le §[\[radrep\]](#radrep){reference-type="ref" reference="radrep"} est consacré à l'étude de ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$, lorsque ${\mathcal{A}}$ est la catégorie des représentations d'un schéma en groupes affine $G$ (par exemple un groupe algébrique linéaire) sur un corps $K$ de caractéristique nulle. On peut conclure des résultats précédents que ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est équivalente à catégorie des représentations d'un schéma en groupes pro-réductif $\operatorname{{}^pRed}(G)$ contenant $G$.

Il est plus technique de rendre cette construction canonique. La question se simplifie si l'on travaille, comme au §[\[jm\]](#jm){reference-type="ref" reference="jm"}, dans la catégorie $\overline{\operatorname{Gaff}}_K$ dont les objets sont les $K$-groupes affines et les morphismes $G\to H$ sont donnés par les ensembles quotients de $Hom_K(G,H)$ par la relation d'équivalence $\sim$ telle que $f\sim g$ s'il existe $h\in H_K$ tel que $g=hfh^{-1}$. Soit $\overline{\operatorname{Gred}}_K$ la sous-catégorie pleine formée des groupes pro-réductifs. Alors (*cf.* théorème [\[t1\]](#t1){reference-type="ref" reference="t1"}):

::: Thm
Le foncteur d'inclusion $\overline{\operatorname{Gred}}_K\to
\overline{\operatorname{Gaff}}_K$ admet un adjoint (et quasi-inverse) à gauche: $G\mapsto \operatorname{{}^pRed}(G)$.
:::

On en déduit une série de résultats concrets concernant d'une part la structure des groupes algébriques, et d'autre part les représentations indécomposables des groupes algébriques.

L'une de ces applications concerne la notion d'*enveloppe réductive* d'un sous-groupe fermé d'un groupe réductif, *i.e.* de sous-groupe réductif intermédiaire minimal. On a (*cf.* théorème [\[T3\]](#T3){reference-type="ref" reference="T3"})

::: Thm
Deux enveloppes réductives de $G$ dans $H$ sont toujours conjuguées par un élément de $h \in H(K)$ commutant à $G$.
:::

Dans un paragraphe antérieur, on examine l'avatar non monoı̈dal, plus simple, de ces constructions, ce qui mène à la notion d'enveloppe semi-simple d'une algèbre profinie (sur un corps parfait). Ces enveloppes sont intimement liées aux algèbres d'Auslander. Nous les calculons dans le cas des algèbres héréditaires de dimension finie.

Enfin, dans un appendice, nous donnons pour mémoire diverses caractérisations des catégories semi-simples, dont la plupart sont sans doute bien connues des spécialistes.

Les auteurs se sont beaucoup amusés à écrire cet article, dont l'élaboration s'est révélée jusqu'au bout pleine de rebondissements. Ils craignent que ce côté ludique n'échappe aux lecteurs. Ils espèrent néanmoins que ceux-ci prendront plaisir à lire l'énoncé de certains théorèmes.

## Post-scriptum

Après la soumission de cet article, nous avons appris que Peter J. O'Sullivan avait introduit et étudié les catégories que nous avons baptisées catégories de Kimura au § [\[kimura\]](#kimura){reference-type="ref" reference="kimura"} de manière indépendante, sous le nom de *catégories semi-positives*. Il a obtenu la plupart des résultats du §[\[kimura\]](#kimura){reference-type="ref" reference="kimura"}, et bien plus, à l'exception toutefois du théorème de nilpotence [\[nouvellekim\]](#nouvellekim){reference-type="ref" reference="nouvellekim"}. Néanmoins, il a pu utiliser ses résultats pour obtenir une démonstration du théorème [\[th1\]](#th1){reference-type="ref" reference="th1"} ci-dessus dans le cas particulier des catégories de Kimura (qu'il faudrait maintenant rebaptiser catégories de Kimura-O'Sullivan), totalement différente de la nôtre et beaucoup plus géométrique. Il a ainsi démontré l'existence des enveloppes pro-réductives de manière indépendante de notre travail [@os].

Par ailleurs, O'Sullivan a apporté une réponse complète à notre question [\[q19.1\]](#q19.1){reference-type="ref" reference="q19.1"}: voir son appendice dans cet article.

 

::: center
**I. Radicaux et nilpotence**
:::

L'objectif de cette partie est l'étude des catégories qui sont extensions d'une catégorie additive semi-simple par un "idéal\" (localement) nilpotent. Comme en algèbre non commutative, la notion de radical joue ici un rôle de premier plan. On étudie aussi ce qui lui arrive par extension des scalaires.

# Idéaux et radicaux {#s1}

Soit $K$ un anneau commutatif unitaire. Pour prévenir les paradoxes ensemblistes, il est utile de fixer dès à présent un univers ${\mathcal{U}}$ (contenant $K$). Les ensembles d'objets et de flèches d'une *petite* catégorie se trouvent donc dans ${\mathcal{U}}$.

## $K$-catégories, catégories $K$-linéaires et $K$-catégories pseudo-abéliennes {#biprod}

Par *$K$-catégorie*, nous entendons une catégorie telle que pour tout couple d'objets $(A,B)$, les morphismes de $A$ vers $B$ forment un $K$-module ${\mathcal{A}}(A,B)$, et que la composition des morphismes soit $K$-linéaire (pour $K=\mathbf{Z}$, on dit aussi catégorie pré-additive).

Un *$K$-foncteur* entre deux $K$-catégories est un foncteur $K$-linéaire (sur les $K$-modules de morphismes).

Étant donné deux objets $A,A'\in {\mathcal{A}}$, un *biproduit* de $(A,A')$ est un système $(C,i,i',p,p')$, avec $C\in {\mathcal{A}}$, $i\in
{\mathcal{A}}(A,C)$, $i'\in {\mathcal{A}}(A',C)$, $p\in {\mathcal{A}}(C,A)$, $p'\in {\mathcal{A}}(C,A')$, le tout vérifiant les identités $$\label{eqbiprod}
pi=1_A,\quad p'i'=1_B,\quad ip+i'p'=1_C.$$

Un tel biproduit, s'il existe, est à la fois un produit et un coproduit et est déterminé à isomorphisme unique près. On dit que ${\mathcal{A}}$ est *$K$-linéaire* si tout couple $(A,A')$ d'objets de ${\mathcal{A}}$ admet un biproduit. Le choix d'un tel biproduit pour chaque couple d'objets $(A,A')$ d'une petite catégorie $K$-linéaire ${\mathcal{A}}$ définit alors un $K$-foncteur $\oplus:{\mathcal{A}}\times{\mathcal{A}}\to {\mathcal{A}}$, déterminé à isomorphisme naturel *unique* près, qui fait de ${\mathcal{A}}$ une catégorie monoı̈dale symétrique (l'unité étant l'objet nul).

D'après une variante de [@maclane ch. VIII, prop. 4], un foncteur $T:{\mathcal{A}}\to {\mathcal{B}}$ entre deux catégories $K$-linéaires est un $K$-foncteur si et seulement s'il transforme un biproduit en un biproduit. Si on s'est donné des biproduits $\oplus$ sur ${\mathcal{A}}$ et ${\mathcal{B}}$, il existe alors un isomorphisme naturel canonique $\oplus \circ (T,T)\cong T\circ \oplus$.

Enfin, une $K$-catégorie ${\mathcal{A}}$ est *pseudo-abélienne* si tout projecteur a un noyau (et une image): pour tout objet $A\in
{\mathcal{A}}$ et tout élément $e\in
{\mathcal{A}}(A,A)$ vérifiant $e^2=e$, il existe un objet $B\in {\mathcal{A}}$ et un morphisme $f:B\to A$ tel que $f$ soit un noyau de $(0,e)$. Si $(C,g)$ est un noyau de $1-e$, le morphisme $f\coprod g:B\oplus C\to A$ est alors un isomorphisme.

Toute $K$-catégorie abélienne est $K$-linéaire et pseudo-abélienne.

::: rem
La terminologie varie suivant les auteurs. Ainsi, Saavedra [@saavedra I.0.1.2] appelle catégorie $K$-linéaire ce que nous appelons $K$-catégorie. De même, une catégorie pseudo-abélienne est souvent appelée *karoubienne*[^1].
:::

On a les définitions suivantes, étroitement liées aux précédentes:

::: defn
[]{#ep-loc label="ep-loc"} Une sous-catégorie pleine ${\mathcal{B}}$ d'une $K$-catégorie ${\mathcal{A}}$ est

::: thlist
*épaisse* si elle est stable par facteur directs (représentables dans ${\mathcal{A}}$);

*localisante* si elle est épaisse et stable par sommes directes quelconques (représentables dans ${\mathcal{A}}$).
:::
:::

::: sorite
[]{#so0 label="so0"} Soient ${\mathcal{A}},{\mathcal{B}}$ deux $K$-catégories et $T,T'$ deux $K$-foncteurs de ${\mathcal{A}}$ vers ${\mathcal{B}}$. Soit $u:T\Rightarrow T'$ une transformation naturelle. Alors, pour tout biproduit $A\oplus B$ dans ${\mathcal{A}}$, on a $$u_{A\oplus B}=u_A\oplus u_B$$ modulo les isomorphismes naturels $T(A\oplus B)\simeq T(A)\oplus
T(B)$.$\square$
:::

## Complétions {#rap}

Étant donné une $K$-catégorie ${\mathcal{A}}$, on peut former son enveloppe $K$-linéaire ${\mathcal{A}}^\oplus$ (adjonction de sommes directes finies, cf. [@kelly §2]), son enveloppe pseudo-abélienne ${\mathcal{A}}^\natural$ (scindage d'idempotents, cf. [@mitchell §1,§ 11]), et son enveloppe $K$-linéaire pseudo-abélienne ${\mathcal{A}}^{\oplus\natural}$ (parfois appelée complétion projective, ou de Cauchy, ou de Karoubi...), formant un carré de sous-catégories pleines $$\label{eq1}
\begin{matrix}
\;&\;& {\mathcal{A}}^\oplus &\;&\;\\
\;&\nearrow\;&\;&\searrow &\;\\
      {\mathcal{A}}&\;&\;&\;& {\mathcal{A}}^{\oplus\natural}. \\
      \;&\searrow\;&\;&\nearrow &\;\\
                        \;&\;&
{\mathcal{A}}^\natural &\;&\; \end{matrix}$$

Pour référence, rappelons les constructions de ${\mathcal{A}}^\oplus$ et de ${\mathcal{A}}^\natural$:

### ${\mathcal{A}}^\oplus$

Les objets sont des suites finies $(A_1,A_2,\dots, A_n)$ d'objets de ${\mathcal{A}}$, notées $A_1\oplus A_2
\oplus \dots \oplus A_n$ [@kelly §2]. Les morphismes entre $A_1\oplus A_2
\oplus \dots \oplus A_n$ et $A'_1\oplus A'_2
\oplus \dots \oplus A'_m$ sont donnés par les matrices dont le coefficient d'ordre $(i,j)$ est dans ${\mathcal{A}}(A_i,A'_j)$ (se composant selon la règle usuelle).

Cette construction est $2$-covariante en ${\mathcal{A}}$: un foncteur $T: {\mathcal{A}}\to
{\mathcal{B}}$ étant donné, on lui associe foncteur $T^\oplus: {\mathcal{A}}^\oplus \to {\mathcal{B}}^\oplus$ construit sur $T$ composante par composante. Il est donc "strictement additif\" par définition: l'isomorphisme canonique $T^\oplus(X)\oplus T^\oplus(Y)=
T^\oplus(X\oplus Y)$ est l'identité pour tout couple d'objets $(X,Y)$ de ${\mathcal{A}}^\oplus$. De même, à une transformation naturelle $u:T\Rightarrow T'$ correspond une transformation naturelle $u^\oplus:T^\oplus\Rightarrow
{T'}^\oplus$ sur le modèle du sorite [\[so0\]](#so0){reference-type="ref" reference="so0"}.

### ${\mathcal{A}}^\natural$

Les objets sont les couples $(A,e)$ avec $A\in{\mathcal{A}}$ et $e\in {\mathcal{A}}(A,A)$ vérifiant $e^2=e$. Pour un autre tel couple $(B,f)$, on pose $${\mathcal{A}}^\natural((A,e),(B,f))=f{\mathcal{A}}(A,B)e\subset {\mathcal{A}}(A,B).$$

Les morphismes se composent de manière évidente. Cette construction est également $2$-covariante en ${\mathcal{A}}$ ($T^\natural(A,e)=(T(A),T(e))$, $u^\natural_{(A,e)}=T'(e)u_A T(e)$).

### Propriétés universelles

Les deux constructions ci-dessus ont des propriétés universelles. Quitte à introduire des $2$-catégories, on peut les interpréter comme des adjoints à gauche. Soit $\{K\}$ la $2$-catégorie dont les objets sont les petites $K$-catégories, les $1$-morphismes les $K$-foncteurs et les $2$-morphismes les transformations naturelles. Soient $\{K\}^\oplus,\{K\}^\natural,\{K\}^{\oplus\natural}$ les sous-$2$-catégories pleines de $\{K\}$ (mêmes $1$-morphismes et mêmes $2$-morphismes) formées des catégories $K$-linéaires, pseudo-abéliennes et $K$-linéaires pseudo-abéliennes. Alors:

::: sorite
[]{#so01 label="so01"} a) Pour tout couple de petites $K$-catégories $({\mathcal{A}},{\mathcal{B}})$, avec ${\mathcal{B}}$ $K$-linéaire, les foncteurs de restriction $$\begin{aligned}
\{K\}^\oplus({\mathcal{A}}^\oplus,{\mathcal{B}})&\to \{K\}({\mathcal{A}},{\mathcal{B}})\\
\{K\}^\natural({\mathcal{A}}^\natural,{\mathcal{B}})&\to \{K\}({\mathcal{A}},{\mathcal{B}})
\end{aligned}$$ sont pleinement fidèles et surjectifs. De plus, pour tout $T\in
\{K\}({\mathcal{A}},{\mathcal{B}})$, la fibre de $T$ est un groupoı̈de à groupes d'automorphismes triviaux.\
b) Pour tout couple de petites $K$-catégories $({\mathcal{A}},{\mathcal{B}})$, les foncteurs $$\begin{aligned}
\{K\}({\mathcal{A}},{\mathcal{B}})&\to \{K\}^\oplus({\mathcal{A}}^\oplus,{\mathcal{B}}^\oplus)\\
\{K\}({\mathcal{A}},{\mathcal{B}})&\to \{K\}^\natural({\mathcal{A}}^\natural,{\mathcal{B}}^\natural)
\end{aligned}$$ sont pleinement fidèles (mais pas essentiellement surjectifs en général).$\square$
:::

(Le fait que les foncteurs considérés en a) ne soient pas bijectifs sur les objets provient des choix possibles de biproduits et de noyaux.)

[^1]: Cette notion n'est pas spécifiquement additive, *cf.* par exemple [@saavedra VI.4.1.2.1].
