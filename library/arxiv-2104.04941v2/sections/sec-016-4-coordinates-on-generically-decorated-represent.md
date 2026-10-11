---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-016-4-coordinates-on-generically-decorated-represent
section_title: "Coordinates on generically-decorated representations"
section_number: 4
pages: 15-23
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.945
---
\label{sec:reps-from-conf3star}

  Here we review \defined{decorations} of representations and define
  \defined{Fock--Goncharov coordinate structures}. For a representation
  $\rho$ and a chosen triangulation, a decoration of $\rho$ is a
  collection of flags for each simplex in the triangulation. These flags
  can recreate $\rho$, and have a canonical form that admits generalized
  minor coordinates. Fock--Goncharov coordinate structures will describe
  coordinates on these decorations.

  These decorations apply to surfaces, but also to $3$-manifolds with
  fixed ideal triangulations. We follow \cite{fockgoncharov2006} for the
  surface case and \cite{zickert2016} for the $3$-manifold case.

  
\subsection{Configurations and gluings}

  \label{sec:configurations-and-gluings}

  \begin{definition}
    \label{def:Conf_k_star}
    Let $G$ be a Lie group over $\mathbb{C}$, with sufficient choices to
    define $G_0$ as in \cref{def:gaussian-decomposition}. Let $K$ be a
    subgroup of $G$ (we will ultimately use $N_{+}$). A tuple of cosets
    $(g_0K, g_1K, \dotsc, g_{m}K)$ is \defined{sufficiently generic} if
    each $g_i^{-1} g_j \in \lifttoG{w_0}G_0$.

    Such a tuple corresponds to a labeling of edges in an oriented
    $m$-simplex by elements of $\lifttoG{w_0}G_0$, as in
    \cref{fig:labeled-sufficiently-generic-simplex}, with the edge from
    $i$ to $j$ (assuming $j>i$) labeled by $g_i^{-1} g_j$.

    The variety of such sufficiently generic $(m+1)$-tuples is the
    \defined{configuration space} $\Conf_{m+1}(G/K)$. Identifying
    elements which differ by left-multiplication of $G$ yields the
    variety $\Conf_{m+1}^{\ast}(G/K)$.
  \end{definition}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/labeled-sufficiently-generic-simplex}

    \caption{Oriented $2$- and $3$-simplices labeled by elements of
      $\Conf_3^{\ast}(G/K)$ and $\Conf_4^{\ast}(G/K)$.
      \label{fig:labeled-sufficiently-generic-simplex}
    }
  \end{figure}

  \begin{definition}
    \label{def:peripheral-stuff}
    Let $M$ be a compact manifold (possibly with boundary) and $G$ a Lie
    group over $\mathbb{C}$, with $K$ a subgroup of $G$. A subgroup $L$
    of $\pi_1(M)$ is \defined{peripheral} if there is a boundary
    component $D$ of $M$ such that $L$ is induced by the inclusion of
    $D$; that is $\iota^{\ast}(\pi_1(D)) = L$.

    A representation $\rho : \pi_1(M) \to G$ is a
    \defined{$(G,K)$-representation} if, for every peripheral subgroup
    $L$, the image $\rho(L)$ is a conjugate of $K$. In the case $K =
    N_{+}$, the term \defined{boundary-unipotent} is used. If $K =
    B_{+}$, then $\rho$ is \defined{boundary-borel}.
  \end{definition}

  \begin{lemma}[{\cite[Lemma~5.8, Proposition~5.9]{zickert2016}}]
    \label{lem:canonical-form-for-conf_3_star}
    There is an isomorphism of varieties \[ \Conf_3^{\ast}(G/N_{+})
      \cong H^3 \times_{H} (N_{-} \cap \lifttoG{w_0} G_0). \] The fiber
    product $\times_{H}$ means that for $(h_1, h_2, h_3, u) \in
    \Conf_3^{\ast}(G/N_{+}))$, we have \[ [\lifttoG{w_0}^{-1} u]_{0} =
      (w_0(h_3 h_1) h_2)^{-1}. \]
  \end{lemma}

  Thus we will often write $(h_1, h_2, h_3, u)$ for $\alpha$, which has
  one representative $(N_{+}, \lifttoG{w_0} h_1 N_{+}, u w_0(h_1) h_2
  s_G N_{+})$. We refer to these as \defined{canonical forms} for
  $\Conf_3^{\ast}(G/N_{+})$.

  \begin{definition}
    \label{rem:canonical-form-for-B-cosets}
    By expanding $N_{+}$ to $B_{+}$ above, we obtain that $\alpha \in
    \Conf_3^{\ast}(G/B_{+})$ can be given as $(B_{+}, \lifttoG{w_0}
    B_{+}, u B_{+})$. Choose the unique $u_x$ such that, for all $k$,
    the minor $\genminoryz{w_k}{}{1}(u_x) = 1$. This element $u_x$ is
    the \defined{canonical form} for $\alpha$.

    For an arbitrary $(B_{+}, \lifttoG{w_0} B_{+}, u B_{+})$, by
    expanding \cref{def:generalized-minor} there is a unique (up to the
    center of $G$) element $h$ such that $h u h^{-1}$ is the canonical
    form $u_x$. When $G$ is centerless, we denote this element by
    $n(u)$.
  \end{definition}

  \begin{proposition}
    \label{prop:Phi-Psi-and-rot}
    This summarizes \cite[Proposition~5.10]{zickert2016}. Let $\alpha
    \in \Conf_3^{\ast}(G/N_{+})$ be given by $\alpha = (h_1, h_2, h_3,
    u)$. Recall $\Phi$ and $\Psi$ of \cref{def:phi-and-psi}. The map \[
      \operatorname{rot}: \Conf_3^{\ast}(G/N_{+}) \to
      \Conf_3^{\ast}(G/N_{+}), \qquad (g_0 N_{+}, g_1 N_{+}, g_2 N_{+})
      \mapsto (g_2 N_{+}, g_0 N_{+}, g_1 N_{+}) \] is given, in this
    form, via \[ \operatorname{rot} : (h_1, h_2, h_3, u) \mapsto (h_3,
      h_1, h_2, h_2^{-1} (w_0(h_1))^{-1} (\Phi \Psi \Phi \Psi)(u)
      (w_0(h_1)) h_2). \]
  \end{proposition}

  \begin{definition}
    \label{def:gluing-configurations}
    This summarizes \cite[Section~2.2.1]{zickert2016}. We define and
    $\Conf_3^{\ast}(G/N_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/N_{+})$
    by gluing copies of $\Conf_3^{\ast}(G/N_{+})$ along matching copies
    of $\Conf_2^{\ast}(G/N_{+})$. Specifically,
    \begin{align*}
      \Conf_3^{\ast}(G/N_{+}) \times_{02}^{s_G} \Conf_3^{\ast}(G/N_{+}) = \Set{ \substack{(g_0 s_G N_{+}, g_1 N_{+}, g_2 N_{+}),\\ (g_0 N_{+}, g_2 N_{+}, g_3 N_{+})} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) \in \Conf_4^{\ast}(G/N_{+}) } \\
      \Conf_3^{\ast}(G/N_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/N_{+}) = \Set{ \substack{(g_1 N_{+}, g_2 N_{+}, g_3 N_{+}),\\ (g_0 N_{+}, g_1 s_G N_{+}, g_3 N_{+})} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) \in \Conf_4^{\ast}(G/N_{+}) } \\
    \end{align*}
    We also define the following maps from $\Conf_4^{\ast}(G/N_{+})$ to
    $\Conf_{3}^{\ast}(G/N_{+}) \times_{jk}^{s_G}
    \Conf_3^{\ast}(G/N_{+})$ for $jk = 02, 13$:
    \begin{align*}
      \Psi_{02} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) &\mapsto \substack{(g_0 s_G N_{+}, g_1 N_{+}, g_2 N_{+}),\\ (g_0 N_{+}, g_2 N_{+}, g_3 N_{+})} \\
      \Psi_{13} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) &\mapsto \substack{(g_1 N_{+}, g_2 N_{+}, g_3 N_{+}),\\ (g_0 N_{+}, g_1 s_G N_{+}, g_3 N_{+})}
    \end{align*}

    See part of \cref{fig:QC2-and-flip} for a graphical depiction.

    In the surface case, these correspond to the two different ways of
    triangulating a quadrilateral. The act of retriangulating a single
    quadrilateral this way is called a ``flip''. In the $3$-manifold
    case, these correspond to decomposing a tetrahedron's vertices into
    the two triangles' worth.
  \end{definition}

  \begin{remark}
    \label{rem:purpose-of-sG}
    The element $s_G$ is in the center of $G$, so is only relevant for
    $N_{+}$-cosets. Its purpose is to allow the quiver amalgamation (see
    \cref{def:dv-dh-construction} ahead) to agree with the
    identification of elements of $\Conf_3^{\ast}(G/N_{+})$ along a copy
    of $\Conf_2^{\ast}(G/N_{+})$.

    To see this, note that \cref{fig:dv-construction} shows identifying
    a $0$--$2$ edge with a $0$--$1$ edge, and \cref{fig:dh-construction}
    identifes a $0$--$2$ edge with a $1$--$2$ edge. Since the associated
    elements of $\Conf_2^{\ast}(G/N_{+})$ are oriented via the cyclic
    ordering on $(0,1,2)$, this quiver amalgamation corresponds to
    identifying elements of $\Conf_2^{\ast}(G/N_{+})$ ``backwards''.

    This use of $s_G$ is why $\mathcal{A}_{G,\Sigma}$ is the moduli
    space of \emph{twisted}, decorated representations from
    $\pi_1(\Sigma)$ into $G$. See \cite[Section~8.6]{fockgoncharov2006}
    and \cite[Section~2.3]{zickert2016} for more details.
  \end{remark}

  
