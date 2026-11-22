---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-000-1-introduction-and-summary
section_title: "Introduction and summary"
section_number: 1
pages: 4-11
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.997
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
\label{sec:Introduction}

In this paper we study objects which we call \ti{spectral networks}.
A spectral network $\wnet$
is made up of \ti{walls} drawn on  a punctured real surface $C$.
Here is a picture of one:
\insfigscaled{sample-network}{0.6}{A spectral network, drawn on
the stereographic
projection of $C = S^2$, with a single puncture at infinity.
All of the walls eventually asymptote to this puncture.
The walls are labeled by pairs $ij$, where $i$, $j$ are sheets of a 3-fold covering $\Sigma \to C$.
The branch points of the covering are shown as orange crosses.
We have trivialized the covering over the complement
of some branch cuts, shown as wavy orange lines.}

Each wall carries some extra discrete data:  a pair $ij$ and (roughly) an integer $\mu$.  The labels $i$ and $j$ are drawn from the set of sheets
of a finite branched covering $\Sigma \to C$.  The walls and their
discrete data obey certain local constraints:  for example,
\begin{itemize}
 \item each simple branch point of the covering $\Sigma \to C$ gives birth to three walls;
 \item when an $ij$ wall and a $jk$ wall intersect, a new
$ik$ wall is born at their intersection point.
\end{itemize}

In \S\ref{sec:review-S}-\S\ref{sec:Examples} of this paper we study
some particular spectral networks which arise naturally in physics.
In \S\ref{sec:spectral-networks} we axiomatize the notion of spectral network.
In \S\ref{sec:moduli} we describe a more mathematical application, to coordinate systems
on moduli spaces of flat connections.  Those sections are mostly self-contained.

\medskip


Here is how spectral networks arise in physics.
Fix an $\N=2$ supersymmetric theory $T$ in $d=4$ and a point $u$ of the Coulomb branch.
Also fix a 1/2-BPS surface defect $\bS_z$ which has
a 1-complex-dimensional space $C$ of UV parameters, and is massive in the IR,
with finitely many vacua for any fixed $z$.
These data determine a 1-parameter family of spectral networks
$\wnet_\vartheta$ drawn on $C$, labeled by phases $\vartheta \in \R / 2 \pi \Z$.
Namely, $\wnet_\vartheta$ is the locus of $z \in C$ for which the surface defect $\bS_z$ carries a BPS soliton whose central charge $Z$ is aligned with $-e^{\I \vartheta}$.
The discrete data $\mu$ on the walls keep track of the degeneracies of these BPS solitons.
The points of the finite cover $\Sigma \to C$ over $z \in C$ are the vacua of $\bS_z$.
The data $ij$ on the walls keep track of which vacua of $\bS_z$ are being interpolated by the solitons.

\medskip

In this paper, for concreteness, we focus on a particular (large) class of $\N=2$ theories,
namely the theories of class $S$ \cite{Witten:1997sc,Gaiotto:2009we,Gaiotto:2009hg}.
These are the theories $S[\fg,C,D]$, associated to
a Lie algebra $\fg$ (which we take to be $\fg = A_{K-1}$),
punctured Riemann surface $C$, and a collection $D$
of defects placed at the punctures of $C$.
They are obtained by a partially topologically twisted compactification
of the six-dimensional $(2,0)$ theory $S[\fg]$.
A point $u$ of the Coulomb branch here means a
tuple $(\phi_2, \dots, \phi_K)$, where each $\phi_r$ is a
meromorphic $r$-differential on $C$, with poles at the defects.
In these theories there is
a canonical surface defect $\bS_z$ whose parameter space is $C$.
Moreover, in these theories the covering $\Sigma \to C$ can be identified with the
Seiberg-Witten curve \cite{Gaiotto:2009fs,Gaiotto:2011tf} and is given concretely by \eqref{eq:sw-curve} below.

The spectral networks $\wnet_\vartheta$ arising from theories of class $S$ can be described concretely.
The walls of the network are solutions of differential equations, given in \eqref{eq:trajectory-de} below.
The full network is built up by a continuous process:  three walls are born from each branch point of
the covering $\Sigma$ and flow according to \eqref{eq:trajectory-de}; whenever
two walls intersect, they can give birth to an additional wall.  This process is described in \S\ref{sec:constructing-w}.

