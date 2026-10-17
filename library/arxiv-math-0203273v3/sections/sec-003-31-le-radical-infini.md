---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-003-31-le-radical-infini
section_title: "Le radical infini"
section_number: 3.1
pages: 22-23
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.901
latex_coverage_ratio: 0.901
---
Soit ${\mathcal{A}}$ une $K$-catégorie.

::: defn
[]{#d3.1 label="d3.1"} Le radical infini de ${\mathcal{A}}$ est l'idéal $\displaystyle
{\operatorname{rad}}^\omega({\mathcal{A}})= 
\bigcap_{n\geq 1}
{\operatorname{rad}}^n({\mathcal{A}})$.
:::

Cet idéal intervient dans diverses questions, *e.g.* dans la théorie du type de représentation des $K$-algèbres de dimension finie (pour ${\mathcal{A}}= A$-$Modf$), et en liaison avec les conjectures de Bloch-Beilinson-Murre sur les motifs (pour ${\mathcal{A}}=$ la catégorie des motifs de Grothendieck pour l'équivalence rationnelle - motifs 'de Chow'- à coefficients dans $K$, *cf.* [\[BBM\]](#BBM){reference-type="ref" reference="BBM"})

::: lemme
[]{#radinf label="radinf"} Si $T: {\mathcal{A}}\to {\mathcal{B}}$ est un $K$-foncteur radiciel entre $K$-catégories, alors $T({\operatorname{rad}}^\omega({\mathcal{A}}))\subset
{\operatorname{rad}}^\omega({\mathcal{B}})$.
:::

C'est clair. $\square$

::: defn
[]{#D4swed label="D4swed"} Une $K$-catégorie ${\mathcal{A}}$ est dite *strictement semi-primaire (*resp.* strictement de Wedderburn)* si

::: thlist
pour tout couple d'objets $(A,B)$, il existe un entier $n>0$ tel que $({\operatorname{rad}}({\mathcal{A}}))^n(A,B)=0$;

${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est une $K$-catégorie semi-simple (*resp.* séparable).
:::
:::

Il est clair qu'une catégorie strictement semi-primaire (*resp.* strictement de Wedderburn) est semi-primaire (*resp.* de Wedderburn) et que son radical infini est nul. La réciproque est vraie si tous les anneaux d'endomorphismes sont artiniens.

Par ailleurs, il est clair qu'une catégorie semi-primaire n'ayant qu'un nombre fini d'objets est strictement semi-primaire.

::: contrex
[]{#Cssp label="Cssp"} Considérons la catégorie ${\mathcal{A}}$ suivante:

-   $Ob ({\mathcal{A}})=E$, où $E$ est un ensemble ordonné dense quelconque (dense signifie qu'entre deux éléments distincts on peut toujours en trouver un troisième distinct);

-   ${\mathcal{A}}(x,y)=K$ si $x\leq y$, $0$ sinon;

la composition étant induite par la multiplication dans $K$. On a alors $$({\operatorname{rad}}\,{\mathcal{A}})(x,y) =
\begin{cases} K &\text{si 
$x<y$}\\
0&\text{sinon.} \end{cases}$$ Ainsi $({\operatorname{rad}}\,{\mathcal{A}})(x,x)=0$ pour tout $x$, donc ${\mathcal{A}}$ est semi-primaire. Mais si $x<y$, $({\operatorname{rad}}\,{\mathcal{A}})(x,y)=({\operatorname{rad}}\, {\mathcal{A}})^n(x,y)$ pour tout $n>0$ (grâce à la densité de $E$). On a donc ${\operatorname{rad}}^\omega({\mathcal{A}})={\operatorname{rad}}({\mathcal{A}})\neq 
0$.

Si $E$ est un groupe commutatif ordonné, il est facile de munir ${\mathcal{A}}$ d'une structure monoı̈dale symétrique rigide. Quitte à passer à ${\mathcal{A}}^{\oplus\natural}$, on peut même construire un exemple $K$-linéaire pseudo-abélien (mais non abélien).
:::

## Cas des catégories de modules {#ccm}

Prenons à présent pour ${\mathcal{A}}$ la catégorie des *modules de type fini sur une algèbre $A$ de dimension finie sur un corps $K$*. Dans ce cas, le théorème d'existence des suites d'Auslander-Reiten montre que le radical ${\mathcal{R}}$ de $A\hbox{--}Modf$ est engendré (à droite ou à gauche) par les morphismes dits irréductibles (*i.e.* dans ${\mathcal{R}}\setminus {\mathcal{R}}^2$), *cf.* [@sisk] ou [@ks] pour plus de précisions. Ce point, et l'analyse détaillée des carquois d'Auslander-Reiten, sont à la base du résultat suivant, qui lie le type de représentation de $A$ au radical infini ${\mathcal{R}}^\omega$.

::: thm
[]{#t3.1 label="t3.1"} a) $A$ est de type de représentation fini (*i.e.* il n'y a qu'un nombre fini de classes d'isomorphismes d'indécomposables dans $A\hbox{--}Modf$) $\iff {\mathcal{R}}^\omega= 0 \iff 
\exists n\;$ tel que $\;{\mathcal{R}}^n=0$.\
b) (Supposons $K$ algébriquement clos[^1]) $A$ est de type de représentation infini sauvage $\iff 
{\mathcal{R}}^\omega$ n'est pas nilpotent.
:::

Un cas intermédiaire est celui de l'algèbre $\bar\mathbf{F}_2[(\mathbf{Z}/2\mathbf{Z})^2]$ (de type de représentation infini modéré); ${\mathcal{R}}^\omega$ est non nul mais nilpotent.

Un exemple standard d'algèbre de type de représentation infini sauvage est donné par le quotient de $K[[T_1,T_2]]$ par le cube de l'idéal maximal, ou même par l'idéal $(T_1^2, T_1T_2^2, T_2^3)$ (Drozd, *cf.* [@gabrielrev], [@nathanson], [@ringel 1]); il s'ensuit que $A\hbox{--}Modf$ n'est pas strictement semi-primaire.

Nous verrons plus loin qu'une catégorie tannakienne algébrique sur un corps de caractéristique nulle n'est pas nécessairement strictement semi-primaire.

Tout ceci indique que la notion de catégorie strictement semi-primaire est beaucoup trop restrictive pour nos besoins, et motive notre choix de traiter systématiquement des catégories semi-primaires (ou de Wedderburn).

::: rem
Un exemple remarquable de catégorie strictement de Wedderburn devrait être fourni par la catégorie des motifs purs pour une équivalence adéquate quelconque; cet exemple conjectural est brièvement discuté en [\[ex2\]](#ex2){reference-type="ref" reference="ex2"} ci-dessous.
:::

[^1]: Il est probable que cette hypothèse, qui figure dans [@ks], peut être affaiblie en: $K$ parfait.
