---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-001-13-algebres-a-plusieurs-objets
section_title: "Alg`ebres `a plusieurs objets"
section_number: 1.3
pages: 9-13
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.904
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
[]{#1.3 label="1.3"} Dans cet article, nous adoptons le point de vue de B. Mitchell [@mitchell] et considérons les $K$-catégories comme des "$K$-algèbres (associatives) à plusieurs objets\".

Suivant ce point de vue, un idéal (bilatère) ${\mathcal{I}}$ d'une $K$-catégorie ${\mathcal{A}}$ est la donnée, pour tout couple d'objets $(A,B)$, d'un sous-$K$-module de ${\mathcal{I}}(A,B)\allowbreak \subset
{\mathcal{A}}(A,B)$ tel que pour tout couple de morphismes $(f \in {\mathcal{A}}(A,A'), g \in
{\mathcal{A}}(B,B'))$, on ait $g{\mathcal{I}}(A',B)f \subset {\mathcal{I}}(A,B')$.

On peut alors former la $K$-catégorie quotient ${\mathcal{A}}/{\mathcal{I}}$ (qui a les mêmes objets que ${\mathcal{A}}$). Si $A=\oplus A_i, B= \oplus B_j$, alors ${\mathcal{I}}(A,B)$ s'identifie canoniquement à $\oplus_{i,j} {\mathcal{I}}(A_i,B_j)$.

::: ex
[]{#ex1.3.1 label="ex1.3.1"} Si $X$ est un ensemble d'objets de ${\mathcal{A}}$, stable par biproduit, la famille d'ensembles $${\mathcal{I}}_X(A,B)=\{f\in {\mathcal{A}}(A,B)\mid f \text{ se factorise \`a travers un objet
de } X\}$$ est un idéal de ${\mathcal{A}}$. Le quotient ${\mathcal{A}}/{\mathcal{I}}$ est souvent noté ${\mathcal{A}}/X$.
:::

On a une notion évidente d'idéal produit (*resp.* somme, *resp.* intersection) de deux idéaux ${\mathcal{I}}\cdot{\mathcal{J}}$ (*resp.* ${\mathcal{I}}+{\mathcal{J}}$, *resp.* ${\mathcal{I}}\cap {\mathcal{J}}$). On prendra toutefois garde de ne pas confondre les idéaux $({\mathcal{I}}\cdot{\mathcal{J}})(A,A)=\{\sum f\circ
g,B \in Ob{\mathcal{A}}, f\in {\mathcal{A}}(B,A),
g\in {\mathcal{A}}(A,B)\}$ et ${\mathcal{I}}(A,A)\cdot{\mathcal{J}}(A,A)$ de la $K$-algèbre ${\mathcal{A}}(A,A)$.

Le noyau d'un $K$-foncteur est l'idéal $\operatorname{Ker}T$ de ${\mathcal{A}}$ formé des morphismes que $T$ annule; $T$ induit une $K$-équivalence entre le quotient ${\mathcal{A}}/\operatorname{Ker}T$ et une sous-catégorie non pleine de ${\mathcal{B}}$.

::: lemme
[]{#l1 label="l1"} Supposons ${\mathcal{A}}$ $K$-linéaire. Soient ${\mathcal{I}},{\mathcal{J}}$ deux idéaux de ${\mathcal{A}}$. Supposons que ${\mathcal{I}}(A,A)\subset {\mathcal{J}}(A,A)$ pour tout objet $A$ de ${\mathcal{A}}$. Alors ${\mathcal{I}}\subset {\mathcal{J}}$.
:::

Soient $A,B\in {\mathcal{A}}$. On a ${\mathcal{A}}(A\oplus B,A\oplus B)={\mathcal{A}}(A,A)\oplus
{\mathcal{A}}(A,B)\oplus
{\mathcal{A}}(B,A)\oplus {\mathcal{A}}(B,B)$. En utilisant les injections de $A$ et $B$ dans $A\oplus B$ et les projections de $A\oplus B$ sur $A$ et $B$, on voit que ${\mathcal{A}}(A,B)\cap {\mathcal{I}}(A\oplus B,A\oplus B)={\mathcal{I}}(A,B)$, et de même pour ${\mathcal{J}}$. Le lemme en résulte.$\square$

Notons $K$-$Mod$ la catégorie $K$-linéaire des $K$-modules.

::: defn
[]{#D2 1/2 label="D2 1/2"} Un *${\mathcal{A}}$-module* (à gauche) est un $K$-foncteur $M:{\mathcal{A}}\to
K$-$Mod$.\
Il est dit *fini* si tous les $M(A)$ sont de type fini sur $K$.
:::

Les ${\mathcal{A}}$-modules (*resp.* les ${\mathcal{A}}$-modules finis) forment une catégorie abélienne $K$-linéaire, notée ${\mathcal{A}}\hbox{--}Mod$ [^1] (*resp.* ${\mathcal{A}}\hbox{--}Modf$). Tout $K$-foncteur $F:{\mathcal{A}}\to {\mathcal{B}}$ induit par composition des $K$-foncteurs en sens inverse $F^\ast:{\mathcal{B}}\hbox{--}Mod\to {\mathcal{A}}\hbox{--}Mod$ et $F^\ast:{\mathcal{B}}\hbox{--}Modf\to
{\mathcal{A}}\hbox{--}Modf$.

Nous aurons aussi besoin de la notion suivante:

::: defn
[]{#d1 label="d1"} Soit $A\in {\mathcal{A}}$. Un *$A$-idéal à gauche* de ${\mathcal{A}}$ est la donnée, pour tout $B\in {\mathcal{A}}$, d'un sous-$K$-module ${\mathcal{I}}(B)$ de ${\mathcal{A}}(A,B)$, telle que la famille des ${\mathcal{I}}(B)$ soit stable par composition à gauche.
:::

On a une notion évidente d'idéal à gauche somme (*resp.* intersection) de deux idéaux à gauche.

Pour tout $A\in {\mathcal{A}}$, notons ${}_A {\mathcal{A}}$ le foncteur $B\mapsto
{\mathcal{A}}(A,B)$. Ceci définit un $K$-foncteur contravariant $$\begin{aligned}
Y_{\mathcal{A}}:{\mathcal{A}}^{\rm o}&\to 
{\mathcal{A}}\hbox{--}Mod\\
A&\mapsto  {}_A {\mathcal{A}}.
\end{aligned}$$

Pour que l'image de $Y_{\mathcal{A}}$ soit contenue dans ${\mathcal{A}}\hbox{--}Modf$, il faut et il suffit que ${\mathcal{A}}(A,B)$ soit un $K$-module de type fini pour tous $A,B\in {\mathcal{A}}$. De ce point de vue, un $A$-idéal à gauche n'est autre qu'un sous-objet de ${}_A {\mathcal{A}}$.

On a dualement les catégories $Mod\hbox{--}{\mathcal{A}}$ et $Modf\hbox{--}{\mathcal{A}}$ des ${\mathcal{A}}$-modules à droite[^2] et des ${\mathcal{A}}$-modules à droite finis (contravariants), ainsi que les $A$-idéaux à droite. On a le $K$-foncteur covariant $$\begin{aligned}
{}_{\mathcal{A}}Y:{\mathcal{A}}&\to Mod\hbox{--}{\mathcal{A}}\\
A&\mapsto   {\mathcal{A}}{}_A:B\mapsto {\mathcal{A}}(B,A).
\end{aligned}$$

::: defn
[]{#d1.1 label="d1.1"} Un objet $X$ d'une catégorie ${\mathcal{C}}$ est *compact* si le foncteur $Y\mapsto {\mathcal{C}}(X,Y)$ commute aux limites inductives quelconques (représentables dans ${\mathcal{C}}$).
:::

Le résultat suivant est bien connu (par exemple [@maclane III.2 et III.7], [@street]):

::: prop
[]{#p1.1 label="p1.1"} a) Pour tout $A\in {\mathcal{A}}$ et tout $M\in
Mod\hbox{--}{\mathcal{A}}$, l'homomorphisme $$\begin{aligned}
Mod\hbox{--}{\mathcal{A}}({\mathcal{A}}{}_A,M)&\to M(A)\\
f&\mapsto f(1_A)
\end{aligned}$$ est bijectif.\
b) Le foncteur ${}_{\mathcal{A}}Y$ est pleinement fidèle. Un module appartenant à son image essentielle est dit *représentable*.\
c) La catégorie $Mod\hbox{--}{\mathcal{A}}$ est stable par limites inductives et projectives quelconques.\
d) Tout objet $M$ de $Mod\hbox{--}{\mathcal{A}}$ est limite inductive d'objets représentables.\
e) Si ${\mathcal{A}}$ est stable par limites inductives quelconques, le foncteur ${}_{\mathcal{A}}Y$ admet un adjoint à gauche $\varinjlim:Mod\hbox{--}{\mathcal{A}}\to {\mathcal{A}}$, qui en est aussi un inverse à gauche.\
f) Pour tout objet $M$ de $Mod\hbox{--}{\mathcal{A}}$, les conditions suivantes sont équivalentes:

::: thlist
$M$ est compact.

Pour tout système inductif $(N_i)_{i\in I}$ d'objets de $Mod\hbox{--}{\mathcal{A}}$ indexé par une petite catégorie $I$, l'homomorphisme $$\varinjlim Mod\hbox{--}{\mathcal{A}}(M,N_i)\to Mod\hbox{--}{\mathcal{A}}(M,\varinjlim N_i)$$ est surjectif.

$M$ est facteur direct d'une somme directe d'objets représentables[^3].
:::

De plus, $M$ est projectif.
:::

Rappelons rapidement la démonstration, pour la commodité du lecteur. Dans a) (lemme de Yoneda enrichi), l'application inverse est donnée par $m\mapsto 
(f\mapsto M(f)m)$. b) en résulte immédiatement. c) est clair, puisque $K\hbox{--}Mod$ a la même propriété: les limites se calculent "argument par argument\".

Pour voir d), on considère la catégorie ${\mathcal{C}}$ dont les objets sont les couples $(A,x)$ avec $A\in {\mathcal{A}}$ et $x\in M(A)$, un morphisme $(A,x)\to (B,y)$ étant un morphisme $f\in
{\mathcal{A}}(A,B)$ tel que $M(f)(x)=y$: par a), le système inductif $$\begin{aligned}
T:{\mathcal{C}}&\to Mod\hbox{--}{\mathcal{A}}\\
(A,x)&\mapsto {\mathcal{A}}_A
\end{aligned}$$ s'envoie vers $M$ et on vérifie que $\varinjlim T\to M$ est un isomorphisme.