\medskip

Here are some of the uses of the spectral networks $\wnet_\vartheta$:

\smallskip
{\bf Framed BPS states.} By letting the parameter $z$ of a surface defect vary along a path $\wp$ in $C$, one can define a supersymmetric interface $L_{\wp,\vartheta}$ \cite{Gaiotto:2011tf}.
Knowing $\wnet_\vartheta$ and $\mu$ allows one to determine the complete spectrum of BPS states of
these interfaces, called ``framed BPS states.''  In fact, the framed BPS spectrum turns out to be \ti{over}determined, so much so that one can use its consistency to compute $\mu$.

\smallskip
{\bf Jumps of $\wnet_\vartheta$ and the 4d BPS spectrum.} As the parameter $\vartheta$
is varied, $\wnet_\vartheta$ also varies.  There are some critical phases $\vartheta_c$
at which the topology of $\wnet_\vartheta$ suddenly changes (in a precise sense explained in
\S \ref{sec:varying-theta}).
These critical phases $\vartheta_c$
are the phases of the central charges $Z_\gamma$ of BPS states in the $d=4$ theory $S[ \fg,C,D]$.
Moreover, one can read off the degeneracies $\Omega(\gamma)$ of these BPS states from
the topology of $\wnet_{\vartheta = \vartheta_c}$.

We find in this way that BPS states in $S[ \fg,C,D]$ correspond to certain ``finite webs'' of
strings on $C$, which appear inside the spectral network $\wnet_\vartheta$ at the critical phase.
Some pictures of finite webs appear in Figure \ref{fig:finite-networks}.
The role of finite webs in the BPS spectrum was already expected
\cite{Klemm:1996bj,Brandhuber:1996xk,Aharony:1997bh,Gaiotto:2009hg}, but our analysis here
gives a much more precise understanding of how to compute the corresponding BPS degeneracies
$\Omega(\gamma)$ than was previously available.
It also provides a geometric argument (if not quite a proof) that the degeneracies so computed obey the
wall-crossing formula
of Kontsevich-Soibelman \cite{ks1}, as well as its extension to include the coupling between
2d and 4d BPS states, given in \cite{Gaiotto:2011tf}.

This story can be thought of as a broad generalization of
parts of \cite{Gaiotto:2009hg,Gaiotto:2011tf}, where we explained why the counts of finite webs
obey the wall-crossing formulas in the case $K=2$.
In fact, our approach here leads to a simpler and more conceptual understanding
even of that case.

The 4d BPS spectrum of $\N=2$ theories has been investigated by many authors recently; see in particular
\cite{Alim:2011ae,Alim2011a}.
One advantage of our approach here via spectral networks
is that, given a point $u$ of the Coulomb branch,
one can determine any particular BPS degeneracy $\Omega(\gamma)$ at $u$ just by drawing
the network $\wnet_{\vartheta = \arg Z_\gamma}$ corresponding to $u$.
The spectral network also gives more precise information ---
not only the 4d BPS degeneracies $\Omega(\gamma)$ but also some enhancements
$\omega(\gamma, \cdot)$,
which keep track of the interaction between the 4d BPS state and the surface defects
$\bS_z$.

\smallskip
{\bf Moduli of flat connections.}
Suppose we compactify on $S^1$ both the $d=4$ theory and the surface defects $\bS_z$.
The ground states of $\bS_z$ on $S^1$ form a $K$-dimensional vector space $E_z$;
letting $z$ vary we obtain
a rank $K$ vector bundle $E$ over $C$.
Now take a path $\wp$ in $C$ from $z_1$ to $z_2$.
The vacuum expectation value $\inprod{L_{\wp,\vartheta}}$ of the corresponding
interface wrapped on $S^1$ is an isomorphism from $E_{z_1}$ to $E_{z_2}$.
In other words, the bundle $E$ is equipped with a natural connection \cite{Gaiotto:2009fs},
which moreover is actually flat.\footnote{We are oversimplifying slightly here: the precise story,
laid out in the main text,
involves a slight twisting of the notion of flat connection.  This twisting
does not modify the basic picture and can safely be ignored at first.}

