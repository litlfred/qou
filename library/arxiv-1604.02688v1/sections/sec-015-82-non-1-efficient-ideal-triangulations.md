---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-015-82-non-1-efficient-ideal-triangulations
section_title: "Non 1-efficient ideal triangulations"
section_number: 8.2
pages: 24-25
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.948
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
When the triangulation $\T$ is not 1-efficient, it turns out that the 
series $I_\T^a(b)$ may converge for some $b \ne {\bf 0}$
even when the series $I_\T^0(0)$ diverges.  See Example \ref{toroidal_ex} 
below. The following result gives an obstruction to convergence.

\begin{lemma} 
Assume that an ideal triangulation $\T$ contains a Q-normal class 
$S \in Q(\T;\Z_+)$ with $[S]_2=a$ and $\bd S$ satisfying $[\bd S]=b$,
and there is a closed normal surface $0 \ne S' \in N(\T;\Z_+)$ such that 
$S'$ is embedded and $-\chi(S')+ 2\delta(S,S') \le 0$.
Then the index sum for $I_\T^a(b)$ diverges.
\end{lemma}

\begin{proof}
By replacing $S'$ by $2 S'$, if necessary, we can assume that 
$S' \in Q_0(\T;\Z_+)$. Then for all $k \in \Z_+$, the normal class 
$S_k=S+k S'$ contributes a term in the index sum 
(\ref{explicit_index_computation}) for $I_\T^a(b)$ with $q^{1/2}$-degree 
\begin{align}
d (S_k) &= -\chi(S+k S') + \delta(S+k S') \nonumber \\
&= -\chi(S)-k\chi(S') +\delta(S)+2k \delta(S,S')+k^2\delta(S') \nonumber \\
& = d(S)+k\left( -\chi(S')+2 \delta(S,S')\right)+k^2\delta(S').
\label{degree_S_k}
\end{align}
Hence $d(S_k)$ remains bounded above as $k \to +\infty$ if $\delta(S')=0$ 
and $-\chi(S')+2 \delta(S,S')\le 0$. Thus the index sum diverges.
\end{proof}

In general, we have the following converse.

\begin{thm} 
\label{cgce_I_T(b)} 
Assume that an ideal triangulation $\T$ does not contain a Q-normal class 
$S \in Q(\T;\Z_+)$ with $\bd S = b$, and a closed normal surface 
$S' \in N(\T;\Z_+)$ such that $S'$ is embedded and 
$-\chi(S')+ 2\delta(S,S') \le 0$. Then the index sum $I_\T^a(b)$ converges.
\end{thm}

\begin{proof}
We start by following the proof of Theorem \ref{1-eff_cgce_I_T(b)}. This 
shows that there exist finitely many normal classes
$S_1, \ldots, S_k \in Q(\T;\Z_+)$ with $\bd S_i=b$ and finitely many 
normal classes  $F_1, \ldots, F_m \in Q(\T;\Z_+)$ with $\bd F_i=0$ 
such that every $S \in Q_b(\T;\Z_+)$ with $\bd S = b$  can be written as
$$
S= S_j + \sum_{i=1}^m x_i F_i, \text{ where } 1\le j \le k 
\text{ and } x_i \in \Z_+.
$$

Now 
\begin{align*}
d(S) 
&= d(S_j)+ \sum_{i} (-\chi(F_i)+ 2 \delta(F_i,S_j))x_i 
+ \sum_{i ,j } \delta(F_i,F_j) x_i x_j \\
&\ge  d(S_j)+ \sum_{i} (-\chi(F_i)+ 2 \delta(F_i,S_j))x_i  
+ \delta(F_i) x_i ^2 .
\end{align*}
For each $i \in I_0$ we have, by assumption,  either $\delta(F_i)\ge 1$ 
or $-\chi(F_i)+ 2 \delta(F_i,S_1) \ge 1$ so it follows that 
$$
f_i(x):=(-\chi(F_i)+ 2 \delta(F_i,S_1))x  + \delta(F_i) x^2
$$
is bounded below for $x \ge 0$ and approaches 
$+\infty \text{ as } x\to +\infty.$
Since  there are only finitely possibilities  for $S_1$,
it follows that there are only finitely
many $S \in Q_b(\T;\Z)$ such that $\bd S = b$ and $d(S) \le D$. Hence the 
index sum for $I_\T^a(b)$ converges.
\end{proof}

\medskip

\begin{rmk}
\begin{enumerate}
\item 
When $b=0$ this reduces to Theorem \ref{index0_cgce}, as we can take $S=0$ 
in the above theorem.
\item 
If the triangulation $\T$ is {\em $0$-efficient} then 
Theorem \ref{cgce_I_T(b)} simplifies to the following: \\
$I_\T^a(b)$ converges if and only if $\T$ 
does not contain a Q-normal class $S \in Q(\T;\Z_+)$ with $\bd S = b$,  
and an \emph{embedded} closed normal surface $S'$ disjoint from $S$ such 
that  $\chi(S') =0$.
\end{enumerate}
\end{rmk}
