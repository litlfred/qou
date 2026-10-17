---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-007-101-trois-contre-exemples
section_title: "Trois contre-exemples"
section_number: 10.1
pages: 55-58
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.885
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
[]{#3contrex label="3contrex"} Voici trois exemples de catégories monoı̈dales $K$-linéaires symétriques et rigides, vérifiant $End({\bf 1})=K$, abéliennes, de Wedderburn, mais *dont le radical n'est pas un idéal monoı̈dal*.

::: contrex
[]{#super label="super"}

Partons de $D=K[\varepsilon],\varepsilon^2=0$, vue comme super-algèbre ($\varepsilon$ placé en degré impair). On considère le super-groupe algébrique $GL(1\vert 1, D)$. Son groupe de points est donné par les matrices $2\times 2$ inversibles du type $$\begin{pmatrix} a &\varepsilon b \\
\varepsilon c & d
\end{pmatrix}, a,b,c,d \in K, a\neq 0, d\neq 0$$ *cf.* [@qfs ch. 1]. On prend pour ${\mathcal{A}}$ la catégorie des représentations de $GL(1\vert 1, D)$. C'est une sous-catégorie $K$-linéaire monoı̈dale rigide non pleine de la catégorie monoı̈dale symétrique rigide des super-$D$-modules.

La représentation standard de $GL(1\vert 1, D)$ est le super-$D$-module $D^{1\vert 1}=D\times \Pi D$ (où $\Pi$ est le foncteur changement de parité). Un endomorphisme de $D^{1\vert 1}$ est donné par une matrice $\begin{pmatrix} a &\varepsilon b \\
\varepsilon c & d
\end{pmatrix}$ comme ci-dessus; s'il commute à tout élément $\begin{pmatrix} a'
&\varepsilon b' \\
\varepsilon c' & d'
\end{pmatrix}\in GL(1\vert 1, D)$, on trouve que $ba'+db'=ab'+bd',
ca'+dc'=ac'+cd'$ pour tous $a',b',c',d' \in K, a'\neq 0, d'\neq 0$, d'où, $b=c=0,a=d$. Donc ${\mathcal{A}}(D^{1\vert
1},D^{1\vert 1})\cong K$ est réduit aux homothéties, et son radical est nul.

La trace monoı̈dale de $\begin{pmatrix} a &\varepsilon b \\
\varepsilon c & d
\end{pmatrix}$ est la supertrace $a-d$. Elle s'annule donc pour toute homothétie, ce qui montre que ${\mathcal{N}}(D^{1\vert 1},D^{1\vert 1})={\mathcal{A}}(D^{1\vert 1},D^{1\vert 1})$. En d'autres termes, $D^{1\vert 1}$ est un objet "fantôme\": il s'envoie sur l'objet nul dans ${\mathcal{A}}/{\mathcal{N}}$.

