---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-010-122-variantes-relatives
section_title: "Variantes relatives"
section_number: 12.2
pages: 63-65
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.894
---
::: prop
[]{#P3 label="P3"} Soit $T:{\mathcal{B}}\to {\mathcal{A}}$ un $K$-foncteur radiciel entre deux petites $K$-catégories de Wedderburn. Notons $\bar {\mathcal{A}}={\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$, $\bar {\mathcal{B}}={\mathcal{B}}/{\operatorname{rad}}({\mathcal{B}})$ et $\bar T:\bar
{\mathcal{B}}\to \bar {\mathcal{A}}$ le foncteur induit. Soit $s_{\mathcal{A}}:\bar{\mathcal{A}}\to {\mathcal{A}}$ (*resp.* $s_{\mathcal{B}}:\bar{\mathcal{B}}\to {\mathcal{B}}$ ) une section de la projection canonique. Alors il existe un système $(u_X)$ d'éléments de $1_{T(X)}+ {\operatorname{rad}}({\mathcal{A}})(T(X),T(X))$ tel que $s_{\mathcal{A}}\bar
T(h)=u_{X'}Ts_{\mathcal{B}}(h)(u_X)^{-1}$ pour tout $h\in \bar {\mathcal{B}}(X,X')$.
:::

1\) Posons ${\mathcal{R}}={\operatorname{rad}}({\mathcal{A}})$. Commençons par le cas où ${\mathcal{R}}^2=0$. On a $Ts_{\mathcal{B}}(h)-s_{\mathcal{A}}\bar T(h)\in {\operatorname{rad}}({\mathcal{A}})$ pour tout $h\in \bar {\mathcal{B}}$. Ceci définit une dérivation de $\bar{\mathcal{B}}$ à valeurs dans le ${\bar{\mathcal{B}}}^e$-module ${\operatorname{rad}}({\mathcal{A}})$ ($1$-cocycle de Hochschild). Cette dérivation est intérieure ($1$-cobord de Hochschild): il existe une famille $n_{X}=u_{X}-1_{T(X)}\in{\mathcal{R}}(T(X), T(X))$ vérifiant, pour tout $h\in \bar 
{\mathcal{B}}(X,X')$, $$Ts_{\mathcal{B}}(h)-s_{\mathcal{A}}\bar T(h) =n_{X'} Ts_{\mathcal{B}}(h) - 
Ts_{\mathcal{B}}(h)n_{X},$$ d'où l'assertion.

