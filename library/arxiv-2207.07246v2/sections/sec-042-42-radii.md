---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-042-42-radii
section_title: "Radii"
section_number: 4.2
pages: 103-105
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 1.0
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
The root mean square (rms) radius $r_m$ can be interpreted as the average distance between any one of the particles and the system's center of mass. The label of the nucleon does not matter, so we can just take nucleon number 1 as reference. The operator can be written as[^1], $$\begin{aligned}
\hat{r}_m = \left| \hat{\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j \right|,
\end{aligned}$$ and we calculate $\langle {r}_m^2 \rangle$ for its ground state expectation value as

::: flalign
\_m\^2 &= Re \_0 \| \_0 \
&= Re \_T\| e\^-H \...e\^-H e\^-H \...e\^-H \| \_T . []{#rmdef label="rmdef"}
:::

Note that $\hat{r}_m$ does not commute with $H$, so PIMC is well suited to calculate it. Eq.([\[rmdef\]](#rmdef){reference-type="ref" reference="rmdef"}) can be recast into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. We put the operator $\hat{r}_m^2$ at the middle bead M, the corresponding $g^V_{lr,M}(\mathcal{R})$ can be written as, $$\begin{aligned}
g^V_{lr,M}(\mathcal{R})  = \langle \psi^l_{M\!-\!1}  (\mathcal{R}) | \bm{\mathcal{G}} e^{\frac{- \mathcal{V}_M  \Delta \tau }{2}}
\left| {\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A {\bm{r}}_j \right|^2
   e^{\frac{- \mathcal{V}^\dagger_M  \Delta \tau }{2}} \bm{\mathcal{G}} | \psi^r_{M\!+\!1} (\mathcal{R}) \rangle,
\label{gVRlrradiidef}
\end{aligned}$$ while other functions remain the same as in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. Once we calculated $\langle {r}_m^2 \rangle$, the rms value is simply $r_m=\sqrt{\langle {r}_m^2 \rangle}$. Note that these are point nucleon radii.

Similarly, we can define the proton(neutron) radii operator $\hat{r}_{p(n)}$ as[^2], $$\hat{r}_{p(n)} = \left| \hat{\bm{r}}_1 - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j \right| P^1_{p(n)},$$ where $P^1_{p}=\frac{1+\tau_{1z}}{2}$ and $P^1_{n}=\frac{1-\tau_{1z}}{2}$ are the proton and neutron projection operator respectively for nucleon whose label is 1.

::: {#TablePIMC3}
   $^A$Z    $r_m$ (fm)    $r_p$ (fm)   $r_n$ (fm)
  -------- ------------- ------------ -------------
   $^2$H     $1.98(2)$                
   $^3$H    $1.7261(5)$   1.6240(4)    $1.7751(5)$
   $^3$He   $1.7426(6)$   1.7962(6)     1.6289(5)
   $^4$He   $1.4716(2)$   1.4736(2)     1.4693(2)

  :  PIMC rms radii of light nuclei based on the AV6' interaction.
:::

::: {#TablePIMC4}
   $^A$Z    $r_m$ (fm)    $r_p$ (fm)   $r_n$ (fm)
  -------- ------------- ------------ -------------
   $^2$H    $1.991(1)$                
   $^3$H    $1.7497(7)$   1.6430(6)    $1.8007(7)$
   $^3$He   $1.7725(8)$   1.8292(9)     1.6520(7)
   $^4$He   $1.4860(4)$   1.4882(4)     1.4834(4)

  :  PIMC rms radii of light nuclei based on the local chiral N$^2$LO interaction.
:::

In Tables [1](#TablePIMC3){reference-type="ref" reference="TablePIMC3"} and [2](#TablePIMC4){reference-type="ref" reference="TablePIMC4"}, we list our PIMC ground state point nucleon rms radii of light nuclei based on the AV6' interaction and the N$^2$LO local chiral interaction. For $^2$H, since there is no Coulomb interaction, $r_m=r_p=r_n$. For other nuclei however, due to the isospin dependent NN interaction (mainly due to the $\bm{\tau_i}\cdot \bm{\tau}_j$ part in the NN interaction) and the Coulomb interaction, $r_m$, $r_p$ and $r_n$ are not the same. E.g., for $^3$H, the only proton is more likely in the center and the two neutrons are likely on the two sides, so the proton is more closer to the center of the mass of the system, so $r_p < r_n$. $^3$He is the opposite. The small difference between $r_p$ and $r_n$ for $^4$He is caused by the Coulomb interaction.

[^1]: In the code, we calculate the averaged operator $\hat{r}_m = \frac{1}{A} \sum_{i=1}^{A} \left| \hat{\bm{r}}_i - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j \right|.$

[^2]: In the code, we calculate the averaged operator $\hat{r}_{p(n)} = \frac{1}{N_{p(n)}} \sum_{i=1}^{A} \left| \hat{\bm{r}}_i - \frac{1}{A}\sum_{j=1}^A \hat{\bm{r}}_j \right| P^i_{p(n)},$ where $N_{p(n)}$ is the number of protons (neutrons).
