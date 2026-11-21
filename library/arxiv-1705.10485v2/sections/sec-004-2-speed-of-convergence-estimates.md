---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-004-2-speed-of-convergence-estimates
section_title: "Speed of convergence estimates"
section_number: 2
pages: 6-7
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 1.0
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#sec:testfunctions label="sec:testfunctions"}

The goal of this section is to introduce the notion of zone of control (Section [\[sec:zone\]](#sec:zone){reference-type="ref" reference="sec:zone"}) and to estimate the speed of convergence in the resulting central limit theorem. More precisely, we take as reference law a stable distribution $\phi_{c,\alpha,\beta}$ and a sequence $(X_n)_{n \in \mathbb{N}}$ that admits a zone of control (with respect to $\phi_{c,\alpha,\beta}$). As for mod-$\phi_{c,\alpha,\beta}$ convergent sequences, it is easy to prove that in this framework, an appropriate renormalization $Y_n$ of $X_n$ converges in distribution towards $\phi_{c,\alpha,\beta}$ (see Proposition [\[prop:zone_CLT\]](#prop:zone_CLT){reference-type="ref" reference="prop:zone_CLT"} below).

If $Y$ has distribution $\phi_{c,\alpha,\beta}$, we then want to estimate $$d_\mathrm{Kol}(Y_n,Y) = \sup_{s \in \mathbb{R}} |\mathbb{P}[Y_n \leq s] - \mathbb{P}[Y \leq s]|.
  \label{eq:dKol}$$ To do this, we follow a strategy proposed by Tao (see [@Tao12 Section 2.2]) in the case of sums of i.i.d. random variables with finite third moment. The right-hand side of [\[eq:dKol\]](#eq:dKol){reference-type="eqref" reference="eq:dKol"} can be rewritten as $$\sup_{f \in \mathcal{F}} |\mathbb{E}[f(Y_n)] - \mathbb{E}[f(Y)]|,$$ where $\mathcal{F}$ is the class of measurable functions $y \mapsto 1_{y \leq s}$.

Therefore, it is natural to approach the problem of speed of convergence by looking at general estimates on test functions. The basic idea is then to use the Parseval formula to compute the difference $\mathbb{E}[f(Y_n)] - \mathbb{E}[f(Y)]$, since we have estimates on the Fourier transforms of $Y_n$ and $Y$. A difficulty comes from the fact that the functions $y \mapsto 1_{y \leq s}$ are not smooth, and in particular, their Fourier transforms are only defined in the sense of distributions. This caveat is dealt with by standard techniques of harmonic analysis (Sections [\[subsec:distributions\]](#subsec:distributions){reference-type="ref" reference="subsec:distributions"} to [\[subsec:smoothing\]](#subsec:smoothing){reference-type="ref" reference="subsec:smoothing"}): namely, we shall work in a space of distributions instead of functions, and use an adequate smoothing kernel in order to be able to work with compactly supported Fourier transforms. Section [\[sec:berry\]](#sec:berry){reference-type="ref" reference="sec:berry"} gathers all these tools to give an upper bound for [\[eq:dKol\]](#eq:dKol){reference-type="eqref" reference="eq:dKol"}. This is the main result of this section and can be found in Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}.

::: remark
An alternative way to get an upper bound for [\[eq:dKol\]](#eq:dKol){reference-type="eqref" reference="eq:dKol"} from estimates on characteristic functions is to use the following inequality due to Berry (see [@Berry1941] or [@Fel71 Lemma XVI.3.2]). Let $X$ and $Y$ be random variables with characteristic functions $f^{*}(\zeta)$ and $g^{*}(\zeta)$. Then, provided that $Y$ has a density bounded by $m$, we have, for any $s \in \mathbb{R}$, $$\left|\mathbb{P}[X \leq s] - \mathbb{P}[Y \leq s]\right|\leq \frac{1}{\pi} \int_{-T}^{T}
\left|\frac{f^{*}(\zeta)-g^{*}(\zeta)}{\zeta}\right|\,d\hspace*{-0.3mm}{\zeta} +\frac{24m}{\pi T}.$$ Using this inequality in our context should lead to similar estimates as the ones we obtain, possibly with different constants. The proof we use here however has the advantage of being more self-contained, and to provide estimates for test functions as intermediate results.
:::
