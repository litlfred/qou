---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-031-74-flip-mutations
section_title: "Flip mutations"
section_number: 7.4
pages: 40-44
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.977
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
We now verify the longest flip mutation: the flip. The idea of the
  proof is similar to that of $\murot$. First, we put the coordinates of
  $\Qdv$ into a rectangular pattern, then apply mutations that respect
  \cite[Theorem~1.17]{fominzelevinsky1999}, showing that the resulting
  coordinates are of $\Qdh$. The most significant difficulty is to
  construct the element of $G$ holding the appropriate generalized
  minors, which we obtain by a result of Zickert.

  \begin{lemma}
    \label{lem:fgcs-exists-flip-works}
    \Cref{def:fgcs-flip-works} of \cref{def:fgcs} holds.
  \end{lemma}
  \begin{proof}
    This proof almost entirely focuses on $\muflipcore$. The prefix,
    $\muint{P}$, is a sequence of rotations as depicted in
    \cref{fig:Qdv-naming}. The suffix, $\muint{O3} \muint{O4}
    \muint{O5}$, is a reordering that switches the left and right sides.

    Let $\alpha = (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) \in
    \Conf_4^{\ast}(G/N_{+})$, and recall
    \cref{def:gluing-configurations}. For notation, let
    \begin{align*}
      \alpha_{012} &= (g_0 s_G N_{+}, g_1 N_{+}, g_2 N_{+}) & \alpha_{023} &= (g_0 N_{+}, g_2 N_{+}, g_3 N_{+}) \\
      \alpha_{123} &= (g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) & \alpha_{013} &= (g_0 N_{+}, g_1 s_G N_{+}, g_3 N_{+}),
    \end{align*}
    with other $\alpha_{ijk}$ defined by rotation, and let $u_{ijk}$ be
    the element of $N_{-}$ in the canonical form of $\alpha_{ijk}$. As
    usual, let $h_{ij} = [ \lifttoG{w_0}^{-1} g_i^{-1} g_j]_{0}$.

    We must show that $\muflip$ takes $\Qdv$ to $\Qdh$. By an argument
    entirely analogous to that of
    \cref{lem:fgcs-exists-rot-works-nontrivial}, we assume that all edge
    coordinates of $\alpha_{123}$ and $\alpha_{013}$ are trivial. That
    is, every $h_{ij}$ is trivial except $h_{20}$ and $h_{02}$. We also
    appeal to \cref{rem:p-commutes-with-mutation}, and only consider
    $\mathcal{A}$-coordinates.

    By \cref{def:dv-dh-construction}, coordinates for $\Qdv$ come from
    $\alpha_{012}$ and $\alpha_{023}$. After applying $\muP$, these are
    rotated to $\alpha_{120}$ and $\alpha_{230}$. Treating
    $\alpha_{230}$ as the rotation of $\alpha_{302}$, the coordinates
    are given by \[ \genminoryz{w_k}{}{\word{i}_k}(u_{120}) \quad
      \text{and} \quad \genminoryz{w_k}{}{\word{i}_k}(u_{230}). \]

    We must show that $\muflipcore$ takes these to \[
      \genminoryz{w_k}{}{\word{i}_k}(u_{123}) \quad \text{and} \quad
      \genminoryz{w_k}{}{\word{i}_k}(u_{013}). \]

    Now consider $g = \Phi^{-1}(u_{123}) u_{130} h_{31}^{-1} h_{30}$. We
    also have $g = u_{120} h_{20} w_0(h_{12}) \Phi^{-1}(u_{023})$ by
    \cite[Proposition~5.14]{zickert2016}, and this will be identity
    which relates the two sides of the flip. All the coordinates we need
    are, up to edge coordinates, minors of $g$.

    \begin{align*}
      \genminoryz{w_k}{}{\word{i}_k}(u_{120}) &= \chi_{\fundamentalweight_{\word{i}_k}}\left(\left[ \dlifttoG{w_k^{-1}} [g]_{-} \right]_{0}\right) \\
      &= \chi_{\fundamentalweight_{\word{i}_k}}\left(\left[ \dlifttoG{w_k^{-1}} g [g]_{0}^{-1} \left( [g]_{0}^{-1} [g]_{+}^{-1} [g]_{0} \right) \right]_{0}\right) \\
      &= \chi_{\fundamentalweight_{\word{i}_k}}\left(\left[ \dlifttoG{w_k^{-1}} g \right]_{0} \right) / \chi_{\fundamentalweight_{\word{i}_k}} \left( [g]_{0} \right) \\
      &= \genminoryz{w_k}{}{\word{i}_k}(g) \frac{1}{\chi_{\fundamentalweight_{\word{i}_k}}(h_{20} w_0(h_{12}))} \\
      &= \genminoryz{w_k}{}{\word{i}_k}(g) \frac{1}{\chi_{\fundamentalweight_{\word{i}_k}}(h_{20}) \chi_{\fundamentalweight_{\word{i}_k}}(w_0(h_{12}))}
    \end{align*}
    \begin{align*}
      \genminoryz{w_k}{}{\word{i}_k}(u_{302}) &= \genminoryz{w_k}{}{\word{i}_k}( (\Phi \Psi \Phi \Psi)(u_{023}) ) \frac{\genminoryz{}{}{\word{i}_k}(w_0(h_{02}) h_{23})}{\genminoryz{w_k}{w_k}{\word{i}_k}(w_0(h_{02}) h_{23})} \\
      &= \genminoryz{w_k}{}{\word{i}_k}( [[\lifttoG{w_0} u_{023}]_{+} \lifttoG{w_0}]_{-}) \frac{\genminoryz{w_k}{w_k}{\word{i}_k}(w_0(h_{02}) h_{23})}{\genminoryz{w_0}{w_0}{\word{i}_k}(w_0(h_{02}) h_{23})} \\
      &= \genminoryz{w_k}{}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{-}^{-1}) \frac{\genminoryz{}{}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_k}{w_k}{\word{i}_k}(w_0(h_{02}) h_{23})}{\genminoryz{w_k}{w_k}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_0}{w_0}{\word{i}_k}(w_0(h_{02}) h_{23})} \\
      &= \genminoryz{}{w_k^{\ast}}{\word{i}_k^{\ast}}([g]_{+}) \frac{\genminoryz{}{}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_k}{w_k}{\word{i}_k}(w_0(h_{02}) h_{23})}{\genminoryz{w_k}{w_k}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_0}{w_0}{\word{i}_k}(w_0(h_{02}) h_{23})} \\
      &= \genminoryz{}{w_k^{\ast}}{\word{i}_k^{\ast}}(g) \frac{\genminoryz{}{}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_k}{w_k}{\word{i}_k}(w_0(h_{02}) h_{23})}{ \genminoryz{}{}{\word{i}_{k}^{\ast}}([g]_{0}) \genminoryz{w_k}{w_k}{\word{i}_k}([\lifttoG{w_0} u_{023}]_{0}) \genminoryz{w_0}{w_0}{\word{i}_k}(w_0(h_{02}) h_{23})} \\
      &= \genminoryz{}{w_k^{\ast}}{\word{i}_k^{\ast}}(g) \frac{\chi_{\fundamentalweight_{\word{i}_k}}\left(w_0(h_{20} h_{30}^{-1}) h_{12}\right)}{\genminoryz{w_k}{w_k}{\word{i}_k}(h_{03})} \\
      &= \genminoryz{}{w_k^{\ast}}{\word{i}_k^{\ast}}(g) \frac{\chi_{\fundamentalweight_{\word{i}_k}}\left(w_0(h_{30}^{-1}) h_{12}\right)}{\chi_{\fundamentalweight_{\word{i}_k}}(h_{02}) \genminoryz{w_k}{w_k}{\word{i}_k}(h_{03})}
    \end{align*}
    \begin{align*}
      \genminoryz{w_k}{}{\word{i}_k}(u_{123}) &= \genminoryz{w_k}{}{\word{i}_k}([g \lifttoG{w_0}]_{-}) \\
      &= \chi_{\fundamentalweight_{\word{i}_k}}\left(\left[ \dlifttoG{w_k^{-1}} g \lifttoG{w_0} [g \lifttoG{w_0}]_{+}^{-1} [g \lifttoG{w_0}]_{0}^{-1} \right]_{0}\right) \\
      &= \genminoryz{w_k}{w_0}{\word{i}_k}(g) \frac{1}{\genminoryz{}{w_0}{\word{i}_k}(g)} \\
      &= \genminoryz{w_k}{w_0}{\word{i}_k}(g) \frac{1}{\chi_{\fundamentalweight_{\word{i}_k}}([\lifttoG{w_0} [\lifttoG{w_0}^{-1} u_{123}]_{-}]_{0} w_0(h_{31}^{-1} h_{30}))} \\
      &= \genminoryz{w_k}{w_0}{\word{i}_k}(g) \frac{1}{\chi_{\fundamentalweight_{\word{i}_k}}([\lifttoG{w_0}^{-1} u_{123}]_{0}^{-1} w_0(h_{31}^{-1} h_{30}))} \\
      &= \genminoryz{w_k}{w_0}{\word{i}_k}(g) \frac{1}{\chi_{\fundamentalweight_{\word{i}_k}}(w_0(h_{12} h_{30}) h_{23})}
    \end{align*}
    \begin{align*}
      \genminoryz{w_0}{w_k}{\word{i}_k}(u_{130}) &= \genminoryz{w_0}{w_k}{\word{i}_k}(\Phi^{-1}(u_{123}) u_{130} h_{31}^{-1} h_{30}) \frac{1}{\genminoryz{w_k}{w_k}{\word{i}_k}(h_{31}^{-1} h_{30})} \\
      &= \genminoryz{w_0}{w_k}{\word{i}_k}(g) \frac{1}{\genminoryz{w_k}{w_k}{\word{i}_k}(h_{31}^{-1} h_{30})}
    \end{align*}

    Amalgamating $\alpha_{120}$ and $\alpha_{302}$ and labeling
    coordinates by minors of $g$ (up to edge coordinates) gives
    \cref{fig:flip-C3-120-302}. This includes the central edge because
    $[g]_{0} = h_{20} w_0(h_{12})$. This is not $\Qdv$, but the
    difference is only a matter of rotations and twistings.

    Note that the factors of
    $\chi_{\fundamentalweight_{\word{i}_k}}(h_{20})$ and
    $\chi_{\fundamentalweight_{\word{i}_k}}(h_{02})$ in the assignments
    for $\genminoryz{w_k}{}{\word{i}_k}(u_{120})$ and
    $\genminoryz{w_k}{}{\word{i}_k}(u_{302})$ are exactly cancelled out
    by the $\genminor{}{i}(h_2)$ factor of $\monomialmap$ from
    \cref{def:conf_3_star-to-seed-torus}. Therefore we are justified in
    ignoring edge coordinates for the remainder of the proof since we
    assume the others to be trivial.

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/flip-C3-120-302}

      \caption{Coordinates from $\alpha_{120}$ and $\alpha_{302}$.
        \label{fig:flip-C3-120-302}
      }
    \end{figure}

    After applying $\left( \murottwistR \right)$ the result is
    $\muP(\Qdv)$, with the coordinates of $\alpha_{120}$ and
    $\alpha_{230}$, as in \cref{fig:flip-C3-120-230}. In this figure,
    since each $\genminoryz{w_j}{w_k}{\word{i}_k}(g)$ is equivalent to
    some $\genminoryz{c^n}{c^m}{\word{i}_k}(g)$, we label vertices by
    the pair $(n,m)$. Further, taking into account that $c^{h} = w_0^2$
    which lifts to an element of $H$, we may consider $n$ and $m$ modulo
    $h$.

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/flip-C3-120-230}

      \caption{Coordinates from $\alpha_{120}$ and $\alpha_{230}$,
        labeled by $(n,m)$.
        \label{fig:flip-C3-120-230}
      }
    \end{figure}

    As with $\murot$, each mutation in $\muflipcore$ takes
    $\genminoryz{c^a}{c^b}{\word{i}_k}(g)$ to
    $\genminoryz{c^{a-1}}{c^{b-1}}{\word{i}_k}(g)$ by
    \cite[Theorem~1.17]{fominzelevinsky1999} and
    \cref{lem:thm-1.17-for-repeated-c}. That results in
    \cref{fig:flip-C3-120-230-post-flipcore}.

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/flip-C3-120-230-post-flipcore}

      \caption{Coordinates after applying $\muflipcore$, labeled by
        $(n,m)$.
        \label{fig:flip-C3-120-230-post-flipcore}
      }
    \end{figure}

    Converting $(n,m)$ back to $\genminoryz{c^n}{c^m}{\word{i}_k}(g)$,
    we obtain \cref{fig:flip-C3-123-013}. By the calculations above,
    these are coordinates of $u_{123}$ on the right and $u_{013}$ (as
    rotated $u_{130}$) on the left.

    \begin{figure}
      \centering \includestandalone[mode=image|tex]{fig/flip-C3-123-013}

      \caption{Coordinates after applying $\muflipcore$.
        \label{fig:flip-C3-123-013}
      }
    \end{figure}

    The final combination of $\muint{O3} \muint{O4} \muint{O5}$ serve to
    swap the left and right halves by \cref{lem:rowsigmaG-does-sigmaG}.
    This completes the proof.
  \end{proof}

  
