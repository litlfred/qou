---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-017-55-w-near-full-defects
section_title: "W near full defects"
section_number: 5.5
pages: 29-30
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:falling-down-holes}

On a close look at Figure \ref{fig:network-growth}, one notices that
as $\Lambda \to \infty$, all of the $\cS$-walls in $\wnet[\Lambda]$
asymptotically approach the full defects $D_n$.

To understand this concretely, let us consider the general behavior of $ij$-trajectories around a full defect.
In a local coordinate $z$ where the defect is at $z=0$,
we have
\begin{equation}
 \lambda^{(i)} = m^{(i)} \frac{\de z}{z} + \cdots
\end{equation}
where $\cdots$ denotes regular terms.  $ij$-trajectories near $z=0$ thus behave asymptotically like
\begin{equation}
 z(t) = z_0 \exp (\xi^{(ij)} t),
\end{equation}
where we defined
\begin{equation}
\xi^{(ij)} = \frac{e^{\I \vartheta}}{m^{(i)} - m^{(j)}}.
\end{equation}
As $t \to \infty$, we have $z(t) \to 0$ if and only if $\Re \, \xi^{(ij)} < 0$.
This suggests a natural ordering on the sheets in a neighborhood of $z=0$:  we say that $i < j$
if $\Re \, e^{- \I \vartheta}m^{(i)} < \Re \, e^{- \I \vartheta}m^{(j)}$.
$ij$-trajectories near $z=0$ asymptote to $z=0$ if and only
if $i < j$ in this ordering.

In the coordinate $z$,
these infalling trajectories asymptotically approach logarithmic spirals.  Passing to the covering coordinate $w = \log z$, the $ij$-trajectories are straight lines,
\begin{equation}
 w(t) = w_0 + \xi^{(ij)} t.
\end{equation}
Now suppose we have an infalling asymptotic $\cS$-wall of type $ij$ and another of type $jk$
(so $i < j < k$.)  Assuming $\arg \xi^{(ij)} \neq \arg \xi^{(jk)}$, these
two walls intersect at infinitely many
points as they spiral into $z = 0$.  Each intersection gives birth to a new $\cS$-wall of type $ik$,
which also spirals into $z = 0$.  This new $\cS$-wall can in turn intersect other
inspiraling $\cS$-walls
and give birth to yet more progeny.  The strict ordering of the sheets ensures
that the progeny cannot commit incest with one another.
Nevertheless, for $K>2$ there are an infinite number of joints accumulating at the
full defect.  See Figure \ref{fig:infalling-trajectories} for an illustration.
\insfigscaled{infalling-trajectories}{0.45}{$\cS$-walls falling into a full defect, shown in the covering coordinate
$w = \log z$.  There is a single $ij$ wall and a single $jk$ wall.  We have $i < j < k$
in the ordering described in the text.
Each intersection between these two walls generates a new $ik$ wall.  There are infinitely many
such intersections, accumulating at the defect, which generate infinitely many $ik$ walls.}
Similar (but more involved) remarks should apply for more general types of defect.

Based on computer experimentation, we expect that the behavior observed in Figure \ref{fig:network-growth}
is indeed generic:  whenever there is a defect
with sufficiently generic mass parameters, and $\vartheta$ is generic, all $\cS$-walls in $\wnet_\vartheta$
should asymptotically
approach punctures.  In the case $K=2$ this follows directly from known mathematical results on the trajectories of
quadratic differentials \cite{MR743423} (see \cite{Gaiotto:2009hg} for an account of this.)
For $K>2$ the analogous foundational results
are not yet available as far as we know.  It would be very desirable to work this out.
