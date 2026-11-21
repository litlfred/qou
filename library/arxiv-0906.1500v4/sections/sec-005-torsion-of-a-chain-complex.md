---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-005-torsion-of-a-chain-complex
section_title: "Torsion of a chain complex"
section_number: null
pages: 3-4
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.98
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
Let 
$C_* = (
  0 \to 
    C_n \xrightarrow{d_n} 
    C_{n-1} \xrightarrow{d_{n-1}} 
    \cdots \xrightarrow{d_1} 
    C_0 \to 
  0 
)$ 
be a chain complex of finite dimensional vector spaces over a field
$\FF$. Choose a basis $\cbasis{(i)}$ of $C_i$ and a basis $\hbasis{i}$
of the $i$-th homology group $H_i(C_*)$. The torsion of $C_*$ with
respect to these choices of bases is defined as follows.

For each $i$, let $\bbasis{i}$ be a set of vectors in $C_{i}$ such that
$d_{i}(\bbasis{i})$ is a basis of 
$B_{i-1}= \im(d_{i} \colon C_{i} \to C_{i-1})$ and 
let $\hbasis[\tilde{h}]{i}$ denote a lift of
$\hbasis{i}$ in $Z_i = \ker(d_{i} \colon C_i \to C_{i-1})$. The set of
vectors $d_{i+1}(\bbasis{i+1})\hbasis[\tilde{h}]{i}\bbasis{i}$ is a
basis of $C_i$. Let
$[d_{i+1}(\bbasis{i+1})\hbasis[\tilde{h}]{i}\bbasis{i}/\cbasis{i}] \in \FF^*$ 
denote the determinant of the transition matrix between those
bases (the entries of this matrix are coordinates of vectors in
$d_{i+1}(\bbasis{i+1})\hbasis[\tilde{h}]{i}\bbasis{i}$ with respect to
$\cbasis{i}$). The \emph{sign-determined Reidemeister torsion} of
$C_*$ (with respect to the bases $\cbasis{*}$ and $\hbasis{*}$) is the
following alternating product (see~\cite[Definition 3.1]{Turaev:2000}):
\begin{equation}\label{def:RTorsion}
  \Tor{C_*}{\cbasis{*}}{\hbasis{*}} 
  = (-1)^{|C_*|} \cdot  
  \prod_{i=0}^n 
  [d_{i+1}(\bbasis{i+1})\hbasis[\tilde{h}]{i}\bbasis{i}/\cbasis{i}]^{(-1)^{i+1}} 
  \in \FF^*.
\end{equation}
Here $$|C_*| = \sum_{k\mygeq 0} \alpha_k(C_*) \beta_k(C_*),$$ where
$\alpha_k(C_*) = \sum_{i=0}^k \dim C_i$ and 
$\beta_k(C_*) = \sum_{i=0}^k \dim H_i(C_*)$.

The torsion $\Tor{C_*}{\cbasis{*}}{\hbasis{*}}$ does not depend on the
choices of $\bbasis{i}$ nor on the lifts $\hbasis[\tilde{h}]{i}$.  Note that if
$C_*$ is acyclic (\ie~if $H_i = 0$ for all $i$), then $|C_*| = 0$.
