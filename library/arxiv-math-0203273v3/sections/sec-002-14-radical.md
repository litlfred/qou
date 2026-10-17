---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-002-14-radical
section_title: "Radical"
section_number: 1.4
pages: 13-22
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.919
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
On démontre [@kelly] que $$\begin{gathered}
{\operatorname{rad}}({\mathcal{A}})(A,B)=\\
\{f\in {\mathcal{A}}(A,B)\mid
\text{pour tout}\ g\in
{\mathcal{A}}(B,A), 1_A-gf \text{  est
inversible}\}
\end{gathered}$$ définit un idéal ${\operatorname{rad}}({\mathcal{A}})$ de ${\mathcal{A}}$.

::: defn
[]{#D1 label="D1"} Cet idéal s'appelle le *radical* de ${\mathcal{A}}$.
:::

Si ${\mathcal{A}}$ est une $K$-algèbre, vue comme $K$-catégorie à un seul objet, on retrouve une définition du radical de Jacobson.

::: rem
[]{#gabriel label="gabriel"} Un autre radical a été introduit dans la thèse de Gabriel [@gabriel] (c'est celui qui est évoqué dans [@bru2]): $${\operatorname{rad}}'({\mathcal{A}})(A,B)=
\{f\in {\mathcal{A}}(A,B)\mid
\text{pour tout}\ g\in
{\mathcal{A}}(B,A), gf \text{  est
nilpotent}\}.$$

On pourrait donc parler de radical de Gabriel et de radical de Kelly (le dernier étant une version catégorique du radical de Jacobson...) On a évidemment ${\operatorname{rad}}'({\mathcal{A}})\subset {\operatorname{rad}}({\mathcal{A}})$, avec égalité si et seulement si, pour tout $A\in {\mathcal{A}}$, ${\operatorname{rad}}({\mathcal{A}})(A,A)$ est un nilidéal.
:::

La caractérisation suivante de ${\operatorname{rad}}'$ est parfois utile:

::: lemme
[]{#rad' label="rad'"} Soit $H:{\mathcal{A}}\to Projf_L$ un foncteur $K$-linéaire de ${\mathcal{A}}$ vers la catégorie des $L$-modules projectifs de type fini, où $L$ est une $K$-algèbre. Alors, pour $(A,B)\in {\mathcal{A}}\times{\mathcal{A}}$, on a $${\operatorname{rad}}'{\mathcal{A}}(A,B)\subset \{f\in {\mathcal{A}}(A,B)\mid \forall g\in {\mathcal{A}}(B,A), tr 
H(gf)=0\},$$ avec égalité si $H$ est fidèle et $L$ est de caractéristique $0$.
:::

L'inclusion $\subset$ est claire, puisque la trace d'un endomorphisme nilpotent est nulle. Pour l'inclusion opposée, soit $f$ un élément du second membre. Alors, pour tout $g\in {\mathcal{A}}(B,A)$ et tout $n\ge 1$, on a $$tr H(gf)^n= tr H((gf)^n) = tr((gf)^{n-1}gf) =0.$$

Comme $L$ est de caractéristique $0$, cela implique que $H(gf)$ est nilpotent, donc également $gf$ par fidélité.$\square$

::: prop
[]{#P1 label="P1"} $a)$ Le radical est le plus grand idéal ${\operatorname{rad}}({\mathcal{A}})$ tel que ${\operatorname{rad}}({\mathcal{A}})(A,A)$ soit contenu (*resp.* coı̈ncide) avec le radical de Jacobson de ${\mathcal{A}}(A,A)$ pour tout objet $A$.\
$b)$ C'est aussi le plus grand idéal de ${\mathcal{A}}$ tel que le foncteur quotient ${\mathcal{A}}\to {\mathcal{A}}
/ {\operatorname{rad}}({\mathcal{A}})$ soit conservatif, i.e. reflète les isomorphismes. Ce foncteur reflète aussi rétractions et corétractions[^1].
:::

Voir [@kelly th. 1], [@mitchell §4], [@street prop. 6]. On voit tout de suite que la notion de radical est auto-duale.

::: cor
[]{#corresp1 label="corresp1"} Les radicaux des catégories ${\mathcal{A}},{\mathcal{A}}^\oplus,{\mathcal{A}}^\natural$ et ${\mathcal{A}}^{\oplus\natural}$ se correspondent par les bijections du lemme [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} b).
:::

Cela découle du point a) de la proposition [\[P1\]](#P1){reference-type="ref" reference="P1"}.$\square$

::: defn
[]{#D2 label="D2"} Soit $T:{\mathcal{A}}\to {\mathcal{B}}$ un $K$-foncteur entre deux $K$-catégories. Alors $T$ est dit *radiciel* si $T({\operatorname{rad}}({\mathcal{A}}))\subset
{\operatorname{rad}}({\mathcal{B}})$.
:::

::: lemme
[]{#L1 label="L1"} Si $T$ est plein, il est radiciel. D'autre part, si $T$ est conservatif, on a $T^{-1}({\operatorname{rad}}({\mathcal{B}}))\subset {\operatorname{rad}}({\mathcal{A}})$.\
Si $T$ est radiciel et conservatif, on a $T^{-1}({\operatorname{rad}}({\mathcal{B}}))={\operatorname{rad}}({\mathcal{A}})$. Si $T$ est même plein, $T({\operatorname{rad}}({\mathcal{A}}))$ est égal à la restriction de ${\operatorname{rad}}({\mathcal{B}})$ à $T({\mathcal{A}})$.
:::

Le premier point découle immédiatement du point $a)$ de la proposition [\[P1\]](#P1){reference-type="ref" reference="P1"}. Prouvons le second: soit $f\in
{\mathcal{A}}(A,B)$ tel que $T(f)\in {\operatorname{rad}}({\mathcal{B}})(T(A),T(B))$. Alors pour tout $g\in
{\mathcal{A}}(B,A)$, $1_{T(A)}-T(g)\circ T(f)$ est inversible. Donc $1_A-g\circ
f$ est inversible puisque $T$ est conservatif. Prouvons la dernière assertion: $T$ radiciel $\Longrightarrow$ ${\mathcal{A}}\subset T^{-1}T({\operatorname{rad}}({\mathcal{A}}))\subset T^{-1}({\operatorname{rad}}({\mathcal{B}}))$, et $T$ conservatif $\Longrightarrow$ $T^{-1}({\operatorname{rad}}({\mathcal{B}}))\subset {\operatorname{rad}}({\mathcal{A}})$, d'où $T^{-1}({\operatorname{rad}}({\mathcal{B}}))=
{\operatorname{rad}}({\mathcal{A}})$. Si $T$ est plein, la dernière assertion en découle.$\square$

::: meg
[]{#meg1 label="meg1"} a) Si $T$ est conservatif, l'inclusion $T^{-1}({\operatorname{rad}}({\mathcal{B}}))\subset {\operatorname{rad}}({\mathcal{A}})$ devient fausse en général si l'on remplace les radicaux par leurs puissances $n$-ièmes, $n>1$ (même si $T$ est pleinement fidèle).\
b) Il découle du premier point du lemme que pour tout idéal ${\mathcal{I}}$ de ${\mathcal{A}}$, ${\operatorname{rad}}({\mathcal{A}}/{\mathcal{I}})\,$ contient l'image de $\,{\operatorname{rad}}({\mathcal{A}})$ dans ${\mathcal{A}}/{\mathcal{I}}$ (la projection $T:{\mathcal{A}}\to {\mathcal{A}}/{\mathcal{I}}$ est un foncteur plein); mais il en est en général distinct si ${\mathcal{I}}\not\subset {\operatorname{rad}}({\mathcal{A}})$ (exemple: $\mathbf{Z}\to
\mathbf{Z}/4\mathbf{Z}$).
:::

::: lemme
[]{#L2 label="L2"} Soit ${\mathcal{A}}$ une $K$-catégorie, et soit $S$ un objet de ${\mathcal{A}}$ tel que ${\mathcal{A}}(S,S)$ soit un corps (par exemple un objet simple dans un catégorie abélienne). Soit $A$ un objet quelconque de ${\mathcal{A}}$. Alors tout morphisme $f \in {\mathcal{A}}(S,A)$ qui n'est pas dans le radical est une corétraction, et tout morphisme $g\in {\mathcal{A}}(A,S)$ qui n'est pas dans le radical est une rétraction. Si en outre ${\mathcal{A}}(S,S)\allowbreak=K$, alors $${\operatorname{rad}}({{\mathcal{A}}})(S,A)= \{f \in {\mathcal{A}}(S,A 
),
\forall g\in
{\mathcal{A}}(A ,S),
         g\circ f =0\} .$$
:::

Par définition du radical, il existe $h \in 
{\mathcal{A}}(A,S)$ tel que $1_S
- hf$ ne soit pas inversible dans ${\mathcal{A}}(S,S)$. Comme ${\mathcal{A}}(S,S)$ est un corps, ceci entraı̂ne que $1_S = hf$. Pour $g$ on raisonne dualement.

Prouvons la dernière assertion. Tout $f \in {\mathcal{A}}(S,A )$ tel que $g\circ f =0$ pour tout $g\in
{\mathcal{A}}(A 
,S)$ n'est pas une corétraction, donc appartient au radical. Réciproquement, si $f\in
{\operatorname{rad}}({{\mathcal{A}}})(S,A)$, alors, par définition, l'élément $1-g\circ f$ de $K$ est inversible, c'est-à-dire non nul, pour tout $g \in {\mathcal{A}}(A ,S)$ par définition. Comme $g$ peut être multiplié par toute constante de $K$, ceci entraı̂ne $g\circ f=0$. $\square$

# catégories de Wedderburn {#s2}

Dans ce paragraphe, on suppose que *$K$ est un corps.*

## Catégories semi-simples

::: defn
[]{#D3 label="D3"} Une $K$-catégorie est dite *semi-simple* si tout ${\mathcal{A}}$-module à gauche est semi-simple.
:::

Cette notion est manifestement Morita-invariante. En particulier, elle est stable par passage à ${\mathcal{A}}^{\oplus},{\mathcal{A}}^{\natural},{\mathcal{A}}^{\oplus\natural}$. Elle a été étudiée dans [@leduc], [@mitchell § 4] et [@street][^2]. Pour la commodité du lecteur, nous avons donné en appendice un exposé des nombreuses caractérisations des catégories semi-simples, et quelques contre-exemples. Nous en extrayons la proposition suivante:

::: prop
[]{#P4/3 label="P4/3"} Soit ${\mathcal{A}}$ une (petite) catégorie $K$-linéaire. Les conditions suivantes sont équivalentes:\
a) $\;{\mathcal{A}}$ est semi-simple,\
b) $\;{\operatorname{rad}}({\mathcal{A}})=0$ et pour tout $A\in {\mathcal{A}}$, ${\mathcal{A}}(A,A)$ est un anneau artinien,\
c) pour tout objet $A$, ${\mathcal{A}}(A,A)$ est une $K$-algèbre semi-simple[^3].\
Sous ces conditions, ${\mathcal{A}}$ est abélienne si et seulement si elle est pseudo-abélienne.
:::

En particulier, la notion de semi-simplicité est *auto-duale*, et *stable par quotient par tout idéal*. Voir [@mitchell §4] ou l'appendice de ce travail.

En particulier, si ${\mathcal{A}}$ est semi-simple (non nécessairement $K$-linéaire ni pseudo-abélienne), on a $\operatorname{Ext}^i_{\mathcal{A}}(M,N)=0$ pour tout couple $(M,N)$ de ${\mathcal{A}}$-modules et tout $i>0$.

::: lemme
[]{#l2.1 label="l2.1"} Toute sous-catégorie pleine ${\mathcal{B}}$ d'une $K$-catégorie semi-simple ${\mathcal{A}}$ est semi-simple. De plus, si ${\mathcal{A}}$ et ${\mathcal{B}}$ sont $K$-linéaires pseudo-abéliennes, il existe une unique sous-catégorie pleine ${\mathcal{C}}$ de ${\mathcal{A}}$ telle que ${\mathcal{A}}={\mathcal{B}}\coprod {\mathcal{C}}$ (*cf.* définition [\[A.D7\]](#A.D7){reference-type="ref" reference="A.D7"} c)).
:::

Par invariance de Morita, on se ramène immédiatement au cas où ${\mathcal{A}}$ et ${\mathcal{B}}$ sont $K$-linéaires pseudo-abéliennes. La première assertion résulte alors de la caractérisation c) de la proposition [\[P4/3\]](#P4/3){reference-type="ref" reference="P4/3"}. Pour voir la deuxième, notons $S({\mathcal{A}})$ (*resp.* $S({\mathcal{B}})$) l'ensemble des classes d'isomorphismes (types) d'objets simples de ${\mathcal{A}}$ (*resp.* de ${\mathcal{B}}$). Il est clair que les objets de ${\mathcal{B}}$ sont les sommes directes d'objets simples de type appartenant à ${\mathcal{B}}$. La catégorie ${\mathcal{C}}$ est alors la catégorie des sommes directes d'objets simples de ${\mathcal{A}}$ de type appartenant à $S({\mathcal{A}})-S({\mathcal{B}})$.$\square$

::: meg
Dans le lemme [\[l2.1\]](#l2.1){reference-type="ref" reference="l2.1"}, si ${\mathcal{A}}$ est monoı̈dale et si ${\mathcal{B}}$ est une sous-catégorie monoı̈dale de ${\mathcal{A}}$, il n'est pas vrai en général que ${\mathcal{C}}$ soit monoı̈dale.
:::

Le lemme suivant est à mettre en regard de [\[meg1\]](#meg1){reference-type="ref" reference="meg1"}b.

::: lemme
[]{#NewL1 label="NewL1"} Soit ${\mathcal{A}}$ une $K$-catégorie telle que ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ soit semi-simple. Pour tout idéal ${\mathcal{I}}$, le radical de ${\mathcal{A}}/{\mathcal{I}}$ est l'image de ${\operatorname{rad}}({\mathcal{A}})$ dans ${\mathcal{A}}/{\mathcal{I}}$.
:::

Le point est l'inclusion ${\operatorname{rad}}({\mathcal{A}}/{\mathcal{I}})\subset {\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})+{\mathcal{I}}$. Il découle de ce que le foncteur de projection ${\mathcal{A}}/{\mathcal{I}}\to {\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})+{\mathcal{I}}$ est plein, donc radiciel, et de ce que le radical de ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})+{\mathcal{I}}$ est nul puisque c'est une catégorie semi-simple (comme quotient de ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$). $\square$

Voici enfin deux compléments au lemme [\[l2.1\]](#l2.1){reference-type="ref" reference="l2.1"}, qui montrent que la structure des catégories semi-simples est "triviale\":

::: prop
Soit ${\mathcal{A}}$ une petite catégorie abélienne semi-simple, où $K$ est un corps commutatif. Notons $S({\mathcal{A}})$ (resp $\mathbb{I}({\mathcal{A}})$, $C({\mathcal{A}})$) l'ensemble des classes d'isomorphismes d'objets simples de ${\mathcal{A}}$ (resp. l'ensemble des idéaux de ${\mathcal{A}}$, l'ensemble des sous-catégories strictement épaisses de ${\mathcal{A}}$, c'est-à-dire strictement pleines et stables par somme directe et facteur direct). Considérons les applications suivantes:

-   $SC:C({\mathcal{A}})\to S({\mathcal{A}})$: ${\mathcal{B}}\mapsto S({\mathcal{B}})$.

-   $CS:S({\mathcal{A}})\to C({\mathcal{A}})$: $X\mapsto\{\bigoplus S_i\mid S_i\in X\}$.

-   $IC:C({\mathcal{A}})\to \mathbb{I}({\mathcal{A}})$: ${\mathcal{B}}\mapsto {\mathcal{I}}_{\mathcal{B}}$ (*cf.* exemple [\[ex1.3.1\]](#ex1.3.1){reference-type="ref" reference="ex1.3.1"}).

-   $SI: \mathbb{I}({\mathcal{A}})\to S({\mathcal{A}})$: ${\mathcal{I}}\mapsto \{S\in S({\mathcal{A}})\mid 1_S\in {\mathcal{I}}\}$.

Alors $SC,CS,IC$ et $SI$ sont bijectives, $SC$ et $CS$ sont inverses l'une de l'autre, $SI\circ IC = SC$ et $CS\circ SI = IC^{-1}$.
:::

Le fait que $SC\circ CS =Id$ est évident. Si ${\mathcal{B}}\in C({\mathcal{A}})$, on a $CS\circ SC({\mathcal{B}})\subset {\mathcal{B}}$ parce que ${\mathcal{B}}$ est $K$-linéaire, avec égalité parce que ${\mathcal{B}}$ est pseudo-abélienne. De plus, $SI\circ 
IC({\mathcal{B}})=\{S\mid 1_S \text{ se factorise \`a travers un objet de } {\mathcal{B}}\}$ contient clairement $S({\mathcal{B}})$. Réciproquement, pour un $S\in SI\circ 
IC({\mathcal{B}})$, il existe $a:S\to X$ et $b:X\to S$ tels que $ba=1_S$. Soit $S'=a(S)$: restreignant $b$ à $S'$, on se ramène au cas où $X$ est simple. Ceci montre que $S\in S({\mathcal{B}})$ puisque ${\mathcal{B}}$ est strictement pleine.

Il reste à montrer que $IC\circ CS\circ SI = Id$. Pour ${\mathcal{I}}\in\mathbb{I}$, $IC\circ CS\circ SI({\mathcal{I}})$ est l'idéal des morphismes qui se factorisent à travers un objet de la forme $\bigoplus S_i$, où les $S_i$ sont simples et tels que $1_{S_i}\in{\mathcal{I}}$ pour tout $i$. Cet idéal est évidemment contenu dans ${\mathcal{I}}$. Réciproquement, soit $f\in{\mathcal{I}}$: écrivons $f$ comme somme directe d'un morphisme nul et d'un isomorphisme $u$ (lemme [\[lA.3\]](#lA.3){reference-type="ref" reference="lA.3"}). Alors $u\in{\mathcal{I}}$. Si $S$ est un facteur simple de la source de $u$, $1_S$ se factorise à travers $u$, donc $1_S\in{\mathcal{I}}$. $\square$

::: prop
Soit ${\mathcal{I}}$ un idéal de ${\mathcal{A}}$. Alors:

1.  Le foncteur de projection $\pi:{\mathcal{A}}\to {\mathcal{A}}/{\mathcal{I}}$ est essentiellement surjectif (i.e. ${\mathcal{A}}/{\mathcal{I}}$ est pseudo-abélienne).

2.  $\pi$ a une section $i$, qui en est un adjoint à gauche et à droite.

3.  Posons ${\mathcal{B}}=CS\circ SI({\mathcal{I}})$. Alors on a ${\mathcal{A}}={\mathcal{B}}\coprod i({\mathcal{A}}/{\mathcal{I}})$.

4.  La suite $$0\to K_0({\mathcal{B}})\to K_0({\mathcal{A}})\to K_0({\mathcal{A}}/{\mathcal{I}})\to 0$$ est exacte scindée.
:::

Pour tout $A\in {\mathcal{A}}$, ${\mathcal{I}}(A,A)$ est un idéal bilatère de la $K$-algèbre semi-simple ${\mathcal{A}}(A,A)$; l'homomorphisme d'anneaux ${\mathcal{A}}(A,A)\to 
{\mathcal{A}}(A,A)/{\mathcal{I}}(A,A)={\mathcal{A}}/{\mathcal{I}}(\pi(A),\pi(A))$ a donc une unique section $s_A$. En particulier, tout idempotent de ${\mathcal{A}}/{\mathcal{I}}(\pi(A),\pi(A))$ se relève dans ${\mathcal{A}}(A,A)$, ce qui prouve 1). De même, on construit 2) à l'aide des $s_A$; ses propriétés sont immédiates. 3) en résulte grâce à la proposition précédente, et 4) résulte de 3).$\square$

## Catégories séparables

::: prop
[]{#Psep label="Psep"} Soit $A$ une $K$-algèbre (associative unitaire). Les conditions suivantes sont équivalentes:

1.  []{#Psep1 label="Psep1"} $A$ est un $A$-bimodule projectif.

2.  []{#Psep2 label="Psep2"} Toute dérivation de $A$ vers un bimodule est intérieure.

3.  []{#Psep3 label="Psep3"} $A$ est de dimension finie sur $K$, est semi-simple, et le reste après toute extension des scalaires.

4.  []{#Psep4 label="Psep4"} $A$ est semi-simple, et le reste après toute extension des scalaires.

5.  []{#Psep5 label="Psep5"} $A$ est de dimension finie sur $K$, sans radical, et le reste après toute extension des scalaires.

6.  []{#Psep6 label="Psep6"} L'algèbre $A^{\rm o}\otimes_K A$ est semi-simple.
:::

Pour [\[Psep1\]](#Psep1){reference-type="ref" reference="Psep1"} $\iff$ [\[Psep2\]](#Psep2){reference-type="ref" reference="Psep2"}, voir [@cq 4]. Pour [\[Psep1\]](#Psep1){reference-type="ref" reference="Psep1"} $\iff$ [\[Psep3\]](#Psep3){reference-type="ref" reference="Psep3"} $\iff$ [\[Psep4\]](#Psep4){reference-type="ref" reference="Psep4"}, on renvoie à [@ce ch. IX, th. 7.10]. Pour [\[Psep4\]](#Psep4){reference-type="ref" reference="Psep4"} $\iff$ [\[Psep5\]](#Psep5){reference-type="ref" reference="Psep5"}, voir [@alg 7.5, cor.]. Pour [\[Psep1\]](#Psep1){reference-type="ref" reference="Psep1"} $\iff$ [\[Psep6\]](#Psep6){reference-type="ref" reference="Psep6"}, voir [@ce ch. IX, th. 7.9].

En particulier, l'hypothèse de finitude dans [@ce ch. IX, th. 7.10] n'est pas nécessaire. Pour la commodité du lecteur, nous reproduisons l'argument de [@cq 4] qui montre que [\[Psep1\]](#Psep1){reference-type="ref" reference="Psep1"} $\Longrightarrow$ $\dim_K A<\infty$. Soit $s$ une section de l'application de multiplication $A\otimes_K 
A\to A$, comme homomorphisme de $A$-bimodules. Écrivons $s(1)=\sum_1^n x_i\otimes y_i$, avec $n$ minimal; en particulier, les $y_i$ sont linéairement indépendants sur $K$, donc séparés par les formes $K$-linéaires sur $A$. Notons $I$ le $K$-espace de dimension finie $\sum_1^n Kx_i \subset A$. Alors $I$ est un idéal à gauche de $A$: en effet, pour tout $a\in A$, on a $as(1)=s(1)a$, d'où $\sum ax_ia^\ast(y_i)=\sum x_ia^\ast(y_ia)$ pour tout $a^\ast 
\in Hom_K(A,K)$, et le résultat. En outre, l'action de $A$ par multiplication à gauche sur $I$ est fidèle du fait que $\sum x_i 
y_i= 1$. Par conséquent, $A$ s'injecte dans $End_K(I)$. $\square$

::: defn
[]{#D4sep label="D4sep"} Une $K$-algèbre $A$ est dite *séparable* (ou *absolument semi-simple*) si elle vérifie les conditions de la proposition [\[Psep\]](#Psep){reference-type="ref" reference="Psep"}.
:::

::: rem
Nous nous écartons ici légèrement de la terminologie de Bourbaki [@alg 7.5], pour qui une algèbre est séparable si elle est sans radical et le reste après toute extension des scalaires. Dans le cas commutatif, on dit d'ailleurs plutôt *étale* que séparable.
:::

::: lemme
[]{#l2.2 label="l2.2"} Toute algèbre de dimension finie sans radical sur un corps parfait $K$ est séparable.
:::

Voir [@alg 7.5,7.6]. $\square$

::: lemme
[]{#l2.3 label="l2.3"} Le produit tensoriel de deux $K$-algèbres séparables est séparable.
:::

Voir [@ce ch. IX, prop. 7.4].$\square$

::: defn
[]{#D4sep1 label="D4sep1"} Une catégorie $K$-linéaire ${\mathcal{A}}$ est dite *séparable* (ou *absolument semi-simple*) si la catégorie ${\mathcal{A}}_L$ qui s'en déduit[^4] en tensorisant les morphismes par $L$ est semi-simple pour toute extension $L/K$.
:::

La notion de catégorie séparable est Morita-invariante (*cf.* proposition [\[P4/3\]](#P4/3){reference-type="ref" reference="P4/3"}), auto-duale, et stable par passage au quotient par un idéal.

D'après le théorème [\[tsep\]](#tsep){reference-type="ref" reference="tsep"}, on en a les autres caractérisations suivantes:

-   (si ${\mathcal{A}}$ est $K$-linéaire) Pour tout objet $A\in
    {\mathcal{A}}$, ${\mathcal{A}}(A,A)$ est une $K$-algèbre séparable.

-   La catégorie enveloppante[^5] ${\mathcal{A}}^e={\mathcal{A}}^{\rm o}\boxtimes_K{\mathcal{A}}$ est semi-simple.

::: prop
[]{#p2.1 label="p2.1"} Si $K$ est parfait, une $K$-catégorie ${\mathcal{A}}$ est séparable si et seulement si elle est semi-simple et $\dim_K
{\mathcal{A}}(A,B)<\infty$ pour tout couple d'objets $(A,B)$.
:::

Cela résulte du lemme [\[l2.2\]](#l2.2){reference-type="ref" reference="l2.2"}.$\square$

## Catégories semi-primaires

::: defn
[]{#D4 label="D4"} Une $K$-catégorie ${\mathcal{A}}$ est *semi-primaire* si

::: thlist
pour tout objet $A\in {\mathcal{A}}$, le radical ${\operatorname{rad}}({\mathcal{A}}(A,A))$ est nilpotent;

${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est semi-simple.
:::
:::

::: rems
[]{#R1 label="R1"} 

-   Dans le cas d'une catégorie à un seul objet, on retrouve une notion connue en algèbre non commutative sous le nom d'"anneau semi-primaire\" [@rowen] [^6]. Ainsi une catégorie $K$-linéaire est semi-primaire si et seulement si tous ses anneaux d'endomorphismes sont semi-primaires.

-   Cette notion est auto-duale.

-   Une catégorie $K$-linéaire pseudo-abélienne semi-primaire n'est pas nécessairement abélienne (exemple: la catégorie des modules projectifs de type fini sur une $K$-algèbre artinienne non semi-simple).

-   La condition (i) entraı̂ne que les radicaux de Kelly et de Gabriel coı̈ncident.
:::

L'un des aspects classiques des anneaux semi-primaires est la propriété de relèvement des idempotents modulo le radical, qui suit du lemme classique suivant

::: lemme
[]{#idemp label="idemp"} Soit $N$ un nil-idéal d'un anneau $A$. Alors tout idempotent de $A/N$ se relève en un idempotent de $A$. $\square$
:::

::: prop
[]{#P3/2 label="P3/2"} a) Si ${\mathcal{A}}$ est semi-primaire, il en est de même de ${\mathcal{A}}/{\mathcal{I}}$ pour tout idéal ${\mathcal{I}}$, et le radical de ${\mathcal{A}}/{\mathcal{I}}$ est l'image du radical de ${\mathcal{A}}$.\
b) Supposons ${\mathcal{A}}$ semi-primaire. Alors ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est pseudo-abélienne si et seulement si ${\mathcal{A}}$ l'est (et même abélienne si ${\mathcal{A}}$ est $K$-linéaire).\
Plus généralement, le foncteur canonique (*cf.* lemme [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} d)) ${\mathcal{A}}^\natural/{\operatorname{rad}}({\mathcal{A}}^\natural)\allowbreak\to
({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^\natural$ est un isomorphisme.\
c) La notion de $K$-catégorie semi-primaire est Morita-invariante. En particulier, si ${\mathcal{A}}$ est semi-primaire, alors ${\mathcal{A}}^{\oplus},{\mathcal{A}}^{\natural},{\mathcal{A}}^{\oplus\natural}$ le sont (et réciproquement).\
d) Si ${\mathcal{A}}$ est $K$-linéaire et si ${\mathcal{A}}(A,A)$ est un anneau artinien pour tout $A\in {\mathcal{A}}$, alors ${\mathcal{A}}$ est semi-primaire.\
e) Si ${\mathcal{A}}$ est semi-primaire, ${\mathcal{B}}$ est semi-simple et $T:{\mathcal{A}}\to{\mathcal{B}}$ est un $K$-foncteur plein, alors il existe une unique factorisation de $T$ en un $K$-foncteur plein $\bar T:{\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})\to {\mathcal{B}}.$\
f) Si ${\mathcal{A}}$ est semi-primaire et pseudo-abélienne, et $T:{\mathcal{A}}\to{\mathcal{B}}$ est un $K$-foncteur radiciel qui n'envoie aucun objet non nul de ${\mathcal{A}}$ sur l'objet nul de ${\mathcal{B}}$, alors $T$ est conservatif.
:::

a\) Cela résulte aisément du lemme [\[NewL1\]](#NewL1){reference-type="ref" reference="NewL1"}.

b\) suit des lemmes [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} d) et [\[idemp\]](#idemp){reference-type="ref" reference="idemp"} (et du fait qu'une catégorie $K$-linéaire pseudo-abélienne semi-simple est abélienne, *cf.* [\[A.P4\]](#A.P4){reference-type="ref" reference="A.P4"}).

c\) Pour l'invariance par équivalence de Morita, il s'agit d'après le corollaire [\[morita\]](#morita){reference-type="ref" reference="morita"} de voir que ${\mathcal{A}}$ est semi-primaire si et seulement si ${\mathcal{A}}^{\oplus\natural}$ l'est. D'après le corollaire [\[corresp1\]](#corresp1){reference-type="ref" reference="corresp1"}, la trace sur ${\mathcal{A}}$ du radical de ${\mathcal{A}}^{\oplus\natural}$ est le radical de ${\mathcal{A}}$. Il suit de ceci, du lemme [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} d) et du lemme [\[l2.1\]](#l2.1){reference-type="ref" reference="l2.1"} que ${\mathcal{A}}$ est semi-primaire si ${\mathcal{A}}^{\oplus\natural}$ l'est.

Supposons réciproquement ${\mathcal{A}}$ semi-primaire. Le point b) entraı̂ne que ${\mathcal{A}}^{\natural}$ l'est. On peut donc supposer ${\mathcal{A}}$ pseudo-abélienne. En vertu du lemme [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} c), il suffit de voir que si les radicaux de ${\mathcal{A}}^\oplus(A,A)$ et ${\mathcal{A}}^\oplus(B,B)$ sont nilpotents, il en est de même du radical de ${\mathcal{A}}^\oplus(A\oplus B,A\oplus B)$.

Supposons donc que ${\mathcal{R}}(A,A)^m={\mathcal{R}}(B,B)^n=0$, et montrons qu'alors ${\mathcal{R}}(A\oplus 
B,A\oplus B)^{m+n+2}=0$. Par additivité, on se ramène à supposer que le composé de toute chaı̂ne de $N\ge 2n+2$ morphismes $f_i\; (i=1,\dots, N)$ composables appartenant à ${\mathcal{R}}(A,A),{\mathcal{R}}(A,B),{\mathcal{R}}(B,A)$ ou ${\mathcal{R}}(B,B)$ est nul.

Considérons par exemple une chaı̂ne partant de $A$ et aboutissant en $A$. La composition correspondante appartient à un produit de la forme $$\begin{gathered}
{\mathcal{R}}(A,A)^{m_{k+1}}{\mathcal{R}}(B,A){\mathcal{R}}(B,B)^{n_k}{\mathcal{R}}(A, 
B){\mathcal{R}}(A,A)^{m_{k}}\cdots\\
\cdots{\mathcal{R}}(A,A)^{m_2}{\mathcal{R}}(B,A){\mathcal{R}}(B,B)^{n_1}\ 
sR(A,B){\mathcal{R}}(A,A)^{m_1}
\end{gathered}$$ avec $m_1+\dots+m_{k+1}+n_1+\dots+n_k+2k+1=N$. Ce produit est contenu dans ${\mathcal{R}}(A,A)^a$, avec $a=m_1+\dots+m_{k+1}+k$. D'autre part, le produit intermédiaire $${\mathcal{R}}(B,B)^{n_k}{\mathcal{R}}(A,B){\mathcal{R}}(A,A)^{m_{k}}
\cdots{\mathcal{R}}(A,A)^{m_2}{\mathcal{R}}(B,A){\mathcal{R}}
(B,B)^{n_1}$$ est contenu dans ${\mathcal{R}}(B,B)^b$, avec $b=n_1+\dots+n_k+k-1$. On a donc $a\ge m$ ou $b\ge n$ et le morphisme composé est nul. Les autres cas se traitent de la même manière.

d\) Un raisonnement analogue à celui fait dans le cas des anneaux montre que, pour toute ${\mathcal{A}}$, le radical de ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est réduit à $0$. En particulier, pour tout objet $A$ de ${\mathcal{A}}$, la $K$-algèbre $({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))(A,A)$ est semi-simple. Comme ${\mathcal{A}}$ est supposée $K$-linéaire, on conclut par la proposition [\[P4/3\]](#P4/3){reference-type="ref" reference="P4/3"} que ${\mathcal{A}}$ est semi-simple.

e\) suit de la première assertion du lemme [\[L1\]](#L1){reference-type="ref" reference="L1"}.

f\) Le $K$-foncteur radiciel $T$ induit un $K$-foncteur $$\bar T: ({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^\oplus\to 
({\mathcal{B}}/{\operatorname{rad}}({\mathcal{B}}))^\oplus .$$

Tout comme $T$, $\bar T$ n'envoie aucun objet non nul de $({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^\oplus$ sur l'objet nul de $({\mathcal{B}}/{\operatorname{rad}}({\mathcal{B}}))^\oplus$. D'autre part, $({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^\oplus$ est abélienne semi-simple puisque ${\mathcal{A}}$ est semi-primaire pseudo-abélienne (utiliser le point b) ci-dessus). Il en découle que $\bar T$ est conservatif (lemme [\[utile\]](#utile){reference-type="ref" reference="utile"}), et il en est de même de $T$ par [\[P1\]](#P1){reference-type="ref" reference="P1"} b. $\square$

::: prop
[]{#ablfspr label="ablfspr"} Soit ${\mathcal{A}}$ une catégorie abélienne dont tout objet est de longueur finie. Alors ${\mathcal{A}}$ est semi-primaire.
:::

Le plus court est d'envoyer ${\mathcal{A}}$ par un foncteur pleinement fidèle dans une catégorie de modules (théorème de plongement de Freyd-Mitchell). Dans le cas d'une catégorie de modules, l'assertion revient à ceci: l'anneau d'endomorphismes de tout module $M$ de longueur finie est semi-primaire. Ce résultat, qui repose sur le lemme de Fitting, est bien connu, *cf.* [@rowen 2.9.10] (la longueur du module est une borne pour l'échelon de nilpotence du radical).$\square$

## Catégories de Wedderburn {#catégories-de-wedderburn}

::: defn
[]{#D4wed label="D4wed"} Une $K$-catégorie ${\mathcal{A}}$ est dite de *Wedderburn* si

::: thlist
pour tout objet $A\in {\mathcal{A}}$, le radical ${\operatorname{rad}}({\mathcal{A}}(A,A))$ est nilpotent;

${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est une $K$-catégorie séparable.
:::
:::

::: meg
Il est clair qu'une $K$-catégorie de Wedderburn est semi-primaire. Nous verrons en [\[C3.1.\]](#C3.1.){reference-type="ref" reference="C3.1."} qu'elle le reste après toute extension des scalaires. La réciproque est évidemment *fausse* au moins quand $K$ est imparfait, comme le montre l'exemple de la $K$-catégorie à un seul objet donné par une extension finie inséparable de $K$.
:::

::: rem
[]{#R1wed label="R1wed"} Dans le cas d'un seul objet, les algèbres correspondantes sont celles auxquelles s'appliquent le théorème de scindage de Wedderburn dont il sera question au §[\[s5\]](#s5){reference-type="ref" reference="s5"}, d'où la terminologie. Nous les appellerons *algèbres de Wedderburn*.
:::

::: prop
[]{#Pwed label="Pwed"} a) La notion de $K$-catégorie de Wedderburn est stable par passage au quotient par un idéal.\
b) La notion de $K$-catégorie de Wedderburn est Morita-invariante. En particulier, si ${\mathcal{A}}$ est de Wedderburn, alors ${\mathcal{A}}^{\oplus},{\mathcal{A}}^{\natural},{\mathcal{A}}^{\oplus\natural}$ le sont (et réciproquement).\
c) Si $K$ est parfait et si ${\mathcal{A}}(A,B)$ est de dimension finie sur $K$ pour tout couple $(A,B)\in Ob({\mathcal{A}})$, alors ${\mathcal{A}}$ est de Wedderburn. En particulier, toute catégorie tannakienne sur $K$ est de Wedderburn.
:::

a\) découle de [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"} a): si ${\mathcal{A}}$ est de Wedderburn, ${\mathcal{A}}/{\mathcal{I}}$ est semi-primaire, et le quotient par son radical (qui n'est autre que l'image du radical de ${\mathcal{A}}\,$) est séparable, en tant que quotient de ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$.

b\) On sait déjà que ${\mathcal{A}}^{\oplus},{\mathcal{A}}^{\natural},{\mathcal{A}}^{\oplus\natural}$ sont semi-primaires. Il est alors facile de conclure, compte-tenu de ce que, par le lemme [\[corresp\]](#corresp){reference-type="ref" reference="corresp"} et la proposition [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"} b), le quotient de ${\mathcal{A}}^{\oplus\natural}$ par son radical est isomorphe à $({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^{\oplus\natural}$.

c\) Il revient au même de dire que toute algèbre d'endomorphismes de ${\mathcal{A}}^\oplus$ est de dimension finie. D'après le point d) de la proposition [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"}, on voit que ${\mathcal{A}}^\oplus$, donc ${\mathcal{A}}$, est semi-primaire. On conclut par le fait que toute algèbre de dimension finie sur un corps parfait est séparable. $\square$

# Radical infini et nilpotence renforcée {#radrenf}

[^1]: Rappelons qu'une rétraction (*resp.* corétraction) est un morphisme inversible à droite (*resp.* à gauche); on dit aussi épimorphisme scindé (*resp.* monomorphisme scindé).

[^2]: Prendre garde à la terminologie: les notions de semi-simplicité utilisées dans [@leduc] et dans [@street] sont plus faibles.

[^3]: Selon la terminologie de Bourbaki [@alg]; selon la terminologie anglo-saxonne, on dirait plutôt "semisimple artinian\", *cf.* [@rowen].

[^4]: Voir la définition [\[d3\]](#d3){reference-type="ref" reference="d3"} ci-dessous pour plus de détails.

[^5]: Voir le § [\[prodtens\]](#prodtens){reference-type="ref" reference="prodtens"} ci-dessous pour plus de détails.

[^6]: Ces anneaux sont caractérisés par l'existence d'une borne uniforme pour la longueur de toute chaı̂ne décroissante de modules cycliques, *cf.* [@rowen 2.7.7].
