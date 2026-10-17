---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-016-64-summary
section_title: "Summary"
section_number: 6.4
pages: 34-34
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.986
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀerence Galois groups of order three equations for a large class"
---
Let 
 $$
 L := \phi^3 + a_2 \phi^2 +a_1 \phi +a_0\in \k\left< \phi,\phi^{-1}\right>
 $$  and let $G\subset \GL_{3}(C)$ be the Galois group of $Ly=0$.
 
If the Riccati  equation  attached to $L$ or the similar equation attached to $L^{\vee}$  has a solution then $G$ is reducible. Otherwise, it is irreducible.
\medskip

When it is the reducible case, $L$ or  $L^{\vee}$ has a right factor of order $1$ denoted by $\phi-\alpha$. Consider the case where $L$  has a right factor of order $1$, the other situation is similar. Therefore, up to an isomorphism, the Galois group $G$ is the one of the system 
$$\phi (Y)= \left(\begin{array}{c|c}
\alpha &  1 \hspace*{0.3cm} 0  \\
\hline
0 &  A_2 
\end{array}\right)Y \, . $$
We already know how to reduce the systems $[\alpha]$ and $[A_2]$ (order $1$ and $2$) and we denote respectively by $[\beta]$ and $[B_2]$ these reduced systems. We consider the system $[A]$ which is equivalent to this previous system with $A$ of the form  
$\begin{pmatrix}
\beta &\star \\ 
0 & B_2
\end{pmatrix}$. To reduce the system $[A]$ and compute its Galois group, which is $G$ up to an isomorphism, we proceed in two steps:
\begin{enumerate}
    \item With Theorem \ref{thm:reduc_blocdiag}, we reduce the bloc diagonal system $[D]$ where $D = \begin{pmatrix}
\beta &0 \\ 
0 & B_2
\end{pmatrix}$ and we find an associated reduction  matrix denoted by $T'$.
\item We reduce the system $[B]$ where $B:=\phi(T')A T'^{-1}$. Doing this, we introduce some linear equations and we know which is the group $G$ if we know that there exists a solution or not of these equations (see equations \eqref{eq:eqverif}, \eqref{eqaverifier}, \eqref{eqaverifierbis}, \eqref{eq:eqverif3}) 
\end{enumerate}

\medskip

When it is not the reducible case, we have to distinguish between the imprimitive case and the primitive case. Let $A:=A_L$. We know that it is imprimitive if and only if the difference Galois group of $\phi^3 Y=A_{[3]}Y$ is diagonal. We use the reducible case (with $\phi$ replaced by $\phi^3$) to check this property.  

\medskip

Finally,  when it is irreducible and primitive, we have to distinguish between $D(G)=\mathrm{SO}_3 (C)$ and  $D(G)=\mathrm{SL}_3 (C)$. We have $D(G)=\mathrm{SO}_3 (C)$, if and only if there is a symmetric solution over $\overline{\mathbf{k}}^*$ of the linear difference equation $A XA^t =\det(A)^{2/3}\phi(X)$.  

Combining the facts proved in Examples \ref{ex1},  \ref{ex2},  \ref{ex3}, and  \ref{ex4}, we then find the Galois group of \eqref{eq0} over  $\C(z^{1/*})$:

\begin{thm}\label{thm2}
For all $t\neq 0$, the difference Galois group of \eqref{eq0} over  $\C(z^{1/*})$ is $\mathrm{GL}_3(\C)$.
\end{thm}
