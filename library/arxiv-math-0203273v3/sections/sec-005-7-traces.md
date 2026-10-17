---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-005-7-traces
section_title: "Traces"
section_number: 7
pages: 35-50
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.944
---
*Dans tout ce paragraphe, on suppose que $({\mathcal{A}},\bullet)$ est $K$-linéaire monoı̈dale rigide, symétrique, et que $End({\bf 1}) =K$* (en revanche, on ne suppose pas ${\mathcal{A}}$ abélienne).

## Traces et idéal ${\mathcal{N}}$ {#traces}

Rappelons que la *trace* d'un endomorphisme $h\in
{\mathcal{A}}(C,C)$ est l'élément $tr(h) \in K= End({\bf 1})$ défini par $$\varepsilon_C \circ R_{C^\vee, C} \circ({\iota_{CC}}^{-1}(h) ): {\bf
1 }\to {\bf 1},$$ où $\varepsilon_C:   C\bullet C^\vee \to  {\bf 1}$ est l'évaluation. Dans la situation symétrique dans laquelle nous nous plaçons, la formule s'écrit aussi $$\label{eq6.2.8,5} tr(h)= \varepsilon_{C^\vee}
\circ({\iota_{CC}}^{-1}(h) )$$ La *dimension* (ou rang) de l'objet $A$ est la trace de $1_A$.

Soient $f\in {\mathcal{A}}(A,B)$ et $g\in {\mathcal{A}}(B,A)$. Des formules [\[eq6.2.0\]](#eq6.2.0){reference-type="eqref" reference="eq6.2.0"} et [\[eq6.2.3\]](#eq6.2.3){reference-type="eqref" reference="eq6.2.3"}, on déduit que $$tr(g\circ f)=\varepsilon_{A^\vee}(1_{A^\vee}\bullet \varepsilon_B\bullet
1_A)(\iota_{AB}^{-1}f\bullet \iota_{BA}^{-1}g)=\varepsilon_{A^\vee B}\circ
(\iota_{AB}^{-1}f\bullet \iota_{BA}^{-1}g)$$ d'où $$\label{eq6.2.9}tr(g\circ f)= tr(f\circ g)$$ et, en appliquant [\[eq6.2.6\]](#eq6.2.6){reference-type="eqref" reference="eq6.2.6"} $$\label{eq6.4.1}
tr(g\circ f)=(\iota_{AB}^{-1}f)^t\circ
\iota_{BA}^{-1}g \;\; (=tr((\iota_{AB}^{-1}f)^t\circ \iota_{BA}^{-1}g)).$$

En appliquant [\[eq6.2.11\]](#eq6.2.11){reference-type="eqref" reference="eq6.2.11"}, on obtient aussi l'identité $$tr(h^t)=tr(h).$$

Voici une autre formule utile (*cf.* [@de 7.2]): si $f$ et $g$ sont des endomorphismes de $A$ et $B$, on a $$\label{eq6.2.10}tr(f\bullet g)= tr(f) tr(g).$$

Introduisons à présent l'idéal ${\mathcal{N}}$, protagoniste principal de ce paragraphe.

::: lemme
La formule $${{\mathcal{N}}}(A,B)=\{f \in {\mathcal{A}}(A,B), \forall g\in {\mathcal{A}}(B,A), tr(g\circ f)=0\}$$ définit un idéal monoı̈dal de ${\mathcal{A}}$ [^1]. On a $${{\mathcal{N}}}(A,B)=\iota_{AB}\{f \in {\mathcal{A}}({\bf 1},A^\vee\bullet B),
\forall g\in{\mathcal{A}}(A^\vee\bullet B,{\bf 1}),  g\circ f =0\} .$$
:::

La stabilité par composition à gauche est claire et la stabilité par composition à droite s'en déduit en vertu de la formule [\[eq6.2.9\]](#eq6.2.9){reference-type="eqref" reference="eq6.2.9"}. Il suffit alors de prouver la seconde assertion, qui dit que ${\mathcal{N}}={\mathcal{N}}^{(\bullet)}$. C'est immédiat à partir de la formule [\[eq6.4.1\]](#eq6.4.1){reference-type="eqref" reference="eq6.4.1"}. $\square$

::: ex
[]{#ex1 label="ex1"} Dans le cas de l'exemple [\[ex2\]](#ex2){reference-type="ref" reference="ex2"} (motifs), l'idéal monoı̈dal ${\mathcal{N}}$ correspond à l'équivalence numérique des cycles algébriques.
:::

::: lemme
[]{#Ldim label="Ldim"} On suppose que $K$ est un corps. Soit $f_1,\dots,f_n
\in
{\mathcal{A}}(A,A)$ une famille de $n$ éléments linéairement indépendants modulo ${\mathcal{N}}(A,A)$. Alors $(f_1,\dots,f_n)$ correspond à une corétraction ${{\bf 1}}^n\hookrightarrow A^\vee\bullet A$.
:::

La donnée des $f_i$ fournit un morphisme ${{\bf 1}}^n\rightarrow 
A^\vee\bullet A$ (de $i$-ème composante $\iota_{AA}^{-1}(f_i)$). Remarquons que, par définition de ${\mathcal{N}}$, la trace induit une forme bilinéaire (symétrique) non dégénérée $${\mathcal{A}}(A,A)/{\mathcal{N}}(A,A)\times {\mathcal{A}}(A,A)/{\mathcal{N}}(A,A)\to 
K.$$

Il existe donc des éléments $g_1,\dots, g_n$ de ${\mathcal{A}}(A,A)$ tels que $tr(g_i\circ f_j) = \delta_{ij}$ (symbole de Kronecker). Le morphisme composé $$\begin{CD}
A^\vee\bullet A 
@>\circ g_1,\dots ,\circ
g_n>>  (A^\vee\bullet A)^n
@>R_{A^\vee 
A},\dots, R_{A^\vee A}>>
(A\bullet A^\vee )^n  @>{ev,\dots 
,ev}>>{{\bf 1}}^n
\end{CD}$$ est un inverse à gauche de ${{\bf 1}}^n\hookrightarrow
A^\vee\bullet A$. Réciproquement, toute corétraction comme dans l'énoncé s'obtient clairement ainsi. $\square$

::: prop
[]{#new p1 label="new p1"} On suppose que $K$ est un corps. Soit ${\mathcal{A}}$ un catégorie $K$-linéaire monoı̈dale symétrique rigide, avec $K=End({\bf 1})$. On note ${\mathcal{R}}$ son radical. Alors\
a) ${\mathcal{N}}={\mathcal{R}}^{(\bullet)}$: ${\mathcal{N}}(A,B)= \iota_{AB}({\mathcal{R}}({\bf 1}, 
A^\vee \bullet
B))$ pour tout couple $(A,B)$.\
b) ${\mathcal{N}}$ est le plus grand idéal monoı̈dal distinct de ${\mathcal{A}}$.\
c) Soit ${\mathcal{J}}$ un idéal monoı̈dal distinct de ${\mathcal{A}}$. Si ${\mathcal{A}}/{\mathcal{J}}$ est semi-simple, alors ${\mathcal{J}}={\mathcal{N}}$.
:::

$a)$ Que ${\mathcal{N}}$ soit distinct de ${\mathcal{A}}$ se voit sur le couple $({\bf 1},{\bf 1})$. Pour l'égalité ${\mathcal{N}}={\mathcal{R}}^{(\bullet)}$, il s'agit de voir que pour tout objet $A$, ${\mathcal{N}}({\bf 1},A)={\mathcal{R}}({\bf 1},A)$. C'est bien le cas, car d'après le lemme [\[L2\]](#L2){reference-type="ref" reference="L2"}, $${{\mathcal{R}}}({\bf 1},A)= \{f \in {\mathcal{A}}({\bf 1},A 
),
\forall g\in
{\mathcal{A}}(A ,{\bf 1}),
          g\circ f =0\} .$$ $b)$ Prouvons que tout idéal monoı̈dal ${\mathcal{J}}$ distinct de ${\mathcal{A}}$ est contenu dans ${\mathcal{N}}$: il suffit de faire voir que pour tout objet $A$, ${\mathcal{J}}({\bf 1},A)\subset {\mathcal{N}}({\bf 1},A)$, c'est-à-dire que pour tout $f\in {\mathcal{J}}({\bf 1},A)$ et tout $g\in
{\mathcal{A}}(A,{\bf 1})$, $g\circ f=0 \in K$. Si tel n'était pas le cas, on pourrait supposer $g\circ f=1$, donc $1\in {\mathcal{J}}({\bf 1},{\bf 1})$, d'où ${\mathcal{J}}({\bf 1},A)={\mathcal{A}}({\bf 1}
,A)$. Par ailleurs, ${\mathcal{N}}({\bf 1},{\bf 1})=0$, donc ${\mathcal{N}}\neq {\mathcal{A}}$.

$c)$ Si ${\mathcal{A}}/{\mathcal{J}}$ est semi-simple, alors ${\mathcal{R}}\subset {\mathcal{J}}$. Donc ${\mathcal{R}}^{(\bullet)}={\mathcal{N}}$ est contenu dans ${\mathcal{J}}^{(\bullet)}={\mathcal{J}}$. On a l'inclusion opposée d'après $i)$.$\square$

