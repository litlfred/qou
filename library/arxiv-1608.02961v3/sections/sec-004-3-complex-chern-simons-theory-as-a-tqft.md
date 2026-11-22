---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-004-3-complex-chern-simons-theory-as-a-tqft
section_title: "Complex Chern-Simons theory as a TQFT?"
section_number: 3
pages: 10-12
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 1.0
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:TQFT}

Now, having seen very explicitly that complex Chern-Simons Hilbert spaces are infinite-dimensional (and exactly how they're infinite-dimensional), let us think a bit about the properties of partition functions.

For a closed three-manifold $M$, it is expected that the complex Chern-Simons partition function takes the form

\DIbe \CalZ[M]_{k,s} = \sum_{\text{flat $\alpha$}} \frac{1}{|\text{Stab}(\alpha)|} \CalB_\alpha(q^{\frac12})\widetilde\CalB_\alpha(\tilde q^{\frac12}) \,. \label{DI.fact} \DIee

The sum here is over flat complex connections $\alpha$ on $M$, which are the critical points of the Chern-Simons path integral; and $\CalB_\alpha$, $\widetilde\CalB_\alpha$ are holomorphic and antiholomorphic contributions to the path integral from quantum fluctuations around the critical point, with $q,\tilde q$ defined by \eqref{DI.qq}. The prefactor $|\text{Stab}(\alpha)|$ is the volume of the stabilizer of $\alpha$, \DIie\ the volume of the subgroup of the gauge group that preserves a particular flat connection.


One certainly expects such a formula to be valid perturbatively, due to standard properties of path integrals in quantum field theory. (The perturbative version of \eqref{DI.fact} formed the basis for the physical explanation of the Volume Conjecture in \cite{DIgukov-2003}.) It was argued in \cite{DIWit-anal}, however, that the formula is actually valid non-perturbatively as well. Roughly, one should think of \eqref{DI.fact} as expanding the integration cycle in the Chern-Simons path integral into a sum of integration cycles $\Gamma_\alpha$ defined by gradient flow off of each critical point with respect to the Chern-Simons action. The $\Gamma_\alpha$ can further be written as products

\footnote{In general, there could be a nontrivial matrix $n_{\alpha\beta}$ connecting holomorphic and anti-holomorphic sectors. However, when one considers unitary Chern-Simons theory with an integration contour $\Gamma$ along which $\ol\CalA$ is honestly the conjugate of $\CalA$, the matrix is just the identity.} 

of cycles $\gamma_\alpha\times \widetilde\gamma_\alpha$ in the space of (holomorphic)$\times$(anti-holomorphic) connections, leading to the factorization $\CalB_\alpha(q^{\frac12})\widetilde\CalB_\alpha(\tilde q^{\frac12})$.\,

\footnote{The 3d-3d correspondence relates holomorphic-antiholomorphic factorization in complex Chern-Simons theory to a rather nontrivial statement about lens-space partition functions of 3d $\CalN=2$ theories $T[M]$~\cite{DIBDP-blocks}.}

For a three-manifold with boundary $\Sigma$, the same type of formula holds after properly accounting for boundary conditions. In particular, the sum is over flat connections with a fixed behavior at $\Sigma$, and each summand becomes a wavefunction  in $\CalH[\Sigma]_{k,s}$. For example if $\Sigma=T^2$ is a torus, we would fix A-cycle holonomy eigenvalues $x,\bar x$ of a flat connection as in Section \ref{DI.sec:quant}, and the individual wavefunctions would have the factorized form $\CalB_\alpha(x,q^{\frac12})\widetilde\CalB_\alpha(\bar x,\tilde q^{\frac12})$.

What can we learn from \eqref{DI.fact}? In the best-case scenario, there is a finite number of flat connections on $M$, and all the flat connections have finite-volume stabilizers. This would lead to a finite, well-defined (in principle) $\CalZ[M]_{k,s}$. In contrast:

\begin{itemize}
\item If a flat connection $\alpha$ is isolated but its stabilizer has infinite volume, its contribution to \eqref{DI.fact} vanishes.
\item If flat connections come in a continuous family on which the Chern-Simons action is constant, then the contribution to \eqref{DI.fact} can be infinite.
\end{itemize}

Unfortunately, the best-case scenario never holds, and both of these potentially bad situations can arise. We consider some examples.

If $M$ is hyperbolic (meaning that it admits a hyperbolic metric), it is expected that there are a finite number of $SL(2,\BC)$ flat connections on $M$.
Intuitively, for hyperbolic $M$ the fundamental group $\pi_1(M)$ is sufficiently complicated that the representations $\pi_1(M)\to SL(2,\BC)$ are isolated.

\footnote{On hyperbolic $M$, one particular flat $SL(2,\BC)$ connection --- the one corresponding to the global hyperbolic metric --- is well known to be isolated \cite{DImostow-1973, DIthurston-1980}. Computational experiments suggest that in fact all flat connections $SL(2,\BC)$ are isolated, but there exists no general proof of this statement.} 

Then the partition function is finite. As we discuss in Section \ref{DI.sec:angle}, the partition function can actually be computed.
However, there is always at least one flat connection $\alpha_{\rm abel}$ whose holonomies belong to the maximal torus $GL(1,\BC)\subset SL(2,\BC)$. The stabilizer of $\alpha_{\rm abel}$ contains constant $GL(1,\BC)$-valued gauge transformations; since $GL(1,\BC)$ has infinite volume, $\alpha_{\rm abel}$ does not contribute at all to the partition function. This becomes hugely problematic when trying to formulate complex Chern-Simons as a TQFT, as all flat connections must be accounted for during cutting and gluing \cite{DICDGS}.

There are some simple manifolds whose fundamental group $\pi_1(M)$ is abelian. For example, if $M$ is a lens space $L(p,r)\simeq S^3/\BZ_p$, the fundamental group is $\BZ_p$. In this case, every single flat connection has holonomy in the maximal torus of the gauge group, the volume of the stabilizer is always infinite, and $\CalZ[M]$ vanishes identically.

In the opposite extreme are manifolds $M$ on which the flat connections are not isolated. In this case, we expect that $\CalZ[M]$ diverges.
For example, consider $M=\Sigma\times S^1$. Then  $\CalM_{\rm flat}(G_\BC,M) = \CalM_{\rm flat}(G_\BC,\Sigma)\times T_\BC$ (where $T_\BC$ is the maximal torus of $G_\BC$). The partition function is

\DIbe \CalZ[M]_{k,s} = \text{Tr}_{\CalH[M]_{k,s}} 1\hspace{-.15cm}1 = \text{dim}\,\CalH[M]_{k,s} = \infty\,. \label{DI.tr} \DIee


Both the zeroes and infinities appearing here obstruct the definition of consistent cutting and gluing rules needed to make Chern-Simons theory a TQFT. The zeroes and infinities have to be regularized. While no systematic approach to regularization has been formulated so far, there are exist several promising and exciting proposals. Almost all of them are motivated by string/M-theory and the 3d-3d correspondence.
