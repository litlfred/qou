---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-003-2-necessary-conditions-on-dihedral-angles
section_title: "Necessary conditions on dihedral angles"
section_number: 2
pages: 5-7
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.912
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#necessary label="necessary"}

In order for the linear program $L$ to have any chance of having a solution, the dihedral angles $\Delta$ must satisfy some constraints. Indeed, suppose $L$ has a solution.

::: condition
[]{#dihpos label="dihpos"} All of the dihedral angles must be positive.
:::

Furthermore, the sum of all of the dihedral angles of all of the edges of $T$ must be equal to the sum of all of the angles of all of the faces of $T,$ or $F(T) \pi$. On the other hand, it is almost equally obvious that if $t_1, \dots, t_n \in F(T)$ is is some proper subset of the faces of $T$, then the sum of the dihedral angles at the edges incident to one of the $t_i$ must be strictly greater than the $n \pi$. In other words:

::: condition
[]{#sumdih label="sumdih"} Let $\mathcal{F} \subseteq F(T)$, and let $E(\mathcal{F})$ be the set of all edges incident to an element of $\mathcal{F}$. Then $$\label{sumdihineq}
\sum_{e\in E(\mathcal{F})} \Delta(e)\geq \pi |\mathcal{F}|,$$ with equality if and only if $\mathcal{F} = F(T)$ or $E(\mathcal{F})=\emptyset.$
:::

::: definition
For a subcomplex $\mathcal{F}$ of $T$, we define the *excess* of $\mathcal{F}$ to be $$\mathrm{excess\:}\mathcal{F} = \sum_{e\in E(\mathcal{F})} \Delta(e) - \pi |\mathcal{F}|,$$
:::

::: definition
An edge $e$ of a subcomplex $\mathcal{F}$ of $T$ is a *relative boundary edge* of $\mathcal{F}$ if it is incident to a top-dimensional face of $\mathcal{F}$ on exactly one side, and is not a boundary edge of $T$.
:::

The following lemma will prove useful in the sequel.

::: lemma
[]{#boundaryineq label="boundaryineq"} Let $\Delta: E(T) \rightarrow (0, \pi ]$ be an assignment of dihedral angles to edges of $T$ satisfying condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}. Let $t_1, t_2, \ldots, t_n$ be a collection of closed triangles of $T$, and let $\mathcal{F} = t_1 \cup t_2 \cup \ldots \cup t_n$ -- assume $\mathcal{F} \neq T$. Let $\sum_\partial \mathcal{F}$ be the sum of the dihedral angles of the boundary edges of $\mathcal{F}$. Then $$\label{doublebd}
0 < \mathrm{excess\:}\mathcal{F} < \sum_\partial \mathcal{F}.$$
:::

::: proof
*Proof.* The first inequality of [\[doublebd\]](#doublebd){reference-type="ref" reference="doublebd"} is a restatement of Condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}, applied to the subcomplex $\mathcal{F}$. To show the second inequality, let $$\overline{\mathcal{F}} = \bigcup_{t \in F(T) \backslash \{t_1,
\ldots, t_n\}} t.$$ Evidently, $$\mathcal{F} \cup \overline{\mathcal{F}} = T,$$ while $$\mathcal{F} \cap \overline{\mathcal{F}} = \partial\mathcal{F}.$$ Applying the conditions [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"} to $\mathcal{F}$, we see that $$\label{ineqf}
0 < \sum_{e\in E(\mathcal{F})} \Delta(e) -  \pi |F(\mathcal{F})|,$$ while applying them to $\overline{\mathcal{F}}$, we see that $$\label{ineqf2}
0 < \sum_{e\in E(\overline{\mathcal{F}})} \Delta(e) -  \pi
|F(\overline{\mathcal{F}})|.$$

Note now that $$\label{ufaces}
|F(\mathcal{F})| + |F(\overline{\mathcal{F}})| = |F(T)|,$$ while $$\label{uedges}
\sum_{e\in E(\mathcal{F})} \Delta(e)+ \sum_{e\in
  E(\overline{\mathcal{F}})} \Delta(e) - \sum_\partial \mathcal{F} =
\sum_{e\in E(T)} \Delta(e).$$ Adding inequalities [\[ineqf\]](#ineqf){reference-type="ref" reference="ineqf"} and [\[ineqf2\]](#ineqf2){reference-type="ref" reference="ineqf2"}, and applying equations [\[ufaces\]](#ufaces){reference-type="ref" reference="ufaces"} and [\[uedges\]](#uedges){reference-type="ref" reference="uedges"}, we obtain $$\begin{aligned}
 & &  \sum_{e\in E(\mathcal{F})} \Delta(e) -  \pi |F(\mathcal{F})| \\
 & < & \left(\sum_{e\in E(\mathcal{F})} \Delta(e) -  \pi |F(\mathcal{F})|\right) +
         \left(\sum_{e\in E(\overline{\mathcal{F}})} \Delta(e) -
         \pi|F(\overline{\mathcal{F}})|\right) \\
  & = & \left(\sum_{e\in E(\mathcal{F})} \Delta(e) + \sum_{e\in
    E(\overline{\mathcal{F}})} \Delta(e)\right) - \left(\pi |F(\mathcal{F})| +
         \pi|F(\overline{\mathcal{F}})|\right) \\
  & = & \sum_{e\in E(T)} \Delta(e) +  \sum_\partial \mathcal{F} + \pi
  |F(T)|  =  \sum_\partial\mathcal{F},
\end{aligned}$$ where the last equality is obtained by applying the equality case of Condition [\[sumdih\]](#sumdih){reference-type="ref" reference="sumdih"}. ◻
:::
