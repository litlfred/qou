---
doc_id: arxiv-2404.02087v1
doc_title: "Extreme plasmons"
section_id: sec-012-fields-of-the-extreme-plasmon
section_title: "Fields of the extreme plasmon"
section_number: null
pages: 8-9
source_pdf: 2404.02087v1.pdf
source_sha256: ac92bd0dff8ad907
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.995
doc_brief: "Extreme plasmons — 15 sections: Extreme plasmons; Introduction; Quantum framework"
---
\label{sec:field-estimation}

When the existence, Eq.\ref{eq:existence-condition} and excitation condition, Eq.\ref{eq:excitation-condition} are satisfied, the kinetic model in Eq.\ref{eq:crunch-in-plasmon-kinetic} and the expression for $r_m$ in Eq.\ref{eq:r-max-nano-Gaussian}, allow determination of the net charge displaced in the plasmon. Using the net charge that crunches-in into the core region of the tube, magnitude of peak fields is obtained.

The total charge that builds up in the electron compression layer at $r_m$ during the outward radial excursion phase, is restored back towards the axis by the force of the uncovered ionic lattice. However, instead of merely reverting to their respective equilibrium positions, the excited electrons collectively cross the surface to crunch in towards the axis, $r=0$. 

During this crunch-in phase of radially inward electron compression, the force of ionic lattice ceases to exist for $r < r_t$. So, electrons continue to crunch in until the total compressed electron density results in a radial electric field, $E_r$ that opposes further compression. The electrons first crunch in to a minimum radius, $r_{c}$ at the longitudinal position, $\xi_{r_c}$. This minimum radius, $r_{c}$ is dictated by their initial acceleration at excitation.

The charge density that crunches in within the radial area enclosed by $r_{c}$ is calculated using the collective motion of all electrons between $r_m$ and $r_t$ to result in their collective collapse into the tube. 























































































































The net change displaced in the excited electron rings with infinitesimal slice thickness, $dz$, that crunch-in at the longitudinal position, $\xi_{r_c}$ of maximum inward compression (equal to the charge at maximum outward compression) using Eq.\ref{eq:r-max-nano-Gaussian} is,
\begin{align}\label{eq:charge-collective-rings-step-nano-Gaussian}
\begin{split}
\delta Q_{\rm m}&(\xi_{r_c})  = - e n_0 \pi (r_m^2 - r_t^2) ~ dz = - e n_{b0} \sigma_r^2 ~ dz


\end{split}
\end{align}

The minimum radius to which the electrons crunch-in to is represented relative to the tube radius, $r_{c} = r_t / (\mathscr{F}_Q\Theta)$, where $\Theta>1$. The minimum radius to which the electrons compress increases by $\mathscr{F}_Q$. The peak radial electric field using the net charge, $Q_m$, and its simplification using SI units is,
\begin{align}\label{eq:crunch-in-charge-radial-field-Gaussian}
\begin{split}



E_{r}(\xi_{r_c}) & = -\mathscr{F}_Q ~ \frac{2\Theta}{(2\pi)^{3/2}} ~ \frac{1}{r_t} ~ \frac{Q_b}{\sigma_z} \\
& = - \mathscr{F}_Q ~ \Theta ~ \frac{114.2}{r_t\rm[100nm]}  ~ \frac{Q_b{\rm [nC]} }{\sigma_z{\rm [100nm]} } {\rm \frac{TV}{m}}
\end{split}
\end{align}
Because the beam field, $E_b(r)$ outside the beam decreases radially, conduction electrons at increasing radial equilibrium positions $r_0>r_t$, gain decreasing initial momentum. Thereby, when electrons crunch into the tube each reaches a different crunch-in radius, $r_c(r_0,t)$ at any instant. $E_r(r)$, therefore, increases radially outwards until $r_t$, as the net crunched in charge increases. Consequently, $\Theta$ depends upon the excitation conditions.

The peak longitudinal field, $E_{z}$ is obtained using the Panofsky-Wenzel theorem \cite{Panofsky-Wenzel-theorem}, $\frac{1}{r}\frac{\partial rE_z}{\partial r} = -\frac{\partial E_r}{\partial \xi}$ or ${\rm lim_{\Delta\rightarrow 0}}\frac{\Delta r E_z}{\Delta r} = -r\frac{\Delta E_r}{\Delta \xi}$. $E_{z}$ radially varies over $\Delta r\simeq r_t$ as the phase of the radial field transitions from negative to positive over $\Delta \xi=\kappa \lambda_c$. The crunch-in wavelength for a given set of beam properties, $\lambda_c$ is itself proportional to the tube radius $r_t$ \cite{plasmonics-ieee-2022}. As the tube radius increases, per the excitation condition in Eq.\ref{eq:excitation-condition} the plasmon becomes less nonlinear. On the other hand, as $r_t\rightarrow 0$ (bulk media) $\lambda_c\simeq\lambda_Q$. Therefore, relativistically corrected wavelength of the surface crunch-in plasmon is, $\lambda_c = \lambda_Q \sqrt{\langle\gamma_e\rangle} ~ \left[ \frac{r_t}{\lambda_Q} + 1\right]$. 

