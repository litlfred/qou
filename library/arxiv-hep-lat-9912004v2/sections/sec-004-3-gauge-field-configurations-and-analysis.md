---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "arXiv:hep-lat/9912004v2 9 Mar 2000"
section_id: sec-004-3-gauge-field-configurations-and-analysis
section_title: "Gauge field configurations and analysis"
section_number: 3
pages: 3-4
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-lat/9912004v2 9 Mar 2000 — 11 sections: Front matter; Chiral Random Matrix Theory; Introduction"
---
By courtesy of the MILC collaboration [@MILC96] there are sets of gauge configurations [@MILCNERSC] available to the lattice community. These were generated with two species of dynamical staggered fermions, at various lattice sizes, temperatures, values of the gauge coupling and small values of the bare fermion mass. In Table [1](#tabconf){reference-type="ref" reference="tabconf"} the samples used in the present study are listed. For further details on the method of determination of the gauge configurations and the physical parameters we refer to [@MILC96].

::: {#tabconf}
  ---------- ----------- ------- ------- ----------- ----------------- ------------
  MILC-set     \# conf's $n_x$     $n_t$ $\beta_g$   $m\,a(\beta_g)$   phase
  124A                61 12            4 5.25        0.0125            $<T_c$
  124B                91 12            4 5.26        0.0125            $<T_c$
  124C               126 12            4 5.27        0.0125            near $T_c$
  124D                57 12            4 5.28        0.0125            $>T_c$
  1241                42 12            4 5.25        0.008             $<T_c$
  1242                50 12            4 5.255       0.008             $<T_c$
  1243                45 12            4 5.26        0.008             near $T_c$
  1244                47 12            4 5.265       0.008             near $T_c$
  1245                42 12            4 5.27        0.008             $>T_c$
  1246                40 12            4 5.28        0.008             $>T_c$
  FT01                30 24           12 5.65        0.008             $<T_c$
  FT03               131 24           12 5.725       0.008             near $T_c$
  FT04               188 24           12 5.8         0.008             $> T_c$
  FT05               146 24           12 5.85        0.008             $>T_c$
  ---------- ----------- ------- ------- ----------- ----------------- ------------

  :  Summary of the MILC configurations used in our analysis (for FT01 we only considered a subset of the total of 149 configurations available). The suggestions in the rightmost column are based on MILC's results. The transition is near $\beta$=5.26 for $n_t=4$ and $\beta$=5.725 for $n_t=12$.
:::

[]{#tabconf label="tabconf"}

The massless staggered Dirac operator is anti-hermitian and therefore has purely imaginary eigenvalues, lying symmetric to the origin. We determine the lowest lying eigenvalues with help of the implicitly restarted Arnoldi method [@So92], using Chebyshev polynomials to improve the convergence.

The convergence speed depends on the separation between the eigenvalues. The configurations below $T_c$ therefore exhibit much slower convergence and for $V
= 24^3\times 12$ the determination is then quite time-consuming. Configurations that are supposedly above $T_c$ develop a gap for the smallest eigenvalue and the convergence of the diagonalization is faster. All eigenvalues have been obtained with a precision of at least 5 significant digits.

We have determined (on the positive imaginary axis) the lowest ten eigenvalues for the $12^3\times 4$ ensembles and the lowest eight eigenvalues for the $24^3\times 12$ ensembles.

The chRMT-prediction for the smallest eigenvalue distribution has been tested against quenched QCD [@DaHeKr99; @EdHeKi99] and dynamical SU(2) [@BeMeWe98] lattice simulations at $T=0$; there are also recent quenched QCD results for non-zero temperature [@EdHeKi99a]. RMT distributions for the bulk nearest-neighbor spacing in both, the confinement and the deconfinement phase of full QCD have been observed in [@PuRaWe98] on $6^3\times 4$ lattices (Wigner surmise, see Eq. ([\[WUE\]](#WUE){reference-type="ref" reference="WUE"})).
