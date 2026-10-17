---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents"
section_id: sec-005-31-symmetries-regularizations-and-the-3d-3d-corr
section_title: "Symmetries, regularizations, and the 3d-3d correspondence"
section_number: 3.1
pages: 12-13
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.919
latex_coverage_ratio: 0.996
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Contents — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
\label{DI.sec:sym}

In principle, the 3d-3d correspondence itself may suffice to resolve the difficulties with cutting and gluing in complex Chern-Simons theory.

\footnote{We will not review the 3d-3d correspondence here. For recent reviews and discussions, especially in the context of Chern-Simons theory and TQFT, see \cite{DID-volume, DICDGS, DIGukovPei, DIPeiKe} as well as the related \cite{DIYamazaki-defects}.} 

The correspondence assigns to a closed 3-manifold $M$ and a Lie algebra $\mathfrak g$ of type $ADE$ (and a bit of extra discrete data) a three-dimensional field theory $T_G[M]$ with the property that that

\DIbe \begin{array}{l} \text{partition function of $T_G[M]$ on squashed lens space $L(k,1)_b$} \\[.1cm]
\qquad =\text{$G_\BC$ Chern-Simons partition function $\CalZ[M]_{k,s}$ with $is=k\frac{1-b^2}{1+b^2}$.}
\end{array}\DIee

where $\mathfrak g=\text{Lie}(G)$.
When $G_\BC=SL(N,\BC)$, the theory $T_{G_\BC}[M]$ is the effective low-energy worldvolume theory of $N$ M5 branes compactified on $M$; the branes wrap $M\times \BR^3$ in the M-theory geometry $T^*M\times \BR^5$.
Similarly, the correspondence assigns to a three-manifold $M$ with boundary $\Sigma$ a boundary condition $T_G[M]$ for the four-dimensional theory $T_G[\Sigma]$ of class $\CalS$ \cite{DIGaiotto-dualities, DIGMN}.


Typically $T_G[M]$ is an $\CalN=2$ superconformal theory, though both supersymmetry and conformal invariance might be broken. Unfortunately, it is not completely understood what conditions on $M$ guarantee $\CalN=2$ superconformal theories. We assume for the present heuristic argument that we do have $\CalN=2$ superconformal theories.

The basic idea, then, would be to replace $G_\BC$ Chern-Simons theory on $M$ with $T_{G_\BC}[M]$, which is a much more powerful object. Even when the Chern-Simons partition functions $\CalZ[M]_{k,s}$ (equivalently, lens-space partition functions of $T_G[M]$) are ill-defined, the theory $T_G[M]$ itself should still make sense. Moreover, the theories $T_G[M]$ obey cutting and gluing rules. Gluing $M=N_1\cup_\Sigma N_2$ corresponds to ``sandwiching'' the four-dimensional theory $T_G[\Sigma]$ between boundary conditions $T_G[N_1]$ and $T_G[N_2]$, and colliding  the boundaries together to produce a new effective theory $T_G[N_1\cup_\Sigma N_2]$. In this way, we reproduce the structure of a three-dimensional TQFT. If we should ever want to recover Chern-Simons partition functions, we just place the superconformal theories on a lens space $L(k,1)_b$.

There are two practical difficulties with this proposal that will hopefully be overcome soon. First, the full theories $T_G[M]$ are not actually known for most manifolds, for any nonabelian $G$. A construction using ideal triangulations was outlined in \cite{DIDGG, DIDGG-Kdec} (also \cite{DICCV, DICordova-tangles}); however, that construction produces subsectors of the full theories $T_G[M]$ that are missing some branches of vacua, the same way partition functions of Chern-Simons theory on hyperbolic manifolds are ``missing'' abelian flat connections. Examples of complete theories $T_G[M]$ for a handful of manifolds (including a hyperbolic one) were postulated in \cite{DICDGS}, and theories for lens spaces $M=L(p,r)$ were studied in \cite{DICDGS, DIGukovPei, DIPeiKe}.

The second difficulty, or potential shortcoming, is that zeroes and infinities still remain in the actual Chern-Simons partition functions. Here, however, another solution presents itself: the theories $T_G[M]$ often have extra symmetries; and parameters associated to these symmetries (twisted masses or fugacities) can be used to refine the squashed-lens-space $L(k,1)_b$ partition functions of $T_G[M]$ --- thus literally regularizing the Chern-Simons zeroes and infinities.

We already met one such symmetry in Section \ref{DI.sec:equiv}: the $U(1)_t$ that gave an equivariant quantization of the Hilbert space $\CalH[\Sigma]_{k,s=0}$. Via the 3d-3d correspondence, this Hilbert space is mapped to the BPS Hilbert space of the 4d class-$\CalS$ theory $T_G[\Sigma]$ on $\BR\times L(k,1)_{b=1}$. This 4d theory has an additional R-symmetry $U(1)_t$ that commutes with the supercharge used to define the ``BPS'' Hilbert space, and provides the $U(1)_t$ grading.

Similarly, the three-dimensional theory $T_G[\Sigma\times S^1]$ (obtained by compactifying $T_G[\Sigma]$ on a circle) has $\CalN=4$ rather than $\CalN=2$ supersymmetry. The larger R-symmetry group of the $\CalN=4$ theory contains $U(1)_t$, and including its twisted mass in partition functions leads to finite answers that encapsulate the graded dimension \eqref{DI.grdim}.

Theories $T_G[M]$ for Seifert-fibered three-manifolds $M$ should also retain this $U(1)_t$ symmetry. In this case, it can ultimately be traced back to an exceptional isometry

\footnote{This very same symmetry played a central role in defining refined (compact) Chern-Simons theory on Seifert-fibered manifolds \cite{DIAS-refinedCS}.} 

 of the $M$-theory geometry $T^*M\times \BR^5$. An simple example of such a manifold is a lens space $M=L(p,r)$, whose refined partition functions were analyzed in \cite{DIPeiKe}, and put precisely into the factorized form \eqref{DI.fact} --- with the factors $1/|\text{Stab}(\alpha)| = 1/\infty$ now regularized.

When $M$ is generic (\DIeg\ hyperbolic) this exceptional $U(1)_t$ symmetry is, unfortunately, absent. It was nevertheless proposed in \cite{DICDGS} that there exists yet \emph{another} symmetry $U(1)_{t'}$ in any theory $T_G[M]$, related to the standard $U(1)$ R-symmetry of three-dimensional $\CalN=2$ theories --- as well as to categorification of colored knot polynomials. This $U(1)_{t'}$ was used to regularize Chern-Simons partition functions for the trefoil and figure-eight knot complements (Seifert-fibered and hyperbolic manifolds, respectively), producing sums of the form \eqref{DI.fact} that included all flat connections, even abelian ones.
