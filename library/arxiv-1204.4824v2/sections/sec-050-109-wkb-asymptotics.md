---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-050-109-wkb-asymptotics
section_title: "WKB asymptotics"
section_number: 10.9
pages: 72-74
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:WKB-Asymptotics}

So far in this section we have been considering the map $\Psi_\wnet$ associated to an arbitrary
spectral network $\wnet$.  These maps have especially interesting asymptotic properties if we choose $\wnet$
to be the particular network $\wnet_\vartheta$ which we studied in the rest of the paper.
In this section we briefly explain this point.  (We will gloss over the role of the twisting in this section,
and use spin structures to pass freely between twisted and untwisted connections.)

Equip $C$ with a complex structure.
Suppose given a $GL(K)$ \ti{Higgs bundle} over $C$, i.e. a triple $(V, \bar\partial, \varphi)$
where $V$ is a complex vector bundle
of rank $K$, $\bar\partial$ a holomorphic structure on $V$,
and $\varphi$ a meromorphic $\End(V)$-valued $1$-form, with poles at the
punctures on $C$.
Let $\Sigma$ be the spectral cover
determined by $\varphi$,
\begin{equation}
\Sigma = \{ \det(\varphi - \lambda) = 0 \} \subset T^* C.
\end{equation}
Now assume that $\Sigma$ is smooth (this is the case for generic $\varphi$.)  Then
we have a corresponding spectral line bundle over $\Sigma$,
\begin{equation}
 \CL = \ker (\varphi - \lambda),
\end{equation}
and the Higgs bundle $(V,\bar\partial,\varphi)$ is the pushforward of $(\CL, \lambda)$.\footnote{The passage from $(V,\bar\partial,\varphi)$ to $\CL$ is
often called abelianization and has been exploited heavily in the study of ``nonabelian theta functions''; see e.g. \cite{MR92b:57008}
where it was introduced, and \cite{dongaits} for a very precise description of the abelianization map
in the more general setting of an arbitrary Lie group $G$.
Abelianization for Higgs bundles is simpler than for flat connections in one important respect:  for
Higgs bundles the monodromy around branch points causes no problem and no spectral network is needed.  There is thus
only \ti{one} abelianization map for Higgs bundles, in contrast to the various $\Psi_\wnet$ we found
in this paper for flat connections.}

Now, given a Higgs bundle there is a corresponding solution of Hitchin's equations \cite{MR89a:32021,MR965220,MR887285,hbnc,wnh}.
In \cite{Gaiotto:2011tf} we proposed a new method for constructing that solution.
The key ingredient is a set of integral equations written in \S 5.6 of \cite{Gaiotto:2011tf}.
The equations are determined by the data of:
\begin{itemize}
 \item the Higgs bundle $(V,\bar\partial,\varphi)$,
 \item the BPS degeneracies $\mu$ and $\omega$, which (as we have explained in \S\S \ref{sec:F-basics},\ref{sec:wnet},\ref{sec:varying-theta}) are computed from the spectral networks $\wnet_\vartheta$ determined by $\Sigma$,
 \item a real parameter $R>0$.
\end{itemize}

These equations are expected to have a unique solution for large enough $R$ (constructed e.g. by iteration).
The solution produces a family of flat connections $\nabla(\zeta)$ in $V$,
together with a family of flat connections $\nabla^\ab(\zeta)$ in $\CL$,
and a family of isomorphisms
\begin{equation}
g(\zeta): \Psi_{\wnet_{\vartheta = \arg \zeta}}(\CL, \nabla^\ab(\zeta)) \to (V, \nabla(\zeta)).
\end{equation}

The integral equations give some control over the analytic structure
and $\zeta \to 0,\infty$ asymptotic behavior of $g(\zeta)$ and $\nabla^{\ab}(\zeta)$.
From this we deduce that the family $\nabla(\zeta)$ is of the form
\begin{equation} \label{eq:hitchin-connection}
 \nabla(\zeta) = R \zeta^{-1} \varphi + D + R \zeta \bar\varphi,
\end{equation}
where $D$ is a connection in $V$, unitary with respect to some Hermitian metric $h$ in $V$ (``harmonic metric''),
and $\bar\varphi$ is the adjoint of $\varphi$ in the metric $h$.
The fact that $\nabla(\zeta)$ is flat for all $\zeta \in \IC^\times$ is equivalent to the statement
that $(V, \varphi, D, \bar\varphi)$
constitute a solution of \ti{Hitchin's equations} on $C$.  (The natural conjecture is that it is the unique
such solution corresponding to the given Higgs bundle $(V, \bar\partial, \varphi)$).
So the integral equations are a machine for producing solutions to Hitchin's equations.

