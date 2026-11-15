---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-007-41-hyperbolic-volumes-twisted-torsion-and-large
section_title: "Hyperbolic volumes, twisted torsion, and large N"
section_number: 4.1
pages: 13-15
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.956
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:vol}

The most fundamental relation between complex Chern-Simons theory and hyperbolic geometry has been understood for a long time, and concerns the semi-classical asymptotic expansion of partition functions \cite{DIWitten-gravCS} (see also \cite{DIgukov-2003, DIGukovMurakami}). It is easiest to formulate it first in terms of the ``holomorphic blocks'' $\CalB_\alpha,\,\widetilde\CalB_\alpha$ appearing in \eqref{DI.fact}, labelled by flat connections $\alpha$\,:

\DIbe \label{DI.B-asymp}
\begin{array}{ll} \text{as $k+is\to\infty$ or $q^{\frac12} = e^{\frac{2\pi i}{k+is}}\to 1$}\,,\qquad & \ds \CalB_\alpha(q^{\frac12}) \sim \sqrt{\frac{4\pi^3}{\tau(\alpha)}}e^{\frac{i(k+is)}{8\pi}S_{CS}(\alpha)}\,; \\[.2cm]
\text{as $k-is\to\infty$ or $\tilde q^{\frac12} = e^{\frac{2\pi i}{k-is}}\to 1$}\,,\qquad & \ds \widetilde \CalB_\alpha(\tilde q^{\frac12}) \sim \sqrt{\frac{4\pi^3}{\tau(\alpha)^*}}e^{\frac{i(k-is)}{8\pi}S_{CS}(\alpha)^*}\,;
\end{array}
\DIee

where $S_{CS}(\alpha)$ is the classical Chern-Simons action evaluated on a particular flat connection and $\tau(\alpha)$ is the analytic Ray-Singer torsion twisted by the flat connection $\alpha$ \cite{DIRaySinger}. This is the standard result expected from Chern-Simons perturbation theory \cite{DIBW-cx}. In the presence of a boundary, the classical action and torsion on the RHS depend on the choice of boundary conditions (boundary holonomies) for $\alpha$. From \eqref{DI.fact}, it then follows that if both $k+is\to\infty$ and $k-is\to \infty$

\DIbe \CalZ[M]_{k,s} \sim \sum_{\text{flat $\alpha$}} \frac{1}{|\text{Stab}(\alpha)|} \frac{4\pi^3}{|\tau(\alpha)|} e^{\frac{ik}{4\pi}\text{Re}\,S_{CS}(\alpha)-\frac{is}{4\pi}\text{Im}\,S_{CS}(\alpha)}\,. \label{DI.sum-asymp} \DIee

The formula is particularly meaningful if $s$ is analytically continued to (say) positive imaginary values. Then each term in \eqref{DI.sum-asymp} shows exponential growth or decay at large $|s|$, controlled by $\text{Im}\,S_{CS}(\alpha)$. 


Now suppose that $M$ is hyperbolic, meaning that it admits a hyperbolic metric. The hyperbolic metric is unique (given suitable boundary conditions) and is a topological invariant of $M$ \cite{DImostow-1973, DIthurston-1980}. Moreover, the vielbein and spin connection of the hyperbolic metric can be rewritten as a flat $SL(2,\BC)$ connection $\alpha_{\rm hyp} = w+ie$, with the property that $\text{Im}\,S_{CS}(\alpha_{\rm hyp}) = \text{Vol}(M)$ is the hyperbolic volume of $M$. The real part $\text{Re}\,S_{CS}(\alpha_{\rm hyp})$ is known as the Chern-Simons invariant of the hyperbolic structure, and provides a natural complexification of the hyperbolic volume \cite{DICheegerSimons, DIChernSimons}. It is also useful to note that the connection $\alpha_{\rm hyp}$ necessarily has a trivial stabilizer -- the connection is fundamentally non-abelian.

Therefore, if the gauge group is $SL(2,\BC)$ and $M$ is hyperbolic, the sum \eqref{DI.sum-asymp} contains a term that is controlled by the hyperbolic volume of $M$. Typically, $\text{Im}\,S_{CS}(\alpha_{\rm hyp})$ is larger than the ``volume'' of any other flat connection, and the entire sum \eqref{DI.sum-asymp} is dominated by the hyperbolic volume. (It is expected that $\text{Im}\,S_{CS}(\alpha_{\rm hyp})$ always dominates, but no general result of this type has been proven.)


