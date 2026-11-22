---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-018-41-configurations-and-gluings
section_title: "Configurations and gluings"
section_number: 4.1
pages: 16-17
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.993
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:configurations-and-gluings}

  \begin{definition}
    \label{def:Conf_k_star}
    Let $G$ be a Lie group over $\mathbb{C}$, with sufficient choices to
    define $G_0$ as in \cref{def:gaussian-decomposition}. Let $K$ be a
    subgroup of $G$ (we will ultimately use $N_{+}$). A tuple of cosets
    $(g_0K, g_1K, \dotsc, g_{m}K)$ is \defined{sufficiently generic} if
    each $g_i^{-1} g_j \in \lifttoG{w_0}G_0$.

    Such a tuple corresponds to a labeling of edges in an oriented
    $m$-simplex by elements of $\lifttoG{w_0}G_0$, as in
    \cref{fig:labeled-sufficiently-generic-simplex}, with the edge from
    $i$ to $j$ (assuming $j>i$) labeled by $g_i^{-1} g_j$.

    The variety of such sufficiently generic $(m+1)$-tuples is the
    \defined{configuration space} $\Conf_{m+1}(G/K)$. Identifying
    elements which differ by left-multiplication of $G$ yields the
    variety $\Conf_{m+1}^{\ast}(G/K)$.
  \end{definition}

  \begin{figure}[h]
    \centering \includestandalone[mode=image|tex]{fig/labeled-sufficiently-generic-simplex}

    \caption{Oriented $2$- and $3$-simplices labeled by elements of
      $\Conf_3^{\ast}(G/K)$ and $\Conf_4^{\ast}(G/K)$.
      \label{fig:labeled-sufficiently-generic-simplex}
    }
  \end{figure}

  \begin{definition}
    \label{def:peripheral-stuff}
    Let $M$ be a compact manifold (possibly with boundary) and $G$ a Lie
    group over $\mathbb{C}$, with $K$ a subgroup of $G$. A subgroup $L$
    of $\pi_1(M)$ is \defined{peripheral} if there is a boundary
    component $D$ of $M$ such that $L$ is induced by the inclusion of
    $D$; that is $\iota^{\ast}(\pi_1(D)) = L$.

    A representation $\rho : \pi_1(M) \to G$ is a
    \defined{$(G,K)$-representation} if, for every peripheral subgroup
    $L$, the image $\rho(L)$ is a conjugate of $K$. In the case $K =
    N_{+}$, the term \defined{boundary-unipotent} is used. If $K =
    B_{+}$, then $\rho$ is \defined{boundary-borel}.
  \end{definition}

  \begin{lemma}[{\cite[Lemma~5.8, Proposition~5.9]{zickert2016}}]
    \label{lem:canonical-form-for-conf_3_star}
    There is an isomorphism of varieties \[ \Conf_3^{\ast}(G/N_{+})
      \cong H^3 \times_{H} (N_{-} \cap \lifttoG{w_0} G_0). \] The fiber
    product $\times_{H}$ means that for $(h_1, h_2, h_3, u) \in
    \Conf_3^{\ast}(G/N_{+}))$, we have \[ [\lifttoG{w_0}^{-1} u]_{0} =
      (w_0(h_3 h_1) h_2)^{-1}. \]
  \end{lemma}

  Thus we will often write $(h_1, h_2, h_3, u)$ for $\alpha$, which has
  one representative $(N_{+}, \lifttoG{w_0} h_1 N_{+}, u w_0(h_1) h_2
  s_G N_{+})$. We refer to these as \defined{canonical forms} for
  $\Conf_3^{\ast}(G/N_{+})$.

  \begin{definition}
    \label{rem:canonical-form-for-B-cosets}
    By expanding $N_{+}$ to $B_{+}$ above, we obtain that $\alpha \in
    \Conf_3^{\ast}(G/B_{+})$ can be given as $(B_{+}, \lifttoG{w_0}
    B_{+}, u B_{+})$. Choose the unique $u_x$ such that, for all $k$,
    the minor $\genminoryz{w_k}{}{1}(u_x) = 1$. This element $u_x$ is
    the \defined{canonical form} for $\alpha$.

    For an arbitrary $(B_{+}, \lifttoG{w_0} B_{+}, u B_{+})$, by
    expanding \cref{def:generalized-minor} there is a unique (up to the
    center of $G$) element $h$ such that $h u h^{-1}$ is the canonical
    form $u_x$. When $G$ is centerless, we denote this element by
    $n(u)$.
  \end{definition}

  \begin{proposition}
    \label{prop:Phi-Psi-and-rot}
    This summarizes \cite[Proposition~5.10]{zickert2016}. Let $\alpha
    \in \Conf_3^{\ast}(G/N_{+})$ be given by $\alpha = (h_1, h_2, h_3,
    u)$. Recall $\Phi$ and $\Psi$ of \cref{def:phi-and-psi}. The map \[
      \operatorname{rot}: \Conf_3^{\ast}(G/N_{+}) \to
      \Conf_3^{\ast}(G/N_{+}), \qquad (g_0 N_{+}, g_1 N_{+}, g_2 N_{+})
      \mapsto (g_2 N_{+}, g_0 N_{+}, g_1 N_{+}) \] is given, in this
    form, via \[ \operatorname{rot} : (h_1, h_2, h_3, u) \mapsto (h_3,
      h_1, h_2, h_2^{-1} (w_0(h_1))^{-1} (\Phi \Psi \Phi \Psi)(u)
      (w_0(h_1)) h_2). \]
  \end{proposition}

  \begin{definition}
    \label{def:gluing-configurations}
    This summarizes \cite[Section~2.2.1]{zickert2016}. We define and
    $\Conf_3^{\ast}(G/N_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/N_{+})$
    by gluing copies of $\Conf_3^{\ast}(G/N_{+})$ along matching copies
    of $\Conf_2^{\ast}(G/N_{+})$. Specifically,
    \begin{align*}
      \Conf_3^{\ast}(G/N_{+}) \times_{02}^{s_G} \Conf_3^{\ast}(G/N_{+}) = \Set{ \substack{(g_0 s_G N_{+}, g_1 N_{+}, g_2 N_{+}),\\ (g_0 N_{+}, g_2 N_{+}, g_3 N_{+})} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) \in \Conf_4^{\ast}(G/N_{+}) } \\
      \Conf_3^{\ast}(G/N_{+}) \times_{13}^{s_G} \Conf_3^{\ast}(G/N_{+}) = \Set{ \substack{(g_1 N_{+}, g_2 N_{+}, g_3 N_{+}),\\ (g_0 N_{+}, g_1 s_G N_{+}, g_3 N_{+})} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) \in \Conf_4^{\ast}(G/N_{+}) } \\
    \end{align*}
    We also define the following maps from $\Conf_4^{\ast}(G/N_{+})$ to
    $\Conf_{3}^{\ast}(G/N_{+}) \times_{jk}^{s_G}
    \Conf_3^{\ast}(G/N_{+})$ for $jk = 02, 13$:
    \begin{align*}
      \Psi_{02} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) &\mapsto \substack{(g_0 s_G N_{+}, g_1 N_{+}, g_2 N_{+}),\\ (g_0 N_{+}, g_2 N_{+}, g_3 N_{+})} \\
      \Psi_{13} : (g_0 N_{+}, g_1 N_{+}, g_2 N_{+}, g_3 N_{+}) &\mapsto \substack{(g_1 N_{+}, g_2 N_{+}, g_3 N_{+}),\\ (g_0 N_{+}, g_1 s_G N_{+}, g_3 N_{+})}
    \end{align*}

    See part of \cref{fig:QC2-and-flip} for a graphical depiction.

    In the surface case, these correspond to the two different ways of
    triangulating a quadrilateral. The act of retriangulating a single
    quadrilateral this way is called a ``flip''. In the $3$-manifold
    case, these correspond to decomposing a tetrahedron's vertices into
    the two triangles' worth.
  \end{definition}

  \begin{remark}
    \label{rem:purpose-of-sG}
    The element $s_G$ is in the center of $G$, so is only relevant for
    $N_{+}$-cosets. Its purpose is to allow the quiver amalgamation (see
    \cref{def:dv-dh-construction} ahead) to agree with the
    identification of elements of $\Conf_3^{\ast}(G/N_{+})$ along a copy
    of $\Conf_2^{\ast}(G/N_{+})$.

    To see this, note that \cref{fig:dv-construction} shows identifying
    a $0$--$2$ edge with a $0$--$1$ edge, and \cref{fig:dh-construction}
    identifes a $0$--$2$ edge with a $1$--$2$ edge. Since the associated
    elements of $\Conf_2^{\ast}(G/N_{+})$ are oriented via the cyclic
    ordering on $(0,1,2)$, this quiver amalgamation corresponds to
    identifying elements of $\Conf_2^{\ast}(G/N_{+})$ ``backwards''.

    This use of $s_G$ is why $\mathcal{A}_{G,\Sigma}$ is the moduli
    space of \emph{twisted}, decorated representations from
    $\pi_1(\Sigma)$ into $G$. See \cite[Section~8.6]{fockgoncharov2006}
    and \cite[Section~2.3]{zickert2016} for more details.
  \end{remark}
