---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-037-411-preparations
section_title: "Preparations"
section_number: 4.1.1
pages: 90-103
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.983
---
[]{#setup label="setup"}

The exact PIMC expectation value of operator $\hat{O}$ is calculated by Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}) and therefore Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}), and we need to choose a proper total imaginary time $\tau$ and time step $\Delta \tau$ to project out the ground state $|\Phi_0\rangle$. In this section, we discuss the choice of $\tau$ and $\Delta \tau$ and use $^4$He as an example.

From Eq.([\[eHPsiT\]](#eHPsiT){reference-type="ref" reference="eHPsiT"}) we can see that, the residual amount of excited states depends on the ratio $a_i/a_0$ and the factor $e^{-(E_i-E_0)\tau_1}$. We have to make sure that the coefficient of the first excited state $| \Phi_1 \rangle$ is negligible compared with the ground state $| \Phi_0 \rangle$.

The experimental ground state energy $E_0$ of $^4$He is about -28.3 MeV and the first excited state energy $E_1$ is the energy of a separated nucleon and triton, -8 MeV ([@Tiley92a]). The energy difference $E_1-E_0$ is about -20 MeV. If we choose $\tau_1=0.1 \textrm{ MeV}^{-1}$ then $e^{-(E_1-E_0)\tau_1}$ will be $e^{-2}\approx 0.135$. If there is only $|\Phi_0\rangle$ and $|\Psi_1\rangle$ in $|\Psi_T\rangle$, and if $|a_1/a_0|$ is small enough, then the percentage of the first excited state $|\Phi_1 \rangle$ in $|\Psi_T \rangle$ will be greatly suppressed by $|a_1/a_0 e^{-(E_1-E_0)\tau_1}|$, therefore $e^{-H \tau_1} |\Psi_T \rangle$ is dominated by the ground state $|\Phi_0 \rangle$. In fact, if there are other excited states in $|\Psi_T \rangle$, the ground state $|\Phi_0 \rangle$ will be projected out even sooner, because $|a_1/a_0|$ will be smaller for a good trial wave function and other excited states $|\Phi_i\rangle$ will die out faster than $|\Phi_1\rangle$ due to the factor $|a_i/a_0 e^{-(E_i-E_0)\tau_1}|$. So, even a less than $0.1 \textrm{ MeV}^{-1}$ imaginary time $\tau_1$ may still be adequate.

The analysis above suggests that $\tau_1=0.1 \textrm{ MeV}^{-1}$ should be enough for our PIMC to project out the ground state. Since we usually put operator $\hat{O}$ in the middle of two propagators as $\langle \Psi_T| e^{-H \tau_1}  \hat{O} e^{-H \tau_2} | \Psi_T \rangle$ as shown in Eq.([\[PIMCopexpdetail\]](#PIMCopexpdetail){reference-type="ref" reference="PIMCopexpdetail"}), and we usually set $\tau_1=\tau_2$, so we can conclude that the total imaginary time $\tau$ for our PIMC calculations can be set as $\tau=2\tau_1=2\times 0.1=0.2 \textrm{ MeV}^{-1}$. In our PIMC calculations, besides using $\tau=0.2 \textrm{ MeV}^{-1}$, and we also show results with $\tau=0.15 \textrm{ MeV}^{-1}$ and $\tau=0.3 \textrm{ MeV}^{-1}$ for comparisons. The total imaginary time for chiral N$^2$LO interaction has a similar range and $\tau=0.2 \textrm{ MeV}^{-1}$ should be enough as well.

Given a total imaginary time $\tau$, for the time step $\Delta \tau$, we need to consider the computational cost and the accuracy. In GFMC ([@Carlson87a]), $\Delta \tau$ is usually chosen to be $10^{-5} \sim 10^{-4} \textrm{ MeV}^{-1}$. In our PIMC calculation, we find that a $10^{-4} \sim 10^{-3} \textrm{ MeV}^{-1}$ time step $\Delta \tau$ works reasonably well. Depending on $\tau$ and $\Delta \tau$, the number of beads for PIMC ranges from 41 to 1501. In the most time consuming case, for $\tau=0.3 \textrm{ MeV}^{-1}$ and $\Delta \tau=2\times 10^{-4} \textrm{ MeV}^{-1}$, we need 1500 short-time propagators and therefore 1501 beads. Such a calculation (all the calculations are performed at the Agave Cluster at Research Computing at Arizona State University), in order to reach a less than $0.02\textrm{ MeV}$ error in the ground state energy calculation, takes about 20 thousand core hours for the chiral N$^2$LO interaction and 13 thousand core hours for the AV6' interaction. For 41 beads it takes about 240 core hours to reach less than $0.02\textrm{ MeV}$ error, which means it can be done on a modern laptop in few days or less.

## Calculations {#secResultCalc}

The calculation of the ground state energy $E_0$ can be recast into the form of Eq.([\[OABP\]](#OABP){reference-type="ref" reference="OABP"}) as discussed in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}, with the operator $\hat{O}$ being the Hamiltonian $H=T+V$. And we calculate the ground state energy $E_0$ by $$E_0 (\Delta \tau)
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

## Verifications {#secVerify}

In order to further support our conclusion that $\tau=0.2\textrm{ MeV}^{-1}$ indeed projected out the ground state and therefore our PIMC results are reliable, we calculate the potential $V=V^{NN}+V^{EM}$ along all the beads on the path. This is a typical quantity to calculate in PIMC calculations ([@Schmidt2000JCP]). The calculation is done in the same way as introduced in section [\[Recast\]](#Recast){reference-type="ref" reference="Recast"}. We just need to use the potential operator $V$ as the operator $\hat{O}$, and we place the $V$ at each imaginary time position from bead 0 to the last bead $N$ on the path. In other words, the $g^V_{lr,M}(\mathcal{R})$ in Eq.([\[gVRlrdef2\]](#gVRlrdef2){reference-type="ref" reference="gVRlrdef2"}) needs to be calculated from $M=0$ to $M=N={\tau}/{\Delta \tau}$. In this way, we are actually calculating $\langle {V}(\tau_1) \rangle$ which is, $$\begin{aligned}
\langle {V}(\tau_1) \rangle
= \frac{ Re  \langle \Psi_T| e^{-H \tau_1}  \left(V^{NN}+V^{EM}\right) e^{-H (\tau-\tau_1) } | \Psi_T \rangle  }
{ Re \langle \Psi_T| e^{-H \tau} | \Psi_T \rangle} ,
\label{potentialbeads}
\end{aligned}$$ where $\tau_1$ ranges from 0 MeV$^{-1}$ to $\tau$ as we put the $V$ operator from bead 0 to bead $N$. $\langle {V}(\tau_1) \rangle$ is symmetric around $\tau_1=\tau/2$. When $\tau/2$ is big enough to project out the ground state, $\langle {V}(\tau/2) \rangle$ is the ground state potential energy.

<figure id="potential">
<embed src="Figures/potential.eps" />
<figcaption>The potential energy along the beads for <span class="math inline"><em>τ</em> = 0.2</span> and 0.3 <span class="math inline">MeV<sup>−1</sup></span> for <span class="math inline"><sup>4</sup></span>He based on the AV6’ interaction. </figcaption>
</figure>

<figure id="potentialN2LO">
<embed src="Figures/potentialN2LO.eps" />
<figcaption>The potential energy along the beads for <span class="math inline"><em>τ</em> = 0.2</span> and 0.3 <span class="math inline">MeV<sup>−1</sup></span> for <span class="math inline"><sup>4</sup></span>He based on the local chiral N<span class="math inline"><sup>2</sup></span>LO interaction.</figcaption>
</figure>

In Fig. [5](#potential){reference-type="ref" reference="potential"}[^2], we show the results of $\langle {V}(\tau_1) \rangle$ as a functions of $\tau_1$ for $\tau=0.2$ MeV$^{-1}$ and $\tau=0.3$ MeV$^{-1}$. On the upper panel of Fig. [5](#potential){reference-type="ref" reference="potential"}, we show for different time step $\Delta \tau$ how $\langle {V}(\tau_1) \rangle$ change as $\tau_1$ from 0 MeV$^{-1}$ to the total imaginary time $\tau=0.2$ MeV$^{-1}$. As expected, since PIMC is projecting out the Hamiltonian's ground state, and the Hamiltonian's ground state is not the same as the potential operator's eigenstate, the time step error introduced by $\Delta \tau$ will have noticeable impact on $\langle {V}(\tau_1) \rangle$. That is why the curve of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ are different for different $\Delta \tau$. However, as $\Delta \tau$ decreases, time step error will become smaller and smaller. And indeed, as we can see, the result for $\Delta \tau=1.5\times 10^{-4}$ MeV$^{-1}$ almost coincides with that of $\Delta \tau=2.5\times 10^{-4}$ MeV$^{-1}$. $\langle {V}(\tau_1) \rangle$ is about $-127\sim-123$ MeV. It looks like $\langle {V}(\tau_1) \rangle$ has converged when $\Delta \tau \leq 2.5\times 10^{-4}$ MeV$^{-1}$. This is a clear signal that a stable eigenstate of the Hamiltonian for $\tau=0.2$ MeV$^{-1}$ has been reached, and smaller $\Delta \tau$ and therefore more beads will not improve the convergence. Furthermore, in order to verify if this eigenstate is truly the ground state, we calculate for a larger total imaginary time of $\tau=0.3$ MeV$^{-1}$ with a similar time step $\Delta \tau=2 \times 10^{-4}$ MeV$^{-1}$, i.e. 1501 beads. The result is in the lower panel of Fig. [5](#potential){reference-type="ref" reference="potential"}. Indeed, the curve of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ is almost the same as the $\tau=0.2$ MeV$^{-1}$ and $\Delta \tau \leq 2.5\times 10^{-4}$ MeV$^{-1}$ cases. This means further increasing the total time $\tau$ will not change the state, so the stable state reached for $\tau=0.2$ MeV$^{-1}$ must be the ground state.

Therefore, the ground state of the Hamiltonian is indeed reached when $\tau=0.2$ MeV$^{-1}$, and $\Delta \tau$ around $1.5\sim2.5\times 10^{-4}$ MeV$^{-1}$ is small enough. Besides, from Fig. [5](#potential){reference-type="ref" reference="potential"} we can see that in the area when $0.075\textrm{ MeV}^{-1}\leq\tau_1\leq0.125\textrm{ MeV}^{-1}$ for $\tau=0.2$ MeV$^{-1}$, and the area when $0.075\textrm{ MeV}^{-1}\leq\tau_1\leq0.225\textrm{ MeV}^{-1}$ for $\tau=0.3$ MeV$^{-1}$, the curves of $\langle {V}(\tau_1) \rangle$ vs. $\tau_1$ are almost flat. So that even $\tau=2\times0.075=0.15$ MeV$^{-1}$ may be sufficient to project out the ground state. Fig. [6](#potentialN2LO){reference-type="ref" reference="potentialN2LO"} is a similar graph for the local chiral interaction which also indicates $\tau=0.2$ MeV$^{-1}$ is sufficient[^3].

<figure id="figPIMCstructR">
<embed src="Figures/PIMCstructR.eps" style="width:95.03%" />
<figcaption>PIMC leading order structure function <span class="math inline"><em>R</em><sub>S</sub><sup>(1)</sup>(<em>τ</em>,<em>Δ</em><em>τ</em>)</span>. </figcaption>
</figure>

Besides checking the potential along the beads, the robustness of the ground state energy PIMC calculation can be understood as follows.

The trial state $| \Psi_T \rangle$, after operating with $\left[U(\Delta \tau)\right]^N$, can be expanded by the eigenstates of the Hamiltonian, $$\begin{aligned}
\left[U(\Delta \tau)\right]^N |\Psi_T \rangle = \sum_{n=0}^{\infty} A_n(\tau,\Delta \tau) |\Phi_n\rangle
=A_0(\tau,\Delta \tau)\left[ | \Phi_0 \rangle  +  \sum_{i=1}^{+\infty} \frac{A_i(\tau,\Delta \tau)}{A_0(\tau,\Delta \tau)} | \Phi_i \rangle \right] . ~~~
\label{UdtNexp}
\end{aligned}$$ where $A_n(\tau,\Delta \tau)$ are the coefficients which depend on $\tau$ and $\Delta \tau$ for $|\Phi_n\rangle$. We know that $\lim\limits_{\Delta \tau \rightarrow 0} \left[U(\Delta \tau)\right]^N= e^{-H \tau}$ and we also notice from Eq.([\[eHPsiT\]](#eHPsiT){reference-type="ref" reference="eHPsiT"}) that, $$e^{-H \tau} |\Psi_T \rangle =
a_0 e^{-E_0 \tau}
\left[ | \Phi_0 \rangle +  \sum_{i=1}^{\infty}\frac{a_i}{a_0}e^{-(E_i-E_0) \tau} | \Phi_i \rangle  \right],
\label{eHPsiTau}$$ So, comparing Eq.([\[UdtNexp\]](#UdtNexp){reference-type="ref" reference="UdtNexp"}) and Eq.([\[eHPsiTau\]](#eHPsiTau){reference-type="ref" reference="eHPsiTau"}) we find that for $\Delta \tau \rightarrow 0$,

::: flalign
\_ A_0(,) & = a_0 e\^-E_0 ,\
\_ &= e\^-(E_n-E_0) \_ []{#ratioAnA0 label="ratioAnA0"} .
:::

We calculate the ground state energy by using Eq.([\[PIMCopexpdetailE0dtau\]](#PIMCopexpdetailE0dtau){reference-type="ref" reference="PIMCopexpdetailE0dtau"}), the two parts in it are essentially the same and we pick one of them to take a closer look. We find $$\frac{\langle \Psi_T| H [U(\Delta \tau)]^N  | \Psi_T \rangle}{\langle \Psi_T| [U(\Delta \tau)]^N  | \Psi_T \rangle}
= E_0 \frac{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  }
\equiv E_0 R_{\text{S}}(\tau,\Delta \tau) ,
\label{PIMCstrucfull}$$ since Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) is real, we define a real function $R_{\text{S}}(\tau,\Delta \tau)$ as our PIMC error structure function, $$R_{\text{S}}(\tau,\Delta \tau)
\equiv Re \frac{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{+\infty}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  } ,
\label{PIMCstrucRs}$$ and we can define its cutoff functions $R^{(n)}_{\text{S}}(\tau,\Delta \tau)$ such that $$R^{(n)}_{\text{S}}(\tau,\Delta \tau)
\equiv Re \frac{1+ \sum_{i=1}^{n}\frac{a_i^* A_i(\tau,\Delta \tau) E_i }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \sum_{i=1}^{n}\frac{a_i^* A_i(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  } .
\label{PIMCstrucRsn}$$ Considering Eq.([\[ratioAnA0\]](#ratioAnA0){reference-type="ref" reference="ratioAnA0"}), $R_{\text{S}}(\tau,\Delta \tau)$ and $R^{(n)}_{\text{S}}(\tau,\Delta \tau)$ will converge to 1 when $\tau$ is big enough and $\Delta \tau$ is small enough, and the energy will converge to $E_0$. We find that the structure Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) may be much less sensitive to $\Delta \tau$ than one may expect. We can assume the errors in Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) are mostly coming from the leading order errors in its denominator and the numerator. If the leading order error is from the first excited state, Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) can be approximated as $$\frac{\langle \Psi_T| H [U(\Delta \tau)]^N  | \Psi_T \rangle}{\langle \Psi_T| [U(\Delta \tau)]^N  | \Psi_T \rangle}
\approx E_0 \times Re \frac{1+ \frac{a_1^* A_1(\tau,\Delta \tau) E_1 }{a_0^* A_0(\tau,\Delta \tau) E_0 }  }
{1+ \frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }  }
=E_0 R^{(1)}_{\text{S}}(\tau,\Delta \tau) ,
\label{PIMCstruc1}$$ and since Eq.([\[PIMCstrucfull\]](#PIMCstrucfull){reference-type="ref" reference="PIMCstrucfull"}) is real, we can assume $\frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }$ in Eq.([\[PIMCstruc1\]](#PIMCstruc1){reference-type="ref" reference="PIMCstruc1"}) is mostly real and we can define a real function $B_1(\tau,\Delta \tau)$ as $$B_1(\tau,\Delta \tau) = Re \frac{a_1^* A_1(\tau,\Delta \tau) }{a_0^* A_0(\tau,\Delta \tau) }
\label{PIMCstrucB1}$$ such that $$R_{\text{S}}(\tau,\Delta \tau) \approx
R^{(1)}_{\text{S}}(\tau,\Delta \tau) \approx
\frac{ 1+B_1(\tau,\Delta \tau) \frac{E_1}{E_0} }{1+B_1(\tau,\Delta \tau)}.
\label{PIMCstrucRsB1}$$

Therefore, our result $E(\Delta \tau)$ in Eq.([\[PIMCopexpdetailE0dtau\]](#PIMCopexpdetailE0dtau){reference-type="ref" reference="PIMCopexpdetailE0dtau"}) will be very close to the true expectation $E_0$, as long as Eq.([\[PIMCstrucRsB1\]](#PIMCstrucRsB1){reference-type="ref" reference="PIMCstrucRsB1"}) is close to 1. In Fig. [7](#figPIMCstructR){reference-type="ref" reference="figPIMCstructR"} we plot the contour graph and show how the value of the leading order structure function $R^{(1)}_{\text{S}}(\tau,\Delta \tau)$ changes as $B_1(\tau,\Delta \tau)$ and $E_1/E_0$ change. We find as long as $B_1(\tau,\Delta \tau) \in [-0.1,0.1]$ (which is a reasonable range for a proper $\Delta \tau$), $R^{(1)}_{\text{S}}(\tau,\Delta \tau)$ will be close to 1 (the green area), it fluctuates from 0.9 to 1.1 so $E(\Delta \tau)$ will be around $E_0$ with at most $10\%$ error or so. In fact, our results in section [0.1](#secResultCalc){reference-type="ref" reference="secResultCalc"} shows that $E(\Delta \tau)$ in PIMC works even better. From Figs. [2](#energyall){reference-type="ref" reference="energyall"} and [4](#energyallN2LO){reference-type="ref" reference="energyallN2LO"} we see that even with a wide range of $\Delta \tau$, the difference between $E(\Delta \tau)$ and $E_0$ is less than $3\%$ which is well below $10\%$. The robust $E(\Delta \tau)$ value also indicates the ground state path is robust, so the expectation values of other operators should be reliable too.

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

[^2]: Note that the potential operators and the Hamiltonian do not commute, so the eigenstates of the potential operators and the Hamiltonian are not the same. So even when the system reaches the ground state of its Hamiltonian, this ground state $| \Phi_0 \rangle$ is not an eigenstate of the potential operators. So $\langle {V}(\tau_1) \rangle$ has larger fluctuations than $\langle H(\tau_1) \rangle$. So in order to make Fig. [5](#potential){reference-type="ref" reference="potential"} look 'smooth', we need to take a longer computation time than computing the ground state energy.

[^3]: In order to save computation time, we did not include spin-orbit interaction, but it does not alter the conclusion. Fig. [6](#potentialN2LO){reference-type="ref" reference="potentialN2LO"} is not as smooth as Fig. [5](#potential){reference-type="ref" reference="potential"} simply because we used fewer core hours for it than we did for Fig. [5](#potential){reference-type="ref" reference="potential"}.
