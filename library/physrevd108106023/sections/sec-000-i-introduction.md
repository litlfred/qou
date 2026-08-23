---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots"
section_id: sec-000-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 1-2
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
doc_brief: "Knot-quiver correspondence for double twist knots — 9 sections: INTRODUCTION; DOUBLE TWIST KNOTS; Fk ˜Fk /C1/C1/C1 /C1/C1/C1 Fk ˜Fk"
---
Knot-quiver correspondence (KQC) conjectured by
Kucharski-Reineke-Stosic-Sulkowski [1] provides a new
encoding of HOMFL Y -PT invariants of knots in terms of the
representation theory of quivers. Such a correspondence
was motivated by studying the supersymmetric quiver
quantum mechanics description of BPS states in brane
systems describing knots [2].
Quivers are denoted as directed graphs with finite number
of vertices connected by oriented edges. For a quiver with n
number of vertices, the directed graph is encoded in a n × n
quiver matrix C. The diagonal elements C
ii refer to the
number of loops at the ith vertex, and the off-diagonal
elements Cij give the number of oriented edges from the
vertex i to the vertex j. Hence, the elements in the matrix C
are non-negative integers.
According to the conjecture, at least one quiver graph
QK is associated with the knot K satisfying the exponential
growth property of the symmetric r-colored HOMFLY -PT
polynomials ¯PKr ðA; qÞ (normalized appropriately) 1 as
elaborated in Refs. [1,3,4]. In the context of KQC, the
quivers are symmetric quivers. That is, CðKÞ
ij ¼ CðKÞ
ji .
Further, these quiver matrix elements can be negative
integers and be made non-negative by change of framing.
Particularly, for the knot K which obey exponential growth
property, we can write the generating series for ¯PKr ðA; qÞ in
two equivalent forms,
PQK ðxÞ¼
X
r
¯PKr ðA; qÞxr
¼
X
d
ð−qÞ
Pn
i;j diCðKÞ
ij dj xd
Yn
i¼1
Ydi
j¼1
1
1 − q2j
¼
Y
d≠0
Y
j ∈ Z
Y
k≥0
ð1 − ð−1Þjxdqjþ2kþ1Þ−Ωd;j ; ð1Þ
to extract the quiver matrix CðKÞ as well as the mo-
tivic Donaldson-Thomas invariants Ωd;j. Here, d ≡
ðd1;d2;… dnÞ ≥ 0 and xd ¼ Qn
i¼1 xdi
i with xi ¼
xAβi qαi−1ð−1Þγi .N o t et h a ts e t sfdig satisfy the condition
r ¼ d1 þ d2 þ/C1/C1/C1þ dn. The procedure to obtain such a
motivic series for any knot is still an open question.
For a class of torus knots ð2; 2p þ 1Þ, the twist knots
Kpðp ∈ ZÞ and other knots up to seven crossings the quiver
presentation were obtained [1,5]. Except for unknot and
trefoil, knots have more than one quiver presentation with
the same number of nodes, indicating that the correspon-
dence of knots to quivers is not unique. In Ref. [6],
equivalent quivers with the same number of nodes were
*vks2024@nyu.edu
Published by the American Physical Society under the terms of
the Creative Commons Attribution 4.0 International license.
Further distribution of this work must maintain attribution to
the author(s) and the published article ’s title, journal citation,
and DOI. Funded by SCOAP 3.
1This normalization includes dividing the reduced r-colored
HOMFLY -PT polynomial [PKr ðA; qÞ in variables A and q]b y q-
Pochhammerðq2; q2Þr (also known as intermediate normalization).
PHYSICAL REVIEW D 108, 106023 (2023)
2470-0010=2023=108(10)=106023(11) 106023-1 Published by the American Physical Society
shown as vertices on a permutohedra graph, giving a
systematic enumeration of such equivalent quivers.
There are also quivers with a different number of nodes
that describe the same physics, i.e., a pool of dualities in 3d
N ¼ 2 theory [7].
The physical and the geometrical interpretations of the
conjectural KQC were addressed [8] within the framework
of Ooguri-V afa large N duality. From the physics perspec-
tive, the motivic generating series of Q
K matches the vortex
partition function of 3d N ¼ 2 theory T½QK /C138 . On the
geometrical side [8], the spectrum of holomorphic curves
with a boundary on the conormal Lagrangian LK of the
knot in the resolved conifold encodes the quiver data. That
is, the basic holomorphic disks correspond to the nodes of
the quiver QK and the linking of their boundaries to the
quiver arrows.
With a double fat diagram description for arborescent
knots, the r-colored HOMFL Y -PT invariant,PKr ðA ¼ qN ;q Þ
[r refers to symmetric color ], for a
universal arborescent knot familyK involving seven param-
eters was proposed in [9,10]. Such a family includes most of
the arborescent knots up to 10 crossings. Also, the colored
HOMFLY -PT polynomials (up to four symmetric colors
for knots up to 10 crossings) have been updated in the
website [11]. Recent papers on the existence of quivers for
all rational knots, tangles, and arborescent knots [5,12]
motivated us to deduce a universal quiver for our arborescent
knot family. Even though the problem is concrete, finding
explicit quivers for this universal arborescent family appears
to be a hard problem.
As a first step, we wanted to investigate some arbores-
cent knots whose Alexander polynomial has a structure
similar to that of the twist knots K
p. That is,
ΔðXÞ¼ 1 − pX. In fact, there is a systematic reverse
engineering approach of the Melvin-Morton-Rozansky
(MMR) formalism to obtain the quiver representation for
such twist knots [13]. We observed ΔðXÞ¼ 1–4X for knot
8
