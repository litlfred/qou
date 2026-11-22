---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-041-10-coordinates-for-moduli-of-flat-connections
section_title: "Coordinates for moduli of flat connections"
section_number: 10
pages: 61-62
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:moduli}

In this last section we discuss a mathematical application of spectral networks.
Given a spectral network $\wnet$ subordinate to a $K$-fold covering $\Sigma \to C$, we will construct
a map
\begin{equation}
 \Psi_\wnet: \CM(\Sigma, GL(1); \fm) \to \CM_F(C, GL(K); \fm)
\end{equation}
where $\CM(\Sigma, GL(1); \fm)$ is a moduli space of twisted flat $GL(1)$-connections $\nabla^\ab$ on $\Sigma$
and $\CM_F(C, GL(K); \fm)$ is a moduli space of twisted flat $GL(K)$-connections $\nabla$ on $C$, decorated
by some ``flag data'' as we explain below.
This map is a local symplectomorphism, and conjecturally 1-1 onto its image.

Roughly speaking,
$\nabla = \Psi_\wnet(\nabla^\ab)$ is obtained by a two-step process.  We first push forward the $GL(1)$ connection $\nabla^\ab$ from
$\Sigma$ to $C$.  This gives a flat $GL(K)$ connection on the complement of the branch locus in $C$, which is
everywhere diagonal.  This connection however cannot be extended over the branch points, because it has
monodromy around them.  To deal with this problem we cut $C$ into pieces along the network $\wnet$,
and then reglue the connection with a nontrivial (and non-diagonal) transition function, controlled by
the soliton content of $\wnet$.
This process eliminates the monodromy around branch points, while not introducing unwanted
monodromy anywhere else.  We call this construction ``nonabelianization.''

The space $\CM(\Sigma, GL(1); \fm)$ is a torsor for $(\IC^\times)^{2 g_{\bar\Sigma}}$,
where $\bar\Sigma$ is the closure of $\Sigma$,  so another way to
read $\Psi_\wnet$ is as a \ti{local coordinate system} on $\CM_F(C, GL(K); \fm)$.
These coordinate systems are closely related to the ``cluster coordinates''
introduced by Fock and Goncharov \cite{MR2233852}.  In the case $K=2$, it is straightforward to see that
our coordinates in fact coincide with the cluster coordinates.  In the case $K>2$ a fully explicit description
of the most general cluster coordinate system is not available in the literature; we conjecture that
the $\Psi_\wnet$ actually give the most general cluster coordinates, thus filling this gap.

One point in favor of this conjecture is that when
$\wnet$ is of a special form, $\Psi_\wnet$ yields a coordinate system which was explicitly described by
Fock and Goncharov; this will be described in \cite{gmn6-to-appear}.

Although we are emphasizing its mathematical content in this section, this
construction also has a natural physical meaning, which appears most clearly
when the theory is compactified from four to three dimensions on $S^1$.
Indeed, the expansion \eqref{eq:pt-exp} of the parallel transport of $\nabla$
as a linear combination of parallel transports $\bX_a(\nabla^\ab)$ is precisely the
``Darboux expansion'' of the vacuum expectation value of the supersymmetric interface
associated with $\tilde \wp$.  This point of view was described at length in \cite{Gaiotto:2011tf}.
