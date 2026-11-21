---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-024-a-variant-of-the-graph-reconstruction-conjecture
section_title: "A variant of the Graph Reconstruction Conjecture"
section_number: null
pages: 47-51
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
The Kelly-Ulam graph reconstruction program aims to recover a graph from its deck of
one-vertex-deleted subgraphs [62, 36]. A standard bipartite version was formulated by
Bondy and Hemminger as the problem of showing that bipartite graphs are reconstructible
[10]. The following theorem proves a structured incidence-deletion analogue under strong
type-distinguishability assumptions.
Terminology Let Ω = 𝐿⊔𝑅be a finite vertex set with a partition into the disjoint parts
𝐿, 𝑅⊆Ω. A graph 𝐾is bipartite with respect to (𝐿, 𝑅) if every edge of 𝐾has one endpoint in
𝐿and one endpoint in 𝑅. We say 𝐾is 2-connected if 𝐾is connected and, for every vertex 𝑣,
the induced graph on Ω \ {𝑣} is connected. For a graph 𝐾and a vertex 𝑣, write 𝐾\inc 𝑣for
the graph obtained from 𝐾by deleting all edges incident to 𝑣, while leaving the vertex set
unchanged. Thus
𝐸(𝐾\inc 𝑣) = {𝑥𝑦∈𝐸(𝐾) : 𝑥≠𝑣, 𝑦≠𝑣}.
A bipartite isomorphism 𝐾𝐵𝐾′ is a graph isomorphism whose underlying bijection preserves
both parts 𝐿and 𝑅. The bipartite deck is the multiset
D𝐵(𝐾) := {{[𝐾\inc 𝑣]𝐵: 𝑣∈Ω}},
47
Advancing Mathematics Research with AI-Driven Formal Proof Search
where [·]𝐵denotes bipartite-isomorphism class. Let 𝑁𝐾(𝑥) be the neighbor set of 𝑥in 𝐾. The
degree profile and type of 𝑥are
𝑃𝐾(𝑥) := {{deg𝐾(𝑦) : 𝑦∈𝑁𝐾(𝑥)}},
𝜏𝐾(𝑥) := (deg𝐾(𝑥), 𝑃𝐾(𝑥)).
The type profile of 𝑢is the multiset of the types of its neighbors:
𝑇𝐾(𝑢) := {{𝜏𝐾(𝑥) : 𝑥∈𝑁𝐾(𝑢)}}.
Finally, for a type 𝑡= (𝑑, 𝑀) ∈ℕ× Multiset(ℕ) and 𝑎∈ℕ, define
𝐹𝑎(𝑡) := (max(𝑑−1, 0), 𝑀\ {𝑎}),
where 𝑀\ {𝑎} means deletion of one occurrence of 𝑎from the multiset 𝑀. In the applications
below, 𝐹𝑎is applied to neighbor-types, whose first coordinate is positive, so max(𝑑−1, 0) =
𝑑−1 there. We write #𝑡𝑀for the multiplicity of 𝑡in a multiset 𝑀.
Theorem (Weak bipartite graph reconstruction) Let 𝐺and 𝐻be finite simple graphs on
the same finite vertex set Ω, both bipartite with respect to the same parts Ω = 𝐿⊔𝑅and
|Ω| ≥3. Assume that 𝐺is 2-connected and all vertex types of 𝐺are pairwise distinct, that is,
𝜏𝐺(𝑥) ≠𝜏𝐺(𝑦) if 𝑥≠𝑦. If D𝐵(𝐺) = D𝐵(𝐻), then 𝐺and 𝐻are bipartite-isomorphic.
Proof. Write 𝑛= |Ω| and 𝑒(𝐾) = |𝐸(𝐾)|. Since bipartite isomorphisms preserve edge counts,
the deck determines the multiset
{{𝑒(𝐾\inc 𝑣) : 𝑣∈Ω}}.
For every vertex 𝑣,
𝑒(𝐾\inc 𝑣) + deg𝐾(𝑣) = 𝑒(𝐾),
(1)
because 𝐾\inc 𝑣removes exactly the edges incident to 𝑣. Also,
∑︁
𝑣∈Ω
𝑒(𝐾\inc 𝑣) = (𝑛−2)𝑒(𝐾),
(2)
because each edge of 𝐾remains in precisely the cards indexed by the 𝑛−2 vertices not
incident to that edge. Since 𝑛≥3, equation (2) shows that the deck determines 𝑒(𝐾).
Applying this to the equal decks of 𝐺and 𝐻gives
𝑒(𝐺) = 𝑒(𝐻),
(3)
and then equation (1) shows that the degree multisets of 𝐺and 𝐻are equal.
Equality of the two decks also gives a bijection 𝑓: Ω →Ω such that, for every 𝑣∈Ω,
there is a bipartite isomorphism
𝜙𝑣: 𝐺\inc 𝑣𝐵𝐻\inc 𝑓(𝑣).
(4)
For this matched pair of cards, edge counts are equal. Combining this with (1) and (3) yields
deg𝐺(𝑣) = deg𝐻( 𝑓(𝑣))
(5)
for every 𝑣.
48
Advancing Mathematics Research with AI-Driven Formal Proof Search
Next, 𝐺has minimum degree at least 2. Indeed, if a vertex had degree 0, then 𝐺would
not be connected; if a vertex 𝑥had the unique neighbor 𝑦, then the induced graph on Ω \ {𝑦}
would contain the isolated vertex 𝑥, contradicting 2-connectivity. Since the degree multisets
of 𝐺and 𝐻are equal, 𝐻also has minimum degree at least 2.
Therefore, in any graph 𝐾with minimum degree at least 2, the card 𝐾\inc 𝑣has a unique
isolated vertex, namely 𝑣. Indeed, the vertex 𝑣is isolated because all its incident edges have
been removed. On the other hand, if 𝑥≠𝑣, then 𝑥has at least two neighbors in 𝐾, at most
one of which is 𝑣; hence 𝑥has a neighbor 𝑦≠𝑣, and the edge 𝑥𝑦remains in 𝐾\inc 𝑣.
Applying this uniqueness to (4), the isomorphism 𝜙𝑣sends the unique isolated vertex of
𝐺\inc 𝑣to the unique isolated vertex of 𝐻\inc 𝑓(𝑣). Hence
𝜙𝑣(𝑣) = 𝑓(𝑣).
(6)
Since 𝜙𝑣preserves 𝐿and 𝑅, (6) implies that 𝑓preserves the two parts:
𝑣∈𝐿⇐⇒𝑓(𝑣) ∈𝐿,
𝑣∈𝑅⇐⇒𝑓(𝑣) ∈𝑅.
(7)
We now prove that 𝑓preserves vertex types. It remains, in view of (5), to compare degree
profiles. For a graph 𝐾and vertex 𝑣, put
𝐴𝐾(𝑘) := #{𝑥∈Ω : deg𝐾(𝑥) = 𝑘},
𝐵𝐾,𝑣(𝑘) := #{𝑥∈Ω : deg𝐾\inc𝑣(𝑥) = 𝑘},
and
𝐶𝐾,𝑣(𝑘) := #{𝑥∈𝑁𝐾(𝑣) : deg𝐾(𝑥) = 𝑘}.
Counting vertices of degree 𝑘before and after deleting the incidence set of 𝑣gives, for every
𝑘≥0,
𝐶𝐾,𝑣(𝑘+ 1) + 𝐴𝐾(𝑘) + 1𝑘=0 = 𝐶𝐾,𝑣(𝑘) + 𝐵𝐾,𝑣(𝑘) + 1deg𝐾(𝑣)=𝑘.
(8)
Indeed, in 𝐾\inc 𝑣, every non-neighbor of 𝑣keeps its degree, while every neighbor of 𝑣has
its degree lowered by 1. Hence the vertices of degree 𝑘in 𝐾\inc 𝑣are precisely the old
non-neighbors of degree 𝑘, the old neighbors of degree 𝑘+ 1, and additionally 𝑣itself if 𝑘= 0.
Therefore
𝐵𝐾,𝑣(𝑘) = 𝐴𝐾(𝑘) −𝐶𝐾,𝑣(𝑘) −1deg𝐾(𝑣)=𝑘+ 𝐶𝐾,𝑣(𝑘+ 1) + 1𝑘=0.
Since the global degree multisets are equal, 𝐴𝐺(𝑘) = 𝐴𝐻(𝑘). Since 𝜙𝑣is an isomorphism
between the matched cards, 𝐵𝐺,𝑣(𝑘) = 𝐵𝐻, 𝑓(𝑣)(𝑘). By (5), the final indicator in (8) is also
the same for 𝐺and 𝐻. Finally, 𝐶𝐾,𝑣(0) = 0, because a neighbor always has positive degree.
Induction on 𝑘in (8) gives
𝐶𝐺,𝑣(𝑘) = 𝐶𝐻, 𝑓(𝑣)(𝑘)
(𝑘≥0).
Thus
𝑃𝐺(𝑣) = 𝑃𝐻( 𝑓(𝑣)),
and together with (5) this proves
𝜏𝐺(𝑣) = 𝜏𝐻( 𝑓(𝑣))
(9)
49
Advancing Mathematics Research with AI-Driven Formal Proof Search
for every 𝑣∈Ω. We next prove equality of type profiles:
𝑇𝐺(𝑢) = 𝑇𝐻( 𝑓(𝑢))
(10)
for every 𝑢. Fix 𝑢. If 𝑢∈𝐿, take 𝑆= 𝑅, otherwise take 𝑆= 𝐿(thus 𝑆is the opposite side from
𝑢). By (7) and (9), the multisets of global types on 𝑆agree:
{{𝜏𝐺(𝑥) : 𝑥∈𝑆}} = {{𝜏𝐻(𝑥) : 𝑥∈𝑆}}.
(11)
The card isomorphism 𝜙𝑢also preserves 𝑆, and therefore the multisets of local types on 𝑆
agree:
{{𝜏𝐺\inc𝑢(𝑥) : 𝑥∈𝑆}} = {{𝜏𝐻\inc 𝑓(𝑢)(𝑥) : 𝑥∈𝑆}}.
(12)
For 𝑥∈𝑆, bipartiteness gives the local-type formula
𝜏𝐺\inc𝑢(𝑥) =
(
𝐹deg𝐺(𝑢)(𝜏𝐺(𝑥)),
if 𝑥∈𝑁𝐺(𝑢),
𝜏𝐺(𝑥),
if 𝑥∉𝑁𝐺(𝑢).
(13)
Indeed, if 𝑥is adjacent to 𝑢, then deleting the incidence set of 𝑢removes the edge 𝑢𝑥, lowering
deg𝐺(𝑥) by one and deleting one occurrence of deg𝐺(𝑢) from the degree profile of 𝑥. If 𝑥is
not adjacent to 𝑢, then any neighbor of 𝑥lies on the same side of the bipartition as 𝑢, and
therefore cannot be adjacent to 𝑢; hence the type of 𝑥is unchanged. The same formula holds
for 𝐻and 𝑓(𝑢).
Taking the number of occurrences of an arbitrary type 𝑡in (13) gives
#𝑡{{𝜏𝐺\inc𝑢(𝑥) : 𝑥∈𝑆}} + #𝑡𝑇𝐺(𝑢) = #𝑡{{𝜏𝐺(𝑥) : 𝑥∈𝑆}} + #𝑡{{𝐹deg𝐺(𝑢)(𝑠) : 𝑠∈𝑇𝐺(𝑢)}}.
(14)
There is an identical identity for 𝐻. The first terms on the two sides of (14) agree by (12),
and the global-type terms agree by (11). Also deg𝐺(𝑢) = deg𝐻( 𝑓(𝑢)) by (5). Hence equality
of the type-profile counts can be proved by descending induction on the first coordinate of 𝑡.
The base case is that no type in a type profile can have first coordinate at least 𝑛, since every
vertex degree is < 𝑛. For the induction step, the only types 𝑠with 𝐹deg𝐺(𝑢)(𝑠) = 𝑡have first
coordinate 𝑡1 + 1; moreover every 𝑠occurring in a type profile has positive first coordinate.
Thus the rightmost term in (14) is already equal for 𝐺and 𝐻by the induction hypothesis,
and subtracting the two versions of (14) yields equality of the number of occurrences of 𝑡in
𝑇𝐺(𝑢) and in 𝑇𝐻( 𝑓(𝑢)). This proves (10).
The distinctness of types transfers from 𝐺to 𝐻: if 𝜏𝐻(𝑥) = 𝜏𝐻(𝑦), then by applying (9) to
𝑓−1(𝑥) and 𝑓−1(𝑦) we obtain equality of the corresponding 𝐺-types, so 𝑥= 𝑦.
Since types are pairwise distinct, adjacency is determined by type profiles: for every
graph 𝐾among 𝐺, 𝐻and every pair of vertices 𝑎, 𝑏,
𝐾has edge 𝑎𝑏
⇐⇒
𝜏𝐾(𝑏) ∈𝑇𝐾(𝑎).
(15)
The forward implication is the definition of 𝑇𝐾(𝑎). Conversely, if 𝜏𝐾(𝑏) occurs in 𝑇𝐾(𝑎), then
some neighbor 𝑐of 𝑎has 𝜏𝐾(𝑐) = 𝜏𝐾(𝑏), and distinctness of types gives 𝑐= 𝑏.
Finally, for any 𝑢, 𝑣∈Ω, equations (9), (10), and (15) give
𝐺has edge 𝑢𝑣⇐⇒𝜏𝐺(𝑣) ∈𝑇𝐺(𝑢) ⇐⇒𝜏𝐻( 𝑓(𝑣)) ∈𝑇𝐻( 𝑓(𝑢)) ⇐⇒𝐻has edge 𝑓(𝑢) 𝑓(𝑣).
50
Advancing Mathematics Research with AI-Driven Formal Proof Search
Thus 𝑓is a graph isomorphism 𝐺 𝐻. By (7), it preserves the two bipartition parts, so it is a
bipartite isomorphism.
□
The Lean proof discovered for this problem is at https://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/AICollaborator/G
raphs/bipartite_graph_reconstruction_conjecture_2.lean.
