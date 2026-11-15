---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-009-appendix-b-proof-of-lemma-4-and-lemma-7
section_title: "PROOF OF LEMMA 4 AND LEMMA 7"
section_number: Appendix B
pages: 6-8
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
Lemma 4. (restatement).
Fix Δ ∈Z+. Let G = (V, E) be a graph of maximum degree at most Δ, and let β be a complex number such that
∣β∣≤
1
e4Δ. The cluster expansion for log(ZG(β)) converges absolutely, ZG(β) ≠0, and for m ∈Z+,
∣Tm(ZG(β)) −log(ZG(β))∣≤∣V∣e−m.
Proof. For convenience, we normalize the trace so that Tr(I) = 1. Note that this is equivalent to a rescaling of the partition function by
a multiplicative factor. We introduce a polymer γx to every vertex x in G consisting of only that vertex. We define γx to be incompatible with
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-5
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
every polymer that contains x. Then, we have
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤∑
γ≁γx
e∣γ∣+∥γ∥+1∣β∣∥γ∥
∏e∈Eγmγ(e)!
∥γ∥
∏
i=1
∥Φ(γi)∥≤∑
γ≁γx
e∣γ∣+∥γ∥+1∣β∣∥γ∥
∏e∈Eγmγ(e)! ≤e ∑
γ≁γx
(2e)∣γ∣(e∣β∣
2 )
∥γ∥
.
For a vertex x, there are at most (eΔ)n
2
connected subgraphs with n edges that contain x (Ref. 31, Lemma 2.1). Furthermore, for such a subgraph,
there are precisely ( k−1
n−1) polymers (multisets) γ with ∥γ∥= k that correspond to it. Thus, we may write
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤e
2
∞
∑
n=1
(2e2Δ)n ∞
∑
k=n
( k −1
n −1)(e∣β∣
2 )
k
.
By interchanging the summations over n and k, we obtain
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤e
2
∞
∑
k=1
(e∣β∣
2 )
k k
∑
n=1
( k −1
n −1)(2e2Δ)n
= e
2
∞
∑
k=1
(e∣β∣
2 )
k
(2e2Δ)(2e2Δ + 1)k−1
≤e
2
∞
∑
k=1
∣β∣k(e3Δ + e
2)
k
.
By taking ∣β∣≤
1
e4Δ, we have
∑
γ≁γs
∣wγ∣e∣γ∣+∥γ∥+1 ≤e
2
∞
∑
k=1
(1
e + 1
e3 )
k
< 1.
Fix a polymer γ. By summing over all vertices in γ, of which there are at most ∣γ∣+ 1, we obtain
∑
γ∗≁γ
∣wγ∗∣e∣γ∗∣+∥γ∗∥+1 ≤∣γ∣+ 1.
Now, by applying the main theorem of Ref. 20 with a(γ) = ∣γ∣+ 1 and d(γ) = ∥γ∥, we obtain that the cluster expansion converges absolutely
in β, ZG(β) ≠0, and
∑
Γ∈GC
Γ∋γx
RRRRRRRRRRR
φ(Γ)∏
γ∈Γ
wγ
RRRRRRRRRRR
e∥Γ∥≤1.
We complete the proof by summing over all vertices in G,
∑
Γ∈GC
∥Γ∥≥m
RRRRRRRRRRR
φ(Γ)∏
γ∈Γ
wγ
RRRRRRRRRRR
≤∣V∣e−m.
■
Lemma 7 (restatement).
The weight wγ of a polymer γ can be computed in time exp(O(∥γ∥)).
Proof. For convenience, let n = ∥γ∥and fix an enumeration γ1, . . . , γn of the multiset of edges in γ. By an inclusion–exclusion argument
as in the derivation of Ryser’s formula for the permanent,32 we have
∑
σ∈Sn
n
∏
i=1
Φ(γσ(i)) = (−1)n ∑
A⊆[n]
(−1)∣A∣(∑
i∈A
Φ(γi))
n
.
Thus, we may write
wγ =
(−β)n
n!∏e∈Eγmγ(e)! Tr
⎡⎢⎢⎢⎣
∑
σ∈Sn
n
∏
i=1
Φ(γσ(i))
⎤⎥⎥⎥⎦
=
βn
n!∏e∈Eγmγ(e)! ∑
A⊆[n]
(−1)∣A∣Tr[(∑
i∈A
Φ(γi))
n
].
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-6
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
The first sum is over all subsets of [n], of which there are 2n. For each of these subsets A, we diagonalize the sum of the interactions ∑i∈AΦ(γi)
to obtain the eigenvalues. This can be achieved in time exp(O(n)); here, we are using our assumption that the single-spin Hilbert spaces Hx
are d-dimensional with d < ∞. The trace may then be evaluated in time exp(O(n)) by evaluating the sum of the nth powers of the eigenvalues.
Hence, the weight of a polymer can be computed in time exp(O(n)) = exp(O(∥γ∥)).
■
