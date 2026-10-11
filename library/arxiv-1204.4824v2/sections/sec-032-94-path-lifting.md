---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-032-94-path-lifting
section_title: "Path lifting"
section_number: 9.4
pages: 59-61
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
text_source: latex
latex_prose_ratio: 0.817
latex_coverage_ratio: 0.981
---
\label{subsec:Path-Lifting}

In \S\S\ref{sec:F-basics}-\ref{sec:wnet}
we studied at great length the generating functions $F(\wp, \vartheta)$ of
framed 2d-4d BPS degeneracies.
Let us set aside the physical meaning of these functions for a moment and just
think of them as some interesting mathematical objects.
We found in \S\ref{subsec:Compute-FP} that $F(\wp, \vartheta)$ could
be completely constructed from the datum of the spectral network $\wnet_\vartheta$
together with its soliton content.
One of the main motivations of our definition of spectral network is that,
given \ti{any} spectral network, we can make a very similar construction.
In this section we describe that construction.  For notational convenience we
consider only the case of a nondegenerate spectral network, but what we write
has an obvious extension to the degenerate case.

We will be rather brief since
everything is parallel to what we did in \S\ref{subsec:Compute-FP}.
However, we slightly modify
\S\ref{subsec:Compute-FP}, in two respects.  First,
with an eye toward future applications,
instead of \ti{homology} classes of open paths
on $\tilde\Sigma$, we will keep track of \ti{homotopy} classes.
This turns out to be no more difficult.
We will generally denote the homotopy objects with a bold letter to distinguish
them from their homology cousins.  Second, instead of considering smooth paths $\wp$ in $C$
and using their canonical lift to $\tilde C$, it will be convenient to
work with arbitrary paths $\twp$ on $\tilde C$ from the beginning.
This will involve lifting many objects from $C$ to $\tilde C$ or from $\Sigma$
to $\tilde \Sigma$; we always use a tilde
to denote the lifted objects.

For any homotopy class $\ba$ of open paths on $\tilde\Sigma$, we introduce a corresponding
formal variable $\bX_\ba$,
subject to the relation that if $\ba$ and $\ba'$ project to the same homotopy class on
$\Sigma$
then we have
\begin{equation} \label{eq:bold-winding-rule-2}
 \bX_\ba / \bX_{\ba'} = (-1)^{w(\ba,\ba')}.
\end{equation}
Now, given a spectral network $\wnet$, let $\tilde \wnet$ be the preimage of $\wnet$ on
$\tilde C$.  Given a
path $\twp$ on $\tilde C$ whose endpoints are not on $\tilde \wnet$,
we are going to define a formal sum of these variables, with integer coefficients:
\begin{equation} \label{eq:F-expand}
 \bF(\tilde \wp, \wnet) = \sum_{\ba} \fro'(\tilde \wp, \wnet, \ba) \bX_{\ba}.
\end{equation}
(In \S\ref{sec:gen-func} we met a similar expansion for which the coefficients $\fro'$
were interpreted as framed 2d-4d BPS degeneracies.  In the more general setting of this section,
we do not know what the physical interpretation of $\fro'$ should be.)

The assignment $\bF(\cdot, \wnet)$ will obey two important properties:
\begin{itemize}
 \item For two concatenatable paths $\twp$, $\twp'$ on $\tilde C$,
\begin{equation} \label{eq:composition-bold}
\bF(\twp \twp', \wnet) = \bF(\twp, \wnet) \bF(\twp', \wnet).
\end{equation}

\item If $\twp$ and $\twp'$ are two paths on $\tilde C$ which project to the same
homotopy class on $C$,
\begin{equation} \label{eq:twisted-homotopy}
\bF(\twp, \wnet) = (-1)^{w(\twp, \twp')} \bF(\twp', \wnet).
\end{equation}
(In particular, if $\twp$ and $\twp'$ are homotopic,
then $\bF(\twp, \wnet) = \bF(\twp', \wnet)$.)
\end{itemize}
Given any path $\twp$ on $\tilde C'$ we first define
\begin{equation}
 \bD(\twp) = \sum_{i=1}^K \bX_{\twp^{(i)}}.
\end{equation}
where  $\twp^{(i)}$ is the open path given by
lifting the initial point of $\twp$ to the $i$-th sheet and then using the
canonical connection on $\tilde \Sigma \to \tilde C$ to lift the path.
For any $\twp$ which does not cross $\tilde \wnet$ we have simply
\begin{equation} \label{eq:F-no-cross}
 \bF(\twp, \tilde\wnet) = \bD(\twp).
\end{equation}
For any $\twp$ which crosses $\tilde \wnet$ exactly once at a wall $p_c$, we have
\begin{equation} \label{eq:F-one-cross}
 \bF(\twp, \tilde\wnet) = \bD(\twp_+) \left(1 + \sum_{\nu \in \CS_c} \bX_{\ba(\nu,\twp)}\right) \bD(\twp_-),
\end{equation}
where $\ba(\nu,\twp)$ is a particular lift of the soliton $s_\nu$
to $\tilde\Sigma$, described in the next paragraph.

Let $\wp$ be the projection of $\twp$ to $C$.  Let $z$ be the point of intersection between $\wp$ and $\wnet$.
Let $\tz$ be the point of $\twp$ lying over $z$, dividing $\twp$
into $\twp_+ \twp_-$.
Let $o_+$ be a tangent vector at $z$ oriented along $\wnet$,
and $o_-$ a tangent vector at $z$ oriented oppositely to $\wnet$.
Let $A_+$ be some
path from $\tz$ to $o_+$ in the circle fiber $\tilde C_z$,
and $A_-$ a path from $o_-$ to $\tz$ in $\tilde C_z$.  The
concatenation $A = A_- + A_+$ is thus a path from $o_-$ to its antipode
$o_+$ in $\tilde C_z$;
we fix our choices of $A_\pm$ so that $A$ is homotopic to
a simple arc which covers half of $\tilde C_z$, and this arc includes
the tangent vector $\wp'(z)$.
Each soliton $s_\nu(z)$ has a canonical lift to a smooth path
$\tilde s_\nu(z)$ on $\tilde \Sigma$ from $o_+^{(i)}$ to $o_-^{(j)}$.
The path $\ba(\nu,\twp)$ on $\tilde \Sigma$ from $\tz^{(i)}$ to $\tz^{(j)}$ is defined by
\begin{equation}
 \ba(\nu,\twp) = A^{(i)}_+ + \tilde s_\nu(z) + A^{(j)}_-.
\end{equation}

Finally, to define $\bF(\twp, \wnet)$ for an arbitrary path $\twp$ on $\tilde C$ whose endpoints are
not on $\tilde\wnet$, we perturb $\twp$ slightly
so that its intersections with $\tilde \wnet$ are all transverse, break it into
pieces which meet $\tilde \wnet$ at most once, and use \eqref{eq:F-no-cross},
\eqref{eq:F-one-cross} and the composition property
\eqref{eq:composition-bold}.

Our construction makes the composition property \eqref{eq:composition-bold} manifest.
The same arguments given in \S\ref{sec:homotopy-invariance} apply
to our current construction and show the twisted homotopy invariance
\eqref{eq:twisted-homotopy}.

The path-lifting rule $\bF$ will be put to some mathematical use in
\S \ref{sec:moduli} below.
As mentioned in \S \ref{sec:Introduction}, we are hopeful that it will also have
some interesting physical applications, as well as connections to
upcoming work of Goncharov and Kontsevich.



\section{Coordinates for moduli of flat connections}\label{sec:moduli}

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
