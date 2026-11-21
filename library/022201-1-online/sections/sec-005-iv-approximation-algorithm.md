---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-005-iv-approximation-algorithm
section_title: "APPROXIMATION ALGORITHM"
section_number: IV
pages: 4-5
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
We now establish our approximation algorithm. First, we show that the truncated cluster expansion provides a good approximation to
log(ZG(β)). Netoˇcný and Redig3 provided a sufficient condition for the convergence of the quantum cluster expansion based on the formalism
of Kotecký and Preiss.20 In the following lemma, we follow their analysis in the setting of bounded-degree graphs. In particular, we obtain
convergence criteria based on the maximum degree alone.
Lemma 4. Fix Δ ∈Z+. Let G = (V, E) be a graph of maximum degree at most Δ, and let β be a complex number such that ∣β∣≤
1
e4Δ. The
cluster expansion for log(ZG(β)) converges absolutely, ZG(β) ≠0, and for m ∈Z+,
∣Tm(ZG(β)) −log(ZG(β))∣≤∣V∣e−m.
We prove Lemma 10 in Appendix B. This lemma implies that to obtain an multiplicative ϵ-approximation to ZG(β), it is sufficient
to compute Tm(ZG(β)) to order m = log(∣V(G)∣/ϵ). We shall proceed by establishing an algorithm for computing Tm(ZG(β)) in time
exp(O(m)) ⋅∣V(G)∣O(1). Helmuth, Perkins, and Regts4 showed that such an algorithm exists, given the following three lemmas:
Lemma 5. Fix Δ ∈Z+, and let G = (V, E) be a graph of maximum degree at most Δ. The clusters of size at most m can be listed in time
exp(O(m)) ⋅∣V∣O(1).
Proof. Our proof follows that of Ref. 4, Theorem 6. First, we enumerate all connected subgraphs in G of size at most m. This can be
achieved in time exp(O(m)) ⋅∣V∣O(1) by Ref. 18, Lemma 3.6. Then, for each subgraph H, we enumerate all polymers (multisets) of size at
most m whose corresponding subgraph in G is H. If H has size n, then there are precisely ( m−1
n−1 ) of these, and they can be enumerated in time
exp(O(m)). The enumeration of clusters in the claimed time then follows as in the proof of Ref. 4, Theorem 6.
■
Lemma 6. The Ursell function φ(H) can be computed in time exp(O(∣V(H)∣)).
Proof. This is a result of Ref. 24; see Ref. 4, Lemma 5.
■
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-3
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
Lemma 7. The weight wγ of a polymer γ can be computed in time exp(O(∥γ∥)).
We prove Lemma 11 in Appendix B.
Lemma 8. Fix Δ ∈Z+, and let G = (V, E) be a graph of maximum degree at most Δ. The truncated cluster expansion Tm(ZG(β)) can be
computed in time exp(O(m)) ⋅∣V(G)∣O(1).
Proof. We can list all clusters in G of size at most m in time exp(O(m)) ⋅∣V∣O(1) by Lemma 5. For each of these clusters, we can compute
the Ursell function in time exp(O(m)) by Lemma 6, and the polymer weights in time exp(O(m)) by Lemma 11. Hence, the truncated cluster
expansion for log(ZG(β)) can be computed in time exp(O(m)) ⋅∣V(G)∣O(1).
■
Combining Lemmas 10 and 8 gives a fully polynomial-time approximation scheme for the partition function ZG(β) when G has
maximum degree at most Δ and ∣β∣is at most
1
e4Δ. This proves Theorem 1.
