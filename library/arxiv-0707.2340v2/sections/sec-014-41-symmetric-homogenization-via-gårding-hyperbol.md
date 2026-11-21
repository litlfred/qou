---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-014-41-symmetric-homogenization-via-gårding-hyperbol
section_title: "Symmetric Homogenization via Gårding Hyperbolic Polynomials"
section_number: 4.1
pages: 21-24
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.955
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — We introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polynomials that amount to"
---
\label{s-gar}

The following theorem shows that the symmetric 
homogenization (cf.~\S \ref{s22}) of any strongly Rayleigh measure is again
strongly Rayleigh, so that 
strongly Rayleigh measures belong to the class PHR (Definition~\ref{phr}).
 
\begin{theorem}\label{SH}
If $\mu\in \fP_{n}$ is strongly Rayleigh then so is its symmetric 
homogenization $\mu_{sh}\in\fP_{2n}$.
\end{theorem}

The proof of Theorem~\ref{SH} makes use of the theory of hyperbolic 
polynomials that has its origins in partial differential equations 
and was developed by 
Petrovsky, G\aa rding, H\"ormander, Atiyah and Bott 
\cite{ABG,garding,hormander}. Recently, hyperbolic polynomials have proved
to be quite useful in other areas of mathematics such as convex optimization 
\cite{BGLS,guler}, complex analysis \cite{BBS}, matrix theory and 
combinatorics \cite{Gu1,Gu}. 

Let $e\in \RR^n$. A homogeneous polynomial $p \in \RR[z_1,\ldots, z_n]$ is 
said to be {\em (G\aa rding) hyperbolic with respect to} $e$ if $p(e)\neq 0$ 
and for all $x \in \RR^n$ the univariate polynomial 
$t \mapsto p(x+te)$ has only real zeros. Recall that the {\em homogenization} 
of a polynomial $f(z_1,\ldots,z_n)=\sum_{\alpha \in \NN^n}a(\alpha)z^\alpha  
\in \CC[z_1, \ldots, z_n]$ of degree $d$ is given by
 $$f_H(z_1,\ldots,z_{n+1}) = z_{n+1}^df(z_1/z_{n+1}, \ldots, z_n/z_{n+1}).$$  

Recall the characterization of real stable polynomials given in 
Proposition~\ref{pro-rs} (1). The relationship between 
real stable polynomials and hyperbolic polynomials is made explicit by the 
following result, see \cite[Proposition 1]{BBS2}.

\begin{proposition}\label{hyp-stab}
Let $f \in \RR[z_1,\ldots, z_n]$. Then $f$ is real stable if and only if 
$f_H$ is hyperbolic with respect to all vectors $e \in \RR^{n+1}$ of the form 
$e=(e_1, \ldots, e_n, 0)$, where $e_i>0$ for $1 \leq i \leq n$. 
\end{proposition} 

Let $p$ be hyperbolic with respect to $e\in\RR^n$. The cone 
$$
C_e(p)=\{x \in \RR^n : p(x+te) \neq 0, t \geq 0\}
$$
is called the {\em hyperbolicity cone} of $p$. The following fundamental 
properties of the hyperbolicity cone are due to G\aa rding \cite{garding}, 
see also \cite{ABG,guler,hormander}. 

\begin{proposition}\label{fund-hyp}
Let $p \in \RR[z_1,\ldots,z_n]$ be hyperbolic with respect to $e\in\RR^n$. 
Then 
\begin{itemize}
\item[(a)] $C_e(p)$ is convex; 
\item[(b)] $C_e(p)$ is equal to the connected component of the set 
$\{ x \in \RR^n : p(x) \neq 0\}$ that contains $e$;
\item[(c)] $(s,t)\mapsto p(x+su+te)$ is real stable for any $x\in \RR^n$ 
and $u\in C_e(p)$; 
\item[(d)] $p$ is hyperbolic with respect to any $u\in C_e(p)$ and 
$C_u(p)=C_e(p)$.
\end{itemize}
\end{proposition}

Below are examples of hyperbolic polynomials and their hyperbolicity 
cones: 

\begin{itemize}
\item[(I)] The polynomial $p(z_1,\ldots,z_n)= z_1z_2\cdots z_n$ is hyperbolic 
with respect to the direction $e=(1,\ldots,1)\in\RR^n$ and the hyperbolicity 
cone is the positive orthant $C_e(p)=\RR_+^n$; 
\item[(II)] The (principal) symbol of the hyperbolic wave equation, i.e., 
the polynomial 
$$
p(z_1,\ldots, z_n) = z_1^2-\sum_{j=2}^n z_j^2
$$
is hyperbolic with respect to the direction $e=(1,0,\ldots,0)\in\RR^n$ and 
the hyperbolicity cone is the Lorentz cone 
$$
C_e(p)=\left\{z \in \RR^n : \sqrt{z_2^2+\cdots+z_n^2} \leq z_1\right\};
$$
\item[(III)] Let $z_{ij}$, $1\le i\le j\le n$, be $n(n+1)/2$ different 
variables and let $X=(x_{ij})_{i,j=1}^n$  be the matrix with entries 
$$
x_{ij} = \begin{cases} 
z_{ij} \mbox{ if } i \leq j, \\
z_{ji} \mbox{ if } i > j.
\end{cases} 
$$
The polynomial (in $n(n+1)/2$ variables) 
$p(z_{11}, \ldots, z_{nn}) = \det(X)$ is  hyperbolic with respect to the
$n\times n$ identity matrix $I$ and the hyperbolicity cone is the cone of 
positive definite $n\times n$ matrices; 
\item[(IV)] Let $A_1, \ldots, A_m$ be symmetric $n \times n$ matrices and let 
$e=(e_1,\ldots,e_m) \in \RR^m$ be such that  $e_1A_1 + \cdots+e_mA_m$ is 
positive definite. Then the polynomial 
$$
p(z_1,\ldots, z_m) = \det\left(\sum_{j=1}^m z_jA_j\right)
$$
is hyperbolic with respect to $e$ and the hyperbolicity cone is given by 
$$
C_e(p)= \left\{ x \in \RR^m : \sum_{j=1}^n x_jA_j \mbox{ is positive 
definite}\right\}.
$$   
\end{itemize}

