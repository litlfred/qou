---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-004-wigner-quantum-phase-space
section_title: "Wigner quantum phase-space"
section_number: null
pages: 2-3
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 1.0
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
The dynamics of any many-body quantum system with N quantum entities such as the quantum electron gas in this work, is fully describable by suitably transforming (Wigner-Weyl) the quantum variables representing the ensemble over the real-space $\mathbb{R}^{3N}$. Instead of exact determination of many-body wavefunction, the density matrix, $\rho(\vec{r},\vec{r'},t)$ which allows determination of the statistical distribution of states, is used to obtain the {\em Wigner function}, $f_W$ (in Complex space, $\mathbb{C}$):
\begin{align}\label{eq:Wigner-Weyl-transform}
\begin{split} 
& f_W(\vec{r},\vec{p},t) = \int_{\mathbb{R}^{3N}\rightarrow\mathbb{C}} d^3s~~e^{-is\frac{\vec{p}}{\hbar}}~ \rho\left(\vec{r}+\frac{s}{2}, \vec{r}-\frac{s}{2}, t\right). \\
& \rho = \int_{\mathbb{C}\rightarrow\mathbb{R}^{3N}}\int_{a,b} \frac{f_W(\vec{r},\vec{p})}{(2\pi\hbar)^{3N}} \left(e^{i[a(Q-\vec{r})+b(P-\vec{p})]}\right) \text{d}x\, \text{d}p\, \text{d}a\, \text{d}b.
\end{split}
\end{align}
This representation overcomes the limitations imposed by Heisenberg's uncertainty principle. It allows treatment of quantum mechanics in phase-space by simultaneous representation of the distribution of non-commuting variables, here instantaneous position ($\hat{Q}$) and momentum ($\hat{P}$). Although, $f_W$ is a quasi probability distribution function, it allows modeling the evolution of a quantum system using phase-space formalism. Density, $n(\vec{r},t)$ and momentum, $n(\vec{p},t)$ distributions are obtained from the Wigner function, as follows:
 \begin{align}\label{eq:density-momentum-distribution}
\begin{split} 
\int d^3p ~ f_W(\vec{r}, \vec{p}, t) = n(\vec{r}, t).\\
\int d^3r ~ f_W(\vec{r}, \vec{p}, t) = n(\vec{p}, t).
\end{split}
\end{align}

The evolution of Wigner distribution function is described by the {\em Wigner equation} \cite{Wigner}. 
\begin{align}\label{eq:wigner-eq}
\begin{split} 
\frac{\partial f_W}{\partial t} + \frac{\hbar\vec{k_\ell}}{2m^*}\frac{\partial f_W}{\partial \vec{r}} = \int d\vec{k_\ell'} ~ \phi_W(\vec{r},\vec{k_\ell'}-\vec{k_\ell},t)f_W(\vec{r},\vec{k_\ell'},t)
\end{split}
\end{align}
The Wigner transport equation, Eq.\ref{eq:wigner-eq} describes ballistic carrier transport. Further correction terms are needed to account for collisional dynamics. Here, $\vec{k_\ell}$ ($\hat{p}=-i\hbar\vec{\nabla}$) is the wavevector which determines the lattice or crystal momentum of individual electrons with effective mass, $m_e^*$. Naturally, when conduction electrons that sustain the extreme plasmon individually attain large $\vec{k_\ell}$ the collective wavevector, $\vec{k}$ also becomes large.

The electromagnetic force due to long-range Coulomb interaction (due to non-equilibrium distribution in space) in the Wigner equation is accounted for by an electrostatic potential, $\phi_W$ (using mean-field approximation) which is determined by Poisson equation:
\begin{align}\label{eq:Poisson-eq}
\begin{split} 
\nabla^2\phi_W(\vec{r}, t) = 4\pi e (n(\vec{r}, t) - n_0).
\end{split}
\end{align}

For the quantum electron gas, the Wigner-Poisson system provides a framework similar to the Vlasov-Poisson system for classical gasses.

In our work, the quantum electron gas on a surface is strongly excited such that the displacement amplitude of  constituent conduction electrons approaches the wavelength, in Eq.\ref{eq:plasmonic-wavelength}. The resulting large-amplitude trajectories cannot be perturbatively treated and linearized. Such trajectories underlying extreme plasmons are discernible from Fig.\ref{fig:cross-section-3D-crunchin-plasmon} which shows the planar cross-section of electron density (of the 3D simulation in Fig.\ref{fig:3D-crunch-in-plasmon}). 




\begin{figure}[!htb]
\centering
   \includegraphics[width=0.9\columnwidth]{crunchin_mode_cross_section_yellow.jpg}
   \caption{Cross-section of the surface crunch-in plasmon in a conductive tube from 3D particle-tracking simulation same as in Fig.\ref{fig:3D-crunch-in-plasmon} using \cite{epoch-pic,xsede-rmacc-citation}.}
\label{fig:cross-section-3D-crunchin-plasmon}
\end{figure}

Consequently, large-amplitude quantum gas oscillations cannot be modeled using fluid theory (tracking macroscopic quantities such as moments of phase-space) which uses macroscopic material properties and classical hydrodynamic model \cite{Kronig-Korringa-1943}. Similarly, small-amplitude quantum mechanical framework \cite{Pines-Bohm-PhysRev-1952} based upon perturbative expansion around smallness of $\alpha$ (see sec.\ref{subsec:quantum-small-plasmons}), is not applicable to extreme plasmons.

Our analytical model below, therefore, uses quantum kinetic theory to model large-amplitude plasmons. Particularly, we build upon the small-amplitude plasmon model \cite{Pines-Bohm-PhysRev-1952} that matches experimental observations.
