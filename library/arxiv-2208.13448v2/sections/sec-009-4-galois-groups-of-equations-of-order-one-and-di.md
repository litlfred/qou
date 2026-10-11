---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-009-4-galois-groups-of-equations-of-order-one-and-di
section_title: "Galois groups of equations of order one and diagonal systems"
section_number: 4
pages: 20-21
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.656
---
\label{sec:GaloisGpsOrderOneEtDiag}


\subsection{Galois groups of equations of order one}\label{secorder1}

We consider the equation of order one
\begin{equation}
\label{eq:orderone}
\phi(y)=\alpha y \, \quad \alpha\in \k^*.
\end{equation}

Let us now see how to compute the Galois group $G$ of this difference equation. Recall that since $G\subset \mathrm{GL}_1 (C)$ is an algebraic group, either $G$ is $C^*$, or it is isomorphic to $\Z/\ell\Z$ for some $\ell \in \N^*$.

\begin{prop}\label{propord1}
 We have $G\sim \Z/\ell\Z$ if and only if there exists $\zeta$, a primitive $\ell$th root of unity and  a nonzero solution $f\in \k^*$ of  $\phi(y)=(\zeta/\alpha)y$.  In that situation,  $\zeta=\alpha\frac{\phi(f)}{f}$, and $[\zeta]$ is a reduced form of $[\alpha]$ with a gauge transformation $(f)$.  
\end{prop}

\begin{proof}
Since the Galois group $G$ of \eqref{eq:orderone} is an algebraic subgroup of $C^{\star}$, it is a finite cyclic group or the multiplicative group $C^{\star}$. 
Any equivalent equation of \eqref{eq:orderone} is of the form $\phi(y)=\alpha\frac{\phi(f)}{f}y$ with $f\in\k^{\star}$. 
Therefore, from Theorem \ref{theo:reduced form}, if $G$ is a finite cyclic group of order $\ell\in\mathbb{N}^*$ then there exist $f\in\k^{\star}$ and $\zeta$, a primitive $\ell$th root of unity,  such that $\zeta= \alpha\frac{\phi(f)}{f}$. \par Conversely, assume that there exist $f\in\k^{\star}$ and $\zeta$, a primitive $\ell$th root of unity,  such that $\zeta= \alpha\frac{\phi(f)}{f}$. From Theorem \ref{theo:reduced form}, $G$ is contained in $\Z/\ell\Z$. Then,  
$G\sim \Z/\ell_1\Z$ where $\ell_1$ divides $\ell$. Then, there exist $g\in\k^{\star}$ and $\zeta_1$, a primitive $\ell_1$th root of unity,  such that $\zeta_1= \alpha\frac{\phi(g)}{g}$. This implies $\alpha^{\ell_1}=g^{\ell_1}/\phi(g^{\ell_1})$. Let $h:=(f/g)^{\ell}$. Thus, $\phi(h) = h$ so $h\in C^*$. Since $C$ is algebraically closed, there exists $c\in C^*$ such that $f=cg$ (with $c^{\ell} = h$). Using this equality, we obtain $\zeta = \zeta_1$ and since $\zeta$ is a primitive $\ell$th root of unity, $\ell=\ell_1$.
\end{proof}


\begin{rem}
Since $\det(G)$ is the Galois group of $\phi (y)=\det (A)y$, an equation of order $1$, we may now compute $\det(G)$ if we are able to reduce the  difference equations of order $1$.
\end{rem}

\begin{ex}\label{ex3}
Consider the difference equation \eqref{eq0} and let $G$ be its difference Galois group over $\C(z^{1/*})$. Assume that $t\neq 0$. We want to compute $\det(G)$.  We have to compute the difference Galois group of $\phi(y)=\frac{-q^3 z}{t}y=\alpha y$ over $\C(z^{1/*})$.  By Proposition~\ref{propord1},  $\det(G)$ is finite if and only if there exists $\zeta$, a primitive $\ell$th root of unity, and a nonzero solution $f\in \k^*$ of  $\phi(y)=(\zeta/\alpha)y$.  But the valuation of $\alpha$ at $z=0$ is $1$, proving that $\zeta/\alpha$ must have valuation $-1$. Since for $f\in\k^*$,  $f$ and $\phi(f)$ have the same valuation,  the equation $\phi(f)=(\zeta/\alpha)f$ with $f\in\k^*$, and $\zeta$ a root of unity,  has no solutions.  Therefore,  $\det(G)=\C^*$.
\end{ex}