\subsection{Triangular quivers and Fock--Goncharov coordinate
    structures}

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

  
\subsection{From coordinates to representations}

  \label{sec:coords-to-representations}

  The Fock--Goncharov program for defining $\mathcal{A}_{G,\Sigma}$ and
  $\mathcal{X}_{G,\Sigma}$ works for any compact, oriented $\Sigma$ with
  boundary components. In the case that the boundary consists of
  punctures, we can describe reconstructing a representation from a
  point in the moduli space. We start with the $\mathcal{A}$-coordinate
  version due to complications in technicalities, referring to
  \cite[Section~8]{fockgoncharov2006}, \cite[Section~6]{zickert2016} for
  more details.

  We start with an ideal triangulation $\triang$ of $\Sigma$, together
  with a quiver $Q$ and seed torus $\seedAtorus_Q$ for each triangle in
  $\triang$, amalgamated together.

  First, we truncate the triangulation, as in
  \cref{fig:truncated-simplex}. We will associate an element of $G$ to
  each directed edge: elements on the long edges will be called
  $\alpha_{ij}$, and elements on short edges will be called
  $\beta_{ijk}$. The local labeling of vertices by $0$, $1$, and $2$ is
  determined by triangularity (see \cref{def:triangular-quiver}) of the
  quiver $Q$.

  \begin{figure}[h]
    \centering
    \begin{subfigure}[t]{0.40\textwidth}
      \centering
      \includestandalone[mode=image|tex]{fig/truncated-simplex}

      \caption{A truncated simplex. ``Long'' edges are in black,
        ``short'' edges are in blue.
        \label{fig:truncated-simplex}
      }
    \end{subfigure}
    ~ \hspace{0.05\textwidth} ~
    \begin{subfigure}[t]{0.40\textwidth}
      \centering
      \includestandalone[mode=image|tex]{fig/doubly-truncated-simplex}

      \caption{A doubly-truncated simplex. ``Long'' edges are in black,
        ``middle'' edges are in blue, ``short'' edges are in red.
        \label{fig:doubly-truncated-simplex}
      }
    \end{subfigure}
    \caption{Truncations of $\triang$. The left is used for
      $\mathcal{A}$-coordinates, the right for
      $\mathcal{X}$-coordinates.}
  \end{figure}

  To compute $\rho(\gamma)$, we homotope $\gamma$ to follow these edges,
  then multiply together the elements in the order given by $\gamma$.
  When the orientation of $\gamma$ disagrees with the orientation of the
  edge, we use the inverse of the attached element.

  All that remains is to give a formula for the $\alpha_{ij}$ and
  $\beta_{ijk}$.

  \begin{itemize}
  \item
    We start with an element in $\seedAtorus_Q$; the
    $\mathcal{A}$-coordinates of $Q$.
  \item
    Since we have a Fock--Goncharov coordinate structure, we may apply
    $(\conftoquiv)^{-1}$. This gives an explicit element of
    $\Conf_3^{\ast}(G/N_{+})$. It is most conveniently expressed as
    $(h_1, h_2, h_3, u)$.
  \item
    Set
    \begin{align*}
      \alpha_{01} &= \lifttoG{w_0} h_1 & u_0 &= u & \beta_{201} &= \left( w_0(h_1) h_2 \right)^{-1} (\Psi \Phi \Psi)(u_0) \left( w_0(h_1) h_2 \right) \\
      \alpha_{12} &= \lifttoG{w_0} h_2 & u_1 &= \left( w_0(h_1) h_2 \right)^{-1} (\Phi \Psi)^2(u_0) \left( w_0(h_1) h_2 \right) & \beta_{120} &= \left( w_0(h_2) h_3 \right)^{-1} (\Psi \Phi \Psi)(u_1) \left( w_0(h_2) h_3 \right) \\
      \alpha_{20} &= \lifttoG{w_0} h_3 & u_2 &= \left( w_0(h_1) h_2 \right)^{-1} (\Phi \Psi)^2(u_1) \left( w_0(h_1) h_2 \right) & \beta_{012} &= \left( w_0(h_3) h_1 \right)^{-1} (\Psi \Phi \Psi)(u_2) \left( w_0(h_3) h_1 \right).
    \end{align*}
  \end{itemize}

  \begin{remark}
    Since all $\beta_{ijk}$ are assigned elements of $N_{+}$, and any
    peripheral $\gamma$ can be homotoped to follow only short edges, any
    $\rho$ constructed this way is boundary-unipotent.
  \end{remark}

  Also, given a point in $\mathcal{X}^{+}_{G,\Sigma}$, we can
  reconstruct a boundary-borel representation $\rho$ (up to conjugation)
  as follows. We refer to \cite[Section~6]{fockgoncharov2006},
  \cite[Section~9]{ggz2015} for more details.

  Again, we start with an ideal triangulation $\triang$ of $\Sigma$,
  together with a quiver $Q$ and seed torus $\seedXtorus_Q$ for each
  triangle in $\triang$. Instead of triangulating, however, we doubly
  triangulate, as in \cref{fig:doubly-truncated-simplex}. To compute
  $\rho(\gamma)$, we homotope $\gamma$ to follow the edges, then
  multiply $\alpha_{ij}$, $\beta_{ijk}$, or $\gamma_{ijk}$ (or their
  inverses) as appropriate.

  \begin{itemize}
  \item
    We start with elements of $\seedXtorus_Q$.
  \item
    Taking $(\conftoquiv)^{-1}$ gives elements of
    $\Conf_3^{\ast}(G/B_{+})$ for each triangle. To compute edges at a
    particular triangle, assume its flags are $(g_0 B_{+}, g_1 B_{+},
    g_2 B_{+}) = (B_{+}, \lifttoG{w_0} B_{+}, u_x B_{+})$, and that the
    neighboring triangles have vertices $(0, 1, 3)$, $(1, 2, 4)$, and
    $(2, 0, 5)$ (with cosets $g_3 B_{+}$, $g_4 B_{+}$, and $g_5 B_{+}$).
  \item
    Recall $n(u)$ of \cref{rem:canonical-form-for-B-cosets}. The element
    assignments are
    \begin{align*}
      \alpha_{01} &= \lifttoG{w_0} & \alpha_{12} &= \lifttoG{w_0} & \alpha_{20} &= \lifttoG{w_0} \\
      \beta_{012} &= \Phi^{-1}(u_x) & \beta_{120} &= \lifttoG{w_0}^{-1} u_x^{-1} \lifttoG{w_0} & \beta_{201} &= \left( \Phi^{-1}(u_x^{-1}) \right)^{-1} \\
      \gamma_{012} &= n(g_3) & \gamma_{120} &= n([\lifttoG{w_0} u_x^{-1} g_4]_{-}) & \gamma_{201} &= n([\lifttoG{w_0} [\lifttoG{w_0}^{-1} u_x^{-1}]_{-}^{-1} \lifttoG{w_0}^{-1} u_x^{-1} g_5 ]_{-}]_{-}) \\
      \gamma_{102} &= \left( n([\lifttoG{w_0} g_3]_{-}) \right)^{-1} & \gamma_{210} &= \left( n(u_x^{-1} g_4) \right)^{-1} & \gamma_{021} &= \left( n([\lifttoG{w_0} [\lifttoG{w_0}^{-1} u_x]_{-} \lifttoG{w_0}^{-1} g_5 ]_{-}) \right)^{-1} \\
    \end{align*}
  \end{itemize}

  \begin{remark}
    All middle edges are assigned elements of $N_{+}$, and all short
    edges are assigned elements of $H$. Therefore any peripheral loop
    lies in $B_{+}$ and $\rho$ is boundary-borel.
  \end{remark}

  \begin{remark}
    Since $n(u)$ may require taking square roots, the field over which
    the $\mathcal{X}$-coordinates are defined may need to be extended in
    order to define $\rho$.
  \end{remark}

  Since we can now explicitly interpret points in these moduli spaces as
  representations, we describe the positivity conditions of higher
  Teichmüller spaces.

  \begin{definition}
    \label{def:positive-structure}
    Let $N_{+}$ be a maximal unipotent subgroup of $G$. Then
    \cref{def:factorization-coords-xi} gives coordinate charts on
    $N_{+}$ for each presentation of $w_0$. These charts are the
    \defined{positive structure} on $N_{+}$. The elements of $N_{+}$
    which have coordinates entirely in $\mathbb{R}_{>0}$ for all these
    charts are the \defined{positive part} of $N_{+}$.

    The maps $\chi_{\fundamentalweight_k}$ of
    \cref{def:root-space-decomposition} are also a \defined{positive
      structure} on the maximal torus $H$ of $G$. Again, the
    \defined{positive part} consists of the elements which have
    coordinates in $\mathbb{R}_{>0}$ by the positive structure.

    By \cite[Section~8.1]{fockgoncharov2006}, together with the
    canonical form of \cref{lem:canonical-form-for-conf_3_star}, these
    provide a \defined{positive structure}, and a \defined{positive
      part}, of $\Conf_3^{\ast}(G/N_{+})$. There is also a completely
    analogous positive structure on $\Conf_3^{\ast}(G/B_{+})$ following
    \cite[Section~5.5]{fockgoncharov2006}.
  \end{definition}

  \begin{remark}
    Generalized minors are compatible with these positive structures, as
    from \cite[Theorem~5.1]{fockgoncharov2006}. Therefore, positive
    points in the flag varieties $\Conf_3^{\ast}(G/K)$ are exactly those
    points for which all $\mathcal{A}$- and $\mathcal{X}$-coordinates in
    the cluster ensemble are in $\mathbb{R}_{>0}$.
  \end{remark}

  \begin{definition}
    \label{def:teich-plus}
    The space $\teich^{+}(\Sigma)$ is Teichmüller space, together with
    choices of orientation for non-cuspidal boundary components. For a
    surface $\Sigma$ with $n \ge 0$ boundary circles $b_1, \dotsc, b_n$,
    define \[ \teich^{+}(\Sigma) = \set{(p, \epsilon_1, \dotsc,
        \epsilon_n) : p \in \teich(S), \epsilon_i = \pm 1}, \] where
    $\epsilon_i$ is positive to denote that the chosen orientation of
    $b_i$ agrees with that naturally induced by $\Sigma$.
  \end{definition}

  \begin{remark}
    When $\Sigma$ has only cuspidal boundary components,
    $\teich^{+}(\Sigma) = \teich(\Sigma)$.
  \end{remark}

  \begin{definition}
    When $G$ is centerless, we may repeat the above construction, but
    take the $\mathcal{X}$-coordinates of the cluster ensemble. This
    gives the moduli space $\mathcal{X}_{G,\Sigma}$ of \defined{framed,
      $G$-local systems} on $\Sigma$ by
    \cite[Section~2.1]{fockgoncharov2006}. The $\mathbb{R}_{>0}$ points
    also give $\mathcal{X}^{+}_{G,\Sigma}$. This space is identified
    with $\teich^{+}(\Sigma)$.

    That $\teich^{+}(\Sigma)$ appears instead of $\teich(\Sigma)$ is
    rather a technicality. Restricting our attention to orderings of
    ideal triangulations that agree with the surface's natural
    orientation restrictrs $\teich^{+}(\Sigma)$ to a set we can
    canonically identify with $\teich(\Sigma)$.
  \end{definition}

  \begin{definition}
    When $G$ is simply connected, choose an ordered, oriented
    triangulation of $\Sigma$. Associate a copy of $Q$ to each triangle,
    and amalgamate all the quivers together by identifying shared edge
    vertices between triangles. The $\mathcal{A}$-coordinates of the
    cluster ensemble form the moduli space $\mathcal{A}_{G,\Sigma}$.

    By \cite[Section~8.6]{fockgoncharov2006} the $\mathbb{C}$-points of
    this moduli space parameterize \defined{twisted, decorated
      representations} into $G$. The $\mathbb{R}_{>0}$-points give
    $\mathcal{A}^{+}_{G,\Sigma}$, a \defined{higher Teichmüller space}.
    These correspond to flag varieties such that all generalized minors
    are strictly positive.
  \end{definition}

  These moduli spaces have further interpretations and properties,
  explored in \cite{fockgoncharov2006}, \cite{fockgoncharov2006_2},
  \cite{fockgoncharov2009}, \cite{goncharovshen2018}, etc.
