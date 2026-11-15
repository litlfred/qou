---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules"
section_id: sec-005-5-the-geometry-of-bott-samelson-bimodules
section_title: "The geometry of Bott-Samelson bimodules"
section_number: 5
pages: 14-15
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.836
latex_coverage_ratio: 0.967
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules — An important step in the calculation of the triply graded link homology theory of Khovanov and Rozansky is the determination of the"
---
[]{#sec:geom-soerg-bimod label="sec:geom-soerg-bimod"}

In this section, we discuss Bott-Samelson bimodules, calculate their $B \times B$-equivariant cohomology and obtain the formality results needed above.

Since we have already described the geometric realization of indecomposable bimodules, as intersection cohomology of subvarieties of $G$, we know abstractly that the Bott-Samelson bimodule $\S\Bi$ must be the hypercohomology of a perverse sheaf obtained by taking a direct sum of $\IC{}$-sheaves of these subvarieties with appropriate multiplicities.

However, this is deeply dissatisfying from a geometric viewpoint, and totally at odds with our viewpoint that Bott-Samelson bimodules are very natural objects. Thus we would like a more natural geometric realization of them.

For each simple reflection $s$, let $P_s$ be the minimal parabolic containing $s$. For a sequence $\Bi = (s, t,  \dots, u)$ of simple reflections, let $$\BSi=P_s\times_{B} P_t \dots \cdots\times_{B}P_u.$$ We call this the **Bott-Samelson variety** corresponding to $\Bi$. Note that this variety still carries a $B\times B$-action, and thus a diagonal $B$-action.

Furthermore, we have a projective $B\times
B$-equivariant map $m_\Bi:\BS{\Bi}\to G$ given by multiplication, intertwining the diagonal $B$-action on $G_\Bi$ with the conjugation $B$-action on $G$.

The quotient of $\BS{\Bi}$ by the right Borel action is the familiar projective Bott-Samelson variety which is used to construct resolutions of singularities for Schubert varieties. It is worth noting that just like in the flag variety case, if $\Bi$ is a reduced expression (i.e. if $\ell(st\dots u)$ is the length of $\Bi$), then the multiplication map is a resolution of singularities.

Let us explain how to calculate the $B \times B$-equivariant cohomology of the Bott-Samelson varieties. Actually, we will calculate the corresponding dg-module over $S \otimes S$. We start with a lemma:

::: lem
Suppose $\mathcal{F} \in D_{\BB}(pt)$ and let $s$ be a simple reflection. Then: $$\Gamma_{\BB}( \res_{P_s \times B}^{\BB} \ind_{\BB}^{P_s \times B} \mathcal{F}) = \HT\otimes_{\HT^s} \Gamma_{\BB}(\mathcal{F})$$
:::

::: proof
*Proof.* Thanks to Theorem [\[equiv-thm\]](#equiv-thm){reference-type="ref" reference="equiv-thm"} we know that $\Gamma_{P_s \times B} (\ind_{\BB}^{P_s \times B} \mathcal{F})$ is equal to $\Gamma_{\BB}(\mathcal{F})$ regarded as an $\HT^s \otimes
  \HT$-module. Hence $$\Gamma_{\BB}( \res_{P_s \times B}^{\BB}
  \ind_{\BB}^{P_s \times B} \mathcal{F}) = (\HT \otimes \HT)
  \Lotimes_{\HT^s \otimes \HT} \Gamma_{\BB}(\mathcal{F}).$$ However, $S \otimes S$ is free as a module over $S^s\otimes S$ and is hence $\mathcal{K}$-projective. Thus the derived tensor product coincides with the naive tensor product and the result follows. ◻
:::

We can now prove the crucial "formality" claim mentioned above:

::: prop
The direct images of the sheaves $\Cs{\BS{\Bi}}$ and $\IC(\Gw)$ in $D_{B \times
    B}(pt)$ are formal.
:::

::: proof
*Proof.* First notice that we can can write the sheaf $(m_{\Bi})_*\Cs{\BS{\Bi}}$ as a iterated induction and restriction: $$(m_{\Bi})_*\Cs{\BS{\Bi}}\cong \res_{P_{s} \times B}^{B \times B}\ind_{B \times B}^{P_{s} \times B} \dots 
\res_{P_{t} \times B}^{B \times B}\ind_{B \times B}^{P_{t} \times B}(\Cs{B})$$ Hence by the above lemma, letting $p$ be the projection to a point: $$\Gamma_{B \times B} (p_*\Cs{\BS{\Bi}}) = S\otimes_{S^{s}} S \otimes_{S^{t}} \otimes \dots \otimes_{S^{u}} S \qquad \text{in $D_{\A_{\BB}}$}$$ Thus the proposition is true for $\Cs{\BS{\Bi}}$. Now, by the decomposition theorem of [@BBD] or more precisely, its equivariant version in [@BL], we may obtain $\IC(\Gw)$ as a direct summand of $(m_{\Bi})_*\BS{\Bi}$, if $\Bi  = (s, \dots, s)$ is a reduced expression for $w$. Thus $p_*\IC(\Gw)$ is a direct summand of $p_*\Cs{\BS{\Bi}}$ and is also formal. ◻
:::
