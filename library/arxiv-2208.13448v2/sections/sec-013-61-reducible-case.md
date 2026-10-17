---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-013-61-reducible-case
section_title: "Reducible case"
section_number: 6.1
pages: 22-23
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.878
latex_coverage_ratio: 0.657
---
We first decide whether $L$ has a right factor of order one.  This is the case if and only if $G$ is reducible.  Recall, see Lemma \ref{lem:eq left factor},  that it is equivalent to the existence of  a solution $\alpha$ of the Riccati equation $\phi(y)y+a_1y+a_0=0$. \par 
Assume first that $L$ is reducible and let us write $L=(\phi-\beta)(\phi-\alpha)$.  Then, $\alpha$ is a solution of the Riccati equation  $\phi(y)y+a_1y+a_0=0$, and $\beta$ is determined by $\alpha \beta=a_0$.  The difference equation is equivalent to $\phi(Y)=AY$ where $A=\left(\begin{array}{cc}
\alpha &  1\\
0 & \beta
\end{array}\right)
$. 
 We now follow the strategy of Section \ref{sec:reducible case}.  As in the diagonal case, we reduce the diagonal system $\phi(Y)=\left(\begin{array}{cc}
\alpha &  0\\
0 & \beta
\end{array}\right)Y
$ with a diagonal  matrix  $D$.  Let $B:=\phi(D)AD^{-1}$,  with $B=\left(\begin{array}{cc}
\alpha' &  \gamma'\\
0 & \beta'
\end{array}\right)$.   By \cite[Lemma 4.4]{hendriks1998algorithm}, either $[B]$ is already reduced, or a reduced form is $\left( \begin{array}{cc}
\alpha' &  0\\
0 & \beta'
\end{array}\right)$. 
We now have to decide if there exists $t\in \k$ such that $T=\left(\begin{array}{cc}
1 & t\\
0 & 1
\end{array}\right)$ satisfies $\phi(T)B=\left( \begin{array}{cc}
\alpha' &  0\\
0 & \beta'
\end{array}\right)T$.  Note that this is equivalent to 
$$  \gamma'+ \phi(t) \beta'= \alpha' t.$$
So we just have to decide if an equation of order $1$ has a solution $t$ in $\k$ or not.  
If such a $t$ exists,  then the reduction matrix is given by $TD$,  and a reduced form is $\left( \begin{array}{cc}
\alpha' &  0\\
0 & \beta'
\end{array}\right)$. Otherwise,  the reduction matrix is given by $D$ and a reduced form is $\left(\begin{array}{cc}
\alpha' &  \gamma'\\
0 & \beta'
\end{array}\right)$. \par
