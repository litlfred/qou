---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-009-112-complexe-de-hochschild-mitchell
section_title: "Complexe de Hochschild-Mitchell"
section_number: 11.2
pages: 59-63
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.93
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
[]{#7.2 label="7.2"} Soit ${\mathcal{A}}$ une petite $K$-catégorie, telle que pour tout $(A,B)\in
{\mathcal{A}}\times {\mathcal{A}}$, ${\mathcal{A}}(A,B)$ soit un $K$-module projectif.

Notons $C_*({\mathcal{A}})$ le complexe de Hochschild de ${\mathcal{A}}$ [@mitchell § 17]: c'est un complexe de ${{\mathcal{A}}}^e$-modules tel que $$\scriptstyle 
C_m({\mathcal{A}})(A,B)=\displaystyle\bigoplus_{A_0,\dots,A_{m}}
\scriptstyle
\scriptstyle
A(A,A_0)\otimes_K{\mathcal{A}}(A_0,A_1)\otimes_K\dots\otimes_K{\mathcal{A}}(A_{m-1}
,A_m) 
\otimes_K {\mathcal{A}}(A_m,B),\quad m\geq 0$$ où $(A_0,\dots,A_m)$ décrit les $n$-uplets d'objets de ${\mathcal{A}}$. La différentielle est $$d_m(f_0\otimes
f_1\otimes\dots\otimes 
f_{m+1})=
\sum_{i=0}^m(-1)^if_0\otimes
f_1\otimes\dots \otimes 
f_if_{i+1}\otimes\dots \otimes f_{m+1}.$$

Il est connu que $C_*({\mathcal{A}})$ est une résolution projective du ${{\mathcal{A}}}^e$-module ${{\mathcal{A}}}$.

Pour tout ${{\mathcal{A}}}^e$-module $M$, on note $C^*({\mathcal{A}},M)$ le complexe de $K$-modules $Hom_{{\mathcal{A}}^e}(C_*({\mathcal{A}}), M)$. Plus concrètement, pour $m>0$, un élément de $C^m({\mathcal{A}},M)(A,B)$ *équivaut* à la donnée d'un élément de $M(A,B)$ pour chaque $m$-uplet de flèches composables $(f_1,\dots,
f_{m})$, $f_1$ étant de source $A$ et $f_m$ de but $B$, cette donnée étant $K$-multilinéaire en $(f_1,\dots, f_{m})$; pour $m=0$, c'est la donnée d'un élément de $M(A,A)$ pour tout $A$.

Voici comment: on obtient une telle donnée en considérant, dans $Hom_{{\mathcal{A}}^e}(C_*({\mathcal{A}}), M)(A_0,A_m)$ le facteur correspondant à $A=A_0, f_0=1_{A_0}, B=A_{m},
f_{m}=1_{A_{m}}$. Réciproquement, une telle donnée fournit une cochaı̂ne de Hochschild grâce à la commutativité du carré (bivariance en $(A,B)$): $$\begin{CD}
Hom_{{\mathcal{A}}^e}(C_*({\mathcal{A}}), M)(A,B) 
@>>>M(A,B)\\
@V{(f_0,f_{m+1})}VV 
@V{(f_0,f_{m+1})}VV\\
Hom_{{\mathcal{A}}^e}(C_*({\mathcal{A}}), M)(A_0,A_m) @>>> 
M(A_0,A_m).
\end{CD}$$

Avec cette interprétation, la différentielle de Hochschild prend la forme habituelle $$\begin{gathered}
(d^m\varphi)(f_1,\dots,
f_{m+1})=f_1\varphi(f_2, 
\dots, 
f_{m+1})\\
+\sum_1^m
(-1)^i\varphi(f_1,\dots,f_if_{i+1},\dots,
f_{m+1})\\ 
+(-1)^{m+1}\varphi(f_1,\dots, f_m)f_{m+1}.
\end{gathered}$$

