---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT"
section_id: sec-009-41-normal-khovanov-homology
section_title: "Normal Khovanov Homology"
section_number: 4.1
pages: 13-13
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POLYNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant Jn K and the so(2n + 1) knot invariant soJn K studied by"
---
We briefly recall how the complex $Kh(L)$ for Khovanov homology of an oriented link $L$ with is defined.
We use notation similar to \cite{BN2, P} to define the Khovanov complexes so that we can easily reference it again when we look at a similar e-graded version of covering Khovanov homology.
Let $X$ be a crossing in $L$, and $L_0, L_1$ denote the diagram obtained by replacing $X$ with its $0$ and $1$-resolution respectively.
Replace each crossing $X$ with a two term chain complex $D_X: L_0 \to L_1\{1\}$, where $L_0$ lives in cohomological degree $0$ is $X$ is a positive crossing and lives in cohomological degree $-1$ otherwise.
$D_X$ is a saddle cobordism, so the degree of $D_X$ is $1-1=0$ (see \cite[Section 6]{BN2}).

Doing this for all the crossings gives the cube of resolutions with a saddle cobordism associated to each edge.
Then for any sign assignment $\epsilon$ for the edges of the cube of resolutions so that faces anti-commute (e.g \cite[Section 3.2]{BN1}), one obtains a chain complex of cobordisms $[L]'$ defined by
\begin{align*}
  [L]_{r-n_-}'&= \bigoplus_{\sum z_i =r} L_z'\{r\} \\
  d|_{L_z'}&=\sum\limits_{\alpha: z\to w}\epsilon(\alpha)D_{\alpha}
\end{align*}
where $\alpha$ sums over edges out of $z$.
Let $j$ be the entry where $z$ and $w$ differ and $X_j$ denote the $j$-th crossing; then $D_\alpha= D_{X_j}$.
Then $Kh(L)^i=[L]_{i}'\{n_+-2n_-\}$ is the Khovanov complex.
One then applies the usual TQFT to get a complex of $\Z$-modules whose homology is Khovanov homology.
