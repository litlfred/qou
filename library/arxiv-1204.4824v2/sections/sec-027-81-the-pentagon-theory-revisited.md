---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-027-81-the-pentagon-theory-revisited
section_title: "The pentagon theory revisited"
section_number: 8.1
pages: 48-52
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.975
---
The first new example we consider is obtained by taking $K=3$ and $C = \IC\IP^1$,
with a single defect at $z = \infty$, imposing the boundary conditions
that $\phi_2$ has a pole of order 4 and $\phi_3$ one of order 8.
These conditions imply that after rescaling and shifting the coordinate $z$, one can put
$\phi_2$ and $\phi_3$ in the form
\begin{equation}
 \phi_2 = 3 \Lambda^2 \, \de z^{2}, \qquad \phi_3 = (z^2 + u) \, \de z^{3}.
\end{equation}
Here $\Lambda$ is a parameter and $u$ parameterizes the 1-dimensional Coulomb branch $\CB$.
For any particular $u$, we have a corresponding $3$-fold cover of $C$ (Seiberg-Witten curve) given by \eqref{eq:sw-curve},
\begin{equation}
 \Sigma = \{ \lambda^3 + (3 \Lambda^2 \, \de z^{2}) \lambda + (z^2 + u) \, \de z^{3} = 0 \} \subset T^* C,
\end{equation}
or if we write more concretely $\lambda = x \, \de z$,
\begin{equation} \label{eq:sw-pentagon-1}
 \Sigma = \{ x^3 + 3 \Lambda^2 x + z^2 + u = 0 \}.
\end{equation}

We can now study the BPS spectrum, by scanning through the spectral networks $\wnet_\vartheta$ as $\vartheta$ varies
between $0$ and $\pi$ and looking
for critical phases where the topology of $\wnet_\vartheta$ jumps.

\insfig{pentagon-evolution-strong}{The network $\wnet_\vartheta$ when $u=0$, at the phases $\vartheta = \pi n / 10$, with
$1 \le n \le 10$; the first row begins with $n=1$ and the second with $n=6$.  We indicate the labelings of the $\cS$-walls
in the $n=1$ figure:  all walls in each indicated group carry the same label (e.g. there are three walls carrying the label $13$
exiting the figure to the north.)  The two critical phases at which a $\cK$-wall occurs
are indicated by blue lines; one is between $n=2$ and $n=3$, the other between $n=7$ and $n=8$.  See \cite{spectral-network-movies}
for an animated version of this figure.}
\insfigscaled{pentagon-bps-states-strong}{0.45}{The two saddle connections which appear at the critical phases, when $u=0$.  They could equally
well have been represented by segments with the opposite orientation and the labels $ij$ transposed.}
For example, suppose $u = 0$.  In this case
$\wnet_\vartheta$ jumps 2 times as we vary the phase, as we show in Figure \ref{fig:pentagon-evolution-strong}.
Both of these jumps are of the type we discussed in \S\ref{sec:saddle-connection}:
at the critical phase there is a saddle connection, i.e. an $ij$-trajectory
running between two $(ij)$ branch points.
We depict these two saddle connections in Figure \ref{fig:pentagon-bps-states-strong}.  Following the recipe of \S\ref{sec:f-jump} we see that
they correspond to closed loops $L_1$, $L_2$ on $\Sigma$ (just obtained by lifting the saddle connections to $\Sigma$) with corresponding
charges $\gamma_1 = [L_1]$, $\gamma_2 = [L_2]$, and the 4d BPS degeneracies are
\begin{equation}
\Omega(\gamma_1) = 1, \qquad \Omega(\gamma_2) = 1.
\end{equation}
(We also have $\Omega(-\gamma_1) = \Omega(-\gamma_2) = 1$; these other two BPS multiplets would be encountered in varying
$\vartheta$ between $\pi$ and $2 \pi$.  The network $\wnet_{\vartheta+\pi}$ is obtained from $\wnet_\vartheta$ just by
transposing the labels $ij$ on all walls, so we do not need to draw new figures for this range of phases.)
The intersection pairing between these charges is $\inprod{\gamma_2, \gamma_1} = 1$;
this reflects the fact that the two saddle connections cross at a single point, at which they have a single sheet in common
(sheet $2$ in the notation of Figure \ref{fig:pentagon-bps-states-strong}.)