Puisque $C_*({\mathcal{A}})$ est une résolution projective du ${{\mathcal{A}}}^e$-module ${{\mathcal{A}}}$, on a $$H^i({\mathcal{A}}, M):= 
H^i(C^*({\mathcal{A}},M))=\operatorname{Ext}^i_{{\mathcal{A}}^e}({{\mathcal{A}}},M).$$

Si ${\mathcal{A}}$ est séparable, ${\mathcal{A}}^e$ est semi-simple, donc ces groupes de cohomologie sont donc

nuls pour tout $M$ et tout $i>0$ (*cf.* lemme [\[L6\]](#L6){reference-type="ref" reference="L6"} et proposition [\[P4/3\]](#P4/3){reference-type="ref" reference="P4/3"}).

La formation de $C_*({\mathcal{A}})$ est naturelle en ${\mathcal{A}}$. Plus précisément, tout $K$-foncteur $F: 
{\mathcal{A}}\to {\mathcal{B}}$ donne lieu à des applications $K$-linéaires $C_n({\mathcal{A}})(A,B)\allowbreak\to C_n({\mathcal{B}})(FA,FB)$, et, pour tout ${\mathcal{B}}^e$-module $N$, à un homomorphisme de complexes de $K$-modules dans l'autre sens $$C^*({\mathcal{B}},N)\to  C^*({\mathcal{A}},F^\ast 
N).$$

::: rem
[]{#rhoch label="rhoch"} (Homologie de Hochschild) Si $M$ et $N$ sont deux ${\mathcal{A}}$-bimodules, on peut voir $M$ comme ${{\mathcal{A}}^e}$-module à droite, et $N$ comme ${{\mathcal{A}}^e}$-module à gauche, ce qui permet de former le $K$-module $M\otimes_{{\mathcal{A}}^e} N$ (*cf.* [@mitchell pp. 29, 71]). Cette construction étant fonctorielle en $N$, on peut bâtir un complexe $M\otimes_{{\mathcal{A}}^e} 
C_*({\mathcal{A}})$, et on a $$H_i({\mathcal{A}}, M):= H_i(M\otimes_{{\mathcal{A}}^e} 
C^*({\mathcal{A}}))=\operatorname{Tor}_i^{{\mathcal{A}}^e}(M,{{\mathcal{A}}}).$$ En particulier, pour $i=0$, on retrouve la notion du §[\[h0\]](#h0){reference-type="ref" reference="h0"}.
:::

# Un "théorème de Wedderburn à plusieurs objets\" {#s5}

Dans ce paragraphe, on se donne un corps $K$. On renvoie à la définition [\[D4wed\]](#D4wed){reference-type="ref" reference="D4wed"} pour la notion de $K$-catégorie de Wedderburn.

## Existence et "unicité\" de sections

Le théorème de structure fondamental pour les $K$-algèbres de Wedderburn (théorème de Wedderburn) dit que toute extension d'une $K$-algèbre séparable de dimension finie par un idéal nilpotent se scinde. En suivant la preuve cohomologique classique de Hochschild et Whitehead, nous généralisons ce résultat aux algèbres "à plusieurs objets\".

::: thm
[]{#T1 label="T1"} Soit ${\mathcal{A}}$ une petite $K$-catégorie de Wedderburn, de radical ${\mathcal{R}}$. Posons $\bar{\mathcal{A}}= {\mathcal{A}}/{\mathcal{R}}$. Alors:\
a) Le $K$-foncteur de projection $\pi_{{\mathcal{A}}}:{\mathcal{A}}\to \bar{\mathcal{A}}$ admet une section $s$.\
b) Si $s'$ est une autre section, il existe une famille $(u_A)_{A\in
{\mathcal{A}}}, u_A \in 
1_A+{\mathcal{R}}(A,A)$, telle que pour tous $A,B\in
{\mathcal{A}}$ et tout $f\in 
\bar{\mathcal{A}}(A,B)$, on ait $s'(f)=
u_Bs(f)(u_A)^{-1}$.
:::

$1)$ Supposons d'abord ${\mathcal{R}}^2=0$. Alors ${\mathcal{R}}$ hérite d'une structure de $\bar{\mathcal{A}}^e$-module par passage au quotient de l'action de ${\mathcal{A}}$.

Pour tout $A,B\in {\mathcal{A}}$, choisissons une section $K$-linéaire $$\sigma_{A,B}: \bar{\mathcal{A}}(A,B)\to {\mathcal{A}}(A,B)$$

de la projection naturelle. Si $C$ est un troisième objet de ${\mathcal{A}}$ et si $(f,g)\in \bar{\mathcal{A}}(A,B)\times
               \bar{\mathcal{A}}(B,C)$, notons $$\gamma(g,f)=\sigma_{A,C}(gf)-\sigma_{B,C}(g)\sigma_{A,B}(f).$$

C'est un élément de ${\mathcal{R}}(A,C)$, et, si $D$ est un quatrième objet et $h\in \bar{\mathcal{A}}(C,D)$, on a la relation $$\gamma(h,gf)+h\gamma(g,f)=\gamma(hg,f)+\gamma(h,g)f.$$

Ain si $\gamma$ définit un *$2$-cocycle de Hochschild* de $\bar{\mathcal{A}}$ à valeurs dans ${\mathcal{R}}$. D'après le § [\[hochschild\]](#hochschild){reference-type="ref" reference="hochschild"}, ce $2$-cocycle est un $2$-cobord; autrement dit, il existe une fonction $\rho$ telle que, pour tous $f,g$ composables, on ait $$\gamma(g,f)=\rho(gf)-g\rho(f)-\rho(g)f.$$

La nouvelle section $s(f)=\sigma(f)-\rho(f)$ vérifie alors $s(gf)=s(g)s(f)$ pour tout couple $(f,g)$ composable.

$2)$ Posons $\delta(f)=s'(f)-s(f)\in 
{\mathcal{R}}(A,B)$. On a, pour tout couple $(f,g)$ composable, $$\delta(gf)=\delta(g)f+\delta(f)g$$ donc $\delta$ est un $1$-cocycle de Hochschild. C'est donc un cobord $f\mapsto n_B f-fn_A$ pour un choix convenable d'éléments $n_A\in
{\mathcal{R}}(A,A)$. En posant $u_A= 1_A+n_A$, on a bien $s'(f)=
u_Bs(f)(u_A)^{-1}$.

