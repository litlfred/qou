---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-014-41-basic-structure
section_title: "Basic structure"
section_number: 4.1
pages: 15-16
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
compact Lie group) was initially studied by Witten in [Wit89, Wit91]. It is a topologi-
cal quantum ﬁeld theory in three-dimensions, whose action is a sum of holomorphic and
antiholomorphic copies of the usual Chern-Simons action
(37) S(A,A) = t
8πICS(A) +
˜t
8πICS(A),
whereA is a connection on aGC bundle over a 3-manifoldM, andICS(A) =
∫
M(AdA+ 2
3A3)
(with additional boundary terms if M is not closed). In order for the path-integral measure
exp(−iS) to be invariant under all gauge transformations of A, the levels t, ˜t must obey the
quantization condition
(38) k := 1
2(t + ˜t)∈ Z.
16 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
Additionally, the theory is unitary for σ := 1
2(t− ˜t)∈ iR, and less obviously so for σ∈ R.
We will not require unitarity in the following, however.
The classical solutions of Chern-Simons theory are ﬂat GC connections. Indeed, in the
limitt, ˜t→∞ , which corresponds to inﬁnitely weak coupling, the partition functionZ(t, ˜t) =∫
DADAe−iS is dominated by ﬂat connections
Z(t, ˜t)∼
∑
ﬂatA∗
τ(A∗) exp
[ t
8πiICS(A∗) +δ(A∗) logt +
∞∑
n=2
(8πi
t
)n−1
Sn(A∗)
]
(39)
×τ(A
∗
) exp
[ ˜t
8πiICS(A
∗
) +δ(A∗) logt +
∞∑
n=2
(8πi
˜t
)n−1
Sn(A
∗
)
]
whereτ(A)−2 is a Ray-Singer torsion twisted by the ﬂat connectionA and theSn are “higher-
loop” topological invariants. For GC =SL(2, C) andA∗ the hyperbolic ﬂat connection, such
an asymptotic expansion at weak coupling played a central role in the generalized Volume
Conjecture [Guk05].
