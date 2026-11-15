---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-002-21-examples
section_title: "Examples."
section_number: 2.1
pages: 2-3
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.877
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
\begin{prop}[Proposition 2.4 of \cite{BB1}]
For $i\in[m]$, let $A_i$ be an $n$-by-$n$ matrix and let $x_i$ 
be an indeterminate, and let $B$ be an $n$-by-$n$ matrix. If $A_i$ is
positive semidefinite for all $i\in[m]$ and $B$ is Hermitian then
$$
f(\x) = \det(x_1 A_1 + x_2 A_2 + \cdots + x_m A_m + B)
$$
is real stable.
\end{prop}
\begin{proof}
Let $\overline{f}$ denote the coefficientwise complex conjugate of $f$.
Since $\overline{A_i}=A_i^\T$ for all $i\in[m]$, and $\overline{B}=B^\T$,
it follows that $\overline{f}=f$, so that $f\in\RR[\x]$.  By Hurwitz's Theorem
and a routine perturbation argument,
it suffices to prove that $f$ is stable when each $A_i$ is positive definite.  
Consider any $\z=\a+\i\b\in\HH^m$, with $\a,\b\in\RR^m$ and $b_i>0$ for all
$i\in[m]$ (abbreviated to $\b>\zero$).  Now $Q=\sum_{i=1}^m b_i A_i$ is
positive definite, and hence has a
positive definite square-root $Q^{1/2}$.  Also note that
$H=\sum_{i=1}^m a_i A_i + B$ is Hermitian, and that
$$
f(\z) = \det(Q)\det(\i I + Q^{-1/2}HQ^{-1/2}).
$$
Since $\det(Q)\neq 0$, if $f(\z)=0$ then $-\i$ is an eigenvalue of
$Q^{-1/2}HQ^{-1/2}$, contradicting the fact that this matrix is Hermitian.
Thus, $f(\z)\neq 0$ for all $\z\in\HH^m$.  That is, $f$ is stable.
\end{proof}

\begin{coro}
Let $Q$ be an $n$-by-$m$ complex matrix, and let
$X=\diag(x_1,...,x_m)$ be a diagonal matrix of indeterminates.
Then $f(\x)=\det(QXQ^\dagger)$ is real stable.
\end{coro}
\begin{proof}
Let $Q=(q_{ij})$, and for $j\in[m]$ let $A_j$ denote
the $n$-by-$n$ matrix with $hi$-th entry $q_{hj}\overline{q}_{ij}$.  That is,
$A_j=Q_j Q_j^\dagger$ in which $Q_j$ denotes the $j$-th column of $Q$.
Since each $A_j$ is positive semidefinite and
$QXQ^\dagger = x_1 A_1 + \cdots + x_m A_m$,
the conclusion follows directly from Proposition 2.1.
\end{proof}
