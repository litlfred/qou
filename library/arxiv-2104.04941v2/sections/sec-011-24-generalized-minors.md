---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-011-24-generalized-minors
section_title: "Generalized minors"
section_number: 2.4
pages: 9-11
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 1.0
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:generalized-minors}

  We review generalized minors. These are the extension of flag minors
  on $\GL_n$ of \cite{fominzelevinsky1996},
  \cite{berensteinzelevinsky1997} to arbitrary semisimple algebraic
  groups. This generalization is described fully in
  \cite{fominzelevinsky1999}, to which we refer for more details.

  \begin{definition}
    \label{def:gaussian-decomposition}
    For $G$ a Lie group over $\mathbb{C}$ admiting $H$ and $N_{\pm}$,
    $G_0 = N_{-} H N_{+}$. For $x \in G_0$, the \defined{Gaussian
      decomposition} of $x$ into these components is $x = [x]_{-}
    [x]_{0} [x]_{+}$, with $[x]_{0} \in H$ and $[x]_{\pm} \in N_{\pm}$.
    This decomposition is necessarily unique.
  \end{definition}

  \begin{definition}
    For $G$ a Lie group over $\mathbb{C}$ admiting $H$ as above, we may
    identify the Weyl group $W$ with $N_G(H)/H$, the quotient of the
    normalizer of $H$ in $G$ by $H$. We denote \[ \lifttoG{s_i} =
      x_i(-1) y_i(1) x_i(-1) \qquad \dlifttoG{s_i} = x_i(1) y_i(-1)
      x_i(1). \] These satisfy the braid relations, and whenever
    $\length{u v} = \length{u} + \length{v}$, we have \[ \lifttoG{u v} =
      \lifttoG{u} \cdot \lifttoG{v}, \qquad \dlifttoG{u v} =
      \dlifttoG{u} \cdot \dlifttoG{v}. \]

  \end{definition}

  \begin{remark}
    \label{rem:w0-switches-Ns}
    If $G$ is semisimple, then the standard choice of bases $\set{e_i}$,
    $\set{h_i}$, and $\set{f_i}$ for $\mathfrak{n}_{-}$, $\mathfrak{h}$,
    and $\mathfrak{n}_{+}$ give rise, via $\exp$, to one-parameter
    subgroups in $N_{-}$, $H$, $N_{+}$ respectively, and the
    identification of $W$ with $N_G(H)/H$ identifies $w_0$ with
    $\lifttoG{w_0}$. Acting by conjugation on $G$, this element switches
    each pair of subgroups $\exp(\mathbb{R}e_i)$, $\exp(\mathbb{R}f_i)$.
    Thus $\lifttoG{w_0}$ switches $N_{-}$ and $N_{+}$.
  \end{remark}

  \begin{remark}
    \label{rem:sG}
    The element $\lifttoG{w_0}^2$ arises frequently. It shall be denoted
    $s_G$, and is in the center of $G$, having order either $1$ or $2$.
  \end{remark}

  \begin{definition}
    \label{def:pre-generalized-minor}
    For $G$ a Lie group over $\mathbb{C}$, and any fundamental weight
    $\fundamentalweight_i$, define \[ \pregenminor{\fundamentalweight_i}
      : H \mapsto \mathbb{C} \qquad \text{by} \qquad
      \pregenminor{\fundamentalweight_i} : h \mapsto
      \exp(\fundamentalweight_i\exp^{-1}(h))). \]
  \end{definition}

  \begin{definition}
    \label{def:generalized-minor}
    For $G$ a Lie group over $\mathbb{C}$, admitting decomposition as
    above, $v, w$ elements of the Weyl group $W$, and
    $\fundamentalweight_i$ a fundamental weight, the
    \defined{generalized minor} for the words and fundamental weight $v
    \fundamentalweight_i, w \fundamentalweight_i$ is the regular
    function $\genminoryz{v}{w}{i} : G \mapsto \mathbb{C}$, defined by
    its restriction on $\dlifttoG{v} G_0 \lifttoG{w^{-1}}$ by \[
      \genminoryz{v}{w}{i} : g \mapsto
      \pregenminor{\fundamentalweight_i} \left( \left[\dlifttoG{v^{-1}}g
      \lifttoG{w}\right]_{0} \right). \]

    In the case $w$ is trivial, as it often is in our construction, we
    denote \[ \genminor{v}{i}(g) = \genminoryz{v}{}{i}(g). \]
  \end{definition}

  \begin{example}
    If $G = \SL(n,\mathbb{C})$ (of type $A_{n-1}$), we may take $H$ as
    diagonal matrices, with $N_{+}$ and $N_{-}$ as strictly upper and
    lower triangular matrices.

    The fundamental weights are $\fundamentalweight_i = (e_1 + e_2 +
    \dotsb + e_i)^{\ast}$, and the function
    $\pregenminor{\fundamentalweight_i}$ corresponds to taking the
    product $h_{11} h_{22} \dotsb h_{ii}$: the $i \times i$ minor of the
    first $i$ rows and columns. The reflections $s_{\alpha_i}$ lift to
    \[ \dlifttoG{s_i} = \Id_{i-1} \boxplus \begin{bmatrix} & 1 \\ -1 &
      \end{bmatrix} \boxplus \Id_{n-i-1} \qquad \lifttoG{s_i} =
      \Id_{i-1} \boxplus \begin{bmatrix} & -1 \\ 1 & \end{bmatrix}
      \boxplus \Id_{n-i-1}. \] (Here $\boxplus$ is diagonal matrix
    concatenation.) Thus $\dlifttoG{s_i}$ acts on $\SL(n, \mathbb{C})$
    on the left by permuting rows, $\lifttoG{s_i}$ acts on the right by
    permuting columns, and the generalized minor for $v
    \fundamentalweight_i,w\fundamentalweight_i$ on $\SL(n, \mathbb{C})$
    is exactly the $i \times i$ minor of the top left rows and columns
    after permutation.
  \end{example}

  \begin{definition}
    \label{def:gamma-k}
    For a fixed presentation $\word{i} = (i_1, i_2, \dotsc, i_m)$ of
    $w_0$, define \[ w_k = s_{i_m} \dotsb s_{i_{k+1}} s_{i_k}, \] and
    define the \defined{$\word{i}$-chamber weights} \[ \gamma_k = w_k
      \fundamentalweight_{i_k}. \] We also count
    $\fundamentalweight_{i_k}$ as $\word{i}$-chamber weights.
  \end{definition}

  \begin{remark}
    The $w_k$ are pairwise distinct and fill the involution set of
    $w_0$, see \cite[Chapter VI, \textsection 1.6]{bourbaki2002_46}.
  \end{remark}

  \begin{remark}
    \label{rem:all-wkomegaj-are-gamma-k-or-trivial}
    Any $\genminor{w_k}{j}$ is some $\genminorgk{k}$ or
    $\genminor{}{j}$. This follows from the fact that
    $\pregenminor{i}([\dlifttoG{s_{j \ne i}} g]_{0}) =
    \pregenminor{i}([g]_{0})$, so for use with generalized minors, any
    $w_k \fundamentalweight_{j}$ may be reduced to $w_{k+1}
    \fundamentalweight_{j}$ whenever $w_k$ is not trivial and $i_k \ne
    j$.
  \end{remark}

  \begin{definition}
    \label{def:non-negative-generalized-minor}
    When restricted to $H$, we may express $\genminor{v}{i}$ in another
    fashion. For $G$ of rank $r$, let $P$ denote the \defined{weight
      lattice}, integral combinations of $\set{\fundamentalweight_i}$.
    For $\beta \in P \cong \mathbb{Z}^r$, and for $A = \prod_{k=1}^{r}
    \torush_k(t_k) \in H$, \cref{def:pre-generalized-minor} is
    equivalent to \[ \pregenminor{\beta}(A) = \exp( \ip{\beta, t} ), \]
    where $\ip{\cdot, \cdot}$ is the normal Euclidean inner product.

    Now for $v \in W$, we may consider $v$ acting on $P \subset
    \mathfrak{h}_0$ by $v \beta = (v \beta^{\ast})^{\ast}$, using the
    action of $W$ on $\mathfrak{h}_{0}^{\ast}$. This allows expanding
    the above definition to \[ \Delta_{v \beta, v \beta}(A) = \exp(\ip{v
        \beta, t}). \]

    Now, define the \defined{non-negative generalized minor},
    $\genminornumerator{v}{\beta} : H \to \mathbb{C}$ as \[
      \genminornumerator{v}{\beta}(A) = \exp(\ip{ \max(v \beta, (0, 0,
        \dotsc, 0)), t}), \] where $\max$ operates componentwise.
  \end{definition}

  The $\oplus$ is intended to suggest tropical addition.

  \begin{remark}
    \label{rem:numerator-calculation}
    For $A \cong (t_1, t_2, \dotsc, t_r)$, the map
    $\genminornumerator{v}{\fundamentalweight_i}(A)$ can be computed by
    computing $\genminoryz{v}{v}{i}((s_1, s_2, \dotsc, s_r))$
    abstractly, taking the numerator of the result, then substituting
    $t_i$ for $s_i$.
  \end{remark}
