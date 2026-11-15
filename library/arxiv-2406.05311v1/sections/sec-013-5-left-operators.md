---
doc_id: arxiv-2406.05311v1
doc_title: "Draft of June 11, 2024 A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD"
section_id: sec-013-5-left-operators
section_title: "Left operators"
section_number: 5
pages: 15-15
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
toc_source: outline
text_source: latex
latex_prose_ratio: 0.876
latex_coverage_ratio: 1.0
doc_brief: "A quantum Murnaghan–Nakayama rule for the flag manifold — In this paper, we give a rule for the multiplication of a Schubert class by a tautological class in the (small) quantum cohomology ring of"
---
[]{#left-operators label="left-operators"}

We will prove the following quantum analog of the first part of Proposition [\[P:peaklessChains\]](#P:peaklessChains){reference-type="ref" reference="P:peaklessChains"}.

::: theorem
[]{#Th:nonZero label="Th:nonZero"} Let $u,w\in S_n$ and $q^\alpha w\in S_n[q]$ be such that $[u,q^\alpha w]^q_k$ is a minimal interval. Then there is a hook partition $\lambda$ with $|\lambda|=\ell(q^\alpha w)-\ell(u)$ such that $C^{q^\alpha w}_{u,v(\lambda,k)}$ is nonzero.
:::

Our proof of Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"} is given at the end of this section. We sketch the organization of this section and that proof. We first extend the approach in [@BS-Monoid] (see also [@Benedetti_Bergeron]) of studying saturated chains in the $k$-Bruhat order using operators. We introduce operators ${\mathbf v}$ with an action $\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}$ on $S_{n}[q]$ and an equivalence relation in Section [\[SS:monoid\]](#SS:monoid){reference-type="ref" reference="SS:monoid"} that encodes saturated chains in the quantum $k$-Bruhat order as follows: Let ${\mathbf v}$ be an operator, $u,w\in S_n$, and $\alpha\in{\mathbb N}^{n-1}$ be such that $u\leq^q_k {\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u = q^\alpha w$. Elements of the equivalence class of ${\mathbf v}$ are in bijection with chains in $[u,q^\alpha w]^q_k$. The operator ${\mathbf v}$ is if $q^\alpha=1$, in which case ${\mathbf v}$ is an operator from [@BS-Monoid].

We show in Section [\[SS:diagrammatic-notation\]](#SS:diagrammatic-notation){reference-type="ref" reference="SS:diagrammatic-notation"} that these operators and the equivalence relation exhibit symmetries that are enjoyed by the quantum $k$-Bruhat order, the most important being Postnikov's cyclic shift [@Postnikov_symmetry], which induces a cyclic symmetry of the coefficients $C^{q^\alpha w}_{u,v}$. Relations of degree two are studied in Section [\[S:degreeTwo\]](#S:degreeTwo){reference-type="ref" reference="S:degreeTwo"}. In Section [\[crossing-products\]](#crossing-products){reference-type="ref" reference="crossing-products"} we associate a graph to an operator ${\mathbf v}$, and show that if ${\mathbf v}\mathop{\mathrm{{\scriptstyle \bullet}}}_{k}u=q^\alpha w$ and if the interval $[u,q^\alpha w]_k^q$ is minimal, then the graph of ${\mathbf v}$ is a (noncrossing) forest. In Section [\[ss:Paths\]](#ss:Paths){reference-type="ref" reference="ss:Paths"} we study operators whose graph is a path. In Section [\[SS:trees\]](#SS:trees){reference-type="ref" reference="SS:trees"}, we use induction to prove that a noncrossing forest ${\mathbf v}$ is equivalent to a composition $\mathbf{R}\mathbf{C}$ of what we term a row ($\mathbf{R}$) and a column ($\mathbf{C}$), and that ${\mathbf v}$ (and hence $\mathbf{R}\mathbf{C}$) may be cyclically shifted to a classical operator ${\mathbf v}'$, which is also a composition $\mathbf{R}'\mathbf{C}'$ of a row $\mathbf{R}'$ and a column $\mathbf{C}'$ in the classical sense of [@Benedetti_Bergeron]. The product $\mathbf{R}'\mathbf{C}'$ corresponds to a peakless chain in the classical interval corresponding to ${\mathbf v}'$. Given this, Postnikov's cyclic symmetry [@Postnikov_symmetry Thm. 4] and Proposition [\[pieri-formulas-version-2\]](#pieri-formulas-version-2){reference-type="ref" reference="pieri-formulas-version-2"} enable us to deduce Theorem [\[Th:nonZero\]](#Th:nonZero){reference-type="ref" reference="Th:nonZero"}.
