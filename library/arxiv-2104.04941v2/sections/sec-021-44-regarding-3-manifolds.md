---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-021-44-regarding-3-manifolds
section_title: "Regarding 3-manifolds"
section_number: 4.4
pages: 23-23
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.872
latex_coverage_ratio: 0.988
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
The process described can be applied to $3$-manifolds as well as
  surfaces. We omit all details. An element of $\Conf_4^{\ast}(G/K)$ is
  attached to each tetrahedron, and the coordinates for these flag
  varieties are encoded on a quiver for each face of the tetrahedron.

  As in \cref{def:gluing-configurations}, only two copies of
  $\Conf_3^{\ast}(G/K)$ are necessary to define an element in
  $\Conf_4^{\ast}(G/K)$, so any two copies of $Q$ should determine all
  the coordinates of the tetrahedron. Therefore, the coordinates on any
  pair of faces determine the coordinates on the other pair. This
  relation is given by the mutation $\muflip$.

  Finally, as coordinates are identified along glued edges in the
  surface case, in the $3$-manifold case they are glued along faces, as
  in \cref{fig:tetrahedra-with-quivers}. When reconstructing $\rho$, the
  path $\gamma$ is homotoped as before and the same elements on each
  segment are used.

  \begin{figure}[h]
    \centering
    \includestandalone[mode=image|tex]{fig/tetrahedra-with-quivers}

    \caption{Two tetrahedra with a face identification. The quivers
      $Q_{C_2}$ on the front two faces of each tetrahedron are shown.
      \label{fig:tetrahedra-with-quivers}
    }
  \end{figure}

  The $\mathcal{A}$-coordinate variety constructed this way is called
  the \defined{Ptolemy variety}, see \cite{ggz2015}, \cite{gtz2015},
  \cite{zickert2016} for details. The variety constructed by the
  $\mathcal{X}$-coordinates will be the analogue of the \defined{shape
    coordinates} of \cite{ggz2015}, and the defining equations will
  generalize Thurston's gluing equations.

  Defining varieties by quivers in this fashion allows efficient
  computation, and databases have been constructed of Ptolemy varieties
  for large numbers of triangulations, See \cite{unhyperbolic}.
