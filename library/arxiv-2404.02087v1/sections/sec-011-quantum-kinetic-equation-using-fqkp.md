---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-011-quantum-kinetic-equation-using-fqkp
section_title: "Quantum kinetic equation using FQ(k,p)"
section_number: null
pages: 7-8
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.904
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
A kinetic equation is developed here within the quantum kinetic framework using modified single-particle approach (sec.\ref{quantum-kinetic-approx}). Specifically, an equation of motion of individual conduction electrons oscillating at average frequency, $\omega_Q$ is obtained. 

Assuming azimuthal symmetry, radial motion over an infinitesimally thin disk of thickness $dz$ is considered. The key parameters of the kinetic model are:
\begin{description}[itemsep=0pt, topsep=0pt, parsep=0pt]
\item[$r_0$] is the equilibrium position of a tube electron which always satisfies the condition, $r_t < r_0 < r_t+\Delta w$
\item[$r(t)$] is the instantaneous radial position of an oscillating tube electron ($r = r_0 + \Delta r$ where, $\Delta r$ is the radial displacement of the electron which can be positive or negative)
\item[$r_m$] is the maximum radius to which the strongly driven tube electrons reach and bunch up to form an electron sheath 
\item[$\mathcal{H}(r)$] is the step function which is defined as $\mathcal H(0^+) = 1$ and $\mathcal H(0^-) = 0$. This function models the step-like change in the density across the surface.
\end{description}

{\bf Coherent oscillations:}  Radially oscillating conduction electrons retain mutual coherence until they maintain the same ordering in the radial direction, as that at equilibrium. Ordering precludes crossing of trajectories and disallows electron-electron collisions, a key requirement for ballistic oscillations.

This condition requires that a conduction electron located at an equilibrium radial position, $r_0$ which is initially less than that of a neighboring electron, always remains at a lesser instantaneous radii, $r(t)$ throughout its trajectory underlying the plasmon. 

It requires that when other conduction electrons which are located at an equilibrium radial position less than the electron under consideration (between $r_0$ and $r_t$) move with it, they remain ordered and just behind $r(t)$. This adherence to equilibrium ordering during oscillation ensures coherent and collisionless oscillations.

Mutual coherence along with collisionless characteristics ensure that the plasmon does not collisionally dissipate energy coupled to it.

