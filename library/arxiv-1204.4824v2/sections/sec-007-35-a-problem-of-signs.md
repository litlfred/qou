---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-007-35-a-problem-of-signs
section_title: "A problem of signs"
section_number: 3.5
pages: 17-19
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.972
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:tricky-sign}

We must now confront a pesky but important detail.

There is an ambiguity in \eqref{eq:2d-4d-motindx}:  the generators $F$ and $\CJ$
are well defined only up to $c$-number shifts.  As a result, the index $\fro'(L_{\wp,\vartheta}, \bar a)$
suffers from some potential ambiguity (which even depends on $\wp$).  We can partially fix this ambiguity by requiring that
$\fro'(L_{\wp,\vartheta}, \bar a)$ is real, but this still leaves the possibility of an integer shift
of $F$ or $\CJ$.  Such a shift would reverse the sign of $\fro'(L_{\wp,\vartheta}, \bar a)$.
So, \ti{a priori}, we would expect that we need some additional data in order
to fix $\fro'(L_{\wp,\vartheta}, \bar a)$ uniquely.
A similar ambiguity afflicts the 2d-4d BPS degeneracies $\mu(\bar a)$:  the definition \eqref{eq:def-mu}
depends on the choice of generator $F$, and changing this choice can change $\mu(\bar a)$ by a sign.

There is no difficulty in fixing these ambiguities locally in any particular corner of parameter space.
In this paper, though, we will mainly be concerned with phenomena which occur when parameters are
varied, sometimes over long distances in parameter space.  It is therefore
desirable to have a global way of fixing these sign ambiguities, which is consistent with all of the
physical constraints, and ideally one that does not depend on any arbitrary choices.
We have found such a rule, which we now describe.  It would be desirable to give a first-principles
\ti{derivation} of this rule from the physics of the $(2,0)$ theory $S[\fg]$ in six dimensions.

\insfig{tangent-vectors}{Two tangent directions at $z$ determined by a finite web $N$:  $\tz_1$
points ``into'' the finite web while $\tz_2$ points ``away.''}

It will be useful to keep track of
a bit more information about the finite webs $N$ representing 2d-4d BPS states.
For any real surface $S$, let $\tilde S$ denote the circle
bundle of tangent directions to $S$.
For $z\in S$ we will let $\tilde z$ denote a lift
of $z$ to $\tilde S$, that is, a choice of tangent direction at $z$.  Any smooth path $\wp$
on $S$ carries a natural tangent direction field and hence has a canonical lift to a path
$\tilde\wp$ on $\tilde S$; we will use this lift often.
There is a distinguished class $H \in H_1(\tilde\Sigma; \Z)$, represented by a path which winds
once around a fiber of $\tilde\Sigma$ (the choice of fiber does not matter).

By smoothing out the junctions slightly,
we can deform $N_\Sigma$ into a finite union of \ti{smooth} paths on $\Sigma$,
which thus has a canonical lift to a path $N_{\tilde\Sigma}$ on $\tilde\Sigma$.
Let $\tz_1$ and $\tz_2$ denote the tangent directions to $C$ at $z$ shown in
Figure \ref{fig:tangent-vectors}.  Let $\tz_1^{(i)}$ be the lift of $\tz_1$ to the $i$-th sheet of $\tilde\Sigma$,
and similarly define $\tz_2^{(j)}$.  The path $N_{\tilde\Sigma}$ then has
\begin{equation} \label{eq:lifted-boundary}
 \partial N_{\tilde\Sigma} = \tz_2^{(j)} - \tz_1^{(i)}.
