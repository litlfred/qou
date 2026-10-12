---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-008-33-the-primitive-case
section_title: "The primitive case"
section_number: 3.3
pages: 19-20
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.956
---
In this section, we assume that $G$ is irreducible, primitive, and $n$ is prime. We want to prove that the same holds for $G^0$ and $D(G^0)$ where $D(G^0)$ denotes the derived group of $G^0$. Note that $G^0$ is a connected normal subgroup of $G$ and $D(G^0)$ is a connected normal subgroup of $G^0$. 

First, we recall the following result given in \cite[Lemma 4.2]{adamczewski2021hypertranscendence}.

\begin{lem}
\label{lem:connected+irred}
    If $K\subset \GL_n(C)$ is a connected and irreducible algebraic group, then $K$ is also primitive. 
\end{lem}


\begin{lem}
\label{lem:irred_primitive_G^0}
Let $n$ be a prime number. If $H\subset\GL_n(C)$ is an irreducible and primitive group, then the derived subgroup of $H$, denoted by $D(H)$, is not composed only of dilatations.
\end{lem}

\begin{proof}
By contradiction, assume that $D(H)$ is composed only of dilatations. In this case, for all $\mathscr{G},\mathscr{H}\in H$, there exists $\alpha\in C^*$ such that $\mathscr{G}\mathscr{H}\mathscr{G}^{-1}\mathscr{H}^{-1} = \alpha \textnormal{Id}_n$, that is  $\mathscr{G}\mathscr{H}=\alpha \mathscr{H}\mathscr{G}$. The group $H$ is irreducible so there exists $\mathscr{H}_0\in H$ having an eigenspace $W$ of maximal dimension $\nu<n$, otherwise $H$ would be composed of dilatations contradicting its irreducibility. Let $V$ be the direct sum of the eigenspaces of $\mathscr{H}_0$ of dimension $\nu$. From the previous equality and the fact that $\mathscr{H}_0(W)=W$, we obtain that 
\begin{equation}
    \label{eq:permut_eigenspace}
    \forall \mathscr{G}\in H,\hspace{0.15cm} \mathscr{H}_0(\mathscr{G}(W))=\mathscr{G}(W)\, .
\end{equation}
 Thus, $\mathscr{G}(W)$ is also  an eigenspace of $\mathscr{H}_0$  of dimension $\nu$ for all $\mathscr{G}\in H$ so $H(W)\subset V$. Therefore, $H(V)\subset V$ (in fact, taking the dimension, it is an equality of vector spaces) which implies that $V=C^n$ by irreducibility of $H$. Hence  $\nu$ divides $n$. Since $n$ is a prime number and $\nu<n$, we have $\nu=1$. This means that $\mathscr{H}_0$ is a diagonal matrix with distinct eigenvalues and we denote by $V_1,\ldots,V_n$ its eigenspaces. However, from \eqref{eq:permut_eigenspace} with $W:=V_1$, we obtain that every $\mathscr{G}\in H$ induces a permutation between the $V_i$, which contradicts the fact that $H$ is primitive.
\end{proof}


\begin{prop}\label{prop4}
    Assume that $n$ is prime and $G \subset \mathrm{GL}_n (C)$ is an irreducible and primitive group. Then, the same holds for $G^0$ and $D(G^0)$ and we may write $G^0=Z(G^0).D(G^0)$ where $Z(G^0)$ denotes the center of $G^0$.
\end{prop}

\begin{proof}
We recall that $G^0$ is a connected normal subgroup of $G$ and $D(G^0)$ is a connected normal subgroup of $G^0$.

From Lemma \ref{lem:irred_primitive_G} (with $H:=G^0$), $G^0$ is not composed only of dilatations. Thus, by Proposition \ref{prop:irred_primitive} (with $H:=G$ and $K:=G^0$), $G^0$ is irreducible. Using Lemma \ref{lem:connected+irred}, $G^0$ is also primitive. 
Then, the irreducibility of $D(G^0)$ follows from Lemma \ref{lem:irred_primitive_G^0} (with $H:=G^0$) and Proposition \ref{prop:irred_primitive} (with $H:=G^0$ and $K:=D(G^0)$). Thanks to Lemma \ref{lem:connected+irred}, $D(G^0)$ is also primitive.

By \cite[Corollary 8.1.6]{springer1998linear}, any connected algebraic group $H$ satisfies $H\sim Z(H). D(H)$, which proves that $G^0=Z(G^0).D(G^0)$. 
\end{proof}
