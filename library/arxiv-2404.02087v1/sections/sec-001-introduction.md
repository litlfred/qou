---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-001-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.977
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
Plasmons \cite{Pines-PhysRev-1953, Pines-Bohm-PhysRev-1952, Ritchie-surface-plasmon} underpin nanosciences \cite{plasmonics-1} by making possible nanometric energy confinement. Nanometric size of these quasiparticles constituted by collective oscillations of delocalized, conduction band electron gas is realizable only due to the innately quantum nature of the gas which allows ultra-high densities, $n_0\simeq10^{24}\mathrm{cm^{-3}}$ that enforce a characteristic wavelength:
\begin{align}\label{eq:plasmonic-wavelength}
\begin{split} 
\lambda_{Q}\lesssim\frac{30}{\sqrt{n_0\mathrm{(10^{24}cm^{-3}})}} ~ \mathrm{nm}.
\end{split}
\end{align}
The very existence of the quantum electron gas (densities unattainable for a classical gas) and thereby nanoscale plasmons is dependent on quantum effects. These nonclassical properties are essential for collisionless dynamics of conduction electrons, as determined by Bloch's theorem \cite{Bloch-1933} (electron-lattice interactions) and Pauli's exclusion principle \cite{Pauli-spin-statistics} (electron-electron). 

The conduction electron gas maintains its quantum character with electron states valid only at discrete energies, $\mathcal{E}_\vec{k}$ and wavevectors, $\vec{k_{\ell}}$ (unlike a classical gas) as long as the ionic lattice exists. These discrete states are occupied in accordance with Fermi-Dirac statistics which makes the quantum electron gas free of collisions with an ideal, stationary lattice. The nonclassical distribution along with nearly non-interacting fermions gives rise to a Fermi electron gas, a quantum entity which is a prerequisite for plasmons.





\begin{figure}[!htb]
\centering
   \includegraphics[width=\columnwidth]{analytical-paper-3D-crunch-in-mode-profile.jpg}
   \caption{Extreme plasmon excited in a conductive tube by an electron bunch (green envelope) launched inside it,  illustrated in 3D using particle-tracking simulation. The conduction electrons in a tube with core radius: $r_t\rm=100nm$, wall thickness: $\Delta w\rm=250nm$ and electron density: $n_0=\rm 2\times10^{22}cm^{-3}$ are relativistically excited. The red (denser) and gray surfaces show electron density variations. Electron trajectories approach $\lambda_{Q}\simeq 200{\rm nm}$ and tunnel across the tube surface to ``crunch-in''. The bunch that has here propagated about $\rm20\mu m$ inside the tube is initially Gaussian with: $\sigma_z\rm=400nm$, $\sigma_r\rm=250nm$ and density, $n_{b0}=\rm 5\times10^{21}cm^{-3}$.}
\label{fig:3D-crunch-in-plasmon}
\end{figure}

Our work has uncovered a new class of plasmons in the large-amplitude limit \cite{plasmonics-ieee-2021,spie-2021,pct-2021,plasmonics-ieee-2022,nanofocusing-2022, ion-wake, crunch-in-regime, jinst-2023}. Large-amplitude, non-perturbative plasmons have a trajectory amplitude ($\delta$) of collective oscillations that approaches the wavelength, $\delta\simeq\lambda_{Q}$. The extreme limit of oscillation amplitude is set by breakdown in mutual phase coherence (onset of collisions) which is critical for the quintessential ``collective'' nature of plasmons. In contrast, conventional plasmons are sustained by oscillations of small amplitude, $\delta\ll\lambda_{Q}$. Furthermore, while  conventional plasmons are made up of excited states with electron velocities relatively close to the Fermi velocity, $v_F$; excited quantum states underlying large-amplitude plasmons correspond with relativistic electron momenta, ${\bf p}\simeq m_ec\gg p_F$. 

Extreme plasmons introduced by our work gain prominence as they open unprecedented PetaVolts per meter (PV/m) electromagnetic fields \cite{plasmonics-ieee-2021, spie-2021, nanofocusing-2022} (sec. \ref{subsec:quantum-coherence-limit}). As this unique quantum technology brings about a PV/m {\it extreme field frontier}, it promises unparalleled possibilities. A few of which include nano-wiggler based gamma-ray lasers \cite{plasmonics-ieee-2021, ginzburg-2003, pct-2021} and opening the vacuum (field-driven vacuum polarization) \cite{jinst-2023, schwinger-limit}.

Our efforts \cite{slac-2023,slac-2022, slac-2020} are aimed at controlled excitation of extreme plasmons. Controlled nanometric confinement of electromagnetic energy is only possible by preserving the ingrained quantum nature critical to sustain collisionless oscillations. This quantum nature vital for plasmons is maintained by the ionic lattice which is preserved in our model by exciting plasmons using high-density charged particle beams \cite{plasmonics-ieee-2021, pct-2021}. Due to bunching characteristics, particle accelerators intrinsically rid the beams of any significant pre-pulses capable of disrupting the lattice (contrary to high-intensity lasers).

Further control over the interaction is enabled by a specific type of extreme plasmon, which based upon the key requirements described in sec.\ref{sec:controlled-excitation} has been identified and introduced in our work as the surface crunch-in plasmon. However, unlike perturbative surface plasmons \cite{Ritchie-surface-plasmon}, plasmons in the large-amplitude limit have highly localized, small spatial scale collective electron accumulation (large collective wavevector, $\vec{k}\simeq 2\pi\lambda_Q^{-1}$) excited by relativistic  momenta ($\bf p$). These characteristics invalidate customary fluid model based on initialized constitutive parameters and necessitate kinetic modeling supported by particle-tracking simulations (in Fig.\ref{fig:3D-crunch-in-plasmon}). In Fig.\ref{fig:3D-crunch-in-plasmon}, where $\lambda_Q$ is around 200 nm; conduction electrons are collectively displaced by $\delta \simeq 100 {\rm nm}$ and accumulate over a few tens of nm, at the maxima of their trajectories. 

In this work, extreme plasmons are analytically modeled from the first principles. These principles and the framework they shape are laid out in sec.\ref{sec:framework}. In particular, our quantum kinetic model is based on the {\it Wigner quantum phase-space} formalism. Using this formalism under a modified {\it independent electron approximation} which accounts for the quantum oscillation frequency, $\omega_Q$ (see sec.\ref{subsec:quantum-small-plasmons}), we model a surface ``crunch-in'' plasmon collisionlessly excited on the inner surface of conductive tubes, as depicted in Fig.\ref{fig:3D-crunch-in-plasmon}. The kinetic model developed in sec.\ref{sec:kinetic-model} is used to estimate the fields in sec.\ref{sec:field-estimation}.

The extreme plasmon model, particularly the surface crunch-in plasmon forms the basis of our ongoing experimental effort \cite{slac-2023,slac-2022, slac-2020} (initially using tunable, semiconductor plasmons \cite{plasmonics-ieee-2022}).