On the other hand, suppose we take $u/\Lambda = 5$.  In this case the picture looks somewhat different:  $\wnet_\vartheta$ jumps 3 times
as we vary $\vartheta$ from $0$ to $\pi$, as shown in Figure \ref{fig:pentagon-evolution-weak}.  These three jumps correspond to three finite
webs as indicated in Figure \ref{fig:pentagon-bps-states-weak}.
\insfig{pentagon-evolution-weak}{The network $\wnet_\vartheta$ when $u=4$ and $\Lambda=1$, at the phases $\vartheta = \pi n / 200$, with
(reading from left to right and top to bottom)
$n = 1, 23, 45, 68, 82, 90, 97, 103, 110, 118, 132, 155, 177, 199$.  The three critical phases at which a $\cK$-wall occurs
are indicated by blue lines.  See \cite{spectral-network-movies}
for an animated version of this figure.}
\insfigscaled{pentagon-bps-states-weak}{0.45}{The two saddle connections and one more complicated finite web
which appear at the critical phases, when $u=4$
and $\Lambda = 1$.  Each segment could equally well be replaced
by one with the opposite orientation and the labels $ij$ transposed.}

Again following \S\ref{sec:f-jump} we find that all three of these lift to closed loops on $\Sigma$, now with corresponding charges
$\gamma_2$, $\gamma_1 + \gamma_2$ and $\gamma_1$ in order, and we have
\begin{equation}
 \Omega(\gamma_1) = 1, \qquad \Omega(\gamma_2) = 1, \qquad \Omega(\gamma_1 + \gamma_2) = 1
\end{equation}
(along with $\Omega(-\gamma_1) = \Omega(-\gamma_2) = \Omega(-\gamma_1-\gamma_2) = 1$, as before).

So the 4d BPS spectrum changes as we vary $u$.  Of course, this is not unexpected:
it is the wall-crossing phenomenon, and occurs exactly as
predicted by the wall-crossing formula \cite{Denef:2007vg,ks1,Gaiotto:2008cd,Gaiotto:2009hg}.
At large $\abs{u}$ the two BPS multiplets of charges $\gamma_1$ and $\gamma_2$ form
a bound multiplet of charge $\gamma_1 + \gamma_2$.

The BPS spectrum here (two hypermultiplets with symplectic product $1$ at small $\abs{u}$,
three hypermultiplets at large $\abs{u}$) might look familiar to the reader:
it is just the same structure one meets in the first nontrivial Argyres-Douglas theory.
Wall-crossing in Argyres-Douglas theories was first studied in \cite{Shapere:1999xr};
we also studied this particular theory in
Section 9.4.4 of \cite{Gaiotto:2009hg}.  There
we took $K=2$ and $\phi_2 = z^3 - 3 \Lambda^2 z + u$,
thus obtaining the Seiberg-Witten curve
\begin{equation}
 \Sigma = \{ \lambda^2 + (z^3 - 3 \Lambda^2 z + u) dz^{2} = 0 \},
\end{equation}
or writing $\lambda = x\, \de z$,
\begin{equation}
 \Sigma = \{ x^2 + z^3 - 3 \Lambda^2 z + u = 0 \}.
\end{equation}
Now comes the point:  the change of variables $x \to -z$, $z \to x$ transforms this into \eqref{eq:sw-pentagon-1}!
This change of variables
does not quite preserve $\lambda$, but it takes $\lambda \to \lambda - \de(x z)$,
so as far as the periods of $\lambda$ over closed cycles
are concerned, these two Seiberg-Witten curves
are fully equivalent.  This constitutes strong evidence that the two 4d
theories $S[A_1, C, D]$ and $S[A_2, C, D']$ which we have considered
are actually the same.
These two descriptions of the theory however
privilege different classes of surface
defect, one with $K=2$ vacua and one with $K=3$.
Moreover they lead to rather different-looking representations of the BPS states:
in the $K=2$ picture, all three BPS hypermultiplets at large $u$ are represented by saddle
connections, quite unlike the situation depicted in Figure \ref{fig:pentagon-bps-states-weak}.  We regard the fact that the BPS degeneracies nevertheless
agree as a useful consistency check of our story.

This ``duality'' between two different descriptions of the same theory is an example
of a more general phenomenon.  There is a class of theories discussed in \cite{Cecotti:2010fi}, labeled by pairs
$(G,G')$ of Dynkin diagrams, and the theory with diagram $(G, G')$ is the same as the one with diagram $(G', G)$.
The example we considered here is the case of $(A_1, A_2)$.



\subsection{The pure $SU(3)$ theory at strong coupling}\label{sec:su3-strong}

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
