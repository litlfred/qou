---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-019-42-triangular-quivers-and-fockgoncharov-coordina
section_title: "Triangular quivers and Fock–Goncharov coordinate structures"
section_number: 4.2
pages: 17-21
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.922
latex_coverage_ratio: 0.987
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
We want a variety that is independent of the choice of triangulation.
  Therefore, we will need coordinate change maps corresponding to
  changes in triangulation (the rotation of individual triangles, or the
  quadrilateral flip).

  Here we define the outputs of the algorithm of \cref{sec:main-result}.
  These are \defined{triangular quivers} (see
  \cref{def:triangular-quiver}), which have vertices on edges and in the
  interior. If, moreover, these quivers admit a rotation and a flip as
  quiver mutations, they have \defined{triangulation-compatible
    symmetry} (see \cref{def:tcs}). And if we can then associate the
  $\mathcal{A}$- and $\mathcal{X}$-coordinates to coordinates on
  $\Conf_3^{\ast}(G/N_{+})$ and $\Conf_3^{\ast}(G/B_{+})$, we have a
  \defined{Fock--Goncharov coordinate structure} (see \cref{def:fgcs}).

  \begin{definition}
    \label{def:dynkin-type}
    Let $D$ be a Dynkin diagram, with associated Cartan matrix
    $\begin{bmatrix}a_{ij}\end{bmatrix}$. A quiver $Q$ is of
    \defined{Dynkin type $D$} if $\abs{\epsilon(i,j)} = -a_{ji}$ (for $i
    \ne j$) and $\sigma(i,j)$ takes values only in $\set{-1, 0, +1}$.
    The undirected graph of $Q$ carries the adjacency information of
    $D$, and the vertex weights carry the edge details.

    $Q$ is of \defined{half-Dynkin type $D$} if $2Q$, the quiver
    obtained by multiplying all edge weights by $2$, is of Dynkin type
    $D$.
  \end{definition}

  \begin{definition}
    \label{def:Coxeter-elt-induced-by-quiver}
    Let $D$ be a quiver of Dynkin type (with no oriented cycles). We can
    obtain a particular Coxeter element $c$ by requiring that
    $s_{\alpha_i}$ appear before $s_{\alpha_j}$ in $c$ if $\sigma(i, j)
    > 0$ in $D$. Such a $c$ is \defined{induced} by the quiver $D$.
  \end{definition}

  \begin{definition}
    \label{def:tree-like-quiver}
    A quiver of Dynkin type is \defined{tree-like} if, as an unoriented
    graph, it is a tree, and the directed edges always point away from
    the root. In this case, there is a partition of vertices $\set{T_0,
      T_1, \dotsc, T_m}$ such that the vertices in $T_i$ are of distance
    $i$ (in the unoriented graph) from the root vertex.

    Note that Coxeter elements induced by tree-like Dynkin quivers
    always take the form \[ c = \left( \prod_{\alpha \in T_0} s_{\alpha}
      \middle) \middle( \prod_{\alpha \in T_1} s_{\alpha} \middle)
      \dotsb \middle( \prod_{\alpha \in T_m} s_{\alpha} \right). \]
  \end{definition}

  \begin{definition}
    \label{def:well-rooted-tree-like-quiver}
    The involution $\sigma_G$ acts on quivers of Dynkin type in the same
    way that it would act on the Dynkin diagram as in
    \cref{rem:sigma_G-action-on-Dynkin-diagram}. A tree-like quiver $Q$
    of Dynkin type $D$ is \defined{well-rooted} if this action of
    $\sigma_G$ preserves all $T_i$ partitions. See
    \cref{fig:well-rooted-quivers}.
  \end{definition}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/well-rooted-E6}

    \caption{A non-well-rooted quiver (left) and a well-rooted quiver
      (right) for $E_6$.
      \label{fig:well-rooted-quivers}
    }
  \end{figure}

  \begin{remark}
    In the most cases, the quiver obtained by applying a na\"ive
    ``left-to-right'' ordering to the common presentation of the Dynkin
    diagram is well-rooted. The pathological case is $E_6$.
  \end{remark}

  \begin{definition}
    \label{def:triangular-quiver}
    A quiver $Q$ is \defined{triangular} if, for a standard $2$-simplex
    $\sigma$ with vertices $0, 1, 2$, each vertex in $Q$ is associated
    to the interior of some sub-simplex $\sigma'$ of $\sigma$.
    $\facemap_{\sigma'}(Q)$ is defined to be the sub-quiver of $Q$
    obtained by deleting all vertices except those that lie on the
    interior of $\sigma$. See \cref{fig:visually-triangular}.

    In other words, a triangular quiver $Q$ is one that can be split
    into sub-quivers:
    \begin{itemize}
    \item
      $\facemap_{(0,1)}(Q)$, $\facemap_{(1,2)}(Q)$, and
      $\facemap_{(0,2)}(Q)$: the vertices on the edges of the triangle.
    \item
      $\facemap_{(0,1,2)}(Q)$: the vertices in the interior of the
      triangle.
    \end{itemize}

    We label the vertices on the $\facemap_{(0,1)}$ edge's vertices by
    $A_i$, those on the $\facemap_{(1,2)}$ edge by $B_i$, and those on
    the $\facemap_{(0,2)}$ edge by $C_i$.

    An isomorphism $\varphi$ of triangular quivers must preserve these
    classifications: $\facemap_{\Delta}(\varphi(Q)) =
    \varphi(\facemap_{\Delta}(Q))$.
  \end{definition}

  \begin{figure}[h]
    \centering
    \includestandalone[mode=image|tex]{fig/visually-triangular}

    \caption{A triangular quiver (this one is associated to a Lie group
      of type $C_2$).
      \label{fig:visually-triangular}
    }
  \end{figure}

  \begin{definition}
    \label{def:dv-dh-construction}
    Let $Q$ be a triangular quiver such that the edge sub-quivers are
    isomorphic as sets of vertices. That is, fix isomorphisms $\varphi:
    \facemap_{(0,1)}(Q) \cong \facemap_{(0,2)}(Q)$ and $\psi :
    \facemap_{(0,2)}(Q) \cong \facemap_{(1,2)}(Q)$. Then we define
    \begin{itemize}
    \item
      $\Qdv$ as the quiver obtained by identifying two copies of $Q$
      along $\varphi$, and
    \item
      $\Qdh$ as the quiver obtained by identifying two copies of $Q$
      along $\psi$.
    \end{itemize}
    In performing the identification of vertices, edge weights are
    added. They need not agree, and in particular might cancel; see
    \cref{fig:dv-construction,fig:dh-construction}.
  \end{definition}

  This is a special case of \defined{amalgamation} as defined in
  \cite[\S 2.2]{fockgoncharov2006_2}.

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.40\textwidth}
      \centering \includestandalone[mode=image|tex,width=\textwidth]{fig/dv-construction}

      \caption{Construction of $\Qdv$ (for $G$ of type $C_2$).
        \label{fig:dv-construction}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.40\textwidth}
      \centering \includestandalone[mode=image|tex,width=\textwidth]{fig/dh-construction}

      \caption{Construction of $\Qdh$ (for $G$ of type $C_2$).
        \label{fig:dh-construction}
      }
    \end{subfigure}
    \caption{Amalgamating triangular quivers.}
  \end{figure}

  \begin{definition}
    \label{def:tcs}
    A quiver \defined{has triangulation-compatible symmetry} if
    \begin{enumerate}
    \item
      \label{def:tcs-1}
      It is triangular by \cref{def:triangular-quiver},
    \item
      \label{def:tcs-rot}
      There is a quiver mutation $\murot$ which is an isomorphism of
      triangular quivers between $Q$ and $Q'$, where $Q'$ is obtained
      from $Q$ by permuting simplex indices from $(0,1,2)$ to $(2,0,1)$.
    \item
      \label{def:tcs-flip}
      There is a quiver mutation $\muflip$ which transforms $\Qdv$ to
      $\Qdh$.
    \end{enumerate}
  \end{definition}

  If $\triang$ is an oriented triangulation of a surface, and $\triang'$
  is an orientation-preserving retriangulation of $\triang$, then
  inscribing $Q$ in each simplex of $\triang$ and $\triang'$ and
  amalgamating along edges results in two quivers that differ by some
  sequence of $\murot$ and $\muflip$. Therefore, if the cluster
  variables of $Q$ are coordinates for the representation variety, the
  existence of $\murot$ and $\muflip$ will (eventually) show the variety
  to be independent of the specific choice of triangulation.

  \begin{definition}
    \label{def:fgcs}
    Fix a semisimple Lie group $G$ over $\mathbb{C}$ with a fixed
    maximal torus $H$ and a maximal unipotent subgroup $N_{+}$, with
    $B_{+} = HN_{+}$. A quiver $Q$ carries a \defined{Fock--Goncharov
      coordinate structure for $G$ } if
    \begin{enumerate}
    \item
      \label{def:fgcs-1}
      $Q$ has triangulation-compatible symmetry as in \cref{def:tcs}.
    \item
      \label{def:fgcs-2}
      Each of the edge sub-quivers of $Q$ are of half-Dynkin type for
      $G$, as by \cref{def:dynkin-type}, and the isomorphisms $\varphi$
      and $\psi$ of \cref{def:dv-dh-construction} identify vertices that
      come from the same nodes in the Dynkin diagram.
    \item
      \label{def:fgcs-M-is-birational-equivalence}
      There exists a map $\conftoquiv : \Conf_3^{\ast}(G/N_{+}) \to
      \seedAtorus_Q$, which is a birational equivalence.
    \item
      \label{def:fgcs-rot-works}
      Moreover, $\conftoquiv$ respects the rotation. That is, the
      following diagrams commute:

      {\centering
        \begin{tikzcd}
          \Conf_3^{\ast}(G/N_{+}) \ar[r, "\conftoquiv"] \ar[d, "\operatorname{rot}"] & \seedAtorus_Q \ar[d, "\murotind"] &
          \Conf_3^{\ast}(G/B_{+}) \ar[r, "\conftoquiv"] \ar[d, "\operatorname{rot}"] & \seedXtorus_Q \ar[d, "\murotind"] \\
          \Conf_3^{\ast}(G/N_{+}) \ar[r, "\conftoquiv"] & \seedAtorus_{\murot(Q)} &
          \Conf_3^{\ast}(G/B_{+}) \ar[r, "\conftoquiv"] & \seedXtorus_{\murot(Q)}
        \end{tikzcd}

      } with $\operatorname{rot} : (g_0 K, g_1 K, g_2 K) \mapsto (g_2 K,
      g_0 K, g_1 K)$ (see also \cref{fig:QC2-and-rot}).
    \item
      \label{def:fgcs-flip-works}
      Moreover, $\conftoquiv$ respects the flip. That is, the following
      diagrams commute:

      {\centering
        \begin{tikzcd}
          \Conf_3^{\ast}(G/N_{+}) \times_{02}^{s_G} \Conf_3^{\ast}(G/N_{+}) \ar[r, "\conftoquiv"] \ar[d, "\Psi_{13} \circ \Psi_{02}^{-1}"] & \seedAtorus_{\Qdv} \ar[d, "\muflipind"] &
          \Conf_3^{\ast}(G/B_{+}) \times_{02}^{s_G} \Conf_3^{\ast}(G/B_{+}) \ar[r, "\conftoquiv"] \ar[d, "\Psi_{13} \circ \Psi_{02}^{-1}"] & \seedXtorus_{\Qdv} \ar[d, "\muflipind"] \\
          \Conf_3^{\ast}(G/N_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/N_{+}) \ar[r, "\conftoquiv"] & \seedAtorus_{\Qdh} &
          \Conf_3^{\ast}(G/B_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/B_{+}) \ar[r, "\conftoquiv"] & \seedXtorus_{\Qdh}
        \end{tikzcd}

      } where $\Psi_{jk}$ are defined as in
      \cref{def:gluing-configurations} (see also
      \cref{fig:QC2-and-flip}).
    \end{enumerate}
  \end{definition}

  \begin{remark}
    By the map $p$ of \cref{def:cluster-ensemble}, $\conftoquiv$
    provides a map to $\seedXtorus_Q$. In fact, this map factors through
    $\Conf_3^{\ast}(G/B_{+})$. By abuse of notation, we also refer to
    this map as $\conftoquiv$ in
    \cref{def:fgcs-rot-works,def:fgcs-flip-works}.
  \end{remark}

  \begin{example}
    \Cref{fig:QC2-and-rot,fig:QC2-and-flip} illustrate the last two
    demands: to move back and forth between $\Conf_{3}^{\ast}(G/N_{+})$
    and $\seedAtorus_{Q}$, or $\Conf_{4}^{\ast}(G/N_{+})$ and
    $\seedAtorus_{\Qdv}$ in terms of coordinates and quiver mutations.
  \end{example}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/QC2-and-rot}

    \caption{Quiver for type $C_2$, illustrating $\murotind \circ
      \conftoquiv = \conftoquiv \circ \operatorname{rot}$, with
      $\seedAtorus_Q$ depicted by a graph for $Q$.
      \label{fig:QC2-and-rot}
    }
  \end{figure}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/QC2-and-flip}

    \caption{Quiver for type $C_2$, illustrating $\muflipind \circ
      \conftoquiv = \conftoquiv \circ \Psi_{13} \circ \Psi_{02}^{-1}$.
      The tetrahedron shows the use of the flip in the $3$-manifold
      context.
      \label{fig:QC2-and-flip}
    }
  \end{figure}

  We can now restate \cref{thm:intro-main-result} as the following

  \begin{theorem}
    \label{thm:fgcs-exists}
    For a split semisimple simply-connected (or centerless) algebraic
    group $G$ over $\mathbb{Q}$, a quiver with a Fock--Goncharov
    structure exists.
  \end{theorem}

  We will mostly focus on the simple case. The semisimple case follows
  quickly as described in \cref{sec:products}. The construction for
  \cref{thm:fgcs-exists} is given in \cref{sec:main-result}.
