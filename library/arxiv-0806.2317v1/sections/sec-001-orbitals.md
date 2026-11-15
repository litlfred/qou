---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-001-orbitals
section_title: "Orbitals"
section_number: null
pages: 3-5
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.955
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:orbitals}

In this section we describe the orbits of pairs of elements of $\gras{m}{n}$ under the action of $U(n)$. 

First, we claim that $\gras{m}{n}$ can be identified with a factor group of the unitary group, $\nobreak{U(n)/(U(m) \times U(n-m))}$. For, consider the first $m$ columns of a matrix of $U(n)$ as the basis for a subspace $a$ of dimension $m$ in $\cx^n$, letting the last $n-m$ columns be a basis for $a^{\perp}$. Then $a$ is invariant under the action of $U(m)$ on the first $m$ columns, while $a^{\perp}$ is invariant under $U(n-m)$. 

As a result of this factor group, $U(n)$ acts on $\gras{m}{n}$ as follows: if $U$ is in $U(n)$ and $P_a$ is the projection matrix for $a \in \gras{m}{n}$, then 
\[
U: P_a \mapsto UP_aU^*.
\]
This action is an isometry, in that it preserves the trace inner product on $\gras{m}{n}$. Unlike the complex unit sphere, however, $U(n)$ is not \defn{$2$-homogeneous} on $\gras{m}{n}$: $U(n)$ does not act transitively on pairs of subspaces with the same distance. In other words, the fact that $\tr(P_aP_b) = \tr(P_cP_d)$ does not imply that there is a unitary matrix mapping $a$ to $c$ and $b$ to $d$. In order to use zonal polynomials, we need to understand the orbits of pairs in $\gras{m}{n}$ under this isometry group, which requires principal angles. 

Given $a$ and $b$ in $\gras{m}{n}$, the \defn{principal angles} $\th_1,\ldots,\th_m$ between $a$ and $b$ are defined as follows: firstly, $\th_1$ is the largest angle that occurs between any two unit vectors $a_1 \in a$ and $b_1 \in b$:
\[
\th_1 := \min_{\substack{a_1 \in a\\b_1 \in b}} \; \arccos \abs{a_1^*b_1}.
\]
Secondly, $\th_2$ is the largest angle that occurs between any two unit vectors $a_2 \in a \cap a_1^\perp$ and $b_2 \in b \cap b_1^\perp$. Similarly define $\th_3,\ldots,\th_m$. These principle angles are closely related to the eigenvalues of $P_aP_b$: the first $m$ eigenvalues of $P_aP_b$ are $\{\cos^2 \th_1,\ldots,\cos^2\th_m\}$. Because of this correspondence, for the remainder of this paper we simply refer to the eigenvalues $y_i := \cos^2 \th_i$ (rather than the values $\th_i$) as the principal angles between $a$ and $b$. Note that $n-m$ of the eigenvalues of $P_aP_b$ are zero, so we need only consider the first $m$ eigenvalues. Conway, Hardin, and Sloane \cite{chs} accredit the following lemma to Wong \cite[Theorem 2]{wong}.

\begin{comment}
Let $M_a$ be the  $n \times m$ matrix with columns $[a_1, \ldots, a_m]$ and $M_b := [b_1,\ldots,b_m]$, where $\cos \th_i = \abs{a_i^*b_i}$. then $M_a^*M_b$ is a diagonal matrix with diagonal $(a_1^*b_1,\ldots,a_n^*b_n)$. Likewise, $M_b^*M_a$ is diagonal with entries $(b_1^*b_1,\ldots,b_n^*b_a)$, and so $M_a^*M_bM_b^*M_a$ is diagonal with diagonal entries $(\cos^2 \th_1,\ldots, \cos^2 \th_m)$. However, $M_a^*M_bM_b^*M_a$ and $M_aM_a^*M_bM_b^* = P_aP_b$ have the same nonzero eigenvalues, so the first $m$ eigenvalues of $P_aP_b$ are $\{\cos^2 \th_1,\ldots, \cos^2 \th_m\}$. \qed
\end{comment}

