---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-004-23-a-triangle-inequality
section_title: "A triangle inequality"
section_number: 2.3
pages: 5-6
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.953
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
Let $\{A_1, \dots , A_k\}$ be a partition of $[n]$.
If, for $1\leq i\leq k$, $\pi_i$ is a permutation of the set $A_i$
we denote by $\pi_1\times \cdots\times \pi_k\in S_n$ the
concatenation of these permutations. We say that
$\pi=\pi_1\times\cdots\times \pi_k$ is a cycle decomposition if
additionally every factor $\pi_i$ is a cycle.

\begin{notation}
1) For $A\in\cP(n)$ we put $| A|:=n-\#(A)$ \\
2) For any $\pi \in S_n$ and any $\pi$-invariant $A\in\cP(n)$
we put
$$| (A,\pi) |:=2\vert A\vert-\vert\pi\vert.$$
\end{notation} 

\begin{lemma}\label{triangleinequality}
1 ) For all $A,B\in\cP(n)$ we have 
$$\vert A \vee B \vert\leq \vert A\vert+\vert B\vert$$
2) If $\pi$ and $\sigma$ are in $S_n$ and $A, B \in \cP(n)$ are
$\pi$ and $\sigma$ invariant respectively, then
$$\vert(A \vee B,\pi\sigma)\vert\leq \vert(A,\pi)\vert
+\vert(B,\sigma)\vert.$$
\end{lemma}

\begin{proof}
1) Each block of $B$ with $k$ points can glue together at
most $k$ blocks of $A$, thereby reducing the number of
blocks of $A$ by at most $k-1$. Thus $B$ can reduce by at
most $n-\#(B)$ the number of blocks of $A$. Hence the
difference between $\#(A)$ and $\#(A\vee B)$ cannot exceed $n-\#(B)$
and hence $$\#(A)-\#(A\vee B)\leq n-\#(B).$$ 
This is equivalent to our assertion.

2) We prove this, for fixed $\pi$ and $\sigma$ by induction
on $\vert A\vert+\vert B\vert$. The smallest possible
value of $\vert A\vert+\vert B\vert$ occurs when $\vert
A\vert=\vert\pi\vert$ and $\vert B\vert=\vert\sigma\vert$.
But then we have (since $A\vee B\geq \pi\sigma$)
$$2\vert A\vee B\vert-\vert\pi\sigma\vert
\leq \vert A\vee B\vert\leq \vert A\vert+\vert B\vert 
\eqno \textrm{by (1)}
$$
which is exactly our assertion for this case.
For the induction step note that we have just shown that
$$2\vert A\vee B\vert-\vert\pi\sigma\vert
\leq 2\vert A\vert - |\pi| + 2\vert B\vert - |\sigma| 
$$
when $|A| = |\pi|$ and $B| = |\sigma|$. Now one
only has to observe that if one increases $\vert A\vert$ (or
$\vert B\vert$) by 1 then $\vert A\vee B\vert$ can also
increase by at most 1. \end{proof}
