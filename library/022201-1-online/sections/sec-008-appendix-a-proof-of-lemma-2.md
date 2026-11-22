---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-008-appendix-a-proof-of-lemma-2
section_title: "PROOF OF LEMMA 2"
section_number: Appendix A
pages: 5-6
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
Lemma 2 (restatement).
The partition function ZG(β) admits the following abstract polymer model representation:
ZG(β) = ∑
Γ∈G
∏
γ∈Γ
wγ,
where
wγ ∶=
(−β)∥γ∥
∥γ∥!∏e∈Eγmγ(e)! Tr
⎡⎢⎢⎢⎢⎣
∑
σ∈S∥γ∥
∥γ∥
∏
i=1
Φ(γσ(i))
⎤⎥⎥⎥⎥⎦
.
Proof. Our proof follows the work of Netoˇcný and Redig.3 By definition,
ZG(β) = Tr[e−βHG]
=
∞
∑
n=0
(−β)n
n!
Tr
⎡⎢⎢⎢⎢⎣
⎛
⎝∑
e∈E(G)
Φ(e)⎞
⎠
n⎤⎥⎥⎥⎥⎦
=
∞
∑
n=0
(−β)n
n!
∑
e1,...,en∈E(G)
Tr[
n
∏
i=1
Φ(ei)].
We shall now rewrite the inner sum as a product over disjoint objects. Let S = (ei)n
i=1 denote any sequence of hyperedges, and let GS be the
graph with vertex set [n] and edges between any two vertices i and j if and only if ei ∩ej ≠∅. Define a sequential polymer to be a subsequence
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-4
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
of S that corresponds to a maximally connected component of GS. Say that two sequential polymers are compatible if and only if their
corresponding subgraphs in G are vertex disjoint. Let ΓS denote the set of all sequential polymers in S. It follows that
ZG(β) =
∞
∑
n=0
(−β)n
n!
∑
S:∣S∣=n
∏
γ∈ΓS
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
.
Let ∣γ∣denote the length of a sequential polymer. Furthermore, let ΓG ∶= ∪SΓS denote the set of all sequential polymers in G, and let GG denote
the collection of all admissible sets of sequential polymers in G. Observe that for any admissible set of sequential polymers {γi}k
i=1, there are
precisely
(∑k
i=1∣γi∣)!
∏k
i=1∣γi∣! sequences S that give rise to it. Thus, we may write
ZG(β) =
∞
∑
n=0
(−β)n
n!
n
∑
k=0
1
k!
∑
m1,...,mk≥1
m1+⋅⋅⋅+mk=n
(
n
m1, . . . , mk
)
∑
γ1,...,γk∈ΓG
∣γ1∣=m1,...,∣γk∣=mk
admissible
k
∏
i=1
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
=
∞
∑
n=0
n
∑
k=0
1
k!
∑
m1,...,mk≥1
m1+⋅⋅⋅+mk=n
∑
γ1,...,γk∈ΓG
∣γ1∣=m1,...,∣γk∣=mk
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣!
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
.
By interchanging the summations over n and k, we obtain
ZG(β) =
∞
∑
k=0
1
k!
∞
∑
n=k
∑
m1,...,mk≥1
m1+⋅⋅⋅+mk=n
∑
γ1,...,γk∈ΓG
∣γ1∣=m1,...,∣γk∣=mk
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣!
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
=
∞
∑
k=0
1
k!
∑
γ1,...,γk∈ΓG
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣!
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
= ∑
Γ∈GG
∏
γ∈Γ
(−β)∣γ∣
∣γ∣!
Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
.
Now, by transforming the sum over admissible sets of sequential polymers into a sum over admissible sets of polymers and summing the
weights of their permutations, we obtain
ZG(β) = ∑
Γ∈G
∏
γ∈Γ
(−β)∥γ∥
∥γ∥!∏e∈Eγmγ(e)! Tr
⎡⎢⎢⎢⎢⎣
∑
σ∈S∥γ∥
∥γ∥
∏
i=1
Φ(γσ(i))
⎤⎥⎥⎥⎥⎦
.
Since there are equivalent sequential polymers being distinguished in the sum over permutations, i.e., permutations of repeated hyperedges,
we had to introduce a factor of
1
∏e∈Eγ mγ(e)! to avoid overcounting. This completes the proof.
■
