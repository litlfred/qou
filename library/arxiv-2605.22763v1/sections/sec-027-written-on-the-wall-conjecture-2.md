---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-027-written-on-the-wall-conjecture-2
section_title: "Written on the Wall, Conjecture 2"
section_number: null
pages: 58-59
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
For a graph 𝐺, let 𝑉(𝐺) be the set of vertices and 𝐸(𝐺) the set of edges. For 𝑣∈𝑉(𝐺), write
𝑑(𝑣) for the degree of 𝑣, and let 𝑁(𝑣) be the set of vertices adjacent to 𝑣in 𝐺. Let 𝛼(𝑣) be
the local independence number of 𝑣: the size of the largest independent set in 𝐺[𝑁(𝑣)]. Let
ℓ(𝐺) := 1
𝑛
Í
𝑣𝛼(𝑣) be the average of the local independence numbers, and let 𝐿𝑆(𝐺) be the
maximum number of leaves in a spanning tree of 𝐺, or 0 if 𝐺is not connected.
Theorem. If 𝐺is a simple connected graph on 𝑛vertices, then
𝐿𝑆(𝐺) ≥2(ℓ(𝐺) −1).
Proof. Let 𝑉:= 𝑉(𝐺). For every vertex 𝑣∈𝑉, fix a maximum independent set 𝐴(𝑣) in 𝐺[𝑁(𝑣)].
Then 𝛼(𝑣) = |𝐴(𝑣)|.
Now take two copies of 𝑉, and add edges 𝑢𝑣from 𝑢∈𝑉on the left to 𝑣∈𝐴(𝑢) on the
right. This forms a bipartite graph, where vertices on the left side have degree 𝛼(𝑣). The key
idea is to look at the degrees of the vertices on the right side, and formulate the entire proof
in terms of them. Formally, put 𝑐(𝑣) := |𝑢∈𝑉(𝐺) : 𝑣∈𝐴(𝑢)| as the degree of a vertex 𝑣on
the right side.
Note that 𝑐(𝑣) ≤𝑑(𝑣), for all 𝑣∈𝑉. Because Í
𝑣𝛼(𝑣) = Í
𝑣𝑐(𝑣), it is enough to show that
Í
𝑣𝑐(𝑣) ≤𝑛(𝐿𝑆(𝐺)/2 + 1). To simplify the notation, we set 𝜇:= 𝐿𝑆(𝐺)/2 + 1, and so the goal
is to show Í
𝑣𝑐(𝑣) ≤𝑛𝜇.
Lemma 1. For every edge 𝑢𝑣∈𝐸(𝐺) we have 𝑐(𝑢) + 𝑐(𝑣) ≤|𝑁(𝑢) ∪𝑁(𝑣)|.
Proof of Lemma 1. For every vertex 𝑤∈𝑁(𝑢) ∪𝑁(𝑣), at most one of 𝑢and 𝑣can be part
of 𝐴(𝑤), otherwise the edge 𝑢𝑣would contradict the fact that 𝐴(𝑤) is independent. On the
other hand, if 𝑤∈𝑉is such that 𝑢or 𝑣is in 𝐴(𝑤), then 𝑤must be part of 𝑁(𝑢) ∪𝑁(𝑣). Then
𝑐(𝑢) + 𝑐(𝑣) is at most the size of 𝑁(𝑢) ∪𝑁(𝑣). □
Lemma 2. For every edge 𝑢𝑣∈𝐸(𝐺) we have |𝑁(𝑢) ∪𝑁(𝑣)| ≤𝐿𝑆(𝐺) + 2.
Proof of Lemma 2. We construct a spanning tree in 𝐺with at least |𝑁(𝑢) ∪𝑁(𝑣)| −2 leaves.
Start with the edge 𝑢𝑣and add all the vertices in 𝑁(𝑢) ∪𝑁(𝑣) \ {𝑢, 𝑣} as pendant vertices
of degree 1. There are |𝑁(𝑢) ∪𝑁(𝑣)| −2 leaves in this tree 𝑇′. Because 𝐺is connected, we can
expand 𝑇′ to a spanning tree 𝑇of 𝐺by adding edges until no more can be added. Then from
every leaf in 𝑇′ there is a path to a leaf in 𝑇that doesn’t cross 𝑢𝑣. All these leaves must be
distinct, since they are contained in distinct subtrees of 𝑇. Then 𝑇has at least |𝑁(𝑢)∪𝑁(𝑣)|−2
leaves. □
Lemmas 1 and 2 show that for every edge 𝑢𝑣∈𝐸(𝐺),
𝑐(𝑢) + 𝑐(𝑣) ≤𝐿𝑆(𝐺) + 2 = 2𝜇.
Next, we observe that Í
𝑣𝑐(𝑣) ≤𝑛𝜇trivially holds if every 𝑐(𝑣) ≤𝜇. So assume this is
not the case. Then we can split the vertices into "heavy" vertices with 𝑐(𝑣) > 𝜇, and "light"
vertices with 𝑐(𝑣) ≤𝜇. Let 𝑆be the set of heavy vertices.
𝑆must be an independent set, since the above equation shows that for any edge 𝑢𝑣,
at most one of 𝑢or 𝑣can be heavy. Less obvious is that light vertices cannot have many
neighbors in 𝑆.
Lemma 3. If 𝑣is a light vertex, then |𝑁(𝑣) ∩𝑆| < 𝜇.
58
Advancing Mathematics Research with AI-Driven Formal Proof Search
Proof of Lemma 3. Let 𝑢∈𝑁(𝑣) ∩𝑆. Since 𝑆is independent, all neighbours of 𝑢are outside
𝑁(𝑣) ∩𝑆. So |𝑁(𝑢) ∪𝑁(𝑣)| ≥|𝑁(𝑣) ∩𝑆| + |𝑁(𝑢)|. Using Lemma 2 we get
|𝑁(𝑣) ∩𝑆| ≤|𝑁(𝑢) ∪𝑁(𝑣)| −|𝑁(𝑢)| ≤𝐿𝑆(𝐺) + 2 −𝑑(𝑢).
As 𝑑(𝑢) ≥𝑐(𝑢) > 𝜇, we obtain |𝑁(𝑣) ∩𝑆| < 𝐿𝑆(𝐺) + 2 −𝜇= 𝜇. □
Then the theorem follows from the following more general statement:
Claim. Let 𝑐: 𝑉→ℝand 𝜇≥0 satisfy:
1. 𝑐(𝑣) ≤𝑑(𝑣) for all 𝑣,
2. 𝑐(𝑢) + 𝑐(𝑣) ≤2𝜇for every edge 𝑢𝑣,
3. 𝑆:= {𝑢: 𝑐(𝑢) > 𝜇} is an independent set,
4. |𝑁(𝑣) ∩𝑆| < 𝜇for every 𝑣∉𝑆.
Then Í
𝑣𝑐(𝑣) ≤𝑛𝜇.
Proof of Claim. We assume 𝑆is non-empty, otherwise the claim is trivially true. The proof
uses a discharging argument: it sends the excess 𝑐(𝑢) −𝜇from a heavy vertex 𝑢∈𝑆to its
neighbors. The redistribution keeps the total sum Í
𝑣𝑐(𝑣) constant. However, the amount
sent to a light vertex 𝑣is less than the slack 𝜇−𝑐(𝑣), so the overall sum can’t exceed 𝑛𝜇.
Precisely, define a weight function that transfers excess from heavy to light vertices:
𝑊(𝑢, 𝑣) :=
( 𝜇−𝑐(𝑣)
𝑑(𝑢)
if 𝑢∈𝑆and 𝑢𝑣is an edge,
0
otherwise.
Because 𝑆is independent, the weight flows only from heavy to light vertices. We now show
two statements.
Each heavy vertex sends out enough weight. If 𝑢∈𝑆and 𝑢𝑣is an edge, then 𝑐(𝑢)+𝑐(𝑣) ≤2𝜇
by condition 2. So 𝜇−𝑐(𝑣) ≥𝑐(𝑢) −𝜇. Then
∑︁
𝑣∈𝑁(𝑢)
𝑊(𝑢, 𝑣) ≥𝑑(𝑢) 𝑐(𝑢) −𝜇
𝑑(𝑢)
= 𝑐(𝑢) −𝜇.
Each light vertex absorbs at most its slack. Let 𝑣∉𝑆. Then 𝑣receives weight from vertices
in 𝐹:= 𝑁(𝑣) ∩𝑆.
Let 𝑢∈𝐹. From conditions (1) and (4), we have |𝐹| < 𝜇< 𝑐(𝑢) ≤𝑑(𝑢). Then the total weight
received is
∑︁
𝑢∈𝐹
𝑊(𝑢, 𝑣) =
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
𝑑(𝑢)
<
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
|𝐹|
= 𝜇−𝑐(𝑣).
These two statements together show that
∑︁
𝑢∈𝑆
𝑐(𝑢) −𝜇≤
∑︁
𝑢∈𝑆
∑︁
𝑣∉𝑆
𝑊(𝑢, 𝑣) =
∑︁
𝑣∉𝑆
∑︁
𝑢∈𝑆
𝑊(𝑢, 𝑣) ≤
∑︁
𝑣∉𝑆
𝜇−𝑐(𝑣).
Re-arranging the terms gives Í
𝑣𝑐(𝑣) < 𝑛𝜇as desired.
□
The discovered lean proof for this is available at https://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/OEIS/GraphConjec
ture2.lean.
59
