---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-007-invariance-under-m1
section_title: "Invariance under M1"
section_number: null
pages: 20-21
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.861
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
First we consider move M1. Note that by applying M2 and M3, we can
transform an open book  with any number of pages to one with only one page
(see \firef{f:book}). 
\begin{figure}[ht]
\begin{align*}&\figscale{0.7}{figures/book0.eps}
    \xxto{\text{add edge to each page}}
    \figscale{0.7}{figures/book1.eps}
    \\
     & \xxto{\text{add faces between new edges}}
    \figscale{0.7}{figures/book2.eps}
     \xxto{\text{remove all pages but one}}  
   \figscale{0.7}{figures/book3.eps} 
   \end{align*}
 \caption{Decomposing an open book into a single page book}\label{f:book}
 \end{figure} 
Thus, it suffices to prove invariance under M1 in this
special case. Drawing the dual graph in the vicinity of the vertex,
invariance under M1 is equivalent to the following equality:
$$
\frac{1}{\DD^2}\sum_{j,k\in \Irr(\C)}d_{j}d_{k}\tzPairingVII
=
\sum_{i\in \Irr(\C)}d_{i}\tzPairingIII
$$
Note the normalizing factor
$\frac{1}{\mathcal{D}^2}$ which comes from the fact that we are removing a
vertex.

Using semisimplicity of $\C$, it is easy to see that it suffices to show
this equality in the special case when $V=V_1\otimes \dots \otimes V_n$ is
simple:
$$
\frac{1}{\DD^2}\sum_{j,k\in \Irr(\C)}d_{j}d_{k}\tzPairingVIII
=
\sum_{i\in \Irr(\C)}d_{i}\tzPairingIX
$$
By \leref{l:pairing}, the right-hand side is equal to $\coev_V\colon \one
\to V\otimes V^*$. Since $\Hom(\one, V\otimes V^*)$ is one-dimensional,
the left-hand side is also a multiple of $\coev_V$. Composing it with the
evaluation morphism  $\ev_V$, we get
\begin{align*}
&\frac{1}{\DD^2}\sum_{j,k}d_jd_kN_{1}^{Vjk} =
\frac{1}{\DD^2}\sum_{j,k}N_{k^*}^{Vj}d_kd_j\\
&\quad=\frac{1}{\DD^2}\sum_{j}\Bigl(\sum_{k}N_{k^*}^{Vj}d_k\Bigr)d_j=
\frac{1}{\DD^2}\sum_{j}(d_{V}d_j)d_j=d_V,
\end{align*}
which proves that the left-hand side is equal to $\coev_V$.