\section{Proof of \cref{thm:fgcs-exists} for semisimple
    \texorpdfstring{$G$}{G}}

  \label{sec:products}

  We now expand from ``simple'' to ``semisimple''. Since the algorithm
  of \cref{sec:main-result} really only needed the information of $G$'s
  Dynkin diagram, and Dynkin diagrams behave very nicely with respect to
  products, the construction easily generalizes.

  \begin{lemma}
    \label{lem:fgcs-exists-for-products}
    Let $G$, a semisimple Lie group over $\mathbb{C}$, be $G = G_1
    \oplus G_2 \oplus \dotsb \oplus G_n$, with each $G_i$ a simple Lie
    group over $\mathbb{C}$ admitting quivers $Q_i$ with Fock--Goncharov
    coordinate structures $(\murot)_i$, $(\muflip)_i$, and
    $\conftoquiv_i$.

    Then for $G$, there is a quiver $Q$ which also carries a
    Fock--Goncharov coordinate structure.
  \end{lemma}
  \begin{proof}
    We must construct $Q$, $\murot$, $\muflip$, $\conftoquiv$, then show
    that all requirements of \cref{def:fgcs} are satisfied. This follows
    entirely from the fact that the Dynkin diagram of the direct product
    of groups is the disjoint union of Dynkin diagrams of the factors.

    For $Q$, take the disjoint union of each $Q_i$, with each
    $\facemap_{\Delta}(Q)$ being the disjoint union of all
    $\facemap_{\Delta}(Q_i)$. This is triangular since each component
    is.

    The mutations $\murot$ and $\muflip$ are concatenations of all
    $(\murot)_i$ and $(\muflip)_i$ respectively. The ordering of these
    components are irrelevant, because quiver mutations at disconnected
    vertices commute and $Q$ is exactly a disjoint union. Any
    concatenation will operate componentwise on the pieces of the
    disjoint union. This satisfies \cref{def:fgcs-1}.

    By the aforementioned fact of Dynkin diagrams, \cref{def:fgcs-2} is
    also satisfied.

    The map $\conftoquiv$ is defined as a product of each
    $\conftoquiv_i$ in the following manner. Let $\alpha_i$ and
    $\alpha_j$ be any two elements of the roots system for $G$
    associated to different factors. Then the nodes corresponding to
    those roots are disconnected in the Dynkin diagram for $G$, so the
    $A_{ij} = 0$ in the Cartan matrix.

    By e.g. \cite[Proposition~2.95]{knapp1996}, the bracket of any
    $\set{e_i, f_i, h_i}$ and $\set{e_j, f_j, h_j}$ vanishes, so any
    $\set{x_i, y_i, \torush_i}$ and $\set{x_j, y_j, \torush_j}$ commute.
    Letting $\alpha = (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+})$, by
    sufficient genericity we may factorize any $g_i$ as a product of
    $x_k, y_k, \torush_k$ elements, and may therefore rearrange these
    factors so that \[ g_i = (g_i)_1 (g_i)_2 \dotsb (g_i)_n, \qquad
      (g_i)_j \in G_j. \] Then the maps $\operatorname{rot}$ and
    $\Psi_{ij}$ trivially factor through the decomposition of $\alpha$
    into \[ \prod_{i = 1}^{n} \left[ \strut \alpha_i = ((g_0)_i, (g_1)_i
      N_{+}, (g_2)_i N_{+}, (g_3)_i N_{+}) \right]. \] That is, it is
    obvious that $\prod_i \operatorname{rot}(\alpha_i) =
    \operatorname{rot}(\prod_i \alpha_i)$. This, together with the
    construction of $Q$, shows that \cref{def:fgcs-M-is-birational-equivalence,def:fgcs-rot-works,def:fgcs-flip-works}
    are satisfied since they are satisfied for each $G_i$.
  \end{proof}