\begin{lemma}
The principal angles characterize the orbits of pairs of subspaces under $U(n)$.
\end{lemma}

\begin{proof}
Suppose $U \in U(n)$ maps projection matrices $P_a$ and $P_b$ to $P_c$ and $P_d$ respectively. Then by similarity, the eigenvalues of 
\[
P_cP_d = (UP_aU^*)(UP_bU^*) = UP_aP_bU^*
\]
are the same as the eigenvalues of $P_aP_b$.

Conversely, we show that if $P_aP_b$ and $P_cP_d$ have the same eigenvalues, then some unitary matrix $U$ maps $a$ to $c$ and $b$ to $d$. We do this by unitarily mapping $a$ and $b$ into a canonical form that depends only on the eigenvalues of $P_aP_b$. 

Let $M_a$ be an $n \times m$ matrix whose columns $[a_1, \ldots, a_m]$ are an orthonormal basis for $a$, so that $M_aM_a^* = P_a$ and $M_a^*M_a = I$. Similarly define $M_b = [b_1, \ldots, b_m]$ for $b$. Suppose $M_a^*M_b$ has singular value decomposition $UDV^*$, where $U$ and $V$ are $m \times m$ unitary and $D$ is $m \times m$ diagonal. Then $(M_aU)^*(M_bV) = D$. Since the columns of $M_aU$ are another orthonormal basis for $a$, without loss of generality we replace $M_a$ by $M_aU$ and likewise replace $M_b$ with $M_bV$. In other words, we may assume without loss of generality that $M_a^*M_b = D$, where $D$ is a diagonal matrix of singular values. 

Next, define the columns of $N_a = [a_{m+1},\ldots,a_n]$ to be any orthonormal basis for $a^\perp$, so that $N_aN_a^* = I-P_a$ and $N_a^*N_a = I$. Further assume that $N_a^*M_b = QR$, where $Q$ is $(n-m) \times (n-m)$ unitary and $R$ is $(n-m) \times m$ upper triangular (the $QR$-decomposition of $N_a^*M_b$). Then $Q^*N_a^*M_b = R$, and the columns of $N_aQ$ form another orthonormal basis for $a^\perp$. Replacing $N_a$ by $N_aQ$, we may assume without loss of generality that $N_a^*M_b$ is upper triangular. 

Finally, let $U_a := \Big(\begin{smallmatrix}M_a^* \\ N_a^*\end{smallmatrix}\Big)$; this is an $n \times n$ unitary matrix. Then
\[
U_aM_a = \left(\begin{matrix}I_m \\ 0 \end{matrix}\right); \quad U_aM_b  = \left(\begin{matrix}D \\ R \end{matrix}\right).
\]
If $P_aP_b$ has eigenvalues $\cos^2 \th_i$, then $M_a^*M_b = D$ has singular values $\cos \th_i$. Moreover, since $U_aM_b$ has orthonormal columns, it follows that $R$ also has orthogonal columns. We may therefore assume that $R$ is not just the upper triangular but diagonal, with diagonal entries $\sin \th_i$. Thus $U_a$ is a unitary matrix which maps $M_a$ and $M_b$ into the form
\[
M_a \mapsto \left(\begin{matrix}I_m \\ 0 \end{matrix}\right), \quad M_b \mapsto \left(\begin{matrix}
\cos \th_1 & & \\
& \ddots & \\
& & \cos \th_m \\
\sin \th_1 & & \\
& \ddots & \\
& & \sin \th_m \\
& 0 & \\
\end{matrix}\right).
\]
Since any pair $(M_a,M_b)$ with principal angles $\cos^2 \th_i$ can be mapped to this canonical form, it follows that the eigenvalues of $P_aP_b$ characterize the orbits of pairs $(a,b)$ under the unitary group. \qed
\end{proof}
