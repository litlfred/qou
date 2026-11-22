---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-020-71-weak-real-stability-preservation
section_title: "Weak Real Stability Preservation"
section_number: 7.1
pages: 24-24
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.937
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
Borcea and Brändén obtain the following characterization of weak real stability preserving linear operators. Recall the notion of *proper position* (denoted by $\ll$) given in Definition [\[pp_def\]](#pp_def){reference-type="ref" reference="pp_def"}.

::: BB_Rops_thm
**Theorem [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"} 1** (Borcea-Brändén). *Fix $\lambda \in \mathbb{N}_0^m$ and any linear operator $T: \mathbb{R}_\lambda[x_1,\ldots,x_m] \to \mathbb{R}[x_1,\ldots,x_m]$. The following are equivalent.*

1.  *$T$ maps real stable polynomials to weakly real stable polynomials.*

2.  *One of the following holds:*

    1.  *$\mathop{\mathrm{Symb}}_{BB}(T)$ is $\mathcal{H}_+^{2m}$-stable.*

    2.  *$\mathop{\mathrm{Symb}}_{BB}(T)$ is $(\mathcal{H}_-^m \times \mathcal{H}_+^m)$-stable.*

    3.  *$T$ has image of dimension at most two, and is of the form $$T: p \mapsto q \cdot \psi_1(p) + r \cdot \psi_2(p)$$ where $q,r \in \mathbb{R}[x_1,\ldots,x_m]$ are weakly real stable such that $q \ll r$, and $\psi_1,\psi_2$ are real linear functionals.*
:::

As in the case of complex operators, the degeneracy condition $(ii)(c)$ is the result of allowing weak real stability preserving operators. We now give an example which demonstrates its necessity.

::: example
Define $T: \mathbb{R}_n[x] \to \mathbb{R}[x]$ via: $$T: \sum_{k=0}^n \binom{n}{k} a_k x^k \mapsto a_nx^n + a_{n-2}x^{n-1} = (a_nx + a_{n-2})x^{n-1}$$ This operator obviously preserves weak real stability. We then have that $\mathop{\mathrm{Symb}}_{BB}(T) = (z^2+x)x^{n-1}$, which is not $\mathcal{H}_+^2$-stable nor $(\mathcal{H}_-\times \mathcal{H}_+)$-stable.
:::

Again, the degeneracy condition is required for the characterization but obscures the connection between an operator and its symbol. To remove it, we now turn to our characterization of strong real stability preserving operators.
