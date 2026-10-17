---
doc_id: arxiv-2211.13362v2
doc_title: "Double-slit experiment revisited"
section_id: sec-005-numerical-dse
section_title: "Numerical DSE"
section_number: null
pages: 6-9
source_pdf: 2211.13362v2.pdf
source_sha256: 3becbeaa1135d2e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.613
---
<figure id="bohmianplots">
<figure id="fig:triple_hist">
<embed src="Figures/triple_hist.pdf" />
<figcaption>Joint distributions of ToFs and <span class="math inline"><em>x</em></span>-screen coordinates for different slit-screen separations, generated from Bohmian trajectory impacts.</figcaption>
</figure>
<figure id="fig:triple_curr">
<embed src="Figures/triple_curr.pdf" />
<figcaption>The flux density across the screen.</figcaption>
</figure>
<figcaption>Numerical data generated for <span class="math inline">$\smash{V_0=10^3}$</span>, <span class="math inline">$\smash{\sigma_b=0.125}$</span>, <span class="math inline">$\smash{\sigma_s=0.5}$</span>, <span class="math inline">$\smash{k_x=0}$</span>, <span class="math inline">$\smash{k_z=15}$</span>, <span class="math inline">$\smash{z_0=3}$</span>, <span class="math inline">$\smash{\sigma_x=3}$</span>, <span class="math inline">$\smash{\sigma_z=0.25}$</span>, with <span class="math inline">$\smash{d=0.9}$</span> (top), <span class="math inline">$\smash{d=10}$</span> (middle), and <span class="math inline">$\smash{d=15}$</span> (bottom), taking <span class="math inline">$\smash{\hbar=m=\Delta=1}$</span>. (The slits were closed after the passage of the wave packet to avoid reflection from the boundary of the grid, see <a href="#eq:dynamicT" data-reference-type="eqref" data-reference="eq:dynamicT">[eq:dynamicT]</a>; <span class="math inline"><em>t</em><sub><em>c</em></sub> = 0.5</span>, <span class="math inline"><em>γ</em> = 4</span>.)<span id="bohmianplots" label="bohmianplots"></span></figcaption>
</figure>

To simulate the first-passage distribution for the DSE, Schrödinger's equation with the double-slit potential [\[eq:pot\]](#eq:pot){reference-type="eqref" reference="eq:pot"} was solved numerically for an initial Gaussian wave packet [\[eq:GGG\]](#eq:GGG){reference-type="eqref" reference="eq:GGG"}. The wave function then determines the particle velocity in the guidance equation [\[eq:guide\]](#eq:guide){reference-type="eqref" reference="eq:guide"}.

Since the wave function evolution is simulated on a grid with Dirichlet boundary conditions, we need to avoid effects arising from reflection at the boundary, in particular reflection from the back wall. To achieve this, the slits were closed dynamically after the passage of the bulk of the wave packet, by changing the $f_{1,2}$ in [\[eq:pot\]](#eq:pot){reference-type="eqref" reference="eq:pot"} to $$\label{eq:dynamicT}
  f = \frac{1}{2}\kern 0.1em\bigg(\kern 0.1em1+\tanh\kern-0.1em\big[\gamma\kern 0.1em(t_c-t)\big]\kern 0.1em\bigg).$$ This closing of the slits of course also cuts off the back tails of the wave packet, but without significant changes of the FPT distribution of the particles passing through the slits.

Numerically integrating the guidance equation Eq. [\[eq:guide\]](#eq:guide){reference-type="eqref" reference="eq:guide"} for $5\times 10^5$ initial conditions randomly sampled from the $|\psi(\vb{r},0)|^2$ distribution, the crossing position $\big(X(t_{\!f}),Y(t_{\!f})\big)$ and time $t_{\!f}$ of Bohmian trajectories through $\smash{z=d}$ were recorded.[^1] Histograms of obtained $t_{\!f}$ and $X(t_{\!f})$ are presented in Fig. [1](#fig:triple_hist){reference-type="ref" reference="fig:triple_hist"}, and current densities $j_\perp(\vb{r},t_{\!f})$ at the screens are shown in Fig. [2](#fig:triple_curr){reference-type="ref" reference="fig:triple_curr"}. The code used for the numerics is publicly available [@DSEnumerics].

![A few snapshots of the evolving $|\psi|^2$-density, using the same parameters as in Fig. [1](#fig:triple_hist){reference-type="ref" reference="fig:triple_hist"}. Note the closing of the slits (see [\[eq:dynamicT\]](#eq:dynamicT){reference-type="eqref" reference="eq:dynamicT"}; $t_c=0.75$, $\gamma=4$) to prevent the reflected wave from influencing the arrivals.](Figures/240910145525_psi4.pdf){#fig:psi2-example width="\\linewidth"}

[^1]: Since the wave function remains a separable function of $(x,z)$ and $y$, the particle motion in the $y$-direction is independent of the motion in the $(x,z)$-plane and hence does not affect the FPT $t_{\!f}$ nor the $x$-screen-coordinate $X(t_{\!f})$.
