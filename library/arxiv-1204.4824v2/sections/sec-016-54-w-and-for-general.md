---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-016-54-w-and-for-general
section_title: "W[] and [] for general"
section_number: 5.4
pages: 27-29
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:constructing-w}

We have determined $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$ for small
$\Lambda$.
Now we can ask how $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$
evolve as $\Lambda$ increases.
Using the properties of $\wnet_\vartheta$ and $\mu$ we have already determined, it is
straightforward to deduce the answer.

The three $\cS$-walls
emerging from each branch point $\fb$ flow according to the
differential equation \eqref{eq:trajectory-de}, for a distance
determined by the cutoff $\Lambda$.
When we increase $\Lambda$ enough, it might happen that
an $\cS$-wall of type $ij$ intersects
another $\cS$-wall of type $jk$.  At this point
a new $\cS$-wall of type $ik$ is born, as shown in
Figure \ref{fig:ijkl-collision-birth}.  The soliton degeneracy $\mu$
on this new wall is determined by the soliton degeneracies on
its parents, as in \eqref{eq:cv-wcf}.\footnote{Note that if two $\cS$-walls
carrying charges $\bar a \in \Gamma_{ij}$, $\bar b \in \Gamma_{jk}$ meet at a joint $z \in C$,
the joint is visible in $\wnet_\vartheta[\Lambda]$ beginning
at $\Lambda = \textrm{Max}(\abs{Z_{\bar a}(z)},
\abs{Z_{\bar b}(z)})$, but the $\cS$-wall born from the joint
does not appear until
$\Lambda = \abs{Z_{\bar a}(z)}+\abs{Z_{\bar b}(z)}$.}
This new ``secondary'' $\cS$-wall, in turn, also evolves according to \eqref{eq:trajectory-de}.
As $\Lambda$ increases the secondary walls can intersect with other $\cS$-walls and give birth to yet
more progeny, and so on.
In Figure \ref{fig:network-growth} we give an illustration
of the growth of $\wnet_\vartheta[\Lambda]$ with $\Lambda$ in one particular theory $S[\fg,C,D]$.
\insfigscaled{network-growth}{0.52}
{Sample $\wnet_\vartheta[\Lambda]$ in the theory $S[A_2,\IC\IP^1,D]$
where the $D_n$ are 3 full defects (blue dots at $z = -1, 0, 1$).
We choose $\vartheta = \pi/4$, $\phi_2 = \frac{2}{(z - 1)^2} + \frac{2}{(z + 1)^2} - \frac{4}{z^2}$, $\phi_3 = \frac{1 - 3 (z - 1) + 6 (z - 1)^2}{(z - 1)^3} + \frac{1 + 3 (z + 1) + 6 (z + 1)^2}{(z + 1)^3} - \frac{2 + 12  z^2}{z^3}$.
The plots shown are at $\Lambda = 1, 2, 5, 12, 20, \infty$.
At $\Lambda = 0$ three $\cS$-walls are born at each of the 6 branch points
(orange crosses); at larger values of $\Lambda$, additional $\cS$-walls are born at intersections.
As $\Lambda \to \infty$ all $\cS$-walls asymptotically approach the defects.
Some $\cS$-walls are cut off
by the boundary of the plot; the visible range is a square with side length $2.6$.
See \cite{spectral-network-movies}
for an animated version of this figure.}

We may also have intersections where three $\cS$-walls meet at a point, as
in Figure \ref{fig:ijkl-collisions}.
(The reader might feel that this phenomenon should not occur generically; indeed, three arbitrary
trajectories of types $ij$, $jk$, $ik$ would be unlikely to intersect at a single point, but the $\cS$-walls
are not arbitrary trajectories.  We include an example in Figure \ref{fig:threefold-intersection}.)
\insfigscaled{threefold-intersection}{0.69}{A portion of a sample $\wnet_\vartheta$,
exhibiting an intersection between three $\cS$-walls, marked by a yellow dot.  The region in the blue box is
blown up at right.
The $\cS$-walls which appear somewhere
in the genealogy of the three intersecting $\cS$-walls are shown in black; other $\cS$-walls
are shown in gray.  There are six branch points (orange crosses).
This example arises in the theory $S[A_3, C = \IC\IP^1, D]$ with
$\phi_2 = -10z \, \de z^2$, $\phi_3 = 4 \, \de z^3$, $\phi_4 = 9 z^2 \, \de z^4$.
We took $\vartheta = 1.841$, but we emphasize that this triple intersection persists
for nearby $\vartheta$ as well.}

There is one more complicated phenomenon which one can imagine:
what would happen if an $\cS$-wall of type $ij$ ran directly into an $(ij)$ branch point?
In this case it would not be immediately clear how to continue the network
$\wnet_\vartheta[\Lambda]$ and the BPS degeneracies $\mu[\Lambda]$.
This puzzling-looking situation cannot occur when $\vartheta$ is generic.
It does occur for non-generic $\vartheta$,
and this fact plays a crucial role in the considerations of \S\ref{sec:varying-theta} below.

We have now
given a recipe for constructing $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$
for any $\Lambda > 0$ and generic $\vartheta$.  $\wnet_\vartheta[\Lambda]$
consists of a finite number of $\cS$-walls for any $\Lambda$.
Taking the limit $\Lambda \to \infty$ we obtain the full $\wnet_\vartheta$
and $\mu$.  So we have now managed to determine \ti{all} of the soliton degeneracies of the
theory (including their tricky signs) using only the constraint of homotopy invariance!

More precisely, so far we have fixed some $\vartheta$ and determined all $\mu(a,p)$ --- i.e. we determined $\mu(a)$
when the parameter $z$ of the surface defect lies on an $\CS$-wall supporting the charge $a$.  This is not what one
would usually mean by ``determining the soliton degeneracies'':  what one would usually mean is that we fix some $z$
once and for all, and then compute all $\mu(a)$ for $a \in \tGamma(\tz,\tz)$.  The point is that, for any $a \in \tGamma(\tz,\tz)$,
there is some $\vartheta$ for which $z$ \ti{does} lie on an $\CS$-wall supporting $a$:  namely,
$\vartheta = \arg -Z_{\bar a}$.  So for each $a$ we can draw the corresponding network $\wnet_{\vartheta= \arg -Z_{\bar a}}$
and use it to compute $\mu(a)$.
