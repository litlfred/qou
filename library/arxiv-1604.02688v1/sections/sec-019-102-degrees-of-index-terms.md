---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-019-102-degrees-of-index-terms
section_title: "Degrees of index terms"
section_number: 10.2
pages: 29-30
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.889
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Recall, from equation (\ref{index_deg_surface}), that the $q^{1/2}$-degree 
of a term $I([S])$  in the $q$-series for the 3D-index is given by the 
expression 
$$
d(S)=d(S^*) =-\chi(S^*) +\delta(S^*),
$$
where $S^*$ is the minimal positive coset representative for $[S]=S+\TT$. 
Then $S^*$ is a normal class with at most two quadrilateral types in each 
tetrahedron, and 
$$
d(S^*)=-\chi(S^*) +\sum_i p_iq_i,
$$
where $p_i,q_i\ge0$ are the numbers of quadrilaterals for $S^*$ in the 
$ith$ tetrahedron, and $\chi(S^*)$ denotes the formal Euler characteristic 
of $S^*$.

\begin{lemma} 
\label{deg_for_gen_norm_surf}
Let $S \in Q(\T;\Z)$ be a Q-normal class 
and let $\tilde S$ be the embedded generalised normal surface 
$\tilde S$ corresponding to $S^*$. Then
$$d(S)= -\chi(\tilde S)+ \sum_i (p_i q_i - p_i - q_i + \gcd(p_i,q_i)),$$
where $p_i,q_i\ge0$ are the numbers of quadrilaterals for $S^*$ in the 
$ith$ tetrahedron.

Hence
$d(S) \ge -\chi(\tilde S)$ with equality if and only if $\tilde S$ is a  
``special'' embedded generalised normal surface, i.e. in each tetrahedron one 
of the coefficients $p_i$ or $q_i$ is either $0$ or $1$. 
\end{lemma}

\begin{proof} 
We can choose a generalised angle structure on $\T$ with vanishing 
rotational peripheral holonomy by 
Proposition \ref{gen_ang_zero_periph_rot_hol},  and use this to compare 
the Euler characteristic of $\tilde S$ 
with the formal Euler characteristic of $S^*$, using 
Proposition \ref{comb_Gauss-Bonnet} and 
Definition \ref{formal_euler_from_ang_str} from Appendix \ref{gen_angle_euler}.

In both cases we get corner terms of $(\text{formal angles})/2\pi$ which 
add to $1$ for each vertex. 
Moreover the number of edges in $\tilde S$ is the same as for $S^*$, but 
the number of disks is reduced from $\sum_i (p_i+q_i)$ to 
$\sum_i \gcd(p_i,p_i)$.  So
$\chi(\tilde S)= \chi(S^*) + \sum ( \gcd(p_i,q_i) - p_i -q_i )$. Hence
$d(S^*) = - \chi(S^*) + \sum_i p_i q_i = -\chi(\tilde S)
+ \sum_i (p_i q_i - p_i - q_i + \gcd(p_i,q_i)).$

\smallskip
The final result now follows from the observation that for any integers 
$p, q \ge 0$ we have
\begin{itemize}
\item $pq - p - q + \gcd(p,q) = 0$ if $p$ or $q$ is $0$, and otherwise
\item $pq - p - q + \gcd(p,q) \ge pq-p-q+1 =(p-1)(q-1) \ge 0$ with equality 
if and only if $p$ or $q$ is $1$.
\end{itemize}
\end{proof}

\begin{rmk}  
A very similar function is studied in \cite[Section 4.1]{FrKa}.
\end{rmk}

\begin{rmk} 
We will be particularly interested in terms in the 3D-index sum which 
have non-positive degrees. 
\end{rmk}
