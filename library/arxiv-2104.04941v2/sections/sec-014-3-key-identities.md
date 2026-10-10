---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-014-3-key-identities
section_title: "Key identities"
section_number: 3
pages: 13-14
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
text_source: latex
latex_prose_ratio: 0.647
latex_coverage_ratio: 0.958
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
\label{sec:external-results}

  Here we reproduce two external results of particular significance to
  our constructions and proofs, from \cite{yangzelevinsky2008} and
  \cite{fominzelevinsky1999}. We refer to their respective origins for
  more details. These identities allow us to perform a program we call
  ``adjusting a minor coordinate''. Depending on the surrounding
  conditions, these will allow us to conclude that the action of
  mutation on $\seedAtorus_Q$ is to replace \[ \genminoryz{u}{v}{i}(g)
    \qquad \text{with} \qquad \genminoryz{u'}{v'}{i}(q) \] for some $u,
  v, u', v'$.

  \subsection{Actions of \texorpdfstring{$\sigma_G$}{sigma\_G}}

  \label{sec:yz-dynkin-identity}

  We give an overview of the identity used to justify mutations which
  apply $\sigma_G$ to the Dynkin diagram-like graph underlying a quiver,
  as in \cref{rem:sigma_G-action-on-Dynkin-diagram}. We use this in the
  proofs of \cref{lem:colsigmaG-does-sigmaG,lem:rowsigmaG-does-sigmaG}.
  This identity is collected from several results in
  \cite{yangzelevinsky2008}, so we import some notation.

  \begin{definition}
    Let the \defined{reduced double Bruhat cell} $L^{s,t} = N_{+}
    \lifttoG{s} N_{+} \cap B_{-} \lifttoG{t} B_{-}$. (We shall not need
    many facts about this object.) Recall that $k^{\star} =
    \sigma_G(k)$. The relation $a \prec_{c} b$ means that $a$ precedes
    $b$ in the Coxeter element $c$, and that $a$ and $b$ are connected
    by an edge in the Dynkin diagram associated to $c$.
  \end{definition}

  We shall mostly be interested in minors of the form
  $\genminoryz{c^m}{c^m}{k}$. Yang--Zelevinsky denote these as $x_{c^m
    \fundamentalweight_k;c}$, but we will avoid this for notational
  consistency.

  The main result is that for a cluster algebra $\mathcal{A}(c)$ defined
  by an initial seed with quiver of Dynkin type associated to Coxeter
  element $c$, there exists a $g \in L^{c,c^{-1}}$ such that all cluster
  coordinates and coefficients of $\mathcal{A}(c)$ are given by certain
  generalized minors of $g$. This allows combinatorially defining the
  exchange relations of all \defined{source} or \defined{sink mutations}
  (at vertices where all edges point out or in). These always exchange
  variables of the form $\genminoryz{c^m}{c^m}{i}$ with
  $\genminoryz{c^{m \pm 1}}{c^{m \pm 1}}{i}$. Yang--Zelevinsky refer to
  these as \defined{primitive exchange relations}.

  Finally, a number $h(i;c)$ is defined such that
  $\genminoryz{c^{h(i;c)}}{c^{h(i;c)}}{i} = \genminoryz{}{}{i^{\ast}}$.
  This allows convenient analysis of periodicity of source/sink mutation
  sequences.
  \begin{proposition}[{\cite[Equation~2.13]{yangzelevinsky2008}}]
    \label{prop:def-h(i;c)}
    In some cases, $h(i;c)$ is easily calculated.
    \begin{itemize}
    \item
      When $i^{\ast} = i$ (for example, if $\sigma_G = e$) we trivially
      have $h(i;c) = 0$.
    \item
      Otherwise, when $h$ is even, $c^{h/2} = w_0$, and by action of
      $w_0$ on simple roots, $h(i;c) = \frac{h}{2}$.
    \end{itemize}
    When $G$ is of type $A_{\ell}$, however, the calculation is more
    delicate. Let \[ t_{+} = s_1 s_3 \dotsb s_{2 \lfloor (\ell+1)/2
        \rfloor - 1}, \qquad t_{-} = s_2 s_4 \dotsc s_{2 \lfloor
        (\ell+1)/2 \rfloor}, \qquad w_0 = \overbrace{t_{+} t_{-} \dotsb
        t_{\pm}}^{\text{$h = \ell + 1$ factors}}, \qquad c = t_{+}
      t_{-}. \] Then by \cite[Equation~2.13]{yangzelevinsky2008}, as $h
    = \ell + 1$ be the Coxeter number for $A_{\ell}$, \[ h(i;c) =
      \begin{cases} \lfloor \frac{h}{2} \rfloor = \lfloor \frac{\ell +
          1}{2} \rfloor & \text{$i$ even} \\ \lceil \frac{h}{2} \rceil =
        \lceil \frac{\ell + 1}{2} \rceil & \text{$i$ odd.} \end{cases}
    \]
  \end{proposition}
  Note that \[ \genminoryz{c^{m + h(k;c) + 1}}{c^{m + h(k;c) + 1}}{k} =
    \genminoryz{c^m}{c^m}{k^{\ast}}. \]

  We now combine several results of \cite{yangzelevinsky2008}, mainly
  Theorem~1.5.

  \begin{proposition}
    \label{prop:compressed-yang-zelevinsky}
    The cluster variables in $\mathcal{A}(c)$ satisfy the following
    primitive exchange relation (letting $A$ be the Cartan matrix): \[
      \genminoryz{c^{m-1}}{c^{m-1}}{k} \genminoryz{c^m}{c^m}{k} =
      \prod_{i \prec_{c} k} (\genminoryz{c^m}{c^m}{i})^{-A_{i,k}}
      \prod_{k \prec_{c} i}
      (\genminoryz{c^{m-1}}{c^{m-1}}{i})^{-A_{i,k}} + 1. \]
  \end{proposition}

  \begin{remark}
    This does not give us much information about $g \in L^{c,c^{-1}}$,
    but we will restrict our attention to periodic mutations. The only
    effect will be to change which root the vertices of the quiver are
    associated to.
  \end{remark}

  \subsection{Grid exchange relations}

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
