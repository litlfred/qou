---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-013-12-motivation
section_title: "Motivation"
section_number: 1.2
pages: 20-23
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.977
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
All the current continuous space nuclear QMC calculations (such as GFMC and AFDMC) are performed within the framework of DMC. Due to the nature of DMC, when we perform ground state calculations, the operators will typically be sandwiched between the trial wave function $\Psi_T$ and the ground state wave function $\Phi_0$. Therefore, DMC based methods can accurately calculate the ground state expectation values of the operators which commute with the Hamiltonian, e.g., the ground state energy $E_0$ itself. However, if the operators do not commute with the Hamiltonian, the ground state expectation values cannot be obtained without tradeoff[^1]. In fact, there are a lot of operators which do not commute with the Hamiltonian, such as the root-mean-square (rms) radius, the particle number density, response functions, etc. Therefore, if we want to accurately calculate the ground state properties beyond the energy itself, we may want to use methods other than DMC.

Path integral Monte Carlo (PIMC) method ([@Ceperley95a]) can be a natural choice for such calculations. Unlike DMC methods, in PIMC, the operator can indeed be sandwiched easily between the ground states. So, whether the operator commutes with the Hamiltonian or not, we can always naturally calculate its ground state expectation value. This is the most attractive feature of PIMC.

There were important applications of PIMC in calculating the properties of condensed Helium atoms ([@Ceperley95a]) before. There are also PIMC calculations of nuclei on the lattice ([@LEE2009117; @Lee2012PRL]). However, there are no PIMC with the realistic NN potentials such as Argonne potential or ChEFT potentials to calculate the properties of any nuclei in continuous space time before this work.

<figure id="PIMCwalker">
<embed src="Figures/PIMCwalker.eps" />
<figcaption>Illustration of a GFMC walker and a PIMC walker.</figcaption>
</figure>

One of the main reasons is that continuous space PIMC calculations can be computationally expensive (even more expensive than GFMC). As illustrated in Fig. [1](#PIMCwalker){reference-type="ref" reference="PIMCwalker"}, for a PIMC walker, just like in the path integral, we need to separate the total imaginary time of the path into $N$ slices, insert a complete basis at each slice, and form a bead which contains the spatial configuration of the nucleus. Computing the beads one by one will be more and more time consuming as $N$ increases, especially considering that the realistic nuclear interactions contain spin and isospin structure. As a rough estimation, the amount of work a PIMC walker does is about $N$ times more than a GFMC walker does. However, due to the nature of DMC, a GFMC walker needs to evolve $N/2$ steps to reach $\tau_d$ which is half of the total imaginary time $\tau$ a PIMC walk does, in order to project out the ground state. Besides, for a given amount of computation time, the GFMC walkers can be more uncorrelated with each other than PIMC walkers. That is to say, PIMC actually needs more than twice the computation time to have equally uncorrelated walkers as GFMC walkers. So, overall the cost of a PIMC walker can be more than twice the cost of a GFMC walker. Therefore PIMC can be more expensive than GFMC. The storage space a PIMC walker requires is also $N$ times bigger than a GFMC walker, because the configurations of all the nucleons in the nucleus at each of $N$ beads need to be stored.

Nonetheless, ever since the early nuclear QMC simulation such as GFMC performed in 1987 ([@Carlson87a]), in the last more than three decades, human beings have witnessed an impressive increase in supercomputers' power. A typical CRAY system in the 1980s could do about $10^9$ floating point operations per second (FLOPS) ([@ChodoshEVO1946]), and today's most powerful supercomputer Fugaku[^2] can do more than $10^{17}$ FLOPS. With a magnitude of $10^8$ increase in computing power as well as the better understanding of NN interaction such as those from ChEFT, we have seen more and more ChEFT based GFMC and AFDMC calculations ([@Lynn14a; @Gerzerlis14a; @Lynn2017PRC; @Lonardoni2018PRL; @Lonardoni2018PRC]). Therefore, we will naturally ask, what can PIMC do in nuclear physics?

The motivation of this work is to show that (as a benchmark test to begin with), it is now possible to perform a reliable continuous space PIMC calculation of light nuclei, by using modern realistic NN interactions (particularly the chiral interaction).

[^1]: Diffusion based QMC methods typically use a technique called 'future walking' ([@HammondMCbook]) or 'forward walking' ([@Runge92PRB; @Casulleras1995PRB; @Samaras1999ForwardwalkingGF]) to deal with operators which do not commute with $H$. This technique is sensitive to the quality of the trial wave function $\Psi_T$.

[^2]: As of June 2020 ([@wiki:Fugaku2020]), the most powerful supercomputer in the world is Fugaku (peak performance is around 0.54 exaFLOPS) which is installed at RIKEN Center for Computational Science in Kobe, Japan. It is preceded by the Summit (peak performance is around 0.2 exaFLOPS) which is located at the Oak Ridge National Laboratory in Tennessee, USA.
