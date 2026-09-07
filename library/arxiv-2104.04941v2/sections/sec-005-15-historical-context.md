---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-005-15-historical-context
section_title: "Historical context"
section_number: 1.5
pages: 7-8
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
ploying the cluster algebra work of Fomin–Zelevinsky [FZ02 ], [FZ03], [BFZ05] as well as Lusztig’s study of
positivity [Lus94], [Lus97]. The application was laid out f or a split semisimple simply-connected Lie group
over R, but explicit constructions were only known for type An. Since then, there has been ongoing work.
• In [Zic19], Zickert produced examples of cluster ensembles and mutations for types A2,B2, C2, and
G2, directly employing Lusztig’s positive maps to explicitly construct varieties. Our work addresses
Conjecture 2.7, which predicts the existence of quivers, ro tation and ﬂip mutations, and coordinate
maps for semisimple G.
This work also expanded the use of Fock–Goncharov coordinat es to representations of ideally-
triangulated hyperbolic 3-manifolds, building on [GTZ15].
• With [Le16b] and [Le16a], Le described constructions for qu ivers of types An, Bn, Cn, and Dn
using tensor invariants and webs. Our work addresses Conjec ture 3.12 (that the cluster algebra for
Conf ∗
m(G/N+) is invariant under retriangulation and reordering) for the orientation-preserving case,
for our choice of presentation of w0.
• Using representations of quivers, Fei constructed quivers and mutations for many types in [Fei16],
though associated to a slightly diﬀerent ﬂag variety.
• In [Ip18], Ip produced similar “basic quivers”, though not p resenting mutation sequences in the
general case.
• Goncharov–Shen continued work on invariants of cluster ens embles with [GS18], providing existence
proofs.
There were several obstacles to extending these results to o ur proof of Theorem 1.1. First, the cluster
ensembles for typeAn have trivial triangular symmetry. However, direct dimensi on counting of the coordinate
ring shows that this is not possible for general G.
Second, the algorithm of [BFZ05, Section 2] to produce a quiv er carrying the coordinate structure of
B− (which is a signiﬁcant step) is well-known. However, this al gorithm depends on a particular choice of
presentation for w0 in the Weyl group of G. It is not immediately obvious how to choose w0 for each group,
or if this choice should matter.
7
Third, the same non-triviality of triangular symmetry for Q extends to non-triviality of the coordinate
assignment map M. In other words, fully three sides of each square in Figure 6 a re trivial in the An case,
and therefore give few clues as to the general case.
Finally, the action of w0 on a simple root αi is not necessarily w0(αi) = −αi. This creates various
complications.
The following observations are the key to our result.
• An is the exception, not the base case. Speciﬁcally, for all G except type A2n, there exists a very