::: cor
L'idéal ${\mathcal{N}}$ ne dépend pas du choix du tressage (symétrique) $R$.$\square$
:::

::: prop
[]{#new p3/2 label="new p3/2"} Sous les mêmes hypothèses, les conditions suivantes sont équivalentes:

::: thlist
${\mathcal{R}}\supset {\mathcal{N}}$,

le foncteur de projection ${\mathcal{A}}\to {\mathcal{A}}/{\mathcal{N}}$ est conservatif,

pour tous objets $A,B$ de ${\mathcal{A}}$, l'identification $$\iota_{AB}:\;{\mathcal{A}}({\bf 1}, A^{\vee}\bullet B)\overset{\sim}{\longrightarrow}{\mathcal{A}}(A,B)$$ induit une inclusion $${\mathcal{R}}(A,B)\supset {\mathcal{R}}({\bf 1},A^{\vee}\bullet B).$$
:::

En outre, ${\mathcal{R}}$ est un idéal monoı̈dal si et seulement si $\;{\mathcal{R}}={\mathcal{N}}$.
:::

\(i\) $\iff$ (ii) résulte de [\[P1\]](#P1){reference-type="ref" reference="P1"} b); (i) $\iff$ (iii) n'est autre qu'une reformulation de la proposition [\[new p1\]](#new p1){reference-type="ref" reference="new p1"} a). La dernière assertion suit de ce que ${\mathcal{N}}={\mathcal{R}}^{(\bullet)}$ (ou de (i) $\iff$ (iii)).$\square$

::: cor
[]{#c2 label="c2"} Si ${\mathcal{A}}$ est semi-simple, ${\mathcal{N}}=0$. Si $\;{\mathcal{R}}\ne {\mathcal{N}}$, ${\mathcal{R}}\ne 0$.
:::

En effet, la première (*resp.* deuxième) affirmation résulte de la proposition [\[new p1\]](#new p1){reference-type="ref" reference="new p1"} (*resp.* [\[new p1\]](#new p1){reference-type="ref" reference="new p1"} et [\[new p3/2\]](#new p3/2){reference-type="ref" reference="new p3/2"}) compte tenu de ce que le radical d'une catégorie semi-simple est nul (*resp.* de ce que $0$ est un idéal monoı̈dal).$\square$

::: ex
[]{#BBM label="BBM"} Revenons à l'exemple de la catégorie monoı̈dale symétrique rigide ${\mathcal{A}}$ des motifs de Chow à coefficients rationnels. Des conjectures très fortes dues à A. Beilinson [@beilinson] et de J. Murre [@murre] (qui sont en fait équivalentes, *cf.* [@jannsen2]) prédisent l'existence d'un filtration finie fonctorielle sur les objets de ${\mathcal{A}}$. Chaque cran de la filtration est supposé provenir d'une équivalence adéquate, donc définit un idéal monoı̈dal $F^p$. D'après [@jannsen2], il résulterait de ces conjectures et des conjectures standard que $F^p$ est la puissance $p$-ième de l'idéal $F^1$ (correspondant à l'équivalence homologique) et que $F^1={\mathcal{N}}$. La finitude conjecturale de la filtration a pour conséquence que $F^1 \subset {\mathcal{R}}$, donc $F^1= {\mathcal{R}}= {\mathcal{N}}$ (${\mathcal{R}}$ est monoı̈dal), et implique alors: ${\mathcal{A}}$ est strictement de Wedderburn (noter que ${\mathcal{R}}^\omega=
\cap F^p= 0$). Ces propriétés se transférent aux catégories de motifs purs pour une équivalence adéquate quelconque.

Cet exemple conjectural est l'une des principales sources d'inspiration de ce travail.
:::

::: rem
[]{#r6.1 label="r6.1"} La compatibilité de ${\mathcal{N}}$ vis-à-vis de l'extension des scalaires (naı̈ve) ne pose pas de problème (contrairement à celle du radical ${\mathcal{R}}$, *cf.* §3.) C'est prouvé dans [@bru2 1.4.1], dans un contexte beaucoup plus large.
:::

## Traces et puissances extérieures {#tr et pext}

Cette partie est inspirée par [@de 7.2] et par le récent travail de Kimura ([@ki], voir aussi [@gu-pe]). Ici la symétrie du tressage est essentielle.

Soit $n$ un entier $>0$. On fait opérer le groupe symétrique $\mathfrak{S}_n$ sur $A^{\bullet n}$ au moyen du tressage \[symétrique!\] $R$, en écrivant tout élément $\sigma$ de $\mathfrak{S}_n$ comme produit de transpositions de la forme $(i\;i+1)$ (le résultat ne dépend pas de cette écriture, *cf.* [@de 7.2]). Plus généralement, si $A_1,\dots,A_n\in {\mathcal{A}}$ et $\beta\in \mathfrak{S}_n$, on a un isomorphisme bien déterminé $$\beta:A_1\bullet\dots\bullet A_n\to A_{\beta(1)}\bullet \dots\bullet
A_{\beta(n)}$$ covariant en $\beta$. Si $B_1,\dots,B_n$ sont d'autres objets, pour toute famille $f_i\in
{\mathcal{A}}(A_i,B_i)$, on a $$\label{eq6.5.1} \beta \circ
(f_1\bullet\dots\bullet f_n)=(f_{\beta(1)}\bullet\dots \bullet
f_{\beta(n)})\circ \beta.$$

On a aussi les formules suivantes qui nous seront utiles $$\label{eq6.5.1,4/3} \iota_{A_{\beta(1)}\bullet \ldots
\bullet A_{\beta(n)},A_{\beta(1)}\bullet
\ldots \bullet A_{\beta(n)}}((\beta^{-1},\beta)\circ\varphi)=\beta\circ
   \iota_{A_1\bullet \ldots \bullet A_n,A_1\bullet \ldots \bullet
A_n}(\varphi) \circ \beta^{-1}$$ $$\label{eq6.5.1,5/3} 
\varepsilon_{A_{\beta(n)}^\vee\bullet \ldots \bullet 
A_{\beta(1)}^\vee}\circ(\beta^{-1},\beta)
=\varepsilon_{A_n^\vee\bullet
\ldots
\bullet A_1^\vee },$$ où $(\beta^{-1},\beta)$ désigne la "permutation\" $$A_n^\vee\bullet 
\ldots \bullet A_1^\vee \bullet A_1\bullet \ldots
\bullet A_n  \to 
A_{\beta(n)}^\vee\bullet \ldots \bullet 
A_{\beta(1)}^\vee \bullet 
A_{\beta(1)}\bullet \ldots \bullet 
A_{\beta(n)}.$$

*Cas particulier de [\[eq6.5.1\]](#eq6.5.1){reference-type="eqref" reference="eq6.5.1"}*: soit $\sigma\in 
\mathfrak{S}_n$, et supposons que $B_i=A_{\sigma(i)}$ pour tout $i$. On peut alors considérer l'endomorphisme suivant de $A_1\bullet\dots\bullet A_n$ (*cf.* [@de 7.2]): $$F=\sigma^{-1}\circ (f_1\bullet\dots\bullet 
f_n).$$

Nous nous proposons de calculer la *trace de $F$*.

Écrivons $\sigma$ comme produit de cycles disjoints $\sigma_1\circ\dots\circ \sigma_p$, et soit $I_k\subset 
\{1,\dots,n\}$ le support de $\sigma_k$. Pour tout $i\in I_k$, on peut considérer l'endomorphisme de $A_i$ $$F_{k,i}=f_{\sigma^{\ell_k-1}(i)}\circ\dots\circ 
f_{\sigma(i)}\circ f_i$$ où $\ell_k=|I_k|$ est la longueur du cycle $\sigma_k$. D'après [\[eq6.2.9\]](#eq6.2.9){reference-type="eqref" reference="eq6.2.9"}, la trace $tr(F_{k,i})$ ne dépend pas du choix de $i$: notons-là $t_k$.

::: prop
[]{#p6.4.1 label="p6.4.1"} On a $$tr(F)=\prod_{k=1}^p 
t_k.$$
:::

Soit $\beta\in \mathfrak{S}_n$. D'après [\[eq6.5.1\]](#eq6.5.1){reference-type="eqref" reference="eq6.5.1"} et [\[eq6.2.9\]](#eq6.2.9){reference-type="eqref" reference="eq6.2.9"}, on a $$\begin{gathered}
tr(\beta\sigma^{-1}
\beta^{-1}\circ(f_{\beta(1)}\bullet\dots\bullet 
f_{\beta(n)}))\\
=tr(\beta\circ\sigma^{-1}\circ(f_1\bullet\dots\bullet 
f_n)\circ
\beta^{-1})\\
=tr(\sigma^{-1}\circ(f_1\bullet\dots\bullet 
f_n)).
\end{gathered}$$

Cette formule permet de se ramener au cas où les $I_k$ forment une partition croissante de $\{1,\dots,n\}$: $$I_k=\{\ell_1+\dots+\ell_{k-1}+1,\dots,\ell_1+\dots+ 
\ell_k\}$$ et où, de plus, pour tout $k$, $\sigma_k$ est le cycle "croissant\" $$\sigma_k=(\ell_1+\dots+\ell_{k-1}+1,\cdots 
,\ell_1+\dots+\ell_k).$$

Posant alors $$F_k=\sigma_k^{-1}\circ
(f_{\ell_1+\dots+\ell_{k-1}+1}\bullet\displaystyle
ots\bullet f_{\ell_1+\dots+\ell_k})$$ une itération de la formule [\[eq6.2.10\]](#eq6.2.10){reference-type="eqref" reference="eq6.2.10"} donne $$tr(F)=\prod_{k=1}^p tr(F_k).$$

Ceci ramène la démonstration de la proposition [\[p6.4.1\]](#p6.4.1){reference-type="ref" reference="p6.4.1"} au cas où $\sigma$ est la permutation cyclique de $\{1,\dots,n\}$. Par itération de la formule [\[eq6.2.3\]](#eq6.2.3){reference-type="eqref" reference="eq6.2.3"}, et compte tenu de [\[eq6.2.0\]](#eq6.2.0){reference-type="eqref" reference="eq6.2.0"} et [\[eq6.2.8\]](#eq6.2.8){reference-type="eqref" reference="eq6.2.8"}, on trouve $$\begin{gathered}
\label{eq6.5.3}
\iota^{-1}_{A_1A_1}(f_n\circ 
\dots \circ
f_1)\\
= (1_{A_1^\vee}\bullet\varepsilon_{A_2}\dots 
\bullet\varepsilon_{A_{n}}
\bullet 1_{A_1})\circ (\iota_{A_1A_2}^{-1} 
f_1\bullet \dots \bullet
\iota_{A_nA_1}^{-1} f_n)  \\
= 
(1_{A_1^\vee}\bullet\varepsilon_{A^\vee_n\bullet\dots \bullet 
A^\vee_2}
\bullet 1_{A_1})\circ (\iota_{A_2\bullet\dots \bullet A_n 
\bullet
A_1,A_2\bullet\dots \bullet A_n \bullet A_1}^{-1} F 
).
\end{gathered}$$

En appliquant $\varepsilon_{A^\vee}$ "aux deux facteurs extrêmes $A^\vee$ et $A$\" (ce qui fait sens grâce au tressage), on obtient $$\begin{gathered}
\label{eq6.5.4}
tr(f_n\circ \dots \circ f_1)=
\varepsilon_{A^\vee_1\bullet A^\vee_n\bullet\dots \bullet A^\vee_2}
(\iota_{A_2\bullet\dots \bullet A_n \bullet A_1,A_2\bullet\dots \bullet
A_n \bullet A_1}^{-1} F )\\
=\varepsilon_{A^\vee_1\bullet
A^\vee_n\bullet\dots\bullet A^\vee_2}  (\iota_{A_2\bullet\dots \bullet
A_n \bullet A_1,A_2\bullet\dots \bullet A_n \bullet A_1}^{-1} F )\\
=\varepsilon_{A^\vee_n\bullet\dots \bullet A^\vee_1}
(\iota_{A_1\bullet\dots \bullet A_n  ,A_1\bullet\dots \bullet A_n}^{-1}
(\sigma \circ  (f_1\bullet\dots\bullet f_n)))
= tr(\sigma\circ(f_1\bullet\dots\bullet f_n))
\end{gathered}$$ (*cf.* aussi [@de 7.2]). $\square$

::: cor
[]{#c6.5.1 label="c6.5.1"} Supposons $A_1=\dots=A_n=A$ et $f_1=\dots=f_n=f$. Alors $$tr(F)=\prod_{k=1}^p tr(f^{\circ \ell_k}).$$ En particulier, pour $f=1$, on a $tr(\sigma)=\dim(A)^p$.$\square$
:::

*Dans la suite de ce paragraphe (jusqu'à [0.3](#tracesnil){reference-type="ref" reference="tracesnil"}), on suppose que ${\mathcal{A}}$ est pseudo-abélienne.*

::: defn
[]{#alt, sym label="alt, sym"} Soit $n$ un entier naturel tel que $n!$ soit inversible dans $K$, et soit $A\in {\mathcal{A}}$. La *puissance extérieure $n$-ième* $\Lambda^n A$ de $A$ est l'image du projecteur d'antisymétrisation sur $A^{\bullet n}$ $$\label{eq6.5.2} a_n=\frac{1}{n!}\sum_{\sigma \in \mathfrak
S_n}\,sgn(\sigma)
\sigma.$$ De même, la puissance symétrique $n$-ième ${\bf S}^n
A$ d'un objet $A$ de ${\mathcal{A}}$ est l'image du projecteur de symétrisation $s_n=\frac{1}{n!}\sum_{\sigma \in \mathfrak S_n}\, \sigma.$
:::

Ces constructions sont *fonctorielles* en $A$.

::: prop
[]{#a la Deligne label="a la Deligne"} Soit $A$ un objet de ${\mathcal{A}}$, et soit $f$ un endomorphisme de $A$. Alors on a $$tr(\Lambda^n(f))=\frac{1}{n!}
\sum_{\sigma\in \mathfrak{S}_n} sgn(\sigma) \prod_{k=1}^p tr(f^{\circ
\ell_k})$$ où, pour tout $\sigma\in \mathfrak{S}_n$, $\ell_1,\dots,\ell_p$ sont les longueurs des cycles disjoints constitutant $\sigma$. En particulier, si $d=\dim A$, la dimension de $\Lambda^n A$ est $$\binom{d}{n} = \frac{d(d-1)\dots (d-n+1)}{n!}.$$ De même, on a $$tr(\mathbf{S}^n(f))=\frac{1}{n!}
\sum_{\sigma\in \mathfrak{S}_n} \prod_{k=1}^p tr(f^{\circ
\ell_k})$$ $$\dim \mathbf{S}^n(A)=\binom{d+n-1}{n} = \frac{d(d+1)\dots
(d+n-1)}{n!}.$$
:::

La première assertion résulte directement du corollaire [\[c6.5.1\]](#c6.5.1){reference-type="ref" reference="c6.5.1"}. La seconde résulte du cas particulier $f=1$ et de l'identité bien connue $$\binom{d}{n}=\frac{1}{n!}\sum_{\sigma\in \mathfrak{S}_n} sgn(\sigma)
d^{\alpha(\sigma)}$$ où $\alpha(\sigma)$ est le nombre de cycles intervenant dans $\sigma$. Les assertions pour les puissances symétriques se démontrent de même. $\square$

::: cor
Sous les hypothèses de la proposition [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"},\
a) $tr(f^{\circ n})$ s'exprime comme un polynôme universel en les $tr(\Lambda^i(f))$ pour $i=1,\dots,n$ à coefficients dans $\mathbf{Z}[1/n!]$.\
b) On a $$\label{eq6.6.4}tr(\Lambda^n (1_A+f))= \sum_{i=0}^n
tr(\Lambda^i f ).$$
:::

a\) Posons $t_i = tr(f^{\circ i})$: le second membre de la proposition [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"} est donc un polynôme universel en les $t_i$. On remarque que $t_n$ intervient dans le terme $\prod_{k=1}^p tr(f^{\circ\ell_k})$ si et seulement si $\sigma$ est un cycle de longueur $n$, et qu'alors ce terme est égal à $t_n$. Tous ces cycles ont la même signature $(-1)^{n-1}$, et ils sont au nombre de $(n-1)!$. Ainsi, le second membre de la proposition [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"} est un polynôme du premier degré en $t_n$, et le coefficient de $t_n$ est égal à $(-1)^{n-1}/n$. L'assertion en résulte, par récurrence sur $n$.

b\) Grâce à a), on voit que $tr(\Lambda^n(1+f))$ s'écrit comme un polynôme universel à coefficients dans $\mathbf{Z}[\frac{1}{n!}]$ en les $tr(\Lambda^i f )$ pour $i\leq n$. Prenant pour ${\mathcal{A}}$ la catégorie monoı̈dale des modules libres de type fini sur $K$, on obtient la formule voulue.$\square$

En nous inspirant de Kimura [@ki] (qui se plaçait dans le cadre des motifs de Chow, voir aussi [@gu-pe 3.15]), nous allons démontrer un résultat plus précis que [\[p6.4.1\]](#p6.4.1){reference-type="ref" reference="p6.4.1"} et [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"}, qu'on retrouve en appliquant $\varepsilon_{A_1^\vee}$ aux facteurs extrêmes. On reprend les notations de [\[p6.4.1\]](#p6.4.1){reference-type="ref" reference="p6.4.1"}.

::: prop
[]{#a la Kimura label="a la Kimura"} Pour tout $\sigma\in  \mathfrak S_n$, notons $\ell_1(\sigma)$ la longueur du cycle $\sigma_1$ de $\sigma$ ayant $1$ dans son support. On a $$\begin{gathered}
\label{eq6.6.3}\iota_{A_1
A_1}\big((1_{A_1^\vee}\bullet\varepsilon_{A_n^\vee
\bullet\dots
\bullet A_2^\vee} \bullet 1_{A_1  })( \iota_{A_1\bullet \dots \bullet
A_n,A_1\bullet \dots \bullet
A_n}^{-1}( \sigma^{-1}\circ  f_1\bullet\dots\bullet f_n))\big)\\
=t_\sigma.f_{\sigma_1^{\ell_1-1}(1)}\circ\dots\circ f_{\sigma_1(1)}\circ
f_1,
\end{gathered}$$ où $t_\sigma= 1$ si $\sigma$ est cyclique ($\ell_1=n$), et $t_\sigma  \in K$ est un produit de traces de monômes non triviaux en les $f_i$ si $\sigma$ n'est pas cyclique.

A fortiori, si $A_1=\ldots = A_n =A$ et $f_1=\ldots = f_n =f \in
{\mathcal{A}}(A,A)$, et si $n!$ est inversible dans $K$, on obtient $$\label{eq6.6.4a}
\iota_{AA}\big((1_{A^\vee}\bullet\varepsilon_{A^{\bullet (n-1)}}
\bullet 1_{A })\circ (\iota_{A^{\bullet n},A^{\bullet n}}^{-1}(\Lambda^n
f ))\big)= \sum_{\sigma\in \mathfrak
S_n}  t'_\sigma f^{\ell_1(\sigma)}$$ $$\label{eq6.6.4b}
\iota_{AA}\big((1_{A^\vee}\bullet\varepsilon_{A^{\bullet (n-1)}}
\bullet 1_{A })\circ (\iota_{A^{\bullet n},A^{\bullet
n}}^{-1}(\mathbf{S}^n f ))\big)=
\sum_{\sigma\in \mathfrak
S_n}  t"_\sigma f^{\ell_1(\sigma)}$$ où $t'_\sigma= \frac{(-1)^{n-1}}{n!}$ si $\sigma$ est cyclique, et $t'_\sigma=\pm\frac{1}{n!}\times$ un produit de traces de puissances non nulles de $f$ sinon (*resp.* mêmes formules pour $t"_\sigma$, sans les signes).
:::

Abrégeons provisoirement $\iota_{AA}$ en $\iota_A$, et $$(1_{A_1^\vee}\bullet\varepsilon_{A_n^\vee
\bullet\dots
\bullet A_2^\vee} \bullet 1_{A_1  })\circ   \iota_{A_1\bullet \dots
\bullet A_n,A_1\bullet \dots \bullet
A_n}^{-1}(-)$$ en $\Theta_{A_1\ldots A_n}(-)$.

Soit $\beta\in \mathfrak{S}_n$ une permutation telle que $\beta(1)=1$. Compte tenu de [\[eq6.5.1\]](#eq6.5.1){reference-type="eqref" reference="eq6.5.1"}, [\[eq6.5.1,4/3\]](#eq6.5.1,4/3){reference-type="eqref" reference="eq6.5.1,4/3"} et [\[eq6.5.1,5/3\]](#eq6.5.1,5/3){reference-type="eqref" reference="eq6.5.1,5/3"}, on a $$\begin{gathered}
\iota_{A_1 A_1} \big(   \Theta_{ A_{1}   A_{\beta (1)} \ldots
A_{\beta (n)}  }(\beta \sigma^{-1}
\beta^{-1}\circ (f_1\bullet f_{\beta (2)} \bullet \dots \bullet 
f_{\beta (n)} ))\big) \\=
\iota_{A_1 A_1} \big(\Theta_{A_1A_{\beta (2)}\ldots A_{\beta (n)} }
(\beta\circ \sigma^{-1}
\circ (f_1\bullet\dots\bullet f_n)\circ \beta^{-1})\big)\\
=\iota_{A_1 A_1}\big(\Theta_{A_1\ldots A_n}(\sigma^{-1}\circ
(f_1\bullet\dots\bullet f_n))\big).
   
\end{gathered}$$ Comme dans la preuve de [\[p6.4.1\]](#p6.4.1){reference-type="ref" reference="p6.4.1"}, et parce que $\sigma_1$ est choisi de telle sorte que $1$ soit dans son support, cette formule permet de se ramener au cas où les $I_k$ forment une partition croissante de $\{1,\dots,n\}$ et où, de plus, pour tout $k$, $\sigma_k$ est le cycle "croissant\" $$\sigma_k=(\ell_1+\dots+\ell_{k-1}+1,\cdots ,\ell_1+\dots+\ell_k),$$ ce qui permet d'écrire $$\sigma^{-1}\circ f_1\bullet\dots\bullet f_n   =
(\sigma_1^{-1}\circ f_1\bullet\dots\bullet f_{\ell_1})\bullet \dots
\bullet  (\sigma_p^{-1}\circ f_{n-{\ell_p}}\bullet\dots\bullet f_n ).$$ Compte tenu de [\[eq6.2.0\]](#eq6.2.0){reference-type="eqref" reference="eq6.2.0"} et [\[eq6.2.8\]](#eq6.2.8){reference-type="eqref" reference="eq6.2.8"}, on en tire $$\begin{gathered}
 \iota_{A_1} \big(\Theta_{A_1\ldots A_n}(
f_1\bullet\dots\bullet f_n)\big)
     \\ =\iota_{A_1  }\big( (1_{A_1^\vee} \bullet
\varepsilon_{A^\vee_{\ell_1} \bullet \dots \bullet A^\vee_2 }\bullet
1_{A_1  })
   (\iota_{A_1 \bullet \ldots \bullet A_{\ell_1} }^{-1}(\sigma_1^{-1}\circ
f_1\bullet\dots\bullet f_{\ell_1}) )\bullet \\
   \varepsilon_{A^\vee_{\ell_1+\ell_2} \bullet \dots \bullet
A^\vee_{\ell_1+1} }
   (\iota_{A_{\ell_1 +1} \bullet \ldots \bullet A_{\ell_1+\ell_2}
}^{-1}(\sigma_2^{-1}\circ
f_{\ell_1+1}\bullet\dots\bullet f_{\ell_1+\ell_2}) )\bullet \\ \ldots
\bullet
   \varepsilon_{A^\vee_{n } \bullet \dots \bullet A^\vee_{n-\ell_p} }
   (\iota_{A_{n-\ell_p} \bullet \ldots \bullet
A_{n}}^{-1}(\sigma_p^{-1}\circ f_{n-\ell_p}\bullet\dots\bullet f_{n})
)\big)
\end{gathered}$$ ce qui n'est autre que $$(f_{\ell_1}\circ \cdots \circ
f_1).tr(f_{\ell_1+\ell_2}\circ
\dots \circ f_{\ell_1 +1}).\cdots .tr(f_n \circ \cdots \circ
f_{n-\ell_p})$$ par [\[eq6.5.3\]](#eq6.5.3){reference-type="eqref" reference="eq6.5.3"} et [\[eq6.5.4\]](#eq6.5.4){reference-type="eqref" reference="eq6.5.4"}. Ceci démontre la première assertion, et la seconde s'ensuit immédiatement. $\square$

::: prop
[]{#nouvelle label="nouvelle"} Soit $A\ne 0$ un objet de ${\mathcal{A}}$. On suppose qu'il existe un entier $n>0$ tel que $n!$ soit inversible dans $K$ et tel que tel que $\Lambda^n A= 0$ (*resp.* que $\mathbf{S}^nA=0$). Alors\
i) ${\mathcal{N}}(A,A)$ est un nil-idéal de ${\mathcal{A}}(A,A)$ d'échelon de nilpotence $\leq n$. C'est même un idéal nilpotent de ${\mathcal{A}}(A,A)$, d'échelon de nilpotence borné en fonction de $n$. En particulier, l'image de $A$ n'est pas nulle dans ${\mathcal{A}}/{\mathcal{N}}$.\
ii) Si $K$ est intègre de caractéristique nulle, la dimension de $A$ (*resp.* l'opposé de la dimension de $A$) est un entier naturel $\le n$.
:::

i\) la formule [\[eq6.6.4a\]](#eq6.6.4a){reference-type="eqref" reference="eq6.6.4a"} nous dit que $$\iota_{A  }(1_{A ^\vee}\bullet\varepsilon_{A^{\bullet
(n-1)}}\bullet 1_{A })(
\iota_{A^{\bullet n}}^{-1}(\Lambda^n f ))= \sum_{\sigma\in \mathfrak
S_n}  t'_\sigma f^{\ell_1(\sigma)},$$ où $t'_\sigma= \frac{({-1)}^{n-1}}{n!}$ si $\sigma$ est cyclique, et $t'_\sigma=\pm\frac{1}{n!}\times$ un produit de traces de puissances non nulles de $f$ sinon. Pour $f\in {\mathcal{N}}$, ces derniers termes s'annulent, et on a donc $$\iota_{A}(1_{A ^\vee}\bullet\varepsilon_{A^{\bullet (n-1)}}
\bullet 1_{A })(\iota_{A^{\bullet n}}^{-1}(\Lambda^n f ))=
\frac{({-1)}^{n-1}}{n}f^n.$$

Mais $\Lambda^n f = 0$ si $\Lambda^n A= 0$, et on trouve finalement que $f^n=0$. De même avec $S^n$ au lieu de $\Lambda^n$. La nilpotence de ${\mathcal{N}}(A,A)$ résulte alors du théorème de Nagata-Higman [@nagata; @higman], rappelé ci-dessous pour la commodité du lecteur.

La troisième assertion de i) est immédiate.

ii\) D'après la proposition [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"}, la dimension de $\Lambda^n A$ est donnée par le coefficient binômial $\binom{\dim
A}{n}$, qui ne s'annule que si $\dim A$ est un entier naturel $\le n$.

Le cas d'une puissance symétrique se traite de même.$\square$

::: lemme
[]{#naghig label="naghig"} Soient $n$ un entier $>0$ et $K$ un anneau commutatif unitaire dans lequel $n!$ est inversible. Soit $R$ une $K$-algèbre associative non unitaire telle que tout élément $x\in R$ vérifie $x^n=0$. Alors $R^{2^n-1}=0$.
:::

(d'après P. Higgins) On raisonne par récurrence sur $n$, en posant $R= R_n$. Posons $$\xi (x,y) = \sum_{i=0}^{n-1} x^i y x^{n-1-i}
\text{ et }\eta (x,y,z)=\sum_{i,j= 0}^{n-1} x^i z y^j x^{n-i-1}
y^{n-j-1}.$$

En écrivant $(x+iy)^n= 0$ pour $i=0,\ldots n-1$, on obtient par Van der Monde (compte tenu de ce que $(n-1)!$ est inversible dans $K$) que $\xi(x,y)$ est identiquement nul sur $R_n\times R_n$. Donc $\eta(x,y,z)=\sum_{j=0}^{n-1} \xi(x, zy^j)y^{n-1-j}=0$, mais $\eta(x,y,z)$ se réécrit $nx^{n-1}zy^{n-1} +
\sum_{j=0}^{n-2}\, x^j z \xi (y, x^{n-1-j})$, d'où $x^{n-1} zy^{n-1}
= 0$ (compte tenu de ce que $n$ est inversible dans $K$). Soit $I_{n-1}$ l'idéal de $R_n$ engendré par les puissances $(n-1)$-ièmes. La $K$-algèbre $R_{n-1}= R_n/I_{n-1}$ est nil d'échelon $n-1$. Par récurrence, $R_{n-1}^{2^{n-1}-1}=0$, *i.e.* $R_n^{2^{n-1}-1}\subset I_{n-1}$, et on conclut de ce qui précède que $$R_n^{2^n-1}= R_n^{2^{n-1}-1}.R_n.R_n^{2^{n-1}-1}\subset I_{n-1}\cdot
R_n\cdot I_{n-1}=0.$$ $\square$

## Trace des endomorphismes nilpotents {#tracesnil}

Nous ignorons si un endomorphisme nilpotent est toujours de trace nilpotente, sans hypothèse supplémentaire. Nous allons néanmoins le démontrer dans deux cas particuliers.

::: prop
[]{#nil, tr label="nil, tr"} Supposons que ${\mathcal{A}}$ soit pseudo-abélienne et que la dimension de tout objet de ${\mathcal{A}}$ soit un entier naturel. Soit $A$ un objet de dimension $n$ telle que $n!$ soit inversible dans $K$. Alors tout endomorphisme nilpotent de $A$ est de trace nilpotente dans $K$.
:::

Par le théorème de Krull et par extension des scalaires (naïve), on se ramène au cas où $K$ est un corps. Par extension des scalaires de $K$ à $K[t]$, la formule [\[eq6.6.4\]](#eq6.6.4){reference-type="eqref" reference="eq6.6.4"} donne $tr(\Lambda^n (1+t f ))= 
\sum_{i=0}^n t^i tr(\Lambda^i f)$. Pour montrer que $tr(f)=0$ pour tout $f$ nilpotent, il suffit donc d'établir que $tr(\Lambda^n (1+f 
))=1$ pour tout tel $f$. Or par la proposition [\[a la Deligne\]](#a la Deligne){reference-type="ref" reference="a la Deligne"}, le rang de $\Lambda^n A$ est $1$. Il suffit donc de démontrer que pour tout objet $B$ de rang $1$, $({\mathcal{A}}/{\mathcal{N}})(B,B)=K.1_B
\stackrel{tr 
\,\cong}{\longrightarrow} K$, compte tenu de ce que $K$ est un corps. Cela découle du lemme suivant, qui est une conséquence immédiate de [\[Ldim\]](#Ldim){reference-type="ref" reference="Ldim"}:

::: lemme
[]{#dim 0 ou 1 label="dim 0 ou 1"} Supposons que $K$ soit un corps, que ${\mathcal{A}}$ soit pseudo-abélienne et que la dimension de tout objet soit un entier naturel. Alors tout objet de dimension $0$ de ${\mathcal{A}}/{\mathcal{N}}$ est nul, et pour tout objet $B$ de ${\mathcal{A}}/{\mathcal{N}}$ de dimension $1$, le morphisme canonique $\eta_B:{\bf 1}\to B^\vee\bullet B$ est un isomorphisme. $\square$
:::

::: prop
[]{#a la bru label="a la bru"} Supposons qu'il existe un foncteur monoı̈dal symétrique $H$ de ${\mathcal{A}}$ vers une catégorie abélienne monoı̈dale symétrique rigide ${\mathcal{V}}$; supposons en outre que l'application $K\to  {\mathcal{V}}({\bf 1}, {\bf 1})$ soit injective. Alors tout endomorphisme nilpotent est de trace nulle.
:::

On se ramène au cas ${\mathcal{A}}={\mathcal{V}}$, donc à supposer ${\mathcal{A}}$ abélienne. Cela permet de factoriser $f=m\circ e$ en épi suivi de mono. Si $f^n=0$, on a donc $$0=(me)^n=m(em)^{n-1}e$$ d'où $(em)^{n-1}=0$ puisque $m$ (*resp.* $e$) est simplifiable à gauche (*resp.* à droite). On écrit alors $tr(me)=tr(em)$, et on conclut par récurrence sur l'échelon de nilpotence. $\square$

::: rem
Dans [\[nil, tr\]](#nil, tr){reference-type="ref" reference="nil, tr"}, contrairement à [\[a la bru\]](#a la bru){reference-type="ref" reference="a la bru"}, on ne peut remplacer "trace nilpotente\" par "trace nulle\" si $K$ n'est pas réduit: la catégorie ${\mathcal{A}}$ des modules libres de type fini sur l'algèbre des nombres duaux $D=K[\varepsilon]/(\varepsilon^2)$ est monoı̈dale, $D$-linéaire, symétrique, rigide, et vérifie $End\,{\bf 1}= D$ (mais n'est pas abélienne). Or $\varepsilon.1_{\bf 1}$ est un endomorphisme nilpotent de trace non nulle.
:::

## $\otimes$-Radicaux {#tens-rad}

On suppose toujours ${\mathcal{A}}$ monoı̈dale symétrique rigide.

::: defn
[]{#d6.2 label="d6.2"} Soit ${\mathcal{J}}$ un idéal monoı̈dal de ${\mathcal{A}}$. Le $\otimes$-radical de ${\mathcal{J}}$ est défini par: $$\sqrt[ \otimes]{ {\mathcal{J}}}(A,B)=\{f\in {\mathcal{A}}(A,B), \exists n \in {\bf N},
f^{\bullet n} \in {\mathcal{J}}(A^{\bullet
n},B^{\bullet n})\}.$$
:::

::: lemme
[]{#l8.1 label="l8.1"} i) $\sqrt[ \otimes]{ {\mathcal{J}}}$ est un idéal monoı̈dal.\
ii) Pour tout objet $A$, l'idéal $\sqrt[\otimes]{0}(A,A)$ est nil. Qui plus est, l'idéal bilatère engendré par un élément quelconque de $\sqrt[\otimes]{0}(A,A)$ est nilpotent.\
iii) $\sqrt[ \otimes]{0}$ est contenu dans ${\mathcal{R}}\cap {\mathcal{N}}$ (rappelons que ${\mathcal{R}}$ désigne le radical de ${\mathcal{A}}$.)
:::

$i)$ Pour montrer que $\sqrt[ \otimes]{ {\mathcal{J}}}$ est un idéal monoı̈dal, le seul point non trivial est de vérifier que $\sqrt[ \otimes]{ {\mathcal{J}}}(A,B)$ est stable par addition. Soient $f$ et $g$ deux éléments de cet ensemble. Il existe donc $n \in {\bf N}$ tel que $f^{\bullet n}
=g^{\bullet n}\in {\mathcal{J}},$ et l'on voit alors que $(f+g)^{\bullet 2n}\in {\mathcal{J}}$ puisque ${\mathcal{J}}$ est un idéal monoı̈dal.

$ii)$ (*cf.* [@ki dém. de la prop. 2.16]). Soit $f\in \sqrt[
\otimes]{0}(A,A)$. Pour tous $g_1,
\ldots ,  g_{n+1}\in {\mathcal{A}}(A,A)$, on a $g_{n+1}\bullet f
\bullet g_n \bullet \ldots \bullet f \bullet g_{1}=0$ (appliquer le tressage), d'où, par [\[eq6.5.3\]](#eq6.5.3){reference-type="eqref" reference="eq6.5.3"}, $$\begin{gathered}
\iota_{AA}^{-1}(g_1\circ f \circ g_2 \circ \ldots \circ f
\circ g_{n+1})=\\
(1_{A^\vee}\bullet\varepsilon_{A^\vee \bullet\dots\bullet A^\vee }
\bullet 1_A)\circ  \iota_{A^{\bullet 2n+1},A^{\bullet 2n+1}}^{-1}
(\sigma^{-1} \circ(g_{n+1}\bullet f
\bullet g_n \bullet \ldots \bullet f \bullet g_{1}))
\end{gathered}$$ où $\sigma$ est la permutation cyclique de $\{1,\dots,2n+1\}$. On obtient donc que $g_1\circ f \circ g_2\circ
\ldots\circ f \circ g_{n+1}=0$.

$iii)$ $\sqrt[ \otimes]{0}\subset {\mathcal{R}}$ suit immédiatement de $ii)$. Pour $\sqrt[ \otimes]{0}\subset {\mathcal{N}}$, on utilise la formule [\[eq6.2.10\]](#eq6.2.10){reference-type="eqref" reference="eq6.2.10"}: $tr(f^{\bullet n})= tr(f)^n$. $\square$

::: ex
[]{#ex1' label="ex1'"} Dans le cas de l'exemple [\[ex2\]](#ex2){reference-type="ref" reference="ex2"} (motifs), l'idéal monoı̈dal $\sqrt[ \otimes]{0}$ correspond à l'équivalence de smash-nilpotence sur les cycles algébriques, introduite par V. Voevodsky [@voevodsky]. Sa conjecture principale (loc. cit.) revient à dire que $\sqrt[ \otimes]{0}={\mathcal{N}}$ (dans le cas où le corps de coefficients est de caractéristique nulle).

Par ailleurs, dans [@thomason], Thomason calcule $\sqrt[ 
\otimes]{0}$ dans le cas des catégories dérivées de catégories de faisceaux cohérents.
:::

::: rem
[]{#r6.1a label="r6.1a"} La compatibilité de $\sqrt[\otimes]{0}$ vis-à-vis de l'extension des scalaires (naı̈ve) est immédiate.
:::

# Théorèmes de structure {#nouveau par}

Dans ce paragraphe, nous tirons les fruits des calculs précédents, pour obtenir des théorèmes de structure: ceux-ci sont rassemblés dans [1.2](#rtss){reference-type="ref" reference="rtss"}. Dans tout le paragraphe, *$K$ est un corps et ${\mathcal{A}}$ est une catégorie $K$-linéaire monoı̈dale symétrique rigide, avec $End({\bf 1})=K$*.

On note ${\mathcal{R}}$ le radical, et ${\mathcal{N}}$ le plus grand idéal monoı̈dal distinct de ${\mathcal{A}}$. (*cf.* [\[new 
p1\]](#new 
p1){reference-type="ref" reference="new 
p1"}).

## Structure de ${\mathcal{A}}/{\mathcal{N}}$ {#a sur n}

 

::: prop
[]{#new p2 label="new p2"} On suppose qu'il existe un foncteur $F:
{\mathcal{A}}\to Vec_L$ vers la catégorie des espaces vectoriels de dimension finie sur une extension $L$ de $K$, vérifiant $\;F({\bf 1})\neq 0$.\
a) Alors les morphismes de ${\mathcal{A}}/{\mathcal{N}}$ forment des $K$-espaces de dimension finie. Plus précisément, $$\dim_K 
({\mathcal{A}}/{\mathcal{N}})(A,B)\leq \dim_LF(A^\vee\otimes B).\dim_LF({\bf 1}).$$ En particulier, ${\mathcal{A}}/{\mathcal{N}}$ est semi-primaire.\
b) Si $F$ est la composée $G\circ H$ d'un foncteur monoı̈dal symétrique $H$ de ${\mathcal{A}}$ vers une catégorie abélienne monoı̈dale symétrique rigide ${\mathcal{V}}$, et d'un foncteur $G:
{\mathcal{V}}\to Vec_L$, alors ${\mathcal{R}}\subset{\mathcal{N}}$ et ${\mathcal{A}}/{\mathcal{N}}$ est semi-simple.
:::

$a)$ On va donner deux preuves, la première valable seulement si $F$ est $K$-linéaire.

1\) Comme $({\mathcal{A}}/{\mathcal{N}})(A,B)\otimes_K L\simeq ({\mathcal{A}}_L/{\mathcal{N}}_L)(A,B)$ (*cf.* remarque [\[r6.1\]](#r6.1){reference-type="ref" reference="r6.1"}), on peut supposer $L=K$. D'autre part, par rigidité, on peut supposer que $A={\bf 1}$. Considérons alors l'application $K$-linéaire définie par $F$: $$F:{\mathcal{A}}({\bf 1},B)\to 
Hom_K(F({\bf 1}),F(B)).$$

Soit $f\in {\mathcal{A}}({\bf 1},B)$ tel que $F(f)=0$. Pour tout $g\in {\mathcal{A}}(B,{\bf 1})$, on a $F(gf)=0$, donc $gf=0$: en effet, $F:K=End({\bf 1})\to End_K(F({\bf 1}))$ est injectif puisque $F({\bf 1})\ne 0$. Ainsi $\operatorname{Ker}F\subset {\mathcal{N}}({\bf 1},B)$. On a donc $$\dim {\mathcal{A}}/{\mathcal{N}}({\bf 1},B)\le 
\dim {\mathcal{A}}({\bf 1},B)/\operatorname{Ker}F\le \dim
Hom(F({\bf 1}),F(B)).$$

2\) Soit $V$ le sous-$L$-espace de $Hom_L(F(A^\vee\bullet  B),F({\bf 1}))$ engendré par $F({\mathcal{A}}(A^\vee\bullet  B,{\bf 1}))$. On peut donc trouver des éléments $b_1, \dots, b_n$ de ${\mathcal{A}}(A^\vee\bullet  B,{\bf 1})$, avec $n\leq \dim_L F(A^\vee\bullet
B).\dim_LF({\bf 1})$, qui engendrent $V$. Soit $a\in
{\mathcal{A}}(A,B)\cong
{\mathcal{A}}({\bf 1},A^\vee\bullet  B)$. Dire que $a\in {\mathcal{N}}(A,B)\cong
{\mathcal{N}}({\bf 1},A^\vee\bullet  B)$, c'est dire que $b\circ a=0$ dans $K=End({\bf 1})$ pour tout $b\in {\mathcal{A}}(A^\vee\bullet 
B,{\bf 1})$. Comme $F$ est un foncteur, cela revient à dire que $V\circ F(a)=0\in L$. Comme les $F(b_i)$ engendrent $V$ sur $L$, cela revient finalement à dire que $b_i\circ a=0$ pour $i=1,\dots n$. Ainsi $a\mapsto (b_i\circ a)_i$ définit un plongement $K$-linéaire de $({\mathcal{A}}/{\mathcal{N}})(A,B) \cong ({\mathcal{A}}/{\mathcal{N}})({\bf 1},
A^\vee\bullet 
B)$ dans $K^n$.

$b)$ Comme ${\mathcal{A}}/{\mathcal{N}}$ est semi-primaire, toutes les $K$-algèbres d'endomorphismes ${\mathcal{A}}/{\mathcal{N}}(C,C)$ sont semi-primaires, donc leurs radicaux sont nilpotents. D'après [\[a la bru\]](#a la bru){reference-type="ref" reference="a la bru"}, tout élément de ce radical est donc de trace nulle. En appliquant ceci à $C=A\oplus B$, on voit que ${\mathcal{R}}(A,B)\subset {\mathcal{N}}(A,B)$. Donc ${\mathcal{R}}\subset
{\mathcal{N}}$, et ${\mathcal{A}}/{\mathcal{N}}$ est semi-simple puisque semi-primaire et de radical nul.$\square$

::: rems
[]{#rmot label="rmot"} 1) La preuve de $a)$ est une variante abstraite de la preuve classique de la finitude des cycles algébriques modulo l'équivalence numérique. L'hypothèse est très faible, mais non superflue: on peut montrer que l'exemple de [@de 2.19] (il s'agit d'une ind-catégorie obtenue à partir de la catégorie monoı̈dale symétrique rigide ${\mathcal{A}}$ librement engendrée par un objet $X$ de dimension transcendante sur $\mathbf{Q}$) vérifie nos conditions et est même abélienne, mais que ${\mathcal{A}}/{\mathcal{N}}$ n'est pas semi-primaire (en fait, il découle du calcul de ${\mathcal{A}}(X,X)$ fait dans *loc. cit.* que ${\mathcal{N}}(X,X)=0$).

2\) Le même énoncé (sans les inégalités de dimensions) vaut si l'on suppose seulement que $L$ est une $K$-algèbre semi-simple commutative plutôt qu'un corps. En effet, on se ramène à la proposition [\[new p2\]](#new p2){reference-type="ref" reference="new p2"} en projetant sur la catégorie $Vec_{L_i}$, où $L_i$ est un facteur simple de $L$ tel que $F({\bf 1})\otimes_L L_i\ne 0$.
:::

Voici un autre énoncé qui va dans le même sens:

::: prop
[]{#new p5/2 label="new p5/2"} On suppose que ${\mathcal{A}}$ est pseudo-abélienne et que les dimensions des objets sont des entiers naturels.\
$a)$ Alors les morphismes de ${\mathcal{A}}/{\mathcal{N}}$ forment des $K$-espaces de dimension finie. On a plus précisément, pour tout objet $A$: $$\dim_K ({\mathcal{A}}/{\mathcal{N}})(A,A)\leq 
(\dim A )^2.$$ $b)$ En fait ${\mathcal{R}}\subset
{\mathcal{N}}$, et ${\mathcal{A}}/{\mathcal{N}}$ est semi-simple.
:::

$a)$ Comme ${\mathcal{A}}$ est $K$-linéaire, on se ramène au cas des endomorphismes. Choisissons $n$ endomorphismes $f_1,\dots, f_n$ dont les images dans

${\mathcal{A}}(A,A)/{\mathcal{N}}(A,A)$ sont linéairement indépendantes. Il s'agit de voir que $n\leq
(\dim\,A)^2=
\dim\,A^\vee\bullet A$. Au lemme [\[Ldim\]](#Ldim){reference-type="ref" reference="Ldim"}, on a vu que les $f_1,\dots, f_n$ donnent lieu à un facteur direct ${{\bf 1}}^n$ dans $A^\vee\bullet
A$ dans la catégorie monoı̈dale pseudo-abélienne ${\mathcal{A}}/{\mathcal{N}}$. Tout supplémentaire sera de dimension un entier naturel par hypothèse, d'où l'inégalité voulue.

$b)$: comme dans la proposition précédente, mais en invoquant [\[nil, tr\]](#nil, tr){reference-type="ref" reference="nil, tr"} au lieu de [\[a la bru\]](#a la bru){reference-type="ref" reference="a la bru"}.$\square$

## Radical, traces, semi-simplicité. Trois théorèmes de structure {#rtss}

 

Comme dans le sous-paragraphe précédent, on suppose que *$K$ est un corps, et que ${\mathcal{A}}$ est une catégorie $K$-linéaire monoı̈dale symétrique rigide, avec $End({\bf 1})=K$*.

::: thm
[]{#wedtr label="wedtr"} On suppose $K$ de caractéristique nulle et ${\mathcal{A}}$ munie d'un foncteur monoı̈dal symétrique fidèle $H:{\mathcal{A}}\to
L$-$Modf$, où $L$ est une $K$-algèbre commutative semi-simple. Alors ${\mathcal{A}}$ est de Wedderburn et $H$ a les propriétés énumérées dans le corollaire [\[c6\]](#c6){reference-type="ref" reference="c6"} b).
:::

Comme dans la remarque [\[rem en fam\]](#rem en fam){reference-type="ref" reference="rem en fam"}, on se ramène au cas où $L$ est un corps. D'après le corollaire [\[c6\]](#c6){reference-type="ref" reference="c6"}, il suffit alors de vérifier que, pour tout $a\in
{\mathcal{A}}(A,A)$, le polynôme caractéristique de $H(a)$ est à coefficients dans $K$. Or, comme $\operatorname{car}K=0$, ces coefficients s'expriment comme polynômes à coefficients rationnels en les $tr(H(a^i))$. Puisque $H$ est monoı̈dal symétrique, on a $tr(H(a^i))=H(tr(a^i))\in
H(End({\bf 1}))=K$. $\square$

Au vu de l'exemple [\[ex1\]](#ex1){reference-type="ref" reference="ex1"}, le point $a)$ de l'énoncé suivant peut être considéré comme une version abstraite des résultats de Jannsen [@jannsen] (*cf.* [@{ak(note)}]).

::: thm
[]{#absJannsen label="absJannsen"} a) On suppose qu'il existe un foncteur monoı̈dal symétrique $H$ de ${\mathcal{A}}$ vers une catégorie abélienne monoı̈dale symétrique ${\mathcal{V}}$, et un foncteur $\,G:{\mathcal{V}}\to L$-$Modf$ vérifiant $\,G({\bf 1})\neq 0$, où $L$ est une $K$-algèbre commutative semi-simple. Alors

::: thlist
${\mathcal{R}}\subset {\mathcal{N}}$,

${\mathcal{A}}/{\mathcal{N}}$ est semi-simple,

le seul idéal monoı̈dal ${\mathcal{I}}$ de ${\mathcal{A}}$ tel que ${\mathcal{A}}/{\mathcal{I}}$ soit semi-simple est ${\mathcal{I}}={\mathcal{N}}$.
:::

b\) Supposons de plus que $K$ soit de caractéristique nulle, que $G=Id$ et que $H$ soit fidèle. Alors

::: thlist
${\mathcal{R}}={\mathcal{N}}$,

${\mathcal{A}}$ est de Wedderburn,

${\mathcal{A}}$ est pseudo-abélienne si et seulement si ${\mathcal{A}}/{\mathcal{N}}$ est abélienne.
:::
:::

a\) (i) et (ii) suivent de la proposition [\[new p2\]](#new p2){reference-type="ref" reference="new p2"} b) et de la remarque [\[rmot\]](#rmot){reference-type="ref" reference="rmot"} 2); (iii), indiqué pour mémoire, a déjà été vu dans la proposition [\[new p1\]](#new p1){reference-type="ref" reference="new p1"} c).

b\) Pour (i), il faut voir que ${\mathcal{N}}\subset {\mathcal{R}}$. On remarque que, via $H$, la trace monoı̈dale $tr$ s'interprète comme une "vraie\" trace au sens de l'algèbre linéaire. Comme $K$ est supposé de caractéristique nulle, un endomorphisme d'un $L$-module de type fini dont toutes les puissances strictement positives sont de trace nulle est nilpotent, et on déduit de là que ${\mathcal{N}}(A,A)$ est un nil-idéal, donc contenu dans ${\mathcal{R}}(A,A)$, pour tout objet $A$ de ${\mathcal{A}}$. Le point (ii) découle du théorème précédent. Enfin, (iii) résulte de ceci et de la proposition [\[P3/2\]](#P3/2){reference-type="ref" reference="P3/2"} b). $\square$

::: rems
[]{#nouv rem label="nouv rem"} 1) Si ${\mathcal{A}}$ est tannakienne et que $K$ est de caractéristique nulle, on verra dans la proposition [\[c4\]](#c4){reference-type="ref" reference="c4"} que ${\mathcal{A}}/{\mathcal{R}}$ est encore tannakienne (neutre si ${\mathcal{A}}$ l'est). Par contre, on verra aussi que l'hypothèse de caractéristique nulle est nécessaire (contre-exemple [\[Carp\]](#Carp){reference-type="ref" reference="Carp"}, ou remarque [\[r1\]](#r1){reference-type="ref" reference="r1"} 1).

2\) Par ailleurs, il ne suffirait pas dans le théorème [\[absJannsen\]](#absJannsen){reference-type="ref" reference="absJannsen"} de supposer que $H$ est un foncteur fibre $\mathbf{Z}/2$-gradué, *cf.* contre-exemple [\[super\]](#super){reference-type="ref" reference="super"} ci-dessous.
:::

::: thm
[]{#nouveau label="nouveau"} Supposons $K$ de caractéristique nulle et ${\mathcal{A}}$ pseudo-abélienne. Considérons les propriétés suivantes:\
a) pour tout objet $A$ de ${\mathcal{A}}$, il existe un entier $\,n>0\,$ tel que $\Lambda^n A= 0$,\
b) ${\mathcal{A}}/{\mathcal{N}}$ est semi-simple, et pour tout objet $A$ de ${\mathcal{A}}$, ${\mathcal{N}}(A,A)$ est un idéal nilpotent,\
c) ${\mathcal{R}}={\mathcal{N}}$,\
d) ${\mathcal{A}}$ ne contient pas d'objet fantôme, *i.e.* d'objet non nul dont l'image dans ${\mathcal{A}}/{\mathcal{N}}$ est nulle,\
e) ${\mathcal{A}}$ est de Wedderburn,\
f) ${\mathcal{A}}/{\mathcal{N}}$ est tannakienne semi-simple.\
g) la dimension de tout objet de ${\mathcal{A}}$ est un entier naturel,\
Alors

::: thlist
$a)\Longrightarrow b) \Longrightarrow c) \Longrightarrow d) + e)$ et $a)\Longrightarrow f) + g)$,

sous $g)$, on a $a)\iff b)  \iff c)\iff 
d)$.
:::
:::

