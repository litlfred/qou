---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-007-22-the-invariant-trace-field
section_title: "The invariant trace field"
section_number: 2.2
pages: 3-4
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.949
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
\begin{definition}
  For a hyperbolic manifold $M = \mathbb{H}^3 / \Gamma$ defined by a
  discrete subgroup $\Gamma$ of $\PSL(2, \mathbb{C})$, the
  \definedterm{trace field} of $\Gamma$, denoted
  $\tracefield{\Gamma}$, is
  \[ \mathbb{Q}( \set{ \tr \gamma : \pi(\gamma) \in \Gamma } ) \]
  where $\pi: \SL(2, \mathbb{C}) \to \PSL(2, \mathbb{C})$ is the
  standard projection map.
\end{definition}

Since for any matrices $a, b \in \SL(2, \mathbb{C})$ we have
$\tr (aba^{-1}) = \tr(b)$, the trace field of $\Gamma$ is a
conjugation invariant of $\Gamma$. Unfortunately, it is not a
commensurability invariant, since it is possible to create finite
degree extensions of $\Gamma$ which extend the trace field: we refer
to \parencite[116]{maclachlanreid} for an explicit example. A slight
modification smooths over this difficulty.

\begin{definition}
  For a non-elementary subgroup $\Gamma \subset \PSL(2, \mathbb{C})$,
  the \definedterm{invariant trace field} of $\Gamma$ is the trace
  field $\invtracefield{\Gamma}$, where
  \[ \Gamma^{(2)} := \angset{ \gamma^2 \given \gamma \in \Gamma }. \]
\end{definition}
