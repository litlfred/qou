---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-005-14-results
section_title: "Results"
section_number: 1.4
pages: 6-7
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.984
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
Our main result is an explicit construction for cluster ensembles
  described above for all semisimple $G$, including the rotation and the
  flip. In other words, we present a constructive result of the
  following theorem.

  \begin{theorem}
    \label{thm:intro-main-result}
    For a split semisimple simply-connected (or centerless) algebraic
    group $G$ over $\mathbb{Q}$, there exists a quiver $Q$, quiver
    mutations $\murot$ and $\muflip$, and a coordinate map
    $\conftoquiv$.

    The map $\conftoquiv$ associates coordinates of a flag configuration
    to the coordinates on the cluster ensemble for $Q$, the quiver
    mutation $\murot$ describes how the coordinates change under
    rotation of an ordered triangle and $\muflip$ describes how the
    coordinates change under retriangulation.
  \end{theorem}

  We call this collection $(Q, \murot, \muflip, \conftoquiv)$ a
  \defined{Fock--Goncharov coordinate structure}. The construction
  algorithm is presented in \cref{sec:main-result}. First, we use the
  algorithm of \cite[Section~2]{fominzelevinsky1999}, using a specific
  choice of $w_0$ (the longest word in the Weyl group) by
  \cref{fac:w0-construction}. This produces a quiver whose
  $\mathcal{A}$-coordinates generate the coordinate ring for $B_{-} = H
  \times N_{-}$. We call this quiver $Q_0$.

  The quiver $Q_0$ has the same mutable portion that we need for $Q$.
  However, the non-mutable portion isn't complete, so $Q_0$ does not
  have \defined{triangulation-compatible symmetry} (see \cref{def:tcs}).
  We therefore can apply the rotation $\murot$ to $Q_0$, and define $Q$
  to be the smallest quiver with triangulation-compatible symmetry
  containing $Q_0$.

  The quiver $Q$ and the map $\conftoquiv$ allow constructing
  representation varieties easily given a triangulation of a surface: a
  copy of $Q$ is inscribed on each triangle and vertices along edges are
  identified. The maps $\murot$ and $\muflip$ describe how the
  coordinate functions of the variety respond to retriangulation,
  ensuring that the variety itself is independent of triangulation
  choices.

  \begin{remark}
    The existence of cluster ensemble structures was shown
    non-constructively, and by different methods, in
    \cite{goncharovshen2018}.
  \end{remark}

  This theorem can also be used to compute representation varieties for
  $3$-manifolds, following work of Zickert. In this case, quivers are
  drawn on each face of each ideal tetrahedron in the triangulation. The
  map $\muflip$ describes the relation between coordinates on the four
  triangular faces of each tetrahedron. The variety constructed is not,
  however, independent of triangulation. If the triangulation is
  sufficiently fine, however, the variety detects all representations.