::: rems
1\) La propriété $a)$ présente l'avantage sur les suivantes d'être testable sur des "générateurs tensoriels\" de ${\mathcal{A}}$: soit $(A_\alpha)$ une famille d'objets $A_\alpha$ de ${\mathcal{A}}$ tels que tout objet de ${\mathcal{A}}$ soit isomorphe à un facteur direct d'une somme directe de $\bullet$-monômes en les $A_\alpha$; on peut montrer que $a)$ est vérifié dès que pour tout $\alpha$, il existe $n_\alpha$ tel que $\Lambda^{n_\alpha} A_\alpha= 0$.\
2) Les propriétés $a), f)$ et $g)$ dépendent du tressage, alors que $b), c), d)$ et $e)$ n'en dépendent pas.\
3) Nous verrons en [\[super\]](#super){reference-type="ref" reference="super"} que $g) 
+ e)$ ne suffit pas à impliquer ${\mathcal{R}}={\mathcal{N}}$).\
4) Les propriétés du théorème sont par exemple vérifiées dans le cas de la catégorie monoı̈dale des fibrés vectoriels sur une variété projective géométriquement connexe sur $K$.
:::

Séparons $b)$ en $b_1)$: ${\mathcal{A}}/{\mathcal{N}}$ est semi-simple, et $b_2)$: $\forall {\mathcal{A}}$, ${\mathcal{N}}(A,A)$ est un idéal nilpotent. Nous allons démontrer que $a)\Longrightarrow b_2)$, $b_1) 
+b_2)\Longrightarrow c)\Longrightarrow d)$, $a)\Longrightarrow g)\Longrightarrow b_1)$, $b_1)+b_2)+c)\Longrightarrow e)$, $a)+ 
b_1)+b_2)\Longrightarrow f)$ et $d)+ g) \Longrightarrow a)$.

