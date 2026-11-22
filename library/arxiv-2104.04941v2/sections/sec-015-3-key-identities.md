---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-015-3-key-identities
section_title: "Key identities"
section_number: 3
pages: 13-14
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.994
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
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
