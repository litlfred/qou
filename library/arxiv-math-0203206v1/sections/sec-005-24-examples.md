---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-005-24-examples
section_title: "Examples"
section_number: 2.4
pages: 11-12
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.696
latex_coverage_ratio: 0.989
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
The examples discussed below are treated in depth in [@ES]. The translation into the framework of aqgis straightforward and is recommended as an exercise.

Throughout this section let $\Gamma$ denote a discrete group with unit $e$. Consider the group algebra ${\mathbb C}\Gamma$ and the algebra $C_c (\Gamma )$ of finitely supported complex valued functions with the usual pointwise operations. They are both non-degenerate $*$-algebras. The group algebra has unit $\delta_e$, whereas $C_c (\Gamma )$ has a unit iff $\Gamma$ is finite.

In the group algebra case $({\mathbb C}\Gamma, \Delta)$ the comultiplication is given by $\Delta(\delta_g )=\delta_g\otimes\delta_g$ and yields a Hopf $*$-algebra with counit $\varepsilon (\delta_g )=1$ and coinverse $S(\delta_g )=\delta_{g^{-1}}$, for all $g\in\Gamma$. The functional defined by $\varphi (\delta_g )=\delta_{g,e}$, for $g\in\Gamma$, is unital, positive and both left and right invariant, so $({\mathbb C}\Gamma, \Delta)$ is a cocommutative compact aqg.

Note that $M(C_c (\Gamma ))\cong C(\Gamma )$, where $C(\Gamma )$ is the unital $*$-algebra of all functions on $\Gamma$, and that $C_c (\Gamma\times\Gamma )\cong C_c (\Gamma )\otimes C_c (\Gamma )$ (as $*$-algebras). Thus the algebra $C_c (\Gamma )$ has comultiplication $\Delta:C_c (\Gamma )\rightarrow M(C_c (\Gamma )\otimes C_c (\Gamma ))$ given by $\Delta(a)(g,h)=a(gh)$ for $a\in C_c (\Gamma )$ and $g,h\in\Gamma$. It is easy to see that the support of $\Delta(a)$ for $a\in C_c (\Gamma )$ is infinite whenever $\Gamma$ is. This shows that the Hopf algebra framework is too restrictive to cover this example. For $(C_c(\Gamma), \Delta)$ we have $\varepsilon(a)=a(e)$ and $S(a)(g)=a(g^{-1})$ where $a\in C_c(\Gamma\times\Gamma)$ and $g\in\Gamma$. The integral $\varphi(a)=\sum_{g\in\Gamma} a(g)$, $a\in{\mathbb C}\Gamma$, w.r.t. the counting measure is positive and both left and right invariant, so $(C_c (\Gamma ), \Delta)$ is a commutative discrete aqg.

The following proposition shows that these two examples exhaust the cocommutative compact aqg and the commutative discrete aqg.

::: prop
Let $(A,\Delta)$ be an aqg. Then

1.  $(A,\Delta)$ is discrete and commutative iff there exists a discrete group $\Gamma$ such that $(A,\Delta)\cong (C_c (\Gamma),\Delta)$.

2.  $(A,\Delta)$ is compact and co-commutative iff there exists a discrete group $\Gamma$ such that $(A,\Delta)\cong ({\mathbb C}\Gamma, \Delta)$.
:::

It is also easy to check that $(\hat{{\mathbb C}\Gamma },\hat{\Delta})\cong (C_c (\Gamma),\Delta)$ and $(\hat{C_c (\Gamma)},\hat{\Delta})\cong ({\mathbb C}\Gamma, \Delta)$, so they are dual to each other.

Giving a characterization of the commutative compact and the cocommutative discrete algebraic quantum groups on the algebraic level, is less immediate and requires some (co-) representation theory. For the moment we mention that the commutative-compact case can be described in terms of the algebra of regular functions on a compact group, and we make here an analytic statement concerning both cases.

::: prop
Let $(A,\Delta)$ be an aqg with analytic extension $(A_r, \Delta_r )$. Then

1.  $(A,\Delta)$ is compact and commutative iff there exists a compact group $G$ such that $(A_r,\Delta_r )\cong (C(G),\Delta_r )$.

2.  $(A,\Delta)$ is discrete and cocommutative iff there exists a compact group $G$ such that $(A_r, \Delta_r )\cong (C_r^* (G),\Delta_r )$.
:::

Again these two cases are dual to each other. Here $C(G)$ denotes the C\*-algebra of continuous functions on $G$ with uniform norm, whereas $C_r^* (G)$ denotes the reduced group C\*-algebra of $G$. Since a compact group $G$ is amenable, $C_r^* (G)$ coincides with the universal group C\*-algebra $C^* (G)$, and therefore, as we shall see very explicitly in the next section, the representation theory of a discrete cocommutative aqg coincides with that of $G$. We shall also give a simple algebraic description of the associated aqg in this case.