2\) Supposons maintenant seulement que ${\mathcal{R}}={\operatorname{rad}}({\mathcal{A}})$ soit nilpotent d'échelon $r+1$, et raisonnons par récurrence sur $r$ (le cas $r=1$ étant acquis). Considérons la composition ${\mathcal{B}}\overset{T}{\to}{\mathcal{A}}\to 
{\mathcal{A}}^{(r)}={\mathcal{A}}/{\mathcal{R}}$. En appliquant l'hypothèse de récurrence au foncteur composé, on trouve un système $(u_X)$ d'éléments de $1_{T(X)}+{\mathcal{R}}(T(X),T(X))$ tel que $$s_{\mathcal{A}}\bar 
T(h)\equiv u_{X'}Ts_{\mathcal{B}}(h)(u_X)^{-1}\pmod{{\mathcal{R}}^{r}}.$$

Quitte à remplacer $s_{\mathcal{A}}$ par la section conjuguée par les $(u_A)^{-1}$, on se ramène au cas où $s_{\mathcal{A}}\bar
T(h)\equiv Ts_{\mathcal{B}}(h)$ modulo ${\mathcal{R}}^{r}$. On peut alors remplacer ${\mathcal{B}}$ par $\bar{\mathcal{B}}$ et ${\mathcal{A}}$ par la catégorie $\tilde {\mathcal{A}}$ introduite au pas $3)$ de la preuve du théorème [\[T1\]](#T1){reference-type="ref" reference="T1"}. Comme le radical de cette dernière est de carré nul, on conclut par le pas précédent.

3\) Dans le cas général, on applique un raisonnement à la Zorn comme au dernier pas de la preuve du théorème [\[T1\]](#T1){reference-type="ref" reference="T1"}: brièvement, il existe une sous-catégorie pleine maximale ${\mathcal{C}}$ de ${\mathcal{B}}$ telle que la proposition vaille pour ${\mathcal{C}}$. On peut alors supposer que ${\mathcal{B}}$ contient un seul objet hors de ${\mathcal{C}}$, et de même que $A$ contient un seul objet hors de $T(Ob({\mathcal{C}}))$. On constate comme ci-dessus que le radical de cette nouvelle catégorie ${\mathcal{A}}$ est alors (globalement) nilpotent. $\square$

Dans le paragraphe suivant, nous appliquerons la proposition [\[P3\]](#P3){reference-type="ref" reference="P3"} dans le cas où ${\mathcal{A}}$ est munie d'une structure monoı̈dale $\bullet$ et où $T$ est le foncteur canonique ${\mathcal{A}}\boxtimes_K {\mathcal{A}}\to {\mathcal{A}}: X=(A, B)\mapsto A\bullet B$, supposé radiciel (ce qui revient à supposer que le radical est un idéal monoı̈dal). Pour $h=f\otimes g,s=s_{\mathcal{A}}$, on a alors

$$s_{\mathcal{A}}\bar
T(h) =s( f\bullet  g),Ts_{\mathcal{B}}(h)=s(f)\bullet s( g) .$$

Le complément de Malcev au théorème de Wedderburn dit qu'on peut choisir un scindage de Wedderburn dont l'image contient une sous-algèbre semi-simple donnée d'une $K$-algèbre de Wedderburn. En voici une variante à plusieurs objets.

::: cor
[]{#cmalcev label="cmalcev"} Sous les hypothèses du théorème [\[T1\]](#T1){reference-type="ref" reference="T1"}, supposons donnée en outre une sous-catégorie ${\mathcal{B}}$ séparable de ${\mathcal{A}}$ (non nécessairement pleine), avec $Ob({\mathcal{B}})=Ob({\mathcal{A}})$. Alors il existe une section $s$ de $\pi_{\mathcal{A}}$ vérifiant $(s\circ \pi_{\mathcal{A}}
)\vert {\mathcal{B}}= id_{{\mathcal{B}}}$.
:::

Partant d'une section de $\pi_{\mathcal{A}}$ (dont l'existence est assurée par le théorème [\[T1\]](#T1){reference-type="ref" reference="T1"}), on la modifie en appliquant la proposition précédente pour obtenir une section fixant ${\mathcal{B}}$. $\square$

# Sections monoı̈dales {#s6}

## Foncteurs monoı̈daux {#9.1}

Soient $({\mathcal{B}},\top)$ et $({\mathcal{A}},\bullet)$ deux catégories monoı̈dales. Rappelons qu'un *foncteur monoı̈dal* est la donnée $(s,(\tilde s_{AB}))$ d'un foncteur $s: {\mathcal{B}}\to {\mathcal{A}}$ et d'isomorphismes fonctoriels $\tilde 
s_{AB}: s(A)\bullet s(B)\allowbreak\to
s(A\top B)$ vérifiant une compatibilité aux contraintes d'associativité et d'unité (on écrit souvent par abus $s$ au lieu de $(s,(\tilde s_{AB}))$ pour abréger). Les foncteurs monoı̈daux se composent, avec la règle $\widetilde{s's}_{AB}=s'(\tilde s_{AB})\circ \tilde 
s'_{s(A)s(B)}$.

Un *morphisme de foncteurs monoı̈daux* est une transformation naturelle des foncteurs sous-jacents, compatible aux données $\tilde s_{AB}, \tilde s'_{AB}$, et aux unités, *cf.* [@saavedra I.4.1.1]. En d'autres termes, un tel morphisme est la donnée pour tout $A\in {\mathcal{B}}$ d'un morphisme $u_A:s(A)\to s'(A)$, naturel en $A$, tel que les diagrammes $$\begin{CD}\label{eq4}
s(A)\bullet 
s(B)@>\tilde s_{A,B}>> s(A\top B)\\
@Vu_A\bullet u_B VV @Vu_{A\top 
B}VV\\
s'(A)\bullet s'(B)@>\tilde s'_{A,B}>> s'(A\top 
B)
\end{CD}$$ soient tous commutatifs, et tel que le morphisme $$\begin{CD}\label{eq4'}
s({{\bf 1}})={{\bf 1}} 
@>u_{{\bf 1}}>> s'({{\bf 1}})={{\bf 1}} \\\end{CD}$$ soit l'identité dans l'anneau commutatif $End({{\bf 1}})$.

Un foncteur monoı̈dal $\pi: {\mathcal{A}}\to {\mathcal{B}}$ étant donné, une *section* de $\pi$ est un foncteur monoı̈dal $s: {\mathcal{B}}\to {\mathcal{A}}$ tel que $\pi\circ 
s=id_{\mathcal{B}}$ (égalité de foncteurs monoı̈daux). Deux sections $s,s'$ sont dites *isomorphes* s'il existe un isomorphisme de foncteurs monoı̈daux $s\Rightarrow s'$ tel que $\pi\circ 
s\Rightarrow \pi \circ s'$ soit le foncteur identique.

Dans une $K$-catégorie monoı̈dale, le bifoncteur $\bullet$ est $K$-bilinéaire. Nous supposerons toujours nos catégories monoı̈dales non nulles (*i.e.* $End({\bf 1}) \neq 
0$).

## Existence et "unicité\" de sections monoı̈dales

Après ces préliminaires, nous pouvons énoncer la version monoı̈dale du théorème de Wedderburn à plusieurs objets. On suppose de nouveau que $K$ est un corps.

::: thm
[]{#T2 label="T2"} Soit $({\mathcal{A}}, \bullet)$ une petite $K$-catégorie de Wedderburn monoı̈dale. Supposons que les $End({{\bf 1}})$-bimodules ${\mathcal{A}}(A,B)$ soient commutatifs, *i.e.* l'action à gauche coı̈ncide avec l'action à droite[^1].\
Supposons que ${\operatorname{rad}}({\mathcal{A}})$ soit monoı̈dal, d'où une structure monoı̈dale sur $\bar
{\mathcal{A}}={\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$. Notons $\pi_{\mathcal{A}}:
{\mathcal{A}}\to 
\bar {\mathcal{A}}$ la projection canonique, vue comme foncteur monoı̈dal. Alors:\
a) Il existe une section monoı̈dale $s$ de $\pi_A$.\
b) Toute autre section monoı̈dale de $\pi_{\mathcal{A}}$ est isomorphe à $s$.
:::

[^1]: Une catégorie monoı̈dale vérifiant cette hypothèse est appelée *catégorie de Penrose* dans [@bru1]. C'est par exemple le cas si $End({{\bf 1}})=K$, ou en présence d'un tressage.
