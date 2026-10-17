---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-008-11-cohomologie-de-hochschild-mitchell
section_title: "Cohomologie de Hochschild-Mitchell"
section_number: 11
pages: 58-59
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.913
---
[]{#hochschild label="hochschild"}[]{#s4 label="s4"}

## Produit tensoriel de $K$-catégories {#prodtens}

Ici, $K$ désigne de nouveau un anneau commutatif unitaire quelconque.

::: defn
[]{#D5 label="D5"} (*cf.* [@mitchell §11]). Soient ${\mathcal{A}},{\mathcal{B}}$ deux $K$-catégories. Le *produit tensoriel* de ${\mathcal{A}}$ par ${\mathcal{B}}$ est la $K$-catégorie ${\mathcal{A}}\boxtimes_K{\mathcal{B}}$ dont les objets sont les couples $(A,B)$ ($A\in {\mathcal{A}},
B\in
{\mathcal{B}}$), avec $$({\mathcal{A}}\boxtimes_K {\mathcal{B}})((A, B),(A', B'))={\mathcal{A}}(A,A')\otimes_K
{\mathcal{B}}(B,B').$$
:::

On a des isomorphismes canoniques $${\mathcal{A}}\boxtimes_K{\mathcal{B}}\cong
{\mathcal{B}}\boxtimes_K{\mathcal{A}},\quad({\mathcal{A}}\hbox{-}Mod)^{\mathcal{B}}\cong ({\mathcal{B}}\hbox{-}Mod)^{\mathcal{A}}
\cong
({\mathcal{A}}\boxtimes_K {\mathcal{B}})\hbox{-}Mod.$$

Par ailleurs, on note ${\mathcal{A}}^o$ la catégorie opposée de ${\mathcal{A}}$ et on pose ${{\mathcal{A}}}^e= {\mathcal{A}}^o  \boxtimes_K{\mathcal{A}}$. Les ${{\mathcal{A}}}^e$-modules (à gauche) sont parfois appelés ${\mathcal{A}}$-bimodules. Alors ${\mathcal{A}}$ définit de manière évidente un ${\mathcal{A}}$-bimodule (par la loi $(X,Y)\mapsto {\mathcal{A}}(X,Y)$) qu'on identifie à ${\mathcal{A}}$; un idéal (bilatère) de ${\mathcal{A}}$ (*cf.* §1) n'est autre qu'un sous-bimodule de ${\mathcal{A}}$.

::: lemme
[]{#L6 label="L6"} Supposons que $K$ soit un corps. Si ${\mathcal{A}}$ et ${\mathcal{B}}$ sont séparables (*cf.* définition [\[D4sep1\]](#D4sep1){reference-type="ref" reference="D4sep1"}), alors il en est de même de ${\mathcal{A}}\boxtimes_K {\mathcal{B}}$. A fortiori ${\mathcal{A}}\boxtimes_K {\mathcal{B}}$ (et en particulier ${{\mathcal{A}}}^e$) est semi-simple.
:::

Cela résulte du lemme [\[l2.3\]](#l2.3){reference-type="ref" reference="l2.3"}.$\square$

::: lemme
[]{#L6' label="L6'"} Supposons seulement que les $K$-catégories ${\mathcal{A}}$ et ${\mathcal{B}}$ soient de Wedderburn (*cf.* définition [\[D4wed\]](#D4wed){reference-type="ref" reference="D4wed"}). Alors il en est de même de ${\mathcal{A}}\boxtimes_K {\mathcal{B}}$.
:::

En effet, il découle du lemme précédent que pour tout objet $A$ de ${\mathcal{A}}$ et tout objet $B$ de ${\mathcal{B}}$, le quotient de la $K$-algèbre $({\mathcal{A}}\boxtimes_K
{\mathcal{B}})((A,B),(A,B))$ par l'idéal bilatère $${\operatorname{rad}}({\mathcal{A}})(A,A)\otimes_K
{\mathcal{B}}(B,B)+{\mathcal{A}}(A,A)\otimes_K {\operatorname{rad}}({\mathcal{B}})(B,B)$$ est séparable, donc semi-simple. Il en découle que cet idéal contient le radical. Par ailleurs, il est clair que c'est un nil-idéal, donc contenu dans le radical, donc finalement égal à ${\operatorname{rad}}({\mathcal{A}}\boxtimes_K {\mathcal{B}})$. D'où le résultat.$\square$

La caractérisation suivante des catégories de Wedderburn est celle qui nous servira effectivement dans cette partie.

::: prop
[]{#Wedcaract label="Wedcaract"} On suppose que $K$ est un corps. Une $K$-catégorie ${\mathcal{A}}$ est de Wedderburn si et seulement si ${\mathcal{A}}^e$ est semi-primaire et ${\mathcal{A}}^e/{\operatorname{rad}}({\mathcal{A}}^e)=({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^e$.
:::

Le lemme précédent montre que ${\mathcal{A}}^e$ est semi-primaire et vérifie ${\mathcal{A}}^e/{\operatorname{rad}}({\mathcal{A}}^e)=({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^e$ dès lors que ${\mathcal{A}}$ est de Wedderburn. Réciproquement, si ${\mathcal{A}}^e$ est semi-primaire et ${\mathcal{A}}^e/{\operatorname{rad}}({\mathcal{A}}^e)=({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^e$, on a ${\operatorname{rad}}({\mathcal{A}}^e)\supset id\otimes_K
{\operatorname{rad}}({\mathcal{A}})$, donc la condition de nilpotence (dans la définition des catégories semi-primaires) passe de ${\mathcal{A}}^e$ à ${\mathcal{A}}$; d'autre part, ${\mathcal{A}}^e/{\operatorname{rad}}({\mathcal{A}}^e)$ est semi-simple par hypothèse, et on conclut que $({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^e$ est semi-simple, donc ${\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}})$ est séparable, *cf.* [\[D4sep1\]](#D4sep1){reference-type="ref" reference="D4sep1"} .$\square$

Le même exemple que dans la remarque [\[imparf\]](#imparf){reference-type="ref" reference="imparf"} montre que la condition ${\mathcal{A}}^e/{\operatorname{rad}}({\mathcal{A}}^e)=({\mathcal{A}}/{\operatorname{rad}}({\mathcal{A}}))^e$ est nécessaire.
