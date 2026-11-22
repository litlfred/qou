---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-009-chern-simons-theory
section_title: "Chern-Simons theory"
section_number: null
pages: 19-23
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Chern-Simons theory
In this section we will briefly review how the model described in the previous section emerges from a
three-dimensional quantum gauge theory. The review will be rather imprecise and its understanding is
not necessary for discussion of the applications in the next section, but it might provide some additional
intuition about the connection between topology, quantum mechanics gauge and conformal field theories
(CFT). The main reference here is the work of Edward Witten on Chern-Simons theory and Jones
polynomials [20]. Further details can be found in lecture notes [62].
Nonabelian Chern-Simons theory with gauge gauge group G (which we will latter assume to be SU(2))
is given by the action
SCS =
k
4π
Z
d3x ϵµνρ tr

Aµ∂νAρ + 2
3AµAνAρ

,
(79)
where the trace is evaluated in the fundamental representation of G. Note that this covariant action is
written without any use of the metric and therefore has vanishing stress-energy tensor, and consequently,
Hamiltonian, according to (54).
The equations of motion of this theory state that the covariant field tensor is zero:
Fµν = 0 ,
(80)
which implies that all the dynamical field configurations are pure gauge. The theory appears to be trivial,
with no physical degrees of freedom.
To make this theory more interesting, one can couple the gauge field to some matter degrees of
freedom. The simplest case is the one of coupling to nondynamical particles, which allows to keep the
theory sufficiently simple, introducing some nontrivial observables at the same time.
One way of doing it is to consider singular gauge transformations. Let us think that the Chern-Simons
theory is defined in the space I × Σ, where I is a time interval and Σ is a closed two-dimensional surface.
In the gauge A0 = 0, the equation of motion, corresponding to the variation with respect to A0, becomes
a constraint F12 = 0, with indices 1 and 2 corresponding to the coordinates on Σ. There are two types
of gauge transformations in the theory. The small gauge transformations are the true ones – they do not
modify the constraint. The large gauge transformations are singular – they can introduce delta-function
sources in the constraint:
k
2π F a
12 =
X
i
T a
(i)δ(2)(x −xi) .
(81)
Here xi are the locations of the pointlike sources, which carry nonabelian charges characterized by the
group generators T a.
This situation is similar to the Aharonov-Bohm effect. The field is zero everywhere except a finite
number of points, where a finite flux of the field is localized. Since Σ is closed the net flux should be zero.
For the abelian case this would correspond to the condition of a zero net charge (on closed Σ all the field
lines should end somewhere). In the nonabelian case zero net charge is generalized to the condition of
the trivial net representation of the group.
Equation (81) can also be obtained from a theory modified by the explicit addition of the sources into
the action:
SCS →SCS +
X
i
Z
γi
Aµ dxµ .
(82)
(Singular gauge transformations essentially add such terms.)
One can canonically quantize Chern-Simons fields on Σ. The classical constraint (81) needs to be
imposed as an operator equation on the Hilbert space. The solution to this quantum constraint reduces
the Hilbert space to a finite dimensional vector space labeled by classes of large gauge transformations,
19
specifically, by the number of the sources on Σ and by the associated representations. As above, the net
representation of the sources is constrained to be trivial.
It is also useful to discuss the path integral quantization of the Chern-Simons theory. Consider the
path integral of a theory defined inside a three-dimensional space M with boundary Σ. If, as before, the
time direction is chosen orthogonally to Σ, then such a path integral can be thought of as producing a
state in a Hilbert space:
Ψ(Σ) =
Z
DA

