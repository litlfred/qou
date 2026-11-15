---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-003-22-strongly-rayleigh-measures
section_title: "Strongly Rayleigh Measures"
section_number: 2.2
pages: 9-10
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.971
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s23}
Motivated by similar notions in the theory of multivariate entire functions
studied by Levin \cite{Le}, the following definition was made in
\cite{BBS,BBS1,BBS2} (see also \cite{BB,BB-2}).

\begin{definition}\label{d-rs-pol}
A polynomial $f \in \CC[z_1,\ldots, z_n]$ is called {\em stable} if 
$f(z_1,\ldots, z_n) \neq 0$ 
whenever $\Im(z_j) >0$ for $1\le j\le n$. A stable polynomial with all
real coefficients is called {\em real stable}.
\end{definition}

Multivariate stable polynomials are intimately connected with other fundamental
objects such as hyperbolic polynomials, Lee-Yang polynomials and 
polynomials with the half-plane property. Polynomials of the aforementioned 
types are widely encountered in both mathematics and physics
\cite{ABG,BBCV,BBS,BBS1,BBS2,BB,PB,COSW,guler,garding,LS} (see also 
\S \ref{s-gar}). 

Let us define a class of measures induced by stable polynomials.

\begin{definition}\label{def-rsm}
A measure $\mu\in\fP_n$ is called {\em strongly Rayleigh} if its generating 
polynomial $g_\mu\in\PP_n$ is (real) stable. For convenience, we will  
sometimes refer to a real stable polynomial $f\in\PP_n$ as a 
{\em strongly Rayleigh polynomial}.
\end{definition}

\begin{remark}\label{r-term}
As we explain in \S \ref{ss-real-s} and \S \ref{s-stable}, a strongly 
Rayleigh measure is necessarily
Rayleigh. The terminology adopted is 
motivated by the 
fact that the equivalent condition for real stability for multi-affine 
polynomials in
Theorem~\ref{stable-Rayleigh} is a natural strengthening of the definition 
of a 
Rayleigh polynomial/measure (Definition~\ref{d1}). The term is taken 
from \cite{CW}, where a 
matroid was defined to be strongly Rayleigh if \eqref{stable} holds for
 its bases-generating polynomial. However, it was not known 
then that condition \eqref{stable} is equivalent to stability. 
\end{remark}

A simple albeit important example of strongly Rayleigh measure is the
following.

\begin{definition}\label{d-prod-m}
A {\em product measure} on $2^{[n]}$
is a measure $\mu\in\fP_n$ with generating polynomial $g_\mu$ of the form
$$g_\mu(z_1,\ldots,z_n)
=\prod_{i=1}^{n}(q_iz_i+1-q_i),\quad 0\leq q_i\leq 1,\,i\in [n].$$
One says that $\mu$ is
{\em deterministic} or {\em non-random} if it is a point mass
on $2^{[n]}$, i.e., if there exists $S\subseteq [n]$ such that
$q_i=1$ if $i\in S$ and $q_j=0$ for  
$j\in [n]\setminus S$.
\end{definition}

In \S \ref{s3-ex} we show that the class of strongly Rayleigh measures 
contains numerous other 
important examples of measures appearing in matrix theory,
combinatorics, probability theory, particle systems, 
and in \S \ref{s-stable} we study this class in detail.
