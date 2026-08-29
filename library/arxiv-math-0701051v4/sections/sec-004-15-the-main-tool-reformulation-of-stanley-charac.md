---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-004-15-the-main-tool-reformulation-of-stanley-charac
section_title: "The main tool: reformulation of Stanley character formula"
section_number: 1.5
pages: 3-4
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
main tool in our investigations will be the following reformulation of Stan-
ley character formula.
The set of cycles of a permutation π is denoted by C(π). For given
permutations σ1, σ2 ∈ Sl we shall consider colorings h of the cycles of σ1
(where each cycle is colored by the number of some column of λ) and of
the cycles of σ2 (where each cycle is colored by the number of some row of
λ). Formally, each such coloring can be viewed as a function h : C(σ1) ⊔
C(σ2) → N. We say that a coloring h is compatible with a Young diagram
λ if for all c1 ∈ C(σ1) and c2 ∈ C(σ2) if c1∩c2 ⁄= ∅ then (h(c1), h(c2)) ∈ λ;
in other words
(5) 0 < h(c1) ≤ λh(c2)
holds true for all c1 ∈ C(σ1), c2 ∈ C(σ2) such that c1 ∩ c2 ⁄= ∅.
Theorem 2 (The new formulation of Stanley character formula) . For any
Young diagram λ and a permutation π ∈ Sl (where l ≤ n) the value of the
normalized character (1) is given by
(6) Σ λ(π) =
∑
σ1,σ2∈Sl,
σ1σ2=π
(−1)|σ1| N λ(σ1, σ2),
where
(7) N λ(σ1, σ2) = # {h : h is a coloring of the cycles of σ1 and σ2
which is compatible with λ}.
Example 3. For a given factorization π = σ1σ2 it is convenient to consider
a bipartite graph with the set of vertices C(σ1) ⊔ C(σ2) and with an edge
between vertices c1 ∈ C(σ1) and c2 ∈ C(σ2) if and only if c1 ∩ c2 ⁄= ∅.
4 V ALENTIN FÉRAY AND PIOTR ´SNIADY
(1)
(2)
(12)
/Bullet
/Bullet
/Bullet
FIGURE 1. Bipartite graph associated to the factorization
(12) = (1)(2) · (12).
Notice that the value ofN λ(σ1, σ2) does not depend on the exact form ofσ1
and σ2 but only on the corresponding bipartite graph.
Figure 1 presents such a bipartite graph for π = (12) , σ1 = (1)(2) and
σ2 = (12). Now it becomes clear that
N λ(
(1)(2), (12)
)
=
∑
i
(λi)2.
Similarly,
N λ(
(12), (1)(2)
)
=
∑
i
(λ′
i)2,
where λ′ denotes the Young diagram conjugate to λ. In this way, Theorem
2 shows that
Σ λ(12) = n(n − 1) Trρλ(12)
Trρλ(e) =
N λ(
(1)(2), (12)
)
− N λ(
(12), (1)(2)
)
=
∑
i
(λi)2 −
∑
i
(λ′
i)2.
