---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-015-35-another-product
section_title: "Another product"
section_number: 3.5
pages: 11-12
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.884
latex_coverage_ratio: 0.952
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:bullet_product label="subsect:bullet_product"}

In this paragraph, we recall the definition of the disjoint product $\bullet$ on $\mathscr{O}$ (see [@Sniady06]), which will be useful in section [\[sect:second_order\]](#sect:second_order){reference-type="ref" reference="sect:second_order"}. It is enough to give the value of the product of two elements of the basis $\varSigma_\rho$: $$\varSigma_\mu \bullet \varSigma_\nu = \varSigma_{\mu \cup \nu}.$$ If we look at the description of the classical product on the $\varSigma_\mu$ given at the previous paragraph, taking the product $\bullet$ consists in keeping in the result the terms indexed by families of disjoint indices. This remark can be generalized to expression of the kind: $$X_{i_1,\dots,i_r}^{\mathcal{G}} = \sum_{ \substack{\forall j,\,\,A_j \in \mathcal{A}(n,i_j) \\  G(a_{i,j}) \in \mathcal{G}}} \!\!\!\!\!\!\!\! C(A_1) \cdots C(A_r),$$ where $G(a_{i,j})$ is, as in the previous paragraph, the graph describing which of the $a_{i,j}$'s are equal and $\mathcal{G}$ a collection of *admissible* graphs. The following lemma will be useful in subsection [\[subsect:bound_cumulants\]](#subsect:bound_cumulants){reference-type="ref" reference="subsect:bound_cumulants"}:

::: lemma
[]{#lem:bullet label="lem:bullet"} The disjoint product of two such expressions is given by: $$X_{i_1,\dots,i_r}^{\mathcal{G}} \bullet X_{i'_1,\dots,i'_r}^{\mathcal{G}'} = X_{i_1,\dots,i_r,i'_1,\dots,i'_r}^{\mathcal{G} \sqcup \mathcal{G}'},$$ where $\mathcal{G} \sqcup \mathcal{G}'$ is the collection of all graphs obtained by the disjoint union of a graph of $\mathcal{G}$ and a graph of $\mathcal{G}'$. In other words, the disjoint product of two expressions as above is obtained by keeping in the usual product only terms such that the two families of indices are disjoint.
:::

::: proof
*Proof.* As in the previous paragraph, the summation over sequences of indices corresponding to a given graph gives a term $\varSigma_\rho$. Therefore: $$X_{i_1,\dots,i_r}^{\mathcal{G}} = \sum_{G \in \mathcal{G}} \varSigma_{\rho(G)}$$ and we have $$\begin{aligned}
X_{i_1,\dots,i_r}^{\mathcal{G}} \bullet X_{i'_1,\dots,i'_r}^{\mathcal{G}'} & = \sum_{G \in \mathcal{G}} \sum_{G' \in \mathcal{G}'} \varSigma_{\rho(G),\rho(G')};\\
&=X_{i_1,\dots,i_r,i'_1,\dots,i'_r}^{\mathcal{G} \sqcup \mathcal{G}'}.\qedhere
\end{aligned}$$ ◻
:::