$a)\Longrightarrow b_1)$ suit de la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"} i).

$b_1)+b_2)\Longrightarrow c)$: l'inclusion ${\mathcal{R}}
\supset {\mathcal{N}}$ vient grâce au fait que le radical d'une $K$-algèbre contient tout nilidéal. L'inclusion opposée de la semi-simplicité de ${\mathcal{A}}/{\mathcal{N}}$ ([\[L1\]](#L1){reference-type="ref" reference="L1"}).

$c)\Longrightarrow d)$: en effet, la projection ${\mathcal{A}}\to {\mathcal{A}}/{\mathcal{R}}$ étant conservative, elle ne peut envoyer un objet non nul sur un objet nul.

$a)\Longrightarrow g)$: cela résulte de la proposition [\[nouvelle\]](#nouvelle){reference-type="ref" reference="nouvelle"} ii).

$b_1)+b_2)+c)\Longrightarrow
e)$: immédiat.

Il reste à montrer que $a)+ b_1)+b_2)\Longrightarrow f)$. Par $b_2)$, ${\mathcal{A}}/{\mathcal{N}}$ est pseudo-abélienne tout comme ${\mathcal{A}}$ (lemme [\[idemp\]](#idemp){reference-type="ref" reference="idemp"}). Par $b_1)$, elle est donc abélienne (*cf.* [\[A.P4\]](#A.P4){reference-type="ref" reference="A.P4"}). Comme elle vérifie aussi $a)$, le théorème de Deligne [@de 7.1] montre qu'elle est tannakienne.

$g)\Longrightarrow b)$: cela résulte de la proposition [\[new
p5/2\]](#new
p5/2){reference-type="ref" reference="new
p5/2"}.

$d)+ g) \Longrightarrow a)$: Soit $A$ un objet de dimension $d$. Notons $\bar A$ son image dans ${\mathcal{A}}/{\mathcal{N}}$ et posons $B:=\Lambda^{d+1}A$. Montrons que $B=0$. Par $d)$, il suffit de montrer que son image $\bar B$ dans ${\mathcal{A}}/{\mathcal{N}}$, qui n'est autre que $\Lambda^{d+1}\bar A$, est nulle. Notons que $\bar B$ est de dimension $\binom{d}{d+1}=0$. Par $g)$, et d'après [\[dim 0 ou 1\]](#dim 0 ou 1){reference-type="ref" reference="dim 0 ou 1"}, on a bien $\bar B=0$ puisque ${\mathcal{A}}$ est pseudo-abélienne. $\square$

## Variante $\mathbf{Z}/2$-graduée {#Z/2}

En théorie des motifs, la catégorie monoı̈dale des motifs purs modulo l'équivalence numérique est parfois appelée la "fausse\" catégorie des motifs. La raison en est que cette catégorie ne peut pas être tannakienne car la dimension d'un objet $M$ est un entier éventuellement négatif: si $H$ est une cohomologie de Weil et si $\tilde M$ est un relèvement de $M$ à la catégorie des motifs modulo l'équivalence $H$-homologique, alors $\dim M = \dim \tilde M
=\sum_{i\in \mathbf{Z}} (-1)^i H^i(M)$. En particulier, la condition g) du théorème [\[nouveau\]](#nouveau){reference-type="ref" reference="nouveau"} ne s'applique pas dans ce contexte.

Pour corriger ce défaut, on fait la conjecture standard que les projecteurs de Künneth de tout motif $M$ (relatifs à $H$) sont algébriques, ce qui permet de modifier la contrainte de commutativité de façon à obtenir la formule $\dim M =\sum_{i\in
\mathbf{Z}} H^i(M)\ge 0$. Pour y parvenir, il suffit en fait que la somme des projecteurs de Künneth pairs (ou impairs, de manière équivalente), soit algébrique.

Faute de savoir démontrer cette conjecture standard en général, on peut se limiter à la sous-catégorie pleine formée des motifs $M$ pour lesquelles elle est vraie: c'est le point de vue adopté dans [@{ak(note)}]. (C'est une sous-catégorie monoı̈dale qui contient au moins les motifs attachés aux courbes, aux surfaces et aux variétés abéliennes, et qui contient tous les motifs si le corps de base est un corps fini.) Le formalisme de la modification de la contrainte de commutativité est abstrait dans la proposition suivante:

