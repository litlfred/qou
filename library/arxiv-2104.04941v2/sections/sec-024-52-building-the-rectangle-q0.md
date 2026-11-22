---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-024-52-building-the-rectangle-q0
section_title: "Building the rectangle Q0"
section_number: 5.2
pages: 24-29
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.997
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:Q0-construction}

  We desire to construct a quiver that holds coordinates for most of
  $H^3 \times_H N_{-}$. Conveniently, $H \times N_{-} = B_{-}$ is the
  \defined{double Bruhat cell} $G^{w_0,e} = B_{+} w_0 B_{+} \cap B_{-} e
  B_{-}$. We will not need any more information about double Bruhat
  cells, except to note that \cite[Section~2]{fominzelevinsky2005}
  describes an algorithm which accepts $u, v$ and creates a quiver whose
  cluster coordinates are coordinates on $G^{u,v}$. Therefore, we will
  follow this algorithm (with slight modifications) in the special case
  $u = w_0$, $v = e$. Since this simplifies the algorithm greatly, we
  can completely reproduce it here.

  The result will be a rectangle of $(h/2) + 1$ copies of $D$, with the
  first and last copies being frozen, and having half-weight edges. The
  first copy of $D$ will have vertices labeled $\set{B_{i}}_{i \in D}$,
  the last will be labeled with $\set{C_{i}}_{i \in D}$, The middle
  vertices will be labeled $v_{jk}$, where $j$ is the corresponding
  entry in $D$, and $k$ is the distance along the path from
  $B_{\bullet}$ to $C_{\bullet}$.

  Begin by setting $Q_0$ to be $D$. Label the vertices $\set{v_{i0}}_{i
    \in D}$. Let $f_i$ be the ``frontier vertices'' of $Q_0$, with
  initially $f_i = v_{i0}$ for each $i \in D$. For convenience, let $j :
  v_{ij} \mapsto j$, so that we may refer to $j(f_i)$. Also for
  convenience, let $\sigma(f_j, f_k)$ be the weight of the edge between
  $f_j$ and $f_k$ (taking values in $\set{-1, 0, 1}$).

  Now, proceed in order through the letters of $w_0$. For each letter
  $k$, let $j' = j(f_k) + 1$.
  \begin{itemize}
  \item
    Add $v_{kj'}$, a vertex of the same weight as $f_k$, to the left of
    $f_k$.
  \item
    For each $\ell \in D$, add an edge of weight $-\sigma(f_k,
    f_{\ell})$ from $v_{kj'}$ to $f_{\ell}$.
  \item
    Add an edge of weight $1$ from $v_{kj'}$ to $f_k$.
  \item
    Set $f_k$ to $v_{kj'}$.
  \end{itemize}

  When finished, all $f_k$ will be $v_{k(h/2)}$. Rename each $v_{k0}$ to
  $C_k$, each $v_{k(h/2)}$ to $B_k$, and halve the weights of any edges
  if they connect two $B_{\bullet}$ vertices or two $C_{\bullet}$
  vertices.

  \begin{remark}
    At each step, the frontier vertices form a sub-quiver of Dynkin
    type. Further, replacing $v_{ij}$ with $v_{i(j + 1)}$ operates,
    graphically, as a quiver mutation on the frontier.
  \end{remark}

  \begin{example}
    \label{ex:f4-part-1}
    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/rect-F4-in-progress}

      \caption{In-progress $Q_0$ for $F_4$ after $0$, $1$, and $6$
        letters of $w_0$.
        \label{fig:rect-F4-in-progress}
      }
    \end{figure}

    \begin{figure}[h]
      \centering \includestandalone[mode=image|tex]{fig/rect-F4}

      \caption{Completed $Q_0$ for $F_4$.
        \label{fig:rect-F4}
      }
    \end{figure}

    The Dynkin-type quiver for $G = F_4$ in \cref{ex:dynkin-quiver-f4},
    with $c = \set{1,2,3,4}$ and $\ell = 6$ gives \[ w_0 = \set{1, 2, 3,
        4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4}.
    \] Carrying out the construction produces the rectangle shown in
    \cref{fig:rect-F4-in-progress,fig:rect-F4}.

    Using \cite{gilles2019}, the initial step of $Q_0$ can be generated
    by

    {\centering \texttt{clav-bfzIII -U -c F4 -v
        "1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4" > Q0.clav}.}
  \end{example}

  
\subsection{Construction of \texorpdfstring{$\murot$}{mu\_\{rot\}}}

  The most difficult step is modifying $Q_0$ to become triangular by
  adding a third group of vertices, $A_{\bullet}$, also of half-Dynkin
  type. However, since the $A_{\bullet}$, $B_{\bullet}$, and
  $C_{\bullet}$ vertices will be frozen, the $Q_0$ alone is enough to
  describe the mutation sequence $\murot$. It will be composed of three
  main pieces.
  \begin{itemize}
  \item
    The mutation $\murottwist$ transforms coordinates of $\alpha$ to
    coordinates of $\operatorname{rot}(\alpha)$, in some order. The
    component mutation $\mucol(j)$ performs a mutation on column $j$
    that adjusts the minor coordinates by concatenating the Coxeter
    element to each word.
  \item
    The mutation $\muint{O1}$ (``ordering-1'') performs a
    $\sigma_{A_{\ell}}$ action on each row (a Dynkin diagram of
    $A_{\ell}$) using $\murowperm$ (``row $\sigma_{A_{\ell}}$'')
  \item
    The mutation $\muint{O2}$ (``ordering-2'') performs a $\sigma_G$
    action on each column (a Dynkin diagram of $G$) using $\mucolperm$
    (``column $\sigma_G$''), as in
    \cref{rem:sigma_G-action-on-Dynkin-diagram}. When $\sigma_G$ is
    trivial, this can be ignored.
  \end{itemize}

  \begin{definition}
    \label{def:murot-components}
    For any quiver\footnote{We are vague because we will use these
      mutations on $Q_0$ to find $Q$, and then on $Q$ itself as
      $\murot$.} with the same mutable portion as $Q_0$, fix an induced
    Coxeter element $c = \set{c_1, c_2, \dotsc, c_n}$, which admits a
    tree-like partition $\Set{T_1, T_2, \dotsc, T_m}$. Let $\ell =
    \frac{h}{2} - 1$. The sequences $\murot$ and $\murottwist$
    (``twisting rotation'') perform almost the same function, though
    they permute the vertices of the quiver differently.

    \begingroup \allowdisplaybreaks
    \begin{align*}
      \muT(i,j) &= \prod_{z \in T_i} \mu\Set{v_{zj}} \\
      \mucol(j) &= \prod_{i = 1}^{m} \muT(i,j) \\
      \murowperm(i) &= \left[ \prod_{k=1}^{\ell} \prod_{j=0}^{\ell - k} \muT(i, 1 + j) \right] \left[ \prod_{j=1}^{\ell} \muT(i, \ell - j) \right] \\
      \mucolperm(j) &= \left[ \prod_{i=0}^{\ell + 1} \mucol(j) \right] \\
      \murottwist &= \prod_{x=1}^{\ell} \prod_{y = 1}^{\ell + 1 - x} \mucol(y) \\
      \muint{O1} &= \prod_{i=1}^{m} \murowperm(i), \quad \muint{O2} = \begin{cases} \prod_{j=1}^{\ell} \mucolperm(j) & \text{$\sigma_G$ non-trivial} \\ \varnothing & \text{$\sigma_G$ trivial} \end{cases}\\
      \murot &= \left[ \murottwist \right ] \left[ \muint{O1} \right] \left[ \muint{O2} \right]
    \end{align*}
    \endgroup (Recall that, by \cref{not:writing-mutations}, multiplied
    mutations are applied left-to-right, and that products carry an
    ordering.)
  \end{definition}

  \begin{remark}
    An alternate presentation of $\murot$ which has the same effect on
    quivers may be given as roughly ``$\murottwist$ four times'', though
    we will focus on the above definition. \[ \left(\left[
      \prod_{x=1}^{\ell} \prod_{y =1}^{\ell + 1 - x} \mucol(y) \right]
      \left[ \prod_{x=1}^{\ell} \prod_{y=1}^{\ell + 1 - x}
      \mucol(\ell+1-y) \right] \right)^2. \]
  \end{remark}

  \begin{example}
    \label{ex:f4-part-2}
    Continuing from \cref{ex:f4-part-1} gives the following\footnote{The
      elements of the sequence are presented in usual reading order. The
      spacing is to emphasize decomposition into $\mucol$ terms.}:
    \begin{align*}
      \murottwist &= \mu\Set{
        \begin{subarray}{l}
          
\phantom{
         v_{1 5}, v_{2 5}, v_{3 5}, v_{4 5}, \quad
         v_{1 4}, v_{2 4}, v_{3 4}, v_{4 4}, \quad
         v_{1 3}, v_{2 3}, v_{3 3}, v_{4 3}, \quad
         v_{1 2}, v_{2 2}, v_{3 2}, v_{4 2}, \quad
}
         v_{1 1}, v_{2 1}, v_{3 1}, v_{4 1}, \\
\phantom{
         v_{1 5}, v_{2 5}, v_{3 5}, v_{4 5}, \quad
         v_{1 4}, v_{2 4}, v_{3 4}, v_{4 4}, \quad
         v_{1 3}, v_{2 3}, v_{3 3}, v_{4 3}, \quad
}
         v_{1 2}, v_{2 2}, v_{3 2}, v_{4 2}, \quad
         v_{1 1}, v_{2 1}, v_{3 1}, v_{4 1}, \\
\phantom{
         v_{1 5}, v_{2 5}, v_{3 5}, v_{4 5}, \quad
         v_{1 4}, v_{2 4}, v_{3 4}, v_{4 4}, \quad
}
         v_{1 3}, v_{2 3}, v_{3 3}, v_{4 3}, \quad
         v_{1 2}, v_{2 2}, v_{3 2}, v_{4 2}, \quad
         v_{1 1}, v_{2 1}, v_{3 1}, v_{4 1}, \\
\phantom{
         v_{1 5}, v_{2 5}, v_{3 5}, v_{4 5}, \quad
}
         v_{1 4}, v_{2 4}, v_{3 4}, v_{4 4}, \quad
         v_{1 3}, v_{2 3}, v_{3 3}, v_{4 3}, \quad
         v_{1 2}, v_{2 2}, v_{3 2}, v_{4 2}, \quad
         v_{1 1}, v_{2 1}, v_{3 1}, v_{4 1}, \\
\phantom{
}
         v_{1 5}, v_{2 5}, v_{3 5}, v_{4 5}, \quad
         v_{1 4}, v_{2 4}, v_{3 4}, v_{4 4}, \quad
         v_{1 3}, v_{2 3}, v_{3 3}, v_{4 3}, \quad
         v_{1 2}, v_{2 2}, v_{3 2}, v_{4 2}, \quad
         v_{1 1}, v_{2 1}, v_{3 1}, v_{4 1} \\
          
        \end{subarray}
      } \\
      \muint{O1} &= \mu\Set{
        \begin{subarray}{l}
          
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, \quad
w_{41}, w_{42}, w_{43}, w_{44}, \quad
w_{41}, w_{42}, w_{43}, \quad
w_{41}, w_{42}, \quad
w_{41}, \quad
w_{45}, w_{44}, w_{43}, w_{42}, w_{41}, \\
\\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, \quad
w_{31}, w_{32}, w_{33}, w_{34}, \quad
w_{31}, w_{32}, w_{33}, \quad
w_{31}, w_{32}, \quad
w_{31}, \quad
w_{35}, w_{34}, w_{33}, w_{32}, w_{31}, \\
\\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, \quad
w_{21}, w_{22}, w_{23}, w_{24}, \quad
w_{21}, w_{22}, w_{23}, \quad
w_{21}, w_{22}, \quad
w_{21}, \quad
w_{25}, w_{24}, w_{23}, w_{22}, w_{21}, \\
\\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, \quad
w_{11}, w_{12}, w_{13}, w_{14}, \quad
w_{11}, w_{12}, w_{13}, \quad
w_{11}, w_{12}, \quad
w_{11}, \quad
w_{15}, w_{14}, w_{13}, w_{12}, w_{11} \\
          
        \end{subarray}
      } \\
      \muint{O2} &= \mu\Set{ }
    \end{align*}
  \end{example}

  \begin{lemma}
    \label{lem:murot-works-for-making-Q}
    $\murot \circ \murot \circ \murot$ induces the identity on $Q_0$.
    Furthermore, $\murot$ induces a graph isomorphism on the mutable
    portion of the $Q_0$ (the sub-quiver containing only the
    $\set{v_{ij}}$ vertices).
  \end{lemma}

  
\subsection{The \texorpdfstring{$A_{\bullet}$}{A.} edge}

  \label{sec:the-A-edge}

  With $\murottwist$ in hand, we are ready to construct $A_{\bullet}$.
  Let $Q_1$ be $Q_0$ together with a dummy $A_{\bullet}$, which is of
  Dynkin type $D$ with edges removed. Denote $Q_i' = \murottwist(Q_i)$
  and $Q_i'' = (\murottwist)^{-1}(Q_i)$.

  We would like $Q_1$ to be isomorphic to $Q_1'$ and $Q_1''$ via
  $\varphi$ and $\varphi^{-1}$, with \[ \varphi: \Set{v_{ij} \mapsto
      v_{ij}, \qquad A_i \mapsto C_i, \qquad B_i \mapsto A_i, \qquad C_i
      \mapsto B_i}, \] but unfortunately these are not isomorphisms.
  However, we can correct for this. Let $Q_2$ be the quiver containing
  the vertices of $Q_1$, and with edges defined by \[ \sigma_{Q_2}(v, w)
    = \sum \set{\sigma_{Q_1}(v,w), \sigma_{\varphi^{-1}(Q_1')}(v,w),
      \sigma_{\varphi(Q_1'')}(v,w)}. \] That is, we repeatedly rotate
  $Q_1$, taking the inclusion of all frozen vertices necessary to ensure
  that $\murot$ is of order $3$ on the entire quiver.

  \begin{remark}
    \label{rem:yes-using-murot-is-justified}
    It is not yet obvious that $\murot$ actually does rotate by a third.
    The proof of \cref{lem:fgcs-exists-rot-works-trivial}, however, will
    show that $\murot$ acts with order $3$ on the seed torus for $Q_0$,
    and therefore on the quiver. There is no circular dependency here,
    as that lemma does not depend on the existence of $A_{\bullet}$,
    $B_{\bullet}$, or $C_{\bullet}$.
  \end{remark}

  We therefore define $Q$ to be $Q_2$, and we have constructed $Q$ and
  $\murot$.

  \begin{remark}
    \label{rem:Q-is-visually-triangular}
    To impose \cref{def:triangular-quiver}, we will customarily put
    $A_{\bullet}$ on the $(0,1)$ edge, $B_{\bullet}$ on the $(1,2)$
    edge, and $C_{\bullet}$ on the $(2,0)$ edge, with the $v_{ij}$ as
    face vertices.
  \end{remark}

  \begin{example}
    \label{ex:f4-part-3}

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/F4-Q1s}

      \caption{$Q_1$, $(Q_1')$, and $(Q_1'')$ for $F_4$ (rotated to
        agree with $\id$, $\varphi^{-1}$, and $\varphi$ respectively).
        \label{fig:rect-F4-Q1s}
      }
    \end{figure}

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/QF4}

      \caption{$Q$ for $F_4$.
        \label{fig:QF4}
      }
    \end{figure}

    Continuing from \cref{ex:f4-part-2}, we obtain the quivers of
    \cref{fig:rect-F4-Q1s}. Merging them, we obtain $Q = Q_2$ as in
    \cref{fig:QF4}.

  \end{example}

  
\subsection{Construction of \texorpdfstring{$\muflip$}{mu\_\{flip\}}}

  \label{sec:constructing-muflip}

  As in the case of $\murot$, the flip mutation is given by a tedious,
  repetitive sequence which looks like intertwined mutations on each row
  and column. It is again composed of pieces.
  \begin{itemize}
  \item
    The mutation $\muint{P}$ (``Pre-mutation'') rotates the sub-quivers
    on the left and right into a position where all the $w_{i,j}$
    vertices forma rectangle. See \cref{fig:Qdv-naming}.
  \item
    The mutation $\muflipcore$ is the core of the flip. It performs an
    analogous function to $\murottwist$: sequences of $\mucol(j)$
    mutations which adjusts minor coordinates (in the sense of
    \cref{sec:external-results}) in column $j$.
  \item
    The mutation $\muint{O3}$ (``ordering-3'') mirrors the rectangle of
    $w_{i,j}$ coordinates horizontally, again by
    \cref{rem:sigma_G-action-on-Dynkin-diagram}. The mutations
    $\muint{O4}$ and $\muint{O5}$ (``ordering-4'' and ``ordering-5'') do
    the same, but restricted to the left and right triangles. So the
    product $\muint{O3} \muint{O4} \muint{O5}$ switches positions of the
    left and right triangle interiors by translation as a composition of
    reflection.
  \end{itemize}

  To distinguish notation from $Q$, we shall label the edges of $\Qdv$
  by $D_{\bullet}$, $E_{\bullet}$, $F_{\bullet}$, $G_{\bullet}$, and the
  interior, mutable vertices by $w_{ij}$. See \cref{fig:Qdv-naming}.

  For $\mu$ a mutation defined on $Q$, let $\mu^R_{\ast}$ (resp.
  $\mu^L_{\ast}$) be the mutation defined to act on the right (left)
  part of the double quiver. Technically, replace each $v_{ij}$ with
  $w_{i(\ell + 1 - j)}$ (with $w_{i(L + 1 - j)}$) in $\mu_{\bullet}$ to
  obtain $\mu^{R}_{\bullet}$ ($\mu^{L}_{\bullet}$).

  \begin{figure}
    \centering \includestandalone[mode=image|tex]{fig/Qdv-naming}

    \caption{Vertex naming for $\Qdv$ (with $L = 2\ell + 1$), agreeing
      with \cref{fig:dv-construction} and labeled to induce a mutable
      rectangle in $\muP(\Qdv)$.
      \label{fig:Qdv-naming}
    }
  \end{figure}

  \begin{definition}
    \label{def:muflip-components}
    Construct $\Qdv$ by \cref{def:dv-dh-construction} and labeled as in
    \cref{fig:Qdv-naming}. Recall that $m$ is the number of partitions
    $T_i$ of $c$ from \cref{def:tree-like-quiver}. Some names such as
    $\muT$ are re-used from \cref{def:murot-components} with slightly
    different meanings.

    \begingroup \allowdisplaybreaks
    \begin{align*}
      \muP &= \left( \murottwistL \right)^{-1} \left( \murottwistR \right)^{-1} \tag{See \cref{def:murot-components}} \\
      \muT(i,j) &= \prod_{k \in T_i} \mu\Set{w_{kj}} \quad \text{(possibly empty)} \\
      \mucol(j) &= \prod_{i = 1}^{m} \muT(i,j) \\
      \muflipcore &= \prod_{i=1}^{L} \prod_{j=i}^{L} \mucol(L + i - j) \\
      \murowperm(i, a, b) &= \left[ \prod_{k=0}^{b-a} \prod_{j=0}^{(b-a) - k} \muT(i, a + j) \right] \left[ \prod_{j=0}^{b-a} \muT(i, b - j) \right] \\
      \muint{O3} &= \prod_{i=1}^{m} \murowperm(i, 1, L), \quad \muint{O4} = \prod_{i=1}^{m} \murowperm(i, \ell + 2, L), \quad \muint{O5} = \prod_{i=1}^{m} \murowperm(i, 1, \ell) \\
      \mufliptwist &= \left[ \muP \right] \left[ \muflipcore \right] \\
      \muflip &= \left[ \muP \right] \left[ \muflipcore \right] \left[ \muint{O3} \right] \left[ \muint{O4} \right] \left[ \muint{O5} \right]
    \end{align*}
    \endgroup
  \end{definition}

  \begin{remark}
    Because $\muP$ is composed entirely of rotation mutations, we are
    morally justified in focusing on $\muP(\Qdv)$ instead of $\Qdv$: it
    makes the isomorphism with $\Qdh$ more evident.

    The mutation $\murowperm(i, a, b)$ permutes the
    $\mathcal{A}$-coordinates at those vertices, and is purely used for
    rearranging.
  \end{remark}

  \begin{example}
    \label{ex:f4-part-4}

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/Q0-2F4}

      \caption{$\muP(\Qdv)$ for $F_4$. We apologize for the hexadecimal
        notation; rows have $>9$ vertices.
        \label{fig:Q0-2F4}
      }
    \end{figure}

    Continuing from \cref{ex:f4-part-3} constructs $\Qdv$ such that
    $\muP(\Qdv)$ is as in \cref{fig:Q0-2F4}. The sequence of mutations
    defining the flip is given in \cref{fig:F4-muflip-example}.

    \begin{figure}[h]
      \begin{align*}
        \muP &= \mu\Set{
          \begin{subarray}{l}
            
\phantom{
         w_{47}, w_{37}, w_{27}, w_{17}, \quad
         w_{48}, w_{38}, w_{28}, w_{18}, \quad
         w_{49}, w_{39}, w_{29}, w_{19}, \quad
         w_{4a}, w_{3a}, w_{2a}, w_{1a}, \quad
}
         w_{4b}, w_{3b}, w_{2b}, w_{1b}, \\
\phantom{
         w_{47}, w_{37}, w_{27}, w_{17}, \quad
         w_{48}, w_{38}, w_{28}, w_{18}, \quad
         w_{49}, w_{39}, w_{29}, w_{19}, \quad
}
         w_{4a}, w_{3a}, w_{2a}, w_{1a}, \quad
         w_{4b}, w_{3b}, w_{2b}, w_{1b}, \\
\phantom{
         w_{47}, w_{37}, w_{27}, w_{17}, \quad
         w_{48}, w_{38}, w_{28}, w_{18}, \quad
}
         w_{49}, w_{39}, w_{29}, w_{19}, \quad
         w_{4a}, w_{3a}, w_{2a}, w_{1a}, \quad
         w_{4b}, w_{3b}, w_{2b}, w_{1b}, \\
\phantom{
         w_{47}, w_{37}, w_{27}, w_{17}, \quad
}
         w_{48}, w_{38}, w_{28}, w_{18}, \quad
         w_{49}, w_{39}, w_{29}, w_{19}, \quad
         w_{4a}, w_{3a}, w_{2a}, w_{1a}, \quad
         w_{4b}, w_{3b}, w_{2b}, w_{1b}, \\
\phantom{
}
         w_{47}, w_{37}, w_{27}, w_{17}, \quad
         w_{48}, w_{38}, w_{28}, w_{18}, \quad
         w_{49}, w_{39}, w_{29}, w_{19}, \quad
         w_{4a}, w_{3a}, w_{2a}, w_{1a}, \quad
         w_{4b}, w_{3b}, w_{2b}, w_{1b}, \\
\phantom{
         w_{41}, w_{31}, w_{21}, w_{11}, \quad
         w_{42}, w_{32}, w_{22}, w_{12}, \quad
         w_{43}, w_{33}, w_{23}, w_{13}, \quad
         w_{44}, w_{34}, w_{24}, w_{14}, \quad
}
         w_{45}, w_{35}, w_{25}, w_{15}, \\
\phantom{
         w_{41}, w_{31}, w_{21}, w_{11}, \quad
         w_{42}, w_{32}, w_{22}, w_{12}, \quad
         w_{43}, w_{33}, w_{23}, w_{13}, \quad
}
         w_{44}, w_{34}, w_{24}, w_{14}, \quad
         w_{45}, w_{35}, w_{25}, w_{15}, \\
\phantom{
         w_{41}, w_{31}, w_{21}, w_{11}, \quad
         w_{42}, w_{32}, w_{22}, w_{12}, \quad
}
         w_{43}, w_{33}, w_{23}, w_{13}, \quad
         w_{44}, w_{34}, w_{24}, w_{14}, \quad
         w_{45}, w_{35}, w_{25}, w_{15}, \\
\phantom{
         w_{41}, w_{31}, w_{21}, w_{11}, \quad
}
         w_{42}, w_{32}, w_{22}, w_{12}, \quad
         w_{43}, w_{33}, w_{23}, w_{13}, \quad
         w_{44}, w_{34}, w_{24}, w_{14}, \quad
         w_{45}, w_{35}, w_{25}, w_{15}, \\
\phantom{
}
         w_{41}, w_{31}, w_{21}, w_{11}, \quad
         w_{42}, w_{32}, w_{22}, w_{12}, \quad
         w_{43}, w_{33}, w_{23}, w_{13}, \quad
         w_{44}, w_{34}, w_{24}, w_{14}, \quad
         w_{45}, w_{35}, w_{25}, w_{15} \\
          
          \end{subarray}
        } \\
        \muflipcore &= \mu\Set{
          \begin{subarray}{l}
            
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
        \qquad \qquad w_{15}, w_{25}, w_{35}, w_{45}, w_{14}, w_{24}, w_{34}, w_{44}, w_{13}, w_{23}, w_{33}, w_{43}, w_{12}, w_{22}, w_{32}, w_{42}, w_{11}, w_{21}, w_{31}, w_{41}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
        \qquad \qquad w_{15}, w_{25}, w_{35}, w_{45}, w_{14}, w_{24}, w_{34}, w_{44}, w_{13}, w_{23}, w_{33}, w_{43}, w_{12}, w_{22}, w_{32}, w_{42}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
        \qquad \qquad w_{15}, w_{25}, w_{35}, w_{45}, w_{14}, w_{24}, w_{34}, w_{44}, w_{13}, w_{23}, w_{33}, w_{43}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
        \qquad \qquad w_{15}, w_{25}, w_{35}, w_{45}, w_{14}, w_{24}, w_{34}, w_{44}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
        \qquad \qquad w_{15}, w_{25}, w_{35}, w_{45}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, w_{16}, w_{26}, w_{36}, w_{46}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, w_{17}, w_{27}, w_{37}, w_{47}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, w_{18}, w_{28}, w_{38}, w_{48}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, w_{19}, w_{29}, w_{39}, w_{49}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, w_{1a}, w_{2a}, w_{3a}, w_{4a}, \\
w_{1b}, w_{2b}, w_{3b}, w_{4b}, \\
          
          \end{subarray}
        } \\
        \muint{O3} &= \mu\Set{
          \begin{subarray}{l}
            
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, w_{47}, w_{48}, w_{49}, w_{4a}, w_{4b}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, w_{47}, w_{48}, w_{49}, w_{4a}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, w_{47}, w_{48}, w_{49}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, w_{47}, w_{48}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, w_{47}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, w_{46}, \\
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, \\
w_{41}, w_{42}, w_{43}, w_{44}, \\
w_{41}, w_{42}, w_{43}, \\
w_{41}, w_{42}, \\
w_{41}, \\
w_{4b}, w_{4a}, w_{49}, w_{48}, w_{47}, w_{46}, w_{45}, w_{44}, w_{43}, w_{42}, w_{41}, \\
\\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, w_{37}, w_{38}, w_{39}, w_{3a}, w_{3b}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, w_{37}, w_{38}, w_{39}, w_{3a}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, w_{37}, w_{38}, w_{39}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, w_{37}, w_{38}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, w_{37}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, w_{36}, \\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, \\
w_{31}, w_{32}, w_{33}, w_{34}, \\
w_{31}, w_{32}, w_{33}, \\
w_{31}, w_{32}, \\
w_{31}, \\
w_{3b}, w_{3a}, w_{39}, w_{38}, w_{37}, w_{36}, w_{35}, w_{34}, w_{33}, w_{32}, w_{31}, \\
\\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, w_{27}, w_{28}, w_{29}, w_{2a}, w_{2b}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, w_{27}, w_{28}, w_{29}, w_{2a}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, w_{27}, w_{28}, w_{29}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, w_{27}, w_{28}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, w_{27}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, w_{26}, \\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, \\
w_{21}, w_{22}, w_{23}, w_{24}, \\
w_{21}, w_{22}, w_{23}, \\
w_{21}, w_{22}, \\
w_{21}, \\
w_{2b}, w_{2a}, w_{29}, w_{28}, w_{27}, w_{26}, w_{25}, w_{24}, w_{23}, w_{22}, w_{21}, \\
\\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, w_{17}, w_{18}, w_{19}, w_{1a}, w_{1b}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, w_{17}, w_{18}, w_{19}, w_{1a}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, w_{17}, w_{18}, w_{19}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, w_{17}, w_{18}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, w_{17}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, w_{16}, \\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, \\
w_{11}, w_{12}, w_{13}, w_{14}, \\
w_{11}, w_{12}, w_{13}, \\
w_{11}, w_{12}, \\
w_{11}, \\
w_{1b}, w_{1a}, w_{19}, w_{18}, w_{17}, w_{16}, w_{15}, w_{14}, w_{13}, w_{12}, w_{11}, \\
          
          \end{subarray}
        },
        \substack{
          \muint{O4} = \mu\Set{
            \begin{subarray}{l}
              
w_{47}, w_{48}, w_{49}, w_{4a}, w_{4b}, \\
w_{47}, w_{48}, w_{49}, w_{4a}, \\
w_{47}, w_{48}, w_{49}, \\
w_{47}, w_{48}, \\
w_{47}, \\
w_{4b}, w_{4a}, w_{49}, w_{48}, w_{47}, \\
\\
w_{37}, w_{38}, w_{39}, w_{3a}, w_{3b}, \\
w_{37}, w_{38}, w_{39}, w_{3a}, \\
w_{37}, w_{38}, w_{39}, \\
w_{37}, w_{38}, \\
w_{37}, \\
w_{3b}, w_{3a}, w_{39}, w_{38}, w_{37}, \\
\\
w_{27}, w_{28}, w_{29}, w_{2a}, w_{2b}, \\
w_{27}, w_{28}, w_{29}, w_{2a}, \\
w_{27}, w_{28}, w_{29}, \\
w_{27}, w_{28}, \\
w_{27}, \\
w_{2b}, w_{2a}, w_{29}, w_{28}, w_{27}, \\
\\
w_{17}, w_{18}, w_{19}, w_{1a}, w_{1b}, \\
w_{17}, w_{18}, w_{19}, w_{1a}, \\
w_{17}, w_{18}, w_{19}, \\
w_{17}, w_{18}, \\
w_{17}, \\
w_{1b}, w_{1a}, w_{19}, w_{18}, w_{17}, \\
            
            \end{subarray}
          } \\
          \muint{O5} = \mu\Set{
            \begin{subarray}{l}
              
w_{41}, w_{42}, w_{43}, w_{44}, w_{45}, \\
w_{41}, w_{42}, w_{43}, w_{44}, \\
w_{41}, w_{42}, w_{43}, \\
w_{41}, w_{42}, \\
w_{41}, \\
w_{45}, w_{44}, w_{43}, w_{42}, w_{41}, \\
\\
w_{31}, w_{32}, w_{33}, w_{34}, w_{35}, \\
w_{31}, w_{32}, w_{33}, w_{34}, \\
w_{31}, w_{32}, w_{33}, \\
w_{31}, w_{32}, \\
w_{31}, \\
w_{35}, w_{34}, w_{33}, w_{32}, w_{31}, \\
\\
w_{21}, w_{22}, w_{23}, w_{24}, w_{25}, \\
w_{21}, w_{22}, w_{23}, w_{24}, \\
w_{21}, w_{22}, w_{23}, \\
w_{21}, w_{22}, \\
w_{21}, \\
w_{25}, w_{24}, w_{23}, w_{22}, w_{21}, \\
\\
w_{11}, w_{12}, w_{13}, w_{14}, w_{15}, \\
w_{11}, w_{12}, w_{13}, w_{14}, \\
w_{11}, w_{12}, w_{13}, \\
w_{11}, w_{12}, \\
w_{11}, \\
w_{15}, w_{14}, w_{13}, w_{12}, w_{11}, \\
            
            \end{subarray}
          } \\
        } \\
      \end{align*}
      \caption{The flip for $F_4$.
        \label{fig:F4-muflip-example}
      }
    \end{figure}
  \end{example}

  \begin{remark}
    At intermediate stages of $\murot$ and $\muflip$, the quiver may
    contain edges with weights higher than $1$. This is one of several
    phenomena which do not appear in the $A_n$ case. It is possible that
    alternate presentations of mutations exist which do not exhibit
    this.
  \end{remark}
