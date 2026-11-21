---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-006-bosonic-models
section_title: "Bosonic models"
section_number: null
pages: 14-15
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 1.0
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
Using the techniques described in \cite{mmr-an}, one can extract the trans-series of the free energy from the equations above. 
In this section we will concentrate on the bosonic models, which include the $O(N)$ non-linear sigma model 
and the $SU(N)$ principal chiral field (PCF). The structure of the trans-series is generically given by

\begin{equation}
\Phi_\pm(\tilde{\alpha}) = \sum_{\ell\geq 0} y^\ell \varphi_\ell(\tilde{\alpha}) + \mathcal{C}_{\text{IR}}^\pm \tilde{\alpha}^{2-2a} \re^{-2/\tilde{\alpha}},
\label{eq_free_energy_transseries}
\end{equation}

where $\tilde{\alpha}$ is a conveniently defined coupling (see \eqref{eq_alpha_tilde_def} below) and $y = \tilde\alpha^{-2a\xi_1} \re^{-2\xi_1/\tilde{\alpha}}$ (see below for the definition of $\xi_1$) is the appropriate exponentially small term in the present example. The second term in the r.h.s. is an IR renormalon term and it is not relevant for the analysis of the trans-series convergence. The free energy can be recovered from Borel resummation of \eqref{eq_free_energy_transseries} as
\begin{equation}
\mathcal{F}(h) = -\frac{k^2 h^2}{4 \tilde{\alpha}} s_\pm \bigl( \Phi_\pm \bigr)(\tilde{\alpha}) = -\frac{k^2 h^2}{4 \tilde{\alpha}}\left\{ \sum_{\ell\ge 0} y^\ell s_\pm (\varphi_\ell) (\tilde{\alpha}) + \mathcal{C}_{\text{IR}}^\pm  \tilde{\alpha}^{2-2a} \re^{-2/\tilde{\alpha}} \right\}.
\end{equation}

The coupling $\tilde{\alpha}$ that we use for the trans-series expansion is defined as

\begin{equation}
\frac{1}{\tilde{\alpha}} + \left( a - \frac{1}{2} \right) \log \tilde{\alpha} = \log \frac{h}{\Lambda},
\label{eq_alpha_tilde_def}
\end{equation}
where $\Lambda$ is the dynamically generated scale in the $\overline{\text{MS}}$ scheme. This is a convenient choice of coupling that makes possible the contact with standard perturbative results, when one computes the free energy directly from the Lagrangian. The parameters $k$ and $a$ can be extracted from the behavior of $G_+(\omega)$ near the origin:

\begin{equation}
G_+(\ri\xi) = \frac{k}{\sqrt{\xi}} \bigl( 1 - a\xi \log\xi - b\xi + \mathcal{O}(\xi^2) \bigr), \quad \xi >0.
\label{eq_G_series}
\end{equation}

The structure of \eqref{eq_G_series} is valid for generic bosonic models, but it does 
not apply to fermionic models and, for this reason, we have to treat them separately in 
section \ref{sec_gross_neveu}. Further, we denote by $\xi_\ell$ the singularities of $\sigma(\ri\xi)$ 
at $\xi>0$, which we assume to be equally spaced\footnote{This holds in the models we study here, but it is not a generic property of bosonic models.}: $\xi_\ell = \xi_1 \ell$. This determines the set 
of exponentially small terms that we find in the trans-series \eqref{eq_free_energy_transseries} of the free energy. Lastly, as we will see in the explicit computation further below, the coefficients determining each formal power series $\varphi_\ell(\tilde{\alpha})$ can be expressed as multinomials in the residues
\begin{equation}
\ri\sigma^\pm_\ell = \Res_{\xi=\xi_\ell\mp \ri 0} \sigma(\ri\xi),
\end{equation}
which have an imaginary ambiguity (denoted by the two possible sign choices) due to the presence of a branch cut along $\xi>0$.  Thus, the coefficients of $\varphi_\ell(\tilde{\alpha})$ are also themselves ambiguous. See Fig. \ref{fig_residue_ambiguity} for the singularity structure of $\sigma(\omega)$ and an illustration of how the residues depend on the branch choice.
\begin{figure}
\centering
\includegraphics[scale=1]{residue_ambiguity.pdf}
\caption{Generic singularity structure of $\sigma(\omega)$. The second integral in \eqref{eq_Q_integral_equation} or \eqref{eq_epsilon_0} is integrated over $\mathbb{R}$, but we deform the contour upwards, picking the discontinuity of $\sigma(\omega)$ and its residues. The residues will depend on the branch choice for $\sigma(\omega)$, as illustrated by tilting the branch cut with a small angle.}
\label{fig_residue_ambiguity}
\end{figure}
