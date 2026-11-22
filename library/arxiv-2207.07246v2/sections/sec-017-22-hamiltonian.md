---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-017-22-hamiltonian
section_title: "Hamiltonian"
section_number: 2.2
pages: 29-33
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.98
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secHamilton label="secHamilton"}

In this work, the Hamiltonian $H$ of our light nuclei calculations is non-relativistic. It can be written as, $$H = \sum_{i=1}^A \frac{\bm{p}_i^2}{2m}  + \sum_{i<j}V_{ij}, \label{PIMCHamilton}$$ where $A$ is total number of nucleons in the system, $\bm{p}_i=-i\hbar \nabla_i$ is the momentum of particle $i$ in real space. The complete two body interaction for a given $ij$ pair of particles, $V_{ij}$, is composed of the nucleon-nucleon interaction $V^{NN}_{ij}$ and the electric magnetic force $V^{EM}_{ij}$, $$V_{ij}=V_{ij}^{NN}+V^{EM}_{ij}.\label{Vij}$$

By using both the local chiral interaction with N$^2$LO ([@Gerzerlis14a; @Lynn2017PRC; @Lonardoni2018PRC]) and the Argonne $v'_6$ (AV6') interaction ([@WiringaPieper02a]), we use PIMC to calculate the ground state properties of light nuclei such as $^2$H, $^3$H, $^3$He and $^4$He. The nucleon-nucleon interaction is written as, $$V^{NN}_{ij}=\sum_{p=1}^7 v_p(r_{ij}) O_{ij}^p , \label{AV6'}$$ where $r_{ij}$ is the length of $\bm{r}_{ij}$, $v_p(r_{ij})$ is the radial function for the $p^{\text{th}}$ operator, and they are different for chiral and AV6' interactions. The first 6 of the operators $O_{ij}^p$ are 1, $\bm{\tau}_i \cdot \bm{\tau}_j$, $\bm{\sigma}_i \cdot \bm{\sigma}_j$, $\bm{\sigma}_i \cdot \bm{\sigma}_j \bm{\tau}_i \cdot \bm{\tau}_j$, $S_{ij}$ and $S_{ij} \bm{\tau}_i \cdot \bm{\tau}_j$, where $\bm{\sigma}$ and $\bm{\tau}$ are spin and isospin operators. The tensor force $S_{ij}$ which comes from one-pion-exchange (OPE) is , $$S_{ij}=3 \bm{\sigma}_i \cdot \hat{r} \bm{\sigma}_j \cdot \hat{r} - \bm{\sigma}_i \cdot \bm{\sigma}_j , \label{AV6'O}$$ where $\hat{r}$ is the unit vector of $\bm{r}_{ij}$. Note that the spin term $\bm{\sigma}_i \cdot \bm{\sigma}_j = 2P_{ij}^{\sigma} -1$ and isospin term $\bm{\tau}_i \cdot \bm{\tau}_j = 2P_{ij}^{\tau} -1$ where $P_{ij}^{\sigma}$ and $P_{ij}^{\tau}$ are spin and isospin exchange operators. The tensor force flips the spins of nucleons.

The AV6' is a local interaction, which is a six operator truncation of the full Argonne AV18 NN interaction ([@Wiringa95PRC]) which consists of 18 operators. The prime symbol means that the parameters in AV6' are refitted and therefore they are different from those in AV18. The AV6' only contain the first 6 operators, it does not have the operator $O_{ij}^7$, so its $v_7(r_{ij})=0$.

When we say a potential is local, the word 'local' means the operators can be determined once the positions of particles are given. If an interaction contains mostly local operators, it is a local interaction. If an interaction contains some non-local operators, usually like momentum operator $\bm{p}$ and/or powers of $\bm{p}$, it is 'non-local'. This is because momentum operator in real space is a differential operator, if it operates on a function $f(x)$ then we need to calculate the derivative of the function $f'(x)$. The value of $f(x)$ is not enough to determine $f'(x)$, we need to know the value of $f(x+dx)$ at $x+dx$ so that we can calculate $f'(x)$, so the information at the local point $x$ is not enough, information at $x+dx$ is needed, so it is called 'non-local'. If an interaction contains $\bm{p}^n$, then in order to compute $f^{(n)}(x)$ at $x$, we need to know all the non-local information of $f(x+dx)$, $f(x+2dx)$, \..., $f(x+ndx)$, so as the integer $n$ increase, the interaction will become more and more 'non-local'.

Chiral interactions from ChEFT are obtained based on a momentum expansion so they are naturally non-local, so computing them is usually not easy for real space QMC methods. However, it was shown that up to N$^2$LO, we are able to obtain a mostly local version of chiral interaction ([@Gerzerlis13a]) which is suitable for QMC calculations ([@Lynn14a; @Gerzerlis14a; @Lynn2017PRC; @Lonardoni2018PRL; @Lonardoni2018PRC]). For chiral local N$^2$LO interaction, it has the same 6 local operators as AV6', just with different radial functions. However it has the operator in the $V^{NN}_{ij}$ in Eq.([\[AV6\'\]](#AV6'){reference-type="ref" reference="AV6'"}), and it is the spin-orbit term ([@Lonardoni2018PRC]) which is $$O_{ij}^7 = \bm{L} \cdot \bm{S},$$ where $\bm{L}$ is the relative angular momentum operator and $\bm{S}$ is the total spin operator, $$\begin{aligned}
\bm{L} & = \frac{1}{2\hbar}(\bm{r}_i-\bm{r}_j) \times (\bm{p}_i-\bm{p}_j) , \\
\bm{S} & = \frac{1}{2} (\bm{\sigma}_i+\bm{\sigma}_j) .
\end{aligned}$$ With the radial function $v_7(r_{ij})$, the spin-orbit interaction $v_{LS}(r_{ij})$ is, $$v_{LS}(r_{ij})=v_7(r_{ij}) \bm{L} \cdot \bm{S},
\label{vlsrij}$$

