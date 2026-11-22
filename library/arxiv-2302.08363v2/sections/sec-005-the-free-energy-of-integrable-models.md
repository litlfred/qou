---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-005-the-free-energy-of-integrable-models
section_title: "The free energy of integrable models"
section_number: null
pages: 11-14
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.995
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Two-dimensional, integrable, asymptotically free quantum field theories are an interesting family of toy 
models where one can obtain an explicit but highly non-trivial trans-series 
for the free energy \cite{fkw-letter,fkw, volin, mr-ren, abbh1, 
abbh2, mmr, dmss, mmr-an, bbv, bbhv, 
bbhv2, mmr-theta, bbv2,s-thompson}, and therefore one can hope that the 
convergent property of the partial series can be 
tested in detail. 




In integrable quantum field theories, the free energy is a quantity that can be computed after we 
introduce into the Hamiltonian $\mathsf{H}$ a chemical potential $h$ coupled to a conserved charge $\mathsf{Q}$:

\begin{equation}
\mathsf{H} \rightarrow \mathsf{H} - h \mathsf{Q}.
\label{eq_hamiltonian_mod}
\end{equation}

For each model, there can be different convenient choices of the charge $\mathsf{Q}$. 

The ground state of the Hamiltonian \eqref{eq_hamiltonian_mod} is a finite density state characterized by the free energy per unit volume

\begin{equation}
F(h) = -\lim_{V, \beta \rightarrow \infty} {1\over V\beta } \log {\Tr}\,  \re^{-\beta (\mathsf{H}-h \mathsf{Q})},
\end{equation}

where $V$ is the total volume of space and $\beta$ is the total length of Euclidean time. For convenience, we will write our 
equations in terms of

\begin{equation}
\label{subF}
\mathcal{F}(h) = F(h) - F(0).
\end{equation}

As found by Polyakov and Wiegmann \cite{pw,wiegmann}, $\CF(h)$ can be computed by the Bethe ansatz. This amounts to 
the following integral equation for a Fermi density $\epsilon(\theta)$:

\begin{equation}
\epsilon(\theta)-\int_{-B}^B K(\theta-\theta') \epsilon (\theta') \rd \theta' = h-m \cosh(\theta),\quad \theta \in[-B,B].
\label{eq_epsilon_integral_equation}
\end{equation}

In this equation, $m$ is the mass of the particles charged under $\mQ$. The kernel of the integral equation $K(\theta)$ is given by 

\begin{equation}
K(\theta) = \frac{1}{2\pi\ri} \frac{\rd}{\rd \theta} \log S(\theta),
\end{equation}

where $S(\theta)$ is the $S$-matrix appropriate for the scattering of the charged particles. 
The endpoints $\pm B$ of the Fermi density are fixed by the boundary condition

\begin{equation}
\epsilon(\pm B) = 0.
\label{eq_boundary_condition_0}
\end{equation}

As we will see later, the boundary condition determines the parameter $B$ in terms of $h/m$. 
Once we find the solution $\epsilon(\theta)$ to \eqref{eq_epsilon_integral_equation}, the free energy is given by

\begin{equation}
\mathcal{F}(h) = -\frac{m}{2\pi} \int_{-B}^B \epsilon(\theta) \cosh(\theta) \rd\theta.
\label{eq_free_energy_integral}
\end{equation}

Note that we calculate $\CF(h)$ for $h>m$, such that the ground state has particles in it. 
At the threshold value $h=m$, the one particle state has the same energy as the vacuum and we have $\CF(m)=0$. 
In fact, $\CF(h)$ has a branch cut singularity as $h\rightarrow m^+$, as it can be verified 
by explicit calculations, see \figref{fig-singfh}. For example, for the $O(3)$ non-linear sigma model, one has \cite{hmn}

\be
\CF(h) \sim (h-m)^{3/2}, \qquad h\rightarrow m^+. 
\ee

 \begin{figure}
\center
\includegraphics[width=.4\textwidth]{singulFh.pdf} 
\caption{The free energy $\CF(h)$ has a branch cut singularity at $h=m$.}
\label{fig-singfh}
\end{figure}



