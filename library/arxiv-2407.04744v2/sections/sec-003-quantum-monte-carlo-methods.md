---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods"
section_id: sec-003-quantum-monte-carlo-methods
section_title: "Quantum Monte Carlo methods"
section_number: null
pages: 2-3
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.989
doc_brief: "Magnetic structure of A ≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods — 26 sections: Magnetic structure of A 10 nuclei ; Introduction; Theory"
---
[]{#sec:qmc label="sec:qmc"}

Quantum Monte Carlo (QMC) approaches [@Carlson:2014vla] are a suite of computational methods used to stochastically solve the Schrödinger equation $$H \Psi(J^\pi;T,T_z)= E \Psi(J^\pi;T,T_z) \ ,$$ where $\Psi(J^\pi;T,T_z)$ is a nuclear wave function with specific spin-parity $J^\pi$, isospin $T$, and charge state $T_z$. The Hamiltonian has the form $$\begin{aligned}
\label{eq:hamiltonian} H = \sum_{i} K_i + {\sum_{i<j}} v_{ij} + \sum_{i<j<k}
V_{ijk} \ ,
\end{aligned}$$ where $K_i$ is the non-relativistic kinetic energy and $v_{ij}$ and $V_{ijk}$ are respectively two- and three-nucleon potentials.

The QMC approach of this work is a two-step process that begins with the variational Monte Carlo (VMC) method. In nuclear VMC calculations, the variational ansatz taken for the many-body wave function is [@Pudliner:1997ck] $$\ket{\Psi_T} = \mathcal{S}\prod_{i<j}\left[ 1 + U_{ij} + \sum_{i<j\neq k} \widetilde{U}^{\rm TNI}_{ijk} \right] \ket{\Psi_J}\, \label{eq:psi.t}$$ where $\mathcal{S}$ is the symmetrization operator, $U_{ij}$ is a two-body correlation operator, $\widetilde{U}^{\rm TNI}_{ijk}$ is a three-body correlation operator, and $\Psi_J$ is a Jastrow-like wave function. The antisymmetric state $\Psi_J$ encodes the long-range structure of the system and is constructed by acting on a Slater determinant that places nucleons in $s$- and $p$-shell orbitals with correlation functions that encode the appropriate cluster structure (*e.g.*, $^6$Li $\sim \alpha$ + $d$) of the system. The design of the two- and three-body correlation functions in Eq. [\[eq:psi.t\]](#eq:psi.t){reference-type="ref" reference="eq:psi.t"} reflects the influence of the short-distance nuclear interaction in the medium. The correlation operators contain embedded variational parameters that one then optimizes to find a best variational state, $\Psi_V$, by minimizing the expectation value $$E_V = \frac{\mel{\Psi_V}{H}{\Psi_V}}{\langle \Psi_V | \Psi_V \rangle} \geq E_0$$ where $E_0$ is the true ground state energy of the system.

The VMC result is then further improved upon by using the Green's function Monte Carlo (GFMC) method. The method leverages the fact that the real time ($t$) Schrödinger Equation $$i\frac{\partial}{\partial t}\ket{\Psi(t)} = (H-E_T)\ket{\Psi(t)}\, ,$$ may be recast as a diffusion equation in imaginary time $\tau=it$ $$-\frac{\partial}{\partial \tau}\ket{\Psi(\tau)} = (H-E_T)\ket{\Psi(\tau)}\, ,
\label{eq:diffusion}$$ where $E_T$ is an energy offset that controls the normalization of the wave function. Noting that one may expand any state in a complete orthonormal basis, we can write $\Psi_V$ as a sum of the true eigenstates $\psi_i$ of the Hamiltonian $$\ket{\Psi_V} = \sum_{i=1}^{\infty} c_i\ket{\psi_i}\, .$$ From Eq. ([\[eq:diffusion\]](#eq:diffusion){reference-type="ref" reference="eq:diffusion"}), if the energy offset $E_T$ is taken to be the exact energy of the ground state $E_0$, it is clear that in the limit $\tau \to \infty$ $$\lim_{\tau\to\infty} e^{-(H-E_0)\tau}\ket{\Psi_V} \propto c_0\psi_0\, ,$$ making it possible to project the true ground state out of $\Psi_V$. In practice, the propagation is performed in $n$ small steps in imaginary time $\Delta\tau$, $$\ket{\Psi(\tau)} = \left[ e^{-(H-E_0)\Delta\tau}\right]^n\ket{\Psi_V}\, ,$$ until spurious contamination is removed from the wave function and convergence is reached.

In this work, we will study matrix elements of operators $\mathcal{O}$ acting on the VMC wave function. To obtain expectation values in GFMC, we compute the so-called "mixed-estimate,\" $$\langle \mathcal{O}(\tau) \rangle \approx 2\frac{\mel{\Psi_V}{\mathcal{O}}{\Psi(\tau)}}{\langle \Psi_V | \Psi(\tau) \rangle}
- \frac{\mel{\Psi_V}{\mathcal{O}}{\Psi_V}}{\langle \Psi_V | \Psi_V \rangle}\, ,$$ derived assuming the GFMC wave function at $\tau$ is a small improvement over the VMC state; *i.e.*, $\Psi(\tau)=\Psi_V+\delta\Psi$. Since the variational wave functions are typically good descriptions of light nuclei, this a valid approximation. In principle, it is possible to calculate a matrix element between two propagated states in GFMC; however, this requires performing separate imaginary time propagations for each matrix element that one would like to compute [@Pervin:2007sc], which makes an order-by-order analysis of the magnetic moments and form factors quite costly. Thus, the mixed estimate is a necessary approximation to systematically analyze the convergence of $\chi$EFT predictions for the magnetic structure of nuclei over a range of momenta.
