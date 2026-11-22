---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-008-31-real-stable-polynomials-and-transcendental-en
section_title: "Real Stable Polynomials and Transcendental Entire Functions"
section_number: 3.1
pages: 13-15
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.98
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-real-s}

In \cite{PB} it was proved that a multi-affine polynomial 
$f \in \RR[z_1,\ldots,z_n]$ is stable (in the sense of 
Definition~\ref{d-rs-pol}) 
if and only if 
\begin{equation}\label{stable}
\frac {\partial f} {\partial z_i}(x) \frac {\partial f} {\partial z_j}(x)
\geq \frac {\partial^2 f} {\partial z_i \partial z_j}(x) f(x)
\end{equation}
for all $x \in \RR^n$ and $1\leq i<j \leq n$ (see also 
Theorem~\ref{stable-Rayleigh} in \S \ref{s-stable} below). Therefore, 
a stable multi-affine polynomial with non-negative coefficients is 
Rayleigh/h-NLC+. As we will prove in \S \ref{s-stable}, such polynomials are 
in fact CNA+.

Clearly, by setting all variables equal in a stable polynomial one gets a 
univariate stable polynomial. Hence, if $f(z_1,\ldots,z_n)$ is stable then 
so is its diagonal specialization (see Definition~\ref{d-ulc})
$$
\De(f)(t)=\sum_{k=0}^n \binom n k c_k t^k.
$$
A univariate polynomial with real coefficients is stable if and only if it 
has all real zeros, so the familiar Newton inequalities 
(cf., e.g., \cite{CC,HLP}) imply that $f$ satisfies the conclusion of 
Conjecture~\ref{big} if $f$ is stable with non-negative coefficients. 

Multivariate generalizations of Newton's inequalities for homogeneous real
stable polynomials with non-negative coefficients were
obtained in \cite[Theorem 3]{BBS1}. Corollaries 2 and 3 of 
{\em op.~cit.~}show that the coefficients of (symmetric) such polynomials 
also satisfy unimodality properties in the sense of majorization/stochastic
domination \cite{MO}. In \S \ref{ss-trunc} we establish natural analogs
of these results for truncations of (non-homogeneous) multi-affine 
stable polynomials with non-negative coefficients.

The well-known Laguerre-Tur\'an inequalities for univariate polynomials and 
transcendental entire functions in the Laguerre-P\'olya class \cite{CC}
amount to saying that the sequence of Taylor coefficients of such a function
is SLC (Definition~\ref{d-ulc}). 
One can argue that both Newton's inequalities and the 
Laguerre-Tur\'an inequalities are 
natural manifestations of negative dependence properties encoded in 
the {\em geometry} of the zero sets of these functions. Indeed, as we will 
see in \S \ref{s-stable}, the geometric features of real stability 
(Definition~\ref{d-rs-pol}) are a key tool in our study of negative 
dependence properties for strongly Rayleigh measures and allow us to
establish many such properties for this class of measures, including:
\begin{itemize}
\item the strongest form of negative association (CNA+);
\item closure under operations (i)--(vi) defined in \S \ref{s21};
\item closure under symmetric homogenization;
\item stochastic domination properties for truncations;
\item the ULC property for rank sequences.
\end{itemize}

Rayleigh polynomials that are not stable do not seem 
to have a geometric description by means of their zero sets similar to that
of stable polynomials. 
This may explain why several negative dependence properties fail for 
arbitrary (non-strongly) Rayleigh
polynomials/measures (see \S \ref{s-countex}).

We summarize below some of the closure properties of real stable 
polynomials (see \cite{BBS1,BBS2} for their proofs) that we need
for later use.

