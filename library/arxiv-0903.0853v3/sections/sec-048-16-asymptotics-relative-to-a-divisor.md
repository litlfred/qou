---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-048-16-asymptotics-relative-to-a-divisor
section_title: "Asymptotics relative to a divisor"
section_number: 16
pages: 79-80
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.811
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:asymptoticsreldivisor label="section:asymptoticsreldivisor"}

In this section, we fix a divisor $\Lambda := \nu_1[\lambda_1] + \cdots +\nu_m[\lambda_m]$ and we write $\nu := \left |\Lambda \right |= \nu_1 + \cdots + \nu_m$. Without loss of generality, we make the following\
**ASSUMPTION:**\
The complex numbers $\lambda_i$ are pairwise distinct and such that: $$\label{hypothese:lambdas}
1\leq \left |\lambda_1 \right |\leq \left |\lambda_2 \right |\leq 
\cdots \leq  \left |\lambda_m \right |< \left |q\lambda_1 \right |.$$

::: defi
[]{#defi:ALambda label="defi:ALambda"} Let $f \in {\mathbb B}^{\Lambda}$. We write[^1] $f \in {\mathbb A}_{q}^{\Lambda}$ []{#not67 label="not67"} and we say that $f$ admits a *$q$-Gevrey asymptotic expansion of level $\nu$ (or order $s := 1/\nu$) along divisor $\Lambda$ at $0$*, if there exists a power series $\sum\limits_{n \ge0} a_n z^n$ and constants $C$, $A > 0$ such that, for any $\epsilon > 0$ and any integer $N \ge 0$, one has, for some small enough $R > 0$ and for all $z\in S(\Lambda,\epsilon;R)$: $$\label{eqn:fN}
\left |f(z) - \sum_{0\le n<N} a_n z^n \right |<
\dfrac{C}{\epsilon} A^N \left |q \right |^{N^2/(2\nu)} \left |z \right |^N~.$$
:::

Recall that condition $z\in S(\Lambda,\epsilon;R)$ means that $0 < \left |z \right |< R$ and $d_q(z,\Lambda) > \epsilon$; see definition [\[defi:secteur\]](#defi:secteur){reference-type="ref" reference="defi:secteur"}. One sees at once that, if $f \in {\mathbb A}_{q}^{\Lambda}$, its asymptotic expansion, written $J(f)$, belongs to the space of $q$-Gevrey series of level $\nu$, whence the following linear map: $$\label{not68}
J: \quad {\mathbb A}_{q}^{\Lambda} \rightarrow {{\mathbf C}[[z]]}_{q;1/\nu}, \quad f \mapsto J(f).$$ (For the notation ${{{\mathbf C}[[z]]}_{q;s}}$, see paragraph [\[subsection:qGevreylevels\]](#subsection:qGevreylevels){reference-type="ref" reference="subsection:qGevreylevels"} of the general notations, in the introduction.) In section [\[section:BorelRitt\]](#section:BorelRitt){reference-type="ref" reference="section:BorelRitt"}, we shall see that this map is onto, providing a \"meromorphic $q$-Gevrey version\" of classical Borel-Ritt theorem. In order to get the surjectivity of $J$, we shall obtain a characterization of ${\mathbb A}_{q}^{\Lambda}$ in terms of the residues along poles belonging to the divisor $\Lambda$. This description will be shared among the following two paragraphs.

[^1]: The set ${\mathbb A}_{q}^{\Lambda}$ was previously written ${\mathbb A}_{q;|\Lambda|}^{\Lambda}$ in our Note [@RSZ2].
