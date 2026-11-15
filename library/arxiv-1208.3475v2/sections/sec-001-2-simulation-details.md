---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-001-2-simulation-details
section_title: "Simulation details"
section_number: 2
pages: 2-2
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 1.0
doc_brief: "Poisson - Random Matrix transition in the QCD Dirac spectrum — 12 sections: Front matter; Introduction; Simulation details"
---
[]{#se:Sd label="se:Sd"}

At first we summarize the details of our lattice simulations. We use the Symanzik improved gauge and and the two level stout smeared staggered fermion action of Ref. [@Aoki:2005vt] with $N\ensuremath _{\mbox{\scriptsize f}}=2+1$ flavors. We take the simulation parameters from the work of the Budapest-Wuppertal collaboration who determined the lattice spacing from the kaon decay constant $f_K$ and set the bare quark masses by requiring the pion and kaon masses to be equal to their physical value [@Borsanyi:2010cj]. The bare parameters we used and the corresponding lattice spacings are summarized in Table [1](#tab:bare_parameters){reference-type="ref" reference="tab:bare_parameters"}.

::: ruledtabular
::: {#tab:bare_parameters}
  $\beta$   $m\ensuremath _{\mbox{\scriptsize ud}}$   $m\ensuremath _{\mbox{\scriptsize s}}$   $a$(fm)
  --------- ----------------------------------------- ---------------------------------------- ---------
  3.75      0.001786                                  0.05030                                  0.125
  3.938     0.001172                                  0.03300                                  0.082
  4.08477   0.000836                                  0.02354                                  0.062

  : The bare parameters we used in the lattice simulations; the inverse gauge coupling ($\beta$), the light quark mass ($m\ensuremath _{\mbox{\scriptsize ud}}$), the strange quark mass ($m\ensuremath _{\mbox{\scriptsize s}}$) and the corresponding lattice spacing ($a$).
:::
:::

To explore the dependence of the localized-delocalized mode transition on the temperature and the lattice spacing we performed the simulations at three different lattice spacings $a=0.06, 0.082$ and $0.125$ fm and three different temporal lattice extensions $N_t=4, 6, 8$. The physical temperature of the system is set by its temporal extension as

$$T = \frac{1}{N_t a}.$$

In this way the lattice parameters we used correspond to the physical temperature range of $1.7 T_c < T < 5 T_c$.

To understand the nature of the transition it is crucial to consider the spatial volume dependence of spectral and wave function statistics. For this reason we also repeated some simulations on different spatial volumes. The spatial linear size of the boxes we used were all in the range $2 \,
\mathrm{fm}~\leq~L~\leq~6 \, \mathrm{fm}$. The details of the parameters of our ensembles are summarized in Table [2](#tab:sim_parameters){reference-type="ref" reference="tab:sim_parameters"}.

::: ruledtabular
::: {#tab:sim_parameters}
        $T$(MeV)   $a$(fm)   $N_s$   $N_t$   Nconf    Nevs 
  ---- ---------- --------- ------- ------- ------- ------ --
  A1      263       0.125     24       6      430      512 
  A2                          36              420      256 
  B       300       0.082     32       8      434      256 
  C1      394       0.125     16       4     1622      512 
  C2                          24             1600      512 
  C3                          32              900      512 
  C4                          48              604      128 
  D1      401       0.082     24       6      440      512 
  D2                          36              440      256 
  E       397       0.062     32       8      593      256 
  F       530                          6      420      512 
  G       601       0.082     24       4      396      512 
  H       794       0.062     32       4      417      512 

  : The parameters of the simulations; the temperature, the lattice spacing, the spatial and temporal box size, the inverse gauge coupling, the number of configurations and the number of Dirac eigenvalues computed on each configuration.
:::
:::

Since low Dirac modes can potentially be slow modes of the system we also checked for autocorrelations. In a long run performed on the finest lattice we found that the autocorrelation time for the smallest Dirac modes is definitely smaller than ten trajectories. To be on the safe side on the finest lattice the configurations that we used for spectrum calculations were always separated by thirty trajectories. Even on the coarsest lattice configurations were separated by ten trajectories.
