---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-004-41-ryu-takayanagi-formula
section_title: "Ryu-Takayanagi formula"
section_number: 4.1
pages: 11-13
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
boundary region [3] and the negativity of tripartite information [9].
4.1 Ryu-Takayanagi formula
The Ryu-Takayanagi (RT) formula says that for a CFT whose gravitational dual is well-
approximated by Einstein gravity at low energies, in any static state with a geometric
bulk description the entropy SA of a boundary subregion A at ﬁxed time obeys
SA = Area(γA)
4G ; (4.1)
here G is Newton’s constant and γA is the minimal-area codimension-two bulk surface
whose boundary matches the boundary ∂A of A. In our examples the bulk theory is
2 + 1 dimensional, so γA will be a spacelike bulk geodesic whose “area” is just deﬁned
as its length.
In our discrete setting, we will deﬁneγA as a certain cut through the tensor network
which partitions it into two disjoint sets of perfect tensors. Associated with a cut c is
a decomposition of the tensor network as a contraction of two tensors P andQ, where
the contracted legs lie along the cut; the number of contracted legs is called the length
of c, denoted |c|. If A is a set of boundary legs and Ac is the complementary set of
boundary legs, then we say that the boundary of the cut c matches the boundary of A
if the uncontracted legs of P are the legs of A, and the uncontracted legs of Q are the
legs of Ac. The minimal bulk geodesic bounded by A, γA, is then deﬁned as the cut c
of shortest length whose boundary matches the boundary of A. We use P to denote,
not just the tensor associated with one side of the cut, but also the set of bulk lattice
sites corresponding to the perfect tensors which are contracted to construct P ; likewise
for Q. We note that P or Q might have more than one connected component, and so
mightγA when regarded as a path in the dual graph.
– 9 –
A standard argument for tensor network representations of quantum states shows
that|γA| provides an upper bound onSA. If P andQ are the tensors associated with a
cutc whose boundary matches the boundary of A, then the holographic state|ψ⟩ may
be expressed (up to normalization) as
|ψ⟩ =
∑
a,b,i
|ab⟩PaiQbi≡
∑
i
|Pi⟩A⊗|Qi⟩Ac. (4.2)
Here a and b run over complete bases for A and Ac respectively, and i runs over all
possible values of the indices contracted along c; the vectors {|Pi⟩} inHA and the
vectors{|Qi⟩} inHAc are not necessarily orthogonal or normalized. (See ﬁgure 5.)
Tracing outAc we obtain (up to normalization) the density operator on A:
c
a
bi
P
Q
b
b
b
b
a
a
a
a
a
i
i
i
i
A Ac
Figure 5 . A cut through a holographic tensor network by a curve c bounded by∂A. Bound-
ary indices a andb are uncontracted in A and its complement Ac respectively; tensors P and
Q are contracted by summing over the index i which is cut by c.
ρA =
∑
i,i′
⟨Qi′|Qi⟩|Pi⟩⟨Pi′|. (4.3)
Evidently the rank of ρA is at most the number of terms in the sum over i, namely
v|c|. The density operator of a given rank with maximal Von Neumann entropy is
proportional to the identity on its support, and has entropy equal to log of the rank.
We obtain the best bound by choosing the cut c =γA with the shortest length:
SA≤|γA|· logv. (4.4)
In most of what follows, we will deﬁne entropy by taking logs with base v, and so
– 10 –
suppress the logv factor.
If the tensors P and Q are actually isometries from i to a and b respectively, then
{|Pi⟩} and{|Qi⟩} are sets of orthonormal vectors; in that case (4.4) is saturated and a
discrete analogue of the RT formula holds exactly. Under what conditions will P and
Q be isometries? We can prove the following theorem:
Theorem 2. Suppose that we have a holographic state associated to a simply-connected
planar tensor network of perfect tensors, whose graph has “non-positive curvature”. 3
Then for any connected region A on the boundary, we have SA =|γA|; in other words,
the lattice RT formula holds.
The strategy of the proof is to show that P and Q can in fact be interpreted as
unitary transformations, from the cut together with some subregion of A or Ac to the
rest of A or Ac respectively. We can then use the identity depicted in ﬁgure 3 to re-
interpret these transformations as isometries from the cut to A and from the cut to Ac
respectively; the RT formula follows. The key to the argument, explained in appendix
B, is using a strengthened version of the max-ﬂow min-cut theorem (which is standard
in graph theory [33]) to establish that the tensor network representations of P and Q
can be interpreted as unitary quantum circuits.
