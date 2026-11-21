---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-002-21-hyperbolicity-and-stability-preservers
section_title: "Hyperbolicity and Stability Preservers"
section_number: 2.1
pages: 3-7
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.986
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{ss21}

To formulate the complete answers to Problems~\ref{pb1}--\ref{pb2} for $\RR$ 
and 
the half-plane $\{z \in \CC: \Im(z) \leq 0\}$  we need to introduce some 
notation.
As in \cite{BBS} -- and following the commonly used terminology in 
e.g.~the theory of partial differential equations \cite{ABG} -- we call a 
non-zero univariate polynomial with real 
coefficients {\em hyperbolic} if all its zeros are real. Such a polynomial
is said to be {\em strictly hyperbolic} if in addition 
all its zeros are distinct. 
A univariate polynomial 
$f(z)$ with complex coefficients is called {\em stable} if 
$f(z) \neq 0$ for all $z \in \CC$ with $\Im(z) >0$ and it is called 
{\em strictly stable} if 
$f(z) \neq 0$ for all $z \in \CC$ with $\Im(z) \geq 0$.  Hence a univariate 
polynomial with real coefficients is stable if and only if it is hyperbolic. 
These classical concepts have several natural extensions to multivariate 
polynomials, the most general notion being as follows.

\begin{definition}\label{def1}
A polynomial $f(z_1, \ldots, z_n)\in\bC[z_1,\ldots,z_n]$ is 
{\em stable} 
if  $f(z_1, \ldots, z_n) \neq 0$ for all $n$-tuples 
$(z_1, \ldots, z_n) \in \CC^n$ with $\Im(z_j) >0$, $1\le j\le n$.  
If in addition $f$ has real coefficients it will be referred  to as 
{\em real stable}. The 
sets of stable and real stable polynomials in $n$ variables are denoted 
by $\HH_n(\CC)$
 and 
$\HH_n(\RR)$, respectively. 
\end{definition}

Note that $f$ is stable (respectively, real stable) if and only if for all 
$\alpha \in \RR^n$ and $v \in \RR_+^n$ the 
univariate polynomial $f(\alpha + vt)\in\bC[t]$ is stable 
(respectively, hyperbolic). The connection between real stability and 
(G\aa rding) hyperbolicity
for multivariate homogeneous polynomials is explained in 
e.g.~\cite[Proposition 1]{BBS}.

\begin{notation}\label{not-cplx}
Henceforth it is understood that if $T$ is a linear operator on
some (real) linear subspace $V\subseteq \bR[z_1,\ldots,z_n]$ then $T$ extends 
in an obvious fashion to a linear operator -- denoted again by $T$ -- on the 
complexification $V\oplus iV$ of $V$.
\end{notation}

\begin{definition}\label{def2}
A linear operator $T$ defined on a linear subspace $V$ of 
$\bC[z_1,\ldots,z_n]$ (respectively,
$\bR[z_1,\ldots,z_n]$) is called {\em stability preserving} 
(respectively, {\em real stability preserving}) on a given subset 
$M\subseteq V$ if
$$T(\HH_n(\CC)\cap M)\subseteq \HH_n(\CC)\cup\{0\}\text{ (respectively,
$T(\HH_n(\bR)\cap M)\subseteq \HH_n(\bR)\cup\{0\}$)}.$$ 
A real stability preserver 
in the univariate case will alternatively be referred to as a 
{\em hyperbolicity preserver}. For $m\in\bN$ let 
$\RR_m[z] = \{ f \in \RR[z] : \deg(f) \leq m\}$ and 
$\CC_m[z]=\RR_m[z]\oplus i\RR_m[z]=\{ f \in \CC[z] : \deg(f) \leq m\}$. 
If $T$ is a stability (respectively, hyperbolicity) preserving operator 
on $\bC_m[z]$ (respectively, $\bR_m[z]$)
we will also say that $T$ {\em preserves stability} (respectively, 
{\em hyperbolicity}) {\em up to degree} $m$.
\end{definition}

P\'olya-Schur's characterization of multiplier sequences of the first kind
that we already alluded to in the introduction is given in the following 
theorem \cite{CC1,Le,PS}.

