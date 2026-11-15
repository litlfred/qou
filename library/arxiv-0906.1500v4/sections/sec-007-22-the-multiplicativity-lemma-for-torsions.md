---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-007-22-the-multiplicativity-lemma-for-torsions
section_title: "The Multiplicativity Lemma for torsions"
section_number: 2.2
pages: 5-5
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{subsection:multiplicativitylemma}

In this section, we briefly review the Multiplicativity Lemma for
Reidemeister torsions (with sign). 

First, we review the notion of \emph{compatible bases}. Let $0 \to E'
\xrightarrow{i} E \xrightarrow{j} E'' \to 0$ be a short exact sequence
of finite dimensional vector spaces and let $s$ denotes a section of
$j$. Thus, $i \oplus s : E' \oplus E'' \to E$ is an isomorphism. We
equip the three vector spaces $E'$, $E$ and $E''$ respectively with
the following three bases : $\mathbf{b}' = \left( b'_1, \ldots,
  b'_p\right)$, $\mathbf{b} = \left(b_1, \ldots, b_n\right)$, and
$\mathbf{b}'' = \left(b''_1, \ldots, b''_q\right)$. With such
notation, one has $n = p+q$, and we say that the bases $\mathbf{b}'$,
$\mathbf{b}$ and $\mathbf{b}''$ are compatible if the isomorphism $i
\oplus s : E' \oplus E'' \to E$ has determinant $1$ in the bases
$\mathbf{b}' \cup \mathbf{b}'' = \left( b'_1, \ldots, b'_p, b''_1,
  \ldots, b''_q\right)$ of $E' \oplus E''$ and $\mathbf{b}$ of $E$. If
it is the case, we write $\mathbf{b} \sim \mathbf{b}' \cup
\mathbf{b}''$.

Let us now review the multiplicativity property of the Reidemeister torsion (with sign).

\begin{MultLemma}[Lemma 3.4.2 in~\cite{Turaev86:torsion_in_knot_theory}]
  \label{lemma:Multiplicativite}
  Let
  \begin{equation}\label{eqn:short_exact_seq_complexes}
      0 \to C'_* \to C_* \to C_*'' \to 0
  \end{equation}
  be an exact sequence of chain complexes. Assume that $C'_*$, $C_*$
  and $C''_*$ are based and homology based. For all $i$, let
  $\cbasis[c']{i}$, $\cbasis[c]{i}$ and $\cbasis[c'']{i}$ denote the
  reference bases of $C_i'$, $C_i$ and $C_i''$ respectively.
  Associated to~(\ref{eqn:short_exact_seq_complexes}) is the long
  sequence in homology
  \[
    \cdots \to 
    H_i(C'_*) \to 
    H_i(C_*)  \to 
    H_i(C''_*) \to 
    H_{i-1}(C'_*) \to 
    \cdots 
  \]
  Let $\mathcal{H}_*$ denote this acyclic chain complex and base
  $\mathcal{H}_{3i+2} = H_i(C'_*)$, $\mathcal{H}_{3i+1} = H_i(C_*)$
  and $\mathcal{H}_{3i} = H_i(C''_*)$ with the reference bases of
  $H_i(C'_*)$, $H_i(C_*)$ and $H_i(C''_*)$ respectively.  If for all
  $i$, the bases $\cbasis[c']{i}$, $\cbasis{i}$ and $\cbasis[c'']{i}$
  are compatible, 
  \ie~$\cbasis{i} \sim \cbasis[c']{i} \cup \cbasis[c'']{i}$, then
  \begin{align*}
    \lefteqn{\Tor{C_*}{\cbasis{*}}{\hbasis{*}}} &\\
    &= (-1)^{\alpha(C'_*, C''_*) + \varepsilon(C'_*, C_*, C''_*)} \;
    \Tor{C'_*}{\cbasis[c']{*}}{\hbasis[h']{*}}
    \Tor{C''_*}{\cbasis[c'']{*}}{\hbasis[h'']{*}}
    \Tor{\mathcal{H}_*}{\{\hbasis[h']{*}, \hbasis{*},\hbasis[h'']{*}\}}{\emptyset}
  \end{align*}
  where 
  \begin{align*}
    \alpha(C'_*, C''_*) &= 
    \sum_{i \mygeq 0} \alpha_{i-1}(C'_*) \alpha_i(C''_*) \in \ZZ/2\ZZ 
  \quad \hbox{and}\\
    \varepsilon(C'_*, C_*, C''_*) &= 
    \sum_{i \mygeq 0}
    \{(\beta_i(C_*)+1)(\beta_i(C_*') + \beta_i(C_*'')) + 
      \beta_{i-1}(C_*')\beta_i(C_*'')\}
    \in \ZZ/2\ZZ.
  \end{align*}
\end{MultLemma}
The proof is a careful computation based on linear algebra,
see~\cite[Lemma 3.4.2]{Turaev86:torsion_in_knot_theory}
and~\cite[Theorem 3.2]{Milnor:1966}.  This lemma appears to be a very
powerful tool for computing Reidemeister torsions. It will be used all
over this paper.