On déduit e) de d) comme suit: soit $M\in Mod\hbox{--}{\mathcal{A}}$. Écrivons $M=\varinjlim{\mathcal{A}}_{A_i}$: on définit alors $\varinjlim M=\varinjlim A_i$. On utilise b) pour montrer que ce foncteur est bien défini et pour vérifier sa propriété d'adjonction.

On déduit également f) de a) et d) comme suit: (iii) $\Longrightarrow$ (i) résulte immédiatement de a). (i) $\Longrightarrow$ (ii) est évident. Pour voir que (ii) $\Longrightarrow$ (iii), soit $M$ un objet vérifiant (ii): écrivons $M=\varinjlim_{i\in I} {\mathcal{A}}_{A_i}$, où $I$ est une petite catégorie. Il existe alors un ensemble fini $I_0$ d'objets de $I$ tel que l'identité: $M\to M$ se factorise à travers $\displaystyle\bigoplus_{i\in I_0}{\mathcal{A}}_{A_i}$.

Enfin, la dernière assertion résulte du lemme [\[lA.2\]](#lA.2){reference-type="ref" reference="lA.2"}.$\square$

::: rems
 []{#r1.1 label="r1.1"}

-   On laisse au lecteur le soin d'obtenir les énoncés correspondants pour ${\mathcal{A}}\hbox{--}Mod$, en remplaçant ${\mathcal{A}}$ par ${\mathcal{A}}^{\rm o}$.

-   On dit qu'un objet $M\in Mod\hbox{--}{\mathcal{A}}$ est *de présentation finie* si le foncteur ${}_M Mod\hbox{--}{\mathcal{A}}$ commute aux limites inductives *filtrantes*. (Comme il est additif, il commute alors aussi aux sommes directes quelconques.) On se gardera de confondre cette notion avec celle d'objet compact, qui est plus restrictive. On peut montrer que $M$ est de présentation finie si et seulement s'il s'insère dans une suite exacte $$P_1\to P_0\to M\to 0$$ où $P_1$ et $P_0$ sont compacts.
:::

Voici une réciproque de la proposition [\[p1.1\]](#p1.1){reference-type="ref" reference="p1.1"}:

::: prop
Soit ${\mathcal{A}}$ une catégorie abélienne stable par limites inductives quelconques. Notons ${\mathcal{A}}_{\operatorname{comp}}$ la sous-catégorie pleine de ses objets compacts. Supposons ${\mathcal{A}}_{\operatorname{comp}}$ dense dans ${\mathcal{A}}$, c'est-à-dire que tout objet de ${\mathcal{A}}$ est limite inductive d'objets de ${\mathcal{A}}_{\operatorname{comp}}$. Alors le foncteur "de Yoneda\" $$\begin{aligned}
{\mathcal{A}}&\to Mod\hbox{--}{\mathcal{A}}_{\operatorname{comp}}\\
A&\mapsto ({\mathcal{A}}_A:C\mapsto {\mathcal{A}}(C,A))
\end{aligned}$$ est une équivalence de catégories.
:::

La pleine fidélité se démontre comme dans le lemme de Yoneda enrichi: Si $A\in {\mathcal{A}}$ est limite inductive d'objets compacts $C_i$ et $M\in Mod\hbox{--}{\mathcal{A}}_{\operatorname{comp}}$, l'homomorphisme $$\begin{aligned}
Mod\hbox{--}{\mathcal{A}}_{\operatorname{comp}}({\mathcal{A}}_A,M)&\to \varprojlim M(C_i)\\
f&\mapsto (f(\iota_i))
\end{aligned}$$ où $\iota_i$ est le morphisme $C_i\to A$, est un isomorphisme d'inverse $(m_i)\mapsto (g\mapsto M(g_i)m_i)$ pour $C\in {\mathcal{A}}_{\operatorname{comp}}$ et $g\in
{\mathcal{A}}(C,A)=\varinjlim{\mathcal{A}}(C,C_i)$ écrit sous la forme $\iota_i\circ g_i$ pour $i$ assez grand. On en déduit que, pour $A,B\in {\mathcal{A}}$, $$Mod\hbox{--}{\mathcal{A}}_{\operatorname{comp}}({\mathcal{A}}_A,{\mathcal{A}}_B)\stackrel{\sim}{\to} \varprojlim
{\mathcal{A}}_B(C_i)=\varprojlim{\mathcal{A}}(C_i,B)={\mathcal{A}}(A,B).$$

Pour l'essentielle surjectivité, on utilise le fait que ${\mathcal{A}}_{\operatorname{comp}}$ est dense dans $Mod\hbox{--}{\mathcal{A}}_{\operatorname{comp}}$ d'après la proposition 1.3.6 d).$\square$

La construction ${\mathcal{A}}\mapsto Y_{\mathcal{A}}$ *n'est pas* $2$-fonctorielle en ${\mathcal{A}}$. Par contre:

::: cor
[]{#morita label="morita"} Soit $F:{\mathcal{A}}\to
{\mathcal{B}}$ un $K$-foncteur. Alors $F^*:{\mathcal{B}}\hbox{--}Mod\to 
{\mathcal{A}}\hbox{--}Mod$ est une équivalence de catégories si et seulement si $F^{\oplus\natural}$ est une équivalence de catégories. On dit alors que $F$ est une *équivalence de Morita*.$\square$
:::

Cela résulte immédiatement de la proposition [\[p1.1\]](#p1.1){reference-type="ref" reference="p1.1"} f).$\square$

::: lemme
[]{#corresp label="corresp"} Soit $A\in {\mathcal{A}}$; notons encore $A$ son image dans ${\mathcal{A}}^\oplus$, ${\mathcal{A}}^\natural$ et ${\mathcal{A}}^{\oplus\natural}$. Alors\
a) Il y a bijection entre les $A$-idéaux à gauche dans ${\mathcal{A}}$, ${\mathcal{A}}^\oplus$, ${\mathcal{A}}^\natural$ et ${\mathcal{A}}^{\oplus\natural}$.\
b) Il y a bijection entre les idéaux (bilatères) dans ${\mathcal{A}}$, ${\mathcal{A}}^\oplus$, ${\mathcal{A}}^\natural$ et ${\mathcal{A}}^{\oplus\natural}$.\
c) Pour tout idéal ${\mathcal{I}}$ de ${\mathcal{A}}$, notons ${\mathcal{I}}^\oplus$ l'idéal correspondant de ${\mathcal{A}}^\oplus$. Alors on a un isomorphisme canonique ${\mathcal{A}}^\oplus/{\mathcal{I}}^\oplus= ({\mathcal{A}}/{\mathcal{I}})^\oplus$.\
d) Pour tout idéal ${\mathcal{I}}$ de ${\mathcal{A}}$, notons ${\mathcal{I}}^\natural$ l'idéal correspondant de ${\mathcal{A}}^\natural$. Alors on a un foncteur canonique pleinement fidèle ${\mathcal{A}}^\natural/{\mathcal{I}}^\natural\to 
({\mathcal{A}}/{\mathcal{I}})^\natural$. C'est un isomorphisme si et seulement si les idempotents des algèbres d'endomorphismes $({\mathcal{A}}/{\mathcal{I}})(A,A)$ se relèvent en des idempotents des algèbres d'endomorphismes ${\mathcal{A}}(A,A)$.
:::

a): Cela résulte immédiatement de l'interprétation des $A$-idéaux à gauche comme étant les sous-modules du ${\mathcal{A}}$-module à gauche ${}_A{\mathcal{A}}:B\mapsto {\mathcal{A}}(A,B)$ et du fait que le carré [\[eq1\]](#eq1){reference-type="eqref" reference="eq1"} induit un carré d'équivalences de catégories (corollaire [\[morita\]](#morita){reference-type="ref" reference="morita"}): $$\begin{matrix}   \;&\;& 
{\mathcal{A}}^\oplus\hbox{--}Mod
&\;&\;\\
\;&\nearrow\;&\;&\searrow 
&\;\\

{\mathcal{A}}\hbox{--}Mod &\;&\;&\;& {\mathcal{A}}^{\oplus\natural}\hbox{--}Mod. 
\\

\;&\searrow\;&\;&\nearrow &\;\\
 
\;&\;&
{\mathcal{A}}^\natural\hbox{--}Mod &\;&\;
\end{matrix}$$ b): voir [@street prop. 2]

c\) est immédiat.

d): pour tout couple d'objets $(A,e), (A,e')$ de ${\mathcal{A}}^\natural$, on a $${\mathcal{A}}^\natural((A,e),(A',e'))=e'{\mathcal{A}}(A,A')e$$ et $${\mathcal{I}}^\natural((A,e) 
,(A',e'))=e'{\mathcal{I}}(A,A')e.$$

On a donc $${\mathcal{A}}^\natural/{\mathcal{I}}^\natural((A,e),(A',e'))= 
\bar
e'(({\mathcal{A}}/{\mathcal{I}})^\natural(A,A'))\bar
e=({\mathcal{A}}/{\mathcal{I}})^\natural((A,\bar 
e),(A',\bar e'))$$ où $\bar e,\bar e'$ désignent les images de $e$ et $e'$ modulo ${\mathcal{I}}$. Le foncteur $(A,e)\mapsto 
(A,\bar e)$ est donc pleinement fidèle. L'hypothèse de relèvement des idempotents équivaut à dire qu'il est bijectif sur les objets. $\square$

[^1]: Notation compatible à la précédente si l'on considère $K$ comme catégorie à un seul objet.

[^2]: C'est celle considérée par Street [@street].

[^3]: Si ${\mathcal{A}}$ est $K$-linéaire pseudo-abélienne, cette condition équivaut au fait que $M$ soit représentable.
