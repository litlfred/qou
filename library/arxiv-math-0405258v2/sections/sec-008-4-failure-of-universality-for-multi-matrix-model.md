---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-008-4-failure-of-universality-for-multi-matrix-model
section_title: "Failure of Universality for multi-matrix models"
section_number: 4
pages: 27-30
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.98
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
In this section we want to make the meaning of second order freeness
for fluctuations of random matrices more explicit and relate this
with the question of universality of such fluctuations. There has
been much interest in global fluctuations of random matrices, in
particular, since it was observed that for large classes of
one-matrix models these fluctuations are universal. In the physical
literature this observation goes at least back to Politzer \cite{P},
culminating in the paper of Ambj\o{}rn et al. \cite{AJM}, whereas a
proof on the mathematical level of rigour is due to Johansson
\cite{J}. Universality for one-matrix models lets one expect
that one would also have such universality for multi-matrix
models. Indeed, this expectation was one of the starting points
of our investigations. However, our machinery around second order
freeness shows that such universality is {\it not}\/ present in
multi-matrix models.

Before we address multi-matrix models let us first recall the
relevant result of Johansson \cite{J}. We consider Hermitian
$N\times N$-random matrices $A=(a_{ij})_{i,j=1}^N$ equipped with the
probability measure
\begin{equation}\label{ensemble}
d\mu_N(A)=\frac 1{Z_N}\exp\bigl\{-N\Tr[P(A)]\bigr\}dA,
\end{equation}
where
$$dA=\prod_{1\leq i<j\leq N}d\,\text{Re}\, a_{ij}\, d\,\text{Im}\, a_{ij}
\prod_{i=1}^N da_{ii}.$$ Here, $P$ is a polynomial in one variable,
which we will address as ``potential" in the following, and $Z_N$ is
a normalization constant. If one restricts to a special class
$\mathcal{V}$ of potentials $P$ (the most important condition being
that the limit eigenvalue distribution has a single interval as
support -- which we normalize in the following to $[-2,2]$) then
Johansson proved the following universality of fluctuations for this
class: Consider the sequence of $N\times N$-random matrices
$\{A_N\}_N$ given by (\ref{ensemble}). Then this sequence has a
second order limit distribution which can be described as follows:
\begin{enumerate}
\item
We have
$$\lim_{N\to\infty}
\kk_1\{\tr[A^n_N]\}=\int t^nd\nu_P(t)\qquad (n\in\NN),$$ where
$\nu_P$ is a probability measure on $\RR$ (``limiting eigenvalue
distribution") which is given as the solution of the singular
integral equation
\begin{equation}\label{integral}
\int\frac{d\nu_P(t)}{t-s}=-\frac 12 P'(s)\qquad \text{for all
$s\in\text{supp } \nu_P$}.
\end{equation}
\item
Let $T_n$ ($n\in\NN$) be the Chebyshev polynomials of first kind
(which are the orthogonal polynomials with respect to the arcsine
law on $[-2,2]$). Then
$$\lim_{N\to\infty}
\kk_2\{\Tr[T_n(A_N)],\Tr[T_m(A_N)]\}=\delta_{mn}\cdot n.$$
\end{enumerate}
Whereas the limiting eigenvalue distribution $\nu_P$ depends on the
form of the potential $P$, the fluctuations are the same for all
potentials in the class $\mathcal{V}$ -- they are always
diagonalized by the same polynomials $\{T_n\mid n\in\NN\}$. Note
that the most prominent example for the considered class of random
matrices is given by $P(A)=A^2$, which corresponds to the Gaussian
random matrix ensemble. So one can phrase this universality also in
the way that all considered random matrices have the same
fluctuations as Gaussian random matrices (but their eigenvalue
distributions are of course different from Wigner's semi-circle
law).

Let us now consider multi-matrix models. For notational convenience
we restrict to the case of two-matrix models. Take now a polynomial
$P(A,B)$ in two non-commuting variables and consider pairs of
hermitian $N\times N$-matrices $A=(a_{ij})_{i,j=1}^N$ and
$B=(b_{ij})_{i,j=1}^N$ equipped with the probability measure
\begin{equation}\label{ensemble-two}
d\mu_N(A,B)=\frac 1{Z_N}\exp\{-N\Tr[P(A,B)]\}dA dB,
\end{equation}
where $Z_N$ is a normalization constant. The simplest ensemble of
this kind is the case of two independent Gaussian random matrices
which corresponds to the choice $P(A,B)=A^2+B^2$. The above
mentioned universality result for the one-matrix case lets one
expect that one might also have universality for multi-matrix
ensembles which are close to the ensemble of independent Gaussian
random matrices. However, we will now show that even restricted to
potentials of the form $P(A,B)= P_1(A)+P_2(B)$ we do not have
universal fluctuations.

Let us first observe that our concept of second order freeness tells
us how to diagonalize fluctuations. We spell this out in the
following theorem which is an easy consequence of Definition
\ref{free} of second order freeness.

