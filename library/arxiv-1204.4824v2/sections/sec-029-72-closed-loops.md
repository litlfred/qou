---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-029-72-closed-loops
section_title: "Closed loops"
section_number: 7.2
pages: 43-45
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:closed-loops}

\insfigscaled{closed-trajectories}{0.45}{A more complicated way in which $\cS$-walls can collide head-on.  At $\vartheta < \vartheta_c$,
the $\cS$-wall supporting charge $a$
winds once clockwise around the cylinder and then disappears
toward the bottom, while the $\cS$-wall supporting charge $b$ winds many times counterclockwise
around the cylinder and eventually disappears toward the top.  In the figure, for clarity we truncate the
latter $\cS$-wall after it has wound around a few times.
At the critical $\vartheta = \vartheta_c$,
all of the windings of the $\cS$-wall supporting charge $b$
coalesce onto a single closed trajectory.  At $\vartheta > \vartheta_c$ these two $\cS$-walls exchange roles.}

A more interesting possibility is shown in Figure \ref{fig:closed-trajectories}.  This case involves
an $\cS$-wall which winds around a cylinder in $C$ many times, more and more tightly as
$\vartheta \to \vartheta_c$.  In this case two two-way streets appear simultaneously at
$\vartheta = \vartheta_c$; let $p$ denote one of them.
$p$ begins and ends at the \ti{same} branch point, and the soliton degeneracies
are a bit more interesting than the previous case:  there are infinitely many
nonvanishing $\mu^-(\cdot)$,
coming from the infinite set of windings of the $\cS$-wall around the cylinder, which have all
coalesced onto $p$.  Explicitly
\begin{equation}
 \mu^-(a) = 1, \qquad \mu^-(b + n(a+b)) = 1 \text{ for all } n \ge 0,
\end{equation}
with all other $\mu^-(\cdot)$ vanishing.
Hence by \eqref{eq:def-Q},
\begin{align}
Q(p) &= 1 + X_{\cl(a+b)} + X_{\cl(2(a+b))} + \cdots \\
&= (1 - X_{\cl(a+b)})^{-1}.
\end{align}
Define $\gamma = \cl(\bar a + \bar b)$.
The preferred lift of $\gamma$ is $\tilde\gamma = \cl(a+b)$, so we have
$Q(p) = (1 - X_{\tilde\gamma})^{-1}$, which means $\alpha_\gamma(p) = -1$.
Now, to compute $L(\gamma)$ we must sum the contributions from both two-way streets ---
call them $p^1$ and $p^2$ --- so we obtain
\begin{equation}
 L(\gamma) = - p^1_\Sigma - p^2_\Sigma.
\end{equation}

Both $p^1_\Sigma$ and $p^2_\Sigma$ are in the homology class $\gamma$,
so $[L(\gamma)] = -2\gamma$, or
\begin{equation}
\Omega(\gamma) = -2.
\end{equation}
Thus we have recovered the result
of \cite{Klemm:1996bj,Gaiotto:2009hg}:  this pair of closed trajectories
represents a BPS vectormultiplet.

In \cite{Gaiotto:2009hg} we derived the result $\Omega(\gamma) = -2$ in
this situation (in the special case $K=2$),
by a rather delicate analysis of the jumps of the vacuum expectation
values of line defects associated to \ti{closed} paths.
This analysis gave the right answer but depended on the assumption that
at $\vartheta = \vartheta_c$ the third trajectory emerging from the branch points in Figure \ref{fig:closed-trajectories}
ends on a puncture. As
Ivan Smith pointed out to us, this assumption can be violated for higher genus $C$:  the cylinder
of closed trajectories could be dividing $C$ into two pieces, one of which contains no puncture.
Our present analysis using line defects associated to \ti{open} paths is much simpler and is free of such extra assumptions.

Incidentally, from the point of view of the theory $S[\fg, C, D]$
these two closed trajectories would not seem to be the whole story.  Indeed, these two
$ij$-trajectories are actually the two ends of a one-parameter \ti{family} of closed
$ij$-trajectories, which sweep out a cylinder on $C$.  Any member of this family is
a BPS string.  So physically speaking we should regard this $\Omega(\gamma) = -2$ as giving
the contribution from this whole one-parameter family, not just from the two ends of the family.
From our current point of view though, the ends play a privileged role, in
that they are $\CS$-walls, while the trajectories in the interior of the cylinder are not.

Finally, although we have hidden it up to this point, the behavior of the networks
$\wnet_\vartheta$ as $\vartheta \to \vartheta_c$ is actually rather complicated.  In Figure
\ref{fig:closed-trajectories}, at $\vartheta < \vartheta_c$, we see two $\cS$-walls which wind
many times around the cylinder.  There we truncated them at some finite distance in order not
to make the figure too confusing.  In Figure \ref{fig:cylinder-colored} we show the full $\cS$-walls
at some particular $\vartheta < \vartheta_c$.  Note that the two winding $\cS$-walls thread
past one another many times before they escape the cylinder.  As we vary
$\vartheta$ slightly, the angle at which they are threaded changes, and there are infinitely many
critical phases $\vartheta_n$ at which they actually collide head-to-head.  The critical phases
$\vartheta_n$ accumulate at the value $\vartheta_c$.  At each of these
critical phases we have a saddle connection and the network $\wnet_\vartheta$ jumps,
just as we discussed in \S\ref{sec:saddle-connection}.
\insfigscaled{cylinder-colored}{0.45}{Another picture of the $\CS$-walls on the cylinder for $\vartheta$
near the critical phase $\vartheta_c$.  Here we do \ti{not} truncate the walls, and we distinguish
different walls by giving them different colors.}
We analyzed this limiting process rather closely in \cite{Gaiotto:2009hg}; but we emphasize
that in our current analysis, if all we want to know is the BPS degeneracy $\Omega(\gamma)$ which
appears exactly at the critical phase $\vartheta_c$,
it is \ti{not} necessary to study this infinite sequence of jumps.