While it might be easy to numerically extract the 
free energy from \eqref{eq_epsilon_integral_equation} and 
\eqref{eq_free_energy_integral}, the key challenge is to study these 
equations in the weakly coupled regime $h \gg m$, which 
corresponds to the limit $B \gg 1$, and to extract the complete 
asymptotics, including exponentially small corrections. In 
\cite{volin}, a powerful technique to extract perturbative 
corrections was found, while in \cite{mmr-an} an analytic method 
to extract exponentially small corrections analytically, directly from the Bethe ansatz,  
was developed. More recently, \cite{bbv2} put together these 
two developments and obtained explicit results for the full 
trans-series. Since 
we will only consider the very first partial series, we will follow 
the method in \cite{mmr-an}. It is possible that more systematic results might be 
obtained by implementing the method of \cite{bbv2}. 

The first step is to reexpress \eqref{eq_epsilon_integral_equation}, 
\eqref{eq_boundary_condition_0}, \eqref{eq_free_energy_integral} in the Fourier space of the 
$\theta$ variable and use the Wiener--Hopf approach \cite{jap-w,hmn,fnw1}. 
We consider the Fourier transform of the kernel

\begin{equation}
\tilde{K}(\omega) = \int_\mathbb{R} \re^{\ri \omega \theta} K(\theta) \rd\theta
\end{equation}

and its Wiener--Hopf factorization

\begin{equation}
1-\tilde{K}(\omega) = \frac{1}{G_+(\omega) G_-(\omega)},
\end{equation}

where $G_\pm(\omega)$ is analytic in the upper (respectively, lower) 
complex half plane. The functions $G_\pm(\omega)$ will depend on the 
specific model, but we will only
consider the case in which $K(\theta)$ is an even function, which implies that $G_-(\omega) = G_+(-\omega)$. It will be convenient to define

\begin{equation}
\sigma(\omega) = \frac{G_-(\omega)}{G_+(\omega)}.
\label{eq_sigma_def}
\end{equation}

We further introduce

\begin{equation}
g_+(\omega) = \ri h \frac{1-\re^{2\ri B\omega}}{\omega} +
 \frac{\ri m\re^B}{2}\left( \frac{\re^{2\ri B\omega}}{\omega-\ri} - \frac{1}{\omega+\ri}  \right),
\label{eq_g}
\end{equation}

which is the Fourier transform of a function related to the 
expression appearing on the r.h.s. of the integral equation 
\eqref{eq_epsilon_integral_equation} (for details, see 
\cite{mmr-an}). Lastly, we define

\begin{equation}
\epsilon_\pm(\omega) = \re^{\pm\ri B \omega} \tilde{\epsilon}(\omega),
\end{equation}

where $\tilde{\epsilon}(\omega)$ is the Fourier 
transform of the Fermi density $\epsilon(\theta)$.

As shown in \cite{hmn,fnw1}, the integral equation \eqref{eq_epsilon_integral_equation} can be 
reformulated as the following equation

\begin{equation}
Q(\omega) = \frac{1}{2 \pi \ri} 
\int_\mathbb{R} \frac{G_-(\omega') g_+(\omega')}{\omega+ \omega'+ \ri 0} \rd \omega' 
+ \frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{\re^{2 \ri B\omega'} \sigma (\omega') Q(\omega')}{\omega+ \omega'+ \ri 0} \rd \omega',
\label{eq_Q_integral_equation}
\end{equation}

which has to be solved for $Q(\omega)$. The solution $Q(\omega)$ determines 
$\epsilon_+(\omega)$ through the equation

\begin{equation}
\frac{\epsilon_+(\omega)}{G_+(\omega)} = \frac{1}{2 \pi \ri} 
\int_\mathbb{R} \frac{G_-(\omega') g_+(\omega')}{\omega'-\omega- \ri 0} \rd \omega'+ 
\frac{1}{2 \pi \ri} \int_\mathbb{R} \frac{\re^{2 \ri B\omega'} \sigma (\omega')Q(\omega')}{\omega'- \omega- \ri 0} \rd \omega'.
\label{eq_epsilon_0}
\end{equation}

A relationship between $B$ and $h/m$ is determined by the boundary 
condition \eqref{eq_boundary_condition_0}, which in Fourier space takes the form

\begin{equation}
\lim_{\kappa \to +\infty} \kappa \epsilon_+(\ri \kappa)=0.
\label{eq_boundary_condition}
\end{equation}

Finally, from \eqref{eq_free_energy_integral}, the free energy can be written as

\begin{equation}
\mathcal{F}(h)= -{1\over 2 \pi} m \re^B \epsilon_+(\ri). 
\label{eq_free_energy_fourier}
\end{equation}
