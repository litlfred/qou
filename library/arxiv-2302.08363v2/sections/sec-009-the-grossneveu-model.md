---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-009-the-grossneveu-model
section_title: "The Gross–Neveu model"
section_number: null
pages: 24-25
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 1.0
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
\label{sec_gross_neveu}

The Gross--Neveu model is an integrable model of $N$ Majorana fermions in 1+1 dimensions with a quartic interaction. 
We restrict ourselves to the case $N>4$. Its Lagrangian is given by 

\begin{equation}
\CL = \frac{\ri}{2}\bar{\boldsymbol{\chi}}\cdot\slashed{\partial}\boldsymbol{\chi}+\frac{g^2}{8}\left(\bar{\boldsymbol{\chi}}\cdot\boldsymbol{\chi}\right)^2.
\end{equation}

This model is integrable and its $S$-matrix is known exactly. As in (\ref{eq_hamiltonian_mod}), we 
will introduce a chemical potential $h$ coupled to a conserved charge $\mathsf{Q}$, which will be 
chosen as in \cite{fnw1,fnw2}. In the Gross--Neveu case, the Wiener--Hopf formalism can be 
slightly simplified, and as described in \cite{fnw1,mmr-an}, one can encode the solution to \eqref{eq_Q_integral_equation} in a function $u(\omega)$ 
that solves the integral equation

\begin{equation}
u(\omega) = \frac{\ri}{\omega}+ \frac{1}{2\pi\ri}\int_\IR \frac{\re^{2\ri B \omega'}\rho(\omega')u(\omega') }{\omega'+\omega+\ri 0} \rd \omega'.
\label{inteq_u}
\end{equation}

The boundary condition \eqref{eq_boundary_condition_0} reads in this case

\begin{equation}
u(\ri) = \frac{m \re^B}{2h} \frac{G_+(\ri)}{G_+(0)}.
\label{u_bc}
\end{equation}

The 
function $\rho(\omega)$ in \eqref{inteq_u} is defined as

\begin{equation}
\rho(\omega) = - \frac{\omega+\ri}{\omega-\ri}\sigma(\omega),
\label{rhofunc_def}
\end{equation}

where $\sigma(\omega)$ was introduced in \eqref{eq_sigma_def}. The Wiener--Hopf decomposition of the kernel gives

\begin{equation}
G_+(\omega)=\re^{-\frac{\Upsilon}{2}\ri\omega\left[1-\log\left(-\frac{\Upsilon}{2}\ri\omega\right)\right]+\frac{1}{2}\ri\omega[1-\log(-\frac{1}{2}\ri\omega)]} \frac{\Gamma\big(\frac{1}{2} - \frac{\Upsilon}{2}\ri\omega\big)}{\Gamma\big(\frac{1}{2} - \frac{1}{2}\ri\omega\big)},\quad \Upsilon = \frac{N-4}{N-2}.
\label{GN_Gplus_usec}
\end{equation} 
Lastly, the free energy (\ref{subF}) can be obtained directly from  $u(\omega)$ through
\begin{equation}
\CF(h) = - \frac{h^2}{2\pi}u(\ri)G_+(0)^2\left(1- \frac{1}{2\pi\ri}\int_\IR \frac{\re^{2\ri B \omega'}\rho(\omega')u(\omega') }{\omega'-\ri} \rd \omega'\right).
\label{fh-u}
\end{equation}











Using the techniques described in \cite{mmr-an}, which we outline in section \ref{gn-sum}, 
one can extract the trans-series expansion of the free energy from the integral equation.
As found therein, the trans-series can be written as

\begin{equation}
\Phi_\pm({\alpha}) = \varphi_0(\tilde{\alpha})+ \CC_{\text{IR}}^\pm \re^{-\frac{2}{\tilde{\alpha}}} \tilde{\alpha}^{2\Delta}
+ \sum_{\ell\geq 1} \CC_\ell^\pm \re^{-\frac{2}{1-2\Delta}\frac{\ell}{\tilde{\alpha}}}\tilde\alpha^{\frac{2\Delta}{1-2\Delta}\ell}\varphi_\ell(\tilde{\alpha}).
\label{free-energy-ts}
\end{equation}

The observable itself is then given by Borel summation,

\begin{equation}
\CF(h) = - \frac{h^2}{2\pi} s_\pm(\Phi_\pm)(\tilde{\alpha})= - \frac{h^2}{2\pi}\left\{\sum_{\ell\geq 0} y^\ell \CC_\ell^\pm s_\pm(\varphi_\ell)(\tilde{\alpha}) + \CC_{\text{IR}}^\pm \re^{-\frac{2}{\tilde{\alpha}}} \tilde{\alpha}^{2\Delta}\right\},\label{sum-kappa}
\end{equation}

where

\begin{equation}
\CC^\pm_0=1,\quad
y = \re^{-\frac{2}{\Upsilon\tilde{\alpha}}}\tilde\alpha^{\frac{2\Delta}{\Upsilon}},\quad \Upsilon = 1-2\Delta,\quad \Delta = \frac{1}{N-2}.
\end{equation}

This trans-series is expressed in terms of the auxiliary coupling defined as

\begin{equation}
\frac{1}{\tilde{\alpha}}-\Delta\log\tilde{\alpha}=\log\frac{h}{\Lambda},
\label{tilde-alpha-def}
\end{equation}

where $\Lambda$ is the dynamically generated scale. This scale can be related to the non-perturbative mass of the model through the mass gap derived in \cite{fnw1,fnw2},
\begin{equation}
\frac{m}{\Lambda} = \frac{(2\re)^\Delta}{\Gamma(1-\Delta)}.
\label{eq_mass_gap_GN}
\end{equation}
As previously outlined, the key test is to reorganize the asymptotic series $\varphi_{\ell}(\tilde{\alpha})$



and consider the radius of convergence of the series $\CG_n(y)$ indexed by $\tilde{\alpha}^n$.



As in (\ref{eq_free_energy_transseries}), the single, distinct, IR renormalon term proportional to
$\re^{-\frac{2}{\tilde{\alpha}}} \tilde{\alpha}^{2\Delta}$ is not relevant for the analysis of the trans-series convergence.
