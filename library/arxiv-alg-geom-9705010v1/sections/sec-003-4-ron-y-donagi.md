---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-003-4-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 4
pages: 4-6
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
isometries of ( X,g ). When dim X = 4, the equations are also invariant under
the duality F ↦→ ∗F . When X = R4 with the Minkowski metric, this duality
interchanges the electric and magnetic ﬁelds. The group of i sometries in this case
is the Poincare group, an extension of the Lorentz group SO(3 , 1) of rotations by
the group ( R4, +) of translations.
Geometrically, we ﬁx a U (1)-bundleL onX and consider a connection A onL
as a new variable. The ﬁrst equation dF = 0 is interpreted as saying that (locally)
F =dA is the curvature. The remaining equation then is d ∗dA = 0. The group of
isometries of the triple (X,g,L ) acts on the connections and preserves the equation.
This is an extension of the group of those isometries of ( X,g ) which preserve L by
the gauge group ofC∞ maps from X toU (1). The duality is still there, but is now
hidden.
Now impose an external ﬁeld j. (In R4, j is a 3-form whose dx∧dy∧dz com-
ponent is the charge density, while the other 3 components gi ve the current.) The
equations become
dF = 0, d ∗F =j,
and duality is lost. Geometrically, once we think of F as curvature, the ﬁrst equation
becomes a tautology (the Bianchi identity), while the secon d is an extra condition
which may or may not hold. Physically, we explain this asymme try as due to the
absence of magnetic charges (“monopoles”).
Dirac proposed that some magnetic charges can be introduced by changing the
topology, or allowing singularities. For example, a monopo le at the origin of R3 is
represented by a U (1)-bundle on ( R3
x,y,z /integerdivide0) × Rt. Such bundles are characterized
topologically by their Chern class c1 ∈ Z, and this c1 is interpreted as the magnetic
charge at the origin. Indeed, the “magnetic charge” at the or igin is just the total
magnetic ﬂux across a small sphere S2 around the origin in R3; this is the integral
overS2 ofB, which equals the integral of F , which is c1. We can extend F to R4 as
a distribution, but now dF is the δ-functionc1.δx,y,z instead of dF = 0. This is not
yet suﬃcient to restore the symmetry to Maxwell’s equations : the electric charge
is arbitrary, but the magnetic charge is allowed only in disc rete “quanta”. This
does raise the possibility, though, that complete symmetry could be restored in a
quantum theory, where, as in the real world, electric charge also comes in discrete
units. Indeed, Dirac discovered that in quantum mechanics, where an electrically
charged particle is represented by a wave function satisfyi ng Schrodinger’s equation,
the electric charge e of one particle and the magnetic charge g of another (in
appropriate units) satisfy eg ∈ Z . This has the curious interpretation that all
electric charges are automatically quantized as soon as one magnetic monopole
exists somewhere in the universe.
In [ MO], Montonen and Olive conjectured that in certain supersymm etric
Yang-Mills quantum ﬁeld theories the electric-magnetic du ality is indeed restored.
This involves an extension of the basic picture in three sepa rate directions: replac-
ing the “abelian” Maxwell equations by the non-abelian Yang -Mills; quantizing the
classical theory; and adding supersymmetry to the Poincar´ e invariance.
Y ang-Mills theory
Yang-Mills theory is quite familiar to mathematicians. It i nvolves replacing the
structure groupU (1) by an arbitrary reductive group G. We thus have a connection
A on some G-bundleV over our fourfold X, the curvature is now the ad( V )-valued
two-formdA + 1
2 [A,A ], and the equations are as before, dF = 0, d ∗F = 0, except
SEIBERG-WITTEN INTEGRABLE SYSTEMS 5
that the covariant derivative d =dA on ad(V ) now replaces the exterior derivative
d on the trivial bundle ad( L).
These equations can be, and usually are, considered as varia tional equations
for the Lagrangian
L(A) :=
∫
X
Tr(F ∧ ∗F ),
where the trace Tr can be any non-degenerate invariant pairi ng on the Lie algebra
g of G. This Lagrangian is considered as a functional on an appropr iate space
of connections A (if X is not compact, we must impose some decay condition at
inﬁnity for the integral to converge). The equation dF = 0 is again the Bianchi
identity, while d ∗F = 0 is the equation of the critical locus of L. Either from the
Lagrangian description or directly from the equations, it i s clear that the symmetry
group includes global isometries of X which lift to V (“the Poincare group”) as well
as local diﬀeomorphisms of the bundle (“the gauge group”) an d, in dimension 4,
the duality F ↦→ ∗F . In the original model of Yang and Mills, the group G was
SU(2), while in QCD it is SU(3). For any “realistic” model of a ll of particle physics,
G would need to contain at least U (1) × SU(2) × SU(3).
Quantization
Quantization is an art form which, when applied to classical physical theo-
ries, yields predictions of subatomic behavior which are in spectacular agreement
with experiments. The quantization of the classical mechan ics of particles leads
to quantum mechanics, which can be described, in a Hamiltoni an approach, via
operators and rays in Hilbert space, or in a Lagrangian formu lation, via path in-
tegrals. Quantization of continuous ﬁelds leads to QFT: qua ntum ﬁeld theory. It
has a Hamiltonian formulation, where the Hilbert space is re placed by the “larger”
Fock space, as well as a Lagrangian formulation, based on ave raging the action
(= exp of the Lagrangian) over “all possible histories” via p ath integrals. These
are generally ill-deﬁned integrals over inﬁnite-dimensio nal spaces. Nevertheless,
there exist powerful tools for expanding them perturbative ly, as power series in
some “small” parameters such as Planck’s constant, around a point corresponding
to a “free” limit where the integral becomes Gaussian and can be assigned a value.
(Actually, in modern QFT the “small parameters” used are oft en taken to be di-
mensionless coupling constants rather than Planck’s const ant.) The coeﬃcients of
the expansion are ﬁnite dimensional integrals encoded comb inatorially as Feynman
diagrams. These power series typically diverge and need to b e “regularized” and
“renormalized”. These processes are somewhat akin to the wa y we make the Weier-
strass P-function converge, by subtracting a correction term from e ach summand
in an inﬁnite series: a ﬁrst attempt to write down a doubly per iodic meromorphic
function in terms of an inﬁnite series of functions leads, un fortunately, to an every-
where divergent series; nevertheless we can obtain a series which does converge, and
indeed to a doubly periodic meromorphic function, by subtra cting an appropriate
constant from each term. A physicist might say that we “cance lled the inﬁnity” of
the original series by subtracting “an inﬁnite constant”. I n any case, it is some of
these renormalized values which are conﬁrmed to amazing acc uracy by experiment,
providing physicists with unshakable conﬁdence in the vali dity of the technique.
For a physicist, a “theory”, either classical or quantum, is usually speciﬁed
by its Lagrangian L, a functional given by integration over the underlying spac e
X of a Lagrangian density L, which is a local expression involving the values and
