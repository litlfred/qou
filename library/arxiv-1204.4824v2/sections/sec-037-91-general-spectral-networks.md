---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-037-91-general-spectral-networks
section_title: "General spectral networks"
section_number: 9.1
pages: 55-56
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:GenSpecNet}

Let $C$ be an oriented real surface with a (perhaps empty) boundary.
Each connected component of the boundary is a copy of $S^1$;
on each such component fix a (nonempty) set of marked points.  Also fix a (perhaps empty) set of marked
points in the interior of $C$. We refer to the interior marked points as \emph{punctures} and
we refer to all the marked points as \ti{singular points} (although they are not singularities of $C$)
and denote them as $\mathfrak{s}_n$.  We require that there is at least one singular point.

Let $\Sigma \to C$ be a $K$-fold branched covering which is unramified
over the boundaries and the singular points.
Let $C'$ be $C$ minus the branch points.
For simplicity we assume the branch points are all simple,
so the monodromy around each branch point just exchanges
two sheets of $\Sigma$. (This condition can likely be relaxed at the price of a
more cumbersome definition.)

A \emph{spectral network subordinate to
the covering $\Sigma$} is a collection
\begin{equation}
\wnet = ( o(\mathfrak{s}_n), \{z_\mu\}, \{p_c\} )
\end{equation}
where the symbols refer to the following data:

\begin{description}
\item[D1.] For each singular point $\mathfrak{s}_n$, $o(\mathfrak{s}_n)$
is a \ti{partially ordered subset} of the set of sheets of $\Sigma$
over a neighborhood of $\mathfrak{s}_n$.  $o(\mathfrak{s}_n)$ must contain
at least two elements, and if $\fs_n$ is a puncture, $o(\mathfrak{s}_n)$ must contain
\ti{all} of the sheets over a neighborhood of $\fs_n$.

\item[D2.] $\{z_\mu\}$ is a locally finite collection of points on $C'$, called \emph{joints}.

\item[D3.] $\{p_c\}$ is a finite or countable collection of
closed segments (i.e. images of
\emph{embeddings} of $[0,1]$ into $C$), called \ti{walls} or \emph{streets} (depending
which metaphor is more useful in a given context, cf. footnote \ref{fn:wall-street}).
For each orientation
$o$ of the street $p_c$, $p_c$ is labeled with an ordered pair of distinct sheets of the
covering $\Sigma \to C$ over $p_c$.  Reversing the orientation reverses this ordered pair of sheets.
So $p_c$ comes with two labels which we could
write as $(o, ij)$ and $(-o, ji)$.

\end{description}


The data must satisfy the following conditions:

\begin{description}

\item[C1.] The segments $p_c$ cannot cross one another (but they are allowed to
have common tangents).  Each $p_c$ must begin on a branch point or a joint,
and must end on a joint or a singular point.  Any compact subset of $C'$
intersects only finitely many segments.

\item[C2.] Around each branch point $\fb$ there is a neighborhood where $\wnet$
looks like Figure \ref{fig:branch-point-trajectories}.  That is,
each branch point of type $(ij)$ is an endpoint of three
streets which carry labels $(o,ij)$ or $(o,ji)$, and
the streets encountered consecutively traveling around a loop around $\fb$
have oppositely ordered sheets.

\item[C3.] Around each joint $z_\mu$ there is a neighborhood where
$\wnet$ looks like Figure \ref{fig:trajectories-meeting-commuting},
Figure \ref{fig:ijkl-collisions}, or Figure \ref{fig:ijkl-collision-birth}.

\item[C4.] If a segment with label $ij$ ends at a singular point $\mathfrak{s}_n$,
then $i$ and $j$ lie in the ordered subset $o(\mathfrak{s}_n)$,
and with respect to the ordering of $o(\mathfrak{s}_n)$ we have $i < j$.

\end{description}

Our definition of ``spectral network'' is somewhat provisional.
With an eye toward the future let us mention one natural
generalization:  we could have relaxed the requirement that there is at least
one singular point $\fs_n$, and allowed
the segments to be infinite in one direction.  This generalization would be needed
if we want our definition to encompass the networks $\wnet_\vartheta$ in theories $S[\fg, C]$
where the set of defects is actually \ti{empty}.
The resulting spectral networks would be expected to look much more complicated --- e.g.
the streets may well be dense on $C$.  Nevertheless, as we described in the introduction,
we think that it should be possible to extend everything described in this paper to this case.