\begin{proposition}\label{pro-rs}
Let $\HH_n(\RR)$ be the set of all real stable polynomials in $n$
variables. 
\begin{enumerate}
\item $f\in \HH_n(\RR)$ if and only if for any $\lambda\in\RR_+^n$ and 
$\mu\in\RR^n$ the univariate polynomial $t\mapsto f(\lambda t+\mu)$ has all 
real zeros;
\item  If $f\in\HH_n(\RR)$ has degree $d_j$ in variable $z_j$, $j\in [n]$,
then
\begin{itemize}
\item $\partial_j f \in \HH_n(\RR)\cup\{0\}$ for 
$1 \leq j \leq n$;
\item $f(z_1, \ldots, z_{j-1}, \alpha z_j, z_{j+1}, \ldots, z_n) 
\in \HH_{n}(\RR)$ for $j \in [n]$, $\alpha > 0$;
\item $f(z_1, \ldots, z_{j-1},\beta, z_{j+1}, \ldots, z_n) 
\in \HH_{n-1}(\RR)\cup\{0\}$ for $j \in [n]$, $\beta\in \RR$;
\item $z_1^{d_1}\cdots z_n^{d_n}
f(\lambda_1 z_1^{-1},\ldots,\lambda_n z_n^{-1})\in\HH_n(\RR)$ if 
$\pm (\lambda_1,\ldots,\lambda_n)\in\RR_+^n$;
\item $f(z_1,\ldots, z_{i-1}, z_j, z_{i+1}, \ldots, z_n) \in \HH_{n-1}(\RR)$ 
for 
$i\neq j \in [n]$.
\end{itemize}
\item If $\{f_j\}_{j=1}^\infty \subset \HH_n(\RR)$ and 
$f \in \RR[z_1,\ldots, z_n]\setminus \{0\}$ is the limit, uniformly on 
compact subsets of $\CC^n$, of the sequence $\{f_j\}_{j=1}^\infty$ then 
$f \in \HH_n(\RR)$. 
\end{enumerate}
\end{proposition}

Important examples of real stable 
polynomials are given by the following construction 
(see, e.g., \cite{BBS1,BBS2}).

\begin{proposition}\label{det-pen}
Let $A_1,\ldots, A_m$ be (complex) positive semi-definite matrices and let $B$
be a (complex) Hermitian matrix, all matrices being of the same size.
\begin{enumerate} 
\item The polynomial 
\begin{equation}\label{pencil}
z=(z_1,\ldots,z_n)\mapsto f(z)= \det(z_1A_1+\cdots +z_mA_m+B) 
\end{equation}
is either identically zero or real stable; 
\item If $B$ is also 
positive semi-definite then $f$ has all non-negative coefficients.
\end{enumerate}
In particular, if $Z=\text{{\em diag}}(z_1,\ldots,z_m)$ and $A$ is a positive 
semi-definite $m\times m$ matrix 
then $\det(A+Z)$ is a multi-affine real 
stable polynomial with all non-negative coefficients, hence a (positive)
constant multiple of a strongly 
Rayleigh polynomial (cf.~Definition~\ref{def-rsm}). 
\end{proposition}

\begin{proof}
By the second part of Proposition~\ref{pro-rs} and a density argument,  
it suffices to prove (1) 
in the case when  all matrices $A_j$, $1\le j\le m$, are 
positive definite. Set $z(t)=\lambda t+ \mu$ with
$\lambda=(\lambda_1,\ldots,\lambda_n)\in \RR_+^n$,
$\mu=(\mu_1,\ldots,\mu_n)\in \RR^n$, and $t\in \CC$. Note that 
$P:=\sum_{j=1}^m\lambda_jA_j$
is positive definite and thus it is invertible and has a square root $Q$ (recall
that $\RR_+=(0,\infty)$). 
Then 
\begin{equation*}
f(z(t))=\det(P)\det(tI+QHQ^*),
\end{equation*}
where $H:=B+\sum_{j=1}^m\mu_jA_j$ is a Hermitian matrix. 
Therefore, $f(z(t))$ is a polynomial in $t$ that is a 
constant multiple of the characteristic polynomial of a
Hermitian matrix and so it must have all real zeros. By 
the first part of Proposition~\ref{pro-rs}, this proves (1), and then (2)
follows by noticing that the coefficients of the polynomial in \eqref{pencil}
are products of non-negative numbers, namely principal minors of the 
positive semi-definite matrices $A_1,\ldots,A_m,B$.
\end{proof}

Further properties of (not necessarily multi-affine) real stable 
polynomials, their linear
preservers and applications to entire function theory in one or several 
variables, matrix theory, combinatorics, convex optimization and statistical 
mechanics may be found in \cite{BBS,BBS1,BBS2,PB,COSW,guler,LS}.