\begin{theorem}\label{homhom}
Suppose that all the coefficients of $f \in \RR[z_1,\ldots, z_n]$ are 
non-negative. The following are equivalent:
\begin{enumerate} 
\item $f_H$ is stable; 
\item $f$ is stable; 
\item $f_H$ is hyperbolic with respect to some vector $e$ with $e_i\geq 0$; 
$1 \leq i \leq n+1$;
\item $f_H$ is hyperbolic with respect to any vector $e$ with $e_i>0$, 
$1 \leq i \leq n+1$. 
\end{enumerate}
\end{theorem}

\begin{proof}
By the fact that the stability property is 
closed under setting variables equal to real numbers 
(Proposition~\ref{pro-rs}) and Proposition~\ref{hyp-stab} we have that 
(1) $\Rightarrow$ (2) $\Rightarrow$ (3). 
Now if (3) holds then since $f$ has all non-negative coefficients it follows
from Proposition~\ref{fund-hyp} (b) that 
$C_e(f_H)$ contains the cone $\RR_+^{n+1}$, which by 
Proposition~\ref{fund-hyp} (d) proves (4). Finally, 
(4) $\Rightarrow$ (1) by Proposition~\ref{pro-rs}.
\end{proof}

Let $f \in \CC[z_1,\ldots, z_n]$ be a polynomial of degree $d_i$ in $z_i$, 
$1\le i\le n$. The 
{\em polarization} $\pi(f)$ of $f$ is the unique polynomial in 
$\sum_{i=1}^{n}d_i$ variables 
$z_{ij}$, $1 \leq i \leq n$, $1 \leq j \leq d_i$, satisfying:
\begin{enumerate}
\item[(i)] $\pi(f)$ is multi-affine; 
\item[(ii)] $\pi(f)$ is symmetric in the variables 
$z_{i1}, \ldots z_{id_i}$ for 
$1 \leq i \leq n$;
\item[(iii)] if we let  $z_{ij}=z_i$ for all $i,j$ in $\pi(f)$ we recover $f$.
\end{enumerate}

Recall that a {\em circular region} in $\CC$ is either an open or closed 
affine half-plane or the open or closed interior or exterior of a circle. 
The famous Grace-Walsh-Szeg\"o coincidence theorem 
\cite{grace,RS,walsh} is stated next. For a proof of the following version we 
refer to \cite[Theorem 2.12]{COSW}. 

\begin{theorem}[Grace-Walsh-Szeg\"o]\label{GWS}
Let $f \in \CC[z_1,\ldots, z_n]$ be symmetric and multi-affine and let $C$ be 
a circular region 
containing the points $\zeta_1, \ldots, \zeta_n$. Suppose that either $f$
has total degree $n$ or $C$ is convex (or both). Then there exists at least
one point 
$\zeta \in C$ such that 
$f(\zeta_1, \ldots, \zeta_n)=f(\zeta, \ldots, \zeta)$.

\end{theorem}
From the Grace-Walsh-Szeg\"o coincidence theorem we deduce:

\begin{corollary}\label{polarizeit}
Let $f \in \CC[z_1,\ldots, z_n]$. Then 
$f$ is stable if and only if $\pi(f)$ is stable. 
\end{corollary}

\begin{proof}
If $\pi(f)$ is stable then so is $f$ since the latter is recovered from 
$\pi(f)$ by setting variables equal as in (iii) above. Now suppose that 
$\pi(f)$ is not stable. Then there are numbers 
$\zeta_{ij} \in \{z \in \CC : \Im(z)>0\}$, $1 \leq i \leq n$, 
$1 \leq j \leq d_i$, such 
that $\pi(f)(\zeta)=0$, where
$\zeta
=(\zeta_{11},\ldots,\zeta_{1d_1},\ldots,\zeta_{n1},\ldots,\zeta_{nd_n})$.
By successively applying the Grace-Walsh-Szeg\"o coincidence theorem we see 
that there is a vector $\zeta' = 
(\zeta_{11}',\ldots,\zeta_{1d_1}',\ldots,\zeta_{n1}',\ldots,\zeta_{nd_n}')$ 
with coordinates in $\{z \in \CC : \Im(z)>0\}$ for which $\zeta_{ij}'
= \zeta_{k\ell}'$ whenever $i=k$ and $\pi(f)(\zeta')=\pi(f)(\zeta)=0$. Hence 
$f(\zeta_{11}', \zeta_{21}' \ldots, \zeta_{n1}')=\pi(f)(\zeta')=0$, so $f$ is 
not stable either. 
\end{proof}

We now have all the tools to prove Theorem~\ref{SH}. 

\begin{proof}[Proof of Theorem~\ref{SH}]
Let $g$ be the generating polynomial of $\mu\in\fP_n$ and 
suppose that $g$ is stable of degree $d$. 
Then so is the homogenization $g_H$ of $g$ by Proposition~\ref{hyp-stab}. 
Now straightforward computations show that the generating polynomial of 
the symmetric homogenization $\mu_{sh}\in\fP_{2n}$ is given by
 $\pi(z_{n+1}^{n-d}g_H)$, so the theorem follows from 
Corollary~\ref{polarizeit}. 
\end{proof}
