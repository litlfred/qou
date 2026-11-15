---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-004-13-higher-teichmüller-spaces
section_title: "Higher Teichmüller spaces"
section_number: 1.3
pages: 5-6
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.987
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
We view higher Teichmüller spaces as collections of representations \[
    \Set{ \rho : \pi_1(\Sigma) \to G \text{ discrete and faithful}} / G,
  \] where the standard Teichmüller space case is given by $G =
  \Isom^{+}(\mathbb{H}^2) = \PSL_2(\mathbb{R})$. In order to apply the
  Fock--Goncharov program, we need the following conditions.
  \begin{itemize}
  \item
    The surface $\Sigma$ must admit an ideal triangulation, so we demand
    that it be hyperbolic with $n \ge 1$ punctures.
  \item
    The group $G$ must be a split semisimple algebraic group over
    $\mathbb{Q}$; for technical reasons the moduli space
    $\mathcal{A}_{G,\Sigma}$ is defined when $G$ is simply-connected,
    and $\mathcal{X}_{G,\Sigma}$ is defined when $G$ is centerless.
    However, the field underlying $G$ is not critical.
  \end{itemize}

  As another technical point, when $G$ is simply connected we will
  parametrize boundary-unipotent representations, and when $G$ is
  centerless the representations will be boundary-borel (see
  \cref{def:peripheral-stuff}).

  We now replay the program to create moduli spaces
  $\mathcal{A}_{G,\Sigma}$ and $\mathcal{X}_{G,\Sigma}$ for higher rank
  $G$.

  \begin{quote}
    \emph{1. The structure is determined by ideal points.}
  \end{quote}

  By restrictions on $\Sigma$, the representation is still defined by
  ideal points of a fundamental domain.

  \begin{quote}
    \emph{2. We can identify ideal points with cosets of isometries in
      $\Isom^{+}(\mathbb{H}^2)$ that define them}
  \end{quote}

  We replace $\Isom^{+}(\mathbb{H}^2)$ with general $G$. By our
  restrictions on $G$, subgroups $N_{+}$ and $B_{+}$ are still
  available.

  \begin{quote}
    \emph{3. Choosing an ordered triangulation attaches a non-degenerate
      ordered triple of cosets to each triangle.}
  \end{quote}

  Non-degenerate cosets are replaced by \defined{sufficiently generic
    configuration spaces} (see \cref{def:Conf_k_star}). These ensure
  that a well-defined element of $H$, the maximal torus of $G$,
  corresponding to translations along geodesics in the
  $\PSL_2(\mathbb{R})$ case, can be attached to each edge of each
  triangle.

  \begin{quote}
    \emph{4. Coordinates can be assigned to each triple (or pairs of
      triples) of cosets.}
  \end{quote}

  To assign coordinates to configuration spaces, Fock--Goncharov use
  \defined{generalized minors} (see \cref{def:generalized-minor}). In
  the case of $\GL_n$, these correspond to shuffling rows and columns
  according to two permutations, then taking the upper $i \times i$
  minor. In the more general case, two words in the Weyl group of $G$
  are invoked and a coordinate associated to the $i^{\text{th}}$
  fundamental weight is used.

  By work of Lusztig, configuration spaces carry a positive structure
  via \defined{factorization coordinates} (see
  \cref{def:factorization-coords-xi}). By work of Fomin--Zelevinsky,
  generalized minors inherit this positive structure.

  \begin{quote}
    \emph{5. We must describe how the coordinates change under
      (oriented) reordering and retriangulation}
  \end{quote}

  A major result of the Fock--Goncharov program is that reordering of
  triangles (we restrict to orientation-preserving reorderings, which we
  refer to as \defined{rotation}) and retriangulation of quadrilaterals
  (which we refer to as a \defined{flip} of the diagonal) preserve this
  positive structure. All general retriangulations and reorderings can
  be obtained this way.

  \begin{quote}
    \emph{6. Hyperbolic structures are those for which all coordinates
      are positive.}
  \end{quote}

  Instead of hyperbolic structures, we are interested in points in
  higher Teichmüller spaces. Since the general moduli spaces carry
  positive structures, the sets of positive points
  $\mathcal{A}^{+}_{G,\Sigma}$ and $\mathcal{X}^{+}_{G,\Sigma}$ are
  well-defined when $G$ is over $\mathbb{R}$. These do, in fact,
  correspond to higher Teichmüller spaces or decorations of them (see
  \cref{sec:coords-to-representations}).

  \begin{quote}
    \emph{7. The representation $\rho : \pi_1(\Sigma) \to G$ can be
      reconstructed.}
  \end{quote}

  The representation $\rho(\gamma)$ can still be computed by
  $\mathcal{A}$- or $\mathcal{X}$-coordinates (again, see
  \cref{sec:coords-to-representations}). Here our restrictions on $G$
  being simply connected or centerless are necessary.

  So the Fock--Goncharov program holds beyond $\PSL_2(\mathbb{R})$. We
  now address the following question:

  \begin{quote}
    \emph{The positive structure on coordinates is preserved under
      retriangulation and reorientation, but how are those two
      operations realized on coordinates?}
  \end{quote}

  In the $A_1$ case, the cluster ensemble of \cref{fig:QA1-and-flip}
  provides the answer. In \cite{fockgoncharov2006}, Fock--Goncharov
  produced cluster ensembles for all types $A_n$. The quivers appear as
  triangular lattices, see \cref{sec:An-case} for an overview.
  Fock--Goncharov also provided descriptions for coordinate changes
  under the two key operations as sequences of mutations. The
  \defined{rotation} describes reordering of a triangle, and the
  \defined{flip} describes retriangulation of a quadrilateral.

  Fock--Goncharov predicted that $\mathcal{A}_{G,\Sigma}$ and
  $\mathcal{X}_{G,\Sigma}$ would carry cluster ensemble structures as
  well. To realize those structures, we need, we need
  \begin{itemize}
  \item
    A way to assign coordinates of $\Conf_4^{\ast}(G/K)$ to a triangle.
    These coordinates will be encoded in a cluster ensemble. We will
    call the coordinate assignment map $\conftoquiv$. When the group $G$
    is over $\mathbb{R}$, collections of coordinates will be
    $(\mathbb{R}^{\ast})^n$. Seeds with all coordinates positive will be
    the \defined{positive points}.
  \item
    A way to realize (orientable) symmetries of a triangle on those
    coordinates (the \defined{rotation}, see \cref{fig:short-rot}). The
    bottom map will be realized by a quiver mutation which we call
    $\murot$.
  \item
    A way to realize changes of triangulation on those coordinates (the
    \defined{flip}, see \cref{fig:short-flip}). The bottom map will be
    realized by a quiver mutation which we call $\muflip$.
  \item
    The maps $\murot$ and $\muflip$ should preserve the positive
    structure. That is, if a seed has positive coordinates, applying the
    rotation or the flip should not change that. Using generalized
    minors for coordinates is a way to preserve positivity.
  \end{itemize}

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.30\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/short-rot}

      \caption{The rotation.
        \label{fig:short-rot}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.50\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/short-flip}

      \caption{The flip.
        \label{fig:short-flip}
      }
    \end{subfigure}
    \caption{Retriangulation and reordering (for a group over
      $\mathbb{R}$).
      \label{fig:retriangulation-and-reordering}
    }
  \end{figure}
