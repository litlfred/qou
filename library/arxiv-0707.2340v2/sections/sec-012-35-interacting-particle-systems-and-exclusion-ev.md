---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-012-35-interacting-particle-systems-and-exclusion-ev
section_title: "Interacting Particle Systems and Exclusion Evolutions"
section_number: 3.5
pages: 20-21
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.984
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{ss-ex-case}

The exclusion process is one of the main models considered in the area of
Probability Theory known as Interacting Particle Systems. The idea is 
that particles move in continuous time on a countable set $S$, in such a way 
that there is always at most one particle per site. The motion of
each particle would be a continuous time Markov chain on $S$, except that
transitions to occupied sites are forbidden. This process has been used to 
model many situations, including biopolymers and traffic flow. We refer to
\cite[Chap.~VIII]{L0} and \cite[Part 3]{L00} for detailed
treatments of this process. 

The (finite) {\em symmetric} exclusion process
generates a continuous time evolution on the set $\fP_n$. 
The limiting measure under the 
symmetric exclusion evolution with initial measure $\mu$ 
is the symmetrization $\mu_s$ of $\mu$ as defined in \S \ref{s21}. 
A problem that has attracted some attention is the following (see, e.g.,
\cite{L0,L2}).

\begin{problem}\label{p-see}
Find a natural negative dependence property that is preserved by symmetric 
exclusion evolutions.
\end{problem}

Since the limiting distribution of the evolution as $t\to\infty$ is the 
symmetrization
of the initial distribution defined in \eqref{sym}, any such property would  
have to be preserved by
this symmetrization procedure. In order for a solution to Problem~\ref{p-see}
to be useful in settling
Conjecture~\ref{con-lig}, the negative dependence property should be 
satisfied  by non-random/deterministic distributions and should
imply NA. Problem~\ref{p-see} is also
motivated by a theorem of Harris \cite[Theorem 2.14]{L0} that provides a 
general criterion for the preservation of positive dependence for Markov 
processes. Theorems 3.1 and 3.3 of \cite{L2} give negative dependence 
properties that are preserved by the symmetric exclusion evolution. However, 
one can make an argument that neither of these is ideal -- the first is too 
weak while 
the second is too strong. In \cite[Theorem 3.2]{L2} it was proved that NA is
not preserved by the symmetric exclusion 
process. The examples that we construct in \S \ref{s-countex}
further show that in fact none of the properties NLC, h-NLC, Rayleigh/h-NLC+, 
CNA, CNA+ defined in \S \ref{s21} is preserved by such evolutions. 
This is a consequence of the 
following criterion established by
Pemantle in \cite[Theorem 2.7]{P} (see also \cite[Proposition 3.6]{W}) for the 
ultra log-concavity of rank sequences of 
symmetric polynomials in $\PP_n$:

\begin{theorem}[\cite{P}]\label{pro-w}
For $0\le k\le n$ let $e_k(z_1,\ldots,z_n)$ be the $k$-th elementary symmetric 
function on $\{z_1,\ldots,z_n\}$ and consider the polynomial
$$f(z_1,\ldots,z_n)=\sum_{k=0}^{n}a_ke_k(z_1,\ldots,z_n),$$
where $a_k\ge 0$, $0\le k\le n$. The following are equivalent:
\begin{enumerate}
\item $f$ satisfies the conclusion of 
Conjecture~\ref{big}, that is, it has an ULC rank sequence 
(cf.~Definition~\ref{d-ulc});
\item $f$ has either (and then all) of the following five properties: NLC, 
h-NLC, Rayleigh/h-NLC+, CNA, CNA+.
\end{enumerate}
\end{theorem}

In \S \ref{n-s6} we show that the strongly Rayleigh 
property is preserved by (finite) symmetric exclusion evolutions  
and thus provide an answer to Problem~\ref{p-see}. 
We then prove that the distribution at time 
$t>0$ for the (not necessarily finite) symmetric exclusion process is 
CNA+ whenever the initial distribution is a product measure, which confirms 
Conjecture \ref{con-lig}.

Symmetric strongly Rayleigh measures are described in the following theorem. 
Recall that a (possibly infinite) matrix 
$A$ is said to be totally 
non-negative of order $p$ or $\text{TP}_p$ for short 
if for any $k\le p$ all its $k \times k$ minors are non-negative \cite{Kar}.
If $A$ has all non-negative minors then $A$ is called 
totally non-negative or $\TP$ for short. 

\begin{theorem}[Exchangeable Strongly Rayleigh Case]\label{ESC}
Suppose $\mu\in\PP_n$ has a symmetric generating polynomial and 
rank sequence $\{r_k\}_{k=0}^n$. The following are equivalent:
\begin{itemize}
\item[(a)] The generating polynomial of $\mu$ is stable, i.e., $\mu$ is
strongly Rayleigh; 
\item[(b)] All zeros of the univariate polynomial $\sum_{k=0}^{n}r_kz^k$
are real; 
\item[(c)] The infinite Toeplitz matrix $(r_{i-j})_{i,j=0}^{\infty}$ is $\TP$,
where $r_k=0$ if $k\notin \{0\}\cup [n]$. 
\end{itemize}
\end{theorem}

\begin{proof}
The equivalence (b) $\Leftrightarrow$ (c) is a classical result due to 
Aissen, Schoenberg and 
Whitney \cite{ASW}, while the equivalence (a) $\Leftrightarrow$ (b) is a 
consequence of the Grace-Walsh-Szeg\"o coincidence theorem 
(see Theorem~\ref{GWS} below). 
\end{proof}
