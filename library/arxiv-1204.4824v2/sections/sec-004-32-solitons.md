---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-004-32-solitons
section_title: "Solitons"
section_number: 3.2
pages: 14-15
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:2d4d-bps-states}

In the presence of the canonical surface defect $\bS_z$, there is a second kind of BPS state in the story:
we can consider BPS particles which are bound to the defect and interpolate between distinct vacua.
We call these particles \ti{solitons}.

As described in \cite{Gaiotto:2011tf}, BPS solitons
are also realized geometrically in terms of finite webs of strings.  The main difference is that now
we consider webs in which one of the strings ends on the point $z$, which we call
\ti{finite open webs}.  See Figure \ref{fig:finite-networks-2d}.
\insfigscaled{finite-networks-2d}{0.24}{Some possible topologies for finite open webs of BPS strings, representing BPS solitons
on the surface defect $\bS_z$.
Each finite open web includes one string that ends on the point $z \in C$.
An orange cross with label $(ij)$ denotes an $(ij)$-branch point.}

Let $N$ denote a finite open web.
As for the pure 4d case, the charge of the corresponding BPS soliton is
determined by the topology of the web, as follows.
Let $N_\Sigma$ denote the union of the lifts of all strings in $N$ to $\Sigma$.
Suppose the string of $N$ ending on $z$ is an $ij$-string oriented out of $z$.
Let $z^{(i)}$ and $z^{(j)}$ be the preimages of $z$
on the $i$-th and $j$-th sheets of $\Sigma$.
$N_\Sigma$ is a 1-chain with boundary:
\begin{equation} \label{eq:chain-boundary}
\partial N_\Sigma = z^{(j)} - z^{(i)}.
\end{equation}
We let $\Gamma_{ij}(z,z)$ denote the set of relative homology
classes on $\Sigma$ obeying \eqref{eq:chain-boundary}, and
\begin{equation}
\Gamma(z,z) = \cup_{i,j} \Gamma_{ij}(z,z).
\end{equation}
Thus the charges $[N_\Sigma]$ of BPS solitons on $\bS_z$ are elements of $\Gamma(z,z)$,
and in fact of the smaller set $\cup_{i,j,i \neq j} \Gamma_{ij}(z,z)$.

The central charges of BPS solitons are given by a formula analogous to \eqref{eq:Zgamma}:
for any $\bar a \in \Gamma(z,z)$ we have\footnote{In \cite{Gaiotto:2011tf} we denoted
elements of $\Gamma_{ij}(z,z)$ by $\gamma_{ij}$, but we are now deprecating that notation in favor of $\bar a$.
See Appendix \ref{app:Conv-conv} for a summary of conventions.}
\begin{equation}
 Z_{\bar a} = \frac{1}{\pi} \int_{\bar a} \lambda.
\end{equation}
There is a BPS index $\mu(\bar a) \in \Z$ which counts 2d-4d BPS states
of charge $\bar a$, defined as a trace over the Hilbert space of 1-particle
BPS states \cite{Cecotti:1992qh,Cecotti:1993rm},
\begin{equation} \label{eq:def-mu}
 \mu(\bar a) = {\rm Tr}_{\CH^{1,\rm BPS}_{\bS_z,\bar a}}\,F e^{\I \pi F},
\end{equation}
where $F$ is a fermion number operator.
In principle, $\mu(\bar a)$ could be determined by quantizing the zero modes
of the BPS strings.  In practice, as with $\Omega(\gamma)$, we will take a more
indirect route in this paper.

We hasten to warn the reader that there are two important subtleties
in the definition \eqref{eq:def-mu}.  The first subtlety is
addressed in \S\ref{sec:tricky-sign}:
to define $F$ properly we will need to keep track of slightly more information about
the 2d-4d BPS states, by extending the charge $\bar{a}$ to a new ``charge'' denoted $a$.
It will turn out that $\mu$ really depends on $a$, not $\bar a$.  The second subtlety is that the
space of 1-particle BPS states is only well defined when the parameters are not on
a wall of marginal stability.  At these walls, $\mu(a)$ can jump. In particular,
if $\bar a \in \Gamma(z,z)$, then generically, if we move $z$ holding all other parameters
fixed, and apply the natural parallel transport to the
relative homology cycle $\bar a$, $\mu(a)$ remains constant.  However, there are
walls on $C$ across which $\mu(a)$ jumps, and in this case we will need to
define limits $\mu^\pm(a)$ as $z$ approaches
the wall from either side. This will be important in \S \ref{sec:varying-theta}.
