---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-049-108-coordinate-systems-and-a-cluster-conjecture
section_title: "Coordinate systems and a cluster conjecture"
section_number: 10.8
pages: 71-72
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:Coord-System}

Let us consider a spectral network $\wnet$ for which \eqref{eq:Branch-bound}
is saturated.  In this case, as we have noted,
$\Psi_\wnet$ is at least locally one-to-one.
Thus the holonomies $\tilde\CY_{\tilde\gamma}$ of $\nabla^\ab = \Psi_\wnet^{-1}(\nabla)$,
where $\tilde\gamma$ runs over a basis of $H_1(\tilde\Sigma;\IZ)$,
provide \ti{local coordinates} on $\CM_F(C, GL(K);\mathfrak{m})$.

It is natural to ask whether $\Psi_\wnet$ might be even globally one-to-one,
so that it would give global coordinates on its whole image $\CU_\wnet$.
We conjecture that this is indeed the case.\footnote{This is the moment where it is important
that we use the moduli space $\CM_F(C, GL(K);\mathfrak{m})$ with flag data rather than just $\CM(C, GL(K);\mathfrak{m})$.  If we used $\CM(C, GL(K);\mathfrak{m})$, then
$\Psi_\wnet$ would be only finite-to-one.}
At least in the case $K=2$ this conjecture
is true:  in this case the coordinate system in
question is essentially the Fock-Goncharov coordinate system \cite{MR2233852,Gaiotto:2009hg}.
Some further special cases in which the conjecture is true
will be treated in \cite{gmn6-to-appear}.

As we noted above, if $\wnet$ and $\wnet'$ are equivalent
nondegenerate spectral networks then
$\Psi_{\wnet}$ and $\Psi_{\wnet'}$ are related by parallel transport, in the sense
explained under \eqref{eq:equalpt}.
Thus we can roughly say that $\Psi_\wnet$ is constant as $\wnet$ varies within one of
the cells of $X$.  If $\wnet$ and $\wnet'$ are in neighboring cells, then the story is
more interesting:  taking a path $\wnet(t)$ from $\wnet$ to $\wnet'$, there is a critical
$t = t_c$ where $\wnet(t)$ becomes a degenerate spectral network.
At this moment $\Psi_{\wnet(t)}$ jumps discontinuously.  This jump should be determined by the arguments of \S\ref{sec:f-jump}.
Indeed, by the same formulas we used there (and assuming the same conjectures we
assumed there), the degenerate network $\wnet(t_c)$ determines integers $\Omega(\gamma)$
and distinguished lifts $\tilde\gamma$,
for $\gamma$ lying in a semilattice $\Gamma_c \subset H_1(\Sigma(t_c); \IZ)$ with a single generator.
Using these data we define a (birational) automorphism $\CK$ of
$\CM(\Sigma(t_c), GL(1); \fm)$, by its action on the holonomies $\tilde\CY_{\tilde\gamma}$
of $\nabla^\ab$ around 1-cycles $\tilde\gamma$:
\begin{equation} \label{eq:holonomy-jump}
 \CK(\tilde\CY_{\tilde\gamma}) =\tilde \CY_{\tilde\gamma} \prod_{\gamma' \in \Gamma_c}
 (1 + \tilde \CY_{\tilde\gamma'})^{\inprod{\gamma,\gamma'} \Omega(\gamma')}.
\end{equation}
When $t$ crosses $t_c$, the map $\Psi_{\wnet(t)}$ jumps by composition with $\CK$, so
\begin{equation}
\Psi_{\wnet}(\nabla^\ab) = \Psi_{\wnet'}(\CK^{\pm 1}(\nabla^{\ab}))
\end{equation}
(where the sign $\pm 1$ is determined by which direction we cross the cell boundary, and
we must bear in mind the comment under \eqref{eq:equalpsi}.)

Finally, we conjecture that the coordinate systems we have defined are actually
\ti{cluster} coordinates.\footnote{It was noted in \cite{ks1,Gaiotto:2010be} that
the $\CK$-transformations which appeared there
could be viewed as cluster transformations in an appropriate sense; see also
\cite{Cecotti:2010fi,Cecotti:1993rm,Alim:2011ae,Alexandrov:2011ac,Cecotti:2011gu} for further
discussion of the relation of cluster varieties to four-dimensional
$\CN=2$ theory.}  The spaces $\CM(C)$ which we are considering are indeed cluster varieties,
as shown by Fock-Goncharov in \cite{MR2233852}.  However, relatively few of the cluster
coordinate systems on $\CM(C)$ have been described explicitly.  We believe that for each $\wnet$, the coordinate system
induced by $\Psi_\wnet$ should be an element of the cluster atlas.
So in particular,
we conjecture that there is an algorithm which determines from a
$\wnet$ a finite set of charges $\gamma^{n}_{\wnet} \in \Gamma$.
The $\gamma^{n}_{\wnet}$ should be the elements of a cluster
seed, with exchange matrix given by the intersection pairings:
$\eps^{nm} = \inprod{\gamma^{n}, \gamma^{m}}$.
Informally speaking, the $\gamma^{n}_\wnet$ should be
the charges of finite webs which can appear inside of $\wnet$ when $\wnet$ degenerates;
said otherwise, the $\gamma^{n}_\wnet$
label faces of the boundary of the cell in $X$ containing $\wnet$.
Finally, the $\cK$-transformation \eqref{eq:holonomy-jump}, in the simplest case where there is only a
single $\Omega(\gamma) = 1$ contributing,
should be identified with the action of a mutation on cluster variables.

This conjecture is true when $K=2$, and in \cite{gmn6-to-appear} we will
give some additional evidence for it in some special cases with $K>2$.  In general, though,
we do not know how to prove it, or even how to read off the $\gamma^{n}_\wnet$ from $\wnet$.

It is natural to wonder further whether spectral networks might give \ti{all} of the coordinate
systems in the cluster atlas on $\CM$.
