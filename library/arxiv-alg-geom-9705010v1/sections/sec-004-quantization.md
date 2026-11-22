---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-004-quantization
section_title: "Quantization"
section_number: null
pages: 5-8
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
Quantization is an art form which, when applied to classical physical theo-
ries, yields predictions of subatomic behavior which are in spectacular agreement
with experiments. The quantization of the classical mechanics of particles leads
to quantum mechanics, which can be described, in a Hamiltonian approach, via
operators and rays in Hilbert space, or in a Lagrangian formulation, via path in-
tegrals. Quantization of continuous ﬁelds leads to QFT: quantum ﬁeld theory. It
has a Hamiltonian formulation, where the Hilbert space is replaced by the “larger”
Fock space, as well as a Lagrangian formulation, based on averaging the action
(= exp of the Lagrangian) over “all possible histories” via path integrals. These
are generally ill-deﬁned integrals over inﬁnite-dimensional spaces.
Nevertheless,
there exist powerful tools for expanding them perturbatively, as power series in
some “small” parameters such as Planck’s constant, around a point corresponding
to a “free” limit where the integral becomes Gaussian and can be assigned a value.
(Actually, in modern QFT the “small parameters” used are often taken to be di-
mensionless coupling constants rather than Planck’s constant.) The coeﬃcients of
the expansion are ﬁnite dimensional integrals encoded combinatorially as Feynman
diagrams. These power series typically diverge and need to be “regularized” and
“renormalized”. These processes are somewhat akin to the way we make the Weier-
strass P-function converge, by subtracting a correction term from each summand
in an inﬁnite series: a ﬁrst attempt to write down a doubly periodic meromorphic
function in terms of an inﬁnite series of functions leads, unfortunately, to an every-
where divergent series; nevertheless we can obtain a series which does converge, and
indeed to a doubly periodic meromorphic function, by subtracting an appropriate
constant from each term. A physicist might say that we “cancelled the inﬁnity” of
the original series by subtracting “an inﬁnite constant”. In any case, it is some of
these renormalized values which are conﬁrmed to amazing accuracy by experiment,
providing physicists with unshakable conﬁdence in the validity of the technique.
For a physicist, a “theory”, either classical or quantum, is usually speciﬁed
by its Lagrangian L, a functional given by integration over the underlying space
X of a Lagrangian density L, which is a local expression involving the values and
6
RON Y. DONAGI
derivatives of a given collection of ﬁelds. The classical theory considers extrema of
L, while the quantum theory averages the action over all possible ﬁelds. The largest
weight is thus still assigned to the extrema of L, but all “quantum ﬂuctuations”
around the extrema are now included. The Lagrangian density typically consists
of a quadratic part, plus higher order terms which in a perturbative approach
are interpreted as small perturbations. In a theory consisting of scalar ﬁelds ϕi,
the quadratic term might be P
i(|dϕi|2 + m2
i ϕ2
i ), where mi are the masses.
A
perturbation might include terms like gIϕI, where I = (i1, . . . , ik) is a multiindex,
and gI is a (supposedly small) coupling constant giving the strength of an interaction
involving the k ﬁelds ϕi, i ∈I. (Other types of theories might involve also some
ﬁelds which are vectors or spinors with respect to the Poincare group.) A typical
quantity to be computed is the n-point function
⟨x1, . . . , xn⟩:=
Z
ϕ(x1) . . . ϕ(xn) exp iL(ϕ)Dϕ,
where integration is over the inﬁnite-dimensional space of all ϕ’s, with respect to a
(non-existent) measure Dϕ, and L(ϕ) :=
R
X L(ϕ).
A formal approach to this integral is to interpret it as a power series in the
coupling constants. Terms of the expansion are described by Feynman diagrams.
The types of edges in a diagram correspond to the types of ﬁelds in the theory. The
vertex types correspond to the multiindices I with non-zero gI. A ϕ4 term thus
corresponds to a vertex where four ϕ edges meet (this may represent two incoming
particles which collide and scatter away), while a ϕψ ¯ψ vertex can represent an
electron ψ annihilating a positron ¯ψ to produce a photon ϕ. The Feynman rules
assign to each diagram a 4ℓdimensional integral, where ℓis the number of loops,
i.e. ﬁrst Betti number, of the diagram, and 4 is the dimension of space-time: the
integration is over all ways of assigning a momentum (a 4-vector) to each oriented
edge, subject to Kirchhoﬀ’s law of null-sum at each vertex.
The integrand for
each diagram is the product over all edges of a basic function (the propagator)
of the momentum assigned to that edge, times a factor involving the coupling
constant gI at each vertex of type I, and an overall numerical factor accounting
for graph automorphisms. The n-point function, or rather its Fourier tranform, is
then expanded as the sum of all possible diagram integrals with n external legs.
One problem is that some of these Feynman integrals may be divergent. Of
course, even if they converge individually, their sum may not. So the individual
integrals need to be regularized, and the entire theory needs to be renormalized.
A theory is said to be superrenormalizable if all divergences in it disappear after
a ﬁnite number of its divergent diagrams are made ﬁnite by adjusting some of
the parameters.
In a renormalizable theory there are inﬁnitely many divergent
diagrams, but they can all be renormalized by iteratively adjusting the values of just
a ﬁnite collection of parameters. There is an easily veriﬁable necessary condition
for renormalizability: each ﬁeld ϕ carries a certain dimensionality [ϕ]. (This is
measured in powers of the mass; time and distance are converted to mass-inverse
by setting the speed of light c and Planck’s constant h to 1.) Now L, which occurs
as an exponent, must have no dimensionality (it is a pure number, independent
of units), so each term in L must have dimensionality 4.
This determines the
dimensionality of each gI. The obvious necessary condition for renormalizability
is that [gI] ≥0 for all I: otherwise, the insertion of a vertex of type I in an
already divergent diagram will give a new diagram with divergence which is worse.
SEIBERG-WITTEN INTEGRABLE SYSTEMS
7
Similarly, a necessary condition for superrenormalizability is that [gI] > 0 for all
I, since otherwise insertions into one divergent diagram would yield others with
equally bad divergence. These conditions serve to point out the very few candidates
for renormalizable theories. Actually proving renormalizability in each case tends
to be much harder.
For regularization, we introduce an auxiliary variable Λ so that the integral
can be interpreted as (the “limit” of) a function of Λ going to inﬁnity with Λ.
For example, Λ can be a momentum cutoﬀ, meaning that the integral is carried
out only over the ball of momenta p satisfying |p| ≤Λ.
(Or better, use some
approximation of unity by smooth compactly supported cutoﬀfunctions.) Another
popular variation is dimensional regularization: one writes down the expression
for a given integral in a d-dimensional space, and observes that the answer is an
analytic function in d for suﬃciently small d, typically acquiring a singularity at
the relevant dimension d = 4. The analogue of Λ in this version is exp
1
4−d.
The modern approach to renormalization is based on the renormalization group
ﬂow. Very crudely, one might illustrate this process as follows. The integral for
each diagram D translates into a function fD(m, g, p, Λ) of the masses, coupling
constants, external momenta and cutoﬀ(or whatever else we used for Λ). If the
number of divergent diagrams is ﬁnite (and ≤the number of parameters in L) then
the simultaneous level sets of the corresponding fD will be (or will contain) a family
of curves on which Λ is unbounded. So we may hope to ﬁnd a ﬂow parametrized
by Λ along these curves:
m = m(Λ), g = g(Λ), p = p(Λ).
In a general renormalizable theory there may be inﬁnitely many fD, but each may
be modiﬁed (by a quantity which is bounded as a function of Λ) so there is still a
ﬂow tangent to all of them. Instead of attempting to ﬁx the parameters at their
“bare” values and taking Λ to inﬁnity, renormalization is accomplished by ﬂowing
along this renormalization group ﬂow. The eﬀective, physically measurable value of
the parameters thus varies with the scale Λ. Similar phenomena are rather common
in statistical physics. For example, the electric charge of a particle in a dielectric
appears to be reduced, or screened, with distance, as a result of the alignment of
the dielectric’s charges around it. In QFT this occurs even in vacuum, because of
the quantum ﬂuctuations.
A famous series of experiments at the Stanford Linear Accelerator showed that,
when bombarded by very high energy electrons, a proton behaves as if it is made
of three separate subparticles (quarks) which move freely within it.
Yet at low
energies (or equivalently, as viewed on a larger distance scale), the quarks are
conﬁned within the proton. A major success of QFT was its interpretation of these
results in terms of the varying coupling constant g for the strong force. The relevant
theory (QCD: quantum chromodynamics) is asymptotically free, which means that
g →0 as Λ →∞, and g →∞as Λ →0. Thus at high energy scale Λ, the quarks
behave as if g = 0, i.e. as in the free theory, while at large distance Λ →0 the force
becomes stronger and is presumably suﬃcient to conﬁne the quarks. (This last point
is not rigorously proved; Seiberg and Witten obtained a model for conﬁnement in
the supersymmetric analogue.)
An often computable quantity which describes the behavior of a coupling con-
stant is its beta function, β := Λ∂g/∂Λ. An asymptotically free theory corresponds
8
RON Y. DONAGI
to β < 0 for small values of g. In the boundary case where β is identically 0, the
theory is scale-invariant.
An additional complication is involved in the quantization of theories which are
(that is, their Lagrangian is) gauge-invariant. The problem with gauge-invariant
theories stems from the degeneracy of their Lagrangian. In classical gauge theory,
the classical solutions (extrema of the action) are not isolated, but come in entire
gauge-group orbits. The equivalence of the Lagrangian and Hamiltonian descrip-
tions breaks down: this equivalence is based on a Legendre transform, which makes
sense only near isolated points. In the quantized theory, the path integral needs
to be taken not over all paths, but over gauge-equivalence classes. This is seen
already for the free (unperturbed) theory: the value of a Gaussian integral is given
by the inverse determinant of the operator in the exponent; degeneracy (or gauge
invariance) implies that this determinant vanishes, and needs to be replaced by a
determinant on an appropriate transversal slice or quotient. For quantized Yang-
Mills, or gauge, theories, a good reference is [FS]. The reward for handling these
additional complications is a collection of theories which are renormalizable and
sometimes asymptotically free: the beta-function of the basic theory (correspond-
ing to Maxwell’s in vacuo) is negative. The coupling to matter increases beta, but
it remains negative when the number of quarks is small enough.
