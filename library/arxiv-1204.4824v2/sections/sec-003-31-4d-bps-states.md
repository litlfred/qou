---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-003-31-4d-bps-states
section_title: "4d BPS states"
section_number: 3.1
pages: 12-14
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{subsec:4d-BPS-States}

Now we recall the geometric description of BPS states in $S[\fg, C, D]$.

All such BPS states arise from BPS strings of the six-dimensional $S[\fg]$, which are extended
along $C$ and hence look like point particles in the remaining 3+1 dimensions.
Roughly there are $\binom{K}{2}$ distinct
kinds of BPS string, but the topological twisting and compactification makes the story slightly
trickier, as we now recall.

An oriented
segment of string passing through a point $z \in C$
is labeled by the choice of a pair of distinct sheets of the $K$-fold covering
$\Sigma \to C$, i.e. two solutions
$\lambda^{(i)}$, $\lambda^{(j)}$ ($i \neq j$) of the degree-$K$ polynomial equation \eqref{eq:sw-curve},
in a neighborhood of $z$.  To keep track of this discrete label, we use the term
``$ij$-string'' rather than just ``string.''
Reversing orientation exchanges $ij$-strings and $ji$-strings.

The $\N=2$ central charge $Z$ of an $ij$-string is obtained by integrating the complex 1-form $\frac{1}{\pi}(\lambda^{(i)} - \lambda^{(j)})$ along the string.
The mass $M$ of an $ij$-string is obtained by integrating the real density $\frac{1}{\pi} \abs{\lambda^{(i)} - \lambda^{(j)}}$.

When is such a string BPS?
Introduce a local coordinate on $C$ by $w^{(ij)} = \int \lambda^{(i)} - \lambda^{(j)}$, and
then define an \ti{$ij$-trajectory with phase $\vartheta$} to be a straight line in the
$w^{(ij)}$-coordinate, with inclination $\vartheta$, i.e. a line along which
\begin{equation} \label{eq:trajectory-de}
\Im(e^{- \I \vartheta} \dot{w}^{(ij)}) = 0.
\end{equation}
An $ij$-trajectory is naturally oriented:
the positive direction is the
direction in which $\Re(e^{-\I \vartheta} w^{(ij)})$ increases.
Reversing orientation of an $ij$-trajectory gives a $ji$-trajectory.
An $ij$-string is BPS if and only if it is stretched along an $ij$-trajectory
with some phase $\vartheta$; we call such a string a ``BPS string of phase $\vartheta$.''
We see at once that for BPS strings $\abs{Z} = M$ as expected.
The phase $\vartheta$ determines which supercharges the BPS string preserves.

An $ij$-string can end in two ways.  First, it can end on an \ti{$(ij)$-branch point}, i.e.
a point where $\lambda^{(i)} - \lambda^{(j)} = 0$.\footnote{We use the notation $(ij)$ for the branch
points but $ij$ for the trajectories; the $(ij)$ is meant to denote the \ti{transposition} associated
to the branch point, which exchanges sheet $i$ and sheet $j$ of the covering $\Sigma \to C$.
In particular $(ij) = (ji)$.}
Second, it can end on a \ti{junction}
where an $ij$-string, $jk$-string and $ki$-string meet (all oriented into the junction.)
In the latter case, for the combined web of strings to be BPS, all three strings must be BPS
strings with the \ti{same} phase $\vartheta$.

BPS states in $S[\fg, C, D]$ arise from webs of BPS strings, such that
all strings in the web have finite total central charge.
This condition means that the
strings are either closed loops or have both ends on branch points or junctions.
We call these \ti{finite webs}.
Some possible topologies for finite webs
are shown in Figure \ref{fig:finite-networks}.
\insfigscaled{finite-networks}{0.24}{Some possible topologies for finite webs of BPS strings.
An orange cross with label $(ij)$ denotes an $(ij)$-branch point.  Wherever
a string with label $ij$ appears, it could equally well have been represented by
a string with label $ji$ and the opposite orientation.}

The charges of the BPS states are determined by the topology of the webs, in the following way.
An $ij$-string stretched along an oriented path $p$ on $C$
can be lifted in a canonical way to $p_\Sigma$, a union of oriented curves on $\Sigma$:
namely, $p_\Sigma$ is the union of the lift $p^{(i)}$ of
$p$ to the $i$-th sheet and the lift $-p^{(j)}$ of $-p$ ($p$ with reversed orientation)
to the $j$-th sheet.  Letting $p$ run over the strings in a finite web $N$, the union of the $p_\Sigma$ is a closed 1-cycle $N_\Sigma$ on $\Sigma$.
$N_\Sigma$ has a homology class $[N_\Sigma] \in \Gamma := H_1(\Sigma; \Z)$.  This $[N_\Sigma]$
is the charge of the BPS state.\footnote{The precise charge lattice of
the theory $S[\fg, C, D]$ is actually a subquotient of
$H_1(\Sigma; \Z)$, as explained in \cite{Gaiotto:2009hg}. Nevertheless, in this paper,
we consider $\Gamma = H_1(\Sigma; \Z)$ for simplicity.}

The central charge of a finite web $N$ is the sum of the central charges of the
strings in $N$; this gives a simple result which depends only on $\gamma = [N_\Sigma]$,
\begin{equation} \label{eq:Zgamma}
 Z_\gamma = \frac{1}{\pi} \oint_\gamma \lambda.
\end{equation}

To determine the BPS spectrum of the theory, in particular the second helicity supertrace
$\Omega(\gamma)$, one should in principle proceed by quantizing
the zero modes of each finite web.  This would give some definite formula
for the contribution of each finite web to $\Omega(\gamma)$.
In practice, such a quantization has not been completely carried out, and we will not do it here
either.\footnote{In \cite{Gaiotto:2009hg} we used wall-crossing to determine $\Omega(\gamma)$ in the case $K=2$,
reproducing earlier results of \cite{Klemm:1996bj}.
That case is particularly simple since there are only two possible topologies for finite
webs:  one can either have a single string connecting two branch points or a single closed loop.
These topologies contribute $\Omega(\gamma) = +1$ and $\Omega(\gamma) = -2$ respectively.
We will reproduce this result yet again in \S\ref{sec:k2-examples} below.}
Rather, we will explain a more indirect route, which determines $\Omega(\gamma)$ using the interactions between 2d and 4d BPS states.

One could also ask about extending $\Omega(\gamma)$ to an object which keeps track of the spins
of the BPS multiplets appearing.  Such ``refined BPS degeneracies'' and ``protected
spin characters'' have been considered in the $\N=2$ context
e.g. in \cite{ks1,Dimofte:2009tm,Cecotti:2009uf,Cecotti:2010qn,Gaiotto:2010be}.  We will not consider
that extension in this paper.
