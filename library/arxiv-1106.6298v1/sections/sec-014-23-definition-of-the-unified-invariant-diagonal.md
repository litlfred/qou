---
doc_id: arxiv-1106.6298v1
doc_title: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS"
section_id: sec-014-23-definition-of-the-unified-invariant-diagonal
section_title: "Definition of the unified invariant: diagonal case"
section_number: 2.3
pages: 11-11
source_pdf: 1106.6298v1.pdf
source_sha256: 23b0754067873a04
toc_source: outline
text_source: latex
latex_prose_ratio: 0.911
latex_coverage_ratio: 1.0
doc_brief: "ON THE UNIFICATION OF QUANTUM 3–MANIFOLD INVARIANTS — In 2006 Habiro initiated a construction of generating functions for Witten– Reshetikhin–Turaev (WRT) invariants known as uniﬁed WRT invariants."
---
\label{2501}
Suppose that the linking number between any two components of $L$
is 0, and  the framing on components of $L$ are $b_i=\pm p_i^{k_i}$ for
$i=1,\dots, m$, where each $p_i$ is prime or 1.
Let us denote the link $L$ with all framings switched to zero by $L_0$.





Using \eqref{Jones}, taking into account the framings $b_i$'s, we have
\[
J_{L}(\bn)\prod_{i=1}^m [n_i] = \sum_{\bk\ge 0} C_{L_0 }
(\bk) \, \prod_{i=1}^m q^{b_i \frac{n_i^2-1}{4}} A(n_i,k_i).
\]
By the definition of $F_{L}$, we have
\[ F_{L}(\xi)= \sum_{\bk \ge 0}
\ev_\xi(C_{L_0 }(\bk)) \, \prod_{i=1}^m
{\sum_{n_i}}^\xi \,  q^{b_i \frac{n_i^2-1}{4}} A(n_i,k_i).
\]
From \eqref{0077} and  Theorem \ref{0078}, we get
\[
\tau'_{M}(\xi) = \ev_\xi \left \{  \prod_{i=1}^m  I_{L(b_i,1)} \,
 \sum_{\bk} C_{L_0 }(\bk) \, \prod_{i=1}^m  Q_{b_i,k_i} \right \},
\]
where the existence of
 the unified invariant of the lens space $I_{L(b_i,1)}\in \R_b$,
with
 $\ev_\xi(I_{L(b_i,1)})=\tau'_{L(b_i,1)}(\xi)$ can be shown by a
direct computation (we refer to \cite{BBL} for more details).

Thus if we define
\[
I_{M}:= \prod_{i=1}^m  I_{L(b_i,1)} \, \sum_{\bk}
C_{L_0 }(\bk) \, \prod_{i=1}^m  Q_{b_i,k_i}\, ,
\]
then \eqref{0080} is satisfied. By Theorem \ref{GeneralizedHabiro},
$C_{L_0 }(\bk)$ is divisible by $(q^{k+1};q)_{k+1}/(1-q)$, which is
divisible by $(q;q)_k$, where $k = \max k_i$. It follows that
$I_{M} \in \R_b$. In addition, if $b$ is odd,
then $I_{M} \in \calS_b$.
