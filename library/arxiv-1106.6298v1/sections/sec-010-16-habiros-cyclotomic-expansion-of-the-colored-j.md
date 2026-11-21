---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-010-16-habiros-cyclotomic-expansion-of-the-colored-j
section_title: "Habiro's cyclotomic expansion of the colored Jones polynomial"
section_number: 1.6
pages: 8-9
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.97
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
For non--negative integers $n,k$ we define
$$ A(n,k) := \frac{\prod^{k}_{i=0}
\left(q^{n}+q^{-n}-q^i -q^{-i}\right)}{(1-q) \, (q^{k+1};q)_{k+1}}.$$
For $\bk=(k_1,\dots,k_m)$ let
$$ A(\bn,\bk):= \prod_{j=1}^m \; A(n_j,k_j).$$
Note that $A(\bn,\bk)=0$ if $k_j \ge n_j$ for some index $j$. Also
$ A(n,0)= q^{-1} J_U(n)^2.$


The colored Jones polynomial $J_{L}
(\n)$  can be repackaged into the invariant $C_{L}
(\bk)$ as stated in the following theorem.
\begin{Thm} {\rm [Habiro]}\label{GeneralizedHabiro}
 Suppose $L$ is a link in $S^3$ having zero linking matrix.


Then  there are invariants
\begin{equation}\label{Jones2}
C_{L}(\bk) \in \frac{(q^{k+1};q)_{k+1}}{(1-q)}
\,\,\BZ[q^{\pm 1}] ,\quad \text{where  $k=\max\{k_1,\dots, k_m\}$}
\end{equation}
such that for every $\bn =(n_1,\dots, n_m)$
\begin{equation}\label{Jones}
 J_{L}
(\n)  \,  \prod^m_{i=1}\; [n_i] = \sum_{0\le k_i \le n_i-1}
C_{L}(\bk)\;
  A(\bn, \bk).
\end{equation}
\end{Thm}




 Note that the existence of $C_{L}(\bk)$ as
rational functions in $q$ satisfying \eqref{Jones} is
 easy to establish. They correspond to the Jones polynomial
colored by different elements of the Grothendieck ring
of $U_q(\frak {sl}_2)$, i.e. by linear combinations of representations.
The difficulty here is to show the integrality
of \eqref{Jones2}.

 Since $A(\bn, \bk) =0$ unless $ \bk < \bn$, in the sum on the right
hand side of \eqref{Jones} one can assume that $\bk$ runs over the set
 of all $m$--tuples $\bk$ with non--negative integer components. We will use
this fact later.