On the other hand, we could also take the perspective of the IR (abelian) theory.
From that point of view we would have surface defects
labeled by points on $\Sigma$ rather than on $C$, with $1$-dimensional spaces of vacua,
thus forming a line bundle $\CL$ over $\Sigma$.
Considering interfaces between these surface defects, we see that
$\CL$ too is naturally equipped with a flat connection.

So, to each vacuum of the compactification of the $d=4$ theory
on $S^1$, we have assigned on the one hand a flat rank $K$
connection over $C$, and on the other hand a flat rank $1$ connection over the covering $\Sigma$.
This induces a correspondence $\Psi_{\wnet_\vartheta}$
between the two types of connection, which turns out to be
(at least locally) an isomorphism of moduli spaces.  Moreover, we can compute
$\Psi_{\wnet_\vartheta}$ concretely:  the key is the framed BPS degeneracies mentioned above,
which (roughly) give the coefficients in the expansion of a UV interface $L_{\wp,\vartheta}$
in terms of IR interfaces.  Upon taking expectation values this becomes an expansion
of the vacuum expectation value $\inprod{L_{\wp,\vartheta}}$ in terms of ``Darboux coordinates''
as described e.g. in \S 5.8 of \cite{Gaiotto:2011tf}.
In particular, the correspondence $\Psi_{\wnet_\vartheta}$
is determined by the spectral network $\wnet_\vartheta$.

\smallskip
{\bf Cluster coordinate systems.}
Since the space of flat rank $1$ connections over $\Sigma$
is a product of copies of $\IC^\times$, another way to describe the last item
is to say that $\Psi_{\wnet_\vartheta}$ is a local \ti{coordinate system}
on the moduli space $\CM$ of flat rank $K$ connections over $C$.
The construction of $\Psi_{\wnet_\vartheta}$ from $\wnet_\vartheta$ can be
generalized:  it uses only some general properties of $\wnet_\vartheta$,
which we abstract into a definition of ``spectral network''.  Given any
spectral network $\wnet$ there is a corresponding $\Psi_\wnet$.

We conjecture that $\Psi_{\wnet}$ is a particularly nice coordinate system:
it is a \ti{cluster} coordinate system,
in the sense of \cite{MR2567745}.
Indeed, Fock and Goncharov proved \cite{MR2233852}
that the spaces $\CM$ we consider admit an atlas of cluster coordinate systems.\footnote{This
fact implies e.g. that these spaces admit a natural quantization \cite{MR2567745,qd-cluster}.}
For $K=2$ the cluster atlas
consists precisely of the coordinate systems $\Psi_\wnet$.
For $K>2$, Fock and Goncharov did not give a completely
explicit description of the atlas --- rather they described some particular cluster coordinate
systems.  The most general cluster coordinate system would be obtained by beginning with
one of these and performing some sequence of coordinate transformations
known as ``mutations''; each mutation generates a new coordinate system, and the
cluster atlas is the set of all coordinate systems obtained in this way.
We conjecture that our $\Psi_\wnet$ are coordinate systems in the
cluster atlas.\footnote{Again, here we are glossing over some slight differences between
our setup and that of Fock-Goncharov, and ignoring some extra discrete ``flag data'' attached to
the connections.}

How do the mutations arise in our story?
Small deformations of the spectral network $\wnet$ leave the coordinate
system $\Psi_{\wnet}$ invariant.  However,
there are some natural ``degenerations'' of spectral networks
which interpolate between ``inequivalent''  $\wnet$.  We have already seen these degenerations
in this introduction:  they occur in the families $\wnet_\vartheta$ when the parameter
$\vartheta$ is adjusted to a critical
phase $\vartheta_c$.  When such a degeneration occurs,
$\Psi_{\wnet}$ jumps by an automorphism $\CK$
of the torus of flat rank $1$ connections on $\Sigma$.  This $\CK$ is
simply determined by the degeneracies $\Omega(\gamma)$ read off from the
degenerate network (see \eqref{eq:holonomy-jump} for its explicit form.)
$\CK$ has a form very similar to that of a cluster mutation,
and part of our conjecture is that for the simplest types of degenerations
it is indeed a mutation.

