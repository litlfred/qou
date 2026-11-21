---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-063-212-a-sequence-of-central-extensions
section_title: "A sequence of central extensions"
section_number: 21.2
pages: 111-112
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.959
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:centralextensions label="subsection:centralextensions"}

[]{#not91 label="not91"} For simplicity, we write ${\mathfrak{G}}$ for ${\mathfrak{G}}_{A_{0}}$. The Lie algebra ${\mathfrak{g}}$ of ${\mathfrak{G}}$ consists in all nilpotent matrices of the form: $$\begin{pmatrix}
0_{r_{1}}  & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots  & F_{i,j} & \ldots \\
0      & \ldots & \ldots   & \ldots & \ldots \\
\ldots & 0 & \ldots  & \ldots & \ldots \\
0      & \ldots & 0       & \ldots & 0_{r_{k}}    
\end{pmatrix},$$ where $0_r$ is the square null matrix of size $r$ and where each $F_{i,j}$ is in ${\text{Mat}}_{r_{i},r_{j}}$ for $1 \leq i < j \leq k$. For each integer $\delta$, write ${\mathfrak{g}}^{\geq \delta}$ the sub-Lie algebra of matrices whose only non null blocks $F_{i,j}$ have level $\mu_{j} - \mu_{i} \geq \delta$; it is actually an ideal of ${\mathfrak{g}}$ and ${\mathfrak{G}}^{\geq \delta} := I_{n} + {\mathfrak{g}}^{\geq \delta}$ is a normal subgroup of ${\mathfrak{G}}$. Moreover, one has an exact sequence: $$0 \rightarrow {\mathfrak{G}}^{\geq \delta}/{\mathfrak{G}}^{\geq \delta+1}
\rightarrow {\mathfrak{G}}/{\mathfrak{G}}^{\geq \delta+1} 
\rightarrow {\mathfrak{G}}/{\mathfrak{G}}^{\geq \delta} \rightarrow 1,$$ actually, a central extension. The map $g \mapsto I_{n} + g$ induces an isomorphism from the vector space ${\mathfrak{g}}^{\geq \delta}/{\mathfrak{g}}^{\geq \delta+1}$ to the kernel ${\mathfrak{G}}^{\geq \delta}/{\mathfrak{G}}^{\geq \delta+1}$ of this exact sequence. We write $g^{(\delta)}$ this group: it consists of matrices in ${\mathfrak{g}}$ whose only non null blocks $F_{i,j}$ have level $\mu_{j} - \mu_{i} = \delta$. (This is the reason why we wrote a $0$ instead of a $1$ at the left of the exact sequence !)\
[]{#not92 label="not92"} Restricting the above consideration to $\Lambda := \Lambda_{I}(M_{0})$ considered as a sheaf of subgroups of ${\mathfrak{G}}$ (with coefficients in function fields), we get a similar central extension: $$0 \rightarrow \lambda^{(\delta)} \rightarrow 
\Lambda/\Lambda^{\geq \delta+1} \rightarrow 
\Lambda/\Lambda^{\geq \delta} \rightarrow 1.$$ Now, a fundamental theorem in the non-abelian cohomology of sheaves says that we have an exact sequence of cohomology sets:

::: theo
[]{#theo:devissageH1 label="theo:devissageH1"} One has an exact sequence of pointed sets: $$0 \rightarrow H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)}) \rightarrow 
H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1}) \rightarrow 
H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta}) \rightarrow 1.$$
:::

::: proof
*Proof.* The exactness should be here understood in a rather strong sense. The sheaf $\lambda^{(\delta)}$ is here a pure isoclinic holomorphic vector bundle of degree $- \delta$ and rank $\sum\limits_{\mu_{j} - \mu_{i} = \delta} r_{i} r_{j}$. Its first cohomology group $V^{(\delta)}$ is therefore a vector space of dimension $\delta \sum\limits_{\mu_{j} - \mu_{i} = \delta} r_{i} r_{j}$. The theorem says that $V^{(\delta)}$ operates on the pointed set $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1})$ with quotient the pointed set $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta})$. For a proof, see [@Frenkel th. 1.4 and prop. 8.1]. ◻
:::

::: coro
[]{#coro:devissageH1 label="coro:devissageH1"} There is a natural bijection of $H^{1}({\mathbf{E}_{q}},\Lambda_I(M_0))$ with $\bigoplus\limits_{\delta \geq 1} H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)})$.
:::

::: proof
*Proof.* Indeed, the cohomology sets being pointed, the theorem yields a bijection of each $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1})$ with $H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta}) \times 
H^{1}({\mathbf{E}_{q}},\lambda^{(\delta)})$. ◻
:::

[]{#not93 label="not93"} We shall write ${\mathcal{F}}_{\leq \delta}(M_{0}) := H^{1}({\mathbf{E}_{q}},\Lambda/\Lambda^{\geq \delta+1})$. This space is the solution to the following classification problem: two matrices with diagonal part $A_{0}$ are declared equivalent if their truncatures corresponding to the levels $\leq \delta$ are analytically equivalent (through a gauge transform in ${\mathfrak{G}}$); and there is no condition on the components with levels $> \delta$. This is exactly the equivalence under ${{{\mathbf C}((z))}_{q;s}}$ for $\delta < s \leq \delta + 1$. The corresponding Birkhoff-Guenther normal forms have been described in section [\[section:qGevreyinterpolation\]](#section:qGevreyinterpolation){reference-type="ref" reference="section:qGevreyinterpolation"}. The extreme cases are $\delta > \mu_{k} - \mu_{1}$, where ${\mathcal{F}}_{\leq \delta}(M_{0})$ is the whole space ${\mathcal{F}}(M_{0})$; and $\delta < 1$, where it is trivial.