An approximate expression for the average $\langle\gamma_e\rangle$ is obtained using $\Delta p_r = eE_b\frac{\sigma_z}{c} \gtrsim m_ec$, such that,
$\gamma_e = \sqrt{1 + \left(\frac{p_r}{m_ec}\right)^2 } \simeq \frac{\omega_{p}^2(n_0)}{c^2} ~ \frac{1}{r_t} ~ \frac{n_{b0}}{n_0} ~ \frac{\sigma_r^2\sigma_z}{2\pi}$. 
Using this $\gamma_e$, the peak longitudinal field, $E_{z}$ is evaluated as:
\begin{align}\label{eq:crunch-in-panofsky-wenzel-simplified-sigr-lte-rt}
\begin{split}
E_z & = E_{r} ~ \frac{r_t}{\kappa ~ 2\pi c} \frac{\omega_{Q}(n_0)}{\sqrt{\gamma_e} }

= E_{r} ~ \frac{r_{t}}{\kappa \sqrt{2\pi}} \sqrt{ \frac{n_0 r_t}{n_{b0} \sigma_r^2\sigma_z } }
\end{split}
\end{align}
The peak longitudinal field, $E_{z}(\xi_{r_c})$ is obtained using Eq.\ref{eq:crunch-in-charge-radial-field-Gaussian} with $\left(1+r_t/\lambda_Q\right)\simeq 1$ and simplified using SI units,
\begin{align}\label{eq:crunch-in-charge-acc-field-Gaussian}
\begin{split}
E_{z}&(\xi_{r_c}) 
= \frac{\mathscr{F}_Q}{\kappa} ~ \frac{\sqrt{2}}{(2\pi)^{7/4}} ~ \sqrt{\frac{Q_b}{e}} ~ \frac{\sqrt{r_t r_e}}{\sigma_z} ~ E_{Q} \\
& = \mathscr{F}_Q^2 ~ \frac{3}{4\kappa} \sqrt{n_0[{\rm cm^{-3}}] ~ r_t\rm[100nm]} \frac{\sqrt{Q_b{\rm [nC]}} }{\sigma_z{\rm [100nm]} } {\rm \frac{TV}{m}}
\end{split}
\end{align}

The expressions for peak electric fields in Eq.\ref{eq:crunch-in-charge-radial-field-Gaussian} and Eq.\ref{eq:crunch-in-charge-acc-field-Gaussian} are evaluated against previously published simulation results based on classical kinetic theory. 

From the nanoporous metal simulations in \cite{plasmonics-ieee-2021}, using $n_0 = 2\times 10^{22} {\rm cm^{-3}}$, $r_t = 100 {\rm nm}$, $Q_b = 315 ~ {\rm pC}$, and $\sigma_z=400{\rm nm}$; the peak radial field is, $E_r = \mathscr{F}_Q ~ \Theta ~ 9 ~ {\rm TV/m}$ and longitudinal field with $\kappa=0.25$ is, $E_z = \frac{\mathscr{F}_Q}{\kappa} 5.74 ~ {\rm TV/m}$. Similarly, for semiconductor plasmon simulations in \cite{plasmonics-ieee-2022}, with $n_0 = \mathrm{10^{18} cm^{-3}}$, $r_t = \mathrm{12.5\mu m}$, $n_{b0} = \mathrm{10^{18} cm^{-3}}$, $Q_b = 1.5 ~ {\rm nC}$ and $\sigma_z \simeq \mathrm{10 \mu m}$; the peak radial field is, $E_r = \mathscr{F}_Q ~ \Theta ~ 13.7 ~ {\rm GV/m}$ and peak longitudinal field with $\kappa=0.25$ is, $E_z = \frac{\mathscr{F}_Q}{\kappa} 39.4 ~ {\rm GV/m}$. This establishes a good agreement with both previously published simulation results validating the quantum model of extreme plasmon presented here. 

However, precise characteristics including $\Theta$, $\kappa$, and especially $\mathscr{F}_Q$ that emanates from the quantum nature need dedicated efforts to develop a comprehensive understanding. Our ongoing work including experiments \cite{slac-2023,slac-2022,slac-2020} is geared towards addressing this.
