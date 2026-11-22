---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-004-23-mapping-class-groups
section_title: "Mapping class groups"
section_number: 2.3
pages: 4-6
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
Mapping class groups
The braid groups Bn can also be realized as mapping class groups, which exposes the very
interesting relation with the topology of surfaces. Let M, N be compact manifolds, possibly
with boundary. We denote by C(M, N) the space of all continuous functions from M to N.
There is a natural topology on C(M, N), the compact open topology, deﬁned as follows: for any
K ⊂M compact and U ⊂N open, set:
V (K, U) := {f ∈C(M, N) : f(K) ⊂U}.
The compact open topology is the smallest topology for which all V (K, U) are open. We denote
by Homeo(M) the group of homeomorphisms of M. This is a subset of C(M, M) and in this
way inherits a topology which gives it the structure of a topological group.
Let us now specialize the discussion to the case of an orientable compact surface S. The group
of orientation preserving homeomorphism of S that ﬁx the boundary pointwise will be denoted
by Homeo+(S, ∂S). The connected component of the identity in Homeo+(S, ∂S) is denoted by
Homeo0(S, ∂S) and consists of the set of homeomorphism that are isotopic to the identity via
an isotopy that ﬁxes the boundary pointwise.
Deﬁnition 2.5. The mapping class group of a surface S denoted Mod(S) is deﬁned as:
Mod(S) = Homeo+(S, ∂S)/Homeo0(S, ∂S).
Remark 2.6. The mapping class group can alternatively be deﬁned by replacing homeomor-
phisms by diﬀeomorphism and isotopies by homotopies.
The following is a list of possible
deﬁnitions of Mod(S):
Mod(S)
∼=
Homeo+(S, ∂S)/Homeo0(S, ∂S)
∼=
Diﬀ+(S, ∂S)/Diﬀ0(S, ∂S)
∼=
π0(Homeo+(S, ∂S))
∼=
π0(Diﬀ+(S, ∂S)).
Example 2.7. The notation Mod(S) for the mapping class group is motivated by the example
of the torus T, where:
Mod(T) ∼= SL2(Z).
The isomorphism is deﬁned by the action of Mod(T) on homology.
Deﬁnition 2.8. Let S be a surface and Q ⊂S a ﬁnite set of marked points.
We denote
by Homeo(S, Q) the group of homeomorphisms of S that ﬁx Q as a set and ﬁx the boundary
pointwise. The mapping class group of S, seen as a surface with marked points is
Mod(S, Q) := π0(Homeo+(S, ∂S) ∩Homeo(S, Q)).
Example 2.9 (Alexander-Tietze Theorem). The mapping class group of the disk is trivial:
Mod(D) = {0}.
In order to prove this fact we consider an automorphism f : D →D that ﬁxes the boundary.
Then we deﬁne the isotopy:
ht(z) =
(
z
if t ≤|z| ≤1,
th(z
t )
if |z| ≤t.
]
Figure 2: Halftwist of a two pointed disk
Example 2.10. An example of a nontrivial mapping class is that of the half twist. Here S is
the disk with two marked points, that we may take to be p = (−1
2, 0) and q = (1
2, 0). The half
twist H is the class of the diﬀeormorphism described by the following picture:
Theorem 2.11. Let D be a disk with n marked points Q = {p1, . . . , pn}. There is an isomor-
phism:
ψ : Bn →Mod(D, Q),
characterized by the property that:
σi 7→Hi.
Here Hi denotes the class of the homeomorphism which is supported on a disk containing only
the i-th and i + 1-th punctures, and which acts as a half twist on that disk.
The reader interested in the proof of this theorem may consult [6]. In this section we have
closely followed the book by Farb and Margalit [12], which is an excellent reference for learning
about mapping class groups.
