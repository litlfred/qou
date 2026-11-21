---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-015-53-the-mass-filtration-w-and-for-small
section_title: "The mass filtration; W[] and [] for small"
section_number: 5.3
pages: 25-27
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:determining-wnet}

We begin with the observation that
$\wnet_\vartheta$ carries a useful filtration.  Namely, for any $\Lambda > 0$ (with dimensions
of mass), we can define a new object $\wnet_\vartheta[\Lambda]$ by truncating all the $\cS$-walls:
for a wall $w$ supporting a charge $\bar a$,
$\wnet_\vartheta[\Lambda]$ includes only the portion of $w$ with $\abs{Z_{\bar a}} < \Lambda$.
So
\begin{equation}
\wnet_\vartheta[\Lambda] \subset \wnet_\vartheta[\Lambda'] \text{ for } \Lambda \le \Lambda'
\end{equation}
and
\begin{equation}
 \wnet_\vartheta = \lim_{\Lambda \to \infty} \wnet_\vartheta[\Lambda].
\end{equation}
We also define a truncated version $\mu[\Lambda]$ of the soliton degeneracies
$\mu$:  $\mu[\Lambda](a)$ is defined only for charges $a$ with $\abs{Z_{\bar a}} < \Lambda$,
and for such charges it agrees with $\mu(a)$.

For small enough $\Lambda$, we can
describe $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$ simply and explicitly.
The reason is that charges $\bar a \in \Gamma(z,z)$ with $\abs{Z_{\bar a}} < \Lambda$
are represented by very short paths on $\Sigma$
between distinct lifts $z^{(i)}$ and $z^{(j)}$ of $z$.  The only way to get such a
short path is for $z$ to be close to an $(ij)$ branch point $\fb$:  then if we take $\bar a \in \Gamma(z,z)$ to be a path running
from $z^{(i)}$ to the ramification point over $\fb$
and returning to $z^{(j)}$, we indeed have $\abs{Z_{\bar a}} \to 0$
as $z \to \fb$.
We could also have considered the charge $-\bar a \in \Gamma(z,z)$, corresponding to a path
running in the opposite direction.
These two charges are exchanged by the monodromy when $z$ goes once around $\fb$.
They are the only charges which become massless at $\fb$.

So, to determine $\wnet_\vartheta[\Lambda]$ for $\Lambda$ small,
we just have to describe the $\cS$-walls supporting these light charges.
Letting $z$ be a local coordinate with $z=0$ at $\fb$, we have $Z_{\bar a} \sim z^{3/2}$
and $Z_{-\bar a} \sim -z^{3/2}$ (the
square-root branch cut arises from the monodromy $\bar a \to -\bar a$ noted above.)
It follows that there are $3$ $\cS$-walls
emerging from the branch point, as shown in Figure \ref{fig:branch-point-trajectories}.
\insfig{branch-point-trajectories}{The $3$ $\cS$-walls emerging from a branch point.
Because the two relevant sheets of the covering $\Sigma \to C$
are exchanged by monodromy around the branch point,
we cannot assign labels to the trajectories globally; instead we have chosen a branch cut and
a labeling of the sheets $i$ and $j$ on the complement of the cut.  We also label the cut with
the transposition $(ij)$ which relates the sheets on the two sides of the cut.}

If $z$ lies on one of these three $\cS$-walls near $\fb$, then
there is a light 2d-4d BPS soliton on the surface defect $\bS_z$, with central charge
in $\R_- e^{\I \vartheta}$.\footnote{In a sense
it would be better to refer to these light states simply as ``2d'' solitons rather than ``2d-4d,'' since their existence
does not depend much on the coupling to the 4d theory.  Indeed, the
existence of these light states can be deduced from a universal computation
involving the simplest nontrivial Landau-Ginzburg
model.  See Section 8.1 of \cite{Gaiotto:2011tf} for further discussion.}
This BPS soliton is represented by a short finite open web $N(z)$, consisting of a single
BPS string connecting $z$ to $\fb$, as illustrated in
Figure \ref{fig:short-trajectory}.
\insfig{short-trajectory}{A finite open web $N(z)$ consisting of a single short $ij$-trajectory, with one end on the $(ij)$-branch point $\fb$
and one end on $z$.  This finite open web represents a light BPS soliton
on the surface defect $\bS_z$.}
In accordance with the general rules of \S\ref{sec:2d4d-bps-states}, the charge $\bar a$ of this
BPS state is $\bar a = [N(z)_\Sigma]$, where $N(z)_\Sigma$ is the lift of $N(z)$ to $\Sigma$, i.e. a short path on $\Sigma$
running from $z^{(i)}$ to the ramification point over $\fb$ and then back to $z^{(j)}$.

As we have mentioned in \S\ref{sec:tricky-sign}, however,
to fix the sign of the BPS degeneracy for this soliton,
we need to choose a lift from the charge $\bar a$ to a class $a$.
Suppose we make the most obvious choice, namely the one determined by the web $N(z)$:  $a = [N(z)_{\tilde\Sigma}]$.  Let $p$ denote the $\cS$-wall on which $z$ sits.
Then finally $\mu(a, p)$ is a well defined integer, and it is meaningful to ask what it is.
We have a single isolated 2d-4d BPS web here, so it should contribute just
a single state; the only question is whether we will have $\mu(a, p) = +1$ or $\mu(a, p) = -1$.
We claim that the correct answer is
\begin{equation} \label{eq:mu-near-bp}
 \mu(a, p) = +1.
\end{equation}
Indeed, this is forced on us by the requirement of homotopy
invariance, which we discuss in \S\ref{sec:homotopy-invariance} below.
