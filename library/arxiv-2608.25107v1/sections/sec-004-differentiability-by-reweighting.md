---
doc_id: arxiv-2608.25107v1
doc_title: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples"
section_id: sec-004-differentiability-by-reweighting
section_title: "Differentiability by reweighting"
section_number: null
pages: 3-4
source_pdf: 2608.25107v1.pdf
source_sha256: 6dca8b99a1f32db4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.986
doc_brief: "ADoNIS: A Differentiable generatOr of Neutrino Interaction Samples — 19 sections: ADoNIS: A Differentiable generatOr; Introduction; Differentiable programming in part"
---
[]{#sec:adonis_reweighting label="sec:adonis_reweighting"}

A neutrino event generator is an intrinsically stochastic program: it samples a neutrino energy from a flux, an interaction channel, a struck nucleon from the nuclear ground state, a hard-scattering kinematic configuration from a squared amplitude, where applicable the hadronisation of the produced partonic state, and final-state interactions as the outgoing particles propagate through the nuclear medium. Differentiating such a program directly is obstructed at every one of these steps, both by the discrete choices and by the expensive, tabulated amplitude evaluations that are not themselves written to be differentiated.

[ADoNIS]{.smallcaps} circumvents this by separating the physics that has to be differentiated from the physics that does not: the expensive, well-understood calculation is evaluated *once*, when the events are generated, and captured in a compact per-event record; differentiability is then arranged only over the physics parameters of interest, through a closed-form *reweighting* of that record. Concretely, [ADoNIS]{.smallcaps} generates a fixed sample of events, a *bank*, and stores with each event the auxiliary quantities from which its weight can be recomputed as a function of $\bm\theta$. The generation is a conventional, stochastic forward pass; the object that is made differentiable is the per-event weight $$\label{eq:adonis_weight}
w_i(\bm\theta) \;=\; w_i^{0}\,
\underbrace{r^{\rm vertex}_i(\bm\theta)}_{\text{amplitude}}\,
\underbrace{r^{\rm FSI}_i(\bm\theta)}_{\text{cascade}}\,
\underbrace{r^{\rm SF}_i(\bm\theta)}_{\text{nucleus}},$$ where $w_i^{0}$ is the fixed proposal weight assigned at generation and each factor $r_i$ is a differentiable ratio, equal to one at the nominal tune, that transports the event from the parameters it was generated with to the parameters $\bm\theta$. The three factors correspond to the three physics blocks above and are described in the subsections that follow. Because every $r_i$ is a pure JAX function of $\bm\theta$, so is the product, and the entire map $\bm\theta \mapsto w_i(\bm\theta)$ is available to automatic differentiation. Generation and reweighting are performed in double precision (64-bit), since small variations of the reweighting factors around unity can fall below single-precision resolution.

Each of the three factors is controlled by its own group of parameters, and each reweight below is constructed to be identically unity when its parameters sit at nominal, so that the nominal prediction is untouched. The $28$ parameters divide into eleven acting at the electroweak vertex, eleven in the cascade, four on the spectral function, and two overall channel normalisations; each is introduced below in the subsection where it acts.

Each parameter also carries a physically allowed range, which is enforced wherever it is varied. Most multiplicative rate and normalisation parameters have nominal value unity and are restricted to positive values; for the cascade rates of Sec. [\[sec:adonis_cascade\]](#sec:adonis_cascade){reference-type="ref" reference="sec:adonis_cascade"}, positivity is additionally required because the total-rate scale $g$ appears in the denominator of $\exp(-a/g)$. $f^{\rm cex}_{NN}$ is a probability and is restricted to $[0,1]$. The axial masses enter only through $M_A^2$, so the prediction is exactly invariant under $M_A \to -M_A$ and the two signs describe the same physical model. The one boundary that directly affects the gradient, the wall in $\Delta E_b$, is discussed in Sec. [\[sec:adonis_nucleus\]](#sec:adonis_nucleus){reference-type="ref" reference="sec:adonis_nucleus"}.
