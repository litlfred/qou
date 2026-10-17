---
doc_id: arxiv-2208.14188v2
doc_title: "Resurgence in complex Chern-Simons theory at generic levels"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 2208.14188v2.pdf
source_sha256: 92a7651c81b799b3
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.943
doc_brief: "Resurgence in complex Chern-Simons theory at generic levels — In this note we study the resurgent structure of sl(2, C) Chern-Simons state integral model on knot complements S3\41, S3\52 with generic"
---
\label{sc:intr}


Complex Chern-Simons theory remains an active field of research that
links up many fields in both physics and mathematics.  From the
physics side, $sl(2,\IC)$ Chern-Simons theory was first considered in
\cite{Witten:1988hc} as a means to describe three dimensional quantum
gravity on Lorentzian spacetime with positive cosmological constant.
Later a beautiful connection was revealed between $sl(N,\IC)$
Chern-Simons theory and 3d $N=2$ superconformal field theories by the
name of the 3d-3d correspondence
\cite{Dimofte:2010tz,Terashima:2011qi,Dimofte:2011ju,Dimofte:2013iv}
(see \cite{Dimofte:2014ija} for a review), which was used to define a
large class of 3d SCFTs.  Conversely, the BPS sector of the dual 3d
SCFT was used in \cite{Gukov:2016gkn,Gukov:2017kmk} to define
homological invariants $\widehat{Z}$ for the three manifold.



From the mathematical side, complex Chern-Simons theory plays an
important role in quantum topology.  It was found by Witten long time
ago \cite{Witten:1988hf} that Jones polynomials of knots, which are
Laurent polynomials in $q$, are vacuum expectation values of Wilson
loops along the knot in $SU(2)$ Chern-Simons theory with
$q = \exp(2\pi\ri/(k+2))$, where $k$ is the discrete level.  It is
then natural to consider more general complex values of $q$, which
translates to the complexification of the gauge group
\cite{Witten:2010cx}.
The complex Chern-Simons theory then provides a new topological
invariant for 3d manifolds.

For instance, when $M$ is a knot complement, the partition function of
the $sl(2,\IC)$ Chern-Simons theory on $M$ is generally believed to
reduce to a finite-dimensional integral called the state integral, as
proposed in
\cite{Andersen:2011bt,Andersen:2014aoa,Andersen:2016ugz,Dimofte:2011py,Dimofte:2014zga}
based on \cite{Hikami:2006cv,Dimofte:2009yn}, which is constructed
based on an ideal triangulation of the manifold.

The saddle points of the state integral in the weak coupling limit are
non-Abelian $sl(2,\IC)$ flat connections on the three manifold
\cite{Witten:1988hf}, and the associated asymptotic series
$\varphi^{(\s_j)}$ ($j\geq 1$) can be obtained by Gaussian expansion
\cite{Dimofte:2009yn}.  The state integral and thus the asymptotic
series are believed to be topological invariants as they do not change
with a different triangulation scheme.


On the other hand, the state integral model has the disadvantage that
it is incomplete in the sense that it misses the information of
Abelian flat connections \cite{Chung:2014qpa}.  Instead, the
asymptotic series $\varphi^{(\s_0)}(\tau)$ associated to the Abelian
flat connection $\sigma_0$ can be determined from the colored Jones
polynomials of the knot expanded in terms of $h = \log q$
\cite{Bar-Natan,Rozansky:1998urb,Kricker,GK:noncommutative}.


It is natural to study the resurgent structure of these asymptotic
series.  On the one hand, complex Chern-Simon theory is a special
quantum field theory with no renormalons, and therefore these
asymptotic series of saddle points must transform to each other by
Stokes automorphism, forming a so-called resurgent structure.  On the
other hand, the resurgence theory tells us that the Stokes constants
that control all the Stokes automorphisms define necessarily new
invariants which are non-perturbative in nature.  The resurgence
problem in Chern-Simons theory was first considered in
\cite{Garoufalidis:2007wa}, where it was found (and later emphasized
again in \cite{Garoufalidis:2021osl}) that the Borel transform of
$\varphi^{(\s_0)}(\tau)$ has poles at
$\text{Vol}(M)+\ri CS(M) +4\pi^2\IZ\ri$, which can be interpreted as a
resurgent formulation of the Volume Conjecture
\cite{Kashaev:1996kc,Murakami:2001cjp}.  Later the resurgent problems
of the series $\varphi^{(\s_j)}(\tau)$ ($j\neq 0$) for non-Abelian
saddle points were considered in
\cite{Gukov2016,Gang:2017hbs,Garoufalidis:2021lcp}.  See also
\cite{Garoufalidis:2020pax} on related results on Faddeev's quantum
dilogarithm which is a crucial ingredient of state integrals.

Recently the resurgent problem for the $sl(2,\IC)$ Chern-Simons theory
at level $k=1$ on the complement of the two simplest hyperbolic knots
$\knot{4}_1$ and $\knot{5}_2$ were completely solved in
\cite{Garoufalidis:2021osl,Garoufalidis:2020xec,Garoufalidis:2020nut}.
It was demonstrated that $\varphi^{(\s_0)}(\tau)$ of the Abelian flat
connection is related to $\varphi^{(\s_j)}(\tau)$ ($j\neq 0$) of
non-Abelian flat connections by Stokes automoprhisms but not the other
way around, while $\varphi^{(\s_j)}(\tau)$ ($j\neq 0$) transform to
themselves.  The Stokes constants of all these Stokes automorphisms
were computed explicitly.  Surprisingly the Stokes constants relating
$\varphi^{(\s_j)}(\tau)$ ($j\neq 0$) were found to coincide with the
BPS invariants in the dual 3d $N=2$ superconformal field theory on
$S^1$ \cite{Garoufalidis:2020xec,Garoufalidis:2020nut}, providing
another interesting entry of dictionary in the 3d-3d correspondence.
Furthermore, Stokes automorphisms were used to construct a new state
integral for the knot $\knot{4}_1$, which now includes the
contribution of the Abelian flat connection as well
\cite{Garoufalidis:2021osl}.  Finally, the statement that the series
$\varphi^{(\s_0)}(\tau)$ Borel resums to the $\widehat{Z}$ invariant
\cite{Gukov:2019mnk} was corrected to include additional contributions
from Borel resummation of $\varphi^{(\s_j)}(\tau)$
\cite{Garoufalidis:2021osl}.


In this work we continue this line of research, and generalise the
results of \cite{Garoufalidis:2020xec,Garoufalidis:2020nut} to
$sl(2,\IC)$ Chern-Simons theories with levels $k\geq 1$ with small
boundary holonomy deformation $x$.
We first demonstrate that the asymptotic series $\varphi^{(k,\s_j)}(x;\tau)$
($j\geq 1$) associated to non-Abelian flat connections are such that
their coefficients always live in the trace field of the knot extended
by the holonomy parameter $x$.
We then show that these asymptotic series enjoy universal resurgent
structures:
Both the distribution of Borel plane singularities and the associated
Stokes constants are independent of the level $k$, despite that the
asymptotic series themselves depend highly non-trivally on the level.

The remainder of the paper is structured as follows.  We summarise our
results, both on the properties of the asymptotic series and their
resurgent structure in section~\ref{sc:resurg}.  We then give details
in two example sections~\ref{sc:41},\ref{sc:52}.  Finally we conclude
and list open questions\ in section~\ref{sc:con}.
