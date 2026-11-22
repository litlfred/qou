---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-009-22-unipotent-subgroups
section_title: "Unipotent subgroups"
section_number: 2.2
pages: 9-9
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\begin{definition}
    \label{def:root-space-decomposition}
    For a Lie group $G$ (the Lie algebra of which is $\mathfrak{g}$), a
    Cartan subalgebra $\mathfrak{h}$ and a root system $\roots$ with a
    choice of positive roots $\posroots$, there is a \defined{root space
      decomposition} defining $\mathfrak{n}_{\pm}$ by \[ \mathfrak{g} =
      \overbrace{\bigoplus_{\alpha \in \posroots}
        \mathfrak{g}_{-\alpha}}^{\mathfrak{n}_{-}} {}\oplus{}
      \mathfrak{h} \oplus \overbrace{\bigoplus_{\alpha \in \posroots}
        \mathfrak{g}_{\alpha}}^{\mathfrak{n}_{+}}. \]

    The Lie subgroups of $G$ with these Lie algebras are, respectively,
    $N_{-}$, $H$, and $N_{+}$. The $N_{\pm}$ subgroups are
    \defined{maximal unipotent} subgroups of $G$. $H$ is a
    \defined{maximal torus}. We also have the \defined{borel subgroups}
    $B_{\pm} = H N_{\pm}$.

    We also fix standard generators $e_i \in \mathfrak{g}_{\alpha_i}$,
    $f_i \in \mathfrak{g}_{- \alpha_i}$, and $h_i \in \mathfrak{h}$
    (with $i \in \set{1, 2, \dotsc, \rank G}$, so that we may write \[
      x_i(t) = \exp(t e_i) \in N_{+}, \qquad y_i(t) = \exp(t f_i) \in
      N_{-}, \qquad \torush_{i}(t) = \exp(t h_i) \in H. \]
  \end{definition}
