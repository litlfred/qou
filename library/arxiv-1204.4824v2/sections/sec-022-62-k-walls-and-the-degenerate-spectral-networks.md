---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-022-62-k-walls-and-the-degenerate-spectral-networks
section_title: "K-walls and the degenerate spectral networks Wc"
section_number: 6.2
pages: 34-36
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.889
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:K-walls}

There is also a second, more interesting kind of jump which can occur at a critical phase
$\vartheta = \vartheta_c$.  In contrast to the previous case, these jumps do not arise because of
a change in the interaction between $\wnet_\vartheta$ and $\wp$.  Rather, they arise because of
a topology change in $\wnet_\vartheta$ itself.

\insfigscaled{near-branch-point}{0.18}{The behavior of $ij$-trajectories
approaching a branch point of type $(ij)$.}
The claim that a topology change in $\wnet_\vartheta$
could occur as we continuously vary $\vartheta$ might at
first seem strange.  After all, we have given a recipe for $\wnet_\vartheta$ in \S\ref{sec:wnet},
$\vartheta$ enters this recipe only
through the differential equation \eqref{eq:trajectory-de}, and this equation
evidently depends continuously on $\vartheta$.
The point is that the \ti{solutions} of \eqref{eq:trajectory-de}
can nevertheless exhibit discontinuous behavior,
because of the phenomenon of bifurcation near the branch points:  $ij$- or $ji$-trajectories coming close to
an $(ij)$ branch point can veer off in one of two directions, as indicated in Figure \ref{fig:near-branch-point}.
This figure can be considered to depict either a foliation of $C$ by $ij$-trajectories at fixed $\vartheta$
or the evolution of an $\cS$-wall in $\wnet_\vartheta$ as $\vartheta$ varies. From the latter
viewpoint it follows that the critical phases $\vartheta_c$ are those
at which some $\cS$-wall of type $ij$ or $ji$ runs directly into a branch point of type $(ij)$.
We call the $\vartheta_c$ where this occurs \ti{$\cK$-walls}.
A simple example is shown in Figure \ref{fig:wnet-jump}.

\insfigscaled{wnet-jump}{0.41}{The simplest way in which $\wnet_\vartheta$ can jump at a $\cK$-wall.
As $\vartheta \to \vartheta_c$, two $\cS$-walls merge into a single two-way street
running between two branch points.  The two-way street supports two distinct charges $\bar a$, $\bar b$.}

To describe the relation between $F(\wp, \vartheta_c^+)$ and $F(\wp, \vartheta_c^-)$,
it is convenient to work directly with the limiting spectral network $\wnet_{\vartheta_c}$.
This limiting network has some features not seen for the generic $\wnet_\vartheta$.
In particular, several (possibly infinitely many) $\cS$-walls, supporting different
charges, might coalesce into a single segment as $\vartheta \to \vartheta_c$; hence a wall
$p$ of $\wnet_{\vartheta_c}$ might support several distinct charges.
Moreover, the $\cS$-walls coalescing onto $p$
might not all be oriented in the same direction; in this case we call $p$ a \ti{two-way street}.\footnote{We now
have two metaphors for the segments in
a spectral network.  They are \emph{walls} because they are the loci
where framed 2d-4d BPS degeneracies jump.  On the other hand
we will find that the metaphor of \emph{streets} is also very useful when tracking
the solitons.  Rather than insisting on one term, we will use them as synonyms.
We feel no inclination to go to wall-street.\label{fn:wall-street}}
Again see Figure \ref{fig:wnet-jump} for an example:  the saddle connection in the middle
of the figure is a two-way street.  Indeed, $\wnet_{\vartheta_c}$ always contains
at least one two-way street, since we get a two-way street whenever an $\cS$-wall
runs into a branch point.

\insfigscaled{crossing-two-way}{0.45}{A path $\wp$ crossing a pair of nearly coincident
$\cS$-walls, which coalesce into a two-way street at $\vartheta = \vartheta_c$.}
Now let us consider a path $\wp$ which crosses a two-way street $p$.  A representative picture of the situation
when $\vartheta$ is near $\vartheta_c$ is indicated in Figure \ref{fig:crossing-two-way}.\footnote{In general the
picture might be a bit more complicated than Figure \ref{fig:crossing-two-way}, because there might be several walls
of type $ij$ and/or of type $ji$ which all coalesce at $\vartheta = \vartheta_c$.
An example appears in Figure \ref{fig:closed-trajectories} below.}
We define BPS soliton degeneracies $\mu^\pm(a,p)$ along the
walls of $\wnet_{\vartheta_c}$ by taking limits of $\mu(a,p)$
as $\vartheta \to \vartheta_c^\pm$.
Applying the rules of \S\ref{subsec:Compute-FP} and taking the limit $\vartheta \to \vartheta_c^\pm$,
we obtain formulas for $F(\wp, \vartheta_c^\pm)$:
\begin{align}
 F(\wp, \vartheta_c^-) &= \cD(\wp_+)
 \left(1 + \sum_{\bar b \in \Gamma^s_{ij}} \mu^-(b) X_{b_{\tilde z}}\right)
 \left(1 + \sum_{\bar a \in \Gamma^s_{ji}} \mu^-(a) X_{a_{\tilde z}}\right) \cD(\wp_-),\label{eq:two-way-crossing-2} \\
 F(\wp, \vartheta_c^+) &= \cD(\wp_+)
 \left(1 + \sum_{\bar a \in \Gamma^s_{ji}} \mu^+(a) X_{a_{\tilde z}}\right)
 \left(1 + \sum_{\bar b \in \Gamma^s_{ij}} \mu^+(b) X_{b_{\tilde z}}\right) \cD(\wp_-).\label{eq:two-way-crossing-1}
\end{align}
Here $\Gamma^s_{ij} \subset \Gamma_{ij}(z,z)$ denotes the set of charges supported along the two-way street.

Note that the order in these products really matters, since $X_{a_{\tilde z}}$ and $X_{b_{\tilde z}}$ do not
commute.
A convenient way to think about this is to regard the limiting network
$\wnet_{\vartheta_c}$ as equipped with a bit of extra structure:  each two-way street is
resolved into two infinitesimally separated and oppositely oriented ``lanes''.
For $\vartheta_c^-$ the division of lanes is according to the American rule (drive on the right),
while for $\vartheta_c^+$ it is according to the British rule (drive on the left).
We can determine $F(\wp, \vartheta_c^\pm)$ completely
from $\wnet_{\vartheta_c}$ and $\mu^\pm$,
using either \eqref{eq:two-way-crossing-2} or \eqref{eq:two-way-crossing-1} as appropriate.
