---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-009-4-galois-groups-of-equations-of-order-one-and-di
section_title: "Galois groups of equations of order one and diagonal systems"
section_number: 4
pages: 20-21
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
text_source: latex
latex_prose_ratio: 0.636
latex_coverage_ratio: 0.957
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
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



\subsection{Galois groups of diagonal systems}\label{sec:diagonalCase}

For more details on what follows, we refer to \cite[Section 2.2]{van2006galois}.
Let us consider a diagonal system 
\begin{equation}
\label{eq:diagsyst}
\phi(Y)=\mathrm{Diag}\left(\alpha_1,\ldots,\alpha_n\right) Y 
\end{equation}
where $\mathrm{Diag}\left(\alpha_1,\ldots,\alpha_n\right)\in\GL_n\left(\k\right)$ is the diagonal matrix whose nonzero entry at the line $i$ is $\alpha_i$.  
By Theorem~\ref{theo:reduced form}, the Galois group is an algebraic subgroup of the $n$-dimensional torus $T$.  The matrices of $G$ are of the form $\mathrm{Diag} (c_1, \dots , c_n)$.  We recall that a character on $T$ is a morphism $\chi:T\rightarrow C^{\star}$. It is of the form   $\chi_{\mathbf{m}}(z_1,\ldots,z_n)=z_1^{m_1}\ldots z_n^{m_n}$ with $\mathbf{m}:=\left(m_1,\ldots,m_n\right)\in\mathbb{Z}^n$. Since an algebraic subgroup of $T$ is the intersection of the kernels of some characters on $T$, we have to find the $\mathbf{m}\in\mathbb{Z}^n$ such that $c_1^{m_1}\ldots c_n^{m_n}=1$ for all  $\mathrm{Diag} (c_1, \dots , c_n) \in G$. 
By Theorem~\ref{theo:reduced form}, a gauge transformation which reduces the system will be diagonal, denoted by  $\mathrm{Diag}(f_1,\dots,f_n)$. Thus, the difference Galois group of \eqref{eq:diagsyst} is the intersection of the kernels of the $\chi_{\mathbf{m}}$ for all $\mathbf{m}\in\mathbb{Z}^n$ such that there exist $f_1,\ldots, f_n\in\k^*$ satisfying
\begin{equation}
\label{eq:conditionsSystDiag}
 \left(\frac{\phi(f_1)}{f_1}\alpha_1 \right)^{m_{1}}\times\ldots \times \left(\frac{\phi(f_n)}{f_n} \alpha_n \right)^{m_{n}}= 1\,.   
\end{equation} 
The question of how to solve  \eqref{eq:conditionsSystDiag} depends on the examples (see one example in \cite[Section 2.2]{van2006galois}). In general it is a complicated task.
