---
doc_id: arxiv-2205.01282v2
doc_title: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI"
section_id: sec-003-21-notations-for-graphs
section_title: "Notations for graphs"
section_number: 2.1
pages: 3-4
source_pdf: 2205.01282v2.pdf
source_sha256: 00f656afa60db838
doc_brief: "WITTEN–RESHETIKHIN–TURAEV INVARIANTS AND HOMOLOGICAL BLOCKS FOR PLUMBED HOMOLOGY SPHERES YUYA MURAKAMI — In this paper, we prove a conjecture by Gukov–Pei–Putrov–Vafa for a wide class of plumbed"
---
Γ = (V,E, (wv)v∈V ) be a plumbing graph and W be its linking matrix such that it is negative definite
and detW =±1. Here we consider the edge set E as the subset of {{v,v′}| v,v′∈V}. We identify
M|V|(Z) and End(ZV ) and consider W as the element of End( ZV ). We remark that wv∈ Z<0 for any
vertexv∈V .
For two plumbing graphs Γ and Γ ′, Neumann ([Neu80, Proposition 2.2], [Neu81, Theorem 3.1])
proved that two 3-manifolds M(Γ) and M(Γ′) are homeomorphic if and only if Γ and Γ ′ are related
by Neumann moves shown in Figure 2. Thus, we can assume wi≤− 2 for a vertex i with deg(i) = 1.
w± 1 ±1 w′± 1
···
....
←→
w w′
···
....
w± 1 ±1
···
←→
w
···
w 0 w′
···
....
←→
w +w′
···
....
Figure 2. Neumann moves
For a positive integer d, let
Vd :={v∈V | deg(v) =d}, V ≥d :={v∈V | deg(v)≥d}.
Let Wd∈ End(ZVd) and W≥d∈ End(ZV≥d) be the submatrices of W with Vd×Vd and V≥d×V≥d
components respectively. Moreover, for a positive integer e, let Wd,≥e∈ Hom(ZV≥e, ZVd) and W≥d,e∈
Hom(ZVe, ZV≥d) be the submatrices of W with Vd×V≥e and V≥d×Ve components respectively.
We need to focus on vertices with degree 1 to calculate WRT invariants and homological blocks.
For this reason, we define
v :={i∈V1|{i,v}∈ E}, M v :=
Y
i∈v
wi
for each vertex v∈V≥2. Here we define Mv := 1 if v =∅.
The condition detW =±1 implies the following lemma, which Akihito Mori told the author.
Lemma 2.1. For a vertex v∈V≥2 ={v∈V | degv≥ 2} and distinct vertices i,j ∈v, it holds that
gcd(wi,wj) = 1.
Proof. Let{ev}v∈V be the standard basis of RV . Since
Wei−Wej = (ev +wiei)− (ev +wjej) =wiei−wjej,
gcd(wi,wj) divides detW =±1. □
4 Y. MURAKAMI
