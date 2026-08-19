---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-003-31-4d-bps-states
section_title: "4d BPS states"
section_number: 3.1
pages: 12-14
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
Now we recall the geometric description of BPS states in S[g,C,D ].
All such BPS states arise from BPS strings of the six-dimensional S[g], which are
extended along C and hence look like point particles in the remaining 3+1 dimensions.
Roughly there are
(K
2
)
distinct kinds of BPS string, but the topological twisting and com-
pactiﬁcation makes the story slightly trickier, as we now recall.
An oriented segment of string passing through a pointz∈C is labeled by the choice of
a pair of distinct sheets of the K-fold covering Σ→C, i.e. two solutions λ(i), λ(j) (i⁄=j)
of the degree-K polynomial equation (2.1), in a neighborhood of z. To keep track of this
discrete label, we use the term “ij-string” rather than just “string.” Reversing orientation
exchangesij-strings and ji-strings.
TheN = 2 central charge Z of an ij-string is obtained by integrating the complex
1-form 1
π(λ(i)−λ(j)) along the string. The massM of anij-string is obtained by integrating
the real density 1
π|λ(i)−λ(j)|.
When is such a string BPS? Introduce a local coordinate on C byw(ij) =
∫
λ(i)−λ(j),
and then deﬁne an ij-trajectory with phase ϑ to be a straight line in the w(ij)-coordinate,
with inclination ϑ, i.e. a line along which
Im(e−iϑ ˙w(ij)) = 0. (3.1)
An ij-trajectory is naturally oriented: the positive direction is the direction in which
Re(e−iϑw(ij)) increases. Reversing orientation of an ij-trajectory gives a ji-trajectory. An
ij-string is BPS if and only if it is stretched along an ij-trajectory with some phase ϑ; we
call such a string a “BPS string of phase ϑ.” We see at once that for BPS strings |Z| =M
as expected. The phase ϑ determines which supercharges the BPS string preserves.
Anij-string can end in two ways. First, it can end on an (ij)-branch point, i.e. a point
where λ(i)−λ(j) = 0.6 Second, it can end on a junction where an ij-string, jk-string and
ki-string meet (all oriented into the junction.) In the latter case, for the combined web of
strings to be BPS, all three strings must be BPS strings with the same phase ϑ.
BPS states in S[g,C,D ] arise from webs of BPS strings, such that all strings in the
web have ﬁnite total central charge. This condition means that the strings are either closed
loops or have both ends on branch points or junctions. We call these ﬁnite webs . Some
possible topologies for ﬁnite webs are shown in Figure 2.
The charges of the BPS states are determined by the topology of the webs, in the
following way. An ij-string stretched along an oriented path p on C can be lifted in a
canonical way to pΣ, a union of oriented curves on Σ: namely, pΣ is the union of the lift
p(i) of p to the i-th sheet and the lift −p(j) of−p (p with reversed orientation) to the j-th
sheet. Letting p run over the strings in a ﬁnite web N, the union of the pΣ is a closed
6We use the notation (ij) for the branch points butij for the trajectories; the (ij) is meant to denote the
transposition associated to the branch point, which exchanges sheet i and sheet j of the covering Σ→C.
In particular (ij) = (ji).
– 10 –
(23)
(12)
12
23 31
(31)
(12)
12
(12)
(12)
12
23
(23)
31
(12)
(23)
32
21
(12)
12
23
(23)
31
(12)
(23)
32
21
43
41
42
12
(12)
12
23
(23)
31
12
23
(31)
Figure 2. Some possible topologies for ﬁnite webs of BPS strings. An orange cross with label ( ij)
denotes an (ij)-branch point. Wherever a string with label ij appears, it could equally well have
been represented by a string with label ji and the opposite orientation.
1-cycle NΣ on Σ. NΣ has a homology class [NΣ]∈ Γ :=H1(Σ; Z). This [NΣ] is the charge
of the BPS state. 7
The central charge of a ﬁnite web N is the sum of the central charges of the strings in
N; this gives a simple result which depends only on γ = [NΣ],
Zγ = 1
π
∮
γ
λ. (3.2)
To determine the BPS spectrum of the theory, in particular the second helicity su-
pertrace Ω(γ), one should in principle proceed by quantizing the zero modes of each ﬁnite
web. This would give some deﬁnite formula for the contribution of each ﬁnite web to Ω(γ).
In practice, such a quantization has not been completely carried out, and we will not do it
here either.8 Rather, we will explain a more indirect route, which determines Ω( γ) using
the interactions between 2d and 4d BPS states.
One could also ask about extending Ω( γ) to an object which keeps track of the spins
of the BPS multiplets appearing. Such “reﬁned BPS degeneracies” and “protected spin
characters” have been considered in the N = 2 context e.g. in [9, 21, 34–36]. We will not
consider that extension in this paper.
7The precise charge lattice of the theory S[g,C,D ] is actually a subquotient of H1(Σ; Z), as explained
in [3]. Nevertheless, in this paper, we consider Γ = H1(Σ; Z) for simplicity.
8In [3] we used wall-crossing to determine Ω(γ) in the caseK = 2, reproducing earlier results of [6]. That
case is particularly simple since there are only two possible topologies for ﬁnite webs: one can either have a
single string connecting two branch points or a single closed loop. These topologies contribute Ω( γ) = +1
and Ω(γ) =−2 respectively. We will reproduce this result yet again in §5.7 below.
– 11 –
