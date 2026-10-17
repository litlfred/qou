---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-004-4-radical-et-extension-des-scalaires
section_title: "Radical et extension des scalaires"
section_number: 4
pages: 23-35
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.933
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
[]{#s3 label="s3"}

##  

Il est connu que le radical d'une algèbre se comporte "mal\" par extension des scalaires en général, *cf.* [@alg], [@rowen]. La situation s'améliore toutefois dans le cas "de Wedderburn\".

::: prop
[]{#L5 label="L5"} 1) Soit $L/K$ une extension de corps. Soit $A$ une $K$-algèbre de Wedderburn, *i.e.* ${\operatorname{rad}}(A)$ est nilpotent et $A/{\operatorname{rad}}(A)$ est séparable. Alors\
a) ${\operatorname{rad}}(A\otimes_K L)\cap A= {\operatorname{rad}}(A)$,\
b) ${\operatorname{rad}}(A)\otimes_K L= 
{\operatorname{rad}}(A\otimes_K L)$,\
c) $A\otimes_K L$ est de Wedderburn.

2\) Si $A\otimes_K L$ est semi-primaire et si ${\operatorname{rad}}(A \otimes_K L)\subset 
{\operatorname{rad}}(A)\otimes_K L$ pour toute extension $L/K$, alors $A$ est de Wedderburn.
:::

1\) Il est clair que ${\operatorname{rad}}(A)\otimes_K L$ est un idéal nilpotent de $A\otimes_K L$, donc contenu dans ${\operatorname{rad}}(A\otimes_K L)$. D'autre part $A/{\operatorname{rad}}(A)$ est séparable, donc aussi $(A/{\operatorname{rad}}(A))\otimes_K L= (A\otimes_K 
L)/({\operatorname{rad}}(A)\otimes_K L)$. En particulier, cette dernière est semi-simple, donc ${\operatorname{rad}}(A)\otimes_K L$ contient ${\operatorname{rad}}(A\otimes_K L)$. D'où $b)$ et $c)$. Le point $a)$ en découle immédiatement.

2\) Supposons $A\otimes_K L$ semi-primaire pour toute extension $L/K$. En particulier ${\operatorname{rad}}(A)$ est nilpotent, donc ${\operatorname{rad}}(A \otimes_K L)\supset 
{\operatorname{rad}}(A)\otimes_K L$, et on a finalement égalité compte tenu de l'hypothèse. Il suit que $(A/{\operatorname{rad}}(A))\otimes_K L\cong 
(A\otimes_K L)/{\operatorname{rad}}(A \otimes_K L)$ est semi-simple pour toute extension $L/K$, donc que $A/{\operatorname{rad}}(A)$ est séparable. Ainsi $A$ est de Wedderburn. $\square$

::: rem
[]{#imparf label="imparf"} La condition que ${\operatorname{rad}}(A \otimes_K L)\subset {\operatorname{rad}}(A)\otimes_K L$ est nécessaire: si $K$ est imparfait, toute extension finie inséparable $A/K$ non triviale fournit un exemple de $K$-algèbre "absolument semi-primaire\" mais pas de Wedderburn.
:::

Si ${\mathcal{A}}$ est une $K$-catégorie, notons ${\mathcal{A}}_L$ la $L$-catégorie qui s'en déduit en tensorisant les morphismes par $L$.

::: meg
Si ${\mathcal{A}}$ est pseudo-abélienne, il n'en est pas de même de ${\mathcal{A}}_L$ en général [^1]. Si ${\mathcal{A}}$ est abélienne, il n'en est pas de même de $({\mathcal{A}}_L)^\natural$ en général. Un contre-exemple est fourni par la catégorie des représentations de dimension finie de $\mathbb{G}_a\times \mathbb{G}_a$ (*cf.* fin du § [\[jm\]](#jm){reference-type="ref" reference="jm"}.)
:::

::: cor
[]{#C3.1. label="C3.1."} Soit ${\mathcal{A}}$ une catégorie de Wedderburn. Alors, pour toute extension $L/K$, ${\mathcal{A}}_L$ est de Wedderburn. De plus

::: thlist
${\operatorname{rad}}({\mathcal{A}}_L)= {\operatorname{rad}}({\mathcal{A}})\otimes_K L$.

Le foncteur d'extension des scalaires ${\mathcal{A}}\to {\mathcal{A}}_L$ est radiciel.

Le carré $$\begin{CD}
\sA@>>> {\mathcal{A}}_L\\
@VVV @VVV\\
{\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})@>>> 
{\mathcal{A}}_L/{\operatorname{rad}}({\mathcal{A}}_L)
\end{CD}$$ est naturellement cocartésien: le foncteur naturel ${\mathcal{A}}_L/{\operatorname{rad}}({\mathcal{A}}_L)\to ({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))_L$ est une équivalence de catégories. $\square$
:::
:::

::: thm
[]{#P2 label="P2"} Soient $K$ un corps, $L$ une extension de $K$, $V$ un $L$-espace vectoriel de dimension finie, et $A$ une sous-$K$-algèbre de $End_L(V)$. On suppose que, pour tout $a\in
A$, le polynôme caractéristique de $a$ dans $V$ est à coefficients dans $K$. Alors\
a) Le radical $R$ de $A$ est nilpotent d'échelon $\le n= \dim V$.\
b) Si $K$ est infini, $A/R$ est semi-simple, produit d'au plus $n$ composants simples. Si de plus $K$ est parfait, $A/R$ est séparable.\
c) Supposons $K$ infini et parfait. Alors le radical de la sous-$L$-algèbre $AL$ de $End_L(V)$ engendrée par $A$ est $RL$, on a $RL\cap A=R$, et l'application canonique $(A/R)\otimes_K L\to AL/RL$ est bijective.
:::

a\) D'après [@alg §11, ex. 1 a)], $R$ est *a priori* un nil-idéal. Montrons même que tout $u\in R$ vérifie $u^n=0$. Pour cela, il suffit de voir que les valeurs propres de $u$ dans $V$ sont toutes nulles. Supposons le contraire et soit $\lambda\ne 0$ une telle valeur propre. Comme $\lambda$ est algébrique sur $K$, il existe un polynôme $Q\in K[T]$ tel que $\lambda Q(\lambda)=1$. Mais $1-uQ(u)$ est inversible, donc $1-\lambda Q(\lambda)$ est inversible, contradiction.

Comme l'image de $R$ dans $End_L(V)$ est un semi-groupe multiplicatif formé d'éléments nilpotents, un théorème de N. Jacobson permet de conclure que $R$ est nilpotent d'échelon $\le \dim V$, *cf.* [@rowen 2.6.30].

b\) Cela résulte de [@alg §11, ex. 1 d)].

