---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-008-51-row-and-column-arcs-order
section_title: "Row and column arcs order"
section_number: 5.1
pages: 8-9
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.96
---
\lbl{sub.rco}

Recall that we fix a generic planar projection $\K$ of an oriented knot with 
$r+1$ crossings.
We order the arcs of $\K$ so that they appear
in increasing order as we walk in the direction of the knot,
and we denote by $K$ the {\em long knot} obtained by breaking the
arc $a_{r+1}$. We also order the crossings of $K$
so that arc $a_i$ ends at the $i$th crossing, for $i=1,\dots,r$.


\begin{definition}
\lbl{def.perm}
\begin{enumerate}
\item
We define two permutations $S,T$ on the set of the arcs of $K$ as follows.
For arc $a_i$ of $K$ let $T(i)= T(i,1),\dots, T(i,k_i)$ 
( $S(i)= S(i,1),\dots, S(i,k_i)$ respectively)
be the block of arcs of $K$ terminating at (starting from) $a_i$ and 
ordered along
the orientation of $a_i$. Let $T$ ($S$) be the permutation of the arcs of $K$
defined by $T= T(1,1),\dots, T(1,k_1),\dots, T(r,k_r)$ 
($S= S(r,k_r),\dots, S(r,1),\dots, S(1,1)$).
\item
We define permutation $R$ of the arcs of $K$ from $T$ as follows:
if $a_i$ appears in $S$ {\it before} the block $S(i)$ then 
replace $T(i,1),\dots, T(i,k_i)$ by $T(i,k_i),\dots, T(i,1)$.
\item
Similarly we define permutation $C$ of the arcs of $K$ from $S$ as follows:
if $a_i$ appears in $S$ {\it after} the block $S(i)$ then 
replace $S(i,k_i),\dots, S(i,1)$ by $S(i,1),\dots, S(i,k_i)$.
\end{enumerate}
\end{definition}