$3)$ Supposons maintenant ${\mathcal{R}}$ nilpotent d'échelon $r+1$. On raisonne par récurrence sur $r$, le cas $r=1$ étant traité ci-dessus. Soit ${\mathcal{A}}^{(r)}={\mathcal{A}}/{\mathcal{R}}^{r}$: le radical ${\mathcal{R}}^{(r)} 
=
{\mathcal{R}}/{\mathcal{R}}^r$ de ${\mathcal{A}}^{(r)}$ est nilpotent d'échelon $r$, donc il existe une section $\bar s:\bar{\mathcal{A}}\to {\mathcal{A}}^{(r)}$ comme dans l'énoncé, et toute autre section s'en déduit par "conjugaison\" par une famille de $\bar u_A\in 1_A+{\mathcal{R}}^{(r)} (A,A)$.

Soit $\bar 
s(\bar{\mathcal{A}})$ l'image d'une telle section $\bar
s$ dans ${\mathcal{A}}^{(r)}$. Pour tout morphisme $f$ dans ${\mathcal{A}}$, notons $f^{(r)}$ son image dans ${\mathcal{A}}^{(r)}$. Posons $$\begin{aligned}
{\tilde{\mathcal{A}}}(A,B)&=\{f\in 
{\mathcal{A}}(A,B)\mid  f^{(r)}\in 
\bar
s(\bar{\mathcal{A}})(A,B)\}\\
{\tilde{\mathcal{R}}}(A,B)&={\mathcal{R}}(A,B)\cap 
{\tilde{\mathcal{A}}}(A,B).
\end{aligned}$$

