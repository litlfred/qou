---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-007-quantum-coherence-limit
section_title: "Quantum coherence limit"
section_number: null
pages: 5-5
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
\label{subsec:quantum-coherence-limit}
Extreme plasmons \cite{plasmonics-ieee-2021,plasmonics-ieee-2022} for the first time access the coherence limit of  oscillations of the quantum electron gas that is inherent in conductive media. 

The conduction electrons that are excited to energy states, $\mathcal{E}\gg\mathcal{E}_F$, attain large $\vec{k_\ell}$. Collectively, electrons with various large $\vec{k_\ell}$ superpose to excite a large $\vec{k}$ plasmon, apparent from its field and density profile. 

For states with $\mathcal{E}\gg\mathcal{E}_F$, oscillations have large trajectories due to being strongly displaced from equilibrium. This increase in displacement requires a corresponding increase in restoring force exerted by the lattice to uphold the plasmon frequency, ${\rm \omega}_Q$,
\begin{align}\label{eq:plasmon-freq}
\begin{split}
	{\rm \omega}_{Q} & = \mathscr{F}_Q(\vec{k},\vec{p}) ~ \omega_{p} \\
							& \simeq \mathscr{F}_Q~ 56.4\sqrt{ n_0[10^{24}{\rm cm^{-3}}] } ~ {\times\rm 10^{15} rad/s} \\
	
\end{split}
\end{align}
While the quantum factor, $\mathscr{F}_Q$ depends on inherent characteristics of the material and properties of excitation, it primarily arises from the change in properties of a correlated many-body system relative to an ensemble of independent single electron states. It may be interpreted as the ability of quantum entities to be compressed to a density, $n_0=\mathscr{F}_Q^2n_e$ higher than uncorrelated ones. It is well known that a quantum ensemble becomes more collisionless at higher densities.

The restoring field that is capable of maintaining ${\rm \omega}_{Q}$ in Eq.\ref{eq:plasmon-freq} under coherence limited amplitude of oscillations of ultradense electron gas is,
\begin{align}\label{eq:plasmonic-field}
\begin{split}
	{\rm E}_Q & = \mathscr{F}_Q(\vec{k},\vec{p})\left(\frac{m_ec^2}{e}\right) \frac{2\pi}{\lambda_Q} \\
	 				& \simeq 0.1\mathscr{F}_Q\sqrt{ n_0[10^{24}{\rm cm^{-3}}] } ~ {\rm PVm^{-1}}.
\end{split}
\end{align}

The displaced Fermi electron gas that sustains the extreme plasmon, undergoes highly localized accumulation or compression which is ultimately limited by breaking of mutual coherence of plasmon under extreme amplitude, $\delta\simeq\lambda_Q$. This limit is a consequence of onset of trajectory overlap or collisions.

The density displaced $\delta n_e$ ($=n_e-n_0$) significantly exceeds equilibrium density, $\frac{\delta n_e}{n_0}\gtrsim 1$ owing to near complete displacement and compression as seen in Fig.\ref{fig:cross-section-3D-crunchin-plasmon}. Consequently, the ionic lattice gets locally bared by evacuation of the enveloping Fermi electron gas. The electric field in Eq.\ref{eq:plasmonic-field} is thus also the instantaneous Coulomb field of the unneutralized ionic lattice or the Fermi gas that get spatially segregated over plasmon timescales.

Eq.\ref{eq:plasmonic-field}, first introduced by our extreme plasmon model \cite{plasmonics-ieee-2021,plasmonics-ieee-2022, jinst-2023} is the electric field at the coherence limit of one-dimensional electron oscillations of a nonclassical gas. Although given the lack of appropriate experiments, Eq.\ref{eq:plasmonic-field} does not yet represent experimentally verified coherence limit of quantum electron oscillations. Specifically, a quantum gas where individual electrons are distinguishable with a well-defined quantum state. 

For a classical electron gas (Maxwell-Boltzmann statistics) commonly obtained by ionizing an atomic or molecular gas to plasma state, experiments have confirmed scaling of peak ${\rm E}_p$ \cite{wavebreaking-limit} with square root of ionized electron density, $\sqrt{n_e}$. Note that it is important to distinguish classical, ionized electron density, $n_e$ against quantum, Fermi electron density, $n_0$. Importantly, classical gasses can hardly be compressed to $n_e > 10^{19}{\rm cm^{-3}}$. 

In contrast, the quantum electron gas that is inherent in conductive materials is naturally ultradense ($n_0$) even at equilibrium. This is because the periodic ionic potential of the background lattice quantizes the electron energy levels in cognizance with the presence of lattice \cite{Bloch-1933}. The resulting electronic states are naturally independent of collisions with the lattice (without impurities, inconsistencies or thermal vibrations). 

Similarly, electron-electron collision cross-sections are suppressed due to a finite separation in electron energies especially owing to spin states, per the exclusion principle \cite{Pauli-spin-statistics}. Furthermore, correlation energy of electrons effectively allows higher spatial compression.

It is these implicit quantum effects that make possible existence of plasmons.
