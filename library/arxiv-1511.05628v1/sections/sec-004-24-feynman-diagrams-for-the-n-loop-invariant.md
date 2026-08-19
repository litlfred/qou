---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-004-24-feynman-diagrams-for-the-n-loop-invariant
section_title: "Feynman diagrams for the n-loop invariant"
section_number: 2.4
pages: 8-9
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
diagram formulation of the higher-loop invariants. A Feynman diagram D is a ﬁnite graph
possibly with loops and multiple edges. To every edge in a Feynman diagram we associate
the symmetric N×N propagator matrix
(24) Π = ℏk(−B−1A + ∆z′)−1,
and to a vertex with valence j we associate the vertex factor Γ (j), which is a tensor of rank
j whose only nonzero entries Γ (j)
i := Γ(j)
ii...i∈FG,k( (ℏ) ) lie on the diagonal, and are functions
of m∈ (Z/kZ)N and θ,
(25)
Γ(0) = ℏ
8kfB−1ν +
∞∑
n=2
ℏn−1
n!
k∑
s=1
Bn
(s
k
) N∑
i=1
Li2−n(ζmi+sθ−1
i )
Γ(1)
i =− 1
2k(B−1ν)i−
∞∑
n=1
ℏn−1
kn !
k∑
s=1
Bn
(s
k
)
Li1−n(ζmi+sθ−1
i )
Γ(2)
i =
∞∑
n=1
ℏn−1
k2n!
k∑
s=1
Bn
(s
k
)
Li−n(ζmi+sθ−1
i )
Γ(j)
i =
∞∑
n=0
(−1)jℏn−1
kjn!
k∑
s=1
Bn
(s
k
)
Li2−n−j(ζmi+sθ−1
i ) ( j≥ 3),
whereBn(x) are the Bernoulli polynomials, deﬁned by text/(et− 1) =∑
n≥0Bn(x)tn/n! and
FG,k( (ℏ) ) denotes the ring of formal Leurent series in ℏ with coeﬃcients in FG,k.
Note that each Γ (j)
i only depends on m, θthrough the combination ζmiθ−1
i . Moreover, all
thel-polylogarithms appearing here involve non-positivel, hence are rational functions. The
evaluation [D]m of a diagram is obtained by contracting propagator and vertex indices, and
multiplying by a standard symmetry factor 1/|σ(D)|, whereσ(D) is the diagram’s symmetry
group,
(26) [ D]m = 1
|σ(D)|
∑
coincident indices
∏
edges e
Π(e)
∏
verticesv
Γ(v).
For example, the diagram in the center of the top row of Figure 2 has an evaluation [ D]m =
1
8
∑N
i,i′=1 ΠiiΓ(3)
i Πii′Γ(3)
i′ Πi′i′. To the trivial diagram• that consists of one vertex and no edges
we associate the vacuum energy [•]m = Γ(0). The next Lemma follows from evaluating the
formal Gaussian integral (21) in terms of Feynman diagrams; see [BIZ80].
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 9
Lemma 2.8. For a Z-non-degenerate Neumann-Zagier datum γ, we have
(27) φ+
γ,ζ(ℏ) = Av
[
exp
( ∑
connected D
[D]m
)]
∈ 1 + ℏ C[ [ℏ] ],
where the sum is over all connected diagrams D, including the empty diagram.
Using the above Lemma and Equation (22), it follows that in order to compute Sγ,n for
n≥ 2, it suﬃces to consider the ﬁnite set of Feynman diagrams with
(28) #(1-vertices) + #(2-vertices) + #(loops) ≤n,
and to truncate the formal power series in each of the vertex factors to ﬁnite order in ℏ. In
the next two sections, we give axplicit formulas for the 2 and 3-loop invariants.
