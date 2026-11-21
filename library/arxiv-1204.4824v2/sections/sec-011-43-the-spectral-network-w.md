---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-011-43-the-spectral-network-w
section_title: "The spectral network W"
section_number: 4.3
pages: 20-23
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:spectral-network}

Our next aim is to explain how $F(\wp,\vartheta)$ can actually be computed.
As it turns out, the answer depends crucially
on how $\wp$ meets a certain codimension-1 locus
$\wnet_\vartheta \subset C$, which we call a \ti{spectral network}.

We say that a point $z \in C$
\ti{supports} those charges $\bar a \in \Gamma(z,z)$ for which $Z_{\bar a}(z) / e^{\I \vartheta} \in \R_-$.
Define $\wnet_\vartheta$ to be the set of $z \in C$ such
that $z$ supports some $\bar a \in \Gamma(z,z)$ with $\mu(a) \neq 0$ (for either lift $a$ of $\bar a$).

$\wnet_\vartheta$ is a codimension-$1$ network on $C$, the union of
segments which we call \ti{$\cS$-walls}.
The $\cS$-walls can end at branch points or at special points which we call \emph{joints},
and can also asymptote to the punctures of $C$.  We will assume that along any $\cS$-wall, a generic point
supports exactly one charge $\bar a$.

There are two ways in which this
genericity could be violated.  One is for $\vartheta$ to be non-generic:  in that case some $\cS$-walls will support
both a charge $\bar a \in \Gamma_{ij}(z,z)$ and a charge $\bar b \in \Gamma_{ji}(z,z)$.  This phenomenon is crucial for our
story and will be analyzed in \S\ref{sec:varying-theta}.  For now, however, we are assuming $\vartheta$ generic, so we explicitly exclude this
possibility.  The second way in which genericity could be violated is less common:  it might happen accidentally that
e.g. $\lambda_i - \lambda_j = \lambda_k - \lambda_l$ on a whole patch of $C$.
In this case a single wall could support both a charge
$\bar a \in \Gamma_{ij}(z,z)$ and $\bar b \in \Gamma_{kl}(z,z)$.  If $i,j,k,l$ are all distinct, all
our discussion in this section has a straightforward
extension to that case; if they are not all distinct the situation is more subtle.  In any case,
from now on we assume that a
generic point along an $\cS$-wall supports exactly one charge $\bar a$.

In this case, all points of any single $\cS$-wall support ``the same'' charge $\bar a$, in the sense that if
$z$, $z'$ are generic points on a common wall, the natural parallel transport along the wall
takes the charge $\bar a \in \Gamma(z,z)$ supported at $z$
into the charge $\bar a' \in \Gamma(z',z')$ supported at $z'$.
If we choose a charge $a \in \tGamma(\tz,\tz)$ lifting $\bar a$ as discussed in \S\ref{sec:tricky-sign},
then the parallel transport also takes $a$ to an $a' \in \tGamma(\tz',\tz')$ lifting $\bar a'$.

Now recall the soliton degeneracies $\mu(a) \in \Z$, which are
defined for any $a \in \tGamma(\tz,\tz)$, so long as
$z \in C$ does not lie on a wall of marginal stability.\footnote{To reduce potential confusion we
emphasize that the walls of marginal stability are \ti{not} the same thing as the $\cS$-walls.}
$\mu(a)$ does not depend on the parameter $\vartheta$, and its definition does not involve the spectral network $\wnet_{\vartheta}$.
In our computation of $F(\wp, \vartheta)$ below, though, we will find that the $\mu(a)$
which are really important are the ones where $\bar a \in \Gamma(z,z)$ is supported at $z$ ---
or said otherwise, we will be mainly interested in evaluating $\mu(a)$ \ti{along the $\cS$-walls supporting $\bar a$.}
We will also find below that $\mu(a)$ is \ti{constant} along each $\cS$-wall supporting $\bar a$;
with this in mind we immediately simplify our notation by letting $\mu(a,p)$ denote the constant value of $\mu(a)$ along
a wall $p$ supporting $\bar a$.



\subsection{Computing $F(\wp,\vartheta)$}\label{subsec:Compute-FP}

Now we can describe how $F(\wp,\vartheta)$ is computed.
The recipe we will summarize here follows from the 2d-4d wall-crossing formula
of \cite{Gaiotto:2011tf}.

