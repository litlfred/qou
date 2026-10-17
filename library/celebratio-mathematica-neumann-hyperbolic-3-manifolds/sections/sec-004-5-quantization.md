---
doc_id: celebratio-mathematica-neumann-hyperbolic-3-manifolds
doc_title: "Jump to Bibliography by Stavros Garoufalidis and Don Zagier Published: 2023"
section_id: sec-004-5-quantization
section_title: "Quantization"
section_number: 5
pages: 12-16
source_pdf: Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds.pdf
source_sha256: 9e541693c60cbd3f
toc_source: inferred
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
nections to number theory described in Section 6.
Define an 
 matrix 
 whose rows form a -basis for the lattice
spanned by the edge equations  (1) together with one “peripheral” equation (a
coprime linear combination of the meridian and longitude equations in  (2)) at
each cusp. Then the above cited results in [1] imply that 
 is symmetric and
that 
 has rank 
, meaning that its 
 columns generate 
. Together, these
two statements are equivalent to saying that 
 can be extended to a 
matrix
in 
, meaning that
But in fact the 
 columns of 
 span the lattice 
, which is equivalent to saying
that 
 can be completed to a 
 symplectic matrix over  . (We will call
such a matrix half-symplectic.) This follows from the chain complex defined by
Walter in [2]. Explicitly, for any simplex 
, let 
 be the abelian group generated
by 
 (corresponding to the pairs of opposite edges) subject to the relation
. This is a free abelian group of rank 2, with a canonical nonsin‐
gular, skew-symmetric bilinear form given by ([2], Section 4)
The Neumann chain complex associated to an ideal triangulation is then defined
by
⇧
8/8/26, 4:27 AM
Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds
https://celebratio.org/Neumann_WD/article/1106/
12/27
Here 
 and 
 are the free abelian groups on the unoriented 0- and 1-simplices
(cusps and edges), respectively, and
(sum over the 3-simplices or tetrahedra), while  maps any cusp to the sum of its
incident edges, the 
-component of  of any edge is the sum of the edges of 
that are identified with it, and 
 and 
 are the duals of  and  with respect to
the obvious scalar products on 
 and the symplectic form on  . Walter shows
([2], Theorem 4.1) that the sequence (12) is a chain complex and, at least after
tensoring with 
, is exact except in the middle, where the homology is the
sum of  rank-2 modules isomorphic to 
 
. Note that the
map  is given precisely by the matrix 
 as defined in (1) if we choose
the obvious basis for 
 and the basis of  given by choosing the basis 
 for
every 
. The rest of the proof that 
 is half-symplectic follows easily from the
theorem just quoted and will be left to the reader.
We make two remarks about this. The first is that both the construction of the
chain complex and the statement about its homology were done in [2] also for 3-
manifolds with boundary components of arbitrary genus (so the vertices of 
need not be cusps), and of course also do not require any hyperbolic structure.
The other is that the gluing equations of [1] and the symplectic results of [2] were
extended to arbitrary 
-representations in [e29].
Half-symplectic matrices occur in other contexts, e.g., in connection with Nahm’s
conjecture on the modularity of certain -hypergeometric series, and also lead to a
new description of the Bloch group. Both topics will be discussed in more detail in
Section 6.
5. Quantization
Perhaps the most far-reaching consequences of Walter’s work on the combinator‐
ics of 3-dimensional triangulations have been the applications of the symplectic
structure to quantization.
Recall the definition of 
 for a single tetrahedron 
 as the abelian group
with the symplectic structure  (11). This symplectic structure on each space
 for any ideal tetrahedron 
 leads to an integral Lagrangian subspace of
⇧
8/8/26, 4:27 AM
Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds
https://celebratio.org/Neumann_WD/article/1106/
13/27
the 10-dimensional symplectic space
associated to five tetrahedra 
 that participate in a 2-3 Pachner move.
Roughly speaking, the Lagrangian subspace records the linear relations among the
angles of the five tetrahedra, where the signed sum of the angles around each in‐
terior edge of the Pachner move is zero.
The quantization of this Lagrangian subspace has appeared numerous times in the
mathematics and physics literature, under different names, and has led to interest‐
ing quantum invariants in dimensions 2, 3 and 4. We briefly discuss this now. In
dimension 2, Kashaev and independently Fock–Goncharov [e8], [e17], [e13] used
the above NZ-symplectic structure to study the change of coordinates of ideally
triangulated surfaces under a 2-2 Pachner move. They found that the correspond‐
ing isomorphism of commutative algebras can be described in terms of cluster al‐
gebras, leading to two dual sets of coordinates (the so-called 
-coordinates and
the 
-coordinates) whose quantization leads to a representation of the so-called
Ptolemy groupoid, and in particular of the mapping class group of a punctured
surface, and also of braid groups. These representations are always infinite-dimen‐
sional (because there are no finite square matrices  and  satisfying the relation
), the Hilbert spaces are typically 
 for some  , and the cor‐
responding theory is usually known as quantum Teichmüller theory.
Going one dimension higher, the 
-coordinates of a 3-dimensional ideal triangu‐
lation are nothing but the shapes of the ideal tetrahedra, whereas the 
-coordin‐
ates are the Ptolemy variables of the ideal tetrahedra. The latter are assignments of
nonzero complex numbers to the edges of the ideal triangulation (where identified
edges are given the same variable) that satisfy a system of quadratic equations: a
(suitably) signed sum 
, where 
, 
 and 
 are the Ptolemy
