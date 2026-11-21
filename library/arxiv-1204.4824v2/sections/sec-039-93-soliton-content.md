---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-039-93-soliton-content
section_title: "Soliton content"
section_number: 9.3
pages: 56-59
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.996
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:Soliton-content}

To a spectral network we can associate some additional data
having to do with \ti{solitons}, which we now define.

A \emph{soliton} $s(z)$, where $z\in p_c$, is an immersion of $[0,1]$ into $\Sigma$,
which begins and ends on preimages of $z$, and such that its projection to $C$ lies
in the spectral network $\wnet$ (or more precisely in a very small neighborhood of $\wnet$;
this correction is necessary because at joints we smooth out
the sharp corners.)  If $p_c$ carries the label $(o, ij)$,
then we say $s(z)$ is \emph{compatible with $o$}
if it begins on $z^{(i)}$ and ends on $z^{(j)}$, and the projection of
$s(z)$ to $C$ begins with orientation $-o$ and ends with orientation $o$.
The soliton content is, for each street $p_c$ and each point $z \in p_c$, a pair of sets of
solitons $\CS^o_c(z)$, $\CS^{-o}_c(z)$, such that
the solitons in $\CS^{o}_c(z)$ are compatible with $o$ and
those in $\cS^{-o}_c(z)$ are compatible with $-o$.

The soliton sets must satisfy some rules, which we will refer to
as \emph{solitonic traffic rules}.  Actually the rules come in two variants:  either
\ti{American} or \ti{British}.  In order to state the rules we introduce a
resolution of the streets of the spectral network, regarding each street as resolved into
two oriented ``lanes'' infinitesimally displaced from one another, either in the ``American'' or the ``British'' fashion.  See Figure \ref{fig:resolutions}.
\insfig{resolutions}{The American (left) and British (right) resolutions of a street.}
Note that this definition uses the
orientation of $C$.  The American and British traffic rules are thus related to one another by a
reflection in the plane.  In what follows we show the British rules only; to get the American
rules simply requires a little reflection.

\begin{description}
\item[ST1.] As $z$ moves continuously along a street $p_c$, the soliton sets
$\CS_c^{\pm o}(z)$ evolve continuously, by the natural parallel transport; in
other words, the soliton sets do not ``jump.''
With this in mind, we abuse notation by writing the soliton sets
simply as $\CS_c^{\pm o}$, suppressing the trivial $z$ dependence.

\insfig{soliton-rules-2}{A spectral network in the vicinity of a branch point.}
\item[ST2.]
Let $\fb$ be a branch point.  The network $\wnet$ then looks like Figure
\ref{fig:soliton-rules-2} in the vicinity of $\fb$.
There are three streets $p_c$ emerging from $\fb$.
We denote the set of orientations of each street by $\{\iin, \out\}$.
For each $c$, define the \emph{light soliton} $s_c$ as follows:
if $p_c$ carries the label $(\out,ij)$,
then $s_c(z)$ begins on $z^{(i)}$, travels along $p_c^{(i)}$
back to the ramification
point on $\Sigma$ covering $\fb$, and returns along $p_c^{(j)}$ to
$z^{(j)}$.  Then,
the soliton sets are related by
\begin{equation}
\CS_1^{\out} = \CS_3^\iin \cup \{ s_1 \}, \quad
\CS_2^{\out} = \CS_1^\iin \cup \{ s_2 \}, \quad
\CS_3^{\out} = \CS_2^\iin \cup \{ s_3 \}.
\end{equation}
(In this equation the solitons are understood to be evolved continuously from
one street to the other.  Since there is a branch point at $\fb$, this continuous
evolution depends on which path we follow to go from one street to the next;
we follow the \ti{short} path, i.e. we go around an arc of length $2 \pi / 3$,
not $4 \pi / 3$.)

