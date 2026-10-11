---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-010-42-galois-groups-of-diagonal-systems
section_title: "Galois groups of diagonal systems"
section_number: 4.2
pages: 21-21
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
text_source: latex
latex_prose_ratio: 0.852
latex_coverage_ratio: 0.981
---
\label{sec:diagonalCase}

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