In addition, the integral equations give some more interesting asymptotic information.
This information is most naturally formulated in terms of the objects
\begin{equation}
\cY_a(\zeta) = X_a(\nabla^\ab(\zeta)) \in \Hom(V_{\tz_1}, V_{\tz_2}).
\end{equation}
If we think of $\cY_a(\zeta)$ as a function of $\tz_2$ then it is flat with respect to the connection
$\nabla(\zeta)$, except when $z_2$ meets the network $\wnet_{\vartheta = \arg \zeta}$:  when $z_2$
crosses the $\CS$-walls, $\cY_a(\zeta)$ jumps discontinuously.  Analogous remarks
hold for the dependence of $\cY_a$ on $\tz_1$.
From the integral equations we learn that
the $\zeta \to 0$ asymptotics of $\cY_a(\zeta)$ are given by
\begin{equation}
 \cY_a(\zeta) \sim \exp \left[ \pi \frac{R}{\zeta} Z_{\bar a} \right].
\end{equation}
Indeed, we can say something a bit stronger:
suppose that we define a new section $\cY_a^\vartheta(\zeta)$ by
\ti{analytic continuation} of $\cY_a(\zeta)$ from the
locus $\arg \zeta = \vartheta$.  In this case, we have the asymptotics
\begin{equation} \label{eq:ya-halfplane}
\cY_a^\vartheta(\zeta) \sim \exp \left[ \pi \frac{R}{\zeta} Z_{\bar a} \right],
\end{equation}
so long as $\zeta \to 0$ while remaining in the half-plane ${\mathbb H}_\vartheta$ centered on the ray $\arg \zeta = \vartheta$.
This is rather sharp asymptotic information about the flat sections of the family of flat connections
$\nabla(\zeta)$.

Our way of describing this asymptotic information is perhaps a bit unfamiliar, so let us relate it to
something better known:  the WKB analysis of 1-parameter families of differential equations.
The flatness equation $\nabla(\zeta)s=0$ takes the general form
\begin{equation}
\left[ \zeta \frac{\de}{\de z} + (R \varphi + \zeta(\cdots)) \right] s = 0.
\end{equation}
The WKB analysis of this equation involves studying formal solutions of the form
\begin{equation} \label{eq:psi-formal}
s^{(i)}_\formal(\zeta) = \exp\left[ \frac{1}{\zeta} \sum_{n=0}^\infty S_n^{(i)} \zeta^n \right] \sum_{n=0}^\infty T^{(i)}_n \zeta^n
\end{equation}
where each $S^{(i)}_n$ is a function and $T^{(i)}_n$ is a section of $V$.
One important difficulty in the WKB method is that these solutions really are only formal:  the series \eqref{eq:psi-formal}
typically has zero radius of convergence.  So one should interpret \eqref{eq:psi-formal} as an asymptotic series.
It is then natural to ask,
are there actual $\nabla(\zeta)$-flat sections $s^{(i)}(\zeta)$ which have these asymptotics?

Our discussion in this section provides the answer:  such sections do indeed exist, in the
following sense.
Fix a phase $\vartheta$, a basepoint $\tz_1 \in \tilde C'_{\wnet_\vartheta}$,
and basis vectors $e^{(i)} \in \CL_{\tz_1}^{(i)}$.  Then
letting $\tilde\wp$ be a path in $\tilde C'_{\wnet_\vartheta}$ from $\tz_1$ to $\tz$, we can define
\begin{equation}
s^{(i)}(\zeta) = e^{(i)} \cY^\vartheta_{\tilde\wp^{(i)}}(\zeta).
\end{equation}
$s^{(i)}(\zeta)$ is a solution of $\nabla(\zeta) s^{(i)}(\zeta) = 0$, and
\eqref{eq:ya-halfplane} implies that $s^{(i)}$ indeed has an asymptotic expansion of the form \eqref{eq:psi-formal},
as $\zeta \to 0$ in the half-plane ${\mathbb H}_\vartheta$.
So, in each connected component of $\tilde C'_{\wnet_\vartheta}$, we have a basis of
$\nabla(\zeta)$-flat sections which have the asymptotics predicted by WKB,
as $\zeta \to 0$ in ${\mathbb H}_\vartheta$.  As we move from one component of $\tilde C'_{\wnet_\vartheta}$ to another,
these bases change.  Thus the walls of $\wnet_\vartheta$ have an interpretation as
Stokes lines.

Finally, we should say that some of the structures which appeared in this paper
have appeared before in the WKB literature (although we arrived at them independently.)  In the case $K=2$,
our constructions here and in \cite{Gaiotto:2009hg}
seem to be closely related to a line of development pursued by Voros and others
(e.g. \cite{Bender1969,Zinn-Justin1984,MR729194,MR1209700}).  For
$K>2$, the phenomenon that new Stokes lines can be born at intersections between old ones was apparently first noticed in
\cite{berk:988}, and has been followed up in a few works since then; we note in particular the reference
\cite{MR2132714}, which contains examples of Stokes diagrams
in the case $K=3$ which look identical to our $\wnet_\vartheta$.  What we have here called \ti{joints} are there called
\ti{virtual turning points}.  There are also results of Simpson on asymptotics
of monodromy which seem likely to be related to ours, e.g. \cite{simpson-agci,MR1166192}.  We have not understood
the precise relation.