c\) Notons provisoirement $R_L$ le radical de $AL$. D'après la proposition [\[L5\]](#L5){reference-type="ref" reference="L5"} b), on a ${\operatorname{rad}}(A\otimes_K L)=R\otimes_K L$, donc l'homomorphisme surjectif $A\otimes_K L\to AL$ induit un homomorphisme surjectif $(A/R)\otimes_K L\to AL/R_L$. Comme $A/R$ est séparable et $R$ nilpotent, le théorème de Wedderburn (*cf.* théorème [\[T1\]](#T1){reference-type="ref" reference="T1"} ci-dessous, dans le cas d'un seul objet) permet de relever $A/R$ dans $A$. Notons ce relevé $B$, et soit $K'$ le centre d'un facteur simple de $B$: $K'$ est une extension finie de $K$. Soit $x$ un élément primitif de $K'$: comme le polynôme caractéristique de $x$ opérant sur $V$ est à coefficients dans $K$, c'est nécessairement une puissance du polynôme caractéristique de $x$ opérant sur $K'$. Ceci implique que la surjection $K'\otimes_K 
L\to
K'L$ est bijective, et donc que $B\otimes_K L\to BL$ est bijective. Il en résulte que $A/R\otimes_K L\to AL/R_L$ est bijective, d'où l'on déduit $R_L=RL$. Enfin, $(R_L\cap A=) RL\cap 
A = R$ découle immédiatement de la nilpotence de $R$. $\square$

::: rems
[]{#R2 label="R2"} 

-   L'hypothèse que $K$ est parfait n'est pas superflue dans b) et c). On obtient un contre-exemple en prenant pour $A=L$ une extension finie inséparable de $K$, $V= L\otimes_K L$ avec la structure gauche de $L$-espace, et $A\hookrightarrow End_L(V)$ donné par $\ell\mapsto 
    (\ell_1\otimes \ell_2 \mapsto
    \ell_1\otimes \ell\ell_2)$.

-   Si l'on suppose que $V=\bigoplus V_i$ est un $L$-espace vectoriel gradué et que $A$ est une sous-algèbre de $\prod End(V_i)$, la borne sur l'échelon de nilpotence $n$ de $R$ dans le point a) du théorème [\[P2\]](#P2){reference-type="ref" reference="P2"} se raffine en: $n\le max\dim V_i$ (même démonstration).

-   Le point a) du théorème [\[P2\]](#P2){reference-type="ref" reference="P2"} reste valable si on remplace l'hypothèse que pour tout $a\in
    A$, le polynôme caractéristique de $a$ est à coefficients dans $K$ par: $K$ est de cardinal strictement supérieur à $\dim_K A$, *cf.* [@alg no. 12, ex. 16].
:::

::: cor
[]{#c6 label="c6"} Soient $K$ un corps parfait infini, $L$ une extension de $K$, ${\mathcal{A}}$ une catégorie $K$-linéaire et $H:{\mathcal{A}}\to Vec_L$ un $K$-foncteur fidèle de ${\mathcal{A}}$ vers la catégorie des $L$-espaces vectoriels de dimension finie. On suppose que, pour tout endomorphisme $a\in
{\mathcal{A}}(A,A)$, le polynôme caractéristique de $H(a)$ est à coefficients dans $K$. Alors\
a) ${\mathcal{A}}$ est une $K$-catégorie de Wedderburn.\
b) Soit $H({\mathcal{A}}) L$ la sous-catégorie (non pleine) $L$-linéaire de $Vec_L$ engendrée par $H({\mathcal{A}})$: les objets de $H({\mathcal{A}}) L$ sont les objets de $H({\mathcal{A}})$ et, pour deux tels objets $X,Y$, $\big(H({\mathcal{A}})L\big)(X,Y)=\allowbreak\big(H({\mathcal{A}})(X,Y)\big)L$. Alors:\
i) ${\operatorname{rad}}(H({\mathcal{A}})L)={\operatorname{rad}}(H({\mathcal{A}}))L$.\
ii) ${\operatorname{rad}}(H({\mathcal{A}})L)\cap 
H({\mathcal{A}})={\operatorname{rad}}(H({\mathcal{A}}))$.\
iii) Le foncteur ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})_L\to 
H({\mathcal{A}})L/{\operatorname{rad}}(H({\mathcal{A}})L)$ induit par $H$ est une équivalence de catégories.\
En particulier, $H({\mathcal{A}}) L$ est une $L$-catégorie de Wedderburn. $\square$
:::

