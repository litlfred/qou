---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-041-101-noncommutative-alexander-polynomials
section_title: "Non–commutative Alexander polynomials"
section_number: 10.1
pages: 31-32
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.941
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{sec:phicompatible}



Let $\mathbb{K}$ be a (skew) field and $\gamma:\mathbb{K}\to \mathbb{K}$ a ring homomorphism. Denote by $\mathbb{K}[t^{\pm 1}]$ the corresponding skew Laurent
polynomial ring over $\mathbb{K}$. The elements in $\mathbb{K}[t^{\pm 1}]$ are formal sums
$\sum_{i=-r}^s a_it^i$ with $a_i\in \mathbb{K}$ and multiplication in $\mathbb{K}[t^{\pm 1}]$ is given by the rule
$t^ia=\gamma^i(a)t^i$ for any $a\in \mathbb{K}$.



Let $N$ be a 3--manifold and let $\phi \in H^1(N;\mathbb{Z})$ be non--trivial.
Following Turaev \cite{Tu02b} we call a ring homomorphism $\varphi:\mathbb{Z}[\pi_1(N)] \to \mathbb{K}[t^{\pm 1}]$ \emph{$\phi$--compatible}
if for any $g\in \pi_1(N)$ we have $\varphi(g)=kt^{\phi(g)}$ for some $k\in \mathbb{K}$.
Given a $\phi$--compatible  homomorphism $\varphi:\mathbb{Z}[\pi_1(N)]\to \mathbb{K}[t^{\pm 1}]$ we  consider
the  $\mathbb{K}[t^{\pm 1}]$--module
\[ H_i(N;\mathbb{K}[t^{\pm 1}])= H_i(C_*(\tilde{N})\otimes_{\mathbb{Z}[\pi_1(N)]} \mathbb{K}[t^{\pm 1}])\]
 where $\tilde{N}$ is the universal cover of $N$.
Since $\mathbb{K}[t^{\pm 1}]$ is a principal ideal domain
(PID) (cf. \cite[Proposition~4.5]{Co04}) we can decompose
\[ H_i(N;\mathbb{K}[t^{\pm 1}])\cong \bigoplus_{k=1}^l
\mathbb{K}[t^{\pm 1}]/(p_k(t))\] for $p_k(t)\in \mathbb{K}[t^{\pm 1}]$, $1 \le k \le l$. We define
$\Delta_{N,\phi,i}^\varphi\mathrel{\mathop:}=\prod_{k=1}^lp_k(t) \in \mathbb{K}[t^{\pm 1}]$.
As for twisted Alexander polynomials we write $\Delta_{N,\phi}^\varphi=\Delta_{N,\phi,1}^\varphi$.
Non--commutative Alexander polynomials have in general a high indeterminacy,
we refer to \cite[p.~367]{Co04} and
\cite[Theorem~3.1]{Fr07} for a discussion of the indeterminacy.
Note though that the degree of a non--commutative Alexander polynomial is well--defined.





The following theorem was proved for knots by Cochran \cite{Co04} and extended to 3--manifolds by
Harvey \cite{Ha05} and Turaev \cite{Tu02b}.

\begin{theorem}\label{thm:lowerboundho}
Let $N$ be a 3--manifold with empty or toroidal boundary and let $\phi\in H^1(N;\mathbb{Z})$ non--trivial.
Let $\varphi:\mathbb{Z}[\pi_1(N)]\to \mathbb{K}[t^{\pm 1}]$ be a $\phi$--compatible  homomorphism.
\begin{enumerate}
\item If the image of $\pi_1(N)\to \mathbb{K}[t^{\pm 1}]$ is non--cyclic, then
\[ \deg(\Delta_{N,\phi,0}^\varphi)=0.\]
\item If the image of $\pi_1(N)\to \mathbb{K}[t^{\pm 1}]$ is non--cyclic and if $\Delta_{N,\phi}^\varphi\ne 0$, then
\[ \deg(\Delta_{N,\phi,2}^\varphi)=0.\]
\item If $\Delta_{N,\phi}^\varphi\ne 0$, then we have the following inequality
\[ ||\phi||_T \geq \deg(\Delta_{N,\phi}^\varphi)- \deg(\Delta_{N,\phi,0}^\varphi)-\deg(\Delta_{N,\phi,2}^\varphi)\]
and equality holds if $\phi$ is a fibered class and $N\ne S^1\times D^2, N\ne S^1\times S^2$.
\end{enumerate}
\end{theorem}

We refer to \cite{Fr07} for the definition of a twisted non--commutative Alexander polynomial
and to a corresponding generalization of Theorem \ref{thm:lowerboundho}, we also refer to \cite{Fr07} for
a reinterpretation of the third statement of
Theorem \ref{thm:lowerboundho} in terms of a certain non--commutative Reidemeister torsion.