A(Σ)=AΣeiSCS[M].
(83)
Here the path integral is calculated over field configurations in M satisfying fixed boundary conditions
on Σ. This is the standard state preparation by the Euclidean path integral, although Chern-Simons
theory, being metric independent, does not distinguish between the Euclidean and Minkowski evolution.
Small gauge transformations leave the action, and the boundary conditions invariant. The integral
over such configurations cancels in normalized vectors. Large gauge transformation produce sources and
modify the boundary conditions according to the constraint (81). Let us choose Σ to be a 2-sphere S2.
We will also assume the gauge group to be SU(2) and the representations of all sources to be fundamental.
In the latter case the sources are nondynamical particles with spin j = 1/2.
Consider a boundary condition that prescribes four fundamental sources on Σ. Then space M should
be something like
,
(84)
where the interior of the three-ball contains lines γi connecting the boundary sources. However, some of
the large gauge transformations may preserve the condition (81) but modify the topology of lines γi in a
singular (nonsmooth) way. For example, one may also think of M as
,
(85)
with an alternative way of connecting the sources. Indeed any modification of γ in the coupling term
Z
γ
Aµdxµ
(86)
does not change the action unless another line or another part of γ is crossed.
We conclude that topologically distinct ways of connecting the points on the sphere through its interior
produce a priori distinct quantum states (83). The connection with the one-dimensional TQFT of the
previous section must be clear now. One can establish a map between the two models as follows:
→
,
→
.
(87)
This mapping is not unique and is fixed by ordering the sources on the sphere.
In order to construct a more precise map, and to see that states corresponding to the situation with
four fundamental sources generate a two-dimensional vector space one has to provide more details about
the quantization. It turns out that the action of the Chern-Simons theory with boundary Σ can be
reduced to a two-dimensional action on Σ. The resulting theory is called Wess-Zumino-Witten (WZW)
theory – a well-studied example of a CFT [62–66].
20
For G = SU(2) the spectrum of the WZW theory consists of operators labeled by integrable repre-
sentations of an associated su(2)k Kac-Moody algebra. This is equivalent to saying that the theory on Σ
only has particles with spin j taking half-integer values between 0 and k/2. Moreover, the particles are
subject to the constraint of net zero spin.
Operators in the CFT satisfy the so-called fusion algebra, which is a particular form of the operator
product expansion expressing the product of a pair of operators as an expansion in an appropriate operator
basis:
Φk · Φl = ⊕jN j
klΦj .
(88)
Here Φj represent conformal classes of the operators (operators modulo conformal transformations). In
the WZW theory the basis is provided by the integrable representations, hence the fusion algebra is
similar to the expansion of the tensor product of representations in the basis of the irreducible ones. The
difference is that in the WZW theory only representations with j ≤k/2 are allowed. Numbers N j
kl are
the multiplicities of the representations with spin j. Note that the irreducible representations that appear
multiple times correspond to linearly independent operators.
Because of the net zero spin constraint, the product of all representations on Σ must be projected
on the subspace spanned by the trivial representations. For four spin 1/2 this subspace has dimension
two, in accord with the dimension of the space spanned by diagrams (74). Therefore any three vectors
obtained from a path integral on M with Σ = S2 are linearly dependent. WZW data permit calculating
the coefficients, cf. [20]:3
−q
+ q
+ (q1/2 −q−1/2)
= 0 ,
(89)
where q is determined in terms of the parameter k:
q = exp
 2πi
k + 2

.
(90)
This is a slightly different version of skein relation (25), or rather (27), which directly computes the
Jones polynomial, without taking into account the framing factor. In order to derive (27) one needs to
compensate for the framing factor rescaling the crossings, namely, in (25) and (26) replace
−→−A3
,
−→−A−3
,
(91)
and matching the parameter as follows:
A = q1/4 ,
d = −2 cos

π
k + 2

