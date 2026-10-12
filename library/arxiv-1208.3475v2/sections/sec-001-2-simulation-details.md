---
doc_id: arxiv-1208.3475v2
doc_title: "Poisson - Random Matrix transition in the QCD Dirac spectrum"
section_id: sec-001-2-simulation-details
section_title: "Simulation details"
section_number: 2
pages: 2-4
source_pdf: 1208.3475v2.pdf
source_sha256: d53fc4eefa070ba3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.989
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

# Anderson transition in the Dirac spectrum {#se:AtitDs}

Previously it was seen that in the high temperature deconfining phase of $SU(2)$ Yang-Mills theory there is a transition in the staggered Dirac spectrum from localized low modes to delocalized modes higher up in the spectrum [@Kovacs:2010wx]. The question we ask here is whether such a transition also occurs in real QCD with light dynamical quarks. This is a non-trivial question since light quarks suppress low Dirac modes through the fermion determinant in the functional integral and in the quenched case it is exactly the lowest Dirac modes that are localized.

The hallmark of a transition from localized to delocalized modes in terms of spectral statistics is a change from Poisson statistics to random matrix statistics in the spectrum. Intuitively speaking, localized modes are such because they cannot mix with other modes; typical gauge field fluctuations do not mix them. Localized modes close in the spectrum are peaked at spatially distant locations and they are sensitive only to gauge field fluctuations there. As a result the corresponding eigenvalues are statistically independent and the level spacings obey Poisson statistics. Delocalized modes, in contrast, are mixed by typical gauge field fluctuations. Gauge field fluctuations change several delocalized modes together which introduces delicate correlations in the spectrum and as a result the eigenvalue statistics is described by Random Matrix Theory (RMT).

The simplest way to detect a transition in the spectrum from Poisson to RMT statistics is to consider the so called unfolded level spacing distribution. Unfolding is essentially a local rescaling of the eigenvalues to have unit spectral density throughout the spectrum. We did the unfolding by ordering all eigenvalues in the given ensemble and replacing them with their rank order normalized by the total number of configurations. On a few ensembles we also checked unfolding by using local spline approximations to the spectral density but there was no discrepancy between the two methods of unfolding.

Since the unfolded level spacing distribution (ULSD) is known analytically for both the Poisson and the RMT statistics it can be easily used to distinguish between the two cases. For Poisson statistics the ULSD is a simple exponential,

$$P\ensuremath _{\mbox{\scriptsize Poisson}}(s)=\exp(-s).$$

In the RMT case the unfolded level spacing distribution depends on the universality class which in the case of staggered fermions in the fundamental representation of the $SU(3)$ gauge group is the Chiral Unitary Ensemble (ChUE) [@Verbaarschot:2000dy]. The corresponding ULSD is very precisely approximated by the chiral unitary Wigner surmise,

$$P\ensuremath _{\mbox{\scriptsize ChUE}}(s) = \dfrac{32}{\pi^{2}}s^{2}\cdot
                       \exp\left(-\dfrac{4}{\pi}s^{2}\right).
  \label{eq:wigner_chu}$$

To demonstrate the transition in the spectrum in Fig. [1](#fig:ulsd){reference-type="ref" reference="fig:ulsd"} we plot the ULSD in different regions of the spectrum of ensemble C3; $0.15 \leq
\lambda a \leq 0.19$ (a), $0.29 \leq \lambda a \leq 0.32$ (b), $0.34 \leq
\lambda a \leq 0.35$ (c) and $0.375 \leq \lambda a \leq 0.385$ (d). We also indicate in the same Figure the distributions corresponding to the Poisson (localized) and the RMT (delocalized) case. The transition from localized modes at the edge of the spectrum to delocalized modes in the bulk can be clearly seen. This shows that light dynamical fermions do not change the picture observed in the quenched case earlier and the transition also occurs in QCD with quarks of physical masses.

<figure id="fig:ulsd">
<div class="center">
<table>
<tbody>
<tr class="odd">
<td style="text-align: center;"><embed src="0_15_0_19_324.eps" /></td>
<td style="text-align: center;"><embed src="0_29_0_32_324.eps" /></td>
</tr>
<tr class="even">
<td style="text-align: center;"><embed src="0_34_0_35_324.eps" /></td>
<td style="text-align: center;"><embed src="0_375_0_385_324.eps" /></td>
</tr>
</tbody>
</table>
</div>
<figcaption><span id="fig:ulsd" label="fig:ulsd"></span>The unfolded level spacing distribution in different regions of the spectrum of ensemble C3. The figures correspond to the spectral regions <span class="math inline">0.15 ≤ <em>λ</em><em>a</em> ≤ 0.19</span> (a), <span class="math inline">0.29 ≤ <em>λ</em><em>a</em> ≤ 0.32</span> (b), <span class="math inline">0.34 ≤ <em>λ</em><em>a</em> ≤ 0.35</span> (c) and <span class="math inline">0.375 ≤ <em>λ</em><em>a</em> ≤ 0.385</span> (d). The dashed line indicates the exponential distribution corresponding to the localized (Poisson) case and the dotted line indicates the chiral unitary Wigner surmise expected in the delocalized (RMT) case.</figcaption>
</figure>
