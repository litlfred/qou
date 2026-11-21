---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-018-56-homotopy-invariance
section_title: "Homotopy invariance"
section_number: 5.6
pages: 30-32
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.851
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:homotopy-invariance}

Now let us consider a key consistency check of our story so far.
We have claimed on general physical grounds that $F(\wp, \vartheta)$ should be
a homotopy invariant of $\wp$, or more precisely a twisted homotopy invariant as
described in \S\ref{sec:tricky-sign}.
On the other hand, we have also given a recipe which completely determines $F(\wp, \vartheta)$.
So we can ask whether this recipe indeed obeys the necessary twisted homotopy invariance.

To check this twisted homotopy invariance it is enough to check the invariance under a few
elementary moves, which we now consider in turn.
This is the first place where the tricky
minus signs mentioned in \S\ref{sec:tricky-sign} play a decisive role.

First, consider a pair of paths $\wp$ and $\wp'$, neither of which meets any $\cS$-walls, and
which are not only homotopic but related by a \ti{regular}
homotopy, i.e. a homotopy through immersions.
In this case the constraint of twisted homotopy invariance requires that
\begin{equation}
 F(\wp, \vartheta) = F(\wp', \vartheta).
\end{equation}
But since neither path meets any $\cS$-walls, this reduces to
\begin{equation}
 \cD(\wp) = \cD(\wp'),
\end{equation}
which is indeed true:  the regular homotopy of $\wp$ to $\wp'$ lifts to
a regular homotopy of each $\wp^{(i)}$ to $\wp'^{(i)}$.

\insfig{collapsing-loop}{A pair of paths that are homotopic but differ by a unit of winding.}
Next, consider the pair of paths in Figure \ref{fig:collapsing-loop}.
In this case the constraint of twisted homotopy invariance requires that
\begin{equation}
 F(\wp, \vartheta) = - F(\wp', \vartheta).
\end{equation}
But neither of these paths meets any $\cS$-walls, so this reduces to
\begin{equation}
 \cD(\wp) = - \cD(\wp'),
\end{equation}
which indeed follows by lifting the homotopy of $\wp$ to $\wp'$ to
homotopies of $\wp^{(i)}$ to $\wp'^{(i)}$ and using \eqref{eq:winding-rule-2}.
We stress that this is a non-regular homotopy, which accounts for the sign change.

Next, consider two paths $\wp$, $\wp'$ which differ by homotopy across an $\cS$-wall as
shown in Figure \ref{fig:s-wall-homotopy}.
\insfigscaled{s-wall-homotopy}{0.36}{Two open paths $\wp$, $\wp'$ which differ by a homotopy across an $\cS$-wall.}
The constraint of twisted homotopy invariance says
\begin{equation} \label{eq:hom-inv-s}
F(\wp, \vartheta) = F(\wp', \vartheta).
\end{equation}
Let $\bar{a}$ be the charge supported on the $\cS$-wall in the figure.
The two intersections $z_\pm$ between $\wp'$ and the wall divide $\wp'$ into $\wp'_+ \wp'_0 \wp'_-$;
let $\tz_\pm$ be the tangent vectors to $\wp'$ at the intersection points.
Then evaluating both sides directly, letting $a$ be the charge supported along the wall,
and using the fact that $\mu(a)$ is constant along the wall,
\eqref{eq:hom-inv-s} becomes
\begin{align}\label{eq:homotop-check}
 \cD(\wp) &= \cD(\wp'_+) (1 + \mu(a) X_{a_{\tz_+}}) \cD(\wp'_0) (1 + \mu(a) X_{a_{\tz_-}}) \cD(\wp'_-) \nonumber \\
&= \cD(\wp') + \mu(a) \cdot \cD(\wp'_+) \left(X_{a_{\tz_+}} \cD(\wp'_0) + \cD(\wp'_0) X_{a_{\tz_-}}\right) D(\wp'_-) \\ & \qquad + \mu(a)^2 \cD(\wp'_+) X_{a_{\tz_+}}\cD(\wp'_0)X_{a_{\tz_-}} \cD(\wp'_-). \nonumber
\end{align}
The two soliton paths $a_{\tz_+}$ and $a_{\tz_-}$
are both of type $ij$, so $X_{a_{\tz_+}}\cD(\wp'_0)X_{a_{\tz_-}} = 0$.
Using the definition \eqref{eq:aztil-def} one can check that
the two terms in the parentheses correspond to paths which differ by one
unit of winding; according to the rule \eqref{eq:winding-rule-2},
these two terms thus differ by a minus sign,
and so cancel one another.
Thus \eqref{eq:homotop-check} reduces to
\begin{equation}
 \cD(\wp) = \cD(\wp')
\end{equation}
which is indeed true since the obvious homotopy of $\wp$ into $\wp'$ also gives homotopies between each
$\wp^{(i)}$ and $\wp'^{(i)}$.  Note that this would not have worked out without using the fact that $\mu(a)$ is constant
along the wall:  indeed this shows that homotopy invariance requires $\mu(a)$ to be constant along walls, thus making good
on a promise we made in \S\ref{sec:spectral-network}.

Next, consider two paths $\wp$, $\wp'$ which differ by homotopy across a joint,
as in Figure \ref{fig:trajectories-meeting-commuting} or Figure \ref{fig:ijkl-collisions}.
We have already verified in \S\ref{sec:wnet-basics} that in this case $F(\wp, \vartheta) = F(\wp', \vartheta)$:  indeed we used this constraint as part of our system for determining
$\mu$.

\insfig{branch-point-loop}{Two paths which differ by homotopy across a branch point.}
Finally we reach the most interesting case.  Consider two paths $\wp$, $\wp'$ which
differ by homotopy across a branch point, as shown in Figure \ref{fig:branch-point-loop}.
The constraint of twisted homotopy invariance says
\begin{equation} \label{eq:hom-inv-bp}
F(\wp, \vartheta) = F(\wp', \vartheta).
\end{equation}
Evaluating both sides of \eqref{eq:hom-inv-bp}, we obtain the explicit sums of paths shown in Figure
\ref{fig:branch-point-monodromy}.  Naively we
see $K+3$ terms in $F(\wp, \vartheta)$
and $K+1$ in $F(\wp', \vartheta)$.
The last two terms in $F(\wp,\vartheta)$, running from sheet $j$ to sheet $j$,
are of the form $X_a + X_{a'}$, where
$a$, $a'$ both project to the same charge $\bar a$, but differ by one unit of winding.
These two terms thus cancel one another thanks to our sign rule
\eqref{eq:winding-rule-2}.
The other $K+1$ terms precisely match the $K+1$ terms in $F(\wp', \vartheta)$.
\insfigscaled{branch-point-monodromy}{0.19}{The explicit sums of paths which occur in \eqref{eq:hom-inv-bp}.  In
the equations shown in the figure, we represent the formal variable $X_a$ by an explicit
picture of a smooth path on $\Sigma$, whose canonical lift to $\tilde\Sigma$ represents the relative
homology class $a$.  The labels next to path segments show which sheet of the covering $\Sigma \to C$
the segments are on.  We have labeled the sheets in the same way as we did in Figure \ref{fig:branch-point-trajectories}.}  So the constraint \eqref{eq:hom-inv-bp} is indeed satisfied.

As an aside, note that this last
constraint would \ti{not} have worked out if there were no $\cS$-walls emerging from the branch point:  in other words, homotopy invariance of the framed 2d-4d BPS spectrum
really \ti{requires} that spectrum to undergo wall-crossing.  This is closely analogous to the
considerations of monodromy invariance that led Seiberg and Witten
to discover wall-crossing in the pure 4d BPS spectrum \cite{Seiberg:1994rs}.
The constraint of monodromy invariance
also would not have worked out if we had taken $\mu = -1$ instead of $\mu = +1$
in \eqref{eq:mu-near-bp}.
