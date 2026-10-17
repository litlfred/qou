---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-019-137-variantes
section_title: "Variantes"
section_number: 13.7
pages: 76-79
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.909
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
Voici un avatar monoı̈dal de la proposition [\[P3\]](#P3){reference-type="ref" reference="P3"}.

::: prop
[]{#P3' label="P3'"} Soit $({\mathcal{B}}, \bullet)$ une autre catégorie monoı̈dale vérifiant les hypothèses du théorème [\[T2\]](#T2){reference-type="ref" reference="T2"}. Soit $T:{\mathcal{B}}\to
{\mathcal{A}}$ un $K$-foncteur monoı̈dal radiciel. Notons $\bar T:\bar
{\mathcal{B}}\to \bar {\mathcal{A}}$ le foncteur induit.\
Soit $s_{\mathcal{A}}:\bar{\mathcal{A}}\to {\mathcal{A}}$ (*resp.* $s_{\mathcal{B}}:\bar{\mathcal{B}}\to {\mathcal{B}}$ ) une section monoı̈dale de la projection canonique.\
Alors $s_{\mathcal{A}}\circ \bar T$ et $T\circ s_{\mathcal{B}}$ sont isomorphes (via un isomorphisme monoı̈dal qui couvre l'isomorphisme monoı̈dal identique modulo les radicaux).\
En particulier, si $T$ et les sections $s_A$ et $s_B$ sont strictes, il existe un système $(u_X)$ d'éléments de $1_{T(X)}+ {\operatorname{rad}}({\mathcal{A}})(T(X),T(X))$ tel que $s_{\mathcal{A}}\bar
T(h)=u_{X'}Ts_{\mathcal{B}}(h)(u_X)^{-1}$ pour tout $h\in \bar {\mathcal{B}}(X,X')$, et $u_{X\bullet Y}=u_X\bullet u_Y$.
:::

On prouve d'abord la seconde assertion, sous l'hypothèse que ${\mathcal{A}}$ et ${\mathcal{B}}$ sont monoı̈dales strictes. La preuve est entièrement parallèle à celle du point $b)$ de la proposition [\[p5\]](#p5){reference-type="ref" reference="p5"}. La proposition [\[P3\]](#P3){reference-type="ref" reference="P3"} montre l'existence d'un système $(u_X)$ d'éléments de $1_{T(X)}+ {\operatorname{rad}}({\mathcal{A}})(T(X),T(X))$ tel que $s_{\mathcal{A}}\bar
T(h)=u_{X'}Ts_{\mathcal{B}}(h)(u_X)^{-1}$ pour tout $h\in \bar {\mathcal{B}}(X,X')$. Pour le modifier en un système vérifiant de plus $u_{X\bullet Y}=u_X\bullet
u_Y$, on construit une suite d'approximations $u^r_X$. Le point est de remplacer le $K\langle Ob({\mathcal{A}})\rangle$-bimodule $C^{[r]}$ par le $K\langle Ob({\mathcal{B}})\rangle$-bimodule $\displaystyle {C'}^{[r]} =\prod_w C'(w)^{[r]}$, où $C'(w)^{[r]}$ est défini de la manière suivante: $$C_{Ts}(w)=\{x\in {\mathcal{A}}(T(\overset{\bullet}{w}))\mid x
(Ts_{\mathcal{B}}(h))=(Ts_{\mathcal{B}}(h))x\text{ pour tout }
h\in\bar{\mathcal{B}}(w)\}$$ $$C_{Ts}^r(w)= {\mathcal{R}}_{\mathcal{A}}(T(\overset{\bullet}{w}))^r\cap C_{Ts}(w)$$ $${C'}^{[r]}(w)=\frac{C_{Ts}^r(w)+{\mathcal{R}}_{\mathcal{A}}(T(\overset{\bullet}{w}))^{r+1}}{{\mathcal{R}}_{\mathcal{A}}(T
(\overset{\bullet}{w}))^{r+1}}\simeq
C_{Ts}^r(w)/C_{Ts}^{r+1}(w).$$ Passons maintenant au cas général. D'après le théorème de conjugaison des sections monoı̈dales, il est loisible de changer de sections $s_{\mathcal{A}}, s_{\mathcal{B}}$. Plutôt que $s_{\mathcal{A}}, s_{\mathcal{B}}$, c'est de ${s'}_{\mathcal{A}}= u_{\mathcal{A}}\circ (s_{\mathcal{A}})^{str} \circ \bar v_{\mathcal{A}},\;{s'}_{\mathcal{B}}= 
u_{\mathcal{B}}\circ (s_{\mathcal{B}})^{str} \circ \bar v_{\mathcal{B}}$ dont nous nous servirons (avec les notations de la construction de MacLane [\[constrM\]](#constrM){reference-type="ref" reference="constrM"}). On est alors ramené à voir que $(s_{\mathcal{A}})^{str} \circ \bar T^{str}$ et $T^{str}\circ (s_{\mathcal{B}})^{str}$ sont isomorphes (via un isomorphisme monoı̈dal qui couvre l'isomorphisme monoı̈dal identique modulo les radicaux); mais on est alors dans le cas strict déjà traité.$\square$

::: cor
Dans la situation de la proposition [\[P3\]](#P3){reference-type="ref" reference="P3"}, supposons ${\mathcal{A}}$, ${\mathcal{B}}$ strictement $K$-linéaires, *i.e.* telles que $\oplus$ soit strictement associative (*cf.* [\[ml\]](#ml){reference-type="ref" reference="ml"}). Supposons aussi que $T$ soit strict vis-à-vis de $\oplus$. Alors on peut choisir les $(u_X)$ (conjuguant $s_{\mathcal{A}}\bar
T$ et $Ts_{\mathcal{B}}$) de telle sorte que $u_{X\oplus Y}=u_X\oplus u_Y$.$\square$
:::

Voici une variante monoı̈dale du complément de Malcev au théorème de Wedderburn.

::: prop
[]{#cmmalcev label="cmmalcev"} Sous les hypothèses du théorème [\[T2\]](#T2){reference-type="ref" reference="T2"}, supposons donnée en outre une sous-catégorie monoı̈dale ${\mathcal{B}}$ *séparable* de ${\mathcal{A}}$ (non nécessairement pleine), telle que tout objet de ${\mathcal{A}}$ soit facteur direct d'un objet de ${\mathcal{B}}$. Alors il existe une section monoı̈dale $s$ de $\pi_{\mathcal{A}}$ qui vérifie $(s\circ \pi_{\mathcal{A}})\vert 
{\mathcal{B}}= id_{{\mathcal{B}}}$.
:::

Quitte à remplacer ${\mathcal{A}}$ et ${\mathcal{B}}$ par ${\mathcal{A}}^\natural$ et ${\mathcal{B}}^\natural$ respectivement, on peut supposer que $Ob({\mathcal{B}})=Ob({\mathcal{A}})$. Dans ce cas, le corollaire [\[cmalcev\]](#cmalcev){reference-type="ref" reference="cmalcev"} montre l'existence d'une section fonctorielle de $\pi_{\mathcal{A}}$ telle que $(s\circ \pi_{\mathcal{A}})_{\vert
{\mathcal{B}}} = id_{{\mathcal{B}}}$. Pour la modifier en une section monoı̈dale vérifiant la même condition, on reprend la méthode de preuve du théorème [\[T2\]](#T2){reference-type="ref" reference="T2"} a), en construisant une suite d'approximations $s_r$ (*cf.* le lemme [\[l5\]](#l5){reference-type="ref" reference="l5"} et sa preuve). Le point est de remplacer le $K\langle 
Ob({\mathcal{A}})\rangle$-bimodule $M^{[r]}$ par le sous-bimodule $\displaystyle {M'}^{[r]} =\prod_w
M'(w)^{[r]}$, où $M'(w)^{[r]}$ est le sous-$K$-espace de $M(w)^{[r]}$ des éléments dont un relevé dans ${\mathcal{R}}(\overset{\bullet}{w})^{[r]}$ commute à $\bar{\mathcal{B}}(w)$. On observe qu'on a bien $ad^{AB}n_{AB}\in M'(AB)^{[r]}$ puisque la restriction de $s_r$ à ${\mathcal{B}}=\bar{{\mathcal{B}}}$ est monoı̈dale (c'est l'identité); on obtient ainsi des $\nu_A$ commutant à $\bar{\mathcal{B}}(A)$, de sorte que $s_{r+1}$ est encore l'identité sur ${\mathcal{B}}=\bar{{\mathcal{B}}}$. $\square$

## Complément

Ce complément servira au §[\[tre\]](#tre){reference-type="ref" reference="tre"}.

::: prop
[]{#t3 label="t3"} Sous les hypothèses du théorème [\[T2\]](#T2){reference-type="ref" reference="T2"}, soit $v$ une structure monoı̈dale sur le foncteur identique de ${\mathcal{A}}$ telle que $\pi_{\mathcal{A}}(v)=1$. Alors $(Id_{\mathcal{A}},v)$ est monoı̈dalement isomorphe à $(Id_{\mathcal{A}},1)$ via un isomorphisme de foncteurs monoı̈daux se projetant sur $1$ dans $\bar{\mathcal{A}}$.
:::

On peut supposer ${\mathcal{A}}$ strictement monoı̈dale. Il s'agit de résoudre l'équation $$v_{A,B}=(u_A^{-1}\bullet u_B^{-1})u_{A\bullet 
B}$$ pour $A,B\in {\mathcal{A}}$, où $u=(u_A)$ est un automorphisme (non monoı̈dal) de $Id_{\mathcal{A}}$ se projetant sur $1$. On procède comme d'habitude, en supposant de plus ${\mathcal{A}}$ strictement $K$-linéaire et en ne traitant que d'endomorphismes. Il suffit de montrer:

::: lemme
[]{#l18 label="l18"} Il existe une famille double $(u^{(r)})_{r\ge 1}$ d'automorphismes de $Id_{\mathcal{A}}$, avec $u_A^{(r)}\allowbreak\in 1+{\mathcal{R}}(A)$, ayant les propriétés suivantes:

::: thlist
$u_A^{(r+1)}\equiv 
u_A^{(r)}\pmod{{\mathcal{R}}(A)^{r}}$ pour tout $A\in{\mathcal{A}}$ et tout $r\ge 1$.

$v_{A,B}\equiv ({u^{(r)}_A}^{-1}\bullet
{u^{(r)}_B}^{-1})u^{(r)}_{A 
\bullet B}\pmod{{\mathcal{R}}(A\bullet
B)^{r}}$ pour tous objets $A,B$ et tout $r\ge 1$.
:::
:::

Récurrence sur $r$, en partant de $r=1$ avec $u^{(1)}=1$. Supposons $r\ge 1$ et trouvée un automorphisme $u^{(r)}$. Quitte à remplacer $v_{A,B}$ par $(u^{(r)}_A\bullet u^{(r)}_B){u^{(r)}_{A\bullet 
B}}^{-1}v_{A,B}$, on peut supposer que $u^{(r)}=1$ et que $v\in 
{\mathcal{R}}^{r}$.

Pour tout mot $w$ en les objets de ${\mathcal{A}}$, posons

$$\begin{aligned}
C(w)&=\{x\in {\mathcal{A}}(\overset{\bullet}{w})\mid x \text{ centralise 
}
{\mathcal{A}}(w)\}\\
C^{<r>}(w)&=C(w)\cap{\mathcal{R}}(\overset{\bullet}{w})^r\quad (r\ge 
0)\\
\Gamma^{[r]}(w)&=C^{<r>}(w)/C^{<r+1>}(w)\\
\Gamma^{[r]}&=\prod_w 
\Gamma^{[r]}(w).
\end{aligned}$$

L'algèbre $K\langle Ob({\mathcal{A}})\rangle$ opère à gauche et à droite sur $\Gamma^{[r]}$ de la manière habituelle.

Posons $v_{A,B}=1-\nu_{A,B}$: alors $\nu_{A,B}\in 
C^{<r>}(AB)$ et on a la congruence identique $$\nu_{A\bullet 
B,C}+\nu_{A,B}\bullet 1_C\equiv \nu_{A,B\bullet
C}+1_A\bullet 
\nu_{B,C}\pmod{{\mathcal{R}}(A\bullet B\bullet C)^{r+1}}.$$

Soit $u^{(r+1)}$ un automorphisme de $Id_{\mathcal{A}}$ solution de (i) et (ii). Posons $u_A^{(r+1)}\allowbreak=1-\mu_A$: on a donc $\mu_A\in C^{<r>}(A)$. Soit $\bar\mu_A$ l'image de $\mu_A$ dans $\Gamma^{[r]}(A)$. On a la congruence identique $$\nu_{A,B}\equiv \mu_{A\bullet 
B}-1_A\bullet
\mu_B-\mu_A\bullet 1_B\pmod{{\mathcal{R}}(A\bullet 
B)^{r+1}}.$$

Réciproquement, si $(\mu_A)$ est une famille d'éléments de $C^{<r>}(A)$ vérifiant ces congruences, alors la famille $(u_A^{(r+1)}=1-\mu_A)$ définit un automorphisme de $Id_{\mathcal{A}}$ solution de (i) et (ii). Il reste à appliquer comme précédemment la nullité de $H^2(K\langle 
Ob({\mathcal{A}})\rangle, 
\Gamma^{<r>})$.$\square$

::: rem
[]{#duaux droite label="duaux droite"} Si $A, B$ admettent des duaux à droite (*cf.* [\[s3.5\]](#s3.5){reference-type="ref" reference="s3.5"}), les isomorphismes canoniques $${\mathcal{A}}({\bf 1},A^\vee\bullet
B)\cong {\mathcal{A}}(A,B)$$

de [\[eq6.2.1\]](#eq6.2.1){reference-type="eqref" reference="eq6.2.1"} passent à $\bar{\mathcal{A}}$ et sont compatibles à toute section monoı̈dale $s$ comme dans le théorème. Si tous les objets de ${\mathcal{A}}$ admettent des duaux à droite (par exemple si ${\mathcal{A}}$ est symétrique et rigide), on en déduit que $s$ est déterminée par ses valeurs sur les $\bar{\mathcal{A}}({\bf 1}, 
A)$.
:::

# Représentabilité {#repr}

Dans ce paragraphe, nous nous proposons d'interpréter les résultats des paragraphes [\[s5\]](#s5){reference-type="ref" reference="s5"} et [\[s6\]](#s6){reference-type="ref" reference="s6"} en termes plus catégoriques. Brièvement, on peut associer à une petite $K$-catégorie de Wedderburn (monoı̈dale) le groupoı̈de des sections (monoı̈dales) de $\pi_{\mathcal{A}}$. Cette construction est $2$-fonctorielle en ${\mathcal{A}}$ pour les foncteurs pleinement fidèles et les isomorphismes naturels. Sous une hypothèse de finitude supplémentaire, elle peut même s'enrichir en un $2$-foncteur à valeurs dans les *$K$-groupoı̈des affines scindés unipotents* (théorèmes [\[gerbe\]](#gerbe){reference-type="ref" reference="gerbe"} et [\[gerbe\'\]](#gerbe'){reference-type="ref" reference="gerbe'"}).

Ces constructions ne dépendent pas des théorèmes [\[T1\]](#T1){reference-type="ref" reference="T1"} et [\[T2\]](#T2){reference-type="ref" reference="T2"}. Dans le cas représentable, elles permettent de les réinterpréter en des résultats très forts de *rationalité* pour les $K$-groupoı̈des en jeu.

Nous nous plaçons d'abord le cadre discret, puis dans le cadre algébrique.
