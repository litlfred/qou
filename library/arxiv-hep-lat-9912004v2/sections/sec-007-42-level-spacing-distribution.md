---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "arXiv:hep-lat/9912004v2 9 Mar 2000"
section_id: sec-007-42-level-spacing-distribution
section_title: "Level spacing distribution"
section_number: 4.2
pages: 6-7
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-lat/9912004v2 9 Mar 2000 — 11 sections: Front matter; Chiral Random Matrix Theory; Introduction"
---
Another observable with definite predictions from RMT (cf. Sect. [\[SecRMT\]](#SecRMT){reference-type="ref" reference="SecRMT"}) is the distribution of level spacings. The advantage here is, that the level spacing should not be influenced by possible distortions of the smallest eigenvalues due to the unknown topological charge of the configurations (if the smallest eigenvalues are removed from the data).

The studies of the level spacing statistics in lattice data so far have shown a uniform picture consistent with the RMT prediction ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}). The agreement extends on both sides of the confinement-deconfinement phase transition [@PuRaWe98; @BeMaPu99]. However, to the authors' knowledge there is no analytical prediction from chRMTfor the level spacing distribution when focusing on the soft edge or at $T_c$. So one might worry that the standard prediction, Eq. ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}), is not appropriate when $\rho(0)=0$. Within the T-model of [@JaVe96] for $T=T_c$ and $T=3\,T_c$, we have performed a numerical high statistics simulation to eliminate such doubt, and we there confirmed the distribution ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"}). (The T-model is defined by ([\[Z\]](#Z){reference-type="ref" reference="Z"}) with $U(M^2)=M^2$ and $t$ in ([\[Tmodel\]](#Tmodel){reference-type="ref" reference="Tmodel"}) chosen proportional to the unit matrix.)

Usually it is possible to get high statistics on the level spacing distributions since each configuration provides a large number of eigenvalue spacings. However, already the lowest 10 (or 8) eigenvalues allow for a crude estimate of the distribution shape.

Recall that the level spacing distribution is measured in the unfolded spectrum, see ([\[defUnf\]](#defUnf){reference-type="ref" reference="defUnf"}). Here we use the average spacings $\langle
\lambda_{i+1}-\lambda_i\rangle$ between contiguous eigenvalues to define the unfolded level spacings $$s_{i+1}-s_i={(\lambda_{i+1}-\lambda_i)\over 
\langle \lambda_{i+1}-\lambda_i\rangle }\; .
\label{UnfSpace}$$

In Fig. [1](#levelspc){reference-type="ref" reference="levelspc"} we compare the data with the parameter-free theoretical expectation. Whereas below and above $T_c$ we find reasonable agreement with the theoretical expectation, there are clear discrepancies near $T_c$. We observe unexpected high histogram entries. Since the average value by definition is 1 this then leads to a shift of the central peak to the left.

In order to further check our unfolding procedure, we also considered other approaches, e.g. using a average density as in ([\[defUnf\]](#defUnf){reference-type="ref" reference="defUnf"}) by smoothing our distribution in various ways. We furthermore tried to discard the higher lying eigenvalues, e.g. using only the lowest 5 level spacings or introducing a cutoff near the peak of the distributions in Fig. [\[firstevs\]](#firstevs){reference-type="ref" reference="firstevs"}. In all those checks we found essentially the same behavior with discrepancies near $T_c$.

<figure id="levelspc">

<figcaption>Histograms for the distribution of (a) the first 9 eigenvalue spacings on the <span class="math inline">12<sup>3</sup> × 4</span> lattice and (b) the first 7 eigenvalue spacings on the <span class="math inline">24<sup>3</sup> × 12</span> lattice with <span class="math inline"><em>m</em> = 0.008</span> (according to [5,6] <span class="math inline"><em>β</em><sub><em>c</em></sub> ≃ 5.7</span> in this case). The standard prediction (<a href="#WUE" data-reference-type="ref" data-reference="WUE">[WUE]</a>) for the level spacing distribution is plotted for comparison.</figcaption>
</figure>

In conclusion of this section, we observe at $T\simeq T_c$ a breakdown of the otherwise universal microscopic spectral correlations. The dynamics of QCD plays an essential rôle in the phase transition. A RMT model where such dynamics is not there fails to account for the increased fluctuations in the eigenvalue level spacings.
