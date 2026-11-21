---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-034-82-the-pure-su3-theory-at-strong-coupling
section_title: "The pure SU(3) theory at strong coupling"
section_number: 8.2
pages: 51-52
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:su3-strong}

For our next example we take again $K=3$ and $C = \IC\IP^1$,
but this time with defects both at $z = 0$ and $z = \infty$, with each defect
imposing the boundary conditions that $\phi_2$ has a pole of order at most 2 and $\phi_3$ one of order 4.
These conditions imply that after rescaling the coordinate $z$, one can put
$\phi_2$ and $\phi_3$ in the form
\begin{equation}
 \phi_2 = -3 u_2 \, \left( \frac{\de z}{z} \right)^2, \qquad \phi_3 = \left( \frac{\Lambda}{z} + u_3 + \Lambda z \right) \left(\frac{\de z}{z}\right)^{3}.
\end{equation}
This corresponds to the pure $SU(3)$ theory \cite{Gaiotto:2009hg}.
Here $\Lambda$ is a parameter (the dynamical scale)
and $(u_3,u_2)$ parameterize the Coulomb branch.
In this paper will not attempt a complete study of the BPS spectrum in this theory:
we just describe what happens at the locus where $u_3 = 0$ and $\abs{u_2} \ll \abs{\Lambda}^{\frac23}$.
This locus is in the ``strongly coupled'' region of the theory.

We could proceed immediately to the pictures of $\wnet_\vartheta$ as $\vartheta$ varies,
but to calibrate our expectations, it is useful to make
some preliminary exploration.
At a generic point $(u_3,u_2)$, the Seiberg-Witten curve $\Sigma$ is a 3-fold covering of $C$
with $4$ simple branch points.  If $u_2 = 0$ then the $4$ branch points coalesce in pairs.
Each pair consists of an $(ij)$ and a $(jk)$ branch point, which at $u_2=0$ coalesce to a single
branch point, with cyclic monodromy $(ijk)$.  There is nothing singular about this situation from the point of view of the IR 4-dimensional
physics (in contrast with the case where two $(ij)$ branch points coalesce, in which case the mass of a BPS hypermultiplet goes to zero.)
For small $u_2$ and generic $\vartheta$, we can work out (and verify by computer calculation) what
the spectral network $\wnet_\vartheta$ around such a pair looks like:
see Figure \ref{fig:two-colliding-bp}.
Taking the limit $u_2 \to 0$ we find that the branch points with monodromy $(ijk)$ emit $8$ walls.
As $\vartheta$ is increased continuously through an angle
$\pi/3$, these $8$ walls rotate by one unit counterclockwise.
\insfig{two-colliding-bp}{Left: the spectral network $\wnet_\vartheta$ in a neighborhood of a pair of nearby branch points
of types $(ij)$ and $(jk)$; right: the limit where the branch points coalesce to form a branch point of type $(ijk)$.
This situation occurs in the pure $SU(3)$ theory as $u_2 \to 0$.}

Now fixing $u_3 = 0$ and $u_2$ small (or even $u_2 = 0$) we can draw $\wnet_\vartheta$ as $\vartheta$ varies from $0$ to $\pi$.
In fact, the picture has a further approximate
symmetry under a shift $\vartheta \mapsto \vartheta + \frac{\pi}{3}$ (which becomes exact at $u_2=0$), so we only need
to look at the variation over some range of length $\frac{\pi}{3}$.  We show this variation in Figure \ref{fig:su3-evolution}.
\insfigscaled{su3-evolution}{0.6}{The evolution of $\wnet_\vartheta$ from $\vartheta = \frac{\pi}{30}$ to $\vartheta = \frac{11 \pi}{30}$,
at $u_3 = 0$ and very small $u_2$.  Each figure is drawn on a flattened-out cylinder, so the left and right sides should be identified.
Note that the last figure looks essentially identical to the first.
There are two critical phases $\vartheta_c$ in this range, very close together,
marked by the two blue lines.  See \cite{spectral-network-movies}
for an animated version of this figure.}
We find two critical phases $\vartheta_c$ very close together.  At each critical phase
a BPS hypermultiplet
appears, represented by a two-way street connecting the two pairs of branch points.
(One of these is evident in the figure; the other is harder to spot since it exits the right side and re-appears on the left.)
As $\vartheta$ varies from $0$ to $\pi$ this picture is repeated twice more, giving $2$ more BPS states each time.
Thus altogether we find that
the strong-coupling spectrum of the $SU(3)$ theory consists of $6$ distinct BPS hypermultiplets
(or $12$ if we include the antiparticles).  This agrees with the recent
result of \cite{Alim:2011ae,Alim2011a}
where the same spectrum is obtained using quiver representations.