\insfigscaled{joint-rule}{0.34}{The rule for constructing outgoing solitons from a
six-way junction, with the British resolution.
We show six allowed types of junction,
one in each ``Weyl chamber'' around the joint.  The most general outgoing soliton
is constructed by a diagrammatic prescription
as follows.  We fix any set of incoming solitons; for each one we draw
an incoming line on the diagram, coming in along the appropriate direction,
and on the left side of the median.
We then combine these incoming solitons with junctions of the allowed types,
to make a single outgoing line.  Every diagram so obtained determines an outgoing
soliton in a natural way, by concatenation of the incoming solitons.}

\insfigscaled{joint-rule-examples}{0.15}{Some examples of diagrams representing outgoing solitons.
Incoming solitons are represented by black lines, the outgoing path by a red line.
(The first example is exceptional in that the incoming line is the same as
the outgoing one.)}

\item[ST3.] In a sufficiently small neighborhood of
a joint of the ``four-way junction''
type shown in Figure \ref{fig:trajectories-meeting-commuting} (where $ij$ and $kl$ walls meet),
the soliton sets vary continuously, i.e. the outgoing soliton sets are equal to the
incoming ones.
In a sufficiently small neighborhood of a joint of the ``six-way junction'' type
(where $ij$, $jk$ and $ki$ walls meet),
the outgoing soliton sets are
determined by the incoming ones according to the
rules shown in Figures \ref{fig:joint-rule}, \ref{fig:joint-rule-examples}.
(A motivation for this peculiar-looking rule
is explained in Appendix \ref{app:joint-rules}.)

\end{description}

Importantly, for any spectral network $\wnet$, the
solitonic traffic rules (including the choice of American or British)
uniquely determine the soliton content.
To prove this claim one can consider a discrete
version of the mass filtration of the spectral networks $\wnet_\vartheta$:
just define the \ti{length} of a soliton to be the number of walls in its
projection to $C$, and construct the soliton content by induction on length
using the solitonic traffic rules.

It is convenient to distinguish two different possibilities for the soliton content.
Consider the two soliton sets $\CS_c^o$, $\CS_c^{-o}$ on a street $p_c$.
If both are nonempty, we refer to $p_c$ as a
\emph{two-way street}.  If exactly one is empty, $p_c$
is a \emph{one-way street}, and in that case we write $\CS_c$ for the single
nonempty soliton set.  (It never happens that both are empty.)
If there are no two-way streets
we say that $\wnet$ is a \emph{nondegenerate} spectral network; otherwise we
say it is \emph{degenerate}.

If $\wnet$ is nondegenerate, the solitonic traffic rules
simplify considerably, to the following.
Consider the joint of Figure \ref{fig:ijkl-collisions}.  We continue the $ij$ and
$jk$ soliton sets continuously through the joint.
For the $ik$ wall, after passing through the joint we add to the set
of $ik$ solitons all new solitons of the
following description:  the new soliton begins at $z^{(i)}$,
projects on $C$ to the path going back to the joint,
then follows one of the the $ij$ solitons from
sheet $i$ to sheet $j$ above the joint, then follows one of the $jk$ solitons from
sheet $j$ to sheet $k$ above the joint, then returns on sheet $k$ on the
trajectory projecting to the $ik$ wall ending at $z^{(k)}$.
In particular, these simplified rules do not depend on whether we started out with
American or British traffic rules (as we should expect since we are
considering the case where there are no two-way streets.)

So for nondegenerate spectral networks the soliton content
is unique, while for degenerate ones there are two possible soliton contents,
one following American traffic rules and one British.

In previous sections we considered integers
$\mu(p,a)$ attached to the spectral networks $\wnet_\vartheta$.  These integers are determined
by the soliton content of $\wnet_\vartheta$ --- indeed they are simply
counts of the solitons with appropriate signs:  $\mu(p_c, a) X_a = \sum_{\nu \in \CS_c} X_{[\tilde s_\nu]}$.
So the soliton content is a slight extension of the $\mu(p,a)$ to keep track of the actual solitons,
not only their number.  This extension will actually not be used for anything in this paper (all
of our constructions really depend only on $\mu$)
but we believe it may be useful in the future.
