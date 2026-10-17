---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-004-22-factorisations-of-difference-operators
section_title: "Factorisations of difference operators"
section_number: 2.2
pages: 6-7
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.896
latex_coverage_ratio: 0.966
---
\label{secfact}
In this subsection, we focus on the reducible difference operators and make the relation with the reducible Galois groups and the Riccati equation.  
Let $G$ be an algebraic subgroup of $\GL_{n}(C)$. We say that $G$ is reducible if there exists a non trivial vector subspace $V$ of $C^n$ such that for all $\sigma\in G$, $\sigma(V)\subset V$.  We say that $G$ is irreducible otherwise. \par 
The following lemma relates the irreducibility of the difference Galois group with the factorisation of the difference operator, see \cite[Lemma 4.4]{adamczewski2021hypertranscendence}.

\begin{lem}\label{lem1}
Let $G\subset \GL_{n}(C)$ be the difference Galois group of \eqref{eq:diffcesystembase}. Then,  $G$ is reducible with a nontrivial invariant space of dimension $0<m<n$, if and only if there exists $T\in \GL_n(\k)$,  $A_1\in \GL_m(\k)$, and $A_2,A_3$ matrices of convenient size,    such that 
$$\phi(T)AT^{-1}=\left(\begin{array}{cc}
A_1 &  A_2\\
0 & A_3  
\end{array}\right).
$$
If we consider the difference system $[A_L]$ attached to \eqref{eq:diffceeqbase}, then its difference Galois group is reducible with $A_1\in \GL_m(\k)$ if and only if
$L$ admits a nontrivial right factor of order $m$.
\end{lem}

Thus, to determine whether $G$ is irreducible or not, we have to determine whether the difference operator $L$ defined in \eqref{eq:diffceeqbase} admits a nontrivial right factor or not.  For right factors of order one, we have the following criterion. 

\begin{lem}[Lemma 2 in \cite{abramov2021rational}]\label{lem:eq left factor}
Let $L$ be the difference operator defined in \eqref{eq:diffceeqbase}.
The operator of order one $\phi-\alpha $ is a right factor of $L$ if and only if 
$$
\sum\limits_{i=0}^n a_i \prod\limits_{j=0}^{i-1} \phi^j(\alpha) = 0.
$$
\end{lem}

Although the above equation,  called the Riccati equation,   is nonlinear it might be solved in some situations we are going to describe later.\par 
When $L$ has order two,  it admits a nontrivial factor if and only if it admits a nontrivial right factor of order one. \par
When $L$ has order three, it admits a nontrivial factor if and only if it admits a nontrivial factor of order one.  The latter may be either a right or a left factor.  Let us see how we can pass from left factor to right factor.   
 We define the dual $M^{\vee} $ of an operator $M=\sum_{i=m}^{n}   a_{i}\phi^{i} \in\k\left< \phi,\phi^{-1}\right>$ by 
$$
M^{\vee} := \sum_{i=m}^{n}  \phi^{-i} (a_{i})
\phi^{-i}.$$ 
By linearity, if $M_1, M_2\in \k\left< \phi,\phi^{-1}\right>$, we can check that
$$
 (M_1 M_2)^{\vee}=M_2^{\vee}M_1^{\vee}. 
$$
Hence, an operator has a left factor of order one if and only if its dual has a right factor of order one.   So we will focus on right factors of order one. 

\begin{rem}
\label{rem:rightFactorOrder1}
Assume $n>1$ and that $L$ admits a right factor of order one so let us write $L$ as 
$\widetilde{L}(\phi-\alpha)$ where $\alpha\in \k$ and  $\widetilde{L}\in\k\left< \phi,\phi^{-1}\right>$ has order $n-1$.  
Let $y_1$ be a solution of $Ly=0$ such that $\phi(y_1)\neq \alpha y_1$ and let $y_2:=\phi(y_1)-\alpha y_1$. By construction $y_2\neq 0$ is a solution of $\widetilde{L}y=0$. If $Y:=\left(y_1,y_2,\ldots,\phi^{n-2}(y_2)\right)^t$ then $\phi(Y)=\widetilde{A}Y$ where
$$
\widetilde{A}:=\left(\begin{array}{c|cccc}
\alpha &  1 & 0 & \cdots & 0 \\
\hline
0 & & & &  \\
\vdots & & & A_{\widetilde{L}}&  \\
0 & & & & 
\end{array}\right)\, .
$$
Thus, the companion system associated with $Ly=0$ is equivalent to the system $[\widetilde{A}]$.  Furthermore, $A_{\widetilde{L}}$ is a companion matrix associated with $\widetilde{L}$.\end{rem}