::: prop
[]{#new p4 label="new p4"} Supposons $K$ de caractéristique nulle, et soit $L$ une $K$-algèbre semi-simple commutative. Supposons ${\mathcal{A}}$ munie d'un foncteur monoı̈dal symétrique fidèle $H$ vers la catégorie monoı̈dale symétrique $Modf_L^\pm$ des $L$-modules de type fini $\mathbf{Z}/2$-gradués munie de la règle de Koszul. Considérons, pour tout $A\in {\mathcal{A}}$, la projection $p^+_A\in End(H(A))$ sur le facteur $H^+(A)$. Soit ${\mathcal{A}}^\pm$ la sous-catégorie pleine de ${\mathcal{A}}$ formée des objets $A$ tels que $p^+_A= H(\pi^+_A)$ pour un $\pi^+_A\in {\mathcal{A}}(A,A)$. On note ${\mathcal{R}}^\pm,
{\mathcal{N}}^\pm$ la restriction de ${\mathcal{R}}, {\mathcal{N}}$ à ${\mathcal{A}}^\pm$. Alors

::: thlist
${\mathcal{A}}^\pm$ est une sous-catégorie $K$-linéaire monoı̈dale de ${\mathcal{A}}$, stable par facteurs directs et rigide.

Il existe sur ${\mathcal{A}}^\pm$ une contrainte de commutativité telle que le foncteur monoı̈dal composé $${\mathcal{A}}^\pm\to 
{\mathcal{A}}\stackrel{H}{\to} Vec_L^\pm\to Vec_L,$$ où le dernier foncteur est le foncteur d'oubli, soit symétrique.
:::

En particulier, ${\mathcal{A}}^\pm$ est de Wedderburn, ${\mathcal{R}}^\pm={\mathcal{N}}^\pm$, et ${\mathcal{A}}^\pm/{\mathcal{N}}^\pm$ est semi-simple.
:::

Vérification immédiate pour (i): si $A,B\in 
{\mathcal{A}}^\pm$, $\pi^+_{A\bullet B}$ est donné par $\pi^+_A\bullet\pi^+_B
+(1-\pi^+_A)\bullet(1-\pi^+_B)$. De même, si $A^\vee$ est le dual de $A\in
{\mathcal{A}}^\pm$, $\pi^+_{A^\vee}$ est donné par le transposé $(\pi^+_A)^t$. Pour $A\in {\mathcal{A}}^\pm$, posons $\varepsilon_A=2\pi^+_A-1$: on a $\varepsilon_A^2=1$. Pour $A,B\in 
{\mathcal{A}}$, soit $R_{A,B}:A\bullet B\to B\bullet A$ la contrainte de commutativité. Si $A,B\in {\mathcal{A}}^\pm$, posons $$\label{kunneth}
R'_{A,B}=R_{A,B}\varepsilon_A\bullet\varepsilon_B.$$

On voit tout de suite que $R'$ est une nouvelle contrainte de commutativité, vérifiant la condition (ii): pour la naturalité, cela résulte du fait que $\pi_A^+$, donc $\varepsilon_A$, est naturel en $A$, et la vérification des identités de tressage symétrique est immédiate. La dernière affirmation résulte du théorème [\[absJannsen\]](#absJannsen){reference-type="ref" reference="absJannsen"}.$\square$

Si l'on est dans la situation de la proposition [\[new p4\]](#new p4){reference-type="ref" reference="new p4"}, on peut appliquer le théorème [\[nouveau\]](#nouveau){reference-type="ref" reference="nouveau"} à ${\mathcal{A}}^\pm$ munie de la nouvelle contrainte de commutativité. En exprimant tout en termes de l'ancienne contrainte, cela revient à utiliser au lieu des puissances extérieures les "super-puissances extérieures\" d'un objet $A=A_+\oplus A_-$ de ${\mathcal{A}}^\pm$, définies par $$s\Lambda^n A= \bigoplus_{i+j=n}\Lambda^i A_+\bullet 
\mathbf{S}^j A_-.$$

Nous reviendrons sur ces super-puissances extérieures dans la section suivante [2](#kimura){reference-type="ref" reference="kimura"}, où nous démontrerons que la catégorie ${\mathcal{A}}^\pm$ de la proposition [\[new p4\]](#new p4){reference-type="ref" reference="new p4"} est *intrinsèque* (*i.e.* indépendante de $H$).

# Le Pair et l'Impair {#kimura}

La catégorie ${\mathcal{A}}$ est toujours $K$-linéaire monoı̈dale symétrique rigide, qu'on suppose en outre *pseudo-abélienne*; $K$ est un corps de caractéristique nulle.

[^1]: Dans [@bru2] cet idéal apparaı̂t, dans le cadre plus général (tressage non nécessairement symétrique) des *tortils* ou *catégories enrubannées*, sous le nom d'idéal des morphismes négligeables.
