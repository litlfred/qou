---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-002-21-the-lattice-of-partitions
section_title: "The lattice of partitions"
section_number: 2.1
pages: 3-4
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.963
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
For natural numbers $m,n\in\NN$ with $m<n$, we denote by $[m,n]$ the
interval of natural numbers between $m$ and $n$, i.e.,
$$[m,n]:=\{m,m+1,m+2,\dots,n-1,n\}$$ and $[m] = [1, m]$.
For a matrix $A=(a_{ij})_{i,j=1}^N$, we denote by $\Tr$ the
unnormalized and by $\tr$ the normalized trace,
$$\Tr(A):=\sum_{i=1}^N a_{ii},\qquad \tr(A):=\frac 1N \Tr(A).$$

We say that $A=\{A_1,\dots,A_k\}$ is a partition of the set $[1,n]$ if
the subsets $A_i$ are disjoint, non-empty,
and their union is equal to $[1,n]$. We call $A_1,\dots,A_k$ the
blocks of the partition $A$. For a permutation $\pi\in S_n$ we say that
a partition $A$ is $\pi$-invariant if $\pi$ leaves invariant each
block $A_i$. Let $1_n$ denote that partition of $[n]$ with one
block and $\cP(n)$ denote the partitions of $[n]$. Given
positive integers $m$ and $n$ let $1_{m,n}$ be the partition of
$[m+n]$ with the two blocks: $[m]$ and $[m+1, m+n]$.

If $A=\{A_1,\dots,A_k\}$ and $B=\{B_1,\dots,B_l\}$ are partitions of
the same set, we say that $A\leq B$ if for every block $A_i$ there
exists some block $B_j$ such that $A_i\subseteq B_j$. For a pair of
partitions $A,B$ we denote by $A\vee B$ the smallest partition $C$
such that $A\leq C$ and $B\leq C$. 

If we are considering classical random variables on a probability
space, then we denote by $\EE$ the expectation with respect to
the corresponding probability measure and by $\kk_r$ the
corresponding classical cumulants (as multi-linear functionals
in $r$ arguments); in particular,
$$\kk_1 (a )=\EE(a) \qquad\text{and}\qquad
\kk_2(a_1,a_2)=\EE( a_1a_2)-\EE(a_1) \EE(a_2).$$

If $a_1, \dots , a_n$ are random variables and $C = \{C_1, \dots , C_k
\}$ is in $\cP(n)$ we let 
$$
\EE_C(a_1, \dots , a_n) = \prod_{i=1}^k
\EE \Big( \mathop{\textstyle\prod}_{j \in C_i} a_j \Big)
$$
On the lattice $\cP(n)$  moments to cumulants are related by
the M\"obius function: $\moeb$. In particular the $n^{th}$
cumulant $\kk_n$ is given by
$$
\kk_n(a_1, \dots , a_r) = 
\sum_{C \in \cP(n)} \moeb(C, 1_r) \EE_C(a_1, \dots , a_n)
$$
where $\moeb(C, 1_n) = (-1)^{k-1} (k-1)!$ and where $k$ is the
number of blocks of $C$. We shall need the following formula for
the second cumulant of the product of random variables, see for
example \cite[3.2]{lehner}.

\begin{equation}\label{leonov}
\kk_2(a_1 \cdots a_m, b_1 \cdots b_n) =
\mathop{\sum_{\tau \in \cP(m+n)}}_{\tau \vee 1_{m,n} = 1_n}
\kk_\tau ( a_1, \dots a_m, b_1, \dots , b_n)
\end{equation}
The sum is over all partitions of $[m+n]$ which have at least
one block which connects the two blocks of $1_{m,n}$.