The simplest situation occurs when $\wp$ does not cross $\wnet_\vartheta$ anywhere.  Define
\begin{equation}
 \cD(\wp) = \sum_{i=1}^K X_{\wp^{(i)}},
\end{equation}
where the $\wp^{(i)}$ are the canonical lifts of $\wp$ to the $K$ sheets of $\tilde\Sigma$.
Then if $\wp \cap \wnet_\vartheta = \emptyset$ we have simply
\begin{equation}\label{eq:TrivPar}
F(\wp,\vartheta) = \CD(\wp).
\end{equation}
In other words, interfaces corresponding to short enough paths $\wp$ on $C$
just support $K$ framed BPS states, one for each vacuum of the surface operator.

The more interesting question is how to compute $F(\wp)$ if $\wp$ does cross $\wnet_\vartheta$.
Because of the composition property \eqref{eq:composition}, it is enough to
answer this question in the case where $\wp$ crosses $\wnet_\vartheta$ exactly once.

So suppose $\wp$ crosses $\wnet_\vartheta$ at a point $z$ supporting
a charge $\bar a \in \Gamma_{ij}(z,z)$.  In this case $\wp$ is divided into two subpaths
$\wp_+$ and $\wp_-$, which we deform slightly to obtain $\wp'_+$ and $\wp'_-$
as shown in Figure \ref{fig:p-crossing-s-wall}.
\insfigscaled{p-crossing-s-wall}{0.4}{A path $\wp$ crossing an $\cS$-wall is locally divided into two pieces
$\wp_\pm$.  We deform $\wp_\pm$ slightly to paths $\wp'_\pm$, so that the final tangent vector of $\wp'_+$ and the initial tangent vector
of $\wp'_-$ point along the $\cS$-wall, in opposite directions.  The paths $\wp'_\pm$ are shown
slightly displaced from the wall for clarity.}
Then we have\footnote{The factor $\mu(a) X_a$
appearing in \eqref{eq:S-factor}
is independent of the choice of lift $a$ of $\bar{a}$, because of \eqref{eq:mu-sign-rule}, \eqref{eq:winding-rule-2}.}
\begin{equation} \label{eq:S-factor}
 F(\wp, \vartheta) = \cD(\wp) + \cD(\wp'_+) (\mu(a) X_a) \cD(\wp'_-).
\end{equation}
The second term is the interesting one:  it says that when $\wp$ crosses $\wnet_\vartheta$, $F(\wp, \vartheta)$ includes paths which
are segments of lifts of $\wp$ combined with ``detours'' along the lifts of
BPS solitons.  (The point of our deformation from $\wp_\pm$ to $\wp'_\pm$ here was to arrange that the second term makes sense, i.e. that $\cD(\wp'_+)$ and $\cD(\wp'_-)$ can be
concatenated with the soliton charge $a$.)

For later convenience, we introduce a second notation for \eqref{eq:S-factor}.  Let $\tz$
denote the tangent vector to $\wp$ at $z$.  Let $t_1$ be the shortest arc running from
$\tz$ to the initial point of $a$, in the fiber of $\tilde\Sigma$ over $z$. Similarly,  let $t_2$
be the shortest arc running from the final point of $a$ to $\tz$, in the fiber of
$\tilde\Sigma$ over $z$; and define
\begin{equation}\label{eq:aztil-def}
a_{\tilde z} = t_1 + a + t_2.
\end{equation}
Note that $t_1,t_2$ are well-defined because the intersection of $\wp$ and $\wnet_{\vartheta}$
is assumed to be transverse.
With this definition  \eqref{eq:S-factor} can be rewritten as
\begin{equation} \label{eq:S-factor-simple}
 F(\wp, \vartheta) = \cD(\wp_+) (1 + \mu(a) X_{a_{\tilde z}}) \cD(\wp_-).
\end{equation}

The formula \eqref{eq:S-factor-simple}
can be interpreted as a kind of wall-crossing formula for the framed 2d-4d BPS spectrum:
it implies that when an endpoint of the path $\wp$ is moved across an $\cS$-wall,
$F(\wp, \vartheta)$ jumps by multiplication with a factor $(1 + \mu(a) X_{a_{\tilde z}})$.
This is the way that this formula appeared in \cite{Gaiotto:2011tf}.
