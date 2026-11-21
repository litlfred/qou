---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-003-12-cluster-ensemble-structures
section_title: "Cluster ensemble structures"
section_number: 1.2
pages: 4-5
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.985
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
In the above program, the retriangulation identity was given by
  Ptolemy's Theorem. Another structure that encodes the identity is a
  \defined{cluster ensemble}. We defer a detailed description to
  \cref{sec:cluster-ensembles}, but for now we only need that a cluster
  ensemble consists of a \defined{quiver} (a directed graph with a
  skew-symmetrizable adjacency matrix) and a pair of coordinate
  structures ($\mathcal{A}$- and $\mathcal{X}$-coordinates), and that
  the shape of the quiver dictates how the coordinates change under
  \defined{mutation} (a certain local alteration of the quiver).

  The quiver of the cluster ensemble which realizes $ac + bd = ef$ for
  the $\mathcal{A}$-coordinates is given (along with the effect of the
  only relevant mutation) in \cref{fig:QA1-and-flip}. The quivers are
  inscribed in two quadrilaterals with different diagonals.

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/QA1-and-flip}

    \caption{Quiver for type $A_1$. The $\mathcal{A}$-coordinate at
      $v_k$ is $a_k$. The relation on $\mathcal{A}$-coordinates for
      mutating at $v_5$ is $a_1 a_3 + a_2 a_4 = a_5 a_5'$.
      \label{fig:QA1-and-flip}
    }
  \end{figure}

  For other surfaces $\Sigma$, larger collections of triangles can be
  glued together. Retriangulations (and reorderings) can be computed as
  sequences of mutations, and the coordinate changes are given by
  collections of low-degree polynomial relations.
