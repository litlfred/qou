---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-020-43-from-coordinates-to-representations
section_title: "From coordinates to representations"
section_number: 4.3
pages: 21-23
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.996
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
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
