---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-084-c-categoriﬁcation-of-the-turaev-viro-invariants
section_title: "Categoriﬁcation of the Turaev-Viro invariants"
section_number: C
pages: 74-76
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
The aim of this paper is to introduce and study new three-manifold invariants. Along the way,
we have seen the important roles played by boundary conditions, abelian ﬂat connections,
homological blocks, reﬁnement, and line operators. Here, we outline how these ideas can be
applied to categoriﬁcation of the Turaev-Viro invariants.
Deﬁned via a state-sum model, the Turaev-Viro (TV) invariants [93] involve a “counting”
problem from the start. This motivates a series of questions: do TV invariants of M3 have
a natural home in physics? Could it be that they are counting BPS states associated with
the theory T [M3] and can be categoriﬁed in a way similar to the WRT invariant? How are
they related to the new invariants discussed in this paper? Can they also be decomposed into
the “atoms” of three-manifold invariants — the homological blocks and abelian connections?
Can they be reﬁned?
From the perspective of the state-sum model, categoriﬁcation of the Turaev-Viro invari-
ants may potentially seem even more natural than that of Chern-Simons (WRT) invariants,
though the two problems are closely connected. Thus, the TV invariant of a closed 3-manifold
M3 is simply the square of the corresponding SU (2) WRT/CS invariants [94–96]:
TV(M3,q ) =
⏐⏐ZCS(M3,q )
⏐⏐2
. (C.1)
As explained in detail in this paper, the WRT invariants can be written as a linear sum of
homological blocks and, when there is only one block,
TV(M3,q ) = ˆZ0(M3,q )ˆZ0(M3,q−1) =IT [M3](q) (C.2)
is exactly given by the index of the theory T [M3]. So, for homological spheres, we have
already categoriﬁed their TV invariants!
For general M3, the story will be more interesting. 61 If we use VB to denote the vector
space of boundary conditions on S1 of the theory T [M3] (a de-categoriﬁcation of CB), then
60more precisely, the linear combination of cablings up to n-th, given by (B.1)
61To streamline the presentation, we will ignore normalization factors, Weyl group actions, etc.
– 73 –
there are two natural bases {|ˆa⟩} and{|a⟩} corresponding to the homological blocks and
(connected components of) abelian ﬂat connections. There are several distinct elements in
VB, one is |0⟩ — the boundary condition at the origin of D2, and another is |CS⟩ — the
boundary condition at ∂D2 that is used to reproduce the WRT invariant. Partition function
of the theory T [M3] on S1×I×S1 deﬁnes the inner product on VB and a map VB→ V∗
B.
Then we have62
ZCS(q,t ) =⟨0|CS⟩, (C.3)
Za(q,t ) = ⟨0|a⟩, (C.4)
ˆZa(q,t ) = ⟨0|ˆa⟩, (C.5)
I(q,t ) = ⟨0|0⟩, (C.6)
and also, in the unreﬁned limit,
TV(q) =ZCS(q)ZCS(q−1) =⟨0|CS⟩⟨CS|0⟩. (C.7)
Using
|CS⟩ =
∑
a
e2πikCS(a)|a⟩, (C.8)
we have
|CS⟩⟨CS| =
∑
a,b
e2πik(CS(a)−CS(b))|a⟩⟨b| =
∑
j
Oj, (C.9)
where
Oj =
∑
a
~q𝓁k(j,2a−j)|a−j⟩⟨a|, (C.10)
is the shift operator that acts on Za by
Za↦→~q𝓁k(j,2a−j)Za−j (C.11)
with
~q =e−2πik (C.12)
being the modular transform of q. The shift operators are the S-dual of Wilson loops, whose
action on the homological block for M3 =L(k, 1), as we have seen in section 4.3.1, is
ˆZa↦→qj(2a−j)ˆZa−j. (C.13)
The S-duality of type IIB string theory becomes 3d mirror symmetry of T [M3] that
exchanges Wilson loops and vortex loops (see e.g. [97] for a detailed description of the map in
a very large class of 3dN = 4 theories), and one expects thatOj corresponds to the insertion
62To obtain homological invariants, one just needs to decompactify the time S1 circle, and VB will be come
the category CB that the 3d theory T [M3] associates to S1. Then the homological invariants are identiﬁed
with Hom(B1,B 2) between two boundary conditions B1, B2 inCB.
– 74 –
of a vortex line. Similar to a Wilson loop, which carries an electric charge, a vortex loop
carries a magnetic ﬂux, creating a holonomy along its meridian — no surprise that it will
shift a which is characterized by holonomies. The relation between vortex loops and abelian
ﬂat connections can be understood more precisely using the M-theory geometry, as we now
explain.
Vortex loops come from codimension-two defects in 6d (2,0) theory and can be engineered
by a stacks of “defect M5-branes” as follows:
M5-branes: R× M3 × D2
∩ ∩
space-time: R× T∗M3× TN
∪ ∪
“defect” M5′-branes: R× M3 × T∗|O
, (C.14)
where T∗|O is the cotangent space at O. The defect ﬁvebranes have a ﬂat background 2-
form connection (“gerbe connection”) on its world volume. The vortex lines will carry ﬂuxes,
labeled by elements in H1(M3, Z)∗. Analogous to the BPS state counting analysis with M2-
branes, the non-torsion part of H1(M3, Z)∗ results in Q-exact deformations of the system,
enabling us to consider only the torsion part (Tor H1(M3, Z))∗. Taking into account multiple
ﬁvebranes gives (TorH1(M3, Λwt,g))∗/WG. In other words, non-trivial BPS vortex loop are
labeled by components of abelian ﬂat connections. For M2-branes propagating in this system
(C.14), this generates the above mentioned shift action of vortex loops on ﬂat connections.
We have now identiﬁed the system relevant for the Turaev-Viro invariant: T [M3] on
R×S2 with the insertion of a exotic defect, given by a linear combination of vortex loops, 63
whose BPS Hilbert space should categorify the TV invariant. This Hilbert space will be
doubly-graded for generic M3 and at least triply-graded for Seifert M3. In the latter case, we
will have reﬁnement for both TV invariants and the “TV homologies.” It would be interesting
to test this proposal in concrete examples, which we leave for future work.
