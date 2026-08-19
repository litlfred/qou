---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-008-24-surgeries-triangulations-and-atiyah-floer
section_title: "Surgeries, triangulations, and Atiyah-Floer"
section_number: 2.4
pages: 16-18
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In order to give a mathematical formulation of the homological invariants that can be useful for
practical calculations on an arbitrary 3-manifold, the starting point must be a construction
of the 3-manifold itself. Then, diﬀerent ways to present the same 3-manifold may lead to
diﬀerent but equivalent deﬁnitions ofHa[M3] which, in physics, correspond to diﬀerent ways
of looking at the ﬁvebrane system ( 2.13).
For example, in addition to its original combinatorial deﬁnition [12], the Khovanov ho-
mology of knots by now has deﬁnitions based on matrix factorizations [13], algebraic geom-
etry [37], symplectic geometry [38–40], etc. As expected, they are all equivalent [41, 42] and
oﬀer diﬀerent useful perspectives. Similarly, we expect that our homological invariantsHa[M3]
of 3-manifolds admit several mathematical deﬁnitions, thus providing new opportunities and
bridges among diﬀerent areas of mathematics.
A standard way to produce a symplectic deﬁnition is based on the Atiyah-Floer conjec-
tures, which relate gauge theory version of Floer homology and its symplectic version (see
e.g. [17] for a review and an application in a closely related context). The idea is to represent
a 3-manifold M3 as a Heegaard decomposition
M3 = M−
3 ∪ΣM +
3 (2.26)
of two handlebodies M±
3 joined by a long “neck” ∼= R× Σ. Then, topological reduction on
Σ gives a 2d sigma-model with target space M(G, Σ) and space-time (“world-sheet”) R×I,
with the boundary conditions B± at the end-points of the interval I determined by M±
3 .
Then, the Floer homology of the higher-dimensional theory can be equivalently formulated
as a symplectic Floer homology in the topological A-model with target space M(G, Σ) and
– 15 –
two Lagrangian submanifoldsB+ andB−:
Ha[M3] = HF∗
symp(B+,B−). (2.27)
As with other candidates for the mathematical deﬁnition of Ha[M3], the main challenge is
to describe precisely the moduli spaces M(G, Σ) andB±. For example, to obtain M(G, Σ)
it is convenient to ﬁrst reduce 6d (0 , 2) theory on Σ times the circle ﬁber of D2 to obtain
a sigma-model with target space Mﬂat(GC, Σ)∼=MH(G, Σ), the Hitchin moduli space (in
whichM +
3 and M−
3 cut out holomorphic Lagrangian submanifolds).
Another way to build 3-manifolds is to start with a simpler 3-manifold, say 3-sphere,
remove a tubular neighborhood of some knot (or link) and then glue it back in a diﬀerent
way. This operation is called surgery and, in fact, every 3-manifold can be realized as a
sequence of surgery operations on a 3-sphere S3. In view of this, it is natural to ask if 3-
manifold homologyHa[M3] of the resulting manifold M3 is related to homology of knots and
links.
As is well known in the theory of quantum group invariants, at the decategoriﬁed level
the answer is “yes” and here we argue that this is also true at the homological level. Indeed,
a quantum group invariant (WRT invariant) of a 3-manifoldM3 obtained by surgery on K is
completely determined by polynomial invariants ofK, with a proviso that one needs to know
all colored invariants of K. In the case of G = SU (2) these are colored Jones polynomials
and to obtain the WRT invariant ofM3 one basically need to sum over color (which is typical
for any state sum type models).
Since at present all colored polynomial invariants of K have rigorous mathematical def-
inition one could try to write a surgery formula where colored Jones polynomials of K are
replaced by the corresponding homologies (or their Poincar´ e polynomials). Surprisingly, in a
few examples that we checked this indeed gives the 3-manifold homology Ha[M3], and it is
natural to conjecture that this is true in general. If so, one extremely concrete, mathemati-
cally well-deﬁned and computable deﬁnition ofHa[M3] could be via surgery formula and sum
over colored knot (link) homologies.
As a concrete example, consider a Lens space M3 = L(p, 1) constructed as a surgery
on the unknot. In fact, this also gives an example of genus-1 Heegaard splitting since the
unknot complement is a solid torus. Let Pn(q,t ) be the Poincar´ e polynomial of n-colored
sl(2) homology categorifying then-colored Jones polynomial Jn(q). As usual, it is convenient
to package all Pn(q,t ) in a single function F (x;q,t ) such that
Pn(q,t ) = F (x;q,t )|x=qn. (2.28)
Put diﬀerently, if ˆA(ˆx,ˆy;q,t ) is the operator that generates recursion relation among Pn(q,t ),
such that ˆxPn(q,t ) =qnPn(q,t ) and ˆyPn(q,t ) =Pn+1(q,t ), then [43,44]:
ˆAF (x;q,t ) = 0 . (2.29)
In terms of the function F (x;q,t ) that packages Poincar´ e polynomials of colored unknot
homology, the Poincar´ e polynomial ofHa[M3], where M3 =L(p, 1), is given by the “Laplace
– 16 –
transform” [22,45,46] of F (x;q,t ),
P (Ha[M3];q,t ) =
∮ dx
2πixF (x;q,t )θ(a)
p (x;q) (2.30)
i.e. by a convolution with the theta-function θ(a)
p (x;q). Note, all the information about ho-
mological grading (that is, t-dependence) comes entirely from F (x;q,t ), i.e. from the colored
unknot homology, and not from the Laplace transform that produces 3-manifold invariant
out of the knot invariant. In other words, categoriﬁcation of the surgery formula aﬀects only
the Jones polynomial part (by replacing it with the Poincar´ e polynomial).
Another way to build 3-manifolds and, therefore, another candidate for constructing
Ha[M3] is based on triangulations. This approach is especially attractive due to its com-
binatorial nature and has been extensively used as a platform for mathematical deﬁnitions
of various supersymmetric partition functions of 3d N = 2 theory T [M3], see e.g. [47–53].
Reducible ﬂat connections, again, are special, for the same reason as before. However, in
partition functions, the non-trivial stabilizer of reducible ﬂat connections works against them
and formally makes their contribution vanish in a Chern-Simons theory with non-compact
gauge group. This has to be contrasted with homological invariants, where redicible solu-
tions produce inﬁnite contributions ( e.g.T+ in Heegaard Floer homology) compared to ﬁnite
contributions of irreducible solutions. This suggests that in partition functions too, both
reducible and irreducible contributions can be seen together if we consider framed gauge
transformations16 and then instead of further dividing by G work equivariantly. To the best
of our knowledge, this has not been done and presents a nice and tractable problem for future
work.17
