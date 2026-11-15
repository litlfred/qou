---
doc_id: oberwolfachreports1223-v20120708-9-40
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by"
section_id: sec-005-naturality-of-heegaard-floer-homology
section_title: "Naturality of Heegaard Floer homology"
section_number: null
pages: 16-19
source_pdf: OberwolfachReports1223_v20120708_9_40.pdf
source_sha256: 94f82cfc185955ba
toc_source: inferred
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 28/2012 Invariants in Low-Dimensional Topology and Knot Theory Organised by — This meeting concentrated on topological invariants in low di"
---
Andr´as Juh´asz
(joint work with Peter Ozsv´ath, Dylan Thurston)
Heegaard Floer homology, deﬁned by Ozsv´ath and Szab´o in [1, 2], is a package
of invariants for 3- and 4-manifolds. For concreteness, we will focus on the 3-
manifold invariant (
HF with Z2-coeﬃcients. Given a closed oriented 3-manifold
Y , the construction of [1] assigns to Y the Z2-vector space (
HF(Y ), well-deﬁned
up to isomorphism. There are several choices involved in the construction; most
importantly, one has to choose a based Heegaard diagram (Σ, α, β, z) of Y . Here
Σ ⊂Y is an oriented genus g surface that splits Y into two handlebodies, α and
β are two g-tuples of pairwise disjoint, homologically linearly independent simple
closed curves in Σ, and z ∈Σ \ (α ∪β) is a basepoint.
To obtain the 4-manifold invariants, one has to deﬁne maps induced on Hee-
gaard Floer homology by cobordisms, and for that one needs to assign a concrete
Invariants in Low-Dimensional Topology and Knot Theory
17
vector space (
HF(Y ) to a 3-manifold Y . The same is needed to have a diﬀeomor-
phism action on (
HF, or to be able to talk about the contact element in Heegaard
Floer homology (as opposed to just being able to say whether this element is zero
or not). In [2], Ozsv´ath and Szab´o attempted to prove these naturality properties
of Heegaard Floer homology. However, as noticed by the author, there is a gap in
their proof, they did not account for the way the Heegaard surface Σ is embedded
in Y . Furthermore, it is unclear whether (
HF depends on the choice of basepoint
(just like the fundamental group depends on a basepoint). As an analogy, one can
consider simplicial homology, which depends on a triangulation, and since man-
ifolds can carry several PL structures, it is a priori unclear how to compare the
homology computed from triangulations lying in diﬀerent PL structures. In that
case, singular homology overcomes this problem.
Intuitively, one should think of (
HF as assigning a Z2-vector space to every
based diagram (Σ, α, β, z) with Σ ⊂Y . Hence, (
HF is a Z2-vector bundle over the
“space of diagrams”. A priori, this might be a non-trivial bundle, one could move
Σ around a non-trivial loop and get a non-trivial automorphism of (
HF(Σ, α, β, z).
This would mean that, a priori, the Goeritz group of the Heegaard splitting (Y, Σ)
might act non-trivially on (
HF(Σ, α, β, z).
As we show in [3], Heegaard Floer homology is in fact natural and is equipped
with a diﬀeomorphism action. If D and D′ are both based diagrams of the based
3-manifold (Y, p), then we construct an isomorphism ΦD,D′ : (
HF(D) →(
HF(D′).
These satisfy the property that ΦD′,D′′ ◦ΦD,D′ = ΦD′′,D. Then the vector space
(
HF(Y, p) is deﬁned to be
)
D
(
HF(D)/ ∼,
where the disjoint union is taken over all based diagrams D of (Y, p) with z = p,
and the equivalence relation ∼is deﬁned by requiring that x ∈(
HF(D) and
x′ ∈(
HF(D′) are equivalent if and only if x′ = ΦD,D′(x). Given a diﬀeomor-
phism d: (Y, p) →(Y ′, p′), we deﬁne the diﬀeomorphism map d∗: (
HF(Y, p) →
(
HF(Y ′, p′) as follows: Let D be a diagram of (Y, p), and D′ = d(D) the corre-
sponding diagram of (Y ′, p′). Then d∗maps the equivalence class of x ∈(
HF(D)
to the equivalence class of d∗(x) ∈(
HF(D′), where d∗on the chain level is simply
given by the map d induces from Tα ∩Tβ to Tα′ ∩Tβ′.
In fact, we provide a set of axioms for arbitrary invariants of Heegaard diagrams
that should be satisﬁed in order to give rise to a functorial invariant of 3-manifolds.
The proof proceeds by studying the bifurcations of generic 2-parameter families of
gradient vector ﬁelds on 3-manifolds. A Heegaard diagram arises from a generic
gradient on Y , while bifurcations of generic 1-parameter families of gradients cor-
respond to certain generalized Heegaard moves.
We assign an isomorphism to
every classical Heegaard move, and then show that no loop of moves produces a
non-trivial monodromy, where a move can be a diﬀeomorphism Σ →Σ′ that is
isotopic to the identity in Y (without this, it is impossible to compare (
HF for
18
Oberwolfach Report 28/2012
Figure 1. A simple handleswap
diﬀerent Heegaard surfaces). From this loop of moves, we construct a loop of gra-
dient vector ﬁelds, parametrized by S1. Then we extend this to D2. The link of
a codimension-2 bifurcation gives a loop of diagrams, and we simplify these loops
until consecutive diagrams are related by the standard Heegaard moves and dif-
feomorphisms isotopic to the identity. Finally, we show the monodromy is trivial
along each loop in the simpliﬁcation. It turns out that, in addition to the loops
checked in [2], one only has to verify that (
HF has no monodromy for one speciﬁc
type of loop that we call a simple handleswap, see Figure 1.
There are simple examples of multi-pointed Heegaard diagrams where moving
the basepoints produces non-trivial automorphisms of the Floer homology. We
conjecture that this is also the case for (
HF(Y, p), but not for the other ﬂavors of
Heegaard Floer homology. The latter claim is motivated by the fact that the other
ﬂavors are isomorphic to the various versions of monopole Floer homology, whose
construction does not depend on the choice of basepoint.
References
[1] P. Ozsv´ath, Z. Szab´o, Holomorphic disks and topological invariants for closed three-
manifolds, Ann. of Math. 159 (2004), 1027–1158.
[2] P. Ozsv´ath, Z. Szab´o, Holomorphic triangles and invariants for smooth four-manifolds,
Adv. Math. 202 (2006), 326–400.
Invariants in Low-Dimensional Topology and Knot Theory
19
[3] A. Juh´asz, P. Ozsv´ath, and Z. Szab´o, Naturality and mapping class groups in Heegaard
Floer homology, in preparation.
