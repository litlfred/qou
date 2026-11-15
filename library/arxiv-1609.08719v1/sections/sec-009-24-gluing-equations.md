---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-009-24-gluing-equations
section_title: "Gluing Equations"
section_number: 2.4
pages: 4-7
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.899
latex_coverage_ratio: 0.985
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
\label{subsec:gluing-equations}

Given a hyperbolic 3-manifold $M$ with cusps, the standard procedure
for determining $\vol(M)$ is to first triangulate $M$ into a
collection of simplices $\set{\Delta_i}$ (together with face
pairings), next to compute the cross ratio $z_i$ of each $\Delta_i$,
and finally to compute $\vol(M)$ by
equation~\ref{eq:sum-of-simplex-vols}. The first step is
well-understood: the manifolds included in the censuses of
\prog{SnapPy} include triangulations. The third step is a matter of
numerical approximation, but the second step deserves more
explanation. We present an overview of the \definedterm{gluing
  equations} here, and refer to \parencite{neumann-zagier} for a more
detailed description, including a treatment of gluing equations for
closed manifolds obtained by Dehn surgery.

Given a triangulation $\set{\Delta_i}$ of $M$, the standard method of
finding $\set{z_i}$ is to exploit the torus boundary components and
local Euclidean nature of the manifold to produce and solve a system
of equations in $\set{z_i}$. Equations~\ref{eq:cusp}, which arise from
torus boundary components, are the \definedterm{cusp equations}, and
equations~\ref{eq:edge}, which arise from local Euclideanness, are the
\definedterm{edge equations}. Together, they are the gluing equations.

Since, in the triangulation of $M$, a link component appears at the
vertices of each simplex, a torus can be determined by truncating the
simplices, then making edge identifications to match face
identifications, as in figure~\ref{fig:constructing_torus}.

