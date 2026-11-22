---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-012-25-factorization-coordinates
section_title: "Factorization coordinates"
section_number: 2.5
pages: 11-11
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.792
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:factorization-coordinates}

  We also review factorization coordinates, referring again to
  \cite{fominzelevinsky1999} for details. In brief, they will give
  coordinates on $\Conf_3^{\ast}(G/N_{+})$ (of \cref{def:Conf_k_star})
  which are governed by a word $\word{i}$ in the Weyl group of $G$.

  \begin{definition}
    \label{def:factorization-coords-xi}
    For $G$ a Lie group of rank $r$ over $\mathbb{C}$ admitting $H$,
    $N_{\pm}$, $x_i$, and $y_i$, with Weyl group $W$, $\word{i} = (i_1,
    \dotsc, i_k)$ a reduced word in $W$, and $t \in
    (\mathbb{C}^{\ast})^k$, we define \[ x_{\word{i}}(t) = x_{i_1}(t_1)
      \dotsb x_{i_k}(t_k) \in N_{+}, \qquad y_{\word{i}}(t) =
      y_{i_1}(t_1) \dotsb y_{i_k}(t_k) \in N_{-}. \]

    Let $\word{i} = (i_1, i_2, \dotsc, i_m)$ be a fixed representation
    for $w_0$. Then
    \begin{align*}
      x_{\word{i}}(\set{t_k}_{k=1}^{m}) &= x_{i_1}(t_1) x_{i_2}(t_2) \dotsb x_{i_m}(t_m) \in N_{+} \cap G_0 \lifttoG{w_0} \\
      y_{\word{i}}(\set{t_k}_{k=1}^{m}) &= y_{i_m}(t_m) \dotsb y_{i_2}(t_2) y_{i_1}(t_1) \in N_{-} \cap \lifttoG{w_0} G_0.
    \end{align*}
  \end{definition}

  By \cite[Theorem~1.3]{fominzelevinsky1999} these are isomorphisms.

  \begin{definition}
    For $u \in N_{-} \cap \lifttoG{w_0} G_0$, the \defined{factorization
      coordinates} of $u$ are $(t_1, \dotsc, t_m) \in \mathbb{C}^m$ such
    that $u = x_{\word{i}}(t_1, \dotsc, t_m)$.
  \end{definition}

  We also recall two utility functions from \cite{fominzelevinsky1999}
  and \cite{fockgoncharov2006}.

  \begin{definition}
    \label{def:phi-and-psi}
    The biregular anti-automorphism $\Psi : G \to G$ and the biregular
    automorphism $\Phi : N_{+} \cap G_0 \lifttoG{w_0} \to N_{-} \cap
    \lifttoG{w_0} G_0$ are the unique maps such that, for $t \in
    \mathbb{C}$, $h \in H$, $x \in N_{+}$, and $y \in N_{-}$,
    \begin{align*}
      \Psi(x_i(t)) &= y_i(t) & \Psi(y_i(t)) &= x_i(t) & \Psi(h) &= h
    \end{align*}
    and
    \begin{align*}
      \Phi(x) &= [x \lifttoG{w_0}]_{-}, & \Phi^{-1}(y) &= \lifttoG{w_0} [\lifttoG{w_0}^{-1} y]_{-} \lifttoG{w_0}^{-1}.
    \end{align*}
  \end{definition}

  \label{sec:quivers-and-cluster-ensembles}