Very recently Goncharov has also defined some new geometric objects which he calls \ti{spectral webs} \cite{goncharov},
and which correspond to coordinate systems in the cluster atlas.  Despite the similar nomenclature, this definition is
different from our definition of spectral networks.  It should be interesting to compare the two constructions.

\smallskip
{\bf WKB expansions and spectral networks as Stokes diagrams.} One of the key tools in \cite{Gaiotto:2009hg} was
the WKB approximation, applied to the $\zeta \to 0$ behavior of
families of flat $SL(2,\IC)$ connections
of the form
\begin{equation}
\nabla(\zeta) = R \frac{\varphi}{\zeta} + D +  R \zeta \bar \varphi.
\end{equation}
Such families are associated with solutions of Hitchin's equations \cite{MR89a:32021}
and naturally arise in theories of class $S$.

Some aspects of the WKB approximation are difficult to generalize
to rank $K>2$, and for a long time this proved a stumbling
block to giving nontrivial illustrations of the general statements
of \cite{Gaiotto:2008cd,Gaiotto:2011tf} in the higher
rank case.  As we briefly explain in \S \ref{subsec:WKB-Asymptotics}, the
spectral networks $\wnet_\vartheta$ in theories of class $S$ appear to be the key missing ingredient
to solve this problem:  they provide a way of constructing a basis of $\nabla(\zeta)$-flat sections in
each connected component of the complement of $\wnet_\vartheta$,
with ``good WKB asymptotics'' as $\zeta \to 0$ in a half-plane ${\mathbb H}_\vartheta$.
Thus, the walls of the spectral networks $\wnet_\vartheta$ also have an
interpretation as Stokes curves.  Similar statements have appeared before
in the mathematical literature, e.g. \cite{MR1209700,MR729194} and especially \cite{MR2132714}
which contains some examples of spectral networks with $K=3$.



\subsection{Open problems}

Our work in this paper leaves many directions unexplored or incompletely explored.  Here are a few:

\begin{enumerate}

\item We discuss the theories $S[\fg, C, D]$ only for $\fg$ of type $A$.
There should be a closely
parallel story for $\fg$ of type $D$ or $E$.  Some parts of this story are easy to predict:
the walls of the spectral networks will be labeled (locally) by roots of $\fg$, and spectral networks will correspond
to coordinate systems on  moduli spaces of $\fg$-connections over $C$.  It would be desirable to work
out this picture in detail.

\item Even in the case of type $A$ our story is not quite complete.
We take the charges of BPS states to be valued in the lattice $\Gamma = H_1(\Sigma;\IZ)$,
but according to the more precise picture in \cite{Gaiotto:2009hg,Gaiotto:2010be},
it is better to identify the charge lattice as a certain subquotient of $H_1(\Sigma;\IZ)$.
This is related to the fact that our nonabelianization map $\Psi_{\wnet_\vartheta}$ most directly
produces connections with structure
group $GL(K,\IC)$, while the physically relevant objects should really be connections with
structure group $SL(K,\IC)$, considered modulo some further discrete equivalences \cite{Gaiotto:2010be}.
There are likely to be some topological subtleties here which deserve careful consideration.

\item Many of the results of \cite{Gaiotto:2009hg} for $K=2$ are subsumed in the present paper and extended to $K>2$.
However, there is one important piece of
\cite{Gaiotto:2009hg} which we have not extended to $K>2$.  Namely, we gave a recipe for computing an object called
the ``spectrum generator,'' which completely determines the whole 4d BPS spectrum of the theory at any point $u$.
This recipe uses only the combinatorics of a single spectral network $\wnet_\vartheta$, for a fixed generic $\vartheta$.
It would be desirable to extend it to the case $K>2$, and also to types $D$ and $E$.
One could further ask for an extension of the spectrum generator to include the 2d spectrum.\footnote{In
the case $K=2$ this has been worked out by Pietro Longhi.}

\item It would be desirable to generalize our discussion of BPS indices to include
information about the spins of the BPS states.  This means taking $y\not=\pm 1$
in the various indices defined below.  Some aspects of the ``motivic 2d-4d wall-crossing
formula'' which governs these degeneracies were spelled out in
\cite{Gaiotto:2011tf}, but important details remain to be filled in.

