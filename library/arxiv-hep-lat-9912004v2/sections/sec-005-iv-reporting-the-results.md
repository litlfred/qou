---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni"
section_id: sec-005-iv-reporting-the-results
section_title: "REPORTING THE RESULTS"
section_number: IV
pages: 4-7
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
doc_brief: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni — 9 sections: Hip; B. Lang; INTRODUCTION"
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
---
We now turn our attention to the measurement of the statistical properties of the Dirac operator. Starting with the distribution of all eigenvalues and then separating out the lowest and the second lowest eigenvalue we observe the first indication of a discrepancy with chRMT. In order to investigate this discrepancy further we study the level spacing distribution. Finally we focus on the inner edge of the spectrum for $T>T_c$ and measure the exponent for the singularity of the spectral density.

## Eigenvalue density

Fig. [1](#all-dist){reference-type="ref" reference="all-dist"} gives the eigenvalue distribution as obtained from the lowest 10 (or 8 for the large lattices) eigenvalues for each configuration. It coincides with the distribution from all eigenvalues only up to the lowest of all 10th (8th) eigenvalues. In order to emphasize this feature we also plot the distribution histogram of this 10th (8th) eigenvalue in full black.

A remarkable change in the features of the distributions occurs around $T_c$, as given in Table [\[tabconf\]](#tabconf){reference-type="ref" reference="tabconf"}. In particular for $n_x=24$, $n_t=12$ a gap in $\rho(\lambda)$ appears for $T>T_c$.

Since we do not know about the topological charge of most of the configurations studied here, we cannot separate the trivial from the non-trivial topological sectors, as would be required for a faithful comparison with chRMTdistributions. For sufficiently rough lattices (i.e. in the

<figure id="all-dist">

<figcaption>Histograms for the 10 (or 8) smallest eigenvalues. The contribution from the 10th (8th) eigenvalue is indicated in black. (a) <span class="math inline">12<sup>3</sup> × 4, <em>m</em> = 0.0125</span>, (b) <span class="math inline">12<sup>3</sup> × 4, <em>m</em> = 0.008</span>, (c) <span class="math inline">24<sup>3</sup> × 12, <em>m</em> = 0.008</span>.</figcaption>
</figure>

strong coupling region), one can argue [@BeMeWe98] that the topological charge $\nu$ is effectively zero from the fermionic point of view; however this is no more the case for fine enough lattices [@FaHiLa99] and the problem of the knowledge of the topological charge becomes critical. For $T>T_c$ the situation is completely different, since topological fluctuations are suppressed in the continuum theory.

<figure id="firstevs">

<figcaption>Histograms for the 1st eigenvalue. (a) <span class="math inline">12<sup>3</sup> × 4, <em>m</em> = 0.0125</span>, (b) <span class="math inline">12<sup>3</sup> × 4, <em>m</em> = 0.008</span>, (c) <span class="math inline">24<sup>3</sup> × 12, <em>m</em> = 0.008</span>. For the data where we fitted to chRMT-distribution (cf. Table II) we also plot the fits. The error bars in (a) are shown to indicate the typical size of errors in all histograms. </figcaption>
</figure>

The "microscopic" distributions should be in the chUE  universality class and prediction ([\[Pmin\]](#Pmin){reference-type="ref" reference="Pmin"}) should apply in particular for the smallest eigenvalue for $T<T_c$. A fit of the corresponding prediction for the topologically trivial case ($\nu=0$) to the normalized data provides us with the (infinite volume) parameter $\Sigma$. We assume the continuum symmetry, i.e. $N_f=2$ in ([\[Pmin\]](#Pmin){reference-type="ref" reference="Pmin"}). This one-parameter fit appears reasonable only for data concerning temperatures well below $T_c$ as indicated in Fig. [2](#firstevs){reference-type="ref" reference="firstevs"}(a). This is made explicit in Table [1](#tab:fit){reference-type="ref" reference="tab:fit"} where the fitted values of $\Sigma$ together with the corresponding $\chi^2/d.o.f.$ are reported; the latter increases with $T$, and for $T\simeq T_c$ (in agreement with Table I) prediction ([\[Pmin\]](#Pmin){reference-type="ref" reference="Pmin"}) becomes incompatible with data.

The formal chRMTexpression ([\[Pmin\]](#Pmin){reference-type="ref" reference="Pmin"}) gives the eigenvalue distribution as a function of volume and fermion mass; the parameter $\Sigma$ (the spectral density at the origin) is thus defined implicitly as the extrapolation to infinite volume and vanishing fermion mass. From our fits -- if the data follows chRMT formulas -- $\Sigma$ should therefore be independent of the spatial lattice size $L_x$ and the fermion mass $m$.

For e.g. $12^3\times 4$, $\beta=5.25$ we find agreement of $\Sigma$ for $m=0.0125$ and 0.008 within the errors. At $\beta=5.26$ the values disagree. This value of $\beta$ is, however, close to $T_c$ and the position of the phase transition (or crossover) is quite sensitive to $m$. Such a change of the transition point is not accounted for in chRMT, which is not at all sensitive to the underlying dynamics of QCD.

For comparison we have to extrapolate the MILC values [@MILC96] for the chiral condensate both, to infinite volume and to vanishing quark mass. Since (except for chRMT) we have no firm prediction concerning the volume dependence, we just extrapolate the MILC results for the large lattices at $\beta=5.65$ and 5.725 linearly to vanishing quark mass. We know however that finite-volume effects on the condensate increase as the quark mass decreases. Therefore, it is not surprising that our linear extrapolation of MILC results tends to come out slightly but systematically smaller than the values we find in Table [1](#tab:fit){reference-type="ref" reference="tab:fit"}.

The issue of the topological sector is likely to be particularly relevant for the finest lattice at our disposal ($24^3\times 12$), where almost zero modes could be present and spoil the validity of the trivial sector predictions from chRMT. These could be the cause of the bump observed for small $\lambda$ at $\beta=5.8$, both in the spectral density and in the smallest eigenvalue distribution. It is therefore with some hesitation, that we compare the histograms for the smallest eigenvalues in Fig. [2](#firstevs){reference-type="ref" reference="firstevs"} with these predictions.

::: {#tab:fit}
  ------- ------- --------- -------- ------------ -----------------
  $n_x$     $n_t$ $\beta$   $m$      $\Sigma$     $\chi^2/d.o.f.$
                4 5.25      0.0125   0.647(29)    0.495
  12            4 5.26      0.0125   0.571(26)    0.562
  12            4 5.27      0.0125   0.449(29)    1.651
  12            4 5.28      0.0125   0.138(13)    2.129
  12            4 5.25      0.008    0.686(37)    0.368
  12            4 5.255     0.008    0.551(52)    1.218
  12            4 5.26      0.008    0.459(43)    1.379
  12            4 5.265     0.008    0.331(39)    2.517
  12            4 5.27      0.008    0.168(21)    2.806
  24           12 5.65      0.008    0.0198(18)   1.048
  24           12 5.725     0.008    0.0063(60)   5.063
  ------- ------- --------- -------- ------------ -----------------

  : Values of the scale $\Sigma$ as obtained from comparison of lattice data for $P(\lambda_{\min})$ with chUE.
:::

[]{#tab:fit label="tab:fit"}

In order to further investigate this feature, we studied (for the set with $\beta=5. 725$) the influence of the configurations where the eigenvectors $u_0$ of the lowest eigenvalues exhibit a large contribution to the total chirality, i.e. $|\langle \bar{u}_0 \gamma_5 u_0\rangle|\geq 0.08$. According to the index theorem, these configurations with large chirality, which make up roughly one half of the ensemble, tend to carry non-vanishing topological charge and therefore zero modes. Indeed we find that a substantial part (75%) of the first peak may be explained from these contributions.

These findings suggest that indeed topological modes are responsible for a low-lying peak in the distributions. Below $T_c$ all topological sectors are present and the low-lying eigenvalues have comparable magnitudes (their average position being roughly proportional to $\nu$). When the temperature approaches $T_c$ the theoretical expectation is that the topological fluctuations begin to be suppressed, although still present in the ensemble, quasi superimposed on the background distribution, which starts to broaden significantly with increasing temperature. Sufficiently far above $T_c$ only the topologically trivial sector survives and there may be no small eigenvalues at all. This is indeed what we actually observe for the lattice $24^3\times
12$.

In a recent study of quenched configurations [@EdHeKi99a] there have been indications for a dilute gas of instanton--anti-instanton pairs producing a Poissonian distribution of small eigenvalues above $T_c$. These may be suppressed or absent when considering dynamical fermions. In our context this seems to be the case for the finest lattices ($24^3\times 12$ with $\beta=5.85$) at our disposal.

Fig. [3](#secondevs){reference-type="ref" reference="secondevs"} gives the histograms for the 2nd smallest eigenvalues. Again we notice a dramatic change of the distribution shape around $T_c(m)$.

<figure id="secondevs">

<figcaption>Histograms for the 2nd smallest eigenvalue for <span class="math inline">12<sup>3</sup> × 4, <em>m</em> = 0.008</span>. By comparison with Fig. <a href="#firstevs" data-reference-type="ref" data-reference="firstevs">2</a>(b) we observe that the mutual overlap between <span class="math inline">$P(\lambda_{\rm min})$</span> and <span class="math inline"><em>P</em>(<em>λ</em><sub>2</sub>)</span> increases as <span class="math inline"><em>β</em> → <em>β</em><sub><em>c</em></sub></span>. This is not consistent with chRMT.</figcaption>
</figure>

We interpret the sudden flatness of the distribution of the smallest eigenvalues as being (i) due to the vanishing spectral density and (ii) due to increasing statistical fluctuations near the chiral phase transition. The latter effect is not reproduced in chRMTsince this is a zero dimensional and non-dynamical theory. Furthermore, the mutual overlap of $P(\lambda_1)$ and $P(\lambda_2)$ increases for $\beta\to\beta_c$. This is also inconsistent with chRMT. In order to study this effect further we now turn to the level spacing distributions.

## Level spacing distribution

Another observable with definite predictions from RMT (cf. Sect. [\[SecRMT\]](#SecRMT){reference-type="ref" reference="SecRMT"}) is the distribution of level spacings. The advantage here is, that the level spacing should not be influenced by possible distortions of the smallest eigenvalues due to the unknown topological charge of the configurations (if the smallest eigenvalues are removed from the data).

The studies of the level spacing statistics in lattice data so far have shown a uniform picture consistent with the RMT prediction ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}). The agreement extends on both sides of the confinement-deconfinement phase transition [@PuRaWe98; @BeMaPu99]. However, to the authors' knowledge there is no analytical prediction from chRMTfor the level spacing distribution when focusing on the soft edge or at $T_c$. So one might worry that the standard prediction, Eq. ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}), is not appropriate when $\rho(0)=0$. Within the T-model of [@JaVe96] for $T=T_c$ and $T=3\,T_c$, we have performed a numerical high statistics simulation to eliminate such doubt, and we there confirmed the distribution ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}). (The T-model is defined by ([\[Z\]](#Z){reference-type="ref" reference="Z"}) with $U(M^2)=M^2$ and $t$ in ([\[Tmodel\]](#Tmodel){reference-type="ref" reference="Tmodel"}) chosen proportional to the unit matrix.)

Usually it is possible to get high statistics on the level spacing distributions since each configuration provides a large number of eigenvalue spacings. However, already the lowest 10 (or 8) eigenvalues allow for a crude estimate of the distribution shape.

Recall that the level spacing distribution is measured in the unfolded spectrum, see ([\[defUnf\]](#defUnf){reference-type="ref" reference="defUnf"}). Here we use the average spacings $\langle
\lambda_{i+1}-\lambda_i\rangle$ between contiguous eigenvalues to define the unfolded level spacings $$s_{i+1}-s_i={(\lambda_{i+1}-\lambda_i)\over 
\langle \lambda_{i+1}-\lambda_i\rangle }\; .
\label{UnfSpace}$$

In Fig. [4](#levelspc){reference-type="ref" reference="levelspc"} we compare the data with the parameter-free theoretical expectation. Whereas below and above $T_c$ we find reasonable agreement with the theoretical expectation, there are clear discrepancies near $T_c$. We observe unexpected high histogram entries. Since the average value by definition is 1 this then leads to a shift of the central peak to the left.

In order to further check our unfolding procedure, we also considered other approaches, e.g. using a average density as in ([\[defUnf\]](#defUnf){reference-type="ref" reference="defUnf"}) by smoothing our distribution in various ways. We furthermore tried to discard the higher lying eigenvalues, e.g. using only the lowest 5 level spacings or introducing a cutoff near the peak of the distributions in Fig. [2](#firstevs){reference-type="ref" reference="firstevs"}. In all those checks we found essentially the same behavior with discrepancies near $T_c$.

<figure id="levelspc">

<figcaption>Histograms for the distribution of (a) the first 9 eigenvalue spacings on the <span class="math inline">12<sup>3</sup> × 4</span> lattice and (b) the first 7 eigenvalue spacings on the <span class="math inline">24<sup>3</sup> × 12</span> lattice with <span class="math inline"><em>m</em> = 0.008</span> (according to [5,6] <span class="math inline"><em>β</em><sub><em>c</em></sub> ≃ 5.7</span> in this case). The standard prediction (<a href="#WUE" data-reference-type="ref" data-reference="WUE">[WUE]</a>) for the level spacing distribution is plotted for comparison.</figcaption>
</figure>

In conclusion of this section, we observe at $T\simeq T_c$ a breakdown of the otherwise universal microscopic spectral correlations. The dynamics of QCD plays an essential rôle in the phase transition. A RMT model where such dynamics is not there fails to account for the increased fluctuations in the eigenvalue level spacings.
