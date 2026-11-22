---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-006-15-historical-context
section_title: "Historical context"
section_number: 1.5
pages: 7-8
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.994
doc_brief: "Fock–Goncharov Coordinates for Semisimple Lie Groups — Fock and Goncharov [FG06b] introduced cluster ensembles, providing a framework for coordi- nates on varieties of surface representations into"
---
\label{sec:historical-context}

  Fock and Goncharov introduced cluster ensembles in
  \cite{fockgoncharov2006} and \cite{fockgoncharov2003}, employing the
  cluster algebra work of Fomin--Zelevinsky \cite{fominzelevinsky2002},
  \cite{fominzelevinsky2003}, \cite{fominzelevinsky2005} as well as
  Lusztig's study of positivity \cite{lusztig1994}, \cite{lusztig1997}.
  The application was laid out for a split semisimple simply-connected
  Lie group over $\mathbb{R}$, but explicit constructions were only
  known for type $A_n$. Since then, there has been ongoing work.

  \begin{itemize}
  \item
    In \cite{zickert2016}, Zickert produced examples of cluster
    ensembles and mutations for types $A_2$, $B_2$, $C_2$, and $G_2$,
    directly employing Lusztig's positive maps to explicitly construct
    varieties. Our work addresses Conjecture~2.7, which predicts the
    existence of quivers, rotation and flip mutations, and coordinate
    maps for semisimple $G$.

    This work also expanded the use of Fock--Goncharov coordinates to
    representations of ideally-triangulated hyperbolic $3$-manifolds,
    building on \cite{gtz2015}.
  \item
    With \cite{le2016} and \cite{le2016_2}, Le described constructions
    for quivers of types $A_n$, $B_n$, $C_n$, and $D_n$ using tensor
    invariants and webs. Our work addresses Conjecture~3.12 (that the
    cluster algebra for $\Conf_m^{\ast}(G/N_{+})$ is invariant under
    retriangulation and reordering) for the orientation-preserving case,
    for our choice of presentation of $w_0$.
  \item
    Using representations of quivers, Fei constructed quivers and
    mutations for many types in \cite{fei2016}, though associated to a
    slightly different flag variety.
  \item
    In \cite{ip2016}, Ip produced similar ``basic quivers'', though not
    presenting mutation sequences in the general case.
  \item
    Goncharov--Shen continued work on invariants of cluster ensembles
    with \cite{goncharovshen2018}, providing existence proofs.
  \end{itemize}

  There were several obstacles to extending these results to our proof
  of \cref{thm:intro-main-result}. First, the cluster ensembles for type
  $A_n$ have trivial triangular symmetry. However, direct dimension
  counting of the coordinate ring shows that this is not possible for
  general $G$.

  Second, the algorithm of \cite[Section~2]{fominzelevinsky2005} to
  produce a quiver carrying the coordinate structure of $B_{-}$ (which
  is a significant step) is well-known. However, this algorithm depends
  on a particular choice of presentation for $w_0$ in the Weyl group of
  $G$. It is not immediately obvious how to choose $w_0$ for each group,
  or if this choice should matter.

  Third, the same non-triviality of triangular symmetry for $Q$ extends
  to non-triviality of the coordinate assignment map $\conftoquiv$. In
  other words, fully three sides of each square in
  \cref{fig:retriangulation-and-reordering} are trivial in the $A_n$
  case, and therefore give few clues as to the general case.

  Finally, the action of $w_0$ on a simple root $\alpha_i$ is not
  necessarily $w_0(\alpha_i) = -\alpha_i$. This creates various
  complications.

  The following observations are the key to our result.

  \begin{itemize}
  \item
    $A_n$ is the exception, not the base case. Specifically, for all $G$
    except type $A_{2n}$, there exists a very regular presentation of
    $w_0$ in terms of Coxeter elements.
  \item
    This regularity causes the quiver with the coordinate ring of
    $B_{-}$ to be be laid out so that
    \cite[Theorem~1.17]{fominzelevinsky1999} and
    \cite[Theorem~1.5]{yangzelevinsky2008} apply, and these identities
    hint at certain sequences of mutations.
  \end{itemize}