\begin{theorem}\label{meaning}
Let $\{A_N\}_N$ and $\{B_N\}_N$ be two sequences of $N\times
N$-random matrices which are asymptotically free of second order.
Let $\{Q_n^A\mid n\in\NN\}$ and $\{Q_n^B\mid n\in\NN\}$ be the
orthogonal polynomials for the limiting eigenvalue distribution of
$A_N$ and $B_N$, respectively, determined by the requirements that
$Q_n^A$ and $Q_n^B$ are polynomials of degree $n$ and that
$$\lim_{N\to\infty}\kk_1\{\tr[Q_n^A(A_N)Q_m^A(A_N)]\}=\delta_{nm},$$
$$\lim_{N\to\infty}\kk_1\{\tr[Q_n^B(B_N)Q_m^B(B_N)]\}=\delta_{nm}.$$
Then the fluctuations of mixed traces in $A_N$ and $B_N$ are
diagonalized by cyclically alternating products of $Q_n^A$ and
$Q_n^B$ and the covariances are given by the number of cyclic
matchings of these products:
\begin{multline*}
\lim_{N\to\infty}
\kk_2\bigl\{\Tr[Q^A_{i(1)}(A_N)Q^B_{j(1)}(B_N)\cdots
Q^A_{i(m)}(A_N)Q^B_{j(m)}(B_N)],\\
\Tr[Q^B_{l(n)}(B_N) Q^A_{k(n)}(A_N) \cdots
Q^B_{l(1)}(B_N) Q^A_{k(1)}(A_N)]\bigr\}\\
=\delta_{mn} \cdot\#\{r\in\{1,\dots,n\}\!\mid\! i(s)=k(s+r),
j(s)=l(s+r)\,\forall s=1,\dots,n\}
\end{multline*}
\end{theorem}

To come back to our problem of universality for multi-matrix models
we only have to observe that Corollary \ref{cor:3.14} tells us that
we have asymptotic freeness of second order if we choose a potential
of the form $P(A,B)=P_1(A)+P_2(B)$.

\begin{theorem}
Let $P(A,B)=P_1(A)+P_2(B)$ where $P_1$ and $P_2$ are polynomials
from the class $\mathcal{V}$. Consider the two-matrix model
$\{A_N, \ab B_N \}_N$ given by the probability measure
(\ref{ensemble-two}). Let $\nu_1$ and $\nu_2$ be the limiting
eigenvalue distribution for $P_1$ and $P_2$, respectively (as
described in Eq. (\ref{integral})) and denote by $\{Q^1_n\mid
n\in\NN\}$ and $\{Q^2_n\mid n\in\NN\}$ the respective orthogonal
polynomials. Then the sequence $\{A_N,B_N\}_N$ has a second order
limit distribution given by $(\cA,\ff_1,\ff_2)$ and $a,b\in\cA$
which can be described as follows:
\begin{enumerate}
\item
$\ff_1$ is the free product of $\nu_1$ and $\nu_2$.
\item
$\ff_2$ is diagonalized by the following collection of polynomials:
$$\{T_n(a)\mid n\in\NN\}$$
$$\{T_n(b)\mid n\in\NN\}$$
$$\{Q^1_{i(1)}(a)Q^2_{j(1)}(b)\cdots
Q^1_{i(n)}(a)Q^2_{j(n)}(b) \},$$ 
where in the last set we choose one representative from each cyclic
equivalence class, i.e. for all $n\in\NN$,
$n$-tuples $\bigl((i(1),j(1)), \ab \dots , \ab
(i(n), \ab j(n))\bigr)$   which are
different modulo cyclic rotation
\end{enumerate}
\end{theorem}

\begin{proof}
Note that the additive form of the potential $P(A,B)=P_1(A)+P_2(B)$
means that $A_N$ and $B_N$ are independent, $A_N$ is a one-matrix
ensemble corresponding, via (\ref{ensemble}), to a potential $P_1$,
and $B_N$ is a one-matrix ensemble corresponding to a potential
$P_2$. Thus the statement about the diagonalizing polynomials in
either only $A_N$ or in only $B_N$ is just Johansson's result. For
getting the statement about the diagonalizing polynomials in both
$A_N$ and $B_N$ we have to note that the random matrices $A_N$ (and
also $B_N$) are $\UU(N)$-invariant, thus Corollary \ref{cor:3.14}
implies that $\{A_N\}_N$ and $\{B_N\}_N$ are asymptotically free of
second order. Hence we can apply Theorem \ref{meaning} 
above.\end{proof}

Note that whereas the polynomials in only one of the matrices are
universal (namely equal to the Chebyshev polynomials $\{T_n\}_n$), the
polynomials which involve both matrices are not universal but depend
on the eigenvalue distributions $\nu_1$ and $\nu_2$. Since the
latter vary with the potentials $P_1$ and $P_2$, the polynomials
$Q^1_n$ and $Q^2_n$, and thus also the alternating products in them,
depend on the choice of $P$. Thus we can conclude that even within
the very restricted class of $P$'s of the form
$P(A,B)=P_1(A)+P_2(B)$ we have no universality of global
fluctuations in multi-matrix models.
