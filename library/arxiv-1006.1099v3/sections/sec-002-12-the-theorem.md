---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-002-12-the-theorem
section_title: "The theorem"
section_number: 1.2
pages: 2-3
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.987
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
Let $\Sigma_g$ be a closed surface of genus $g\geq 2$, equipped with a symplectic form. This has a well-defined balanced Fukaya category $\EuScript{F}(\Sigma_g)$, linear over ${\mathbb C}$. Let $\{Q^{2g}_t\}_{t\in {\mathbb P}^1} \subset {\mathbb P}^{2g+1}$ denote a pencil of smooth $2g$-dimensional quadric hypersurfaces in ${\mathbb P}^{2g+1}$, with smooth base locus $Q^{2g}_0 \cap Q^{2g}_1$. By Moser's theorem, the symplectic manifold underlying the complete intersection $Q_0 \cap Q_1$ is independent of the choice of generic pencil of quadrics. It is a simply-connected Fano variety, in particular a monotone symplectic manifold with a well-defined monotone Fukaya category $\EuScript{F}(Q_0\cap Q_1)$, again defined over ${\mathbb C}$. The latter category actually splits into a collection of mutually orthogonal $A_{\infty}$-subcategories, one for each eigenvalue of quantum multiplication by the first Chern class on the quantum cohomology of $Q_0\cap Q_1$. We denote by $D^{\pi}\EuScript{C}$ the cohomological category $H(Tw^{\pi}\EuScript{C})$ underlying the split-closure of the category of twisted complexes of an $A_{\infty}$-category $\EuScript{C}$. Our main result is:

::: Theorem
[]{#Thm:Embed label="Thm:Embed"} There is a ${\mathbb C}$-linear equivalence of ${\mathbb Z}_2$-graded split-closed triangulated categories $$D^{\pi}\EuScript{F}(\Sigma_g) \simeq D^{\pi}\EuScript{F}(Q_0^{2g} \cap Q_1^{2g};0)$$ where $\EuScript{F}(\bullet;0)$ denotes the summand corresponding to the 0-eigenvalue of quantum cup-product by the first Chern class.
:::

The proof of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} given here relies essentially on the (typically non-geometric) passage to idempotent completion.

If $\Sigma_g \rightarrow {\mathbb P}^1$ is a hyperelliptic curve, branched over $\{\lambda_1, \ldots, \lambda_{2g+2}\} \subset {\mathbb C}$, it determines a $(2,2)$-complete intersection $$Q_0 \cap Q_1 \ = \ \left ( \sum z_j^2 = 0 \right ) \, \cap \, \left ( \sum \lambda_j z_j^2 = 0 \right ) \ \subset \, {\mathbb P}^{2g+1}.$$ Varying the $\lambda_j$ in ${\mathbb C}$, one obtains a natural action, by parallel transport, of the hyperelliptic mapping class group $\Gamma_{g,1}^{hyp}$ of a once-pointed curve on each of $\Sigma_g$ and $Q_0 \cap Q_1$. (There is no universal hyperelliptic curve over configuration space $\operatorname{Conf}_{2g+2}({\mathbb P}^1)$ [@Mess]; we have constrained the $\lambda_j$ to lie in ${\mathbb C}\subset {\mathbb P}^1$, which accounts for the appearance of once-pointed curves.)

::: Addendum
[]{#Thm:Action label="Thm:Action"} The equivalence of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} is compatible with the weak action of $\Gamma_{g,1}^{hyp}$.
:::

Considering the situation when branch points go to infinity more carefully, there is a non-split finite extension $$1 \rightarrow {\mathbb Z}_2^{2g} \longrightarrow \tilde{\Gamma}^{hyp}_g \longrightarrow \Gamma^{hyp}_g \rightarrow 1$$ of the classical hyperelliptic mapping class group which acts, via parallel transport, by symplectomorphisms of $Q_0 \cap Q_1$, cf. Remark [\[Rem:BranchingInfinity\]](#Rem:BranchingInfinity){reference-type="ref" reference="Rem:BranchingInfinity"}. A fairly direct consequence of Theorem [\[Thm:Embed\]](#Thm:Embed){reference-type="ref" reference="Thm:Embed"} is:

::: Corollary
[]{#Cor:Faithful2 label="Cor:Faithful2"} The natural representation $\tilde{\Gamma}^{hyp}_g \rightarrow \pi_0\operatorname{Symp}(Q_0 \cap Q_1)$ is faithful.
:::

Classical surgery theory [@Sullivan Theorem 13.5] shows $\tilde\Gamma_g^{hyp} \rightarrow \pi_0\operatorname{Diff}(Q_0 \cap Q_1)$ has infinite kernel. More surprisingly, the $\Gamma_{g,1}^{hyp}$-action extends to a faithful weak action of the full mapping class group $\Gamma_g$ by autoequivalences of $D^{\pi}\EuScript{F}(Q_0\cap Q_1)$, which has no obvious direct geometric construction. The construction of mapping class group actions on triangulated categories is a well-known problem in that part of representation theory concerned with categorification.
