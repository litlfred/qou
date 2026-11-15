---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-016-32-grid-exchange-relations
section_title: "Grid exchange relations"
section_number: 3.2
pages: 14-15
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.978
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:thm-1.17}

  Here we give an overview of the identity
  \cite[Theorem~1.17]{fominzelevinsky1999} used to justify the exchange
  relations of $\murottwist$ and $\muflipcore$, and to prove
  \cref{lem:fgcs-exists-rot-works-trivial,lem:fgcs-exists-flip-works}:

  \begin{theorem}[{\cite[Theorem~1.17]{fominzelevinsky1999}}]
    \label{thm:local-1.17}
    For $u, v$ two words in the Weyl group $W$ such that $\length(u s_i)
    = \length(u) + 1$ and $\length(v s_i) = \length(v) + 1$, and $A$ the
    Cartan matrix, \[ \genminoryz{u}{v}{i} \genminoryz{u s_i}{v s_i}{i}
      = \genminoryz{u s_i}{v}{i} \genminoryz{u}{v s_i}{i} + \prod_{j \ne
        i} (\genminoryz{u}{v}{j})^{-A_{j,i}}. \]
  \end{theorem}

  \begin{remark}
    It appears that this theorem only allows us to adjust the minor
    coordinates by one letter at a time: $s_i$. By the same logic as
    \cref{rem:all-wkomegaj-are-gamma-k-or-trivial}, however, we actually
    are able to adjust $u$ and $v$ by longer sequences of letters, as
    long as they do not contain multiple $s_i$.
  \end{remark}

  We use this theorem in situations where, mutating at $v_{a,b}$,
  \begin{align*}
    \genminoryz{u s_i}{v s_i }{i} &= \text{Coordinate of $v_{a,b}$ before mutation} \\
    \genminoryz{u}{v}{i} &= \text{Coordinate of $v_{a,b}$ after mutation} \\
    \genminoryz{u }{v s_i}{i} &= \text{Coordinate to left of $v_{a,b}$} \\
    \genminoryz{u s_i}{v }{i} &= \text{Coordinate to right of $v_{a,b}$} \\
    \genminoryz{u }{v}{j} &= \text{Coordinates in same column as $v_{a,b}$}
  \end{align*}

  \begin{example}
    We look ahead to the results of \cref{sec:main-result} and assume
    all edge coordinates are $1$ for simplicity.
    \Cref{fig:QC4-middle-murot} depicts $Q_{C_4}$ partway through the
    rotation mutation. The minors associated to relevant coordinates
    (see the proof of \cref{lem:fgcs-exists-rot-works-trivial} for
    details) are at this point
    \begin{align*}
      v_{22} &: \genminoryz{w_1}{w_{10}}{2} = \genminoryz{w_{3} s_2}{w_{11} s_2}{2}\\
      v_{21} &: \genminoryz{w_5}{w_{10}}{2} = \genminoryz{w_{3} }{w_{11} s_2}{2}\\
      v_{23} &: \genminoryz{w_1}{w_{14}}{2} = \genminoryz{w_{3} s_2}{w_{11} }{2}\\
      v_{12} &: \genminoryz{w_5}{w_{13}}{1} = \genminoryz{w_{3} }{w_{11} }{1}\\
      v_{32} &: \genminoryz{w_1}{w_{11}}{3} = \genminoryz{w_{3} }{w_{11} }{3}\\
    \end{align*}

    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/QC4-middle-murot}

      \caption{After applying $\mu\Set{v_{11}, v_{21}, v_{31}, v_{41},
          v_{12}}$ to $Q_{C_4}$. The next mutation in $\murot$ is at
        $v_{22}$.
        \label{fig:QC4-middle-murot}
      }
    \end{figure}

    The equality follows from
    \cref{rem:all-wkomegaj-are-gamma-k-or-trivial}. Therefore, by
    applying the identity we see that mutating at $v_{22}$ will change
    the coordinate to $\genminoryz{w_{3}}{w_{11}}{2} =
    \genminoryz{w_{6}}{w_{14}}{2}$.
  \end{example}

  Finally, we note that the requirements on $u$ and $v$ may be loosened,
  which we need to prove \cref{lem:fgcs-exists-flip-works}.

  \begin{lemma}
    \label{lem:thm-1.17-for-repeated-c}
    Even if $\length(u s_i) \ne \length(u) + 1$ or $\length(v s_i) \ne
    \length(v) + 1$, the result of \cref{thm:local-1.17} still holds as
    long as $u$ and $v$ are subwords of a repeated Coxeter element $c$.
  \end{lemma}
  \begin{proof}
    From the proof in \cite{fominzelevinsky1999}, the only reason for
    the length condition is to ensure that $\lifttoG{v} \lifttoG{s_i} =
    \lifttoG{vs_i}$ (and similar for $u$), since the lifting is not
    quite a homomorphism: for example $\lifttoG{s_i s_i} \ne
    \lifttoG{e}$.

    However, the only situations in which multiplication is not
    preserved is when the multiplication by $s_i$ induces a
    length-shortening identity in $W$. But if $u$ and $v$ are subwords
    of a repeated Coxeter element, their suffixes will always be of the
    form $w_k$. These admit no length-shortening braid relations.

    So the only possibility for $\lifttoG{v s_i} \ne \lifttoG{v}
    \lifttoG{s_i}$ is if $v s_i$ contains a copy of $w_0 = c^{h/2}$. But
    $\lifttoG{c^{h}} = s_G$ is an element of $H$. By prepending copies
    of $c^h$ to either $u$ or $v$, we may ensure that the difference in
    length between $u$ and $v$ is never more than $\frac{h}{2} - 1$.
    Then, using \[ \genminoryz{w u}{w v}{i}(g) =
      \genminoryz{u}{v}{i}(w^{-1} g w) \] we reduce to the case where
    $u$ and $v$ are each some $w_k$ shorter than $w_0$. By replacing $g$
    with $w g w^{-1} s_G^{\epsilon}$ (where $\epsilon \in {0,1}$
    depending on the exact difference between $u$ and $v$), the desired
    identity follows from the regular theorem.
  \end{proof}
