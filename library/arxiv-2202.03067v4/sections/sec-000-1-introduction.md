---
doc_id: arxiv-2202.03067v4
doc_title: "QUANTUM JET BUNDLES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2202.03067v4.pdf
source_sha256: 22cf51d9d54ff681
toc_source: outline
doc_brief: "QUANTUM JET BUNDLES — We formulate a notion of jet bundles over a possibly noncommutative algebra A equipped with a torsion free connection."
---
Noncommutative geometry is the idea that geometric constructions can be extended to the
case where the ‘coordinate algebra’A is potentially noncommutative. Originally motivated by the
quantisation of phase spaces in quantum mechanics, a more recent motivation is the hypothesis
that spacetime itself is better modelled by noncommutative coordinates due to quantum gravity
eﬀects. The most well-established approach, coming out of operator algebras, the Gelfand-
Naimark theorem and cyclic cohomology is that of A. Connes [9]. Since the 1980s there have
also emerged more algebraic-geometry like approaches such as [24], as well as a constructive
approach motivated by, but not limited to, the diﬀerential geometry of quantum groups and
models of quantum spacetime as in [4]. In this work we use this last approach, ensuring good
contact with examples in the literature. The starting point here is a diﬀerential graded algebra
(DGA) (Ω, d) withA appearing as degree 0 (in fact we will only need this to the degree 2 or 2-form
level) and a bimodule connection ∇∶Ω1→Ω1⊗A Ω1, σ ∶Ω1⊗A Ω1→Ω1⊗A Ω1. More generally,
one can also consider other vector bundles via their sections as bimodules E, and bimodule
connections ∇E on them. In the bimodule setting, one has both left and right Leibniz rules
and referring the latter back to the left requires [10, 21] the existence of a bimodule ‘generalised
braiding’ map σE ∶E⊗A Ω1→Ω1⊗AE. Details are recalled in the preliminary Section 2.
The problem we partially solve using such data is a long-standing one in noncommutative
geometry, namely to ﬁnd a reasonable notion of ‘jet bundle’ over a noncommutative algebra A.
Jet bundles underly the mathematical formulation of Lagrangian ﬁeld theory, Noether theorems
and the Euler-Lagrange equations in physics, hence quantum jet bundles would be a critical ﬁrst
step down the road of physics on quantum spacetime. The mathematical problem is, moreover,
clear enough for ﬁrst order jet bundles where classical algebraic geometry already suggests that
it is natural to take J 1
A = A⊕Ω1 as explained in [15]. This previous work, however, used a
notion of ‘balanced derivations’ in the noncommutative case to deﬁne jet bundles (in fact a ‘jet
algebra’) whereas we insist on a standard DGA as our main input data. Our new proposal for
Key words and phrases. noncommutative geometry, quantum Riemannian geometry, diﬀerential graded al-
gebra, Yang-Baxter equation, braided Hopf algebra, quantum symmetric algebra, braided symmetric, quantum
spacetime, quantum gravity.
Ver.2.
1
arXiv:2202.03067v4  [math.QA]  16 May 2023
2 SHAHN MAJID AND FRANCISCO SIM ˜AO
jets of all orders is to ﬁrst deﬁne the sub-bimodule
Ωk
S ⊆Ω1⊗
A
/uni22EF⊗
A
Ω1
(k copies) deﬁned as the joint kernel of the wedge products between adjacent copies. Then
Jk
A∶=⊕k
j=0Ωj
S with the underlying bimodule structure inherited from Ω 1. This much, i.e. the jet
bundle itself, depends only on the DGA. However, we also need a ‘jet prolongation’ linear map
jk∶A→Jk
A which classically expands a function into its Taylor series to degree k and a second
product ●k byA (classically taken from the left or the right on sections of the jet bundle, but in
our case as a bimodule with ●k on both sides) such that jk is a bimodule map. We then have a
limit J∞
A as the limit of an increasing sequence of A-bimodules
/uni22EF A
/uni22EFJk
A Jk−1
A /uni22EFJ 1
A J 0
A =A
jk
jk−1
... j1
id
with the bullet product in each degree and commuting with the jk maps. This occupies most
of the paper, with Section 3 for k = 1, 2, 3 and Section 4 for general k. The low degree cases
are developed ﬁrst in explicit detail so that we can see the required quantum geometric data
progressively emerging. They also provide the template for the general case with no further
conditions on the geometric data needed for k > 3. By default, Jk
A refers to the ●k structure on
both sides, but our construction respects the underlying inherited bimodule structure by which
Jk
A is regarded as a bundle, with the result that one also has a bimodule in the two mixed cases
where we use the bullet product from one side and the inherited bundle product from the other.
Thejk maps mean that we are constructing split jet bundles, but these are the relevant ones for
physics since, classically, the splitting is needed to deﬁne the contact forms for the variational
double complex [1]. Here jk splits the surjection Jk
A→A going along the bottom.
The further geometric data needed beyond a DGA is as follows. For the bullet products
●k we need a bimodule map σ ∶Ω1⊗A Ω1 →Ω1⊗A Ω1 and for the higher degree theory this
should obey the braid relations in the monoidal category of A-bimodules, which is an innovative
feature of the present work, and also be compatible with the wedge product. Classically, this
σ would just be the ‘ﬂip map’ and would not appear as additional data. In the split case
that we are interested in, i.e. for the jet prolongation maps, we ask that these σ arise as
part of a torsion-free bimodule connection ∇,σ , and for k ≥3 this should moreover be ﬂat.
Requiring the existence of a connection with nice properties is not without precedent in the
constructive approach to noncommutative geometry, as a proxy for non-existent local coordinates.
For example, a bimodule equipped with a ﬂat bimodule connection can be seen as an algebraic
model of a sheaf [4, Chap. 4] and similarly a background connection is used in the construction
of an algebra of diﬀerential operators in [4, Chap. 6], which classically would be dual to the jet
bundle. Likewise, the Hopf-Galois or ‘local triviality’ property of a quantum principal bundle
can be expressed as existence of a connection on the principal bundle. Moreover, one should
not expect that the jet bundle and prolongation maps can all be constructed from the DGA
alone. As already clear in Connes approach to noncommutative geometry, the DGA alone is
not enough to recover a manifold in the commutative case, one needs additional structure (in
Connes case this is provided by a spectral triple or ‘Dirac operator’, which entails a DGA but
contains much more information). Nevertheless, the requirement for k ≥3 of a ﬂat torsion free
connection is a signiﬁcant restriction of the present work, corresponding in the classical case to
an aﬃne structure of some kind [8]. It also means classically that the vector ﬁelds form a Vinberg
QUANTUM JET BUNDLES 3
or pre-Lie algebra. This assumption constitutes therefore an interesting class of ‘nice’ quantum
manifolds which deserve more study and to which the present paper is initially restricted.
This is not the end of the story and it should be possible to drop the ﬂatness assumption in a
future extension of the theory (this is discussed further in the conclusions Section 7). Moreover,
for J 1
A, the construction does not depend on ∇,σ up to isomorphism, while for J 2
A it depends
up to isomorphism only on σ which classically would be the ﬂip map and not additional data.
These results are proven in Section 3. For higher k we are not aware of an isomorphism if we
want to remain compatible with the prolongation maps but otherwise, as noted, the construction
of Jk
A as a bimodule depends only on σ with various compatibility properties rather than on ∇
directly, the latter only being necessary for the jet prolongation maps jk. It is also of interest
that the latter enter through the ‘braided integer’ maps [n,σ] and associated braided binomials
previously used in the theory of braided-linear spaces (such as the quantum plane) as Hopf
algebras in a braided category [16, Chap. 10]. In our case, they will be key to a certain higher-
order derivation property in Lemma 3.5 and its generalisation Lemma 4.7. Braided techniques
also provide a certain ‘braided shuﬄe product’ on the space of symmetric cotensors making this
into an algebra ΩS used in the jet bundle construction. In some cases, we also have a ‘reduced
jet bundle’ similarly built on the braided-symmetric algebra Sσ(Ω1) as explained in Section 4.3.
Although not the main part of the work, we also cover the case of jet bundles Jk
E relevant to
a vector bundle (viewed as a bimodule of sections) over A, in Section 5. Here the order 1 case is
a noncommutative version of the Atiyah exact sequence [2], with
0→Ω1⊗
A
E→J 1
E→E→0
with bullet actions built from a given bimodule map σE. As before, this is not additional data
in the classical case as it would just be the ﬂip map. We will see that splittings j1
E∶E→J 1
E
of this sequence are then in 1-1 correspondence with bimodule connections ∇E with generalised
braiding the given σE. Moreover, Lemma 5.2 shows that diﬀerent choices of ∇E,σE then give
isomorphic split Atiyah sequences. For higher jets, we only consider split jet bundles where the
jet prolongation map jk
E∶E →Jk
E is part of the construction and depends on a choice of ∇E
similarly to the above.
Section 6 addresses the important task of showing that our construction is compatible with
several standard examples of quantum diﬀerential geometries as in [4]. These include M2(C) the
algebra of 2 ×2 matrices regarded as a ‘noncommutative coordinate algebra’ with its standard
2-dimensional Ω 1, the commutative algebra C(S3) of functions on the permutation group of 3
elements with its standard 3-dimensional Ω1 (here 1-forms do not commute with functions so we
are still doing noncommutative geometry), the 2-dimensional bicrossproduct model Minkowski
spacetime with relations [r,t]=λr and its standard 2-dimensional Ω 1 and the quantum group
Cq[SL2]atq a fourth root of unity with its standard 3-dimensional Ω1. A striking observation in
most of these examples is that by the time we have imposed that ∇is torsion free, ﬂat and obeys
the braid relations for its σ, the other conditions needed for our theory – extendability as in [6],
∧-compatibility [4, Chap. 8.1], and the new notion introduced now of ‘Leibniz compatibility’ in
Lemma 3.5, all hold automatically.
Before turning to the noncommutative constructions, we brieﬂy remind the reader of the key
ideas, for orientation purposes only, in the classical theory of jet bundles. There are many works
with more details and we refer, for example, to [12, 22], where the former also contains their
use in Lagrangian ﬁeld theory. If E →M is a vector bundle (for this classical discussion we
denote its sections by Γ (E), not simply by E as above), the jet bundle of degree up to order k
is a certain aﬃne bundle Jk
E→E, which we also regard as a bundle over M via the projection
E →M, together with a map jk
E∶Γ(E) →Γ(Jk
E) that, roughly speaking, provides the Taylor
series expansion of s∈Γ(E) at each point of M. In physics the sections Γ (E) would typically be
4 SHAHN MAJID AND FRANCISCO SIM ˜AO
‘matter ﬁelds’ of which the simplest ‘scalar ﬁeld’ case is provided by takingE trivial with ﬁbre R
or C, so that Γ(E) =C∞(M) is the space of (real or complex valued) functions on the manifold.
Less well-known, but clear by the end of our algebraic version (as discussed in Section 7) is that
in the scalar ﬁeld case Γ (Jk) is just the space of symmetric tensors of degree (0,i) for i≤k, i.e
symmetric tensor powers of the bundle of 1-forms [23]. This means that we can loosely think of
the colimit of the Γ (Jk) as something like the algebra C∞
poly(TM ) of functions on the tangent
bundle polynomial in the ﬁbre direction, but a lot bigger in allowing powerseries. Now, given
s∈C∞(M), the jet prolongation map to a function on TM is via the Taylor series at each point
of M,
s/uni21A6(s,∂is,∂i∂js,/uni22EF),
where ∂i are partial derivatives in a local coordinate chart dual to local 1-forms d xi. Let vi
correspondingly parametrize the tangent space TxM (e.g. a vector ﬁeld would have the form
vi(x)∂i, but in our case we consider only one point x∈M). Then the Taylor expansion provides
functionsvi∂is,vivj∂i∂js etc evaluated atx, as functions of increasing degree on TxM. It is this
construction which in an algebraic form we extend to noncommutative geometry in Sections 3,
