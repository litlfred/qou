---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-004-6-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 6
pages: 6-8
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
derivatives of a given collection of ﬁelds. The classical th eory considers extrema of
L, while the quantum theory averages the action over all possi ble ﬁelds. The largest
weight is thus still assigned to the extrema of L, but all “quantum ﬂuctuations”
around the extrema are now included. The Lagrangian density typically consists
of a quadratic part, plus higher order terms which in a pertur bative approach
are interpreted as small perturbations. In a theory consist ing of scalar ﬁelds ϕi,
the quadratic term might be ∑
i(|dϕi|2 +m2
iϕ2
i ), where mi are the masses. A
perturbation might include terms like gIϕI , where I = (i1,...,i k) is a multiindex,
andgI is a (supposedly small) coupling constant giving the strength of an interaction
involving the k ﬁelds ϕi,i ∈ I. (Other types of theories might involve also some
ﬁelds which are vectors or spinors with respect to the Poinca re group.) A typical
quantity to be computed is the n-point function
⟨x1,...,x n⟩:=
∫
ϕ(x1)...ϕ (xn) expiL(ϕ)Dϕ,
where integration is over the inﬁnite-dimensional space of allϕ’s, with respect to a
(non-existent) measure Dϕ, and L(ϕ) :=
∫
X L(ϕ).
A formal approach to this integral is to interpret it as a powe r series in the
coupling constants. Terms of the expansion are described by Feynman diagrams.
The types of edges in a diagram correspond to the types of ﬁeld s in the theory. The
vertex types correspond to the multiindices I with non-zero gI. A ϕ4 term thus
corresponds to a vertex where four ϕ edges meet (this may represent two incoming
particles which collide and scatter away), while a ϕψ ¯ψ vertex can represent an
electron ψ annihilating a positron ¯ψ to produce a photon ϕ. The Feynman rules
assign to each diagram a 4 ℓ dimensional integral, where ℓ is the number of loops,
i.e. ﬁrst Betti number, of the diagram, and 4 is the dimension of space-time: the
integration is over all ways of assigning a momentum (a 4-vec tor) to each oriented
edge, subject to Kirchhoﬀ’s law of null-sum at each vertex. T he integrand for
each diagram is the product over all edges of a basic function (the propagator )
of the momentum assigned to that edge, times a factor involvi ng the coupling
constant gI at each vertex of type I, and an overall numerical factor accounting
for graph automorphisms. The n-point function, or rather it s Fourier tranform, is
then expanded as the sum of all possible diagram integrals wi th n external legs.
One problem is that some of these Feynman integrals may be div ergent. Of
course, even if they converge individually, their sum may no t. So the individual
integrals need to be regularized, and the entire theory needs to be renormalized.
A theory is said to be superrenormalizable if all divergences in it disappear after
a ﬁnite number of its divergent diagrams are made ﬁnite by adj usting some of
the parameters. In a renormalizable theory there are inﬁnitely many divergent
diagrams, but they can all be renormalized by iteratively ad justing the values of just
a ﬁnite collection of parameters. There is an easily veriﬁab le necessary condition
for renormalizability: each ﬁeld ϕ carries a certain dimensionality [ ϕ]. (This is
measured in powers of the mass; time and distance are convert ed to mass-inverse
by setting the speed of light c and Planck’s constant h to 1.) Now L, which occurs
as an exponent, must have no dimensionality (it is a pure numb er, independent
of units), so each term in L must have dimensionality 4. This determines the
dimensionality of each gI . The obvious necessary condition for renormalizability
is that [ gI ] ≥ 0 for all I: otherwise, the insertion of a vertex of type I in an
already divergent diagram will give a new diagram with diver gence which is worse.
SEIBERG-WITTEN INTEGRABLE SYSTEMS 7
Similarly, a necessary condition for superrenormalizabil ity is that [ gI ] > 0 for all
I, since otherwise insertions into one divergent diagram wou ld yield others with
equally bad divergence. These conditions serve to point out the very few candidates
for renormalizable theories. Actually proving renormaliz ability in each case tends
to be much harder.
For regularization, we introduce an auxiliary variable Λ so that the integral
can be interpreted as (the “limit” of) a function of Λ going to inﬁnity with Λ.
For example, Λ can be a momentum cutoﬀ, meaning that the integ ral is carried
out only over the ball of momenta p satisfying |p| ≤ Λ. (Or better, use some
approximation of unity by smooth compactly supported cutoﬀ functions.) Another
popular variation is dimensional regularization: one writ es down the expression
for a given integral in a d-dimensional space, and observes that the answer is an
analytic function in d for suﬃciently small d, typically acquiring a singularity at
the relevant dimension d = 4. The analogue of Λ in this version is exp 1
4−d .
The modern approach to renormalization is based on the renormalization group
ﬂow . Very crudely, one might illustrate this process as follows . The integral for
each diagram D translates into a function fD(m,g,p, Λ) of the masses, coupling
constants, external momenta and cutoﬀ (or whatever else we u sed for Λ). If the
number of divergent diagrams is ﬁnite (and ≤ the number of parameters in L) then
the simultaneous level sets of the corresponding fD will be (or will contain) a family
of curves on which Λ is unbounded. So we may hope to ﬁnd a ﬂow par ametrized
by Λ along these curves:
m =m(Λ) ,g =g(Λ) ,p =p(Λ) .
In a general renormalizable theory there may be inﬁnitely ma nyfD, but each may
be modiﬁed (by a quantity which is bounded as a function of Λ) s o there is still a
ﬂow tangent to all of them. Instead of attempting to ﬁx the par ameters at their
“bare” values and taking Λ to inﬁnity, renormalization is ac complished by ﬂowing
along this renormalization group ﬂow. The eﬀective, physic ally measurable value of
the parameters thus varies with the scale Λ. Similar phenome na are rather common
in statistical physics. For example, the electric charge of a particle in a dielectric
appears to be reduced, or screened, with distance, as a result of the alignment of
the dielectric’s charges around it. In QFT this occurs even i n vacuum, because of
the quantum ﬂuctuations.
A famous series of experiments at the Stanford Linear Accele rator showed that,
when bombarded by very high energy electrons, a proton behav es as if it is made
of three separate subparticles (quarks) which move freely w ithin it. Yet at low
energies (or equivalently, as viewed on a larger distance sc ale), the quarks are
conﬁned within the proton. A major success of QFT was its inte rpretation of these
results in terms of the varying coupling constant g for the strong force. The relevant
theory (QCD: quantum chromodynamics) is asymptotically free, which means that
g → 0 as Λ → ∞ , and g → ∞ as Λ → 0. Thus at high energy scale Λ, the quarks
behave as if g = 0, i.e. as in the free theory, while at large distance Λ → 0 the force
becomes stronger and is presumably suﬃcient to conﬁne the qu arks. (This last point
is not rigorously proved; Seiberg and Witten obtained a mode l for conﬁnement in
the supersymmetric analogue.)
An often computable quantity which describes the behavior o f a coupling con-
stant is its beta function,β := Λ ∂g/∂ Λ. An asymptotically free theory corresponds
