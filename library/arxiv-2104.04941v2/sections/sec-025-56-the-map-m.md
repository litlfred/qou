---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-025-56-the-map-m
section_title: "The map M"
section_number: 5.6
pages: 29-33
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.759
latex_coverage_ratio: 0.981
---
We now have $Q$ and the mutations, at least graphically. What remains
  is to finalize the association to the Lie group $G$. More
  specifically, the vertices of $Q$ should be associated to coordinates
  on $\Conf_3^{\ast}(G/N_{+})$.

  Recall that $\Conf_3^{\ast}(G/N_{+}) \cong H^3 \times_{H} (N_{-} \cap
  \lifttoG{w_0}G_0)$ by \cref{lem:canonical-form-for-conf_3_star}. So
  let $\alpha \in \Conf_3^{\ast}(G/N_{+})$ be given by $\alpha = (h_1,
  h_2, h_3, u)$. By abuse of notation, we denote the coordinate in
  $\seedAtorus_Q$ by the name of the vertex to which it is associated,
  and regard \[ \seedAtorus_Q =
    \overbrace{\set{A_i}}^{\partialtorus_{A}} \times
    \overbrace{\set{B_i}}^{\partialtorus_B} \times
    \overbrace{\set{C_i}}^{\partialtorus_C} \times
    \overbrace{\set{v_{ij}}}^{\partialtorus_V}. \] We will define
  $\minorcoordmap : \Conf_3^{\ast}(G/N_{+}) \to \seedAtorus_Q$ and a let
  $\conftoquiv$ be in terms of $\minorcoordmap$.

  \begin{definition}
    \label{def:conf_3_star-to-seed-torus}
    Let $k(i,j) = i + rj$. (This has the property that $v_{ij}$ is the
    $k(i,j)^{\text{th}}$ vertex added to $Q_0$ in the algorithm of
    \cref{sec:Q0-construction}.) Alternately, the prefix of $w_0^{-1}$
    used to place vertex $v_{ij}$ in $Q_0$ via the algorithm of
    \cite[Section~2]{fominzelevinsky2005} has length $(m + 1) - k$, and
    is equal to $w_{k(i,j)}$ by \cref{def:gamma-k}. Using
    \cref{def:generalized-minor},

    \begin{align*}
      \minorcoordmap_{A} &: \alpha \mapsto \set{A_{i} = \genminor{}{i}(h_1)} \\
      \minorcoordmap_{B} &: \alpha \mapsto \set{B_{i} = \genminor{}{i}(h_2)} \\
      \minorcoordmap_{C} &: \alpha \mapsto \set{C_{i} = \genminor{}{i}(h_3)} \\
      \minorcoordmap_{V} &: \alpha \mapsto \set{ v_{ij} = \genminor{w_{k(i,j)}}{i}(u)} \\
      \minorcoordmap &: \alpha \mapsto \minorcoordmap_{A}(\alpha) \oplus \minorcoordmap_{B}(\alpha) \oplus \minorcoordmap_{C}(\alpha) \oplus \minorcoordmap_{V}(\alpha) \\
    \end{align*}

    We then define a monomial map $\monomialmap : \seedAtorus_Q \to
    \seedAtorus_Q$ (using
    \cref{def:sigma_G,def:non-negative-generalized-minor}) as
    \begin{align*}
      \monomialmap &: A_i \mapsto A_i \\
      \monomialmap &: B_i \mapsto B_i \\
      \monomialmap &: C_i \mapsto C_i \\
      \monomialmap &: v_{ij} \mapsto v_{ij} \cdot \genminor{}{i}(\sigma_G(h_1^{-1}) h_2) \cdot \genminornumerator{w_{k(i,j)}}{\fundamentalweight_i}(\sigma_G(h_1)) \\
    \end{align*}

    We define $\conftoquiv = \monomialmap \circ \minorcoordmap$.
  \end{definition}

  \begin{remark}
    \label{rem:M-is-birational-equivalence}
    The map $\conftoquiv$ is a birational equivalence, following from
    \cite[Section~2.7]{fominzelevinsky1999}.
  \end{remark}

  \begin{example}
    \label{ex:f4-part-6}

    Continuing from \cref{ex:f4-part-4}, let $\alpha = (h_1, h_2, h_3,
    u)$. Let $h_{ij} = \genminor{}{j}(h_i)$. Then $\minorcoordmap_{V}$
    produces the following: \[ A_1 = h_{11}, \quad A_2 = h_{12}, \quad
      \dotsc, \quad C_4 = h_{34}, \quad v_{11} = \genminor{w_5}{1}(u),
      \quad v_{12} = \genminor{w_6}{2}(u), \quad \dotsc, \quad v_{45} =
      \genminor{w_{24}}{4}(u). \]

    To compute the monomial map, refer to figure
    \cref{fig:abstract-gen-minor}. For example, to calculate
    $\monomialmap(v_{23})$, we have $i = 2$, so
    $\genminor{}{i}(\sigma_G(h_1^{-1}) h_2) = \frac{h_{22}}{h_{12}}$.
    For the second factor, $k = k(2,3) = 2 + 4\cdot 3 = 14$. Taking the
    numerator of the $i = 2$, $k = 14$ entry gives $t_1^2 t_2$, so
    $\genminornumerator{w_{14}}{\fundamentalweight_i}(\sigma_G(h_1)) =
    h_{11}^2 h_{12}$. This gives $\monomialmap(v_{23}) = v_{23} \cdot
    \frac{h_{22}}{h_{12}} \cdot h_{11}^2 h_{12}$, and
    $\conftoquiv(\alpha)$ has $v_{23} = \genminor{w_{14}}{2}(u) \cdot
    h_{11}^2 h_{22}$.

    Repeating this for all others, $\conftoquiv(\alpha)$ has coordinates
    as given in \cref{fig:f4-M-assignment}.
  \end{example}
  \begin{figure}
    \centering \tabulinesep=1.1mm

    \begin{tabu}{r|llll p{0.5in} r|llll p{0.5in} r|llll}
      $i$ & $1$ & $2$ & $3$ & $4$ && & $1$ & $2$ & $3$ & $4$ && & $1$ & $2$ & $3$ & $4$ \\ \hline
      $k=1$ & $\frac{1}{t_1}$ & $\frac{1}{t_2}$ & $\frac{1}{t_3}$ & $\frac{1}{t_4}$ && $9$ & $\frac{t_2}{t_3}$ & $\frac{t_1 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3^2 t_4}$ & $\frac{t_2^2}{t_3 t_4}$ && $17$ & $\frac{t_1 t_2}{t_3}$ & $\frac{t_1 t_2^2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4}$ & $\frac{t_2^2}{t_3}$ \\
      $2$ & $\frac{t_1}{t_2}$ & $\frac{1}{t_2}$ & $\frac{1}{t_3}$ & $\frac{1}{t_4}$ && $10$ & $\frac{t_1}{t_4}$ & $\frac{t_1 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3^2 t_4}$ & $\frac{t_2^2}{t_3 t_4}$ && $18$ & $\frac{t_2}{t_4}$ & $\frac{t_1 t_2^2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4}$ & $\frac{t_2^2}{t_3}$ \\
      $3$ & $\frac{t_1}{t_2}$ & $\frac{t_1}{t_3}$ & $\frac{1}{t_3}$ & $\frac{1}{t_4}$ && $11$ & $\frac{t_1}{t_4}$ & $\frac{t_1^2 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3^2 t_4}$ & $\frac{t_2^2}{t_3 t_4}$ && $19$ & $\frac{t_2}{t_4}$ & $\frac{t_1 t_2}{t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4}$ & $\frac{t_2^2}{t_3}$ \\
      $4$ & $\frac{t_1}{t_2}$ & $\frac{t_1}{t_3}$ & $\frac{t_1^2}{t_3 t_4}$ & $\frac{1}{t_4}$ && $12$ & $\frac{t_1}{t_4}$ & $\frac{t_1^2 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4^2}$ & $\frac{t_2^2}{t_3 t_4}$ && $20$ & $\frac{t_2}{t_4}$ & $\frac{t_1 t_2}{t_4}$ & $\frac{t_2^2}{t_4}$ & $\frac{t_2^2}{t_3}$ \\
      $5$ & $\frac{t_1}{t_2}$ & $\frac{t_1}{t_3}$ & $\frac{t_1^2}{t_3 t_4}$ & $\frac{t_1^2}{t_3}$ && $13$ & $\frac{t_1}{t_4}$ & $\frac{t_1^2 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4^2}$ & $\frac{t_1^2}{t_4}$ && $21$ & $\frac{t_2}{t_4}$ & $\frac{t_1 t_2}{t_4}$ & $\frac{t_2^2}{t_4}$ & $\frac{t_3}{t_4}$ \\
      $6$ & $\frac{t_2}{t_3}$ & $\frac{t_1}{t_3}$ & $\frac{t_1^2}{t_3 t_4}$ & $\frac{t_1^2}{t_3}$ && $14$ & $\frac{t_1 t_2}{t_3}$ & $\frac{t_1^2 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4^2}$ & $\frac{t_1^2}{t_4}$ && $22$ & $t_1$ & $\frac{t_1 t_2}{t_4}$ & $\frac{t_2^2}{t_4}$ & $\frac{t_3}{t_4}$ \\
      $7$ & $\frac{t_2}{t_3}$ & $\frac{t_1 t_2}{t_3 t_4}$ & $\frac{t_1^2}{t_3 t_4}$ & $\frac{t_1^2}{t_3}$ && $15$ & $\frac{t_1 t_2}{t_3}$ & $\frac{t_1 t_2^2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4^2}$ & $\frac{t_1^2}{t_4}$ && $23$ & $t_1$ & $t_2$ & $\frac{t_2^2}{t_4}$ & $\frac{t_3}{t_4}$ \\
      $8$ & $\frac{t_2}{t_3}$ & $\frac{t_1 t_2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3^2 t_4}$ & $\frac{t_1^2}{t_3}$ && $16$ & $\frac{t_1 t_2}{t_3}$ & $\frac{t_1 t_2^2}{t_3 t_4}$ & $\frac{t_1^2 t_2^2}{t_3 t_4}$ & $\frac{t_1^2}{t_4}$ && $24$ & $t_1$ & $t_2$ & $t_3$ & $\frac{t_3}{t_4}$ \\
    \end{tabu}

    \caption{For type $F_4$, $\genminoryz{w_k}{w_k}{i}(A)$ for abstract
      $A = \prod_{i=1}^{r} \torush_i(t_i)$.
      \label{fig:abstract-gen-minor}
    }
  \end{figure}

  \begin{figure}
    \begin{equation*}
      \begin{gathered}
        \begin{aligned}
          A_1 &= h_{11} &\qquad A_2 &= h_{12} &\qquad A_3 &= h_{13} &\qquad A_4 &= h_{14} \\
          B_1 &= h_{11} & B_2 &= h_{12} & B_3 &= h_{13} & B_4 &= h_{14} \\
          C_1 &= h_{11} & C_2 &= h_{12} & C_3 &= h_{13} & C_4 &= h_{14} \\
        \end{aligned}
        \\
        \begin{aligned}
          v_{11} &= \genminor{w_{ 5}}{1}(u) \cdot h_{21} & v_{21} &= \genminor{w_{ 6}}{2}(u) \cdot \frac{ h_{11} h_{22} }{ h_{12} } & v_{31} &= \genminor{w_{ 7}}{3}(u) \cdot \frac{ h_{11}^2 h_{23} }{ h_{13} } & v_{41} &= \genminor{w_{ 8}}{4}(u) \cdot \frac{ h_{11}^2 h_{24} }{ h_{14} } \\
          v_{12} &= \genminor{w_{ 9}}{1}(u) \cdot \frac{ h_{12} h_{21} }{ h_{11} } & v_{22} &= \genminor{w_{10}}{2}(u) \cdot h_{11} h_{22} & v_{32} &= \genminor{w_{11}}{3}(u) \cdot \frac{ h_{11}^2 h_{12}^2 h_{23} }{ h_{13} } & v_{42} &= \genminor{w_{12}}{4}(u) \cdot \frac{ h_{12}^2 h_{24} }{ h_{14} } \\
          v_{13} &= \genminor{w_{13}}{1}(u) \cdot h_{21} & v_{23} &= \genminor{w_{14}}{2}(u) \cdot h_{11}^2 h_{22} & v_{33} &= \genminor{w_{15}}{3}(u) \cdot \frac{ h_{11}^2 h_{12}^2 h_{23} }{ h_{13} } & v_{43} &= \genminor{w_{16}}{4}(u) \cdot \frac{ h_{11}^2 h_{24} }{ h_{14} } \\
          v_{14} &= \genminor{w_{17}}{1}(u) \cdot h_{12} h_{21} & v_{24} &= \genminor{w_{18}}{2}(u) \cdot h_{11} h_{12} h_{22} & v_{34} &= \genminor{w_{19}}{3}(u) \cdot \frac{ h_{11}^2 h_{12}^2 h_{23} }{ h_{13} } & v_{44} &= \genminor{w_{20}}{4}(u) \cdot \frac{ h_{12}^2 h_{24} }{ h_{14} } \\
          v_{15} &= \genminor{w_{21}}{1}(u) \cdot \frac{ h_{12} h_{21} }{ h_{11} } & v_{25} &= \genminor{w_{22}}{2}(u) \cdot h_{11} h_{22} & v_{35} &= \genminor{w_{23}}{3}(u) \cdot \frac{ h_{12}^2 h_{23} }{ h_{13} } & v_{45} &= \genminor{w_{24}}{4}(u) \cdot \frac{ h_{13} h_{24} }{ h_{14} }
        \end{aligned}
      \end{gathered}
    \end{equation*}
    \caption{$\conftoquiv(\alpha)$ for type $F_4$.
      \label{fig:f4-M-assignment}
    }
  \end{figure}

  \begin{remark}
    There is good reason to suspect that this construction is not unique
    up to mutation equivalency of the quivers. It is certainly not
    unique if one relaxes the construction of $\conftoquiv$ as a
    monomial map applied to generalized minors. For example, during our
    investigation $\conftoquiv$ was considered as
    $\Conf_3^{\ast}(G/N_{+}) \times \gen{\sigma_G} \to \seedAtorus_Q
    \times \gen{\sigma_G}$, where $\murot^{\ast}$ acted by $+1$ on the
    second factor. An infinite family of $\conftoquiv$ maps were found,
    depending on this factor of $[\tau] \in \gen{\sigma_G}$ to varying
    extent.
  \end{remark}

  
