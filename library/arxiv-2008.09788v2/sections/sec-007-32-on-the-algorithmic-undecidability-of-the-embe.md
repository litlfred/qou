---
doc_id: arxiv-2008.09788v2
doc_title: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY"
section_id: sec-007-32-on-the-algorithmic-undecidability-of-the-embe
section_title: "On the algorithmic undecidability of the embeddability problem for algebraic varieties over a field of characteristic zero"
section_number: 3.2
pages: 25-28
source_pdf: 2008.09788v2.pdf
source_sha256: 460f4f5432cb1f0c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.947
doc_brief: "NONSTANDARD ANALYSIS, DEFORMATION QUANTIZATION AND SOME LOGICAL ASPECTS OF (NON)COMMUTATIVE ALGEBRAIC GEOMETRY — This paper surveys results related to well-known works of B. Plotkin and V."
---
\label{sec32}


\subsubsection{\bf The Case of Real Numbers}\label{sec-real}
By a \textit{Matiyasevich family of polynomials} we mean a family of polynomials
$$Q(\sigma_1,\dots,\sigma_{\tau},x_1,\dots,x_s)$$
for which the existence of a solution for a given set of parameters of the polynomial is undecidable. As was established in \cite{Mat93}, such a polynomial exists.

Consider the affine space of dimension $5d+1$. We denote coordinates in this space by $X_i, Y_i, Z_i, U_i, W_i, 1\leq i\leq d$, and $T$. Consider the variety $B_{(d)}$ given by the following system of generators and relations:


\begin{equation}\label{sym-1}
\left\{\begin{array}{l}
X_{i}^{2}-\left(T^{2}-1\right) Y_{i}^{2}=1, \\
Y_{i}-(T-1) Z_{i}=V_{i}, \\
V_{i} U_{i}=1,
\end{array}\right.
\end{equation}

where $1\leq i\leq d$. For fixed $i$, the admissible values of the coordinates $X_i, Y_i, Z_i, U_i$, and $W_i$ are determined by the same value of $T$. Consider the ``short'' subsystem

\begin{equation}\label{sym-2}
\left\{\begin{array}{l}
X^{2}-\left(T^{2}-1\right) Y^{2}=1, \\
Y-(T-1) Z=V, \\
V U=1,
\end{array}\right.
\end{equation}


\begin{lem}
The following assertions hold for every solution of system (\ref{sym-2}):
\begin{enumerate}
    \item[1)] $U$ and $V$ are nonzero constants in $\mathbb{F}[t]$ $(\deg U=\deg V=0);$
    \item[2)] either $T=\pm 1$ and $X=\pm 1$ or
    $$Y=\sum_{k=0}^{[N / 2]}\left(\begin{array}{c}N \\2 k+1 \end{array}\right)\left(T^{2}-1\right)^{k} T^{N-1-2 k}$$
    for some integer $N$.
\end{enumerate}

\end{lem}

Let $R$ denote a root of the equation $R^2=T^2-1$ such that $R$ belongs to the algebraic extension $\mathbb{F}[t]$. Then the element $(T+R)^n$ can be uniquely represented in the form $X_n+R Y_n$, where $X_n$ and $Y_n$ are polynomials in $\mathbb{F}[t]$. All solutions of the equation

\begin{equation}
    X^2-(T^2-1)Y^2=1
\end{equation}
are of the form $X=\pm X_n$, $Y=\pm Y_n$ (see \cite{Den78}).

The structure of this set depends on $T$. In the case $T=\pm 1$, the first equation of the system imposes no conditions at all on $Y$. In turn, the other equation implies $Y=(T-1)Z+V$. For every choice of $V\in \mathbb{F}\setminus \{0\}$ and $Z\in \mathbb{F}[t]$, the corresponding solution exists and is unique.

\begin{lem}
If $\deg T>0$, then $V=Y \mathrm{mod} (T-1)=N$ for an integer $N$ and $Z=(Y-N)/(T-1).$ If $T=\text{const} \neq \pm 1$, then $Y$ and $Z$ are constants in $\mathbb{F}[t]$.
\end{lem}

Thus, the following three cases are possible:

\begin{enumerate}
    \item[(1)] for $\deg T>0$, to every set of integers $N_i$ there correspond polynomial solutions $Y_i$ and $X_i$ determined up to sign, as well as the constants $V_i=N_i$ and $U_i=1/V_i$, and $Z_i=(Y_i-V_i)/(T-1);$
    \item[(2)] for $\deg T=0$ and $T\neq \pm1$, there are constant solutions for $Y_i$ chosen from a given sequence; the values $X_i,Z_i,V_i$ and $U_i$ are also constants, and they are determined by the chosen values of $Y_i$;
    \item[(3)] for $T=\pm 1$, we obtain $X_i=\pm1$; for arbitrarily chosen constants $V_i$ and polynomials $Z_i$, we set $U_1=1/V_i$ and $Y_i=(T-1)Z_i+V_i.$
\end{enumerate}

So far, these considerations are valid for an arbitrary ground field $\mathbb{F}$ of characteristic zero. In the case $\mathbb{F}=\mathbb{R}$, we introduce a new coordinate $S$ by completing the main system of equations by the equation
\begin{equation}\label{sym-4}
    T=S^2+2,
\end{equation}
which ensures the impossibility of $T=\pm 1$. All common solutions of systems (\ref{sym-1}) and (\ref{sym-4}) either are constants (if $\deg T=0$, $T\neq\pm 1$) or correspond to some set of integer parameters $(N_1,\dots,N_d)$. We refer to solutions of the first kind as ``bad'' and to those of the second kind as ``good''.

Consider a Matiyasevich family of polynomials $Q(\sigma_1,\dots,\sigma_{\tau},x_1,\dots,x_s)$. Let $d\leq s$. Then, adding the new equation $Q(\sigma,V_1,\dots,V_s)=0$ to systems (\ref{sym-1}) and (\ref{sym-4}), we obtain a system defining a new variety. We denote this variety by $\mathscr{B}'_{(d),\sigma}$.

If $Q = 0$ has no integer solutions, then the original system has no good solutions. In this case, the variety $\mathscr{B}'_{(d),\sigma}$ is zero-dimensional, and there are no embeddings of $A$ in $\mathscr{B}'_{(d),\sigma}$.

Otherwise, for every solution $N_1,\dots,N_s$, we can explicitly construct functions $Y_i(S), X_i(S)$, and $Z_i(S)$ which are solutions. They define an embedding of the line in the variety $\mathscr{B}'_{(d),\sigma}$.

Since the existence of integer solutions for $Q$ is undecidable, it follows that so is the embeddability of $A$ in $\mathscr{B}'_{(d),\sigma}$ (in particular, in $\mathscr{B}'_{(s),\sigma}$). Here the input data is the equations defining $\mathscr{B}'_{(d),\sigma}$. We have proved the following theorem.

\begin{thm}
The problem of the embeddability of the affine line (and, therefore, the general embedding problem for an arbitrary variety) over $\mathbb{R}$ in an arbitrary algebraic variety $\mathscr{B}$ (defined by generators and relations) is undecidable.
\end{thm}


\subsubsection{\bf The Complex Case}\label{cc}
In this case, the situation is more complicated: it is hard to eliminate the case in which $T=\pm 1$ and $X_i=\pm 1$, since no constraints on $Y_i$ arise in this case. Therefore, we consider the problem of the embeddability of an affine space $A^m$ in a given variety $\mathscr{B}$ and construct a class of varieties such that it is impossible to decide whether a desired embedding exists from the defining relations for representatives of this class (for a certain suitable integer $m$). We define the coordinate ring of the variety $\mathscr{B}_{(d,e)}$ by the following system of generators and relations:

