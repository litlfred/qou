---
doc_id: 022201-1-online
doc_title: "Online Export Citation RESEARCH ARTICLE | FEBRUARY 01 2021 Efficient algorithms for approximating quantum partition functions Ryan L. Mann ; Tyler Helmuth"
section_id: sec-006-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 5-8
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
doc_brief: "Online Export Citation RESEARCH ARTICLE | FEBRUARY 01 2021 Efficient algorithms for approximating quantum partition functions Ryan L. Mann ; Tyler Helmuth — 8 sections: Abstract; INTRODUCTION; THE AB"
---
We thank Michael Bremner, Adrian Chapman, Ashley Montanaro, and Will Perkins for helpful discussions. R.L.M. was supported by the
QuantERA ERA-NET Cofund in Quantum Technologies implemented within the European Union’s Horizon 2020 Programme (QuantAlgo
project) and EPSRC Grant Nos. EP/L021005/1 and EP/R043957/1. T.H. was supported by EPSRC Grant No. EP/P003656/1.
APPENDIX A: PROOF OF LEMMA 2
Lemma 2 (restatement). The partition function Z G(β) admits the following abstract polymer model representation:
ZG(β)= ∑
Γ∈G
∏
γ∈Γ
wγ,
where
wγ ∶= (−β)∥γ∥
∥γ∥!∏e∈Eγ mγ(e)! Tr
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
ZG(β)= Tr[e−βHG]
=
∞
∑
n=0
(−β)n
n! Tr
⎡⎢⎢⎢⎢⎣
⎛
⎝ ∑
e∈E(G)
Φ(e)⎞
⎠
n⎤⎥⎥⎥⎥⎦
=
∞
∑
n=0
(−β)n
n! ∑
e1,...,en∈E(G)
Tr[
n
∏
i=1
Φ(ei)].
We shall now rewrite the inner sum as a product over disjoint objects. Let S= (ei)n
i=1 denote any sequence of hyperedges, and let GS be the
graph with vertex set[n] and edges between any two vertices i and j if and only if ei∩ ej ≠ ∅. Define a sequential polymer to be a subsequence
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689 62, 022201-4
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics ARTICLE scitation.org/journal/jmp
of S that corresponds to a maximally connected component of GS. Say that two sequential polymers are compatible if and only if their
corresponding subgraphs in G are vertex disjoint. Let ΓS denote the set of all sequential polymers in S. It follows that
ZG(β)=
∞
∑
n=0
(−β)n
n! ∑
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
Let ∣γ∣ denote the length of a sequential polymer. Furthermore, let ΓG ∶=∪SΓS denote the set of all sequential polymers in G, and let GG denote
the collection of all admissible sets of sequential polymers in G. Observe that for any admissible set of sequential polymers {γi}k
i=1, there are
precisely
(∑k
i=1∣γi∣)!
∏k
i=1∣γi∣! sequences S that give rise to it. Thus, we may write
ZG(β)=
∞
∑
n=0
(−β)n
n!
n
∑
k=0
1
k! ∑
m1,...,mk≥1
m1+⋅⋅⋅+ mk=n
( n
m1, . . ., mk
) ∑
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
k! ∑
m1,...,mk≥1
m1+⋅⋅⋅+ mk=n
∑
γ1,...,γk∈ΓG
∣γ1∣=m1,...,∣γk∣=mk
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣! Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
.
By interchanging the summations over n and k, we obtain
ZG(β)=
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
m1+⋅⋅⋅+ mk=n
∑
γ1,...,γk∈ΓG
∣γ1∣=m1,...,∣γk∣=mk
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣! Tr
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
k! ∑
γ1,...,γk∈ΓG
admissible
k
∏
i=1
(−β)∣γi∣
∣γi∣! Tr
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
∣γ∣! Tr
⎡⎢⎢⎢⎢⎣
∏
e∈γ
Φ(e)
⎤⎥⎥⎥⎥⎦
.
Now, by transforming the sum over admissible sets of sequential polymers into a sum over admissible sets of polymers and summing the
weights of their permutations, we obtain
ZG(β)= ∑
Γ∈G
∏
γ∈Γ
(−β)∥γ∥
∥γ∥!∏e∈Eγ mγ(e)! Tr
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
we had to introduce a factor of 1
∏e∈Eγ mγ(e)! to avoid overcounting. This completes the proof. ■
APPENDIX B: PROOF OF LEMMA 4 AND LEMMA 7
Lemma 4. (restatement). Fix Δ∈ Z+. Let G = (V, E) be a graph of maximum degree at most Δ, and letβ be a complex number such that
∣β∣≤ 1
e4Δ . The cluster expansion for log(ZG(β)) converges absolutely, Z G(β)≠ 0, and for m ∈ Z+,
∣Tm(ZG(β))− log(ZG(β))∣≤ ∣V∣e−m.
Proof. For convenience, we normalize the trace so that Tr(I)= 1. Note that this is equivalent to a rescaling of the partition function by
a multiplicative factor. We introduce a polymerγx to every vertex x in G consisting of only that vertex. We defineγx to be incompatible with
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689 62, 022201-5
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics ARTICLE scitation.org/journal/jmp
every polymer that contains x. Then, we have
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤ ∑
γ≁γx
e∣γ∣+∥γ∥+1∣β∣∥γ∥
∏e∈Eγ mγ(e)!
∥γ∥
∏
i=1
∥Φ(γi)∥≤ ∑
γ≁γx
e∣γ∣+∥γ∥+1∣β∣∥γ∥
∏e∈Eγ mγ(e)! ≤ e ∑
γ≁γx
(2e)∣γ∣( e∣β∣
2 )
∥γ∥
.
For a vertexx, there are at most(eΔ)n
2 connected subgraphs withn edges that containx (Ref. 31, Lemma 2.1). Furthermore, for such a subgraph,
there are precisely ( k−1
n−1) polymers (multisets)γ with ∥γ∥= k that correspond to it. Thus, we may write
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤ e
2
∞
∑
n=1
(2e2Δ)n ∞
∑
k=n
( k− 1
n− 1)( e∣β∣
2 )
k
.
By interchanging the summations over n and k, we obtain
∑
γ≁γx
∣wγ∣e∣γ∣+∥γ∥+1 ≤ e
2
∞
∑
k=1
( e∣β∣
2 )
k k
∑
n=1
( k− 1
n− 1)(2e2Δ)n
= e
2
∞
∑
k=1
( e∣β∣
2 )
k
(2e2Δ)(2e2Δ+ 1)k−1
≤ e
2
∞
∑
k=1
∣β∣k(e3Δ+ e
2)
k
.
By taking ∣β∣≤ 1
e4Δ , we have
∑
γ≁γs
∣wγ∣e∣γ∣+∥γ∥+1 ≤ e
2
∞
∑
k=1
( 1
e + 1
e3)
k
< 1.
Fix a polymerγ. By summing over all vertices inγ, of which there are at most ∣γ∣+ 1, we obtain
∑
γ∗≁γ
∣wγ∗∣e∣γ∗∣+∥γ∗∥+1 ≤ ∣γ∣+ 1.
Now, by applying the main theorem of Ref. 20 with a(γ)= ∣γ∣+ 1 and d(γ)= ∥γ∥, we obtain that the cluster expansion converges absolutely
inβ, ZG(β)≠ 0, and
∑
Γ∈GC
Γ∋γx
⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪
φ(Γ)∏
γ∈Γ
wγ
⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪
e∥Γ∥ ≤ 1.
We complete the proof by summing over all vertices in G,
∑
Γ∈GC
∥Γ∥≥m
⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪
φ(Γ)∏
γ∈Γ
wγ
⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪⌟⟨rro⟪⟪⟩r⟪
≤ ∣V∣e−m.
■
Lemma 7 (restatement). The weight wγ of a polymer γ can be computed in time exp(O(∥γ∥)).
Proof. For convenience, let n= ∥γ∥ and fix an enumerationγ1, . . .,γn of the multiset of edges inγ. By an inclusion–exclusion argument
as in the derivation of Ryser’s formula for the permanent,32 we have
∑
σ∈Sn
n
∏
i=1
Φ(γσ(i))= (−1)n
∑
A⊆[n]
(−1)∣A∣(∑
i∈A
Φ(γi))
n
.
Thus, we may write
wγ = (−β)n
n!∏e∈Eγ mγ(e)! Tr
⎡⎢⎢⎢⎣
∑
σ∈Sn
n
∏
i=1
Φ(γσ(i))
⎤⎥⎥⎥⎦
= βn
n!∏e∈Eγ mγ(e)! ∑
A⊆[n]
(−1)∣A∣ Tr[(∑
i∈A
Φ(γi))
n
].
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689 62, 022201-6
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics ARTICLE scitation.org/journal/jmp
The first sum is over all subsets of[n], of which there are 2n. For each of these subsetsA, we diagonalize the sum of the interactions∑ i∈AΦ(γi)
to obtain the eigenvalues. This can be achieved in time exp(O(n)); here, we are using our assumption that the single-spin Hilbert spaces Hx
are d-dimensional with d<∞. The trace may then be evaluated in time exp(O(n)) by evaluating the sum of thenth powers of the eigenvalues.
Hence, the weight of a polymer can be computed in time exp(O(n))= exp(O(∥γ∥)). ■
DATA AVAILABILITY
No new data were created during this study.
