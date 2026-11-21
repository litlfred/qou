---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-006-small-amplitude-plasmons-quantum-model
section_title: "Small-amplitude plasmons: Quantum model"
section_number: null
pages: 3-5
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.993
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
\label{subsec:quantum-small-plasmons}
Quantum mechanical framework of small-amplitude plasmons was developed by Pines et. al. \cite{Pines-Bohm-PhysRev-1952, Pines-PhysRev-1953} to explain experimental observations. As the electronic states whether in the ground (equilibrium) or the excited (plasmon) state of conduction electrons, are valid only at discrete wavevectors, such a framework is indispensable. 

The dynamics of quantum electrons, particularly their organized behavior which gives rise to collective electron oscillations, is fundamentally a many-body quantum phenomena. Analysis of this many-body quantum state is simplified in \cite{Pines-PhysRev-1953} by using a canonical transform to the basis of collective wavevector, $\vec{k}$.

This transformation allows separating the Hamiltonian into three major, nearly independent terms:
\begin{align}\label{eq:Hamiltonian-quantum}
\begin{split} 
\mathcal{H} = \mathcal{H}_{\rm part}+\mathcal{H}_{\rm coll}+\mathcal{H}_{s. r.} 
\end{split}
\end{align}
Eq.\ref{eq:Hamiltonian-quantum} explicitly recognizes the existence of plasmons using the term $\mathcal{H}_{\rm coll}$. The discrete wavevector basis is suitable for separation of terms contributing to $\mathcal{H}$, because plasmons are only sustained below a {\em critical wavenumber}, $k<k_c$. This critical wavenumber, $k_c$ is close to the {\em Thomas-Fermi screening wavenumber}:
\begin{align}\label{eq:plasmon-critical-wavenumber}
\begin{split} 
k_c^2 \simeq k_{\rm TF}^2 = k_F^2 \left( \frac{16}{3\pi^2}\right)^{2/3} \frac{r_s}{a_0}
\end{split}
\end{align}
This critical wavenumber motivates the canonical transformation as it allows separation of terms in the small-amplitude limit. Using this transformation, analysis of plasmons becomes independent of individual electron dynamics that primarily occurs over $k>k_c$, represented by $\mathcal{H}_{\rm part}$ (individual particle states) and $\mathcal{H}_{s. r.}$ (short range). Here, the Fermi wavevector, $k_F=(3\pi^2 n_0)^{1/3}$ represents electron momentum at the Fermi energy, $E_F=\hbar^2k_F^2(2m_e)^{-1}$, $r_s$ is radius of the Wigner-Seitz sphere and $a_0$ the Bohr radius.

The energy of plasmons ($\mathcal{H}_{\rm coll}$) is required to be higher than the ground-state energy (itself greater than the Fermi energy) of the electron assembly to eliminate their spontaneous excitation. So, when the quantum electron gas is externally excited to sustain plasmons, the term $\mathcal{H}_{\rm coll}$ in Eq.\ref{eq:Hamiltonian-quantum} becomes dominant. 

Experimentally verifiable quantities such as the frequency of plasmon, $\omega_{Q}$ using the quantum model in \cite{Pines-Bohm-PhysRev-1952} were obtained in the small-amplitude limit by perturbatively expanding about a small parameter, $\alpha$:
\begin{align}\label{eq:alpha-QM}
\begin{split} 
\alpha = \left\langle \left(\frac{\vec{k} \cdot \vec{p}}{m\omega}\right)^2 \right\rangle
\end{split}
\end{align}
where, the parameter $\alpha$ is averaged over the particle momenta, $\vec{p}$ and wavevectors of the collective field (or collective density profile), $\vec{k}$ with $\omega$ being the frequency of the collective oscillations. The frequency of  conduction electrons, $\omega$ was defined using quantum dispersion relation obtained based upon small $\alpha$. 
The average plasmon frequency, $\left\langle\omega_{Q}\right\rangle$ from the perturbative expansion about small $\alpha$ is:
\begin{align}\label{eq:plasmon-frequency-small-amplitude}
\begin{split} 
\left\langle\omega_{Q}\right\rangle \simeq \left( 1 + 3\alpha\left[1+ \frac{3}{10}\beta^2\right] \right) \omega_{p} \equiv  \mathscr{F}_Q(\vec{k},\vec{p}) ~ \omega_{p}
\end{split}
\end{align}
where, $\omega_{p}=\sqrt{\frac{n_0 e^2}{\epsilon_0 m_e}}$ is the classical electron (plasma) oscillation frequency, $\beta = \frac{k_c}{k_F}$, and $\alpha \simeq \frac{1}{2} ~ \beta^2 ~ \frac{a_0}{r_s}$. The plasmon frequency is, therefore, material and ($\vec{k}$,$\vec{p}$)-dependent as evident from the term $3\alpha$.

