---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-006-21-cross-ratios
section_title: "Cross-ratios"
section_number: 2.1
pages: 3-3
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.889
latex_coverage_ratio: 1.0
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
It is a feature of hyperbolic geometry that the volume of a complete
3-manifold (if finite) is actually a topological invariant (see e.g.\
\parencite[83]{benedetti1992lectures} for a proof). For an ideal
hyperbolic 3-simplex $\Delta = (a,b,c,d)$ defined by four points in
$\partial \mathbb{H}^3 \cong \mathbb{C} \cup \set{\infty}$,
$\vol(\Delta)$ can be determined knowing just the cross-ratio
$\crossratio{a}{b}{c}{d} = \frac{(c-a)(d-b)}{(d-a)(c-b)}$.  Since
$\Isom^{+}(\mathbb{H}^3) \cong \PSL(2, \mathbb{C})$ is 3-transitive,
for the purposes of volume calculation we may assume $\Delta$ to be of
the form $(\infty,0,1,z)$, which conveniently has cross-ratio $z$. The
volume of $\Delta$ is given by
\begin{equation}
  \label{eq:D}
  D(\Delta) = \im \left( \int_0^1 \frac{\log (1 - tz)}{t} \dx{t} \right) + \arg(1 - z) \log |z|.
\end{equation}

Given a triangulation of a hyperbolic 3-manifold, one may compute
cross-ratios using gluing equations \ref{eq:cusp} and
\ref{eq:edge}. Using cross-ratios, one may compute volumes for each
simplex in the triangulation; we refer to
section~\ref{subsec:gluing-equations} for more details. Summing those
volumes gives the volume of the manifold: for $\set{\Delta_i}$ the
simplices in a triangulation of $M$,
\begin{equation}
  \label{eq:sum-of-simplex-vols}
  \vol(M) = \sum_i D(\Delta_i).
\end{equation}

In our work, we used experimental data to examine relations between
the volumes of hyperbolic 3-manifolds which share the same invariant
trace field.  We begin by briefly reviewing the basics of the algebraic
invariants of hyperbolic 3-manifolds relevant to our study.
