---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-023-51-overview
section_title: "Overview"
section_number: 5.1
pages: 23-24
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
Here we loosely describe the algorithm for constructing $Q$, $\murot$,
  $\muflip$, and $\conftoquiv$.

  The quiver $Q$ will be divided into an interior and three edges.
  Coordinates at each vertex will be assigned generalized minors of
  elements in the canonical form $(h_1, h_2, h_3, u)$ of an element of
  $\Conf_3^{\ast}$. Each edge should contain information for some $h_i$,
  and the interior should contain information for $u$.

  One minor for each simple root determines an element of $H$; the
  coordinates on an edge will be of the form $\genminor{}{j}(h_i)$.
  Accordingly, the edges of the triangle will be quivers of Dynkin type.
  The interior vertices will be given by generalized minors of the form
  $\genminor{w_k}{\word{i}_k}(u)$. Laying these out to satisfy
  \cite[Theorem~1.17]{fominzelevinsky1999} follows the algorithm of
  \cite[Section~2]{fominzelevinsky2005}. This, together with our choice
  of presentation for $w_0$, means the interior will be a rectangular
  grid of vertices. Recall that these take the names $A_{\bullet}$,
  $B_{\bullet}$, $C_{\bullet}$, and $v_{i,j}$ by
  \cref{def:triangular-quiver}.

  The algorithm of Fomin--Zelevinsky describes a rectangle. Two of the
  rectangle's edges will be edges in the triangle. We call this $Q_0$.
  The chief difficulty of constructing $Q$ is introducing the third edge
  to $Q_0$. To do this, we look ahead to $\murot$. Since that quiver
  mutation must rotate $Q$, and $Q$ and $Q_0$ share a mutable portion,
  we can rotate $Q_0$. And since $Q_0$ already has two of $Q$'s three
  edges, the third edge of $Q$ can be deduced from the action of
  $\murot$ on $Q_0$.

  The flip mutation $\muflip$ is built in the same way that $\murot$ is:
  repeated application of \cite[Theorem~1.17]{fominzelevinsky1999}. We
  need a bit of compensation before and after because the amalgamation
  does not quite line up the quivers as necessary.

  \begin{remark}
    Our construction will produce $\murot$ and $\muflip$ as compositions
    of smaller mutations. They contain smaller mutations ($\murottwist$
    and $\mufliptwist$) which may be more useful for certain
    applications. See \cref{sec:what-does-the-twist-do}.
  \end{remark}

  Finally, the map $\conftoquiv$ is the generalized minors, as described
  above, together with a monomial compensation. At each step of $\murot$
  and $\muflip$, \cite[Theorem~1.17]{fominzelevinsky1999} takes the form
  described in \cref{sec:thm-1.17} \[ (\text{initial}) \cdot
    (\text{final}) = (\text{left}) \cdot (\text{right}) + \prod_{j \ne
      \word{i}_k} \left( \text{in same column} \right). \] However, at
  the edges of $Q$, when $j$ is very low or very high, the left or right
  elements might be trivially $1$ according to the theorem. In our
  quivers, however, these elements are non-trivial, given by frozen
  vertices.

  Therefore, we have to balance the equation of the theorem. To do so,
  we treat the edge coordinates in the mutation relation as ``Extra''
  information, and include this extra information in our definition of
  interior coordinates. Then the quiver mutations take forms similar to
  the following: \[ {\color{blue!60!darkgray!70} \text{Extra} } \cdot
    (\text{initial}) \cdot (\text{final}) =
    \overbrace{({\color{blue!60!darkgray!70}\text{Extra} } \cdot
      1)}^{\text{left}} \cdot (\text{right}) +
    {\color{blue!60!darkgray!70} \text{Extra} } \cdot \prod_{j \ne
      \word{i}_k} \left( \text{in same column} \right). \] Since the
  extraneous factors appear in every term, the desired result still
  holds by the theorem. This is the effect of the monomial map
  $\monomialmap$ in $\conftoquiv$.

  \begin{example}
    \label{ex:dynkin-quiver-f4}
    Based on the Dynkin diagram \inldynkinFfour{} for $F_4$, the
    following is a well-rooted tree-like Dynkin quiver (following
    \cref{def:well-rooted-tree-like-quiver}) for $F_4$:

    {\centering \includestandalone[mode=image|tex]{fig/dynkin-type-F4}

    }
  \end{example}

  \begin{remark}
    \label{rem:sizes-get-switched}
    By \cref{def:dynkin-type}, the nodes with higher weight in the
    quiver correspond to the nodes which are ``smaller'' in the Dynkin
    diagram.
  \end{remark}

  With this, we are ready to begin the construction. Let $D$ be a
  well-rooted tree-like quiver of Dykin type for $G$. Let $c = \set{c_1,
    c_2, \dotsc, c_n}$ be the induced Coxeter element as in
  \cref{def:Coxeter-elt-induced-by-quiver}, and let $w_0$ be the longest
  word, with presentation via \cref{fac:w0-construction}.

  \begin{remark}
    We will abuse notation slightly by writing $s_{i_1} s_{i_2} \dotsb
    s_{i_n}$ as $\set{i_1, i_2, \dotsc, i_n}$.
  \end{remark}
