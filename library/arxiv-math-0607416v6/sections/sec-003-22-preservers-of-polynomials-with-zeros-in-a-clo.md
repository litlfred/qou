---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-003-22-preservers-of-polynomials-with-zeros-in-a-clo
section_title: "Preservers of Polynomials with Zeros in a Closed Circular Domain or Its Boundary"
section_number: 2.2
pages: 7-9
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.966
doc_brief: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES — We characterize all linear operators on ﬁnite or inﬁnite-dimensio- nal polynomial spaces that preserve the property of having"
---
\label{ss22}

Recall that a M\"obius transformation is a bijective conformal map of the 
extended complex plane, i.e., 
a map $\Phi : \CC\cup \{\infty\} \rightarrow \CC \cup \{\infty\}$ given by  
\begin{equation}\label{mobius}
\Phi(z)= \frac {az+b}{cz+d}, \quad a,b,c,d \in \CC,\, ad-bc \neq 0. 
\end{equation}
The inverse of $\Phi$ is then given by 
$$ 
 \Phi^{-1}(z)= \frac{dz-b}{-cz+a}. 
$$

\begin{definition}\label{def-circ}
Let $H=\{z \in \CC : \Im(z) >0\}$ and 
$\overline{H}=\{z \in \CC : \Im(z) \ge 0\}$. An {\em open circular domain} is 
the image 
of $H$ under a  M\"obius transformation, i.e., an open disk, the (open) 
complement of a closed disk or an 
open affine half-plane. A {\em closed circular domain} is the image 
of $\overline{H}$ under a M\"obius transformation, that is, a closed disk, 
the (closed) complement of an open disk or a
closed affine half-plane. 
\end{definition}

For technical reasons we will henceforth assume the following:
\begin{equation}\label{assum}
\begin{split}
&\text{{\em If $C$ is a half-plane then the corresponding M\"obius 
transformation}}\\ 
&\text{{\em $\Phi : C \rightarrow H$  is a translation composed with a 
rotation, i.e., $c=0$ in \eqref{mobius}.}}
\end{split}
\end{equation}

Let us also extend Definition~\ref{def1} to arbitrary sets 
$\Omega\subseteq \CC$. 

\begin{definition}\label{def-stab-om}
A polynomial $f \in \CC[z_1,\ldots, z_n]$ is called 
$\Omega$-{\em stable} if $f(\zeta_1, \ldots, \zeta_n)\neq 0$ whenever 
$\zeta_j \in \Omega$ for all 
$1 \leq j \leq n$. 
\end{definition} 

\begin{remark}\label{r-h-stab}
Note that an $H$-stable polynomial is precisely a stable polynomial in the
sense of Definition~\ref{def1}.
\end{remark}

