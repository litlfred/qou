---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-014-56-erasure-threshold
section_title: "Erasure threshold"
section_number: 5.6
pages: 32-36
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
If the entanglement wedge conjecture is true for AdS/CFT, if holographic codes faith-
fully model the entanglement structure of boundary theories with classical gravitational
duals, and if the greedy entanglement wedge is a reasonable stand-in for the entangle-
ment wedge, then we should be able to ﬁnd holographic codes and boundary regions
such that the greedy entanglement wedge reaches far outside the causal wedge. In this
section we provide examples which conﬁrm this expectation. One way to formalize this
is to choose A to be a randomly chosen set of boundary spins, whose size is a speciﬁed
fraction of the total boundary. The geometry of the hyperbolic plane suggests that, if
A is large enough, the causal wedgeC[A] will stick close to the boundary, yet the entan-
glement wedgeE[A] reaches the center of the bulk with high probability; we illustrate
this in ﬁgure 15. We will see that not all holographic codes have this property, but we
are able to provide concrete examples that do.
C[A1]
C[A2]
C[A3]
C[A4]
C[A5]
C[A6]
C[A7]
(a) Shallow causal wedge
E[A] (b) Deep entanglement wedge
Figure 15 . (a) When a boundary region A is partitioned into many connected components
it may have a very shallow causal wedge C[A] if each connected component is small. (b) In
contrast, if A comprises a suﬃciently large fraction of the boundary, its entanglement wedge
E[A] will extend deep into the bulk.
Another, perhaps better, way to formulate this case is to imagine a probabilistic
noise model which acts independently (without any noise correlations) on each of the
physical boundary spins, where each spin is either erased with probability p or left
untouched with probability 1−p. If p is small, the set A of unerased boundary spins
breaks into many connected islands, where a typical island contains O(1/p) spins and
has a causal wedge which reaches into the bulk by only a constant distance. We can
show, though, that if the holographic code is properly chosen and the erasure probability
p is less than athreshold valuepc, thenE[A] contains the central bulk spin with a success
– 30 –
probability deviating from one by an amount which becomesdoubly exponentially small
as the radius of the bulk increases.
Which codes have an erasure threshold? One necessary requirement is that the
code must have a distance that increases with the system size. For the purpose of
reconstructing the central tensor in the bulk, this means that there should not be any
logical operator supported on a constant number of boundary spins which acts non-
trivially on the central bulk index. That’s because erasure of any constant number of
spins occurs with a nonzero constant probability, and recovery from the erasure error
is not possible if a nontrivial logical operator has support on the erased qubits.
The pentagon code fails to fulﬁll this necessary condition. To illustrate the prob-
lem, it is helpful to consider ﬁrst a simpler code, the “triangle code” constructed by
contracting four-index perfect tensors, where each leg is a 3-level spin, a qutrit. Each
triangle in the bulk has a dangling bulk index, and the code is constructed as a tensor
network forming a tree, the Bethe lattice; each triangle is contracted with one triangle
closer to the center and two triangles further from the center, as shown on the left side
of ﬁgure 16a. (Qi’s model [28] is based on a tensor network with a similar structure.)
One way to describe the greedy algorithm is to say that it propagates erasures from
the boundary toward the center of the bulk — the inward directed leg of a triangle is
erased if either of its outward directed legs is erased, and the central triangle can be
reconstructed only if at least two of that triangle’s legs are unerased.
(a) Triangle code
 (b) Pentagon code
