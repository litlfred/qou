---
doc_id: arxiv-cond-mat-0404617v2
doc_title: "String-net condensation: A physical mechanism for topological phases"
section_id: sec-010-62-n1-string-net-model
section_title: "$N=1$ string-net model"
section_number: 6.2
pages: 14-15
source_pdf: cond-mat-0404617v2.pdf
source_sha256: 8e31b9ec8ac2e034
toc_source: inferred
doc_brief: "String-net condensation: A physical mechanism for topological phases — 18 sections: Front matter; Introduction; String-nets and gauge theories"
---
The next simplest string-net model also contains only
one oriented string type - but with branching. Simple
as it is, we will see that this model contains non-Abelian
anyons and is theoretically capable of universal fault tol-
erant quantum computation [33]. Formally, the model is
deﬁned by
1. Number of string types: N = 1
2. Branching rules: {{1, 1, 1}}
3. String orientations: 1 ∗ = 1.
The string-nets are unoriented trivalent graphs. To ﬁnd
the topological phases that can emerge from these ob-
jects, we solve the self-consistency relations (8). We ﬁnd
two sets of self-consistent rules:
Φ
( )
=γ± ·Φ
( )
Φ
( )
=γ−1
± ·Φ
( )
+γ−1/ 2
± ·Φ
( )
Φ
( )
=γ−1/ 2
± ·Φ
( )
−γ−1
± ·Φ
( )
(50)
where γ± = 1±
√
5
2 . (Once again, we have omitted those
rules that can be derived from topological invariance).
Unlike the previous case, there is no closed form expres-
sion for the wave function amplitude.
Note that the second solution, d1 = 1−
√
5
2 does not
satisfy the unitarity condition (14). Thus, only the ﬁrst
solution corresponds to a physical topological phase. As
we will see, this phase is described by an SO3(3)×SO3(3)
Chern-Simons theory.
As before, the exactly soluble realization of this phase
(10) is a spin-1/2 model with spins on the links of the
honeycomb lattice. We regard a link with σx = −1 as
being occupied by a type-1 string, and a link with σx = 1
as being unoccupied (or equivalently occupied by a type-
0 string). However, in this case we will not explicitly
rewrite (10) in terms of Pauli matrices, since the resulting
expression is quite complicated.
We now ﬁnd the quasiparticles. These correspond to
irreducible solutions of (22). For this model, there are 4
such solutions, corresponding to 4 quasiparticles:
1 : n1, 0 = 1, n 1, 1 = 0, Ω 0
1, 000 = 1, Ω 1
1, 001 = 1
2 : n2, 0 = 0, n 2, 1 = 1, Ω 1
2, 110 = 1, (51)
Ω 0
2, 111 = −γ−1
+ eπi/ 5, Ω 1
2, 111 = γ−1/ 2
+ e3πi/ 5
3 : n3, 0 = 0, n 3, 1 = 1, Ω 1
3, 110 = 1,
Ω 0
3, 111 = −γ−1
+ e−πi/ 5, Ω 1
3, 111 = γ−1/ 2
+ e−3πi/ 5
4 : n4, 0 = 1, n 4, 1 = 1, Ω 0
4, 000 = 1, Ω 1
4, 110 = 1,
Ω 1
4, 001 = −γ−2
+ , Ω 0
4, 111 = γ−1
+ , Ω 1
4, 111 = γ−5/ 2
+ ,
Ω 1
4, 101 = (Ω 1
4, 011)∗ = γ−11/ 4
+ (2 − e3πi/ 5 + γ+e−3πi/ 5).
In all cases, ¯Ω = Ω ∗.
We can calculate the twists and the S-matrix. We ﬁnd:
eiθ 1 = 1, e iθ 2 = e−4πi/ 5, e iθ 3 = e4πi/ 5, e iθ 4 = 1 (52)
S = 1
1 + γ2


1 γ γ γ 2
γ −1 γ2 −γ
γ γ 2 −1 −γ
γ2 −γ −γ 1

 (53)
We conclude that W1 creates trivial quasiparticles, W2,
W3 create (non-Abelian) anyons with opposite chirali-
ties, and W4 creates bosonic bound states of the anyons.
These results agree with SO3(3) × SO3(3) Chern-Simons
theory, the so-called doubled “Yang-Lee” theory.
Researchers in the ﬁeld of quantum computing have
shown that the Yang-Lee theory can function as a univer-
sal quantum computer - via manipulation of non-Abelian
anyons. [33] Therefore, the spin-1/2 Hamiltonian (10) as-
sociated with (50) is a theoretical realization of a univer-
sal quantum computer. While this Hamiltonian may be
too complicated to be realized experimentally, the string-
net picture suggests that this problem can be overcome.
Indeed, the string-net picture suggests that generic spin
Hamiltonians with a trivalent graph structure will ex-
hibit a Yang-Lee phase. Thus, much simpler spin-1/2
Hamiltonians may be capable of universal fault tolerant
quantum computation.