\item In \S \ref{subsec:PictureSN} we paint a heuristic picture of the ``space of all spectral networks,''
which would be nice to spell out more precisely.

\item We conjecture in \S \ref{subsec:Coord-System}
that the coordinate systems $\Psi_\wnet$ on the space $\CM$ of flat connections
are cluster coordinate systems.  It would be very interesting to prove this conjecture.
It would be even more interesting if it turned out that the $\Psi_\wnet$ actually exhaust the set of cluster coordinate systems.
This might be of some internal
use for the study of cluster varieties, e.g. for the positivity conjectures of \cite{MR2233852}.

\item In this paper we always require that the curve $C$ carries at least one defect $D_n$.
This restriction (which we also imposed in \cite{Gaiotto:2009hg})
leads to some simplifications.  One reason for these simplifications is
that the walls in $\wnet_\vartheta$ are solutions of differential equations, and it seems that
these equations generically imply that each wall is ``attracted'' asymptotically to some
defect.  In particular, any open path $\wp$ on $C$ meets $\wnet_\vartheta$ only finitely many times.

This contrasts sharply with
the case without defects:  in that case, a typical open path on $\wp$
may meet $\wnet_\vartheta$ infinitely many times.
We are hopeful that all of the constructions of this paper still make sense in that setting, but there will
be issues of convergence to consider.

Fortunately, some things can be said about the asymptotic behavior of the walls
even in the case without defects.
For example, in the case $K=2$ the walls in $\wnet_\vartheta$ are horizontal
trajectories of a holomorphic quadratic differential $e^{2 \I \vartheta} \phi_2$,
and the leading
asymptotic behavior of a generic such trajectory is classified by a virtual ``limit cycle'' in $H_1(C, \IR)$, with deviations
governed by certain Lyapunov exponents; see \cite{flat-surfaces} for a very useful review.  One can hope that using these kinds of results
(and their to-be-developed generalizations for $K>2$) it will be possible to extend everything in this paper to the
case without defects.

\item In this paper we mainly work at a generic point of the Coulomb branch, where the gauge
symmetry group in the IR is abelian.  If the parameters at the defects are adjusted carefully (or if there are no defects at all)
there may also be points where the unbroken gauge symmetry is nonabelian.
The physics of this situation is much less explored than the fully abelian case.
Nevertheless, much of what we have said should have an extension to this situation.

In particular, a spectral network $\wnet$ associated to a $K$-fold covering $\Sigma \to C$ should give not only
a map $\Psi_\wnet$ between moduli of flat $GL(1)$ connections on $\Sigma$ and moduli of
flat $GL(K)$ connections on $C$, but more generally a map $\Psi_{\wnet,N}$
between moduli of flat $GL(N)$ connections on $\Sigma$ and moduli of flat $GL(NK)$
connections on $C$.\footnote{One way of thinking about this is that the $K$-fold covering $\Sigma$
could arise as a non-reduced degeneration of an $NK$-fold covering, where the sheets coalesce in
groups of $N$.  Readers who prefer to think in terms of M-theory fivebranes might say that we
consider the theory of $NK$ fivebranes wrapped on $C \subset T^* C$,
and then move to a point of the Coulomb branch represented by $N$ fivebranes wrapped on $\Sigma \subset T^* C$.}
Our construction of $\Psi_\wnet$ in \S\ref{sec:moduli} is set up
in a way that should generalize directly to this setting.
We understand that similar constructions will appear in upcoming work of Goncharov and Kontsevich.

\item In this paper we encounter several tricky sign issues.  One of these
first pops up as an ambiguity in the notion of ``fermion number,'' which leads to an ambiguity in the sign of
the 2d BPS degeneracies, and recurs many times
thereafter.  We have found a scheme for fixing this sign ambiguity, which we use systematically
throughout the paper:  very roughly speaking, it amounts to
considering paths on $C$ and $\Sigma$ weighted by signs which keep track of the parity of
the number of times the tangent direction
to the path winds around the circle.  Our slavish implementation of this scheme
has various consequences,
leading us e.g. to consider \ti{twisted} flat connections on $C$ and $\Sigma$ in \S\ref{sec:moduli} rather than
ordinary flat connections.  (Twisted connections on $C$ also appeared in \cite{MR2233852}, and this was a useful clue which helped us to
find our sign prescription.)
While this scheme leads to a consistent picture both mathematically
and physically, we cannot say that we have really understood from physical first principles \ti{why} it works so well.  It would be very good to have a better understanding of how our sign rule arises from the physics of the six-dimensional theory $S[\fg]$.

