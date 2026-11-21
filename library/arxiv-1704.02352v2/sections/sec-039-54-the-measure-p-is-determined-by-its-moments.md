---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-039-54-the-measure-p-is-determined-by-its-moments
section_title: "The measure P is determined by its moments"
section_number: 5.4
pages: 37-38
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.84
latex_coverage_ratio: 0.893
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
By a minor modification of the proof of [\[eq:free-cumulants-behave-nice\]](#eq:free-cumulants-behave-nice){reference-type="eqref" reference="eq:free-cumulants-behave-nice"} we have $$\label{eq:free-cumulants-behave-nice-B}
\lim_{n\to\infty} \frac{1}{n^{\frac{k_1+\cdots+k_\ell}{2}}} 
\ \mathbb{E}_{\chi_n}\left[ \mathcal{S}_{k_1} \cdots \mathcal{S}_{k_\ell} \right]  =
s_{k_1} \cdots s_{k_\ell}.$$ It follows that the relation between the families of real numbers $(s_k)_{k\geq 2}$ and $(r_k)_{k \geq 2}$ (given by [\[eq:free-cumulants-exist\]](#eq:free-cumulants-exist){reference-type="eqref" reference="eq:free-cumulants-exist"}) is given by an analogue of [\[eq:r-s\]](#eq:r-s){reference-type="eqref" reference="eq:r-s"}.

[\[prop:CumulantsGrowSlow\]](#prop:CumulantsGrowSlow){reference-type="ref" reference="prop:CumulantsGrowSlow"} states that there exists some constant $C$ such that $$|r_k| \leq C^{k} k^{mk}$$ for all positive integers $k \geq 2$, where $m$ is given by [\[eq:what-is-m\]](#eq:what-is-m){reference-type="eqref" reference="eq:what-is-m"}. Thus [\[lem:small-free\]](#lem:small-free){reference-type="ref" reference="lem:small-free"} gives us the following estimates for the moments of $P_{\Lambda_\infty}$: $$\left| \int u^k \dif P_{\Lambda_\infty}(u) \right| = 
\left| \frac{1}{k+1} s_{k+2} \right| \leq
C'^{k+2} (k+2)^{m(k+2)}\leq C''^kk^{mk}$$ for some constants $C',C''$.

We consider first the case $g=0$. [\[lem:Carleman\]](#lem:Carleman){reference-type="ref" reference="lem:Carleman"} implies immediately that the measure $P_{\Lambda_\infty}$ is uniquely determined by its moments which concludes the proof.

In the case $g>0$ the height of each box constituting the anisotropic Young diagram $\Lambda_n$ is equal to $g+o(1)>c$ for some constant $c>0$, uniformly over $n$, cf. [\[sec:hypothesis-double-scaling\]](#sec:hypothesis-double-scaling){reference-type="ref" reference="sec:hypothesis-double-scaling"}. By comparison of the areas it follows that the length $l$ of the bottom rectangle constituting $\Lambda_n$ fulfills $l c \leq 1$; in particular it follows that the support of the measure $P_{\Lambda_n}$ is contained in the interval $\left( -\infty, \frac{1}{c} \right]$. It follows that an analogous inclusion holds true for the support of the mean value $\mathbb{E}P_{\Lambda_n}$; by passing to the limit the same is true for $P_{\Lambda_\infty}$. It follows that [\[lem:Carleman\]](#lem:Carleman){reference-type="ref" reference="lem:Carleman"} can be applied which concludes the proof.

The case $g<0$ is fully analogous.