Alors ${\tilde{\mathcal{A}}}$ est une sous-catégorie (non pleine) de ${\mathcal{A}}$, ${\tilde{\mathcal{R}}}$ est son radical, ${\tilde{\mathcal{R}}}^2=0$, et ${\tilde{\mathcal{A}}}/{\tilde{\mathcal{R}}}=\bar{\mathcal{A}}$. Il existe donc une section $\tilde s:\bar
s(\bar{\mathcal{A}})\to {\tilde{\mathcal{A}}}$; la composée $s=\iota\circ\tilde s\circ
\bar s:\bar{\mathcal{A}}\to 
\bar
s(\bar{\mathcal{A}})\to{\tilde{\mathcal{A}}}\to
{\mathcal{A}}$, où $\iota$ est l'inclusion canonique, est la section cherchée.

Si $s'$ est une autre section, notons $\bar s'$ la composition $\bar{\mathcal{A}}\overset{s'}{\to}{\mathcal{A}}\to 
{\mathcal{A}}^{(r)}$, et soit $(\bar u_A)$ une famille d'éléments de $1_A+{\mathcal{A}}^{(r)}(A,A)$ tels que $\bar s'(f)=\bar u_B
\bar s(f) (\bar 
u_A)^{-1}$ pour tout $f\in
{\mathcal{A}}^{(r)}(A,B)$. Choisissons des relevés $u_A$ des $\bar u_A$ dans ${\mathcal{A}}(A,A)$. Quitte à changer $s'$ en la section conjuguée par les $(u_A)^{-1}$, on se ramène au cas où $\bar s'=\bar s$. On conclut par l'étape $2)$.

$4)$ Établissons maintenant l'assertion $a)$ du théorème dans le cas général. Si l'on supposait ${\mathcal{A}}$ strictement de Wedderburn, il suffirait de la voir comme limite projective des ${\mathcal{A}}^{(r)}$ du numéro précédent, cette limite étant alors localement stationnaire sur les $Hom$s, et d'appliquer directement ce numéro. Mais nous supposons ${\mathcal{A}}$ seulement de Wedderburn, ce qui complique la démonstration.

Considérons l'ensemble des couples $({\mathcal{B}}, s)$ formés d'une sous-catégorie pleine ${\mathcal{B}}$ de ${\mathcal{A}}$ et d'une section fonctorielle $s$ de la projection ${\mathcal{B}}\to \bar {\mathcal{B}}$ ($\bar {\mathcal{B}}$ peut être vue comme sous-catégorie pleine de $\bar{\mathcal{A}}$). Cet ensemble est non vide: d'après les pas précédents, il contient par exemple des couples $({\mathcal{B}}, s)$ dès que $Ob({\mathcal{B}})$ est fini.

On ordonne cet ensemble en décrétant que $({\mathcal{B}}', s')\prec ({\mathcal{B}},
s)$ si ${\mathcal{B}}'\subset {\mathcal{B}}$ et si $s'$ est la restriction de $s$ à $\bar{\mathcal{B}}'$. Il est clair que cet ensemble ordonné est inductif, donc admet un élément maximal $({\mathcal{B}}, s)$ d'après Zorn. Démontrons par l'absurde que ${\mathcal{B}}={\mathcal{A}}$. Sinon, soit $X$ un objet de ${\mathcal{A}}$ qui n'est pas dans ${\mathcal{B}}$. On peut remplacer ${\mathcal{A}}$ par sa sous-catégorie pleine dont les objets sont $X$ et ceux de ${\mathcal{B}}$, et il s'agit de construire une extension de $s$ à $\bar {\mathcal{A}}$. Pour cela, on peut derechef remplacer ${\mathcal{A}}$ par toute sous-catégorie non pleine ${\mathcal{A}}'$ ayant mêmes objets, et telle que ${\mathcal{A}}'/({\mathcal{A}}'\cap {\mathcal{R}})=\bar{\mathcal{A}}$.

