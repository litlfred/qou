---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 4-9
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
The gravitational path integral continues to be an enigmatic yet essential tool in un-
derstanding aspects of holography. Low-dimensional models have served as valuable
laboratories for uncovering some of its more intricate features. From these models,
much evidence has been gathered in favour of the idea that the path integral for pure
Einstein gravity can be understood as performing astatisticalaverage over the data
that define the dual conformal field theory. Developing this idea in three-dimensional
gravity has become an active direction of current research, but our understanding of
the statistical holographic dictionary is still incomplete.
Thanks to the absence of local bulk degrees of freedom [1], pure AdS 3 quantum
gravity is a particularly suitable playground to explore the statistical nature of the
gravitational path integral, and significant progress has been made over the past few
years [2–19]. As a starting point, the main entry in the dictionary between pure 3-
dimensional gravity and the statistical ensemble of CFT 2 data posits that averaged
boundary quantities are computed as a sum over topologies in the bulk:
Z[Σ] =
X
∂M=Σ
Zgrav[M].(1.1)
On the right-hand side,Z grav denotes the gravitational path integral for pure Einstein
gravity with a negative cosmological constant, on a fixed bulk topologyM. 1 The
sum runs over all distinct bulk 3-manifolds whose asymptotic boundary is Σ. If Σ
is a connected Riemann surface of genusg, the left-hand side computes the average
genusgpartition function, in some yet to be specified statistical model of CFT 2
data. If Σ consists of multiple disconnected components, then the right-hand side
includes Euclidean wormhole topologies and the left-hand side computes a higher
statistical moment of CFT 2 partition functions. In recent years, powerful new tools
have been developed to computeZ grav[M] exactly, i.e. to all orders inG N, for a large
class of 3-manifolds [11, 12]. Nevertheless, 3-manifold topology is a rich and complex
subject, which means that understanding the full sum over topologies in (1.1) is a
difficult (and unresolved) problem.
In this paper, our principal aim is to systematize the correspondence between
universal statistics of 2d conformal field theory and pure 3d quantum gravity. In par-
ticular, we want to understand what role the sum over topologies plays in the pure
gravity/ensemble duality, and explain how the bulk sum over topologies arises from
theboundaryperspective. We will explore how, and to what extent, the 3-manifolds
contributing to (1.1) are organized to furnish a consistent statistical ensemble of
CFT2 data, compatible with kinematic constraints, crossing symmetry, modular in-
variance and typicality at high energies.
1For notational clarity, we suppress the dependence on the moduli of the boundary Riemann
surface and use Σ as a placeholder for all the boundary data.
– 4 –
γ
Figure 1. Example of a crossing transformationγon a genus-2 Riemann surface. The two
sets of contractible cycles (the thick closed curves) lead to two distinct genus-2 handlebodies
upon filling in the bulk.
Handlebodies and crossing symmetry.To illustrate the question that we want
to ask, suppose that the asymptotic boundary Σ is a Riemann surface of genusg⩾1,
and fix the boundary moduli Ωi, ¯Ωi. Then a natural class of 3-manifolds contributing
to the sum over topologies consists of the genus-ghandlebodies: 2
Z[Σg]⊃
X
γ∈MCG(Σg)/Hg
Zgrav[Mγ].(1.2)
Topologically, a genus-ghandlebody is homeomorphic to a ‘filled-in’ genus-gsurface.
Geometrically, it admits an infinite-volume hyperbolic metric after choosing a col-
lection of 3g−3 disjoint cycles on the boundary Σ g that become contractible in the
bulk (a choice of identity channel, in CFT parlance). Different choices of cycles are
related to each other by crossing transformationsγ, which are elements of the map-
ping class group of Σ g.3 An example of such a mapping class group transformation
is shown in figure 1. The sum over handlebodies can hence be written as a sum over
crossing transformations, modulo the bulk mapping class group of the handlebody
Hg (the so-called handlebody group).
Note that in theg= 1 case, the handlebody sum (1.2) was studied by Maloney
and Witten [21] and subsequently by Keller and Maloney [22]. The resulting sum
over solid tori takes the form of a Poincar´ e series, with MCG(Σ1) = PSL(2,Z) and
H1 =Z. EachZ grav[Mγ] evaluates to a product of left- and right moving Virasoro
vacuum characters,|χ 1(γ·τ)| 2, and hence the role of the sum over topologies is quite
clear: it renders the average partition function modular invariant. Restricting the
sum to a smaller set of bulk saddles would violate modular invariance of the average.4
2Here and in the rest of the paper, we use the symbol⊃to denote that the right-hand side is a
sub-sumof the full sum over topologies.
3For an introduction to crossing transformations, see [20].
4Alargerset of bulk manifolds may be included, as long as it does not spoil modular invariance.
In the genus-1 case, such additional contributions are conjectured to be necessary in order to cure
the negativity in the spectral density in the near-extremal limit [23–27].
– 5 –
In the higher-genus case,g >1, the gravitational path integral on a handlebody
evaluates to the product of left- and right-moving vacuum Virasoro conformal blocks
in the channel specified byγ[11]. Each vacuum block resums all contributions
from descendant states, which are interpreted in 3d gravity as boundary gravitons
[28]. Similar to the genus-1 case, the sum over handlebodies renders the average
genus-gCFT partition function crossing symmetric (invariant under the action of
the mapping class group).
The sum over handlebodies has an interesting implication for the statistics of
OPE coefficients in our model. In the original statistical model of [2, 3], a Gaussian
ansatz was used to describe the statistics of heavy OPE coefficients. This simplified
description captures many important features of gravity, but it generates only a finite
subset of handlebodies (for the genus-2 computation, see section 8.3 of [3]). Hence,
the average is only invariant under a finite subset of all crossing transformations.
Instead, insisting on a fully crossing symmetric average Z[Σg] implies the existence
ofnon-Gaussianitiesin the statistical description of the CFT 2 data [7, 10–17, 29, 30].
In section 3, we will show how to systematically include non-Gaussian OPE statistics
in order to reproduce the full (infinite) sum over handlebodies, for all generag⩾1.
One useful consequence of this systematic approach is that the spinsJ i =h i− ¯hi of
all propagating heavy operators are appropriately quantized.
Why include non-handlebodies?Now we come to the central question of this
paper. In three dimensions, there are many single-boundary topologies that are
not handlebodies: the classic example of such a non-handlebody (in the 3d gravity
literature) is the twistedI-bundle of [31]. However, since the handlebody sum in
equation (1.2) already furnishes a crossing symmetric average (for any choice of
connected genus-gboundary), one could ask why non-handlebodies are needed at all,
from the perspective of the boundary CFT. Said differently, is there a redundancy
in the possible consistent statistical ensembles dual to pure 3d gravity?
This question is especially compelling for a connected boundary of genusg⩾2.
In theg= 1 case, all non-handlebodies are off-shell [21], so there is no semiclas-
sical saddlepoint approximation forZ grav on such topologies. These include single-
boundary Seifert manifolds [14, 25], for which it is currently not known how to
compute the gravitational path integral from first principles. By contrast, forg⩾2
there are many non-handlebodies that support well-definedon-shellsolutions of pure
Einstein gravity with the correct asymptotic boundary behaviour, so there is no a
priori reason to discard their contributions. Moreover, they can be added in a man-
ifestly crossing symmetric way, by summing over mapping class group images of a
given ‘seed’ non-handlebody, as will be shown in section 4. The question is: does
the statistical theory of CFT 2 data require these saddles for internal consistency, or
are they optional? We view this question as a statistical version of the conformal
bootstrap, applied to 3d gravity.
– 6 –
P3 P4
···C i1i2i3Ci4i5i6···
OPE index contractions (typicality)
glue
cylinder surgery
Figure 2. In section 4, we show that index contractions, in a statistical ensemble of heavy
OPE coefficients, correspond to 3-manifold surgery where the gluing surface is a cylinder.
Combining this surgery with crossing transformations generates many non-handlebodies.
Let us emphasize that the above question is distinct from previous work on
Euclidean wormholes and the factorization puzzle [2, 3, 32–36]. When the boundary
Σ has multiple disconnected components, there are well-known wormhole topologies
connecting them (the simplest example being the Maldacena-Maoz solution [32]),
and these are always non-handlebodies. Moreover, it is by now well understood that
these Euclidean wormholes probe higher statistical moments (such as the variance)
in the ensemble of OPE coefficients [2, 3, 12, 13]. So, in the multi-boundary case,
non-handlebodies are clearly needed for the ensemble to have non-zero fluctuations
around the average. On the other hand, thesingle-boundary non-handlebodies that
we address in this paper have so far remained elusive.
Non-handlebodies from statistics.In section 4, we demonstrate that including
non-handlebodies in the sum over topologies becomes necessary when, in addition to
crossing symmetry, we require the ensemble of CFT 2 data to satisfytypicality. This
concept is familiar from the Eigenstate Thermalization Hypothesis [37–41] and can
be generalized to chaotic 2d CFTs [13, 29, 42], where it amounts to approximate
local rotational invariance in microcanonical windows around primary states of high
conformal dimension. Importantly, typicality predicts the structure of index con-
tractions of random OPE coefficients, which in the bulk translates to precisesurgery
operations on 3-manifolds, as illustrated in figure 2. We show that iteratively apply-
ing these surgery moves and combining them with crossing transformations generates
a large class of non-handlebody topologies.
We will refer to this inductive procedure for generating topologies from proper-
ties of the statistical ensemble of CFT 2 data as the “gravitational machine”. This
machine takes as input any handlebody (or multiple handlebodies) and repeatedly
acts on it with three basic surgery operations, which will be specified in section 4.2.
The resulting set of 3-manifold topologies should be seen as theminimalcompletion
– 7 –
/Φ
a) b) c)
n1 n3
n4
n2
Figure 3. Examples of non-handlebodies with genus-2 boundary. These non-handlebodies
are all necessary in the sum over topologies, in order for the statistical description of the
CFT to be consistent.a) Complement of a handlebody-knot in S 3.b) TwistedI-bundle.
c) Dehn surgery on the complement of a handlebody embedded in S 3.
of the handlebody sum that is compatible with typicality, crossing symmetry and
consistency between higher and lower statistical moments. 5
The main results of this paper are to study and rigorously prove certain appealing
properties of the gravitational machine, which we summarize here:
•The machine generates non-handlebodies.We will explicitly show that
the examples illustrated in figure 3 are generated by the machine. Moreover,
we show that they are indeed non-handlebodies by analyzing their fundamen-
tal groups. As a simple class of examples of non-handlebodies, we similarly
analyze all genus-2 handlebody-knots with fewer than 6 crossings (see table 1).
More generally, the machine applies for arbitrary genusg⩾2 of the boundary
manifold and also works for disconnected boundaries.
•The machine is hyperbolic.In section 4.3, we prove that starting from any
hyperbolic 3-manifold, the action of the gravitational machine only produces
3-manifolds that are also hyperbolic. The proof follows from studying how the
fundamental group changes under the operations of the machine, making use
of Thurston’s hyperbolization theorem [45] and geometric group theory. This
key result makes precise the intuition that OPE statistics in the boundary
description only requires on-shell saddles in the bulk.
•But not all hyperbolic non-handlebodies are generated.This is perhaps
the most interesting outcome of our analysis: in section 4.4, we show that all
manifolds generated by the machine are so-calledcylindrical3-manifolds, which
5However, this is not the end of the story: in this paper, we focus on OPE statistics and ignore
spectral correlations. The latter are expected to arise from off-shell topologies [4, 6, 14, 25, 43, 44]
that further correct the dictionary (1.1). We will have more to say on this in the discussion.
– 8 –
contain embedded essential cylinders. However, there are many topologies that
are not cylindrical; as an example of a hyperbolic, acylindrical manifold with
genus-2 boundary, we study Thurston’s so-called ‘tripus’ manifold [46]. We will
discuss the implications of this fact for the sum over topologies below.
Throughout the paper, we demonstrate that the above results, which are mostly
about topology rather than gravity, can be implemented directly on the level of the
gravitational path integral by using Virasoro TQFT [11]. This formalism gives the
exact quantum gravity partition (i.e. at finitec), topology by topology, so we do not
rely on semiclassical arguments. Virasoro TQFT also allows us to straightforwardly
extend our results to 3-manifolds with conical defects: for example, when Σ = Σ 0,4 is
the 4-punctured sphere, the analogue of the handlebody sum is the ‘conformal block
Farey tale’ of [47] and the analogue of a non-handlebody is a non-rational tangle.
Is 3d gravity non-minimal?Let us end this introduction by contemplating what
the above results imply for 3d gravity and the sum over topologies. Although we
have managed to find a boundary interpretation for a large class of non-handlebodies,
there are still infinitely many on-shell manifolds not generated by our gravitational
machine. The main source of such counterexamples are theacylindrical3-manifolds
described in the third point above, which can be characterized by admitting a finite-
volume hyperbolic metric with totally geodesic boundary [48]. Apparently, these
topologies are not strictly necessary in order for the statistical ensemble to obey cross-
ing and typicality, leaving the intriguing possibility that the full sum over topologies