::: rem
[]{#rem 
en fam label="rem 
en fam"} La conclusion $a)$ vaut encore si, au lieu d'un $L$ et d'un $H$, on a une famille finie d'extensions de corps $L_i/L$ et une famille fidèle de foncteurs $H_i:
{\mathcal{A}}\to Vec_{L_i}$ et si l'on suppose que pour tout $a\in
{\mathcal{A}}(A,A)$, le polynôme caractéristique de $H_i(a)$ est à coefficients dans $K$. En effet, plongeant les $L_i$ dans un corps commun $L$, et posant $H(A)= \bigoplus_i H_i(A)\otimes_{L_i} 
L$, on se ramène au cas du corollaire.
:::

::: ex
Comme nous le verrons en [\[wedtr\]](#wedtr){reference-type="ref" reference="wedtr"}, le corollaire précédent s'applique notamment au cas des catégories tannakiennes sur un corps de caractéristique nulle.
:::

# Extensions des scalaires naı̈ve et non naı̈ve {#ext}

Dans ce paragraphe, $K$ est un corps commutatif. Nous allons comparer l'extension des scalaires "naı̈ve\" étudiée dans le paragraphe précédent à une extension des scalaires plus sophistiquée, due à Saavedra, dont nous aurons besoin dans les paragraphes [\[compl\]](#compl){reference-type="ref" reference="compl"} et [\[jm\]](#jm){reference-type="ref" reference="jm"}.

## Deux types d'extensions des scalaires {#extsc}

::: defn
[]{#d3 label="d3"} Soient ${\mathcal{A}}$ une $K$-catégorie et $L$ une $K$-algèbre (commutative unitaire).\
a) La catégorie ${\mathcal{A}}_L$ a pour objets les objets de ${\mathcal{A}}$; si $A,B\in
{\mathcal{A}}_L$, ${\mathcal{A}}_L(A,B)\allowbreak 
=L\otimes_K {\mathcal{A}}(A,B)$. On appelle ${\mathcal{A}}_L$ l'*extension des scalaires naı̈ve* de ${\mathcal{A}}$ de $K$ à $L$.\
b) On note ${\mathcal{A}}_{(L)}=Rep_K(L,{\mathcal{A}})$ la catégorie des $K$-représentations de $L$ dans ${\mathcal{A}}$: un objet de ${\mathcal{A}}_{(L)}$ est un couple $(A,\rho)$, où $A\in {\mathcal{A}}$ et $\rho$ est un homomorphisme de $K$-algèbres unitaires $L\to
{\mathcal{A}}(A,A)$; un morphisme $f:(A,\rho)\to (A',\rho')$ est un élément de ${\mathcal{A}}(A,A')$ commutant à $\rho$ et $\rho'$. On appelle ${\mathcal{A}}_{(L)}$ l'*extension des scalaires à la Saavedra de ${\mathcal{A}}$ de $K$ à $L$* (*cf.* [@saavedra II.1.5]).
:::

::: lemme
[]{#l10 label="l10"} a) La $K$-structure de ${\mathcal{A}}_{(L)}$ s'enrichit en une $L$-structure par la loi $$\lambda f=\rho'(\lambda) f=f\rho(\lambda)$$ pour $\lambda\in L$ et $f\in {\mathcal{A}}_{(L)}((A,\rho),(A',\rho'))$.\
b) Si ${\mathcal{A}}$ est additive (*resp.* pseudo-abélienne, abélienne, stable par limites inductives quelconques), il en est de même de ${\mathcal{A}}_{(L)}$.$\square$
:::

::: rems
[]{#r4 label="r4"} 

-   Pour que cette construction soit raisonnable, il faut que ${\mathcal{A}}$ soit "assez grosse\" ou que $L$ soit "assez petit\". Par exemple, si ${\mathcal{A}}(A,A)$ est de $K$-dimension finie pour tout objet $A$, alors ${\mathcal{A}}_{(L)}=0$ dès que $L$ est un corps infini contenant $K$.

-   Si ${\mathcal{A}}$ est semi-simple, il ne suit pas que ${\mathcal{A}}_{(L)}$ le soit: prendre pour $L/K$ une extension finie inséparable de corps, et pour ${\mathcal{A}}$ la $K$-catégorie à un objet $L$ (ou, si on préfère $Vec_L$). C'est toutefois le cas (trivialement) si $L$ est une extension infinie de $K$, car dans ce cas ${\mathcal{A}}_{(L)}=0$ (voir a))

-   Soit ${\mathcal{A}}= Rep^\infty_K G$ la Ind-catégorie attachée à la catégorie $Rep_K G$ des $K$-représentations de dimension finie d'un $K$-groupe affine. Alors ${\mathcal{A}}_{(L)}$ s'identifie canoniquement à $Rep^\infty_L(G)$, *cf.* [@saavedra III.1]. Même remarque avec $Rep_K(G)$ quand $L/K$ est finie.

-   Soit ${\mathcal{A}}$ une $K$-catégorie quelconque. Alors $(Mod\hbox{--}{\mathcal{A}})_{(L)}$ s'identifie à la catégorie des $K$-foncteurs de ${\mathcal{A}}$ vers $Mod\hbox{--}L$. Cette dernière s'identifie canoniquement à $Mod\hbox{--}{\mathcal{A}}_{L}$ via l'extension des scalaires naı̈ve. D'après la proposition [\[p1.1\]](#p1.1){reference-type="ref" reference="p1.1"} f), les objets compacts de cette catégorie s'identifient à $({\mathcal{A}}_L)^{\oplus\natural}$.
:::

## Sur l'extension des scalaires à la Saavedra {#s.saa}

Notre but est de comparer ${\mathcal{A}}_L$ à ${\mathcal{A}}_{(L)}$. On a un "foncteur fibre\" évident $$\label{eqB.2}
\omega_L:{\mathcal{A}}_{(L)}\to {\mathcal{A}}$$ qui est fidèle et conservatif, commutant aux limites projectives et inductives quelconques, exact si ${\mathcal{A}}$ est abélienne.

La première chose à faire est de définir un foncteur en sens inverse, de ${\mathcal{A}}$ vers ${\mathcal{A}}_{(L)}$. Ce n'est possible que sous des hypothèses restrictives.

::: lemme
[]{#l7 label="l7"} a) Soient $A\in
{\mathcal{A}}$ et $V\in Vec_K$. Le foncteur $$B\mapsto Hom_K(V,{\mathcal{A}}(A,B))$$ est représentable dans les cas suivants:

::: thlist
${\mathcal{A}}$ est $K$-linéaire et $\dim_K V<\infty$.

${\mathcal{A}}$ est stable par limites inductives quelconques.
:::

On note un représentant $V\otimes_K A$.\
b) La construction $(V,A)\mapsto
V\otimes_K A$ est bifonctorielle et bilinéaire. Si $W$ est un autre $K$-espace vectoriel, on a un isomorphisme canonique $$W\otimes_K(V\otimes_K A)\simeq (W\otimes_K V)\otimes_K A$$ pourvu que les deux membres aient un sens. (Nous nous autoriserons de la canonicité de cet isomorphisme pour passer sous silence tout tel parenthésage.)\
c) Si ${\mathcal{A}}$ est $K$-linéaire et que $\dim_K V<\infty$, alors pour tout $B\in {\mathcal{A}}$, le foncteur $$A\mapsto {\mathcal{A}}(V\otimes_K A,B)$$ est représentable par $V^*\otimes_K B$, où $V^*$ est le dual de $V$. $\square$
:::

Soient $A,B\in {\mathcal{A}}$ et $V\in Vec_K$. Supposons que les objets $V\otimes_K
A$ et $V\otimes_K B$ soient définis. L'homomorphisme de fonctorialité $${\mathcal{A}}(A,B)\to {\mathcal{A}}(V\otimes_K
A,V\otimes_K B)\simeq Hom_K(V,{\mathcal{A}}(A,V\otimes_K B))$$ fournit un autre homomorphisme $$\label{eqB.1}
V\otimes_K {\mathcal{A}}(A,B)\to {\mathcal{A}}(A,V\otimes_K B).$$

::: lemme
[]{#l11 label="l11"} L'homomorphisme [\[eqB.1\]](#eqB.1){reference-type="eqref" reference="eqB.1"} est un isomorphisme dans les cas suivants:

::: thlist
$\dim_K V<\infty$;

$A$ est compact (*i.e.* le foncteur $B\mapsto {\mathcal{A}}(A,B)$ commute aux limites inductives quelconques)
:::
:::

\(i\) Écrire $V\simeq K^n$ et se ramener à $n=1$ par additivité. (ii) passer à la limite sur (i).$\square$

::: hyps
[]{#h1 label="h1"} À partir de maintenant, on suppose que ${\mathcal{A}}$ est additive (c'est-à-dire $K$-linéaire). On se donne une $K$-algèbre $L$ (commutative unitaire). On suppose:

-   soit que $\dim_K L<\infty$;

-   soit que ${\mathcal{A}}$ est stable par limites inductives quelconques.
:::

::: lemme
[]{#l8 label="l8"} Sous les hypothèses [\[h1\]](#h1){reference-type="ref" reference="h1"},\
a) La donnée d'une représentation $\rho:L\to {\mathcal{A}}(A,A)$ comme dans la définition [\[d3\]](#d3){reference-type="ref" reference="d3"} b) équivaut à la donnée d'un morphisme $\rho^\vee:L\otimes_K A\to A$ tel que le diagramme $$\begin{CD}
L\otimes_K L\otimes_K A@>1\otimes \rho^\vee>> L\otimes_K A\\
@V{\mu_L\otimes 1}VV @V{\rho^\vee}VV\\
L\otimes_K A@>\rho^\vee>> A,
\end{CD}$$ où $\mu_L$ est la multiplication de $L$, soit commutatif.\
b) Le morphisme $$\begin{CD} \rho_A^\vee:L\otimes_K L\otimes_K A@>\mu_L\otimes 1>>
L\otimes_K A
\end{CD}$$ vérifie la condition de a), donc définit une représentation canonique $\rho_A:L\to {\mathcal{A}}(L\otimes_K A,L\otimes_K A)$.$\square$
:::

Sous les hypothèses [\[h1\]](#h1){reference-type="ref" reference="h1"}, le lemme [\[l8\]](#l8){reference-type="ref" reference="l8"} définit un $K$-foncteur $$\begin{aligned}
{\mathcal{A}}&\to {\mathcal{A}}_{(L)}\label{eqB.3}\\
A&\mapsto (L\otimes_K A,\rho_A).\notag
\end{aligned}$$

::: lemme
[]{#l12 label="l12"} Le foncteur [\[eqB.3\]](#eqB.3){reference-type="eqref" reference="eqB.3"} est adjoint à gauche au foncteur $\omega_L$ de [\[eqB.2\]](#eqB.2){reference-type="eqref" reference="eqB.2"}. Il envoie objet compact de ${\mathcal{A}}$ sur objet compact de ${\mathcal{A}}_{(L)}$.
:::

(La seconde assertion provient du fait que $\omega_L$ commute aux limites inductives quelconques.)$\square$

Le lemme [\[l10\]](#l10){reference-type="ref" reference="l10"} b) montre que le foncteur [\[eqB.3\]](#eqB.3){reference-type="eqref" reference="eqB.3"} s'étend alors en un $L$-foncteur $$\label{eqB.4}
\Xi_L:{\mathcal{A}}_L\to {\mathcal{A}}_{(L)}.$$

## Comparaison de ${\mathcal{A}}_L$ et ${\mathcal{A}}_{(L)}$

::: prop
[]{#p6 label="p6"} Soient $A,B$ deux objets de ${\mathcal{A}}$. Si $\dim_K L=\infty$, supposons que $A$ soit compact. Alors l'homomorphisme $$L\otimes_K{\mathcal{A}}(A,B)\to {\mathcal{A}}_{(L)}(L\otimes_K A,L\otimes_K B)$$ est bijectif. En particulier, $\Xi_L$ est pleinement fidèle si $\dim_K L<\infty$, et sa restriction à la sous-catégorie pleine des objets compacts de ${\mathcal{A}}_L$ est pleinement fidèle en général (et prend ses valeurs dans les objets compacts de ${\mathcal{A}}_{(L)}$ d'après le lemme [\[l12\]](#l12){reference-type="ref" reference="l12"}).
:::

Cela résulte des lemmes [\[l11\]](#l11){reference-type="ref" reference="l11"} et [\[l12\]](#l12){reference-type="ref" reference="l12"}.$\square$

::: thm
[]{#t2 label="t2"} Le foncteur $$\Xi_L^\natural:({\mathcal{A}}_L)^\natural\to {\mathcal{A}}_{(L)}$$ induit par $\Xi_L$ est une équivalence de catégories pour toute $K$-catégorie ${\mathcal{A}}$ pseudo-abélienne si et seulement si $L$ est une $K$-algèbre *étale*. Dans ce cas, $\Xi_L^\natural$ induit une équivalence de catégories sur les sous-catégories pleines formées des objets compacts.
:::

Vu la proposition [\[p6\]](#p6){reference-type="ref" reference="p6"}, le foncteur $\Xi_L^\natural$ est une équivalence de catégories si et seulement s'il est essentiellement surjectif. D'autre part, d'après la proposition [\[Psep\]](#Psep){reference-type="ref" reference="Psep"}, $L$ est étale sur $K$ si et seulement si le $L$-bimodule $L$ est projectif.

1\) Supposons d'abord $L$ projectif sur $L\otimes_K L$. La suite exacte de $L$-bimodules $0\to
\operatorname{Ker}\mu \to L\otimes_K L \stackrel{\mu}{\longrightarrow} L\to 0$ est scindée; on note $s$ un scindage.

Dire que $\Xi_L^\natural$ est essentiellement surjectif est dire que tout objet $B$ dans ${\mathcal{A}}_{(L)}$ est facteur direct de $L\otimes_K A$ pour un objet $A$ de ${\mathcal{A}}$ convenable (comme $\Xi_L^\natural$ est pleinement fidèle, l'expression "facteur direct\" n'est pas ambigüe). Nous allons montrer que $A =\omega_L(B)$ convient, ce qui montrera du même coup la seconde assertion.

Notons $\iota_2$ l'homomorphisme de $L$-algèbres $L\to L\otimes_K L$ donné par $\ell\mapsto 1\otimes \ell$. Dans ${\mathcal{A}}_{(L)}$, on a un isomorphisme $L\otimes_K
\omega_L(B)\cong (L\otimes_K L)\otimes_{L,\iota_2} B$, et un morphisme $\mu\otimes_L 1_B:(L\otimes_K L)\otimes_{L,\iota_2} B \to
L\otimes_{L,\iota_2} B = B$ dont $s\otimes_L 1_B$ est une section. Ceci montre bien que $B$ est facteur direct de $L\otimes \omega_L(B)$.

2\) Supposons maintenant que $L$ ne soit pas $L\otimes_K L$-projectif. Pour obtenir un contre-exemple, prenons ${\mathcal{A}}= Vec_L$ (vue comme $K$-catégorie abélienne): ${\mathcal{A}}_{(L)}$ est la catégorie des $(L\otimes_K L)$-modules finis. Alors $L$, vu comme objet de ${\mathcal{A}}_{(L)}$, n'est pas facteur direct d'un objet de la forme $L\otimes_K
V$, $V \in Ob({\mathcal{A}})$, puisqu'un tel objet est un $(L\otimes_K L)$-module libre. $\square$

::: ex
Prenons pour ${\mathcal{A}}$ la catégorie $Rep_K G$ des $K$-représentations de dimension finie d'un $K$-groupe affine. On note comme ci-dessus $Rep^\infty_K G$ la Ind-catégorie attachée à ${\mathcal{A}}$, de sorte qu'on a une équivalence naturelle (monoı̈dale) $(Rep^\infty_K G)_{(L)}\cong Rep^\infty_L G_L$. En outre, si $L/K$ est (finie) séparable, elle induit une équivalence naturelle (monoı̈dale) entre objets compacts $(Rep_K G)_{(L)}\cong Rep_L G_L$, et aussi (en vertu du théorème ci-dessus) $\cong \allowbreak(Rep_K G)_L^\natural$.
:::

 

::: center
**II. Radical et rigidité**
:::

L'objectif de cette partie est l'étude du radical ${\mathcal{R}}$ en présence d'une structure monoı̈dale sur ${\mathcal{A}}$. Il s'avère que la question de la compatibilité du radical à la structure monoı̈dale est fort délicate, et n'a pas toujours une réponse positive. Nous comparons chemin faisant ${\mathcal{R}}$ au plus grand idéal propre ${\mathcal{N}}$ compatible à la structure monoı̈dale, et analysons le quotient ${\mathcal{A}}/{\mathcal{R}}$.

Pour simplifier, on suppose ${\mathcal{A}}$ *stricte* (la contrainte d'associativité et les contraintes d'unité sont l'identité).

# Généralités {#s3.5}

## Idéaux monoı̈daux, duaux. {#6.2}

Soit $K$ un anneau commutatif unitaire, et soit $({\mathcal{A}},\bullet)$ une $K$-catégorie monoı̈dale.

::: defn
[]{#d6.1 label="d6.1"} Un idéal ${\mathcal{J}}$ de ${\mathcal{A}}$ est dit *monoı̈dal*[^2] s'il est stable par les transformations $1_C\bullet -$ et $- \bullet 1_C$ pour tout objet $C$ de ${\mathcal{A}}$.
:::

::: lemme
[]{#l6.1 label="l6.1"} a) Si ${\mathcal{J}}$ est monoı̈dal, il est stable par produit monoı̈dal à gauche et à droite par un morphisme arbitraire. En particulier, on a une structure monoı̈dale induite sur le quotient ${\mathcal{A}}/{\mathcal{J}}$.\
b) La notion d'idéal monoı̈dal est stable par somme, intersection, produit.
:::

a\) Soient $f\in {\mathcal{J}}(A,B)$ et $g\in {\mathcal{A}}(C,D)$. On a alors $g\bullet
f=(g\bullet 1_B)\circ
(1_C\bullet f)\in{\mathcal{J}}(C\bullet A,D\bullet B)$. On raisonne de même pour les produits à droite.

b\) est immédiat. $\square$

Rappelons qu'un objet $A$ d'une catégorie monoı̈dale ${\mathcal{A}}$ *admet un dual* (à droite) s'il existe un objet $A^\vee\in {\mathcal{A}}$ et des morphismes d'évaluation $$\varepsilon_A:A\bullet A^\vee\to {\bf 1}$$ et de coévaluation $$\eta_A:{\bf 1}\to A^\vee\bullet A$$ tels que les composés $$\begin{CD}
A@> 1_A\bullet\eta_A>> A\bullet A^\vee\bullet A@> \varepsilon_A\bullet 1_A>>
A\\
A^\vee@>\eta_A\bullet 1_{A^\vee}>> A^\vee\bullet A\bullet
A^\vee@>1_{A^\vee}\bullet\varepsilon_A >> A^\vee
\end{CD}$$ soient égaux à l'identité. Le triplet $(A^\vee,\varepsilon_A,\eta_A)$ est déterminé à isomorphisme unique près.

Il en résulte que le foncteur $- \bullet A^\vee$ est adjoint à gauche au foncteur $-\bullet A$ et que le foncteur $A^\vee \bullet -$ est adjoint à droite au foncteur $A\bullet -$. Plus précisément, pour tous objets $B,C$ de ${\mathcal{A}}$, l'homomorphisme composé $$\begin{CD}
{\mathcal{A}}(A\bullet B,C)@>1_{A^\vee}\bullet ->> {\mathcal{A}}(A^\vee\bullet A\bullet B,
A^\vee\bullet C) @>(\eta_A\bullet 1_B)^*>>{\mathcal{A}}(B,A^\vee\bullet C)
\end{CD}$$ est un isomorphisme, d'inverse le composé $$\begin{CD}
{\mathcal{A}}(B,A^\vee\bullet C)@>1_{A}\bullet ->>
{\mathcal{A}}(A\bullet B,A\bullet A^\vee\bullet C) @>(\varepsilon_A\bullet
1_C)_*>>{\mathcal{A}}(A\bullet B,C).
\end{CD}$$ et de même pour l'autre adjonction (*cf.* *e.g.* [@bru1 1]).

Si $A$ et $B$ ont pour duaux à droite $A^\vee$ et $B^\vee$, alors $A\bullet B$ a pour dual à droite $$(A\bullet B)^\vee =B^\vee\bullet A^\vee$$ avec $$\label{eq6.2.0} \varepsilon_{A\bullet B}=
\varepsilon_{A}\circ (1_A\bullet \varepsilon_B \bullet
1_{A^\vee}).$$

On définit de manière duale la notion de dual à gauche ${}^\vee
A$. Si $A$ admet un dual à droite et un dual à gauche, on a $({}^\vee A)^\vee={}^\vee(
A^\vee)=A$. En général, ${}^\vee A$ et $A^\vee$ ne coı̈ncident pas.

::: defn
On dit que $({\mathcal{A}},\bullet)$ est *rigide* si tout objet a un dual à droite et est un dual à droite (ou de manière équivalente, si tout objet a un dual à droite et un dual à gauche).
:::

::: sorite
[]{#sorrig label="sorrig"} Si ${\mathcal{A}}$ est rigide, il en est de même de ${\mathcal{A}}^\oplus,{\mathcal{A}}^\natural$ et de ${\mathcal{A}}^{\oplus\natural}$ (notations du § [\[s1\]](#s1){reference-type="ref" reference="s1"}). Il en est aussi de même du quotient de ${\mathcal{A}}$ par tout idéal monoı̈dal. $\square$
:::

Soient $A$ et $B$ deux objets de ${{\mathcal{A}}}$, $A$ ayant un dual à droite. Par adjonction, on a un isomorphisme canonique de $K$-modules: $$\begin{aligned}
\label{eq6.2.1}\iota_{AB}:&{{\mathcal{A}}}({\bf 1}, A^\vee\bullet B)\overset{\sim}{\longrightarrow}
{{\mathcal{A}}}(A,B)\notag\\
\iota_{AB}(\varphi)&=(\varepsilon_A\bullet 1_B)\circ (1_A\bullet \varphi),
\end{aligned}$$ d'inverse $$\label{eq6.2.2}
\iota_{AB}^{-1}(f)= (1_{A^\vee} \bullet f)\circ  \eta_A.$$

Si $B$ a aussi un dual à droite, la composition de deux morphismes $f\in
{\mathcal{A}}(A,B)$ et $g\in {\mathcal{A}}(B,C)$ peut se calculer comme suit ("composition des correspondances\"): $$\label{eq6.2.3}g\circ f=
\iota_{AC}\left((1_{A^\vee}\bullet
\varepsilon_B \bullet 1_C)(\iota_{AB}^{-1} f\bullet \iota_{BC}^{-1}
g)\right).$$

Appliquant $\iota_{AC}^{-1}$, cette formule fondamentale exprime la commutativité du diagramme $$\begin{CD}
{\bf 1}@>{\eta_A}>>A^\vee A @>1_{A^\vee}\bullet f>> A^\vee B@= A^\vee B \\
@V{\eta_B}VV@V{1_{A^\vee A}\bullet \eta_B}VV@V{1_{A^\vee
B}\bullet\eta_B}VV\left|\right|\\
B^\vee B@>\eta_A\bullet 1_{B^\vee B}>> A^\vee AB^\vee
B@>{1_{A^\vee}\bullet\varepsilon_B\bullet 1_B}>>A^\vee B B^\vee B
@>{1_{A^\vee}\bullet\varepsilon_B\bullet 1_B}>>  A^\vee B\\
@V{1_{B^\vee}\bullet g}VV@V{1_{A^\vee AB^\vee}\bullet g}VV@V{1_{A^\vee
BB^\vee}\bullet g}VV @V{1_{A^\vee}\bullet g}VV\\
B^\vee C@>\eta_A\bullet 1_{B^\vee C}>> A^\vee AB^\vee C@>1_{A^\vee}\bullet
f\bullet 1_{B^\vee C}>>A^\vee B B^\vee C
@>{1_{A^\vee}\bullet\varepsilon_B\bullet 1_C}>> A^\vee C.
\end{CD}$$

On a aussi les variantes $$\label{eq6.2.4} g\circ \iota_{AB}(\varphi)=
\iota_{AC}((1_{A^\vee}\bullet g)\circ \varphi)$$ $$\label{eq6.2.5}  \iota_{BC}(\psi) \circ f=
\iota_{AC}((\varepsilon_B\bullet 1_C)\circ (f\bullet 1_{B^\vee\bullet
C})\circ (1_A\bullet \psi ) )$$ qui se lisent sur le même diagramme.

Si $A, B$ ont des duaux à droite et que $f\in {\mathcal{A}}(A,B)$, on définit (*loc. cit.* ) le transposé $f^t$ (ou dual à droite) de $f$ comme étant le composé $$\label{eq6.2.6}
B^\vee ={\bf 1}\bullet B^\vee \stackrel{\eta_A\bullet 1}{\longrightarrow} A^\vee\bullet A
\bullet B^\vee\stackrel{1\bullet f\bullet 1}{\longrightarrow} A^\vee \bullet B
\bullet B^\vee \stackrel{1\bullet \varepsilon_B }{\longrightarrow} A^\vee \bullet {\bf 1}
=A^\vee,$$ ce qui s'écrit aussi $$\label{eq6.2.6,5} 
f^t=(1_{A^\vee}\bullet
\varepsilon_B )\circ (\iota_{AB}^{-1}(f) \bullet 1_{B^\vee}) ,$$ et on a alors la formule $$\label{eq6.2.7}  (g\circ f)^t= f^t \circ
g^t.$$

On a de même une notion de transposé ${}^tf$ à gauche, et $({}^tf)^t={}^t(f^t)=f$. En général, ${}^tf$ et $f^t$ ne coı̈ncident pas.

::: lemme
[]{#L4.1 label="L4.1"} Tout idéal monoı̈dal ${\mathcal{J}}$ vérifie $${{\mathcal{J}}} (A,B)=\iota_{AB}\big({{\mathcal{J}}}({\bf 1}, A^\vee\bullet B)\big)$$ et $$\big({{\mathcal{J}}}(A,B)\big)^t = {{\mathcal{J}}}(B^\vee ,A^\vee).$$
:::

La première formule découle des formules [\[eq6.2.1\]](#eq6.2.1){reference-type="eqref" reference="eq6.2.1"}, [\[eq6.2.2\]](#eq6.2.2){reference-type="eqref" reference="eq6.2.2"}. Pour la seconde, $$\begin{gathered}
\big({{\mathcal{J}}}(A,B)\big)^t = (1_{A^\vee}\bullet \varepsilon_B )\circ ( 
{{\mathcal{J}}}({\bf 1}, A^\vee\bullet
B)  \bullet 1_{B^\vee}) \\
\subset(1_{A^\vee}\bullet \varepsilon_B )\circ   {{\mathcal{J}}}( {B^\vee} , 
A^\vee\bullet
B\bullet  {B^\vee})  \subset {{\mathcal{J}}}(B^\vee ,A^\vee) .
\end{gathered}$$

L'analogue pour les duaux à gauche de ces deux formules conduit à ${}^t\big({{\mathcal{J}}}(C,D)\big) = {{\mathcal{J}}}({}^\vee D ,{}^\vee C)$. En posant $B={}^\vee C, \,A= {}^\vee D$ (ce qui est loisible puisque ${\mathcal{A}}$ est rigide), et en appliquant ${}^t$, on obtient finalement l'inclusion opposée ${{\mathcal{J}}}(B^\vee ,A^\vee)\subset \big({{\mathcal{J}}}(A,B)\big)^t$. $\square$

On a une réciproque partielle du lemme [\[L4.1\]](#L4.1){reference-type="ref" reference="L4.1"} (mais voir aussi le lemme [\[L4.2\]](#L4.2){reference-type="ref" reference="L4.2"} dans le cas symétrique):

::: lemme
[]{#L4.2bemol label="L4.2bemol"} Soit ${\mathcal{I}}$ un ${\bf 1}$-idéal à gauche de ${\mathcal{A}}$ (définition [\[d1\]](#d1){reference-type="ref" reference="d1"}). La formule $${{\mathcal{I}}}^{(\bullet)}(A,B)=\iota_{AB}\big({{\mathcal{I}}}(A^\vee\bullet B)\big)$$ définit un idéal de ${\mathcal{A}}$ contenant ${\mathcal{I}}$. Cet idéal est monoı̈dal à gauche (stable par produit $\bullet$ à gauche).
:::

Soit $g\in
{{\mathcal{A}}}(B,C)$ un morphisme. En utilisant la formule [\[eq6.2.4\]](#eq6.2.4){reference-type="eqref" reference="eq6.2.4"}, on calcule $$\begin{gathered}
g\circ {{\mathcal{I}}}^{(\bullet)}(A,B) = g\circ  \iota_{AB}\big({{\mathcal{I}}}(A^\vee\bullet
B)\big) = \iota_{AC}\big((1_{A^\vee}\bullet g)\circ
{{\mathcal{I}}}(A^\vee\bullet B)\big) \\
\subset \iota_{AC}\big(  {{\mathcal{I}}}(A^\vee\bullet
C)\big) = {{\mathcal{I}}}^{(\bullet)}(A,C).
\end{gathered}$$

La stabilité par composition à droite se démontre de même en utilisant [\[eq6.2.5\]](#eq6.2.5){reference-type="eqref" reference="eq6.2.5"}.

Enfin, soit $C$ un objet de ${{\mathcal{A}}}$. Observons que l'homomorphisme $$1_C\bullet - :  {{\mathcal{A}}}(A,B)\to {{\mathcal{A}}}(C\bullet A,C\bullet B)$$ n'est autre que $$f\mapsto \iota_{C\bullet A, C\bullet B}[ (1_{A^\vee}\bullet \eta_C
\bullet 1_B)\circ \iota_{AB}^{-1}(f)]$$ où $\eta_C: {\bf 1}\to C^\vee\bullet C$ est la coévaluation. On a donc $$\begin{gathered}
1_C\bullet {{\mathcal{I}}}^{(\bullet)}(A,B) = \iota_{C\bullet A, C\bullet B}[
(1_{A^\vee}\bullet \eta_C \bullet 1_B)\circ
          \big({{\mathcal{I}}}(A^\vee\bullet  B)\big)\\
\subset \iota_{C\bullet A, C\bullet B}  \big({{\mathcal{I}}}(A^\vee\bullet
C^\vee\bullet C\bullet B)\big) = {{\mathcal{I}}}^{(\bullet)}(C\bullet A, C\bullet B).
\end{gathered}$$

On conclut en appliquant (la moitié du) lemme [\[l6.1\]](#l6.1){reference-type="ref" reference="l6.1"}.$\square$

## Le cas symétrique

On suppose désormais que ${\mathcal{A}}$ (qui rappelons-le, est supposée rigide) est munie d'un tressage symétrique $R$ (une contrainte de commutativité, dans le langage de Saavedra). On renvoie à [\[Tre\]](#Tre){reference-type="ref" reference="Tre"} pour plus de détails sur les tressages.

Sous cette hypothèse, ${}^\vee A= A^\vee$ (duaux à droite et à gauche coı̈ncident), et on a $$\label{eq6.2.7,3} \varepsilon_{A^\vee}=\varepsilon_A\circ
R_{A^\vee, A},\eta_{A^\vee}=R_{A^\vee, A}\circ
\eta_A , A^{\vee\vee}=A ,$$ $$\label{eq6.2.7,6}  {}^tf= f^t, \;\;\;\;(f^t)^t=f .$$

On a aussi l'identité $$\label{eq6.2.11}
\iota_{C^\vee,C^\vee}(R_{C^\vee,C}\circ \varphi)=\iota_{C,C}(\varphi)^t$$ (en effet, par [\[eq6.2.6,5\]](#eq6.2.6,5){reference-type="eqref" reference="eq6.2.6,5"} et [\[eq6.2.2\]](#eq6.2.2){reference-type="eqref" reference="eq6.2.2"}, l'image par $\iota_{C^\vee,C^\vee}^{-1}$ du membre de droite s'écrit $(1_{C^\vee}\bullet \varepsilon_C)\circ (\varphi\bullet 1_{C^\vee})$, tandis que celle du membre de gauche s'écrit $(\varepsilon_{C^\vee} \bullet 
1_{C^\vee})\circ (1_{C^\vee}\bullet (R_{C^\vee,C}\circ
\varphi))= ((\varepsilon_{C } \circ R_{C^\vee,C})\bullet 
1_{C^\vee})\circ (1_{C^\vee}\bullet  \varphi)$, et l'égalité des deux membres s'ensuit par permutation des facteurs $C^\vee$.)

Par ailleurs, si $A,B,C,D$ sont quatre objets de ${\mathcal{A}}$ et $\varphi\in
{\mathcal{A}}({\bf 1},A^\vee\bullet B)$, $\psi\in {\mathcal{A}}({\bf 1}, C^\vee\bullet D)$, on a la formule $$\label{eq6.2.8}\iota_{A,B}(\varphi)\bullet\iota_{C,D}(\psi)=
\iota_{A\bullet C,B\bullet D}((R_{A^\vee\bullet B,C^\vee} \bullet
1_D)\circ(\varphi\bullet\psi)).$$

Le lemme suivant complète [\[L4.2bemol\]](#L4.2bemol){reference-type="ref" reference="L4.2bemol"}.

::: lemme
[]{#L4.2 label="L4.2"} Soit ${\mathcal{I}}$ un ${\bf 1}$-idéal à gauche de ${\mathcal{A}}$ (définition [\[d1\]](#d1){reference-type="ref" reference="d1"}). La formule $${{\mathcal{I}}}^{(\bullet)}(A,B)=\iota_{AB}\big({{\mathcal{I}}}(A^\vee\bullet B)\big)$$ définit un idéal monoı̈dal ${{\mathcal{I}}}^{(\bullet)}$; c'est le plus petit idéal monoı̈dal de ${\mathcal{A}}$ contenant ${\mathcal{I}}$.
:::

On a vu que ${{\mathcal{I}}}^{(\bullet)}$ est un idéal contenant ${\mathcal{I}}$, stable par produit à gauche. Par tressage, on a aussi ${{\mathcal{I}}}^{(\bullet)}(A,B) \bullet 1_C \subset 
{{\mathcal{I}}}^{(\bullet)}(A\bullet C,
B\bullet C)$ pour trois objets $A,B,C$. La deuxième assertion est immédiate compte tenu du lemme [\[L4.1\]](#L4.1){reference-type="ref" reference="L4.1"}. $\square$

## Interprétation

Pour expliciter le sens des lemmes [\[L4.1\]](#L4.1){reference-type="ref" reference="L4.1"} et [\[L4.2\]](#L4.2){reference-type="ref" reference="L4.2"}, notons:

-   $\mathbb{G}$ l'ensemble des ${\bf 1}$-idéaux à gauche de ${\mathcal{A}}$;

-   $\mathbb{I}$ l'ensemble des idéaux \[bilatères\] de ${\mathcal{A}}$;

-   $\mathbb{T}$ l'ensemble des idéaux \[bilatères\] monoı̈daux de ${\mathcal{A}}$.

Ces trois ensembles sont ordonnés par inclusion. On a le diagramme suivant d'applications croissantes: $$\begin{CD}
\mathbb{T}&& 
\begin{smallmatrix}i\\\longrightarrow\\\longleftarrow\\j
\end{smallmatrix}&&\mathbb{I}\\
&\scriptstyle t\displaystyle\nwarrow&& 
\scriptstyle
r\displaystyle\swarrow\\ &&\mathbb{G}
\end{CD}$$ où

-   $i$ associe à un idéal monoı̈dal l'idéal sous-jacent;

-   $j$ associe à un idéal le plus petit idéal monoı̈dal le contenant;

-   $r$ associe à un idéal le ${\bf 1}$-idéal à gauche sous-jacent ($r({\mathcal{I}})(A)={\mathcal{I}}({\bf 1},A)$);

-   $t$ associe à un ${\bf 1}$-idéal à gauche ${\mathcal{I}}$ l'idéal monoı̈dal

    ${\mathcal{I}}^{(\bullet)}$ construit dans le lemme [\[L4.2\]](#L4.2){reference-type="ref" reference="L4.2"}.

On a évidemment $ji=Id$. Le lemme [\[L4.1\]](#L4.1){reference-type="ref" reference="L4.1"} dit que $tri=Id$, tandis que le lemme [\[L4.2\]](#L4.2){reference-type="ref" reference="L4.2"} dit que $rit=Id$. En particulier, *les applications $t$ et $ri$ sont des bijections inverses l'une de l'autre*. D'autre part, soit ${\mathcal{I}}\in
\mathbb{I}$. Comme $j({\mathcal{I}})$ contient $r({\mathcal{I}})$, on a $j({\mathcal{I}})\supset 
tr({\mathcal{I}})$, et $j({\mathcal{I}})=tr({\mathcal{I}})$ si et seulement si $tr({\mathcal{I}})\supset 
{\mathcal{I}}$.

Par abus de notation, on écrira encore ${\mathcal{I}}^{(\bullet)}$ pour $tr({\mathcal{I}})$ si ${\mathcal{I}}\in \mathbb{I}$.

Par ailleurs, les ensembles $\,\mathbb{G},\,\mathbb{I},\,\mathbb{T}$ sont munis d'opérations internes "somme\", "intersection\". Il est clair que les applications $i,t,r$ respectent ces opérations.

Le cas du produit est plus intéressant. *A priori*, seuls $\mathbb{I}$ et $\mathbb{T}$ sont munis d'une opération "produit\" évidente. On peut alors munir $\mathbb{G}$ d'un tel produit en posant: ${\mathcal{I}}\cdot{\mathcal{J}}:=
ri(t({\mathcal{I}})\cdot t({\mathcal{J}}))$ (en formule: $$\label{eq15}
({\mathcal{I}}\cdot{\mathcal{J}})(B)   = \sum_A 
\iota_{AB}({\mathcal{I}}(A^\vee \bullet
B))\circ {\mathcal{J}}(A) \;\; 
).$$

Les applications $i,t,r$ respectent alors aussi le produit. On a aussi la formule $$\label{eq15sym}
({\mathcal{I}}\cdot{\mathcal{J}})(B)   = \sum_{u: 
A\bullet A'\to B} 
 Im({\mathcal{J}}(A)  \bullet {\mathcal{I}}(A') \to {\mathcal{A}}({\bf 1}, B))$$ qui montre que le produit des idéaux monoı̈daux (dans le cas rigide) est *symétrique*.

Pour $A'=A^\vee\bullet B$ et $u=
\varepsilon_A
\bullet 1_B$, le terme du second membre de ([\[eq15sym\]](#eq15sym){reference-type="ref" reference="eq15sym"}) s'écrit en effet $(\varepsilon_A \bullet 
1_B)\circ ({\mathcal{J}}(A)\bullet {\mathcal{I}}(A^\vee \bullet
B))$, qui coı̈ncide d'après ([\[eq6.2.5\]](#eq6.2.5){reference-type="ref" reference="eq6.2.5"}) avec le terme courant du second membre de ([\[eq15\]](#eq15){reference-type="ref" reference="eq15"}) (donc avec $({\mathcal{I}}\cdot{\mathcal{J}})(B)$). Réciproquement, ${\mathcal{J}}(A) 
\bullet {\mathcal{I}}(A')\subset  (t({\mathcal{J}}) \cdot 
t({\mathcal{I}}))(A\bullet A')$ puisque $t({\mathcal{J}})$ et $t({\mathcal{I}})$ sont des idéaux monoı̈daux, d'où il découle que le second membre de ([\[eq15sym\]](#eq15sym){reference-type="ref" reference="eq15sym"}) est contenu dans $({\mathcal{I}}\cdot{\mathcal{J}})(B)$.

::: ex
[]{#ex2 label="ex2"} Si ${\mathcal{A}}$ est la catégorie monoı̈dale des motifs de Grothendieck pour l'équivalence rationnelle (motifs 'de Chow') à coefficients dans $K$ et si $K$ est un corps, il y a bijection entre les idéaux monoı̈daux de ${\mathcal{A}}$ et les relations d'équivalence adéquates sur les cycles algébriques à coefficients dans $K$.

Il est plus facile de décrire la bijection entre ${\bf 1}$-idéaux à gauche de ${\mathcal{A}}$ et relations d'équivalence adéquates (*cf.* [@jannsen2 4]). Soit ${\mathcal{I}}$ un tel ${\bf 1}$-idéal, c'est-à-dire la donnée d'une famille de sous-groupes ${\mathcal{I}}(M)$ de ${\mathcal{A}}({\bf 1},M)$ stable par l'action à gauche des correspondances, où $M$ décrit les objets de ${\mathcal{A}}$. Pour le motif $M$ d'une variété $X$ tordu $m$ fois à la Tate, on a ${\mathcal{A}}({\bf 1},M)=CH^m(X)_K$, donc ${\mathcal{I}}$ définit une relation d'équivalence adéquate. Inversement, toute relation d'équivalence adéquate définit un ${\bf 1}$-idéal à gauche de la catégorie des correspondances de Chow (non effectives), et on vérifie que les ${\bf 1}$-idéaux à gauche de cette catégorie sont en correspondance bijective avec ceux de son enveloppe pseudo-abélienne ${\mathcal{A}}$.

On déduit de ([\[eq15\]](#eq15){reference-type="ref" reference="eq15"}) la formule pour le produit de relations d'équivalence adéquates (correspondant au produit d'idéaux, et noté $\ast$ dans *loc. cit.* ).
:::

[^1]: Voir §[1](#ext){reference-type="ref" reference="ext"} ci-dessous pour plus de détails.

[^2]: Jannsen [@jannsen2] dit plutôt *tensoriel*.
