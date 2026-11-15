---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-016-46-gluing-equations-for-general-concrete-triangu
section_title: "Gluing equations for general concrete triangulations"
section_number: 4.6
pages: 14-14
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 1.0
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:ShapeAssignmentSymmetries}

Since every concrete triangulation can be obtained from an oriented one by reordering some of the vertices, Lemma~\ref{shapesymmetries} motivates the following.

\begin{definition}\label{def:ShapeAssignmentGeneral} A shape assignment on a concrete triangulation $\T$ is a shape assignment on each simplex such that
\begin{equation}\label{eqn:GeneralizedGluingOrderAgnostic}
\prod\limits_{(t,\Delta)\in p}\,\prod\limits_{t = s + e} (z^e_{s,\Delta})^{\epsilon_\Delta} = 1, 
\end{equation}
where $\epsilon_\Delta$ is a sign indicating whether or not the orientation of $\Delta$ given by the vertex ordering agrees with the orientation inherited from $M$. The variety of shape assignments is denoted by $V_n(\T)$.
\end{definition}

The following is an immediate corollary of Lemma~\ref{shapesymmetries}, c.f.~Remark~\ref{rm:reordering}.
\begin{lemma}\label{lemma:reorderingshapes}
Let $\{z_{\Delta_i}\}$ be a shape assignment on $(M,\T)$ and let $\T'$ be the triangulation obtained from $\T$ by reordering each simplex $\Delta_i$ by a permutation $\sigma_i\in S_4$. The shape assignments $\{\sigma_i^*z_{\Delta_i}\}$ form a shape assignment on $(M,\T')$. \qed
\end{lemma}

\begin{corollary}
Up to canonical isomorphism, the gluing equation variety only depends on the abstract triangulation.\qed
\end{corollary}

\begin{remark}
The gluing equations can also be defined if $M$ is non-orientable: pick an oriented neighborhood $U$ of the integer point $p$. The sign $\epsilon_\Delta$ now indicates whether or not the orientation of $\Delta$ agrees with the orientation of $U$. We will not explore this further.
\end{remark}