\end{equation}
Let $\tilde\Gamma(\tz_1,\tz_2)$ denote the set of relative homology classes on $\tilde\Sigma$ obeying \eqref{eq:lifted-boundary}, \ti{modulo} shifts by the class $2H$.
$\tilde\Gamma(\tz_1, \tz_2)$ is a principal $\Z/2\Z$-bundle over $\Gamma(z_1, z_2)$,
with the $\Z/2\Z$ action given by adding $H$.
The relative homology class $[N_{\tilde\Sigma}] \in \tilde\Gamma(\tz_1,\tz_2)$ thus keeps track of
one extra $\Z / 2\Z$ worth of information beyond that in $[N_\Sigma] \in \Gamma(z,z)$.
There can be different open finite BPS webs $N$ carrying the same charge $[N_\Sigma]$ but
with different lifts $[N_{\tilde\Sigma}]$; see Figure \ref{fig:distinct-lifts} for an example.
\insfig{distinct-lifts}{Two open finite BPS webs $N$ on the same patch of $C$, drawn displaced
from one another for clarity.  These two webs
carry the same charge $[N_\Sigma]$ but
have different lifts $[N_{\tilde\Sigma}]$. Informally, one can say that the lifts of these two
webs ``differ by one unit of winding.''}

Now we can explain our proposal for how the sign of $\mu$ behaves.  Given a charge $\bar a \in \Gamma(z,z)$,
$\mu(\bar{a})$ is not well defined (although it is well defined up to sign).
In order to make it well defined, we propose that we must choose a class
$a \in \tGamma(\tz_1,\tz_2)$ which projects to $\bar a$.  Having done so,
there should be a way of fixing the ambiguity of $F$ to obtain a well defined
BPS degeneracy, which we call $\mu(a)$.
Two choices $a$, $a'$ differ by a winding number $w(a,a')$;
the corresponding $\mu$ should obey
\begin{equation} \label{eq:mu-sign-rule}
 \mu(a) / \mu(a')  = (-1)^{w(a,a')}.
\end{equation}
(Of course, knowing $\abs{\mu(a)}$ for all $a$ and knowing \eqref{eq:mu-sign-rule} is still not enough by itself to determine $\mu$.
Later in this paper we will fix one more convention, in \eqref{eq:S-factor},  after which we
will be able to calculate $\mu(a)$ for all $a$.)

A similar discussion applies to $\fro'(L_{\wp,\vartheta}, \bar a)$, but with the extra complication
that now we have to discuss both the dependence on the path $\wp$ and on the charge $\bar a$.
First suppose we \ti{fix} the path $\wp$ from $z_1$ to $z_2$, with initial tangent vector $\tz_1$
and final tangent vector $\tz_2$.  Then we propose that the situation is strictly parallel
to our discussion of $\mu$ above:
the degeneracies $\fro'(L_{\wp,\vartheta}, \bar a)$ are not well defined (although they are well
defined up to sign), and
what is really defined is an integer $\fro'(L_{\wp,\vartheta}, a)$, where $a \in \tGamma(\tz_1,\tz_2)$
is a lift of $\bar a \in \Gamma(z_1,z_2)$.  The dependence on the choice of lift is given by
\begin{equation} \label{eq:winding-rule-1}
\fro'(L_{\wp,\vartheta}, a) / \fro'(L_{\wp,\vartheta}, a') = (-1)^{w(a,a')}.
\end{equation}

Now let us also consider the dependence on $\wp$.
Recall from \S \ref{sec:framed-bps} that the line defect $L_{\wp, \vartheta}$ depends only on the
homotopy class of the path $\wp$. Nevertheless,
 the prescription for fixing the sign of $\fro'(L_{\wp,\vartheta},a)$ can depend on
more information than just the homotopy class.  We propose that the sign actually depends on
the homotopy class of the lift of $\wp$ from $C$ to the bundle of tangent directions $\tilde{C}$.
For two paths $\wp$, $\wp'$ whose lifts to $\tilde{C}$
have the same initial and final endpoints, there is a mod-2
winding number $w(\wp,\wp')$ (defined similarly to the winding number we considered above for paths on $\Sigma$).
We propose that for such paths we have
\begin{equation}
\fro'(L_{\wp,\vartheta},a) / \fro'(L_{\wp',\vartheta},a) = (-1)^{w(\wp,\wp')}.
\end{equation}
We summarize this proposal by saying that the framed 2d-4d BPS degeneracies of the
interface $L_{\wp,\vartheta}$ are not quite homotopy invariants of $\wp$, but rather are
``twisted homotopy invariants'' of $\wp$.