The complete chiral N$^2$LO interaction also has a three body interaction ([@Lonardoni2018PRC]), $V_{3b}=\sum_{i<j<k}V_{ijk}$, which to the linear order approximation in the propagator can be straightforwardly added in light nuclei PIMC calculations. Since our PIMC calculation is mainly a benchmark test, we did not include three body interaction in this work.

For the electromagnetic (EM) force $V^{EM}_{ij}$, here we only consider the Coulomb force $v^{C}(r_{ij})$ between proton and proton (pp) which contains the proton charge form factor, $$V^{EM}_{ij}=v^{C}(r_{ij}) P^p_i P^p_j . \label{VEMpp}$$ where $P^p_i= (1+\tau_{iz}  )/2$ is the proton projection operator and $\tau_{iz}$ is the isospin z operator of $i^{\text{th}}$ particle. Coulomb interaction is long range and the NN interaction is short range (typically less than 2 fm).

The total potential energy operator $V$ is, $$V = \sum_{i<j} V_{ij} = \sum_{i<j} (V_{ij}^{NN}+V^{EM}_{ij}) . \label{PE}$$

<figure id="AV6N2LOradial">
<embed src="Figures/AV6N2LOradial.eps" />
<figcaption>Radial functions of the AV6’ and the chiral N<span class="math inline"><sup>2</sup></span>LO interaction. </figcaption>
</figure>

Fig. [1](#AV6N2LOradial){reference-type="ref" reference="AV6N2LOradial"} shows the radial function of each operator in AV6' and chiral N$^2$LO interaction. For the chiral N$^2$LO interactions, their spectral-function-regularization (SFR) cutoff $\tilde{\Lambda}$ is chosen to be 1000 MeV, and we list the radial functions for coordinate-space cutoff $R_0=1.0$ fm and $R_0=1.2$ fm cases ([@Gerzerlis14a]). We find that the chiral N$^2$LO interactions are much softer than AV6' interaction. Usually a soft potential is computationally more easy to simulate than hard ones. Because for soft potentials the chance that we meet with very big or very small values of potentials are much lower than hard ones, and this may lead to less variance (smaller error bar) in the results.
