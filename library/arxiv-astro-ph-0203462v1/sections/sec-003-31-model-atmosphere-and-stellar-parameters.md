---
doc_id: arxiv-astro-ph-0203462v1
doc_title: "arXiv:astro-ph/0203462v1 26 Mar 2002"
section_id: sec-003-31-model-atmosphere-and-stellar-parameters
section_title: "Model atmosphere and stellar parameters"
section_number: 3.1
pages: 3-5
source_pdf: 0203462v1.pdf
source_sha256: 337c24b051365f0a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.877
doc_brief: "arXiv:astro-ph/0203462v1 26 Mar 2002 — We present a high-resolution (R=75,000, S/N ∼500) spectroscopic analysis of the bright (V=11.7), extreme halo giant CS 31082-001 ([Fe/H] = −2.9), obtained in an"
---
The adopted model atmospheres (OSMARCS) were computed with the latest version of the MARCS code, initially developed by Gustafsson et al. ([@gben75]) and subsequently updated by Plez et al. ([@pbn92]), Edvardsson et al. ([@edvardsson]), and Asplund et al. ([@agke97]). The current version includes up-to-date continuum and line opacities for atomic and molecular species, treated in opacity sampling with more than 10$^5$ sampling points between 910Å and 20$\mu$m. Models for CS 31082-001 were computed for a metallicity 1/1000th Solar, with the $\alpha$-elements boosted by 0.4 dex relative to iron.

In our preliminary analysis of the star (Hill et al. [@hill01]), we were using the synthetic spectrum code of Spite ([@codespite] and subsequent improvements in the last thirty years). In the present analysis we have employed a more consistent approach based on the *turbospec* synthesis code developed by Plez (Plez et al. [@codeplez]), which shares routines and input data with OSMARCS. The latest version (Alvarez & Plez [@codeplez98]) features: Full chemical equilibrium including 92 atomic and over 500 molecular species, Van der Waals collisional broadening by H, He, and H$_2$ following Anstee and O'Mara ([@anstee]), Barklem and O'Mara ([@barklem1]), and Barklem et al. ([@barklem2]), and updated continuum opacities, and plane-parallel or spherical geometry. The main differences between the Spite et al. and the Plez codes lie in the continuum opacity, the source function (diffusion is included in the latter), and the collisional broadening calculation.

The effective temperature for the star was computed from multicolor information, using the Alonso et al. ([@alonso99]) color-temperature transformations. A number of photometric data are available for CS 31082-001 : $UBVR_CI_C$ (subscript $C$ indicating the Cousins system) are from Beers et al. ([@beers02a]); the $V$ magnitude and Strömgren photometry are from Twarog et al. ([@twarog00]); infrared data are available from the DENIS (Fouqué et al. [@fou00]) and 2Mass surveys (Cutri et al. [@2mass]). A summary of these photometric data, and the corresponding derived temperatures, is given in Table [1](#T-color){reference-type="ref" reference="T-color"}

::: {#T-color}
  ------------- -------------------------- ---------------------- ----------------------
  Index         value                      T$_{eff}$ (K)          T$_{eff}$ (K)
                                           E$(B-V)$               E$(B-V)$
                                           =0.00                  =0.03
  $V$           11.674$\pm$<!-- -->0.009                          
  $(B-V)$       0.772$\pm$<!-- -->0.015    4822$\pm$<!-- -->120   4903$\pm$<!-- -->120
  $b-y$         0.542$\pm$<!-- -->0.009    4917$\pm$<!-- -->70    4980$\pm$<!-- -->70
  $(V-R)_{C}$   0.471$\pm$<!-- -->0.015    4842$\pm$<!-- -->150   5027$\pm$<!-- -->150
  $(V-I)_{C}$   0.957$\pm$<!-- -->0.013    4818$\pm$<!-- -->125   4987$\pm$<!-- -->125
  $(V-K)$       2.232$\pm$<!-- -->0.008    4851$\pm$<!-- -->50    4967$\pm$<!-- -->50
  ------------- -------------------------- ---------------------- ----------------------

  : Colors and effective temperature of CS 31082-001 .
:::

At a Galactic latitude $l = -76\degr$, the observed colors of CS 31082-001 are not expected to be significantly affected by reddening. The Burstein & Heiles ([@bh82]) maps suggest negligible reddening; the Schlegel et al. maps (Schlegel, Finkbeiner, & Davis [@sc98]) suggest E(B-V)$\approx 0.03$. Table [1](#T-color){reference-type="ref" reference="T-color"} lists effective temperatures derived both for the situation of no reddening, and for an adopted reddening of 0.03 mags. The no-reddening values are in better agreement with the derived excitation temperature from Fe I lines. The final adopted temperature of T$_{eff}$=4825 K is consistent with that obtained from the excitation equilibrium of the Fe I lines. A gravity of $\log g$=1.5$\pm$<!-- -->0.3 dex was assumed in order to satisfy the ionization equilibrium of iron and titanium, and a microturbulence velocity of $\xi$=1.8$\pm$<!-- -->0.2 km.s$^{-1}$ was obtained from the requirement that strong and weak lines of iron yield the same abundance.

In this paper we are mostly concerned with the relative abundances of elements in this star, especially the abundance pattern of the heavy neutron-capture elements. The relative abundances are only very weakly dependent on the adopted stellar parameters; all of the lines of interest respond similarly to small changes in temperature and gravity, hence the pattern of the heavy elements relative to one another is hardly affected. A thorough discussion of errors is provided in section [\[errors\]](#errors){reference-type="ref" reference="errors"}.

::: figure*
![image](M2317f5.ps){width="5.9cm"} ![image](M2317f6.ps){width="5.9cm"} ![image](M2317f7.ps){width="5.9cm"}
:::

::: figure*
![image](M2317f8.ps){width="5.9cm"} ![image](M2317f9.ps){width="5.9cm"} ![image](M2317f10.ps){width="5.9cm"}
:::
