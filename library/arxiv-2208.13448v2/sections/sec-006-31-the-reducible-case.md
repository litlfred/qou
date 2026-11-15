---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-006-31-the-reducible-case
section_title: "The reducible case"
section_number: 3.1
pages: 9-11
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.941
---
\label{sec:reducible case}

Let us treat the case where the Galois group $G$ is reducible.  By Lemma  \ref{lem1},  $G$ is reducible if and only if there exist $T\in \mathrm{GL}_n(\k)$,  $A_1\in \mathrm{GL}_m(\k)$, $m<n$,  and $A_2,A_3$ matrices of convenient size,    such that 
$$\phi(T)AT^{-1}=\left(\begin{array}{cc}
A_1 &  A_2\\
0 & A_3  
\end{array}\right).
$$

The strategy of reduction will follow the one given in the differential setting in \cite[Section 5]{dreyfus2019computing}.   Let us assume that the bloc diagonal system $[D]$, where $D:=\begin{pmatrix}
A_1&0 \\ 
0 &A_3 
\end{pmatrix}$, is in reduced form and let us see how to reduce $[A]$.  In general, $[D]$ is not in reduced form and we have to reduce the bloc diagonal system with a bloc diagonal gauge transformation. 
For small orders, we will see how to do this in practice but we want to emphasize the fact that reducing the bloc diagonal system is a hard task in general.   We denote by $\Gdiag$ the Galois group of $[D]$.



\begin{lem}
 \label{lem:Gauge transfo reduc}
 Let $B$ be a matrix of the form $\begin{pmatrix}
 A_1 & A_2 \\ 0 & A_3
 \end{pmatrix}$ where $D:= \begin{pmatrix}
 A_1 & 0 \\ 0 & A_3
 \end{pmatrix}$ is such that the system $[D]$ is in reduced form. 
A matrix $T\in \GL_n(\k)$ such that $\left[\phi(T)BT^{-1}\right]$ is reduced can be found of the form $T=\begin{pmatrix}
\mathrm{Id}_m & \star \\ 
0 & \mathrm{Id}_{n-m}\\
\end{pmatrix}$. 
\end{lem}

\begin{proof}
It is the same kind of results as  \cite[Theorem 2.4]{dreyfus2019computing} adapted to this difference context.  We denote by $G$ (respectively by $\Gdiag$) the Galois group of $[B]$  (respectively of $[D]$). Let $H$ be the smallest algebraic group of upper bloc triangular matrices such that $B\in H(\k)$. It is an algebraic group whose elements are of the form $\begin{pmatrix} \mathscr{H}_1 & \mathscr{H}_2 \\ 0 & \mathscr{H}_3 \end{pmatrix}$. We denote by $\Hdiag$ the group whose matrices are of the form $\begin{pmatrix} \mathscr{H}_1 & 0\\ 0 & \mathscr{H}_3 \end{pmatrix} $ where $\begin{pmatrix} \mathscr{H}_1 & \mathscr{H}_2\\ 0 & \mathscr{H}_3 \end{pmatrix}\in H $ for a matrix~$\mathscr{H}_2$, it is a block diagonal algebraic group.
Let $\Hunip$ (respectively $\Gunip$) be the subgroup of $H$ (respectively $G$) whose elements are of the form $\begin{pmatrix}
\mathrm{Id}_m & \star \\ 0 & \mathrm{Id}_{n-m}
\end{pmatrix}$. We have $\Hdiag\sim H/\Hunip$. 
Let us prove that the group $\Hdiag$ is the smallest algebraic group 
such that $D\in \Hdiag (\k)$. Indeed, considering the projection morphism $ \pi : H \rightarrow  \Hdiag$, where we identify $H/\Hunip$ and $\Hdiag$, if there exists an algebraic group $\widetilde{\Hdiag}\subsetneq \Hdiag$ such that $D\in \widetilde{\Hdiag}(\k)$, then the algebraic group  $\widetilde{H}:=\pi^{-1}(\widetilde{\Hdiag})\subsetneq H$ is such that $B\in \widetilde{H}(\k)$, which contradicts the minimality of $H$.
  Since $[D]$ is in reduced form,   we have  $\Gdiag= \Hdiag$.  
Let $R = \begin{pmatrix} R_1 & R_2 \\ 0 & R_3 \end{pmatrix}\in H(\k)$ be such that the system $\left[\phi(R)BR^{-1}\right]$ is in reduced form. Let $R_{\mathcal{D}} :=\begin{pmatrix} R_1 & 0 \\ 0 & R_3 \end{pmatrix} \in \Hdiag(\k)=\Gdiag(\k)$.   

Since $\Gdiag\sim G/\Gunip$, there exists $Q_2$, such that $Q:= \begin{pmatrix}
R_1 & Q_2 \\ 0 & R_3
\end{pmatrix}\in G(\k)$. Therefore $Q^{-1} = \begin{pmatrix}
R_1^{-1} &\star \\ 0 & R_3^{-1}
\end{pmatrix}\in G(\k)$. A gauge transformation of $\phi(R)BR^{-1}\in G(\k)$ by the matrix  $Q^{-1}\in G(\k)$ gives an element of $G(\k)$. Hence $\left[\phi(T)BT^{-1}\right]$ is in reduced form where $T:= Q^{-1}R = \begin{pmatrix}
\mathrm{Id}_m & \star \\ 0 & \mathrm{Id}_{n-m}
\end{pmatrix}$.
\end{proof}

\begin{rem}\label{rem1}
As in \cite[Section 5]{dreyfus2019computing},  we may also consider the case where the system has more than two blocs.   More precisely, consider a bloc triangular system $[A]$, where  $$A=\left(\begin{array}{cccc}
A_1 &  A_{1,2}&\dots  &\\
 & A_2 &   A_{2,3}\\
&&\ddots& \\
0&&&A_k
\end{array}\right).$$
Let us assume that the bloc diagonal system $[D]$, with $D=\mathrm{Diag}(A_1,\dots, A_k)$, is in reduced form.   Then, the proof of Lemma \ref{lem:Gauge transfo reduc} may be adapted in that context and we find a gauge transformation $T=\left(\begin{array}{cccc}
\mathrm{Id} &  \star &\dots  & \star\\
0 & \mathrm{Id} & \ddots & \vdots \\
&&\ddots&  \star  \\
&&&\mathrm{Id}
\end{array}\right)\in \GL_n (\mathbf{k})$ such that $[\phi(T)A T^{-1}]$ is in reduced form.  
\end{rem}
