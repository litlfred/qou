---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-005-33-framed-2d-4d-bps-states
section_title: "Framed 2d-4d BPS states"
section_number: 3.3
pages: 15-16
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.809
latex_coverage_ratio: 1.0
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:framed-bps}

Our approach to the BPS spectrum will involve an auxiliary device, the
\ti{framed} BPS states.  These were introduced in the pure 4d context in
\cite{Gaiotto:2010be}, and in the 2d-4d context in \cite{Gaiotto:2011tf}.
Our interest in this paper is in the 2d-4d version.

Consider a pair of points $z_1$, $z_2$ in $C$, and a path
$\wp$ in $C$ from $z_1$ to $z_2$.  Also fix a parameter $\vartheta \in \IR$.
These data determine a pair of surface defects
$\bS_{z_1}$ and $\bS_{z_2}$ in $S[\fg, C, D]$ along with a supersymmetric
interface $L_{\wp,\vartheta}$ between the two surface defects.
The interface $L_{\wp,\vartheta}$ preserves 2 out of the 4 supercharges preserved by
the surface defects; which 2 supercharges are preserved is determined by the parameter
$e^{\I \vartheta}$, as explained
in \cite{Gaiotto:2011tf}.\footnote{The parameter which was called $\zeta$ in \cite{Gaiotto:2011tf}
is here given by $\zeta = e^{\I \vartheta}$.}
It is generally believed that the defect
$L_{\wp,\vartheta}$ does not depend on the precise path $\wp$ but only on its homotopy class.
In the
present paper we will take this as an assumption, and will find a very consistent picture
(although of course the quantities we study are somewhat protected by supersymmetry);
see e.g. \cite{Gaiotto2011} for some related discussion.
Indeed, we will find that the constraint of homotopy invariance is very strong.

Now we study the 4d theory $S[\fg, C, D]$ with the defects $\bS_{z_1}$ and $\bS_{z_2}$
inserted on two half-lines $\{ x^1 = 0, x^2 = 0, x^3 > 0 \}$
and $\{ x^1 = 0, x^2 = 0, x^3 < 0 \}$ respectively,
separated by the interface $L_{\wp,\vartheta}$.  See Figure \ref{fig:two-surface-operators}.
\insfig{two-surface-operators}{Two surface defects connected by an interface.  (This picture
lives in the three-dimensional space where the field theory $S[\fg,C,D]$ is defined; we have factored
out the time direction.)}
We then define
(2d-4d) \ti{framed BPS states} to be states of the 1-particle Hilbert space $\CH^1_{L_{\wp,\vartheta}}$
of this combined system
which are fully supersymmetric, i.e. preserve the 2 supercharges present in the system.

The 2d-4d framed BPS states should be thought of as different ``vacuum states'' of the interface
$L_{\wp, \vartheta}$.  To make this statement sharp, however, we need to impose a constraint.
We say $\vartheta$ is \ti{generic} if there is no charge $\gamma \in \Gamma$ with
$e^{-\I \vartheta} Z_\gamma \in \R_-$.
We say the pair $(\wp, \vartheta)$ is \ti{generic} if
$\vartheta$ is generic and also there is no charge
$\bar a \in \Gamma(z_1,z_1)$ or $\bar a \in \Gamma(z_2,z_2)$ with
$e^{-\I \vartheta} Z_{\bar a} \in \R_-$, where $z_1,z_2$ are the
initial and final points of $\wp$.
When the pair $(\wp, \vartheta)$ is generic, the 2d-4d framed BPS states
are indeed localized near the interface, in the sense that they do not mix with the continua
of unframed 2d-4d or 4d BPS states.

The classification of 2d-4d framed BPS states by charges is similar to that
for the 2d-4d unframed BPS states in \S\ref{sec:2d4d-bps-states}.
Instead of
paths on $\Sigma$ between two lifts $z^{(i)}$, $z^{(j)}$ of a single point $z$, now we consider
paths on $\Sigma$ from a lift $z^{(i)}_1$ of $z_1$ to a lift $z^{(j)}_2$ of $z_2$.
We let $\Gamma_{ij}(z_1, z_2)$ denote the set of relative homology classes represented by such paths,
and $\Gamma(z_1, z_2) = \cup_{i,j} \Gamma_{ij}(z_1,z_2)$.\footnote{In \cite{Gaiotto:2011tf} we denoted
elements of $\Gamma(z_1,z_2)$ by $\gamma_{ij'}$, but we are now deprecating that
notation in favor of $\bar a$. See Appendix \ref{app:Conv-conv} for a summary of conventions.}

There is a ``framed BPS index'' $\fro(L_{\wp,\vartheta}, \bar a;y)$
counting 2d-4d framed BPS states with charge $\bar a \in \Gamma_{ij}(z_1, z_2)$.
It was defined in
\S 4.4 of \cite{Gaiotto:2011tf}:\footnote{As in \cite{Gaiotto:2011tf}, $F$ denotes a generator of $u(1)_V$ of the 2d $(2,2)$ supersymmetry algebra
preserved by $L_{\wp,\vartheta}$, and $\CJ = 2 J_{12} + 2 I_{12}$
is a linear combination of rotation and $su(2)_R$ generators of the 4d $\N=2$
supersymmetry.  There is a subtlety here
which we address in \S\ref{sec:tricky-sign}:
to define $F$ properly we will need to keep track of slightly more information about the 2d-4d framed
BPS states, by extending the charge $\bar{a}$
to a new ``charge'' denoted $a$.  It will turn out that $\fro$ really depends on $a$, not $\bar a$.}
\begin{equation}\label{eq:2d-4d-motindx}
\fro(L_{\wp,\vartheta}, \bar a;y) = {\rm Tr}_{\CH^{1,\rm BPS}_{L_{\wp,\vartheta}},\bar a} \, e^{\I \pi F} (-y)^{\CJ}.
\end{equation}
In this paper we will concentrate on the indices at $y=1$, which will be denoted
by $\fro'(L_{\wp,\vartheta}, \bar a)$.  We leave the generalization of our story to arbitrary $y$
as an important open problem.

Framed 2d-4d BPS states admit a geometric description somewhat similar to those given above
for unframed 2d-4d BPS states.  We will not describe it
explicitly here.\footnote{In the case $K=2$ (i.e. $\fg = A_1$) we did explain the relevant objects
in \cite{Gaiotto:2010be}, where we called them ``millipedes.''}
