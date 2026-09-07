---
doc_id: arxiv-2104.04941v2
doc_title: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES"
section_id: sec-014-3-key-identities
section_title: "Key identities"
section_number: 3
pages: 13-14
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
doc_brief: "FOCK–GONCHAROV COORDINATES FOR SEMISIMPLE LIE GROUPS S. GILLES — Fock and Goncharov [FG06b] introduced cluster ensembles, p roviding a framework for coordi- nates on varieties of surface"
---
Here we reproduce two external results of particular signiﬁ cance to our constructions and proofs, from
[YZ08] and [FZ99]. We refer to their respective origins for m ore details. These identities allow us to perform
a program we call “adjusting a minor coordinate”. Depending on the surrounding conditions, these will allow
us to conclude that the action of mutation on T A
Q is to replace
∆ uωi,vωi(g) with ∆ u′ωi,v′ωi(q)
for some u,v,u ′,v ′.
3.1. Actions of σG. We give an overview of the identity used to justify mutations which apply σG to the
Dynkin diagram-like graph underlying a quiver, as in Remark 2.7. We use this in the proofs of Lemmas 7.1
and 7.2. This identity is collected from several results in [ YZ08], so we import some notation.
Deﬁnition 3.1. Let the reduced double Bruhat cell Ls,t =N+sN+ ∩B−tB−. (We shall not need many
facts about this object.) Recall that k⋆ =σG(k). The relation a ≺cb means that a precedesb in the Coxeter
elementc, and that a and b are connected by an edge in the Dynkin diagram associated to c.
13
We shall mostly be interested in minors of the form ∆ cmωk,cmωk . Yang–Zelevinsky denote these as xcmωk;c,
but we will avoid this for notational consistency.
The main result is that for a cluster algebra A(c) deﬁned by an initial seed with quiver of Dynkin type
associated to Coxeter element c, there exists a g ∈ Lc,c−1
such that all cluster coordinates and coeﬃcients
of A(c) are given by certain generalized minors of g. This allows combinatorially deﬁning the exchange
relations of all source or sink mutations (at vertices where all edges point out or in). These always
exchange variables of the form ∆ cmωi,cmωi with ∆ cm±1ωi,cm±1ωi . Yang–Zelevinsky refer to these as primitive
exchange relations .
Finally, a number h(i;c) is deﬁned such that ∆ ch(i;c)ωi,ch(i;c)ωi = ∆ ωi∗ ,ωi∗ . This allows convenient analysis
of periodicity of source/sink mutation sequences.
Proposition 3.2 ([YZ08, Equation 2.13]) . In some cases, h(i;c) is easily calculated.
• When i∗ =i (for example, if σG =e) we trivially have h(i;c) = 0 .
• Otherwise, when h is even, ch/2 =w0, and by action of w0 on simple roots, h(i;c) = h
2 .
When G is of type Aℓ, however, the calculation is more delicate. Let
t+ =s1s3 · · ·s2⌊(ℓ+1)/2⌋−1, t − =s2s4...s 2⌊(ℓ+1)/2⌋, w 0 =
h = ℓ + 1 factors
/bracehtipdownleft/bracehtipupright/bracehtipupleft/bracehtipdownright
t+t− · · ·t± , c =t+t−.
Then by [YZ08, Equation 2.13], as h =ℓ + 1 be the Coxeter number for Aℓ,
h(i;c) =
{
⌊ h
2 ⌋ = ⌊ ℓ+1
2 ⌋ i even
⌈ h
2 ⌉ = ⌈ ℓ+1
2 ⌉ i odd.
Note that
∆ cm+h(k;c)+1ωk,cm+h(k;c)+1ωk = ∆ cmωk∗ ,cmωk∗.
We now combine several results of [YZ08], mainly Theorem 1.5 .
Proposition 3.3. The cluster variables in A(c) satisfy the following primitive exchange relation (letting A
be the Cartan matrix):
∆ cm−1ωk,cm−1ωk ∆ cmωk,cmωk =
∏
i≺ck
(∆ cmωi,cmωi )−Ai,k
∏
k≺ci
(∆ cm−1ωi,cm−1ωi)−Ai,k + 1.
Remark 3.4. This does not give us much information about g ∈Lc,c−1
, but we will restrict our attention to
periodic mutations. The only eﬀect will be to change which ro ot the vertices of the quiver are associated to.