\begin{equation}\label{sym-5}
\left\{\begin{array}{l}
X_{i j}^{2}-\left(T_{j}^{2}-1\right) Y_{i j}^{2}=1, \\
Y_{i j}-\left(T_{j}-1\right) Z_{i j}=V_{i j}, \\
V_{i j} U_{i j}=1, \\
T_{j+1}=\prod_{k=1}^{j}\left(\left(T_{k}^{2}-1\right) W_{k}\right) W_{j+1},
\end{array}\right.
\end{equation}
where $1\leq i\leq d$ and $1\leq j\leq e$. In fact, we compose a system of many ``clones'' of the main system of the previous subsection and augment it by the ``linking'' relations between the parameters $T_j$. Let us study the solutions of the resulting system in $\mathbb{C}[t]$.

The relations for $X_{ij}, Y_{ij}, Z_{ij}, U_{ij}$, and $V_{ij}$ for each fixed $T_j$ are similar to those considered above. For a fixed set of $T_j$, the set of solutions is the direct sum of the sets $\mathscr{B}_{(d)}$, which have already been studied above.

As above, for each $j$, the following cases can occur: $T_j=\pm 1$ and $\deg T_j=0$; $T_j\neq\pm 1$, and $\deg T_j>0$.

The case most important from the point of view of ``elimination'' is the case where $T_{\hat{j}}=\pm 1$ for some $\hat{j}$. In this case, $T^2_{\hat{j}}-1=0$, and for all $j<\hat{j}$, we obtain
$$T_j=\prod_{k=1}^{j-1}((T_k^2-1)W_k)W_j.$$

\begin{lem}\label{lem-3}
If $T_N=C_N\neq 0$ for some $N$, then all $W_k$ with $k\leq N$ and all $T_k$ with $k\leq N-1$ are constants.
\end{lem}

By Lemma \ref{lem-3}, we have $T_j=C_j$ for $j<\hat{j}$. Here $C_j\neq\pm 1$ (otherwise $C_{j+1}=0$). Thus, if $T_{\hat{j}}=\pm 1$ for some $\hat{j}$, then the corresponding component has dimension $d$. However, in this case, all other components are zero-dimensional, and the total dimension of the variety does not exceed $d$.

In the second case, we have $T_{\hat{j}}=C_{\hat{j}}\neq \pm 1$ for some $\hat{j}$. The corresponding component of the variety has dimension 0. Moreover, Lemma \ref{lem-3} implies $T_j=C_j$ for $j<\hat{j}$. The corresponding $\hat{j}-1$ components of the variety are zero-dimensional as well.

The case $\deg T_j>0$ was considered in Sec. \ref{sec-real}. Each component of the variety is parametrized by a set of integers $N_{1j},\dots,N_{dj}$,for which the corresponding solutions for $X_{ij}, Y_{ij}, Z_{ij}, U_{ij}$, and $V_{ij}$ are constructed explicitly. The corresponding component has dimension 1.

Consider a Matiyasevich family of polynomials $Q(\sigma_1,\dots,\sigma_{\tau},x_1,\dots,x_s)$. The solvability problem of the Diophantine equation $Q(\sigma_1,\dots,\sigma_{\tau},V_{1j},\dots,V_{sj})=0$ is algorithmically undecidable. Let $d\leq s$. Adding the new equations $Q(\sigma,V_{i1},\dots,V_{is})=0$ to system \ref{sym-5}, we obtain a system defining a new variety. We denote it by $\mathscr{B}'_{(d,e),\sigma}$.

If $Q=0$ has no integer solutions, then the original system has no solutions for which $\deg T_0>0$. In this case, the possible solutions correspond either to the case where $T_j=\pm 1$ for some $j$ (and the set of solutions has dimension $d$) or to the case $T_j=C_j\neq\pm 1$. In the latter case, assuming that $j$ is the maximum index for which $T_j=C_j\neq \pm 1$, we see that all the succeeding $e-j$ components are one-dimensional and the total dimension of the set equals precisely $e-j\leq e-1$. Setting $e=s$ and $d=s-1$, we obtain

$$\dim \mathscr{B}'_{(d,e)}\leq \max (e-1,d)=s-1<s.$$

Obviously, in this case, for $m\geq s$, there is no embedding of $\mathscr{A}=A^m$ in $\mathscr{B}'_{(d,e),\sigma}=\mathscr{B}'_{(s-1,s),\sigma}.$ In particular, $A^s$ cannot be embedded in $\mathscr{B}'_{(s-1,s),\sigma}$.

If $Q$ has integer solutions, then, for every such solution $N_1,\dots,N_s$, we can explicitly construct functions $Y_{ij}(T), X_{ij}(T)$, and $Z_{ij}(T)$ which are solutions. These functions define an embedding of $A=A^s$ in the variety $\mathscr{B}'_{(d,e),\sigma}$.

Since the existence of integer solutions for $Q$ is undecidable, it follows that the embeddability of $A^s$ in $\mathscr{B}'_{(s-1,s),\sigma}$ is undecidable as well (the input data is the equations defining $\mathscr{B}'_{(s-1,s),\sigma}$). The proof is valid for any field $K$ of of characteristic zero. The following theorem holds.

\begin{thm}
There is a positive integer s for which the embeddability of an affine space $A^s$ over $K$ in an arbitrary algebraic variety $\mathscr{B}$ (defined by generators and relations) is undecidable. Thus, the general embeddability problem for an arbitrary algebraic variety is undecidable as well.
\end{thm}
