---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-021-5-second-order-asymptotics
section_title: "Second order asymptotics"
section_number: 5
pages: 17-18
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.953
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#sect:second_order label="sect:second_order"}

In this section, we investigate the second order asymptotics of the rows of diagrams under the $q$-Plancherel measure and we prove Theorem [\[th:second_order_as_rows\]](#th:second_order_as_rows){reference-type="ref" reference="th:second_order_as_rows"}. As in the previous section, the first part of the proof consists in studying asymptotics of $p_k$. In particular, we shall prove:

::: proposition
[]{#prop:deviation_powersums label="prop:deviation_powersums"} Under the $q$-Plancherel measure, we have the following convergence result. If we denote the renormalized centered power sum by $$W_{n,q,l}(\lambda)=\sqrt{n}\left(\frac{p_l(\lambda)-\mathbb{E}[p_l]}{n^l}\right),$$ then, for any $k \geq 1$, the finite random vector $(W_{n,q,1},W_{n,q,2},\ldots,W_{n,q,k})$ converges in law towards a gaussian vector of covariance matrix: $$\mathrm{cov}(W_{q,l},W_{q,m})=lm\,(1-q)^{l+m}\,\left(\frac{1}{1-q^{l+m-1,1}}-\frac{1}{1-q^{l,m}}\right).$$
:::

Before we start, recall that the algebra of observables $\mathscr{O}$ admits two different products: the *usual product* of (commuting) observables $\cdot$ and the *disjoint product* $\bullet$, *cf.* section [\[sect:observables\]](#sect:observables){reference-type="ref" reference="sect:observables"}. We shall denote by $\mathscr{O}^\bullet$ the algebra with the latter product, and by $\mathbb{E}^\mathrm{id}$ the identification $\mathscr{O}\to \mathscr{O}^\bullet$. The proof of Proposition [\[prop:deviation_powersums\]](#prop:deviation_powersums){reference-type="ref" reference="prop:deviation_powersums"} relies on the interaction of the two products and on the expectation of character values $\mathbb{E}[\varSigma_\rho]=n^{\downarrow |\rho|}\,(1-q)^{|\rho|}/(1-q^\rho)$.
