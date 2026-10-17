---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-002-representations
section_title: "Representations"
section_number: null
pages: 5-7
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 1.0
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:representations}

In this section and the next, we develop the representation theory needed for Grassmannian LP bounds.

As is standard for compact Lie groups, we work with functions on $\gras{m}{n}$ to find irreducible representations. Define an inner product for functions on $\gras{m}{n}$ as follows:
\[
\ip{f}{g} := \int_{\gras{m}{n}} \conj{f(a)}g(a) \; da.
\]
Here $da$ is the unique measure invariant on $\gras{m}{n}$, normalized so that $\nobreak{\int da = 1}$. That such a measure exists an is unique (the Haar measure) follows from the fact that $\gras{m}{n}$ is a compact Lie group. Equivalently, we may write
\[
\ip{f}{g} := \int_{U(n)} \conj{f(U^*P_aU)}g(U^*P_aU) \;dU,
\]
where $dU$ is the Haar measure on $U(n)$, and $P_a$ is the projection matrix for some fixed $a \in \gras{m}{n}$. Now let $L^2(\gras{m}{n})$ denote the space of square-integrable functions on $\gras{m}{n}$. Then $U(n)$ acts on $f\ \in \gras{m}{n}$ as follows:
\[
(Uf)(P_a) := f(U^*P_aU).
\]
It follows that $L^2(\gras{m}{n})$ provides a representation of $U(n)$. As we will see, this representation can be decomposed into irreducible subrepresentations explicity, and the decomposition is \defn{multiplicity-free}: no irreducible representation of $U(n)$ occurs more than once in $L^2(\gras{m}{n})$. 

Since $U(n)$ is a compact Lie group, its irreducible representations are well-studied: see for example \cite{sep,gw1,bump,fh1}. Every irreducible representation is indexed by a \defn{dominant weight} \cite[Theorem 7.34]{sep}. In the case of $U(n)$, we may take these weights to have the form \cite[Theorem 38.3]{bump}
\[
\la = (\la_1,\ldots,\la_n): \la_1 \geq \la_2 \geq \ldots \geq \la_n, \la_i \in \ints.
\]

The dimension of the irreducible representation $V_\la$ indexed by $\la$ is given by \defn{Weyl's character formula} \cite[Theorem 7.32]{sep}. In the case of $U(n)$, the formula reduces to: 
\begin{equation}
\dim V_\la = \prod_{1 \leq i < j \leq n} \frac{\la_i - \la_j + j-i}{j-i}.
\label{eqn:weylchar}
\end{equation}
For example, the standard representation of $U(n)$ is indexed by $\la = (1,0,\ldots,0)$, which gives
\[
\dim V_{(1,0,\ldots,0)} = n.
\]
Note that there is more than one irreducible representation with the same dimension.

Each dominant weight may also be thought of as a form acting on a maximal Abelian subgroup of the Lie group. Here $\la$ acts on the diagonal matrix $d =\diag(d_1,\ldots,d_n) \in U(n)$ as follows:
\[
d^{\la} := \prod_{i=1}^n d_i^{\la_i}.
\]
The next section describes exactly which of these forms contribute to the decomposition of $L^2(\gras{m}{n})$.
