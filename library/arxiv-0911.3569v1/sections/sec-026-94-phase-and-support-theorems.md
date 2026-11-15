---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-026-94-phase-and-support-theorems
section_title: "Phase and support theorems."
section_number: 9.4
pages: 29-29
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.987
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
A polynomial $f\in\CC[\x]$ has \emph{definite parity} if every monomial
$\x^\alpha$ occurring in $f$ has total degree of the same parity:\
all are even, or all are odd.

\begin{theorem}[Theorem 6.2 of \cite{COSW}]
Let $f\in\CC[\x]$ be Hurwitz stable and with definite parity.  Then
there is a phase $0\leq \theta < 2\pi$ such that $\mathrm{e}^{-\i\theta}f(\x)$
has only real nonnegative coefficients.
\end{theorem}

The \emph{support} of $f=\sum_{\alpha}c(\alpha)\x^{\alpha}$ is
$\supp(f) = \{\alpha\in\NN^{m}:\ c(\alpha)\neq 0\}$.
Let $\delta_i$ denote the unit vector with a one in the $i$-th coordinate,
and for $\alpha\in\ZZ^{n}$ let $|\alpha|=\sum_{i=1}^m |\alpha(i)|$.
A \emph{jump system} is a subset $\J\subseteq\ZZ^m$ satisfying the following
\emph{two-step axiom}:\\
\textbf{(J)}\  If $\alpha,\beta\in\J$ and $i\in[m]$ and
$\epsilon\in\{-1,+1\}$ are such that $\alpha'=\alpha+\epsilon\delta_i$
satisfies $|\alpha'-\beta|<|\alpha-\beta|$, then either $\alpha'\in\J$
or there exists $j\in[m]$ and $\varepsilon\in\{-1,+1\}$ such that
$\alpha''=\alpha'+\varepsilon\delta_j\in\J$ and
$|\alpha''-\beta|<|\alpha'-\beta|$.

Jump systems generalize some more familiar combinatorial objects.
A jump system contained in $\{0,1\}^{m}$ is a \emph{delta-matroid}.
A delta-matroid $\J$ for which $|\alpha|$ is constant for all $\alpha\in\J$
is the set of bases of a \emph{matroid}.  For bases of matroids, the
two-step axiom (J) reduces to the basis exchange axiom familiar from linear 
algebra:\ if $A,B\in\J$ and $a\in A\drop B$, then there exists $b\in 
B\drop A$ such that $(A\drop\{a\})\cup\{b\}$ is in $\J$.

\begin{theorem}[Theorem 3.2 of \cite{B}]
If $f\in\Stab[\x]$ is stable then the support $\supp(f)$ is a jump system.
\end{theorem}

Recall from Section 7 that for multiaffine polynomials with nonnegative
coefficients, real stability implies the Rayleigh property.
A set system $\J$ is \emph{convex} when $A,B\in\J$ and $A\subseteq B$ imply 
that $C\in\J$ for all $A\subseteq C\subseteq B$.
\begin{theorem}[Section 4 of \cite{W}]
Let $f=\sum_{S\subseteq[m]} c(S) \x^S$ be multiaffine with real nonnegative
coefficients, and assume that $f$ is Rayleigh.\\
\textup{(a)}\ The support $\supp(f)$ is a convex delta-matroid.\\
\textup{(b)}\ The coefficients are \emph{log-submodular}:\ for all
$A,B\subseteq[m]$,
$$
c(A\cap B) c(A\cup B) \leq c(A) c(B).
$$
\end{theorem}




\bibliographystyle{amsplain}