Figure 16 . Dangerous small erasures for the triangle (a) and pentagon codes (b). In the
triangle code erasing two boundary spins, boxed in blue, can prevent reconstruction of the
central tensor. In the pentagon code erasing four spins can prevent the reconstruction.
It is easy, then, to prevent the greedy algorithm from reaching the center — only
– 31 –
two spins need to be erased. A single erasure on the boundary propagates all the way up
to the center of the network, erasing one of the central triangle’s legs. A single erasure
on a diﬀerent branch of the tree propagates up to another of the central triangle’s legs,
blocking the reconstruction of the central tensor on the remaining unerased spins.
The greedy algorithm fails for a good reason. As described in appendix A.2, The
logical algebra for the three-qutrit code represented by a single triangle is generated by
logical operators of the form ¯X =X⊗X−1⊗I, whereX is a generalized Pauli operator;
in fact the code is symmetric under permutation of the three qutrits, so we can choose
X and X−1 to act on any two of the three qutrits without changing the operator’s
action on the code space. Now choose a path through the Bethe lattice which begins
on one leaf, travels to the center, exits the center on a diﬀerent branch, and ﬁnally
reaches another leaf on that branch. Apply the operator ¯X to each of the logical bulk
indices visited by this path. Then for each leg along the path the X from the triangle
on one side cancels the X−1 coming from the triangle on the other side, except for one
uncanceledX on one leaf and oneX−1 on the other. We conclude that the code admits
a logical operator acting nontrivially on the central triangle which has support on only
two boundary spins. That is why the central bulk spin can be damaged by erasing only
two boundary spins.
For the pentagon code the situation is only slightly better. If we pick just four
spins at the positions shown on the right side of ﬁgure 16b, then the greedy algorithm
applied to the complement of these four spins never absorbs any of the tensors adjacent
to the dashed line. This failure is just a property of the graph deﬁning the holographic
code, but once again we can understand the failure by noting that there is a logical
operator acting on the central pentagon supported on these four boundary spins, so
erasing these four spins prevents central bulk operators from being reconstructed on
their complement. Now we may consider a product of bulk logical operators acting on
the pentagons just above and just below the dashed line. We use the logical operator of
the ﬁve-qubit code ¯X =−Z⊗X⊗Z⊗I⊗I described in appendix A.1, where X and
Z are Pauli operators (which square to one), and the operator’s action is unchanged
by cyclic permutations of the ﬁve qubits. Now X’s applied from either side of the cut
cancel on the legs crossed by the cut, andZ’s applied from either side cancel for the legs
just above and below the cut, leaving only four uncanceled Z’s acting on the boundary
qubits.
Of course, uncorrectable damage deep inside the bulk caused by erasing just a
few boundary spins is not at all what we expect in AdS/CFT, where according to
the entanglement wedge conjecture we should always be able to reconstruct the center
of the bulk from a suﬃciently large fraction of the boundary, whatever its shape or
location. To obtain a better model for AdS/CFT we should modify the holographic
– 32 –
code, thinning out the algebra of bulk logical operators, and hence reducing the rate
of the code.
A code that works better can be obtained by a simple modiﬁcation of the pentagon
code — the modiﬁed tensor network is constructed by starting with a pentagon at the
center and adding alternating layers of hexagons (with no dangling bulk indices) and
pentagons (each with one bulk index) as the network grows radially outward. The
associated network is depicted in ﬁgure 17. This change suﬃces to remove all the
constant-weight logical operators acting nontrivally on the center and in fact we can
prove that this pentagon/hexagon code has an erasure threshold. Numerical studies
show that erasure can be corrected by the greedy algorithm with high success proba-
bility for p≤pgreedy
c ≈ 0.26; the erasure threshold pc achieved by the optimal recovery
method might be higher than pgreedy
c if the tensors have further special properties aside
from just being perfect.
(a) Pentagon/Hexagon code
 (b) One qubit code
Figure 17 . Tensor networks for holographic pentagon/hexagon codes with erasure thresh-
olds, where neighboring polygons share contracted indices. In the network shown on the left,
pentagons and hexagons alternate on the lattice; each pentagon carries one dangling bulk
index, and hexagons carry no bulk degrees of freedom. The logical qubit residing on the
central pentagon is well protected against erasure if the erasure probability on the boundary
is below the threshold value pc. In the network on the right, there is just a single bulk qubit
located at the center; the rest of the network is similar to the holographic state constructed
from hexagons only.
Since our main interest is in the reconstruction of the center of the bulk, in appendix
D we study a code for which the only logical index resides at the center, also shown in
ﬁgure 17. This code is almost the same as the holographic state obtained by contracting
six-leg perfect tensors (hexagons), except that the tensor network contains one pentagon
– 33 –
at the center; we therefore call it the single-qubit hexagon code. We prove the existence
of an erasure threshold for this code, and also derive an analytic lower bound on the
threshold erasure rate pc≥ 1/12. Numerical evidence indicates that the threshold is
actually quite close to pc = 1/2.
The lower bound on the threshold is derived using a simpliﬁed and less powerful
version of the greedy algorithm, the hierarchical recovery method, which begins at the
boundary and proceeds inward toward the center of the bulk. A tensor at level j + 1
of this hierarchy is connected to at least four tensors at level j, and the level-(j + 1)
tensor is erased if two or more of its level- j neighbors are erased. The proof proceeds
by recursively deriving an upper bound on the erasure probability pj at levelj, ﬁnding
pj≤pc
(p
pc
)λj
, (5.2)
where pc = 1/12 and λ = 1+
√
5
2 . Thus the erasure probability for the central tensor
drops doubly exponentially with the radius of the bulk if p<p c, which means that the
central tensor can be reconstructed on the set of unerased boundary qubits with very
high probability.
A tricky aspect of the proof is that, because a single level- j tensor couples to two
level-(j + 1) tensors, there are noise correlations which propagate from level to level.
Fortunately, the hyperbolic geometry controls the spread of correlations, making the
analysis manageable. In fact, correlations beyond nearest neighbors never arise. This
is one advantage of using the hierarchical recovery method rather than the greedy
algorithm. A similar proof strategy may also be applied to other holographic codes.