\subsection{The significance of the ``twisting'' mutations}

  \label{sec:what-does-the-twist-do}

  The quiver mutations $\murot$ and $\muflip$ are intended to compose
  easily without requiring renaming the vertices of the quiver. For
  example, $\murot^2(Q)$ should be identical to $\murot^{-1}(Q)$.

  Unfortunately, quiver mutations that yield equivalent seeds do not
  necessarily preserve the positions of those seeds. For example,
  consider the classic ``pentagon recurrence'', which happens to be
  equivalent to $\murowperm$ on a row which is of Dynkin type $A_2$. The
  switching of positions is exactly the the action of $\sigma_{A_2}$ on
  the Dynkin diagram.

  \begin{figure}[h]
    \centering
    \includestandalone[mode=image|tex]{fig/pentagon-recurrence}

    \caption{The pentagon recurrence.
      \label{fig:pentagon-recurrence}
    }
  \end{figure}

  The $\muint{Oi}$ parts of $\murot$ and $\muflip$, distinguishing them
  from $\murottwist$ and $\mufliptwist$, are exactly to address these
  actions of $\sigma_G$. If desired, shorter mutations may be used at
  the expense of slightly more complicated identifications between
  variables.

  
\section{Construction for \texorpdfstring{$A_n$}{A\_n}}

  \label{sec:An-case}

  The $A_n$ case was studied in detail in \cite{gtz2015}. We merely
  restate the conclusions in language consistent with the above.

  \begin{remark}
    That the algorithm of \cref{sec:main-result} does not work for
    $A_{2n}$ can be seen in a few different ways, which are
    interconnected.
    \begin{itemize}
    \item
      There is no general formula for a Coxeter element $c$ that yields
      a longest-word presentation $w_0 = c c \dotsb c$.
    \item
      The Coxeter number for $A_{2n}$ is odd.
    \item
      The action of $\sigma_G$ for $A_{2n}$ preserves no simple roots,
      therefore there can be no tree partitioning with a unique root
      node.
    \end{itemize}
  \end{remark}

  \begin{proposition}
    \label{prop:fgcs-exists-for-An}
    For $G$ of type $A_n$, \cref{thm:fgcs-exists} holds.
  \end{proposition}
  \begin{proof}
    For the construction of $Q$, take the quiver consisting of mutable
    vertices $\set{v_{ij} : 1 \le j \le n, 1 \le i \le n - j}$ and
    frozen vertices $\set{A_i, B_i, C_i : 1 \le i \le n}$, all of weight
    $1$. We consider \[ A_{i} = v_{0,i}, \quad B_{i} = v_{i,n+1-j},
      \quad C_{i} = v_{i,0}. \] The edges are given by \[ \sigma(a,b) =
      \begin{cases} c(a,b) & a = v_{i,j}, b = v_{i+1,j} \text{ or } a =
        v_{i,j}, b = v_{i-1,j+1} \text{ or } a = v_{i,j}, b = v_{i,j-1}
        \\ -c(a,b) & a = v_{i+1,j}, b = v_{i,j} \text{ or } a =
        v_{i-1,j+1}, b = v_{i,j} \text{ or } a = v_{i,j-1}, b = v_{i,j}
        \\ 0 & \text{else}, \end{cases} \] and $c(a,b)$ is $\frac{1}{2}$
    if $a$ and $b$ are both $A_i$s, both $B_i$s, or both $C_i$s, and is
    $1$ otherwise.

    The mutation $\murot = \mu\Set{}$ is trivial.

    Since the mutable portion of $Q_{A_n}$ is not rectangular, we need
    another convention for describing coordinates of $\Qdv$ in order to
    describe $\muflip$. We present this by example in
    \cref{fig:amalgamation-QAn}.
  \end{proof}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/amalgamation-QAn}

    \caption{Quivers for type $A_3$, also showing naming convention for
      $\Qdv$.
      \label{fig:amalgamation-QAn}
    }
  \end{figure}

  Mechanically, the inclusion of the left $Q_{A_n}$ into $\Qdv$ is the
  following: \[ A_i \mapsto D_i, \qquad B_i \mapsto E_i, \qquad C_i
    \mapsto w_{i,n}, \qquad v_{i,j} \mapsto w_{i,j+n}, \] and for the
  right $Q_{A_n}$ into $\Qdv$, the following: \[ A_i \mapsto w_{i,n},
    \qquad B_i \mapsto F_i, \qquad C_i \mapsto G_i, \qquad v_{i,j}
    \mapsto w_{j,n+1-i}, \]

  The mutation $\muflip$ is then the ``diamond sequence'':
  \begin{align*}
    t(\ell, j) &= \frac{\ell + 1}{2} - \abs*{j - \frac{\ell + 1}{2}} \\
    \muint{Rect}(\ell) &= \prod_{k = 1}^{\ell} \prod_{j=0}^{n-\ell} \mu\Set{w_{t(\ell,k) + j,2k + n - (\ell + 1)}} \\
    \muflip &= \prod_{\ell = 1}^{n} \muint{Rect}(\ell)
  \end{align*}

  The map $\conftoquiv$ is constructed as in
  \cref{def:conf_3_star-to-seed-torus}. Where needed, the presentation
  of the longest word is given by \[ \word{i} = (1, 2, \dotsc, n, \quad
    1, 2, \dotsc, n-1, \quad \dotsc, \quad 1, 2, \quad 1). \]

  
