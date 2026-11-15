---
doc_id: arxiv-2105.09342v1
doc_title: "A Unitary Matrix Model for q-deformed Plancherel Growth"
section_id: sec-007-5-the-hilbert-space
section_title: "The Hilbert space"
section_number: 5
pages: 17-18
source_pdf: 2105.09342v1.pdf
source_sha256: 57ae12327da7b9a1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.983
doc_brief: "A Unitary Matrix Model for q-deformed Plancherel Growth — In this paper we construct a unitary matrix model that captures the asymptotic growth of Young diagrams under q-deformed Plancherel measure."
---
\label{sec:hilbertspace}

Following \cite{ Chattopadhyay:2020rle,Chattopadhyay:2019pkl} we give a Hilbert space description of the \qd growth process. Using the connection between unitary matrix model and free Fermi droplet description, we map the Young diagrams in automodel class to different shapes of two dimensional phase space droplets. Quantising these droplets, we further set up a correspondence between automodel diagrams and coherent states in the Hilbert space. Thus, growth of Young diagrams are mapped to evolution of coherent states in the Hilbert space. The basic construction of the Hilbert space is similar to the one considered in \cite{Chattopadhyay:2019pkl}. We briefly review the construction in \ref{app:hi}.

The Hilbert space $\cH$ is a direct product of $\cH_+$ and $\cH_-$ where $\cH_\pm$ are the Hilbert spaces associated with the $+$ and $-$ sectors defined in section \ref{sec:umm-droplet} namely the upper and the lower fermi surfaces. These two sectors are isomorphic. A generic state in $\cH_+$ is given by

\ben
\ket{\vec k} = \prod_{n\geq 1} (a^\dagger_n)^{k_n}\ket{s}
\een

where $a^\dagger_n$s are creation operators in $\cH_+$ and $\ket{s}$ is the ground state annihilated by $a_n$s. $\ket{\vec k}$ satisfies the completeness relation (\ref{eq:completeness}). Therefore, $(1/\sqrt{z_{\vec k}})\ket{\vec k}$ is the normalised excited state. One can also define coherent states in the Hilbert space $\cH_+$,

\ben
\ket{\tau_+} = \exp\lb \sum_{n=1}^\infty\frac{\tau_n^+ a_n^\dagger}{n\hbar}\rb \ket{s}. 
\een


We set up a map between a state $\ket{\psi} \in \cH_+$ and shape of the upper Fermi surface

\ben\label{eq:maping}
\ket{\psi} \ra \{\bra{\psi}\bar{h}_+(\theta)\ket{\psi}\}.
\een


Such a mapping has been discussed in \cite{Chattopadhyay:2020rle}. Expectation value of $\bar h_+$ in ground state is given by $\frac12 + s \hbar$ and has zero dispersion. Thus, the ground state $\ket s$ corresponds to an overall shift of $\bar h_+$ by an amount $s/N$ over the classical value. Generic \emph{normalised} excited states correspond to ${\cal O}(\hbar)$ ripples on $\bar h_+$. In this case, the expectation value of $\bar{h}_+$ picks up a non-zero dispersion at ${\cal O}(\hbar)$. ${\cal O}(1)$ deformations of the upper Fermi surface $\bar{h}_+$ are mapped to coherent states $\ket{\tau_+}$ in $\cH_+$ as is evident from (\ref{eq:coherentprofile}). An important thing to note here is that the classical deformations do not disturb the quadratic profile of the droplets \emph{i.e} for a given $\theta$, there exists unique values of $h_\pm(\theta)$.

We first consider the state corresponding to automodel diagrams for ordinary Plancherel growth \cite{Chattopadhyay:2019pkl}. The automodel diagrams corresponds to

\ben
\bar h_\pm(\theta) = \pm \lb \frac12 +\xi \cos\theta\rb. 
\een

The set of coherent states with $\tau_1=\xi/2$ , $\tau_n = 0$ $\forall n > 1$ are mapped to the automodel diagrams. In particular, the state corresponding to the limit shape is given by

\ben
|\tau* \rangle = \text{exp}\left(\frac{a_{1}^{\dagger}}{2\hbar}\right) |0\rangle. \quad
\een


Our final goal is to find the coherent state associated with automodel diagrams for \qd Plancherel growth. For the \qd automodel class, the variable $\bar h_+(\theta)$ is given by
\begin{equation}
    \bar{h}(t,\theta)=\frac{1}{2}-\frac{1}{2\lambda}\log(1-2\lambda \xi \cos \theta +\lambda^2 \xi^2)=\frac12 + \sum_{n=1}^{\infty}\frac{\xi^n \lambda^{n-1}}{n}\cos n\theta. 
\end{equation}
Therefore the coherent state associated to q-automodel class is given by
\ben
\ket{\tau^+_q} = \exp\lb {\sum_{n=1}^\infty \frac{\t_{n}^+ a_n^\dagger}{n\hbar}}\rb \ket{s},\quad \where \quad \tau^+_n = \frac{\xi^n \lambda^{n-1}}{n}.
\een
