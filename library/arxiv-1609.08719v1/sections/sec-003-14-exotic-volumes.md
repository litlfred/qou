---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-003-14-exotic-volumes
section_title: "Exotic volumes"
section_number: 1.4
pages: 2-3
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.923
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
Recall that for a closed hyperbolic 3-manifold and a representation
$\rho : \pi_1(M) \to \SL(n, \mathbb{C})$, Cheeger-Chern-Simons
invariant $\cheegerchernsimons(\rho)$ is given by
\begin{equation}
  \label{eq:cheeger-chern-simons}
  \cheegerchernsimons(\rho) = \frac{1}{2} \int_{M} s^{\ast} \left( \tr \left( A \wedge \dx{A} + \frac{2}{3} A \wedge A \wedge A \right) \right) \in \mathbb{C} / 4\pi^2\mathbb{Z},
\end{equation}
with $E_{\rho}$ the flat $\SL(n, \mathbb{C})$-bundle with holonomy
$\rho$, with $A$ the flat connection in $E_{\rho}$, and with $s$ a
section of $E_{\rho}$.

\begin{definition}
  For a representation $\rho: \pi_1(M) \to \SL(n, \mathbb{C})$, the
  \definedterm{complex volume} $\complexvol(\rho)$ of $\rho$ is
  \[ \complexvol(\rho) = i \cheegerchernsimons(\rho). \] If $\rho$ is
  $\rho_{\text{geo}}$, the geometric representation of a hyperbolic
  $3$-manifold $M$, then
  \[ \complexvol(\rho_{\text{geo}}) = \vol(M) + i \chernsimons(M), \]
  for $\chernsimons(M)$ the Chern-Simons invariant of $M$.

  When $\rho$ is not $\rho_{\text{geo}}$, we call the real part of
  $\complexvol(\rho)$ an \definedterm{exotic volume} of $M$, to
  distinguish it from the geometric volume.
\end{definition}

By means of the Ptolemy coordinates of \parencite{garoufalidis2015},
we were able to compute certain exotic volumes of manifolds to at
least 50 decimal places of precision, and to express them as linear
combinations of geometric volumes of manifolds associated to the same
invariant trace field.
