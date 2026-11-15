---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-030-73-rotation-mutations
section_title: "Rotation mutations"
section_number: 7.3
pages: 36-40
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.98
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:proof-of-rot}

  We now turn to verifying the longer mutations, starting with $\murot$.
  First, we recall work of Zickert to describe the effect of
  $\operatorname{rot}$ in terms of canonical forms, taking $(h_1, h_2,
  h_3, u)$ to $(h_3, h_1, h_2, \widetilde{u})$. We show, using an
  identity of Fomin--Zelevinsky, that when all $h_i$ are trivial,
  $\murottwistind$ takes coordinates of $u$ to those of $\widetilde{u}$.
  Then we show that the monomial map $\monomialmap$ of $\conftoquiv$ is
  exactly what is necessary to extend to the general case. The final
  pieces $\muint{O1}$ and $\muint{O2}$, rearrange the vertices without
  changing their coordinates according to
  \cref{lem:colsigmaG-does-sigmaG,lem:rowsigmaG-does-sigmaG}.

  Recall that by \cref{prop:Phi-Psi-and-rot}, we have \[ \widetilde{u} =
    h_2^{-1} (w_0(h_1))^{-1} (\Phi \Psi \Phi \Psi)(u) (w_0(h_1)) h_2. \]
  So we must consider $(\Phi \Psi)^{2}(u)$ in terms of minor
  coordinates, then show that the result agrees in general with the
  cluster action of $\murot$. In other words, we must show that
  $\murotind$ fits into the diagram of \cref{fig:Psi-Phi-murot-cd}. We
  interpret the actions of the maps $\Phi$ and $\Psi$ on generalized
  minors, then appeal to an identity of Fomin--Zelevinsky that applies
  at every step of the mutation sequence $\murottwist$.

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/Psi-Phi-murot-cd}

    \caption{Maps $\Phi$ and $\Psi$ by \cref{prop:Phi-Psi-and-rot},
      $\minorcoordmap_V$ by \cref{def:conf_3_star-to-seed-torus}.
      \label{fig:Psi-Phi-murot-cd}
    }
  \end{figure}

  \begin{lemma}
    \label{lem:fgcs-exists-rot-works-trivial}
    \Cref{def:fgcs-rot-works} of \cref{def:fgcs} holds for $h_1 = h_2 =
    h_3$ are all trivial.

  \end{lemma}
  \begin{proof}
    By \cref{rem:p-commutes-with-mutation}, we need only consider the
    commuting diagrams for $\mathcal{A}$-coordinates; the diagrams for
    $\mathcal{X}$-coordinates will then follow immediately by applying
    $\TtoZ$.

    Let $\widetilde{u} = (w_0(h_1))^{-1} (\Phi \Psi)^2(u) w_0(h_1) h_2$
    for notation. The core idea is that, modulo coordinates of $h_i$,
    $\genminoryz{w_k}{e}{i_k}(u)$ is approximately
    $\genminoryz{w_0}{w_k}{i_k}(\widetilde{u})$. The mutation sequence
    $\murot$ transforms $\genminoryz{w_0}{w_k}{i_k}$ to
    $\genminoryz{w_k}{e}{i_k}$ by
    \cite[Theorem~1.17]{fominzelevinsky1999}, therefore changing
    coordinates of $u$ into coordinates of $\widetilde{u}$. Later, we
    will show that the monomial map exactly compensates for the
    coordinates of $h_i$.

    To be more precise, the coordinate assigned to interior vertex
    $v_{i,j}$ is (letting $k = k(i,j)$ as in
    \cref{def:conf_3_star-to-seed-torus}) \[ v_{i,j} =
      \genminoryz{w_k}{e}{i_k}(u) \cdot
      \genminor{}{i}(\sigma_G(h_1^{-1}) h_2) \cdot \genminornumerator{w_{k(i,j)}}{\fundamentalweight_i}(\sigma_G(h_1))
    \] Focusing on the first term, consider $(\Phi \Psi)^2(u) = [ \Psi([
        \Psi(u) \lifttoG{w_0} ]_{-}) \lifttoG{w_0} ]_{-}$. Letting
    $x_{\bullet} \in N_{+}$, $h_{\bullet} \in H$, and $y_{\bullet} \in
    N_{-}$,
    \begin{align*}
      y_0 &= u & x_1 &= \Psi(y_0) & y_2 H_2 x_2 &= x_1 \lifttoG{w_0} \\
      y_2 &= (\Phi \Psi)(u) & x_3 &= \Psi(y_2) & y_4 H_4 x_4 &= x_3 \lifttoG{w_0} \\
      y_4 &= (\Phi \Psi)^2(u).
    \end{align*}
    Expanding those terms, we have
    \begin{align*}
      y_4 H_4 x_4 &= x_3 \lifttoG{w_0} \\
      &= \Psi(y_2) \lifttoG{w_0} \\
      &= \Psi(x_1 \lifttoG{w_0} x_2^{-1} H_2^{-1}) \lifttoG{w_0} \\
      &= \Psi(\Psi(y_0) \lifttoG{w_0} x_2^{-1} H_2^{-1}) \lifttoG{w_0} \\
      &= \Psi(H_2^{-1}) \Psi(x_2^{-1}) \Psi(\lifttoG{w_0}) y_0 \lifttoG{w_0} \\
      &= H_2^{-1} \Psi(x_2^{-1}) \lifttoG{w_0} y_0 \lifttoG{w_0} \\
      &= \overbrace{H_2^{-1} \Psi(x_2^{-1}) H_2}^{\in N_{-}} \cdot \overbrace{H_2^{-1} s_G}^{\in H} \cdot \overbrace{\lifttoG{w_0}^{-1} y_0 \lifttoG{w_0}}^{\in N_{+}}
    \end{align*}
    Extracting the $N_{-}$ term, $(\Phi \Psi)^2(u) = y_4 = H_2^{-1}
    \Psi(x_2^{-1}) H_2$, which we can rewrite via \[ H_2 = [ \Psi(y_0)
        \lifttoG{w_0} ]_{0}, \qquad x_2 = \Psi([\Psi(y_0) \lifttoG{w_0}
      ]_{+}^{-1}). \]

    Now, consider the minor $\genminoryz{w_0}{w_k}{i_k}(y_4)$. Denote by
    $w_k^{\ast}$ the word defined by \cref{def:gamma-k} using fixed
    presentation $\word{i}^{\ast} = \sigma_G(\word{i})$. By relying on a
    number of identities from \cite{fominzelevinsky1999},
    \begin{align*}
      \genminoryz{w_0}{w_k}{i_k}(H_2^{-1} \Psi(x_2^{-1}) H_2) &= \frac{\genminoryz{w_0}{w_k}{i_k}(\Psi(x_2^{-1})) \cdot \genminoryz{w_k}{w_k}{i_k}(H_2)}{\genminoryz{w_0}{w_0}{i_k}(H_2)} \tag{\cite[Equation~2.14]{fominzelevinsky1999}} \\
      \genminoryz{w_0}{w_k}{i_k}(\Psi(x_2^{-1})) &= \genminoryz{w_k}{w_0}{i_k}(x_2^{-1}) \tag{\cite[Equation~2.25]{fominzelevinsky1999}} \\
      &= \genminoryz{w_k}{w_0}{i_k}( \Psi([\Psi(y_0)\lifttoG{w_0} ]_{+}^{-1})^{-1} ) \\
      &= \genminoryz{w_k^{\ast}}{w_0}{i_k^{\ast}}( \lifttoG{w_0} [\Psi(y_0)\lifttoG{w_0} ]_{+}^{-1} \lifttoG{w_0}^{-1} ) \\
      &= \genminoryz{w_0w_k^{\ast}}{e}{i_k^{\ast}}( [\Psi(y_0)\lifttoG{w_0} ]_{+}^{-1} ) \\
      &= \genminoryz{w_0w_k^{\ast}}{e}{i_k^{\ast}}( [\lifttoG{w_0} y_0]_{-} ) \\
      &= \left(\genminoryz{w_0w_k^{\ast}}{e}{i_k^{\ast}}( \lifttoG{w_0} y_0 )\middle) \middle/ \middle(\genminoryz{e}{e}{i_k^{\ast}}(\lifttoG{w_0} y_0) \right) \tag{\cite[Equation~2.23]{fominzelevinsky1999}} \\
      &= \left(\genminoryz{w_k^{\ast}}{e}{i_k^{\ast}}( y_0 ) \middle) \middle/ \middle( \genminor{}{i_k^{\ast}}([\lifttoG{w_0}^{-1} y_0]_{0}) \right)
    \end{align*}
    Also, by \cref{lem:canonical-form-for-conf_3_star}, $H_2 =
    [\Psi(y_0) \lifttoG{w_0}]_{0} = [\lifttoG{w_0}^{-1} y_0]_{0} =
    (w_0(h_3 h_1) h_2)^{-1}$, where the $h_i$ in the last term refer to
    the elements of $H$ in the canonical form for
    $\Conf_{3}^{\ast}(G/N_{+})$. Writing solely in terms of $(h_1, h_2,
    h_3, u)$), we have
    \begin{align*}
      \genminoryz{w_0}{w_k}{i_k}((\Phi \Psi)^2(u)) &= \genminoryz{w_k^{\ast}}{e}{i_k^{\ast}}(u) \cdot \frac{ \genminoryz{w_0}{w_0}{i_k}( w_0(h_3 h_1)h_2 ) \genminoryz{e}{e}{i_k^{\ast}}( w_0(h_3 h_1)h_2 ) }{ \genminoryz{w_k}{w_k}{i_k}( w_0(h_3 h_1) h_2 ) } \\
      &= \genminoryz{w_k^{\ast}}{e}{i_k^{\ast}}(u) \cdot \frac{ 1 }{ \genminoryz{w_k}{w_k}{i_k}( w_0(h_3 h_1) h_2 ) } \\
    \end{align*}
    Now, introducing the factor of $w_0(h_1) h_2$, we have
    \begin{align*}
      \genminoryz{w_0}{w_k}{i_k}(\widetilde{u}) &= \genminoryz{w_0}{w_k}{i_k}((w_0(h_1))^{-1} (\Phi \Psi)^2(u) w_0(h_1) h_2) \\
      &= \genminoryz{w_0}{w_k}{i_k}((\Phi \Psi)^2(u)) \cdot \genminoryz{w_0}{w_0}{i_k}(w_0(h_1)^{-1}h_2^{-1}) \cdot \genminoryz{w_k}{w_k}{i_k}(w_0(h_1)h_2) \\
      &= \genminoryz{w_k^{\ast}}{e}{i_k^{\ast}}(u) \cdot \frac{1}{ \genminoryz{w_k}{w_k}{i_k}(w_0(h_3)) \genminoryz{w_0}{w_0}{i_k}(w_0(h_1) h_2) }
    \end{align*}

    Thus, including the assignment of the monomial map $\monomialmap$,
    the coordinate at $v_{i,j}$ is given by
    \begin{align*}
      v_{i,j} &= \genminoryz{w_0}{w_k}{i_k}(\widetilde{u}) \cdot \overbrace{\genminoryz{e}{e}{i_i}(w_0(h_1) h_2) \cdot \genminoryz{w_0}{w_0}{i_k}(w_0(h_1)h_2)}^{1} \cdot \genminoryz{w_k}{w_k}{i_k}(w_0(h_3)) \cdot \genminornumerator{w_k}{\fundamentalweight_{i_k}}(w_0(h_1^{-1})) \\
      &= \genminoryz{w_0}{w_k}{i_k}(\widetilde{u} \cdot w_0(h_3)) \cdot \genminornumerator{w_k}{\fundamentalweight_{i_k}}(w_0(h_1^{-1}))
    \end{align*}

    In the case that $h_1 = h_2 = h_3 = e$, we may ignore the frozen
    vertices of the quiver. The proof is completed by appealing to the
    identity of \cite[Theorem~1.17]{fominzelevinsky1999}, which states
    that when $\length(u s_i) = \length(u) + 1$ and $\length(v s_i) =
    \length(v) + 1$, \[ \genminoryz{u}{v}{i} \genminoryz{us_i}{vs_i}{i}
      = \genminoryz{u s_i}{v}{i} \genminoryz{v}{u s_i}{i} + \prod_{j \ne
        i} \genminoryz{u}{v}{i}^{-a_{ji}}. \]

    This identity exactly matches the quiver mutation relation at each
    step of $\murottwist$, so each $\mucol(i)$ in $\murot$ transforms
    the coordinates of $v_{i,\bullet}$ from \[
      \genminoryz{c^n}{c^m}{j}(\widetilde{u})\] to \[
      \genminoryz{c^{n-1}}{c^{m-1}}{j}(\widetilde{u}).\] Thus, after
    applying $\murottwist$ the vertex $v_{i,j}$ has coordinate \[
      \genminoryz{w_{m+r-k}^{\ast}}{e}{i_k^{\ast}}(\widetilde{u}). \] By
    \cref{lem:colsigmaG-does-sigmaG,lem:rowsigmaG-does-sigmaG},
    $\muint{O1}$ converts the $w_{m+r-k}$ to $w_k$, and $\muint{O2}$
    removes the $\cdot^{\ast}$. Thus $\murot$ changes coordinates for
    $u$ into those for $h_2^{-1} w_0(h_1)^{-1} (\Phi \Psi)^2(u) w_0(h_1)
    h_2$ as desired.
  \end{proof}

  \begin{proof}[Proof of \cref{lem:murot-works-for-making-Q}]
    Since we ignored frozen vertices above, the result applies to $Q_0$.
    Since the quiver mutation changes coordinates of $\alpha$ to those
    of $\operatorname{rot}(\alpha)$, it is of order 3 and induces a
    graph isomorphism.
  \end{proof}

  \begin{lemma}
    \label{lem:fgcs-exists-rot-works-nontrivial}
    \Cref{def:fgcs-rot-works} of \cref{def:fgcs} holds for arbitrary
    $h_1, h_2, h_3$.
  \end{lemma}
  \begin{proof}
    In the case that $h_1, h_2, h_3$ are not trivial, we must verify
    that the equation of \cite[Theorem~1.17]{fominzelevinsky1999} still
    holds with the frozen vertices considered, which introduce factors
    not included in the equation. Again, we only consider
    $\mathcal{A}$-coordinates by \cref{rem:p-commutes-with-mutation}. We
    note the following:

    \begin{itemize}
    \item
      The vertices $B_k$ take the place of
      $\genminoryz{w_0}{e}{i_k}(\widetilde{u}) =
      \chi_{i_k^{\ast}}([\lifttoG{w_0}^{-1} \widetilde{u}]_{0}) =
      \chi_{i_k^{\ast}}(w_0(h_2 h_3) h_1)^{-1}$ in the equation.
      Therefore, they should be considered as \[ B_k =
        \genminoryz{w_0}{e}{i_k}(\widetilde{u}) \cdot
        \frac{A_{k^{\ast}}}{C_k} =
        \genminoryz{w_0}{e}{i_k}(\widetilde{u} \cdot w_0(h_3)) \cdot
        A_{k^{\ast}}. \]
    \item
      If, at each step of the mutation, the frozen vertices and the
      monomial map $\monomialmap$ induce equal extra factors on the
      $\genminoryz{u s_i}{v}{i} \genminoryz{v}{u s_i}{i}$ and $\prod_{j
        \ne i} \genminoryz{u}{v}{i}^{-a_{ji}}$ terms, then the
      difference of the final terms from coordinates of $\widetilde{u}$
      will also be a monomial map.
    \item
      If this final difference monomial map matches $\monomialmap$, the
      result will be proven.
    \item
      Since the extra factors at each coordinate are given by a monomial
      map, each frozen vertex may be checked individually.
    \end{itemize}

    For any particular group, these results may be verified by a few
    numerical calculations: to verify the monomial identity $x_1^{a_1}
    \dotsb x_m^{a_m} \stackrel{?}{=} x_1^{b_1} \dotsb x_m^{b_m}$, taking
    $\log$ of both sides reduces to $\sum_{i} \log(x_i) (a_i - b_i)
    \stackrel{?}{=} 0$. Therefore, evaluating at $m+1$ linearly
    independent choices of vector $\langle\log(x_i)\rangle$ verifies the
    result. This has been carried out for the exceptional groups. The
    \texttt{test-murot} sub-program of \cite{gilles2020sw} may be used
    for this purpose.

    We present an argument that the coordinates of $h_1$ are treated
    correctly by the monomial map and $\murot$ for type $D_n$; other
    arguments are similar.

    We will ignore all terms other than $h_{1,j} = A_j$, and annotate
    vertices with these. Half the Coxeter number minus one will be
    denoted $\ell$, which in the case of $D_n$ is equal to $n - 2$. Then
    we will trace the effects of $\murottwist$ in general. The objective
    is to show that, starting with the assignments given by the monomial
    factors attached to $\genminoryz{w_0}{w_k}{i_k}(\widetilde{u})$
    above, we end with those factors of given by the monomial map
    $\monomialmap$ following $\operatorname{rot}$ (i.e.\ the powers
    associated to $h_2$ by $\monomialmap$). Before applying any
    mutations, $Q_{D_n}$ is as in \cref{fig:murot-QD7-stage0}. The
    formula for $A_j$ factors is, following
    $\genminornumerator{w_k}{\fundamentalweight_{i_k}}(w_0(h_1^{-1}))$,
    \[ \text{at }v_{i,j} : \begin{cases} A_{j} & i \ge n-1 \\ A_{j} & i
        < n-1, i + j < n \\ A_{j} A_{i+j+1-n} & i < n-1, i + j \ge n
      \end{cases} \qquad \text{at }A_k: A_k, \qquad \text{at }B_k:
      A_{k^{\ast}}, \qquad \text{at }C_k: 1 \]

    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/murot-QD7-stage0}

      \caption{$Q_{D_n}$ before any mutation.
        \label{fig:murot-QD7-stage0}
      }
    \end{figure}

    After one iteration of $\mucol(1)$, by straight-forward induction
    the factor at $v_{i,j}$ matches that at $v_{i,j+1}$, as in
    \cref{fig:murot-QD7-stage1}.

    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/murot-QD7-stage1}

      \caption{$Q_{D_n}$ after $\mucol(1)$.
        \label{fig:murot-QD7-stage1}
      }
    \end{figure}

    After $\prod_{y=1}^{\ell} \mucol(y)$, this pattern continues as
    shown in \cref{fig:murot-QD7-stage2}: for $j < \ell$, we have the
    factor at $v_{i,j}$ matching the original factor at $v_{i,j+1}$. At
    $v_{i,\ell}$, however, the factor matches the original factor
    associated to $B_i$. Therefore, the new formula for $A_j$ factors at
    $v_{i,j}$ is \[ \text{at }v_{i,j} : \begin{cases} A_{i^{\ast}} & j =
        \ell \\ A_{j+1} & j < \ell, i \ge n-1 \\ A_{j+1} & j < \ell, i <
        n-1, i + j < n \\ A_{j+1} A_{i+j+2-n} & j < \ell, i < n-1, i + j
        \ge n \end{cases} \]

    \begin{figure}[h]
      \centering
      \includestandalone[mode=image|tex]{fig/murot-QD7-stage2}

      \caption{$Q_{D_n}$ after $\prod_{y=1}^{\ell}\mucol(y)$.
        \label{fig:murot-QD7-stage2}
      }
    \end{figure}

    Each successive $\prod_{y=1}^{\dotsc} \mucol(y)$ performs the same
    adjustment: factors of $A_j$ are copied from left to right. As can
    be shown by induction, after $\prod_{x=1}^{k} \prod_{y=1}^{\ell + 1
      - x} \mucol(y)$, the formula for $A_j$ factors at $v_{i,j}$ is \[
      \text{at }v_{i,j} : \begin{cases} A_{i^{\ast}} & j > \ell - k \\
        A_{j+k} & j \le \ell - k, i \ge n-1 \\ A_{j+k} & j \le \ell - k,
        i < n-1, i + j < n \\ A_{j+k} A_{i+j+1+k-n} & j \le \ell - k, i
        < n-1, i + j \ge n \end{cases} \]

    Thus, after applying $\murottwist$, each $v_{i,j}$ has a factor of
    $A_{i^{\ast}}$ attached. Since the monomial map $\monomialmap$
    associates a factor of $\genminor{}{i}(h_2) = B_{i}$, rotation
    renames $A_{\bullet}$ to $B_{\bullet}$, and $\muint{O1}$ renames
    $v_{i,j}$ to $v_{i^{\ast},j}$, the result is proven.

    Proofs that the monomial map works correctly for factors of $h_2$
    and $h_3$ for type $D$, and for all factors of type $A$, $B$, and
    $C$, have similar forms, and the result has been numerically checked
    for exceptional types. This proves the result in all cases.
  \end{proof}