{\bf Ionic lattice phase:} When a conduction electron under consideration is radially displaced from $r_0$ (by the force of beam fields), it uncovers the ionic lattice in the tube wall. Upon radial displacement of this electron, all the electrons located at equilibrium radii between $r_t$ and $r_0$ move together and are displaced to a new radial location $r(t)$. These electrons bunch together into a sheath layer at the trajectory maxima due to inward force of the uncovered ionic lattice. The inward force exerted due to uncovering of the ionic lattice (using Gauss's law) is:
\begin{align}\label{eq:ionic-force-r}
\begin{split}
-e ~ E_{\rm lattice}(r > r_t) = - m_e \omega_{p}^2(n_0) ~ \frac{(r^2 - r_t^2)}{2r}
\end{split}
\end{align}

However, in addition to the ionic force on the electron under consideration (originally located at $r_0$), the electrons with an equilibrium radii smaller than $r_0$ (located between $r_0$ and $r_t$) collectively move with the electron under consideration and compress together to produce a collective field opposite to that of the lattice. The compressed density is higher in the quantum regime by $\mathscr{F}_Q^2$. The force of electrons collectively compressed together, balances the force exerted by the lattice to form dynamic equilibria (zero velocity) at the trajectory maxima, $r_m$. 

The field due to accumulation of conduction electrons located between $r_0$ and $r_t$ and collectively moving outwards along with the electron at $r_0$ while maintaining the equilibrium radial ordering is,
\begin{align}\label{eq:electronic-force-r}
\begin{split}
-e ~ E_{\rm e}(r) = m_e\omega_{Q}^2(n_0) ~ \frac{(r_0^2 - r_t^2)}{2r}
\end{split}
\end{align}
As conduction electrons undergo a compression greater by $\mathscr{F}_Q^2n_0$, the field is correspondingly higher.

{\bf Crunch-in phase:} After the equilibrium at the outward radial maxima, $r_m$ electron momentum becomes radially negative. Being part of large-amplitude oscillations, the electron under consideration gains large enough velocity to tunnel across the surface and move into the hollow region of the tube. As there is no lattice in the core region of the tube, the collectively moving electrons do not experience any ionic force.

However, since the electrons collectively oscillate, the tube electrons located between $r_0$ and $r_t$ collectively crunch-in into the hollow region. The stronger the force of the beam, the deeper is the radial excursion into the core region of the tube. Under this condition, inside the tube core region the only force acting to restore the electrons back to equilibrium is due to electron accumulation. This is equivalent to the force in Eq.\ref{eq:electronic-force-r}.

Therefore, the net collective force acting on the electrons can be written using the Heaviside step function, $\mathcal{H}(r)$ to segregate the forces controlling the dynamics in the wall in contrast with that inside the tube:
\begin{align}\label{eq:net-force-r}
\begin{split}
F_{\rm coll} &(r>r_t) = -e ~ E_{\rm lattice}(r > r_t) -e ~ E_{\rm e}(r > r_t) \\


								& = - m_e \omega_{Q}^2(n_0) \frac{ (r^2 - r_t^2) \mathcal{H}(r-r_t) - (r_0^2 - r_t^2)  }{2r}
\end{split}
\end{align}
$\mathcal{H}(r-r_t)$ in Eq.\ref{eq:net-force-r} indicates that the first term which is due to the lattice along with the second term together act on the electrons while their instantaneous radial position is in the wall. However, the second term only applies to electrons with instantaneous position in the evacuated region, $r < r_t$, as the effect of lattice ceases at $r_t$.

It is important to note that due to the termination of the lattice at $r=r_t$, the kinetic equation does not account for quantum effects inside the tube core. But, continuity of momentum across the boundary needs to be taken into account. An additional term, $\frac{\partial}{\partial t}\left(\frac{\partial r}{\partial t}\right) |_{r=r_t}$ is used to take this continuity in momentum.

{\bf Beam force:} When negatively charged, ${\rm sgn}[Q_b] = -1$ beam, such as an {\it electron beam}, excites the conduction electrons, they initially propagate outwards and compress together at $r_m$. On the other hand, when excited by a positively charged beam, conduction electrons initially accelerate inwards towards the core region. The bunch length is taken to be smaller than, $\lambda_Q$ such that the beam fields terminate in the crunch-in phase. 
 
{\bf Kinetic equation:} For a conduction electron located at $r(z,t)$, the equation of motion of collective surface oscillation excited by the beam field is $\gamma_e m_e \frac{\partial^2 r(z,t)}{\partial t^2} = F_{\rm coll} + eE_b$. Here, $\gamma_e = \left( 1 + \frac{\vec{p}}{m_ec}\cdot\frac{\vec{p}}{m_ec}\right)^{1/2}$ is the relativistic factor of the conduction electrons and beam field is simplified under the condition, $\sigma_r\lesssim r_t$. 

The kinetic equation of the nonlinear surface wave sustained by localized crunch-in plasmons is obtained by transforming to a coordinate co-moving with the beam, $\xi = c\beta_b t - z$ such that $\frac{\partial \xi}{c\beta_b} =  \partial t$ and using Eq.\ref{eq:fields-Gaussian-bunch},
\begin{align}\label{eq:crunch-in-plasmon-kinetic}
\begin{split}
\frac{\partial^2 r(z,t)}{\partial \xi^2} & +  \frac{\omega_{p}^2(n_t)}{\gamma_e c^2\beta_b^2} \frac{1}{2r} \left[ (r^2 - r_t^2)\mathcal{H}(r-r_t) - \mathscr{F}_Q^2(r_0^2 - r_t^2)  \right] \\
& + {\rm sgn} \left[\frac{\partial r}{\partial \xi}\right] ~ \frac{\partial^2 r}{\partial \xi^2} \biggm\lvert_{r=r_t}  \\
& = - {\rm sgn}[Q_b] \frac{\omega_{p}^2(n_0)}{\gamma_ec^2\beta_b^2} ~ \frac{n_{b0}}{n_0} \frac{\sigma_r^2}{2\pi} ~ \frac{1}{r} ~ e^{{-(z-z_{\rm m})^2/(2\sigma_z^2)}} 
\end{split}
\end{align}

The kinetic equation, Eq.\ref{eq:crunch-in-plasmon-kinetic} is used obtain the radial maxima of electron trajectory, $r = r_m$ where $\frac{\partial^2 r}{\partial t^2} = 0$,
\begin{align}\label{eq:r-max-nano-Gaussian}
\begin{split} 
r_m ~ = ~\left[ r_t^2 ~ + 2 ~ \frac{n_{b0}}{n_0} ~ \frac{\sigma_r^2}{2\pi} \right]^{1/2} 
\end{split}
\end{align}

Existence condition of crunch-in plasmon,  $(r_t+\Delta w)>r_m$ is also obtained as,
\begin{align}\label{eq:existence-condition}
\begin{split} 
\Delta w \left(1+\frac{\Delta w}{2r_t}\right) > \frac{n_0}{n_{b0}} ~ \frac{\sigma_r^2}{2\pi r_t}
\end{split}
\end{align}

Extreme plasmon is excited only when $(r_m - r_t)\lambda_Q^{-1}\gg 0$, which is simplified as,
\begin{align}\label{eq:excitation-condition}
\begin{split}
0\ll\left( \frac{n_{b0}}{n_0} ~ \frac{\sigma_r^2}{2\pi r_t} \right) \lambda_Q^{-1} \simeq 1
 \end{split}
\end{align}