\item In this paper we consider spectral networks $\wnet_\vartheta$ associated to a phase $\vartheta$ and a point $u$ of the Coulomb branch.  It is natural to ask whether every spectral network $\wnet$
(modulo the natural notion of equivalence described in \S\ref{subsubsec:EqivalentGSN}) arises as $\wnet_\vartheta$ for some $(u, \vartheta)$.  If the answer is ``no,'' can we classify those spectral networks which do occur?

\item It is natural to ask whether the framed BPS degeneracies can be categorified.
We have done some work along these lines with E. Witten, and we hope to return to it.

\item The networks $\wnet_\vartheta$
we study on $C$ are made up of ``$\CS$-walls,'' the loci where framed 2d-4d BPS state degeneracies jump.
They depend on a point $u$ of the Coulomb branch $\CB$, so really $\wnet_\vartheta = \wnet_\vartheta(u)$
although we usually do not write this dependence
explicitly.
On the other hand, very similar networks $\knet_\vartheta$ appear directly on $\CB$:
they are made up of ``$\CK$-walls,'' the loci where 4d framed BPS state degeneracies jump.
$\knet_\vartheta$ can be studied by methods very similar to the methods we employ here for $\wnet_\vartheta$.
In particular this gives another scheme for computing the pure 4d BPS state degeneracies $\Omega(\gamma)$,
parallel to what we do here for $\mu(a)$.  (This has also been pointed out by Kontsevich-Soibelman.)
Networks very similar to $\knet_\vartheta$ have appeared previously in the mirror symmetry literature,
e.g. \cite{MR2181810,MR2386535,Gross2007,Gross2009,Gross2011}.

The family of networks $\wnet_\vartheta(u)$ on $C$ and the single network $\knet_\vartheta$ on $\CB$
can be unified into a network $\knet\wnet_\vartheta$ on $\CB \times C$.  We believe that this
is really the most natural perspective, although we do not adopt it explicitly in this paper.

\item We give a recipe for determining the BPS degeneracies $\Omega(\gamma)$ from a degenerate
spectral network, and work out several examples, but not many.
It would be interesting to use spectral networks to study the spectrum of concrete theories, beyond
the few examples we consider in \S\ref{sec:Examples}.
One obvious possibility would be to consider the standard $SU(K)$ gauge theories coupled to
fundamental hypermultiplets.  Even the BPS spectrum of the pure $SU(3)$ theory has been the source of
some controversy; in this paper we study it at strong coupling but do not analyze the more intricate
weak-coupling spectrum.  It would be interesting to compare results obtained from
spectral networks with those in \cite{Fraser:1996pw,Taylor:2001hg,Taylor:2002sg,Chen:2011gk}.

\item In the degenerate spectral networks we do examine we do not
work out any example where the resulting $\abs{\Omega(\gamma)} > 2$, which would suggest
the possibility of higher spin states in the BPS spectrum.  It would be interesting to find
a degenerate spectral network which gives such higher spin states.

\item In this paper we have made some
significant progress in the determination of BPS spectra for a large class of $\N=2$
field theories. We hope that these techniques can shed light on some broader
questions of general interest, such as to what extent the BPS spectrum uniquely
determines a theory, and whether one can always engineer a theory to produce
a desired (consistent) BPS spectrum.

\end{enumerate}

Finally, we mention that in a companion paper \cite{gmn6-to-appear} we
apply the techniques of this paper to make a more direct connection to the
work of Fock and Goncharov on higher Teichm\"uller theory \cite{MR2233852}.
We also find a formula for the spectrum generator for a special class of spectral networks,
valid for all $K \geq 2$; this gives an implicit determination of the BPS spectrum
in the corresponding theories.
