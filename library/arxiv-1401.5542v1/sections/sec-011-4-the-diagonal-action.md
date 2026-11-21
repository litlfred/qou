---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-011-4-the-diagonal-action
section_title: "The diagonal action"
section_number: 4
pages: 9-9
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.982
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
Fix an ordering of the $1$-cells of $\T$ and of the cusps of $M$. As mentioned in Remark~\ref{rm:PickRepresentative} the Ptolemy variety can be regarded as a subset of the ambient space $\C^e$. 



Let $T=(\C^*)^v$ be a torus whose coordinates are indexed by the cusps of $M$. There is a natural action of $T$ on $P^{\sigma}_2(\T)$ defined as follows:
For $x=(x_1,\dots,x_v)\in T$ and $c=(c_1,\dots c_e)\in P^{\sigma}_2(\T)$ define a Ptolemy assignment $cx$ by
\begin{equation}
(xc)_i=x_jx_kc_i,
\end{equation}
where $j$ and $k$ (possibly $j=k$) are the cusps joined by the $i$th edge cycle. The action is thus determined entirely by the $1$-skeleton of $\widehat M$.

\begin{remark}\label{rm:IntrinsicDiagonalAction} There is a more intrinsic definition of this action in terms of decorations: 
Each vertex of $\Mtildehat$ determines a cusp of $M$, and if $D$ is a decoration taking a vertex $w$ to $gP$, the decoration $xD$ takes $w$ to $g\left(\begin{smallmatrix}x_i&0\\0&x_i^{-1}\end{smallmatrix}\right)P$ where $i$ is the cusp determined by $w$. The fact that the two definitions agree under the one-one correspondence \eqref{eq:1to1Obstruction} is an immediate consequence of the relationship given in Figure~\ref{fig:DecToPtolemy}.
\end{remark}
