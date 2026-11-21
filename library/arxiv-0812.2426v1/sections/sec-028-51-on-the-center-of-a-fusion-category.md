---
doc_id: arxiv-0812.2426v1
doc_title: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS"
section_id: sec-028-51-on-the-center-of-a-fusion-category
section_title: "On the center of a fusion category"
section_number: 5.1
pages: 16-17
source_pdf: 0812.2426v1.pdf
source_sha256: df1eb953bc2c6c63
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.854
latex_coverage_ratio: 0.917
doc_brief: "CATEGORICAL CENTERS AND RESHETIKHIN-TURAEV INVARIANTS — A theorem of M¨uger asserts that the center Z(C) of a spherical k-linear category C is a modular category if k is an algebraically closed ﬁeld"
---
[]{#sect-centerfusion label="sect-centerfusion"} Fix a commutative ring $\Bbbk$. Let $\mathcal{C}$ be a fusion category over $\Bbbk$ (see Section [\[sect-fusion\]](#sect-fusion){reference-type="ref" reference="sect-fusion"}). Then the trivial Hopf monad $1_\mathcal{C}$ is centralizable. Its centralizer $Z=Z_{1_\mathcal{C}}$ is: $$Z(X)=\bigoplus_{i \in I} \leftidx{^\vee}{\!V}{}_i \otimes X \otimes V_i,$$ with associated dinatural transformation $i_{X,Y} \colon\leftidx{^\vee}{\!Y}{} \otimes X \otimes Y \to Z(X)$ given by: $$i_{X,Y}=\sum_{\substack{i\in I \\ 1 \leq \alpha \leq N_Y^i}} \leftidx{^\vee}{\!q}{}_Y^{i,\alpha}\otimes \mathrm{id}_X \otimes p_Y^{i,\alpha}.$$

The double of $1_\mathcal{C}$ is $D_{1_\mathcal{C}}=Z \circ 1_\mathcal{C}=Z$. Hence $Z$ is a quasitriangular Hopf monad and $\mathcal{Z}(\mathcal{C}) \cong Z\mbox{-}\,\mathcal{C}$ as braided categories. Furthermore, if $\mathcal{C}$ is spherical, then $Z$ is a ribbon Hopf monad (and so $\mathcal{Z}(\mathcal{C})$ is ribbon).

The structural morphisms of $Z$ can be described only in terms of the category $\mathcal{C}$, that is, only using the $p,q$'s (see Section [\[sect-fusion\]](#sect-fusion){reference-type="ref" reference="sect-fusion"}), the duality morphisms, and the sovereign structure $\phi_X \colon X \to
\leftidx{^{\vee\vee}}{\!X}{}$. They are depicted in Figure [1](#morphZ){reference-type="ref" reference="morphZ"}. The dotted lines in the figure represent $\mathrm{id}_{V_0}=\mathrm{id}_\mathbb{1}$ and can be removed without changing the morphisms. We depicted them in order to remember which factor of $Z(X)$ is concerned. To simplify the reading, we denote $A_{V_{i_1} \otimes \cdots \otimes V_{i_n}}$ by $A_{i_1, \dots, i_n}$ for $A=p^{i,\alpha}$, $q^{i,\alpha}$, or $N^i$.

<figure id="morphZ">
<div class="center">
<p><span class="math inline"><em>Z</em><sub>2</sub>(<em>X</em>,<em>Y</em>) = ∑<sub><em>i</em> ∈ <em>I</em></sub></span>  [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] , <span class="math inline"><em>Z</em><sub>0</sub> = ∑<sub><em>i</em> ∈ <em>I</em></sub></span>  [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline">$\displaystyle \mu_X=\hspace*{-.2cm}\sum_{\substack{i,j,k \in I \\ 1 \leq \alpha \leq N_{i,j}^k }}$</span>  [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [c][c] [c][c] , <span class="math inline"><em>η</em><sub><em>X</em></sub>=</span> [Bc][Bc] [Bc][Bc] [Bc][Bc] ,<br />
<span class="math inline"><em>s</em><sub><em>X</em></sub><sup><em>l</em></sup> = ∑<sub><em>i</em> ∈ <em>I</em></sub></span> [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc]  , <span class="math inline"><em>s</em><sub><em>X</em></sub><sup><em>r</em></sup> = ∑<sub><em>i</em> ∈ <em>I</em></sub></span> [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc]  ,<br />
<span class="math inline">$\displaystyle R_{X,Y}=\hspace*{-.2cm}\sum_{\substack{i \in I \\ 1 \leq \alpha \leq N_Y^i }}$</span> [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [Bc][Bc] [c][c] [c][c] , <span class="math inline">$\displaystyle \theta_X=\hspace*{-.2cm}\sum_{\substack{i \in I \\ 1 \leq \alpha \leq
N_X^i }}$</span> [Bc][Bc] [Bc][Bc] [Bc][Bc] [c][c] [c][c] [c][c] .</p>
</div>
<figcaption>Structural morphisms of <span class="math inline"><em>Z</em></span></figcaption>
</figure>

Using the Maschke theorem for Hopf monad's which characterize semisimplicity (see [@BV2 Theorem 6.5]), we have:

::: prop
[@BV4][]{#propZss label="propZss"} Let $\mathcal{C}$ be a spherical fusion category. Then the (ribbon) Hopf monad $Z$ is semisimple if and only if $\dim \mathcal{C}$ is invertible.
:::

Since $\mathcal{Z}(\mathcal{C}) \cong Z\mbox{-}\,\mathcal{C}$, a direct consequence of Proposition [\[propZss\]](#propZss){reference-type="ref" reference="propZss"} is then:

::: cor
[]{#cor-centerfusion label="cor-centerfusion"} Let $\mathcal{C}$ be a spherical fusion category over an algebraic closed field. Assume $\dim \mathcal{C}$ is invertible. Then $\mathcal{Z}(\mathcal{C})$ is a ribbon fusion category.
:::
