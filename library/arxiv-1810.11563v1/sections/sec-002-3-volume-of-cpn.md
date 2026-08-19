---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-002-3-volume-of-cpn
section_title: "Volume of CP(N)"
section_number: 3
pages: 6-7
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
To do any kind of rigorous counting of points in a continuous space we have to coarse-grain
the space. An example is counting states in classical statistical mechanics where we coarse
grain, replacing points by little balls of radiusϵ. This allows us to count states, for example
to deﬁne entropy,
S = log (#states) (3.3)
at the cost an additive term, ∆ log ϵ, ∆ being the dimension of the phase space. In order
to count states in CP (2K− 1) or unitary operators in SU (2K) we have to do something
similar.
The space of normalized states with phase modded out is the projective spaceCP (2K− 1).
Let’s calculate its volume using the usual Fubini-Study metric. The answer is not hard to
guess: it is the volume of the sphere of the same dimension divided by 2 π. The volume of
CP (N) is,
V [CP (N)] = πN
N!≈
(eπ
N
)N
(3.4)
As I said, in order to count states we need to regulate the geometry. The simplest way
to do that is to replace points by small balls of radius ϵ. The volume of an epsilon-ball of
5
dimension 2N is
V [B(2N)] = πN
N!ϵ2N≈
(eπ
N
)N
ϵ2N. (3.5)
The obvious thing to do is to divide the volume ofCP (N) by the volume of an epsilon-
ball. The result is very simple. The number of an epsilon-balls in CP (N) is ϵ−2N.
Next we replace N by 2K− 1. We identify the number of states with the number of
epsilon-balls in CP (2K).
#states =
(1
ϵ
)2(2K−1)
(3.6)
or
log (#states) = 2(2K− 1) log (1/ϵ) (3.7)
ForK = 4 and ϵ = 1/2 this gives 1, 073, 741, 824 ϵ-balls.
Equation 3.7 shows the same pattern as 2.2. It grows rapidly with K like 2K, and is
only logarithmically sensitive to the cutoﬀ parameter.
