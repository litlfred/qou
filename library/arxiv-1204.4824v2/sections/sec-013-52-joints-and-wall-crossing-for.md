---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-013-52-joints-and-wall-crossing-for
section_title: "Joints and wall-crossing for"
section_number: 5.2
pages: 23-30
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
---
\label{sec:wnet-basics}

Define a \ti{joint} to be a point $z \in C$ where at least two $\cS$-walls intersect.
A joint thus supports at least two charges, say $\bar a \in \Gamma_{ij}(z,z)$ and $\bar b \in \Gamma_{kl}(z,z)$.

\insfig{trajectories-meeting-commuting}{The local picture around a joint where exactly
two $\cS$-walls meet.  We also show two paths $\wp$, $\wp'$ on $C$
which are related to one another by regular homotopy across the joint.}
The simplest situation arises if the joint $z$ supports \ti{only} these two charges, so exactly two $\cS$-walls meet there.  This can only occur if
$i \neq l$ and $j \neq k$.  In that case the local picture around $z$ is as shown in Figure \ref{fig:trajectories-meeting-commuting}.

Now let us consider what happens to the soliton degeneracies $\mu$ as we
move across a joint.  As it turns out, we can answer this question completely
by considering the defect operators attached to the paths $\wp$, $\wp'$ on $C$ shown
in Figure \ref{fig:trajectories-meeting-commuting}.
The requirement of homotopy invariance says that
\begin{equation} \label{eq:flat-simple}
F(\wp, \vartheta) = F(\wp', \vartheta).
\end{equation}
To understand what this really means,
let us evaluate both sides using the rules of \S\ref{subsec:Compute-FP},
and then deform all the resulting paths on $\tilde\Sigma$ so that they run directly into
the joint $z$, with a common tangent vector $\tilde z$ at $z$.
Then we obtain
\begin{multline} \label{eq:x-simp}
\cD(\wp_+) (1 + \mu(a,p) X_{a_{\tilde z}}) (1 + \mu(b,q) X_{b_{\tilde z}}) \cD(\wp_-) = \\
\cD(\wp_+) (1 + \mu(b,q') X_{b_{\tilde z}}) (1 + \mu(a,p') X_{a_{\tilde z}}) \cD(\wp_-).
\end{multline}
The paths $a_{\tilde z}$ and $b_{\tilde z}$ are not composable in either direction
(since $a_{\tilde z}$ runs from $\tz^{(i)}$ to $\tz^{(j)}$ while $b_{\tilde z}$ runs from $\tz^{(k)}$ to $\tz^{(l)}$),
so we have $X_{a_{\tilde z}} X_{b_{\tilde z}} = X_{b_{\tilde z}} X_{a_{\tilde z}} = 0$.  Considering the terms linear in $X_{a_{\tilde z}}$ and $X_{b_{\tilde z}}$ in \eqref{eq:x-simp} then
gives
\begin{align}
 \mu(a,p) &= \mu(a,p'), \\ \mu(b,q) &= \mu(b,q').
\end{align}
In short:  when an $\cS$-wall of type $ij$ and an $\cS$-wall of type $kl$ meet transversely, they
cross without any changes in $\mu$.

\insfig{ijkl-collisions}{The local picture around a
generic collision between three $\cS$-walls.}
A more interesting situation arises when an $\cS$-wall of type $ij$ and an $\cS$-wall of type
$jk$ meet transversely.  Suppose the two walls support charges
$\bar a \in \Gamma_{ij}(z,z)$ and $\bar b \in \Gamma_{jk}(z,z)$.  (Note that in this case
we must have $i \neq k$; otherwise the two walls would obey the \ti{same} differential equation,
and it would be impossible for them to intersect transversely.)
In this case the joint $z$ supports both $\bar a$ and $\bar b$, which are \ti{composable} since $z^{(j)}$ is both
the end of $\bar a$ and the start of $\bar{b}$.  Hence the joint
also supports a third charge $\bar c = \bar a + \bar b \in \Gamma_{ik}(z,z)$, and
so there could be a third $\cS$-wall meeting $z$.  When $\mu$ is generic enough, the
picture is as shown
in Figure \ref{fig:ijkl-collisions}.\footnote{One might think that there is a second, inequivalent
possibility:  one could have
exchanged the $ij$ and $jk$ labels in Figure \ref{fig:ijkl-collisions}.  This gives a new picture, which is not
related to Figure \ref{fig:ijkl-collisions} by a rotation, but \ti{is}
related to Figure \ref{fig:ijkl-collisions} by an orientation-reversing map.  Fortunately, our rules
for computing $F(\wp, \vartheta)$ do not use the orientation of $C$.  So our analysis is fully general.}

The condition
\begin{equation} \label{eq:flat-simple-2}
F(\wp, \vartheta) = F(\wp', \vartheta)
\end{equation}
becomes
\begin{align} \label{eq:x-simp-2}
&\cD(\wp_+) (1 + \mu(a,p) X_{a_{\tilde z}}) (1 + \mu(c,q) X_{c_{\tilde z}}) (1 + \mu(b,r) X_{b_{\tilde z}}) \cD(\wp_-) = \\ \notag
&\cD(\wp_+) (1 + \mu(b,r') X_{b_{\tilde z}}) (1 + \mu(c,q') X_{c_{\tilde z}}) (1 + \mu(a,p') X_{a_{\tilde z}}) \cD(\wp_-).
\end{align}
Using $X_{a_{\tilde z}} X_{b_{\tilde z}} = (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} X_{c_{\tilde z}}$ and $X_{b_{\tilde z}} X_{a_{\tilde z}} = 0$,
\eqref{eq:x-simp-2} implies
\begin{align}
 \mu(a,p') &= \mu(a,p), \\
 \mu(b,r') &= \mu(b,r), \\
 \mu(c,q') &= \mu(c,q) + (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r). \label{eq:cv-wcf}
\end{align}

The result \eqref{eq:cv-wcf}
says that the number of solitons carrying charge $\bar{c}$ changes as we move
the modulus $z$ of the surface defect $\bS_z$ across the joint.
This reflects the phenomenon of decay/formation of bound states between solitons of charges
$\bar{a}$ and $\bar{b}$.  Indeed \eqref{eq:cv-wcf} is the same wall-crossing formula which was
discovered in \cite{Cecotti:1993rm} in the context of pure 2d theories, and was reinterpreted in
the 2d-4d
context in \cite{Gaiotto:2011tf}.  Our derivation of it here, using consistency of the framed 2d-4d
BPS spectrum, is essentially the same as the one given in \cite{Gaiotto:2011tf}.

There are a few important special cases which deserve separate discussion.
One arises when $\mu(c,q)=0$, so that we actually have only two $\cS$-walls intersecting, of
types $ij$ and $jk$.
In this case the situation is as shown in Figure \ref{fig:ijkl-collision-birth}:
the wall $q'$ is born from the joint, and \eqref{eq:cv-wcf} reduces to
$\mu(c,q') = (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r)$.

\insfig{ijkl-collision-birth}{A collision between $\cS$-walls, at which a new $\cS$-wall
is born.}
The reverse situation is also allowed:  if $\mu(c,q) = - (-1)^{w(a_{\tilde z}+b_{\tilde z},c_{\tilde z})} \mu(a,p) \mu(b,r)$, then \eqref{eq:cv-wcf} gives
$\mu(c,q') = 0$, so the wall $q$ ``dies'' at the joint,
as shown in Figure \ref{fig:ijkl-collision-death}.
\insfig{ijkl-collision-death}{A collision between $\cS$-walls, at which an $\cS$-wall
dies.}

So far we have described some local properties of $\wnet_\vartheta$ and $\mu$.  In the
next few sections we describe a recipe for explicitly \ti{constructing} them.



\subsection{The mass filtration; $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$ for small $\Lambda$} \label{sec:determining-wnet}

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



\subsection{$\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$ for general $\Lambda$} \label{sec:constructing-w}

We have determined $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$ for small
$\Lambda$.
Now we can ask how $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$
evolve as $\Lambda$ increases.
Using the properties of $\wnet_\vartheta$ and $\mu$ we have already determined, it is
straightforward to deduce the answer.

The three $\cS$-walls
emerging from each branch point $\fb$ flow according to the
differential equation \eqref{eq:trajectory-de}, for a distance
determined by the cutoff $\Lambda$.
When we increase $\Lambda$ enough, it might happen that
an $\cS$-wall of type $ij$ intersects
another $\cS$-wall of type $jk$.  At this point
a new $\cS$-wall of type $ik$ is born, as shown in
Figure \ref{fig:ijkl-collision-birth}.  The soliton degeneracy $\mu$
on this new wall is determined by the soliton degeneracies on
its parents, as in \eqref{eq:cv-wcf}.\footnote{Note that if two $\cS$-walls
carrying charges $\bar a \in \Gamma_{ij}$, $\bar b \in \Gamma_{jk}$ meet at a joint $z \in C$,
the joint is visible in $\wnet_\vartheta[\Lambda]$ beginning
at $\Lambda = \textrm{Max}(\abs{Z_{\bar a}(z)},
\abs{Z_{\bar b}(z)})$, but the $\cS$-wall born from the joint
does not appear until
$\Lambda = \abs{Z_{\bar a}(z)}+\abs{Z_{\bar b}(z)}$.}
This new ``secondary'' $\cS$-wall, in turn, also evolves according to \eqref{eq:trajectory-de}.
As $\Lambda$ increases the secondary walls can intersect with other $\cS$-walls and give birth to yet
more progeny, and so on.
In Figure \ref{fig:network-growth} we give an illustration
of the growth of $\wnet_\vartheta[\Lambda]$ with $\Lambda$ in one particular theory $S[\fg,C,D]$.
\insfigscaled{network-growth}{0.52}
{Sample $\wnet_\vartheta[\Lambda]$ in the theory $S[A_2,\IC\IP^1,D]$
where the $D_n$ are 3 full defects (blue dots at $z = -1, 0, 1$).
We choose $\vartheta = \pi/4$, $\phi_2 = \frac{2}{(z - 1)^2} + \frac{2}{(z + 1)^2} - \frac{4}{z^2}$, $\phi_3 = \frac{1 - 3 (z - 1) + 6 (z - 1)^2}{(z - 1)^3} + \frac{1 + 3 (z + 1) + 6 (z + 1)^2}{(z + 1)^3} - \frac{2 + 12  z^2}{z^3}$.
The plots shown are at $\Lambda = 1, 2, 5, 12, 20, \infty$.
At $\Lambda = 0$ three $\cS$-walls are born at each of the 6 branch points
(orange crosses); at larger values of $\Lambda$, additional $\cS$-walls are born at intersections.
As $\Lambda \to \infty$ all $\cS$-walls asymptotically approach the defects.
Some $\cS$-walls are cut off
by the boundary of the plot; the visible range is a square with side length $2.6$.
See \cite{spectral-network-movies}
for an animated version of this figure.}

We may also have intersections where three $\cS$-walls meet at a point, as
in Figure \ref{fig:ijkl-collisions}.
(The reader might feel that this phenomenon should not occur generically; indeed, three arbitrary
trajectories of types $ij$, $jk$, $ik$ would be unlikely to intersect at a single point, but the $\cS$-walls
are not arbitrary trajectories.  We include an example in Figure \ref{fig:threefold-intersection}.)
\insfigscaled{threefold-intersection}{0.69}{A portion of a sample $\wnet_\vartheta$,
exhibiting an intersection between three $\cS$-walls, marked by a yellow dot.  The region in the blue box is
blown up at right.
The $\cS$-walls which appear somewhere
in the genealogy of the three intersecting $\cS$-walls are shown in black; other $\cS$-walls
are shown in gray.  There are six branch points (orange crosses).
This example arises in the theory $S[A_3, C = \IC\IP^1, D]$ with
$\phi_2 = -10z \, \de z^2$, $\phi_3 = 4 \, \de z^3$, $\phi_4 = 9 z^2 \, \de z^4$.
We took $\vartheta = 1.841$, but we emphasize that this triple intersection persists
for nearby $\vartheta$ as well.}

There is one more complicated phenomenon which one can imagine:
what would happen if an $\cS$-wall of type $ij$ ran directly into an $(ij)$ branch point?
In this case it would not be immediately clear how to continue the network
$\wnet_\vartheta[\Lambda]$ and the BPS degeneracies $\mu[\Lambda]$.
This puzzling-looking situation cannot occur when $\vartheta$ is generic.
It does occur for non-generic $\vartheta$,
and this fact plays a crucial role in the considerations of \S\ref{sec:varying-theta} below.

We have now
given a recipe for constructing $\wnet_\vartheta[\Lambda]$ and $\mu[\Lambda]$
for any $\Lambda > 0$ and generic $\vartheta$.  $\wnet_\vartheta[\Lambda]$
consists of a finite number of $\cS$-walls for any $\Lambda$.
Taking the limit $\Lambda \to \infty$ we obtain the full $\wnet_\vartheta$
and $\mu$.  So we have now managed to determine \ti{all} of the soliton degeneracies of the
theory (including their tricky signs) using only the constraint of homotopy invariance!

More precisely, so far we have fixed some $\vartheta$ and determined all $\mu(a,p)$ --- i.e. we determined $\mu(a)$
when the parameter $z$ of the surface defect lies on an $\CS$-wall supporting the charge $a$.  This is not what one
would usually mean by ``determining the soliton degeneracies'':  what one would usually mean is that we fix some $z$
once and for all, and then compute all $\mu(a)$ for $a \in \tGamma(\tz,\tz)$.  The point is that, for any $a \in \tGamma(\tz,\tz)$,
there is some $\vartheta$ for which $z$ \ti{does} lie on an $\CS$-wall supporting $a$:  namely,
$\vartheta = \arg -Z_{\bar a}$.  So for each $a$ we can draw the corresponding network $\wnet_{\vartheta= \arg -Z_{\bar a}}$
and use it to compute $\mu(a)$.



\subsection{$\wnet_\vartheta$ near full defects} \label{sec:falling-down-holes}

On a close look at Figure \ref{fig:network-growth}, one notices that
as $\Lambda \to \infty$, all of the $\cS$-walls in $\wnet[\Lambda]$
asymptotically approach the full defects $D_n$.

To understand this concretely, let us consider the general behavior of $ij$-trajectories around a full defect.
In a local coordinate $z$ where the defect is at $z=0$,
we have
\begin{equation}
 \lambda^{(i)} = m^{(i)} \frac{\de z}{z} + \cdots
\end{equation}
where $\cdots$ denotes regular terms.  $ij$-trajectories near $z=0$ thus behave asymptotically like
\begin{equation}
 z(t) = z_0 \exp (\xi^{(ij)} t),
\end{equation}
where we defined
\begin{equation}
\xi^{(ij)} = \frac{e^{\I \vartheta}}{m^{(i)} - m^{(j)}}.
\end{equation}
As $t \to \infty$, we have $z(t) \to 0$ if and only if $\Re \, \xi^{(ij)} < 0$.
This suggests a natural ordering on the sheets in a neighborhood of $z=0$:  we say that $i < j$
if $\Re \, e^{- \I \vartheta}m^{(i)} < \Re \, e^{- \I \vartheta}m^{(j)}$.
$ij$-trajectories near $z=0$ asymptote to $z=0$ if and only
if $i < j$ in this ordering.

In the coordinate $z$,
these infalling trajectories asymptotically approach logarithmic spirals.  Passing to the covering coordinate $w = \log z$, the $ij$-trajectories are straight lines,
\begin{equation}
 w(t) = w_0 + \xi^{(ij)} t.
\end{equation}
Now suppose we have an infalling asymptotic $\cS$-wall of type $ij$ and another of type $jk$
(so $i < j < k$.)  Assuming $\arg \xi^{(ij)} \neq \arg \xi^{(jk)}$, these
two walls intersect at infinitely many
points as they spiral into $z = 0$.  Each intersection gives birth to a new $\cS$-wall of type $ik$,
which also spirals into $z = 0$.  This new $\cS$-wall can in turn intersect other
inspiraling $\cS$-walls
and give birth to yet more progeny.  The strict ordering of the sheets ensures
that the progeny cannot commit incest with one another.
Nevertheless, for $K>2$ there are an infinite number of joints accumulating at the
full defect.  See Figure \ref{fig:infalling-trajectories} for an illustration.
\insfigscaled{infalling-trajectories}{0.45}{$\cS$-walls falling into a full defect, shown in the covering coordinate
$w = \log z$.  There is a single $ij$ wall and a single $jk$ wall.  We have $i < j < k$
in the ordering described in the text.
Each intersection between these two walls generates a new $ik$ wall.  There are infinitely many
such intersections, accumulating at the defect, which generate infinitely many $ik$ walls.}
Similar (but more involved) remarks should apply for more general types of defect.

Based on computer experimentation, we expect that the behavior observed in Figure \ref{fig:network-growth}
is indeed generic:  whenever there is a defect
with sufficiently generic mass parameters, and $\vartheta$ is generic, all $\cS$-walls in $\wnet_\vartheta$
should asymptotically
approach punctures.  In the case $K=2$ this follows directly from known mathematical results on the trajectories of
quadratic differentials \cite{MR743423} (see \cite{Gaiotto:2009hg} for an account of this.)
For $K>2$ the analogous foundational results
are not yet available as far as we know.  It would be very desirable to work this out.