\begin{figure}[h]
  \begin{tikzpicture}[framed]
    \coordinate (A) at (0.4,0);
    \coordinate (B) at (1.4,-0.6);
    \coordinate (C) at (2,0);
    \coordinate (D) at (2,2);
    \coordinate (A') at ($(A)!0.6!(D)$);
    \coordinate (B') at ($(B)!0.6!(D)$);
    \coordinate (C') at ($(C)!0.6!(D)$);

    \coordinate (E) at (4,-0.6);
    \coordinate (F) at (2.5,-0.6);
    \coordinate (G) at (3,0);
    \coordinate (H) at (3,2);
    \coordinate (E') at ($(E)!0.6!(H)$);
    \coordinate (F') at ($(F)!0.6!(H)$);
    \coordinate (G') at ($(G)!0.6!(H)$);

    \draw[dashed] (C) -- (A);
    \draw (A) -- (B) -- (C);
    \filldraw[opacity=0.1] (A') -- (B') -- (C') -- cycle;
    \draw (A') -- (B') -- (C') -- cycle;
    \draw (A) -- (A');
    \draw (B) -- (B');
    \draw (C) -- (C');
    \draw[dashed] (A') -- (D);
    \draw[dashed] (B') -- (D);
    \draw[dashed] (C') -- (D);

    \draw[dashed] (F) -- (G) -- (E);
    \draw (E) -- (F);
    \filldraw[opacity=0.1] (E') -- (F') -- (G') -- cycle;
    \draw (E') -- (F') -- (G') -- cycle;
    \draw (E) -- (E');
    \draw (F) -- (F');
    \draw[dashed] (G) -- (G');
    \draw[dashed] (E') -- (H);
    \draw[dashed] (F') -- (H);
    \draw[dashed] (G') -- (H);

    \draw[dotted] (B) -- (F);
    \draw[dotted] (B') -- (F');
    \draw[dotted] (C) -- (G);
    \draw[dotted] (C') -- (G');
    \draw[dotted] (D) -- (H);
  \end{tikzpicture}
  \caption{Piecing together a torus from a triangulation.}
  \label{fig:constructing_torus}
\end{figure}

Since the meridian and the longitude of a torus are homotopically circles,
it should be possible to require that any path following a meridian or
longitude winds exactly once. In other words, it should be possible to
construct a system of equations, with variables representing various
angles of each $\Delta_i$, such that certain sums are $2 \pi$.

By considering each $\Delta_i$ as ideal, each segment of such a path can
be viewed as complex multiplication (recall that all cross-ratios are in
$\mathbb{C} \cup \set{\infty}$.   For example, in figure~\ref{fig:angles},
the rotation that takes a point from start to end of a bold arrow is
the same rotation that takes $1$ to $z$: multiplication by $z$. By
re-ordering the vertices of $\Delta_i$, other paths may be expressed as
re-ordered cross-ratios.

\begin{figure}[h]
  \begin{tikzpicture}[framed]
    \coordinate (A) at (0,0);
    \coordinate (B) at (3.8,0);
    \coordinate (C) at (4,1.8);
    \coordinate (D) at (1,4);

    \coordinate (txtstart) at ($(A)!0.5!(D)$);
    \coordinate (txtend) at ($(B)!0.5!(D)$);

    \draw (A) ++(-0.4,0) node {$0$};
    \draw (B) ++(0.4,0) node {$1$};
    \draw (C) ++(0.4,0) node {$z$};
    \draw (D) ++(-0.4,0) node {$\infty$};

    \coordinate (A1) at ($(A)!0.8!(D)$);
    \coordinate (B1) at ($(B)!0.8!(D)$);
    \coordinate (C1) at ($(C)!0.8!(D)$);
    \coordinate (A2) at ($(A)!0.8!(C)$);
    \coordinate (B2) at ($(B)!0.8!(C)$);
    \coordinate (D2) at ($(D)!0.8!(C)$);
    \coordinate (A3) at ($(A)!0.8!(B)$);
    \coordinate (C3) at ($(C)!0.8!(B)$);
    \coordinate (D3) at ($(D)!0.8!(B)$);
    \coordinate (B4) at ($(B)!0.8!(A)$);
    \coordinate (C4) at ($(C)!0.8!(A)$);
    \coordinate (D4) at ($(D)!0.8!(A)$);
    \draw (A1) -- (D4);
    \draw (A2) -- (C4);
    \draw (A3) -- (B4);
    \draw (B1) -- (D3);
    \draw (B2) -- (C3);
    \draw (C1) -- (D2);
    \filldraw[opacity=0.1] (A1) -- (B1) -- (C1) -- cycle;
    \draw (C1) -- (A1) -- (B1);
    \draw[very thick, ->] (B1) -- (C1);
    \draw[dashed] (A1) -- (D);
    \draw[dashed] (B1) -- (D);
    \draw[dashed] (C1) -- (D);
    \filldraw[opacity=0.1] (A2) -- (B2) -- (D2) -- cycle;
    \draw (A2) -- (B2) -- (D2) -- cycle;
    \draw[dashed] (A2) -- (C);
    \draw[dashed] (B2) -- (C);
    \draw[dashed] (D2) -- (C);
    \filldraw[opacity=0.1] (A3) -- (C3) -- (D3) -- cycle;
    \draw (A3) -- (C3) -- (D3) -- cycle;
    \draw[dashed] (A3) -- (B);
    \draw[dashed] (C3) -- (B);
    \draw[dashed] (D3) -- (B);
    \filldraw[opacity=0.1] (B4) -- (C4) -- (D4) -- cycle;
    \draw[very thick, ->] (B4) -- (C4);
    \draw (C4) -- (D4) -- (B4);
    \draw[dashed] (B4) -- (A);
    \draw[dashed] (C4) -- (A);
    \draw[dashed] (D4) -- (A);

    \draw[->] (txtstart) ++(-60:.4 and 0.1) arc (-60:60:.4 and 0.1);
    \draw     let \p1 = (txtstart) in let \p2 = (txtend) in
              (txtstart) ++(0.45,0) node[anchor=west,text width=\x2 - \x1,
                  scale=0.7]{$z = \crossratio{\infty}{0}{1}{z}$};

  \end{tikzpicture}
  \caption{Identifying torus traversal with multiplication in $\mathbb{C}$.}
  \label{fig:angles}
\end{figure}

\begin{definition}
  Let a triangulation be fixed. To each simplex associate a variable
  $z_i$. For each edge $e_{ij}$ in the simplex, transforming any point
  by rotating around $e_{ij}$ is equivalent to multiplication of that
  point by either $z_i$, $\frac{z_i - 1}{z_i}$, or $\frac{1}{1-z_i}$
  (fix one angle as $z_i$, determine the rest by cross-ratio
  rearrangement).

  Let $p$ be a closed path in a triangulated surface, transverse to
  all edges. For every consecutive pair of edges that $p$ crosses,
  those edges must meet at an angle, which is associated to some
  $z_i$, $\frac{z_i - 1}{z_i}$, or $\frac{1}{1-z_i}$. The
  \definedterm{path monodromy of $p$}, denoted $\mathcal{M}(p)$, is
  the product of all these variables.
\end{definition}

\begin{definition}
  Let a triangulation of a manifold $M$ be fixed. For each torus
  boundary component $T_i$ of $M$, choose meridian and longitude paths
  in the torus (transverse to all edges) $m_i$ and $\ell_i$
  respectively. The \definedterm{cusp equations} are
  \begin{equation}
    \label{eq:cusp}
    \mathcal{M}(m_i) = 1 \qquad\text{and}\qquad \mathcal{M}(\ell_i) = 1
  \end{equation}
  There are two such equations for each torus boundary component.
\end{definition}

One more piece of geometric information will be useful. For each edge
in the triangulation, consider all face identifications that contain
that edge as an axis. Such identifications identify the edges of
neighboring faces, and these faces join to form two polygons, one
around each vertex of the edge. For example, see figure
\ref{fig:sort_of_lens_space_looking_thing}, in which the shaded region
is a polygon for the edge shown in bold.  We arbitrarily consider the
polygon to be the one about the terminus point of the edge.

\begin{figure}[h]
  \begin{tikzpicture}[framed]
    \coordinate (base) at (0,-1);
    \coordinate (top) at (0,1);
    \coordinate (A) at (30:2);
    \coordinate (B) at (60:1.5);
    \coordinate (C) at (100:2);
    \coordinate (D) at (180:3);
    \coordinate (E) at (200:2.8);
    \coordinate (F) at (340:1);

    \filldraw[opacity=0.1] (A) -- (B) -- (C) -- (D) -- (E) -- (F) -- cycle;
    \draw (A) -- (B) -- (C) -- (D) -- (E) -- (F) -- cycle;
    \draw (A) -- (top);
    \draw (B) -- (top);
    \draw (C) -- (top);
    \draw (D) -- (top);
    \draw (E) -- (top);
    \draw (F) -- (top);
    \draw[dashed] (A) -- (base);
    \draw[dashed] (B) -- (base);
    \draw[dashed] (C) -- (base);
    \draw[dashed] (D) -- (base);
    \draw[dashed] (E) -- (base);
    \draw[dashed] (F) -- (base);
    \draw[very thick, ->] (base) -- (top);
  \end{tikzpicture}
  \caption{Piecing together a polygon from a triangulation.}
  \label{fig:sort_of_lens_space_looking_thing}
\end{figure}

\begin{definition}
  Let a triangulation of a manifold $M$ be fixed. For each distinct
  edge $e_i$ in the triangulation, let $P_i$ be the polygon described
  above associated to that edge. Let $p_i$ be a path in $P_i$ circling
  the central point. The \definedterm{edge equations} are
  \begin{equation}
    \label{eq:edge}
    \mathcal{M}(p_i) = 1
  \end{equation}
  There are as many edge equations as there are distinct edges in the
  chosen triangulation.
\end{definition}

If two triangulations of $M$ are both composed of non-degenerate,
geometrically viable simplices, by Mostow rigidity they must yield the
same volume. Therefore, given a triangulation $\set{\Delta_i}$ of $M$,
if the cross-ratios $z_i$ all have positive imaginary part, then
computing $\sum_i D(\Delta_i)$ will yield $\vol(M)$. It is possible,
however, for a triangulation not to yield solutions that give a
geometric volume. In software implementations, this is usually dealt
with by re-triangulating using different parameters.

As presented, the system of cusp and edge equations can be hard to solve
by hand, because their degree is unbounded.  For example, the complement
of the knot $6_1$ (see figure~\ref{fig:6_1}), known as $m032$, has the
triangulation given in figure~\ref{fig:m032_triangulation}, and admits
the boundary torus given in figure~\ref{fig:m032_boundary}.

\begin{figure}[h]
  \begin{minipage}{.35\textwidth}
    \centering
    \includegraphics{6_1}
    \captionof{figure}{$6_1$.}
    \label{fig:6_1}
  \end{minipage}
  \begin{minipage}{0.5\textwidth}
    \centering
    \includegraphics{m032_triangulation}
    \captionof{figure}{$m032$.}
    \label{fig:m032_triangulation}
  \end{minipage}
\end{figure}

\begin{figure}[h]
  \includegraphics{m032_boundary}
  \caption{The torus boundary of $m032$.}
  \label{fig:m032_boundary}
\end{figure}

A path through the torus from left to right (for example, from the
single-arrow edge of $2_2$ to the corresponding edge of $1_0$) would
have to pass through at least eleven faces, inducing a cusp equation with
eleven terms. Computer programs such as \prog{SnapPy} \parencite{snappy}
can solve these equations (numerically) quite efficiently.
