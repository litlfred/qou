---
doc_id: arxiv-2509.20302v1
doc_title: "Universality in the resurgence of generalized Tracy-Widom distributions"
section_id: sec-003-31-resurgence-relations-between-cal-d-and-cal-d1
section_title: "Resurgence relations between ${\cal D}^{\{\}}$ and ${\cal D}^{\{1\}}$"
section_number: 3.1
pages: 3-4
source_pdf: 2509.20302v1.pdf
source_sha256: 59837f5b511c9e07
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.831
latex_coverage_ratio: 1.0
doc_brief: "Universality in the resurgence of generalized Tracy-Widom distributions — We analyze determinants associated with Bessel kernels and generic symbol functions, which govern a class of ob- servables"
---
The perturbative series ${\cal D}^{\{\}}(g)$ and the non-perturbative correction ${\cal D}^{\{1\}}(g)$ are related by resurgence relations, see [@Marino:2012zq; @Dorigoni:2014hea; @Aniceto:2018bis] for modern references. This correspondence originates from ambiguity cancellations and are manifested in asymptotic relations: the large order behaviour of the peturbative coefficients ${\cal D}_{k}^{\{\}}$ are related to the non-perturbative correction ${\cal D}_{k}^{\{1\}}$ as $${\cal D}_{k}^{\{\}}=\sum_{j=0}\frac{S^{\{1\}}\Gamma(k-j+1)}{i\pi(8\pi x_{1})^{k-j}}{\cal D}_{j}^{\{1\}}+\dots\label{eq:asymrel}$$ We have checked these relations in many cases. We demonstrate one of our findings in Figure [1](#fig:asym12){reference-type="ref" reference="fig:asym12"} for $x_{1}=1,x_{2}=3/2$.

<figure id="fig:asym12">
<div class="centering">
<img src="asym12" style="width:7cm" />
</div>
<figcaption>Asymptotic behaviour of <span class="math inline">${\cal D}_{k}^{\{\}}$</span> for <span class="math inline"><em>x</em><sub>1</sub> = 1, <em>x</em><sub>2</sub> = 3/2</span>. We present the asymptotic series (blue) and its first 3 (yellow, green, red) Richardson transforms against the asymptotical value <span class="math inline"> − 5/<em>π</em></span>, which includes the Stokes constant <span class="math inline"><em>S</em><sup>{1}</sup></span>. We zoomed to the first 70 coefficients for visibility, but we performed the test with 200 terms and also at higher orders. <span id="fig:asym12" label="fig:asym12"></span> </figcaption>
</figure>

Such an asymptotic behaviour determines the nature of the branch cut at $x_{1}$ of the Borel transform of ${\cal D}^{\{\}}$: $${\cal B}[{\cal D}^{\{\}}](s)=\sum_{k=0}{\cal D}_{k}^{\{\}}\frac{(8\pi s)^{k}}{\Gamma(k+1)}$$ We observed that ${\cal B}[{\cal D}^{\{\}}](s)$ does not have any cut at higher multiple of $x_{1}$. This is in contrast to its logarithm, where we have cuts and corresponding non-perturbative corrections at $nx_{1}$ for $n=1,2,\dots$.

Our generic analysis for the logarithm of the determinant showed that for every $y_{i}$ a logarithmic cut starts at $-y_{i}$ on the negative real line, while for any $x_{i}$ a logarithmic cut starts at $x_{i}$ on the positive real line. We investigated numerically many cases with increasing number of $x_{i}$ s and $y_{i}$s for the determinant themself and observed that higher cuts appeared only for locations $\sum_{i}\delta_{i}x_{i}$ with $\delta_{i}=0,1$. This is illustrated in figure [2](#fig:Borel0){reference-type="ref" reference="fig:Borel0"} for $\{x_{1},x_{2},x_{3},y_{1},y_{2}\}$.

<figure id="fig:Borel0">
<div class="centering">
<img src="Borel0a" style="width:7.5cm" />
</div>
<figcaption>Cut structure on the Borel plane of <span class="math inline">${\cal B}[{\cal D}^{\{\}}](s)$</span> for a symbol with <span class="math inline">{<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>, <em>x</em><sub>3</sub>|<em>y</em><sub>1</sub>, <em>y</em><sub>2</sub>}</span>. We indicated the branch points of the cuts, while the other branch point is at infinity. </figcaption>
</figure>

Since ${\cal D}^{\{1\}}$ corresponds to $\Phi^{\{1\}}$ they are labeled by $\{x_{2},x_{3},y_{1},y_{2},y_{3}=x_{1}\}$. (Or the $y$s need to be rearranged according to their magnitudes). The analytic structure of its Borel transform ${\cal B}[{\cal D}^{\{1\}}](s)$ is represented in figure [3](#fig:Borel1){reference-type="ref" reference="fig:Borel1"}.

The trans-series so far was formal as the various expansion coefficients ${\cal D}_{k}^{\{\delta_{i}\}}$ are only asymptotical. In order to give a meaning to the series we use lateral Borel resummation. The inverse of the Borel transform involves an integration on the real positive line, where we avoid the branch cuts by integrating slightly above or below $$S^{\pm}[{\cal D}^{\{\}}](g)=8\pi g\int_{0}^{\infty e^{\pm i\epsilon}}dse^{-8\pi gs}{\cal B}[{\cal D}^{\{\}}](s)$$ The two lateral Borel resummations are related by the Stokes automorphism $S^{-}[{\cal D}]=S^{+}[\mathfrak{S}({\cal D})]$. Its logarithm $\ln\mathfrak{S}=\sum_{j}e^{-8\pi gx_{j}}\Delta_{x_{j}}$ contains the alien derivatives, which are related to the jump of the function at the logarithmic cuts [@Marino:2012zq; @Dorigoni:2014hea; @Aniceto:2018bis]. We found for the cut at $x_{1}$ that $$\Delta_{1}{\cal D}^{\{\}}=-2S^{\{1\}}{\cal D}^{\{1\}}\ ;\quad\Delta_{1}^{2}{\cal D}^{\{\}}=0$$ where we used the abbreviation $\Delta_{x_{j}}\equiv\Delta_{j}$ for $j=1$.

<figure id="fig:Borel1">
<div class="centering">
<img src="Borel1a" style="width:7.5cm" />
</div>
<figcaption>Cut structure on the Borel plane of <span class="math inline">${\cal B}[{\cal D}^{\{1\}}](s)$</span> for a symbol with <span class="math inline">{<em>x</em><sub>1</sub>, <em>x</em><sub>2</sub>, <em>x</em><sub>3</sub>|<em>y</em><sub>1</sub>, <em>y</em><sub>2</sub>}</span>. This is the same cut structure we would have for <span class="math inline">{<em>x</em><sub>2</sub>, <em>x</em><sub>3</sub>|<em>x</em><sub>1</sub>, <em>y</em><sub>1</sub>, <em>y</em><sub>2</sub>}</span>.</figcaption>
</figure>
