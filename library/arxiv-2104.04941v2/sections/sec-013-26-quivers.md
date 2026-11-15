---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-013-26-quivers
section_title: "Quivers"
section_number: 2.6
pages: 11-12
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:quivers}

  We review quivers. These are graphical encodings of cluster algebras
  (specifically, those of geometric type), studied in
  \cite{fominzelevinsky2002}, \cite{fominzelevinsky2003}, and
  \cite{fominzelevinsky2005}. The quiver interpretation, first discussed
  in \cite{marshreinekezelevinsky2003}, is given a complete introduction
  in \cite{marsh2013}, which we follow. The only departure we need from
  Marsh's definition is to allow some edge weights to be in $\frac{1}{2}
  \mathbb{Z}$ instead of $\mathbb{Z}$. We also give a name to the
  symmetrized edge weights $\sigma(v,w)$, and encode the
  symmetrizability of edge weights into vertex weights $d_v$.

  \begin{definition}
    \label{def:quiver}
    A \defined{quiver} is a directed graph with no $1$- or $2$-cycles or
    multiple edges, with weights on edges and vertices. Vertex weights
    are in $\mathbb{N}_{>0}$, and edge weights are in
    $\frac{1}{2}\mathbb{Z}$. The edge weights are denoted $\sigma(v,w)$,
    and the vertex weights $d_v$. Also defined is the auxiliary quantity
    $\epsilon(v,w)$, by \[ \epsilon(v,w) = \frac{d_w}{\gcd(d_v,d_w)}
      \sigma(v,w). \] Vertices are either \defined{frozen} or
    \defined{non-frozen}, and edge weights are integral unless the edge
    is between two frozen vertices, in which case they are
    half-integral.
  \end{definition}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/QC2}

    \caption{A quiver. Larger vertices are of weight $2$, and dotted
      edges correspond to $\sigma(i,j) = \frac{1}{2}$.
      \label{fig:QC2}
    }
  \end{figure}

  \begin{remark}
    Almost all of the time, $\sigma(i,j)$ will lie in $\set{-1,0,+1}$.
    In this case, the edge weights $\sigma(i,j)$ are just the incidence
    matrix of the graph underlying the quiver.
  \end{remark}

  \begin{remark}
    The term \defined{quiver} occurs in other areas of literature as a
    multi-digraph. We use it here as a edge-weighted digraph with
    skew-symmetrizable adjacency matrix, encoding the exchange matrix of
    Fomin--Zelevinsky's cluster algebras.
  \end{remark}

  \begin{definition}
    For each non-frozen $v$, a quiver $\mu_{v}(Q)$ is defined. This is
    the \defined{mutation} of $Q$ at $v$. Edges in $\mu_{v}(Q)$ are
    defined by $\epsilon'(\cdot, \cdot)$, with \[ \epsilon'(x,y) =
      \begin{cases} \epsilon(x,y) & \text{if } \epsilon(x,v)
        \epsilon(v,y) \le 0, v \notin \set{x,y} \\ -\epsilon(x,y) &
        \text{if } v \in \set{x,y} \\ \epsilon(x,y) + |\epsilon(x,v)|
        \epsilon(v,y) & \text{if } \epsilon(x,v) \epsilon(v,y) > 0, v
        \notin \set{x,y}. \end{cases} \]
  \end{definition}

  Customarily, the vertex $v$ is renamed in $\mu_v(Q)$, e.g. to $v'$.
  This is because $\mu_v$ induces a map on the seed torus of $Q$ which
  changes the coordinate associated to $v$ (see
  \cref{def:cluster-ensemble}). For very long sequences, we will usually
  ignore the renamings for readability and think of $v$ as a vertex in a
  graph, not as a coordinate function.

  \begin{notation}
    \label{not:writing-mutations}
    Sequences of mutations are performed left to right: that is
    $\mu_{v,w} = \mu_{w} \circ \mu_{v}$. When subscripts would be
    awkward, we will also write mutation sequences as $\mu\set{v_1, v_2,
      \dotsc}$. We shall also employ $\prod_{v \in I} \mu_{v}$ to mean
    mutating at all vertices in $I$, in the order given by $I$.
  \end{notation}

  \begin{remark}
    When depicting quivers, we shall assume that all black edges have
    weight $\sigma = 1$, and gray, dashed edges have weight $\sigma =
    \frac{1}{2}$.

    Vertex weights will be depicted by the relative size of circles; we
    will only use weights 1, 2, and (only in the case of $G_2$) 3.
    Frozen vertices will be colored blue, but this will also be
    described in the text if at all relevant.

    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/quiver-mutation-example}

      \caption{Mutating the quiver of \cref{fig:QC2} at $v_{11}$.
        \label{fig:quiver-mutation-example}
      }
    \end{figure}

  \end{remark}
