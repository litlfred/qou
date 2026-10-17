---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-018-62-k-walls-and-the-degenerate-spectral-networks
section_title: "K-walls and the degenerate spectral networks Wc"
section_number: 6.2
pages: 34-38
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.943
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




\subsection{The jump of $F(\wp, \vartheta)$ at a $\cK$-wall} \label{sec:f-jump}

The jump of $F(\wp, \vartheta)$ at $\vartheta_c$ is given by a certain universal substitution $\cK$ acting on the formal variables $X_a$:
\begin{equation} \label{eq:k-jump}
F(\wp, \vartheta_c^+) = \cK\left(F(\wp, \vartheta_c^-)\right).
\end{equation}
$\cK$ is determined by the degenerate spectral network $\wnet_{\vartheta_c}$.
In this section we describe what $\cK$ is,
deferring the proof of \eqref{eq:k-jump} to \S\ref{sec:k-proof}.

We are going to
combine the soliton degeneracies on any two-way street $p$ into a new generating function $Q(p)$.
Unlike the generating functions $F(\wp, \vartheta)$ we have considered before, $Q(p)$ is
written in terms of formal variables $X_{\tilde \gamma}$
with $\tilde\gamma \in \tilde\Gamma$,
where $\tilde\Gamma = H_1(\tilde\Sigma; \IZ)$ modulo shifts by $2H$ (cf. the definition of
$\tilde\Gamma(\tz_1, \tz_2)$ in \S\ref{sec:tricky-sign}).
So these formal variables are associated to closed paths, rather than the open ones we have
encountered up to now.
We extend our multiplication rules,
\begin{equation}
 X_{\tilde \gamma} X_a = X_{\tilde \gamma + a}, \qquad X_{\tilde \gamma} X_{\tilde \gamma'} = X_{\tilde \gamma + \tilde \gamma'}
\end{equation}
(where the $+$ denotes the obvious action of $\tilde\Gamma$ on $\tilde\Gamma(\tz_1, \tz_2)$ or on $\tilde\Gamma$).
We also extend our sign rules by imposing
\begin{equation}
 X_H = -1,
\end{equation}
so the two $X_{\tilde\gamma}$ corresponding to different lifts of a single $\gamma \in \Gamma$ differ only by a sign.

One can build closed paths from open ones:  given $a \in \tilde \Gamma_{ii}(\tz,\tz)$,
there is a corresponding $\cl(a) \in \tilde \Gamma$ which is obtained just by forgetting the
basepoint $\tz^{(i)}$.
Using this we define
\begin{equation} \label{eq:def-Q}
Q(p) = 1 + \sum_{\bar a \in \Gamma_{ij}^s,\,\bar b \in \Gamma_{ji}^s} \mu^-(a,p) \mu^-(b,p) X_{\cl(a + b)}.
\end{equation}
(We will see later that we would have gotten the same $Q(p)$ if we had used
$\mu^+$ instead of $\mu^-$ on the right.)
$Q(p)$ is a power series in the variables $X_{\tilde\gamma}$, of a constrained sort: every
$\gamma$ that occurs is a sum $\bar a + \bar b$ of charges supported at $z$, and
hence has $e^{- \I \vartheta_c} Z_\gamma \in \R_-$.

Now we make a new genericity assumption.  Let $\Gamma_c \subset \Gamma$ be the set of all $\gamma \in \Gamma$
with $e^{- \I \vartheta_c} Z_\gamma \in \R_-$; we assume
that $\Gamma_c$ is generated by a single element $\gamma_0$.  (This condition holds automatically if our chosen
$u = (\phi_2, \cdots, \phi_K)$ is not on a wall of marginal stability in the
Coulomb branch.)  $Q(p)$ is then a power series in a single variable:
choosing a lift $\tilde\gamma_0$,
each $X_{\cl(a+b)} = \pm X_{\tilde \gamma_0}^n$
for some $n>0$.
Our next aim is to extract the BPS degeneracies by rewriting this power series as a product, \eqref{eq:Q-exp} below.

For each $\gamma \in \Gamma$ we can define a preferred lift $\tilde\gamma$ by the following rule:\footnote{In the first
preprint version of this paper we proposed a different lifting rule based on the principle that the product \eqref{eq:Q-exp}
should be finite.  More recently, in studying more complicated examples,
it has turned out that sometimes this finiteness is violated \cite{glmmn}.  For completeness
we have back-ported the corrected rule from \cite{glmmn} to here.}
represent $\gamma$ as a union of smooth closed curves $c_m$ on $\Sigma$; then $\tilde\gamma$ is the sum of
the canonical lifts of the $c_m$ to $\tilde\Sigma$, shifted by $\left( \sum_{m \le n} \delta_{mn} + \# (c_m \cap c_n) \right) H$
(of course since we work modulo $2H$, all that matters here is whether this sum is odd or even.)
One can check directly that $\tilde\gamma$ so defined is independent of the choice of how we represent $\gamma$
as a union of $c_m$ (this requirement is what forced us to add the tricky-looking shift.)
Moreover, with this definition one has
\begin{equation}
 X_{\tilde\gamma + \tilde\gamma'} = (-1)^{\inprod{\gamma, \gamma'}} X_{\widetilde{\gamma + \gamma'}}.
\end{equation}

We are ready to factorize $Q(p)$:
there exist exponents $\alpha_{\gamma}(p)\in\Z$ such that
\begin{equation} \label{eq:Q-exp}
Q(p) = \prod_{\gamma \in \Gamma_c} (1 - X_{\tilde \gamma})^{\alpha_\gamma(p)}.
\end{equation}
(Indeed, the equations determining the $\alpha_\gamma(p)$ from $Q(p)$ are
upper-triangular and hence can be solved.)
Then, for any $\gamma \in \Gamma_c$, define a 1-chain $L(\gamma)$ on $\Sigma$ by
\begin{equation} \label{eq:def-L}
L(\gamma) = \sum_p \alpha_\gamma(p)\,p_\Sigma,
\end{equation}
where $p$ runs over the walls in $\wnet_{\vartheta_c}$,
and $p_\Sigma$ is the oriented $1$-chain obtained by lifting $p$
as in \S\ref{subsec:4d-BPS-States}.

It is a crucial fact (proven in \S\ref{sec:k-proof}
below) that $L(\gamma)$ so defined is actually a 1-\ti{cycle}.
This allows us to define\footnote{Different representatives
of the class $\bar c$ differ by addition of 1-boundaries, and the 1-cycle $L(\gamma)$ has zero
intersection with any 1-boundary; this would not have worked if $L(\gamma)$ were merely
a 1-chain.}
an intersection number $\inprod{\bar c, L(\gamma)}$ for any $\bar c \in \Gamma(z_1, z_2)$.
Moreover, $e^{-\I \vartheta_c} \int_{p_\Sigma} \lambda \in \R_-$,
so $e^{-\I \vartheta_c} Z_{[L(\gamma)]} \in \R$;
under our genericity assumption this implies that the homology class
$[L(\gamma)]$ is a multiple of $\gamma$ (though not necessarily a positive multiple).
This fact will be useful below.

Finally we can define our universal substitution $\cK$:
\begin{equation} \label{eq:k-def}
 \cK(X_a) = \prod_{\gamma \in \Gamma_c} (1 - X_{\tilde\gamma})^{\inprod{\bar a,L(\gamma)}} X_a.
\end{equation}
