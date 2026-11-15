---
doc_id: arxiv-hep-ph-0003017v2
doc_title: "arXiv:hep-ph/0003017v2 26 Jun 2000"
section_id: sec-025-53-the-thouless-energy-and-beyond
section_title: "The Thouless Energy and Beyond"
section_number: 5.3
pages: 37-38
source_pdf: 0003017v2.pdf
source_sha256: 1660907865346bdf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.978
doc_brief: "arXiv:hep-ph/0003017v2 26 Jun 2000 — Random matrix theory is a powerful way to describe universal correlations of eigenvalues of complex systems."
---
[]{#BeyondThouless label="BeyondThouless"}

As discussed above, the Dirac spectrum is described by chRMT --- or, equivalently, by the zero-mode approximation of the low-energy effective theory, --- only below the so-called Thouless energy $E_c$. The theoretical prediction for this quantity [@Verb96; @Trento], $$E_c\sim\frac{F^2}{\Sigma\sqrt{V}}\:,$$ has been confirmed quantitatively in the instanton liquid model [@Osbo98a; @Garc00] and on the lattice [@Berb98c; @Gock98; @Guhr99]. To compute the Dirac spectrum beyond the Thouless energy, the calculation must include the kinetic terms in the low-energy effective theory, as discussed in Sec. [\[sec:effective\]](#sec:effective){reference-type="ref" reference="sec:effective"}. The results of such an analysis can again be tested by lattice simulations. This has been done for staggered fermions [@Berb99]. Note that in this case, the effective low-energy theory must be modified to take into account the symmetries of staggered fermions at finite lattice spacing. A convenient quantity to test the theory is the disconnected scalar susceptibility, defined by $$\chi^{\mathrm {disc}}(m)
    =\frac{1}{N}\left\langle\sum_{k,l=1}^N \frac{1}
      {(i\lambda_k+m)(i\lambda_l+m)}\right\rangle
     -\frac{1}{N} \left\langle\sum_{k=1}^N\frac{1}
      {i\lambda_k+m}\right\rangle^2 \:.$$ This quantity can also be computed in chRMT and in chiral perturbation theory (chPT). The result of chRMT is expected to describe the data up to $E_c$. The result of chPT should describe the data beyond $E_c$ but is expected to break down on the scale of the smallest eigenvalue, i.e. for $m\sim
1/V\Sigma$. These expectations are confirmed by the lattice analysis (see Fig. [1](#chPT){reference-type="ref" reference="chPT"} for an example).

<figure id="chPT">
<div class="center">

</div>
<figcaption>The data points represent the disconnected susceptibility computed on the lattice in quenched SU(3) with staggered fermions (<span class="math inline"><em>V</em> = 10<sup>4</sup></span>, <span class="math inline"><em>β</em> = 5.4</span>). The solid line is the prediction of chPT, the dashed line the prediction of chRMT. (The dashed line is hidden by the data points for <span class="math inline"><em>u</em> &lt; 10</span>.) (From Ref. <span class="citation" data-cites="Berb99"></span>.)</figcaption>
</figure>
