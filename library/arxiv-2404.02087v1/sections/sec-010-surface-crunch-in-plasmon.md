---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-010-surface-crunch-in-plasmon
section_title: "Surface crunch-in plasmon"
section_number: null
pages: 6-7
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.814
latex_coverage_ratio: 0.58
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
\label{sec:kinetic-model}
 
In the analysis below we present the kinetic model of surface crunch-in plasmon excited by a charged particle beam. Our model is applicable over collisionless and coherent timescales of extreme plasmon. In consideration of the symmetry of interaction, with quantum electron gas in a tube surrounding the beam, our model is formulated in cylindrical coordinates.

{\bf Radial oscillations:} The charged particle beam which propagates in the positive $z$-direction is taken to be sufficiently relativistic, $\gamma_b\gg1$ such that its electric field, $E_b$ is primarily radial. Therefore, conduction electrons interacting with the radial fields of the beam predominantly oscillate radially. These radial collective oscillations of the quantum electron gas across the surface are significantly different from conventional plasmons. The beam density, $n_b$ ($E_b\propto n_b$) is sufficiently high to strongly excite conduction electrons, ${\rm max}[r(t)]-r_0\simeq\lambda_Q$ (see below) in less than, $2\pi\omega_Q^{-1}$.

{\bf Discrete momentum states:} While conduction electrons are delocalized and free to occupy any arbitrary radial position, $r(t)$, the same is not true about their momentum, $\vec{p}$ which is quantum mechanically, $\hbar\vec{k_\ell}$. The classical continuum in electron momentum, $\frac{dr(t)}{dt}$ is not valid in a quantum system. Therefore, a specific electron lattice wavevector, $\vec{k}_\ell$ needs to exist to accommodate an excited electron. 

However, to simplify our analysis we make a reasonable assumption that electrons excited such that they occupy large quantum numbers in the extreme limit, have discrete quantum states that can be approximated using a continuum. Under this approximation, below momentum states are simplified to be represented as $\frac{dr(t)}{dt}$. 

Nevertheless, the effect of ionic lattice on constraining occupancy to specific lattice wavevectors, $\vec{k}_\ell$, the effect of momentum, $\vec{p}$ and the effect of collective wavevector, $\vec{k}$ on quantum electron gas oscillations, is accounted for using the quantum factor, $\mathscr{F}_Q(\vec{p},\vec{k})$.

{\bf Mixed states:} The simplification afforded by assuming a continuum in momentum also helps in handling the challenge posed by conduction electrons tunneling across the surface. This changes (oscillates) their quantum nature (discrete states) in the presence of the lattice to being free electrons (continuum) in vacuum.




\begin{figure}[!htb]
\centering
   \includegraphics[width=0.75\columnwidth]{Analytical_model_FIG_dimensions.jpg}
   \caption{Notations in our surface crunch-in plasmon kinetic model. Here, $r_t$ is the tube radius, $r_m$ is the maximum radial amplitude of plasmon and $\Delta w$ is the wall thickness of the tube.This is zoomed-in version of Fig.\ref{fig:cross-section-3D-crunchin-plasmon}.}
\label{fig:3D-crunchin-mode-dimensions}
\end{figure}
The parameters of the geometry of conduction electron gas are (depicted in Fig.\ref{fig:3D-crunchin-mode-dimensions}):
\begin{enumerate}[label=\roman*. ,topsep=0pt, itemsep=0ex,partopsep=0ex,parsep=0ex]
\item $n_0$ is the conduction electron density.
\item $r_t$ is the radius of the vacuum core of the tube defined by its inner wall.
\item $\Delta w$ is the wall thickness with the corresponding outer wall radius being $r_t+\Delta w$.
\end{enumerate}

The excitation beam is assumed to approximate a Gaussian distribution (with azimuthal symmetry):
\begin{align}\label{eq:Gaussian-bunch}
\begin{split}
	n_b(r,z) = n_{b0} ~ {\rm exp}\left({-\frac{r^2}{2\sigma_r^2}}\right) ~ {\rm exp}\left({-\frac{(z-z_{\rm m})^2}{2\sigma_z^2}}\right)
	
	
	\end{split}
\end{align}
where the beam parameters are as follows:
\begin{enumerate}[label=\roman*. ,topsep=0pt, itemsep=0ex,partopsep=0ex,parsep=0ex]
\item $\sigma_z$ is the standard deviation along the longitudinal dimension of the Gaussian bunch and characterizes its bunch length.
\item $\sigma_r$ is the standard deviation along the radial dimension (under transverse symmetry) of the Gaussian bunch and characterizes the bunch waist-size at tube entrance.
\item $n_b(r,z)$ is the beam density ($n_{b0}=\frac{N_b}{(2\pi)^{3/2} \sigma_r^2 \sigma_z}$ is the peak density at $r=0$ and $z = z_{\rm m}$).
\item $N_b$ is the number of beam particles and $Q_b = {\rm sgn}[Q_b] ~ e ~ N_b$ is the bunch charge, and $N_b =  \int_{-\infty}^{\infty} \int_0^{\infty} \int_0^{2\pi}  n_b(r,z) ~ d\theta ~ r dr ~ dz$.
\item $\vec{v_b}=\boldsymbol\beta_b c$ is beam velocity and $\gamma_b = (1-\beta_b^2)^{-1/2}$.
\end{enumerate}

The electric field lines of a gaussian bunch of ultra-relativistic charged particles, $\gamma_b\gg1$ are predominantly radial and perpendicular to the direction of the bunch velocity, $|\boldsymbol\beta_b|=\sqrt{1 - 1/\gamma_b^2}$. The radial electric field $E_b(r, z)$ of the beam assuming azimuthal symmetry and $\gamma_b\gg1$ is obtained using Gauss's law,
\begin{align}\label{eq:fields-Gaussian-bunch}
\begin{split}
E_{\rm b}&(r, z) = - {\rm sgn}[Q_b] ~ \omega_{p}^2(n_0) ~ \frac{m_e}{e}\frac{n_{b0}}{n_0} ~ \times \\
& \qquad \frac{\sigma_r^2}{2\pi} ~ \frac{\left[ 1 - {\rm exp}\left( -\frac{r^2}{2\sigma_r^2} \right) \right] }{r} ~ {\rm exp}\left({-\frac{(z-z_{\rm m})^2}{2\sigma_z^2}}\right)
	\end{split}
\end{align}
The beam is here assumed to be in a classical state (plasma, $\omega_{p}$) but it may also attain a quantum state when it satisfies the conditions on $\Gamma$ and $\chi$ in sec.\ref{subsec:quantum-state}.

As the beam undergoes focusing being acted upon by the radial fields of the extreme plasmon, its profile gets modified and the field changes to $- \mathrm{ sgn}[Q_b] ~ \omega_{p}^2(n_0) ~ \frac{m_e}{e} ~ \frac{n_{b0}(\xi)}{n_0} ~ \int_{0}^{r} dr ~ \mathcal{P}(r,z,\xi)$, where $\mathcal{P}(r,z,\xi)$ is the profile function of the continually focused beam. Here, we simplify the analysis assuming that the profile changes slowly and remains Gaussian.
