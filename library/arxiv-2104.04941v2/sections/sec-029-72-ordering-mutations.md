---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-029-72-ordering-mutations
section_title: "Ordering mutations"
section_number: 7.2
pages: 34-36
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.967
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
The ends of both $\murot$ and $\muflip$ are sequences of $\murowperm$
  and $\mucolperm$. We must show that these permute Dynkin sub-quivers
  of $Q$ by switching certain vertices without changing the cluster
  seed, as in \cref{rem:sigma_G-action-on-Dynkin-diagram}. These are
  used in \cref{lem:fgcs-exists-rot-works-trivial,lem:fgcs-exists-rot-works-nontrivial,lem:fgcs-exists-flip-works}
  to justify the $\muint{Oi}$ parts.

  \begin{lemma}
    \label{lem:colsigmaG-does-sigmaG}
    The permutation $\mucolperm$ of
    \cref{def:murot-components,def:muflip-components} acts on quivers
    (and cluster ensembles) by permuting the vertices of the appropriate
    column according to $\sigma_G$.
  \end{lemma}
  \begin{lemma}
    \label{lem:rowsigmaG-does-sigmaG}
    The permutation $\murowperm$ of
    \cref{def:murot-components,def:muflip-components} acts on quivers
    (and cluster ensembles) by permuting the vertices of the mutated
    sub-quiver according to $\sigma_{A_{\ell}}$.
  \end{lemma}

  These proofs rely heavily on results of \cite{yangzelevinsky2008}
  described in \cref{sec:yz-dynkin-identity}. In short, we shall
  restrict the quivers on which $\mucolperm$ and $\murowperm$ act to
  those which Yang--Zelevinsky can strongly analyze. We then use
  counting arguments to establish that the mutation acts by permutation,
  and use classic results to apply these results to larger quivers.

  \begin{proof}[Proof of \cref{lem:colsigmaG-does-sigmaG}]
    In our construction, whenever $\mucolperm$ is applied, the vertices
    at which it mutates form a subquiver of Dynkin type. Therefore,
    first, we shall show that the result holds when $\mucolperm$ is
    applied to a quiver which is of Dynkin type. Then we shall show that
    the result holds for larger quivers which contain a sub-quiver of
    Dynkin type.

    First, suppose $\mucolperm$ acts on quiver of Dynkin type (non
    $A_{2n}$). There exists an element $g$ of $L^{c,c^{-1}}$ such that
    the initial cluster coordinate at $v_k$ is $\genminoryz{}{}{k}(g)$.

    Now we note that $\mucolperm$ is exactly $\ell + 2 = \frac{h}{2} +
    1$ iterations of a mutation following the Coxeter element $c$, with
    each mutation replacing $\genminoryz{c^m}{c^m}{k}$ with
    $\genminoryz{c^{m+1}}{c^{m+1}}{k}$. Since the number $h(i;c)$ is
    always $\frac{h}{2}$ by our construction of $c$, from
    \cref{prop:compressed-yang-zelevinsky} we obtain that the final
    cluster coordinate at $v_k$ is \[ \genminoryz{c^{h(k;c) +
          1}}{c^{h(k;c) + 1}}{k}(g) = \genminoryz{}{}{k^{\ast}}(g), \]
    which was the initial coordinate at $v_{k^{\ast}}$.

    Thus $\mucolperm$ acts on the cluster by permuting the associations
    between vertices and cluster variables according to $\sigma_G$. In
    this way we obtain the desired result without ever having to rely
    directly facts of $g \in L^{c,c^{-1}}$.

    Now it must be shown that this holds when $\mucolperm$ acts on a
    larger quiver. Since the action of $\mucolperm$ is solely a
    permutation on the mutable portion of the quiver, it preserves the
    set of cluster variables. By
    \cite[Theorem~1.12]{fominzelevinsky2003} and the finiteness of
    Dynkin-type quivers, the cluster variables determine the exchange
    matrix and therefore the quiver. Therefore the action of
    $\mucolperm$ on the graph must be trivial up to renaming, and
    therefore must be exactly the renaming that we have created.
  \end{proof}

  \begin{proof}[Proof of \cref{lem:rowsigmaG-does-sigmaG}]
    We would like to apply exactly the same argument as in the proof of
    \cref{lem:colsigmaG-does-sigmaG}. However, since rows are of type
    $A_{\ell}$ and our construction algorithm for $Q$ does not allow
    $\murowperm$ to be repeated iterations of a single Coxeter-style
    mutation, we must be a bit more careful.

    For a type $A_{\ell}$, define $\Q{Lin} = Q_{A_{\ell},\text{Lin}}$ as
    the Dynkin quiver where the graph describes a linear ordering from
    left to right. Also, let $\Q{Alt} = Q_{A_{\ell},\text{Alt}}$ be the
    Dynkin quiver in source-sink position, see
    \cref{fig:dynkin-type-Al}.

    \begin{figure}[h]
      \centering \includestandalone[mode=image|tex]{fig/dynkin-type-Al}

      \caption{$\Q{Alt}$ on the left, $\Q{Lin}$ on the right, both
        quivers of Dynkin type $A_{\ell}$.
        \label{fig:dynkin-type-Al}
      }
    \end{figure}

    We also introduce one more piece of notation.
    \begin{fact}
      \label{fac:Y-sub-parity}
      Let $Y(x)$ be defined as $\frac{1}{2}$ when $x$ is odd and $0$
      when $x$ is even. Then \[ Y(a) - Y(b) =
        (-1)^{\operatorname{parity} a}Y(a-b). \]
    \end{fact}

    As above, we will interpret the cluster coordinates of the mutable
    Dynkin-type quiver as minor coordinates on some $g \in
    L^{c,c^{-1}}$, but we cannot interpret them as the initial minors.

    The mutation $\murowperm$ acts on $\ell = b - a$ vertices, always
    arranged as in $\Q{Lin}$ of \cref{fig:dynkin-type-Al}. Recalling
    notation of \cref{prop:def-h(i;c)}, by \cite{yangzelevinsky2008} the
    quiver $\Q{Alt}$ (together with cluster variables
    $\genminoryz{}{}{i}$ at $v_{i}$) is an initial seed, governed by an
    element of $L^{t_{+}t_{-},(t_{+}t_{-})^{-1}}$.

    It is straightforward that (up to Langlands dualizing, which has no
    effect on coordinates) the mutation
    \begin{equation*}
      \begin{aligned}
        \muint{Lin} &= \begin{cases}\mu\Set{v_1, v_3, \dotsc, v_{\ell - 0}, \quad v_2, v_4, \dotsc, v_{\ell - 1}, \quad \dotsc, \quad v_1, v_3, \quad v_2, \quad v_1} & \text{$\ell$ odd} \\ \mu\Set{v_1, v_3, \dotsc, v_{\ell - 1}, \quad v_2, v_4, \dotsc, v_{\ell - 2}, \quad \dotsc, \quad v_1, v_3, \quad v_2, \quad v_1} & \text{$\ell$ even} \end{cases} \\
        &= \prod_{j= 2 \lfloor \ell / 2 \rfloor - (\ell - 1)}^{\ell - 1} \begin{cases} \prod_{k=1}^{\lceil (\ell - j) / 2 \rceil} \mu\set{v_{2k - 1}} & \text{$\ell - j$ odd} \\ \prod_{k=1}^{(\ell - j) / 2} \mu\set{v_{2k}} & \text{$\ell - j$ even} \end{cases}
      \end{aligned}
    \end{equation*}
    transforms $\Q{Alt}$ to $\Q{Lin}$, using only source or sink
    mutations (thus governed by primitive exchange relations). By
    considering these relations, and counting mutations, it is also
    straightforward that the cluster coordinates of $\Q{Lin}$ are given
    by the following.
    \begin{equation*}
      \text{coordinate at $v_k$ is $\genminoryz{c^{(\ell - k)/2 +
            Y(\ell) + Y(k)}}{c^{(\ell - k)/2 + Y(\ell) + Y(k)}}{k}$}
    \end{equation*}
    For example, coordinates of $Q_{A_4,\text{Lin}}$ are
    $\Set{\genminoryz{c^2}{c^2}{1}, \genminoryz{c^1}{c^1}{2},
      \genminoryz{c^1}{c^1}{3}, \genminoryz{c^0}{c^0}{4}}$, and the
    coordinates for $Q_{A_3,\text{Lin}}$ are
    $\Set{\genminoryz{c^2}{c^2}{1}, \genminoryz{c^1}{c^1}{2},
      \genminoryz{c^1}{c^1}{3}}$. To prove the lemma, we must show that
    $\murowperm$ permutes these by $\sigma_G$, which in the case of
    $A_{\ell}$ replaces each $\fundamentalweight_k$ with
    $\fundamentalweight_{\ell + 1 - k}$.

    Since $\murowperm$ also consists entirely of source-or-sink
    mutations, it is also governed by primitive exchange mutations. Let
    \[ \muint{A} = \prod_{k=1}^{\ell} \prod_{j=0}^{\ell - k} \muT(i, 1 +
      j), \qquad \muint{B} = \prod_{j=1}^{\ell} \muT(i, \ell - j), \] so
    that $\murowperm = \muint{A} \muint{B}$. We make the following
    observations, which are all easily checked by induction:
    \begin{itemize}
    \item
      During $\muint{A}$, whenever a vertex $v_{k}$ is mutated at with
      $k$ odd, $v_{k}$ has coordinate $\genminoryz{c^m}{c^m}{k}$ while
      its neighbors have coordinates $\genminoryz{c^{m -
          1}}{c^{m-1}}{k-1}$ and $\genminoryz{c^{m - 1}}{c^{m-1}}{k+1}$.
      Since $k \prec_{c} k \pm 1$, the coordinate at $v_{k}$ becomes
      $\genminoryz{c^{m-1}}{c^{m-1}}{k+1}$.
    \item
      During $\muint{A}$, whenever a vertex $v_{k}$ is mutated at with
      $k$ even, $v_{k}$ has coordinate $\genminoryz{c^m}{c^m}{k}$ and
      its neighbors have coordinates $\genminoryz{c^m}{c^m}{k-1}$ and
      $\genminoryz{c^m}{c^m}{k+1}$. Since $k \pm 1 \prec_{c} k$, the
      coordinate at $v_{k}$ becomes
      $\genminoryz{c^{m-1}}{c^{m-1}}{k+1}$.
    \item
      By the same logic as the above statements every mutation in
      $\muint{B}$ takes the coordinate at $v_{k}$ from $\genminoryz{c^{m
        }}{c^{m}}{k}$ to $\genminoryz{c^{m+1}}{c^{m+1}}{k}$.
    \end{itemize}

    Therefore, since $\muint{A}$ touches vertex $k$ a total of $\ell - k
    + 1$ times and $\muint{B}$ touches each vertex once, we may conclude
    via \cref{prop:compressed-yang-zelevinsky} that after
    $\muint{A}\muint{B}$ the coordinates are given by
    \begin{equation*}
      \text{coordinate at $v_k$ is $\genminoryz{c^{(\ell - k)/2 +
            Y(\ell) + Y(k) - (\ell - k)}}{c^{(\ell - k)/2 + Y(\ell) +
            Y(k) - (\ell - k)}}{k}$.}
    \end{equation*}

    Now, let us consider the difference between the exponents of $c$ in
    the final coordinate of $v_{k}$ and in the initial coordinate of
    $v_{k^{\ast}}$. If the difference is $-h(k^{\ast};c) - 1$, then
    \cref{prop:compressed-yang-zelevinsky} will show that $\murowperm$
    acts by permuting vertices according to $\sigma_G$.

    \begin{align*}
      \text{final at $k$} - \text{initial at $k^{\ast}$} &= \left[ \frac{\ell - k}{2} + Y(\ell) + Y(k) - (\ell - k) \right] - \left[\frac{\ell - k^{\ast}}{2} + Y(\ell) + Y(k^{\ast}) \right] \\
      &= \frac{k^{\ast} - k}{2} - (\ell - k) + Y(k) - Y(k^{\ast}) \\
      &= \frac{(\ell + 1 - k) - k}{2} - (\ell - k) + Y(k) - Y(\ell + 1 - k) \\
      &= -\left[\frac{\ell + 1}{2} - Y(k) + Y(\ell + 1 - k)\right] - 1 \\
      &= \begin{cases} -\left[ \frac{\ell + 1}{2} + Y(\ell + 1)\right] - 1 & \text{$\ell + 1 - k$ odd} \\ -\left[ \frac{\ell + 1}{2} - Y(\ell + 1)\right] - 1 & \text{$\ell + 1 - k$ even}\end{cases} \tag{\Cref{fac:Y-sub-parity}} \\
      &= \begin{cases} -\lceil\frac{\ell + 1}{2}\rceil - 1 & \text{$k^{\ast}$ odd} \\ -\lfloor \frac{\ell + 1}{2}\rfloor - 1 & \text{$k^{\ast}$ even}\end{cases} \\
    \end{align*}
    Consulting \cref{prop:def-h(i;c)}, the exponent difference is indeed
    $-h(k^{\ast};c) - 1$, so the action of $\murowperm$ is to rearrange
    the vertices of $\Q{Lin}$ according to $\sigma_G$. From here, the
    action of $\murowperm$ generalizes to larger quivers as in the proof
    for $\mucolperm$.
  \end{proof}
