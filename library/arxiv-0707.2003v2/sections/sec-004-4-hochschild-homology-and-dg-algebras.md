---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules"
section_id: sec-004-4-hochschild-homology-and-dg-algebras
section_title: "Hochschild homology and dg-algebras"
section_number: 4
pages: 12-14
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.952
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules — An important step in the calculation of the triply graded link homology theory of Khovanov and Rozansky is the determination of the"
---
[]{#sec:hochsch-homol-dg label="sec:hochsch-homol-dg"}

Recall that the Hochschild homology of an $\HT\otimes S$-module $R$ can be defined as $$\HH_*(\S{})=\HT \Lotimes_{\HT\otimes \HT} \S{}$$ where $\HT$ has been made into an $\HT\otimes\HT$ algebra by the multiplication map. Since $\HT\cong\A_{B}$ and $\HT\otimes\HT\cong\A_{\BB}$, this map is that induced by the diagonal group homomorphism $B\hookrightarrow\BB$. Thus, we expect that the geometric analogue of taking Hochschild homology is restricting from a $\BB$-action to the diagonal $B$.

However, we must be careful about the difference between dg-modules and modules. Hochschild homology is an operation on $\HT-\HT$-bimodules, not dg-bimodules. Thus, to make a precise statement requires us to restrict to formal complexes.

::: defi
Let $M \in \dgmod {\mc A_G}$ be a dg-module. If $M \cong H^*(M)$ in $\dgmod{\mathcal{A}_G}$ we say that $M$ is **formal**. Similarly, $\mathcal{F} \in D_G(pt)$ is **formal** if $\Gamma_G(\mathcal{F})$ is.
:::

The following proposition connects the Hochschild cohomology of formal equivariant sheaves with another equivariant cohomology. This is our main technical tool.

::: prop
[]{#formal-isom label="formal-isom"} Suppose $\mathcal{F} \in D_{B \times B}(pt)$ is formal. Then one has an isomorphism: $$\bigoplus_{i} \HH_i( \hc_{B \times B}(\mathcal{F}))[i] \cong \hc_B( \res_{B \times B}^B \mathcal{F})$$ as graded $S$-modules.

Furthermore this isomorphism is functorial. That is, if $\mc F$ and $\mc G$ are formal sheaves in $D_{B \times B}(pt)$, and $\vp:\mc
F\to\mc G$ is a morphism, the maps $\hc_{B}(\vp)$ and $\HH_*(\hc_{\BB}(\vp))$ commute with this isomorphism.
:::

::: proof
*Proof of Proposition [\[formal-isom\]](#formal-isom){reference-type="ref" reference="formal-isom"}.* In order to work out the Hochschild homology of $\hc_{B \times B}(\mathcal{F})$ we may take a free resolution of $\hc_{B \times B}(\mathcal{F})$ by $S \otimes S$-modules: $$0 \to P_{-2n} \to \dots \to P_{-1} \to \hc_{B \times B}(\mathcal{F})$$ We then apply $S \otimes_{S \otimes S} -$ and take cohomology. However, because $\hc_{B \times B}(\mathcal{F}) \cong
\Gamma_{B \times B}(\mathcal{F})$ in $\dgmod\mathcal{A}_{B \times B}$, we may also regard $\bigoplus P_i[-i]$ as a $\mathcal{K}$-projective resolution of $\Gamma(\mathcal{F})$. By Theorem [\[equiv-thm\]](#equiv-thm){reference-type="ref" reference="equiv-thm"} we have: $$\hc_B(\res_{B \times B}^B \mathcal{F}) \cong H^*( S \overset{L}{\otimes}_{S \otimes S}  \hc_{B \times B}(\mathcal{F})) \cong \bigoplus \HH_i( \hc_{B \times B}(\mathcal{F}))[i]$$ ◻
:::

::: proof
*Proof of Theorem [\[sec:introduction-1\]](#sec:introduction-1){reference-type="ref" reference="sec:introduction-1"}.* Let $\mathcal{F}$ denote the image of the intersection cohomology sheaf on $\overline{BwB}$ in $D_{B \times B}(pt)$. We will see in the next section that $\mathcal{F}$ is formal. Hence we can apply the above proposition. However, we also know that $\hc_{B \times
    B}(\mathcal{F})$ is the indecomposable Soergel bimodule $\S w$. Hence: $$\bigoplus_i \HH_i(\S w)[i] \cong \hc_B (\res_{B \times B}^B \mathcal{F})$$

But $\res_{B \times B}^B$ commutes with the map to a point and $\res_{B \times B}^B(\IC(G_w)) \cong \IC(G_w)$ (Lemma [\[res-lemma\]](#res-lemma){reference-type="ref" reference="res-lemma"}). Hence: $$\bigoplus_i \HH_i(\S w)[i] \cong \hc_B(\IC(G_w))$$ This then yields the main theorem. ◻
:::
