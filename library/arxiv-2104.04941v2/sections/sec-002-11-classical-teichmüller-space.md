---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-002-11-classical-teichmüller-space
section_title: "Classical Teichmüller space"
section_number: 1.1
pages: 3-4
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.933
latex_coverage_ratio: 0.984
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
We start by describing the Fock--Goncharov program for the case of Lie
  groups of type $A_1$. Let $\Sigma$ be a surface that admits ideal
  triangulation, for example the once-punctured torus $\Sigma =
  \Sigma_{1,1}$. The Fock--Goncharov moduli spaces will describe
  (decorated) Teichmüller space, so fix a hyperbolic structure on
  $\Sigma$. This can be described by an embedding of $\Sigma$'s
  fundamental domain in $\mathbb{H}^2$, as in
  \cref{fig:rho-by-fundamental-domain}.

  We now describe the two moduli spaces with seven key points.

  \begin{quote}
    \emph{1. The structure is determined by ideal points.}
  \end{quote}

  This follows from our ideal triangulation: all vertices are on
  $\partial \mathbb{H}^2$, and all edges between them are unique
  geodesics. See \cref{fig:sigma-3}.

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-3}

      \caption{Two different hyperbolic structures on $\Sigma$.
        \label{fig:sigma-3}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-6}

      \caption{Defining a representation by $B_{+}$-cosets.
        \label{fig:sigma-6}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-5}

      \caption{Defining a representation by $N_{+}$-cosets.
        \label{fig:sigma-5}
      }
    \end{subfigure}
    \caption{Representations of $\Sigma$ by cosets.
      \label{fig:rho-by-flags}
    }
  \end{figure}

  \begin{quote}
    \emph{2. We can identify ideal points with cosets of isometries in
      $\Isom^{+}(\mathbb{H}^2)$ that fix them.}
  \end{quote}

  The specific type of isometry determines which moduli space we create.
  \begin{itemize}
  \item
    We can consider $B_{+}$, a maximal borel subgroup, which fixes a
    point on $\partial \mathbb{H}^2$. Thus different cosets $g B_{+}$
    fix, and can be identified with, different points on $\partial
    \mathbb{H}^2$. See \cref{fig:sigma-6}.
  \item
    Replacing points with horocycles, we can consider $N_{+}$, a maximal
    unipotent subgroup, which fixes a horocycle in $\mathbb{H}^2$. See
    \cref{fig:sigma-5}.
  \end{itemize}

  \begin{quote}
    \emph{3. Choosing an ordered triangulation attaches a non-degenerate
      ordered triple of cosets to each triangle.}
  \end{quote}

  The non-degeneracy condition requires that the cosets be distinct, so
  that the triangle has three well-defined edges. Describing how the
  coordinates of Fock--Goncharov's moduli spaces change under alternate
  choices for the triangulation and the ordering is one of our primary
  concerns.

  \begin{quote}
    \emph{4. Coordinates can be assigned to each triple (or pair of
      triples) of cosets.}
  \end{quote}

  \begin{itemize}
  \item
    If we consider $B_{+}$-cosets, then the coordinates we attach to
    each edge resemble Thurston's shear coordinates (as described in
    e.g.\ \cite{bonahon1996}) along that identified edge, as the
    distance $d$ in \cref{fig:sigma-6}. Some of these coordinates need
    two triples to define. We will not focus on these in this
    introduction.
  \item
    If we consider $N_{+}$-cosets, then the portion of each geodesic
    between horocycles has finite length. These are equivalent to
    Penner's $\lambda$-lengths in his parametrization of decorated
    Teichmüller space of \cite{penner1987}. We associate to each
    triangle's edge the $\lambda$-length of its truncated geodesic as a
    coordinate. See \cref{fig:sigma-5}.
  \end{itemize}

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-7}

      \caption{Coordinate assignments for one ordered triangulation.
        \label{fig:sigma-7}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-8}

      \caption{\cref{fig:sigma-7} under reordering.
        \label{fig:sigma-8}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.25\textwidth}
      \centering \includestandalone[mode=image|tex]{fig/sigma-9}

      \caption{\cref{fig:sigma-7} under retriangulation.
        \label{fig:sigma-9}
      }
    \end{subfigure}
    \caption{Coordinates by $N_{+}$-cosets under reordering and
      retriangulation.
      \label{fig:rotation-and-flip-on-A-coords}
    }
  \end{figure}

  In our example, we label the edges $a$, $b$, and $e$ as in
  \cref{fig:sigma-7} (identified edges necessarily have the same
  $\lambda$-length). Using the $(0 \to 1,1 \to 2,2 \to 0)$-ordering on a
  triangle's edges, the coordinates we obtain are $(a,b,e)$ on the left
  and $(e,a,b)$ on the right.

  \begin{quote}
    \emph{5. We must describe how the coordinates change under
      (oriented) reordering and retriangulation.}
  \end{quote}

  In this $A_1$ case, reordering has a trivial effect on the
  coordinates. If we rename $g_0$, $g_1$, $g_2$, $g_3$, but do not
  change their values, we merely rearrange the coordinates following the
  new cyclic ordering on the triangle's edges. The coordinates defined
  by \cref{fig:sigma-8} are $(b,e,a)$ on the left and $(a,b,e)$ on the
  right.

  The retriangulation has a more interesting effect, as shown in
  \cref{fig:sigma-9}. The coordinates we obtain are $(b,a,f)$ for the
  top and $(a,f,b)$ for the bottom, but we need to describe the
  relationship of the new $\lambda$-length $f$ to the $\lambda$-lengths
  $a$, $b$, $e$. This is given by the classic Ptolemy's Theorem
  regarding lengths and diagonals of circumscribed quadrilaterals. In
  Euclidean space this is given by \cref{fig:ptolemy-euclidean}, and in
  hyperbolic space by \cref{fig:ptolemy-hyperbolic}. For our example,
  taking identifications into account, \[ ef = a^2 + b^2. \]

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.40\textwidth}
      \centering
      \includestandalone[mode=image|tex]{fig/ptolemy-euclidean}
      \caption{Ptolemy's Theorem for lengths in Euclidean space.
        \label{fig:ptolemy-euclidean}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.40\textwidth}
      \centering
      \includestandalone[mode=image|tex]{fig/ptolemy-hyperbolic}

      \caption{Ptolemy's Theorem for $\lambda$-lengths in hyperbolic
        space.
        \label{fig:ptolemy-hyperbolic}
      }
    \end{subfigure}
    \caption{Ptolemy's theorem: $ac + bd = ef$}
  \end{figure}

  \begin{quote}
    \emph{6. Hyperbolic structures are those for which all coordinates
      are positive.}
  \end{quote}

  The coordinates $a, b, e, f$ with the relation $ef = a^2 + b^2$
  describe an algebraic variety, but not every point corresponds to a
  hyperbolic structure. Those which do are exactly the points with
  positive coordinates, and thus positive geodesic lengths. This
  positivity need only be checked for one collection of coordinates: if
  $a$, $b$, and $e$ are all positive, then $f$ will be as well.

  \begin{quote}
    \emph{7. The representation $\rho : \pi_1(\Sigma) \to G$ can be
      reconstructed.}
  \end{quote}

  Via the coordinates we have mentioned, the holonomy $\rho(\gamma)$
  corresponding to this hyperbolic structure for $\gamma \in
  \pi_1(\Sigma)$ can be computed. See
  \cref{sec:coords-to-representations} for greater detail.

  The moduli space we have described using $N_{+}$-cosets is
  $\mathcal{A}_{\SL_2(\mathbb{R}),\Sigma}$, and points with positive
  coordinates correspond to points in Penner's decorated Teichmüller
  space for $\Sigma$. The moduli space derived from considering
  $B_{+}$-cosets is $\mathcal{X}_{\PGL_2(\mathbb{R}),\Sigma}$, and
  positive points correspond to points in Teichmüller space for
  $\Sigma$.
