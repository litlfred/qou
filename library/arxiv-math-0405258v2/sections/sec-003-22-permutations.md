---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-003-22-permutations
section_title: "Permutations"
section_number: 2.2
pages: 4-5
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.96
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
We will denote the set of permutations on $n$ elements by $S_n$.  We
will quite often use the cycle notation for such permutations, i.e.,
$\pi=(i_1,i_2,\dots,i_r)$ is a cycle which sends $i_k$ to $i_{k+1}$
($k=1,\dots,r$), where $i_{r+1}=i_1$.


\subsubsection{Length function}

For a partition $\pi\in S_n$ we denote by $\#(\pi)$ the number of
cycles of $\pi$ and by $\vert\pi\vert$ the minimal number of
transpositions needed to write $\pi$ as a product of transpositions.
Note that one has
$$\vert\pi\vert+\#(\pi)=n\qquad\text{for all $\pi\in S_n$}.$$


\subsubsection{Non-crossing permutations}

Let us denote by $\gamma_n\in S_n$ the cycle
$$\gamma_n=(1, 2 ,\dots, n).$$
For all $\pi\in S_n$ one has that
$$n - 1 \leq \vert\pi\vert+\vert\gamma_n\pi^{-1}\vert.$$
If we have equality then we call $\pi$ \emph{non-crossing},
see \cite{Biane97} for the basic properties of non-crossing
partitions. Note that this is equivalent to
$$\#(\pi)+\#(\gamma_n\pi^{-1})=n+1.$$ If $\pi$ is
non-crossing, then so are $\gamma_n\pi^{-1}$ and $\pi^{-1}\gamma_n$;
the latter is called the \emph{(Kreweras) complement} of $\pi$.

We will denote the set of non-crossing permutations in $S_n$ by
$NC(n)$. Note that such a non-crossing permutation can be identified
with a non-crossing partition, by forgetting the order on the
cycles. There is exactly one cyclic order on the blocks of a
non-crossing partition which makes it into a non-crossing
permutation.


\subsubsection{Annular non-crossing permutations}

Fix $m,n\in\NN$ and denote by $\gamma_{m,n}$ the product of the two
cycles
$$\gamma_{m,n}=(1, 2,\dots, m)(m+1, m+2,\dots, m+n).$$
More generally, we shall denote by $\gamma_{m_1,\dots,m_k}$ the
product of the corresponding $k$ cycles.

We call a $\pi\in S_{m+n}$ \emph{connected} if the pair $\pi$ and
$\gamma_{m,n}$ generates a transitive subgroup in $S_{m+n}$. A
connected permutation $\pi\in S_{m+n}$ always satisfies
\begin{equation}\label{annular-NC}
m + n \leq \vert\pi\vert+\vert\gamma_{m,n}\pi^{-1}\vert.
\end{equation}
If $\pi$ is connected and if we have equality in that equation then
we call $\pi$ \emph{annular non-crossing}. Note that with $\pi$ also
$\gamma_{m,n}\pi^{-1}$ is annular non-crossing. Again, we call the
latter the \emph{complement} of $\pi$. Of course, all the above
notations depend on the pair $(m,n)$; if we want to emphasize this
dependency we will also speak about $(m,n)$-connected permutations
and $(m,n)$-annular non-crossing permutations.

We will denote the set of $(m,n)$-annular non-crossing permutations
by $\SNC(m,n)$. Again one can go over to annular non-crossing
partitions by forgetting the cyclic orders on cycles; however, in
the annular case, the relation between non-crossing permutation and
non-crossing partition is not one-to-one. Since we will not use the
language of annular partitions in the present paper, this is of no
relevance here.

Annular non-crossing permutations and partitions were introduced in
\cite{MN}; there, many different characterizations---in particular,
the one (\ref{annular-NC}) above in terms of the length
function---were given.
