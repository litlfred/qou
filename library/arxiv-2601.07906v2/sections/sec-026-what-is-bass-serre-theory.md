---
doc_id: arxiv-2601.07906v2
doc_title: "A universal sum over topologies in 3d gravity"
section_id: sec-026-what-is-bass-serre-theory
section_title: "What is Bass-Serre theory?"
section_number: null
pages: 87-89
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
toc_source: outline
doc_brief: "A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
What is Bass-Serre theory?
The idea behind Bass-Serre theory is to characterize a group G through its action on
a tree (a connected graph without loops). By studying this action, one can describe
the group as built from simpler groups, glued together using amalgamated products
and HNN extensions. The structure of the group and its tree is encoded by a graph of
groups, which consists of a finite graph, not necessarily a tree, together with a group
assigned to each vertex and each edge and so-called boundary maps. To construct
the graph of groups, one considers the quotient of the tree by the group action.
The groups assigned to the vertices and edges of the graph correspond to stabilizer
subgroups. These are the subgroups that fix a given vertex or edge of the tree under
the group action. Bass-Serre theory can be seen as the dictionary that relates graphs
of groups with groups acting on trees.
A very simple example of a tree with a group action is the integer line
,
(B.1)
continued to infinity on both the left and the right. The acting group is the group of
integers Z, which acts by discrete translation. The graph of groups is the quotient
of the tree under this action,
1
1
,
(B.2)
where 1 denotes the trivial group. The action has no fixed vertices or edges, so we
attach the trivial group to the vertex and edge in the graph. The graph of groups
allows one to reconstruct the original group G acting on the tree from the invariant
subgroups attached to it. We explain this reconstruction in detail in the next section.
– 87 –
For the case of a single loop, the group G turns out to be an HNN extension:42
G1
H
−→
G = G1 ∗H .
(B.4)
For the group of the integers, (B.2) corresponds to the presentation:
Z ∼= 1∗1 = ⟨e⟩,
(B.5)
where ⟨e⟩is the infinite cyclic group on a single generator e.
A different example is to consider the action of the infinite dihedral group D∞∼=
Z2 ∗Z2 acting on the same tree (which one can consider as an ∞-gon). Now there
are two kinds of vertices: those serving as targets and those serving as sources. We
color code them as follows
,
(B.6)
again continued indefinitely to the left and the right. The action of D∞is defined as
follows. We start by choosing a pair of adjacent blue and red vertices. We let one of
the Z2 factors act by a half-turn around the blue vertex; the other Z2 factor acts by
a half-turn around the red vertex. The graph of groups is given by
Z2
Z2
1
.
(B.7)
This graph makes the structure of D∞as an amalgamated product of two components
very explicit. More generally, the group reconstructed from a graph of groups which
is given by a single edge and two vertices is given by
G1
G2
H
−→
G = G1 ∗H G2.
(B.8)
A more complicated example is the action of the modular group, which we present
as PSL(2, Z) = ⟨S, T | S2 = 1 = (ST)3⟩, acting on the Farey tree, which is a tree
with two kinds of vertices, namely 2-valent vertices and 3-valent vertices. Edges
connect the 2-valent vertices with 3-valent vertices and we can take the orientation
42The HNN extension G∗A∼B of a group G = ⟨S | R⟩defined via some generators S and relations
R, with τ : A →B an isomorphism between two subgroups A, B ⊂G, is given by
G∗A∼B = ⟨S, t | R, tat−1 = τ(a), ∀a ∈A⟩.
(B.3)
It is also sometimes written as G∗τ, with τ the isomorphism between A and B. For an introduction
to HNN extensions, including an HNN extended version of the Seifert–van Kampen theorem see
[136], page 1685.
– 88 –
to be towards the 3-valent vertices. Here is a portion of the Farey tree with a similar
color coding,
,
(B.9)
again continued indefinitely. The S and ST elements rotate adjacent 2-valent and
3-valent vertices, respectively. As in D∞, the fundamental domain of this tree is
a single edge with two vertices; however, the stabilizer groups of the vertices are
different:
Z2
Z3
1
.
(B.10)
The idea is that the graph of groups makes the relation PSL(2, Z) ∼= Z2 ∗Z3 explicit.
As a last example, consider the similar-looking group SL(2, Z) = ⟨S, T | S4 =
(ST)6 = 1, S2 = (ST)3⟩. We can also let it act on the Farey tree (B.9). In this case,
the element S2 = (ST)3 has a trivial action, leaving the graph invariant. The graph
of groups now reads,
Z4
Z6
Z2
.
(B.11)
This time the edge has a non-trivial stabilizer group. From the graph of groups, we
can read off the group isomorphism:
SL(2, Z) ∼= Z4 ∗Z2 Z6.
(B.12)
