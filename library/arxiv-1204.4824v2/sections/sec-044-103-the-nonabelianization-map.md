---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-044-103-the-nonabelianization-map
section_title: "The nonabelianization map"
section_number: 10.3
pages: 65-66
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Given a nondegenerate spectral network $\wnet$ subordinate to a covering
$\Sigma \to C$, we have defined a nonabelianization operation which takes
a twisted flat rank $1$ connection over $\Sigma$ to a twisted flat rank $K$
connection over $C$ with flag data.  In this section we discuss the corresponding
map $\Psi_{\wnet}$ between \ti{moduli spaces} of twisted flat connections.
For simplicity we take the case where $C$ only has punctures, not boundaries,
and restrict attention to $\wnet$ for which each $o(\fs_n)$ is a total ordering
of the set of all sheets.\footnote{Our discussion can be generalized
to include marked points on boundaries; in that case the relevant moduli spaces
are spaces of connections with \ti{irregular} singularities, on the surface obtained
by shrinking each boundary component of $C$ to a point.
In the special case $K=2$ this was discussed in \cite{Gaiotto:2009hg}.
Examples with irregular singularities and $K>2$ are discussed in
\cite{gmn6-to-appear}.}

Let us first describe the relevant moduli space of rank $1$ connections $\nabla^\ab$.
The covering surface
$\Sigma$ has punctures $\mathfrak{s}_n^{(i)}$, preimages of the $\fs_n$ on $C$.
Fix a complex line bundle $\CL$ over $\tilde{\Sigma}$;
we will consider flat connections
on $\CL$ with fixed holonomy around the punctures.
Namely, fix parameters $\fm^{(i)}_n \in \R / \Z$, with $\fm^{(i)}_n \neq \fm^{(j)}_n$
for $i \neq j$.
Let $\ell_{n^{(i)}}$ be a small counterclockwise
loop around $\fs_n^{(i)}$, and $\tilde \ell_{n^{(i)}}$ its canonical
lift to $\tilde \Sigma$.  We require that the holonomy of $\nabla^\ab$ around
$\tilde \ell_{\fs_n^{(i)}}$ is $\exp (2 \pi \I \mathfrak{m}_n^{(i)})$.
As usual, we consider connections $\nabla^\ab$
only up to gauge equivalence;
our gauge group is the group of smooth
maps $\bar \Sigma \to \IC^\times$,
where $\bar \Sigma$ is the closure
of $\Sigma$.  Let $\CM(\Sigma, GL(1); \mathfrak{m})$ be the resulting
moduli space of twisted rank 1 flat connections.
$\CM(\Sigma, GL(1); \mathfrak{m})$ is a torsor for
$H^1(\bar \Sigma, \IC^\times) \simeq (\IC^\times)^{2g}$, where $g$
is the genus of $\bar\Sigma$.

Next, what can we say about the rank $K$ flat connections $\nabla$ we obtain
by nonabelianization?
Fix a small clockwise loop $\ell_n$ around $\fs_n$, and let $\tilde \ell_n$
be its canonical lift to $\tilde C$.
The holonomy of $\nabla$ around $\ell_n$
is the product of several factors:  the holonomy of $\nabla^\ab$ along the
pieces of $\ell_n$ running between walls of $\wnet$, and the
transformations $\CT_p$ attached to the walls.  With respect to the decomposition
\eqref{eq:e-simp-decomp}, the former are diagonal matrices whose product is
$\diag \{\exp[ 2\pi \I \fm_n^{(i)}] \}$, while the latter are unipotent
upper triangular.  Their product is thus an upper-triangular matrix, with
diagonal elements $\exp[ 2\pi \I \fm_n^{(i)} ]$.
Since we have assumed these values
distinct, it follows that the monodromy of $\nabla$ around $\tilde \ell_n$
is semisimple, with eigenvalues $\exp[ 2\pi \I \fm_n^{(i)} ]$.
So, let $\CM(C, GL(K);\mathfrak{m})$
denote the moduli space of twisted rank $K$ flat connections on $C$
(with fixed topology of the principal bundle),
such that the monodromy around $\tilde \ell_n$ is conjugate to
\begin{equation}\label{eq:diag-elts-diag}
\diag \{ \exp[ 2\pi \I \fm_n^{(1)}], \dots,\exp[2\pi \I \fm_n^{(K)}] \}.
\end{equation}

As we have noted, nonabelianization produces not only a twisted flat connection over $C$,
but a twisted flat connection over $C$
equipped with flag data.  Thus we also define an extended moduli
space $\CM_F(C, GL(K);\mathfrak{m})$, consisting of elements of
$\CM(C, GL(K);\mathfrak{m})$ with flag data.
$\CM_F(C, GL(K);\mathfrak{m})$ is a finite cover of $\CM(C, GL(K);\mathfrak{m})$,
as explained at the end of \S\ref{sec:flags}.
Nonabelianization gives a map
\begin{equation}\label{eq:Psi-MAP}
\Psi_{\wnet}: \CM(\Sigma, GL(1); \mathfrak{m} )\to \CM_F(C, GL(K); \mathfrak{m}).
\end{equation}

One simple property of $\Psi_\wnet$ is worth noting at once.  Given a spectral network $\wnet$,
let $\wnet^*$ be obtained by reversing the labels on all walls and the orderings at all punctures.
Then we have
\begin{equation}
 \Psi_{\wnet^*}(\CL, \nabla^\ab) = \Psi_{\wnet}(\CL^*, (\nabla^\ab)^*)^*.
\end{equation}
This fact may be of some practical use:  the reason is that $\wnet_\vartheta^* = \wnet_{\vartheta + \pi}$,
and determining the relation between $\Psi_{\wnet_\vartheta}$ and $\Psi_{\wnet_{\vartheta+\pi}}$ is equivalent to
determining the ``spectrum generator'' which captures the full BPS spectrum.

For the rest of this section we will study $\Psi_\wnet$ as defined above.
However, we must note that in the physical applications the actual
moduli space $\CM$ of the physical theory $S[\fg, C, D]$ compactified on $S^1$
is not quite $\CM(C, GL(K); \fm)$;
it is more closely related to the space of $SL(K)$ connections (but even
this is a slight oversimplification, see \cite{Gaiotto:2010be}).
We expect that there is a variant of our nonabelianization map
for which the codomain is precisely $\CM$.
The domain of this variant map should not be quite $\CM(\Sigma, GL(1); \fm)$;
rather it should be a space
of twisted rank 1 connections on $\Sigma$ subject to some additional constraints and/or
carrying some additional structure.  This is related to the fact that
the IR charge lattice of $S[\fg, C, D]$ is not $H_1(\Sigma;\Z)$, but rather an appropriate
subquotient of it \cite{Gaiotto:2009hg}.  (See \cite{MR1397059,dongaits}
for a careful discussion of subtle
issues of this sort that arise
in abelianization of Higgs bundles for a general group $G$; we expect that, as far as
these topological issues are concerned, the story for moduli of twisted
flat connections will be similar.) We leave the proper extension of our construction
to account for these variations as an open problem. It is related to open problem 2
of \S \ref{sec:Introduction}.