A fundamental discrepancy between $\pi_n(C_1)$ and $\pi_n(C_2)$, where $C_1$ 
is closed and unbounded 
and $C_2$ is closed and bounded, is that 
$\pi_n(C_1) \setminus \pi_{n-1}(C_1)$ is dense in $\pi_n(C_1)$ while  
$\pi_n(C_2) \setminus \pi_{n-1}(C_2)$ is not dense in $\pi_n(C_2)$ since 
constant non-zero polynomials do not belong to
$\overline{\pi_n(C_2) \setminus \pi_{n-1}(C_2)}$.  In order for a linear 
transformation $T: \CC_n[z] \rightarrow \CC[z]$ to map  
$\pi_n(C_1) \cup \{0\}$  into  $\pi(C_1) \cup\{0\}$ it is therefore enough 
(by Hurwitz' theorem) for 
$T$ to map $\pi_n(C_1) \setminus \pi_{n-1}(C_1)$ into  $\pi(C_1) \cup\{0\}$. 
However, this is not the case for $C_2$.  Indeed, take for instance $C_2$ to 
be the closed unit disk and let $T_n : \CC_n[z] \rightarrow \CC_{n-1}[z]$ be 
defined by 
$$
T(z^k) = (n-k)z^k + kz^{k-1}, \quad 0\le k\le n.
$$ 
An application of Theorem~\ref{circularregion} below shows that 
$T: \pi_n(C_2) \setminus \pi_{n-1}(C_2) \rightarrow \pi(C_2) \cup\{0\}$ but 
$T(z^{n-1})=z^{n-2}(z+n-1)$, which does not belong to $\pi(C_2)$ for 
$n \geq 3$. Therefore we need to solve a more general version of 
Problem~\ref{pb2}, namely Problem~\ref{pb3} in \S \ref{s1}. This is done in 
the next two theorems for all closed circular domains and their boundaries.

\begin{notation}\label{not-sets}
Given $\Omega \subseteq \CC$  we denote its
complement $\bC\setminus \Omega$ by $\Omega'$, its boundary 
$\overline{\Om}\setminus\mathring{\Om}$ by $\partial\Om$, and we let $\Om^r$ 
be the interior of
the complement of $\Om$, that is, $\Om^r=\mathring{\Om'}$. 
\end{notation}

\begin{theorem}\label{circularregion}
Let $n \in \NN$ and $T : \CC_n[z] \rightarrow \CC[z]$ be a linear operator. Let
further $C$ be an open circular domain given by $C=\Phi^{-1}(H)$,
where $\Phi$ 
is a M\"obius transformation as in \eqref{mobius}. 
Then $T : \pi_n(C')\setminus \pi_{n-1}(C') \rightarrow \pi(C')\cup\{0\}$ if 
and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P,\quad f\in\CC_n[z],
$$
where $\alpha: \CC_n[z] \rightarrow \CC$ is a linear functional and 
$P \in \pi(C')$, or 
\item[(b)] The polynomial 
$$
T\left[\big((az+b)(cw+d)+(aw+b)(cz+d)\big)^n\right] 
$$
is $C$-stable.
\end{itemize}
\end{theorem}
\begin{remark}
In the case when $C'$ is the closed unit disk then for 
\begin{equation}\label{spec-fi}
\Phi(z)=\frac{(i/2)(z+i)}{z-i}
\end{equation}
the polynomial in (b) of Theorem~\ref{circularregion} reduces to 
$i^nT[(1+zw)^n]$. 
\end{remark}

\begin{notation}\label{not-fi}
Given a M\"obius transformation $\Phi$ as in \eqref{mobius} and $n\in\bN$ 
we define an invertible linear transformation  
$\phi_n : \CC_n[z] \rightarrow \CC_n[z]$  by 
$\phi_n(f)(z) = (cz+d)^nf(\Phi(z))$.
\end{notation}
 
\begin{theorem}\label{circle}
Let $n \in \NN$ and $T : \CC_n[z] \rightarrow \CC[z]$ be a linear operator 
and let further $C=\Phi^{-1}(H)$ be an unbounded open circular domain, where 
$\Phi$ 
is a M\"obius transformation as in \eqref{mobius}. 
Then 
$T : \pi_n(\partial C)\setminus \pi_{n-1}(\partial C) \rightarrow 
\pi(\partial C)\cup\{0\}$ if and only if either
\begin{itemize}
\item[(a)]  $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P, \quad f\in\CC_n[z],
$$
where $\alpha: \CC_n[z] \rightarrow \CC$ is a linear functional and 
$P \in \pi(\partial C)$, or 
\item[(b)] $T$ has range of dimension  two and the linear operator given 
by $S=\phi^{-1}_mT\phi_n$ is a stability preserver as in (b) of 
Theorem~\ref{finitehypC}, where $m = \max\{\deg T(f): f \in \CC_n[z]\}$, or
\item[(c)] The polynomial  
$$
T\left[\big((az+b)(cw+d)+(aw+b)(cz+d)\big)^n\right] 
$$
is both $C$-stable and $C^r$-stable,  or 
\item[(d)] The polynomial 
$$
T\left[\big((az+b)(cw+d)-(aw+b)(cz+d)\big)^n\right]
$$
is both $C$-stable and $C^r$-stable.
\end{itemize}
\end{theorem}

\begin{remark}
If $\partial C$ is the unit circle then for $\Phi$ as in~\eqref{spec-fi} the 
polynomials in (c) and (d) of Theorem~\ref{circle} simply become 
$i^nT[(1+zw)^n]$ and $T[(z-w)^n]$, respectively. 
\end{remark}

For the sake of completeness we also formulate analogs of 
Corollaries~\ref{cor-alghyp} and~\ref{cor-algstab} providing algebraic 
characterizations in the case of closed circular domains and their boundaries. 

\begin{corollary}[Algebraic Characterization: Closed Circular Domain 
Case]\label{alg-circularregion}
Let $T : \CC[z] \rightarrow \CC[z]$ be a linear operator and let
$C\subset \CC$ be an open circular domain given by $C=\Phi^{-1}(H)$,
where  $\Phi$ 
is a M\"obius transformation as in \eqref{mobius}. 
Then $T : \pi(C') \rightarrow \pi(C')\cup\{0\}$ if and only if either
\begin{itemize}
\item[(a)] $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P,\quad f\in \bC[z],
$$
where $\alpha: \CC[z] \rightarrow \CC$ is a linear functional and 
$P \in \pi(C')$, or 
\item[(b)] For all $n \in \NN$ the polynomial 
$$
T\left[\big((az+b)(cw+d)+(aw+b)(cz+d)\big)^n\right] 
$$
is $C$-stable.
\end{itemize}
\end{corollary}
 
\begin{corollary}[Algebraic Characterization: Circle and Line 
Case]\label{cor-circle}
Let  $T : \CC[z] \rightarrow \CC[z]$ be a linear operator and 
$C=\Phi^{-1}(H)$ be an unbounded open circular domain,  where $\Phi$ 
is a M\"obius transformation as in \eqref{mobius}. 
Then $T : \pi(\partial C) \rightarrow \pi(\partial C)\cup\{0\}$ if and only 
if either
\begin{itemize}
\item[(a)]  $T$ has range of dimension at most one and is of the form 
$$
T(f) = \alpha(f)P,\quad f\in \bC[z],
$$
where $\alpha: \CC[z] \rightarrow \CC$ is a linear functional and 
$P\in\pi(\partial C)$, or 
\item[(b)] $T$ has range of dimension  two and  for all $n \in \NN$ the 
linear operator given by $S_n=\phi^{-1}_{m(n)}T\phi_n$ is a stability 
preserver as in (b) of Theorem~\ref{finitehypC}, where 
$m(n) = \max\{\deg T(f): f \in \CC_n[z]\}$, or  
\item[(c)] For all $n \in \NN$ the polynomial  
$$
T\left[\big((az+b)(cw+d)+(aw+b)(cz+d)\big)^n\right] 
$$
is both $C$-stable and $C^r$-stable,  or 
\item[(d)] For all $n \in \NN$ the polynomial 
$$
T\left[\big((az+b)(cw+d)-(aw+b)(cz+d)\big)^n\right]
$$
is both $C$-stable and $C^r$-stable.
\end{itemize}
\end{corollary}

Similarly, we may characterize all linear maps that take polynomials with 
zeros in one closed 
circular domain $\Om_1$ to polynomials with zeros in another closed circular 
domain $\Om_2$, or 
the boundary of one  
circular domain $\Om_1$ to the boundary of another circular domain $\Om_2$. 
However, this only amounts to composing with linear operators of the type 
defined
in Notation~\ref{not-fi}, namely 
$\phi_n : \CC_n[z] \rightarrow \CC_n[z]$, where 
$
\phi_n(f)(z) = (cz+d)^n f(\Phi(z))
$ 
and $\Phi$ is an appropriate M\"obius transformation of the form 
\eqref{mobius}.
