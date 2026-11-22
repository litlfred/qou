---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-010-25-ptolemy-coordinates
section_title: "Ptolemy coordinates"
section_number: 2.5
pages: 7-8
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.979
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
The Ptolemy coordinates of Garoufalidis-Thurston-Zickert offer an
alternative representation of the information encoded in the gluing
and cusp equations.  For our purposes, their principal use is encoding
information about arbitrary representations
$\rho : \pi_1(M) \to \PSL(n, \mathbb{C})$.  We refer the reader
to \parencite{garoufalidis2015}, \parencite{1401.5542}, and present a
brief overview here, specialized for the particular case of hyperbolic
$3$-manifolds.

\begin{definition}
  For a fixed triangulation of a manifold $M$ (with vertices labeled
  $0$, $1$, $2$, $3$), a \definedterm{Ptolemy assignment} is an
  association of variables in $\mathbb{C}^{\times}$ to each edge of
  each simplex satisfying equations~\ref{eq:ptolemy_relations}
  below. We denote the variable of the $i$th simplex on the edge
  between vertices $j$ and $k$ as $c^i_{jk}$.

  If two edges are identified, their associated variables are the
  same.  This immediately implies, for example, that
  $c^i_{jk} = -c^i_{kj}$.

  The \definedterm{Ptolemy relations} are
  \begin{equation}
    \label{eq:ptolemy_relations}
    c_{03}^{i}c_{12}^{i} + c^i_{01}c^i_{23} = c^i_{02}c^i_{13}
  \end{equation}
\end{definition}

\begin{proposition}
  For a fixed triangulation of a manifold $M$, and for any Ptolemy
  assignment of this triangulation,
  \begin{equation}
    \label{eq:ptolemy_to_cross_ratio}
    z_i = \pm \frac{c^i_{03} c^i_{12}}{c^i_{02} c^i_{13}}
  \end{equation}
  where the sign is determined by an obstruction class, as described
  in \parencite{1401.5542} and \parencite{garoufalidis2015}.
\end{proposition}

Since in our work we are interested only in $z_i$, we may often assume
without loss of generality that certain $c^i_{jk} = 1$, where the number
of such variables depends on the number of cusps of the manifold.

In the case of $m032$ (the manifold presented above), there are only three
distinct edges, therefore three independent $c^i_{jk}$ variables. The
Ptolemy relations are homogeneous degree 2 equations in two variables,
and taking one of the variables to be $1$ makes this a readily solvable
system.
