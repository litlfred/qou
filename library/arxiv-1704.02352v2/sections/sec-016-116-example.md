---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-016-116-example
section_title: "Example"
section_number: 1.16
pages: 10-13
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.848
latex_coverage_ratio: 0.979
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Young diagrams which can be regarded as a natural one-parameter deformation of some classi- cal"
---
[]{#example:removal-of-boxes label="example:removal-of-boxes"}

Let $\alpha>0$ be a fixed positive integer. For a given integer $i>0$ consider the rectangular Young diagram $$(i^{\alpha i}):=(\underbrace{i,\dots,i}_{\text{$\alpha i$ times}})$$ with $n':=\alpha i^2$ boxes. We will assume that $n'$ is an even number. The special case $\alpha=1$ was considered already by Biane [@Biane1998 Figures 1--3].

Using a random iterative procedure introduced by Kerov [@Kerov1996boundaryYounglattice] which is an inverse of the Plancherel growth process and which will be presented in detail in a forthcoming paper [@DolegaSniady-examples-AFP] we remove half of the boxes from the rectangular Young diagram $(i^{\alpha i})$; the resulting random Young diagram with $n:=\frac{1}{2} n'$ boxes will be denoted by $\lambda_n$. We will use the same transformation $$T:=T_{\sqrt{\frac{\alpha}{n}},\sqrt{\frac{1}{\alpha n}}}$$ in order to scale both the original rectangular Young diagram $(i^{\alpha i})$ as well as the resulting random Young diagram $\lambda_n$.

We notice that the anisotropic Young diagram $T(i^{\alpha i})$ is a square, see [1](#fig:biane-lln-square){reference-type="ref" reference="fig:biane-lln-square"}; we shall denote it by $S$. As we shall see in [@DolegaSniady-examples-AFP], the distribution of the random Young diagram $\lambda_n$ can be equivalently formulated via [\[eq:proba-linearcomb-A\]](#eq:proba-linearcomb-A){reference-type="eqref" reference="eq:proba-linearcomb-A"} in terms of the corresponding natural reducible Jack character and [\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"} as well as [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} are applicable. Thus the sequence of random anisotropic Young diagrams $\Lambda_n=T\lambda_n$ converges to some deterministic limit $\Lambda_\infty$. Not very surprisingly, this limit $\Lambda_\infty$ turns out to be the bottom half of the square $S$, see [1](#fig:biane-lln-square){reference-type="ref" reference="fig:biane-lln-square"}.

<figure id="fig:biane-lln-square">

<figcaption>The green square <span class="math inline"><em>S</em></span> depicts the anisotropic Young diagram <span class="math inline"><em>T</em>(<em>i</em><sup><em>α</em><em>i</em></sup>)</span> in the Russian coordinate system. The blue hatched triangle depicts the limit shape <span class="math inline"><em>Λ</em><sub>∞</sub></span>; the blue dashed line depicts the corresponding profile <span class="math inline"><em>ω</em><sub><em>Λ</em><sub>∞</sub></sub></span>.</figcaption>
</figure>

<figure id="fig:bok10">

<figcaption>The analogue of <a href="#fig:bok5" data-reference-type="ref" data-reference="fig:bok5">[fig:bok5]</a> for <span class="math inline"><em>α</em> = 4</span>, <span class="math inline"><em>i</em> = 10</span>, <span class="math inline"><em>n</em> = 200</span>. The increased number of boxes is compensated by a decrease of the size of the individual boxes. With this choice of scaling, the fluctuations of random Young diagrams <span class="math inline"><em>Λ</em><sub><em>n</em></sub></span> around <span class="math inline"><em>Λ</em><sub>∞</sub></span> tend to zero as <span class="math inline"><em>n</em> → ∞</span>.</figcaption>
</figure>

[\[fig:bok5,fig:bok10\]](#fig:bok5,fig:bok10){reference-type="ref" reference="fig:bok5,fig:bok10"} are an illustration of the Law of Large Numbers ([\[theo:lln\]](#theo:lln){reference-type="ref" reference="theo:lln"}): as the number of boxes $n\to\infty$ tends to infinity, suitably scaled random Young diagrams $\Lambda_n$ indeed seem to converge to the deterministic limit $\Lambda_\infty$.

<figure id="fig:anizo5">

<figcaption>The analogue of <a href="#fig:bok5" data-reference-type="ref" data-reference="fig:bok5">[fig:bok5]</a> for the profiles <span class="math inline">$\sqrt{n}\ \omega_{\Lambda_n}$</span> for which only the second Russian coordinate <span class="math inline"><em>v</em></span> was anisotropically stretched by factor <span class="math inline">$\sqrt{n}$</span>. In this example <span class="math inline"><em>α</em> = 4</span>, <span class="math inline"><em>i</em> = 5</span>, <span class="math inline"><em>n</em> = 50</span>.</figcaption>
</figure>

<figure>

<figcaption> The analogue of <a href="#fig:anizo5" data-reference-type="ref" data-reference="fig:anizo5">3</a> for <span class="math inline"><em>α</em> = 4</span>, <span class="math inline"><em>i</em> = 10</span>, <span class="math inline"><em>n</em> = 200</span>. In this scaling the fluctuations of <span class="math inline">$\sqrt{n}\ \omega_{\Lambda_n}$</span> (<em>“the shaded area”</em> of the heatmap) around <span class="math inline">$\sqrt{n}\ \omega_{\Lambda_\infty}$</span> do not vanish as <span class="math inline"><em>n</em> → ∞</span>. Also the discrepancy between the mean value of these fluctuations <span class="math inline">$\sqrt{n}\ \mathbb{E}\omega_{\Lambda_n}$</span> (the red solid line) and the ‘first-order approximation’ <span class="math inline">$\sqrt{n}\ \omega_{\Lambda_\infty}$</span> (the dashed blue line) does not vanish as <span class="math inline"><em>n</em> → ∞</span>. </figcaption>
</figure>

<figure id="fig:anizo20">

<figcaption> The analogue of <a href="#fig:anizo5" data-reference-type="ref" data-reference="fig:anizo5">3</a> for <span class="math inline"><em>α</em> = 4</span>, <span class="math inline"><em>i</em> = 20</span>, <span class="math inline"><em>n</em> = 800</span>. As <span class="math inline"><em>n</em> → ∞</span>, the amplitude of the oscillations of the discrepancy <span class="math inline">$\sqrt{n}\ \left( \mathbb{E}\omega_{\Lambda_n}- \omega_{\Lambda_\infty} \right)$</span> remain roughly constant, but their frequency tends to infinity and thus the discrepancy converges in the sense of Schwartz distributions.</figcaption>
</figure>

In order to speak about CLT one should consider a more refined scaling: the one in which one stretches the second Russian coordinate $v$ by a factor of $\sqrt{n}$. This scaling has a bizarre feature: each individual box is drawn as a parallelogram in which the difference $v_{\operatorname{max}}-v_{\operatorname{min}}=\sqrt{\alpha}+\frac{1}{\sqrt{\alpha}}$ of the $v$-coordinates of the top and the bottom vertex does not depend on $n$ so one cannot claim that the *size* of an individual box converges to zero; nevertheless the *area* of an individual box does converge to zero. Figures [3](#fig:anizo5){reference-type="ref" reference="fig:anizo5"}--[4](#fig:anizo20){reference-type="ref" reference="fig:anizo20"} illustrate this choice of the scaling.

<figure id="eq:sample-path">

<figcaption>A sample profile <span class="math inline">$\sqrt{n}\ \omega_{\Lambda_n}$</span> for <span class="math inline"><em>α</em> = 4</span>, <span class="math inline"><em>i</em> = 80</span>, <span class="math inline"><em>n</em> = 12800</span>.</figcaption>
</figure>

[\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} implies in particular that the limit $$\label{eq:weak-topology}
\mathbb{E}\Delta_\infty= \lim_{n\to\infty} \mathbb{E}\Delta_n$$ exists as a Schwartz distribution on the real line; the convergence holds in the weak sense, i.e. the limit $$\int u^k\ \mathbb{E}\Delta_\infty(u)  \dif u :=
\lim_{n\to\infty} \int u^k\ \mathbb{E}\Delta_n(u) \dif u$$ exists and is finite for an arbitrary integer $k\geq 0$.

The convergence in [\[eq:weak-topology\]](#eq:weak-topology){reference-type="eqref" reference="eq:weak-topology"} is illustrated in Figures [3](#fig:anizo5){reference-type="ref" reference="fig:anizo5"}--[4](#fig:anizo20){reference-type="ref" reference="fig:anizo20"}: the function $\mathbb{E}\Delta_n$ is the difference between the red solid curve (i.e. the plot of $\sqrt{n} \ \mathbb{E}\omega_{\Lambda_n}$) and the blue dashed curve (i.e. the plot of $\sqrt{n}\ \omega_{\Lambda_\infty}$). As one can see on these examples, the function $\mathbb{E}\Delta_n$ has oscillations of period and amplitude related to the grid of the boxes of the Young diagrams. As $n\to\infty$, the amplitude of these oscillations does not converge to zero (so that the convergence in the supremum norm does not hold) but their frequency tends to infinity (which is sufficient for convergence in the weak topology).

The central limit theorem in [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} is somewhat reminiscent to CLT for random walks. A significant difference lies in the nature of the limit object: in the case of the random walks it is the Brownian motion which has continuous trajectories while in the case considered in [\[theo:clt\]](#theo:clt){reference-type="ref" reference="theo:clt"} it is a random Schwartz distribution $\Delta_\infty$ for which computer simulations (such as the one shown in [5](#eq:sample-path){reference-type="ref" reference="eq:sample-path"}) suggest that it has quite singular 'trajectories', reminiscent to that of the white noise. A systematic investigation of such trajectory-wise properties of $\Delta_\infty$ via short-distance asymptotics of the covariance of the corresponding Gaussian field is out of the scope of the current paper.