On a donc $0\subset {\mathcal{R}}\subset {\mathcal{N}}\subset {\mathcal{A}}$ et toutes les inclusions sont strictes (*cf.* théorème [\[absJannsen\]](#absJannsen){reference-type="ref" reference="absJannsen"} et corollaire [\[c2\]](#c2){reference-type="ref" reference="c2"}); en particulier ${\mathcal{A}}$ n'est ni semi-simple, ni de Kimura. Elle est en revanche de Wedderburn (finitude des espaces d'homomorphismes), et la dimension de tout objet est un entier naturel (${\mathcal{A}}/{\mathcal{N}}\sim Vec_K$).
:::

::: contrex
[]{#Carp label="Carp"} $K$ est maintenant supposé de caractéristique $p>0$, et on prend pour ${\mathcal{A}}= Rep_K(GL_p)$ la catégorie des représentations de dimension finie de $GL_p$. Soit $V$ la représentation standard. On a ${\mathcal{A}}(V,V)\allowbreak=K$, ${\mathcal{R}}(V,V)=0$ et, comme toute homothétie de $V$ est de trace nulle, ${\mathcal{N}}(V,V)=K$. Ici encore, $V$ est un objet "fantôme\", *i.e.* nul modulo ${\mathcal{N}}$.
:::

::: contrex
[]{#Car3 label="Car3"} $K$ est maintenant supposé de caractéristique $3$, et on prend ${\mathcal{A}}= Rep_K(SL_2)$. Soit $V$ la représentation standard. On a $V^{\otimes 2}\cong {\bf 1}\oplus S^2V$, et on vérifie comme ci-dessus que $S^2V$ est un objet "fantôme\". On en déduit que la catégorie monoı̈dale symétrique rigide ${\mathcal{A}}/{\mathcal{N}}$ est équivalente à celle des $K$-super-espaces de dimension finie.
:::

## Complément: l'algèbre commutative $HH_0({\mathcal{A}})$ {#h0}

Soient ${\mathcal{A}}$ une petite $K$-catégorie et ${\mathcal{I}}$ un idéal de ${\mathcal{A}}$.

On note $H_0({\mathcal{A}},{\mathcal{I}})$ le $K$-module[^1] engendré par les classes d'isomorphismes de couples $(A,h)$ où $A$ est un objet de ${\mathcal{A}}$ et $h\in {\mathcal{I}}(A,A)$, quotienté par les relations suivantes:

-   l'application canonique ${\mathcal{I}}(A,A)\to H_0({\mathcal{A}},{\mathcal{I}})$ est $K$-linéaire,

-   pour tout $f\in {\mathcal{I}}(A,B)$ et tout $g\in {\mathcal{A}}(B,A)$, les classes de $(A,gf)$ et $(B,fg)$ coı̈ncident dans $H_0({\mathcal{A}},{\mathcal{I}})$.

Cette construction est fonctorielle en $({\mathcal{A}},{\mathcal{I}})$.

On note $[A,h]$ la classe de $(A,h)$. Notons que si ${\mathcal{A}}$ est $K$-linéaire, et si $A,A'$ sont deux objets, on a $[A,1_A= pi] =
[A\oplus A', ip]$ avec les notations $i,p$ de [\[eqbiprod\]](#eqbiprod){reference-type="eqref" reference="eqbiprod"}.

On note encore $H_0({\mathcal{A}},{\mathcal{A}})=HH_0({\mathcal{A}})$. Ce $K$-module est le réceptacle universel des traces abstraites, *i.e.* des applications $t: A\to M$ vérifiant $t(fg)=t(gf)$ pour tout couple de morphismes allant en directions opposées. Il apparaı̂t en théorie des nœuds, *cf.* [@vogel 2], dans le cadre monoı̈dal comme ci-dessous.

Supposons maintenant ${\mathcal{A}}$ monoı̈dale. Par fonctorialité, la loi $\bullet$ induit sur $HH_0({\mathcal{A}})$ une structure de $K$-algèbre, commutative si ${\mathcal{A}}$ est munie d'un tressage symétrique[^2]. Si ${\mathcal{I}}$ est monoı̈dal, $H_0({\mathcal{A}},{\mathcal{I}})$ est un idéal de $HH_0({\mathcal{A}})$, et le quotient $HH_0({\mathcal{A}})/H_0({\mathcal{A}},{\mathcal{I}})$ s'identifie à $HH_0({\mathcal{A}}/{\mathcal{I}})$. Par exemple, $H_0({\mathcal{A}},\sqrt[\otimes]{0})$ est un nil-idéal de $HH_0({\mathcal{A}})$ (par définition, tout élément de $\sqrt[\otimes]{0}({\mathcal{A}},{\mathcal{A}})$ est $\bullet$-nilpotent).

Les traces abstraites à valeurs dans une $K$-algèbre commutative $R$ vérifiant de plus $t(f\bullet g)=t(f)t(g)$ pour tout couple d'endomorphismes $(f,g)$ sont en bijection avec les $R$-points de $\operatorname{Spec}\, HH_0({\mathcal{A}})$. Si ${\mathcal{A}}$ est rigide, la transposition définit une involution de $HH_0({\mathcal{A}})$; la trace monoı̈dale $tr$ définit un *$K$-point canonique* de $\operatorname{Spec}HH_0({\mathcal{A}})$ ou encore une *augmentation* de la $K$-algèbre $HH_0({\mathcal{A}})$, compatible avec l'involution.

Supposons de plus que ${\mathcal{A}}$ vérifie les hypothèses du théorème [\[absJannsen\]](#absJannsen){reference-type="ref" reference="absJannsen"}. On a donc ${\mathcal{R}}={\mathcal{N}}$. Posons $\bar{\mathcal{A}}= {\mathcal{A}}/{\mathcal{R}}= {\mathcal{A}}/{\mathcal{N}}$. Le raisonnement de la démonstration de la proposition [\[a la bru\]](#a la bru){reference-type="ref" reference="a la bru"} montre que toute trace abstraite s'annule sur tout endomorphisme nilpotent, donc sur les ${\mathcal{R}}(A,A)$. Donc le $K$-dual de $HH_0({\mathcal{A}})$ coı̈ncide avec le $K$-dual de $HH_0(\bar{\mathcal{A}})$, et finalement $HH_0({\mathcal{A}})\cong
HH_0(\bar{\mathcal{A}})$.

::: ex
[]{#hh0 label="hh0"} Supposons ${\mathcal{A}}$ tannakienne semi-simple neutre sur un corps $K$ algébriquement clos de caractéristique nulle, de sorte que ${\mathcal{A}}$ est équivalente à la catégorie des $K$-représentations de dimension finie d'un $K$-groupe pro-réductif $G$.

Par linéarité, les éléments $HH_0({\mathcal{A}})$ sont des $K$-combinaisons d'objets $[A,h]$ avec $A$ simple; par le lemme de Schur, on peut même supposer $h=1_A$. On en déduit que $$HH_0({\mathcal{A}})\cong R_K(G)\otimes_\mathbf{Z}K,$$ où $R_K(G)$ désigne l'anneau des représentations de $G$.
:::

 

::: center
**III. Sections**
:::

L'objectif de cette partie est d'établir des analogues catégoriques du théorème de Wedderburn, qui affirme l'existence de sections pour la projection d'une algèbre de dimension finie sur un corps parfait vers son quotient par le radical. On établit de tels analogues tant dans le cadre linéaire général que dans le cadre monoı̈dal ou monoı̈dal tressé.

[^1]: L'explication de cette notation apparaîtra au paragraphe suivant.

[^2]: Là encore, il suffirait que ${\mathcal{A}}$ soit munie d'une structure de tortil, la symétrie du tressage n'étant pas vraiment nécessaire.
