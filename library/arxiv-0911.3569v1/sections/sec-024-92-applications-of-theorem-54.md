---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-024-92-applications-of-theorem-54
section_title: "Applications of Theorem 5.4."
section_number: 9.2
pages: 27-28
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.923
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
It is natural to consider a multivariate anaogue of the multiplier sequences
studied by P\'olya and Schur.  Let $\lambda:\NN^m\goesto\RR$, and define
a linear transformation $T_\lambda:\CC[\x]\goesto\CC[\x]$ by
$T_\lambda(\x^\alpha)= \lambda(\alpha)\x^\alpha$ for all $\alpha\in\NN^m$,
and linear extension.  For which $\lambda$ does $T_{\lambda}$
preserve real stability?  The answer:\  just the ones you get from
the P\'olya-Schur Theorem, and no more.

\begin{theorem}[Theorem 1.8 of \cite{BB4}.]
Let $\lambda:\NN^m\goesto\RR$.  Then $T_\lambda$ preserves real stability if
and only if there are univariate multiplier sequences $\lambda_i:\NN\goesto\RR$
for $i\in[m]$ and $\epsilon\in\{-1,+1\}$ such that
$$
\lambda(\alpha) = \lambda_1(\alpha(1))\cdots\lambda_m(\alpha(m))
$$
for all $\alpha\in\NN^m$, and either
$\epsilon^{|\alpha|}\lambda(\alpha)\geq 0$ for all $\alpha\in\NN^m$, or
$\epsilon^{|\alpha|}\lambda(\alpha)\leq 0$ for all $\alpha\in\NN^m$.
\end{theorem}

Theorem 5.4 (and similarly Propositions 9.1 and 9.2) can be used to derive
a wide variety of results of the form:\ such-and-such an operation
preserves stability (or Schur or Hurwitz stability).  Here is a short
account of Hinkkanen's proof of the Lee-Yang Circle Theorem, taken
from Section 8 of \cite{BB6}.

For $f,g\in\CC[\x]^\ma$, say $f=\sum_{S\subseteq[m]} a(S)\x^S$ and
$g=\sum_{S\subseteq[m]} b(S)\x^S$, let
$$
f\bullet g = \sum_{S\subseteq[m]} a(S)b(S) \x^S
$$
be the \emph{Schur-Hadamard product} of $f$ and $g$.

\begin{theorem}[Hinkkanen, Theorem 8.5 of \cite{BB6}]
If $f,g\in\CC[\x]^\ma$ are Schur stable then $f\bullet g$ is Schur
stable.
\end{theorem}
\begin{proof}
Let $T_g:\CC[\x]^\ma\goesto\CC[\x]^\ma$ be defined by $f\mapsto f\bullet g$.
By Proposition 9.1, to show that
$T_g$ preserves Schur stability it suffices to show that $T_g((\one+\x\y)^{[m]})$
is Schur stable.  Clearly $T_g((\one+\x\y)^{[m]}) = g(x_1 y_1,...,x_m y_m)$
is Schur stable since $g(\x)$ is.  Hence $T_g$ preserves Schur stability,
and so $f\bullet g$ is Schur stable.
\end{proof}

\begin{theorem}[Lee-Yang Circle Theorem, Theorem 8.4 of \cite{BB6}]
Let $A=(a_{ij})$ be a Hermitian $m$-by-$m$ matrix with $|a_{ij}|\leq 1$
for all $i,j\in[m]$.  Then the polynomial
$$
f(\x) = \sum_{S\subseteq[m]}\x^S \prod_{i\in S}\prod_{j\not\in S} a_{ij}
$$
is Schur stable.  The diagonalization $g(x)=f(x,...,x)$ is such that
$x^m g(1/x) = g(x)$, and it follows that all roots of
$g(x)$ are on the unit circle.
\end{theorem}
\begin{proof}
For $i<j$ in $[m]$ let
$$
f_{ij} = (1+a_{ij} x_i + \overline{a_{ij}} x_j + x_i x_j)
\prod_{h\in[m]\drop\{i,j\}} (1+x_h).
$$
One can check that each $f_{ij}$ is Schur stable.  The polynomial $f(\x)$
is the Schur-Hadamard product of all the
$f_{ij}$ for $\{i,j\}\subseteq[m]$.  By Theorem 9.4, $f(\x)$ is Schur stable.
\end{proof}

Section 8 of \cite{BB6} contains many many more results of this nature.
