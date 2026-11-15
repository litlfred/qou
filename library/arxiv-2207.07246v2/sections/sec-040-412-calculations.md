---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-040-412-calculations
section_title: "Calculations"
section_number: 4.1.2
pages: 91-98
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.893
latex_coverage_ratio: 0.861
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secResultCalc label="secResultCalc"} The calculation of the ground state energy $E_0$ can be recast into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) as discussed in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}, with the operator $\hat{O}$ being the Hamiltonian $H=T+V$. And we calculate the ground state energy $E_0$ by $$E_0 (\Delta \tau)
= \frac{
\frac{1}{2}  Re  \left\{  \langle \Psi_T| H [U(\Delta \tau)]^N  | \Psi_T \rangle
 +
 \langle \Psi_T|  [U(\Delta \tau)]^N H | \Psi_T \rangle
 \right\}
 }
{  Re \langle \Psi_T| [U(\Delta \tau)]^N  | \Psi_T \rangle} ,
\label{PIMCopexpdetailE0dtau}$$ which in the limit of $\Delta \tau=0$ becomes the true expectation $E_0$ as shown in Eq.([\[PIMCopexpdetailOH\]](#PIMCopexpdetailOH){reference-type="ref" reference="PIMCopexpdetailOH"}), $$E_0
= \frac{
\frac{1}{2}  Re  \left(  \langle \Psi_T| H e^{-H \tau}  | \Psi_T \rangle
 +
 \langle \Psi_T|  e^{-H \tau} H | \Psi_T \rangle
 \right)
 }
{  Re \langle \Psi_T| e^{-H \tau} | \Psi_T \rangle} .
\label{PIMCopexpdetailE0}$$ The the corresponding $g(\mathcal{R})_{lr}$ takes the form of Eq.([\[gRlrOH\]](#gRlrOH){reference-type="ref" reference="gRlrOH"}) which can be written as, $$g(\mathcal{R})_{lr} = \frac{1}{2}
\left[
\sum\limits_{S} \langle \psi^l_T| H | R_0 S\rangle \langle S | \psi^r_0 (\mathcal{R}) \rangle
+ \sum\limits_{S} \langle \psi^l_N (\mathcal{R}) | S \rangle \langle R_N S| H | \psi^r_T \rangle
 \right]
g^F(\mathcal{R}),$$ and the corresponding $g^V_{lr,M}(\mathcal{R})$ is, $$\begin{aligned}
g^V_{lr,M}(\mathcal{R}) =
\begin{cases}
\sum\limits_{S} \langle \psi^l_T| H | R_0 S\rangle \langle S | \psi^r_0 (\mathcal{R}) \rangle,
 &  M=0. \\
\sum\limits_{S} \langle \psi^l_N (\mathcal{R}) | S \rangle \langle R_N S| H | \psi^r_T \rangle,
 & M=N .
\end{cases}
\label{gVRlrHdef}
\end{aligned}$$ All the other functions are the same as discussed in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}.

The calculations of $\langle R S| H | \psi^r_T \rangle$ and $\langle \psi^l_T| H | R S\rangle$ are straightforward. First, they can be calculated as, $$\begin{aligned}
\langle R S| H | \psi^r_T \rangle &= \langle R S| T | \psi^r_T \rangle + \langle R S| V | \psi^r_T \rangle,  \\
\langle \psi^l_T| H | R S\rangle &= \langle \psi^l_T| T | R S\rangle + \langle \psi^l_T| V | R S\rangle.
\label{RSHPsiTrcalc}
\end{aligned}$$ Then, with the help of Eqs.([\[PER\]](#PER){reference-type="ref" reference="PER"}) and ([\[RSPsiTr\]](#RSPsiTr){reference-type="ref" reference="RSPsiTr"}), taking $^4$He as an example, the potential energy part becomes, $$\begin{aligned}
\resizebox{.9\hsize}{!}{$
\!\!\!\!\!\!\!\!\! \langle R S| V | \psi^r_T \rangle \!=\!
\left\langle \!\! S \! \left| \left\{\! \sum\limits_{i<j} \left[V_{ij}^{NN}(r_{ij}) \!+\! V^{EM}_{ij}(r_{ij}) \right] \!\! \right\}
\! \! \sideset{}{^r} \prod\limits_{i<j} \! \!
\left[
\sum\limits_{p=1}^6   f_{ij}^p (r_{ij})  O_{ij}^p\!
\right]
\! \sum\limits_{N=1}^{96} \! \phi_N
\right| \! N \!\! \right\rangle$,} \\
\resizebox{.938\hsize}{!}{ $
\!\!\! \langle \psi^l_T| V | R S\rangle \!=\!
\! \sum \limits_{N=1}^{96}  \!\! \left\langle \!\! N \! \left| \phi^*_N \!
 \left\{\! \sum\limits_{i<j} \left[V_{ij}^{NN}(r_{ij}) \!+\! V^{EM}_{ij}(r_{ij}) \right]\!\! \right\}
\!\! \sideset{}{^l} \prod\limits_{i<j}\!
\left[
\sum\limits_{p=1}^6 {f_{ij}^p}^* (r_{ij})  O_{ij}^p\!
\right] \!
\right| \! S \! \right\rangle$.}
\end{aligned}$$

For the kinetic energy operator $T$ we have, $$\begin{aligned}
\resizebox{.87222\hsize}{!}{ $
\!\!\!\langle R S| T | \psi^r_T \rangle \!=\!\!\sum \limits_{i=1}^4 \! \frac{-\hbar^2\nabla_i^2}{2m}
\langle R S | \psi^r_T \rangle
\!=\! -\frac{\hbar^2}{2m} \!\sum \limits_{i=1}^4 \!\! \left( \frac{d^2 }{dx_i^2} \!+\! \frac{d^2 }{dy_i^2} \!+\! \frac{d^2 }{dz_i^2} \right) \!\!
\langle R S | \psi^r_T \rangle$,}
\label{KE2ndrorder} \\
\resizebox{.87222\hsize}{!}{ $
\!\!\!\langle \psi^l_T  | T | R S \rangle \!=\!\!\sum \limits_{i=1}^4\! \frac{-\hbar^2\nabla_i^2}{2m}
\langle \psi^l_T | RS \rangle
\!=\! -\frac{\hbar^2}{2m} \!\sum \limits_{i=1}^4\!\! \left( \frac{d^2 }{dx_i^2} \!+\! \frac{d^2 }{dy_i^2} \!+\! \frac{d^2 }{dz_i^2} \right) \!\!
\langle \psi^l_T | RS \rangle .$}
\label{KE2ndlorder}
\end{aligned}$$ The order derivatives in Eqs.([\[KE2ndrorder\]](#KE2ndrorder){reference-type="ref" reference="KE2ndrorder"}) and ([\[KE2ndlorder\]](#KE2ndlorder){reference-type="ref" reference="KE2ndlorder"}) are calculated numerically by using the order central finite difference formula ([@Fornberg88a])[^1].

In our PIMC calculations for $^4$He, we include 2000 steps in one block. A step means any one of the trial moves described in section [\[secSamplingMethod\]](#secSamplingMethod){reference-type="ref" reference="secSamplingMethod"}, it can be either accepted or rejected. We adjusted the number of beads for multi-level sampling as well as the step parameters for regular sampling, and find out the samples are uncorrelated after 125 steps so that each block is uncorrelated with the others (we make sure the samples of the root mean square radius $r_m$ at the middle bead are uncorrelated). We typically calculate the ground-state energy $E_0$, $r_m^2$, potential $V^{NN}+V^{EM}$ along the beads, and one-particle number density $\rho(r)$. We begin to take samples after running several blocks from the initial condition in order to reach the equilibrium.

<figure id="energy">
<embed src="Figures/energy.eps" />
<figcaption>Energy vs. time step <span class="math inline"><em>Δ</em><em>τ</em></span> for different total imaginary time <span class="math inline"><em>τ</em></span> for <span class="math inline"><sup>4</sup></span>He based on the AV6’ potential (quadratic range). </figcaption>
</figure>

<figure id="energyall">
<embed src="Figures/energyall.eps" />
<figcaption>Energy vs. time step <span class="math inline"><em>Δ</em><em>τ</em></span> for different total imaginary time <span class="math inline"><em>τ</em></span> for <span class="math inline"><sup>4</sup></span>He based on the AV6’ potential (wide range). </figcaption>
</figure>

<figure id="energyN2LO">
<embed src="Figures/energyN2LO.eps" />
<figcaption>Energy vs. time step <span class="math inline"><em>Δ</em><em>τ</em></span> for different total imaginary time <span class="math inline"><em>τ</em></span> for <span class="math inline"><sup>4</sup></span>He based on the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction (linear range). </figcaption>
</figure>

<figure id="energyallN2LO">
<embed src="Figures/energyallN2LO.eps" />
<figcaption>Energy vs. time step <span class="math inline"><em>Δ</em><em>τ</em></span> for different total imaginary time <span class="math inline"><em>τ</em></span> for <span class="math inline"><sup>4</sup></span>He based on the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction (wide range). </figcaption>
</figure>

In Fig. [1](#energy){reference-type="ref" reference="energy"}, we show the calculation of the $^4$He ground state energy $E_0$ for different total imaginary time $\tau=0.15\textrm{ MeV}^{-1}$, $\tau=0.2\textrm{ MeV}^{-1}$ and $\tau=0.3\textrm{ MeV}^{-1}$, with various time steps $\Delta \tau$. As discussed in section [\[setup\]](#setup){reference-type="ref" reference="setup"}, at $\tau=0.2\textrm{ MeV}^{-1}$, we can expect the true ground state energy $E_0$ for $^4$He to be located within our calculated ground state energy within its error bar. We added $\tau=0.15\textrm{ MeV}^{-1}$ and $\tau=0.3\textrm{ MeV}^{-1}$ for comparison. Particularly, we can see that for $\Delta \tau < 5 \times 10^{-4} \textrm{ MeV}^{-1}$, for $\tau=0.2\textrm{ MeV}^{-1}$ and $\tau=0.3\textrm{ MeV}^{-1}$, all of the calculated $E_0$ are almost the same within their error bars. For $\tau=0.15\textrm{ MeV}^{-1}$, the smallest $\Delta \tau$ we use is $1.5 \times 10^{-4} \textrm{ MeV}^{-1}$ which means 1000 short-time propagators and 1001 beads, and its $E_0$ is $-26.155 \pm 0.008$ MeV. For $\tau=0.2\textrm{ MeV}^{-1}$, the smallest $\Delta \tau$ we use is $1.5 \times 10^{-4} \textrm{ MeV}^{-1}$ which means 1333 short-time propagators and 1334 beads, and its $E_0$ is $-26.162 \pm 0.004$ MeV. For $\tau=0.3\textrm{ MeV}^{-1}$, the smallest $\Delta \tau$ we use is $2 \times 10^{-4} \textrm{ MeV}^{-1}$ which means 1500 short-time propagators and 1501 beads, and its $E_0$ is $-26.173 \pm 0.006$ MeV.

Also, as pointed out in section [\[propagator\]](#propagator){reference-type="ref" reference="propagator"} and by Eq.([\[Oextrapolation\]](#Oextrapolation){reference-type="ref" reference="Oextrapolation"}), for the AV6' interaction, our PIMC results should contain even orders of $\Delta \tau$ error comparing with the true ground state results for small time step $\Delta \tau$. Usually we do an extrapolation at $\Delta \tau^2$ order, $$\langle \hat{O} (\Delta \tau) \rangle
= \langle \hat{O} \rangle
+  C_{2} \Delta \tau^{2}.
\label{OextrapolationO2}$$ In order to do extrapolation by using Eq.([\[OextrapolationO2\]](#OextrapolationO2){reference-type="ref" reference="OextrapolationO2"}), we need to find the range of $\Delta \tau$ where the error of $\Delta \tau^2$ dominates, so that we can observe a clear $\Delta \tau^2$ dependence of $\langle \hat{O} (\Delta \tau) \rangle$. As a rough estimation, by looking at Eq.([\[Oextrapolation\]](#Oextrapolation){reference-type="ref" reference="Oextrapolation"}) we would require $|\frac{ C_2 \Delta \tau^2  }{C_4 \Delta \tau^4}| \gg 1$. There are combinations of commutator terms of kinetic energy $T$ and potential $V$ in coefficients $C_2$ and $C_4$. For example there can be $TTV$ in $C_2$ and $TTTTV$ in $C_4$ and we can roughly estimate $|\frac{ C_2 \Delta \tau^2  }{C_4 \Delta \tau^4}|$ as $|\frac{ Re \langle \Psi_T | TTV  | \psi_T \rangle  }{Re \langle \Psi_T | TTTTV  | \psi_T \rangle \Delta \tau^2 }|$. For the AV6' interaction, the magnitude of $T$ and $V$ are $10^2$ MeV order, so $|\frac{ C_2 \Delta \tau^2  }{C_4 \Delta \tau^4}| \approx |\frac{ Re \langle \Psi_T | TTV  | \psi_T \rangle  }{Re \langle \Psi_T | TTTTV  | \psi_T \rangle \Delta \tau^2 }|$ may be roughly estimated as $|\frac{ C_2 \Delta \tau^2  }{C_4 \Delta \tau^4}| \approx |\frac{ 10^6  }{10^{10} \Delta \tau^2 }|=|\frac{ 1  }{10^{4} \Delta \tau^2 }|$. In order to make sure $|\frac{ C_2 \Delta \tau^2  }{C_4 \Delta \tau^4}| \gg 1$, we may expect $\Delta \tau$ to be around $10^{-4} \sim 10^{-3} \textrm{ MeV}^{-1}$.

We find that in Fig. [1](#energy){reference-type="ref" reference="energy"} we can observe a clear $\Delta \tau^2$ dependence when $\Delta \tau < 1.3 \times 10^{-3} \textrm{ MeV}^{-1}$, and by using Eq.([\[OextrapolationO2\]](#OextrapolationO2){reference-type="ref" reference="OextrapolationO2"}), the true ground state energy $E_0$ is extrapolated to $-26.16(1)$ MeV. This is consistent with GFMC result ([@WiringaPieper02a]) which is $E_0=-26.15(2)$ MeV. This is reasonable because in this work, we are summing over all the spin and isospin states like GFMC does. So our results should be comparable with GFMC's. The difference is that GFMC is a DMC method based on Eq.([\[DMCopexpdetail\]](#DMCopexpdetail){reference-type="ref" reference="DMCopexpdetail"}), and we are doing a PIMC calculation based on Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}).

In Fig. [3](#energyN2LO){reference-type="ref" reference="energyN2LO"} we show the results of $^4$He based on the local chiral N$^2$LO two-body interaction. We choose the coordinate space cutoff ([@Gerzerlis14a]) as $R_0=1.2$ fm. As discussed in section [\[propagator\]](#propagator){reference-type="ref" reference="propagator"} and Eq.([\[ON2LOextrapolation\]](#ON2LOextrapolation){reference-type="ref" reference="ON2LOextrapolation"}), due to the existence of the spin-orbit operator, a $\Delta \tau$ error will exist in evaluating $\langle \hat{O} (\Delta \tau) \rangle$. We do observe the $\Delta \tau$ error dominates when $\Delta \tau < 1.3 \times 10^{-3} \textrm{ MeV}^{-1}$. So we do a linear extrapolation in this range for the chiral interaction, $$\langle \hat{O} (\Delta \tau) \rangle
= \langle \hat{O} \rangle
+  C_{1} \Delta \tau,
\label{OextrapolationO1}$$ and the extrapolated ground-state energy is found to be $E_0=-24.99(1)$ MeV.

Fig. [2](#energyall){reference-type="ref" reference="energyall"} shows a wider range of $\Delta \tau$ than Fig. [1](#energy){reference-type="ref" reference="energy"}, and we use Eq.([\[PIMCUSdetail\]](#PIMCUSdetail){reference-type="ref" reference="PIMCUSdetail"}) up to $\Delta \tau^4$ in both the numerator and the denominator to do the fitting for all the data points. In Fig. [4](#energyallN2LO){reference-type="ref" reference="energyallN2LO"} we fit the wide range of the data by using Eq.([\[ON2LOextrapolation\]](#ON2LOextrapolation){reference-type="ref" reference="ON2LOextrapolation"}) up to $\Delta \tau^3$.

::: {#TablePIMC2}
   $^A$Z    $E^{\text{PIMC}}_0$ (MeV)   $\tau$ (MeV$^{-1}$)   $E^{\textrm{GFMC}}_0$ (MeV)   $E^{\textrm{EXPT}}_0$ (MeV)
  -------- --------------------------- --------------------- ----------------------------- -----------------------------
   $^2$H           $-2.24(4)$                   0.5                                                    -2.22
   $^3$H           $-7.953(5)$                  0.4                   $-7.95(1)$                       -8.48
   $^3$He          $-7.336(6)$                  0.5                                                    -7.72
   $^4$He         $-26.162(4)$                  0.2                   $-26.15(2)$                     -28.30

  : The AV6' interaction based light nuclei ground state energies.
:::

::: {#TablePIMCN2LO}
   $^A$Z    $E^{\text{PIMC}}_0$ (MeV)   $\tau$ (MeV$^{-1}$)   $E^{\textrm{GFMC}}_0$ (MeV)   $E^{\textrm{AFDMC}}_0$ (MeV)   $E^{\textrm{EXPT}}_0$ (MeV)
  -------- --------------------------- --------------------- ----------------------------- ------------------------------ -----------------------------
   $^2$H           $-2.203(2)$                  0.5                                                                                   -2.22
   $^3$H           $-7.74(1)$                   0.4                   $-7.74(1)$                     $-7.76(3)$                       -8.48
   $^3$He          $-7.11(1)$                   0.5                   $-7.01(1)$                     $-7.12(3)$                       -7.72
   $^4$He          $-25.00(1)$                  0.2                   $-24.86(1)$                   $-25.17(5)$                      -28.30

  : The local chiral N$^2$LO interaction based light nuclei ground state energies.
:::

The ground state energy for all the $A\leq 4$ nuclei are listed in Table [1](#TablePIMC2){reference-type="ref" reference="TablePIMC2"} for the AV6' interaction and in Table [2](#TablePIMCN2LO){reference-type="ref" reference="TablePIMCN2LO"} for the chiral N$^2$LO interaction. The GFMC and AFDMC results ([@Lonardoni2018PRC]) are listed for comparison. Overall, all the PIMC, GFMC and AFDMC results are consistent with each other within $1\%$ error. We also listed the experimental value of the binding energies ([@WiringaPieper02a; @Lee2020FiP; @wiki:NBE]) for comparison. The difference between the experimental values $E^{\textrm{EXPT}}_0$ and our results is mainly due to the absence of the three body interactions in our calculations.

[^1]: For example, for $x_i$ the x coordinate of particle i, it is calculated as, $$\begin{aligned}
    \frac{d^2 \langle R S | \psi^r_T \rangle }{d x_i^2}  &=
    \frac{  \langle R_{x_i^+} S | \psi^r_T \rangle
    \! + \! \langle R_{x_i^-} S | \psi^r_T \rangle
    \! - \! 2 \langle R S | \psi^r_T \rangle    }{\Delta^2}, \\
    \frac{d^2 \langle \psi^l_T  | RS \rangle }{d x_i^2}  &=
    \frac{  \langle \psi^l_T  | R_{x_i^+} S \rangle
    \! + \! \langle \psi^l_T  |  R_{x_i^-} S  \rangle
    \! - \! 2 \langle \psi^l_T  | RS \rangle    }{\Delta^2} .
    \end{aligned}$$ where $\Delta$ is the spatial finite difference which is set as about $10^{-2}$ fm in our calculations. $R_{x_i^+}$ means keeping all the other coordinates in the configuration of the system $R$ the same and just change $x_i$ to $x_i+\Delta$, and $R_{x_i^-}$ means change $x_i$ to $x_i-\Delta$.
