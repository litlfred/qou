---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-019-34-splitting-of-sp-and-evaluation
section_title: "Splitting of Sp and evaluation"
section_number: 3.4
pages: 14-14
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.969
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
For every integer $a$, we put $\N_a := \{ n \in \N \mid (a,n)=1\}$.

Suppose $p$ is a prime. Analogously to \eqref{cofinal},
we have
$$\calS_p \simeq \Z[1/p][q]^\N\,.$$

Observe that $\N$ is not $\Z[1/p]$--connected. In fact one has
 $\N =\amalg_{j=0}^\infty \; p^j \N_p$, where each $p^j\N_p$ is
$\Z[1/p]$--connected.
Let us define
\[
\calS_{p,j}:= \Z[1/p][q]^{p^j \N_p}.
\]
Note that for every $f \in \calS_p$, the evaluation $\ev_\xi(f)$ can be
 defined for every root $\xi$ of unity. For $f\in \calS_{p,j}$, the evaluation
$\ev_\xi(f)$ can be defined  when $\xi$ is a root of unity of order
in $p^j\N_p$. In \cite{BBL} we proved the following.



\begin{proposition} For every prime $p$ one has
\begin{equation} \calS_p\simeq \prod_{j=0}^\infty \calS_{p,j}.
\label{0912}\end{equation}

\end{proposition}

Let $\pi_j: \calS_p \to \calS_{p,j}$ denote the projection onto the
$j$th component in the above decomposition.
Suppose $\xi$ is a root of unity of order $r= p^j r'$,
with $(r',p)=1$. Then
for any $x\in \calS_p$, one has
$$ \ev_\xi(x) = \ev_\xi(\pi_j(x)).$$
If $i\neq j$ then $\ev_\xi(\pi_i(x))=0$.