It is often useful to strip off the holomorphic part of the asymptotic expansion. This can be done by taking a \emph{singular} limit: we fix $k=1$, analytically continue $s$ to imaginary values, and send $s\to - ik=-i$. This has the effect of sending $q\to 1$ but $\tilde q\to 0$, which trivializes the anti-holomorphic blocks, $\widetilde \CalB_\alpha(\tilde q^{\frac12})\to 1$. In this singular limit, we expect

\DIbe \CalZ[M]_{1,s} \sim \sum_{\text{flat $\alpha$}} \frac{1}{|\text{Stab}(\alpha)|} \sqrt{\frac{4\pi^3}{\tau(\alpha)}} e^{-\frac{1}{\hbar}S_{CS}(\alpha)}\qquad\text{as}\quad \hbar=2\pi i\frac{1-is}{1+is}\to 0\,. \label{DI.sing1} \DIee

This sort of limit played a major role in early analyses of partition functions for complex Chern-Simons theory \cite{DIhikami-2006, DIDGLZ}, though it was not realized at the time that the partition functions (derived from quantum Teichm\"uller theory) being analyzed had fixed level $k=1$.

The fact that the perturbative expansion of complex Chern-Simons theory (or individual holomorphic blocks, as in \eqref{DI.B-asymp}) contains geometric invariants of $M$ played a major role in providing a physical justification for the Volume Conjecture, and generalizing it. The original Volume Conjecture \cite{DIkashaev-1997, DIMur-Mur} claims that a particular double-scaling limit of colored Jones polynomials of a knot $K\subset S^3$ leads to exponential growth, controlled by the hyperbolic volume of the knot complement $\text{Vol}(S^3\bs K)$. This was justified in \cite{DIgukov-2003} by embedding $SU(2)$ Chern-Simons theory (which computes colored Jones polynomials) into a holomorphic sector of $SL(2,\BC)$ Chern-Simons theory, and arguing that the asymptotic expansions of $SU(2)$ and (holomorphic) $SL(2,\BC)$ theories should coincide. The argument immediately led to generalizations, involving higher-order terms in the asymptotic expansion and a dependence on boundary conditions, which have been carefully checked in many computations, \DIcf\ \cite{DIGukovMurakami, DIDGLZ, DIDG-quantumNZ}.





It is also interesting to consider ``large-$N$'' limits in complex Chern-Simons theory, taking the gauge group to be $SL(N,\BC)$ and sending $N\to\infty$. Physically, such limits are most conveniently studied by realizing Chern-Simons theory on a stack of $N$ M5 branes (Section \ref{DI.sec:sym}), and using AdS/CFT or large-$N$ duality. A study of the five-brane system \cite{DIHenningsonSkenderis, DIHMM-anomalies, DIGKW-5branes} predicts that the leading asymptotic growth of the partition function $\CalZ[M]_{k,s}$ as in \eqref{DI.sum-asymp} is scales as $N^3\text{Vol}(M)$ at large $N$ \cite{DIDGG-Kdec}. This is not surprising: the hyperbolic flat $SL(2,\BC)$ connection can be embedded into $SL(N,\BC)$ by using the $N$-dimensional representation $\rho_N:SL(2,\BC)\to SL(N,\BC)$, and the Chern-Simons functional evaluates to $\sim N^3\text{Vol}(M)$ on $\rho_N(\alpha_{\rm hyp})$, \DIcf\ \cite{DIGTZ-slN}. As long as \eqref{DI.sum-asymp} is dominated by the flat connection $\rho_N(\alpha_{\rm hyp})$ for any $N$, one quickly recovers the scaling prediction.
 Much more non-trivially, the M-theory analysis predicts that the logarithm of the \emph{torsion} $\tau(\rho_N(\alpha_{\rm hyp}))$ will grow as $N^3\text{Vol}(M)$ \cite{DIMPS-S3b, DIGKL-largeN} at large $N$ as well. This latter result was recently proved by Porti and Menal-Ferrer \cite{DIPorti-largeN}.