Il y a un choix minimal d'une telle ${\mathcal{A}}'$: celle dont les morphismes sont des sommes finies de compositions de flèches de $s({\mathcal{B}})$ et de flèches de ${\mathcal{A}}$ de source ou de but $X$. Le radical de cette $K$-catégorie ${\mathcal{A}}'$ n'est autre que ${\mathcal{A}}'\cap {\mathcal{R}}$: en effet, tous les $({\mathcal{A}}'\cap {\mathcal{R}})(A,A)$ sont des nil-idéaux, ce qui entraı̂ne que $({\mathcal{A}}'\cap {\mathcal{R}})\subset
{\operatorname{rad}}({\mathcal{A}}')$; réciproquement, ${\mathcal{A}}'/({\mathcal{A}}'\cap
{\mathcal{R}})=\bar{\mathcal{A}}$ est semi-simple, donc ${\operatorname{rad}}({\mathcal{A}}')\subset {\mathcal{A}}'\cap {\mathcal{R}}$.

Le point est que ${\mathcal{A}}'\cap {\mathcal{R}}$ est (globalement) nilpotent, ce qui permet, par le pas 3), d'étendre $s$ comme souhaité. En fait, nous allons voir que si $n$ est l'échelon de nilpotence de l'idéal ${\mathcal{R}}(X,X)$ de ${\mathcal{A}}(X,X)$, alors ${\operatorname{rad}}({\mathcal{A}}')^{(2n+1)}=0$. En effet, comme le radical de $s({\mathcal{B}})$ est nul, on observe que pour tout couple d'objets $(A,B)$ de ${\mathcal{A}}$, tout élément de ${\operatorname{rad}}({\mathcal{A}}')(A,B)$ s'écrit comme combinaison linéaire finie $\sum f^i_{XB}\circ g^i_{AX}$, avec $f^i_{XB}\in {\mathcal{A}}(X,B), g^i_{AX}\in {\mathcal{A}}(A,X)$. Tout élément de ${\operatorname{rad}}({\mathcal{A}}')^{(2n+1)}(A,B)$ s'écrit comme somme finie de termes de la forme

$$\begin{gathered}
\sum_{i_1,i_3,\dots,i_{2n+1}} 
f^{i_{2n+1}}_{XB}
g^{i_{2n+1}}_{A_{2n}X}\left( \sum_{i_{2n}} f^{i_{2n 
}}_{XA_{2n}}
g^{i_{2n }}_{A_{2n-1}X}\right)f^{i_{2n-1}}_{XA_{2n-1}} 
\dots\\  \left(
\sum_{i_{2}} f^{i_{2 
}}_{XA_{2}}
g^{i_2}_{A_1X}\right)f^{i_1}_{XA_1} 
g^{i_1}_{AX}.
\end{gathered}$$

Or chaque fragment $g^{i_{2k+1}}_{A_{2k}X}( \sum_{i_{2k}} f^{i_{2k
}}_{XA_{2k}}
g^{i_{2k 
}}_{A_{2k-1}X})f^{i_{2k-1}}_{XA_{2k-1}}$ est dans $${\mathcal{A}}(A_{2k},X)\circ 
{\operatorname{rad}}({\mathcal{A}}')(A_{2k-1},A_{2k})\circ
{\mathcal{A}}(X,A_{2k-1})\subset 
{\mathcal{R}}(X,X).$$

Comme ces fragments apparaissent $\;n\;$ fois consécutives, on trouve bien que $\;{\operatorname{rad}}({\mathcal{A}}')^{(2n+1)}(A,B)=0\;$. Ceci achève la preuve de l'assertion $a)$.

$5)$ Un argument analogue s'applique pour l'assertion $b)$. Soient $s$ et $s'$ deux sections fixées. Par Zorn, il existe une sous-catégorie pleine maximale ${\mathcal{B}}$ de ${\mathcal{A}}$ telle que les restrictions de $s$ et $s'$ à $\bar{\mathcal{B}}$ soient conjuguées au sens de l'assertion $b)$. Raisonnant par l'absurde comme ci-dessus, on peut encore supposer que $Ob({\mathcal{A}})=Ob({\mathcal{B}})\cup\{X\}$. Quitte à conjuguer $s$ au-dessus de $\bar{\mathcal{B}}$, on peut supposer que les restrictions de $s$ et $s'$ à $\bar{\mathcal{B}}$ coı̈ncident. On observe alors que $s$ et $s'$ prennent alors leurs valeurs dans la sous-catégorie ${\mathcal{A}}'$ non pleine de ${\mathcal{A}}$ définie comme ci-dessus. Comme on l'a vu, son radical est globalement nilpotent, ce qui permet d'appliquer le pas 3) et de conclure que $s$ et $s'$ sont conjuguées via une famille d'éléments $u_A\in 1_A+{\mathcal{R}}(A,A)$.$\square$

Le lemme suivant, souvent utile, résulte immédiatement de la proposition [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"} b) et du fait que $\bar {\mathcal{A}}$ est semi-simple:

::: lemme
[]{#l2 label="l2"} Supposons ${\mathcal{A}}$ pseudo-abélienne. Soit $s$ une section de $\pi_{\mathcal{A}}$. Les foncteurs $\pi_{\mathcal{A}}$ et $s$ induisent des bijections inverses l'une de l'autre entre les objets indécomposables de ${\mathcal{A}}$ et les objets irréductibles de $\bar{\mathcal{A}}$.$\square$
:::

::: rem
[]{#r3 label="r3"} Supposons $K$ algébriquement clos. Soit $A$ un objet indécomposable. Alors par Schur, $\bar{\mathcal{A}}(A,A)=K$, donc il y a un unique relevé dans la $K$-algèbre locale ${\mathcal{A}}(A,A)$. Si $B$ est un indécomposable non isomorphe à $A$, alors $\pi_{\mathcal{A}}(A)$ et $\pi_{\mathcal{A}}(B)$ sont des irréductibles non isomorphes dans $\bar{\mathcal{A}}$, donc $\bar{\mathcal{A}}(A, B)=0$. Il en découle que $s$ existe et est unique si les objets de ${\mathcal{A}}$ sont tous indécomposables et deux à deux non isomorphes.

Voici comment tirer de là une preuve élémentaire (non cohomologique) de l'existence d'une section fonctorielle de $\pi_{\mathcal{B}}$ pour une petite catégorie semi-primaire ${\mathcal{B}}$ sur un corps algébriquement clos $K$, dont les $K$-algèbres d'endomorphismes sont de dimension finie. Supposons d'abord ${\mathcal{A}}$ $K$-linéaire et pseudo-abélienne. Il suit de cette hypothèse que tout objet de ${\mathcal{B}}$ est somme directe finie d'indécomposables. Il résulte du § [\[i1\]](#i1){reference-type="ref" reference="i1"} ci-dessous que l'énoncé du théorème [\[T1\]](#T1){reference-type="ref" reference="T1"} est invariant par équivalence $K$-linéaire de catégories et par passage aux complétions $K$-linéaires et pseudo-abéliennes. Il suffit alors d'appliquer le raisonnement précédent à une sous-catégorie pleine ${\mathcal{A}}$ de ${\mathcal{B}}$ dont les objets forment un système de représentants des classes d'isomorphie d'objets indécomposables de ${\mathcal{A}}$.
:::