.
(92)
Note that diagrams (74) can be interpreted as two independent ways of fusing spin 1/2 particles into
singlets. When viewed as evolution, the lines of four spin 1/2 particles coalesce and disappear, which is
interpreted as forming a singlet. An “orthogonal” possibility for the diagram of state |e0⟩∼|0⟩is
|1⟩∼
.
(93)
3This is a SU(2) result. The situation is more complicated in more general cases. See a recent discussion in [67,68].
21
In the latter, two pairs of particles form a spin 1 state instead of the singlet, and the pair of spin 1 states
(dashed line) later annihilate. State |1⟩can be expressed in terms of a pair of non-orthogonal diagrams
according to (77).
When analyzing the Gram matrix of states (74) we observed that it is degenerate if d = −1. For this
value state |1⟩becomes null (has zero norm). On the other hand this value of d corresponds to k = 1,
according to (92). The WZW theory does not have an integrable representation of spin j = 1 in this
case.
For the Temperley-Lieb basis of 2n points the Gram matrix will be degenerate for values of k < n,
in consistence with the integrable representations of the WZW theory. In this case the actual dimension
of the Hilbert space associated with path integral (83) is smaller than the naive dimension given by the
Catalan number Cn. Conversely, if k is kept sufficiently large, one can use Cn as the correct value of
the dimension. One can see that the simple one-dimensional TQFT model of section 3.2 reproduces the
basic features of the WZW CFT.
Diagrams similar to that of state |0⟩in (77) and state |1⟩in (93) are sometimes referred as conformal
blocks of a relevant CFT. A more conventional way of drawing them is
j = 0, 1
1/2
1/2
1/2
1/2
.
(94)
More precisely, conformal blocks are basis elements in the expansion of a correlation function (here
4-point) in a CFT, labeled by conformal classes (primary fields) in the intermediate channels of tree
diagrams.
Finally, path integral representation also provides an explicit realization of a three-dimensional TQFT
functor. Equation (83) is implicitly a map from M to a vector in a linear space. It also fixes the map
between Σ and a Hilbert space, as we explained. A scalar product of two states can be computed as a
product of two functional integrals integrated over the boundary condition AΣ:
⟨Φ|Ψ⟩∼
Z
DAΣ
Z
DA

A(Σ)=AΣ
Z
D ¯A

 ¯
A(Σ)=AΣeiSCS[M1∪M2] .
(95)
This is equivalent to a functional integral over a closed three-dimensional space, which produces a C-
number, as expected.
As an example, consider an overlap of two Chern-Simons states (84) and (85):
*

+
=
.
(96)
The result is a path integral with an insertion of a circular Wilson loop. The integral is computed over
a theory defined in a closed 3-manifold obtained by gluing two 3-balls along an S2 boundary. Such a
3-manifold is the sphere S3. (It is a higher-dimensional generalization of gluing two discs along an S1 to
obtain S2.) Hence, overlaps of states like (84) and (85) compute expectation values of Wilson loops in
Chern-Simons theory.
It is the main result of [20] that expectation values of knotted fundamental Wilson loops in the SU(2)
Chern-Simons theory compute Jones polynomials of the corresponding knots. For Wilson lines in other
representations one obtains a generalization called colored Jones polynomials, while for G = SU(N) one
obtains the HOMFLY-PT polynomials [46,47].
One can also consider other examples of boundaries.
A fundamental example is Σ = T 2 (two-
dimensional torus). In this case a nondegenerate basis is provided by Wilson loops with all half-integer
22
spins between 0 and k/2 winding the noncontractible cycle of the torus. Quantum mechanics and quantum
information applications based on this kind of states have been studied in many recent papers, e.g. [69–83].
This approach gives a direct association of a knot with a quantum state, but we will follow a different
route in this review.
Another generalization is the case of multiple S2 boundaries [59, 84–87]. According to the TQFT
axioms, these correspond to tensor products of Hilbert spaces discussed above. Examples of states in a
tensor product of two 4-point spheres are given by the following diagrams:
,
.
(97)
The functional integral is computed over the filling of the space between two spheres. Wilson lines can
connect to the same boundary S2, or can connect different spheres. We can also map the above states to
the one-dimensional model:
→
= |Φ⟩.
(98)
At the end of the previous section we mentioned a subtlety with evaluating traces of operators in the
one-dimensional model. Note that the state shown in (98) can also be viewed as an operator acting on
a single copy of the 4-point Hilbert space. The trace of this operator is identical to the norm squared
of the state. In one-dimensional model the trace or the norm squared may naively appear as a tracelike
closure of the diagram. Computing it in the three-dimensional theory gives
*

+
=
.
(99)
Identifying the interior and the exterior spheres gives a 3-manifold different from S3. It is not hard to
see that this manifold is S2 × S1. It is not possible to draw the latter, so we rather showed it as a kind
of a solid torus. Unlike the solid torus S2 × S1 does not have a boundary. It is topological invariants in
S2 ×S1 that compute the normal trace of an operator, while the invariants in S3 (and the naive tracelike
closures) compute the Markov traces.
