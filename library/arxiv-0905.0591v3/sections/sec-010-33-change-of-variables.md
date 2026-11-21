---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-010-33-change-of-variables
section_title: "Change of variables"
section_number: 3.3
pages: 8-9
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.982
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
In this section we will show how to reduce the number of variables in twisted Alexander polynomials, in particular
this discussion will show how to obtain one--variable twisted Alexander polynomials from multi--variable twisted Alexander polynomials.

Throughout this section let $N$ be a 3--manifold with empty or toroidal boundary, let
$\psi:\pi_1(N)\to F$ be a non--trivial homomorphism to a free abelian group $F$
and let $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ be a  representation.
Furthermore let $\phi:F\to H$ also be a homomorphism to a  free abelian group such that $\phi\circ \psi$ is non--trivial.
We denote the induced ring homomorphism $R[F]\to R[H]$ by $\phi$ as well.
Let
\[ S=\{ f \in R[F] \, |\, \phi(R[F])\ne 0 \in R[H]\}.\]
Note that $\phi$ induces a homomorphism $R[F]S^{-1}\to Q(R[H])$ which we also denote by $\phi$.

The following is  a slight generalization of \cite[Theorem~6.6]{FK08a}, which in turn builds on ideas of Turaev
(cf. \cite{Tu86} and \cite{Tu01}).

\begin{proposition}\label{prop:changevartau}
We have  $\tau(N,\gamma \otimes \psi)\in R[F]S^{-1}$, and
\[ \tau(N,\gamma\otimes \psi \circ \phi) \doteq \phi(\tau(N,\gamma \otimes \psi)).\]
\end{proposition}

The following is now an immediate corollary of the previous proposition and
Proposition \ref{prop:deltatau}.

\begin{corollary}\label{cor:changevardelta}
Assume that  $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ is a  representation with $R$ a Noetherian UFD.
If $\phi\left(\Delta_{N}^{\gamma\otimes \psi}\right)\ne 0$, then
we have the following equality:
\[ \prod_{i=0}^2 \left(\Delta^{\gamma \otimes \phi\circ \psi}_{N,i}\right)^{(-1)^{i+1}}\doteq
\phi \left(\prod_{i=0}^2 \big(\Delta^{\gamma\otimes \psi}_{N,i}\big)^{(-1)^{i+1}}\right).\]
In particular, if $\mbox{rank}\{\mbox{Im}\{\pi_1(N)\xrightarrow{\phi\circ \psi}H\}\}\geq 2$, then
\[  \Delta^{\gamma \otimes \phi\circ \phi}_{N} \doteq \phi\left(\Delta^{\gamma\otimes \psi}_{N}\right). \]
\end{corollary}
