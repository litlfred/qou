---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-056-72-categorical-diagonalization
section_title: "Categorical diagonalization"
section_number: 7.2
pages: 53-53
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.974
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:cat diag label="sub:cat diag"}

In [@EH], Elias and Hogancamp developed a theory of categorical diagonalization, which we will now recall. Assume we are given an equivariant monoidal category $T \curvearrowright \mathcal{C}$, which can be taken to be triangulated or dg.

::: definition
([@EH]) []{#def:EH1 label="def:EH1"} Fix an object $F \in K^b(\mathcal{C})$. An arrow: $$\label{eqn:eigenmap}
\lambda\cdot \mathbf{1} \stackrel{\alpha}\longrightarrow F$$ is called an **eigenmap** of $F$, and the grading shift $\lambda \in T^\vee$ is called an **eigenvalue** of $F$.
:::

::: definition
([@EH]) []{#def:EH2 label="def:EH2"} An object $F \in K^b(\mathcal{C})$ is called **diagonalizable** if it has a collection of eigenvalues $\lambda_0,...,\lambda_n \in T^\vee$ and eigenmaps: $$\Big\{ \lambda_i \cdot \mathbf{1} \stackrel{\alpha_i}\to F \Big\}_{i\in \{0,...,n\}}$$ such that $\otimes_{i=0}^n \mathrm{Cone}(\alpha_i) \simeq 0$.
:::

The intuition behind the above terminology comes about by considering the Grothendieck group $[\mathcal{C}]$, which is an algebra because the category $\mathcal{C}$ is monoidal. Multiplication by the class of the object $[F]$ induces an operator on $[\mathcal{C}]$, and the datum of Definition [\[def:EH2\]](#def:EH2){reference-type="ref" reference="def:EH2"} amounts to: $$\label{eqn:charpoly}
\prod_{i=0}^n \left( [F]-\lambda_i \right) = 0$$ In other words, the condition that the product of the cones of the eigenmaps is 0 amounts to requiring the operator $* \leadsto * \cdot [F]$ to solve its characteristic polynomial. In Lemma [\[lem:universal\]](#lem:universal){reference-type="ref" reference="lem:universal"}, we establish the fact that categorical diagonalization is universally represented by the category: $$\mathcal{D}= D^b(\mathrm{Coh}_T(\mathbb{P}^n_A))$$ where $A$ is any commutative ring and $T \curvearrowright \mathbb{P}_A^n$ acts via: $$\label{eqn:action}
t \cdot [z_0:...:z_n] \mapsto \left[ \frac {z_0}{\lambda_0(t)}:...: \frac {z_n}{\lambda_n(t)} \right]$$ where $\lambda_0,...,\lambda_n \in T^\vee$. An immediate generalization of Example [\[ex:projective\]](#ex:projective){reference-type="ref" reference="ex:projective"} yields the following:

::: lemma
[]{#lem:universal label="lem:universal"}

The datum of a diagonalizable object $F \in \mathcal{C}$ as in Definition [\[def:EH2\]](#def:EH2){reference-type="ref" reference="def:EH2"} is equivalent to the existence of a $T$--equivariant map: $$\iota:\mathcal{C}\to \mathbb{P}^n_{A}$$ such that $F = \iota^*\left(\mathcal{O}(1)\right)$, where $A = \mathrm{End}_\mathcal{C}(\mathbf{1})$.
:::