\begin{theorem}[P\'olya-Schur theorem]\label{ps}
Let $\lambda : \NN \rightarrow \RR$ be a sequence of real numbers and 
$T: \RR[z] \rightarrow \RR[z]$ be the corresponding (diagonal) linear operator
given by $T(z^n)=\la(n)z^n$, $n\in\bN$.
 Define $\Phi(z)$ to be the formal power series 
$$
\Phi(z) = \sum_{k=0}^\infty \frac{\lambda(k)}{k!}z^k.
$$
The following assertions are equivalent:
\begin{itemize}
\item[(i)] $\lambda$ is a multiplier sequence,  
\item[(ii)] $\Phi(z)$ defines an entire 
function which is the limit, uniformly on compact sets, of 
polynomials with only real zeros of the same sign, 
\item[(iii)] Either $\Phi(z)$ or $\Phi(-z)$ is an entire function 
that can be written as
$$C z^n e^{az} \prod_{k=1}^\infty (1+ \alpha_k z),$$ 
where $n \in \NN$, $C \in \RR$, $a,\alpha_k \geq 0$ for all $k \in \NN$ and 
$\sum_{k=1}^\infty \alpha_k < \infty$, 
\item[(iv)] For all non-negative integers $n$ the  polynomial 
$T[(z+1)^n]$ is hyperbolic with all zeros of the same sign. 
\end{itemize}
\end{theorem} 

As noted in e.g.~\cite[Theorem 3.3]{CC1}, parts (ii)-(iii) in P\'olya-Schur's 
theorem give a 
``transcendental'' description of multiplier sequences while part (iv) 
provides an ``algebraic'' characterization. We emphasize right away the fact
that our main results actually yield 
algebraic and transcendental characterizations of {\em all}
hyperbolicity and stability preservers, respectively, and are therefore
natural generalizations of Theorem~\ref{ps}. Moreover, they also display
an intimate connection between Problem~\ref{pb1} and its finite degree analog
(Problem~\ref{pb2}) in the case of (real) stability preservers. 

\begin{notation}\label{not1}  
Given a linear operator  
$T$ on $\CC[z]$ we extend it to a linear operator -- denoted
again by $T$ -- on the space $\bC[z,w]$ of polynomials in 
the variables $z,w$ by setting
$T(z^kw^\ell) = T(z^k)w^\ell$
for all $k,\ell \in \NN$.
\end{notation}

\begin{definition}\label{def3}
Let $\alpha_1 \leq \alpha_2 \leq \cdots \leq \alpha_n$ and 
$\beta_1 \leq \beta_2 \leq \cdots \leq \beta_m$ be the zeros of two 
hyperbolic polynomials $f,g \in \HH_1(\RR)$. We say that these zeros 
{\em interlace} if they can 
be ordered so that either   
$\alpha_1 \leq \beta_1 \leq \alpha_2 \leq \beta_2 \leq 
\cdots$ or $\beta_1 \leq \alpha_1 \leq \beta_2 \leq \alpha_2 \leq 
\cdots$. Note that in this case one has $|m-n|\le 1$. By convention, 
the zeros of any two polynomials 
of degree $0$ or $1$ interlace. 
\end{definition} 

Our first theorem characterizes linear operators preserving hyperbolicity up 
to some fixed degree $n$. 

\begin{theorem}\label{finitehyp}
Let $n \in \NN$ and let $T : \RR_n[z] \rightarrow \RR[z]$ be a linear 
operator. Then $T$ preserves hyperbolicity 
if and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most two and is of the form 
$$
T(f) = \alpha(f)P + \beta(f)Q,\quad f\in\bR_n[z],
$$
where $\alpha, \beta: \RR_n[z] \rightarrow \RR$ are linear functionals and 
$P, Q\in\HH_1(\bR)$ have interlacing zeros, or 
\item[(b)] $T[(z+w)^n]\in \HH_2(\RR)$, or 
\item[(c)] $T[(z-w)^n]\in \HH_2(\RR)$. 
\end{itemize}
\end{theorem} 

Real stable polynomials in two variables have recently been characterized by 
the authors 
\cite{BBS} as the polynomials $f(z,w)\in\bR[z,w]$ that can be expressed as
\begin{equation}\label{lax}
f(z,w)=\pm \det(zA+wB+C),
\end{equation}
where $A$ and $B$ are positive semi-definite matrices and $C$ is a symmetric 
matrix.  Hence 
(b) and (c) in Theorem~\ref{finitehyp} can be reformulated as 
$$
T[(z+w)^n]= \pm \det(zA \pm wB+C),
$$
where $A$ and $B$ are positive semi-definite matrices and $C$ is a symmetric 
matrix. 

We will also need to deal with the case when we allow complex coefficients. 
\begin{theorem}\label{finitehypC}
Let $n \in \NN$ and let $T : \CC_n[z] \rightarrow \CC[z]$ be a linear 
operator. Then 
$T: \pi_n(\RR) \rightarrow \pi(\RR)$ 
if and only if either 
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one  and is of the form 
$$
T(f) = \alpha(f)P, \quad f\in\bC_n[z],
$$
where $\alpha:\CC_n[z] \rightarrow \CC$ is a linear functional and 
$P\in\HH_1(\bR)$, or 
\item[(b)] $T$ has range of dimension at most two and is of the form 
$$
T(f) = \eta\alpha(f)P + \eta\beta(f)Q,\quad f\in\bC_n[z],
$$
where $\eta \in \CC$,  $\alpha, \beta: \CC_n[z] \rightarrow \CC$  are linear 
functionals such that $\al(\bR_n[z])\subseteq \bR$, $\be(\bR_n[z])\subseteq 
\bR$, and $P,Q\in\HH_1(\bR)$ have interlacing zeros, or 
\item[(c)] There exists $\eta\in\bC$ such that  
$\eta T[(z+w)^n] \in \HH_2(\RR)$, or 
\item[(d)] There exists $\eta\in\bC$ such that  
$\eta T[(z-w)^n]\in \HH_2(\RR)$. 
\end{itemize}
\end{theorem} 

The corresponding theorem for stability preservers up to some fixed degree 
$n$ reads as follows. 

\begin{theorem}\label{finitestab}
Let $n \in \NN$ and let $T : \CC_n[z] \rightarrow \CC[z]$ be a linear 
operator. Then $T$ preserves stability 
if and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P,\quad f\in\bC_n[z],
$$
where $\alpha:\CC_n[z] \rightarrow \CC$ is a linear functional and 
$P\in\HH_1(\bC)$, or 
\item[(b)] $T[(z+w)^n]\in \HH_2(\CC)$. 
\end{itemize}
\end{theorem}

From Theorems~\ref{finitehyp} and~\ref{finitestab} we deduce the following
algebraic characterizations of hyperbolicity and stability preservers,
respectively.

\begin{corollary}[Algebraic Characterization of Hyperbolicity 
Preservers]\label{cor-alghyp}
A linear operator $T:\bR[z]\rightarrow \bR[z]$ preserves hyperbolicity
if and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most two and is of the form 
$$
T(f) = \alpha(f)P + \beta(f)Q,\quad f\in\bR[z],
$$
where $\alpha,\beta:\bR[z]\rightarrow \bR$ are linear functionals and 
$P,Q\in\HH_1(\bR)$ have interlacing zeros, or 
\item[(b)]
$T[(z + w)^n]\in \HH_2(\bR)\cup \{0\}$ for all $n\in \bN$, or
\item[(c)]
$T[(z -w)^n]\in \HH_2(\bR)\cup \{0\}$ for all $n\in \bN$.
\end{itemize}
\end{corollary}

\begin{corollary}[Algebraic Characterization of Stability 
Preservers]\label{cor-algstab}
A linear operator $T:\bC[z]\rightarrow \bC[z]$ preserves stability 
if and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P,\quad f\in\bC[z],
$$
where $\alpha:\bC[z]\rightarrow \bC$ is a linear functional and 
$P\in\HH_1(\bC)$, or 
\item[(b)] $T[(z+w)^n]\in \HH_2(\bC)\cup \{0\}$ for all $n\in \bN$.
\end{itemize}
\end{corollary} 

\begin{notation}\label{not2}
To any linear operator $T:  \CC[z] \rightarrow \CC[z]$ we associate a formal 
power series in $w$ 
with polynomial coefficients in $z$
$$
G_T(z,w)= \sum_{n=0}^\infty \frac{(-1)^nT(z^n)}{n!}w^n\in\bC[z][[w]]. 
$$
Let $n$ be a positive integer and denote by $\HC_n(\CC)$ and $\HC_n(\RR)$, 
respectively, the set of entire functions in $n$ variables that are limits, 
uniformly on compact sets, 
of  polynomials in $\HH_n(\CC)$ and $\HH_n(\RR)$, respectively. Hence in our 
notation $\HC_1(\RR)$ is the Laguerre-P\'olya class of  entire functions, 
sometimes denoted by $\mathcal{L}$-$\mathcal{P}$ in the literature. For a 
description of $\HC_1(\CC)$ and $\HC_2(\CC)$ we refer 
to \cite[Chap. IX]{Le}.
\end{notation} 

\begin{remark}
As noted in \cite{BBS}, any linear operator $T$ on $\bC[z]$ may be uniquely 
represented as a formal linear differential operator with polynomials 
coefficients, i.e., $T=\sum_{k=0}^{\infty}Q_k(z)\frac{d^k}{d z^k}$, where
$Q_k\in \bC[z]$, $k\ge 0$. In \cite{BBS} we used the (formal) 
symbol of $T$, i.e., 
$F_T(z,w):=\sum_{k=0}^{\infty}Q_k(z)w^k\in\bC[z][[w]]$. One can easily check
that the
``modified symbol'' $G_T(z,w)$ introduced in Notation~\ref{not2} satisfies
$G_T(z,w)e^{zw}=F_T(z,-w)$.
\end{remark}

\begin{theorem}[Transcendental Characterization of Hyperbolicity 
Preservers]\label{tranR}
A linear operator $T: \RR[z] \rightarrow \RR[z]$ preserves hyperbolicity if 
and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most two and is of the form 
$$
T(f) = \alpha(f)P + \beta(f)Q,\quad f\in\bR[z],
$$
where $\alpha,\beta:\bR[z]\rightarrow \bR$ are linear functionals and 
$P,Q\in\HH_1(\bR)$ have interlacing zeros, or 
\item[(b)] $G_T(z,w) \in \HC_2(\RR)$, or 
\item[(c)]  $G_T(z,-w)\in \HC_2(\RR)$. 
\end{itemize}
\end{theorem}

\begin{theorem}[Transcendental Characterization of Stability 
Preservers]\label{tranC}
A linear operator $T: \CC[z] \rightarrow \CC[z]$ preserves stability if and 
only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P, \quad f\in\bC[z],
$$
where $\alpha:\CC[z] \rightarrow \CC$ is a linear functional and 
$P\in\HH_1(\bC)$, or 
\item[(b)] $G_T(z,w) \in \HC_2(\CC)$.
\end{itemize}
\end{theorem}
