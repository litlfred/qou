---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-005-spectral-statistics
section_title: "Spectral statistics"
section_number: null
pages: 21-22
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.992
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
\label{sec:spectral_statistics}

In the previous subsections, we have described the constraints imposed by crossing symmetry and typicality on the ensemble. We will now make one further assumption on our ensemble, again motivated by the theory of quantum chaos. Namely, we will assume that, to a good approximation, we can ignore the effects of non-trivial spectral statistics, treating $\rho(h,\bar h)$ fully classically. 

In chaotic many-body quantum systems, which are characterized by a ramp in the spectral form factor after the Thouless time \cite{Altland:2020ccq,Saad:2018bqo,Cotler:2016fpe}, this is indeed a valid assumption for early times, because the spectral variance  is exponentially suppressed in the entropy compared to the leading factorized contribution:
\begin{equation}
    \overline{\rho(E_i)\rho(E_j)} = \overline{\rho(E_i)}\,\, \overline{\rho(E_j)} \,\Big[1+ \mathcal{O}(\e^{-2S})\Big]\,.
\end{equation}
Indeed, in most treatments of the Eigenstate Thermalization Hypothesis it is a standard assumption that discrete sums can be replaced by integrals over products of smooth densities of states \cite{DAlessio:2015qtq}, ignoring any fluctuations around the average $\bar\rho$, because the time scales for thermalization are much shorter than the post-Thouless time scales where spectral rigidity becomes important.  

For chaotic 2d CFT's, one can also study the spectral variance in fixed spin sectors\footnote{For discussions of spectral statistics and the relation to 3d gravity, see \cite{Cotler:2020hgz,DiUbaldo:2023qli, Haehl:2023xys,Haehl:2023mhf, Haehl:2023tkr, deBoer:2025rct, Boruch:2025ilr,Perlmutter:2025ngj,Jafferis:2025jle}.} and formulate a version of late-time random matrix universality that is compatible with modular invariance. Under a suitable coarse-graining procedure, akin to Berry's diagonal approximation \cite{Berry1985SpectralRigidity}, the 2d CFT analog of the spectral form factor displays a linear ramp  \cite{DiUbaldo:2023qli}, which matches to the gravitational calculation of an off-shell torus wormhole $T^2\times I$ by Cotler and Jensen \cite{Cotler:2020ugk}. Recently, \cite{Perlmutter:2025ngj} made the `simple extreme conjecture', which formulates a precise statement of random matrix universality for the primary spectrum of Virasoro CFT's with $c>1$, in fixed spin sectors, in the asymptotic limit of large conformal dimension $\Delta$.

In this paper we do not account for the fluctuations of the primary-state density around its mean. In the discussion, we comment on corrections from higher statistical moments of 
$\rho(h,\bar h)$, and interpret these corrections gravitationally using the “RMT surgery’’ construction of \cite{deBoer:2025rct}. In the main text, however, we make the replacement:
\begin{equation}\label{eq:rho_factorized}
    \overline{\prod_{e_i\in \Gamma_\mathcal{C}}\rho(h_i,\bar h_i)\!\!\!\prod_{v_{ijk}\in \Gamma_\mathcal{C}}\!\!\!\!C_{ijk}} \,\,\boldsymbol{\longrightarrow} \prod_{e_i\in \Gamma_\mathcal{C}}\!\!\overline{\rho(h_i,\bar h_i)}\times\overline{\prod_{v_{ijk}\in \Gamma_\mathcal{C}}\!\!\!\!C_{ijk}}\,.
\end{equation}
That is, we factorize moments of the density of states into products of the mean density $\bar\rho$,
 while retaining the full (non-factorized) OPE statistics.

The above simplification parallels that of \cite{Chandra:2022bqq}, with the only difference that in their CFT ensemble, the mean spectral density was further approximated by $\overline{\rho(h,\bar h)} \approx \rho_0(h)\rho_0(\bar h)$, where $\rho_0$ is the universal Cardy density of states \cite{Collier:2019weq}. By contrast, in this paper we subject the mean $\bar\rho$ to the constraints of modular invariance \eqref{eq:Tinvariance}-\eqref{eq:Sinvariance}. This refinement of the approach of \cite{Chandra:2022bqq} will be essential for identifying some non-handlebody saddles in section \ref{sec:minimal completion}.


The simplification \eqref{eq:rho_factorized} can also be motivated from the bulk. Replacing the statistical moments of $\rho$ by products of means plus \emph{connected} spectral correlations effectively separates out contributions from different bulk topologies. The connected terms---which we neglect---arise exclusively from \emph{off-shell} bulk geometries. As shown by Maloney and Witten \cite{Maloney:2007ud}, any 3-manifold with more than one asymptotic torus boundary is necessarily off-shell (i.e.~non-hyperbolic). Since higher connected moments of $\rho$ are generated by precisely such multi-boundary torus wormholes, all spectral statistics beyond the mean $\bar\rho$ correspond to off-shell topologies. The RMT surgery framework of \cite{deBoer:2025rct} provides a systematic way to build some of these off-shell contributions by `gluing in' torus wormholes. 

Although a complete ensemble description of 3d gravity must ultimately include such off-shell effects, here we focus solely on the contributions from on-shell topologies. Even at this level, the resulting bulk sum includes many nontrivial 3-manifolds. In the next section we begin assembling the sum over topologies, and see to what extent they solve the boundary constraints imposed in this section.
