---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-029-52-the-coend-of-the-center-of-a-fusion-category
section_title: "The coend of the center of a fusion category"
section_number: 5.2
pages: 17-19
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.904
latex_coverage_ratio: 0.538
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-fusioncoend label="sect-fusioncoend"} Let us describe the structure of the coend $(C,r)$ of $Z\mbox{-}\,\mathcal{C}\cong \mathcal{Z}(\mathcal{C})$, where $\mathcal{C}$ is a spherical fusion category. Recall that $C$ is an object of $\mathcal{C}$ and $r\colon Z(C) \to C$ is an action of $Z$ on $C$. From Theorem [\[thm-coend\]](#thm-coend){reference-type="ref" reference="thm-coend"}, we get: $$C=\bigoplus_{j \in I} \leftidx{^\vee}{\!Z(V_j)}{} \otimes V_j= \bigoplus_{i,j \in I} \leftidx{^\vee}{\!V}{}_i \otimes \leftidx{^\vee}{\!V}{}_j \otimes \leftidx{^{\vee\vee}}{\!V}{}_i
\otimes V_j.$$ Note that an immediate consequence of this is: $\dim \mathcal{Z}(\mathcal{C}) =(\dim \mathcal{C})^2$.

The structural morphisms of $C$ can be expressed using only the category $\mathcal{C}$. Those needed to represent Hopf diagrams are depicted in Figure [1](#morphcoendcenter){reference-type="ref" reference="morphcoendcenter"}.

<figure id="morphcoendcenter">
<div class="center">
<p><span class="math inline">$\displaystyle \Delta_C=\hspace*{-.2cm}\sum_{\substack{i,j,k,m,n \in I \\ 1 \leq \alpha \leq N_{k,m}^k \\ 1 \leq
\beta \leq N_{\leftidx{^\vee}{\!k}{},j,k}^n}}$</span> [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [c][c] [c][c] [c][c] [c][c] , <span class="math inline"><em>ε</em><sub><em>C</em></sub> = ∑<sub><em>j</em> ∈ <em>I</em></sub></span>   [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline">$\displaystyle S_C=\hspace*{-.6cm}\sum_{\substack{i,j,k,l \in I \\ 1 \leq \alpha \leq N^{\leftidx{^\vee}{\!i}{}}_{j,k,{j}^\vee} \\ 1
\leq \beta \leq N^l_{\leftidx{^\vee}{\!j}{},\leftidx{^\vee}{\!i}{}, \leftidx{^\vee}{\!j}{}, \leftidx{^{\vee\vee}}{\!i}{}, j}}}$</span> [c][c] [c][c] [c][c] [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline">$\displaystyle \omega_C=\hspace*{-.2cm}\sum_{\substack{i,j,k,l \in I \\ 1 \leq \alpha \leq N^{\leftidx{^\vee}{\!k}{}}_{\leftidx{^\vee}{\!i}{},j,i} \\
1 \leq \beta \leq N^i_{\leftidx{^\vee}{\!k}{},\leftidx{^\vee}{\!l}{},\leftidx{^{\vee\vee}}{\!k}{}}}}$</span> [c][c] [c][c] [c][c] [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline"><em>θ</em><sub><em>C</em></sub><sup>+</sup> = ∑<sub><em>i</em> ∈ <em>I</em></sub></span> [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc]   , <span class="math inline"><em>θ</em><sub><em>C</em></sub><sup>−</sup> = ∑<sub><em>i</em> ∈ <em>I</em></sub></span> [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline">$\displaystyle\tau_{C,C}=\hspace*{-.1cm}\sum_{\substack{i,j,k,l,a,b,m \in I \\
1 \leq \alpha \leq N^m_{\leftidx{^\vee}{\!k}{},\leftidx{^\vee}{\!l}{},\leftidx{^{\vee\vee}}{\!k}{},l} \\
\\ 1 \leq \beta \leq N^b_{\leftidx{^\vee}{\!m}{},j,m}\\ 1 \leq \gamma \leq N^i_{m,a,{m}^\vee}}}$</span> [c][c] [c][c] [c][c] [c][c] [c][c] [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline"><em>Λ</em> = ∑<sub><em>j</em> ∈ <em>I</em></sub>dim (<em>V</em><sub><em>j</em></sub>)</span> [c][c] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] .</p>
</div>
<figcaption>Structural morphisms of the coend of <span class="math inline">𝒵(𝒞)</span></figcaption>
</figure>

::: thm
[]{#thm-coint-coend label="thm-coint-coend"} The morphism $\Lambda\colon\mathbb{1}\to C$ of Figure [1](#morphcoendcenter){reference-type="ref" reference="morphcoendcenter"} is a $S_C$-invariant integral of the coend of $Z\mbox{-}\,\mathcal{C}\cong \mathcal{Z}(\mathcal{C})$.
:::

Following [@Lyu2], a braided category $\mathcal{B}$ is said to be *modular* if it admits a coend $C$ whose Hopf pairing $\omega_C\colon C \otimes C \to \mathbb{1}$ is non-degenerate (meaning there exists $\sigma\colon\mathbb{1}\to C \otimes C$ such that $(\omega_C \otimes \mathrm{id}_C)(\mathrm{id}_C \otimes \sigma)=\mathrm{id}_C=(\mathrm{id}_C \otimes \omega_C)(\sigma \otimes \mathrm{id}_C)$). Note this extends the usual notion of modularity to the non-semisimple case (when $\mathcal{B}$ is a ribbon fusion category, $\mathcal{B}$ is modular in the above sense if and only if the $S$- matrix is invertible).

::: cor
The center of a spherical fusion category is modular.
:::

::: rem
[]{#rem-algclosedmod label="rem-algclosedmod"} Let $\mathcal{C}$ a spherical fusion category over an algebraic closed field such that $\dim \mathcal{C}$ is invertible. Then by Corollary [\[cor-centerfusion\]](#cor-centerfusion){reference-type="ref" reference="cor-centerfusion"} and Theorem [\[thm-coint-coend\]](#thm-coint-coend){reference-type="ref" reference="thm-coint-coend"}, we get that the center $\mathcal{Z}(\mathcal{C})$ of $\mathcal{C}$ is a modular ribbon fusion category. This last result was first shown in [@Mueg] using different method.
:::

## Computing $\mathrm{RT}_{\mathcal{Z}(\mathcal{C})}(M^3)$ from $\mathcal{C}$ {#soussect-RT}

Let $\mathcal{C}$ be a spherical fusion category over a commutative ring $\Bbbk$. As explained in Sections [\[sect-centerfusion\]](#sect-centerfusion){reference-type="ref" reference="sect-centerfusion"} and [\[sect-fusioncoend\]](#sect-fusioncoend){reference-type="ref" reference="sect-fusioncoend"}, the center $Z(\mathcal{C})$ of $\mathcal{C}$ is a ribbon category which admits a coend $C$.

The integral $\Lambda$ of $C$ is then a normalizable Kirby element since $\theta_C^+ \Lambda=1_\Bbbk$ and $\theta_C^-\Lambda=1_\Bbbk$. Hence the invariant $\tau_{\mathcal{Z}(\mathcal{C})}(M,\Lambda)$ of $3$- manifolds (see Section [\[sect-kirby\]](#sect-kirby){reference-type="ref" reference="sect-kirby"}).

Furthermore, since we have an explicit description of the structural morphisms of the coend $C$ (see Figures [1](#morphcoendcenter){reference-type="ref" reference="morphcoendcenter"}), we have a way to compute this invariant by using Hopf diagrams (see Section [\[sect-Hdiag\]](#sect-Hdiag){reference-type="ref" reference="sect-Hdiag"}). For example, we have: $$\tau_{\mathcal{Z}(\mathcal{C})}(S^3;\Lambda)=1 \quad \text{and} \quad \tau_{\mathcal{Z}(\mathcal{C})}(S^2 \times S^1;\Lambda)=\dim \mathcal{C}.$$

Note that the invariant $\tau_{\mathcal{Z}(\mathcal{C})}(M,\Lambda)$ is well-defined even if $\dim \mathcal{C}$ is not invertible. When $\dim \mathcal{C}$ is invertible and $\Bbbk$ is an algebraic closed field (so that $\mathcal{Z}(\mathcal{C})$ is a modular fusion category, see Remark [\[rem-algclosedmod\]](#rem-algclosedmod){reference-type="ref" reference="rem-algclosedmod"}), the invariant $\tau_{\mathcal{Z}(\mathcal{C})}(M,\Lambda)$ equals to the Reshetikhin-Turaev invariant $\mathrm{RT}_{\mathcal{Z}(\mathcal{C})}(M)$ (up to a different normalization, see Remark [\[rem-invRT\]](#rem-invRT){reference-type="ref" reference="rem-invRT"}). Hence we get a way to compute $\mathrm{RT}_{\mathcal{Z}(\mathcal{C})}(M)$ in terms of the structural morphisms of $\mathcal{C}$ (recall one cannot use the original algorithm of Reshetikhin-Turaev since the simple objects of $\mathcal{Z}(\mathcal{C})$ are unknown in general).
