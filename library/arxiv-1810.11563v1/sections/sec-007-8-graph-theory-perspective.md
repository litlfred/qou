---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-007-8-graph-theory-perspective
section_title: "Graph Theory Perspective"
section_number: 8
pages: 17-21
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
Circuits can be usefully described using graph theory7. I’ll call a graph describing a circuit
a circuit graph.
Let’s begin at the identity and act with a circuit of depth one, in other words a circuit
of a single step with K/2 gates. For simplicity let’s assume the allowed gate set is a single
non-symmetric two-qubit gate. A choice must be made of how the K qubits are paired.
Each pairing will lead to a diﬀerent unitary. I’ll call the number of possible choices d (an
odd choice of notation but it corresponds with standard graph-theory notation). It’s an
easy combinatoric exercise to compute d,
d∼ K!
(K/2)!∼
(2K
e
)K
2
(8.22)
Let’s visualize this by a decision-tree embedded in SU (2K). At the central vertex is
the identity operator. The branches (or edges) correspond to the d choices.
7See also Henry Lin, “Caley Graphs and Complexity Geometry”, https://arxiv.org/pdf/1808.
06620.pdf.
16
Figure 7: Vertex with d = 8.
The number of branches or edges d at a vertex is called the degree of that vertex. In
our construction every internal vertex has degree K!
(K/2)!. A graph in which every vertex
has degree d is called d-regular. But so far the circuit graph is not d-regular because the
outer boundary vertices have a single edge. The leaves of the graph are unitary operators
in SU (2K).
Now let’s grow the circuit depth by adding another step. I’m going to make one
restriction of a technical nature. For large K it makes no diﬀerence but it simpliﬁes
things. I will assume that when I add a step the choice of pairings is not the same as in
the previous step. This implies that the next layer of the tree has
K!
(K/2)!− 1
new branches. This is shown in ﬁgure 8
17
Figure 8: Regular tree with degree 8, depth 2.
Now comes an important assumption which underlies everything I will say. Each
endpoint (leaf) of the tree represents a unitary operator. I will assume that the probability
of two leaves being the same unitary is vanishingly small. Basically the reason is the
extremely high dimension of the space of unitaries. If two leaves represent the same
unitary to within ϵ I will say that a collision occurred. My provisional assumption is that
collisions are so rare that they can be ignored.
This no-collision assumption must eventually break down as the tree grows outward
and we will calculate when that happens. But for now let’s ignore collisions.
Assuming no-collisions, the number of unitaries that have been reached at depth D is,
#unitaries =dD≈
(2K
e
)DK
2
(8.23)
The number of gates in a circuit of depth D is DK/2. Assuming no-collisions, the
path to each leaf is the minimal path, implying that the number of gates is the complexity.
Thus we can write,
18
#unitaries =
(2K
e
)C
∼ eC logK (8.24)
Let me rephrase this formula in the following way:
The sub-volume of SU (2K) that corresponds to unitaries of complexity C grows exponen-
tially with C.
It says a number of things. First of all if we think of complexity as the distance from the
origin (the unit operator ) then it says that the volume grows exponentially with radius—a
characteristic of hyperbolic spaces of negative curvature. This may seem surprising: with
the usual bi-invariant metric SU (2K) is positively curved. But we are talking about a
diﬀerent metric, relative complexity. This negative curvature is a symptom of chaos and
in my opinion it, not fast scrambling, is the general signature of quantum chaos.
Equation 8.24 suggests something else. In classical statistical mechanics the volume of
phase space associated with an ensemble of states of a given entropy is exponential in the
entropy. The exponential growth of volume in SU (2K) associated with a given complexity
is the basis for a deep analogy between complexity and entropy, including a Second Law
of Complexity. It can be summarized by the slogan: Complexity is the entropy of the
auxiliary systemA.
One more point about the circuit graph and its embedding in SU (2K). Figures 7
and 8 are very schematic. It is diﬃcult to accurately convey the actual properties of the
embedding with pictures given the fact that the space is extremely high dimensional. One
thing to keep in mind is that with the usual bi-invariant metric, SU (2K) is small in the
sense that the largest distance is π/2. A single one-step circuit will move U about that
distance. So although the tree abstractly grows outward from the center as in the left
panel of ﬁgure 9, the embedding in SU (2K) looks more like the right panel.
19
Figure 9: Two views of the circuit tree. On the left is an abstract decision tree. The
complexity of the unitary leaf grows linearly with the number of steps from the identity
at the center. Relative complexity is proportional to the number of steps between leaves.
On the right the tree is embedded in SU (2K) with the usual inner product metric.
The epsilon balls get ﬁlled in by the growing circuit in a very fractal manner which is
related to the fact mentioned earlier that complexity is discontinuous as ϵ→ 0.
