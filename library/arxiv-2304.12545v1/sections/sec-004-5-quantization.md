---
doc_id: arxiv-2304.12545v1
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN"
section_id: sec-004-5-quantization
section_title: "Quantization"
section_number: 5
pages: 10-12
source_pdf: 2304.12545v1.pdf
source_sha256: bfc3c2be395b1b2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.99
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
---
\label{sec.6}

Perhaps the most far-reaching consequences of Walter's work on the combinatorics of
3-dimensional triangulations have been the applications of the symplectic structure
to quantization.  

Recall the definition of~$J_\D$ for a single tetrahedron~$\D$ as the abelian group
$\langle e_1,e_2,e_3\mid e_1+e_2+e_3=0\rangle$ with the sympectic structure~\eqref{omega}.
This symplectic structure on each space $J_\Delta \otimes_\BZ \BQ$ for any
ideal tetrahedron~$\Delta$ leads to an integral Lagrangian subspace of the
10-dimensional symplectic space \hbox{$\oplus_{j=1}^5 J_{\Delta_j} \otimes_\BZ\BQ$} associated
to 5 tetrahedra $\Delta_1,\dots,\Delta_5$  that participate in a 2--3 Pachner move.
Roughly speaking, the Lagrangian subspace records the linear relations among the
angles of the five tetrahedra, where the signed sum of the angles around each interior 
edge of the Pachner move is zero. 

The quantization of this Lagrangian subspace has appeared numerous times in the
mathematics and physics literature, under different names, and has led to interesting
quantum invariants in dimensions two, three and four. We briefly discuss this now.
In dimension two, Kashaev and independently Fock-Goncharov~\cite{Kashaev:quantization,FG0,FG} 
used the above NZ-symplectic structure to
study the change of coordinates of ideally triangulated surfaces under a 2--2 Pachner
move. They found that the corresponding isomorphism of commutative algebras can be
described in terms of cluster algebras, leading to two dual sets of coordinates
(the so-called $\mathcal{X}$-coordinates and the $\mathcal{A}$-coordinates) whose
quantization leads to a representation of the so-called Ptolemy groupoid, and in 
particular of the mapping class group of a punctured surface, and also of braid groups.
These representations are always infinite-dimensional (because there are no finite square
matrices $A$ and~$B$ satisfying the relation $AB-BA=I$), the Hilbert spaces are typically
$L^2(\BR^n)$ for some~$n$, and the corresponding theory is usually known as quantum 
Teichm\"uller theory.

Going one dimension higher, the $\mathcal{X}$-coordinates of a 3-dimensional ideal
triangulation are nothing but the shapes of the ideal tetrahedra, whereas the
$\mathcal{A}$-coordinates are the Ptolemy variables of the ideal tetrahedra. The latter
are assignments of nonzero complex numbers to the edges of the ideal triangulation
(where identified edges are given the same variable) that satisfy a system of
quadratic equations: a (suitably) signed sum $ab+cd=ef$ where $(a,b)$, $(b,d)$
and $(e,f)$ are the Ptolemy variables of the three pairs of opposite edges. It turns
out that the NZ gluing equations for shapes are equivalent to the Ptolemy equations
(see for instance~\cite{Ga:ptolemy}), and this is not only theoretically interesting, but
practically, too. The quantization of the shape and Ptolemy variables of an ideal
triangulation uses two ingredients, the kinematical kernel of Kashaev~\cite{Kashaev:4D}
and a special
function, the Faddeev quantum dilogarithm that satisfies an integral pentagon identity.
According to Kashaev, the kinematical kernel is nothing but the quantization of the
NZ Lagrangian mentioned above. The outcome of this quantization is the existence of
topological invariants of ideally triangulated 3-manifolds, the invariants being
analytic functions in a cut place $\BC'=\BC\setminus (-\infty,0]$, expressed in terms
of finite dimensional state integrals whose integrand is often determined by
the combinatorial data of an ideal triangulation, namely its Neumann--Zagier matrices.
This construction, that is often known as quantum hyperbolic geometry, has been
axiomatized by Kashaev, and uses as input the combinatorial data of an ideal triangulation
together with a self-dual locally compact abelian group with fixed Gaussian, Fourier
kernel and quantum dilogarithm.   This then leads to further analytic invariants of
3-manifolds, two examples of which are the Kashaev--Luo--Vartanov invariants~\cite{KLV}
and the meromorphic 3D-index~\cite{GK:mero}, for which the LCA groups are $\BR \times \BR$
and $S^1 \times \BZ$, respectively. It is worth noting that the Andersen--Kashaev state
integrals are conjectured to be the partition function of complex Chern--Simons theory
(i.e., Chern--Simons theory with complex gauge group).
The latter is not known to satisfy the cut-and-paste arguments that the $\mathrm{SU}(2)$
Chern--Simons theory does, and as a result, one does not have an a priori definition
of complex Chern--Simons theory other than the state integrals, nor a clear reason
why the infinite dimensional path integral localizes to a finite-dimensional one. 

