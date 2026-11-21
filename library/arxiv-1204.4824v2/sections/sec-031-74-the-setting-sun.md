---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-031-74-the-setting-sun
section_title: "The setting sun"
section_number: 7.4
pages: 46-48
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:setting-sun}

Next we briefly consider a more complicated example, in which several overlapping finite webs
appear simultaneously.
Unlike the previous examples, we just draw the degenerate network of interest, and not the nondegenerate ones
at nearby phases (which would be terribly cluttered in this example).  See Figure \ref{fig:setting-sun}.
\insfig{setting-sun}{The ``setting sun'':  a picture which could occur as part of a degenerate spectral network
at some $\vartheta = \vartheta_c$.  We show the two-way streets slightly resolved, with the ``American resolution'',
which would occur in the limit $\vartheta \to \vartheta_c^-$.  Each street supports the charges indicated as
well as their shifts by positive multiples of $\gamma = \cl(\bar a + \bar b + \bar c)$.}

Label the three two-way streets in this figure as $p^1$, $p^2$, $p^3$ from top to bottom.  Using the rules of
Appendix \ref{app:joint-rules}, we can directly compute the soliton degeneracies $\mu(\cdot, \cdot)$
on all the streets in the figure.  The nonzero degeneracies on $p^1$, $p^2$, $p^3$ come out to
\begin{align}
 \mu (b, p^1) = 1, & \quad \mu(c + a + n (b + c + a), p^1) = 1 \text{ for } n \ge 0, \\
 \mu (c, p^2) = 1, & \quad \mu(a+b, p^2) = 1, \\
 \mu (a + n (b + c + a), p^3) = 1 \text{ for } n \ge 0, & \quad \mu(b+c, p^3) = 1.
\end{align}
(All other streets turn out to be one-way, as anticipated in Figure \ref{fig:setting-sun}, and so do not contribute to $L$ below.)
Define $\gamma = \cl(\bar a + \bar b + \bar c)$, and let $\tilde\gamma$ be its preferred lift.
Plugging into \eqref{eq:def-Q} and keeping careful track of windings, we find
\begin{align}
 Q(p^1) = Q(p^3) &= (1 - X_{\tilde \gamma})^{-1}, \\
 Q(p^2) &= 1 - X_{\tilde \gamma}.
\end{align}
This gives
\begin{equation}
 L(\gamma) = -p^1_\Sigma - p^3_\Sigma + p^2_\Sigma.
\end{equation}
This class is homologically trivial, $[L(\gamma)] = 0$.  (It could hardly be otherwise,
since the projection of $L(\gamma)$ to $C$ lies in a contractible region containing no branch points, which means
$L(\gamma)$ itself lies in the disjoint union of three contractible open sets on $\Sigma$.)
So in particular this degenerate network does not contribute to the 4d BPS spectrum:
\begin{equation} \label{eq:zero-contrib}
 \Omega(\gamma) = 0.
\end{equation}
Nevertheless the enhanced degeneracies $\omega(\gamma, \cdot)$ are certainly \ti{not} zero in this example:
they are given as usual by \eqref{eq:result-omega}.

\insfigscaled{two-finite-webs}{0.21}{Three finite webs, belonging to a 1-parameter family of finite webs
parameterized by an interval:
as we move along the interval, the ``bubble'' in the middle of the web expands from zero size (left) to a finite maximum size (right).}

How should we understand the result \eqref{eq:zero-contrib}?  First note that
there is a 1-parameter family of finite BPS webs here, parameterized by an interval,
as indicated in Figure \ref{fig:two-finite-webs}.  The two ends of the family are built from the $\cS$-walls appearing in
the degenerate network $\wnet_{\vartheta_c}$, while the other finite webs involve a ``bubble'' made out of
BPS strings which are not
$\cS$-walls.  This is the same phenomenon we had in \S\ref{sec:closed-loops} above, where we considered a cylinder swept out
by BPS strings; the boundaries of the cylinder were $\cS$-walls, but the generic BPS strings inside the cylinder were not.

In the present case
one end of the family (at left) looks like the ``three-string web'' we encountered in \S\ref{sec:three-string}
above.  If this three-string web occurred
in isolation it would give rise to a BPS hypermultiplet, with $\Omega(\gamma) = +1$.  However, when it sits in this
1-parameter family its contribution cannot be evaluated in isolation:  rather we must quantize the whole family at once.
What we have seen is that the contribution to $\Omega(\gamma)$ from this family vanishes.