\begin{definition}
\lbl{def.b'}
We define matrix $B'_K= (\gamma_{ij})$ to be obtained from $B_K$ by 
taking the rows in the $R$ order
and the columns in the $C$ order.
\end{definition}

We consider the commutation relations between the variables appearing in 
$B'_K$ as 
in the Definition \ref{def.com}. In particular, $B'_K$ is right-quantum.




\subsection{Flows on $G_K$ and monomials of $G_{B'_K}(m_1,\dots m_r)$}
\lbl{sub.mon}

We interpret each entry $\gamma_{ij}$ with no $z$ indeterminate as arc 
$(ij)$ of the arc-graph $G_K$.
Then each monomial in $G_{B'_K}(m_1,\dots, m_r)$ corresponds to a flow on 
$G_K$
with $indeg(i)= outdeg(i) = m_i, i=1,\dots, r$. If $f$ is such a flow, we 
denote by $G(f)$
the sum of all monomials of $\sum G_{B'_K}(m_1,\dots, m_r)$ corresponding to 
$f$. Summarizing we can write
 
\begin{observation}
\lbl{obs.fl}
$$
\sum_{m_1,\dots, m_r=0}^{\infty} G_{B'_K}(m_1,\dots, m_r)= \sum_f G(f).
$$
\end{observation}

We denote by $C(f)$ the canonical monomial of a product 
(in arbitrary order) of the entries of $B'_K$
corresponding to the edges of $G_K$, where the entry corresponding to 
each edge $e$
appears $f(e)$ times.

\begin{observation}
\lbl{obs.hr}
Let $C$ be a summand of $\prod_{i=1}^r(\sum_{j}\gamma_{ij}x_j)^{m_i}$, which 
contains $m_i$ indeterminates $x_i, i=1,\dots, r$ and contributes to $G(f)$.
For $1\leq v\leq r$ and $1\leq j\leq f(e^r_v)$ let $c(C,v,j)$ be the 
number of $\gamma_{e^b_v}$'s 
which need to be commuted through the $j$-th occurrence of $\gamma_{e^r_v}$ 
in order to get
$C(f)$ from $C$.
Then
$$
C= x_1^{m_1}x_2^{m_2}\dots x_r^{m_r}q^{-\rot(f)}C(f)q^{\exc(f)}
\prod_{v=1}^r\prod_{j=1}^{f(e^r_v)}
q^{\sign(v)c(C,v,j)}.
$$
\end{observation}
\begin{proof}
Let $X_{ij}= \gamma_{ij}x_j$. Hence $C$ is a summand of the coefficient of 
$x_1^{m_1}x_2^{m_2}\dots x_r^{m_r}$ in $\prod_{i=1}^r(\sum_{j}X_{ij})^{m_i}$. 
For each $j$ fixed the $\gamma_{ij}$'s appear ordered in $C$.
In each canonical monomial, the $\gamma_{ij}$'s appear ordered by the 
second coordinate, and then by the 
first coordinate. Hence, in order to get a canonical monomial times 
$x_1^{m_1}x_2^{m_2}\dots x_r^{m_r}$ from a summand of 
$\prod_{i=1}^r(\sum_{j}X_{ij})^{m_i}$,
we only need to commute $X_{ij}$'s so that they are ordered by the 
second coordinate.
This means: if $a_i$ appears in $S$ {\it before} ({\it after} respectively)
the block $S(i)$ 
then $a_i$ appears in $C$ {\it before} ({\it after} respectively )the 
block $S(i)$ 
BUT $a_{i-1}$ appears in $R$ {\it after} ({\it before} respectively) 
the block $T(i)$. Hence 
we need to commute 
\begin{enumerate}
\item[1.]
Each $X_{i-1,i}$ through each $X_{j-1,j}, j\in S(i)$ and
each $X_{k-1,i}$ through each  $X_{j-1,j}, j,k\in S(i), R(k)>R(j)$.
The commutation in $B'_K$ is such that we acquire each time $q^{\sign(j-1)}$.
Hence we acquire in total $q^{\exc(f)}$ since we recall that
$\exc(f)=\sum_{v} \sign(v) f(e^b_v) \sum_{e< e^r_v}f(e)$.
\item[2.]
Each $X_{k-1,i}$ through each  $X_{k-1,k}, k\in S(i)$. The commutation in 
$B'_K$ is such that 
we acquire  in total
$q^{\sign(k-1)(c(C,k-1,1)+\dots c(C,k-1,f(e^r_{k-1}))}$. 
\item[3.]
 The commutation in $B'_K$ is such that if $i<i', j<j'$ and $X_{i,j'},
X_{i',j}$ do not
appear in one of the previous two cases then $X_{i,j'},X_{i',j}= X_{i',j},
X_{i,j'}$.
\end{enumerate}
This finishes the proof.
\end{proof}

\begin{corollary}
\lbl{cor.h}
$$
G(f)= C(f)q^{\d(f)}\prod_{v=1}^r
\sum_{f(e^b_v)\geq c_1\geq\dots \geq c_{f(e^r_v)}\geq 0}
q^{\sign(v)(c_1+\dots c_{f(e^r_v)})}.
$$
\end{corollary}

Since
$$
\sum_{f(e^b_v)\geq c_1\geq\dots \geq c_{f(e^r_v)}\geq 0}
q^{\sign(v)(c_1+\dots c_{f(e^r_v)})}=
\binom{f(v)}{f(e^b_v)}_{q^{\sign(v)}},
$$
we have 

\begin{corollary}
\lbl{cor.skoro}
$$
G(f)= q^{\d(f)}\mult_q(f)C(f).
$$
\end{corollary}

\begin{proof}(of Theorem \ref{thm.nonc})
Theorem \ref{thm.main} tells us that 
$$
J_n(K,q) = q^{\d(K,n)}\sum_{f\in \F(G_K)}\mult_{t}(f)
t^{\d(f)} \prod_{v \in V_K} t^{-\sign(v)nf(e^b_v)}
\prod_{e\text{red};t(e)=v}\prod_{j=0}^{f(e)-1} 
(1-t^{-\sign(s(e))(n- (\sum_{e'<_v e}f(e))-j)}).  
$$
Comparing this with the definition \ref{def.eval} of the n-evaluation and 
using 
Theorem \ref{thm.qMM}, Observation \ref{obs.hr} and Corollary \ref{cor.skoro},
we can see that Theorem \ref{thm.nonc} follows.
\end{proof}