Finally, going yet one dimension higher, the five ideal tetrehedra that participate in a
2--3 Pachner move form the boundary of a single 4-dimensional simplex, a pentachoron.
(Excuse our Greek.) This gives a 4-dimensional interpretation of the NZ-structure and
of the kinematical kernel, and using a complex root of unity, Kashaev was able to give
a tensor invariant under 4-dimensional Pachner moves and thus construct corresponding
topological invariants of closed, triangulated 4-manifolds at roots of
unity~\cite{Kashaev:4D}. This concludes our discussion of the kinematical kernel in 2, 3
and~4 dimensions.

In a different direction, mathematical physicists, using corresondence principles among
supersymmetric theories, have came up with unexpected constructions of various collections
of \hbox{$q$-series} with integer coefficients associated to 3-manifolds.  Perhaps the most
remarkable of these is the 3D-index of Dimofte--Gaiotto--Gukov \cite{DGG1,DGG2}, where
the $q$-series in question, which in this case are indexed by pairs of integers,
were defined explicitly in terms of the NZ-matrices of a suitable ideal
triangulation, with their coefficients counting the number of BPS states of a supersymmetric
theory. This DGG 3D-index was subsequently shown~\cite{GHRS} to be a topological 
invariant of cusped hyperbolic 3-manifolds, and was also extended to 
a meromorphic function of two variables (in case the boundary of the 3-manifold is a 
single torus) whose Laurent coefficients are the DGG index~\cite{GK:mero}.

A quite different place where the NZ equations appear in quantum topology is in 
connection with the Kashaev invariant and Kashaev's famous Volume Conjecture.  
The Kashaev invariant $\langle K\rangle_n$ is a computable algebraic number that was
defined for any knot~$K$ and any positive integer~$n$ by Kashaev~\cite{K95} in~1995 using
ideas of quantum topology similar to those discussed above, and of which an alternative
definition in terms of the so-called colored Jones polynomial was later found by
H.~and J.~Murakami.  The Volume Conjecture~\cite{K97} says that the logarithm of
$|\langle K\rangle_n|$ is asymptotically equal to $n/2\pi$ times the hyperbolic volume
of the knot complement $M=S^3\ssm K$ whenever $M$ is hyperbolic, a very surprising
connection between hyperbolic geometry and 3-dimensional quantum topology that has
given rise to a great deal of subsequent research and has been refined in many ways
and by several authors in connection with complex Chern-Simons theory. In particular,
one has the conjectural sharpening~\cite{Gar:Viet, DGLZ} 
\be
\label{arithmVolConj}
\langle K\rangle_n \;\, \sim  \;\,
n^{3/2}\, e^{\V(K)n/2\pi i}\,\Phi^K\Bigl(\frac{2\pi i}n\Bigr) 
\ee
to all orders in~$1/n$ as~$n\to\infty$, where $\Phi^K(h)$ is a power series in~$h$ with
algebraic coefficients that can be computed to any order in any explicit example, e.g.
\be
\label{as41}
\Phi^{4_1}(h)\=  \frac1{\sqrt[4]{3}}\, 
\Bigl(1 \+ \frac{11}{72\sqrt{-3}}\,h \+ \frac{697}{2\,(72\sqrt{-3})^2}\,h^2
 \+ \frac{724351}{30\,(72\sqrt{-3})^3}\,h^3 \+\cdots\Bigr)\,. 
\ee
for the $4_1$ (figure~8) knot. In~\cite{DG}, an explicit candidate for this power series 
is constructed for any knot as a formal Gaussian integral whose integrand is defined in
terms of the NZ data of an ideal triangulation of~$M$.  It is not yet known beyond the
leading term that the series constructed there is a topological invariant (i.e.,
independent of the choice of triangulation), although this would of course follow from
the conjecture that the asymptotic formula~\eqref{arithmVolConj} holds with this series.
In a follow-up paper~\cite{DG2}, the construction was extended, still using NZ data in
an essential way, to give explicitly computable power series $\Phi_\a^K(h)$ for
any~$\a\in\Q/\Z$, with $\Phi_0^K=\Phi^K$, that is expected to be the power series
predicted by the quantum modularity conjecture for knots that we will discuss in the
next section.

Finally, it is worth noting that the NZ-equations and their symplectic properties
lead to an explicit quantization of the shape variables, where one replaces each
$z$, $z'$ and $z''$ by operators that suitably commute. This was carried out by 
Dimofte~\cite{Dimofte:quantum}, who defined a quantized version of the gluing equations, 
a so-called quantum curve, which is expected to annihilate the partition function 
of complex Chern--Simons theory and to be ultimately related to the asymptotics of
quantum invariants.
