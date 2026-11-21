---
doc_id: qt2pf5d0mn
doc_title: "UC Santa Barbara"
section_id: sec-014-pachner-moves
section_title: "Pachner Moves"
section_number: null
pages: 81-83
source_pdf: qt2pf5d0mn.pdf
source_sha256: 4c8581c3b46398e3
toc_source: outline
doc_brief: "UC Santa Barbara — 19 sections: Front matter; Abstract; Introduction"
---
The map Φ restricted to the component V +
F (τ) ⊗V −
F (τ) is the map Φ′:
V +
F (τ) ⊗V −
F (τ)
V sgn(sτ)(H1(τ)) ⊗V −sgn(sτ)(H2(τ))
V sgn(sτ)
F ′
(τ ′) ⊗V −sgn(sτ)
F ′
(τ ′)
V (H1)⊗V (H2)
can⊗can
To show Φ′(φF,τ) = φF ′,τ ′, it suﬃces to show Φ′ preserves the pairing. Since the canonical
isomorphisms preserves the pairing, it suﬃces then to show (I ⊗can) ◦(V (H1) ⊗V (H2))
in the the following diagram does.
V +
F (τ) ⊗V −
F (τ)
V sgn(sτ)(H1(τ)) ⊗V −sgn(sτ)(H2(τ))
V sgn(sτ)(H1(τ)) ⊗V −sgn(sτ)(H1(τ))
V (H1)⊗V (H2)
V (H1)⊗V (H1)
I⊗can
By Lemma 4.2.4, the above diagram commutes, and by Lemma 4.2.5, V (H1)⊗V (H1)
preserves the pairing.
4.3
Pachner Moves
Let M = M n be any closed manifold of dimension n. A triangulation T of M means
a simplicial complex T such that the underline topological space T top is homeomorphic
to M.
Pachner moves are set of local operations on triangulations which convert a
triangulation of M to any other triangulation of the same manifold.
Let σn be any n-simplex. Its boundary, denoted by ∂(σn), consists of n + 1 (n −1)-
simplices. Let ∂(σn) = I ⊔J be a bi-partition of ∂(σn) into (disjoint) sets I and J such
that |I| = k, |J| = n + 1 −k. We say two triangulations T , T ′ are related by a pachner
move of type (k, n + 1 −k) if I ⊂T and T ′ = (T \ I) ∪J for some σk, I, J. Apparently,
72
Section 4.3
Pachner Moves
(1,2)
←→
Figure 4.5: Pachner move (1, 2); n = 1
(1,3)
←→
(2,2)
←→
Figure 4.6: Pachner moves (1, 3), (2, 2); n = 2
pachner moves of types (k, n + 1 −k) and (n + 1 −k, k) are inverse operations if the
partitions are taken to be (I, J) and (J, I) respectively. If two triangulations are related
by a pachner move, then their underlying spaces are homeomorphic.
Theorem 4.3.1 [49] Let M = M n a closed manifold and T , T ′ be two triangulations of
M, then there is a sequence of triangulations of M, T = T0, T1, · · · , Tk = T ′, such that
any two neighboring triangulations are related by a pachner move of type (k, n + 2 −k),
1 ≤k ≤n
2 + 1, or its inverse.
Some examples of pachner moves are listed as follows.
If dim(M) = n = 1, we have pachner moves of type (1, 2) and (2, 1) which are inverse
to each other. See Figure 4.5.
If n = 2, we have pachner moves of type (1, 3), (2, 2), and (3, 1). See Figure 4.6.
We are more interested in the case n = 4, where we have pachner moves of types
(3, 3), (2, 4), (1, 5) and their inverses.
Given a 5-simplex σ5, we order its vertices by
0, 1, 2, 3, 4, and denote the face which does not contain the vertex i by (0 · · ·ˆi · · · 4). For
each type of pachner moves, we pick a speciﬁc partition I, J, and call it the typical
73
Section 4.4