variables of the three pairs of opposite edges. It turns out that the NZ gluing equa‐
tions for shapes are equivalent to the Ptolemy equations (see for instance [e25]),
and this is not only theoretically interesting, but practically, too. The quantization
of the shape and Ptolemy variables of an ideal triangulation uses two ingredients,
the kinematical kernel of Kashaev [e30] and a special function, the Faddeev
quantum dilogarithm that satisfies an integral pentagon identity. According to
Kashaev, the kinematical kernel is nothing but the quantization of the NZ Lag‐
rangian mentioned above. The outcome of this quantization is the existence of to‐
pological invariants of ideally triangulated 3-manifolds, the invariants being ana‐
lytic functions in a cut place 
, expressed in terms of finite-di‐
mensional state integrals whose integrand is often determined by the combinatori‐
⇧
8/8/26, 4:27 AM
Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds
https://celebratio.org/Neumann_WD/article/1106/
14/27
al data of an ideal triangulation, namely its Neumann–Zagier matrices. This con‐
struction, which is often known as quantum hyperbolic geometry, has been axio‐
matized by Kashaev, and uses as input the combinatorial data of an ideal triangu‐
lation together with a self-dual locally compact abelian group with fixed Gaussian,
Fourier kernel and quantum dilogarithm. This then leads to further analytic in‐
variants of 3-manifolds, two examples of which are the Kashaev–Luo–Vartanov
invariants [e28] and the meromorphic 3D-index [e32], for which the LCA groups
are 
 and 
, respectively. It is worth noting that the Andersen–Kashaev
state integrals are conjectured to be the partition function of complex Chern–Si‐
mons theory (i.e., Chern–Simons theory with complex gauge group). The latter is
not known to satisfy the cut-and-paste arguments that the 
 Chern–Simons
theory does, and as a result, one does not have an a priori definition of complex
Chern–Simons theory other than the state integrals, nor a clear reason why the in‐
finite-dimensional path integral localizes to a finite-dimensional one.
Finally, going yet one dimension higher, the five ideal tetrahedra that participate
in a 2-3 Pachner move form the boundary of a single 4-dimensional simplex, a
pentachoron. (Excuse our Greek.) This gives a 4-dimensional interpretation of the
NZ-structure and of the kinematical kernel, and using a complex root of unity,
Kashaev was able to give a tensor invariant under 4-dimensional Pachner moves
and thus construct corresponding topological invariants of closed, triangulated 4-
manifolds at roots of unity [e30]. This concludes our discussion of the kinematical
kernel in dimensions 2, 3 and 4.
In a different direction, mathematical physicists, using correspondence principles
among supersymmetric theories, have came up with unexpected constructions of
various collections of -series with integer coefficients associated to 3-manifolds.
Perhaps the most remarkable of these is the 3D-index of Dimofte, Gaiotto and
Gukov [e23], [e22], where the -series in question, which in this case are indexed
by pairs of integers, were defined explicitly in terms of the NZ-matrices of a suit‐
able ideal triangulation, with their coefficients counting the number of BPS states
of a supersymmetric theory. This DGG 3D-index was subsequently shown [e27] to
be a topological invariant of cusped hyperbolic 3-manifolds, and was also exten‐
ded to a meromorphic function of two variables (in case the boundary of the 3-
manifold is a single torus) whose Laurent coefficients are the DGG index [e32].
A quite different place where the NZ equations appear in quantum topology is in
connection with the Kashaev invariant and Kashaev’s famous Volume Conjecture.
The Kashaev invariant 
 is a computable algebraic number that was defined
for any knot 
 and any positive integer  by Kashaev [e5] in 1995 using ideas of
quantum topology similar to those discussed above, and of which an alternative
definition in terms of the so-called colored Jones polynomial was later found by
⇧
8/8/26, 4:27 AM
Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds
https://celebratio.org/Neumann_WD/article/1106/
15/27
H. Murakami and J. Murakami. The Volume Conjecture [e6] says that the logar‐
ithm of 
 is asymptotically equal to 
 times the hyperbolic volume of
the knot complement 
 whenever 
 is hyperbolic, a very surprising
connection between hyperbolic geometry and 3-dimensional quantum topology
that has given rise to a great deal of subsequent research and has been refined in
many ways and by several authors in connection with complex Chern–Simons
theory. In particular, one has the conjectural sharpening [e16], [e18]
to all orders in 
 as 
, where 
 is a power series in  with algebraic
coefficients that can be computed to any order in any explicit example, e.g.,
for the 
 (figure-8) knot. In [e20], an explicit candidate for this power series is
constructed for any knot as a formal Gaussian integral whose integrand is defined
in terms of the NZ data of an ideal triangulation of 
. It is not yet known beyond
the leading term that the series constructed there is a topological invariant (i.e.,
independent of the choice of triangulation), although this would of course follow
from the conjecture that the asymptotic formula (13) holds with this series. In a
follow-up paper [e31], the construction was extended, still using NZ data in an es‐
sential way, to give an explicitly computable power series 
 for any 
,
with 
, that is expected to be the power series predicted by the quantum
modularity conjecture for knots that we will discuss in the next section.
Finally, it is worth noting that the NZ-equations and their symplectic properties
lead to an explicit quantization of the shape variables, where one replaces each ,
 and 
 by operators that suitably commute. This was carried out by Dimofte
[e21], who defined a quantized version of the gluing equations, a so-called
quantum curve, which is expected to annihilate the partition function of complex
Chern–Simons theory and to be ultimately related to the asymptotics of quantum
invariants.
