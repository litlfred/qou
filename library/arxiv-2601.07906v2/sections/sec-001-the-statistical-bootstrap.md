---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-001-the-statistical-bootstrap
section_title: "The statistical bootstrap"
section_number: null
pages: 10-11
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.988
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:2}

The goal of this section is to define a statistical theory that models compact irrational CFT$_2$'s with a pure Einstein gravity dual at large central charge $c$ \cite{Hartman:2014oaa}. Such CFT$_2$'s have no extended chiral algebra beyond Virasoro symmetry, so we will organize the spectrum of $(L_0,\bar L_0)$ into Virasoro primaries and descendants. The descendant states are fixed by symmetry, so they should not be treated as random variables. On the other hand, the conformal primaries will be treated statistically. 

Let us imagine there exists a probability distribution $\mu(\{h_i, \bar h_i, C_{ijk}\})$ that we can use as a statistical model for the dynamical CFT$_2$ data, which consist of the infinite list of primary conformal dimensions $\Delta_i = h_i+\bar h_i$, integer spins $J_i = h_i-\bar h_i$ and primary OPE coefficients $C_{ijk} \equiv C_{h_ih_jh_k}$. We package the spectral data in terms of the density of primary states,
\begin{equation}
    \rho(h,\bar h) = \sum_i \delta(h_i-h)\delta(\bar h_i - \bar h),
\end{equation}
where the sum is over the primary spectrum,
with a similar formula for the density of OPE coefficients (as in \cite{Collier:2019weq}).
The average of any function of OPE coefficients and conformal weights is then defined by integrating it against the measure $\mu$:\vspace{2mm}
\begin{equation}
    \overline{F(\{h_i,\bar h_i,C_{ijk}\})} = \int \d L_0 \d \bar L_0 \d C \,\mu(\{h_i, \bar h_i, C_{ijk}\})F(\{h_i,\bar h_i,C_{ijk}\}).\vspace{2mm}
\end{equation}
Here $\d C$ is a volume element on the space of rank-3 tensors.

Crucially, we will impose a number of conditions on the moments of this probability distribution $\mu$, such that the statistical model is a good approximation of a holographic CFT$_2$ in the large-$c$ limit.\footnote{In particular, we do not assume that the average is taken over an ensemble of `true' CFT's. For an exploration of probability distributions on the space of 2d CFT's, see the recent work \cite{Belin:2025qjm}. Also, for a more in-depth discussion about the notion of an `approximate CFT' we refer the reader to section 2 of \cite{Belin:2023efa}.}  The goal of this section is to specify these conditions, which we will refer to as the ``statistical bootstrap''. We will mostly assume that the spectrum of $(L_0,\bar L_0)$ has a twist gap all the way up to the black hole threshold, meaning that $h_i,\bar h_i$ is either zero (the vacuum, denoted by $\mathds{1}$) or bigger than $\frac{c-1}{24}$. However, the material presented in this section can also be extended to incorporate states below the threshold in the conical defect regime \cite{Benjamin:2020mfz}, as will be discussed in section \ref{sec:3}.

Let us emphasize that although we take the conditions considered in this section to be \emph{necessary}, they need not be sufficient: we have not exhausted all constraints on the distribution $\mu$ that one may want to impose. In the discussion, we comment on the possibility of imposing additional constraints on the moments, that arise (for example) from positivity of $\mu$ and the Stieltjes/Hamburger moment problem.