\section{Proof of \cref{thm:fgcs-exists} for simple
    \texorpdfstring{$G$}{G}}

  \label{sec:proof}

  
\subsection{Overview}

  Our goal is to prove \cref{thm:fgcs-exists}. We will only consider the
  case where $G$ is simple, as products are handled by
  \cref{sec:products}. We need to show that, for a fixed $G$, the
  results $Q$, $\murot$, $\muflip$, and $\conftoquiv$ satisfy all the
  requirements of \cref{def:tcs,def:fgcs}.

  \begin{proof}[Proof of \cref{thm:fgcs-exists}]
    If $G$ is not simple, then we may appeal to
    \cref{lem:fgcs-exists-for-products} and recurse, so assume $G$ is
    simple. For $G$ of type $A_n$, \cref{prop:fgcs-exists-for-An} is
    sufficient, so assume $G$ is not of type $A_n$.

    The algorithm of \cref{sec:main-result} produces $Q$, $\murot$,
    $\muflip$, and $\conftoquiv$. We must show these satisfy
    \cref{def:fgcs}.

    \begin{itemize}
    \item
      \cref{def:fgcs-1} (triangularity) is handled last. As described in
      \cref{sec:the-A-edge}, we need to know that $\murot$ is of order
      $3$ on the $\mathcal{A}$-coordinates before concluding that the
      quiver is triangular.
    \item
      \Cref{def:fgcs-2} (that the edges are half-Dynkin) is evident by
      construction.
    \item
      \Cref{def:fgcs-M-is-birational-equivalence} (that $\conftoquiv$ is
      a birational equivalence) is given by
      \cref{rem:M-is-birational-equivalence}.
    \item
      We handle \cref{def:fgcs-rot-works} (the rotation) with \cref{lem:fgcs-exists-rot-works-trivial,lem:fgcs-exists-rot-works-nontrivial}.
    \item
      We handle \cref{def:fgcs-flip-works} (the flip) with
      \cref{lem:fgcs-exists-flip-works}.
    \item
      Now, recalling \cref{rem:yes-using-murot-is-justified}, since
      $\murotind$ is of order $3$ acting on $\seedAtorus_Q$ and the seed
      torus of a cluster determines the quiver, $\murot$ is of order $3$
      on $Q$. Likewise, $\muflip$ must transform $\Qdv$ to $\Qdh$.
      Therefore, $Q$ has triangulation-compatible symmetry and
      \cref{def:fgcs-1} is satisfied.
    \end{itemize}
  \end{proof}

  In what follows, we assume $G$ a simple Lie group over $\mathbb{C}$ of
  type other than $A_n$, and that the $Q$, $\murot$, $\muflip$,
  $\conftoquiv$ are given by \cref{sec:main-result} for $G$.