{\bf Quantum factor:} In this work, we introduce a quantum factor $\mathscr{F}_Q(\alpha,\beta,\vec{k},\vec{p})\equiv \mathscr{F}_Q(\vec{k},\vec{p})$. The characteristics of quantum electron oscillations ($\omega_{Q}$) are quite unlike the oscillations in a classical plasma ($\omega_{p}$) which has randomly distributed ions (no quantum effects) and Maxwell-Boltzmann distribution (energy continuum). 

In \cite{Pines-PhysRev-1953}, characteristics of plasmons measured in experiments were demonstrated to be in agreement with the quantum model (as opposed to a classical one).

{\bf Non-perturbative plasmons:} Extreme plasmons are not amenable to perturbative expansion because of their large oscillation amplitude. Such oscillations have large wavevectors, $\vec{k}$ as is evident from highly localized density accumulation. These large collective wavevectors are a result of relativistic momentum, $\vec{p}$.

Due to the lack of any experimental investigations of extreme plasmons, their underlying non-perturbative, quantum mechanical framework and their characteristic quantities such as oscillation frequency of extreme plasmons, $\omega_{Q}$, quantum properties are incorporated in our model using the quantum factor, $\mathscr{F}_Q({\vec{k},\vec{p}})$. $\mathscr{F}_Q$ ($>1$ even in the small-amplitude limit) is not merely a constant factor \cite{Pines-PhysRev-1953}, it depends upon material properties and scales with $\vec{k}$ and $\vec{p}$ of the excited states.

In the large-amplitude quantum limit, the plasmon frequency and coherence-limit of quantum electron oscillations are obtained by extending into the quantum domain using $\mathscr{F}_Q$. Our experiments \cite{plasmonics-ieee-2022, slac-2023, slac-2022, slac-2020} will comprehensively address these considerations.

{\bf Preceding models:} Quantum mechanical treatment of conduction electron oscillations in \cite{Pines-PhysRev-1953} was preceded by hydrodynamic theory of Kronig and Korringa \cite{Kronig-Korringa-1943} which treated the quantum electron gas as a classical fluid. This model accounted for collisions as viscous friction which led to the erroneous conclusion that collision rate increased with the velocity of oscillating electrons.

Subsequently, Kramers proposed an alternative model \cite{Kramers-1947} in line with an earlier classical kinetic treatment by Drude which was developed prior to the atomic model \cite{Drude-1900}. But, this kinetic model still treated individual electrons with classical properties. This model arrived at the important understanding that the effect of collisions was negligible. However, by not accounting for the quantum mechanical basis of the collisionless behavior, this model also erroneously predicted that the rate of collision increased with electron velocity.

Tomonaga \cite{Tomonaga-1950} first developed a quantum mechanical model of one-dimensional collective oscillations of Fermi electron gas. However, this model approximated the many-body wavefunction of the electron gas to be merely a collection of free electrons with a Fermi distribution at absolute zero, instead of electronic states with discrete wavevectors. In  \cite{Tomonaga-1950}, the degenerate electron gas is found to merely execute classical plasma oscillations in disagreement with experiments.

As is evident from models preceding Pines \cite{Pines-PhysRev-1953}, classical model contradict experiments while even simplified quantum models \cite{Pines-PhysRev-1953} are sufficient (including the effects of Bloch theorem, material dependence such as lattice structure etc.). The assumption that electrons in the presence of an ionic lattice merely form a classical fluid, entirely ignores the discrete electron states. 

Thus, classical approximations of a quantum system result in inaccurate predictions and are incapable of explaining experimental observations.
