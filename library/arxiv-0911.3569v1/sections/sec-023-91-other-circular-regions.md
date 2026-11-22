---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-023-91-other-circular-regions
section_title: "Other circular regions."
section_number: 9.1
pages: 27-27
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.98
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Let $\Omega\subseteq\CC^m$.  A polynomial $f\in\CC[\x]$ is
\emph{$\Omega$-stable} if either $f\equiv 0$ identically, or
$f(\z)\neq 0$ for all $\z\in\Omega$.  At this level of generality little
can be said.  If $\Omega=\A_1\times\cdots\times\A_m$ is a product of
open circular regions then there are M\"obius transformations
$z\mapsto \phi_i(z)=(a_i z+b_i)/(c_i z+d_i)$ such that $\phi_i(\HH)=\A_i$
for all $i\in[m]$.  The argument in Section 4.1 shows that
$f\in\CC[\x]$ is $\Omega$-stable if and only if
$$
\widetilde{f}=(\c\z+\mathbf{d})^{\deg f}\cdot f(\phi_1(z_1),...,\phi_m(z_m))
$$
is stable.  In this way results about stable polynomials can be translated
into results about $\Omega$-stable polynomials for any $\Omega$ that is
a product of open circular regions.

Theorem 6.3 of \cite{BB5} is the $\Omega$-stability analogue of Theorem 5.2.
We mention only two consequences of this.  Let $\D=\{z\in\CC:\ |z|<1\}$ be the
open unit disc, and for $\theta\in\RR$ let $\HH_\theta=\{\e^{-\i\theta}z:\
z\in\HH\}$.  Thus $\HH_0=\HH$, and $\HH_{\pi/2}$ is the open right half-plane.
A $\D^m$-stable polynomial is called \emph{Schur stable}, and a
$\HH_{\pi/2}^m$-stable polynomial is called \emph{Hurwitz stable}.

\begin{prop}[Remark 6.1 of \cite{BB5}.]
Fix $\kappa\in\NN^m$, and let $T:\CC[\x]^{\leq\kappa}\goesto\CC[\x]$
be a linear transformation.  The following are equivalent:\\
\textup{(a)}\ $T$ preserves Schur stability.\\
\textup{(b)}\ $T((\one+\x\y)^\kappa)$ is Schur stable in $\CC[\x,\y]$.
\end{prop}

\begin{prop}[Remark 6.1 of \cite{BB5}.]
Fix $\kappa\in\NN^m$, and let $T:\CC[\x]^{\leq\kappa}\goesto\CC[\x]$
be a linear transformation.  The following are equivalent:\\
\textup{(a)}\ $T$ preserves Hurwitz stability.\\
\textup{(b)}\ $T((\one+\x\y)^\kappa)$ is Hurwitz stable in $\CC[\x,\y]$.
\end{prop}
