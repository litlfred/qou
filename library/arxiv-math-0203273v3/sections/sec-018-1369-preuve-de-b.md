---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-018-1369-preuve-de-b
section_title: "Preuve de b)"
section_number: 13.6.9
pages: 74-76
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.892
doc_brief: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002 — 31 sections: Front matter; Introduction; Alg`ebres `a plusieurs objets"
---
[]{#prb label="prb"} Soient $s,s'$ deux sections monoı̈dales strictes de $\pi_{\mathcal{A}}$. Il s'agit de montrer qu'il existe une famille $(u_A)_{A\in
{\mathcal{A}}}, u_A \in 1_A +{\mathcal{R}}(A,A)$, telle que pour tous $A,B\in {\mathcal{A}}$ on ait $s'(f)= u_As(f)(u_A)^{-1}$ pour tout $f\in 
\bar{\mathcal{A}}(A)$ et $$u_{A\bullet B}=u_A\bullet u_B.$$

Nous allons montrer:

::: lemme
[]{#l6 label="l6"} Il existe une famille double $(u_A^{(r)})_{A\in{\mathcal{A}},r\ge 1}$, avec $u_A^{(r)}\in1+{\mathcal{R}}(A)$, ayant les propriétés suivantes:

::: thlist
$u_A^{(r+1)}\equiv u_A^{(r)}\pmod{{\mathcal{R}}(A)^r}$ pour tout $A\in{\mathcal{A}}$ et tout $r\ge 1$.

$s'(f)= u^{(r)}_A s(f) (u^{(r)}_A)^{-1}$ pour tout $A\in {\mathcal{A}}$, tout $f\in \bar{\mathcal{A}}(A)$ et tout $r\ge 1$.

$u^{(r)}_{A\bullet B}\equiv 
u^{(r)}_A\bullet
u^{(r)}_B\pmod{{\mathcal{R}}(A\bullet B)^{r}}$ pour tous objets $A,B$ et tout $r\ge 1$.
:::
:::

Le lemme [\[l6\]](#l6){reference-type="ref" reference="l6"} implique b) de la même manière que les lemmes [\[l4\]](#l4){reference-type="ref" reference="l4"} et [\[l5\]](#l5){reference-type="ref" reference="l5"} impliquaient c) et a). On procède toujours par récurrence sur $r$. Nous aurons besoin des nouvelles notations suivantes, pour un mot $w$ en les objets de ${\mathcal{A}}$ (voir aussi § [\[co2\]](#co2){reference-type="ref" reference="co2"}): $$C_s(w)=\{x\in {\mathcal{A}}(\overset{\bullet}{w})\mid x 
s(f)=s(f)x\text{ pour tout }
f\in\bar{\mathcal{A}}(w)\}$$ $$C_s^r(w)= 
{\mathcal{R}}(\overset{\bullet}{w})^r\cap 
C_s(w)$$ $$C^{[r]}(w)=\frac{C_s^r(w)+{\mathcal{R}}(\overset{\bullet}{w})^{r+1}}{{\mathcal{R}}(\overset{\bullet}{w})^{r+1}}\simeq
C_s^r(w)/C_s^{r+1}(w).$$

Le groupe $C^{[r]}(w)$ ne dépend pas du choix de $s$, puisque deux sections sont conjuguées par des éléments de $1+{\mathcal{R}}$ (théorème [\[T1\]](#T1){reference-type="ref" reference="T1"} b)) et que $1+{\mathcal{R}}$ opère trivalement sur ${\mathcal{R}}^{[n]}$ par conjugaison. On prendra garde de ne pas le confondre avec le groupe $C(w)^{[r]}$ du §[\[co2\]](#co2){reference-type="ref" reference="co2"}: l'inclusion $$C^{[r]}(w)\subset 
C(w)^{[r]}$$ est en général stricte.

En utilisant le théorème [\[T1\]](#T1){reference-type="ref" reference="T1"} b), choisissons une famille $(u^{(1)}_A)_{A\in 
{\mathcal{A}}}$, avec $u_A^{(1)}\in 1_A+{\mathcal{R}}(A)$, vérifient la propriété (ii) du lemme [\[l6\]](#l6){reference-type="ref" reference="l6"}. La condition (iii) est automatique; le lemme est donc vrai pour $r=1$.

Supposons maintenant $r\ge 1$ et le lemme connu pour $r$. Posons $$n_{A,B}:=1_{A\bullet 
B}-(u^{(r)}_A\bullet
u^{(r)}_B)^{-1}u^{(r)}_{A\bullet 
B}\in
{\mathcal{R}}(A\bullet B)^{r}.$$

Comme $s$ et $s'$ sont monoı̈dales strictes, on a l'identité $$(u^{(r)}_A\bullet 
u^{(r)}_B)^{-1}u^{(r)}_{A\bullet 
B}(s(f)\bullet
s(g))(u^{(r)}_{A\bullet B})^{-1}u^{(r)}_A\bullet 
u^{(r)}_B=s(f)\bullet
s(g)$$ pour $(f,g)\in \bar{\mathcal{A}}(A)\times\bar{\mathcal{A}}(B)$, ce qui équivaut à $$n_{A,B}\in C^r(AB).$$

Par ailleurs, la définition de $n_{A,B}$ donne immédiatement la relation $$1_A\bullet
{\bar n}_{B,C}-{\bar n}_{A\bullet B, C}  +{\bar 
n}_{A,B\bullet C} -
{\bar n}_{A,B}\bullet 1_C=0$$ où $\bar n_{A,B}$ désigne l'image de $n_{A,B}$ dans $C^{[r]}(AB)$.

Soit maintenant $(u^{(r+1)}_A)$ une famille vérifiant les conclusions du lemme [\[l6\]](#l6){reference-type="ref" reference="l6"}. Posons $$u_A^{(r+1)}=u_A^{(r)}(1+m_A).$$

On a donc $m_A\in{\mathcal{R}}(A)^r$. La condition (ii) du lemme se traduit en $$(1+m_A) 
s(f) (1+ m_A)^{-1} =s(f)$$ pour tout $f\in \bar{\mathcal{A}}(A)$, c'est-à-dire $$m_A\in C^r(A).$$

La condition (iii), d'autre part, se traduit en $$\bar n_{A,B}= \bar m_{A\bullet B}-1_A\bullet \bar 
m_B-\bar m_A\bullet
1_B$$ où $\bar m_A$ est la projection de $m_A$ dans $C^{[r]}(A)$ (calcul immédiat). Inversement, la donnée de $m_A\in {\mathcal{R}}(A)^r$ vérifiant ces deux conditions fournit une famille $(u^{(r+1)}_A)$ vérifiant les conclusions du lemme [\[l6\]](#l6){reference-type="ref" reference="l6"}.

On termine comme précédemment, en utilisant le $K\langle
Ob({\mathcal{A}})\rangle$-bimodule $$C^{[r]}=\prod_w 
C^{[r]}(w),$$ et en posant $$\bar n_{w_0,w_1}(w) =\begin{cases}
\bar n_{\overset{\bullet}{w_0},\overset{\bullet}{w_1}}& \text{si $w_0
w_1=w$,}\\
0&\text{sinon.}
\end{cases}$$ Ceci conclut la preuve de b), donc celle de la proposition [\[p5\]](#p5){reference-type="ref" reference="p5"}, et finalement celle du théorème [\[T2\]](#T2){reference-type="ref" reference="T2"}.$\square$

::: rems
[]{#R11/4 label="R11/4"} 

-   Supposons ${\mathcal{A}}$ abélienne et engendrée par un nombre fini d'objets $A_i$, au sens où tout objet est sous-quotient d'une somme finie de copies de $\bullet$-monômes en ces objets. On prendra garde que $\bar{\mathcal{A}}$ n'est pas nécessairement engendrée par les $\pi(A_i)= A_i$. Le point est que l'image dans $\bar{\mathcal{A}}$ d'un monomorphisme de ${\mathcal{A}}$ n'est pas nécessairement un monomorphisme. En fait, on verra plus loin des exemples où $\bar {\mathcal{A}}$ n'est engendrée par aucun ensemble fini d'objets.

-   Dans [@{ak(note)}], nous appliquons le théorème de scindage monoı̈dal ci-dessus pour construire, inconditionnellement, des réalisations de motifs numériques, et les groupes de Galois motiviques associés.

-   Dans la quatrième partie de ce travail, nous appliquons le même théorème pour définir des "enveloppes\" pro-semi-simples ou pro-réductives.
:::
